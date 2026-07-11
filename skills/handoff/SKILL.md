---
name: handoff
type: mode-shift
description: Produce a transition brief and launch command for the user's next interactive primary.
argument-hint: "What will the next session focus on?"
user-invocable: true
model-invocable: true
---

# Handoff

Write a transition brief and print a primary launch command. The user
runs the command to start a new interactive session with a different
agent lead.

If arguments were passed, treat them as the focus for the next session.

## Write the Transition Brief

Start with `/intent-modeling`: separate what the human has said from what
they actually want to be true when this work is done. The modeled intent
shapes everything in the brief.

Then compact the conversation into a file the next agent reads as its
opening prompt:

- Human intent: the end goal in their terms, not implementation steps
- Current state: what was accomplished, where things stand
- Key decisions and why
- Open questions or blockers
- Artifact paths: exact file paths to read first
- Suggested skills to invoke

Reference artifacts by path; don't duplicate their content.

Write to the active work directory (`meridian work current`). No work item
→ write to a temp file.

## Run Pre-* Checks

Before completing the handoff, check if any `pre-*` checkpoint skills are
installed for the next phase (e.g., `pre-dev` for implementation handoffs).
If present, load and run them to verify workspace, branches, and
prerequisites are ready for the next agent. Skip if none are installed.

## Choose the Next Agent

Explicit argument wins: `/handoff tech-lead`.

Otherwise infer from context. If ambiguous, run `meridian mars list --json`
and ask.

## Show the Chain

Before printing the launch command, show the user the handoff trail for the active work item so they can see where they've been:

```bash
meridian work sessions --primary
```

## Print the Launch Command

Resolve `$MERIDIAN_CHAT_ID` to the concrete chat ID (e.g., `c102`): the
user runs this in a new terminal where the env var no longer exists.

```
meridian -a [agent] \
  --work [work-id] \
  --task-dir [path] \
  --prompt-file [path-to-brief] \
  --from [resolved-chat-id]
```

Use `meridian`, not `meridian spawn` (primary launch, interactive). Include
`--work` when active, `--task-dir` when in a worktree or sibling repo.
