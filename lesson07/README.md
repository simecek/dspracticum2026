**Date**: Nov 13, 2026 · **Slides**: [Google Slides](https://docs.google.com/presentation/d/1RveRHi3D4EE5p00RaV2e1phX35yDEw4g/edit?usp=sharing)

**Tools and agents**

* Tool calling by hand with Qwen3.5-0.8B: tool calls, the agent loop, pydantic: [01_tool_calling.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson07/01_tool_calling.ipynb)
* A coding agent in the terminal: [opencode](https://opencode.ai)

## opencode

Install (macOS, Linux; on Windows use WSL or see the [docs](https://opencode.ai/docs)), then run `opencode` in a project folder and pick a *free* model with `/models`. Free models may train on your prompts, so don't send anything private.

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

**Exercises** (in a new folder: `mkdir csfd-analysis && cd csfd-analysis && git init && opencode`):

1. **Plan, then build.** In the `plan` agent (Shift+Tab), plan a project that loads the ČSFD reviews from Lesson 05 (`fewshot-goes-multilingual/cs_csfd-movie-reviews`) and plots star ratings and review lengths. Fix the plan, then let `build` write it.
2. **AGENTS.md.** Let the agent write `AGENTS.md`, add your own rules, and check a new session follows them.
3. **A feature with a test.** A function for the 10 most reviewed movies, with a `pytest` test. Then make shell commands ask first: `{"permissions": [{"action": "shell", "resource": "*", "effect": "ask"}]}` in `opencode.json`.
4. **Push to GitHub.** Run `gh auth login` yourself (never give the agent a token). Let the agent add a README and `.gitignore`, commit, and push to a new repo with `gh`. Read the diff first: `/undo` cannot undo a push.
5. **Bonus:** turn the notebook's agent into `agent.py`, add an MCP server, or run opencode on your Assignment 02 repo.

**More:** [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (Anthropic) · [Function calling](https://developers.openai.com/api/docs/guides/function-calling) (OpenAI) · [Tool use](https://huggingface.co/docs/transformers/chat_extras) (🤗 transformers) · [opencode docs](https://opencode.ai/docs)
