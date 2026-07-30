# Prompt 007 — Adapt to Validate

## Purpose

Verify, without mutating the framework repository, that a valid execution can complete Adapt and activate Validate only when adaptation disposition, implementation, approval, and validation planning satisfy the current contracts.

The revision-specific runner supplies immutable revisions and publication details.

## Authorization

Use the pinned `Infoconex/ai-flywheel-framework` revision. Read the manifest first and all required files in order. Construct complete synthetic artifacts in memory only. Do not mutate the framework repository, inspect an application repository, invent approval or authority, execute real validation, or create alternate results.

Label every displayed artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Starting snapshot

Construct a schema-valid resumable execution/state pair where Adapt is the sole in-progress stage, Execute through Classify are completed, and Validate through Reuse are pending.

Include at least one structured adaptation with complete provenance, affected scope, alternatives, certainty, approval fields, disposition, implementation status, validation status, persistence status, and reuse status.

Use a completion-permitted Adapt matrix row. For Validate activation, at least one adaptation must be approved, fully implemented, and validation-eligible, with at least one planned structured validation entry covering targets, criteria or rules, method, immutable scope, expected outcome, and expected evidence.

## Proposed transition

Construct the complete proposed post-transition pair:

- Adapt becomes completed with summary, timestamps, and adaptation references.
- Validate becomes the sole in-progress stage.
- Persist and Reuse remain pending.
- Eligible adaptations use `validation_status: pending`.
- Execution remains in progress.
- State references the same execution and sets `lifecycle_stage: validate`.
- One whole-second UTC transition instant is used and unrelated state fields are preserved.

## Validation

Validate YAML 1.2, Draft 2020-12 schemas with formats, adaptation matrix semantics, approval and decision provenance, implementation eligibility, validation-plan completeness, lifecycle order, sole active stage, timestamps, state/execution agreement, retained-SHA prechecks, execution-first/state-second compare-and-swap, final pair verification, partial-transition rollback/finding behavior, and repository immutability.

## Required negative cases

Report exactly 18 deterministic rejections:

1. Adapt completes with no structured adaptation.
2. Adapt stage has no references.
3. An adaptation has unresolved provenance.
4. A proposed adaptation attempts Adapt completion.
5. An adaptation remains implementation `in-progress` at completion.
6. Approval-required work is approved without durable approval.
7. Approved work lacks an authorizing decision.
8. Approved work is not fully implemented.
9. Rejected work claims implementation.
10. Deferred work lacks a resolving decision.
11. New-goal-required work is implemented within the current goal.
12. Validate starts with no validation plan.
13. A validation plan omits targets, criteria/rules, method, scope, expected outcome, or expected evidence.
14. A validation-ineligible adaptation is treated as eligible.
15. Adapt and Validate are both in progress.
16. State lifecycle stage does not equal `validate`.
17. Either retained SHA changes before the first write.
18. Validation or repository work begins before final pair verification.

## Result format

Produce exactly 11 numbered sections:

1. Verification Summary
2. Validation Trace
3. Starting Operating Snapshot
4. Transition Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Adaptation and Validation-Plan Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

If no reusable defect exists, state exactly:

> No reusable framework defects were found during the non-persistent Adapt-to-Validate lifecycle verification.

Only the revision-specific runner may authorize writing the canonical result.