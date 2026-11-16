# meridian-base

The agents and skills every Meridian project gets: spawning and delegation, work
tracking, the knowledge layers (`AGENTS.md`, `.context/`, the KB) and the agents that
keep them, plus the model aliases in `mars.toml`. meridian-dev-workflow and
creative-writing-skills depend on it and bundle it into their plugins. Codex and
OpenCode plugin users get its skills but no agents, so an `@agent` a skill names
doesn't resolve for them (meridian-dev-workflow's `AGENTS.md`).

## Model Aliases

Define an alias with the bare canonical model ID and no `provider`, and let Mars
resolve the runnable provider through harness discovery. Set `provider` only when two
providers serve the same model ID and Mars picks the wrong one.

```toml
[models.kimi]
harness = "opencode"
model = "kimi-k3"
```

After changing a `[models.*]` entry, run `uv run scripts/models_table.py` to
regenerate the README model table; `--check` fails when it is stale.

## Watching

- **`/handoff` starts a lead beside the sender.** On the next handoffs: the
  sender keeps to what stays with it and leaves handed-over work to the new
  lead; a lead on separate work starts its own work item before writing; a
  session moving its own work stops once the user starts the new one.
- **The KB records why (`/knowledge-layers` The KB Records Why).** On the
  next kb-lead captures: pages state the behavior with its reason, carry no
  decision IDs or bare rejected-option lists, and options the human floated
  stay in the work directory; kb-lead opens the passages session-miner
  points to rather than working from its notes. On the next run where the
  human asks against a recorded choice: the agent says once what the record
  says, then does what was asked (`/intent-modeling`), without demanding
  evidence first.
- **Leads read for themselves; explorers find (`/zoom-out`,
  `/explore-and-engage`, `explorer`).** On the next runs that orient or
  plan: the agent reads the docs along the path itself, and in a large
  area spawns explorers to find what's related, each in its own area, then
  reads what they point to. Watch for explorers spawned on a small area,
  and for agents that work from an explorer's summary without opening the
  files.
- **Questions grouped by branch (`/explore-and-engage` Asking the Human,
  `/work-artifacts`).** On the next lead runs that ask the human several
  questions, grilling or not: they sit under a heading per decision branch,
  each with background the human can answer from cold and a recommended
  answer, no internal IDs; questions that hang on an open answer wait;
  facts are looked up, not asked; a conversational question stays in chat. On the next grilling: it zooms out
  first and stops when no decision is open.
- **The work directory stays current (`/work-artifacts`).** On the next
  long lead runs: the state says where things stand now, finished and
  answered items leave it, and each decision carries its reason. Watch for
  append-only logs.
- **The human's ideas are weighed (`/intent-modeling`).** On the next run
  where the human floats an idea: the agent gives its gains, costs and
  what it simplifies and recommends, instead of recording it bare; for
  Jimmy it then acts on the recommendation where his instructions let it.
  Relayed to a lead, the idea is marked as his idea, not a decision.
- **Recorded choices read as tradeoffs (`/knowledge-layers` Every Choice
  Is a Tradeoff).** On the next runs that write `AGENTS.md`, `.context/` or
  KB pages: no "invariant" sections, no must/never rules the human didn't
  say, each choice with its reason and cost; agents that meet a recorded
  choice whose reason no longer holds change it and report, instead of
  asking. Watch for the opposite failure: a human's product decision
  dropped on an agent's own judgment.
- **`/handoff` ends with a launch command.** On the next handoffs, muse's
  included: the agent reads Meridian's handoff launch guidance and prints
  the full command (`-C`, `-a`, `--prompt-file`, `--from`, and `--work` or
  `--task-dir` where they apply), not only the brief's path.
- **session-miner quotes (`session-miner`).** On the next mining: each
  passage comes as the human's verbatim words with a cursor that opens it
  in one step, and the caller still opens the passages it relies on. On a
  run without Meridian: it finds the harness's transcript files and gives
  file and line.
- **kb-lead deletes what a change made stale (`resources/capture.md`).** On
  the next captures: it searches for old names too, deletes or rewrites
  pages the code now contradicts, keeps a chosen direction that isn't built
  yet, marked so, reorganizes the pages it touched, and its report leads
  with deletions. One `@cold-reader` reads all the new prose.
