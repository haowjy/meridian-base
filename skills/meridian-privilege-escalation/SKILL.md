---
name: meridian-privilege-escalation
type: reference
description: Use when a spawn fails due to sandbox or permission restrictions.
---

# Privilege Escalation

Treat access as part of staffing. A sandboxed caller cannot launch a child with a weaker sandbox, without its declared spawn capability, or with broader access than its own. Retrying with `--sandbox danger-full-access` is therefore refused instead of escaping the caller's boundary.

## Escalation Discipline

Name the operation the failed spawn could not perform and the access it needs. Then return that evidence to the caller. The caller can select an existing profile that declares the required access, or ask the human to approve a profile change. Pass the failed task and error to the replacement spawn so it does not repeat the diagnosis.

Do not turn a task-specific failure into a broad permanent grant. When no profile declares the needed access, ask the caller or human to perform the operation or decide whether a new profile is warranted.

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
→ Return the error and required port to the caller; use a profile that declares the necessary process access.

**"Can't write files outside workspace"**
→ Return the target path and failed operation to the caller; use a profile whose sandbox declares that scope.

**"Can't access the network / fetch URLs"**
→ Use the profile's web tools when they fit. Otherwise return the failed destination and operation to the caller for a profile with the required access.

**"Permission denied on tool call"**: approval mode is blocking.
→ `--approval auto` first. If that's not enough, surface to the user before using `--approval yolo`.

**"Context too small for the task"**: model limitation.
→ Switch to a model with a larger context window via `-m`.
