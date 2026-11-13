**Date**: Nov 13, 2026

**Tools and agents**

* Tool calling by hand with a tiny open model (Qwen3.5-0.8B, free on the Colab GPU): a tool is just text in the prompt, parsing a tool call, sending the result back, the agent loop, and pydantic for typed tool arguments: [01_tool_calling.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson07/01_tool_calling.ipynb)
* A coding agent: [opencode](https://opencode.ai)

## opencode

opencode is an open-source coding agent that runs in your terminal. Inside, it is the loop from the notebook, with tools for reading and editing files and running commands.

**Install** (macOS, Linux; on Windows use WSL or the zip from the [docs](https://opencode.ai/docs)):

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

**Model:** run `opencode` in a project folder, then `/models`. The models marked *free* need no payment (for a limited time). Some of them may use your prompts for training, so don't send them anything private. With an OpenAI API key (Lesson 05), use `/connect`.

**Exercises** (start in a new folder: `mkdir csfd-analysis && cd csfd-analysis && git init && opencode`):

1. **Plan, then build.** Switch to the `plan` agent (Shift+Tab) and ask it to plan a small project that loads the ČSFD reviews from Lesson 05 (`fewshot-goes-multilingual/cs_csfd-movie-reviews`) and plots the distribution of star ratings and review lengths. Correct the plan, then let the `build` agent write it. Watch which tools it calls.
2. **AGENTS.md.** Ask the agent to write `AGENTS.md` (how to install, run, which libraries, code style), add your own rules, start a new session and check that it follows them.
3. **A feature with a test.** Ask for a function that returns the 10 most reviewed movies, with a `pytest` test, and let it run and fix the tests. Then make shell commands ask first (`opencode.jsonc`):

```jsonc
{
  "permissions": [
    { "action": "shell", "resource": "*", "effect": "ask" }
  ]
}
```

4. **Push to GitHub.** Log in yourself first with `gh auth login` (never give the agent a password or token). Then ask the agent to add a README and a `.gitignore`, commit, and push to a new public repository `csfd-analysis` with `gh`. Read the diff before the commit and approve the push yourself: `/undo` reverts files, not a push. Share the link on Slack (optional).
5. **Bonus:** turn the notebook's agent into `agent.py` with a pydantic tool, add an MCP server, or run opencode on your Assignment 02 repository.

**Additional materials:**

* Anthropic: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), workflows vs. agents
* [Function calling](https://developers.openai.com/api/docs/guides/function-calling) in the OpenAI API, and [Tool use](https://huggingface.co/docs/transformers/chat_extras) in 🤗 transformers
* [opencode documentation](https://opencode.ai/docs): tools, agents, permissions, `AGENTS.md`, MCP servers
