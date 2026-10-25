---
name: meridian-privilege-escalation
type: reference
description: Use when a spawn fails due to sandbox or permission restrictions.
---

# Privilege Escalation

Treat access as part of staffing. What you can do depends on your own sandbox.

- **You are sandboxed** (`read-only` or `workspace-write`): Meridian refuses a child with a weaker sandbox than yours or with no declared spawn capability. Retrying with `--sandbox danger-full-access` is refused. Return the failure to your caller.
- **You are not sandboxed** (`danger-full-access`): a per-spawn `--sandbox` override still works. Surface it to the user first and let them approve it; an agent silently granting itself maximum access defeats the tiers.

## Escalation Discipline

Name the operation the failed spawn could not perform and the access it needs, and pass the failed task and error to whoever acts next so it does not repeat the diagnosis.

Prefer the narrowest fix: an existing profile that already declares the access, then an approved one-off override (unsandboxed callers only). Ask for a profile change only when the need recurs; a one-off failure is not a reason for a permanent grant.

## Approval Modes

The `--approval` flag controls how the harness handles tool-call approvals:

| Mode | Behavior |
|---|---|
| `default` | Harness decides (each harness has its own default policy). |
| `confirm` | User approves each tool call. |
| `auto` | Auto-approve safe operations, prompt for dangerous ones. |
| `yolo` | Approve everything. No prompts. |

Override per-spawn:
```bash
meridian spawn -a subagent --approval auto --prompt-file task.md --bg
meridian spawn -a subagent --approval yolo --prompt-file task.md --bg   # use yolo sparingly
```

Approval changes how the harness handles tool prompts; it does not widen the caller's sandbox. Surface `yolo` to the user before using it.

## Model/Harness Switching

Different models route to different harnesses. Switch only when the task needs a capability the selected profile already permits; model routing is not a way around the caller's boundary.

```bash
# Choose an alias from `meridian mars models list`; use `--live` when you need
# to confirm the needed harness is runnable on this machine.
meridian spawn -a subagent -m MODEL_ALIAS --prompt-file task.md --bg
```

Run `meridian mars models list` to see catalog aliases and static routing hints.
Run `meridian mars models list --live` to confirm the route is runnable.

## Common Escalation Scenarios

**"Can't bind to a port / start a server"**
→ Sandboxes block listeners. Use a profile that runs unsandboxed, or return the error and port to your caller.

**"Can't write files outside workspace"**
→ Return the target path and failed operation to the caller; use a profile whose sandbox declares that scope.

**"Can't access the network / fetch URLs"**
→ Use the profile's web tools when they fit. Otherwise return the failed destination and operation to the caller for a profile with the required access.

**"Permission denied on tool call"**: approval mode is blocking.
→ `--approval auto` first. If that's not enough, surface to the user before using `--approval yolo`.

**"Context too small for the task"**: model limitation.
→ Switch to a model with a larger context window via `-m`.
