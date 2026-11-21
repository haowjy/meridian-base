# /// script
# requires-python = ">=3.11"
# ///
"""Regenerate the README model table from mars.toml.

Usage:
    uv run scripts/models_table.py          # rewrite the table in README.md
    uv run scripts/models_table.py --check  # exit 1 if README.md is out of date

The table sits between the README markers below, one row per [models.<alias>],
sorted by alias.
"""

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARS = ROOT / "mars.toml"
README = ROOT / "README.md"
START = "<!-- models-table:start -->"
END = "<!-- models-table:end -->"


def render() -> str:
    models = tomllib.loads(MARS.read_text())["models"]
    return "\n".join(
        [
            "| Alias | Description |",
            "|---|---|",
            *(
                f"| `{alias}` | {spec.get('description', '').strip()} |"
                for alias, spec in sorted(models.items())
            ),
        ]
    )


def main() -> int:
    text = README.read_text()
    if START not in text or END not in text:
        print(f"README.md is missing {START} / {END} markers", file=sys.stderr)
        return 2
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = f"{head}{START}\n{render()}\n{END}{tail}"
    if "--check" in sys.argv[1:]:
        if updated != text:
            print("README.md model table is out of date; run scripts/models_table.py")
            return 1
        return 0
    README.write_text(updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
