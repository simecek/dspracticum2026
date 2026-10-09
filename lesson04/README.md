**Date**: Oct 9, 2026

**Slides**: https://claude.ai/artifact/DJg4SZeKfTgAAYMs757w8s (outline in [slides04.md](slides04.md))

* Assignment 02 check-in: Gradio and Hugging Face Spaces (see [Lesson 03](../lesson03/))
* Inside GPT-2: tokenization, the transformer block and training a mini GPT, all in one notebook: [gpt2_inside.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson04/gpt2_inside.ipynb)
  * text → bytes → Byte Pair Encoding, and GPT-2's tokenizer rebuilt in ~20 lines
  * embeddings, then one transformer block rebuilt by hand, giving the same numbers as the real GPT-2
  * attention heads, next-token probabilities, generation and temperature
  * the same `Block` class trained from scratch on tiny Shakespeare (needs a GPU runtime)

**Additional materials:**

* [Transformer Explainer](https://poloclub.github.io/transformer-explainer/): GPT-2 running in your browser
* [LLM Visualization](https://bbycroft.net/llm): a 3D walk through a small GPT
* Jay Alammar: [The Illustrated GPT-2](https://jalammar.github.io/illustrated-gpt2/)
* Andrej Karpathy: [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE), [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEb1nY), [Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)
* [Tiktokenizer](https://tiktokenizer.vercel.app): how different models cut text into tokens
* Sebastian Raschka: [From GPT-2 to gpt-oss](https://sebastianraschka.com/blog/2025/from-gpt-2-to-gpt-oss.html)
* [GPT-2 paper (Language Models are Unsupervised Multitask Learners)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

**No new assignment.** [Assignment 02](../lesson03/) is due Oct 15, 18:00.
