# Prompt 004 — Observe to Evaluate

## Purpose

Verify, without mutating the framework repository, that a valid execution can complete Observe and activate Evaluate while preserving the semantic boundary between observations, evidence, and evaluation.

The revision-specific runner supplies all immutable revisions and publication details.

## Authorization

Use the pinned `Infoconex/ai-flywheel-framework` revision as the source of truth. Read the manifest first and all required files in order. Construct and validate complete synthetic artifacts in memory only. Do not mutate the framework repository, inspect an application repository, invent evidence, or create alternate results.

Label every displayed artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Starting snapshot

Construct a schema-valid resumable execution and state pair where Observe is the sole in-progress stage, Execute is completed, Evaluate through Reuse are pending, and all identities, timestamps, state references, and acceptance criteria agree.

Include at least one structured observation and sufficient evidence to permit Observe completion. A complete observation must record an actual result, source or method, observation time, evidence references, uncertainty disposition, and conflict references. It must not contain inferred causes, classifications, recommendations, adaptations, validation conclusions, persistence decisions, or reuse decisions.

## Proposed transition

Construct the complete proposed post-transition pair:

- Observe becomes completed with summary, timestamps, and references.
- Evaluate becomes the sole in-progress stage.
- Classify through Reuse remain pending.
- Execution remains in progress.
- State identifies the same execution and `lifecycle_stage: evaluate`.
- The transition uses one whole-second UTC instant and preserves unrelated state fields.

Evaluate activation does not require an evaluation result yet. Evaluation content is required before Evaluate may complete.

## Validation

Validate YAML 1.2, Draft 2020-12 schemas with formats, observation semantics, evidence sufficiency, reference resolution, lifecycle order, sole active stage, timestamps, state/execution agreement, retained-SHA prechecks, execution-first/state-second compare-and-swap, final pair verification, rollback/finding behavior for a partial transition, and repository immutability.

## Required negative cases

Report exactly 14 deterministic rejections:

1. Observe completes with no observations.
2. Observe completes with no execution-level evidence reference.
3. Observe stage has no references.
4. A complete observation has no evidence.
5. An incomplete or uncertain observation lacks an uncertainty explanation.
6. An observation states an inferred cause or evaluation conclusion as fact.
7. Observe and Evaluate are both in progress.
8. Evaluate starts before Observe completes.
9. Observe completion timestamp or summary is missing.
10. Evaluate start timestamp is missing.
11. State lifecycle stage does not equal `evaluate`.
12. A cross-artifact observation or evidence reference does not resolve.
13. Either retained SHA changes before the first write.
14. Evaluation or repository work begins before final pair verification.

For each include invalid condition, expected rejection, observed result, and enforcing contract.

## Result format

Produce exactly 11 numbered sections:

1. Verification Summary
2. Validation Trace
3. Starting Operating Snapshot
4. Transition Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Observation and Evidence Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

If no reusable defect exists, state exactly:

> No reusable framework defects were found during the non-persistent Observe-to-Evaluate lifecycle verification.

Only the revision-specific runner may authorize writing the canonical result.