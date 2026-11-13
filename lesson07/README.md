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

**Things to try:**

1. Make an empty folder, start `opencode` and ask it to write a script that loads the ČSFD reviews from Lesson 05 and plots the distribution of ratings. Watch which tools it calls.
2. Switch to the `plan` agent first: it explores and suggests a plan, but does not edit files. Then let the `build` agent do it.
3. Write an `AGENTS.md` file: how to run the code, which libraries to use, in which language to comment. Does the agent follow it?
4. Permissions: by default the agent may run commands by itself. Make it ask first (`opencode.jsonc`):

```jsonc
{
  "permissions": [
    { "action": "shell", "resource": "*", "effect": "ask" }
  ]
}
```

**Additional materials:**

* Anthropic: [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), workflows vs. agents
* [Function calling](https://developers.openai.com/api/docs/guides/function-calling) in the OpenAI API, and [Tool use](https://huggingface.co/docs/transformers/chat_extras) in 🤗 transformers
* [opencode documentation](https://opencode.ai/docs): tools, agents, permissions, `AGENTS.md`, MCP servers
