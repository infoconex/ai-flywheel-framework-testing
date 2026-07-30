# AI Flywheel Prompt 001 — Cold-Start Operating Validation

## Purpose

Verify that a fresh operator can discover and follow the framework-defined startup protocol, validate the current durable operating context, and identify the next authorized action without performing goal-directed work or modifying either repository.

This is a reusable capability specification. The framework revision, specification revision, result-format revision, and validator revision are supplied by the run-specific file under `test/ai/runners/`.

## Authority and Scope

Treat the pinned `Infoconex/ai-flywheel-framework` revision as the sole authoritative framework source.

Ignore prior conversations, memory, cached content, branch heads, and unpinned copies.

Startup-only reading and validation are authorized. Do not:

- Create or activate an execution.
- Inspect the application repository.
- Perform onboarding questions or other goal-directed work.
- Create, modify, delete, stage, commit, or push framework files.
- Change durable state, mission, goal, execution, approval, evidence, or readiness records.

## Required Procedure

1. Resolve the pinned framework revision supplied by the runner.
2. Resolve the repository root.
3. Read `.flywheel/manifest.yaml` first.
4. Resolve every manifest path relative to the declared `path_base`.
5. Read `.flywheel/state.yaml` at the point required by the manifest startup entrypoint.
6. Read every `required_files` entry in exact manifest order and retain successful path-resolution evidence.
7. Read the active mission and active goal identified by state.
8. Read applicable records for the active goal from their canonical locations, oldest first.
9. If `active_execution` is non-null, read it last and evaluate resumability. If it is null, confirm whether first-execution creation is the next required action.
10. Validate YAML artifacts against their declared schemas using YAML 1.2 and JSON Schema Draft 2020-12 with format enforcement when the schema declares formats.
11. Validate canonical paths, identifiers, references, uniqueness, statuses, lifecycle values, readiness, application-work permission, blockers, approvals, and state agreement.
12. Produce the exact 14-heading startup opening report required by `startup.md`.
13. Stop before execution creation or any goal-directed action.

## Required Validation

At minimum, independently validate:

- The manifest exists and conforms to `manifest.schema.yaml`.
- The startup entrypoint resolves uniquely.
- Every manifest-required file exists and resolves exactly once.
- Required files were read in manifest order.
- State conforms to `state.schema.yaml`.
- The active mission and goal resolve uniquely at canonical paths and conform to their schemas.
- Mission-goal membership, reciprocal identifiers, status, and ordering agree.
- Active-execution and lifecycle-stage values agree.
- Readiness agrees with `application_missions_allowed` and implementation availability.
- Required blockers and approvals are represented consistently.
- Repository Validation remains `pending` before authorized execution evidence.
- Implementation Validation remains `not-applicable` when no implementation work occurred.
- The next authorized action is derived only from durable artifacts.

A missing first execution and lazy record directories are expected when the framework contract permits them and are not defects.

## Required Opening Report

Include the following headings in this exact order within the result:

1. `Current Phase`
2. `Status`
3. `Readiness`
4. `Application Missions Permitted`
5. `Active Mission`
6. `Active Goal`
7. `Active Execution`
8. `Lifecycle Stage`
9. `Known Blockers`
10. `Required Approvals`
11. `Operating Validation`
12. `Repository Validation`
13. `Implementation Validation`
14. `Next Authorized Action`

The report must explicitly state whether an execution must be resumed or created.

## Framework Defects

Report only reusable framework defects. For each defect include:

- Identifier
- Severity
- Artifact
- Rule
- Observed behavior
- Expected behavior
- Deterministic impact
- Framework-only correction

When none exist, state exactly:

> No reusable framework defects were found during cold-start operating validation.

## Canonical Result Contract

Write or overwrite only:

```text
test/ai/results/001-startup-validation.md
```

The result must contain one level-one title and exactly these numbered level-two sections:

1. Verification Summary
2. Validation Trace
3. Manifest and Required-File Resolution
4. Durable Operating Context
5. Required Opening Report
6. Schema and Invariant Results
7. Framework Defects
8. Repository Mutation Confirmation

The Verification Summary must be a fenced `text` block. Revision and count metadata must follow it as separate one-line paragraphs with one blank line between paragraphs. Repository Mutation Confirmation must also be a fenced `text` block.

The result must identify:

- Exact tested framework revision.
- Exact Prompt 001 specification revision.
- Exact result-format contract and validator revisions.
- Manifest-required read count.
- Schema and invariant validation count.
- Framework and prompt/fixture defect counts.
- Result-format validation outcome.

## Completion Boundary

Prompt 001 passes only when:

- All manifest-required paths resolve and are read in order.
- Durable mission and goal context resolve uniquely.
- All applicable schemas and cross-artifact invariants pass.
- The exact required opening report is produced.
- The next authorized action is correctly selected.
- No goal-directed work or framework mutation occurs.
- The canonical result-format validator passes for eight numbered sections.

Stop after publishing the canonical result.