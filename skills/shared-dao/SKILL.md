---
name: shared-dao
type: principle
description: >
  Load when establishing shared vocabulary, resolving term conflicts,
  disambiguating domain terminology, or auditing consistency across a
  project's vocab. Shared vocabulary is the contract between human intent
  and agent action — ambiguity is the root failure mode, vocab files are
  the record.
model-invocable: false
---

# Shared Dao

Shared vocabulary is the interface between human intent and agent action.
When humans and agents use the same word for different concepts, or different
words for the same concept, downstream work inherits the ambiguity. Vocab is
the contract that prevents this.

## Where Vocab Lives

Vocab files sit in a hierarchy matching the domain. Place terms at the lowest
common domain where they're shared:

- **Root vocab** (`vocab.md`) — project-wide terms used across domains
- **Domain vocab** (`<domain>/vocab.md`) — terms specific to one domain,
  created when a domain accumulates enough distinct terms
- **Subdomain vocab** (`<domain>/<subdomain>/vocab.md`) — further scoping

In the KB, vocab files live within the wiki hierarchy under their domain's
directory. In work items, the root `vocab.md` in the work directory is the
canonical vocabulary for that work item's duration.

Each term entry includes:

- **Canonical name** (heading or bold) — the authoritative form
- **Definition** — concise, one to three sentences. Include what the term
  is NOT when ambiguity is likely.
- **Aliases** — alternative names people or code actually use
- **Links** — to related pages, decision records, or source locations

## Discovery

Before defining new terms, mine what already exists:

1. **Read existing vocab files** — start at the relevant root or domain
   vocab. A term defined elsewhere under a different name is a conflict,
   not a new concept.
2. **Search conversations and artifacts** — scan prior design docs,
   requirements, KB pages, and conversation transcripts for terminology
   in use.
3. **Check the codebase** — code names things too. When code uses a
   different name than humans do, flag the drift.

## Disambiguation

Ambiguity is the root failure mode. Resolve it before writing definitions:

- **Same term, different meanings:** pick one meaning for the canonical
  definition, record the other as an alias with its own canonical name.
- **Different terms, same meaning:** pick one as canonical, record the
  others as aliases.
- **Unclear meaning:** do not define. Interview domain experts ("When you
  say X, what specifically do you mean? What is X NOT?"). Probe until
  meaning converges.

When terminology conflicts with existing KB or codebase usage, flag the
conflict rather than silently overriding:

> `> [!FLAG] **Needs human review** — vocab conflict: "<term A>" and
> "<term B>" may refer to the same concept.`

## Lifecycle

Terms evolve. Track what stage each term is in:

- **Canonical** — authoritative, settled. The source of truth.
- **Tentative** — proposed but not yet settled. Mark with `[tentative]`.
- **Deprecated** — superseded. Move to a "Deprecated terms" section with
  a pointer to the replacement.
- **Reserved** — intentionally held for future use. Move to a "Reserved
  terms" section.

When a term's meaning deepens, update the definition rather than keeping
the old one alongside. One term, one current meaning.

## When to Split

Keep terms at the root vocab while they're few and cross-domain. Split into
a domain vocab when:

- A domain accumulates 10+ terms distinct from the root
- Root vocab grows past ~40 terms
- Two domains use the same word differently (each domain gets its own
  canonical definition in its own vocab)

Domain vocabs should link back to root vocabs for terms they inherit.

## Operations

Flag content needing human attention with `> [!FLAG] **Needs human review**`.
Searchable with `rg '\[!FLAG\]'`.

Before committing to KB: `meridian kg check` (broken links),
`meridian mermaid check` (diagram validity).
