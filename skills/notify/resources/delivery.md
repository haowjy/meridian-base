# Delivery

`meridian notify` sends once to each backend the user configured: push
(ntfy) and email (SMTP or Gmail). It never retries. `--json` prints a
per-backend report.

When a backend fails, the others still deliver; treat the notice as sent if
any backend succeeded. When every backend failed, or none is configured,
don't retry in a loop or try to configure delivery yourself; fall back in
this order:

1. The harness's own notification tool, when it has one (for example a
   push-notification tool in Claude Code).
2. The record: write the notice where the human looks first (the work
   item's decisions, or your report), and put it at the top of your next
   message to them.

Then keep working on whatever doesn't wait on their answer, and say in your
report that delivery failed and which backend errors you saw. Leave
credentials and tokens out of messages and reports.
