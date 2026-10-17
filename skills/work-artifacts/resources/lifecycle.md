# Owning a Work Item

## Start and Track

Small direct tasks can run without a work item. Start one when the work
needs its own artifacts or tracking: `meridian work start "<name>"`, or
`meridian work switch <name>` to attach to an existing one. Spawns inherit
the attachment. Rebind the checkout with `meridian work task-dir <path>`.
`meridian work -h` lists the rest (dashboard, list, show, reopen, delete).

Keep the current phase visible in the free-form status:
`meridian work update <name> --status <phase>`.

## Finish

Handing work off for review is not finishing it: set a status such as
`pr-open` and leave the item active until the change is accepted and
cleaned up. Then `meridian work done <name>` archives the work directory and
detaches the session. Run it only when you own the whole lifecycle, not a
slice of it; use `meridian work clear` to detach from an item you don't own.

## The Work Directory

Its `AGENTS.md` orients a spawn arriving cold: the goal, the artifact
layout, and what is settled versus still moving. Keep it current as the
work shifts, per `/qi-layer`.

Decisions scoped to one change go with it, in its commit message or a note
beside what it explains; structural decisions go in the work directory.
When the plan shifts during execution, log the shift in `DIVERGENCE/`.
Reviewers check alignment against it, and knowledge capture mines it.
