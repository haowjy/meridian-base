---
name: work-artifacts
type: principle
description: "Load when work must survive compaction or crashes or be shared with other agents: findings, decisions, and artifacts go in the work directory, not in context."
model-invocable: true
---

# Work Artifacts

Active artifacts live in the work directory: the shared state between you,
the user, and other agents. If understanding is not on disk, it does not
survive. Write findings, decisions, and design artifacts as you produce them.
Commit frequently where the work directory is version-controlled: sessions
crash and compact.

## Finding the Work Directory

Spawns get `$MERIDIAN_ACTIVE_WORK_DIR` automatically. Use `meridian work
current` if the env var is stale or unset (env vars don't update
mid-session).

The work item also carries `task_dir` — the checkout where the work's
files are edited and checked, distinct from the work directory. Rebind with
`meridian work task-dir <path>`.

## Starting Work

Not every spawn needs a work item: small direct tasks can run without one.
When a task needs work-scoped artifacts or lifecycle tracking:

```bash
meridian work start "descriptive name"   # create and attach
meridian work switch descriptive-name    # attach to existing
meridian work                            # dashboard: what's in flight
```

Spawns inherit the attachment automatically.

## Human Attention

Any agent, including a spawn, may call `meridian notify "<one line>"` only
when the human needs to come look: you are blocked on a decision only they can
make, a long piece of work is ready for them, or a failure stops the work. Put
what they need to decide or see in the message, not a status. Notify each thing
once; routine progress and spawn returns are not reasons. Use `--no-email` when
it can wait until they next look at their phone. Meridian already adds the tmux
session, project, and work item to the message.

Also notify when you made a call you are unsure of and kept going, and it
gets costly to reverse once more work builds on it. Record it with the work
item's decisions first, then send one notice at the next natural pause
(a phase lands, a spawn returns) covering the open calls: what you chose,
the main alternative, and where to look. The human can overturn it before
it hardens. Use `--no-email`. Calls you are confident in, or that are cheap
to undo, need no notice.

## Status and Completion

The agent that started the work item owns its state: spawned agents must not
mutate it unless explicitly instructed (concurrent mutations create race conditions).

Status values are free-form: keep the current phase visible:

```bash
meridian work update auth-refactor --status designing
meridian work done auth-refactor    # archives work dir, detaches session
meridian work clear                 # detach without archiving
```

Only `work done` when you own the whole lifecycle, not just a slice.
Handing work off for review is not finishing the work item: set a status
like `awaiting-review` or `pr-open` and leave it active until the work is
accepted and cleaned up.

## Artifact Placement

**work dir** (`meridian work current`): this work item's artifacts.
**kb** (`$MERIDIAN_CONTEXT_KB_DIR`): project-wide reference material.

Rule of thumb: *this* work item → work dir. Project-wide → kb.

Keep raw files (traces, HARs, profiles, browser data, dumps, build output)
out of the work directory. Where it syncs through git, every file
lands in history that each clone carries, and one over the remote's size
limit blocks the sync. Record the excerpt or summary that carries the
finding; keep the raw file in scratch space only while you need it.

Design decisions go in design docs. Decisions scoped to one change go with
it: its commit message, or a note beside what it explains. Structural decisions go in the work directory.
Record rejected alternatives: they prevent re-proposing what was already
considered.

**`DIVERGENCE/`**: when the design or plan shifts during execution, the
lead logs the shift in this folder. Reviewers check alignment
against it; knowledge capture mines it once the change settles.

**`AGENTS.md`**: the work directory follows `/qi-layer` like any tree
agents enter cold. Its AGENTS.md orients an arriving spawn: the goal, the
artifact layout, what's settled versus still moving. Keep it current as
the work shifts; add `.context/` only if depth accumulates.

See [`resources/lifecycle.md`](resources/lifecycle.md) for detailed lifecycle
management: dashboard commands, status transitions, completion rules,
archival.
