---
name: information-hierarchy
type: principle
description: |
  Load for large human-facing outputs: reports, docs, multi-section
  explanations, artifacts. Choose the right form for each beat (prose, diagram,
  table, mockup) and put the answer first, depth behind it. If the medium allows, use progressive disclosure.
model-invocable: true
---

# Information Hierarchy

The reader should get the answer in the first thing they see, and find depth
only when they reach for it. Everything else here follows from that: each beat
of the piece takes the form that carries it best, what matters most comes
first, and the medium stays as simple as the content allows.

## The answer leads

Readers scan; they don't read top to bottom. A lede that states the finding —
not the setup — is the difference between a piece that works in thirty seconds
and one that gets skimmed and abandoned. The same logic repeats at every
scale: a section's first sentence is its answer, a slide's title is its
takeaway ("Cache misses double p99", not "Performance"), a UI label carries
its whole meaning alone.

Behind the answer sits depth — reasoning, evidence, edge cases — and behind
that, sources. Depth that most readers won't need doesn't have to be deleted;
it has to be *moved*: a later section, a linked page, a footnote. Sources
belong at the end, never woven through the opening.

## Each beat, its best form

Prose is the default; break from it when another form genuinely carries the
idea better. An example grounds an abstract claim faster than more
explanation. A table holds enumerable facts that prose would bury. A chart
shows a trend that a sentence can only assert. A diagram earns its place when
the *relationship* is the hard part — a handful of nodes, set after the prose
it illustrates, validated (`meridian mermaid check`, see `/md-validation`). A
mockup shows a layout the reader would otherwise have to imagine.

The failure mode runs both directions: a diagram standing in for an
explanation teaches less than a paragraph, and a wall of prose describing a
table wastes the reader's time. Ask what the beat is trying to do, then give
it the form that does that.

## The medium can hide; most can't

Chat, email, and plain documents show everything at once, so hierarchy there
means density and order — every early sentence pays for itself, and depth
lives behind a link rather than in the reader's way. Richer media (HTML,
apps) can genuinely hide things: collapsed sections, popovers, child pages.
Use that when it serves the reader, not to decorate — interaction that demos
itself is noise wearing a costume.

Structure helps the scanner either way: headers that carry the argument on
their own, asides for context off the main thread, a table of contents when
the piece is long enough to need a map. These make the surface scannable;
they don't hide anything, and don't substitute for putting the answer first.

Choose the simplest medium that presents every beat well. An HTML site where
a tight reply would do costs the reader more than it gives. When HTML is
earned, it should work on a phone first and default to light mode
(`/structured-artifact` has the mechanics).

## Sources

- [How Users Read on the Web (NN/g)](https://www.nngroup.com/articles/how-users-read-on-the-web/) —
  scanning, why the lede must come first.
- [Progressive Disclosure (NN/g)](https://www.nngroup.com/articles/progressive-disclosure/) —
  defer secondary content to secondary screens.
