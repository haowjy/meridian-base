# Work Item Lifecycle

## Dashboard and Discovery

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

## Completion Lifecycle

The stable lifecycle:
1. create work item
2. do the work
3. open the PR when applicable
4. wait for review + merge when applicable
5. mark the work item done when merge/cleanup is complete

Opening the PR is not the same as finishing the work item. At PR-open time,
leave the work item active and update status to something explicit like
`pr-open`, `awaiting-review`, or `awaiting-merge`. `meridian work done`
belongs after merge and cleanup, not at handoff to review.

```bash
meridian work done auth-refactor    # archives work directory, detaches from session
meridian work clear                 # detach without archiving (work stays active for others)
```

`work done` archives the work directory and detaches the session. A prose
status update does not complete the work item — only `work done` archives
it. Use `work clear` to detach from a work item you don't own.
