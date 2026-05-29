---
name: clear-mind
type: reference
description: >
  Load before spawning subagents to protect focus and role fit. Make sure to
  re-read the available agents before spawning a subagent; choose the most
  specific owner instead of broad defaults, then write a tight handoff with only
  the context that subagent needs.
detail: Context hygiene — when to spawn fresh vs continue inline.
model-invocable: true
---

# Clear Mind

Every word in context competes for attention. Prior turns, dead ends, and
artifacts the subagent doesn't need — all of it dilutes focus. A spawn is
a cleared mind: fresh context, one job, nothing else in the way.

LLMs lose accuracy as context grows, even with perfect retrieval. Keeping
context scoped to one task is the most reliable thing you can do for
output quality.

## When to Spawn

When the current context would interfere. If the chat is crowded with
decisions that don't apply to the next task, spawn. If the next task
requires a different kind of thinking — segmentation needs different
evaluation than review — spawn. If you can't articulate why two
responsibilities belong in one agent, they probably don't.

When in doubt, spawn. A fresh context window costs less than cluttered
output.

## Choosing the Agent

Before spawning, read the relevant installed agent descriptions and choose the
most specific owner for the work. Do not route by broad defaults when a
narrower specialist exists. If ownership is ambiguous, state the distinction,
then choose the agent whose description best matches the work.

Bigger tasks should usually be delegated, but delegation is not offloading.
A scoped handoff to the right specialist beats a broad handoff to a generalist.

## Writing the Handoff

Give the subagent what its role needs. A coder needs what to build and
which files — give the design conclusion, not the deliberation. A reviewer
needs the artifact and a focus area — give the output, not how it was
produced. An architect needs the design question and constraints — give the
problem, not the codebase layout.

Be concrete. "Find where auth logic is duplicated across src/api/handlers/"
tells a subagent where to look — "explore the codebase" tells it nothing.

Front-load the task. Purpose first, specifics second, file references last.
The subagent should know its job by line 3.

Include one way to verify. The subagent checks itself before reporting.

Write the outcome, not the conversation. "The user needs X because Y" —
not "the user and I discussed." The subagent wasn't there.

A handoff fits in one screen. Every sentence you keep is a sentence the
subagent can't use for work.

Write the handoff to a prompt file and invoke with `--prompt-file`. Write to the
system temp directory with a descriptive name: `<tmpdir>/coder-auth.md`. See
`/meridian-spawn` for full mechanics.
