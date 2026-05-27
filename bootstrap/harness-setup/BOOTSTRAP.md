# Harness Setup

Meridian coordinates agents but does not run them directly. It needs at
least one **harness** — an agent runtime that talks to models, executes
tools, and manages sessions.

## What is a harness

A harness is the program that actually runs an agent. It handles:

- Calling the model API (Claude, GPT, Gemini, etc.)
- Executing tool calls (file edits, shell commands, etc.)
- Managing the conversation/session state
- Enforcing safety (approval prompts, sandbox)

Meridian's job is coordination — choosing which harness to use, routing
work to the right agent, passing context. The harness does the execution.

## Available harnesses

| Harness | Runtime | Models | Install |
|---|---|---|---|
| **Claude Code** | Node.js CLI | Claude (Sonnet, Opus, Haiku) | `npm install -g @anthropic-ai/claude-code` |
| **Codex** | Node.js CLI | GPT, o-series | `npm install -g @openai/codex` |
| **OpenCode** | Go binary | Multi-provider (Anthropic, OpenAI, Gemini, local, ChatGPT) | `go install github.com/opencode-ai/opencode@latest` |
| **Pi** | (coming soon) | Multi-provider | TBD |

You need at least one. Most setups use two or three — different harnesses
have different strengths and model access.

## How harness routing works

When you spawn an agent, meridian picks a harness based on the **model**:

```bash
meridian spawn -a coder -m sonnet "do the thing"
#                        ^^^^^^^^
#                        model alias → resolves to claude-sonnet-4-5
#                                    → belongs to claude harness
```

The routing logic:

1. Resolve the model alias (e.g. `sonnet` → `claude-sonnet-4-5`)
2. Use alias metadata, provider hints, project settings, or a launch-time
   harness probe to choose the harness
3. Launch the agent through that harness

This means **the model choice implicitly selects the harness**. You don't
usually need to specify `--harness` explicitly.

### Model → harness mapping

```
sonnet, opus, haiku           → claude harness
codex, gpt55, gptmini, o3    → codex harness
opencode-go/*, kimi-*         → opencode harness
```

Run `meridian mars models list` to see the configured model catalog: aliases,
descriptions, and static routing hints. This command stays fast and does not
probe every installed harness.

Run `meridian mars models list --live` when you need runtime availability: which
installed harnesses can actually launch the models on this machine.

## Overriding harness selection

### Force a harness for a specific spawn

```bash
meridian spawn -a coder --harness codex -m gpt55 "do it"
```

### Set default harness for the project

In `meridian.toml`:

```toml
[defaults]
harness = "codex"    # default when model doesn't determine harness
```

### Set default model per harness

```toml
[harness]
claude = ""                      # empty = harness picks its default
codex = ""                       # empty = harness picks its default
opencode = "opencode-go/kimi-k2.6"   # specific default for opencode
```

### Override model for specific agents

```toml
[agents.tech-lead]
model = "gpt55"

[agents.reviewer]
model = "opus"
```

### Override via model-policies (advanced)

Route specific model patterns to different behavior:

```toml
[[agents.tech-lead.model-policies]]
match = { model-glob = "gpt*" }
override = { effort = "medium", autocompact = 200000 }
```

## Precedence

When multiple sources specify a model or harness:

```
CLI flags (--model, --harness)
  > agent profile YAML
    > [agents.*] overrides in meridian.toml
      > [defaults] in meridian.toml
        > harness default
```

The model determines the harness. If you override the model with `-m`,
the harness follows the model — a profile-level harness won't override
a CLI-level model choice.

## Authentication

Each harness manages its own auth:

**Claude Code:**
```bash
claude auth login
# or set ANTHROPIC_API_KEY
```

**Codex:**
```bash
codex auth login
# or set OPENAI_API_KEY
```

**OpenCode:**
Configure in `~/.config/opencode/config.toml` or set provider-specific
env vars (ANTHROPIC_API_KEY, OPENAI_API_KEY, GEMINI_API_KEY, etc.)

### Using a ChatGPT subscription with OpenCode

If the user has a ChatGPT Plus/Pro/Team subscription (not an API key),
OpenCode can use it via the `chatgpt` provider. This routes through the
ChatGPT backend instead of the OpenAI API — different quota, different
rate limits, uses the subscription instead of pay-per-token billing.

In OpenCode's config (`~/.config/opencode/config.toml`):

```toml
[providers.chatgpt]
type = "chatgpt"
```

Then use models prefixed with `chatgpt/` in meridian:

```bash
meridian spawn -a coder -m "opencode-go/chatgpt/gpt-4o" "do it"
```

This is useful when the user has a ChatGPT subscription but no separate
OpenAI API credits. Ask the user which billing arrangement they have.

## Verify installation

```bash
which claude     # Claude Code
which codex      # Codex
which opencode   # OpenCode
```

Meridian auto-detects installed harnesses. If a harness binary is not on
`$PATH`, meridian won't find it.

## Which to install

Ask the user which providers and subscriptions they have:

- **Anthropic API key** → install Claude Code
- **OpenAI API key** → install Codex
- **ChatGPT subscription (Plus/Pro/Team)** → install OpenCode with chatgpt provider
- **Multiple providers or local models** → install OpenCode
- **Claude Max subscription** → install Claude Code (uses subscription quota)
- **Not sure** → install Claude Code (most common for dev workflows)

Multiple harnesses can coexist. Meridian routes to the right one based on
the model you request. Install all that you have access to — more options
means better model selection for each task.

At minimum, one working harness is required before meridian can do anything.
