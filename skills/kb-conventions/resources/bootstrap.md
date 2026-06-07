# KB Bootstrap

Starter layout for a new project KB.

## Directory Layout

```
kb/
  AGENTS.md          # governance — writing rules, content types, validation
  index.md           # catalog of pages with one-line summaries
  vocab.md           # project-wide terminology
  trash/             # superseded content, not maintained
```

Add directories as the KB grows — a topic earns a directory when it has
multiple related pages.

## Content Types

A KB holds four kinds of content.

**Wiki pages** — synthesized knowledge. How things work, concepts,
architecture, patterns. Agents create pages, update them, and maintain
cross-references.

**Decision records** — what was chosen, what was rejected, and why. Wiki
pages link to decisions for rationale; decisions link to wiki pages for
context. Separate from wiki pages because the reasoning behind a choice
outlives the description of the current system — when the system changes,
the old decision record still explains why it was built that way.

**Sources** — raw material: articles, research, transcripts, data. Immutable.
Agents read from sources but never modify them.

**Log** — what changed in the wiki and why. Append-only audit trail. Each
entry records what was ingested or updated, what pages were touched, and the
reasoning.

## Operations

**Ingest** — new information enters the KB. Read the source, extract key
knowledge, write or update wiki pages, update index, log the change. A
single source may touch many pages.

**Maintain** — keep the wiki current. When a claim is superseded, remove it.
When new information contradicts existing pages, resolve the contradiction.
Current truth over history.

**Lint** — health-check the wiki. Look for contradictions between pages,
stale claims, orphan pages with no inbound links, important concepts
mentioned but lacking their own page, missing cross-references.

## Starter AGENTS.md

```markdown
# KB Guide

## What the KB Is

Cross-cutting knowledge that spans components and outlives sessions.
Decisions, domain concepts, architectural rationale, and patterns.

Raw research dumps and conversation transcripts don't belong here —
synthesize them first. Active task plans live in work directories, not the KB.

## Current Truth Over History

The KB holds the best current understanding. When a claim, explanation, or
term is superseded, remove it from the live KB rather than layering newer
text around older understanding. Move superseded content to `trash/` if it
has historical value.

Pages should read as current truth, not narrate evolution.

## Writing

- One concept per page. Split when a page covers two unrelated topics.
- Cross-reference, don't re-explain. Each concept has one source of truth.
- Name files by what they describe (`token-validation.md`), not when
  (`auth-redesign-notes.md`).
- Calibrate depth to importance. Reference material is terse and scannable.
  Architecture pages walk through reasoning.
- Decision records capture what was chosen, what was rejected, and why.
  Wiki pages link to them for rationale.

## Structure

- `index.md` — catalog. Update when you create or modify a page.
- Directories emerge organically as topics accumulate related pages.

## Validation

Use `/md-validation` for link checking and diagram validation before
committing.
```
