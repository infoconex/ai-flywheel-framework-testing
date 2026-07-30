# AI Flywheel Execution-Creation Verification

## Execution Input

The revision-specific runner supplies the target framework repository and exact immutable framework commit.

Use only that immutable revision. Do not substitute a branch head, later commit, cached content, or prior conversational knowledge.

## Cold-Start Boundary

Treat the repository as newly encountered. The repository and the pinned Prompt 002 specification are the only authoritative sources.

Complete the manifest-declared startup protocol before constructing an execution. Read every manifest-required file in order, resolve durable state, active mission, active goal, applicable records, and any active execution.

Prompt 002 is valid only when startup proves that no resumable active execution exists and that first-execution creation is the next authorized action.

## Objective

Perform a non-persistent verification of first-execution creation and activation.

Construct and validate, entirely in memory:

1. One proposed execution activation snapshot.
2. One matching proposed state update.
3. The deterministic create-only and compare-and-swap sequence that would persist them.

Do not persist either artifact and do not begin repository inspection or other goal-directed work.

## Repository Mutation Boundary

You may read immutable repository content, construct proposed artifacts in memory, validate them, and report reusable framework defects.

You must not create, update, delete, stage, commit, or push framework files. You must not activate an execution, update durable state, inspect the target application repository, gather goal evidence, or begin lifecycle work.

Every proposed artifact must be labeled:

> **PROPOSED ONLY — NOT WRITTEN**

## Required Procedure

1. Resolve the repository and runner-supplied immutable framework revision.
2. Follow the manifest startup protocol completely.
3. Read every manifest-required file in order.
4. Validate the manifest, state, active mission, active goal, applicable records, and all cross-artifact invariants.
5. Confirm `active_execution: null`, `lifecycle_stage: null`, and that no resumable execution exists for the active goal.
6. Resolve the normative execution model, execution schema, state schema, canonical record paths, and execution template when present.
7. Resolve one stable operator identity: authenticated repository actor when exposed, otherwise `chatgpt-session`.
8. Capture one UTC creation instant at whole-second precision.
9. Derive `EX-YYYYMMDDTHHMMSSZ-NNN` using the lowest unused same-second counter beginning with `001`.
10. Derive the canonical path `.flywheel/operations/records/executions/<execution-id>.yaml` and prove it does not exist.
11. Retain the original state content and blob SHA for compare-and-swap protection.
12. Construct the complete proposed execution activation snapshot.
13. Construct the complete proposed state update.
14. Validate each proposed artifact against YAML 1.2 and JSON Schema Draft 2020-12 with format enforcement.
15. Validate all cross-artifact, lifecycle, timestamp, identity, canonical-path, authorization, and state-execution invariants.
16. Model the create-only execution write, same-second collision retry, retained-state recheck, state compare-and-swap, and final pair verification without performing writes.
17. Model the required orphaned-execution startup-failure behavior when execution creation would succeed but state compare-and-swap would fail.
18. Execute all required negative validations.
19. Stop without persistence.

## Proposed Execution Requirements

The proposed execution must:

- Use `schema_version: 1`.
- Belong to the active mission and active goal.
- Use the active goal objective exactly as `intended_outcome`.
- Copy acceptance-criterion IDs exactly in goal order.
- Use `status: in-progress`.
- Set `started_at` to the captured whole-second UTC instant.
- Set `completed_at: null` and `outcome: null`.
- Set `completion.disposition: null` and `completion.rationale: null`.
- Mark `lifecycle.execute.status: in-progress` with the same `started_at` as the execution.
- Set the other seven lifecycle stages to `pending` with null timestamps, summaries, and reasons and empty refs.
- Initialize `actions`, `observations`, `evaluations`, `classifications`, `adaptations`, `blockers`, `approval_refs`, `evidence_refs`, `decision_refs`, `finding_refs`, and `validation_results` as empty arrays.
- Use a filename exactly equal to `<execution-id>.yaml` at the canonical execution path.

Required goal approvals remain requirements of the goal. `approval_refs` stays empty until durable approval records exist.

## Proposed State Requirements

The proposed state must preserve every unrelated field and must:

- Preserve the active mission and active goal.
- Set `status: active`.
- Set `active_execution` to the proposed execution ID.
- Set `lifecycle_stage: execute`.
- Set `last_durable_update.at` exactly equal to execution `started_at`.
- Set `last_durable_update.by` to the resolved operator identity.
- Set `last_durable_update.reason` to `Activated execution <execution-id> for goal <goal-id>.`.

## Persistence-Sequence Verification

Verify the following proposed sequence without writing:

1. Retain the current state blob SHA.
2. Select the deterministic execution ID and canonical path.
3. Create the fully valid execution using create-only semantics.
4. On path collision, re-list the canonical directory and select the next lowest unused counter for the same second.
5. Re-read state and require the retained SHA to remain current.
6. Update state using compare-and-swap against the retained SHA.
7. Re-read execution and state and require exact equality with the validated proposed pair.

If execution creation would succeed but state compare-and-swap would fail, verify that the operator must not overwrite current state, must identify the execution as orphaned in a startup-failure record, and must stop.

## Required Negative Validations

Demonstrate deterministic rejection of exactly these 16 cases:

1. Two lifecycle stages are `in-progress`.
2. No lifecycle stage is `in-progress` for an in-progress execution.
3. Execution `outcome` is non-null while status is `in-progress`.
4. Execution `completed_at` is non-null while status is `in-progress`.
5. Completion disposition or rationale is non-null while status is `in-progress`.
6. Execute stage timestamp differs from execution `started_at`.
7. A successor lifecycle stage is not pending at activation.
8. Acceptance criteria differ from the active goal or are out of order.
9. Intended outcome differs from the active goal objective.
10. Proposed state references a nonexistent execution artifact.
11. Proposed state lifecycle stage is null or differs from `execute`.
12. Proposed state status is not `active`.
13. The execution identifier or filename does not follow the canonical pattern.
14. The selected execution path already exists and the operator does not retry with the next counter.
15. State changes after its retained revision is captured and the operator attempts to overwrite it.
16. Repository inspection or goal-directed work begins before durable activation would complete.

For each case report the invalid condition, expected rejection, observed result, and enforcing schema or semantic rule.

## Framework Defects

Report only reusable framework defects. Do not treat the expected absence of a first execution or lazily created record directories as defects. Do not recommend persisting execution details into the framework-development repository during this verification.

For every defect include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

## Required Result

Follow `test/ai/RESULT_FORMAT.md` and produce exactly these 11 numbered level-two sections beneath one level-one title:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Execution-Creation Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Schema and Invariant Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

The Verification Summary and Repository Mutation Confirmation must use fenced `text` blocks. Complete proposed artifacts must use fenced `yaml` blocks.

The result must record the exact framework revision, Prompt 002 specification commit, result-format contract commit, result-format validator commit, `50/50` manifest-required reads, `16/16` negative cases, 11 numbered sections, result-format validation, and mutation status.

If no defect exists, state exactly:

> No reusable framework defects were found during the non-persistent execution-creation verification.

Write or overwrite only:

```text
test/ai/results/002-execution-creation.md
```

Do not create alternate, dated, corrected, rerun, backup, or history results. Do not modify `test/ai/README.md` during the independent run.