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
- **`/grill` walks clusters.** On the next grilling: it zooms out to what
  the plan is for, then asks one cluster of related decisions at a time,
  each with a recommended answer, looks up facts itself, and stops when no
  decision is open.
- **kb-lead deletes what a change made stale (`resources/capture.md`).** On
  the next captures: it searches for old names too, deletes or rewrites
  pages the code now contradicts, keeps a chosen direction that isn't built
  yet, marked so, reorganizes the pages it touched, and its report leads
  with deletions. One `@cold-reader` reads all the new prose.
