---
name: knowledge-layers
type: reference
description: Use when deciding where knowledge goes or reading/writing durable docs — AGENTS.md, .context/, KB, docs/, and work directories.
model-invocable: true
---

# Knowledge Layers

Load `/qi-layer` when writing or editing AGENTS.md or .context/ files — it
owns the craft (four principles, contents guidelines, what doesn't belong).
Load `/llm-writing` if it isn't already loaded.

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

The living KB holds the best current understanding. When a claim in a concept,
architecture, or operations page is superseded, remove or rewrite the stale
claim rather than layering newer text around older understanding. Pages should
read as current truth.

Decision records are the exception: preserve superseded decisions when they
explain why the system changed. Mark the old decision as superseded and link to
the replacement, following the KB's decision conventions.

### Structure

Read the KB's own `AGENTS.md` before writing. Each KB defines its local
structure, naming, validation commands, and governance. Treat this skill as the
cross-project default; the local KB guide wins for that KB. See
`resources/bootstrap.md` for a suggested starting layout.

### Wiki Page Conventions

**One concept per document.** Split when a doc covers two unrelated topics.
Merge when two docs explain the same concept from different angles. Name
files by what they describe (`token-validation.md`), not when
(`auth-redesign-notes.md`).

**Hierarchical organization.** `index.md` is the entry point — a catalog
with links and one-line summaries. Directories emerge organically as a
domain accumulates enough distinct concepts.

**Vocabulary pages.** Load `/shared-dao` for vocabulary methodology. Follow
the KB's established filename (`vocabulary.md` or `vocab.md`) and index
structure; do not rename pages just to match a generic convention. Vocabulary
pages sit in a hierarchy matching the domain: root vocabulary page, domain
vocabulary pages, and subdomain vocabulary pages. Each term entry includes the
canonical name, definition, aliases when useful, and links to the owning concept
or decision.

**Linking.** Relative paths. Cross-reference instead of re-explaining —
each doc stays focused with one source of truth per concept. When a fact
results from a decision, link to the decision record.

**Readability.** Self-contained (enough inline context to read standalone),
scannable (headers, bullets, tables), concrete (file paths, function names
over vague references).

**Style.** Wiki pages teach how things work — mechanism, flows, edge cases.
Capture what code can't easily tell you. Use mermaid for anything spatial.
Tables for comparisons. Reference source locations rather than pasting code.

## Operations

**Ingest** — new information enters the KB. Read the source, extract key
knowledge, write or update wiki pages, and update indexes/cross-links touched by
the change. Update the KB log only for structural reorganizations or major
additions when the local KB guide asks for it.

**Maintain** — keep the wiki current. When a claim is superseded, remove it.
Current truth over history.

**Lint** — health-check the wiki. Look for contradictions, stale claims,
orphan pages, missing cross-references. Use `/md-validation` for link
checking and diagram validation.

Flag content needing human attention with `> [!FLAG] **Needs human review**`.
