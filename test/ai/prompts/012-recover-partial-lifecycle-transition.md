# AI Flywheel Partial Lifecycle Transition Recovery Verification

## Recover Execution-First, State-Failed Transition Across a Fresh Session (Non-Persistent)

> **Purpose**
>
> Verify that a lifecycle transition interrupted after the execution update but before the state update can be discovered and recovered deterministically by a fresh operator session using only durable repository artifacts, including deterministic validation of the complete structured recovery finding.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `fdb270be55d77b2588b7d589021479c5f6e3097f`

Use this exact revision. Do not resolve or substitute a later branch head.

# Authorization

This prompt authorizes synthetic, read-only operating-model verification. Read framework files, resolve durable framework context, construct complete hypothetical mission, goal, execution, state, persistence-plan, finding, revision, digest, and recovery fixtures in memory, validate them, and construct invalid fixtures.

Do not create, modify, or delete repository files; activate, transition, roll back, or resume the durable onboarding execution; update durable state; persist synthetic plans or findings; inspect an application repository; commit; push; or advance the durable lifecycle.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

# Focused Resolution

Read these 17 files from the immutable revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/startup.md`
4. `.flywheel/operating-model/guidance/execution-model.md`
5. `.flywheel/operating-model/guidance/transition-recovery.md`
6. `.flywheel/operating-model/guidance/lifecycle.md`
7. `.flywheel/operating-model/guidance/failure-handling.md`
8. `.flywheel/operating-model/guidance/records.md`
9. `.flywheel/operating-model/guidance/evidence.md`
10. `.flywheel/operating-model/guidance/persistence.md`
11. `.flywheel/operating-model/config/validation.yaml`
12. `.flywheel/operating-model/schemas/state.schema.yaml`
13. `.flywheel/operating-model/schemas/mission.schema.yaml`
14. `.flywheel/operating-model/schemas/goal.schema.yaml`
15. `.flywheel/operating-model/schemas/execution.schema.yaml`
16. `.flywheel/operating-model/schemas/record.schema.yaml`
17. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`

Also read the active mission and active goal identified by durable state for context. If durable state identifies an active execution or nonterminal persistence plan, read it for context without modifying it.

Report the immutable SHA, `17/17` required-file resolution, and contextual resolution. A missing required file fails verification. Do not stop because multiple reads are required.

# Synthetic Mission and Goal

Construct complete schema-valid in-memory mission and goal artifacts using:

- Mission ID: `verify-transition-recovery`
- Goal ID: `recover-partial-lifecycle-transition`
- Mission criterion: `MSC-930`
- Goal criteria in exact order: `AC-930`, `AC-931`, `AC-932`, `AC-933`, `AC-934`, `AC-935`, `AC-936`

The seven goal criteria must respectively cover durable transition-plan reconstruction, deterministic partial-state recognition, exact execution rollback, durable structured recovery finding and recovery plan, original-plan finalization and continuation boundary, negative fixtures, and repository immutability.

Include all required fields, one evidence requirement per acceptance criterion, read-only constraints, and no required approvals. Construct sufficient in-memory evidence mappings for all seven criteria.

# Stable Pre-Transition Fixture

Use one execution identity throughout:

```text
EX-20260729T050000Z-001
```

Construct a complete schema-valid execution and matching state representing a transition-ready Evaluate stage:

- Execution status `in-progress`.
- Execute and Observe completed.
- Evaluate is the sole `in-progress` stage.
- Evaluate contains complete schema-valid evaluations and references sufficient for completion, but its lifecycle stage has not yet been marked completed.
- Classify through Reuse are pending.
- Mission, goal, execution, state status, and lifecycle stage agree.
- Existing actions, observations, evaluations, evidence, and stage references are durable and use stable identifiers.
- `completed_at`, `outcome`, completion disposition, and completion rationale are null.

Use whole-second UTC timestamps and preserve exact pre-transition execution and state content plus retained blob SHAs and normalized SHA-256 content digests.

The exact next authorized action in this pre-transition pair is to validate Evaluate completion and perform the Evaluate-to-Classify lifecycle transition. Do not repeat completed evaluation work.

# Proposed Evaluate-to-Classify Transition

Construct complete proposed execution and state artifacts using transition instant:

```text
2026-07-29T05:10:00Z
```

The proposed execution must:

- Preserve all identities and prior durable content.
- Mark Evaluate `completed` with a valid summary and completion timestamp.
- Mark Classify as the sole `in-progress` stage with `started_at` equal to or later than Evaluate completion.
- Leave Adapt through Reuse pending.
- Preserve null execution completion fields and `status: in-progress`.

The proposed state must:

- Retain the same mission, goal, and execution.
- Set `lifecycle_stage: classify`.
- Remain `status: active`.
- Update `last_durable_update` using one stable operator identity and the same transition instant.

Validate the complete proposed pair before constructing the plan.

# Original Transition Plan

> **PROPOSED ONLY — NOT WRITTEN**

Use transition plan identity:

```text
PERSIST-20260729T051000Z-001
```

Construct a complete schema-valid persistence plan that governs only:

1. The execution CAS update.
2. The state CAS update.

The plan must:

- Be at the canonical `persistence/` path.
- Match the synthetic mission, goal, and execution.
- Begin as `planned`, then become `applying` through retained-SHA CAS before target writes.
- Include exact execution and state paths.
- Use `operation: update` and `mutability: cas-update` for both targets.
- Retain current blob SHAs as preconditions.
- Include exact normalized SHA-256 proposed-content digests.
- Include exact retained-content digests for rollback.
- Order execution before state, with state last.
- Exclude itself from targets and write order.
- Use recovery mode `not-started`, null finding reference, null blocker, and pending final verification while applying.

This plan is a lifecycle transition plan, not checkpoint persistence and not lifecycle Persist completion.

# Synthetic Partial Transition

Construct the durable repository state after this exact failure sequence:

1. The original transition plan is durable and `applying`.
2. All target preconditions were re-read and current before the first target write.
3. The execution CAS update succeeded and returned a new execution blob SHA.
4. The updated execution was re-read and its digest equals the plan's proposed execution digest.
5. Before state CAS, the state update failed or the operation was interrupted.
6. State remains exactly at its retained precondition SHA and content.
7. The original plan remains `applying` with final verification pending.
8. No recovery finding or recovery plan exists yet.
9. A fresh operator session begins with no access to prior chat history or in-memory transition content.

The current execution therefore represents Classify in progress while state still represents Evaluate in progress.

# Startup Recovery Classification

Perform startup against the synthetic partial repository and prove:

1. The state/execution disagreement is detected.
2. Records are inspected before the mismatch is classified as unexplained corruption.
3. Exactly one nonterminal transition plan governs the current execution and state paths.
4. Plan mission, goal, execution, targets, order, preconditions, proposed digests, and rollback data are complete and valid.
5. Current execution digest equals the plan's proposed execution digest.
6. Current execution SHA differs from its retained precondition SHA.
7. Current state still equals its retained precondition SHA and content.
8. No second nonterminal plan claims either mutable target.
9. The condition is classified exactly as `execution written, state not written`.
10. Recovery authority comes only from durable artifacts.
11. Goal-directed lifecycle work remains prohibited until recovery is durably complete.

Do not treat the proposed Classify stage as authoritative while the plan remains nonterminal.

# Exact Rollback

Demonstrate the complete non-persistent rollback sequence:

1. Re-read the original plan, execution, and state.
2. Reconfirm unique plan ownership and current revisions.
3. Resolve exact retained execution content from the plan's retained execution blob SHA.
4. Verify its normalized content digest equals the execution target's `rollback.retained_content_digest`.
5. Verify current execution content equals the planned proposed digest.
6. Verify state still equals its retained precondition.
7. Hypothetically CAS-update execution from its current post-write SHA to the exact retained pre-transition content.
8. Re-read execution and state.
9. Verify both exactly equal the retained pre-transition pair.
10. Do not update, retry, or roll back state.

A rollback that reconstructs, semantically normalizes, retimes, or otherwise changes the retained execution content fails. Exact retained bytes after the framework's specified normalization boundary are required.

# Structured Recovery Finding

Use finding identity:

```text
FIND-930
```

Construct a complete schema-valid create-only finding with:

- `kind: finding`
- `finding.finding_type: partial-lifecycle-transition`
- A complete `finding.transition_recovery` object.

The structured recovery payload must include:

- `original_plan_id` and canonical `original_plan_path`.
- `transition_operator`, `transition_at`, and recovery `observed_at`.
- Exactly one target snapshot for each original-plan target.
- Each target's ID, artifact type, path, operation, retained SHA and digest, proposed digest, observed SHA and digest, write result, and failure detail.
- At least one target with `write_result: succeeded`.
- At least one target with `write_result: failed` or `not-attempted`.
- A nonempty `failure_condition`.
- Structured rollback data: attempted status, target IDs, exact result, restored content digest, `state_mutated`, and detail.
- `original_pair_restored`.
- `continuation_prohibited: true` and a nonempty reason.
- A nonempty `recovery_action`.
- `human_reconciliation_required`.

For the successful exact-rollback fixture:

- Execution target write result is `succeeded`.
- State target write result is `failed` or `not-attempted`, with a nonempty failure detail.
- Rollback is attempted against the execution target.
- Rollback result is `succeeded`.
- Restored content digest equals the retained execution digest.
- `state_mutated: false`.
- `original_pair_restored: true`.
- `human_reconciliation_required: false`.

Validate the finding against `record.schema.yaml`, then perform the semantic cross-checks required by `transition-recovery.md` and `validation.yaml`:

- Top-level mission, goal, and execution agree with the original plan.
- Plan ID, canonical path, and source/artifact references resolve to the same plan.
- Every target maps exactly once to the original plan.
- Target paths, operations, retained SHAs and digests, and proposed digests equal the original plan.
- Observed SHAs and digests equal the synthetic durable recovery revisions.
- Write results, failure, rollback, restoration, continuation, and recovery action agree with the durable trace.

# Recovery Persistence Plan

Use recovery plan identity:

```text
PERSIST-20260729T051500Z-001
```

Construct a complete schema-valid recovery persistence plan that:

- Governs creation of `FIND-930` at its canonical path.
- Uses create-only semantics and confirmed absence.
- Contains the finding's exact normalized content digest.
- Excludes itself from targets and write order.
- Is created, activated, applied, verified, finalized to `applied`, and re-read conceptually.
- Does not modify the restored execution or unchanged state merely to add a finding reference.

Prove that the finding remains discoverable through canonical goal records and `execution_id` even though the restored execution does not yet reference it.

# Original Plan Finalization

After exact rollback and durable recovery finding verification, construct the original transition plan's terminal update:

- `status: rolled-back`
- `recovery.mode: exact-rollback`
- `recovery.finding_ref: FIND-930`
- `recovery.blocker: null`
- `final_verification.required: true`
- Non-null whole-second `verified_at`
- `final_verification.result: passed`

Update the original plan only through retained-SHA CAS. Re-read the original plan, recovery plan, finding, execution, and state.

Report the transition not applied only after:

- The original execution/state pair is exactly restored.
- The structured recovery finding is schema-valid, semantically valid, and durable.
- The recovery plan is terminal `applied` and verified.
- The original transition plan is terminal `rolled-back` and verified.
- No unexplained mutable target change exists.

# Next Authorized Action After Recovery

The exact next authorized action after successful recovery is:

```text
Revalidate the already-complete durable Evaluate work against the current
execution and state revisions, then construct a new plan-governed
Evaluate-to-Classify transition without repeating the completed evaluations.
```

The rolled-back transition plan must not be reused, returned to `planned`, or changed to `applied` after terminal rollback.

# Alternate Deterministic States

Construct and evaluate:

1. **No target written:** Finalize as `rolled-back` with `recovery.mode: not-started`, null finding, no blocker, and final verification `passed`; verify the pair remains original. No recovery finding is required.
2. **Both targets written, plan still applying:** Verify the complete proposed set and finalize the exact plan to `applied`; do not roll back solely because a new session began.
3. **Rollback cannot be proven:** Persist a schema-valid structured blocking recovery finding when safely possible, finalize the original plan to `blocked` when its revision remains owned, and require human reconciliation.

# Negative Validation

Construct invalid fixtures and demonstrate deterministic rejection of:

1. State/execution mismatch with no durable transition plan.
2. Two nonterminal plans governing the same execution or state target.
3. Plan mission, goal, or execution identity mismatch.
4. Plan omits execution or state target.
5. Plan orders state before execution.
6. Plan lacks retained precondition SHA, proposed digest, or retained rollback digest.
7. Plan includes itself as a target or write-order item.
8. Current execution matches neither retained content nor proposed digest.
9. Current state no longer matches its retained precondition.
10. Operator retries state after execution success.
11. Operator rolls back state.
12. Rollback uses reconstructed or modified execution content.
13. Resolved retained content digest does not match the plan.
14. Rollback uses a stale post-write execution SHA or force update.
15. Recovery is claimed without final execution/state pair re-read.
16. `finding_type: partial-lifecycle-transition` omits `transition_recovery`.
17. Structured recovery payload omits any required plan, timestamp, target, failure, rollback, restoration, continuation, recovery-action, or reconciliation field.
18. Target list lacks a succeeded write or lacks a failed/not-attempted write.
19. Update target omits retained SHA or retained digest.
20. Successful target omits observed SHA/digest or supplies non-null failure detail.
21. Failed/not-attempted target omits failure detail.
22. Successful rollback omits restored digest or records `state_mutated: true`.
23. Original pair is not restored but human reconciliation is false.
24. Finding plan ID/path/reference does not resolve to the original plan.
25. Finding target is missing, duplicated, extra, or does not map to the original plan.
26. Finding target path, operation, retained SHA/digest, or proposed digest differs from the original plan.
27. Observed SHA/digest differs from the durable artifact used for recovery.
28. Write result, failure, rollback, restoration, continuation, or recovery action contradicts the durable recovery trace.
29. Finding is written without a recovery persistence plan.
30. Restored execution is modified solely to add the recovery finding reference.
31. Original plan is marked `rolled-back` before the finding and recovery plan are durable.
32. Original plan finalization uses a stale plan SHA.
33. Original plan returns from `rolled-back` to `planned`, `applying`, or `applied`.
34. Classify work begins while the original plan remains `planned`, `applying`, `failed`, or `blocked`.
35. Pre-transition Evaluate work is repeated after successful rollback.
36. State was written while execution remained retained and automatic recovery is attempted.
37. Both targets match proposed content but rollback occurs without checking exact-plan finalization.
38. Plan is terminal `applied` while either target differs from proposed content.
39. Recovery finding or plan exists only in chat or memory.
40. A terminal or unrelated plan is used as recovery authority.
41. Repository artifacts are actually written during this synthetic verification.
42. A no-target-written plan is finalized as `failed` and continuation is allowed.
43. Classify begins after rollback by reusing the rolled-back plan.

For cases 16 through 23, report whether rejection is enforced directly by `record.schema.yaml`. For cases 24 through 28, report the specific semantic rule that rejects the fixture.

A case that cannot be rejected deterministically is a reusable framework defect.

# Required Validation Results

Report separately:

1. Immutable revision and focused resolution.
2. Durable framework context and synthetic authorization.
3. Mission and goal schema validation.
4. Pre-transition execution and state schema validation.
5. Proposed transition pair validation.
6. Original transition-plan schema and semantic validation.
7. Plan activation and precondition validation.
8. Partial durable-state reconstruction.
9. Unique recovery-authority resolution.
10. Execution-written/state-not-written classification.
11. Transaction-pending authority boundary.
12. Exact retained-content resolution and digest verification.
13. Execution rollback CAS and state non-mutation.
14. Restored-pair verification.
15. Structured recovery finding schema validation.
16. Structured recovery finding semantic cross-checks.
17. Recovery plan target derivation, ordering, commit marker, and verification.
18. Original transition-plan rolled-back finalization.
19. Fresh-session reconstruction without chat history.
20. Next authorized action and non-repetition.
21. No-target-written alternate state.
22. Both-targets-written alternate state.
23. Unrecoverable rollback blocking state.
24. Negative validation cases.
25. Acceptance-criterion evidence mapping.
26. Repository immutability.

For each include expected condition, actual condition, result, and enforcing source.

# Framework Defects

Report only reusable framework defects. Include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during partial lifecycle transition recovery verification.

# Required Output

Use these sections in order:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Synthetic Mission and Goal
5. Pre-Transition Execution and State
6. Proposed Evaluate-to-Classify Transition
7. Original Transition Plan
8. Synthetic Partial Durable State
9. Startup Recovery Classification
10. Exact Execution Rollback
11. Restored Execution and State
12. Structured Recovery Finding
13. Recovery Persistence Plan
14. Original Plan Finalization
15. Alternate Deterministic States
16. Next Authorized Action
17. Acceptance-Criterion Evidence Mapping
18. Validation Results
19. Negative Validation Results
20. Framework Defects
21. Repository Mutation Confirmation
22. Next Test Action

The summary must report:

```text
Operating Validation: Passed | Failed
Verification Result: Passed | Failed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: <count>
```

The final next test action must be one of:

- Request an independent private-session run of Prompt 012 when verification passes with no reusable defect.
- Correct the reusable framework defect on the framework testing branch, pin the prompt to the corrected immutable commit, and rerun Prompt 012.
- Correct only the prompt or synthetic fixture when the framework is sufficient, then rerun Prompt 012.
