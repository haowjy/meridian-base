---
name: kb-conventions
type: reference
description: Use when reading or writing KB entries — layer model, naming conventions, tooling.
model-invocable: true
---

# KB Conventions

Load `/llm-writing` if it isn't already loaded.

## Five Layers

The KB (`meridian context kb`) has five layers:

**Sources** — raw material: articles, research, transcripts, data. Immutable.
The LLM reads from sources but never modifies them.

**Decisions** — the reasoning layer. Why a source matters, why the wiki is
shaped the way it is, what was chosen and rejected. Decisions connect sources
to knowledge by explaining the interpretation and judgment applied.

**Wiki** — synthesized knowledge pages. How things work, concepts,
architecture. The LLM owns this layer: creates pages, updates them, maintains
cross-references, keeps everything consistent. Shaped by the decisions.

**Log** — what changed in the wiki and why. The audit trail of how the KB
evolved — what was added, updated, or restructured, and what triggered it.

**Schema** (`AGENTS.md`) — user-defined governance. Defines layer structure,
conventions, and workflows.

## Current Truth Over History

The living KB holds the best current understanding of the system. Keep it
clean, direct, and current. When a claim, explanation, structure, or term is
superseded, remove it from the live KB rather than layering newer text around
older understanding.

Do not preserve stale knowledge inline just because it was once true. If old
material still has value as history, move it out of the living KB into
`kb/trash/` or another explicit archive area. The wiki should teach the
current system, not narrate its evolution unless the history is itself the
topic.

Current pages should read as current truth. A reader should not need to guess
which paragraph still applies.

## Wiki Page Conventions

### One Concept Per Document

Each doc covers one coherent concept — one component, one interaction pattern,
one decision. When a doc covers two unrelated topics, split it. When two docs
explain the same concept from different angles, merge or cross-reference.

Name files by what they describe (`token-validation.md`), not when they were
written (`auth-redesign-notes.md`).

### Hierarchical Organization

`index.md` is the entry point — a catalog with links and one-line summaries,
organized by domain. Directories emerge organically as a domain accumulates
enough distinct concepts. Nest as deep as the content warrants.

```
index.md
<domain>/
  overview.md
  <topic>.md
  <sub-domain>/
    <topic>.md
```

The overview at each level orients the reader: what exists here, how pieces
relate, where to go deeper.

### Vocab Pages

Load `/shared-dao` for vocab methodology, lifecycle, and conflict resolution.
This section covers the structural conventions.

Vocab files sit in a hierarchy matching the domain:

- **Root vocab** (`vocab.md`) — project-wide terms used across domains
- **Domain vocab** (`<domain>/vocab.md`) — terms specific to one domain
- **Subdomain vocab** (`<domain>/<subdomain>/vocab.md`) — further scoping

Each term entry includes canonical name, definition, aliases, and links.
Flag conflicts with `> [!FLAG] **Needs human review** — vocab conflict: ...`.
Check the vocab hierarchy at each level before creating a new entry.

### Linking

Link to related docs using relative paths. Cross-reference instead of
re-explaining — each doc stays focused and there's one source of truth per
concept. When a fact results from a decision, link to the decision record.
Readers understand the system from wiki pages alone, following links to
decisions when they need the reasoning.

### Readability

Write docs that work in isolation:

- **Self-contained** — enough inline context that a reader doesn't need three
  other docs first
- **Scannable** — headers, bullet lists, tables. Bold key terms on first use.
- **Concrete** — file paths, function names, type signatures over vague
  references
- **State invariants explicitly** — agents follow what's written

### Style

Wiki pages teach how things work — mechanism, flows, edge cases. Capture what
code can't easily tell you: component relationships, dependency directions,
data flows, and why the system is shaped this way.

Use mermaid diagrams for anything spatial — component relationships, data
flows, state machines. Tables for comparisons. Reference source locations
rather than pasting code.

## Operations

Flag content needing human attention with `> [!FLAG] **Needs human review**`.
Searchable with `rg '\[!FLAG\]'`.

Use `/md-validation` for link checking and diagram validation before committing.
