# Context and Autosync Setup

Meridian stores work items and knowledge outside the project repo so they
survive branch switches, worktree changes, and repo moves. This bootstrap
explains how context works and helps you decide how to set it up.

## What contexts are

Meridian uses three context directories:

| Context | Purpose | Required |
|---|---|---|
| **work** | Active and archived work items — designs, plans, requirements, status | Yes — `meridian work start` needs this |
| **kb** | Knowledge base — architecture, decisions, lessons, vocabulary | No — but agents write here during KB capture |
| **strategy** | Shared strategy docs across projects | No — only if your org uses shared strategy |

Contexts are just directories. Meridian reads and writes files in them.
The question is *where* those directories live.

## Default: local files

With no configuration, contexts default to local directories under
`~/.meridian/`:

```
~/.meridian/context/<project-uuid>/work/
~/.meridian/context/<project-uuid>/archive/work/
~/.meridian/context/<project-uuid>/kb/
```

This works for solo use on one machine. No setup needed — `meridian work
start` creates the directories automatically.

**Tradeoff:** Local-only context is invisible to other machines, lost if
`~/.meridian/` is deleted, and cannot be shared across a team.

## Git-backed context

For durability and sharing, contexts can be backed by a git repo. Meridian
clones the repo under `~/.meridian/git/` and reads/writes context paths
inside that clone.

To configure, add `[context.*]` sections to `meridian.toml`:

```toml
[context.work]
source = "git"
remote = "git@github.com:org/docs.git"
path = "work"
archive = "archive/<project>/work"

[context.kb]
source = "git"
remote = "git@github.com:org/docs.git"
path = "kb"
```

Multiple contexts can share one remote repo (different `path` values) or
use separate repos:

```toml
# Public KB, private work items
[context.kb]
source = "git"
remote = "git@github.com:org/public-kb.git"
path = "kb"

[context.work]
source = "git"
remote = "git@github.com:org/private-docs.git"
path = "work"
archive = "archive/myproject/work"
```

Arbitrary named contexts (like `strategy`) use the same pattern:

```toml
[context.strategy]
source = "git"
remote = "git@github.com:org/docs.git"
path = "strategy"
```

**First access triggers the clone.** Run `meridian context kb` or
`meridian context work` to force-clone immediately, or let it happen
lazily on first use.

## Git autosync hook

Without autosync, git-backed context is just a local clone — changes
stay on disk until someone manually commits and pushes.

The `git-autosync` hook automates this: when spawns complete or work
events fire, meridian commits and pushes context changes to the remote.

Add one `[[hooks]]` entry per remote:

```toml
[[hooks]]
builtin = "git-autosync"
remote = "git@github.com:org/docs.git"
```

If contexts span multiple remotes, add one hook per remote:

```toml
[[hooks]]
builtin = "git-autosync"
remote = "git@github.com:org/private-docs.git"

[[hooks]]
builtin = "git-autosync"
remote = "git@github.com:org/public-kb.git"
```

**What autosync does:**

1. Detects uncommitted changes in the context clone
2. Stages and commits them with an auto-generated message
3. Pulls (rebase) to pick up remote changes
4. Pushes to the remote

**What autosync does not do:**

- It does not sync on a timer — only on meridian events (spawn complete,
  work start/archive, KB write)
- It does not resolve merge conflicts automatically — if a conflict occurs,
  use `meridian sync conflict` to inspect and resolve

**Requirements:**

- SSH key access to the remote (or HTTPS credentials configured in git)
- Remote repo must exist (autosync does not create repos)
- Remote branch must exist or the remote must allow pushing new branches

## Verify setup

Check that contexts resolve:

```bash
meridian context           # summary of all contexts
meridian context --verbose # shows source, path, and resolved location
meridian context kb        # prints absolute path to KB directory
meridian context work      # prints absolute path to work directory
```

Test that autosync can push:

```bash
meridian work start test-sync
meridian work archive test-sync
```

Check the remote repo for the committed work item. If push fails, verify
SSH access and that the remote exists.

## Choosing a setup

| Situation | Recommended setup |
|---|---|
| Solo dev, one machine | Local defaults (no config needed) |
| Solo dev, multiple machines | Git-backed + autosync |
| Team, shared knowledge | Git-backed + autosync, shared KB repo |
| Public KB, private work | Separate repos, different visibility |
| Org-wide strategy | Shared strategy context pointing to org docs repo |
