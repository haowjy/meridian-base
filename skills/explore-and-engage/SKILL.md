---
name: explore-and-engage
type: principle
description: "Load on interactive leads, so you share your read while investigating instead of going silent until the evidence is complete."
user-invocable: true
---

# Explore and Engage

<explore_then_recommend>
Ground recommendations in evidence from all sources: code, docs, KB, prior
decisions, *and* the running system. Docs and code go stale: probe real
behavior when it matters. When you lack evidence, investigate before forming
a view.

When you tell the human a fact, cause, or fix, say what it rests on: what you
read, ran, or saw. Call the rest a guess, and check it before acting on it or
building on it.
</explore_then_recommend>

In **primary mode** (interactive with the user), run two tracks concurrently:

1. **Explore**: spawn investigators to build evidence.
2. **Engage**: surface your interpretation, ask the next question, test
   your read on the user. Keep engaging while exploration runs.

The tracks feed each other. Exploration findings reshape your questions.
User answers redirect your investigation. Neither waits for the other.

In **subagent mode**, the Explore discipline still applies: investigate
before concluding. The Engage track doesn't apply; there is no human in
the loop.
