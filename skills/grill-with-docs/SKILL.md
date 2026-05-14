---
name: grill-with-docs
type: reference
description: >
  Use when running an interactive grilling session against a plan or
  proposed direction. Challenges the plan against the project's documented
  domain model, sharpens terminology, and updates durable documentation as
  decisions crystallize. Works for any project domain — product plans,
  workflow designs, prompt systems, operations, architecture, or code.
model-invocable: false
---

# Grill With Docs

Load `/intent-modeling` if it isn't already loaded.

Interview the human relentlessly about every aspect of their plan until you
reach a shared understanding. Walk down each branch of the decision tree,
resolving dependencies between decisions one by one.

Keep each turn to the next unresolved branch or a small cluster of related
questions the human can answer in one reply, then wait. Provide your
recommended answer for each question.

## Starting the Session

Read the plan or proposed direction the human provides. Identify:

- **Decision branches** — choices that gate other choices
- **Dependency order** — which decisions must resolve first
- **Terms needing precision** — vague, overloaded, or undefined vocabulary
- **Assumptions** — things treated as given that may not be

Start with the highest-leverage unresolved dependency — the earliest branch
point that unblocks the most downstream decisions.

## Challenging Terminology

Check every significant term against the project's existing vocabulary
surfaces where they exist:

1. Project glossary or vocabulary pages in the KB (root or domain level) —
   in Meridian projects these are typically KB vocabulary pages, but follow
   whatever convention the project uses.
2. Colocated context docs (AGENTS.md, .context/CONTEXT.md) — local domain
   language near the content it describes.
3. Active work artifacts — terms already defined in the current work item.
4. Prior decision records — terms established by earlier choices.

When the human's language conflicts with documented terms, call it out
immediately. Name the conflict: "You said X, but the KB defines Y for this
concept — which should we use?"

Sharpen vague or overloaded terms into canonical terms. Use concrete
scenarios and edge cases to force precise boundaries — "Does 'sync' here
mean the mars package sync, the session sync, or something new?"

## Gathering Evidence

When answering requires cross-referencing project materials beyond what is
already in context, spawn a bounded explorer rather than bulk-reading the
tree yourself. This preserves your context window for the grilling
conversation.

- **`meridian spawn -a explorer`** — for questions answerable from project
  materials: docs, KB entries, requirements, strategy notes, context files,
  decision logs, implementation files. Scope each spawn to one question and
  target specific files or directories.
- **`meridian spawn -a session-explorer`** — only when the missing context
  lives in conversation transcripts, not artifacts.

Frame explorer prompts as evidence-seeking questions with file/path targets.
Act on findings to sharpen your next question or challenge the human's
assumptions with evidence.

## Updating Documentation

Update artifacts inline as decisions crystallize. Reasoning flattens the
longer you wait — capture it in the moment.

### Active work requirements

Resolve the work directory with `meridian work current`. Update
`requirements.md` there as decisions stabilize — record the decision, the
reasoning, and any constraints that emerged. Keep open questions visible.

### KB vocabulary

When the session produces a new canonical term or refines an existing one,
update the appropriate KB vocabulary page. Root vocabulary for cross-cutting
terms; domain vocabulary pages for subsystem-specific terms. Follow
`/kb-conventions` for page structure.

### Colocated context docs

When domain vocabulary belongs near specific project content, update
AGENTS.md or .context/CONTEXT.md at the relevant boundary. Follow
`/qi-layer` for placement: AGENTS.md for intent and mental model,
.context/CONTEXT.md for contracts and rationale. Keep entries focused on
domain concepts meaningful to project participants, not implementation
details.

### Decision records

Create durable decision records sparingly — only when the choice is hard to
reverse, surprising without context, and involves a real tradeoff. Use the
project's chosen decision surface (KB decision log, ADR directory, or
equivalent). Keep provisional decisions in `requirements.md` until they
prove durable. Follow `/decision-log` conventions where applicable.

## Session Rhythm

Each cycle through a decision branch:

1. State the branch and why it matters now (dependency context).
2. Ask focused questions with your recommended answer for each.
3. Wait for the human's response.
4. If the answer raises a sub-question, drill into it before moving on.
5. If the answer can be verified against project materials, spawn an
   explorer and use findings to confirm or challenge.
6. When the branch resolves, update the relevant documentation surface
   immediately.
7. Advance to the next branch.

The session ends when all branches of the decision tree are resolved and
the documentation reflects the shared understanding.
