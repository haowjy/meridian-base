# meridian-base

Non-opinionated core agents and skills for Meridian. Teaches the harness how to use meridian — spawning, orchestrating, work coordination, install management, and troubleshooting.

This is what Meridian bootstraps by default.

## Layout

- `agents/*.md` — installable agent profiles
- `skills/*/SKILL.md` — installable skills (with optional `resources/`)

Meridian discovers this repo by layout convention. No source manifest is required inside the repo itself.

## Contents

### Agents (2)

| Agent | Model | Purpose |
|---|---|---|
| `__meridian-orchestrator` | (default) | Multi-step orchestrator with work coordination |
| `__meridian-subagent` | gpt-5.3-codex | Default execution agent for scoped tasks |

### Skills (6)

| Skill | Purpose |
|---|---|
| `__meridian-orchestrate` | Supervisor methodology — planning, delegation, review cycles, model selection |
| `__meridian-spawn-agent` | CLI reference for `meridian spawn`, work items, parallel execution |
| `__meridian-session-context` | Session context mining — reading transcripts, searching decisions, discovering sessions per work item |
| `__meridian-work-coordination` | Work item lifecycle, artifact placement, status management |
| `__meridian-install` | Managed install system — syncing agents/skills from external sources |
| `__meridian-troubleshoot` | Diagnostics, common failure patterns, state recovery |

## Bootstrap

Meridian auto-installs `__meridian-orchestrator` and `__meridian-subagent` (plus their skill dependencies) when they're missing locally. This repo is the well-known bootstrap source — if no other provenance is found, Meridian adds it to `agents.toml` automatically.

## Install

```bash
meridian sources add @haowjy/meridian-base
meridian sources install
```

## See Also

- [meridian-channel](https://github.com/haowjy/meridian-channel) — the Meridian coordination engine
- [meridian-dev-workflow](https://github.com/haowjy/meridian-dev-workflow) — opinionated SDLC methodology built on top of this base
