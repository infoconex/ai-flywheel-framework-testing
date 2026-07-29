# AI Flywheel Framework AI Test Prompts

This directory catalogs the reusable AI prompts used to verify the AI Flywheel Framework.

## Test Prompt Status

| Test | Focus Area | Run | Last Run | Passed | Test Result |
|---|---|---:|---|---:|---|
| [Startup Validation](prompts/001-startup-validation.md) | Cold start, manifest-first startup, required-file ordering, state resolution, active mission and goal resolution, and startup boundaries | Yes | 2026-07-27 | Yes | [View result](results/001-startup-validation.md) |
| [Execution Creation](prompts/002-execution-creation.md) | Non-persistent execution identity, canonical path, activation state, schemas, lifecycle initialization, collisions, and compare-and-swap protection | Yes | 2026-07-27 | Yes | [View result](results/002-execution-creation.md) |
| [Execute to Observe](prompts/003-execute-to-observe.md) | Non-persistent lifecycle transition, stage ordering, timestamps, state agreement, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View result](results/003-execute-to-observe.md) |
| [Observe to Evaluate](prompts/004-observe-to-evaluate.md) | Observation semantics, evidence boundaries, Observe completion, Evaluate activation, traceability, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View result](results/004-observe-to-evaluate.md) |
| [Evaluate to Classify](prompts/005-evaluate-to-classify.md) | Evaluation completion, classification semantics and provenance, multiple classifications, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View result](results/005-evaluate-to-classify.md) |
| [Classify to Adapt](prompts/006-classify-to-adapt.md) | Classification completion, adaptation semantics and provenance, scope and approval boundaries, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View result](results/006-classify-to-adapt.md) |
| [Adapt to Validate](prompts/007-adapt-to-validate.md) | Adapt completion, validation semantics and provenance, evidence sufficiency, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-28 | Yes | [View result](results/007-adapt-to-validate.md) |
| [Validate to Persist](prompts/008-validate-to-persist.md) | Validate completion, evidence-backed outcomes, persistence semantics, canonical locations, immutable history, partial-persistence recovery, and repository mutation protection | Yes | 2026-07-28 | Yes | [View result](results/008-validate-to-persist.md) |
| [Persist to Reuse](prompts/009-persist-to-reuse.md) | Persist completion, structured reuse assessments, knowledge qualification, duplicate/conflict handling, immutable supersession/deprecation, Reuse durability, and terminal completion boundaries | Yes | 2026-07-28 | Yes | [View result](results/009-persist-to-reuse.md) |
| [End-to-End Execution](prompts/010-end-to-end-execution.md) | One stable execution across all lifecycle stages, checkpoint persistence, transaction commit markers, planned-to-completed reuse assessments, and terminal closure | Yes | 2026-07-28 | Yes | [View result](results/010-end-to-end-execution.md) |
| [Resume Interrupted Execution](prompts/011-resume-interrupted-execution.md) | Fresh-session discovery and safe CAS resume of a durable interrupted execution without identity loss, repeated work, stale overwrites, or repository mutation | Yes | 2026-07-28 | Yes | [View result](results/011-resume-interrupted-execution.md) |
| [Recover Partial Lifecycle Transition](prompts/012-recover-partial-lifecycle-transition.md) | Fresh-session detection and recovery of an execution-first, state-not-written lifecycle transition using a durable transition plan, exact rollback, and recovery evidence | Yes | 2026-07-29 | Yes | [View result](results/012-recover-partial-lifecycle-transition.md) |

## Status Rules

- **Run** indicates whether the prompt has been executed independently against the target framework repository.
- **Last Run** records the most recent independent framework execution date.
- **Passed** indicates whether the current retained result met the expected result.
- **Test Result** links to the retained result for the test.
