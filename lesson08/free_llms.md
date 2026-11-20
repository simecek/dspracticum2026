# When you hit the free limit

The free OpenCode Zen models have a usage limit. When you hit it, connect another provider. opencode has both of these built in: run `/connect` in opencode (or `opencode auth login <provider>` in the terminal), paste your key, and pick a model with `/models`.

| | OpenRouter | Munito |
|---|---|---|
| What | one key for 300+ models from many providers | open models (DeepSeek, GLM, Qwen) run in the EU |
| Sign-up | [openrouter.ai](https://openrouter.ai) → Keys | [console.munito.ai](https://console.munito.ai/registration) |
| Free use | `:free` models, 50 requests/day (1,000/day after a one-time $10 top-up) | free tier with a verified phone number, daily limits per model (not published), only when capacity is available |
| Key variable | `OPENROUTER_API_KEY` | `MUNITO_API_KEY` |
| opencode login | `opencode auth login openrouter` | `opencode auth login munito` |

The agent sends one request per step, so 50 requests a day is only a few tasks.

## OpenRouter

1. Create an account and a key (`sk-or-…`) at [openrouter.ai](https://openrouter.ai).
2. In opencode: `/connect` → OpenRouter → paste the key.
3. `/models` → pick a model:
   * `openrouter/openrouter/free`: picks a free model for you. This is the easiest free option.
   * a `:free` model, e.g. `openrouter/google/gemma-4-31b-it:free`
   * a cheap paid model, e.g. `openrouter/deepseek/deepseek-v4-flash` (needs credit)

**"Free" often means you pay with your data.** Many `:free` models only work if you allow the provider to train on your prompts (*Free model training* in [privacy settings](https://openrouter.ai/settings/privacy)). If a model fails with *"0 endpoints … data policy"* or *"No allowed providers"*, that setting is the reason. Decide for yourself whether to turn it on, and never send private data to free models.

## Munito

1. Sign up at [console.munito.ai](https://console.munito.ai/registration), verify your phone number and create a key (`munitoai_…`).
2. In opencode: `/connect` → Munito → paste the key.
3. `/models` → e.g. `munito/deepseek-ai/deepseek-v4-flash`. The `munito-eu/…` models run on the EU-only endpoint.

Munito keeps no data and doesn't train on it. Paid use (from about $0.10 per 1M tokens) is meant for business users.
