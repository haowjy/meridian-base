---
name: handoff
type: mode-shift
description: "Use when the next phase belongs to a different interactive lead: writes the transition brief and prepares the new primary session."
argument-hint: "What will the next session focus on?"
user-invocable: true
model-invocable: true
---

# Handoff

Write a transition brief and prepare a new primary session. The user starts the
new interactive session with a different agent lead.

If arguments were passed, treat them as the focus for the next session.

## Write the Transition Brief

Start with `/intent-modeling`: separate what the human has said from what they
actually want to be true when this work is done. The modeled intent shapes
everything in the brief.

Then compact the conversation into a file the next agent reads as its opening
prompt:

- Human intent: the end goal in their terms, not implementation steps
- Current state: what was accomplished, where things stand
- Key decisions and why
- Open questions or blockers
- Artifact paths: exact file paths to read first
- Suggested skills to invoke

Keep artifact content in its files and give their paths in the brief. Write the
brief to the active work directory. Without a work item, use a temporary file.

## Run Pre-* Checks

Before completing the handoff, check whether any `pre-*` checkpoint skills are
installed for the next phase (for example, `pre-dev` for an implementation
handoff). Load and run each applicable checkpoint so the next phase's
prerequisites are ready.

## Choose the Next Agent

An explicit argument wins: `/handoff tech-lead`. Otherwise infer from context
and the agents you can use. Ask when the choice is ambiguous.

## Show the Chain

Show the user the primary-session trail for the active work item so they can see
where they have been.

## Prepare the Primary Session

Prepare a new primary session, not a delegated run. Carry the active work item,
the source checkout, the transition brief, and the current primary session as
its parent so the next lead can recover the chain. Present the prepared handoff
so the user can start the next lead.
