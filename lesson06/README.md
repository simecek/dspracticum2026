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

* **Base model → assistant:** further training on example conversations, with the same next-token loss as our Shakespeare GPT.
* **Models need tokens to think:** each token gets a fixed amount of computation, so hard problems need many tokens.
* **Reinforcement learning:** no labels. The model tries many solutions and the ones with the right answer are reinforced. This is how DeepSeek-R1 learned to reason.

## What has changed since the video (Feb 2025)

* **Thinking is a setting, not a separate model.** You choose how much a model thinks: `reasoning_effort` in the OpenAI API ([Lesson 05, notebook 2](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/02_openai_api.ipynb)), from `"none"` to `"high"` and beyond. More effort is usually better on hard problems, but slower and more expensive.
* **Hidden reasoning is still billed.** You see only how many tokens it took (`usage.completion_tokens_details.reasoning_tokens`). With reasoning on, `temperature` and `logprobs` are not available.
* **Open thinking models** (e.g. gpt-oss, Qwen3) on the Hugging Face Hub show their reasoning as text, often between `<think>` and `</think>`.
* **Models think with tools:** they search the web or run code while thinking.

**Next week** we continue with **tools and agents**: how a model calls tools, and how an agent works by itself in a loop of thinking, calling tools and looking at the results.
