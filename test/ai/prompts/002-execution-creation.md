# AI Flywheel Execution-Creation Verification

## Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Branch:** `feature/self-contained-operating-model`

## Cold-Start Instructions

Ignore all previous conversations, memory, and prior knowledge.

Treat this as the first time you have encountered this repository.

The repository itself is the only authoritative source.

## Objective

Perform a non-persistent verification of first-execution creation and activation.

Validate that the operating model can deterministically construct a schema-valid execution artifact and matching state transition without modifying the repository.

Do not perform repository discovery or any goal-directed work after activation.

## Repository Mutation Rules

You may:

- Read repository files.
- Resolve repository state.
- Construct proposed artifacts in memory.
- Validate proposed artifacts.
- Report proposed artifacts.

You must not:

- Create files.
- Modify files.
- Delete files.
- Stage files.
- Commit changes.
- Push changes.
- Activate an execution.
- Update persisted state.
- Perform repository discovery.
- Gather execution evidence.

All artifacts shown in the report are **PROPOSED ONLY — NOT WRITTEN**.

## Required Procedure

1. Resolve the repository and requested branch.
2. Pin all inputs to one immutable revision.
3. Follow the manifest-declared startup protocol completely.
4. Validate the manifest, state, active mission, active goal, required files, schemas, records, and cross-artifact invariants.
5. Confirm that no active execution exists and that first-execution creation is the next required action.
6. Resolve the normative execution model and execution template.
7. Resolve the canonical execution record directory.
8. Resolve a stable operator identity from the authenticated repository actor when available; otherwise use `chatgpt-session`.
9. Capture one UTC creation timestamp at whole-second precision.
10. Generate the execution identifier using `EX-YYYYMMDDTHHMMSSZ-NNN` and the lowest unused same-second counter beginning with `001`.
11. Verify that the exact proposed path does not already exist.
12. Retain the original state version for compare-and-swap protection.
13. Construct the complete proposed execution artifact in memory.
14. Construct the complete proposed updated state in memory.
15. Validate both proposed artifacts against their schemas.
16. Validate all cross-artifact, lifecycle, timestamp, identity, canonical-path, authorization, and transition invariants.
17. Re-read state and verify stale-state protection.
18. Perform post-transition validation in memory.
19. Run the required negative validation scenarios.
20. Stop without persistence.

## Proposed Activation Requirements

The proposed execution must:

- Belong to the active mission and active goal.
- Use the active goal objective exactly as `intended_outcome`.
- Copy acceptance-criterion identifiers exactly in goal order.
- Use `status: in-progress`.
- Set `started_at` to the captured creation instant.
- Set `completed_at: null`.
- Mark `execute` as the sole `in-progress` lifecycle stage.
- Give `execute` the same start timestamp as the execution.
- Leave all later lifecycle stages `pending` with null timestamps, summaries, and reasons.
- Initialize actions, observations, classifications, adaptations, blockers, approvals, evidence, decisions, findings, and validation results as empty arrays.
- Keep outcome and completion values null.

The proposed state must:

- Preserve the active mission and goal.
- Set `status: active`.
- Set `active_execution` to the proposed execution identifier.
- Set `lifecycle_stage: execute`.
- Preserve all unrelated fields.
- Set `last_durable_update` to the captured timestamp and operator.

## Negative Validation

Demonstrate rejection of at least these invalid scenarios:

1. Two lifecycle stages marked in progress.
2. Non-null outcome while execution remains in progress.
3. Terminal execution with incomplete lifecycle stages.
4. Interrupted execution without the required interruption reason.
5. Active execution with null lifecycle stage.
6. Active execution while state status is not active.
7. Proposed state referencing a nonexistent execution artifact.
8. Reuse of an existing execution identifier.
9. State changed after its original version was captured.
10. Repository inspection beginning before execution creation is complete.

For each scenario report:

- Invalid condition
- Expected rejection
- Actual result
- Rule enforcing rejection

## Framework Defects

Only report reusable framework defects.

Do not report missing first-execution records or lazy record directories as defects.

Do not recommend persisting execution details into this framework-development branch.

## Final Report

Produce exactly these sections.

### 1. Verification Summary

Include:

- Repository
- Branch
- Immutable Revision
- Operating Validation
- Verification Result
- Repository Changes
- Files Written
- Commit Required
- Framework Defects Found

### 2. Validation Trace

Provide a complete step-by-step trace of observable actions.

Do not include hidden reasoning.

For every step include:

- Action
- Artifact
- Rule
- Observed
- Result
- Next

### 3. Current Operating State

Include:

- Active Mission
- Active Goal
- Active Execution
- Lifecycle Stage
- Readiness
- Status

### 4. Execution-Creation Decision

Include:

- Decision
- Creation Authorized
- Verification Only
- Persistence Authorized
- Reason

### 5. Proposed Execution Artifact

Display the complete proposed execution YAML.

Precede it with:

> **PROPOSED ONLY — NOT WRITTEN**

### 6. Proposed State Artifact

Display the complete proposed state YAML.

Precede it with:

> **PROPOSED ONLY — NOT WRITTEN**

### 7. Schema and Invariant Results

Report:

- Execution schema validation
- State schema validation
- Cross-artifact validation
- Lifecycle validation
- Identity validation
- Collision validation
- Compare-and-swap validation
- Post-transition validation

### 8. Negative Validation Results

Report every required invalid scenario and whether it was correctly rejected.

### 9. Framework Defects

If none exist, state exactly:

> No reusable framework defects were found during the non-persistent execution-creation verification.

### 10. Repository Mutation Confirmation

State explicitly:

- No files were created.
- No files were modified.
- No files were deleted.
- No files were staged.
- No commits were created.
- No changes were pushed.
- No execution was activated.
- No repository discovery was performed.

### 11. Next Authorized Action

If no framework defect exists, state:

> Run the next non-persistent lifecycle verification without committing execution details to this framework-development branch.

If a framework defect exists, state:

> Correct only the reusable framework defect before repeating this verification.

Stop after this section.
