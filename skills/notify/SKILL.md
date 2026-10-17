---
name: notify
type: reference
description: "Use when there is a decision for the human, an uncertain call that will be costly to reverse, a blocker, or a finished task: tells them with `meridian notify`."
model-invocable: true
---

# Notify

For a decision the human must make, an uncertain call that will be costly
to reverse, a blocker, or a finished task, run `meridian notify
"<message>"`. The first line says what they need to decide or see; details
can follow, or come from a file with `"$(cat <path>)"`. Send each once;
routine progress is not a reason.

Examples, flags, and batching uncertain calls: `resources/examples.md`.
When delivery fails: `resources/delivery.md`.
