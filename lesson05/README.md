**Date**: Oct 16, 2026

* Hugging Face, part 1: our Shakespeare GPT from [Lesson 04](../lesson04/) in 🤗 `transformers`, and on the Hub: [01_gpt2_on_the_hub.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/01_gpt2_on_the_hub.ipynb)
  * `GPT2Config` + `GPT2LMHeadModel`: the same network (818,048 parameters) as our own class from last week
  * `labels=x`, `generate()`, the context window
  * `save_pretrained`, logging in with an access token (Colab Secrets), `push_to_hub`, a model card, `from_pretrained`
* Hugging Face, part 2: `datasets` and `tokenizers`: [02_datasets_and_tokenizers.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/02_datasets_and_tokenizers.ipynb)
  * Czech movie reviews from ČSFD: `load_dataset`, `filter`, `map`, streaming the Czech Wikipedia, your own dataset on the Hub
  * a BPE tokenizer trained in a fraction of a second, and a tokenizer for Czech
  * the Shakespeare GPT with a real tokenizer, so that it works with `pipeline()`
* BERT and ModernBERT: [03_bert_and_modernbert.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/03_bert_and_modernbert.ipynb)
  * GPT vs BERT: decoder vs encoder, masked language modelling, one word with many vectors
  * ModernBERT (RoPE, local and global attention, 8k context) and mmBERT, which speaks Czech
  * optional: fine-tuning mmBERT to tell positive Czech movie reviews from negative ones, with `Trainer`
* LLMs through an API: [04_openai_api.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson05/04_openai_api.ipynb)
  * request, tokens and price, reasoning, system prompt, logprobs and temperature
  * structured output: an LLM rates ČSFD reviews without any training

**Additional materials:**

* [Hugging Face LLM course](https://huggingface.co/learn/llm-course), chapters 4–6 (sharing models, datasets, tokenizers)
* [BERT paper (Pre-training of Deep Bidirectional Transformers for Language Understanding)](https://arxiv.org/abs/1810.04805), Jay Alammar: [The Illustrated BERT](https://jalammar.github.io/illustrated-bert/)
* [Finally, a replacement for BERT](https://huggingface.co/blog/modernbert): the ModernBERT blog post ([paper](https://arxiv.org/abs/2412.13663)), and [mmBERT](https://huggingface.co/blog/mmbert)
* [OpenAI API documentation](https://developers.openai.com/api/docs)
