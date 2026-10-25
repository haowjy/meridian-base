---
name: handoff
type: mode-shift
description: "Use when the next phase belongs to a different interactive lead: writes the transition brief and gives the user what they need to start the new primary session."
argument-hint: "What will the next session focus on?"
user-invocable: true
model-invocable: true
---

# Handoff

Write a transition brief and give the user what they need to start a new
interactive session with a different agent lead. Do not start it for them.

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

## Prepare the User's Launch

Give the user what they need to start the new primary session themselves; do
not start it for them. It runs in a new terminal where your environment is
gone, so write out every reference as its concrete value, not as a variable:
the work item, the source checkout, and the brief's path. Carry your current
session as the prior run by writing its concrete ID as the parent.
