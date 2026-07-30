# Prompt 006 — Classify to Adapt

## Purpose

Verify, without mutating the framework repository, that a valid execution can complete Classify and activate Adapt while preserving provenance, authorized scope, approval boundaries, and downstream lifecycle integrity.

The revision-specific runner supplies immutable revisions and publication details.

## Authorization

Use the pinned `Infoconex/ai-flywheel-framework` revision. Read the manifest first and all required files in order. Construct complete synthetic artifacts in memory only. Do not mutate the framework repository, inspect an application repository, invent approval or authority, implement an adaptation, or create alternate results.

Label every displayed artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Starting snapshot

Construct a schema-valid resumable execution/state pair where Classify is the sole in-progress stage, Execute through Evaluate are completed, and Adapt through Reuse are pending.

Include at least one structured classification with unique identity, permitted type, evaluation and evidence provenance, rationale, certainty, uncertainty disposition, relationship references, and all type-specific decision, finding, or validation references required by the current contracts.

## Proposed transition

Construct the complete proposed post-transition pair:

- Classify becomes completed with summary, timestamps, and classification references.
- Adapt becomes the sole in-progress stage.
- Validate through Reuse remain pending.
- Execution remains in progress.
- State references the same execution and sets `lifecycle_stage: adapt`.
- One whole-second UTC transition instant is used and unrelated state fields are preserved.

Adapt activation may introduce a proposed adaptation. An approval-required proposal may remain pending with no approval or decision reference and implementation not started. It must not claim implementation, validation, persistence, or reuse outcomes.

## Validation

Validate YAML 1.2, Draft 2020-12 schemas with formats, classification semantics, provenance and reference resolution, scope and approval boundaries, lifecycle order, sole active stage, timestamps, state/execution agreement, retained-SHA prechecks, execution-first/state-second compare-and-swap, final pair verification, partial-transition rollback/finding behavior, and repository immutability.

## Required negative cases

Report exactly 16 deterministic rejections:

1. Classify completes with no structured classification.
2. Classify stage has no references.
3. A classification has no evaluation reference.
4. A classification has no evidence reference.
5. A classification uses an unsupported type.
6. A provisional or disputed classification lacks uncertainty.
7. A decision classification lacks a decision reference.
8. A finding-like classification lacks a finding reference.
9. A validated-learning classification lacks passed validation provenance.
10. Classify and Adapt are both in progress.
11. Adapt starts before Classify completes.
12. A proposed adaptation silently expands scope.
13. Approval-required work is treated as approved without durable approval and decision.
14. A proposed adaptation claims implementation or downstream results.
15. Either retained SHA changes before the first write.
16. Adaptation or repository work begins before final pair verification.

## Result format

Produce exactly 11 numbered sections:

1. Verification Summary
2. Validation Trace
3. Starting Operating Snapshot
4. Transition Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Classification and Adaptation-Boundary Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

If no reusable defect exists, state exactly:

> No reusable framework defects were found during the non-persistent Classify-to-Adapt lifecycle verification.

Only the revision-specific runner may authorize writing the canonical result.