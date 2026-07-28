# AI Flywheel Cold-Start Operating Validation

## Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Branch:** `feature/self-contained-operating-model`

## Cold-Start Instructions

Ignore all previous conversations, memory, and prior knowledge.

Treat this as the first time you have encountered this repository.

The repository itself is the only authoritative source.

## Objective

Perform startup and operating validation only.

Validate that a fresh operator can deterministically discover and follow the repository-defined startup path, resolve the current operating state, and identify the next authorized action.

Do not create or activate an execution.

Do not perform repository discovery or any goal-directed work.

Do not modify the repository.

## Required Procedure

1. Resolve the repository and requested branch.
2. Pin all validation inputs to one immutable revision.
3. Resolve the repository root.
4. Read the repository-root operator entry instructions.
5. Read `.flywheel/manifest.yaml`.
6. Follow the manifest-declared startup entrypoint exactly.
7. Read `.flywheel/state.yaml` at the required point in the startup sequence.
8. Read every manifest-required file in manifest order.
9. Resolve the active mission and active goal from state.
10. Resolve any applicable records and any active execution.
11. Validate all loaded YAML artifacts against their declared schemas using YAML 1.2 and JSON Schema Draft 2020-12 with format enforcement.
12. Validate all applicable cross-artifact invariants, canonical paths, reciprocal identifiers, statuses, lifecycle values, readiness values, and active-item uniqueness rules.
13. Determine whether an existing execution must be resumed or a new execution must be created before goal-directed work.
14. Stop before execution creation or repository inspection.

## Repository Mutation Rules

You may:

- Read repository files.
- Resolve branches, commits, paths, and records.
- Validate schemas and cross-artifact invariants.
- Report defects in reusable framework artifacts.

You must not:

- Create files.
- Modify files.
- Delete files.
- Stage files.
- Commit changes.
- Push changes.
- Create an execution.
- Activate an execution.
- Update state.
- Perform repository discovery.
- Gather execution evidence.
- Begin goal-directed work.

## Required Validation

Validate at least:

- Repository and branch resolution.
- Immutable revision pinning.
- Repository-root path resolution.
- Manifest existence and schema conformance.
- Manifest entrypoint resolution.
- Required-file existence and ordering.
- State schema conformance.
- Active mission resolution and schema conformance.
- Active goal resolution and schema conformance.
- Mission-goal membership and ordering.
- Active mission and goal uniqueness.
- Active execution consistency.
- Lifecycle-stage consistency.
- Readiness and application-mission permission consistency.
- Canonical path and identifier agreement.
- Startup stop conditions.

## Framework Defects

Only report reusable framework defects.

Do not report the expected absence of a first execution record or lazy record directories as a defect.

For each defect include:

- Identifier
- Severity
- Artifact
- Rule
- Observed behavior
- Expected behavior
- Why deterministic operation is affected
- Framework-only correction

## Final Report

Produce exactly these sections.

### 1. Startup Summary

Include:

- Repository
- Branch
- Immutable Revision
- Operating Validation
- Repository Validation
- Implementation Validation
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
- Application Missions Allowed

### 4. Startup Decision

Include:

- Resume Existing Execution
- Create First Execution
- Goal-Directed Work Authorized
- Repository Inspection Authorized
- Reason

### 5. Schema and Invariant Results

Report all schema, reference, uniqueness, lifecycle, readiness, and cross-artifact validation results.

### 6. Framework Defects

If none exist, state exactly:

> No reusable framework defects were found during cold-start operating validation.

### 7. Repository Mutation Confirmation

State explicitly:

- No files were created.
- No files were modified.
- No files were deleted.
- No files were staged.
- No commits were created.
- No changes were pushed.
- No execution was created or activated.
- No repository discovery was performed.

### 8. Next Authorized Action

State the single next action authorized by the validated operating model.

If no execution exists and the active goal is ready, the expected action is to create the first execution before repository inspection.

Stop after this section.
