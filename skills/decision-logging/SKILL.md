---
name: decision-logging
type: principle
description: Record decisions where they're made — why, not just what.
detail: Log significant decisions close to where they're made so the next reader understands why.
model-invocable: true
---

# Decision Logging

Record significant decisions close to where they're made. When you choose
between alternatives, reject an approach, or make a tradeoff — log it so
the next reader understands why, not just what. Decisions that live only in
conversation context will be lost to compaction.

Design decisions go in design docs. Implementation decisions go in commit
messages or inline comments. Anything structural goes in the work directory.

Load /decision-log for format and placement conventions.
