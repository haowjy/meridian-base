# Changelog

Be brief. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versioning: [SemVer](https://semver.org/). Versions before 0.0.13 in git history only.

## [Unreleased]

### Changed
- **Breaking:** Migrated hook manifests to mars-agents' native-passthrough
  schema, requiring mars-agents >= 0.11.0.
  `context-autosync` now runs on Claude `SubagentStop` as well as `SessionEnd`.

## [0.8.9] - 2026-07-24

### Added
- `context-autosync` hook (`.claude`, session end): pushes stranded context-repo
  commits (work docs, KB) when a Claude session ends. Closes the gap where
  commits made after the last meridian lifecycle event — e.g. kb-lead knowledge
  capture as a session's final act — sat unpushed until the next spawn. No-op
  unless the project configures `git-autosync` in meridian.toml; `meridian hooks
  list` is the runtime authority. Requires mars-agents ≥ the session.end→
  SessionEnd fix (mars-agents#129) to compile to a live event.

## [0.8.8] - 2026-07-17

## [0.8.7] - 2026-07-14

### Added
- `/qi-maintenance`: compact guardrail for durable source editors — keep colocated current-truth docs synchronized in the same branch, update only when a cold agent would otherwise be misled, and defer substantial writing craft to `/qi-layer`.

### Changed
- `kb-lead`: every settled-phase capture now reconciles changed source areas against their nearest `AGENTS.md` and current-truth `.context/` docs, repairing omissions left by implementation before cross-cutting KB capture.
- `/knowledge-layers`: directory-scoped must-do and nice-to-have deferrals route to colocated `.context/TODO` and `.context/FUTURE`; cross-cutting or externally visible work routes to the project issue tracker.
- `/qi-layer`: ambient synchronization responsibility moved to `/qi-maintenance`; this skill remains the detailed writing and structure reference.

## [0.8.6] - 2026-07-11

## [0.8.5] - 2026-07-11

## [0.8.4] - 2026-07-10

## [0.8.3] - 2026-07-10

## [0.8.2] - 2026-07-10

### Changed
- `/qi-layer`: AGENTS.md framed as a prompt — minimal, every line load-bearing; think-vs-lookup test gains a delete branch; pair scope widened to any tree agents work in (code, KB, docs, work dirs); description retargeted to writing/maintaining intent docs; line floor dropped; nested AGENTS.md composes with ancestors. New CLAUDE.md Mirrors section owns `meridian qi claude-md-fix`: mirrors are `@AGENTS.md`, divergence is a deliberate visible conflict, root vs nested loading spelled out.
- `/knowledge-layers`: placement sharpened — intent test precedes the `.context/` scope test, subsystem-dependent knowledge stays colocated even when conceptual, KB takes big-picture code-agnostic knowledge. Truth anchored per layer: colocated docs describe their checkout and ride its branch; KB records settled intent (what the system should be) merged or not; `docs/` describes shipped behavior. Current Truth scoped to durable layers; deletion is the content-truth owner's call. KB tree itself follows `/qi-layer`; bootstrap template split into intent AGENTS.md + `.context/CONTEXT.md`.
- `/work-artifacts`: work directories carry an AGENTS.md per `/qi-layer` to orient arriving spawns (goal, artifact layout, settled vs moving); `.context/` only if depth accumulates.
- `kb-lead`: human decisions are authoritative intent, not implementation — anchor per `/knowledge-layers`, flag unconverged code; caller-facing description (when to spawn, what to pass, what comes back); `composer` fallback replaced with `terra` at high.
- `kb-maintainer`: caller-facing description (target, operations, result shape); duplicated `claude-md-fix` instruction removed — `/qi-layer`, loaded by both KB agents, owns the mirror workflow; no-target default (project KB) must be named in the report; `composer` fallback removed.

## [0.8.1] - 2026-07-09

### Added
- Pinned `sol`, `terra`, and `luna` aliases for GPT-5.6.

### Changed
- Removed the obsolete `sonnet46` alias.
- The pinned GPT-5.6 aliases and temporary `gpt55` redirect share the same outcome-first prompting guidance.
- `gpt55` temporarily redirects to `gpt-5.6-sol` while remaining references migrate to `sol`.
- `explorer` now defaults to `luna`; its existing fallback set remains available while Luna quality is evaluated.
- `subagent` now defaults to `sol` at `xhigh`, adds `terra` and `luna` at `xhigh` as its first fallbacks, and removes GPT Mini.
- KB Lead replaces its GPT-5.5 fallback with `sol` at `xhigh`; Explorer drops its GPT-5.3 Codex Spark fallback while retaining GPT-5.4 Mini.
- KB Maintainer and Session Miner now default to `terra` at `medium` and remove their GPT-5.4 Mini fallbacks.

## [0.8.0] - 2026-07-09

### Added
- `mars.toml`: pinned `sonnet46` and `sonnet5` model aliases alongside the catch-all.
- `/work-artifacts`: `DIVERGENCE/` convention (orchestrator logs plan shifts; reviewers and knowledge capture consume) and task_dir check/rebind mechanics.

### Changed
- `kb-lead`: source-generic orient step (caller-passed sources, work directory logs, conversations behind them), mid-work invocation (capture what settled, leave what is moving), verification deferred to `/md-validation`, and Current Truth Over History named as its core discipline.
- `/knowledge-layers`: Current Truth Over History promoted to a layer-wide section — deletion needs no replacement, git history is the archive (commit untracked files before deleting).
- `kb-maintainer`: prunes structural dead weight (empty stubs, orphaned pages, empty indexes); content staleness stays flagged for the caller.
- `/grill-with-docs` is model-invocable so agents instructed to use it can self-load it.
- `/information-hierarchy`: diagram-first guidance defers validation mechanics to `/md-validation`.
- Subagent profile retunes (explorer, session-miner, subagent).

## [0.7.41] - 2026-07-06

### Added
- Codex hook that denies interactive-prone auth commands unless they include a noninteractive fail-fast guard.

## [0.7.40] - 2026-07-05

### Changed
- Deleted `gpt54`.

## [0.7.39] - 2026-07-04

### Changed
- Remove em dashes across all skills and agents.

## [0.7.38] - 2026-07-04

### Changed
- `@kb-lead`: merge redundant canonical/write-inline blocks, add information-hierarchy, add composer/gpt-5.4-mini/deepseekflash to model-policies, trim capture loop. Enforce delete-or-archive; live content never references archived content.
- `@kb-maintainer`: add information-hierarchy, trim body from ~100 to ~40 lines. Remove gpt-5.3-codex-spark and glm from model-policies.
- `knowledge-layers`: Wiki Page Conventions collapsed to follow `/information-hierarchy`. Deduplicate Operations (removed from bootstrap). Drop Log content type. Replace `trash/` with `archive/` (.kgignore'd); live content never references archived content.

## [0.7.37] - 2026-07-04

### Added
- `@subagent` agent: general-purpose subagent for any task. Supports all catalog models, ranked by subagent usefulness (gpt55 default, opus46, gpt54, glm, deepseek, composer, deepseekflash, gptmini).

## [0.7.36] - 2026-07-03

### Added
- `information-hierarchy` skill (principle, model-invocable): pick modality and disclosure tier (answer / depth / sources) per beat for large human-facing output.

### Changed
- `interactive-artifact` renamed to `structured-artifact` and reframed as the static-HTML build mechanism (single or multi-page); loads `/information-hierarchy` first. New `resources/multi-page-site.md` and `resources/mockups.md`; `explorable-diagram.md` renamed to `diagrams.md`; `layout-and-theme.md` rewritten mobile-first with Tailwind v4 browser build, highlight.js, and vendoring guidance for offline use.
- `structured-artifact` enrichment resources lead with plain-DOM thresholds before libraries; CDN snippets pinned to major versions only — skill body owns freshness checks and browser verification at build time.
- `llm-writing` loads `/information-hierarchy` and checks disclosure tiers during revision.

## [0.7.35] - 2026-07-03

### Changed
- `@kb-lead` can run `meridian qi` and now runs `meridian qi claude-md-fix <code-tree>` after adding or moving `AGENTS.md` files so Claude mirrors stay current.
- `@kb-maintainer` now loads `qi-layer` and runs the same mirror repair after structural changes involving code-local `AGENTS.md`.

## [0.7.34] - 2026-06-29

- Add `goal-writing` skill for writing executable agent goals with evidence, anti-goals, stop conditions, and reviewer gates.

## [0.7.33] - 2026-06-29

## [0.7.32] - 2026-06-28

### Changed
- Backfilled the missing `0.7.31` changelog entry after an empty release cut.

## [0.7.31] - 2026-06-28

### Changed
- `grill-with-evidence`: when external grounding is needed, search the web directly instead of assuming a separate `@web-researcher` agent exists.

## [0.7.30] - 2026-06-28

### Changed
- `grill-with-evidence`: when external grounding is needed, search the web directly instead of assuming a separate `@web-researcher` agent exists.

## [0.7.29] - 2026-06-28

### Added
- `grill`: compact interactive grilling skill for stress-testing a plan or direction branch by branch with the human.
- `grill-with-evidence`: grounding overlay for `/grill` that routes evidence gathering across project artifacts, code in the wild, official docs, research, articles, first-hand accounts, and bounded `@explorer` / `@web-researcher` / `@session-miner` spawns.

### Changed
- `grill-with-docs`: reduced to a docs-first overlay for `/grill`; loads `/knowledge-layers`, checks project artifacts and vocabulary first, and uses bounded explorer/session-miner spawns instead of duplicating the full grilling method.

## [0.7.28] - 2026-06-28

### Changed
- `llm-writing`: tightened as a generic writing guardrail for human-facing text, focused on reader context, deliberate wording, and removing default LLM phrasing.

## [0.7.27] - 2026-06-27

### Changed
- `knowledge-layers`: align KB guidance with project-local KB `AGENTS.md`, current-truth exceptions for decision records, established vocabulary filenames, and log-only-for-major-changes convention.
- Model prompting metadata trimmed to actionable guidance; `gpt55` now emphasizes outcome-first handoffs with success criteria, high-level context, and concrete verification evidence.

### Removed
- `sonnet` model alias and low-value prompting notes that repeated model descriptions or capability tiers.

## [0.7.26] - 2026-06-19

### Changed
- `intent-modeling`: positively reframed — direct guidance ("Read for the outcome", "Match depth and shape") replaces contrastive negatives.
- `@kb-lead`: description reworded to natural sentence (drops `/post-impl-capture` reference). Body trimmed: shorter intro, tighter capture loop, Orient step gains "after shipped work" diff-intent-against-outcome guidance. Dropped `reflection` from load.
- `@kb-maintainer`: body trimmed — structural refactoring and content health sections rewritten shorter. Dropped `reflection` from load.
- `@explorer`: body trimmed — shorter Flag Contradictions, shorter Scope and Report. Description reworded to natural sentence.
- `@session-miner`: trimmed report convention line.
- `handoff` skill: removed over-explanation in launch command section.

### Added
- `reflect` skill: user-invoked pause before reporting (`model-invocable: false`). Loads `/intent-modeling`, points to `/knowledge-layers` and `/qi-layer` for carry-forward. Replaces always-loaded `reflection`.

### Removed
- `clear-mind` skill deleted. Handoff doctrine (agent selection, handoff craft) moves to `meridian spawn -h` in meridian-cli.
- `reflection` skill deleted. Zero invocations observed globally; always-loaded generic checklist added tokens without changing outcomes. Optional user pause via new `/reflect`.

## [0.7.25] - 2026-06-19

### Changed
- `deny-generic-agent` hook: captures blocked Agent() prompt to `/tmp/meridian-<pid>/`, returns ready-to-run `meridian spawn -a <agent> --prompt-file <path> --bg` command with available agent list.

## [0.7.24] - 2026-06-19

### Changed
- `qi-layer`: deduplicated with `knowledge-layers` — qi-layer now owns the craft of writing AGENTS.md/.context/ (four principles, contents, structural rules, what doesn't belong). Adds every-session test, think-vs-lookup test, and session bleed detection. Loads `/llm-writing`. Removed LLM writing tells (negation lists, restated explanations).
- `knowledge-layers`: owns routing across all 5 layers and KB conventions only. Drops redundant AGENTS.md/.context/ definitions (qi-layer owns those).

## [0.7.23] - 2026-06-17

### Changed
- `@explorer`: AGENTS.md is now the non-negotiable first read (was `.context/`). `.context/` is optional. New "Flag Contradictions" section: explorer must call out when raw source files contradict AGENTS.md or `.context/` claims.

## [0.7.22] - 2026-06-17

### Added
- `interactive-artifact` skill: mechanism for building self-contained interactive HTML artifacts. Mermaid by default, click-to-detail panel, responsive/mobile (pinch-zoom, bottom-sheet detail), theme-agnostic. Resources: `html-patterns.md` (CDN stack, Mermaid config, click callbacks, pan/zoom, mobile, Tailscale serve), `experimental-react-flow.md` (React Flow CDN alternative for custom node rendering).

### Removed
- `meridian-spawn` skill deleted. Spawn doctrine now lives in meridian itself — system prompt injects a spawn contract + discovery pointers, and `meridian spawn -h` is the on-demand reference. Removed `meridian-spawn` from `@kb-lead` and `@kb-maintainer` `available:` lists, from the `/clear-mind` cross-reference (now points at `meridian spawn -h`), and from the README skills table.
- `@kb-lead`: dropped "Run `meridian -h` for CLI reference" prose line.

## [0.7.21] - 2026-06-14

### Changed
- Renamed `kb-conventions` skill to `knowledge-layers`. Scope expanded to cover all documentation layers (`AGENTS.md`, `.context/`, KB, `docs/`, work directories); KB page conventions and operations remain. `knowledge-layers` loads `/qi-layer`.
- `qi-layer`: description and tone sharpened — AGENTS.md must be read first, must not duplicate `.context/`, must stay 50–200 lines; points to `/knowledge-layers` for the full layer map.
- `explorer`: description and body made more directive; `.context/` first is non-negotiable; callers must spawn it for any multi-file exploration.
- `grill-with-docs`, `shared-dao`, `zoom-out` now load `/qi-layer`.
- `kb-lead` and `kb-maintainer` agents load `knowledge-layers` and reference `/knowledge-layers`.

## [0.7.20] - 2026-06-14

### Removed
- `meridian-default-orchestrator` and `meridian-subagent`: the generic "default" orchestrator and subagent profiles are removed. Real work routes through specialized agents (tech-lead, product-lead, design-lead, etc.); the minimal generic defaults were unused and the orchestrator carried no `subagents` roster, so under capability-gated spawn injection it would ship without an agent inventory anyway.

## [0.7.19] - 2026-06-13

### Fixed
- All agents: remove invalid `tools:` deny rules (`cron`, `notifications`, `plan_mode`, `worktree`) — no matching tools in harness.

## [0.7.18] - 2026-06-12

## [0.7.17] - 2026-06-12

### Fixed
- intent-modeling: quote description to fix YAML colon parsing error

## [0.7.16] - 2026-06-12

### Changed
- explorer, kb-maintainer, session-miner: add composer model alias for cursor-based harnesses
- session-miner: add approval: never (read-only operations need explicit approval mode)
- intent-modeling: refine body for clarity, replace dash in description with colon
- llm-writing: positive reframing of Behavioral Pulls introduction

## [0.7.15] - 2026-06-10

## [0.7.14] - 2026-06-07

### Changed
- Handoff skill: add `--task-dir` to primary launch command template for worktree/sibling-repo handoffs.

## [0.7.13] - 2026-06-07

### Changed
- Handoff skill: lead with `/intent-modeling` before writing the transition brief — capture what the human actually wants, not just implementation details.
- Handoff skill: human intent is now the first item in the brief, not buried in the middle.
- Handoff skill: replaced ALL CAPS negative closing with positive framing.

## [0.7.12] - 2026-06-07

## [0.7.11] - 2026-06-07

## [0.7.10] - 2026-06-07

## [0.7.9] - 2026-06-07

### Added
- `deny-generic-agent` PreToolUse hook: blocks generic `Agent(subagent_type: "claude")` spawns, forcing use of named agents or meridian spawn.

## [0.7.8] - 2026-06-07

### Changed
- `kb-conventions`: add lifecycle operations (Ingest, Maintain, Lint) to SKILL.md and bootstrap. Reframe five layers as four content types (wiki pages, decision records, sources, log). Add starter AGENTS.md template. Cut LLM writing patterns (labeled conclusions, escape hatches).

## [0.7.7] - 2026-06-07

### Changed
- `kb-conventions` skill: replace five-layer taxonomy with clear "what the KB is" framing and `.context/` vs KB vs `docs/` placement table. Layer structure now project-defined via KB AGENTS.md. Add `resources/bootstrap.md` starter template.

## [0.7.6] - 2026-06-07

### Changed
- `kb-conventions` skill: clarify what the KB is and where it sits (missing changelog from rushed release).

## [0.7.5] - 2026-06-07

### Changed
- `meridian-spawn` skill: replace incorrect `-C "$MERIDIAN_TASK_DIR"` / `mars sync` guidance with `--task-dir` flag usage — spawned agents don't run mars sync, and `-C` changes project root, not task dir.

## [0.7.4] - 2026-06-05

## [0.7.3] - 2026-05-31
### Added
- `@kb-lead` — generic documentation-capture agent (moved from meridian-dev-workflow). Mines the work via `@explorer`/`@session-miner` read-only investigators, reconciles against the human's canonical decisions, writes `.context/` + KB + `docs/` inline, and hands structure to `@kb-maintainer`. Dev-specific behavior layers on via `--skills` (e.g. `post-impl-capture`).

### Changed
- `@kb-maintainer`: scope broadened to any documentation tree (KB, `.context/`, `docs/`, work-item `design/`), not just the KB — generic structural health (split/merge/rename/folders/cross-refs). qi-layer semantic placement (AGENTS.md ↔ `.context/`) stays the writer's job; kb-maintainer flags layer-misplaced content for the caller. Added `/llm-writing` reminder for the prose it rewrites. Content authority fully removed — detects and flags contradictions/staleness/superseded knowledge but never resolves which claim is true or moves history out of the live tree (that needs the canonical context `@kb-lead` holds). git merge handling reconciles non-semantic structure only; contradictory claims get flagged, not won on recency. Description states: pass exactly one writable tree. git perms narrowed from `bash(git *)` to read-only + structural (`status`/`diff`/`log`/`show`/`mv`/`rm`) — no commit/push/merge/rebase, since it doesn't own commits.
- `@kb-lead`: investigator widening hard-capped at three waves (widen only when an area can change a doc target, then report uncovered). Commits each repo it touched — KB is a separate repo from the code tree's `.context/`/`docs/` — never destructive git, pushing left to the caller. Spawns one `@kb-maintainer` per writable tree (it takes one target per spawn) and resolves the content contradictions it flags. Description teaches the launch contract: pass the originating conversation or source artifacts, `/post-impl-capture` for shipped work. Concrete validation commands (`meridian kg check kb`, `meridian kg graph kb`, `meridian mermaid check <path>`). Keeps the house-default destructive-git denylist (branch-switch + uncommitted-work destruction); commits via `bash`/`git` under the broad posture it owns.

### Removed
- `@kb-writer` agent — KB writing folded into `@kb-lead`, which now writes the KB inline.

## [0.7.1] - 2026-05-30

### Changed
- `meridian-spawn`: warn that `MERIDIAN_PROJECT_DIR` anchors Meridian commands inside managed sessions; use `meridian -C "$MERIDIAN_TASK_DIR" ...` for task checkouts.

## [0.7.0] - 2026-05-30

### Added
- `/handoff` skill — conversation compaction into handoff doc, spawn command for the next agent. `user-invocable: true`, `model-invocable: true`.
- `/explore-and-engage` skill — orientation pattern for cold-start agents.
- `/zoom-out` skill — 4-angle orientation (code, KB, decisions, vocabulary).
- `/work-artifacts` skill — anchors work in work items, artifact placement, decision recording. Combined from `work-tracking` + `meridian-work-coordination`. Progressive: `resources/lifecycle.md` for detailed status management.

### Changed
- All skill descriptions trimmed to one-line "when + what" format. Removed `detail` field from all skills.
- `clear-mind`: added "Own the outcome" from merged `delegation`. `model-invocable: false` (loaded on 6 agents, never available).
- `shared-dao`: trimmed from 123 → 43 lines. Cut vocab file hierarchy, lifecycle stages, operations.
- `llm-writing`: description now explains what it catches. Trimmed 40 → 28 lines; renamed "Conversational Mode Leaking" → "Conversational Bleed".
- `intent-modeling`: trimmed 27 → 17 lines. Cut illustrative examples, kept core instruction.
- `kb-conventions`: replaced inline validation commands with `/md-validation` reference.
- `handoff`: `user-invocable: true` (body shows `/handoff` syntax). Softened `pre-*` checkpoint reference to "if installed."
- `@kb-writer`: added `read` and `rg` tools (was missing read access). Moved `kb-conventions` from available → load.
- `@kb-maintainer`: moved `kb-conventions` from available → load.
- `@session-miner`: moved `session-mining` from available → load.
- Fixed corrupted body content in `meridian-privilege-escalation`, `qi-layer`, `md-validation` (stale `detail:` lines leaked into body text).
- mars.toml model descriptions: fixed conversational bleed, typos, and missing personality differentiation across opus46/47/48, deepseek/deepseekflash. Descriptions now capture model strengths positively.

### Removed
- `agent-management` — unreferenced by any agent. Covered by `clear-mind` guardrail.
- `delegation` — merged into `clear-mind`. Same content, `clear-mind` had more depth.
- `decision-logging` — merged into `decision-log`.
- `decision-log` — folded into `work-artifacts`.
- `knowledge-capture` — 21-line shim pointing at other skills.
- `work-tracking` — renamed and expanded into `work-artifacts`.
- `meridian-work-coordination` — folded into `work-artifacts`.

## [0.6.0] - 2026-05-29

### Added
- 4 principle shims: `delegation`, `decision-logging`, `work-tracking`, `knowledge-capture` — thin WHY principles pointing to reference skills for HOW.

### Changed
- All agent descriptions papered to one-liners — portable, no spawn syntax.
- `clear-mind`: reclassified `type: reference` → `type: guardrail`.
- 10 reference skills flipped to `model-invocable: true`.

## [0.5.0] - 2026-05-29

### Changed
- All agents: add `mode: subagent` for progressive loading
- 16 skills: add `detail` field for inventory summaries

## [0.4.24] - 2026-05-29

## [0.4.23] - 2026-05-28

### Fixed
- Composer alias now declares `harness = "cursor"` and `provider = "cursor"`, fixing routing to cursor instead of falling through to Pi.

## [0.4.22] - 2026-05-28

## [0.4.21] - 2026-05-28

## [0.4.20] - 2026-05-27

### Added
- `@meridian-subagent`: base-profile preamble for `MERIDIAN_TASK_DIR` vs `MERIDIAN_PROJECT_ROOT` — source-code ops target task dir, project context (skills, KB, harness config) stays at project root, `-f` relative paths already resolve against task dir. Convention inherited by subagents built on this profile.

## [0.4.19] - 2026-05-26

### Added
- `meridian-spawn`: "While a Spawn Runs" section — launch with a clear goal, use `spawn wait`, stop polling `session log` in a loop.

### Changed
- `meridian-spawn`: inject guidance scoped to relaying user direction only; self-generated nudges called out as attention waste.

## [0.4.18] - 2026-05-26

### Changed
- `mars.toml`: removed hardcoded `harness =` from most models — harness selection is now dynamic/probe-based.
- `mars.toml`: updated deepseek descriptions, simplified model names, commented out kimi and qwen.
- `explorer`: default model switched to `deepseek`.
- `meridian-default-orchestrator`, `meridian-spawn`, `meridian-privilege-escalation`: `models list` references now document `--live` flag for runtime availability.
- `bootstrap/harness-setup`: harness routing explanation updated for probe-based selection.
- `meridian-spawn`: `-f` guidance now prefers folder orientation scopes plus at most one source-of-truth file; explains AGENTS.md/QI autoloading and why multiple file refs should be exceptional.

## [0.4.17] - 2026-05-25

### Changed
- `meridian-spawn`, `session-mining`: session log guidance updated for finalized CLI — segment-local default, entry-0 setup slot, `--segment current|previous|N`, `--full`/`--no-truncate` for deliberate expansion, and `--global` as explicit opt-in for one flat stream across segments (conflicts with `--segment`, requires `--from/--before/--around`).
- `meridian-spawn`, `session-mining`: `session search` guidance now teaches scoped variants (`--work`, `--workspace`) and instructs agents to run the deterministic `Open:` command printed per hit instead of recomputing windows.

## [0.4.16] - 2026-05-25

### Added
- `composer` model alias — Cursor's native coding model (composer-2.5). Moved from consumer config to base package.

### Changed
- `meridian-spawn`, `session-mining`: session transcript examples now teach safe bare `session log` defaults, entry-based `--tail`, explicit `--full`, `--no-truncate`, and absolute windows instead of removed `--last`/`-n`/`-c` flags.
- `meridian-spawn`, `session-mining`: session transcript guidance now names entry `0` as the segment prologue/handoff slot and shows `--from 0 --limit 1`.

## [0.4.15] - 2026-05-24

### Changed
- `meridian-work-coordination`, `shared-workspace`: removed dev-workflow worktree policy from base coordination guidance.
- `meridian-work-coordination`: Starting Work now scoped to "when work coordination is warranted" instead of teaching session-attachment as a default precondition for every spawn. Small direct tasks can run without a work item.

## [0.4.14] - 2026-05-22

### Changed
- `/shared-dao`, `/intent-modeling`: model-invocable — core principle skills auto-attach in Cursor and other harnesses.

## [0.4.13] - 2026-05-22

### Changed
- `/shared-dao`: sharper and more general. Shared language is now framed as a structural boundary across workflows, records, docs, prompts, and implementation — not just code. Guidance now pushes faster convergence on one name per concept with more positive framing.
- `/kb-conventions`: added "current truth over history" — live KB should read as the best current understanding, with superseded material moved out of the live tree.
- `@kb-writer`, `@kb-maintainer`: KB updates now favor replacing superseded claims and moving historical leftovers to `kb/trash/` instead of layering corrections inline.
- `/session-mining`: model-invocable.

## [0.4.12] - 2026-05-19

### Changed
- `meridian-spawn`: tightened inject guidance — explains mechanism and scope boundary (course-correct current task, not new scope).

## [0.4.11] - 2026-05-17

### Changed
- `clear-mind`: choose subagents by installed agent descriptions and most-specific ownership before writing scoped handoffs.

## [0.4.10] - 2026-05-16

### Changed
- `meridian-spawn`: always `--prompt-file`, even for trivial inline strings. No inline prompt path.
- `clear-mind`: added `--prompt-file` mechanics — write handoffs to prompt files, not inline.

## [0.4.9] - 2026-05-16

## [0.4.8] - 2026-05-16

### Added
- `shared-dao` principle: shared vocabulary as contract between human intent and agent action. Covers vocab hierarchy, discovery, disambiguation, lifecycle, and conflict resolution.

### Changed
- `kb-conventions`: glossary section replaced with pointer to `shared-dao`
- `kb-writer`, `kb-maintainer`: carry `shared-dao`

## [0.4.7] - 2026-05-16

## [0.4.6] - 2026-05-16

## [0.4.5] - 2026-05-16

## [0.4.4] - 2026-05-15

### Changed
- `llm-writing`: explicitly model-invocable. Safety-net writing guardrail can be discovered during artifact work.

## [0.4.3] - 2026-05-15

### Changed
- `shared-workspace`: workspace ownership guardrail. Model-invocable again; git/staging discipline removed.

## [0.4.2] - 2026-05-14

### Added
- `grill-with-docs` skill: interactive grilling sessions against plans/proposals. Challenges terminology against KB vocabulary, spawns explorers for evidence, updates work requirements inline as decisions crystallize. Domain-agnostic — works for product plans, prompt systems, operations, architecture, or code.
- Model aliases: `deepseek` → `opencode-go/deepseek-v4-pro`, `deepseekflash` → `opencode-go/deepseek-v4-flash`, `kimi` → `opencode-go/kimi-k2.6`, `qwen` → `opencode-go/qwen3.6-plus`.

### Changed
- `kb-conventions`: glossary/vocabulary convention — hierarchical glossary pages (`glossary.md` at root and domain levels), term entry format (canonical name, definition, aliases, links), terminology conflict flagging via `[!FLAG]`.

## [0.4.1] - 2026-05-12

## [0.4.0] - 2026-05-11

## [0.3.12] - 2026-05-11

### Changed
- `@kb-maintainer`: gpt-5.5 → gpt-5.4-mini high. Structural doc health checks don't need frontier reasoning. Added reflection + llm-writing skills.

## [0.3.11] - 2026-05-11

### Fixed
- `meridian-privilege-escalation`: replaced stale `full-access` sandbox tier with `danger-full-access`. The old tier doesn't exist — agents using it got spawn failures.

## [0.3.10] - 2026-05-10

### Changed
- `qi-layer`: reframed AGENTS.md as Intent Nodes — compressed understanding (mental model, rules, anti-patterns), not routing tables. Four principles: fractal compression, hierarchical summarization, LCA deduplication, progressive disclosure. .context/ rationale sharpened around co-location.
- `@explorer`: read .context/ first before raw files.

## [0.3.9] - 2026-05-10

## [0.3.8] - 2026-05-10

### Changed
- `@kb-writer`: loads `qi-layer` — knows placement rules for .context/ vs KB vs docs/.

## [0.3.7] - 2026-05-10

### Changed
- `qi-layer`: tighter opening — removed contrastive framing that corrects a misconception nobody has.

## [0.3.6] - 2026-05-10

### Added
- `qi-layer` skill: inline knowledge placement rules — what goes in AGENTS.md vs .context/CONTEXT.md vs KB vs docs/. Domain-agnostic.

### Changed
- `@explorer`: description tells callers to scope spawns tightly (one module/question per spawn) — cheap models run out of context on broad exploration.

## [0.3.5] - 2026-05-10

## [0.3.4] - 2026-05-10

### Changed
- `@explorer`: `meridian qi <path>` → `meridian qi graph <path>` (bare qi is now summary view).
- `@kb-maintainer`: uses `meridian kg check kb` / `meridian kg graph kb` context aliases directly.
- `md-validation`: documents context aliases (`kb`, `strategy`, `work`) as valid path arguments for all kg subcommands.

## [0.3.3] - 2026-05-10

## [0.3.2] - 2026-05-10

### Added
- `@explorer`: knowledge-first exploration — `meridian qi <path>` checks AGENTS.md and .context/CONTEXT.md before reading raw source files. `Bash(meridian qi *)` added to tools.

### Changed
- `agent-management`: removed cross-package design-lead behavioral assumption. Deliverable shape guidance now package-neutral.
- `meridian-spawn`: `-p` escape hatch tightened to trivial smoke tests only. Everything else requires `--prompt-file`.
- `session-mining`: example switched from inline `-p` to `--prompt-file`, consistent with meridian-spawn discipline.
- `meridian-privilege-escalation`: fixed Claude sandbox self-contradiction (approval escalation only, no sandbox tiers). Removed invented model placeholders — use `meridian mars models list`.
- `meridian-work-coordination`: "run work start before spawning" softened to "ensure session is attached to correct work item."
- `kb-writer`: replaced vague "highest-value content" with concrete reasoning about why decisions need explicit capture.
- `kb-conventions`: removed harness-specific `CLAUDE.md`/`@AGENTS.md` reference. Schema layer described generically.
- `md-validation`: replaced contrastive "not just KB content" with positive framing.

## [0.3.1] - 2026-05-10

### Changed
- `meridian-spawn`: removed `--yield-after-secs` and polling guidance. Agents trust `spawn wait` timing — re-enter wait on yield, act on terminal state. Stops the nervous-babysitter pattern (show → log → short-yield wait → repeat).

## [0.3.0] - 2026-05-09

### Added
- `/reflection` skill — generic self-review guardrail, moved from `meridian-dev-workflow`. Step back, verify, fix before reporting.
- `meridian-work-coordination`: worktree section — `--worktree` / `--no-worktree` flags for `meridian work start`.

### Changed
- All skills tagged with `type:` field (principle, guardrail, or reference).
- `shared-workspace`: orientation step 1 now teaches `$(meridian work current)` inline pattern for resolving work directory.
- `meridian-work-coordination`: added inline command substitution examples for `meridian work current`.

## [0.2.12] - 2026-05-09

### Changed
- `agent-management`: "Decide from reports" principle — trust agents for work, own decisions, verify at LLM failure seams.
- `explorer`: description reframed as decision trigger, body emphasizes comprehensive self-contained reports with snippets.

## [0.2.11] - 2026-05-09

## [0.2.10] - 2026-05-09

## [0.2.9] - 2026-05-09

### Changed
- `meridian-spawn`: `--goal` taught as completion contract — injected into spawned agent context as verifiable exit condition. `--desc` removed from all examples and skill text; `--goal` replaces it throughout (examples, parallel spawns section, advanced-commands).
- `meridian-work-coordination`: work context is session-scoped. `work start` before spawning (spawns inherit via session attachment). `meridian work current` for parent agent's own work dir path (env vars don't update mid-session). Completion split into `work done` (archive + detach) and `work clear` (detach only).

## [0.2.8] - 2026-05-09

## [0.2.7] - 2026-05-06

### Changed
- `meridian-work-coordination`: completion guidance now keys work-done authority to lifecycle scope, not agent identity.
- `meridian-spawn`: added Prompt Passing section — `--prompt-file` as default for delegation, shell quoting rationale. All delegation examples now use `--prompt-file` + `--bg`. `-p` kept for short inline cases.
- `meridian-spawn/resources/advanced-commands.md`: delegation examples updated to `--prompt-file` + `--bg` (continue/fork, dry-run, permission tiers, background flag).
- `meridian-privilege-escalation`: spawn examples updated to `--prompt-file` + `--bg`.
- `README.md`: showcase examples updated to `--prompt-file` + `--bg`.

## [0.2.6] - 2026-05-04

### Changed
- agent-management: handoff prompts must carry user's full intent — agents own their deliverable shape, callers state the problem

## [0.2.5] - 2026-05-04

### Added
- Model alias: `opus46` pinned to `claude-opus-4-6`.

## [0.2.4] - 2026-05-03

### Changed
- Skill schema: migrated from `invocation: explicit` to `model-invocable: false` / `user-invocable: false`. Some skills previously marked explicit are now model-discoverable.

## [0.2.3] - 2026-05-03

## [0.2.2] - 2026-05-03

### Added
- Model catalog: `opus`, `gpt`, `sonnet`, `codex`, `gptmini`, `gpt55`, `opus47` aliases defined here as single source of truth. Downstream packages (meridian-dev-workflow, meridian-prompter) no longer duplicate these — eliminates "model alias defined by both" warnings during sync.

## [0.2.1] - 2026-05-02

### Changed
- Skill frontmatter: migrated all skills from legacy `disable-model-invocation`/`allow_implicit_invocation` to canonical `invocation: explicit`.
- `agent-management`: restructured as directory-based skill with `resources/` (convergence, escalation docs).

## [0.2.0] - 2026-05-02

### Added
- `@session-miner` agent: interpretive conversation mining — decisions, rejected alternatives, intent, constraints. Sonnet model for pragmatic interpretation. Splits from `@explorer`, which stays cheap/codebase-only.

### Changed
- `@explorer`: narrowed to codebase-only. Dropped `meridian session *`, `meridian work show *`, `meridian spawn show *` tools. Description routes to `@session-miner` for conversation history.
- `@kb-writer`: added `llm-writing` and `intent-modeling` — writes prose for humans, mines conversation for decisions.
- `@kb-writer`: trimmed body. Structural conventions (SRP, hierarchy, linking, readability) moved to `kb-conventions` skill.
- `@kb-maintainer`: trimmed body. Same structural conventions consolidated into `kb-conventions`.
- `kb-conventions`: expanded with wiki page conventions — SRP, hierarchical organization, linking discipline, readability, style. Single source of truth for structural standards; both kb-writer and kb-maintainer reference it.
- `session-mining`: delegation target `@explorer` → `@session-miner` for transcript mining.

## [0.1.3] - 2026-05-02

### Added
- `intent-modeling` skill: universal discipline for understanding human intent before acting. Covers overcorrection pattern (directional corrections encoded as absolute prohibitions), helpfulness instinct (pulling toward what feels helpful vs what was asked), and systematic misalignment detection.
- `llm-writing` skill: universal writing awareness for any artifact produced for humans. Covers behavioral pulls (fluent text without purpose, label-summaries, smoothed uncertainty) and conversational mode leaking into documents.

### Changed
- `decision-log`: loads `intent-modeling`. Reframed as transparency layer — LLM writes down its interpretation of human intent so misreadings are checkable before they get baked into artifacts.
- `kb-conventions`: restructured around five-layer KB model (sources, decisions, wiki, log, schema). Loads `llm-writing`. Writing guidance removed — belongs in per-writer agent prompts.
- Skill descriptions across 6 skills rewritten as triggers (when to load) instead of content summaries: `decision-log`, `meridian-privilege-escalation`, `meridian-spawn`, `meridian-work-coordination`, `shared-workspace`, `kb-conventions`.

## [0.1.2] - 2026-05-01

### Added
- `meridian-spawn`: Reading Transcripts section — `meridian session log` and `meridian session search` for inspecting spawn and session transcripts.

### Changed
- `meridian-spawn`: strengthened `spawn wait` enforcement — must-drain language in Parallel Spawns, closing reminder at skill end. Agents were skipping wait despite inline CLI reminders.

## [0.1.1] - 2026-05-01

### Removed
- `meridian-cli` skill (entire directory with SKILL.md and resources/). CLI operational knowledge now lives in `meridian --help` agent-mode supplements — run `meridian --agent -h` to see. Cross-references in `meridian-spawn` and `session-mining` updated to point at CLI commands instead of skill resources.

## [0.1.0] - 2026-04-30

### Changed
- `meridian-cli`, `meridian-spawn`, `meridian-work-coordination`: context dirs now available as `MERIDIAN_CONTEXT_*_DIR` env vars, injected into agent system prompts at launch. Removed "not in environment variables" guidance. `$MERIDIAN_WORK_DIR` documented as active work item (separate from `$MERIDIAN_CONTEXT_WORK_DIR` work root).
- `meridian-spawn`: trimmed 1589→756w. Absorbed meridian-cli §3 (output discipline, spawn lifecycle, crash-only design). Fixed abbreviated commands. Removed redundant examples.
- `decision-log`: trimmed 412→186w. Core ideas only — record while fresh, what/why/what-else, skip obvious. Decisions belong where they naturally belong, not a mandatory file path.
- `md-validation`: trimmed body, moved mermaid authoring and command reference to resources/.
- `meridian-privilege-escalation`: removed stale `unrestricted` sandbox tier and `--add-dir` flag.
- `kb-writer`: removed mandatory `decisions.md` file references. Decision mining captures to relevant domain docs.
- `kb-maintainer`: removed `decisions.md` verification requirements.
- `kb-conventions`: removed `decisions.md` from KB layout.
- All skills get explicit invocation-control flags. Safety nets (`meridian-privilege-escalation`) explicitly flipped to allow implicit loading.
- `AGENTS.md`: fixed title (was copy of dev-workflow), added `mars version` release guidance.
- `README.md`: removed stale `meridian-cli` skill from table, fixed parallel spawn example, removed stale `meridian report search`.

### Removed
- `agent-creator` skill (entire directory with resources/).
- `skill-creator` skill (entire directory with resources/).
- `meridian-cli` from `explorer`, `kb-writer`, `kb-maintainer`, `meridian-default-orchestrator` skill lists.

## [0.0.36] - 2026-04-30

### Changed

- update kb-maintainer and md-validation

## [0.0.34] - 2026-04-30

### Changed
- `@kb-maintainer`: target-aware path resolution — operates on an explicitly passed tree (e.g., work-item `design/` via `-f`) or defaults to the durable KB via `meridian context kb`. KB-specific commands (`meridian kg check/graph`) gated to KB target only; non-KB targets use `rg` and directory listing for cross-reference analysis. Description, body, and workflow all generalized. Navigability and diagram validation sections apply to any target with the relevant files present.
- `md-validation` skill: documents shipped `mermaid check` style warnings — `--strict`, `--no-style`, `--disable` flags; default categories (`ox-edge`, `bare-end`, `fill-no-color`); inline suppression syntax (`%% mermaid-check-ignore[-next-line] [category]`); warning output format and exit code semantics. Authoring rules and dark/light mode color guidance preserved.

## [0.0.33] - 2026-04-28

### Added
- `@explorer` agent: moved from meridian-dev-workflow. Generic cheap reader — codebase, sessions, work items. Nothing dev-workflow-specific about it.

### Changed
- All base agents now use direct model names instead of project-specific aliases. Aliases like `gpt`, `sonnet`, `codex`, `gptmini` only exist in the consuming project's config — base agents must resolve anywhere.
- `@kb-maintainer`: add `meridian-spawn` skill so it can delegate bulk reading.
- `shared-workspace` skill: orientation now starts with `meridian context` to discover available context locations (work, kb, project-specific). Route artifacts to the right context instead of hardcoding paths.
- `shared-workspace` skill: revert/stash/reset rule tightened — no escape hatch. Use `git worktree` if you need a clean tree.

## [0.0.32] - 2026-04-28

### Added
- `@kb-writer` agent: writes and updates KB — decisions, domain knowledge, architecture, synthesized research. Replaces content-writing half of old `@code-documenter`. Sonnet model, workspace-write.
- `@kb-maintainer` agent: structural health of KB — splits oversized docs, merges fragments, fixes cross-references, flags contradictions with `> [!FLAG]` markers for human review. GPT model, workspace-write.
- `kb-conventions` skill: shared KB structure, navigation, writing standards, flag protocol, what-belongs-where table. Loaded by both kb-writer and kb-maintainer.
- `decision-log` skill: moved from meridian-dev-workflow. Decision capture methodology — reasoning, alternatives, constraints.
- `session-mining` skill: moved from meridian-dev-workflow. Transcript mining patterns — top-level session recovery, bulk delegation to explorer, per-work-item session discovery.

### Changed
- Model catalog guidance: use `meridian mars models list`, not old `meridian models list`.

## [0.0.30] - 2026-04-25

### Changed
- `meridian-spawn` skill: background waits now taught as pending-set barriers, not per-spawn immediate waits. Explicitly says do not poll constantly, prefer sparse 10-minute shell polling, and keep one live wait session instead of reissuing waits.

## [0.0.29] - 2026-04-24

### Added
- `meridian-spawn` skill: "Steering a Running Spawn" section — teaches inject-before-cancel pattern so agents send course corrections instead of killing spawns.

### Changed
- `meridian-default-orchestrator`, `meridian-subagent`: broaden disallowed git commands — block `checkout`, `switch`, `stash` (not just `checkout --`).

## [0.0.28] - 2026-04-24

### Added
- `md-validation` skill — teaches agents `meridian kg` (link topology, broken link checking) and `meridian mermaid check` (diagram validation). Loaded by doc-facing agents.

## [0.0.26] - 2026-04-21

### Added
- `AGENTS.md` and `CLAUDE.md` — project instructions from dev-workflow.

### Changed
- `meridian-cli` skill: `$MERIDIAN_CHAT_ID` semantics corrected — top-level primary session id at root of chat tree, not parent. Fixed in prose, env-var table, sessions section. `session log <ref>` expanded: covers chat id / spawn id / harness session id; `--file path/to/session.jsonl` documented as separate invocation form; fallback resolution noted.
- `meridian-spawn` skill: new `--from` section. Covers `<spawn-id>` for predecessor reasoning and `$MERIDIAN_CHAT_ID` for top-level primary conversation. Examples show env-var paired with `-f` files (framing vs scope discipline).
- Context backend migration: `work_dir`/`fs_dir` → `work`/`kb`. All skills now use `meridian work current` and `meridian context kb` instead of old field names or env vars.
- `meridian-cli/SKILL.md`: context query section rewritten — documents `meridian context work`, `meridian context kb`, `meridian context work.archive`. Removed stale `work_dir`/`fs_dir`/`repo_root`/`state_root`/`depth`/`context_roots` field list.
- `meridian-spawn/SKILL.md`: shared filesystem section uses new query commands. `-f` now documented as accepting folders (tree listing) plus files (full content) — folder-for-map, file-for-content pattern.
- `meridian-work-coordination/SKILL.md`: artifact placement uses `work`/`kb` vocabulary with query commands.
- `meridian-cli/resources/debugging.md`: removed `$MERIDIAN_FS_DIR` env var refs — replaced with `meridian context kb` query.
- `agent-creator`: removed `$MERIDIAN_WORK_DIR` env var refs from SKILL.md, example-profiles.md, anti-patterns.md.
- `meridian-prompter` dep switched to `local-dependencies` — expects sibling checkout.
- `meridian-spawn/SKILL.md`: teach `--bg` + single `wait` pattern for parallel spawns. Old pattern (harness-level `run_in_background` per spawn) caused N notifications and N partial summaries — token waste. New pattern: launch with `--bg`, single `wait` for all, one summary. Documents 30-minute wait checkpoint.

## [0.0.21] - 2026-04-18

### Changed
- Skills trimmed for conciseness — context query model uses `meridian context` / `meridian work current` instead of env vars.
- `meridian-cli`: diagnostics tables moved to `resources/debugging.md`, Mars section removed (use `--help`), Resources section added, Context Query section trimmed.
- `meridian-spawn`: inject docs trimmed (1 line), prompt examples simplified.
- `meridian-work-coordination`: artifact placement updated for context query pattern.


## [0.0.19] - 2026-04-17

### Added
- `shared-workspace` skill: moved from `meridian-dev-workflow`. Multi-agent safety for shared repos — orientation on active work, rules for not destroying other actors' uncommitted changes, staging discipline. Base agents and dev-workflow agents both need it.

## [0.0.18] - 2026-04-17

### Changed
- `@meridian-default-orchestrator` and `@meridian-subagent`: comprehensive `disallowed-tools` hardening. Block `ScheduleWakeup`, `Cron*`, `PushNotification`, `RemoteTrigger`, `EnterPlanMode`, `ExitPlanMode`, `EnterWorktree`, `ExitWorktree`, `NotebookEdit`. Keep `LSP` and `Monitor` available. Orchestrator keeps `Task*` and `AskUserQuestion`.

## [0.0.17] - 2026-04-16

### Changed
- `meridian-cli/SKILL.md`: add `finalizing` to spawn lifecycle ("queued → running → finalizing → terminal"). Teach `finalizing` as transient/non-terminal so agents stop treating it as stuck. Failure-mode table: drop `orphan_stale_harness` (deleted upstream), add `orphan_finalization` row, rename `missing_wrapper_pid`/`missing_worker_pid` → `missing_runner_pid`.
- `meridian-cli/resources/configuration.md`: drop `defaults.agent` and `defaults.primary_agent` rows (both removed upstream). Teach profile-less spawn default when no `-a`. Add `primary.*` namespace section for primary-session knobs. Add `defaults.harness` row. Bump `timeouts.wait_minutes` default 30 → 120. Tighten resolution-order list to match live precedence; add per-field-override note.
- `meridian-cli/resources/debugging.md`: teach that `finalizing` is not stuck, give the reconciliation path to `orphan_finalization`, note `report.md` may still hold useful content after abandonment.
- `meridian-spawn/resources/advanced-commands.md`: remove `meridian spawn report create` examples (subcommand deleted upstream). Fix `report show` example to positional form. Add explanatory note that reports are written by the spawned agent itself at end-of-run.
- `meridian-spawn/SKILL.md`: Parallel Spawns section names the concrete Claude Code mechanism — `run_in_background: true` Bash tool parameter. Prior text said "use your harness's native background execution" abstractly; example-less direction didn't map cleanly to the specific tool agents actually have. Concrete syntax for Claude Code; pointer to "equivalent mechanisms" for other harnesses.
- `agent-creator` and `skill-creator`: "dial back aggressive language" guidance now more precise. Prefer ordinary framing by default, but keep load-bearing negatives when they carry a real boundary with reasoning. Warn against blind rewrite sweeps that strip every `must`/`never`.

## [0.0.14] - 2026-04-10

### Fixed
- `meridian-cli/resources/mars-toml-reference.md`: "Item Filtering" section claimed `agents`/`skills` and `exclude` could combine ("Both: `agents`/`skills` defines the set, `exclude` removes from it"). Wrong — per mars source, `FilterConfig::to_mode()` makes filter modes mutually exclusive. When both are set, `exclude` is silently dropped. Rewrote the section to document the actual precedence order and the mutual-exclusion rule. Sent an agent down a rabbit hole this session (see `meridian-dev-workflow/CHANGELOG.md` `0.0.16` entry).

## [0.0.13] - 2026-04-10

### Added
- `CHANGELOG.md`. Keep a Changelog format, caveman style.

### Changed
- Git URLs moved `haowjy/` → `meridian-flow/` org.
