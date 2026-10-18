# Notify Examples

## Title and Body

The title is what a lock screen shows: lead with what the human has to do
or see. A few lines of options or a summary go in the body. Files already
on disk go as attachments: email carries them all, a phone push one per
message.

- `meridian notify "Pick auth storage: sessions table or JWT" "Tradeoffs in decisions.md"`
- `meridian notify "PR #412 ready for review" "Retry backoff; all checks green"`
- `meridian notify "Blocked: staging DB refuses connections" "Since 14:10; nothing else to do until it's back"`
- `meridian notify "Review the new settings page" --attach screenshot.png --attach report.md`

Weak titles make them open the session to find out whether it matters:
"Update", "Done with phase 2", "Spawn p31 finished", "FYI". Meridian ends
the body with a headline naming the tmux session, the agent, and the work
item (or the project when there is none), so the message needn't name them.

## Push Only

A notice goes to push and email. Add `--no-email` when it can wait until
they next check their phone: an uncertain call, a finished task they
weren't waiting on.

## Uncertain Calls

When you kept going past a call you were unsure of, tell the human before
more work builds on it and reversing it gets expensive. Record the call
with the work item's decisions, then batch: at the next pause (a phase
lands, a spawn returns), send one notice that names each open call, what
you chose, the main alternative, and where the record is.

`meridian notify --no-email "2 open calls in decisions.md" "Kept the sync API (async rewrite deferred); split billing out of users"`

Calls you're confident in, or that are cheap to undo, need no notice.

## Priority

`--priority` runs 1–5 (default 3). Raise it only for a failure that is
costing something while it waits, such as a broken deploy or a runaway job.
