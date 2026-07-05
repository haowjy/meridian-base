---
name: subagent
description: General-purpose subagent
mode: subagent
model: gpt55
effort: high
model-policies:
  - match: {alias: gpt55}
    override: {effort: high}
  - match: {alias: opus46}
    override: {effort: high}
  - match: {alias: glm}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: composer}
    override: {}
  - match: {alias: deepseekflash}
    override: {effort: high}
  - match: {alias: gptmini}
    override: {effort: high}
tools:
  bash: allow
  'bash(meridian spawn *)': allow
  'bash(meridian session *)': allow
  'bash(meridian work *)': allow
  'bash(meridian context *)': allow
  'bash(meridian qi *)': allow
  read: allow
  write: allow
  edit: allow
  notebook: deny
  ask_user: deny
  'bash(git revert:*)': deny
  'bash(git checkout:*)': deny
  'bash(git switch:*)': deny
  'bash(git stash:*)': deny
  'bash(git restore:*)': deny
  'bash(git reset --hard:*)': deny
  'bash(git clean:*)': deny
sandbox: danger-full-access
approval: auto
---

Make no mistakes.
