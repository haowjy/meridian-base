---
name: work-artifacts
type: principle
description: Anchor work in a work item — artifacts on disk, not in context.
model-invocable: true
---

# Work Artifacts

Active artifacts live in the work directory; spawns reference the work item
for continuity across sessions and compaction. If understanding is not on
disk, it does not survive.

Write findings, decisions, and design artifacts to the work directory as you
produce them. Reference files accumulate; conversation context compacts. The
work directory is the shared state between you, the user, and other agents.

See [`resources/coordination.md`](resources/coordination.md) for work item
mechanics — creating, switching, status updates, completion, artifact placement.
