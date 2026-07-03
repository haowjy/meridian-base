---
name: structured-artifact
type: reference
description: |
  Load when building a static HTML artifact — single page or multi-page site —
  to make structured information explorable through layout and navigation.
model-invocable: false
---

# Structured Artifact

Load `/information-hierarchy` first — it decides what each page shows and in
what order; this skill is the build mechanism.

## Shape

- **Single page** — one `index.html` when the content fits one map: first
  viewport carries the answer, depth discloses in place (`<details>`, popovers,
  collapsible detail panel).
- **Multi-page** — a folder (`index.html` + child pages + `shared.css`) when
  the structure earns navigation: the index is a map with links, each child
  page owns one cluster of beats. See `resources/multi-page-site.md`.

## Ground rules

- **Static, no build step.** CDN `<script>` tags. No npm, no bundler.
- **Mobile-first.** Narrow viewport is the design target; wider layouts are
  enhancements. Touch targets ≥ 44px, pan/pinch on diagrams.
- **Light mode default with toggle.** Colors from CSS custom properties on
  `:root`; dark mode adds `.dark` to `<html>`. ☀/🌙 button in the toolbar.
- **Validate diagrams.** Mermaid goes through `meridian mermaid check`
  (`/md-validation`) before you call the artifact done.

`resources/layout-and-theme.md` has the concrete layout, theme, and mobile
patterns shared across everything below.

## Enrichments

Load a resource only when a beat calls for its pattern:

| Pattern | When a beat needs | Resource |
|---|---|---|
| Multi-page site | Index + child pages, nav, cross-links | `resources/multi-page-site.md` |
| Mockup | Wireframe or annotated plan the reader must see | `resources/mockups.md` |
| Diagram | Dependencies, flow, system maps | `resources/diagrams.md` |
| Data table | Records with sortable/filterable columns | `resources/data-table.md` |
| Data chart | Quantities, trends, distributions | `resources/data-chart.md` |
| Timeline | Chronological events with detail | `resources/timeline.md` |
| Tree / TOC | Hierarchy navigation, document outline | `resources/tree-and-toc.md` |
| Card grid | Items with summary + expandable detail | `resources/card-grid.md` |
| Diff / comparison | Before/after, version diff | `resources/diff-view.md` |

For custom node rendering, drag, or live filtering on graphs beyond what
Mermaid offers, see `resources/experimental-react-flow.md`.
