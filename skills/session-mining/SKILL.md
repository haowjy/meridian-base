---
name: session-mining
type: reference
description: Use when recovering decisions or context from conversation history — session log navigation, transcript delegation.
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
entries from the current segment with safe previews. Navigation is
**segment-local by default**: `--from/--before/--around` are ordinals inside
the selected segment, defaulting to the current one. Entry `0` of any segment
is its setup slot (prologue/handoff); reach it with `--from 0 --limit 1`. Use
`--segment previous|current|N` to switch segments, `--full` for the full
selected segment (entry 0 included), `--no-truncate` for complete content, and
`--around N --context M` for a deterministic window around a known entry.

Reach for `--global` only when you need one flat stream across all segments
(every segment's entry 0 included, with unique global ordinals starting at 0).
It conflicts with `--segment` and requires `--from/--before/--around`. Prefer
segment-local navigation — it stays stable across compactions.

Search instead of paging when you know what you're looking for:

```bash
meridian session search "decision text" "$MERIDIAN_CHAT_ID"
meridian session search "auth" --work <work-id>     # scope to a work item
meridian session search "shape" --workspace         # current project + workspace
```

Each hit prints a deterministic `Open:` command — run it to jump straight to
the entry instead of recomputing windows.

## Delegate Bulk Reading, Don't Inline It

When the question spans long histories or multiple sessions, spawn @session-miner for transcript mining and synthesis. That keeps your context window focused on decisions instead of raw transcript paging.

```bash
meridian spawn -a session-miner \
  --prompt-file session-mine.md
```

If you are the @session-miner, mine directly rather than spawning recursively.

## Discover Sessions Per Work Item

When work spans interruptions, reopenings, or multi-day execution, list all related sessions before mining. Reading only the current session misses prior decisions.

```bash
meridian work sessions <work_id> --all
```

## When to Skip Mining Entirely

Skip mining if the spawning prompt already includes the needed rationale, or if current design/plan artifacts already capture the decisions you need. Skim artifacts first, and mine only the gaps.
