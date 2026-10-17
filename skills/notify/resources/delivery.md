# Delivery

`meridian notify` sends once through each route the user configured: by
default push (ntfy) and email (SMTP or Gmail), plus any channels they added
as hooks. It never retries. `--json` prints one result per route; a failed
route's error names the backends that failed.

When a route fails, the others still deliver; treat the notice as sent if the
command exits 0. When it exits 1 (nothing delivered), or nothing is configured,
don't retry in a loop or try to configure delivery yourself; fall back in
this order:

1. The harness's own notification tool, when it has one (for example a
   push-notification tool in Claude Code).
2. The record: write the notice where the human looks first (the work
   item's decisions, or your report), and put it at the top of your next
   message to them.

Then keep working on whatever doesn't wait on their answer, and say in your
report that delivery failed and which errors you saw. Leave
credentials and tokens out of messages and reports.
