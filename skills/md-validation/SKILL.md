---
name: md-validation
description: "Load after writing, moving, or linking markdown pages or Mermaid diagrams, before committing them: validates links, the KB link graph, and diagram syntax."
metadata:
  type: reference
---

# Markdown Validation

Validate links before committing documentation changes, and read the link graph
before and after restructuring a tree. Validate Mermaid syntax after diagram
edits. Fix every reported issue and repeat the validation until it is clean.

The validators' commands, warning categories, suppression comments, and ignore
files belong to your runtime; read its Markdown-validation guidance before
running them.

When a warning marks a construct you meant, suppress only that category, as
narrowly as the validator allows, with the reason beside the diagram. Exclude
generated or vendored material from validation; never exclude a broken page
that belongs to the tree.

See `resources/mermaid-authoring.md` for diagram authoring rules.
