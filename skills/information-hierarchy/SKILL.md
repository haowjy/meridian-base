---
name: information-hierarchy
type: principle
description: |
  Load before producing human-facing output. Pick modality and disclosure tier
  per beat; place what matters first.
model-invocable: true
---

# Information Hierarchy

Present information well — words, examples, diagrams, charts, mockups, as each
beat needs. The reader should get the answer in the first thing they see; depth
should be there when they reach for it and invisible when they don't. Simplest
carrier wins.

## Workflow

1. **Scope beats.** Break the output into beats — each carries one idea the
   reader needs (see `/llm-writing`).
2. **Pick a modality per beat.** Prose is the default; switch only when another
   form carries the beat better.
3. **Place by disclosure tier.** Answer first, depth behind it, sources last.
4. **Pick the carrier.** The simplest medium that presents every beat well.
5. **Apply layout mechanisms** so tier 1 is scannable.

## Modalities

- **Prose** — default. One idea per paragraph.
- **Example** — when the general claim is abstract; one concrete case beats a
  second paragraph of explanation.
- **Diagram** — when the *relationship* is the hard part. ~5–12 nodes, placed
  after the prose it illustrates, never instead of it. Validate with
  `meridian mermaid check` (`/md-validation`).
- **Chart** — quantities, trends, distributions.
- **Table** — short enumerable facts; explanation goes in surrounding prose.
- **Mockup** — when the reader must *see* a layout or plan, not read about it.
- **Link / child page** — depth that most readers won't need.

## Disclosure tiers

- **T1 Answer** — what the reader came for. First screen, first paragraph.
- **T2 Depth** — reasoning, evidence, examples, sub-structure. Flat carriers:
  omit and link out. Rich carriers: expand, hover, or tap.
- **T3 Sources** — citations and further reading. Footer or link list, never
  inline in T1.

**Flat vs rich carriers.** Chat, email, and most docs cannot hide content —
earn density: every sentence in T1 must pay for itself, and T2 becomes a link,
not a section. HTML and apps may disclose in place (collapse, popover, child
page) when it genuinely helps the reader, not to decorate. Two extremes for
calibration: a slide title carries the takeaway, not a topic label ("Cache
misses double p99", not "Performance"); a UI string is T1 alone — if it needs
a paragraph, the design is wrong, not the copy.

## Layout mechanisms

These make T1 scannable; they are not disclosure tiers.

- **Headers** — one idea each; a reader skimming only headers should follow the
  argument.
- **Table of contents** — long documents only.
- **Asides** — callouts for context the main thread doesn't need.
- **Footers** — sources, next steps.
- **Hover/tap popovers** — rich carriers only, for T2 depth.

## Constraints

- **Mobile-first.** Design for a narrow viewport; wider layouts are
  enhancements.
- **Light mode default** with dark toggle on HTML (`:root` variables, `.dark`
  class).
- **Agent-agnostic.** No assumptions about which model or agent pack renders
  the output.

## Anti-patterns

- Diagram replaces prose — the reader learns less than from a paragraph.
- No lede — the answer is buried under setup.
- Conflating layout with disclosure — headers and asides don't hide anything.
- Widget theater — interaction that demos features instead of presenting
  information.
- Carrier overbuild — an HTML site where a tight reply would have done.
- Unverifiable output — broken links, invalid Mermaid, claims without sources.
- Dark-only desktop layouts.

## Sources

- [How Users Read on the Web (NN/g)](https://www.nngroup.com/articles/how-users-read-on-the-web/) —
  scanning, why the lede must come first.
- [Progressive Disclosure (NN/g)](https://www.nngroup.com/articles/progressive-disclosure/) —
  defer secondary content to secondary screens.
