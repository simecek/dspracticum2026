# Lesson 04 slides: Tokenization & the Transformer block (GPT-2)

**Date**: Oct 9, 2026

This file lists what the slides should contain. The visual design comes later. Each slide links to a section of the companion Colab, [`gpt2_inside.ipynb`](gpt2_inside.ipynb). The slides explain the ideas and the Colab lets students check them on the real GPT-2.

**Running example used everywhere:** the prompt `"The capital of France is"` → next token `" Paris"`. We follow it from text to tokens, to vectors, through 12 blocks, back to probabilities. *(To verify in Colab: does GPT-2 small rank `" Paris"` first? If not, use `"The Eiffel Tower is in the city of"`.)*

**Rough timing:** ~100 min of core content, plus 10–15 min of training if time permits (110 min is fine).
Part 0: 10 · Part 1: 10 · Part 2: 25 · Part 3: 10 · Part 4: 30 · Part 5: 10 · *Part 6 (training, optional): 10–15* · Part 7: 5

**Two "we rebuilt it ourselves" moments:** our own tokenizer gives exactly the same tokens as GPT-2's (2.4), and our own block gives exactly the same output as GPT-2's (4.9). Then the same block, with random weights, gets trained from scratch (Part 6).

---

## Part 0: Assignment 02 check-in: Gradio & HF Spaces (10 min)

The Lesson 03 README promises to explain Gradio and Spaces on Oct 9. Drop this part if it moves elsewhere.

### 0.1 Gradio in one slide
- Gradio turns a Python function into a web page: `gr.Interface(fn=predict, inputs=gr.Image(), outputs=gr.Label())`.
- *Visual:* the ~10 lines of `lesson03/gradio_app/app.py` next to a screenshot of the running app.

### 0.2 HF Space = a git repo that runs your app
- Three files: `app.py`, `requirements.txt`, `README.md` (its header sets SDK and Python version), plus `model.pkl`.
- Pitfall: a model exported on Colab (Python 3.13) does not load on Python 3.10, so set `python_version: '3.13'` in the README.
- The CPU runtime is free and good enough for inference.
- Deadline: Oct 15, 18:00.

---

## Part 1: The big picture (10 min)

### 1.1 An LLM is a next-token predictor
- Text → tokens → vectors → 12 × transformer block → probabilities for the next token → pick one → append → repeat.
- Recap of the 3Blue1Brown talk from last week: everything today is "zooming into one box of this diagram".
- *Visual:* the full pipeline as one horizontal diagram, used as a "you are here" map in later parts.

### 1.2 Meet GPT-2
- OpenAI, Feb 2019. Paper: *Language Models are Unsupervised Multitask Learners*. Release was staged because the model was "too dangerous".
- Trained on WebText: ~40 GB of text from 8M web pages.
- Four sizes: 124M / 355M / 774M / 1.5B parameters. We use the smallest: it runs on Colab even without a GPU.
- GPT-2 small in numbers: vocabulary **50,257**, context **1,024** tokens, vector size **768**, **12** layers, **12** heads, **124,439,808** parameters.
- *Colab:* §4 (load the model, `print(model)`, count parameters).

### 1.3 Why GPT-2 and not BERT?
- BERT = *encoder*: sees the whole sentence, fills in blanks, good for classification.
- GPT = *decoder*: sees only the past, predicts what comes next, can generate text.
- ChatGPT, Claude, Llama, Gemma, Qwen are all decoder-only descendants of GPT-2. The block has changed surprisingly little since 2019 (see 7.1).
- *Visual:* two small diagrams, one with a `[MASK]` in the middle of a sentence and one with `?` at the end.

---

## Part 2: Tokenization (25 min)

### 2.1 How to cut text into pieces?
- Characters: tiny vocabulary, but very long sequences (expensive attention, short memory).
- Words: short sequences, but a huge vocabulary, and unknown words (typos, new names, Czech word forms like *nejneobhospodařovávatelnějšími*) break it.
- **Subwords**: the sweet spot. Frequent words get one token, rare words are built from pieces.
- *Visual:* the same sentence cut three ways, with the token count under each.

### 2.2 Text is just bytes
- Every character has a Unicode number (`ord("ř") = 345`).
- UTF-8 stores it as 1–4 bytes: `a` = 1 byte, `ř` = 2 bytes, `👋` = 4 bytes.
- There are only 256 possible bytes, so they make a vocabulary where **no text is ever "unknown"**.
- *Colab:* §1.

### 2.3 Byte Pair Encoding (BPE) in four steps
- Count all neighbouring pairs, merge the most frequent pair into a new token, repeat.
- Toy example: `aaabdaaabac` → `ZabdZabac` (Z = aa) → `ZYdZYac` (Y = ab) → `XdXac` (X = ZY).
- Vocabulary = 256 bytes + one new token per merge. GPT-2: 256 + 50,000 merges + 1 special `<|endoftext|>` = **50,257**.
- *Visual:* the toy example as 4 rows, with the merged pair highlighted in each row.
- *Colab:* §2 (`get_stats` + `merge`, train ~20 merges on a short text and watch `" the"` appear).

### 2.4 Rebuilding GPT-2's tokenizer
- Step 1: a regex splits the text into words, numbers and punctuation, so a merge never crosses a word boundary: `"Hello've world123!!!?"` → `Hello` · `'ve` · ` world` · `123` · `!!!?`.
- Step 2: inside each piece, apply GPT-2's 50,000 merges in the order they were learned.
- Our ~15-line encoder plus GPT-2's merge table gives `our_encode(text) == tiktoken_encode(text)` → `True`, for English, Czech, Korean, emoji and code alike.
- *Visual:* one Czech word going through the merges, one row per merge.
- *Colab:* §3a.

### 2.5 Live demo: Tiktokenizer
- https://tiktokenizer.vercel.app, switch between `gpt2` and `o200k_base`.
- Things to point at:
  - The space belongs to the *next* token: `" egg"` is one token, `"Egg"` is `E` + `gg`, `" EGG"` is `" E"` + `GG`.
  - Numbers split arbitrarily: `127 + 677 = 804` → `127`, `" 6"`, `77`, `" 8"`, `04`.
  - GPT-2 spends one token per space when indenting code. Newer tokenizers merge spaces.

### 2.6 The Czech "token tax"
| | English: *The capital of France is Paris.* | Czech: *Hlavní město Francie je Paříž.* |
|---|---|---|
| GPT-2 (50k vocab) | 7 tokens | 19 tokens |
| GPT-4 `cl100k_base` (100k) | 7 | 15 |
| GPT-4o `o200k_base` (200k) | 7 | 12 |
- GPT-2 does not even have a token for `ě` or `ř`. Each one is split into 2 raw bytes.
- More tokens means higher API cost, a context window that fills up faster, and a harder task for the model.
- *Colab:* §3b (students count tokens in their own sentences).

### 2.7 Tokenization explains many LLM quirks
- "How many r's in strawberry?" The model sees `" strawberry"` as **one** token and never sees the letters.
- Reversing strings, spelling and arithmetic are hard for the same reason.
- Glitch tokens (`SolidGoldMagikarp`): tokens that were in the tokenizer's training data but almost never in the model's.
- *Visual:* `" strawberry"` drawn as one opaque box with the letters hidden inside.

### 2.8 The tokenizer is a separate model
- It is trained separately (BPE on its own text corpus) and then frozen.
- The LLM never sees text, only integer IDs.
- Special tokens mark structure: `<|endoftext|>` in GPT-2, and chat markers like `<|im_start|>` in chat models.
- Vocabulary sizes keep growing: BERT ~30k · GPT-2 50k · Llama 3 128k · GPT-4o 200k · Gemma 3 ~262k.
- *Visual:* `text ⇄ tokenizer ⇄ [15496, 995] ⇄ LLM`.

---

## Part 3: From tokens to vectors (10 min)

### 3.1 The embedding is a lookup table
- `wte` is a 50,257 × 768 matrix, and row *i* is the vector of token *i*.
- It holds 38.6M parameters, **31 %** of all of GPT-2 small, before any "thinking" happens.
- The vectors are learned during training, exactly like the weights of a CNN.
- *Colab:* §5 (`model.transformer.wte.weight.shape`, look up the vector of `" Paris"`).

### 3.2 Directions carry meaning
- Similar tokens end up close to each other. Recap of the 3Blue1Brown "king − man + woman ≈ queen" idea.
- Demo: nearest neighbours of `" dog"` and `" Paris"` by cosine similarity. *(Pick the actual examples after running Colab. GPT-2 input embeddings are noisy for analogies, so neighbours are the safer demo.)*
- *Colab:* §5.

### 3.3 Position embeddings
- Attention itself does not know word order ("dog bites man" = "man bites dog").
- GPT-2 adds a learned position vector: `x = wte[token] + wpe[position]`, where `wpe` is 1,024 × 768.
- This is also why the context is limited: there is no row 1,025. Modern models use RoPE instead.
- *Visual:* the 5 tokens of the running example as 5 columns of 768 numbers, token vector + position vector.

---

## Part 4: The transformer block (30 min)

### 4.1 The residual stream
- One vector per token flows upward through 12 blocks.
- Each block *reads* from the stream and *adds* its result back: `x = x + attn(ln_1(x))`, then `x = x + mlp(ln_2(x))`.
- Every block has the same shape (768 in, 768 out), so we can stack as many as we like.
- *Visual:* 5 vertical lanes (tokens) going up, with 12 blocks as horizontal bands. Each band has an "attn" step that mixes lanes and an "MLP" step that stays inside each lane.

### 4.2 Two jobs: communicate, then compute
- **Attention**: tokens exchange information ("what is around me?").
- **MLP**: each token processes on its own ("what do I make of it?").
- Split of the block's 7.1M parameters: attention ≈ 1/3 (2.4M), MLP ≈ 2/3 (4.7M).

### 4.3 Attention: the intuition
- 3Blue1Brown example: in "a fluffy blue creature", the adjectives update the vector of "creature".
- Every token produces three vectors:
  - **Query**: "what am I looking for?"
  - **Key**: "what do I offer?"
  - **Value**: "what I hand over if you pick me".
- Score = how well my query matches your key. High score → I take a lot of your value.
- *Visual:* the running example, with arrows from `" is"` to earlier tokens and the arrow width showing the weight.

### 4.4 Attention: the math in one picture
- `weights = softmax( Q·Kᵀ / √64 + mask )`, then `output = weights · V`.
- Shapes for one head: X (5×768) → Q, K, V (5×64 each) → weights (5×5) → output (5×64).
- Why `√64`: without it the scores are too large, and softmax always picks a single token.
- *Visual:* the matrix product drawn as rectangles with shapes written on the sides. The 5×5 weight matrix shown as a heatmap.
- *Colab:* §6.2 (one head written by hand).

### 4.5 The causal mask: no peeking
- A token may look only at itself and earlier tokens, so the weight matrix is lower-triangular.
- This makes training cheap: one sequence of *T* tokens gives *T* next-token examples at once.
- In BERT (an encoder) the mask is removed and everyone sees everyone.
- *Visual:* the 5×5 heatmap with the upper triangle greyed out.

### 4.6 Multi-head attention
- 12 heads × 64 dimensions = 768. Each head can look for a different relation. The outputs are concatenated, then mixed by one more linear layer.
- Real GPT-2 heads (screenshots from Colab §7):
  - a "previous token" head;
  - a head that dumps most of its attention on the first token (an "attention sink");
  - *(optional)* an induction head in layers 5–7: on a repeated sequence, it looks at what followed the last occurrence.
- *(Head numbers to be filled in after running Colab.)*
- *Colab:* §6.3 (12 heads by hand) and §7 (heatmaps).

### 4.7 MLP: where facts might live
- 768 → 3,072 (GELU) → 768, applied to each token separately.
- It holds two thirds of the block's parameters. The 3Blue1Brown picture: "Michael Jordan" + MLP → a "basketball" direction gets added.
- *Visual:* one token vector expanding into a wide layer and shrinking back.

### 4.8 LayerNorm: keep the numbers sane
- Before each attention and MLP: rescale every token vector to mean 0 and standard deviation 1, then apply a learned scale and shift.
- GPT-2 puts it *before* each sub-block ("pre-LN") and adds one final `ln_f` at the end.
- This keeps training of deep stacks stable. One slide is enough.

### 4.9 Highlight: we rebuilt a GPT-2 block ourselves
- A `Block` class in about 30 lines of PyTorch. We copy the real model's weights into it, and `torch.allclose(our_block(x), gpt2_block(x))` → `True`.
- Part 6 reuses the same class with random weights.
- Parameter count of one block: 7,087,872. Times 12 blocks, plus embeddings, gives 124,439,808 (this matches `model.num_parameters()`).
- *Colab:* §6.5–6.7 (block by hand → `Block` class → the whole GPT-2, `our_gpt2(ids)` == the real logits).

---

## Part 5: Back to text (10 min)

### 5.1 Unembedding: from vector to probabilities
- Take the last token's vector, apply `ln_f`, multiply by `wteᵀ` (the same matrix as the input embedding: "weight tying") → 50,257 scores (logits) → softmax.
- *Visual:* a bar chart of the top-10 next tokens for the running example.
- *Colab:* §8.

### 5.2 Generating text = a loop
- Predict → pick a token → append it to the input → repeat.
- **Temperature**: divide the logits by T. T → 0 always picks the top token (boring, repetitive). T = 1 samples the model's own distribution. T = 2 gives nonsense.
- Top-k / top-p: sample only from the most likely tokens.
- *Visual:* the same prompt continued at T = 0, 0.7, 1.5.
- *Colab:* §8 (a hand-written generation loop with a temperature knob).

### 5.3 Bonus: logit lens
- Apply the unembedding after *every* layer to see in which layer `" Paris"` starts to win.
- *Visual:* a layers × top-token table or heatmap.
- *Colab:* §9 (optional). Drop it if time is short.

---

## Part 6: Training a mini GPT from scratch (10–15 min, if time permits)

Tip: start the training cell at the beginning of Part 5 (it takes a few minutes on a T4) and come back to it here.

### 6.1 Same blocks, random weights
| | GPT-2 small | our mini GPT |
|---|---|---|
| blocks | 12 | 4 |
| vector size | 768 | 128 |
| heads | 12 | 4 |
| context | 1,024 tokens | 128 characters |
| vocabulary | 50,257 BPE tokens | ~65 characters |
| parameters | 124M | ~0.8M |
| training data | 40 GB | ~1 MB |
- Why characters and not GPT-2's tokens: a 50,257-row embedding would have 6.4M parameters, 8× more than the rest of our tiny model.
- *(Final config and training time to be filled in after running Colab.)*

### 6.2 Training data = the text shifted by one
- Input `First Citize` → target `irst Citizen`. Each of the T positions is one training example. This is why the causal mask matters (4.5).
- A batch = B random windows of T characters, i.e. a tensor of shape B×T.
- *Visual:* the input and target strings aligned, with arrows from each prefix to its next character.

### 6.3 The training loop is the Lesson 02 loop
- forward → loss → backward → step → zero_grad. Only the data and the model are bigger.
- Loss = cross-entropy of the true next token, averaged over every position.
- A random model starts at ln(vocabulary size), a uniform guess: ln(65) ≈ **4.2** for our characters and ln(50,257) ≈ **10.8** for GPT-2.
- *Visual:* the loss curve from Colab (train and validation).

### 6.4 Watch it learn
- Samples after 0, a few hundred and a few thousand steps: random characters → words and line breaks → dialogue that looks like Shakespeare, with invented words.
- Same architecture as GPT-2, but ~150× fewer parameters and ~40,000× less data. That gap is what the rest of the semester is about.
- *Visual:* three text boxes side by side, copied from Colab.
- *Colab:* §10 ("Try it": train on your own text).

---

## Part 7: Wrap-up (5 min)

### 7.1 From GPT-2 to today's LLMs
- **What changed:** size (124M → hundreds of billions), data (40 GB → tens of trillions of tokens), RoPE instead of `wpe`, RMSNorm instead of LayerNorm, SwiGLU instead of GELU, grouped-query attention, mixture of experts, long context, and post-training (SFT + RLHF) that turns a text predictor into an assistant.
- **What did not change:** tokens → embeddings → [attention + MLP + residual] × N → unembedding.
- Link: Sebastian Raschka, [From GPT-2 to gpt-oss](https://sebastianraschka.com/blog/2025/from-gpt-2-to-gpt-oss.html).

### 7.2 The whole picture with shapes
- `"The capital of France is"` → 5 IDs → 5×768 → 12 blocks → 5×768 → 5×50,257 → last row → `" Paris"`.
- *Visual:* the diagram from 1.1 again, now with every shape filled in.

### 7.3 Further reading
- Interactive GPT-2 in the browser: [Transformer Explainer](https://poloclub.github.io/transformer-explainer/), [LLM Visualization (bbycroft)](https://bbycroft.net/llm)
- Jay Alammar: [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
- Andrej Karpathy: [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE), [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY), [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)
- 3Blue1Brown: Deep Learning chapters 5–7 (GPT, attention, how LLMs store facts)

### 7.4 No new assignment
- Assignment 02 (dataset + fine-tuned model + Gradio app) is still running. Due Oct 15, 18:00.

---

## Companion Colab: planned sections

| § | Content | Slides |
|---|---|---|
| 0 | Setup (`transformers`, `tiktoken`; CPU is enough) | |
| 1 | Text → Unicode → UTF-8 bytes | 2.2 |
| 2 | BPE by hand: `get_stats`, `merge`, train ~20 merges | 2.3 |
| 3a | Rebuild GPT-2's tokenizer: regex split + the merges from `tiktoken`, check `our_encode == enc.encode` | 2.4 |
| 3b | The real GPT-2 tokenizer: quirks, English vs Czech, "Try it" with your own sentence | 2.5–2.7 |
| 4 | Load GPT-2, `print(model)`, count parameters per part | 1.2 |
| 5 | Embeddings: `wte`, `wpe`, nearest neighbours | 3.1–3.3 |
| 6.1 | LayerNorm by hand | 4.8 |
| 6.2 | One attention head by hand on the running example, causal mask | 4.4–4.5 |
| 6.3 | 12 heads + output projection | 4.6 |
| 6.4 | MLP | 4.7 |
| 6.5 | Full block with residuals, compared with HF via `allclose` | 4.1, 4.9 |
| 6.6–6.7 | Reusable `Block` and `GPT` classes, GPT-2 weights copied in, logits match HF | 4.9 |
| 7 | Attention heatmaps; automatic search for previous-token, first-token and induction heads | 4.6 |
| 8 | Unembedding, top-10 next tokens, generation loop, temperature | 5.1–5.2 |
| 9 | *(bonus)* Logit lens | 5.3 |
| 10 | *(if time)* Train a mini GPT from scratch: character-level data, stack 4 `Block`s, training loop, loss curve, samples before and after | 6.1–6.4 |

Notes for writing the Colab:
- §3a: `tiktoken`'s `enc._mergeable_ranks` maps byte strings to token IDs, which equal the merge order. Encoding = repeatedly merge the adjacent pair with the lowest rank. Checked on Oct 8: about 15 lines reproduce `enc.encode` exactly on English, Czech, Korean, emoji and code.
- §6.6: `Block` is an `nn.Module` with ordinary `nn.Linear` layers, so §10 reuses it unchanged. Hugging Face GPT-2 uses `Conv1D`, whose weights are stored transposed compared to `nn.Linear`, so they are copied with `.T`. Also, `c_attn` packs Q, K and V into one 768 × 2,304 matrix.
- §10 needs a GPU runtime. Everything before it runs on CPU.

## To check after the first Colab run (real GPT-2 weights)

The notebook was tested end to end with random GPT-2 weights (every cell runs, and our block and model match Hugging Face). These depend on the real weights and still need to be filled in:
- 1.1 / 5.1: does GPT-2 small rank `" Paris"` first for the running example?
- 3.2: which nearest-neighbour examples look best.
- 4.6: block/head numbers of the previous-token, attention-sink and induction heads.
- 5.3: in which block `" Paris"` starts to win (logit lens).
- 6.1 / 6.4: the training time on a T4, the final loss, and text samples (training uses tiny Shakespeare).
