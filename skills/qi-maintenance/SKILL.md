---
name: qi-maintenance
type: guardrail
description: "Load on agents that make durable source changes, so the colocated AGENTS.md and .context/ docs stay true for the next cold agent."
model-invocable: false
---

# Qi Maintenance

Treat the nearest `AGENTS.md` and current-truth `.context/` documents like
comments attached to the source: read them before changing the code they
cover.

As you make a coherent source change, keep those documents accurate in the
same branch. If a cold agent could still work correctly from them, leave them
alone. If they would mislead the next agent, update them before finishing.

Write what a cold agent needs and can't read from source. When the
implementation diverged from the settled plan, record the divergence and leave
the intent as settled.

Load `/qi-layer` when creating, moving, restructuring, or substantially
rewriting colocated knowledge.

Track deferred work separately: directory-local must-do work goes in the
nearest `.context/TODO`, directory-local nice-to-have work in
`.context/FUTURE`, and cross-cutting or externally visible work in the project
issue tracker. Load `/knowledge-layers` when placement is unclear.
Cross-cutting KB synthesis belongs to `@kb-lead`, once per change after it settles.
