# Prompt 012 — Recover Partial Lifecycle Transition

## Purpose

Verify, without modifying the framework repository, that a fresh operator session can detect and recover a lifecycle transition interrupted after the execution update but before the state update, using only durable repository artifacts and exact retained revisions.

## Authorization

Use the immutable framework revision supplied by the canonical runner. Read the manifest first and all required files in manifest order. Resolve durable state, mission, goal, execution, transition plan, findings, and relevant revisions from repository artifacts only. Construct all recovery fixtures in memory and label displayed artifacts `PROPOSED ONLY — NOT WRITTEN`.

Do not alter the real execution or state, perform rollback or forward completion, inspect an application repository, create framework commits, or push changes.

## Required fixture

Construct a complete partial-transition condition in which:

- The execution reflects the successor lifecycle stage.
- State still reflects the predecessor lifecycle stage.
- A durable transition plan identifies the intended pair, retained SHAs or digests, write order, and recovery behavior.
- The execution write is verifiably complete.
- The state write is absent or failed.
- No later goal-directed work has begun.

Construct both legal recovery choices when allowed by the contracts: exact rollback to the retained execution bytes, or guarded forward completion to the already validated proposed state. Select the deterministic authorized outcome from the fixture conditions.

## Required verification

Verify startup detection, mismatch classification, plan and reference resolution, exact byte/digest agreement, authorization, no-guess boundaries, schema and semantic validity, whole-second UTC ordering, retained-SHA compare-and-swap, recovery write ordering, final-pair verification, durable recovery finding completeness, blocker handling, idempotent fresh-session rediscovery, and repository immutability.

The recovery finding must identify the transition, affected artifacts, expected and observed revisions, completed and failed writes, selected recovery action, outcome, operator, timestamps, evidence, and any required human reconciliation.

## Negative validation

Demonstrate deterministic rejection of at least 24 invalid cases covering absent or ambiguous plans, mismatched identities, unknown retained bytes, stale SHAs, unverified execution write, later work already begun, unauthorized forward completion, unsafe rollback, missing recovery finding fields, conflicting recovery attempts, repeated recovery, timestamp regression, incomplete final verification, unresolved inconsistency, and actual framework mutation.

## Result requirements

Produce exactly 15 numbered top-level sections:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Partial Transition Snapshot
5. Detection and Classification Results
6. Recovery Authorization Decision
7. Proposed Recovery Execution Artifact
8. Proposed Recovery State Artifact
9. Proposed Recovery Finding
10. Schema and Semantic Results
11. Compare-and-Swap and Final-Pair Results
12. Negative Validation Results
13. Framework Defects
14. Repository Mutation Confirmation
15. Next Authorized Action

Report only reusable framework defects. Stop after the next authorized action.