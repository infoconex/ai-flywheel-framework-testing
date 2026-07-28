# AI Flywheel Cold Lifecycle Verification
## Classify → Adapt Transition (Non-Persistent)

> **Purpose**
>
> Validate that the AI Flywheel operating model can deterministically transition from **Classify** to **Adapt** without modifying the repository.
>
> This verification must prove that adaptations are justified by supported classifications, remain within authorized scope, preserve human authority, and do not bypass validation or persistence.

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
Classify (in progress)
        ↓
Classify (completed)
        ↓
Adapt (in progress)
```

Determine whether the framework provides deterministic rules for:

- Completing Classify.
- Starting Adapt.
- Deriving adaptations from classifications.
- Distinguishing an adaptation from a recommendation, decision, classification, action, or validation result.
- Determining when Adapt is required versus not applicable.
- Preserving traceability to classifications, evaluations, observations, and evidence.
- Enforcing goal scope, governance, approval, and human-authority boundaries.
- Preventing unsupported, premature, or out-of-scope adaptations.
- Preventing adaptation from claiming validation, persistence, or reuse before those stages occur.
- Enforcing lifecycle ordering, timestamps, state agreement, identity, and compare-and-swap protection.
- Rejecting invalid transitions.

Do **not** perform repository mutations.

---

# Repository Mutation Rules

You may:

- Read repository files.
- Resolve startup and operating guidance.
- Resolve the active mission and goal.
- Reconstruct a valid Classify-in-progress execution in memory.
- Construct classifications and proposed adaptations in memory.
- Construct proposed approval, decision, and finding references when required by repository rules.
- Validate proposed execution and state artifacts.
- Execute negative validation using in-memory fixtures.
- Report proposed artifacts and results.

You must **not**:

- Create, modify, or delete files.
- Stage, commit, or push changes.
- Activate an execution.
- Update repository state.
- Persist observations, evidence, evaluations, classifications, adaptations, findings, decisions, approvals, learning, logs, or lifecycle records.
- Inspect or modify an application repository.
- Perform the proposed adaptation.
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
5. Evaluate-to-Classify transition.

Do not copy artifacts from prior test results.

Use current repository rules to reconstruct the complete valid operating state with:

- Execute completed.
- Observe completed.
- Evaluate completed.
- Classify in progress.
- Adapt through Reuse pending.
- State identifying Classify as the active lifecycle stage.
- Structured observations and evidence.
- Structured evaluations with provenance.
- Structured classifications with required certainty and type-specific references.

If the repository does not provide enough information to reconstruct this state deterministically, report a reusable framework defect and stop before inventing missing rules.

---

# Startup and Operating Resolution

Before testing the transition:

1. Begin at the repository root.
2. Follow repository-defined startup instructions.
3. Resolve the manifest and ordered required files.
4. Read state, active mission, and active goal.
5. Read schemas and guidance for executions, lifecycle, classifications, adaptation, decisions, findings, approvals, evidence, validation, persistence, governance, authority, and scope control.
6. Resolve timestamp, identity, cross-artifact, and compare-and-swap rules.
7. Record the immutable repository revision.

Do not begin transition verification until the operating model has been resolved.

---

# Classify Completion Verification

Determine from repository-defined rules only:

1. What outputs Classify must produce before completion.
2. Whether every material classification requires evaluation and evidence provenance.
3. Whether classification certainty and uncertainty must be resolved before Adapt.
4. Whether conflicting classifications may remain unresolved when Classify completes.
5. Whether Classify may complete with no classifications.
6. Whether Classify may contain recommendations or adaptations.
7. Which findings, decisions, or validation references are required by classification type.
8. What summary, references, and timestamps are required.
9. Whether a classification can remain provisional and still justify Adapt.
10. Whether classifications must identify the condition that Adapt will address.

Construct a representative classification set containing at least:

- One confirmed classification that may justify an adaptation.
- One uncertainty or risk classification.
- One classification that does not justify an adaptation.
- Required evaluation and evidence provenance.

Determine whether Classify may legally complete.

---

# Adaptation Semantic Verification

Determine from repository-defined rules only:

1. What qualifies as an adaptation.
2. What kinds of artifacts may be adapted, including application code, tools, configuration, guidance, plans, or scope.
3. How an adaptation differs from a recommendation.
4. How an adaptation differs from a decision.
5. How an adaptation differs from the action that implements it.
6. Whether every adaptation requires one or more classification references.
7. Whether every adaptation requires evidence provenance directly or indirectly.
8. Whether adaptations require a rationale and intended effect.
9. Whether adaptations must identify affected artifacts or scope.
10. Whether an adaptation may be proposed without being executed.
11. Whether Adapt may be `not-applicable` and what reason is required.
12. Whether multiple adaptations may arise from one classification.
13. Whether one adaptation may address multiple classifications.
14. How conflicting or uncertain classifications constrain adaptation certainty.
15. When human approval is required before proposing or performing an adaptation.
16. Whether scope expansion requires approval or a new goal.
17. Whether an adaptation may claim success before Validate.
18. Whether an adaptation may be persisted or promoted for reuse before Persist and Reuse.

For every adaptation require traceability sufficient to explain:

- What will change.
- Why it will change.
- Which classifications justify it.
- Which evidence ultimately supports it.
- Which artifact or operating boundary is affected.
- Whether approval is required.
- Whether the adaptation is proposed, approved, rejected, deferred, or not applicable.

Do not invent adaptation semantics absent from the repository.

---

# Representative Adaptation Set

Construct a small concrete adaptation set entirely in memory.

The set must include, when supported by the framework:

1. At least one proposed adaptation justified by a confirmed classification.
2. At least one classification for which no adaptation is warranted.
3. At least one uncertain or approval-dependent adaptation.
4. Full provenance to classifications, evaluations, observations, and evidence.
5. Any required decision or approval references.

The set must not contain:

- Unsupported adaptations.
- Work outside the active goal.
- Application implementation performed during this verification.
- Validation conclusions.
- Persistence decisions.
- Reuse decisions.
- Adaptations disguised as classifications or recommendations.
- Claims that a proposed change succeeded.

Clearly label the set:

> **PROPOSED ONLY — NOT WRITTEN**

---

# Adapt Activation Verification

Determine what must exist before Adapt may transition from `pending` to `in-progress`.

Validate at minimum:

- Execute, Observe, and Evaluate remain completed.
- Classify is completed.
- Classify completion timestamp exists.
- Adapt start timestamp exists.
- Adapt starts no earlier than Classify completion.
- Adapt becomes the only in-progress stage.
- Validate through Reuse remain pending.
- Classification outputs remain available and unchanged.
- Adaptation work is within the active goal and mission.
- Required approvals or decisions are present, or the adaptation remains explicitly pending approval.
- No validation, persistence, or reuse conclusion is already asserted.
- State and execution agree on the active execution and stage.
- Identity and compare-and-swap rules remain satisfied.

Determine whether Adapt can legally begin.

---

# Proposed Lifecycle Transition

Construct and validate this complete in-memory transition:

```text
Execute  = completed
Observe  = completed
Evaluate = completed
Classify = completed
Adapt    = in-progress
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
- State lifecycle stage is `adapt`.
- State and execution identify the same active execution.
- All unchanged state fields are preserved.
- No repository mutation occurs.

---

# Proposed Execution and State Artifacts

Construct the complete proposed execution and state artifacts exactly as they would exist after Classify completes and Adapt starts.

Requirements:

- Use concrete values.
- Do not use placeholders.
- Preserve all unchanged fields.
- Include all lifecycle stages.
- Include structured observations, evaluations, classifications, and proposed adaptations required by the framework.
- Preserve mission, goal, execution, readiness, and implementation fields.
- Include required references, summaries, timestamps, identity, approvals, decisions, and revision information.

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
8. Classification semantic validation.
9. Classification provenance validation.
10. Classify completion validation.
11. Adaptation semantic validation.
12. Adaptation provenance validation.
13. Scope and governance validation.
14. Approval and decision validation.
15. Adapt activation validation.
16. Lifecycle ordering validation.
17. Transition validation.
18. Cross-artifact validation.
19. Timestamp validation.
20. Identity validation.
21. Compare-and-swap validation.
22. Post-transition validation.
23. Repository immutability validation.

For every validation include:

- Artifact or rule evaluated.
- Expected condition.
- Actual condition.
- Pass or fail result.
- Repository source enforcing the result.

---

# Negative Validation

Construct invalid in-memory fixtures and demonstrate rejection of at least these cases:

1. Adapt starts while Classify remains in progress.
2. Classify and Adapt are both in progress.
3. Adapt starts before Classify completion.
4. Classify completes with no required classifications.
5. Classification lacks required provenance.
6. Adaptation has no classification reference.
7. Adaptation has no traceable evidence basis.
8. Adaptation is based only on an inconclusive classification without uncertainty handling.
9. A recommendation is treated as an approved adaptation.
10. An adaptation is recorded as already implemented during Adapt activation.
11. An adaptation claims successful validation before Validate.
12. An adaptation is marked persisted before Persist.
13. An adaptation is marked reusable before Reuse.
14. Adaptation exceeds the active goal scope.
15. Scope expansion occurs without approval or a new goal.
16. Human approval is required but absent.
17. A decision is required but no decision record exists.
18. An uncertain adaptation is marked confirmed without support.
19. Duplicate adaptation identity, when identities are required.
20. Validate starts before Adapt completes.
21. Lifecycle stage is skipped.
22. State says Adapt while execution says Classify.
23. Execution says Adapt while state says Classify.
24. Stage timestamps are out of order.
25. Stale compare-and-swap value is used.
26. Partial execution/state transition lacks required recovery handling.
27. Repository artifacts are persisted during verification.

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
## 4. Classify Completion Findings
## 5. Adaptation Semantic Findings
## 6. Representative Classification and Adaptation Set
## 7. Classify Completion Decision
## 8. Adapt Activation Decision
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

> No reusable framework defects were found during the non-persistent Classify-to-Adapt lifecycle verification.

For the next authorized action, state only one of:

> Run the next non-persistent lifecycle verification.

or

> Correct only the reusable framework defect before repeating this verification.

Stop after the final section.