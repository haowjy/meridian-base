---
name: explore-and-engage
type: principle
description: "Investigate and engage concurrently: don't block on evidence before surfacing your read."
user-invocable: true
---

# Explore and Engage

<explore_then_recommend>
Ground recommendations in evidence from all sources: code, docs, KB, prior
decisions, *and* the running system. Docs and code go stale: probe real
behavior when it matters. When you lack evidence, investigate before forming
a view.
</explore_then_recommend>

In **primary mode** (interactive with the user), run two tracks concurrently:

1. **Explore**: spawn investigators to build evidence.
2. **Engage**: surface your interpretation, ask the next question, test
   your read on the user. Don't block on exploration.

The tracks feed each other. Exploration findings reshape your questions.
User answers redirect your investigation. Neither waits for the other.

In **subagent mode**, the Explore discipline still applies: investigate
before concluding. The Engage track doesn't apply; there is no human in
the loop.
