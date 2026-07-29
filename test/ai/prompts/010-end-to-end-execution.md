# AI Flywheel End-to-End Verification
## Full Execution Lifecycle (Non-Persistent)

> **Purpose**
>
> Verify that one coherent synthetic execution can move from creation through all eight lifecycle stages and terminal closure without accumulated contradiction or repository mutation.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `b79e505dbcc8dde9966ee581a124647b2d7fb08b`

Use this exact revision. Do not resolve or substitute a later branch head.

# Authorization

This prompt authorizes synthetic, read-only operating-model verification. Read framework files, construct complete hypothetical artifacts in memory, validate them, and construct invalid fixtures.

Resolve actual durable state, mission, and goal as context only. Do not force the synthetic fixture into the active onboarding goal.

Do not create, modify, or delete repository files; activate an execution; update durable state; persist artifacts; inspect an application repository; commit; push; or advance the durable lifecycle.

Label every displayed artifact:

> **PROPOSED ONLY — NOT WRITTEN**

# Focused Resolution

Read these 20 files from the immutable revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/lifecycle.md`
4. `.flywheel/operating-model/guidance/execution-model.md`
5. `.flywheel/operating-model/guidance/records.md`
6. `.flywheel/operating-model/guidance/evidence.md`
7. `.flywheel/operating-model/guidance/classifications.md`
8. `.flywheel/operating-model/guidance/adaptation.md`
9. `.flywheel/operating-model/guidance/validation.md`
10. `.flywheel/operating-model/guidance/persistence.md`
11. `.flywheel/operating-model/guidance/reuse.md`
12. `.flywheel/operating-model/config/validation.yaml`
13. `.flywheel/operating-model/schemas/state.schema.yaml`
14. `.flywheel/operating-model/schemas/mission.schema.yaml`
15. `.flywheel/operating-model/schemas/goal.schema.yaml`
16. `.flywheel/operating-model/schemas/execution.schema.yaml`
17. `.flywheel/operating-model/schemas/record.schema.yaml`
18. `.flywheel/operating-model/schemas/knowledge.schema.yaml`
19. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
20. `.flywheel/operating-model/schemas/reuse-assessment.schema.yaml`

Also read the active mission and active goal identified by durable state for context. Report the SHA, `20/20` resolution, and contextual resolution. A missing required file fails verification. Do not stop because multiple reads are required.

# Synthetic Mission and Goal

Construct complete schema-valid in-memory mission and goal artifacts using:

- Mission ID: `verify-end-to-end-lifecycle`
- Goal ID: `verify-complete-execution`
- Mission criterion: `MSC-910`
- Goal criteria in exact order: `AC-910`, `AC-911`, `AC-912`, `AC-913`, `AC-914`, `AC-915`

The six goal criteria must respectively cover lifecycle identity/state continuity, cross-stage provenance, checkpoint and final transaction completeness, knowledge qualification and immutable history, negative fixtures, and repository immutability.

Include complete required fields, one evidence requirement per acceptance criterion, read-only constraints, and no required approvals. Construct sufficient in-memory evidence mappings for all six before terminal completion.

# Stable Fixture

Use one execution identity throughout:

```text
EX-20260728T210000Z-001
```

Include:

- One approved, implemented, and passed adaptation.
- One rejected or deferred adaptation that is not validation-eligible.
- One failed required validation with evidence, finding, recovery action, and authorized persistence-permitting disposition.
- One confirmed validated-learning classification eligible for promotion.
- One provisional or execution-specific learning item that must not be promoted.
- Existing applicable and inapplicable knowledge, a duplicate, and a conflict requiring supersession or immutable deprecation.
- Complete evidence, decisions, findings, approvals, validations, assessments, and knowledge artifacts.

All identities, references, timestamps, statuses, and scope values must remain stable.

# Transition and Checkpoint Sequence

Reconstruct execution and state snapshots for:

1. Execution creation and Execute activation.
2. Execute completion and Observe activation.
3. Observe completion and Evaluate activation.
4. Evaluate completion and Classify activation.
5. Classify completion and Adapt activation.
6. Adapt completion and Validate activation.
7. Validate completion and Persist activation.
8. Persist transaction commit and Reuse activation.
9. Reuse transaction commit and terminal execution closure.
10. Goal and mission completion with terminal state cleanup.

For every transition verify one active stage, predecessor/successor ordering, stable identities, state agreement, whole-second UTC timestamps, required metadata, compare-and-swap, final pair verification, and recovery.

When a transition first introduces any external evidence, decision, finding, approval, or other durable record referenced by the proposed execution, construct a checkpoint persistence plan. The checkpoint must commit supporting records before execution and state, use the plan commit marker, and be terminal `applied` before the new stage snapshot is authoritative.

When a transition changes only execution and state and introduces no new or changed external reference, validate the direct dual-artifact CAS transition without a checkpoint plan.

Checkpoint plans do not complete the lifecycle Persist stage and do not promote knowledge.

# Cross-Stage Continuity

Prove:

- Execute actions remain within the synthetic goal.
- Observations contain facts rather than later-stage conclusions.
- Evaluations use only referenced observations and evidence.
- Classifications remain traceable to evaluations and evidence.
- Adaptations remain traceable to classifications, evaluations, observations, and evidence.
- Validations target only eligible implemented adaptations and preserve failed-validation history.
- Every external reference is durable before the execution snapshot that first uses it.
- The final Persist transaction verifies all checkpoint artifacts and includes every remaining changed artifact plus planned assessments required for Reuse activation.
- Reuse assessments retain stable identities from planned creation through completed CAS update.
- Knowledge includes evidence, passed validation, applicability, limitations, guidance, origin, and completed-assessment provenance.
- Acceptance-criterion mappings remain valid and durable at terminal closure.

# Checkpoint Plans

Construct representative complete checkpoint plans for transitions that introduce:

- Observation evidence before Observe completion.
- Decisions and approvals before Adapt completion.
- Validation evidence, findings, recovery actions, and failed-validation disposition before Validate completion.

Each plan must include every new supporting target, execution update, and state update; order supporting records before execution and state; use canonical paths, digests, create-only/CAS semantics, final re-read, commit-marker semantics, and recovery.

A checkpointed artifact must not be recreated or included as an unchanged target in the later Persist transaction.

# Persist Transaction

Construct the final Persist-stage plan containing every artifact still new or changed after checkpoint persistence, every required planned reuse assessment, and the execution/state values that will represent Persist completion and Reuse activation when committed.

The plan must verify all earlier checkpoint artifacts referenced by the execution exist unchanged. It must include every remaining changed record, planned assessments, execution, changed goal or mission, and state. It must not include completed assessments or promoted knowledge.

Every planned assessment is a create target at its canonical `reuse/` path, precedes execution/state targets, uses a stable `REUSE-NNN` identity, and has null disposition, rationale, assessment timestamp, and assessor.

The proposed Persist-completed and Reuse-active execution/state values remain transaction-pending while the plan is `applying`. They become authoritative together only after terminal `applied` finalization and re-read. Test `PERSIST-COMMIT-001`.

# Reuse Transaction

Construct a separate plan containing:

- CAS updates of every planned assessment to `completed` using retained planned-record SHAs.
- Validated, superseding, and deprecation-tombstone knowledge referencing completed assessments.
- New Reuse decisions and approvals.
- Completed goal and mission updates.
- Terminal execution update.
- Terminal state update as final pointer.

Verify fixed assessment identity/scope fields remain unchanged, completed fields are supplied, assessments precede knowledge, execution precedes state, state is last, and complete target derivation, CAS, verification, and recovery pass.

Reuse completion, terminal execution, completed goal and mission, and cleared state remain transaction-pending while the plan is applying. They become authoritative together only when the plan is terminal `applied` and re-read. Finalization failure blocks use of pending values and requires reconciliation.

# Terminal Form

Validate all eight stages completed, execution `succeeded`, completion timestamp/outcome/disposition/rationale set, goal and mission completed, state `ready`, and all active pointers null.

Do not leave a terminal lifecycle under an in-progress execution. Do not report or use transaction-pending values before the applicable plan commit marker is verified.

# Required Validation Results

Report separately:

1. Immutable revision and focused resolution.
2. Durable context and synthetic authorization.
3. Mission and goal schema validation.
4. Stable execution creation and identity.
5. All eight lifecycle transition continuities.
6. Checkpoint-plan necessity decisions.
7. Checkpoint schemas, targets, ordering, and commit markers.
8. Cross-stage references and provenance.
9. Evidence and acceptance-criterion mappings.
10. Decision, approval, finding, and failed-validation authorization.
11. Adaptation/validation/persistence synchronization.
12. Planned assessment creation and schema validation.
13. Final Persist plan completeness, ordering, and commit marker.
14. Persist-to-Reuse continuity.
15. Planned-to-completed assessment CAS lifecycle.
16. Knowledge qualification and immutable history.
17. Reuse plan completeness, ordering, and commit marker.
18. Reuse-to-terminal continuity.
19. Terminal execution, goal, mission, and state validation.
20. Compare-and-swap and partial recovery.
21. Timestamp ordering.
22. Repository immutability.

For each include expected condition, actual condition, result, and enforcing source.

# Negative Validation

Construct invalid fixtures and demonstrate deterministic rejection of:

1. Execution, mission, or goal identity changes mid-execution.
2. Two stages active, skipped stage, early successor, or state disagreement.
3. Observation contains unsupported classification or recommendation.
4. Evaluation, classification, or adaptation has missing or stale provenance.
5. Adaptation approval lacks required decision or approval.
6. Rejected or deferred adaptation is validation-eligible.
7. Validation passes without evidence.
8. Failed validation is rewritten or lacks finding, recovery, or governing disposition.
9. Blocking disposition permits persistence.
10. Execution references new external evidence or records before they are durably checkpointed.
11. A required checkpoint is replaced by a direct execution/state transition.
12. A checkpoint omits a referenced supporting record or writes execution/state first.
13. A checkpoint is treated as lifecycle Persist completion or promotes knowledge.
14. The final Persist plan recreates or targets an unchanged checkpoint artifact.
15. The final Persist plan omits a remaining changed artifact or planned assessment.
16. Reuse activates with an assessment existing only in memory.
17. Planned assessment contains final disposition or assessment timestamp.
18. A plan targets or digests itself.
19. State is written before referenced targets.
20. Durability is claimed without whole-set and plan-finalization re-read.
21. Transaction-pending values are reported before `applied`.
22. Plan finalization fails but pending values remain usable.
23. Completed assessment changes fixed identity or scope.
24. Planned assessment completes without retained-SHA CAS.
25. Completed assessment is updated again or returned to planned.
26. Reuse promotes nondurable, provisional, rejected, or failed learning.
27. Duplicate or conflicting knowledge is promoted without proper disposition.
28. Existing knowledge is overwritten.
29. Knowledge references a planned assessment or lacks required provenance and guidance.
30. Reuse plan omits any changed assessment, knowledge, decision, approval, goal, mission, execution, or state target.
31. Knowledge is ordered before its completed assessment.
32. Reuse completes before its plan commit marker is verified.
33. Acceptance criterion uses chat text or an artifact omitted from persistence.
34. A formerly valid reference is stale at terminal closure.
35. Adaptation validation, persistence, or reuse status is unsynchronized.
36. Terminal execution retains a pending/active stage or remains in-progress.
37. Terminal execution lacks required completion data.
38. Goal lacks evidence for any AC-910 through AC-915.
39. Mission completes while its goal is incomplete.
40. State is cleared before terminal artifacts commit or retains an active pointer afterward.
41. Timestamps regress or a stale CAS revision is used.
42. Partial transition or persistence lacks rollback, compensation, or reconciliation.
43. An unplanned artifact changes.
44. Repository artifacts are actually written.

A case that cannot be rejected deterministically is a reusable framework defect.

# Framework Defects

Report only reusable framework defects. Include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during the non-persistent end-to-end lifecycle verification.

# Required Output

Use these sections in order:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Synthetic Mission and Goal
5. Stable Execution Identity
6. Lifecycle Transition Trace
7. Checkpoint Persistence Results
8. Cross-Stage Provenance Findings
9. Representative Execution Record Set
10. Final Persist Plan and Planned Assessments
11. Reuse Assessment and Knowledge Set
12. Reuse Persistence Plan
13. Acceptance-Criterion Evidence Mapping
14. Terminal Execution, Goal, Mission, and State
15. Validation Results
16. Negative Validation Results
17. Commit-Marker, Compare-and-Swap, and Recovery Results
18. Framework Defects
19. Repository Mutation Confirmation
20. Next Authorized Action

The summary must report:

```text
Operating Validation: Passed | Failed
Verification Result: Passed | Failed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: <count>
```

When verification passes, end with:

> Prepare the framework branch for milestone review.

When a reusable framework defect blocks verification, end with:

> Correct only the reusable framework defect before repeating this verification.
