---
name: knowledge-layers
type: reference
description: Use when deciding where knowledge goes or reading/writing durable docs — AGENTS.md, .context/, KB, docs/, and work directories.
model-invocable: true
---

# Knowledge Layers

Load `/qi-layer` when writing or editing AGENTS.md or .context/ files — it
owns the craft (four principles, contents guidelines, what doesn't belong).
Load `/information-hierarchy` if not already loaded for disclosure tiers.
Load `/llm-writing` if not already loaded.

## The Five Layers

| Layer | What it holds | When to use it |
|---|---|---|
| `AGENTS.md` | Intent and mental model for a directory | First thing agents read on entry; what to understand *before* working here |
| `.context/CONTEXT.md` | Contracts, architecture, rationale | Reference depth, co-located with the code it describes |
| KB | Cross-cutting decisions, domain concepts, patterns | Spans directories; outlives sessions; no single directory owns it |
| `docs/` | User-facing documentation | Different audience, different update cadence |
| Work directory | Temporary design decisions and scratch | Not colocated with durable content; scoped to an active work item |

## Placement Rules

If knowledge is scoped to one directory → `.context/`.
If it's intent/mental-model for a directory → `AGENTS.md`.
If it spans directories or isn't anchored to code → KB.
If it's for end users → `docs/`.
If it's a temporary work artifact → work directory.

When in doubt, colocate. Knowledge that lives far from what it describes
rots faster — changes to the code don't trigger awareness that a distant
doc needs updating.

## KB Conventions

### Current Truth Over History

The living KB holds the best current understanding. When content is
superseded, delete it or move it to `archive/` (`.kgignore`'d, excluded
from the knowledge graph). Use judgment. Live content never references
archived content. Pages read as current truth, never narrate their own
evolution.

Decision records are the exception: preserve superseded decisions in place
when they explain why the system changed. Mark the old decision as
superseded and link to the replacement.

### Structure

Read the KB's own `AGENTS.md` before writing. Each KB defines its local
structure, naming, validation commands, and governance. Treat this skill as the
cross-project default; the local KB guide wins for that KB. See
`resources/bootstrap.md` for a suggested starting layout.

### Wiki Page Conventions

Follow `/information-hierarchy`. One concept per document; name files by
what they describe (`token-validation.md`), not when (`auth-redesign-notes.md`).
Cross-reference instead of re-explaining. Load `/shared-dao` for vocabulary
methodology. Use mermaid for anything spatial; capture what code can't
easily tell you.

## Operations

**Ingest** — new information enters the KB. Read the source, extract key
knowledge, write or update wiki pages, and update indexes/cross-links touched
by the change.

**Maintain** — keep the wiki current. When content is superseded, delete it
or archive it. Live content never references archived content.

**Lint** — health-check the wiki. Look for contradictions, stale claims,
orphan pages, missing cross-references. Use `/md-validation` for link
checking and diagram validation.

Flag content needing human attention with `> [!FLAG] **Needs human review**`.
