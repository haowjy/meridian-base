---
name: correct
description: "Use when the human wants a mistake agents keep making fixed. Starts from their correction or the mistake they name, finds what led the agent there, and fixes it where the next agent would meet it: the project's docs first, then the code's shape; a cause in an installed prompt becomes a note for that prompt's owner."
user-invocable: true
model-invocable: false
metadata:
  type: mode-shift
harness-overrides:
  claude:
    argument-hint: The correction or mistake to start from
---

# Correct

The human corrected an agent and doesn't want to do it again. Find what led
the agent to the mistake, and change that.

## Find the Cause

Start from the correction the human gave or the mistake they name. Read the
session where it happened: what the agent read, what it was told, what it
did (`@session-miner` finds the passages; read them yourself). When the
human asks for a sweep, mine recent sessions for the same mistake.

A single occurrence can be a bad run, with nothing in the setup to blame.
When that's what the evidence shows, say so and change nothing.

The usual causes:

- a line the agent read that misled it: stale, contradicted by the code, or
  buried under lines that matter less
- a code shape that invites the mistake: two ways to do one task, a
  misleading name, an example that copies wrong
- a prompt (an agent or a skill) that steers wrong, or says nothing at the
  moment of choice

## Fix It Where the Agent Meets It

In this order:

1. **The project's docs.** Correct or delete the line that misled the agent
   in `AGENTS.md`, `.context/` or the KB. Thinning is often the fix: a rule
   lost among ten others gets followed once they go. Add a line only when
   nothing the agent read covers the choice, and put it where the agent
   reads it as it makes that choice.
2. **The code's shape.** One supported way per task, a name that says what
   it does, no dead example to copy. This is a code change: it goes through
   the project's normal flow, not in with the correction.
3. **A prompt.** Leave an installed prompt as it is: the package is shared,
   and the next sync overwrites a local edit. Find its source (the package
   repository the project's Mars config names) and leave a note where its
   owners will see it: wherever the source's `AGENTS.md` says, an issue on
   its repository, or a message to whoever maintains it. The note says what
   the human corrected, in which session, and the line you suspect.
4. **A check or a permission**, only for a destructive mistake that has
   repeated, and with the human's approval: a denied command or a failing
   check blocks legitimate work too.

## Report

Each mistake with its evidence and cause, and what you changed or where you
left the note; and each one you judged a bad run, with why.
