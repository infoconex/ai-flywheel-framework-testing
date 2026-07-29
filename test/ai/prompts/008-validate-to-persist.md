# AI Flywheel Lifecycle Verification
## Validate → Persist Transition (Non-Persistent)

> **Purpose**
>
> Verify that the AI Flywheel operating model can deterministically complete **Validate** and begin **Persist** without modifying the repository.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Branch:** `feature/self-contained-operating-model`

# Cold Verification Rules

Ignore prior conversations, memory, cached repository knowledge, and prior Prompt 008 results.

Resolve and report the immutable commit SHA for the branch. Use only files read from that immutable revision.

This prompt verifies one lifecycle boundary. It does **not** repeat the complete cold-start conformance test already covered by Prompt 001.

# Verification Authorization

This prompt explicitly authorizes a synthetic, read-only operating-model verification.

You may:

- Read framework repository files.
- Reconstruct hypothetical execution, state, record, validation, and persistence artifacts in memory.
- Validate proposed artifacts against schemas and semantic rules.
- Construct invalid in-memory fixtures.

This work is not a durable execution and is not governed by the current active goal’s application-work scope. Resolve and report current state, mission, and goal as context, but do not reject this synthetic verification because their objective differs.

You must not:

- Create, modify, or delete repository files.
- Activate an execution or update state.
- Persist any record or plan.
- Inspect an application repository.
- Stage, commit, push, or advance the durable lifecycle.

Every displayed artifact must be labeled:

> **PROPOSED ONLY — NOT WRITTEN**

# Required Repository Resolution

Before reconstructing the transition, read these files from the immutable revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/authority.md`
4. `.flywheel/operating-model/guidance/invariants.md`
5. `.flywheel/operating-model/guidance/lifecycle.md`
6. `.flywheel/operating-model/guidance/execution-model.md`
7. `.flywheel/operating-model/guidance/records.md`
8. `.flywheel/operating-model/guidance/evidence.md`
9. `.flywheel/operating-model/guidance/decisions.md`
10. `.flywheel/operating-model/guidance/failure-handling.md`
11. `.flywheel/operating-model/guidance/adaptation.md`
12. `.flywheel/operating-model/guidance/validation.md`
13. `.flywheel/operating-model/guidance/persistence.md`
14. `.flywheel/operating-model/guidance/classifications.md`
15. `.flywheel/operating-model/config/governance.yaml`
16. `.flywheel/operating-model/config/validation.yaml`
17. `.flywheel/operating-model/schemas/README.md`
18. `.flywheel/operating-model/schemas/state.schema.yaml`
19. `.flywheel/operating-model/schemas/execution.schema.yaml`
20. `.flywheel/operating-model/schemas/record.schema.yaml`
21. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
22. The active mission and active goal identified by state.

Report the immutable SHA and whether all 22 resolution items were read successfully. A missing or unreadable required item is a failed verification. Do not stop because multiple reads are required.

# Verification Starting Point

Assume conceptually that Prompts 001 through 007 passed. Do not copy prior result artifacts.

Using current repository rules, reconstruct a complete in-memory execution with:

- Execute, Observe, Evaluate, Classify, and Adapt completed.
- Validate in progress initially.
- Persist and Reuse pending initially.
- State identifying Validate as the active stage.
- Complete structured observations, evaluations, classifications, adaptations, and validations.
- At least one approved and implemented adaptation.
- At least one validation-ineligible adaptation with explicit exclusion.
- At least one evidence-backed passed validation.
- At least one evidence-backed failed validation with finding, recovery action, linked disposition decision, and required approvals when the framework supports persistence after failure.

If deterministic reconstruction is impossible after all required repository items are read, report a reusable framework defect. Do not substitute active-goal scope or missing durable test artifacts for that determination.

# Validate Completion Verification

Determine and exercise repository rules for:

- Required validation-plan fields.
- Planned versus executed validation.
- Eligibility and explicit exclusion.
- Evidence requirements for pass and failure.
- Finding and recovery requirements.
- Failed-validation disposition, decision, approval, scope, supersession, and persistence permission.
- Pending-validation restrictions.
- Adaptation-status synchronization.
- Stage references, summaries, and timestamps.
- Revised-validation history.
- Whether command success alone proves an outcome.

Construct passed, not-applicable, and failed validation examples with complete traceability. Determine whether Validate may legally complete.

# Persistence Verification

Determine and exercise repository rules for:

- Persist activation prerequisites.
- Persistence-plan structure and lifecycle.
- Complete target derivation.
- Canonical paths.
- Create-only, supersede-only, and compare-and-swap mutation semantics.
- SHA-256 digest calculation.
- Dependency and type ordering.
- State as the final operational pointer.
- Per-write and whole-set verification.
- Rollback and compensation.
- Failed-validation authorization precheck.
- Immutable-history protection.
- Reuse boundary protection.

Construct a schema-valid in-memory persistence plan containing every required target, operation, mutability rule, precondition, digest, dependency, rollback action, and write-order entry. The plan must not target or digest itself.

# Proposed Transition

Construct and validate:

```text
Execute  = completed
Observe  = completed
Evaluate = completed
Classify = completed
Adapt    = completed
Validate = completed
Persist  = in-progress
Reuse    = pending
```

Construct complete proposed execution and state artifacts with concrete values. Validate schema shape, lifecycle order, timestamps, identities, canonical references, state agreement, and persistence-plan reference.

# Required Validation Results

Report separately:

1. Immutable revision resolution.
2. Required repository-item resolution.
3. Active state, mission, and goal resolution.
4. Synthetic-verification authorization.
5. Starting execution reconstruction.
6. Execution schema validation.
7. State schema validation.
8. Validation semantics and provenance.
9. Eligibility and evidence sufficiency.
10. Failure handling and disposition authorization.
11. Adaptation-status synchronization.
12. Validate completion.
13. Persistence-plan schema validation.
14. Persistence semantics and canonical locations.
15. Immutable history.
16. Persist activation.
17. Lifecycle ordering and transition.
18. Cross-artifact references.
19. Timestamps and identities.
20. Compare-and-swap.
21. Partial-persistence recovery.
22. Post-transition verification.
23. Repository immutability.

For each include expected condition, actual condition, result, and enforcing repository source.

# Negative Validation

Construct invalid in-memory fixtures and demonstrate deterministic rejection of:

1. Persist starts while Validate remains active.
2. Validate and Persist are both active.
3. Persist starts before Validate completion.
4. Required validation remains pending.
5. Passed or failed validation lacks evidence.
6. Failure lacks a finding or recovery action.
7. Failure lacks a valid linked disposition.
8. A blocking disposition permits persistence.
9. Required approval is missing or scope-mismatched.
10. Not-applicable lacks an exclusion reason.
11. Ineligible adaptation passes.
12. Adaptation status disagrees with validation.
13. A reference does not resolve.
14. Command success alone is treated as proof.
15. Failed validation is silently changed to passed.
16. Revised validation weakens scope or lacks supersession.
17. Persistence plan omits a required target.
18. Persistence plan targets or digests itself.
19. Target path is noncanonical.
20. Immutable history is overwritten.
21. Required decision, approval, finding, evidence, or execution target is omitted.
22. Persist claims Reuse early.
23. Lifecycle stage is skipped.
24. State and execution disagree.
25. Timestamps are out of order.
26. A stale compare-and-swap revision is used.
27. Partial persistence lacks recovery.
28. Final artifacts are not re-read and verified.
29. Repository artifacts are actually persisted during verification.

For each report invalid condition, expected rejection, actual result, and enforcing rule. A case that cannot be rejected deterministically is a reusable framework defect.

# Framework Defects

Report only reusable framework defects. Do not report absent durable test artifacts, active-goal scope, or the synthetic nature of this verification as defects.

For each defect include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during the non-persistent Validate-to-Persist lifecycle verification.

# Required Output

Use these sections in this exact order:

1. Verification Summary
2. Validation Trace
3. Starting Operating State
4. Validate Completion Findings
5. Persistence Semantic Findings
6. Representative Validation and Persistence Set
7. Validate Completion Decision
8. Persist Activation Decision
9. Proposed Execution Artifact
10. Proposed State Artifact
11. Validation Results
12. Negative Validation Results
13. Compare-and-Swap and Partial Persistence Results
14. Framework Defects
15. Repository Mutation Confirmation
16. Next Authorized Action

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
