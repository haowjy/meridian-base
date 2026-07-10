---
name: structured-artifact
type: reference
description: |
  Load when building a static HTML artifact: single page or multi-page site
  to make structured information explorable through layout and navigation.
model-invocable: false
---

# Structured Artifact

Plain HTML that opens from `file://` and works on a phone. Load
`/information-hierarchy` first: it decides what each page shows and in what
order; this skill builds it.

## Show before you tell

Default to diagrams, tables, and interactive layouts over prose.
`resources/diagrams.md` for relationships and flow,
`resources/data-table.md` for structured comparisons,
`resources/mockups.md` for layouts. Prose is for linear narrative with no
spatial structure. When in doubt, draw it.

## One page or several

- **Single page**: one question, layered depth. Reports, dashboards,
  comparisons. Disclose with `<details>`, popovers, collapsible panels.

- **Multi-page**: distinct topics that stand alone. Architecture sections,
  system components, separate concerns. `index.html` as map, child pages
  with shared nav and `shared.css`.

Default to multi-page when there are 3+ topics.
`resources/multi-page-site.md` for folder mechanics.

## Build so it keeps working

Ship static — plain `<script>` tags, zero build step. CDN tags by default;
vendor scripts when the artifact must work offline
(`resources/layout-and-theme.md`).

Resource snippets are pinned to a major version. Web-search the library's
current version before building rather than trusting the snippet.

Narrow viewport first; wider layouts are enhancements. Touch targets ≥ 44px.
Colors from CSS custom properties on `:root`, default light, ☀/🌙 toggle
adds `.dark` to `<html>`.

`resources/layout-and-theme.md` has layout, theme, and mobile patterns.

## Serve it

Serve the artifact so the team can browse it live. Use whichever is
available: `meridian artifact serve .`, `tailscale serve`, or a local
HTTP server (`python -m http.server`).

## Verify

Check in a browser: first viewport carries the answer, pages render at
~375px, theme toggle works on both text and embedded content, cross-links
resolve, Mermaid passes `meridian mermaid check` (`/md-validation`).

## Enrichments

| Pattern | When | Resource |
|---|---|---|
| Multi-page site | 3+ distinct topics | `resources/multi-page-site.md` |
| Mockup | Layout the reader must see | `resources/mockups.md` |
| Diagram | Relationships, flow, system maps | `resources/diagrams.md` |
| Data table | Sortable/filterable records | `resources/data-table.md` |
| Data chart | Quantities, trends, distributions | `resources/data-chart.md` |
| Timeline | Chronological events | `resources/timeline.md` |
| Tree / TOC | Hierarchy, document outline | `resources/tree-and-toc.md` |
| Card grid | Items with expandable detail | `resources/card-grid.md` |
| Diff / comparison | Before/after, version diff | `resources/diff-view.md` |

For custom node rendering or live filtering beyond Mermaid, see
`resources/experimental-react-flow.md`.
