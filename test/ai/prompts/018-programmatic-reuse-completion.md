# Prompt 018 — Programmatic Reuse Completion

## Purpose

Verify, without depending on a CLI or mutating the framework repository, that the framework contract supports an atomic transition from Persist through Reuse to governed execution, goal, mission, and state completion.

This is a reusable AI evaluation specification. The revision-specific runner supplies the immutable framework revision, this specification commit, result-format identities, fixture identities when required, and publication instructions.

## Authority and boundaries

Treat the pinned `Infoconex/ai-flywheel-framework` revision as the sole authoritative source for lifecycle, persistence, reuse, completion, mission-evaluation, schema, semantic, atomicity, and state-synchronization requirements.

Do not treat a CLI, SDK, branch head, prior result, cached copy, or prior conversation as authoritative. Auxiliary tools may be used only to read, construct, digest, and validate synthetic artifacts; their behavior is not evidence of framework conformance by itself.

Read `.flywheel/manifest.yaml` first and every manifest-required file in order. Construct complete synthetic fixtures and proposed transitions in an isolated temporary workspace or entirely in memory. Do not modify the framework repository or inspect an application repository.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

Only the revision-specific runner may authorize writing the canonical testing result.

## Starting fixtures

Construct schema-valid synthetic mission, goal, execution, state, persistence-plan, persistence-record, reuse-assessment, evidence, finding, decision, classification, validation-result, and approval artifacts as required by the pinned framework contract.

Use stable deterministic identities, canonical paths, whole-second UTC timestamps, and byte-level digests. Preserve one baseline digest set for every governed file before each proposed operation.

The fixtures must permit evaluation of both:

- a mission with an eligible dependent goal after the current goal; and
- a mission whose current goal is the final mission goal.

## Required scenarios

### 1. Generic Persist completion is rejected

Place a valid execution with Persist as the sole in-progress lifecycle stage. Model a generic lifecycle advancement that attempts to complete Persist without the dedicated persistence transaction.

Verify deterministic rejection under the framework contract and prove that every governed artifact remains byte-identical to its baseline digest.

### 2. Dedicated persistence activates Reuse atomically

Construct the complete proposed dedicated persistence transaction.

Verify that it creates the required terminal persistence record and planned reuse assessment, completes Persist, activates Reuse, and synchronizes execution and state as one governed transaction. Verify that preflight validation, retained revisions, content digests, compare-and-swap conditions, write ordering, rollback or recovery behavior, and final re-read cover the complete mutable set.

### 3. Duplicate reuse identity is rejected atomically

Pre-create the requested reuse-assessment identity and retry the proposed persistence transaction.

Verify deterministic rejection before any write and prove byte-level equality of every governed file before and after rejection.

### 4. Whole-set schema and semantic preflight is enforced

Evaluate proposed transitions containing, separately:

1. a missing classification finding reference;
2. a missing applicable validation result; and
3. incomplete persistence-to-reuse linkage.

Verify each complete proposed mutation set is rejected before writing. Correct the entire proposed set and verify that it passes schema and semantic preflight.

### 5. Generic Reuse advancement is rejected in favor of governed AI work

Place a valid execution in Reuse with a planned assessment. Model generic lifecycle advancement without completing the governed reuse work.

Verify deterministic rejection, identify the framework rule requiring governed assessment work, and prove that no governed artifact changes.

### 6. A completed reuse assessment is required

Attempt governed completion while the required reuse assessment remains planned. Verify atomic rejection and unchanged governed-file digests.

Then construct a completed assessment containing every framework-required disposition, provenance, applicability, limitation, guidance, rationale, timestamp, assessor, duplicate/conflict evaluation, approval or decision reference, and proposed knowledge linkage.

### 7. Governed completion synchronizes Reuse, execution, goal, and state

Construct the complete proposed completion transaction.

Verify that Reuse and the execution become terminal, the goal closes only when its completion contract is satisfied, an eligible dependent goal is readied at most once, and state clears or updates active goal, active execution, and lifecycle stage consistently. Verify whole-set preflight, atomic write semantics, rollback or recovery behavior, final re-read, and byte-level evidence.

### 8. Final-goal mission evaluation is explicit

Complete the final goal in a synthetic mission.

Verify that the mission completes when its success criteria are supported and no mission-level blocker or required approval remains. Verify that it remains active only when a concrete governed blocker or approval-bound reason within the mission objective is durably represented.

Verify specifically that approval for external work outside the mission objective does not keep an otherwise complete preparation mission active.

### 9. Final repository validation and cleanup pass

Re-read every proposed final artifact and validate the complete synthetic repository against YAML 1.2, JSON Schema Draft 2020-12 with format enforcement, canonical-path rules, reference resolution, uniqueness, lifecycle ordering, timestamp monotonicity, persistence and reuse linkage, execution-goal-mission-state agreement, blocker and approval semantics, and terminal cleanup requirements.

Verify that no active execution or lifecycle stage remains after terminal completion and that every final reference resolves exactly once.

## Atomicity evidence

For every rejected operation, record:

- the complete governed-file set;
- the baseline byte digest for each file;
- the post-rejection byte digest for each file;
- the structured rejection category and reason derived from the framework contract; and
- an explicit equality result for the entire set.

Do not infer atomicity from an error message or from unchanged high-level values.

For every accepted proposed transaction, record preflight coverage, retained revisions, intended write set and order, rollback or recovery requirements, final byte digests, and post-transaction re-read results.

## Framework defects

Report only reusable defects or ambiguities in the pinned framework contract. Do not report the absence or behavior of any CLI as a framework defect.

For each defect include identifier, severity, artifact, rule, observed contract behavior, expected behavior, deterministic impact, and framework-only correction.

When none exist, state exactly:

> No reusable framework defects were found during the non-persistent programmatic Reuse-completion verification.

## Result requirements

Follow `test/ai/RESULT_FORMAT.md` and produce exactly these 15 numbered level-two sections beneath one level-one title:

1. Verification Summary
2. Validation Trace
3. Starting Synthetic Fixtures
4. Generic Persist Rejection
5. Dedicated Persistence and Reuse Activation
6. Duplicate Reuse Identity Rejection
7. Whole-Set Preflight Results
8. Generic Reuse Rejection
9. Reuse Assessment Completion
10. Governed Completion Transaction
11. Final-Goal Mission Evaluation
12. Final Artifact State
13. Repository Validation
14. Framework Defects
15. Repository Mutation Confirmation

The result must identify the exact framework revision, Prompt 018 specification commit, result-format contract commit, result-format validator commit, fixture or tool identities used, scenario results, rejection digest comparisons, final execution/goal/mission/state values, persistence and reuse identities, unresolved-reference result, defect counts, and format-validation result.

Write or overwrite only:

```text
test/ai/results/018-programmatic-reuse-completion.md
```

Do not create alternate, dated, corrected, rerun, backup, or history result files. Do not modify README files during an independent run.

## Pass conditions

Prompt 018 passes only when:

- all nine scenarios satisfy the pinned framework contract;
- every rejected operation has complete byte-level no-mutation evidence;
- every accepted proposed transaction passes whole-set schema and semantic preflight;
- Persist, Reuse, execution, goal, mission, and state synchronization is explicitly verified;
- final-goal mission evaluation handles irrelevant external-work approval correctly;
- all final references resolve and complete repository validation passes;
- the framework repository remains unchanged; and
- the canonical result-format validator passes for 15 numbered sections.

Stop after publishing the canonical result.