---
name: meridian-work-coordination
type: reference
description: Use whenever you need to create, switch, update, or complete a work item, or decide where work-scoped notes versus broader shared docs belong.
model-invocable: false
---

# Work Coordination

The orchestrator owns work state — subagents should not mutate it unless explicitly instructed, because concurrent mutations from multiple spawns create race conditions and inconsistent status.

## Starting Work

Run `work start` before spawning anything. It attaches the work item to your session — spawns inherit the attachment and get `$MERIDIAN_ACTIVE_WORK_DIR` set automatically.

```bash
meridian work start "descriptive name"   # create and attach
meridian work switch descriptive-name    # attach to existing
```

After starting, use `meridian work current` to get the work directory path. Env vars set at launch don't update mid-session, so `$MERIDIAN_ACTIVE_WORK_DIR` may be stale or unset if you started work after launch.

```bash
meridian work current                              # -> /path/to/work/descriptive-name
ls "$(meridian work current)"/design/              # use inline in commands
cat "$(meridian work current)"/requirements.md     # read work artifacts
```

Work context is session-scoped. A new session has no active work until you explicitly start or switch. Check `meridian work` to see what's in flight before creating a duplicate.

## Worktrees

Work items can create a git worktree automatically:

```bash
meridian work start "auth refactor" --worktree   # create work item + feature worktree
meridian work start "quick fix" --no-worktree     # skip even if configured as default
```

With `--worktree`, meridian creates a branch and worktree, then launches spawns
inside it. All implementation happens in the worktree, not on main. Ship by
pushing the branch and creating a PR back to main.

Worktree cleanup happens automatically on `meridian work done`.

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

```bash
meridian work done auth-refactor    # archives work directory, detaches from session
meridian work clear                 # detach without archiving (work stays active for others)
```

`work done` archives the work directory and detaches the session. A prose status update does not complete the work item — only `work done` archives it. Use `work clear` to detach from a work item you don't own.

## Artifact Placement

**active work** — the directory returned by `meridian work current`. Write work-scoped artifacts here. Spawns get this as `$MERIDIAN_ACTIVE_WORK_DIR` automatically.

**kb** (`$MERIDIAN_CONTEXT_KB_DIR`) — long-lived reference material. Persists across work items.

Rule of thumb: *this* work item → work dir. Project-wide → kb.

## Commit Work Artifacts

Sessions can crash or compact. Work artifacts are the only thing that survives — commit them frequently, not just at the end.
