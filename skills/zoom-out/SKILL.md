---
name: zoom-out
type: mode-shift
description: Use when orienting in an unfamiliar area — fans out parallel explorers across code, knowledge, and history, then synthesizes one orientation map.
user-invocable: true
model-invocable: true
---

# Zoom Out

Orient in an unfamiliar area by fanning out parallel explorers — each covering a different angle — then synthesizing their reports into one orientation map. A single explorer sees one slice; zoom-out covers code *and* knowledge *and* history at once, so the picture isn't skewed by one lens.

Use when starting in an unfamiliar subsystem, picking up someone else's work, or when the user says "orient me" / "what's the lay of the land here."

## Fan Out

Spawn in parallel, each scoped to one angle and one question. Drain with `meridian spawn wait`.

- **Code structure** — `@explorer`: callers, dependencies, module boundaries, entry points, where behavior actually lives.
- **Documented knowledge** — `@explorer` over the KB (`meridian context kb`): what's been written about this area — architecture, guides, synthesized research.
- **Decision history** — `@session-miner`: why it's shaped this way — prior choices, rejected alternatives, constraints discovered. Skip when there's no relevant session history.
- **Domain concepts** — `@explorer`: the vocabulary in use (KB vocab pages, `.context/CONTEXT.md`, AGENTS.md).

Scope each prompt to its angle with concrete path or topic targets. Don't let one explorer cover two angles — the value is independent coverage.

## Synthesize

Read the reports and produce one orientation map, not four stitched-together dumps:

- **What this is** — the area's purpose and boundaries, in two or three sentences.
- **Structure** — the modules and interfaces that matter and how they connect (a mermaid diagram if the shape is spatial).
- **Why it's like this** — the decisions and constraints that explain the current shape.
- **Vocabulary** — the terms needed to speak about it precisely.
- **Open threads** — gaps, debt, or unresolved questions the explorers surfaced.

When reports contradict each other, resolve it rather than listing both — code is ground truth; a doc that disagrees is stale (note it). Keep the map tight: the goal is a reader who can now navigate the area, not an exhaustive transcript.
