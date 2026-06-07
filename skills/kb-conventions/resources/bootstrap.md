# KB Bootstrap

Starter layout for a new project KB. Adapt to your project — not every
project needs all layers.

## Suggested Directory Layout

```
kb/
  AGENTS.md          # governance — what the KB is, writing rules, validation
  index.md           # catalog of pages with one-line summaries
  decisions.md       # decision index — what, when, link to rationale
  vocab.md           # project-wide terminology
  sources/           # raw material: articles, research, transcripts. Immutable.
  decisions/         # reasoning: why a source matters, what was chosen/rejected
  wiki/              # synthesized knowledge pages, owned and maintained by agents
  log/               # audit trail: what changed in the wiki and why
  trash/             # superseded content, not maintained
```

## Five Layers

**Sources** — raw material: articles, research, transcripts, data. Immutable.
The LLM reads from sources but never modifies them.

**Decisions** — the reasoning layer. Why a source matters, why the wiki is
shaped the way it is, what was chosen and rejected. Decisions connect sources
to knowledge by explaining the interpretation and judgment applied.

**Wiki** — synthesized knowledge pages. How things work, concepts,
architecture. The LLM owns this layer: creates pages, updates them, maintains
cross-references, keeps everything consistent. Shaped by the decisions.

**Log** — what changed in the wiki and why. The audit trail of how the KB
evolved — what was added, updated, or restructured, and what triggered it.

**Schema** (`AGENTS.md`) — user-defined governance. Defines layer structure,
conventions, and workflows.
