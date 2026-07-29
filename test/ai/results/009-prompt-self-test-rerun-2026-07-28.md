# Prompt 009 Final Self-Test

## Summary

```text
Prompt Validation: Passed
Framework Revision: d7cf8e6928d818d7f51485fb79c7a6a4c931a2d7
Prompt Changes Required: None
Framework Changes Required: None
Repository Changes During Verification: None
```

## Scope

This self-test evaluated the revised `009-persist-to-reuse.md` after the initial independent run exposed incomplete repository resolution and fixture-boundary problems.

The test focused on:

- The pinned immutable framework revision.
- The 18 transition-relevant repository artifacts.
- Complete synthetic mission and goal shapes.
- Acceptance criteria `AC-901` through `AC-905` and their evidence mappings.
- Persist completion and Reuse activation.
- Reuse-assessment schema conditions.
- Knowledge promotion, supersession, and immutable deprecation tombstones.
- Dedicated Reuse-output persistence ordering.
- Terminal execution completion.
- Terminal synthetic state with cleared active pointers.
- Negative fixture coverage.

## Findings

### Synthetic mission and goal

The prompt now provides complete schema-shaped synthetic mission and goal artifacts. The synthetic work is no longer forced into the repository's actual onboarding goal.

### Execution lifecycle

The activation fixture uses exactly one active stage: Reuse. The terminal fixture changes the execution to `succeeded`, supplies `completed_at`, `outcome`, and `completion`, and leaves every lifecycle stage terminal.

The prompt explicitly prohibits leaving an `in-progress` execution after all lifecycle stages become terminal.

### State lifecycle

The activation state identifies the synthetic execution and `lifecycle_stage: reuse`. The terminal state clears active mission, goal, execution, and lifecycle pointers and uses `status: ready`.

### Acceptance-criterion completion

The prompt requires evidence mappings for all five synthetic acceptance criteria before terminal execution, goal, or mission completion can be claimed.

### Reuse assessments

The assessment model supports:

- Candidate-learning and existing-knowledge subjects.
- Planned and completed assessment states.
- Promotion, supersession, deferral, rejection, not-reusable, reused, inapplicable, revision-required, deprecated, and not-considered dispositions.
- Evidence, validation, applicability, limitations, reuse guidance, approval, decision, duplicate, conflict, and supersession fields.

Promotion and supersession require evidence, validation, applicability, actionable guidance, and a proposed knowledge identity. Supersession requires prior knowledge references.

### Knowledge history

Validated knowledge uses create-only identities. Replacement uses a new identity with `supersedes`. Deprecation uses a new immutable tombstone artifact with a decision and prior-knowledge reference; the prior artifact is never edited.

### Reuse-output durability

The prompt requires a dedicated persistence plan containing every Reuse output. Canonical ordering places decisions and approvals before reuse assessments, assessments before knowledge, execution before state, and state last. The plan must exclude itself, use create-only semantics for assessments and knowledge, apply CAS to existing mutable targets, verify every write and the final set, and define rollback or compensation.

### Negative coverage

The 41 negative cases cover premature activation, invalid promotion, missing provenance, unresolved duplicates or conflicts, unsafe deprecation, missing approvals, incomplete assessments, omitted persistence targets, incorrect ordering, stale CAS, invalid terminal execution/state, unsupported mission or goal completion, and repository mutation.

## Decision

Prompt 009 is ready for an independent private-session run against framework revision:

`d7cf8e6928d818d7f51485fb79c7a6a4c931a2d7`

The independent framework result remains inconclusive until rerun; this prompt self-test does not mark Prompt 009 as passed.