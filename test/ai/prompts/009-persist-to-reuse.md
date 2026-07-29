# AI Flywheel Lifecycle Verification
## Persist → Reuse Transition (Non-Persistent)

> **Purpose**
>
> Verify that the AI Flywheel operating model can deterministically complete **Persist**, begin and complete **Reuse**, durably qualify reusable knowledge, preserve immutable history, and terminally close a synthetic verification execution without modifying the repository.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `d7cf8e6928d818d7f51485fb79c7a6a4c931a2d7`

Use this exact immutable revision. Do not resolve or substitute a later branch head.

# Cold Verification Rules

Ignore prior conversations, memory, cached repository knowledge, and prior Prompt 009 results.

This prompt verifies one lifecycle boundary. It does not repeat Prompt 001 or prior lifecycle tests.

# Verification Authorization

This prompt explicitly authorizes synthetic, read-only operating-model verification. You may read framework files, reconstruct hypothetical artifacts in memory, validate them, and construct invalid fixtures.

This is not durable goal-directed work. Resolve current durable state, mission, and goal as context only. Do not reject the test because their objective differs.

You must not create, modify, or delete repository files; activate an execution; update durable state; persist records, assessments, plans, or knowledge; inspect an application repository; or stage, commit, push, or advance the durable lifecycle.

Every displayed artifact must be labeled:

> **PROPOSED ONLY — NOT WRITTEN**

# Focused Repository Resolution

Read these 17 items from the exact immutable revision before reconstruction:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/lifecycle.md`
4. `.flywheel/operating-model/guidance/execution-model.md`
5. `.flywheel/operating-model/guidance/records.md`
6. `.flywheel/operating-model/guidance/classifications.md`
7. `.flywheel/operating-model/guidance/persistence.md`
8. `.flywheel/operating-model/guidance/reuse.md`
9. `.flywheel/operating-model/config/validation.yaml`
10. `.flywheel/operating-model/schemas/README.md`
11. `.flywheel/operating-model/schemas/state.schema.yaml`
12. `.flywheel/operating-model/schemas/goal.schema.yaml`
13. `.flywheel/operating-model/schemas/execution.schema.yaml`
14. `.flywheel/operating-model/schemas/record.schema.yaml`
15. `.flywheel/operating-model/schemas/knowledge.schema.yaml`
16. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
17. `.flywheel/operating-model/schemas/reuse-assessment.schema.yaml`

Also read the active mission and active goal identified by durable state for context. These two contextual reads do not change the 17-item focused-resolution count.

Report the immutable SHA, `17/17` focused resolution, and active-context resolution. A missing required item fails verification. Do not stop because multiple reads are required.

# Synthetic Verification Goal

Do not force the fixture into the repository's actual onboarding goal.

Construct an in-memory synthetic goal under the resolved active mission:

```yaml
id: verify-persist-to-reuse
mission_id: establish-ai-flywheel-operations
status: active
objective: Verify the Persist-to-Reuse lifecycle boundary without repository mutation.
acceptance_criteria:
  - id: AC-901
    statement: Persist completion is deterministic and evidence-backed.
  - id: AC-902
    statement: Reuse assessments and knowledge dispositions are deterministic.
  - id: AC-903
    statement: Reuse outputs have canonical durable transaction semantics.
  - id: AC-904
    statement: Invalid Persist-to-Reuse fixtures are deterministically rejected.
  - id: AC-905
    statement: Repository immutability is preserved.
```

Use exactly these five acceptance-criterion IDs, in this order, in the synthetic execution. Construct sufficient in-memory evidence mappings for all five so terminal execution completion can be evaluated honestly.

The actual durable mission, goal, and state remain unchanged and are reported separately as context.

# Verification Starting Point

Assume conceptually that Prompts 001 through 008 passed. Do not copy prior result artifacts.

Reconstruct a complete synthetic execution with Execute through Validate completed, Persist initially in progress with an applied and verified persistence plan ready for completion, Reuse pending, and a synthetic state identifying Persist as active.

Include:

- Confirmed validated learning eligible for assessment.
- At least one candidate that must not be promoted.
- Existing validated knowledge that is applicable.
- Existing validated knowledge that is inapplicable.
- A semantic duplicate.
- A material conflict requiring disposition.
- A replacement eligible to supersede prior knowledge.
- A deprecation case requiring a new immutable tombstone artifact rather than mutation of prior knowledge.

If deterministic reconstruction is impossible after focused resolution, report a reusable framework defect.

# Persist Completion Verification

Determine and exercise:

- Terminal applied persistence-plan status.
- Passed final whole-set verification.
- Required Persist references, summary, and timestamps.
- Durable reference and authorization resolution.
- Absence of persistence blockers.
- Execution/state agreement.
- Prevention of premature Reuse claims.

Determine whether Persist may legally complete.

# Reuse Activation and Assessment Verification

Determine and exercise:

- Reuse activation prerequisites.
- Planned versus completed reuse assessments.
- Candidate-learning and existing-knowledge subject types.
- Promotion, supersession, deferral, rejection, not-reusable, reused, inapplicable, revision-required, deprecated, and not-considered dispositions.
- Evidence and passed-validation provenance.
- Applicability, limitations, and actionable reuse guidance.
- Origin mission, goal, execution, classification, and assessment provenance.
- Duplicate and conflict detection.
- New knowledge creation versus superseding prior identities.
- Immutable deprecation through a new tombstone artifact that supersedes prior knowledge.
- Approval and decision requirements for material or risk-bearing guidance.
- Existing-knowledge usage dispositions.
- Adaptation `reuse_status` synchronization.
- Reuse stage references, summary, timestamps, and completion.

Construct concrete schema-valid reuse assessments and knowledge artifacts.

# Reuse Output Durability

Construct a dedicated Reuse persistence plan that includes every new or changed Reuse output:

- Completed reuse assessments at canonical goal record paths under the synthetic goal.
- New validated, superseding, or deprecation-tombstone knowledge artifacts at canonical knowledge paths.
- Required decisions and approvals.
- Synthetic execution update with final assessment references, synchronized reuse statuses, Reuse completion, terminal status, outcome, and completion disposition.
- Synthetic state update as final operational pointer, clearing `active_execution` and `lifecycle_stage` after terminal execution.

Validate:

- The plan does not target or digest itself.
- `reuse-assessment` appears after approvals and before knowledge in canonical type order.
- Assessments and knowledge are create-only.
- Execution and state use retained-SHA compare-and-swap when modeled as existing synthetic artifacts.
- State is last.
- Per-write and whole-set verification are required.
- Partial failure has deterministic rollback or compensation.
- Reuse cannot complete until this dedicated plan is terminal `applied` and re-read successfully.

# Proposed Transitions

Construct and validate the activation form:

```text
Execute  = completed
Observe  = completed
Evaluate = completed
Classify = completed
Adapt    = completed
Validate = completed
Persist  = completed
Reuse    = in-progress
Execution status = in-progress
Synthetic state lifecycle_stage = reuse
```

Then construct the terminal form:

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
Synthetic state active_execution = null
Synthetic state lifecycle_stage = null
```

Do not leave an `in-progress` execution with all lifecycle stages terminal. Do not claim terminal completion unless all five synthetic acceptance criteria have sufficient evidence mappings and all blockers and required approvals are resolved.

Construct complete proposed synthetic goal, execution, and before/after state artifacts with concrete values. Validate schemas, lifecycle order, timestamps, identities, canonical paths, references, evidence mappings, state agreement, immutable history, and compare-and-swap requirements.

# Required Validation Results

Report separately:

1. Immutable revision resolution.
2. Focused repository-item resolution.
3. Durable state, mission, and goal context resolution.
4. Synthetic-verification authorization.
5. Synthetic goal schema validation.
6. Starting persisted-state reconstruction.
7. Persist-plan terminal validation.
8. Persist completion.
9. Execution schema validation.
10. State schema validation.
11. Reuse activation.
12. Reuse-assessment schema validation.
13. Knowledge schema validation.
14. Promotion eligibility.
15. Evidence and validation provenance.
16. Applicability, limitations, and reuse guidance.
17. Duplicate and conflict handling.
18. Supersession and immutable history.
19. Immutable deprecation tombstone handling.
20. Existing-knowledge disposition.
21. Approval and decision handling.
22. Adaptation reuse-status synchronization.
23. Reuse persistence-plan validation.
24. Reuse output durability.
25. Reuse completion.
26. Terminal execution completion.
27. Lifecycle ordering and timestamps.
28. Cross-artifact references and canonical locations.
29. Compare-and-swap and partial recovery.
30. Acceptance-criterion evidence mapping.
31. Repository immutability.

For each include expected condition, actual condition, result, and enforcing repository source.

# Negative Validation

Construct invalid in-memory fixtures and demonstrate deterministic rejection of at least:

1. Reuse starts while Persist remains in progress.
2. Persist and Reuse are both in progress.
3. Reuse starts before the Persist plan is applied and verified.
4. Persist completes with an unresolved blocker.
5. Reuse promotes an observation directly.
6. Knowledge lacks evidence provenance.
7. Knowledge lacks passed-validation provenance.
8. Candidate learning is validated without qualification.
9. Knowledge lacks applicability.
10. Knowledge lacks a limitations assessment.
11. Knowledge lacks actionable reuse guidance.
12. Knowledge lacks origin or assessment provenance.
13. Existing knowledge is silently overwritten.
14. Supersession omits the prior knowledge reference.
15. Existing knowledge status is mutated to deprecated.
16. A deprecation tombstone omits the prior knowledge reference or decision.
17. Conflicting knowledge is promoted without disposition.
18. Duplicate knowledge is created without resolution.
19. Rejected, provisional, or failed learning is promoted.
20. Material risk-bearing guidance lacks approval.
21. Existing knowledge is reused outside applicability or against limitations.
22. Existing knowledge is ignored without disposition.
23. Adaptation `reuse_status` disagrees with assessments.
24. Reuse completes with unresolved assessments.
25. Reuse stage lacks references, summary, or timestamps.
26. Reuse outputs exist only in memory with no applied Reuse persistence plan.
27. Reuse persistence omits an assessment, knowledge, decision, approval, execution, or state target.
28. Reuse plan orders knowledge before its assessment.
29. Reuse plan targets or digests itself.
30. Reuse claims durability without final re-read.
31. Execution closes while a lifecycle stage remains pending or active.
32. An execution remains `in-progress` after all lifecycle stages become terminal.
33. Terminal execution lacks outcome, completion timestamp, or completion disposition.
34. Goal completion is claimed without evidence for all AC-901 through AC-905.
35. Synthetic state retains an active execution after terminal completion.
36. State and execution disagree.
37. Stage timestamps are out of order.
38. A stale compare-and-swap revision is used.
39. Partial transition or persistence lacks recovery.
40. Repository artifacts are actually written during verification.

For each report invalid condition, expected rejection, actual result, and enforcing rule. A case that cannot be rejected deterministically is a reusable framework defect.

# Framework Defects

Report only reusable framework defects. For each include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during the non-persistent Persist-to-Reuse lifecycle verification.

# Required Output

Use these sections in this exact order:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Synthetic Verification Goal
5. Starting Persisted State
6. Persist Completion Findings
7. Reuse Semantic Findings
8. Representative Reuse Assessment Set
9. Proposed Knowledge Artifacts
10. Reuse Persistence Plan
11. Persist Completion Decision
12. Reuse Activation Decision
13. Reuse Completion Decision
14. Terminal Execution Completion Decision
15. Proposed Execution Artifact
16. Proposed State Artifacts
17. Validation Results
18. Negative Validation Results
19. Compare-and-Swap and Recovery Results
20. Acceptance-Criterion Evidence Mapping
21. Framework Defects
22. Repository Mutation Confirmation
23. Next Authorized Action

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

> Run the next non-persistent lifecycle verification.

When a reusable framework defect blocks verification, end with:

> Correct only the reusable framework defect before repeating this verification.
