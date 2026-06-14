---
name: qi-layer
type: reference
description: Use when exploring or changing the codebase — read AGENTS.md first, use .context/CONTEXT.md for detail, keep intent docs succinct.
---

# qi-layer

Inline knowledge is a hierarchical intent system. It gives agents
working understanding through fractal compression — each level summarizes
the level below, not the raw content.

## AGENTS.md — The Intent Layer

**Read AGENTS.md before opening code files.**

AGENTS.md is the first thing agents read on entry. Keep it **succinct**:
purpose, mental model, key rules, anti-patterns, entry points. Put detail in
`.context/CONTEXT.md`; AGENTS.md stays high-level.

AGENTS.md is the intent layer — the mental model, constraints, invariants,
and "how to think about this area" that an agent needs BEFORE touching any
file. It is not a routing table or table of contents.

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
4. **Progressive Disclosure** — give just enough to work correctly at this
   level. Link to `.context/CONTEXT.md` for depth.

### Contents

Keep AGENTS.md **50–200 lines**. Include only what has substance:

- **Purpose** — what this area IS and what it ISN'T (1–3 sentences)
- **Mental model** — how to think about this area, key abstractions, the
  shape of the design
- **Key rules** — constraints, invariants, what breaks if you get it wrong
- **Anti-patterns** — what NOT to do here, common mistakes
- **Entry points** — where to start reading, key files
- **Downlinks** — to `.context/` for reference depth, to related areas

AGENTS.md provides the frame; `.context/` provides the reference material.
Keep `.context/` content in `.context/`.

## .context/CONTEXT.md — Reference Depth

Detailed documentation that lives physically next to what it describes.
Co-location is the point — `.context/` stays in sync with adjacent files
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
| **Token budget** | 50–200 lines | Unlimited |
| **Proximity** | Points to what matters | Lives next to what it describes |

An agent that only reads AGENTS.md should be able to work correctly here.
An agent that also reads .context/ should be able to change things safely.

## What Does NOT Belong

- What the files already show — agents read content directly
- Exhaustive documentation — this is compression, not coverage
- Content that belongs elsewhere (see placement rules below)

The failure mode: AGENTS.md that lists files without providing
understanding, or .context/ that restates what the content makes obvious.

## Where the Other Layers Live

`AGENTS.md` and `.context/` are the code-local inline-knowledge pair. For the
full map — KB, `docs/`, work directories, and when to use each — load
`/knowledge-layers`.

## Structural Rules

- Relative paths for all links
- AGENTS.md and .context/ at the same directory level (siblings)
- Link to files, not headings (headings change more often)
- Lateral links between `.context/` directories with contracts between them
- LCA deduplication: if two siblings share context, put it in the parent
