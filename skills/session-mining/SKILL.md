---
name: session-mining
type: reference
description: "Use when mining conversation history during dev work — recovering decisions from the top-level primary session, delegating bulk transcript reading to an explorer, or discovering all sessions tied to a work item across interruptions."
model-invocable: true
---

# session-mining

## Why Mining Matters

Design decisions, rejected alternatives, and discovered constraints often live in conversation instead of code or docs. Compaction makes that context expensive to recover later, so mine it before the next implementation or documentation step starts.

## Recover From the Top-Level Session First

Start from the top-level conversation. `$MERIDIAN_CHAT_ID` points to the primary session at the root of the chat tree, regardless of how deep in the spawn tree you are. That root context holds the primary's decisions and framing — usually the highest-leverage read.

Use a recent-context read first, then widen or anchor only if needed:

```bash
meridian session log "$MERIDIAN_CHAT_ID" --tail 20
```

Bare `meridian session log "$MERIDIAN_CHAT_ID"` reads the last 5 interaction
entries with safe previews. Entry `0` is the selected segment's
prologue/handoff slot; read it with `--from 0 --limit 1`. Use `--full` for the
full current segment, `--no-truncate` for complete content, and
`--around N --context M` when you need a deterministic window around a known
entry number.

## Delegate Bulk Reading, Don't Inline It

When the question spans long histories or multiple sessions, spawn @session-explorer for transcript mining and synthesis. That keeps your context window focused on decisions instead of raw transcript paging.

```bash
meridian spawn -a session-explorer \
  --prompt-file session-mine.md
```

If you are the @session-explorer, mine directly rather than spawning recursively.

## Discover Sessions Per Work Item

When work spans interruptions, reopenings, or multi-day execution, list all related sessions before mining. Reading only the current session misses prior decisions.

```bash
meridian work sessions <work_id> --all
```

## When to Skip Mining Entirely

Skip mining if the spawning prompt already includes the needed rationale, or if current design/plan artifacts already capture the decisions you need. Skim artifacts first, and mine only the gaps.
