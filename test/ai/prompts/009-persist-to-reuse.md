# AI Flywheel Lifecycle Verification
## Persist → Reuse Transition (Non-Persistent)

> **Purpose**
>
> Verify that the AI Flywheel operating model can deterministically complete **Persist**, begin **Reuse**, assess validated knowledge, and close Reuse without modifying the repository.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Branch:** `feature/self-contained-operating-model`

# Cold Verification Rules

Ignore prior conversations, memory, cached repository knowledge, and prior Prompt 009 results.

Resolve and report the immutable commit SHA for the branch. Use only files read from that immutable revision.

This prompt verifies one lifecycle boundary. It does not repeat the complete cold-start test covered by Prompt 001 or prior lifecycle boundaries covered by Prompts 002 through 008.

# Verification Authorization

This prompt explicitly authorizes a synthetic, read-only operating-model verification. You may read framework files, reconstruct hypothetical artifacts in memory, validate them, and construct invalid fixtures.

This is not durable goal-directed work. Resolve current state, mission, and goal as context, but do not reject the synthetic verification because their objective differs.

You must not create, modify, or delete repository files; activate an execution; update state; persist records or knowledge; inspect an application repository; or stage, commit, push, or advance the durable lifecycle.

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
15. `.flywheel/operating-model/guidance/reuse.md` when present
16. `.flywheel/operating-model/config/governance.yaml`
17. `.flywheel/operating-model/config/validation.yaml`
18. `.flywheel/operating-model/schemas/README.md`
19. `.flywheel/operating-model/schemas/state.schema.yaml`
20. `.flywheel/operating-model/schemas/execution.schema.yaml`
21. `.flywheel/operating-model/schemas/record.schema.yaml`
22. `.flywheel/operating-model/schemas/knowledge.schema.yaml`
23. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
24. The active mission and active goal identified by state.

Report the immutable SHA and whether all applicable items were read successfully. Do not stop because multiple reads are required.

# Verification Starting Point

Assume conceptually that Prompts 001 through 008 passed. Do not copy prior result artifacts.

Reconstruct a complete in-memory execution with Execute through Validate completed, Persist initially in progress with an applied and verified persistence plan, Reuse pending, and state identifying Persist as active.

The fixture must include validated learning eligible for knowledge assessment, at least one item not eligible for promotion, and existing validated knowledge against which applicability, duplication, conflict, and supersession can be tested.

If deterministic reconstruction is impossible after required repository resolution, report a reusable framework defect.

# Persist Completion Verification

Determine and exercise rules for:

- Terminal applied persistence-plan status.
- Successful final whole-set verification.
- Required Persist references, summary, and timestamps.
- Resolution of all durable references and failed-validation authorizations.
- Absence of persistence blockers.
- Execution/state agreement.
- Prevention of Reuse claims before Persist completes.

Determine whether Persist may legally complete.

# Reuse Activation and Assessment Verification

Determine and exercise rules for:

- Reuse activation prerequisites.
- What must be assessed for reuse.
- Difference between execution records, candidate learning, validated knowledge, and reused knowledge.
- Eligibility for knowledge promotion.
- Required evidence, validation provenance, applicability, limitations, reuse guidance, and origin references.
- Duplicate and conflict detection against existing knowledge.
- New knowledge creation versus superseding prior knowledge.
- Rejection, deferral, deprecation, and not-applicable outcomes.
- Human approval requirements for material knowledge or risk-bearing guidance.
- Recording whether existing knowledge was reused, rejected as inapplicable, or exposed a revision need.
- Synchronization of adaptation `reuse_status` with reuse outcomes.
- Reuse stage references, summary, timestamps, and completion.
- Execution and goal completion boundaries.

Construct concrete structured reuse assessments and proposed knowledge artifacts when supported.

# Proposed Transition

Construct and validate:

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

Then construct the Reuse-completed form with every stage completed or properly not applicable. Keep the execution active unless repository rules deterministically authorize terminal execution completion within this verification.

Construct complete proposed execution and state artifacts with concrete values. Validate schemas, lifecycle order, timestamps, identities, canonical paths, references, state agreement, immutable history, and compare-and-swap requirements.

# Required Validation Results

Report separately:

1. Immutable revision resolution.
2. Required repository-item resolution.
3. Active state, mission, and goal resolution.
4. Synthetic-verification authorization.
5. Starting persisted-state reconstruction.
6. Persistence-plan terminal validation.
7. Persist completion.
8. Execution schema validation.
9. State schema validation.
10. Reuse activation.
11. Reuse-assessment schema validation.
12. Knowledge-promotion eligibility.
13. Evidence and validation provenance.
14. Applicability and limitations.
15. Duplicate and conflict handling.
16. Supersession and immutable history.
17. Existing-knowledge reuse disposition.
18. Adaptation reuse-status synchronization.
19. Reuse completion.
20. Lifecycle ordering and timestamps.
21. Cross-artifact references and canonical locations.
22. Compare-and-swap and partial-transition recovery.
23. Execution-completion boundary.
24. Repository immutability.

For each include expected condition, actual condition, result, and enforcing repository source.

# Negative Validation

Construct invalid in-memory fixtures and demonstrate deterministic rejection of at least:

1. Reuse starts while Persist remains in progress.
2. Persist and Reuse are both in progress.
3. Reuse starts before the persistence plan is applied and verified.
4. Persist completes with an unresolved blocker.
5. Reuse promotes an observation directly to knowledge.
6. Knowledge lacks evidence provenance.
7. Knowledge lacks validation provenance.
8. Candidate learning is marked validated without qualification.
9. Knowledge lacks applicability.
10. Knowledge lacks limitations assessment.
11. Knowledge lacks actionable reuse guidance.
12. Knowledge silently overwrites an existing item.
13. Supersession omits the prior knowledge reference.
14. Conflicting knowledge is promoted without disposition.
15. Duplicate knowledge is created without resolution.
16. Rejected or failed learning is promoted as validated.
17. Material risk-bearing guidance is promoted without required approval.
18. Existing validated knowledge is reused outside its applicability.
19. Existing knowledge is ignored without recording a disposition.
20. Adaptation `reuse_status` disagrees with reuse assessment.
21. Reuse completes with unresolved required assessments.
22. Reuse stage lacks references, summary, or timestamps.
23. Reuse claims persistence that was not durably verified.
24. Execution closes while a lifecycle stage remains pending or active.
25. Goal completion is claimed without acceptance-criterion evidence.
26. State and execution disagree on the active stage.
27. Stage timestamps are out of order.
28. A stale compare-and-swap revision is used.
29. Partial execution/state transition lacks recovery.
30. Repository artifacts are actually written during verification.

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
8. Persist Completion Decision
9. Reuse Activation Decision
10. Reuse Completion Decision
11. Proposed Execution Artifact
12. Proposed State Artifact
13. Validation Results
14. Negative Validation Results
15. Compare-and-Swap and Recovery Results
16. Execution and Goal Completion Boundary
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

> Run the next non-persistent lifecycle verification.

When a reusable framework defect blocks verification, end with:

> Correct only the reusable framework defect before repeating this verification.
