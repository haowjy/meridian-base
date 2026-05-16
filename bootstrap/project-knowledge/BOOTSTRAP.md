# Project Knowledge Setup (CLAUDE.md / AGENTS.md)

When agents enter a directory, they automatically load instruction files
that tell them how to work there. This is how you give agents project
context without repeating yourself in every prompt.

## The files

| File | What it does | Who reads it |
|---|---|---|
| `CLAUDE.md` | Root-level project instructions. Loaded by Claude Code on every session. | Claude Code harness |
| `AGENTS.md` | Directory-level intent. Loaded by any agent entering that directory. | All harnesses via meridian |
| `.context/CONTEXT.md` | Detailed reference docs colocated with code. Read on demand. | Agents that need depth |

**`CLAUDE.md` and `AGENTS.md` at root are typically symlinked** — same
content, but the filename determines which harness picks it up. Claude
Code reads `CLAUDE.md`; other harnesses read `AGENTS.md`.

## What goes in root CLAUDE.md / AGENTS.md

This is the project's "instruction manual for agents." Include:

- **What this project is** — one paragraph orientation
- **Dev workflow** — how to run, test, lint, build
- **Key conventions** — naming, file organization, commit style
- **What NOT to do** — common mistakes, forbidden patterns
- **Architecture pointers** — where things live, how pieces connect

This file is loaded into every agent session in this repo. Keep it
focused on what agents need to work correctly. It's not documentation
for humans — it's instructions for agents.

## What goes in subdirectory AGENTS.md files

Deeper AGENTS.md files provide local context for specific areas:

```
src/
  AGENTS.md          ← "how to work in src/"
  api/
    AGENTS.md        ← "how to work in the API layer"
  workers/
    AGENTS.md        ← "how to work with workers"
```

Each AGENTS.md answers: **what must an agent understand before working
here?** Mental models, constraints, invariants, anti-patterns.

Context is hierarchical — agents accumulate understanding as they descend.
Don't repeat parent content in children.

## What goes in .context/

`.context/CONTEXT.md` provides reference depth — contracts, architecture
diagrams, rationale for design decisions. It lives next to the code it
documents so it stays in sync.

Agents read `.context/` when they need to understand *why* something is
the way it is, or *what contracts* they must preserve when making changes.

## The qi-layer skill

The `qi-layer` skill teaches agents how to write and maintain these files.
It covers:

- What belongs in AGENTS.md vs .context/ vs KB vs docs/
- How to compress understanding (fractal compression)
- How to deduplicate across the hierarchy (LCA rule)
- When to create new AGENTS.md or .context/ files

You don't need to configure anything — the skill is loaded automatically
when agents need to write inline knowledge.

## Getting started

If this project does not have a root `CLAUDE.md` or `AGENTS.md` yet,
create one now. Start with:

1. What this project is (1-2 sentences)
2. How to run the dev loop (install, test, lint, build commands)
3. Key conventions and constraints
4. Common mistakes to avoid

Ask the user what they want agents to know about this project. Their
answers become the initial CLAUDE.md content.

If the project already has these files, verify they are up to date with
the current codebase and conventions.
