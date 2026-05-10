---
name: qi-layer
type: reference
description: >
  Use when writing, reading, or deciding where to place inline knowledge —
  AGENTS.md and .context/CONTEXT.md files colocated with the content they
  describe. Covers what belongs in each, how they relate, and what goes
  elsewhere.
---

# qi-layer

Inline knowledge captures intent, boundaries, rationale, and anti-patterns —
what the surrounding files can't express on their own.

## AGENTS.md

Hierarchical routing nodes at directory boundaries. When an agent enters a
directory, AGENTS.md loads automatically — it orients before the agent
reads anything else. Parent context applies to children (hierarchical
loading).

Contents (50-150 lines, compressed):
- Purpose and scope (1-2 sentences)
- Entry points (key files, starting points)
- Downlinks to `.context/` for depth
- Downlinks to related directories

AGENTS.md routes. It does not explain, justify, or duplicate .context/.

## .context/CONTEXT.md

Depth content at semantic boundaries — where understanding is non-obvious
from the files alone, where responsibilities shift, or where an agent
reading cold would make wrong assumptions.

Sections (use only those with substance):

- **Contracts** — interfaces, invariants, obligations between producers
  and consumers. What breaks if violated.
- **Architecture** — component relationships, data flow, dependency
  direction. Mermaid for anything spatial.
- **Rationale** — why X over Y, rejected alternatives, constraints that
  drove the shape. What's invisible from the content itself.
- **Patterns** — how to work here, anti-patterns, concrete pitfalls.

The `.context/` directory is extensible — additional files alongside
CONTEXT.md for specialized concerns.

## What Does NOT Belong

- What the files already show — agents read content directly
- Exhaustive documentation — this is compression, not coverage
- Content that belongs elsewhere (see placement rules below)

The failure mode: a root AGENTS.md that balloons to 15k+ tokens, or
.context/ files that restate what surrounding files already make obvious.

## Placement Rules

| Content | Layer | Why |
|---|---|---|
| Local contracts, architecture | .context/ | Belongs with what it describes |
| Lean routing (what's here, where to look) | AGENTS.md | Orients agents before they read content |
| Cross-cutting concepts spanning directories | KB | Not owned by any one area |
| User-facing documentation | docs/ | Different audience, different lifecycle |
| Design decisions (work in progress) | work directory | Temporary, not colocated with content |

## Structural Rules

- Relative paths for all links
- AGENTS.md and .context/ at the same directory level (siblings)
- Link to files, not headings (headings change more often)
- Uplinks to KB for cross-cutting context
- Lateral links between .context/ directories with contracts between them
- Progressive disclosure: minimal at AGENTS.md level, full depth in .context/
