---
name: meridian-spawn
type: reference
description: >
  Use whenever you need to delegate work to another agent, run tasks in
  parallel, coordinate multiple agents, or inspect spawn outputs. Also
  use when routing work to a specific model or provider.
model-invocable: false
---

# meridian-spawn

## Prompt Passing

Write spawn prompts to files. Use `--prompt-file` for delegation.

Write prompt files to the system temp directory with descriptive names. Get the temp dir path with:

```bash
uv run python -c "import tempfile; print(tempfile.gettempdir())"
```

Use descriptive absolute paths: `<tmpdir>/coder-auth.md`, `<tmpdir>/reviewer-structural.md`.

Shell quoting mutates prompts before meridian receives them, backticks become command substitutions, `$variables` expand, quotes nest wrong, and multiline formatting collapses. Prompt files preserve exact text and make handoffs inspectable.

Always use `--prompt-file`. Even trivial inline strings get written to a prompt file first.

## Core Loop

Spawns block by default. Use `--bg` to return immediately with a spawn ID, then `wait` to block until completion:

```bash
meridian spawn -a coder --prompt-file step-a.md --bg  # -> p101
meridian spawn -a coder --prompt-file step-b.md --bg  # -> p102
meridian spawn wait                                    # blocks until both complete
```

### Output Discipline

Parse `spawn_id` and `status` from JSON responses in agent mode. Some commands return JSON for complex data, others return text — check per-command. Run `meridian <command> -h` for format details.

### Spawn Lifecycle

Spawns transition `queued` -> `running` -> `finalizing` -> `succeeded | failed | cancelled`. `finalizing` is transient — treat it as active when polling. `spawn wait` blocks through `finalizing` and returns only on a terminal state.

### Crash-Only Design

Writes are atomic (tmp+rename), reads tolerate truncation. Recovery is startup behavior. If a spawn dies mid-flight, `meridian doctor` or read-path reconciliation detects and reports it.

## Spawning

**`-a` (agent profile)** — use when a profile exists for the role:

```bash
meridian spawn -a reviewer --prompt-file review-task.md --bg
```

**`-m` (direct model)** — use for one-off tasks where no profile fits:

```bash
meridian spawn -m MODEL --prompt-file task.md --bg
```

Pass reference files or directories with `-f` so the spawned agent starts with context. Use `-f` for material that must be available at launch, not for everything that might become relevant.

Prefer folder references over file bundles. A folder reference is an orientation scope: it tells the agent where to work and lets the agent inspect exact files as needed. Folder references should not imply every file belongs in the prompt.

Most harnesses auto-load local instruction files such as `AGENTS.md` or equivalent when an agent works in a directory. Rely on that for directory orientation instead of passing `AGENTS.md` with `-f`. Point the handoff at the target folder; pass `.context/CONTEXT.md` only when contracts or rationale are needed up front.

Normal handoff shape: one folder plus zero or one source-of-truth file, such as requirements, a design note, or an issue brief. Multiple file references need a clear reason because file references may be inlined and drain context. If you need several source files, write a focused note or pass the folder and let the agent read selectively.

```bash
meridian spawn -a coder --prompt-file implement-auth.md --bg \
  -f src/middleware/ -f design/phase-2.md
```

Pass prior conversation history with `--from` when the spawn needs reasoning that isn't materialized to files. `--from <spawn-id>` pulls a specific prior spawn's transcript. `--from $MERIDIAN_CHAT_ID` pulls the top-level primary session — available at any depth because `$MERIDIAN_CHAT_ID` is inherited by every descendant.

Run `meridian mars models list` for available models. Run `meridian mars list` for agent profiles and skills. Model preferences belong in agent profiles or `meridian config`, not hardcoded in spawn commands.

## Completion Goals

`--goal` injects a completion contract into the spawned agent's context. The agent evaluates it as a stopping condition — work until met, report blockers if stuck.

```bash
meridian spawn -a coder --prompt-file impl.md --bg \
  --goal "All auth middleware tests pass and no type errors"
```

The prompt describes the work. The goal defines the exit condition. Write goals as verifiable states: "Auth module uses the adapter pattern, existing tests pass" — something the agent can check. "Refactor the auth module" belongs in the prompt.

Goals are persisted as spawn metadata and visible in `meridian spawn show`.

## Work Items

Attach spawns to a work item with `--work` so they're grouped and traceable. For work item lifecycle, see the `/meridian-work-coordination` skill.

## Parallel Spawns

Use `--bg` to launch without blocking, then `wait` to collect all results in one notification:

```bash
meridian spawn -a coder --prompt-file auth.md --bg \
  --goal "Auth middleware passes all tests"
meridian spawn -a coder --prompt-file cache.md --bg \
  --goal "Cache layer passes all tests"
meridian spawn wait   # one notification when ALL complete
```

Every `--bg` spawn must be drained with `meridian spawn wait` before you respond to the user, start dependent work, or end your turn. Background spawns that aren't waited on are invisible — their results are lost and their failures go unnoticed.

`spawn wait` is harness-aware — it yields at the right interval to preserve your prompt cache. When a wait yields, call `meridian spawn wait` again immediately to re-enter the wait. Act on results when it returns a terminal state.

## Checking Status

Use the work dashboard for situational awareness:

```bash
meridian work
```

Reattach to spawns from a previous session with `meridian spawn wait` or `meridian spawn wait <spawn_id>`. Use `meridian spawn children <id>` to see what a spawn spawned.

## Steering a Running Spawn

Inject course-corrects a spawn's current task — wrong approach, missed
constraint, clarified requirement. The message lands as a user turn
mid-session, so the agent will pivot to it. New scope belongs in a
separate spawn or issue.

```bash
meridian spawn inject p107 --message "Use the existing adapter pattern in src/adapters/"
```

## When a Spawn Fails

Read the report via `meridian spawn show SPAWN_ID`. For deeper investigation, run `meridian doctor` or check `meridian spawn show` for log paths.

## Reading Transcripts

Use `meridian session log` to read a session's conversation transcript — spawns, prior sessions, or the current primary session:

```bash
meridian session log p107                       # last 5 interaction entries, safe previews
meridian session log p107 --tail 20             # last 20 entries
meridian session log p107 --from 0 --limit 1    # segment setup slot (entry 0)
meridian session log p107 --around 120 --context 10
meridian session log p107 --from 120 --limit 30
meridian session log p107 --segment previous    # switch to previous segment
meridian session log p107 --full                # full current segment incl. entry 0
meridian session log p107 --full --no-truncate  # plus full content of each entry
meridian session log p107 --global --around 240 --context 8   # flat ordinals across segments
meridian session log $MERIDIAN_CHAT_ID          # primary session transcript
```

`meridian spawn show` gives the structured report; `meridian session log` gives the transcript. Bare `session log REF` is a safe recent read: last 5 interaction entries from the current (last) segment, oldest-to-newest, with oversized content preview-truncated.

Navigation is **segment-local by default**: `--from/--before/--around` are ordinals inside the selected segment, and the selected segment is the current one unless `--segment previous|current|N` says otherwise. Entry `0` of any segment is its setup slot (prologue/handoff); reach it with `--from 0 --limit 1`. `--full` expands the selected segment (including entry 0); `--no-truncate` returns full per-entry content. Windows that touch segment edges include `Previous segment:` / `Next segment:` hints with the deterministic command to cross.

Use `--global` only when you need one flat stream across all segments (every segment's entry 0 included, with unique global ordinals starting at 0). `--global` conflicts with `--segment` and requires `--from/--before/--around`. Prefer segment-local commands for stable navigation across compactions.

Search the transcript without reading the whole thing:

```bash
meridian session search "auth middleware" p107
meridian session search "timeout" --workspace          # current project + workspace roots
meridian session search "report" --work feature/api    # sessions on a work item
```

Each match prints a deterministic `Open:` command: entry-0 hits open with `--segment N --from 0 --limit 1`, interaction hits with `--segment N --around K --context 5`. Run the printed command directly instead of guessing flags.

## Shared Filesystem

Spawns share filesystem directories for exchanging data. Context directories (`$MERIDIAN_CONTEXT_*_DIR`) are injected into every agent's system prompt at launch.

See the `/meridian-work-coordination` skill for when to use which.

## Committing Spawn Changes

Use `meridian spawn files` to stage exactly what a spawn changed:

```bash
meridian spawn files p107 | xargs git add
meridian spawn files p107 -0 | xargs -0 git add   # paths with spaces
```

## Template Variables

Use `{{KEY}}` placeholders in prompts, replaced at launch time with `--prompt-var`:

```bash
meridian spawn -a coder --prompt-file task.md --bg \
  --prompt-var TASK=auth-refactor \
  --prompt-var CONSTRAINT="no direct DB access"
```

Where `task.md` contains `{{TASK}}` and `{{CONSTRAINT}}` placeholders — they're replaced at launch time.

## Beyond the Basics

For continue/fork, cancel, stats, permission tiers, reports, and dry-run, see [`resources/advanced-commands.md`](resources/advanced-commands.md).
For troubleshooting, run `meridian doctor --help` and `meridian spawn show SPAWN_ID`.
For project defaults, run `meridian config show` or `meridian config --help`.

**If you launched any `--bg` spawns, run `meridian spawn wait` before responding to the user.**
