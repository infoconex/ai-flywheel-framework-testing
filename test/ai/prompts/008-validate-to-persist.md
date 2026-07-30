# Prompt 008 — Validate to Persist

## Purpose

Verify, without mutating the framework repository, that a valid execution can complete Validate and activate Persist only when validation coverage, evidence, findings, recovery actions, adaptation status, and persistence planning satisfy the current contracts.

The revision-specific runner supplies immutable revisions and publication details.

## Authorization

Use the pinned `Infoconex/ai-flywheel-framework` revision. Read the manifest first and all required files in order. Construct complete synthetic artifacts in memory only. Do not mutate the framework repository, inspect an application repository, perform persistence, invent evidence, or create alternate results.

Label every displayed artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Starting snapshot

Construct a schema-valid resumable execution/state pair where Validate is the sole in-progress stage, Execute through Adapt are completed, and Persist and Reuse are pending.

Include complete structured validation coverage for every eligible adaptation. Every required validation must be executed; passed and failed results must have sufficient evidence; failures must identify a finding and recovery action; adaptation validation statuses must agree with validation outcomes.

Include a schema-valid planned persistence plan before Persist activation. It must enumerate every proposed new or changed durable artifact, canonical path, operation, mutability, dependency, precondition, proposed digest, write order, rollback behavior, recovery state, and final-verification requirement.

## Proposed transition

Construct the complete proposed post-transition pair:

- Validate becomes completed with summary, timestamps, and validation references.
- Persist becomes the sole in-progress stage.
- Reuse remains pending.
- Execution remains in progress.
- State references the same execution and sets `lifecycle_stage: persist`.
- One whole-second UTC transition instant is used and unrelated state fields are preserved.

No persistence target is actually written.

## Validation

Validate YAML 1.2, Draft 2020-12 schemas with formats, validation eligibility and coverage, evidence sufficiency, failed-result finding/recovery linkage, adaptation/result agreement, persistence-plan completeness and ordering, lifecycle order, sole active stage, timestamps, state/execution agreement, retained-SHA prechecks, execution-first/state-second compare-and-swap, final pair verification, partial-transition rollback/finding behavior, and repository immutability.

## Required negative cases

Report exactly 18 deterministic rejections:

1. Validate completes with an eligible adaptation lacking coverage.
2. A required validation remains pending.
3. A passed result lacks evidence.
4. A failed result lacks evidence.
5. A failed result lacks a finding.
6. A failed result lacks a recovery action.
7. Adaptation validation status conflicts with validation results.
8. A validation-ineligible adaptation is marked passed.
9. Validate stage has no references or summary.
10. Persist starts without a persistence plan.
11. The persistence plan omits a changed artifact.
12. A target lacks canonical path, operation, mutability, dependency, precondition, digest, or rollback data.
13. Write order places state before supporting records or execution.
14. A create target lacks an absence precondition.
15. An update target lacks retained-SHA compare-and-swap.
16. Validate and Persist are both in progress.
17. Either retained SHA changes before the first write.
18. Persistence or repository work begins before final pair verification.

## Result format

Produce exactly 11 numbered sections:

1. Verification Summary
2. Validation Trace
3. Starting Operating Snapshot
4. Transition Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Validation and Persistence-Plan Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

If no reusable defect exists, state exactly:

> No reusable framework defects were found during the non-persistent Validate-to-Persist lifecycle verification.

Only the revision-specific runner may authorize writing the canonical result.