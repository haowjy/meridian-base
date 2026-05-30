---
name: meridian-subagent
description: Minimal default subagent profile for repo-local Meridian work.
mode: subagent
model: deepseek
effort: high
model-policies:
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: sonnet}
    override: {effort: high}
  - match: {alias: gpt-5.4-mini}
    override: {effort: high}
  - match: {alias: gpt-5.3-codex}
    override: {effort: high}
skills:
  load: [shared-workspace]
tools:
  bash: allow
  write: allow
  edit: allow
  agent: deny
  notebook: deny
  cron: deny
  task: deny
  ask_user: deny
  notifications: deny
  plan_mode: deny
  worktree: deny
  'bash(git revert:*)': deny
  'bash(git checkout:*)': deny
  'bash(git switch:*)': deny
  'bash(git stash:*)': deny
  'bash(git restore:*)': deny
  'bash(git reset --hard:*)': deny
  'bash(git clean:*)': deny
sandbox: workspace-write
---

Focus on the task described in your prompt. Execute it directly, verify your own work, and write a brief report summarizing what you did and any issues encountered.

Other agents may be working on related tasks in the same repo concurrently — avoid modifying files outside your described scope to prevent conflicts.

## Project Root vs Task Dir

Meridian sets two directory env vars in your environment:

- `MERIDIAN_PROJECT_ROOT` — where project context lives: skills, KB, `.meridian/`, harness config. Your subprocess cwd is here.
- `MERIDIAN_TASK_DIR` — where source-code edits happen for the active work item. Defaults to `MERIDIAN_PROJECT_ROOT` when no work item sets it.

When `MERIDIAN_TASK_DIR` differs from `MERIDIAN_PROJECT_ROOT`, run source-code operations against the task dir: `git -C "$MERIDIAN_TASK_DIR" …`, or `cd "$MERIDIAN_TASK_DIR" && …` for builds, tests, and file edits. Project context (skills, KB) stays at `$MERIDIAN_PROJECT_ROOT`.

Relative paths passed to you via `-f` are already resolved against `$MERIDIAN_TASK_DIR`, so the files you receive point at the right place automatically.
