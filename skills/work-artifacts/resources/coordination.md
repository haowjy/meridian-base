# Work Coordination

The orchestrator owns work state — subagents should not mutate it unless
explicitly instructed (concurrent mutations create race conditions).

## Starting Work

Not every spawn needs a work item — small direct tasks can run without one.
When a task needs work-scoped artifacts or lifecycle tracking:

```bash
meridian work start "descriptive name"   # create and attach
meridian work switch descriptive-name    # attach to existing
meridian work                            # dashboard — what's in flight
```

Spawns inherit the attachment and get `$MERIDIAN_ACTIVE_WORK_DIR`
automatically. Use `meridian work current` to get the path (env vars don't
update mid-session).

## Status and Completion

Status values are free-form — keep the current phase visible:

```bash
meridian work update auth-refactor --status designing
meridian work done auth-refactor    # archives work dir, detaches session
meridian work clear                 # detach without archiving
```

Only `work done` when you own the whole lifecycle, not just a slice.
Opening a PR is not finishing the work item — update status to `pr-open`
or `awaiting-merge` and leave it active until merge and cleanup.

## Artifact Placement

**work dir** (`meridian work current`) — this work item's artifacts.
**kb** (`$MERIDIAN_CONTEXT_KB_DIR`) — project-wide reference material.

Rule of thumb: *this* work item → work dir. Project-wide → kb.

Commit work artifacts frequently — sessions crash and compact.
