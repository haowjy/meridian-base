# /// script
# requires-python = ">=3.11"
# ///
"""Regenerate the README model table from mars.toml.

Usage:
    uv run scripts/models_table.py          # rewrite the table in README.md
    uv run scripts/models_table.py --check  # exit 1 if README.md is out of date

Each [models.<alias>] description may end with
"Value N, intelligence N, taste N." (taste optional); those become columns.
The table sits between the README markers below. Rows sort by intelligence,
then value, highest first; aliases without scores go last.
"""

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MARS = ROOT / "mars.toml"
README = ROOT / "README.md"
START = "<!-- models-table:start -->"
END = "<!-- models-table:end -->"
SCORES = re.compile(
    r"\s*Value (\d+), intelligence (\d+)(?:, taste (\d+))?\.\s*$"
)


def rows() -> list[str]:
    models = tomllib.loads(MARS.read_text())["models"]
    entries = []
    for alias, spec in models.items():
        desc = spec.get("description", "").strip()
        m = SCORES.search(desc)
        if m:
            value, intel, taste = m.group(1), m.group(2), m.group(3) or "—"
            desc = desc[: m.start()].strip()
            key = (0, -int(intel), -int(value), alias)
        else:
            value = intel = taste = "—"
            key = (1, 0, 0, alias)
        entries.append((key, f"| `{alias}` | {value} | {intel} | {taste} | {desc} |"))
    return [row for _, row in sorted(entries)]


def render() -> str:
    lines = [
        "| Alias | Value | Intelligence | Taste | Description |",
        "|---|---|---|---|---|",
        *rows(),
    ]
    return "\n".join(lines)


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
