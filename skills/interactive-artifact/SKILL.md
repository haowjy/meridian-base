---
name: interactive-artifact
type: reference
description: |
  Build a self-contained, interactive HTML artifact that makes complex information
  explorable — click a node to drill into detail. Use it to map a knowledge base, a
  codebase, a data model, or any structured subject.
model-invocable: false
---

# Interactive Artifact

- **Mermaid by default.** Keep a diagram to ~5-12 nodes; split larger subjects across
  several. Validate with `/md-validation` before finalizing. For custom node rendering,
  drag, or live filtering, see `resources/experimental-react-flow.md`.
- **Overview first, detail on click.** Clicking a node opens a panel with its
  description and a relevant, syntax-highlighted snippet.
- **Link each node back to its source** so the viewer can verify it.
- **Works on a phone.** Responsive layout, touch pan and pinch-zoom, detail panel as a
  bottom sheet on narrow screens.
- **Static, no build step.** Load libraries from CDN (Mermaid, Tailwind, Shiki). Match
  structure to the subject: a single interactive view is one HTML file; several pages the
  viewer navigates between is a folder of static HTML/CSS/JS.

`resources/html-patterns.md` has the concrete implementation: CDN setup, Mermaid config,
click-callback wiring, detail panel, pan/zoom, mobile, and serving the folder over
Tailscale.
