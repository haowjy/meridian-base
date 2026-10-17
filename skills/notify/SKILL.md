---
name: notify
type: reference
description: "Use when there is a decision for the human, an uncertain call that will be costly to reverse, a blocker, or a finished task: tells them with `meridian notify`."
model-invocable: true
---

# Notify

For a decision the human must make, an uncertain call that will be costly
to reverse, a blocker, or a finished task, run `meridian notify "<title>"
"<body>"`. The title is one line: what they need to decide or see. The body
is optional detail. Send the material behind it, such as a decision record,
report or screenshot, with `--attach <path>` (repeatable) rather than pasting
it. Send each once; routine progress is not a reason.

Examples, flags, and batching uncertain calls: `resources/examples.md`.
When delivery fails: `resources/delivery.md`.
