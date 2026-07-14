---
name: qi-maintenance
type: guardrail
description: "Always load on agents that make durable source changes: keep colocated agent-facing knowledge synchronized with the source."
model-invocable: false
---

# Qi Maintenance

Treat the nearest `AGENTS.md` and current-truth `.context/` documents like
comments attached to the source.

As you make a coherent source change, keep those documents accurate in the
same branch. If a cold agent could still work correctly from them, leave them
alone. If they would mislead the next agent, update them before finishing.

Do not narrate the diff, duplicate facts visible in source, or rewrite intent
to bless an implementation that diverged from the settled plan. Record the
divergence instead.

Load `/qi-layer` when creating, moving, restructuring, or substantially
rewriting colocated knowledge.

Track deferred work separately: directory-local must-do work goes in the
nearest `.context/TODO`, directory-local nice-to-have work in
`.context/FUTURE`, and cross-cutting or externally visible work in the project
issue tracker. Load `/knowledge-layers` when placement is unclear.
Cross-cutting KB synthesis belongs to `@kb-lead` after the phase settles.
