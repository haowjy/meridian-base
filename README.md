# meridian-base

Core coordination primitives for [Meridian](https://github.com/haowjy/meridian-cli).
Shared execution, exploration, and knowledge-maintenance agents, plus
runtime-independent skills for planning, documenting, reviewing, and preserving
work.

## What You Get

Shared workers and generic coordination guidance for workflows such as:

- breaking work into bounded tasks and delegating them in parallel,
- keeping findings and decisions in a work directory, and
- reading past sessions for missing context.

Each runtime supplies the operations behind those capabilities. The agents and
skills below teach the judgment that carries across runtimes.

## Agents

Each agent's `description` says when to spawn it, what to pass, and what comes back. What it does lives in its body and in this table.

| Agent | Model | Purpose |
|---|---|---|
| `subagent` | luna | General-purpose worker for a bounded task no specialist fits |
| `explorer` | luna | Read-only facts from a project's files and git history |
| `session-miner` | luna | Where past conversations discuss a question, for the caller to read |
| `kb-lead` | opus | Writes durable knowledge to `.context/`, the KB, and `docs/` from the work; deletes stale and misplaced docs; commits each repo it touches without pushing |
| `cold-reader` | luna | Reads text meant to outlive the work as a reader who wasn't there; reports where that reader stalls, edits nothing |
| `kb-maintainer` | luna | Restructures documentation trees and repairs cross-references; flags content questions instead of deciding them |

These are profile defaults. Ordered alternatives and effort settings live in
`agents/*.md`; the model aliases they name are below.

## Models

The model aliases in `mars.toml`. Each alias resolves to the newest model in
its family, or to the model it pins. Agents pick models from these
descriptions, which `meridian mars models aliases` prints; this table is
generated from them with `uv run scripts/models_table.py`.

<!-- models-table:start -->
| Alias | Description |
|---|---|
| `argon` | Creative writing and editing long manuscripts; send the text inline, since its tool calling is unreliable. |
| `argon-contributor` | `argon` on a free endpoint that may train on your prompts; never for manuscripts the author hasn't cleared. |
| `astra` | The hardest cross-system decisions, and finding bugs, security issues and regressions. Slow. |
| `composer` | Cheap coder for bounded edits, tests and implementing a settled plan. |
| `deepseek` | Cheap coder for concrete repo changes, tool loops and bulk drafting. |
| `deepseekpro` | Legacy alias for `deepseek`. |
| `fable` | Escalation only: a second opinion when a strong model runs out of depth. Slowest and priciest. |
| `glm` | Open-weight coder for backend, repo-scale work and 3D builds; mid-pack on frontend UI, behind Opus and Fable on design taste. |
| `grok` | Long-horizon coding and knowledge work. Slow. |
| `haiku` | Summaries, classification, notes and light parallel subagents. |
| `hydrogen` | Fast, cheap worker for agentic coding, UI builds and tool loops. |
| `kimi` | Long coding and research over large inputs; good at frontend. Slow. |
| `luna` | Cheap general worker for implementation, exploration and summaries; check its claims. |
| `muse` | Coding and computer use on simpler and UI tasks. |
| `muse-contributor` | `muse` on a free endpoint that may train on your prompts; use only when that's acceptable. |
| `opus` | Orchestration, conversation, writing, and judging code quality and direction. |
| `sol` | Hard technical analysis, complex coding and long implementation. Slow. |
| `sonnet` | Daily implementation, frontend polish, documents and bounded review. |
| `terra` | Fast computer use and clear technical writing. |
<!-- models-table:end -->

## Skills

**Coordination and work state**

| Skill | What it covers |
|---|---|
| `work-artifacts` | The work directory as current state that survives compaction and reaches other agents |
| `shared-workspace` | Working safely in a checkout that holds other agents' changes |
| `handoff` | Starting a new interactive lead on a piece of work, or moving your own work to a fresh session: its opening brief and pre-phase checks |
| `zoom-out` | Orienting in an unfamiliar area with parallel explorers and one synthesized map |

**Thinking with the human**

| Skill | What it covers |
|---|---|
| `intent-modeling` | Separating what the human said from what they meant |
| `explore-and-engage` | Sharing your read while investigating instead of going silent |
| `shared-dao` | One name per concept, settled early, recorded in vocab files |
| `correct` | A user-invoked fix for a mistake agents keep making: finds what led the agent there and fixes the project's docs or code; a cause in an installed prompt becomes a note for its owner. Adapted from [pstack](https://github.com/backnotprop/pstack)'s `/correct` (MIT) |

**Writing and knowledge**

| Skill | What it covers |
|---|---|
| `llm-writing` | Writing for the reader and cutting default LLM phrasing |
| `structured-artifact` | Structured HTML artifacts for explaining and presenting |
| `atlas` | Maps you click down through: Markdown pages with one diagram each, a viewer and a check |
| `knowledge-layers` | Where knowledge lives: AGENTS.md, `.context/`, KB, `docs/`, work directories |
| `qi-layer` | Keeping AGENTS.md and `.context/` minimal and load-bearing |
| `qi-maintenance` | Keeping colocated docs true after source changes |
| `md-validation` | Checking markdown links and Mermaid diagrams |

## Install Into a Project

```bash
meridian mars init
meridian mars add @meridian-flow/meridian-base
meridian mars sync
```

If `mars.toml` already exists, you can skip `meridian mars init`.

## Layout

```
agents/*.md              # Agent profiles (YAML frontmatter + markdown)
skills/*/SKILL.md        # Skills (with optional resources/ subdirectory)
```

Mars discovers these by layout; `mars.toml` does not list them.

## See Also

- [meridian-cli](https://github.com/haowjy/meridian-cli) — the Meridian coordination engine
- [meridian-dev-workflow](https://github.com/meridian-flow/meridian-dev-workflow) — opinionated dev team built on top of this base
