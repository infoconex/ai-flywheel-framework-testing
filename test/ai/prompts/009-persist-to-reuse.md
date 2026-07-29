# AI Flywheel Lifecycle Verification
## Persist → Reuse Transition (Non-Persistent)

> **Purpose**
>
> Verify that the AI Flywheel operating model can deterministically complete **Persist**, begin and complete **Reuse**, durably qualify reusable knowledge, and preserve immutable history without modifying the repository.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Branch:** `feature/self-contained-operating-model`

# Cold Verification Rules

Ignore prior conversations, memory, cached repository knowledge, and prior Prompt 009 results.

Resolve and report the immutable commit SHA for the branch. Use only files read from that immutable revision.

This prompt verifies one lifecycle boundary. It does not repeat Prompt 001 or prior lifecycle tests.

# Verification Authorization

This prompt explicitly authorizes synthetic, read-only operating-model verification. You may read framework files, reconstruct hypothetical artifacts in memory, validate them, and construct invalid fixtures.

This is not durable goal-directed work. Resolve current state, mission, and goal as context, but do not reject the test because their objective differs.

You must not create, modify, or delete repository files; activate an execution; update state; persist records, assessments, plans, or knowledge; inspect an application repository; or stage, commit, push, or advance the durable lifecycle.

Every displayed artifact must be labeled:

> **PROPOSED ONLY — NOT WRITTEN**

# Required Repository Resolution

Before reconstruction, read from the immutable revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/authority.md`
4. `.flywheel/operating-model/guidance/invariants.md`
5. `.flywheel/operating-model/guidance/principles.md`
6. `.flywheel/operating-model/guidance/lifecycle.md`
7. `.flywheel/operating-model/guidance/execution-model.md`
8. `.flywheel/operating-model/guidance/records.md`
9. `.flywheel/operating-model/guidance/evidence.md`
10. `.flywheel/operating-model/guidance/decisions.md`
11. `.flywheel/operating-model/guidance/failure-handling.md`
12. `.flywheel/operating-model/guidance/classifications.md`
13. `.flywheel/operating-model/guidance/validation.md`
14. `.flywheel/operating-model/guidance/persistence.md`
15. `.flywheel/operating-model/guidance/reuse.md`
16. `.flywheel/operating-model/config/governance.yaml`
17. `.flywheel/operating-model/config/validation.yaml`
18. `.flywheel/operating-model/schemas/README.md`
19. `.flywheel/operating-model/schemas/state.schema.yaml`
20. `.flywheel/operating-model/schemas/execution.schema.yaml`
21. `.flywheel/operating-model/schemas/record.schema.yaml`
22. `.flywheel/operating-model/schemas/knowledge.schema.yaml`
23. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
24. `.flywheel/operating-model/schemas/reuse-assessment.schema.yaml`
25. The active mission and active goal identified by state.

Report the immutable SHA and whether all 25 items were read successfully. A missing item fails verification. Do not stop because multiple reads are required.

# Verification Starting Point

Assume conceptually that Prompts 001 through 008 passed. Do not copy prior result artifacts.

Reconstruct a complete in-memory execution with Execute through Validate completed, Persist initially in progress with an applied and verified persistence plan ready for completion, Reuse pending, and state identifying Persist as active.

Include:

- Confirmed validated learning eligible for assessment.
- At least one candidate that must not be promoted.
- Existing validated knowledge that is applicable.
- Existing validated knowledge that is inapplicable.
- A semantic duplicate.
- A material conflict requiring disposition.
- A replacement eligible to supersede prior knowledge.
- A deprecation case requiring a new immutable tombstone artifact rather than mutation of prior knowledge.

If deterministic reconstruction is impossible after required resolution, report a reusable framework defect.

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

- Completed reuse assessments at canonical goal record paths.
- New validated, superseding, or deprecation-tombstone knowledge artifacts at canonical knowledge paths.
- Required decisions and approvals.
- Execution update with final assessment references, synchronized reuse statuses, and Reuse completion.
- State update as final operational pointer.

Validate:

- The plan does not target or digest itself.
- `reuse-assessment` appears after approvals and before knowledge in canonical type order.
- Assessments and knowledge are create-only.
- Execution and state use retained-SHA compare-and-swap.
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
```

Then construct the Reuse-completed form with every stage completed or properly not applicable and the Reuse persistence plan applied and verified.

Construct complete proposed execution and state artifacts with concrete values. Keep execution active unless repository rules deterministically authorize terminal completion. Separately evaluate the execution and goal completion boundary without inventing acceptance-criterion evidence.

# Required Validation Results

Report separately:

1. Immutable revision resolution.
2. Required repository-item resolution.
3. Active state, mission, and goal resolution.
4. Synthetic-verification authorization.
5. Starting persisted-state reconstruction.
6. Persist-plan terminal validation.
7. Persist completion.
8. Execution schema validation.
9. State schema validation.
10. Reuse activation.
11. Reuse-assessment schema validation.
12. Knowledge schema validation.
13. Promotion eligibility.
14. Evidence and validation provenance.
15. Applicability, limitations, and reuse guidance.
16. Duplicate and conflict handling.
17. Supersession and immutable history.
18. Immutable deprecation tombstone handling.
19. Existing-knowledge disposition.
20. Approval and decision handling.
21. Adaptation reuse-status synchronization.
22. Reuse persistence-plan validation.
23. Reuse output durability.
24. Reuse completion.
25. Lifecycle ordering and timestamps.
26. Cross-artifact references and canonical locations.
27. Compare-and-swap and partial recovery.
28. Execution and goal completion boundary.
29. Repository immutability.

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
32. Goal completion is claimed without acceptance-criterion evidence.
33. State and execution disagree.
34. Stage timestamps are out of order.
35. A stale compare-and-swap revision is used.
36. Partial transition or persistence lacks recovery.
37. Repository artifacts are actually written during verification.

For each report invalid condition, expected rejection, actual result, and enforcing rule. A case that cannot be rejected deterministically is a reusable framework defect.

# Framework Defects

Report only reusable framework defects. For each include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during the non-persistent Persist-to-Reuse lifecycle verification.

# Required Output

Use these sections in this exact order:

1. Verification Summary
2. Validation Trace
3. Starting Persisted State
4. Persist Completion Findings
5. Reuse Semantic Findings
6. Representative Reuse Assessment Set
7. Proposed Knowledge Artifacts
8. Reuse Persistence Plan
9. Persist Completion Decision
10. Reuse Activation Decision
11. Reuse Completion Decision
12. Proposed Execution Artifact
13. Proposed State Artifact
14. Validation Results
15. Negative Validation Results
16. Compare-and-Swap and Recovery Results
17. Execution and Goal Completion Boundary
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

> Run the next non-persistent lifecycle verification.

When a reusable framework defect blocks verification, end with:

> Correct only the reusable framework defect before repeating this verification.
