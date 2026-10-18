# meridian-base

Core coordination primitives for [Meridian](https://github.com/haowjy/meridian-cli).
Shared execution, exploration, and knowledge-maintenance agents, plus the
skills that teach them how to spawn work, track state, and coordinate across
sessions.

## What You Get

Shared workers and coordination skills for workflows like these:

```bash
# Break work into subtasks and delegate
meridian spawn -a subagent --prompt-file implement-model.md -f plan/phase-1.md --bg

# Run tasks in parallel
meridian spawn -a subagent --prompt-file phase-2a.md --bg
meridian spawn -a subagent --prompt-file phase-2b.md --bg
meridian spawn wait

# Track work items across sessions
meridian work start "auth-refactor"
meridian work show auth-refactor

# Search past context
meridian session search "auth design decision"

# Ask the human to come look
meridian notify "<title>" ["<body>"] [--attach <path>]... [--no-email] [--priority 1..5] [--json]
```

Meridian's system prompt and each command's `-h` teach the CLI. The skills
below teach agents how to coordinate with it.

## Agents

Each agent's `description` says when to spawn it, what to pass, and what comes back. What it does lives in its body and in this table.

| Agent | Model | Purpose |
|---|---|---|
| `subagent` | luna | General-purpose worker for a bounded task no specialist fits |
| `explorer` | luna | Read-only facts from a project's files and git history |
| `session-miner` | luna | Decisions, rejected alternatives, constraints, and intent from past conversations |
| `kb-lead` | opus | Writes durable knowledge to `.context/`, the KB, and `docs/` from the work and the human's decisions; deletes stale and misplaced docs; commits each repo it touches without pushing |
| `cold-reader` | luna | Reads text meant to outlive the work as a reader who wasn't there; reports where that reader stalls, edits nothing |
| `kb-maintainer` | luna | Restructures documentation trees and repairs cross-references; flags content questions instead of deciding them |

These are profile defaults. Ordered alternatives and effort settings live in
`agents/*.md`; the model aliases they name are below.

## Models

The model aliases in `mars.toml`, scored 1–10 as of October 2026. Each alias
resolves to the newest model in its family, or to the model it pins.
Intelligence and value come from the Artificial Analysis Intelligence Index
and its cost per task; taste is judged against Opus (9), the highest of any
model here. Agents pick models from these descriptions, which
`meridian mars models aliases` prints; this table is generated from them with
`uv run scripts/models_table.py`.

<!-- models-table:start -->
| Alias | Value | Intelligence | Taste | Description |
|---|---|---|---|---|
| `fable` | 2 | 10 | 8 | Escalation only, never a default or fallback: when a strong model has run out of depth on long-horizon planning, architecture, critique, or bug-finding, a second opinion on work that can be verified. Slow and the most expensive; Opus is the better general orchestrator. |
| `opus` | 5 | 9 | 9 | Orchestration and interactive primaries, conversation, frontend, prompt and prose writing, deep sustained work. Best judge of code quality and long-term direction: structure, taste, refactoring, thermo-nuclear review, and what should be deleted. Can over-delegate. |
| `terra` | 9 | 8 | 4 | Scoped, repeatable implementation, triage, and lower-risk review; clear and less prone to overthinking than Sol. Emits several times Sol's output per task and passes fewer long tasks. |
| `sol` | 8 | 8 | 5 | Difficult technical analysis, complex coding, computer use, long-horizon implementation. Slow to stream and output-heavy; a review benchmark on the previous version found many of its findings unactionable. Less sure-footed on ambiguous architecture. |
| `sonnet` | 7 | 8 | 5 | Daily implementation: bug fixes, multi-file coding, frontend polish, documents, bounded review. Opus is better for ambiguous architecture and open-ended judgment. |
| `muse` | 6 | 8 | 4 | Coding and agent or computer-use work; does well on simpler and UI tasks, loops on hard ones. Prompts and completions are not used for training. |
| `astra` | 5 | 8 | 6 | The hardest cross-system decisions, computer use and browser work, software engineering, important communication. Best judge of correctness: bugs, security, regressions. Slow; cyber-safety checks can pause legitimate security work. |
| `grok` | 3 | 8 | 5 | Long-horizon coding and knowledge work. Verbose and slow. |
| `glm` | 7 | 7 | 3 | Open-weight coder for backend, repository-scale implementation, and code review. Slow to start and verbose; makes confident assumptions and stops following steering late in long runs. No image input; weak at UI. |
| `kimi` | 4 | 7 | 5 | Long-running coding and research over large inputs; native multimodal, good at frontend and web apps. Slow and token-heavy; avoid bulk work. |
| `composer` | 10 | 6 | 3 | Coding for bounded edits, scaffolding, tests, and implementing a settled plan. Unreliable on long-horizon, ambiguous, or high-risk work; plan and review with a stronger model. |
| `luna` | 10 | 6 | 4 | General worker for implementation, exploration, summaries, and bounded execution; can own substantial coherent objectives given clear context and verification criteria. Can stall or report done early, so check its claims. Fine for quick, low-risk checks; not for ambiguous architecture or subtle cross-module debugging. |
| `deepseek` | 9 | 6 | 3 | Coding and agent work: concrete repo changes, tool loops, bulk drafting from focused briefs; takes image input. Review its ambiguous or high-stakes work. |
| `deepseekpro` | 9 | 6 | 3 | Legacy alias. Until DeepSeek ships a new Pro model, it routes Pro requests to Flash at Flash pricing, so this is `deepseek` under another name. |
| `haiku` | 9 | 6 | — | Summaries, compaction, classification, notes, cold reads, lightweight review, parallel subagents; not ambiguous architecture or complex autonomous implementation. |
| `muse-contributor` | — | — | — | Same model as `muse` on a free endpoint that may train on submitted prompts and completions; select it only when that is acceptable. Suits inexpensive visual probing. |
<!-- models-table:end -->

## Skills

**Coordination and work state**

| Skill | What it covers |
|---|---|
| `work-artifacts` | Work items and the work directory: findings, decisions, and artifacts that survive compaction and reach other agents |
| `shared-workspace` | Working safely in a checkout that holds other agents' changes |
| `handoff` | Moving to a different interactive lead: transition brief and launch command |
| `goal-writing` | Turning intent into an executable goal: outcome, evidence, constraints, stop conditions |
| `meridian-privilege-escalation` | Least-privilege fixes when a spawn hits sandbox or permission limits |
| `session-mining` | Recovering decisions and context from conversation history |
| `notify` | Telling the human about a decision, a costly uncertain call, a blocker, or a finished task |
| `zoom-out` | Orienting in an unfamiliar area with parallel explorers and one synthesized map |

**Thinking with the human**

| Skill | What it covers |
|---|---|
| `intent-modeling` | Separating what the human said from what they meant |
| `explore-and-engage` | Sharing your read while investigating instead of going silent |
| `shared-dao` | One name per concept, settled early, recorded in vocab files |
| `grill` | Stress-testing a plan branch by branch with the human |
| `grill-with-docs` | Grilling grounded in project docs and prior decisions |
| `grill-with-evidence` | Grilling grounded in project artifacts and primary sources |
| `reflect` | A user-invoked check that you delivered what they needed before you report |
| `correct` | A user-invoked fix for mistakes agents keep repeating: the strongest fix that holds, proven on a past mistake, from the KB corrections register |

**Writing and knowledge**

| Skill | What it covers |
|---|---|
| `llm-writing` | Writing for the reader and cutting default LLM phrasing |
| `information-hierarchy` | Answer first, depth behind it, the right form for each beat |
| `structured-artifact` | Structured HTML artifacts for explaining and presenting |
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

Meridian discovers these by layout convention — no manifest needed.

## See Also

- [meridian-cli](https://github.com/haowjy/meridian-cli) — the Meridian coordination engine
- [meridian-dev-workflow](https://github.com/meridian-flow/meridian-dev-workflow) — opinionated dev team built on top of this base
