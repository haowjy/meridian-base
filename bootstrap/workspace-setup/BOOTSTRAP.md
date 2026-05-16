# Workspace Setup

Meridian workspaces let agents access files across multiple repos — sibling
checkouts, worktrees, shared libraries. This bootstrap explains how to set
them up and a critical Claude Code limitation to watch for.

## What workspaces do

By default, an agent can only see files in the current project repo. A
workspace entry grants access to additional directories:

```toml
# meridian.toml
[workspace.sibling-repos]
path = ".."
```

This tells meridian (and the harness) that agents may read and write
files in the parent directory — which typically contains sibling repos.

## Recommended layout: sibling repos

The standard layout is repos checked out as siblings under a common
parent:

```
~/repos/
  my-project/           ← your main project
  shared-lib/           ← sibling repo
  docs/                 ← sibling repo
  prompts/              ← prompt source repos
```

With this layout, a workspace of `..` (parent directory) gives agents
access to all sibling repos.

## Claude Code limitation: skill leakage

**This is a critical gotcha with Claude Code.**

When Claude Code's `--add-dir` (which meridian uses to implement workspace
access) points to a directory that contains `.claude/skills/`, Claude Code
loads ALL skills from that directory into the agent's context.

This means if your workspace points directly to a sibling repo that has
its own skills installed:

```toml
# DANGEROUS with Claude Code:
[workspace.shared-lib]
path = "../shared-lib"    # ← if shared-lib has .claude/skills/, they ALL load
```

Those skills get injected into every agent session — doubling or tripling
the context window usage. Agents get confused by irrelevant skills from
other projects.

### The fix: use the parent directory

Instead of pointing workspace entries at individual sibling repos, point
at their **parent**:

```toml
# SAFE — parent directory doesn't have .claude/skills/
[workspace.sibling-repos]
path = ".."
```

The parent directory (`~/repos/`) does not have `.claude/skills/`, so no
skill leakage occurs. Agents can still read files in any sibling repo
via the parent path — they just don't get that repo's skills loaded.

### Why this works

Claude Code scans for skills at the **workspace root** it's given, not
recursively through subdirectories. Pointing to `..` (the parent) means
Claude Code looks for `../.claude/skills/` — which doesn't exist. The
sibling repos' skills at `../shared-lib/.claude/skills/` are not loaded
because they're one level deeper.

### If you must add a specific repo

If you need to add a specific sibling repo (not the parent), and that
repo has `.claude/skills/`, be aware of the cost:

```toml
[workspace.shared-lib]
path = "../shared-lib"    # loads shared-lib's skills too — extra context
```

Decide whether the file access is worth the context overhead. For most
cases, the parent directory approach avoids the problem entirely.

## Configuration

### In meridian.toml (committed, shared with team)

```toml
[workspace.sibling-repos]
path = ".."
```

### In meridian.local.toml (gitignored, machine-specific overrides)

```toml
# Override if your checkout is at a non-standard location
[workspace.sibling-repos]
path = "/home/me/different-location"
```

### Multiple workspace entries

```toml
[workspace.sibling-repos]
path = ".."

[workspace.data-dir]
path = "~/datasets"     # additional directory for data access
```

## Summary

| Setup | Workspace path | Skill leakage? |
|---|---|---|
| Parent directory (recommended) | `..` | No — parent has no `.claude/skills/` |
| Specific sibling repo | `../sibling` | Yes — if sibling has `.claude/skills/` |
| Absolute path to non-repo dir | `/path/to/data` | No — no skills there |

Ask the user about their repo layout and configure accordingly. Default
to the parent directory approach unless they have a specific reason to
add individual repos.
