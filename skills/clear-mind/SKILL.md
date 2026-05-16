---
name: clear-mind
type: reference
description: >
  Load when spawning subagents. Why scoped spawns produce better work,
  when to spawn versus continue inline, and how to give the subagent
  exactly what it needs and nothing more.
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
