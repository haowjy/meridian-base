---
name: meridian-privilege-escalation
type: reference
description: Use when a delegated agent fails because its sandbox, permissions, or network access are too narrow.
---

# Privilege Escalation

Treat access as part of staffing. A sandboxed caller cannot give a delegated
agent a weaker sandbox, broader network access, or a capability the caller does
not have. Return that failure to the caller instead of retrying the same task
with broader access.

An unsandboxed caller may grant a one-off sandbox or network override for one
run. Surface it to the user and get approval first; an agent silently granting
itself maximum access defeats the permission boundary.

## Escalation Discipline

Name the operation the delegated agent could not perform and the access it
needs. Pass the failed task and exact error to whoever acts next so it does not
repeat the diagnosis.

Prefer the narrowest fix: an existing agent profile that already declares the
access, then a user-approved one-off exception from a caller allowed to grant
it. Ask for a profile change only when the need recurs; a one-off failure is not
a reason for a permanent grant.

Approval policy changes how the harness handles tool prompts; it does not widen
the caller's sandbox. Use the least permissive policy that allows the work and
surface any fully automatic approval to the user first.

## Model and Harness Switching

Different models may route to different harnesses. Check the live model catalog
and model-specific prompting guidance before rerouting. Switch only when the
task needs a capability that the selected profile already permits; model
routing is not a way around the caller's boundary.

## Common Escalation Scenarios

**"Can't bind to a port / start a server"**
→ Local listeners require network access. A sandboxed caller can grant it only
if it already has that access; otherwise return the error and port to the
caller.

**"Can't write files outside the workspace"**
→ Return the target path and failed operation to the caller; use a profile
whose sandbox declares that scope.

**"Can't access the network / fetch URLs"**
→ Use the profile's web tools when they fit. Otherwise use the narrowest
network access that permits the destination. A sandboxed caller cannot grant a
child broader network access. A child refused for the network floor can be
relaunched with narrower network access when the task permits; otherwise return
the failed destination and operation to the caller.

**"Permission denied on tool call"**
→ Use the least permissive approval policy that permits the operation. Surface
unbounded approval to the user first.

**"Context too small for the task"**
→ Choose a model with a larger context window from the live model catalog.
