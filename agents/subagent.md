---
name: subagent
description: "Spawn for a bounded task no specialist agent fits. Pass the full task and the context it needs."
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
