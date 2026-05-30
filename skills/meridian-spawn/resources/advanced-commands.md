# Advanced Spawn Commands

Read this when you need continue, cancel, stats, permissions, reports, or dry-run — commands beyond the core loop. For troubleshooting, run `meridian doctor` or inspect spawn state with `meridian spawn show SPAWN_ID`.

## Continue & Fork

Resume a previous spawn's harness session, or fork it to try an alternate approach:

```bash
meridian spawn --continue SPAWN_ID --prompt-file followup.md --bg
meridian spawn --continue SPAWN_ID --fork --prompt-file alt-approach.md --bg
```

`--continue` reuses the harness session (conversation history preserved) — use it for follow-ups where you want the agent to build on what it already did. `--fork` branches from the same session but creates a new spawn ID — use it when you want to explore an alternative direction while preserving the original trajectory as a fallback.

## Cancel

```bash
meridian spawn cancel SPAWN_ID
```

Sends SIGINT to the harness process. The spawn finalizes with exit code 130.

## Stats

Check cost, token usage, and duration across spawns — useful for tracking budget, comparing model costs, or identifying spawns that took unexpectedly long:

```bash
meridian spawn stats
meridian spawn stats --session ID
```

Use `--session` to scope to a specific coordination session.

## Spawn Show Flags

```bash
meridian spawn show SPAWN_ID --no-report     # omit the full report text
meridian spawn show SPAWN_ID --include-files  # include file metadata
```

## Reports

`spawn` returns status when complete. Use `spawn show` (report included by default) or `spawn report` subcommands for report management:

```bash
# View status + report together
meridian spawn show SPAWN_ID

# View a spawn's report
meridian spawn report show SPAWN_ID

# Search across all spawn reports by text
meridian spawn report search "auth refactor" --limit 10
```

Reports are written by the spawned agent itself at the end of its run — there is no external `report create` command. If you need to annotate a spawn from the outside, attach notes to the work item instead.

## Inspecting a Spawn's Conversation

Read what a spawn said and did using `meridian session log` with the spawn ID:

```bash
meridian session log p107                    # last 5 interaction entries, current segment
meridian session log p107 --tail 20          # last 20 entries
meridian session log p107 --from 0 --limit 1 # segment setup slot (entry 0)
meridian session log p107 --around 80 --context 8
meridian session log p107 --segment previous # earlier segment after compaction
meridian session log p107 --full             # full current segment (incl. entry 0)
meridian session log p107 --full --no-truncate
meridian session log p107 --global --around 240 --context 8  # flat ordinals across segments
meridian session search "error" p107         # search; each hit prints an Open: command
```

Navigation is segment-local by default; `--global` is explicit opt-in for a single flattened stream and conflicts with `--segment`. Boundary hints (`Previous segment:` / `Next segment:`) appear when a window touches a segment edge. Search results include a deterministic `Open:` command per hit — run it directly.

This reads the spawn's own transcript. Combine with `spawn children` to trace a full spawn tree:

```bash
meridian spawn children p107           # discover child IDs
meridian session log p108              # read a child's conversation
```

## Steering a Running Spawn

`inject` relays user direction to a running spawn — wrong approach, missed constraint, clarified requirement. The message lands as a user turn mid-session, so the agent pivots to it. Only inject when forwarding something the user said; self-generated nudges waste the spawn's attention.

```bash
meridian spawn inject p107 --message "Use the existing adapter pattern in src/adapters/"
```

## Committing Spawn Changes

Use `meridian spawn files` to stage exactly what a spawn changed:

```bash
meridian spawn files p107 | xargs git add
meridian spawn files p107 -0 | xargs -0 git add   # paths with spaces
```

## Template Variables

Use `{{KEY}}` placeholders in prompt files, replaced at launch time with `--prompt-var`:

```bash
meridian spawn -a coder --prompt-file task.md --bg \
  --prompt-var TASK=auth-refactor \
  --prompt-var CONSTRAINT="no direct DB access"
```

Where `task.md` contains `{{TASK}}` and `{{CONSTRAINT}}` placeholders.

## Dry Run

```bash
meridian spawn --dry-run -m MODEL --prompt-file plan-migration.md
```

Preview the assembled prompt and command without executing the harness.

## Permission Tiers

Use `--sandbox` to control filesystem access and `--approval` to control tool approval behavior:

```bash
meridian spawn -m MODEL --prompt-file analysis.md --sandbox read-only --bg
meridian spawn -m MODEL --prompt-file task.md --approval confirm --bg
```

Flags:
- `--sandbox read-only|workspace-write|full-access|danger-full-access` — filesystem sandbox tier
- `--approval default|confirm|auto|yolo` — tool approval mode

## Background Flag (manual polling)

If your harness doesn't support background execution or parallel tool calls, you can use `--background` to launch spawns without blocking:

```bash
meridian spawn --background -a agent --prompt-file task.md
# → returns immediately: {"spawn_id": "p107", "status": "running"}

meridian spawn wait
# → blocks until all pending spawns complete, returns status + full report

# Multiple spawns in parallel
meridian spawn --background -a agent --prompt-file step-a.md \
  --goal "Step A acceptance criteria met"
meridian spawn --background -a agent --prompt-file step-b.md \
  --goal "Step B acceptance criteria met"
# Wait for all pending spawns — IDs discovered automatically
meridian spawn wait
```

Most harnesses have built-in background execution that handles per-spawn notification natively. Prefer that over `--background` + `spawn wait`.

For stuck spawns, logs, or low-level state inspection, run `meridian doctor` or `meridian spawn show SPAWN_ID`.
