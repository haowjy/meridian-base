---
name: subagent
description: General-purpose subagent
mode: subagent
model: sol
effort: xhigh
model-policies:
  - match: {alias: sol}
    override: {effort: xhigh}
  - match: {alias: terra}
    override: {effort: xhigh}
  - match: {alias: luna}
    override: {effort: xhigh}
  - match: {alias: sonnet}
    override: {effort: high}
  - match: {alias: glm}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: composer}
    override: {}
  - match: {alias: deepseekflash}
    override: {effort: high}
tools:
  'bash(meridian spawn *)': allow
  'bash(meridian session *)': allow
  'bash(meridian work *)': allow
  'bash(meridian context *)': allow
  'bash(meridian qi *)': allow
sandbox: danger-full-access
approval: auto
---

Make no mistakes.
