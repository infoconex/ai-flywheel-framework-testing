# Prompt 010 — End-to-End Execution

## Purpose

Verify, without modifying the framework repository, that one coherent synthetic execution can move from creation through Execute, Observe, Evaluate, Classify, Adapt, Validate, Persist, Reuse, and terminal closure without identity drift, broken provenance, premature durability claims, or transaction inconsistency.

## Authorization

Use the framework revision supplied by the canonical runner. Read the manifest first and all manifest-required files in order. Resolve durable state, mission, and goal as context only. Construct all verification artifacts in memory and label displayed artifacts `PROPOSED ONLY — NOT WRITTEN`.

Do not inspect an application repository, mutate framework files, activate a durable execution, perform a durable lifecycle transition, create framework commits, or push framework changes.

## Required fixture

Use one stable execution identity and complete schema-valid synthetic mission and goal artifacts. Include:

- One approved, implemented, and passed adaptation.
- One rejected or deferred validation-ineligible adaptation.
- Evidence-backed observations and evaluations.
- Traceable classifications, decisions, findings, and approvals.
- A failed validation preserved with evidence, finding, recovery action, and authorized disposition.
- Checkpoint persistence when a transition first introduces an externally referenced durable record.
- A complete final Persist plan with planned Reuse assessments.
- A separate Reuse transaction that completes assessments, creates or supersedes knowledge, closes the execution, completes the goal and mission, and clears state pointers.

## Required verification

Verify all lifecycle boundaries in order, including stage metadata, sole-active-stage rules, whole-second UTC timestamps, stable mission/goal/execution identities, state agreement, reference resolution, acceptance-criterion evidence mapping, retained-SHA compare-and-swap, deterministic target ordering, commit-marker finalization, final-pair verification, rollback or compensation, and repository immutability.

Checkpoint plans must persist supporting records before execution and state. They must not be treated as lifecycle Persist completion or promote knowledge. The final Persist transaction must not recreate unchanged checkpoint artifacts. Reuse must not begin until Persist and its controlling plan are terminal and verified.

Terminal form requires all eight stages completed or justified not applicable, execution succeeded with complete outcome and completion data, goal and mission completed, state ready, and all active pointers null.

## Negative validation

Demonstrate deterministic rejection of at least 44 invalid cases covering identity drift, lifecycle overlap or skipping, unsupported provenance, missing approvals, invalid adaptation eligibility, evidence-free validation, rewritten failed validation, missing checkpoint durability, incomplete or self-targeting plans, stale CAS, premature transaction values, invalid assessment lifecycle, unqualified or duplicate/conflicting knowledge, incomplete terminal artifacts, missing acceptance-criterion evidence, stale references, unsynchronized adaptation statuses, partial writes without recovery, unplanned changes, and actual framework mutation.

## Result requirements

Produce exactly 20 numbered top-level sections:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Synthetic Mission and Goal
5. Stable Execution Identity
6. Lifecycle Transition Trace
7. Checkpoint Persistence Results
8. Cross-Stage Provenance Findings
9. Representative Execution Record Set
10. Final Persist Plan and Planned Assessments
11. Reuse Assessment and Knowledge Set
12. Reuse Persistence Plan
13. Acceptance-Criterion Evidence Mapping
14. Terminal Execution, Goal, Mission, and State
15. Validation Results
16. Negative Validation Results
17. Commit-Marker, Compare-and-Swap, and Recovery Results
18. Framework Defects
19. Repository Mutation Confirmation
20. Next Authorized Action

Report only reusable framework defects. Stop after the next authorized action.