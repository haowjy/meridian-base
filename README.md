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
```

These capabilities come from the skills below — they're injected into the
agent's system prompt so it knows how to use meridian's CLI.

## Agents

| Agent | Model | Purpose |
|---|---|---|
| `subagent` | luna | General-purpose execution worker for scoped tasks. |
| `explorer` | luna | Read-only codebase facts and git-history exploration. |
| `session-miner` | luna | Decisions, rejected alternatives, constraints, and intent from conversations. |
| `kb-maintainer` | luna | Documentation structure and cross-reference maintenance; flags content questions. |
| `kb-lead` | sol | Reconciles evidence and human decisions, then writes durable knowledge. |

These are profile defaults. Ordered alternatives and effort settings live in
`agents/*.md`. Model aliases live in `mars.toml`; Composer is retained there for
compatibility while its fallback references are retired.

## Skills

| Skill | What it teaches the agent |
|---|---|
| `meridian-work-coordination` | Work item lifecycle — creating, switching, updating status, placing artifacts |

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
