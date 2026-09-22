---
name: subagent
description: General-purpose subagent
mode: subagent
model: luna
effort: high
model-policies:
  - match: {alias: luna}
    override: {effort: high}
  - match: {alias: deepseek}
    override: {effort: high}
  - match: {alias: sol}
    override: {effort: high}
  - match: {alias: sonnet}
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
