---
name: llm-writing
type: guardrail
description: Load before writing any artifact. Every sentence you produce defaults toward LLM patterns; this skill catches them.
model-invocable: true
---

# LLM Writing

Load `/intent-modeling` if it isn't already loaded.

## Write Intentionally

Before producing a written artifact:

1. **Scope.** What does the reader know when they start, and what should they know when they finish? What do they not need to know? Name each beat and its idea before writing.
2. **Ground.** Check any relevant source material, references, or notes before writing.
3. **Draft.** Write a full draft to disk.
4. **Cut.** Scrutinize every word, every sentence, every section: what is the point of this? Is it correct? Is it consistent with what you already wrote? Does it tell the reader something they don't already know? If there is no point, delete it. Then reread for flow: does each idea connect to the one before it, and does the rhythm vary?

## What to Cut

- Writing to fill a section because it exists. Delete it or merge its content where it belongs.
- Labeling concepts without explaining how they work. Explain the mechanism or cut the label.
- Stating conclusions without evidence. Show the evidence or drop the claim.
- Hiding uncertainty behind confident language. Say what you don't know.
- Softening every claim with qualifiers ("it's worth noting," "it's important to consider"). Say it or don't.
- Repeating what you already said in different words, or summarizing the body as a conclusion ("In summary," "Overall"). Delete it.
- Connecting ideas with transition words instead of meaning ("Moreover," "Furthermore," "Additionally"). If the relationship isn't clear without the word, restructure.
- Pairing clauses where one half already carries the meaning ("It's not X, it's Y"). Keep the half that carries it.
- Writing for the person who asked for the document instead of the person who will read it. Write for the reader.
