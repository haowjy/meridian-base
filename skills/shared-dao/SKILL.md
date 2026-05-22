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

Shared vocabulary is a structural boundary between human intent and action.
Ambiguous, overloaded, drifting, or misleading terms corrupt reasoning early
and spread confusion through prompts, plans, docs, workflows, records, and
decisions. Treat vocabulary problems as design problems.

## Core Discipline

Scrutinize important terms aggressively. Reuse existing names when they
already fit the concept. Converge on one name per concept and one concept per
name as quickly as the evidence allows.

Resolve terminology early:

- rename when the clearer term is available
- define when the concept is real but still blurry
- flag when human judgment is genuinely required

Clear vocabulary compounds through every downstream artifact. Resolve
terminology while the meaning is still easy to sharpen.

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
3. **Check the operational artifacts** — file names, forms, workflows,
   records, schemas, commands, or code name things too. When these use a
   different name than people do, treat that as drift to resolve, not trivia
   to note.

Mint new terms when they mark a real new concept. Let new vocabulary reflect
clear distinctions rather than uncertainty, local convenience, or
unexamined drift.

## Disambiguation

Ambiguity is the root failure mode. Resolve it before writing definitions or
carrying the term forward:

- **Same term, different meanings:** pick one meaning for the canonical
  definition, and give the other meaning its own canonical name.
- **Different terms, same meaning:** pick one as canonical, record the
  others as aliases.
- **Unclear meaning:** interview domain experts ("When you say X, what
  specifically do you mean? What is X NOT?"). Probe until meaning
  converges, then define.

When terminology conflicts with existing KB, workflow, or implementation
usage, resolve the drift if you can. When you cannot, flag it explicitly
rather than silently carrying two competing names forward:

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

When a term's meaning deepens, update the definition to reflect the new
understanding. One term, one current meaning.

## Operations

Flag content needing human attention with `> [!FLAG] **Needs human review**`.
Searchable with `rg '\[!FLAG\]'`.

Before committing to KB: `meridian kg check` (broken links),
`meridian mermaid check` (diagram validity).

---

Shared vocabulary is the contract between human intent and agent action.
Ambiguity you leave in vocab propagates into every downstream decision.
Resolve terminology early so the structure stays clear.
