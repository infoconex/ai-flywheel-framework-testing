# Prompt 011 — Resume Interrupted Execution

## Purpose

Verify, without modifying the framework repository, that a fresh operator session can discover, validate, and safely resume a durable interrupted execution using only repository artifacts, without chat history, identity changes, repeated completed work, lost evidence, stale overwrites, or lifecycle contradiction.

## Authorization

Use the immutable framework revision supplied by the canonical runner. Read the manifest first and all required files in manifest order. Resolve durable state, mission, goal, records, and execution from repository artifacts only. Construct synthetic fixtures in memory and label displayed artifacts `PROPOSED ONLY — NOT WRITTEN`.

Do not resume or mutate the real durable execution, update state, inspect an application repository, create framework commits, or push changes.

## Required fixture

Construct one complete interrupted execution/state pair with stable mission, goal, execution, operator, timestamps, lifecycle history, references, and retained revisions. The execution must be resumable rather than terminal, and its interruption reason and last durable checkpoint must be explicit.

Construct the proposed resumed execution/state pair. Preserve all completed work, evidence, records, lifecycle history, and immutable identities. Resume only the correct active stage and do not repeat completed actions.

## Required verification

Verify:

- Fresh-session startup and unique active-reference resolution.
- Schema validity and semantic consistency of the interrupted and resumed pairs.
- Stable execution identity and mission/goal ownership.
- Exactly one active lifecycle stage before and after resume.
- No completed stage or action is repeated.
- All references remain resolvable and evidence is preserved.
- Resume authorization and blocker handling.
- Whole-second UTC timestamp ordering.
- Retained-SHA compare-and-swap for execution and state.
- Execution-first/state-second write order, final-pair verification, and exact rollback or reconciliation after partial failure.
- Repository immutability during verification.

## Negative validation

Demonstrate deterministic rejection of at least 24 invalid cases covering missing or ambiguous active references, identity mismatch, terminal execution resume, stage disagreement, repeated work, missing evidence, stale references, timestamp regression, unauthorized resume, unresolved blockers, stale execution or state SHA, reversed write order, missing final verification, partial transition without recovery, and actual framework mutation.

## Result requirements

Produce exactly 14 numbered top-level sections:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Interrupted Execution Snapshot
5. Resume Authorization Decision
6. Proposed Resumed Execution Artifact
7. Proposed Resumed State Artifact
8. Work-Preservation and Reference Results
9. Schema and Lifecycle Results
10. Compare-and-Swap and Recovery Results
11. Negative Validation Results
12. Framework Defects
13. Repository Mutation Confirmation
14. Next Authorized Action

Report only reusable framework defects. Stop after the next authorized action.