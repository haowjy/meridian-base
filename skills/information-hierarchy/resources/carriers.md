# Carriers

How disclosure tiers and modalities land on each carrier. The skill body has
the tiers (T1 answer, T2 depth, T3 sources); this shows what they look like in
practice.

## Chat reply

Flat. The first paragraph is T1 — the answer, not a preamble. T2 is a short
supporting section or a link to a file/URL. T3 is a trailing link list only if
the reader will actually follow it. If the reply needs a table of contents, it
should have been a document.

## Markdown document

Flat, but structured. Lede paragraph carries T1. Headers carry the argument for
skimmers. T2 lives in later sections or linked pages — never in a wall the
reader must cross to reach the point. Asides (blockquotes, callouts) hold
context the main thread doesn't need. T3 is a reference-style link footer.

Diagrams: place a small Mermaid block after the prose it illustrates; run
`meridian mermaid check` before committing.

## Static HTML (single or multi-page)

Rich. T1 is the first viewport of `index.html`. T2 may disclose in place —
`<details>`, popovers, or child pages linked from the index. T3 is a footer.
Multi-page: the index is a map, each child page owns one beat cluster. Build
mechanics: `/structured-artifact`.

## Slides

One beat per slide; the slide title is the takeaway, not a topic label ("Cache
misses double p99" not "Performance"). T2 goes in speaker notes or an appendix
section. Never paste a document onto slides.

## UI strings / product copy

T1 only — the label or message must carry the meaning alone. T2 is a tooltip or
help link at most. If a control needs a paragraph of explanation, the design is
wrong, not the copy.

## Email

Flat and hostile to depth. Subject line is the lede. First two sentences carry
T1. Anything past one screen gets cut or moved to an attachment/link.

## Sources

- [How Users Read on the Web (NN/g)](https://www.nngroup.com/articles/how-users-read-on-the-web/) —
  scanning, F-pattern, why the lede must come first.
- [Progressive Disclosure (NN/g)](https://www.nngroup.com/articles/progressive-disclosure/) —
  defer secondary content to secondary screens.
- [Visual Hierarchy (IxDF)](https://www.interaction-design.org/literature/topics/visual-hierarchy) —
  size, contrast, and placement signal importance.
