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
meridian notify "<msg>" [--title T] [--no-email] [--priority 1..5] [--json]
```

Meridian's system prompt and each command's `-h` teach the CLI. The skills
below teach agents how to coordinate with it.

## Agents

Each agent's `description` says when to spawn it, what to pass, and what comes back. What it does lives in its body and in this table.

| Agent | Model | Purpose |
|---|---|---|
| `subagent` | luna | General-purpose worker for a bounded task no specialist fits |
| `explorer` | luna | Read-only codebase facts and git history |
| `session-miner` | luna | Decisions, rejected alternatives, constraints, and intent from past conversations |
| `kb-lead` | opus | Writes durable knowledge to `.context/`, the KB, and `docs/` from the work and the human's decisions; deletes stale and misplaced docs; commits each repo it touches without pushing |
| `kb-maintainer` | luna | Restructures documentation trees and repairs cross-references; flags content questions instead of deciding them |

These are profile defaults. Ordered alternatives and effort settings live in
`agents/*.md`. Model aliases live in `mars.toml`; Composer is retained there for
compatibility while its fallback references are retired.

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
