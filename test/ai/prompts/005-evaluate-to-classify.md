# Prompt 005 — Evaluate to Classify

## Purpose

Verify, without mutating the framework repository, that a valid execution can complete Evaluate and activate Classify while preserving provenance from observations and evidence into structured evaluations and classifications.

The revision-specific runner supplies immutable revisions and publication details.

## Authorization

Use the pinned `Infoconex/ai-flywheel-framework` revision. Read the manifest first and all required files in order. Construct complete synthetic artifacts in memory only. Do not mutate the framework repository, inspect an application repository, invent evidence, or create alternate results.

Label every displayed artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Starting snapshot

Construct a schema-valid resumable execution/state pair where Evaluate is the sole in-progress stage, Execute and Observe are completed, and Classify through Reuse are pending.

Include structured observations, evidence, and at least one material structured evaluation. Every evaluation must reference existing observations and evidence, identify applicable criteria or rules, state its result, limitations, and rationale, and avoid prematurely asserting classifications, adaptations, persistence, or reuse outcomes.

## Proposed transition

Construct the complete proposed post-transition pair:

- Evaluate becomes completed with summary, timestamps, and evaluation references.
- Classify becomes the sole in-progress stage.
- Adapt through Reuse remain pending.
- Execution remains in progress.
- State references the same execution and sets `lifecycle_stage: classify`.
- One whole-second UTC transition instant is used and unrelated state fields are preserved.

Classify activation does not require a classification yet. Structured classifications are required before Classify may complete.

## Validation

Validate YAML 1.2, Draft 2020-12 schemas with formats, evaluation semantics, observation/evidence provenance, reference resolution, lifecycle order, sole active stage, timestamps, state/execution agreement, retained-SHA prechecks, execution-first/state-second compare-and-swap, final pair verification, partial-transition rollback/finding behavior, and repository immutability.

## Required negative cases

Report exactly 14 deterministic rejections:

1. Evaluate completes with no structured evaluation.
2. Evaluate stage has no references.
3. An evaluation has no observation reference.
4. An evaluation has no evidence reference.
5. An evaluation references a missing observation.
6. An evaluation references missing evidence.
7. An evaluation introduces an unsupported fact.
8. An evaluation prematurely asserts a classification or adaptation.
9. Evaluate and Classify are both in progress.
10. Classify starts before Evaluate completes.
11. Evaluate completion summary or timestamp is missing.
12. State lifecycle stage does not equal `classify`.
13. Either retained SHA changes before the first write.
14. Classification or repository work begins before final pair verification.

## Result format

Produce exactly 11 numbered sections:

1. Verification Summary
2. Validation Trace
3. Starting Operating Snapshot
4. Transition Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Evaluation and Provenance Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

If no reusable defect exists, state exactly:

> No reusable framework defects were found during the non-persistent Evaluate-to-Classify lifecycle verification.

Only the revision-specific runner may authorize writing the canonical result.