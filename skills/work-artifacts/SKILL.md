---
name: work-artifacts
type: principle
description: "Load when work must survive compaction or crashes or be shared with other agents: findings, decisions, and artifacts go in the work directory, not in context."
model-invocable: true
---

# Work Artifacts

The work directory is the shared state between you, the user, and other
agents; what isn't on disk doesn't survive a crash or compaction. Write
findings and decisions there as you make them, with the alternatives you
rejected, and commit where it is version-controlled. Find it with
`meridian work current`. Source edits go in the work item's `task_dir`, not
the work directory.

This work item's artifacts go in the work directory; project-wide reference
goes in the KB (`meridian context kb`). Keep raw files (traces, HARs,
dumps, build output) out of the work directory, which syncs through git:
record the excerpt that carries the finding.

The agent that started a work item owns its state; leave it alone unless
your brief says otherwise. The owner's side (starting and finishing work
items, `DIVERGENCE/`, the work directory's AGENTS.md) is in
`resources/lifecycle.md`.
