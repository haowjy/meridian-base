---
name: decision-log
type: reference
description: Use when making design choices — record why, not just what, with rejected alternatives.
model-invocable: true
---

# Decision Log

Record decisions while the reasoning is fresh. Reasoning flattens the longer
you wait — capture it in the moment, not retroactively.

A decision record makes the LLM's understanding visible: what the human
said, what you interpreted their intent to be, what goal you derived from
that, and what you chose based on that understanding. If the interpretation
is wrong, the record makes it checkable and correctable before the
misreading gets baked into code or artifacts.

The rejected alternatives are often the most valuable part. They prevent
the next person from re-proposing what was already considered.

Design decisions go in design docs. Implementation decisions go in commit
messages or inline comments. Anything structural goes in the work directory.

Skip boilerplate decisions that follow directly from project conventions.
The test: would you want this context if you were reading this code for the
first time?
