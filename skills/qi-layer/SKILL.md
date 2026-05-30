---
name: qi-layer
type: reference
description: Use when placing or reading inline knowledge — AGENTS.md and .context/CONTEXT.md conventions.
---

# qi-layer

Inline knowledge is a hierarchical intent system. It gives agents
working understanding through fractal compression — each level summarizes
the level below, not the raw content.

## AGENTS.md — The Intent Layer

Intent Nodes at directory boundaries. When an agent enters a directory,
AGENTS.md loads automatically — it provides the compressed understanding
needed to work correctly here. Parent context applies to children
(hierarchical loading).

AGENTS.md is NOT a routing table or table of contents. It is the intent
layer — the mental model, constraints, invariants, and "how to think about
this area" that an agent needs BEFORE touching any file.

Ask: **what must someone understand before working here?** That's what
AGENTS.md captures.

### The Four Principles

1. **Fractal Compression** — leaf AGENTS.md summarizes its directory's
   content; parent AGENTS.md summarizes its children. Each level is a
   compression of the level below.
2. **Hierarchical Summarization** — root provides broad architectural
   frame. Leaves provide local working knowledge. Agents accumulate
   understanding as they descend.
3. **LCA Deduplication** — shared knowledge appears once at the shallowest
   node covering all relevant paths. Never duplicate between siblings.
4. **Progressive Disclosure** — enough to work correctly at this level.
   Links to .context/ for depth. Links to KB for cross-cutting concepts.

### Contents

Compressed, 50-200 lines. Include what has substance:

- **Purpose** — what this area IS and what it ISN'T (1-3 sentences)
- **Mental model** — how to think about this area, key abstractions, the
  shape of the design
- **Key rules** — constraints, invariants, what breaks if you get it wrong
- **Anti-patterns** — what NOT to do here, common mistakes
- **Entry points** — where to start reading, key files
- **Downlinks** — to .context/ for reference depth, to related areas

AGENTS.md does NOT duplicate .context/ content. It provides the frame;
.context/ provides the reference material.

## .context/CONTEXT.md — Reference Depth

Detailed documentation that lives physically next to what it describes.
Co-location is the point — .context/ stays in sync with adjacent files
because it's visible, discoverable, and maintained alongside them.

Where an agent goes when it needs to understand contracts, architecture,
or rationale in detail — the specifics behind the AGENTS.md frame.

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

## Why Two Layers

Progressive disclosure. AGENTS.md gives the frame; .context/ gives depth
when needed. Information layered by need, not dumped all at once.

| | AGENTS.md | .context/ |
|---|---|---|
| **Loading** | Auto-loaded on entry | On demand |
| **Purpose** | Orient — mental model, rules | Document — contracts, rationale |
| **Token budget** | 50-200 lines | Unlimited |
| **Proximity** | Points to what matters | Lives next to what it describes |

An agent that only reads AGENTS.md should be able to work correctly here.
An agent that also reads .context/ should be able to change things safely.

Even without auto-loading, you'd want the split: AGENTS.md compresses
understanding hierarchically; .context/ keeps detailed documentation
co-located with the content it documents, where it stays discoverable
and in sync.

## What Does NOT Belong

- What the files already show — agents read content directly
- Exhaustive documentation — this is compression, not coverage
- Content that belongs elsewhere (see placement rules below)

The failure mode: AGENTS.md that lists files without providing
understanding, or .context/ that restates what the content makes obvious.

## Placement Rules

| Content | Layer | Why |
|---|---|---|
| Mental model, constraints, anti-patterns | AGENTS.md | Orients agents on entry |
| Detailed contracts, architecture, rationale | .context/ | Reference depth on demand |
| Cross-cutting concepts spanning directories | KB | Not owned by any one area |
| User-facing documentation | docs/ | Different audience, different lifecycle |
| Design decisions (work in progress) | work directory | Temporary, not colocated with content |

## Structural Rules

- Relative paths for all links
- AGENTS.md and .context/ at the same directory level (siblings)
- Link to files, not headings (headings change more often)
- Uplinks to KB for cross-cutting context
- Lateral links between .context/ directories with contracts between them
- LCA deduplication: if two siblings share context, put it in the parent
