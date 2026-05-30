---
name: meridian-spawn
type: reference
description: Use when delegating work to subagents — spawn flags, prompt passing, parallel coordination, output inspection.
model-invocable: true
---

# meridian-spawn

Delegate work by spawning subagents. This is the core loop; deeper commands live in [`resources/advanced-commands.md`](resources/advanced-commands.md).

## Prompt Passing

Always use `--prompt-file`, never inline strings — even trivial ones. Shell quoting mutates prompts before meridian sees them: backticks become command substitutions, `$variables` expand, quotes nest wrong, multiline collapses. Prompt files preserve exact text and make handoffs inspectable.

Write prompt files to the system temp dir with descriptive absolute paths (`<tmpdir>/coder-auth.md`). Get the temp dir with `uv run python -c "import tempfile; print(tempfile.gettempdir())"`.

## Core Loop

Spawns block by default. Use `--bg` to return immediately with a spawn ID, then `wait` to block until completion:

```bash
meridian spawn -a coder --prompt-file step-a.md --bg   # -> p101
meridian spawn -a coder --prompt-file step-b.md --bg   # -> p102
meridian spawn wait                                     # blocks until ALL complete
```

**Every `--bg` spawn must be drained with `meridian spawn wait` before you respond to the user, start dependent work, or end your turn.** Un-waited background spawns are invisible — their results are lost and their failures go unnoticed.

`spawn wait` is harness-aware: it yields at intervals to preserve your prompt cache. When it yields, call `meridian spawn wait` again immediately; act on results only on a terminal state. Spawns transition `queued → running → finalizing → succeeded | failed | cancelled` — treat `finalizing` as active when polling.

## Spawning

Use **`-a <profile>`** when a profile fits the role; **`-m <model>`** for one-off tasks where none does:

```bash
meridian spawn -a reviewer --prompt-file review.md --bg
meridian spawn -m MODEL --prompt-file task.md --bg
```

Pass launch context with `-f`. **Prefer a folder reference over a file bundle** — a folder tells the agent where to work and lets it read exact files as needed; it does not imply every file belongs in the prompt. Normal shape: one folder plus zero or one source-of-truth file (requirements, a design note, an issue brief). Multiple `-f` files need a reason — references may be inlined and drain context.

```bash
meridian spawn -a coder --prompt-file implement-auth.md --bg \
  -f src/middleware/ -f design/phase-2.md
```

Most harnesses auto-load `AGENTS.md` / `.context/CONTEXT.md` when an agent works in a directory — rely on that instead of passing them with `-f`.

Pass prior reasoning that isn't materialized to files with `--from`: `--from <spawn-id>` for a specific spawn's transcript, `--from $MERIDIAN_CHAT_ID` for the top-level primary session (inherited at any depth).

Run `meridian mars list` for profiles and skills, `meridian mars models list` for the model catalog. Model preferences belong in profiles or `meridian config`, not hardcoded in spawn commands.

## Completion Goals

`--goal` injects a completion contract — the agent works until it's met, reports blockers if stuck. Write goals as verifiable states, not tasks:

```bash
meridian spawn -a coder --prompt-file impl.md --bg \
  --goal "Auth middleware tests pass and no type errors"
```

The prompt describes the work; the goal defines the exit condition. Goals are visible in `meridian spawn show`.

## Parallel Spawns

Launch several with `--bg`, then a single `wait` collects all results in one notification:

```bash
meridian spawn -a coder --prompt-file auth.md --bg --goal "Auth middleware passes all tests"
meridian spawn -a coder --prompt-file cache.md --bg --goal "Cache layer passes all tests"
meridian spawn wait
```

Launch with a clear goal, then move on — don't poll with repeated `session log` / `spawn show`, which burns context on supervision instead of work. Wait on all in-flight spawns, or do your own work in parallel.

## Status, Work Items, Shared State

- `meridian work` — situational dashboard. Reattach to earlier spawns with `meridian spawn wait [<id>]`; `meridian spawn children <id>` shows what a spawn spawned.
- Attach spawns to a work item with `--work` so they're grouped and traceable — see `/work-artifacts`.
- Spawns share filesystem context dirs (`$MERIDIAN_CONTEXT_*_DIR`), injected into every agent's prompt at launch.

## Beyond the Core Loop

See [`resources/advanced-commands.md`](resources/advanced-commands.md) for:

- **Reading transcripts** — `meridian session log` / `session search` navigation (also `/session-mining`)
- **Steering** a running spawn — `meridian spawn inject`
- **Continue / fork**, cancel, stats, dry-run, permission tiers
- **Committing** spawn changes — `meridian spawn files`
- **Template variables** — `--prompt-var`
- **When a spawn fails** — `meridian spawn show`, `meridian doctor`

**If you launched any `--bg` spawns, run `meridian spawn wait` before responding to the user.**
