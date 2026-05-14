---
name: meridian-work-coordination
type: reference
description: Use whenever you need to create, switch, update, or complete a work item, or decide where work-scoped notes versus broader shared docs belong.
model-invocable: false
---

# Work Coordination

The orchestrator owns work state — subagents should not mutate it unless explicitly instructed, because concurrent mutations from multiple spawns create race conditions and inconsistent status.

## Starting Work

Before spawning, ensure your session is attached to the correct work item. Spawns inherit the attachment and get `$MERIDIAN_ACTIVE_WORK_DIR` set automatically.

```bash
meridian work start "descriptive name" --worktree   # create, attach, and create the feature worktree
meridian work switch descriptive-name    # attach to existing
```

For code implementation work, prefer `--worktree` at creation time so design,
planning, implementation, QA, and KB spawns all inherit the worktree-backed
context from the start.

After starting, use `meridian work current` to get the work directory path. Env vars set at launch don't update mid-session, so `$MERIDIAN_ACTIVE_WORK_DIR` may be stale or unset if you started work after launch.

```bash
meridian work current                              # -> /path/to/work/descriptive-name
ls "$(meridian work current)"/design/              # use inline in commands
cat "$(meridian work current)"/requirements.md     # read work artifacts
```

Work context is session-scoped. A new session has no active work until you explicitly start or switch. Check `meridian work` to see what's in flight before creating a duplicate.

## Dashboard

```bash
meridian work                    # dashboard — what's in flight
meridian work list               # list active work items
meridian work list --done        # list done/archived items
meridian work show auth-refactor # drill into one work item
```

## Status Management

Status values are free-form. Keep the current phase visible:

```bash
meridian work update auth-refactor --status designing
meridian work update auth-refactor --status implementing
meridian work reopen auth-refactor         # restore archived work
meridian work delete stale-item            # remove empty work items
meridian work delete old-item --force      # remove even if it has artifacts
```

## Completion and Cleanup

Only mark work done when you own the whole work item lifecycle, not just a task inside it. If your context only covers one phase, file set, review lane, or implementation slice, report your slice as complete and leave the work item active.

The stable lifecycle is:
1. create work item + worktree
2. do the work in that worktree
3. open the PR
4. wait for human review + merge
5. prune merged worktrees with `scripts/prune-worktrees.sh`
6. mark the work item done when merge/cleanup is complete

Opening the PR is not the same as finishing the work item. At PR-open time,
leave the work item active and update status to something explicit like
`pr-open`, `awaiting-review`, or `awaiting-merge`. `meridian work done`
belongs after merge and cleanup, not at handoff to review.

```bash
meridian work done auth-refactor    # archives work directory, detaches from session
meridian work clear                 # detach without archiving (work stays active for others)
```

`work done` archives the work directory and detaches the session. A prose status update does not complete the work item — only `work done` archives it. Use `work clear` to detach from a work item you don't own.

For worktree-based stable flow, post-merge cleanup belongs to
`scripts/prune-worktrees.sh`. That script removes merged worktrees/branches
and can best-effort call `meridian work done` for the associated work item.

## Artifact Placement

**active work** — the directory returned by `meridian work current`. Write work-scoped artifacts here. Spawns get this as `$MERIDIAN_ACTIVE_WORK_DIR` automatically.

**kb** (`$MERIDIAN_CONTEXT_KB_DIR`) — long-lived reference material. Persists across work items.

Rule of thumb: *this* work item → work dir. Project-wide → kb.

## Commit Work Artifacts

Sessions can crash or compact. Work artifacts are the only thing that survives — commit them frequently, not just at the end.
