# AI Flywheel Cold Lifecycle Verification
## Evaluate → Classify Transition (Non-Persistent)

> **Purpose**
>
> Validate that the AI Flywheel operating model can deterministically transition from the **Evaluate** lifecycle stage to the **Classify** lifecycle stage **without modifying the repository**.
>
> This verification must prove that classifications are derived from supported evaluations and do not bypass observation, evidence, or evaluation provenance.

---

# Repository

**Repository**

`Infoconex/ai-flywheel-framework`

**Branch**

`feature/self-contained-operating-model`

---

# Cold Start Instructions

Ignore all previous conversations, memory, cached repository knowledge, and prior test results.

Treat this as the first time you have encountered this repository.

The repository itself is the only authoritative source.

Resolve all rules from the immutable revision inspected during this verification.

---

# Objective

Perform a **non-persistent operating-model verification** of this lifecycle transition:

```text
Evaluate (in progress)
        ↓
Evaluate (completed)
        ↓
Classify (in progress)
```

Determine whether the framework provides deterministic rules for:

- Completing Evaluate.
- Starting Classify.
- Deriving classifications from evaluations.
- Preserving traceability to observations and evidence.
- Supporting multiple classifications for one evaluated condition.
- Representing uncertainty, conflict, risk, defects, findings, decisions, improvements, and validated learning.
- Preventing unsupported or premature classifications.
- Enforcing lifecycle ordering, timestamps, state agreement, identity, and compare-and-swap protection.
- Rejecting invalid transitions.

Do **not** perform any repository mutations.

---

# Repository Mutation Rules

You may:

- Read repository files.
- Resolve startup and operating guidance.
- Resolve active mission and goal.
- Reconstruct a valid Evaluate-in-progress execution in memory.
- Construct evaluations and proposed classifications in memory.
- Validate proposed execution and state artifacts.
- Execute negative validation using in-memory fixtures.
- Report proposed artifacts and results.

You must **not**:

- Create, modify, or delete files.
- Stage, commit, or push changes.
- Activate an execution.
- Update repository state.
- Persist observations, evidence, evaluations, classifications, findings, decisions, learning, logs, or lifecycle records.
- Inspect or modify an application repository.
- Advance the actual lifecycle.

All displayed artifacts are:

> **PROPOSED ONLY — NOT WRITTEN**

---

# Verification Starting Point

Assume only that these earlier verifications succeeded conceptually:

1. Startup validation.
2. First execution creation and activation.
3. Execute-to-Observe transition.
4. Observe-to-Evaluate transition.

Do not copy artifacts from prior test results.

Use current repository rules to reconstruct the complete valid operating state with:

- Execute completed.
- Observe completed.
- Evaluate in progress.
- Classify through Reuse pending.
- State identifying Evaluate as the active lifecycle stage.
- Structured observations and supporting evidence.
- At least one structured evaluation with required provenance.

If the repository does not provide enough information to reconstruct this state deterministically, report a reusable framework defect and stop before inventing missing rules.

---

# Startup and Operating Resolution

Before testing the transition:

1. Begin at the repository root.
2. Follow repository-defined startup instructions.
3. Resolve the manifest and ordered required files.
4. Read state, active mission, and active goal.
5. Read schemas and guidance for executions, lifecycle, evaluations, classifications, evidence, findings, decisions, adaptation, validation, and persistence.
6. Resolve timestamp, identity, cross-artifact, and compare-and-swap rules.
7. Record the immutable repository revision.

Do not begin transition verification until the operating model has been resolved.

---

# Evaluation Completion Verification

Determine from repository-defined rules only:

1. What qualifies as a material evaluation.
2. What outputs Evaluate must produce before completion.
3. Whether every evaluation requires observation references.
4. Whether every evaluation requires evidence references.
5. Whether criteria or rule references are mandatory when applicable.
6. How limitations and uncertainty are represented.
7. Whether evaluations may conflict.
8. Whether Evaluate may complete with no evaluations.
9. Whether Evaluate may contain classifications, recommendations, adaptations, persist decisions, or reuse decisions.
10. What summary, references, and timestamps are required.

Construct a representative evaluation set containing at least:

- One evaluation that supports a conclusion.
- One evaluation that does not support a conclusion or remains inconclusive.
- One evaluation with explicit limitations or uncertainty.
- Supporting observation and evidence references.

Determine whether Evaluate may legally complete.

---

# Classification Semantic Verification

Determine from repository-defined rules only:

1. What qualifies as a classification.
2. Which classification types are permitted.
3. Whether one evaluation may produce multiple classifications.
4. Whether multiple evaluations may support one classification.
5. Whether classifications require evaluation references.
6. Whether classifications require observation or evidence references directly or indirectly.
7. Whether uncertainty must remain uncertainty unless evidence supports another type.
8. Whether conflicting classifications may coexist.
9. Whether a decision classification requires a decision record.
10. Whether validated learning requires prior validation.
11. Whether a finding differs from a defect.
12. Whether recommendations and adaptations are prohibited during Classify.

For every classification, require a stable identity and traceability sufficient to explain:

- What was classified.
- Why it received that classification.
- Which evaluation supports it.
- Which evidence ultimately supports it.
- Whether it remains uncertain, conflicting, or unresolved.

Do not invent classification semantics absent from the repository.

---

# Representative Classification Set

Construct a small concrete classification set entirely in memory.

The set must include, when supported by the framework:

1. At least one finding or defect classification.
2. At least one uncertainty or risk classification.
3. At least one case where a single evaluation produces more than one legitimate classification.
4. Full provenance to evaluations, observations, and evidence.

The set must not contain:

- Unsupported classifications.
- Recommendations.
- Adaptations.
- Validation conclusions not yet established.
- Persistence decisions.
- Reuse decisions.
- Classifications disguised as observations or evaluations.

Clearly label the set:

> **PROPOSED ONLY — NOT WRITTEN**

---

# Classify Activation Verification

Determine what must exist before Classify may transition from `pending` to `in-progress`.

Validate at minimum:

- Execute and Observe remain completed.
- Evaluate is completed.
- Evaluate completion timestamp exists.
- Classify start timestamp exists.
- Classify starts no earlier than Evaluate completion.
- Classify becomes the only in-progress stage.
- Adapt through Reuse remain pending.
- Evaluation outputs remain available and unchanged.
- No adaptation is already asserted.
- State and execution agree on the active execution and stage.
- Identity and compare-and-swap rules remain satisfied.

Determine whether Classify can legally begin.

---

# Proposed Lifecycle Transition

Construct and validate this complete in-memory transition:

```text
Execute  = completed
Observe  = completed
Evaluate = completed
Classify = in-progress
Adapt    = pending
Validate = pending
Persist  = pending
Reuse    = pending
```

Also validate:

- Exactly one lifecycle stage is in progress.
- No stage is skipped.
- All predecessor stages are completed or properly not applicable.
- All successor stages remain pending.
- Stage timestamps are chronologically valid.
- State lifecycle stage is `classify`.
- State and execution identify the same active execution.
- All unchanged state fields are preserved.
- No repository mutation occurs.

---

# Proposed Execution and State Artifacts

Construct the complete proposed execution and state artifacts exactly as they would exist after Evaluate completes and Classify starts.

Requirements:

- Use concrete values.
- Do not use placeholders.
- Preserve all unchanged fields.
- Include all lifecycle stages.
- Include structured observations, evaluations, and proposed classifications required by the framework.
- Preserve mission, goal, execution, readiness, and implementation fields.
- Include required references, summaries, timestamps, identity, and revision information.

Precede each artifact with:

> **PROPOSED ONLY — NOT WRITTEN**

Validate both artifacts against schemas and all semantic and cross-artifact rules.

---

# Required Validation

Report separately:

1. Startup resolution.
2. Required-file resolution.
3. Active mission resolution.
4. Active goal resolution.
5. Starting execution reconstruction.
6. Execution schema validation.
7. State schema validation.
8. Evaluation semantic validation.
9. Evaluation provenance validation.
10. Evaluate completion validation.
11. Classification semantic validation.
12. Classification provenance validation.
13. Multiple-classification validation.
14. Classify activation validation.
15. Lifecycle ordering validation.
16. Transition validation.
17. Cross-artifact validation.
18. Timestamp validation.
19. Identity validation.
20. Compare-and-swap validation.
21. Post-transition validation.
22. Repository immutability validation.

For every validation include:

- Artifact or rule evaluated.
- Expected condition.
- Actual condition.
- Pass or fail result.
- Repository source enforcing the result.

---

# Negative Validation

Construct invalid in-memory fixtures and demonstrate rejection of at least these cases:

1. Classify starts while Evaluate remains in progress.
2. Evaluate and Classify are both in progress.
3. Classify starts before Evaluate completion.
4. Evaluate completes with no required evaluations.
5. Evaluate completes without required provenance.
6. Evaluation references a nonexistent observation.
7. Evaluation references nonexistent evidence.
8. Classification has no evaluation reference.
9. Classification has no traceable evidence basis.
10. Unsupported classification type.
11. Duplicate classification identity.
12. A defect is asserted when the evaluation is only inconclusive.
13. Uncertainty is silently converted into a confirmed defect.
14. A recommendation or adaptation is recorded as a classification.
15. A decision classification exists without the required decision record.
16. Validated learning is asserted before validation.
17. Adapt starts before Classify completes.
18. Lifecycle stage is skipped.
19. State says Classify while execution says Evaluate.
20. Execution says Classify while state says Evaluate.
21. Stage timestamps are out of order.
22. Stale compare-and-swap value is used.
23. Repository artifacts are persisted during verification.

For each scenario report:

- Invalid condition.
- Expected rejection.
- Actual result.
- Rule enforcing rejection.

If a required case cannot be rejected deterministically, report a reusable framework defect.

---

# Framework Defects

Only report reusable framework defects.

Do not report the absence of persisted execution artifacts as a defect.

For each defect include:

- Identifier.
- Severity.
- Artifact.
- Rule.
- Observed behavior.
- Expected behavior.
- Deterministic impact.
- Framework-only correction.

---

# Final Report

Produce exactly these sections:

## 1. Verification Summary
## 2. Validation Trace
## 3. Starting Operating State
## 4. Evaluation Completion Findings
## 5. Classification Semantic Findings
## 6. Representative Evaluation and Classification Set
## 7. Evaluate Completion Decision
## 8. Classify Activation Decision
## 9. Proposed Execution Artifact
## 10. Proposed State Artifact
## 11. Validation Results
## 12. Negative Validation Results
## 13. Compare-and-Swap Results
## 14. Framework Defects
## 15. Repository Mutation Confirmation
## 16. Next Authorized Action

Expected successful summary values:

```text
Operating Validation: Passed
Verification Result: Passed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: None
```

If no framework defect exists, state exactly:

> No reusable framework defects were found during the non-persistent Evaluate-to-Classify lifecycle verification.

For the next authorized action, state only one of:

> Run the next non-persistent lifecycle verification.

or

> Correct only the reusable framework defect before repeating this verification.

Stop after the final section.