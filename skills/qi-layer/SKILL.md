---
name: qi-layer
type: reference
description: Use when exploring or changing the codebase — read AGENTS.md first, use .context/CONTEXT.md for detail, keep intent docs succinct.
---

# qi-layer

Load `/knowledge-layers` for where each layer lives and what it holds.
Load `/llm-writing` if it isn't already loaded.

This skill is about **how to write and maintain** the code-local pair:
AGENTS.md and `.context/CONTEXT.md`.

## The Four Principles

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

## Writing AGENTS.md

**Read AGENTS.md before opening code files.**

Ask: **what must someone understand before working here?** That's what
AGENTS.md captures. It is the intent layer — not a routing table, file
index, or reference card.

Keep AGENTS.md **50–200 lines**. Include only what has substance:

- **Purpose** — what this area IS and what it ISN'T (1–3 sentences)
- **Mental model** — how to think about this area, key abstractions
- **Key rules** — constraints, what breaks if you get it wrong
- **Anti-patterns** — what NOT to do here
- **Downlinks** — to `.context/` for depth, to related areas

An agent that only reads AGENTS.md should be able to work correctly here.
An agent that also reads .context/ should be able to change things safely.

## Writing .context/CONTEXT.md

Reference depth, co-located with the code it describes. Where an agent
goes when it needs contracts, architecture, or rationale in detail.

Sections (use only those with substance):

- **Contracts** — interfaces, invariants, what breaks if violated
- **Architecture** — component relationships, data flow, dependency direction
- **Rationale** — why X over Y, rejected alternatives
- **Patterns** — how to work here, concrete pitfalls

The `.context/` directory is extensible — additional files alongside
CONTEXT.md for specialized concerns.

## What Does NOT Belong in AGENTS.md

Apply the **every-session test**: root AGENTS.md loads on every session.
If knowledge is only relevant when working in a specific domain, it belongs
in that domain's AGENTS.md or .context/, not root.

Apply the **think-vs-lookup test**: if removing a piece of text would cause
an agent to make a *wrong decision*, it belongs. If it would just mean the
agent has to *look it up*, it belongs in .context/ instead.

Specific failure modes:

- **Session bleed** — LLM working notes that calcified into the instruction
  file. Tells: status-update language ("**deleted**", "shipped", "deferred"),
  implementation terms packed without framing, history narration. These are
  artifacts of the session that *produced* the change, not understanding about
  the codebase *as it stands now*.
- **Reference material posing as intent** — tables, command blocks, full
  scheme vocabularies, implementation specifics. These are lookup material,
  not mental model.
- **Redundant guards** — prose warnings for invariants already enforced by
  tests or types. The code is the real guard; prose rots faster.
- **Duplicated knowledge** — restating what lives in a skill, a domain
  .context/, or a KB page. Point, don't duplicate.
- **Domain-specific detail at root** — URI scheme tables, gateway pricing
  internals, auth implementation details. These belong in their domain's
  AGENTS.md, not root.

## Structural Rules

- Relative paths for all links
- AGENTS.md and .context/ at the same directory level (siblings)
- Link to files, not headings (headings change more often)
- Lateral links between `.context/` directories with contracts between them
- LCA deduplication: if two siblings share context, put it in the parent

## Maintenance

Keep knowledge layers current as you work. When your changes shift the
mental model, contracts, or decisions — update AGENTS.md, .context/, and KB
in the same pass, not as a deferred follow-up.
