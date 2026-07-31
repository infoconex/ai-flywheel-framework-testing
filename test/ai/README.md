# AI Flywheel Framework AI Test Prompts

This directory catalogs the reusable AI prompts used to verify the AI Flywheel Framework.

## Repository Structure

- `prompts/` contains one reusable specification per prompt number.
- `runners/` contains one current revision-specific run-and-publish file per prompt number when a runner is required.
- `results/` contains one canonical retained result per prompt number.
- `fixtures/` and `tools/` contain supporting test implementation and validators.

Do not create launcher files under `prompts/`, corrected runner copies, or alternate result files. Update the canonical runner or overwrite the canonical result instead.

## Test Prompt Status

| Test | Focus Area | Run | Last Run | Passed | Test Result |
|---|---|---:|---|---:|---|
| [Startup Validation](prompts/001-startup-validation.md) | Cold start, manifest-first startup, required-file ordering, state resolution, active mission and goal resolution, and startup boundaries | Yes | 2026-07-30 | Yes | [View result](results/001-startup-validation.md) |
| [Execution Creation](prompts/002-execution-creation.md) | Non-persistent execution identity, canonical path, activation state, schemas, lifecycle initialization, collisions, and compare-and-swap protection | Yes | 2026-07-30 | Yes | [View result](results/002-execution-creation.md) |
| [Execute to Observe](prompts/003-execute-to-observe.md) | Non-persistent lifecycle transition, stage ordering, timestamps, state agreement, negative cases, and repository mutation protection | Yes | 2026-07-30 | Yes | [View result](results/003-execute-to-observe.md) |
| [Observe to Evaluate](prompts/004-observe-to-evaluate.md) | Observation semantics, evidence boundaries, Observe completion, Evaluate activation, traceability, negative cases, and repository mutation protection | Yes | 2026-07-30 | Yes | [View result](results/004-observe-to-evaluate.md) |
| [Evaluate to Classify](prompts/005-evaluate-to-classify.md) | Evaluation completion, classification semantics and provenance, multiple classifications, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-30 | Yes | [View result](results/005-evaluate-to-classify.md) |
| [Classify to Adapt](prompts/006-classify-to-adapt.md) | Classification completion, adaptation semantics and provenance, scope and approval boundaries, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-30 | Yes | [View result](results/006-classify-to-adapt.md) |
| [Adapt to Validate](prompts/007-adapt-to-validate.md) | Adapt completion, validation semantics and evidence requirements, and the transition from Adapt to Validate | Yes | 2026-07-30 | Yes | [View result](results/007-adapt-to-validate.md) |
| [Validate to Persist](prompts/008-validate-to-persist.md) | Validate completion, evidence-backed outcomes, persistence semantics, canonical locations, immutable history, partial-persistence recovery, and repository mutation protection | Yes | 2026-07-30 | Yes | [View result](results/008-validate-to-persist.md) |
| [Persist to Reuse](prompts/009-persist-to-reuse.md) | Persist completion, structured reuse assessments, knowledge qualification, duplicate/conflict handling, immutable supersession/deprecation, Reuse durability, and terminal closure | Yes | 2026-07-30 | Yes | [View result](results/009-persist-to-reuse.md) |
| [End-to-End Execution](prompts/010-end-to-end-execution.md) | One stable execution across all lifecycle stages, checkpoint persistence, final durability transactions, and terminal completion | Yes | 2026-07-30 | Yes | [View result](results/010-end-to-end-execution.md) |
| [Resume Interrupted Execution](prompts/011-resume-interrupted-execution.md) | Fresh-session discovery and safe CAS resume of a durable interrupted execution without identity loss, repeated work, stale overwrites, or repository mutation | Yes | 2026-07-30 | Yes | [View result](results/011-resume-interrupted-execution.md) |
| [Recover Partial Lifecycle Transition](prompts/012-recover-partial-lifecycle-transition.md) | Fresh-session detection and recovery of an execution-first, state-not-written lifecycle transition using a durable transition plan, exact rollback, and structured recovery evidence | Yes | 2026-07-30 | Yes | [View result](results/012-recover-partial-lifecycle-transition.md) |
| [Enforce Approval Boundary](prompts/013-enforce-approval-boundary.md) | Fresh-session enforcement of exact durable approval before a material dependency action, including authority, scope, persistence, delegation, revocation, and invalid authorization cases | Yes | 2026-07-30 | Yes | [View result](results/013-enforce-approval-boundary.md) |
| [Recover Missing Required Artifact](prompts/014-recover-missing-required-artifact.md) | Isolated startup failure when a manifest-required operating file is absent, including exact stop boundaries, startup-failure evidence, optional blocked state, collision handling, and repository immutability | Yes | 2026-07-30 | Yes | [View result](results/014-recover-missing-required-artifact.md) |
| [Recover Broken Active Reference](prompts/015-recover-broken-active-reference.md) | Isolated startup failure when state points to a missing, ambiguous, or identity-mismatched active artifact, including exact reference evidence, no-guess boundaries, startup-failure persistence, and safe reconciliation | Yes | 2026-07-30 | Yes | [View result](results/015-recover-broken-active-reference.md) |
| [Run Representative Proving Mission](prompts/016-run-representative-proving-mission.md) | Representative non-destructive mission that inventories manifest-required framework artifacts, maps criterion evidence, applies the lifecycle, and proves useful terminal completion without repository mutation | Yes | 2026-07-30 | Yes | [View result](results/016-run-representative-proving-mission.md) |
| [Self-Host Certification](prompts/017-self-host-certification.md) | Self-hosted certification assembly with all ten scenarios passed, certification ready for approval, and readiness held pending human authority | No | — | No | Pending correction of the transformation tool's stale retained evidence revision and independent rerun |

## Status Rules

- **Run** indicates whether the prompt has been executed independently against the target framework repository.
- **Last Run** records the most recent independent framework execution date.
- **Passed** indicates whether the current retained result met the expected result.
- **Test Result** links to the retained result for the test.