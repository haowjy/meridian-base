# Command Reference

## `meridian kg`

Run `meridian kg [path]` for a fast status pass — file count, link count, broken link count.

All `kg` subcommands accept context aliases as path: `kb`, `strategy`, `work`
resolve to their context directories (e.g. `meridian kg check kb`).

### `meridian kg graph`

Run `meridian kg graph [path]` to see link topology.

Targets: file path, directory path, or context alias (`kb`, `strategy`, `work`).

Flags:
- `--depth N` — link-hop depth (default `3`)
- `--external` — include external URLs as leaf nodes
- `--exclude PATTERN` — exclude matches by glob (repeatable)
- `--format json` — machine-readable output

Persistent exclusions: `.kgignore` at the scan root (gitignore-style matching).

Tree markers:
- `(already shown)` — node was previously rendered
- `(N links hidden)` — links truncated by depth/filters
- `(not found)` — local target could not be resolved

### `meridian kg check`

Run `meridian kg check [path]` as a commit/CI gate.

Targets: file path, directory path, or context alias (`kb`, `strategy`, `work`).

Flags:
- `--exclude PATTERN` — exclude matches by glob (repeatable)
- `--format json` — machine-readable output

Exit: `0` no broken links, `1` broken links found.

## `meridian mermaid check`

Run `meridian mermaid check [path]` to validate Mermaid in fenced blocks, `.mmd`, and `.mermaid` files.

Runs syntax validation AND default style warnings.

### Flags

Core:
- `--depth N` — directory traversal depth
- `--exclude PATTERN` — exclude by glob (repeatable)
- `--format json` — machine-readable output

Style control:
- `--strict` — warnings cause exit code 1
- `--no-style` — skip style checks, syntax-only; wins over `--strict`
- `--disable cat1,cat2` — skip named warning categories

Persistent exclusions: `.mermaidignore` at the scan root.

### Parser Modes

- Python heuristic parser by default
- Optional JS strict parser when Node.js is available

### Default Warning Categories

| Category | Phase | Detects |
|----------|-------|---------|
| `ox-edge` | pre-parse | `---oNode` / `---xNode` parsed as circle/cross edge endings |
| `bare-end` | pre-parse | Bare lowercase `end` collides with subgraph terminator |
| `fill-no-color` | post-parse | Inline `style` with `fill:` but no `color:` — text unreadable |

Pre-parse checks run on all blocks. Post-parse checks run only on valid blocks.
`classDef` declarations do not trigger `fill-no-color`.

### Inline Suppression

```
%% mermaid-check-ignore-next-line ox-edge
API ---oBackend

%% mermaid-check-ignore bare-end
```

- `%% mermaid-check-ignore-next-line <category>` — suppress one category on next line
- `%% mermaid-check-ignore-next-line` — suppress all warnings on next line
- `%% mermaid-check-ignore <category>` — suppress one category for entire block
- `%% mermaid-check-ignore` — suppress all warnings for entire block

### Warning Output Format

Text: `warning[ox-edge] docs/flow.md:12: edge ...`
JSON: `warnings` array alongside `results`, plus `total_warnings` and `suppressed_warnings`.

### Exit Behavior

- `0` — clean (warnings present but no `--strict`)
- `1` — syntax errors, or warnings with `--strict`
- `2` — target path not found
