---
name: structured-artifact
type: reference
description: |
  Load when building a static HTML artifact — single page or multi-page site —
  to make structured information explorable through layout and navigation.
model-invocable: false
---

# Structured Artifact

A structured artifact is plain HTML that opens from `file://` and works on a
phone. Load `/information-hierarchy` first — it decides what each page shows
and in what order; this skill builds it.

## One page or several

Start from one `index.html`. Its first viewport carries the answer, and depth
discloses in place — `<details>`, popovers, a collapsible detail panel. Grow
into a folder (`index.html` + child pages + `shared.css`) when readers need
whole pages per branch: the index becomes a map with links, and each child
page stands alone with its own lede. `resources/multi-page-site.md` has the
folder mechanics.

## Build so it keeps working

Everything ships static — CDN `<script>` tags, zero build step — so the
artifact opens anywhere, years later, with nothing installed. Design for a
narrow viewport and let wider layouts be enhancements; touch targets stay
≥ 44px and diagrams pan and pinch. Drive colors from CSS custom properties on
`:root`, default light, with a ☀/🌙 toggle that adds `.dark` to `<html>` —
readers get a readable page in daylight and a choice at night. Run Mermaid
through `meridian mermaid check` (`/md-validation`) before calling the
artifact done, so every diagram a reader meets actually renders.

`resources/layout-and-theme.md` has the concrete layout, theme, and mobile
patterns shared across everything below.

## Enrichments

Load a resource when a beat calls for its pattern:

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
