---
name: work-artifacts
type: principle
description: "Anchor work in a work item: artifacts on disk, not in context."
model-invocable: true
---

# Work Artifacts

Active artifacts live in the work directory: the shared state between you,
the user, and other agents. If understanding is not on disk, it does not
survive. Write findings, decisions, and design artifacts as you produce them.
Commit frequently: sessions crash and compact.

## Finding the Work Directory

Spawns get `$MERIDIAN_ACTIVE_WORK_DIR` automatically. Use `meridian work
current` if the env var is stale or unset (env vars don't update
mid-session).

The work item also carries `task_dir` — the checkout where source edits,
builds, and tests run, distinct from the work directory. Rebind with
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

## Status and Completion

The orchestrator owns work state: subagents should not mutate it unless
explicitly instructed (concurrent mutations create race conditions).

Status values are free-form: keep the current phase visible:

```bash
meridian work update auth-refactor --status designing
meridian work done auth-refactor    # archives work dir, detaches session
meridian work clear                 # detach without archiving
```

Only `work done` when you own the whole lifecycle, not just a slice.
Opening a PR is not finishing the work item: update status to `pr-open`
or `awaiting-merge` and leave it active until merge and cleanup.

## Artifact Placement

**work dir** (`meridian work current`): this work item's artifacts.
**kb** (`$MERIDIAN_CONTEXT_KB_DIR`): project-wide reference material.

Rule of thumb: *this* work item → work dir. Project-wide → kb.

Design decisions go in design docs. Implementation decisions go in commit
messages or inline comments. Structural decisions go in the work directory.
Record rejected alternatives: they prevent re-proposing what was already
considered.

**`DIVERGENCE/`**: when the design or plan shifts during execution, the
orchestrator logs the shift in this folder. Reviewers check alignment
against it; knowledge capture mines it after the phase settles.

**`AGENTS.md`**: the work directory follows `/qi-layer` like any tree
agents enter cold. Its AGENTS.md orients an arriving spawn: the goal, the
artifact layout, what's settled versus still moving. Keep it current as
the work shifts; add `.context/` only if depth accumulates.

See [`resources/lifecycle.md`](resources/lifecycle.md) for detailed lifecycle
management: dashboard commands, status transitions, completion rules,
archival.
