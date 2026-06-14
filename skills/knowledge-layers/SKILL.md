---
name: knowledge-layers
type: reference
description: Use when deciding where knowledge goes or reading/writing durable docs — AGENTS.md, .context/, KB, docs/, and work directories.
model-invocable: true
---

# Knowledge Layers

Load `/qi-layer` if it isn't already loaded.
Load `/llm-writing` if it isn't already loaded.

Where knowledge lives in a Meridian project. Use this to route information to
the right layer and to keep each layer doing its own job.

## Documentation Layers

| Layer | What it holds | Why it's separate |
|---|---|---|
| `AGENTS.md` | Intent and mental model for a directory | First thing agents read on entry |
| `.context/CONTEXT.md` | Detailed contracts, architecture, rationale | Reference depth, co-located with content |
| KB | Cross-cutting decisions, domain concepts, patterns | Spans components; outlives sessions |
| `docs/` | User-facing documentation | Different audience, different update cadence |
| Work directory | Temporary design decisions and scratch artifacts | Not colocated with durable content |

If knowledge is scoped to one directory, it belongs in `.context/`. If it
spans directories or isn't anchored to a specific location in the code, it
belongs in the KB. If it's for end users, it belongs in `docs/`. If it's a
temporary work artifact, it belongs in the current work directory.

## Placement Rules

| Content | Layer | Why |
|---|---|---|
| Mental model, constraints, anti-patterns | `AGENTS.md` | Orients agents on entry |
| Detailed contracts, architecture, rationale | `.context/` | Reference depth on demand |
| Cross-cutting concepts spanning directories | KB | Not owned by any one area |
| User-facing documentation | `docs/` | Different audience, different lifecycle |
| Design decisions (work in progress) | Work directory | Temporary, not colocated with content |

## KB Conventions

The KB holds cross-cutting knowledge that no single directory owns and that
outlives any individual session — decisions, domain concepts, architectural
rationale, and patterns.

### Current Truth Over History

The living KB holds the best current understanding of the system. Keep it
clean, direct, and current. When a claim, explanation, structure, or term is
superseded, remove it from the live KB rather than layering newer text around
older understanding.

Do not preserve stale knowledge inline just because it was once true. If old
material still has value as history, move it out of the living KB into
`kb/trash/` or another explicit archive area. The wiki should teach the
current system, not narrate its evolution unless the history is itself the
topic.

Current pages should read as current truth.

### Structure

Each project's KB `AGENTS.md` defines its own layer structure and governance.
See `resources/bootstrap.md` for a suggested starting layout.

### Wiki Page Conventions

#### One Concept Per Document

Each doc covers one coherent concept — one component, one interaction pattern,
one decision. When a doc covers two unrelated topics, split it. When two docs
explain the same concept from different angles, merge or cross-reference.

Name files by what they describe (`token-validation.md`), not when they were
written (`auth-redesign-notes.md`).

#### Hierarchical Organization

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

#### Vocab Pages

Load `/shared-dao` for vocab methodology, lifecycle, and conflict resolution.

Vocab files sit in a hierarchy matching the domain:

- **Root vocab** (`vocab.md`) — project-wide terms used across domains
- **Domain vocab** (`<domain>/vocab.md`) — terms specific to one domain
- **Subdomain vocab** (`<domain>/<subdomain>/vocab.md`) — further scoping

Each term entry includes canonical name, definition, aliases, and links.
Flag conflicts with `> [!FLAG] **Needs human review** — vocab conflict: ...`.
Check the vocab hierarchy at each level before creating a new entry.

#### Linking

Link to related docs using relative paths. Cross-reference instead of
re-explaining — each doc stays focused and there's one source of truth per
concept. When a fact results from a decision, link to the decision record.
Readers understand the system from wiki pages alone, following links to
decisions when they need the reasoning.

#### Readability

Write docs that work in isolation:

- **Self-contained** — enough inline context that a reader doesn't need three
  other docs first
- **Scannable** — headers, bullet lists, tables. Bold key terms on first use.
- **Concrete** — file paths, function names, type signatures over vague
  references
- **State invariants explicitly** — agents follow what's written

#### Style

Wiki pages teach how things work — mechanism, flows, edge cases. Capture what
code can't easily tell you: component relationships, dependency directions,
data flows, and why the system is shaped this way.

Use mermaid diagrams for anything spatial — component relationships, data
flows, state machines. Tables for comparisons. Reference source locations
rather than pasting code.

## Operations

**Ingest** — new information enters the KB. Read the source, extract key
knowledge, write or update wiki pages, update the index, log the change.
A single source may touch many pages.

**Maintain** — keep the wiki current. When a claim is superseded, remove it.
When new information contradicts existing pages, resolve the contradiction.
Current truth over history.

**Lint** — health-check the wiki. Look for contradictions between pages,
stale claims, orphan pages with no inbound links, important concepts
mentioned but lacking their own page, missing cross-references. Use
`/md-validation` for link checking and diagram validation.

Flag content needing human attention with `> [!FLAG] **Needs human review**`.
Searchable with `rg '\[!FLAG\]'`.
