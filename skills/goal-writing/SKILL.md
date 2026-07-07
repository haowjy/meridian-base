---
name: goal-writing
type: reference
description: >
  Load when turning intent into an executable goal for an agent, spawn, work
  item, experiment, or handoff. Use to define outcome, evidence, constraints,
  anti-goals, stop conditions, and reporting shape before work begins.
model-invocable: true
---

# Goal Writing

Use this skill when a task needs a goal that another agent or future session can
execute without reinterpreting intent.

A goal is the control surface for agent work. It says what should become true,
what evidence proves it, and what the agent must not do while pursuing it. A loop
is only one way to execute a goal; do not make looping the primitive.

## What a Good Goal Needs

Write goals with the parts that change behavior:

1. **Outcome.** What should be observably true when the work succeeds?
2. **Why.** What decision, user need, or research question does this unblock?
3. **Ground truth.** What files, artifacts, prior decisions, baselines, or current
   state should the agent treat as authoritative?
4. **Scope.** What is in scope, out of scope, and not to be changed?
5. **Priority.** If goals conflict, which outcome wins and which tradeoff is
   acceptable?
6. **Constraints.** Cost, time, risk, compatibility, safety, compute, style, or
   process limits.
7. **Evidence.** What command, metric, artifact, review, citation, run, or
   observation proves the outcome?
8. **Anti-goals.** What would be a bad way to achieve the metric or an invalid
   shortcut?
9. **Redesign protocol.** What core invariant is frozen, which mechanisms are
   negotiable, and what numeric trigger makes repeated failure a design verdict?
10. **Stop / ask conditions.** When should the agent stop, ask, defer, or declare
   the goal blocked?
11. **Report shape.** What should come back: changes, findings, decision,
   validation evidence, open risks, or next step?

Do not fill every slot with boilerplate. Name only the information that would
change what the agent does.

Name the frozen core separately from the negotiable mechanisms. If a mechanism
can change while preserving the outcome, say so up front. Give the agent a
numeric redesign trigger, e.g. "N failed rounds on one mechanism means
redesign through the divergence protocol, not another patch." Require a brief
DIVERGE note or equivalent audit trail so pivots are protocol, not crisis.

## Optimization Goals

Optimization goals need extra guardrails because agents can satisfy a narrow
metric while damaging the real objective.

For any goal shaped like "improve X," specify:

- the metric or observable target,
- the baseline being compared against,
- the allowed search space,
- the invariants that must not regress,
- the data, benchmark, evaluator, or review gate that cannot be changed,
- what counts as cheating, leakage, overfitting, cherry-picking, or metric gaming,
- how many attempts, how much budget, or what escalation threshold applies,
- what evidence must be reported for all meaningful attempts, not only the best
  attempt.

If the strategy is unknown, write a learning goal first: identify mechanisms,
baselines, constraints, or promising directions. Do not force a performance goal
before the agent has a credible path to improve it.

## Quality Checks

Before handing off a goal, check:

- **Specific:** Could two agents read it and aim at the same outcome?
- **Observable:** Can success be verified without trusting the agent's opinion?
- **Bounded:** Does it prevent adjacent work from expanding silently?
- **Grounded:** Does it name the artifacts, baseline, or state needed to begin?
- **Honest:** Does it define invalid shortcuts and ways the result could be fake?
- **Calibrated:** Is this a performance goal when the path is known, or a
  learning goal when the path is uncertain?
- **Actionable:** Does the agent have a plausible next action?
- **Reportable:** Will the final answer include enough evidence to decide what
  to do next?

If a goal fails these checks, rewrite it before spawning or starting the work.

## When the Goal Drives a Loop

Some goals require repeated attempts. Add loop mechanics only when feedback from
one attempt should change the next attempt.

For loop-driven goals, specify:

- what changes between attempts,
- what signal is observed after each attempt,
- how the signal is compared to the target or baseline,
- what memory or log is updated,
- when to continue, branch, stop, or ask,
- who reviews the loop when cheating or metric gaming is possible.

A loop without a clear goal is drift. A goal without feedback is wishful
thinking. Keep the goal primary and the loop accountable to it.

## Reviewer Gates

Use an independent reviewer when the goal creates incentives to cheat, hide
failures, overfit, or reinterpret success after the fact.

Ask the reviewer to check:

- whether the metric matches the real objective,
- whether the baseline and data were preserved,
- whether failures and non-best attempts were reported,
- whether constraints were violated,
- whether the claimed success follows from the evidence,
- what would change their mind.

For research and benchmark work, prefer reviewer gates before promotion, not
after the result has already been written as a win.

## Handoff Template

```markdown
Goal: <observable outcome>

Why: <decision, user need, or research question this unblocks>

Ground truth:
- <files, artifacts, baselines, prior decisions, current state>

Scope:
- In: <owned work>
- Out: <explicit exclusions>

Priority / tradeoffs:
- <what wins when objectives conflict>

Constraints:
- <limits, invariants, cost/risk boundaries>

Anti-goals / invalid shortcuts:
- <ways not to win>

Evidence of success:
- <commands, metrics, artifacts, citations, review gates, or observations>

Stop / ask if:
- <ambiguity, risk, budget, blocker, or cheating concern>

Redesign trigger:
- <frozen core, negotiable mechanisms, N failed rounds, DIVERGE/audit note>

Report back with:
- <summary shape and evidence>
```

Keep the template terse. Delete sections that do not change the agent's behavior.
