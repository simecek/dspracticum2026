**Date**: Nov 6, 2026 (online, via Google Meet)

**How large language models are trained, and how "thinking" models learned to think**

Today we watch parts of Andrej Karpathy's [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) (Feb 2025). We skip the first hour (tokenization, the neural network inside, training GPT-2), because we did all of that ourselves in [Lesson 04](../lesson04/).

| | segment | chapters | length |
|---|---|---|---|
| core | [0:59:23–1:20:32](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=3563s) | pretraining to post-training, post-training data (conversations) | 21 min |
| core | [1:46:56–2:07:28](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=6416s) | models need tokens to think, spelling, jagged intelligence | 20 min |
| core | [2:07:28–2:48:26](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=7648s) | supervised finetuning to reinforcement learning, reinforcement learning, DeepSeek-R1, AlphaGo | 41 min |
| optional, if time | [2:48:26–3:09:39](https://www.youtube.com/watch?v=7xTGNNLPyMI&t=10106s) | reinforcement learning from human feedback (RLHF) | 21 min |

**Things to watch for:**

* **From a base model to an assistant.** The base model after pretraining only continues documents, like GPT-2 in [Lesson 05](../lesson05/). An assistant comes from more training on example conversations (*supervised finetuning*). This uses the same next-token loss as our Shakespeare GPT.
* **Models need tokens to think.** Every token gets the same, fixed amount of computation: one pass through all the blocks, 12 in GPT-2. A hard problem therefore has to be spread over many tokens: the model "thinks out loud".
* **Reinforcement learning.** So far we always trained on labels: the correct next token, the correct class. In reinforcement learning the model tries many solutions, we check which ones reach the right answer, and we reinforce those. Nobody writes the reasoning for it. Long reasoning that checks and corrects itself emerged this way in DeepSeek-R1.

## What has changed since the video (Feb 2025)

* **Thinking is now a setting, not a separate model.** In early 2025 you chose between "thinking" models (OpenAI o1/o3, DeepSeek-R1) and normal ones (GPT-4o). Today most models can do both, and you choose how much they think. In the OpenAI API this is the `reasoning_effort` parameter from [Lesson 05, notebook 2](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/02_openai_api.ipynb). For `gpt-5.6-luna` it goes from `"none"` over `"low"`, `"medium"` (the default) and `"high"` up to `"xhigh"` and `"max"`. More effort usually means better answers to hard questions, but also slower and more expensive ones.
* **You pay for thinking you do not see.** The reasoning tokens are hidden, but they are billed as output tokens. You only see how many there were: `response.usage.completion_tokens_details.reasoning_tokens`. DeepSeek-R1 in the video shows its whole reasoning; OpenAI's models show at most a summary.
* **Some settings no longer work.** With reasoning switched on, the OpenAI API does not accept `temperature` or `logprobs`. Sampling and next-token probabilities, which we played with in Lessons 04 and 05, are only available with `reasoning_effort="none"`.
* **Open thinking models.** Thinking models with public weights are now common on the Hugging Face Hub, e.g. OpenAI's gpt-oss and Qwen3. Their reasoning is visible as text, often between `<think>` and `</think>`. Small models often learn to reason by training on the reasoning of bigger models (*distillation*).
* **Thinking with tools.** Today's models do not only think: while thinking, they search the web, run code and call other tools, and then continue thinking with the results.

**Try it:** In [Lesson 05, notebook 2](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/02_openai_api.ipynb), section 2, ask the bat-and-ball question with `reasoning_effort` set to `"none"`, `"low"` and `"high"`. Compare the answers, the number of hidden reasoning tokens and the price.

**Additional materials:**

* Andrej Karpathy: [How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw) (Feb 2025), the practical companion to today's video
* [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948): reinforcement learning that taught a model to reason
* [InstructGPT paper](https://arxiv.org/abs/2203.02155): supervised finetuning and RLHF, the recipe behind the first ChatGPT
* [AlphaGo, move 37](https://www.youtube.com/watch?v=HT-UZkiOLv8): what reinforcement learning can discover

**Next week** we continue with **tools and agents**: how a model calls tools, and how an agent works by itself in a loop of thinking, calling tools and looking at the results.
