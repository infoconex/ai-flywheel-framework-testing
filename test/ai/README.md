# AI Flywheel Framework AI Test Prompts

This directory catalogs the reusable AI prompts used to verify the AI Flywheel Framework.

## Test Prompt Status

| Test | Focus Area | Run | Last Run | Passed | Test Result |
|---|---|---:|---|---:|---|
| [Startup Validation](prompts/001-startup-validation.md) | Cold start, manifest-first startup, required-file ordering, state resolution, active mission and goal resolution, and startup boundaries | Yes | 2026-07-27 | Yes | [View result](results/001-startup-validation.md) |
| [Execution Creation](prompts/002-execution-creation.md) | Non-persistent execution identity, canonical path, activation state, schemas, lifecycle initialization, collisions, and compare-and-swap protection | Yes | 2026-07-27 | Yes | [View result](results/002-execution-creation.md) |
| [Execute to Observe](prompts/003-execute-to-observe.md) | Non-persistent lifecycle transition, stage ordering, timestamps, state agreement, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View result](results/003-execute-to-observe.md) |
| [Observe to Evaluate](prompts/004-observe-to-evaluate.md) | Observation semantics, evidence boundaries, Observe completion, Evaluate activation, traceability, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View result](results/004-observe-to-evaluate.md) |
| [Evaluate to Classify](prompts/005-evaluate-to-classify.md) | Evaluation completion, classification semantics and provenance, multiple classifications, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View latest result](results/005-evaluate-to-classify-rerun-2026-07-27.md) |
| [Classify to Adapt](prompts/006-classify-to-adapt.md) | Classification completion, adaptation semantics and provenance, scope and approval boundaries, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-27 | Yes | [View latest result](results/006-classify-to-adapt-rerun-2-2026-07-27.md) |
| [Adapt to Validate](prompts/007-adapt-to-validate.md) | Adapt completion, validation semantics and provenance, evidence sufficiency, lifecycle ordering, negative cases, and repository mutation protection | Yes | 2026-07-28 | No | [View latest result](results/007-adapt-to-validate-rerun-4-2026-07-28.md) |

## Result History

- Prompt 005 initial run: [Failed](results/005-evaluate-to-classify.md)
- Prompt 005 rerun after framework corrections: [Passed](results/005-evaluate-to-classify-rerun-2026-07-27.md)
- Prompt 006 initial run: [Failed](results/006-classify-to-adapt.md)
- Prompt 006 rerun after structured adaptation changes: [Failed](results/006-classify-to-adapt-rerun-2026-07-27.md)
- Prompt 006 rerun after pending-approval correction: [Passed](results/006-classify-to-adapt-rerun-2-2026-07-27.md)
- Prompt 007 initial run: [Failed](results/007-adapt-to-validate.md)
- Prompt 007 rerun after structured validation changes: [Failed](results/007-adapt-to-validate-rerun-2026-07-28.md)
- Prompt 007 rerun after Adapt-completion matrix correction: [Inconclusive due to immutable-revision resolution limitation](results/007-adapt-to-validate-rerun-2-2026-07-28.md)
- Prompt 007 rerun against immutable revision after matrix correction: [Failed due to deferred-adaptation schema conflict](results/007-adapt-to-validate-rerun-3-2026-07-28.md)
- Prompt 007 rerun after deferred-validation-status schema correction: [Failed due to deferred approval-status conflict](results/007-adapt-to-validate-rerun-4-2026-07-28.md)

## Directory Structure

```text
test/ai/
├── README.md
├── prompts/
│   ├── README.md
│   ├── 001-startup-validation.md
│   ├── 002-execution-creation.md
│   ├── 003-execute-to-observe.md
│   ├── 004-observe-to-evaluate.md
│   ├── 005-evaluate-to-classify.md
│   ├── 006-classify-to-adapt.md
│   └── 007-adapt-to-validate.md
└── results/
    ├── 001-startup-validation.md
    ├── 002-execution-creation.md
    ├── 003-execute-to-observe.md
    ├── 004-observe-to-evaluate.md
    ├── 005-evaluate-to-classify.md
    ├── 005-evaluate-to-classify-rerun-2026-07-27.md
    ├── 006-classify-to-adapt.md
    ├── 006-classify-to-adapt-rerun-2026-07-27.md
    ├── 006-classify-to-adapt-rerun-2-2026-07-27.md
    ├── 007-adapt-to-validate.md
    ├── 007-adapt-to-validate-rerun-2026-07-28.md
    ├── 007-adapt-to-validate-rerun-2-2026-07-28.md
    ├── 007-adapt-to-validate-rerun-3-2026-07-28.md
    └── 007-adapt-to-validate-rerun-4-2026-07-28.md
```

## Status Rules

- **Run** indicates whether the prompt has been executed against the target framework repository.
- **Last Run** records the most recent known execution date.
- **Passed** indicates whether the most recent execution met the expected result.
- **Test Result** links to the captured result for the most recent run.
