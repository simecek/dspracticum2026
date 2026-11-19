**Date**: Nov 20, 2026

**Working with a coding agent**

We work with [opencode](https://opencode.ai) and its free models, but almost everything carries over to Codex and Claude Code:

* choosing a model: [Terminal-Bench](https://tbench.ai), [Artificial Analysis](https://artificialanalysis.ai) and [OpenRouter](https://openrouter.ai/rankings)
* the working folder, approvals and safety, prompt injection
* sandboxing (Docker for opencode, `--sandbox` in Codex)
* `AGENTS.md`, MCP servers (Hugging Face, Context7), skills and commands

## Skills worth trying

A skill is a folder with a `SKILL.md` file. To use one in opencode, copy it to `.opencode/skills/<name>/SKILL.md` in your project, or to `~/.config/opencode/skills/<name>/SKILL.md` for all projects. opencode also reads `.claude/skills` and `.agents/skills`, so the same folders work in Claude Code.

* [Karpathy guidelines](https://github.com/multica-ai/andrej-karpathy-skills): four rules against the coding mistakes Andrej Karpathy complained about: think before coding, simplicity first, surgical changes, goal-driven execution. It comes as a `CLAUDE.md` (in opencode, put the text into `AGENTS.md`) and as a skill in `skills/karpathy-guidelines/`.
* [Socratic tutor](https://github.com/janestreet/agent_skills/blob/master/socratic-tutor/SKILL.md) (Jane Street): the agent teaches you a topic by asking questions instead of lecturing. It finds your level first, then quizzes you up to a final test. Start it with "teach me…" or "quiz me…".
* [Ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md): "lazy senior developer" mode. The agent looks for the smallest change that fully solves the task: no extra features, abstractions or new dependencies. It has three levels (`lite`, `full`, `ultra`).
* [Humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md): rewrites text that sounds AI-generated, without changing what it says. It lists the typical patterns, such as "not X but Y" contrasts, forced groups of three, inflated claims and dashes everywhere.
* [STE80 humanizer](https://github.com/Dodaios/ste80-humanizer/blob/main/SKILL.md): the same idea in two passes. First it removes the AI tells, then it rewrites the text "80% of the way" to Simplified Technical English (ASD-STE100, the language of aircraft maintenance manuals): short sentences, one idea each, active voice. Karpathy suggested this method.

Read a skill before you install it. It is a set of instructions for your agent, so treat it like code you run.
