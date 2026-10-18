# Delivery

`meridian notify` sends once through each route the user configured: by
default push (ntfy) and email (SMTP or Gmail), plus any channels they added
as hooks. It never retries. `--json` prints one result per route; a failed
route's error names the backends that failed.

When a route fails, the others still run. Read the command's output rather
than treating every exit 0 as delivery:

- `Notification sent via ...` means at least one route delivered. With
  `--json`, at least one result has `status: "sent"`.
- A warning with a sent result is partial delivery. In particular, when ntfy
  accepted the text but rejected an attached file, the warning names that
  file. Do not resend the notification text; mention the missing attachment
  in the record or report.
- `Nothing delivered.` means every route was disabled, skipped, or selected a
  `none` backend. The warning `no notification route ran` also covers hooks
  being disabled. These outcomes exit 0 because delivery was intentionally
  inactive, but the human was not notified.
- Exit 1 means every attempted route failed and none delivered.

For either no-delivery outcome, don't retry in a loop or try to configure
delivery yourself; fall back in this order:

1. The harness's own notification tool, when it has one (for example a
   push-notification tool in Claude Code).
2. The record: write the notice where the human looks first (the work
   item's decisions, or your report), and put it at the top of your next
   message to them.

Then keep working on whatever doesn't wait on their answer, and say in your
report that delivery was inactive or failed and which warnings or errors you
saw. Leave
credentials and tokens out of messages and reports.
