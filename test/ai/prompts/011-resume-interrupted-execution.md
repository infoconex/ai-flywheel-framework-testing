# AI Flywheel Interrupted Execution Resume Verification

## Durable Resume Across a Fresh Session (Non-Persistent)

> **Purpose**
>
> Verify that a durable interrupted execution can be discovered, validated, and resumed safely by a fresh operator session without relying on chat history, changing execution identity, repeating completed work, losing evidence, or overwriting concurrent changes.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `9f128c1c3aeb4a0fbdac9fcddaa95546539f0226`

Use this exact revision. Do not resolve or substitute a later branch head.

# Authorization

This prompt authorizes synthetic, read-only operating-model verification. Read framework files, resolve the durable framework context, construct complete hypothetical mission, goal, execution, state, record, and revision fixtures in memory, validate them, and construct invalid fixtures.

Do not create, modify, or delete repository files; activate or resume the durable onboarding execution; update durable state; persist synthetic artifacts; inspect an application repository; commit; push; or advance the durable lifecycle.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

# Focused Resolution

Read these files from the immutable revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/startup.md`
4. `.flywheel/operating-model/guidance/execution-model.md`
5. `.flywheel/operating-model/guidance/lifecycle.md`
6. `.flywheel/operating-model/guidance/failure-handling.md`
7. `.flywheel/operating-model/guidance/records.md`
8. `.flywheel/operating-model/guidance/evidence.md`
9. `.flywheel/operating-model/config/validation.yaml`
10. `.flywheel/operating-model/schemas/state.schema.yaml`
11. `.flywheel/operating-model/schemas/mission.schema.yaml`
12. `.flywheel/operating-model/schemas/goal.schema.yaml`
13. `.flywheel/operating-model/schemas/execution.schema.yaml`
14. `.flywheel/operating-model/schemas/record.schema.yaml`
15. `.flywheel/operating-model/schemas/startup-failure.schema.yaml`

Also read the active mission and active goal identified by durable state for context. If durable state identifies an active execution, read it for context without modifying it.

Report the immutable SHA, `15/15` required-file resolution, and contextual resolution. A missing required file fails verification. Do not stop because multiple reads are required.

# Synthetic Mission and Goal

Construct complete schema-valid in-memory mission and goal artifacts using:

- Mission ID: `verify-resume-recovery`
- Goal ID: `verify-interrupted-execution-resume`
- Mission criterion: `MSC-920`
- Goal criteria in exact order: `AC-920`, `AC-921`, `AC-922`, `AC-923`, `AC-924`, `AC-925`

The six goal criteria must respectively cover durable reconstruction, identity and lifecycle continuity, interruption-reason preservation, exact next-action selection, CAS and stale-revision safety, and deterministic rejection of contradictory active-execution states.

Include all required fields, one evidence requirement per acceptance criterion, read-only constraints, and no required approvals. Construct sufficient in-memory evidence mappings for all six criteria.

# Stable Interrupted Fixture

Use one execution identity throughout:

```text
EX-20260729T040000Z-001
```

Construct a complete schema-valid execution and matching state with:

- Execution status `interrupted`.
- A nonempty interruption reason in `outcome`.
- Null `completed_at`, completion disposition, and completion rationale.
- Mission and goal IDs matching synthetic state.
- Exactly one in-progress lifecycle stage: `evaluate`.
- Execute and Observe completed with valid timestamps, summaries, references, actions, observations, and durable evidence.
- Evaluate started but incomplete.
- Classify through Reuse pending.
- Previously durable evidence, records, and stage references with stable identifiers and canonical paths.
- State status consistent with an interrupted active execution, retaining the same active execution and `lifecycle_stage: evaluate`.
- Retained execution and state blob SHAs representing the pre-resume revisions.

Use stable new-session operator identity `chatgpt-session` unless the framework exposes an authenticated repository actor in the synthetic fixture. The new operator identity is session identity only; it must not replace the execution identity or rewrite prior actor history.

# Startup and Resume Decision

Perform the startup protocol against the synthetic fixture and prove:

1. The active execution is discovered from durable state.
2. Mission, goal, execution, state, status, and lifecycle stage agree.
3. The execution is resumable under the framework rules.
4. The interruption reason is nonempty and durable.
5. All references required by completed stages and active Evaluate resolve to durable artifacts.
6. Reconstruction uses no chat history, prior-session memory, or unpersisted plan.
7. The existing execution is selected rather than creating a new execution.
8. The exact next authorized action is the first incomplete Evaluate action supported by durable observations and evidence.
9. Completed Execute and Observe actions are not repeated.
10. No application or repository mutation occurs during this synthetic test.

# Proposed Resume Transition

Construct the complete proposed execution and state pair for resume using one whole-second UTC transition timestamp.

The proposed transition must:

- Preserve execution ID, mission ID, goal ID, `started_at`, acceptance criteria, all lifecycle history, completed timestamps, evidence, observations, actions, references, and prior durable content.
- Preserve the interruption reason durably in an appended execution action or referenced durable record before clearing `outcome`.
- Change execution status from `interrupted` to `in-progress`.
- Set `outcome` to null only after the reason is durably preserved.
- Keep `completed_at`, completion disposition, and completion rationale null.
- Keep Evaluate as the sole in-progress lifecycle stage without changing its original `started_at`.
- Leave Classify through Reuse pending.
- Set state status to `active`.
- Retain the same active mission, goal, execution, and lifecycle stage.
- Update `last_durable_update.at`, `.by`, and `.reason` for the resume transition.
- Use the new session operator identity only in the new resume metadata.

Validate the complete proposed pair before any hypothetical write.

# Compare-and-Swap Sequence

Demonstrate the exact non-persistent resume sequence:

1. Retain complete current execution and state content and their blob SHAs.
2. Validate the current durable pair and resume eligibility.
3. Construct and validate the complete proposed pair.
4. Re-read execution and state and confirm both retained SHAs remain current.
5. Hypothetically update execution first using CAS against the retained execution SHA.
6. Re-read state and verify its retained SHA remains current.
7. Hypothetically update state using CAS against the retained state SHA.
8. Re-read both and verify they exactly equal the validated proposed pair.
9. Report resume durable only after final pair verification.

Do not perform actual writes.

# Stale and Partial-Transition Cases

Construct and evaluate:

- Execution revision changes before the first write: reject with no writes.
- State revision changes before the first write: reject with no writes.
- Execution CAS succeeds but state revision changes before state CAS: do not overwrite state; apply exact-content execution rollback using the returned post-update execution SHA; require a durable finding.
- Rollback succeeds: verify the original durable pair and report resume not applied.
- Rollback fails: block continuation and require human reconciliation.
- Retrying state against a newer SHA: reject.
- Force update of either artifact: reject.

# Negative Validation

Construct invalid fixtures and demonstrate deterministic rejection of:

1. Interrupted execution with null or empty interruption reason.
2. State points to a missing execution.
3. State points to a terminal execution.
4. State and execution disagree on mission, goal, execution ID, status, or lifecycle stage.
5. No lifecycle stage is in progress.
6. Multiple lifecycle stages are in progress.
7. A predecessor is incomplete or a successor has already started.
8. Multiple executions appear active for the goal and durable state does not resolve the ambiguity uniquely.
9. An active-stage reference is missing, stale, ambiguous, or nondurable.
10. Resume creates a new execution ID.
11. Resume changes mission, goal, original start timestamp, completed stage timestamps, or existing evidence.
12. Resume repeats a completed Execute or Observe action.
13. Resume selects its next action from chat history or memory.
14. Resume clears the interruption reason without preserving it durably.
15. Resume changes Evaluate `started_at` merely because a new session began.
16. Resume advances to Classify before Evaluate completion.
17. Resume uses a stale execution or state SHA.
18. Resume updates state before execution.
19. Resume retries state against a newly observed SHA after execution CAS succeeds.
20. Resume reports success before final pair verification.
21. A blocked execution becomes in-progress without durable blocker reconciliation or human authorization.
22. A terminal execution is mutated.
23. Synthetic verification writes repository artifacts.

A case that cannot be rejected deterministically is a reusable framework defect.

# Required Validation Results

Report separately:

1. Immutable revision and focused resolution.
2. Durable framework context and synthetic authorization.
3. Mission and goal schema validation.
4. Interrupted execution and state schema validation.
5. Startup active-execution resolution.
6. Resumability decision.
7. Durable reconstruction without chat history.
8. Stable operator identity for the new session.
9. Existing execution identity preservation.
10. Interruption-reason validation and preservation.
11. Lifecycle-stage and timestamp continuity.
12. Durable reference validation.
13. Exact next authorized action.
14. Non-repetition of completed work.
15. Proposed resume-pair validation.
16. Compare-and-swap prechecks and ordering.
17. Final pair verification.
18. Stale-revision rejection.
19. Partial-transition rollback and reconciliation.
20. Invalid active-execution-state rejection.
21. Acceptance-criterion evidence mapping.
22. Repository immutability.

For each include expected condition, actual condition, result, and enforcing source.

# Framework Defects

Report only reusable framework defects. Include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during interrupted execution resume verification.

# Required Output

Use these sections in order:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Synthetic Mission and Goal
5. Interrupted Execution Fixture
6. Startup Resolution
7. Resumability Decision
8. Proposed Resume Transition
9. Exact Next Authorized Action
10. Durable Evidence and Reference Preservation
11. Compare-and-Swap Results
12. Stale and Partial-Transition Recovery Results
13. Acceptance-Criterion Evidence Mapping
14. Validation Results
15. Negative Validation Results
16. Framework Defects
17. Repository Mutation Confirmation
18. Next Authorized Action

The summary must report:

```text
Operating Validation: Passed | Failed
Verification Result: Passed | Failed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: <count>
```

The final next authorized action must be one of:

- Request an independent private-session run of Prompt 011 when verification passes with no reusable defect.
- Correct the reusable framework defect on the framework testing branch, pin the prompt to the corrected immutable commit, and rerun Prompt 011.
- Correct only the prompt or synthetic fixture when the framework is sufficient, then rerun Prompt 011.
