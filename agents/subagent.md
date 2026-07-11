---
name: subagent
description: General-purpose subagent
mode: subagent
model: sonnet
effort: high
model-policies:
  - match: {alias: sol}
    override: {effort: high}
  - match: {alias: terra}
    override: {effort: high}
  - match: {alias: luna}
    override: {effort: high}
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
