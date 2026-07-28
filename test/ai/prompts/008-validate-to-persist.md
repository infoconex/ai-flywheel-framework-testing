# AI Flywheel Cold Lifecycle Verification
## Validate → Persist Transition (Non-Persistent)

> **Purpose**
>
> Validate that the AI Flywheel operating model can deterministically complete **Validate** and begin **Persist** without modifying the repository.

---

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Branch:** `feature/self-contained-operating-model`

---

# Cold Start Instructions

Ignore all previous conversations, memory, cached repository knowledge, and prior test results.

Treat this as the first time you have encountered this repository. The repository is the authority for framework semantics. Resolve all rules from the immutable revision inspected during this verification.

---

# Verification Authorization

This prompt explicitly authorizes a **synthetic, non-persistent operating-model verification**.

This authorization is limited to:

- Reading the framework repository.
- Reconstructing hypothetical execution, state, record, and persistence artifacts entirely in memory.
- Evaluating those proposed artifacts against repository-defined schemas and semantic rules.
- Constructing and testing invalid in-memory fixtures.
- Reporting proposed artifacts and results.

This verification is **not goal-directed repository work** and MUST NOT be rejected merely because the repository's current active mission or goal has a different objective.

The active mission, active goal, and current durable state MUST still be resolved and reported, but they provide structural context only. Their scope restrictions apply to actual repository operations, not to this read-only synthetic conformance test.

Do not create or activate an execution. Do not update state. Do not inspect an application repository. Do not persist any artifact. All reconstructed artifacts are hypothetical and MUST be labeled:

> **PROPOSED ONLY — NOT WRITTEN**

---

# Objective

Perform a non-persistent verification of:

```text
Validate (in progress)
        ↓
Validate (completed)
        ↓
Persist (in progress)
```

Determine whether the framework provides deterministic rules for:

- Completing Validate.
- Starting Persist.
- Validation planning versus execution.
- Evidence requirements for passed and failed validation.
- Failed-validation findings, recovery actions, dispositions, decisions, and approvals.
- Adaptation-status synchronization.
- Persistence target derivation, canonical locations, mutability, digests, ordering, compare-and-swap, verification, rollback, and compensation.
- Preserving immutable history.
- Preventing premature Reuse claims.
- Rejecting invalid transitions.

---

# Repository Mutation Rules

You may read repository files and construct artifacts in memory.

You MUST NOT:

- Create, modify, or delete repository files.
- Stage, commit, or push changes.
- Activate an execution or advance the durable lifecycle.
- Update state.
- Persist records, evidence, findings, decisions, approvals, validation results, learning, logs, knowledge, or persistence plans.
- Inspect or modify an application repository.
- Run application-changing commands.

---

# Mandatory Startup Completion Checkpoint

Before lifecycle reconstruction:

1. Begin at the repository root.
2. Resolve `.flywheel/manifest.yaml`.
3. Read every path in `required_files` in the declared order.
4. Read current state, active mission, active goal, and any active execution last.
5. Resolve the immutable commit revision.

Report:

- Required files declared.
- Required files successfully read.
- Missing or unreadable files.
- Startup resolution as passed or failed.

Do not treat response length, tool-call count, or partial inspection as a reason to stop. Continue until every manifest-required file has been read. If all files exist and are readable, startup MUST NOT fail merely because multiple reads were required.

After startup succeeds, continue this synthetic verification regardless of whether the current active goal would authorize an actual Validate-to-Persist execution.

---

# Verification Starting Point

Assume conceptually that Prompts 001 through 007 succeeded. Do not copy prior result artifacts.

Using current repository rules, reconstruct in memory a complete valid state with:

- Execute, Observe, Evaluate, Classify, and Adapt completed.
- Validate in progress.
- Persist and Reuse pending.
- State identifying Validate as the active stage.
- Structured observations, evaluations, classifications, adaptations, and validations.
- At least one approved and implemented adaptation.
- At least one validation-ineligible adaptation with explicit exclusion.
- At least one evidence-backed passed validation.
- When supported, at least one failed validation with finding, recovery action, linked disposition decision, and required approvals.

If the repository lacks deterministic rules needed for reconstruction, report a reusable framework defect. Do not substitute the active-goal scope boundary for this determination.

---

# Validate Completion Verification

Determine from repository rules:

1. Required validation-plan fields.
2. Planned versus executed states.
3. Permitted completion statuses.
4. Eligibility and exclusion rules.
5. Evidence requirements for pass and failure.
6. Finding and recovery requirements for failure.
7. Failed-validation disposition, decision, approval, scope, supersession, and persistence-permission rules.
8. Pending-validation restrictions.
9. Adaptation-status synchronization.
10. Stage references, summaries, and timestamps.
11. Revised-validation history requirements.
12. Whether command success alone is sufficient proof.

Construct a representative validation set containing passed, not-applicable, and—when supported—failed validation with complete traceability.

Determine whether Validate may legally complete.

---

# Persistence Semantic Verification

Determine from repository rules:

1. Persist activation prerequisites.
2. Required persistence-plan structure and lifecycle.
3. Complete target-set derivation.
4. Canonical target locations.
5. Create-only, supersede-only, and compare-and-swap mutation semantics.
6. Digest calculation.
7. Dependency and type ordering.
8. State as final operational pointer.
9. Per-write and whole-set verification.
10. Partial-write rollback and compensation.
11. Failed-validation authorization precheck.
12. Immutable-history protection.
13. Reuse boundary protection.

Do not invent persistence semantics absent from the repository.

---

# Representative Validation and Persistence Set

Construct a concrete in-memory set containing:

- Passed validation with evidence.
- Not-applicable validation with exclusion reason.
- Failed validation with evidence, finding, recovery action, and a valid linked decision disposition when supported.
- Required approvals when applicable.
- Synchronized adaptation statuses.
- A schema-valid persistence plan.
- Every required target and canonical path.
- Exact operation, mutability, precondition, digest, dependencies, rollback action, and write order.
- Complete traceability through validation, adaptation, classification, evaluation, observation, and evidence.

Use concrete values, not placeholders.

---

# Proposed Lifecycle Transition

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

Validate:

- Exactly one stage is in progress.
- No stage is skipped.
- Timestamps are ordered.
- State and execution agree.
- All references resolve.
- No repository mutation occurs.

---

# Proposed Execution and State Artifacts

Construct complete proposed execution and state artifacts as they would exist after Validate completes and Persist starts.

Requirements:

- Concrete values only.
- All lifecycle stages included.
- Required structured records and references included.
- Validation results and adaptation statuses synchronized.
- Persistence plan referenced without claiming persistence completion.
- Reuse remains pending.

Precede each artifact with:

> **PROPOSED ONLY — NOT WRITTEN**

Validate both artifacts against schemas and semantic and cross-artifact rules.

---

# Required Validation

Report separately:

1. Startup resolution.
2. Required-file resolution.
3. Active mission resolution.
4. Active goal resolution.
5. Synthetic-verification authorization.
6. Starting execution reconstruction.
7. Execution schema validation.
8. State schema validation.
9. Validation semantics and provenance.
10. Validation eligibility and evidence sufficiency.
11. Failure handling and disposition authorization.
12. Adaptation-status synchronization.
13. Validate completion.
14. Persistence semantics and target locations.
15. Immutable history.
16. Persist activation.
17. Lifecycle ordering and transition.
18. Cross-artifact references.
19. Timestamps and identities.
20. Compare-and-swap.
21. Partial-persistence recovery.
22. Post-transition verification.
23. Repository immutability.

For each include the expected condition, actual condition, result, and repository source.

---

# Negative Validation

Construct invalid in-memory fixtures and demonstrate rejection of at least:

1. Persist starts while Validate is in progress.
2. Validate and Persist both in progress.
3. Persist starts before Validate completion.
4. Required validation remains pending.
5. Passed or failed validation lacks evidence.
6. Failed validation lacks finding or recovery action.
7. Failed validation lacks a valid linked disposition.
8. A blocking disposition is treated as permitting persistence.
9. A required approval is missing or scope-mismatched.
10. Not-applicable lacks exclusion reason.
11. Ineligible adaptation passes.
12. Adaptation status disagrees with validation.
13. A reference does not resolve.
14. Command success alone is treated as proof.
15. Failed validation is silently changed to passed.
16. Revised validation weakens scope or lacks supersession.
17. Persistence plan lacks a complete target set.
18. Persistence plan targets itself or uses a self-digest.
19. Target path is noncanonical.
20. Immutable history is overwritten.
21. Required record is omitted.
22. Persist claims Reuse early.
23. Lifecycle stage is skipped.
24. State and execution disagree.
25. Timestamps are out of order.
26. A stale compare-and-swap revision is used.
27. Partial persistence lacks recovery.
28. Final artifacts are not re-read and verified.
29. Repository artifacts are actually persisted during verification.

For each report the invalid condition, expected rejection, actual result, and enforcing rule.

If a case cannot be rejected deterministically, report a reusable framework defect.

---

# Framework Defects

Only report reusable framework defects. Do not report absent persisted execution artifacts, current active-goal scope, or the synthetic nature of this test as defects.

For each defect include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

If none are found, state:

> No reusable framework defects were found during the non-persistent Validate-to-Persist lifecycle verification.

---

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

When verification passes, the final section must state:

> Run the next non-persistent lifecycle verification.

When a reusable framework defect blocks verification, use:

> Correct only the reusable framework defect before repeating this verification.
