# AI Flywheel End-to-End Verification
## Full Execution Lifecycle (Non-Persistent)

> **Purpose**
>
> Verify that one coherent synthetic execution can move from creation through all eight lifecycle stages and terminal closure without accumulated contradiction or repository mutation.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `bcc1ed3458e3a2d2a800fa14a59db3d351d960e6`

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

Construct these complete in-memory artifacts:

```yaml
mission:
  schema_version: 1
  id: verify-end-to-end-lifecycle
  title: Verify End-to-End Lifecycle
  status: active
  objective: Verify one complete AI Flywheel execution without repository mutation.
  success_criteria:
    - id: MSC-910
      statement: One execution completes every lifecycle stage with deterministic traceability and closure.
  goals: [verify-complete-execution]
  constraints:
    - All artifacts are proposed only and must not be written.
  approvals_required: []

goal:
  schema_version: 1
  id: verify-complete-execution
  mission_id: verify-end-to-end-lifecycle
  title: Verify Complete Execution
  status: active
  objective: Verify lifecycle continuity from execution creation through terminal closure.
  acceptance_criteria:
    - id: AC-910
      statement: Execution identity and state remain consistent through every transition.
    - id: AC-911
      statement: All material values remain traceable across lifecycle stages.
    - id: AC-912
      statement: Persist and Reuse transactions contain every required changed artifact.
    - id: AC-913
      statement: Reusable knowledge is qualified without overwriting history.
    - id: AC-914
      statement: Invalid accumulated and terminal states are deterministically rejected.
    - id: AC-915
      statement: Repository immutability is preserved.
  evidence_required:
    - criterion_id: AC-910
      evidence_types: [lifecycle-transition-trace]
    - criterion_id: AC-911
      evidence_types: [cross-stage-provenance-validation]
    - criterion_id: AC-912
      evidence_types: [durability-transaction-validation]
    - criterion_id: AC-913
      evidence_types: [reuse-and-knowledge-validation]
    - criterion_id: AC-914
      evidence_types: [negative-fixture-results]
    - criterion_id: AC-915
      evidence_types: [repository-immutability-confirmation]
  constraints:
    - All verification is synthetic and read-only.
  approvals_required: []
```

Use exactly `AC-910` through `AC-915`, in order, in the execution. Construct sufficient in-memory evidence mappings for all six before terminal completion.

# Stable Fixture

Use one execution identity throughout:

```text
EX-20260728T210000Z-001
```

Include:

- One approved, implemented, and passed adaptation.
- One rejected or deferred adaptation that is not validation-eligible.
- One failed required validation with evidence, finding, recovery action, and an authorized persistence-permitting disposition.
- One confirmed validated-learning classification eligible for promotion.
- One provisional or execution-specific learning item that must not be promoted.
- Existing applicable and inapplicable knowledge, a semantic duplicate, and a conflict requiring supersession or immutable deprecation.
- Complete evidence, decisions, findings, approvals, validations, assessments, and knowledge artifacts.

All identities, references, timestamps, statuses, and scope values must remain stable.

# Transition Sequence

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

For every transition verify one active stage, predecessor/successor ordering, stable identities, state agreement, whole-second UTC timestamp ordering, required metadata, retained-SHA compare-and-swap, final pair verification, and deterministic recovery.

# Cross-Stage Continuity

Prove:

- Execute actions remain within the synthetic goal.
- Observations contain facts rather than later-stage conclusions.
- Evaluations use only referenced observations and evidence.
- Classifications remain traceable to evaluations and evidence.
- Adaptations remain traceable to classifications, evaluations, observations, and evidence.
- Validations target only eligible implemented adaptations and preserve failed-validation history.
- Persist contains all new or changed artifacts produced through Validate, governing decisions and approvals, and the planned assessments required for Reuse activation.
- Reuse assessments retain stable identities from planned creation through completed CAS update.
- Knowledge includes evidence, passed validation, applicability, limitations, guidance, origin, and completed-assessment provenance.
- Acceptance-criterion mappings remain valid and durable at terminal closure.

# First Persistence Transaction

Construct a complete persistence plan containing all changed artifacts produced through Validate, every planned reuse assessment required for activation, and the execution/state values that will represent Persist completion and Reuse activation when committed.

The plan must include all applicable evidence, decisions, findings, approvals, planned reuse assessments, execution, changed goal or mission, and state. It must not include completed assessments or promoted knowledge because Reuse has not executed yet.

Every planned assessment must be a create target at its canonical `reuse/` path, precede the execution/state targets that reference it, use a stable `REUSE-NNN` identity, and contain no final disposition, rationale, assessment timestamp, or assessor.

Verify canonical paths, complete targets, exact SHA-256 digests, create-only/CAS semantics, dependency and type order, state last, per-write re-read, whole-set verification, and rollback or compensation.

The proposed execution/state targets may contain Persist-completed and Reuse-active values while the plan is `applying`, but those values are transaction-pending and non-authoritative. They become authoritative together only after the exact plan is terminal `applied`, final verification passed, and plan finalization is re-read. Test `PERSIST-COMMIT-001` explicitly.

# Reuse Persistence Transaction

Construct a separate complete plan containing:

- CAS updates of every planned reuse assessment to `completed` using the retained planned-record SHA.
- Validated, superseding, and deprecation-tombstone knowledge that references completed assessments.
- New Reuse decisions and approvals.
- Completed goal and mission updates.
- Terminal execution update.
- Terminal state update as final pointer.

Verify that fixed assessment identity and scope fields are unchanged, completed fields are supplied, assessments precede knowledge, execution precedes state, state is last, and complete target derivation, CAS, per-write and whole-set verification, and recovery all pass.

The governed target content may contain Reuse completion, terminal execution, completed goal and mission, and cleared state while the plan is `applying`, but those values remain transaction-pending. They become authoritative together only when the plan is terminal `applied` and re-read successfully. A finalization failure must block use of the pending values and require reconciliation.

# Terminal Form

Validate:

```text
Execute  = completed
Observe  = completed
Evaluate = completed
Classify = completed
Adapt    = completed
Validate = completed
Persist  = completed
Reuse    = completed
Execution status = succeeded
Execution completed_at = set
Execution outcome = set
Execution completion.disposition = goal-completed
Synthetic goal status = completed
Synthetic mission status = completed
Synthetic state status = ready
Synthetic state active_mission = null
Synthetic state active_goal = null
Synthetic state active_execution = null
Synthetic state lifecycle_stage = null
```

Do not leave a terminal lifecycle under an in-progress execution. Do not report or use transaction-pending completion values before the applicable plan commit marker is verified.

# Required Validation Results

Report separately:

1. Immutable revision and focused resolution.
2. Durable context and synthetic authorization.
3. Mission and goal schema validation.
4. Stable execution identity and creation.
5. Execute-to-Observe continuity.
6. Observe-to-Evaluate continuity.
7. Evaluate-to-Classify continuity.
8. Classify-to-Adapt continuity.
9. Adapt-to-Validate continuity.
10. Validate-to-Persist continuity.
11. Planned reuse-assessment creation and schema validation.
12. First plan schema, target completeness, and ordering.
13. First transaction commit-marker behavior.
14. Persist-to-Reuse continuity.
15. Cross-stage references and provenance.
16. Evidence and acceptance-criterion mappings.
17. Decision, approval, finding, and failed-validation authorization.
18. Adaptation/validation/persistence synchronization.
19. Planned-to-completed assessment CAS lifecycle.
20. Knowledge qualification and immutable history.
21. Reuse plan schema, target completeness, and ordering.
22. Reuse transaction commit-marker behavior.
23. Reuse-to-terminal continuity.
24. Terminal execution, goal, mission, and state validation.
25. Compare-and-swap and partial recovery.
26. Timestamp ordering.
27. Repository immutability.

For each include expected condition, actual condition, result, and enforcing source.

# Negative Validation

Construct invalid fixtures and demonstrate deterministic rejection of:

1. Execution identity changes between stages.
2. Mission or goal identity changes mid-execution.
3. Two stages are active.
4. A stage starts before its predecessor completes.
5. A successor is non-pending while an earlier stage is active.
6. State disagrees with execution or stage.
7. Observation contains an unsupported classification or recommendation.
8. Evaluation references missing observation or evidence.
9. Classification references stale or unresolved provenance.
10. Adaptation lacks required provenance.
11. Adaptation becomes approved without required decision or approval.
12. Rejected or deferred adaptation is validation-eligible.
13. Validation passes without evidence.
14. Failed validation is silently changed to passed.
15. Failed validation lacks finding, recovery, or governing disposition.
16. A blocking disposition permits persistence.
17. The first plan omits an earlier changed record, approval, or required planned assessment.
18. Reuse activates with an assessment that exists only in memory.
19. A planned assessment contains a final disposition or assessment timestamp.
20. A plan targets or digests itself.
21. A plan writes state before referenced targets.
22. Durability is claimed without final whole-set and plan-finalization re-read.
23. Transaction-pending completion values are reported or reused before `applied`.
24. Plan finalization fails but pending completion values remain usable.
25. A completed assessment changes identity, subject, execution, mission, goal, or adaptation scope.
26. A planned assessment is completed without retained-SHA CAS.
27. A completed assessment is updated again or returned to planned.
28. Reuse promotes nondurable, provisional, rejected, or failed learning.
29. Duplicate knowledge creates a new identity without resolution.
30. Conflict is promoted without scope distinction, supersession, or deprecation.
31. Existing knowledge is overwritten.
32. Knowledge references a planned rather than completed assessment.
33. Knowledge lacks required evidence, validation, applicability, limitations, guidance, origin, or assessment provenance.
34. Reuse plan omits a changed assessment, knowledge, decision, approval, goal, mission, execution, or state target.
35. Knowledge is ordered before its completed assessment.
36. Reuse completes before its plan commit marker is verified.
37. Acceptance criterion is satisfied by chat text rather than durable evidence.
38. Acceptance evidence references an artifact omitted from persistence.
39. A formerly valid reference is stale at terminal closure.
40. Adaptation validation, persistence, or reuse status is unsynchronized.
41. Terminal execution retains a pending or active stage.
42. Execution remains in-progress after all stages are terminal.
43. Terminal execution lacks outcome, completion time, disposition, or rationale.
44. Goal completes without evidence for any AC-910 through AC-915.
45. Mission completes while its goal is not completed.
46. State is cleared before terminal artifacts are committed.
47. Terminal state retains an active pointer.
48. Timestamps regress.
49. A stale CAS revision is used.
50. Partial execution/state transition lacks recovery.
51. Partial multi-artifact persistence lacks recovery or reconciliation.
52. An unplanned artifact changes.
53. Repository artifacts are actually written.

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
7. Cross-Stage Provenance Findings
8. Representative Execution Record Set
9. First Persistence Plan and Planned Assessments
10. Reuse Assessment and Knowledge Set
11. Reuse Persistence Plan
12. Acceptance-Criterion Evidence Mapping
13. Terminal Execution, Goal, Mission, and State
14. Validation Results
15. Negative Validation Results
16. Commit-Marker, Compare-and-Swap, and Recovery Results
17. Framework Defects
18. Repository Mutation Confirmation
19. Next Authorized Action

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
