# AI Flywheel Self-Hosting Certification Verification

## Purpose

Verify certification scenario 10 by using the AI Flywheel's own operating contracts to assemble, validate, classify, and govern its certification package.

This verification is expected to prove that the self-hosting process succeeds while the certification and readiness records fail safely because retained Prompt 001 and Prompt 002 evidence does not identify the exact tested framework commit SHA.

## Repositories and immutable revisions

Framework repository: `Infoconex/ai-flywheel-framework`

Framework revision:

```text
18335e57165a8984adab4790d3a6210355b484ba
```

Historical testing evidence repository: `Infoconex/ai-flywheel-framework-testing`

Historical evidence revision:

```text
aceda4a01c27abcdca96bed3319cfa987a0272b5
```

Use these exact revisions for their respective reads. Do not substitute branch heads, later commits, chat history, cached content, or inferred revisions.

## Authorization and isolation

This prompt authorizes an isolated, in-memory self-hosting certification verification.

It authorizes:

- Reading the pinned framework and testing evidence.
- Executing the immutable fixture sources in memory.
- Constructing and validating proposed mission, goal, execution, evidence, finding, decision, certification, readiness, persistence, reuse, and state artifacts.
- Reporting certification evidence gaps and corrective rerun actions.

It does not authorize:

- Modifying the framework repository or its feature branch.
- Modifying durable framework state or lifecycle records.
- Creating human approval.
- Changing readiness.
- Completing the durable onboarding mission or certification goal.
- Inspecting an application repository.
- Correcting Prompt 001 or Prompt 002 during this independent run.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Framework resolution

Read `.flywheel/manifest.yaml` first at the pinned framework revision.

Then read and independently resolve every manifest-required file in manifest order. The corrected manifest contains exactly 50 required files. Report `50/50` manifest-required resolution.

Resolve the durable active mission and active goal from state for context only. Do not use the durable onboarding goal as authorization for this isolated certification fixture.

Pay particular attention to:

- `.flywheel/operating-model/guidance/certification.md`
- `.flywheel/operating-model/guidance/readiness.md`
- `.flywheel/operating-model/guidance/records.md`
- `.flywheel/operating-model/guidance/persistence.md`
- `.flywheel/operating-model/guidance/mission-model.md`
- `.flywheel/operating-model/guidance/execution-model.md`
- `.flywheel/operating-model/guidance/lifecycle.md`
- `.flywheel/operating-model/guidance/evidence.md`
- `.flywheel/operating-model/guidance/validation.md`
- `.flywheel/operating-model/guidance/approval-boundaries.md`
- `.flywheel/operating-model/config/certification-validation.yaml`
- `.flywheel/operating-model/config/validation.yaml`
- `.flywheel/operating-model/schemas/mission.schema.yaml`
- `.flywheel/operating-model/schemas/goal.schema.yaml`
- `.flywheel/operating-model/schemas/execution.schema.yaml`
- `.flywheel/operating-model/schemas/record.schema.yaml`
- `.flywheel/operating-model/schemas/approval-record.schema.yaml`
- `.flywheel/operating-model/schemas/certification-record.schema.yaml`
- `.flywheel/operating-model/schemas/readiness-validation.schema.yaml`
- `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
- `.flywheel/operating-model/schemas/reuse-assessment.schema.yaml`
- `.flywheel/operating-model/schemas/state.schema.yaml`
- `.flywheel/operating-model/schemas/README.md`

A missing manifest-required file or unresolved contextual mission or goal fails verification.

## Historical certification evidence audit

Read these 16 files at historical testing evidence revision `aceda4a01c27abcdca96bed3319cfa987a0272b5`:

1. `test/ai/prompts/001-startup-validation.md`
2. `test/ai/results/001-startup-validation.md`
3. `test/ai/prompts/002-execution-creation.md`
4. `test/ai/results/002-execution-creation.md`
5. `test/ai/prompts/010-end-to-end-execution.md`
6. `test/ai/results/010-end-to-end-execution.md`
7. `test/ai/prompts/011-resume-interrupted-execution.md`
8. `test/ai/results/011-resume-interrupted-execution.md`
9. `test/ai/prompts/013-enforce-approval-boundary.md`
10. `test/ai/results/013-enforce-approval-boundary.md`
11. `test/ai/prompts/014-recover-missing-required-artifact-launcher.md`
12. `test/ai/results/014-recover-missing-required-artifact.md`
13. `test/ai/prompts/015-recover-broken-active-reference-launcher.md`
14. `test/ai/results/015-recover-broken-active-reference.md`
15. `test/ai/prompts/016-run-representative-proving-mission-launcher.md`
16. `test/ai/results/016-run-representative-proving-mission.md`

Report `16/16` historical evidence reads.

Independently confirm:

- Prompt 001's retained prompt and result identify only a branch and do not identify the exact tested framework commit SHA.
- Prompt 002's retained prompt and result identify only a branch and do not identify the exact tested framework commit SHA.
- Do not infer either missing revision from branch history, later commits, chat history, likely intent, or repository chronology.
- The retained results for scenarios 3 through 9 identify sufficient immutable tested framework revisions and evidence for this fixture's expected conclusions.

A tested framework revision and the revision containing testing evidence are different identities. Do not substitute one for the other.

## Immutable self-hosting fixture definition

Read:

```text
test/ai/fixtures/017-self-host-certification.yaml
```

at commit:

```text
42461bcc86ea75c3752082b33d7c24dd18a8bd62
```

Expected blob SHA:

```text
4a14008db5ef906999e3f41570192fe3efcc378a
```

Verify the exact blob and required expected behavior before executing the harness.

## Deterministic fixture harness

Retrieve the immutable base fixture source:

```text
test/ai/tools/verify_prompt_017_fixtures.py
```

Base fixture commit:

```text
e032b9ed23aca4476c2d4c95557c1fc32121d669
```

Base fixture blob:

```text
ea34857e39da0440a5d6f4d555475c91161aac24
```

Retrieve the deterministic correction runner:

```text
test/ai/tools/run_prompt_017_fixtures.py
```

Correction runner commit:

```text
9f995a90f95ba87b1301b286a4ea2683dab1e8e3
```

Correction runner blob:

```text
1106d396ab13aeb4c79451ed96c6f3e367cec657
```

Verify both connector-reported Git blob SHAs before execution.

Execute the sources directly in memory. Do not download, mount, write, or manually reconstruct either source.

Use this procedure conceptually:

```python
runner_namespace = {"__name__": "prompt_017_runner"}
exec(compile(runner_source, "run_prompt_017_fixtures.py", "exec"), runner_namespace)
fixture_output = runner_namespace["run"](base_source)
```

The fixture run is valid only when:

- `framework_revision` equals `18335e57165a8984adab4790d3a6210355b484ba`.
- `evidence_revision` equals `aceda4a01c27abcdca96bed3319cfa987a0272b5`.
- `self_host_evidence_revision` equals `42461bcc86ea75c3752082b33d7c24dd18a8bd62`.
- `execution_mode` is `in-memory connector source with deterministic correction runner`.
- `correction_count` is `16`.
- `result` is `passed`.
- Exactly 11 complete artifact snapshots are returned.
- All 16 fixture checks are true.
- All 44 negative cases are true.
- The certification record contains exactly ten scenarios.
- Scenarios 1 and 2 have `tested_framework_revision: null`, a non-null evidence revision, and `result: failed`.
- Every passed scenario has a non-null tested framework revision.
- Scenario 8 uses only Prompt 016 as its revision-consistent evidence-completeness fixture.
- Scenario 10 references the immutable Prompt 017 fixture definition.

Do not manually adjust fixture identities, timestamps, hashes, artifact bytes, scenario outcomes, or correction counts.

## Independent artifact validation

Independently validate all 11 snapshots and every contained artifact using JSON Schema Draft 2020-12 after YAML 1.2 parsing with `format` enforcement.

Validate these individual artifacts:

- One mission against `mission.schema.yaml`.
- One goal against `goal.schema.yaml`.
- One execution against `execution.schema.yaml`.
- Four evidence records against `record.schema.yaml`.
- Two finding records against `record.schema.yaml`.
- One decision record against `record.schema.yaml`.
- One certification record against `certification-record.schema.yaml`.
- One readiness validation against `readiness-validation.schema.yaml`.
- One reuse assessment against `reuse-assessment.schema.yaml`.
- One persistence plan against `persistence-plan.schema.yaml`.
- One state artifact against `state.schema.yaml`.

Also validate all cross-artifact invariants, including:

- Stable mission, goal, and execution identities.
- Goal ownership and acceptance-criterion order.
- Complete criterion-to-evidence mapping.
- Evidence, evaluation, classification, finding, decision, adaptation, and validation provenance.
- All eight lifecycle stages completed in canonical order.
- Successful execution with `completion.disposition: goal-blocked`.
- Active mission, blocked goal, and blocked state consistency.
- Certification scenario ID/name mapping and revision identity semantics.
- Certification findings and corrective-action coverage.
- Null approval and authority identities.
- Failed readiness with blockers and `proposed_state: null`.
- Complete persistence target set, canonical paths, operations, dependencies, mutability, and digests.
- Certification and readiness targets accepted by the persistence-plan schema.
- Supporting records ordered before certification, readiness, goal, execution, and state.
- State as the final operational pointer.
- Deferred reuse promotion with no knowledge record.

## Expected self-hosting and certification outcomes

The expected results are deliberately different:

```text
Self-Hosting Scenario Result: Passed
Certification Record Result: Failed
Readiness Validation Result: Failed
```

The self-hosting scenario passes because the Flywheel uses its own contracts to:

- Audit all ten scenarios.
- Detect insufficient immutable evidence.
- Persist durable-shaped evidence, findings, decision, validation, certification, readiness, persistence, and reuse artifacts in memory.
- Define corrective reruns.
- Preserve the human approval and readiness boundaries.

The certification record fails because scenarios 1 and 2 lack exact tested framework revisions.

The readiness validation fails because certification failed, human approval is absent, and the certification goal remains blocked.

Do not classify this expected certification failure as a framework defect or a current Prompt 017 defect.

## Required validation results

Report exactly 32 validation-result rows in this order:

1. Immutable framework revision and manifest resolution.
2. Durable contextual mission and goal resolution.
3. Historical evidence revision and 16-file resolution.
4. Prompt 001 immutable-revision evidence gap.
5. Prompt 002 immutable-revision evidence gap.
6. Self-hosting fixture definition identity.
7. Base fixture source identity.
8. Correction runner source identity and correction count.
9. Harness execution result, snapshot count, and checks.
10. Synthetic mission schema validation.
11. Synthetic goal schema validation.
12. Synthetic execution schema validation.
13. Evidence-record schema validation.
14. Finding-record schema validation.
15. Decision-record schema validation.
16. Certification-record schema validation.
17. Readiness-validation schema validation.
18. Reuse-assessment schema validation.
19. Persistence-plan schema validation.
20. State schema validation.
21. Exact ten-scenario identity and ordering.
22. Scenario revision-identity semantics.
23. Scenarios 1 and 2 failed-evidence classification.
24. Scenarios 3 through 9 evidence sufficiency.
25. Scenario 10 self-hosting result.
26. Self-hosting cross-artifact provenance.
27. Eight-stage lifecycle and terminal execution consistency.
28. AC-970 through AC-973 evidence sufficiency.
29. Certification failure, findings, and corrective actions.
30. Readiness failure and approval/state boundary.
31. Persistence completeness, ordering, and recovery semantics.
32. Negative cases, result-format compliance, and repository immutability.

For each row include expected condition, actual condition, result, and enforcing source.

Every row must pass for Prompt 017 verification to pass, including rows that verify the expected certification and readiness failures.

## Negative validation

Enumerate all 44 corrected harness negative cases in harness order and identify the enforcing schema or semantic rule.

A negative case passes only when the invalid behavior is rejected.

The corrected cases include rejection of:

- Missing, duplicate, or mismatched certification scenarios.
- A passed scenario without evidence or tested framework revision.
- Treating a testing evidence commit or branch name as the tested framework revision.
- Filling missing revisions from chat history.
- Passing or preparing certification for approval while a scenario failed.
- Passing certification without durable human approval.
- Assumed authority or incomplete approval scope.
- Failed certification without findings or corrective actions.
- Incomplete self-hosting mission, goal, execution, evidence, validation, or persistence references.
- Passing readiness from a failed certification.
- Pending or failed readiness carrying a proposed ready state.
- Enabling application missions while readiness is not ready.
- Completing the goal or mission despite certification blockers.
- Marking the self-hosting execution failed when its authorized evaluation succeeded.
- Omitting `goal-blocked` from the successful execution.
- Lifecycle, evidence, classification, decision, adaptation, or scope violations.
- Persistence plans that omit or reject certification and readiness targets.
- Readiness or state written before supporting records.
- Framework writes, README changes, alternate results, or invalid result formatting.

A negative case that cannot be rejected deterministically is a reusable framework defect.

## Framework defects

Report only reusable defects in the pinned framework revision.

For each defect include identifier, severity, artifact, rule, observed behavior, expected behavior, deterministic impact, and framework-only correction.

Do not report the Prompt 001 and Prompt 002 historical evidence gaps as framework defects. They are certification corrective actions.

When none are found, state:

> No reusable framework defects were found during self-hosted certification verification.

## Required result format

Follow `test/ai/RESULT_FORMAT.md` at commit `43b35bd896554793a3142ddf6f654ffdf8bec7f2`.

Use exactly these 22 numbered level-two sections beneath one level-one document title:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Certification Authorization and Scope
5. Historical Evidence Audit
6. Self-Hosting Mission and Goal
7. Self-Hosting Execution
8. Evidence Record Set
9. Findings and Corrective Actions
10. Decision and Adaptation
11. Certification Record
12. Certification Scenario Results
13. Readiness Validation
14. Persistence Plan
15. Reuse Assessment
16. Acceptance-Criterion Evidence Mapping
17. Validation Results
18. Negative Validation Results
19. Result-Format Validation
20. Framework Defects
21. Repository Mutation Confirmation
22. Next Test Action

Under `## 1. Verification Summary`, reproduce this completed structure inside one fenced `text` block:

```text
Operating Validation: Passed | Failed
Verification Result: Passed | Failed
Fixture Harness Result: Passed | Failed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: <count>
Prompt or Fixture Defects Found: <count>
```

After the summary block, put each identity, revision, execution mode, count, and outcome in its own one-line paragraph separated by one blank line.

Required metadata includes:

- Framework revision tested.
- Historical evidence revision.
- Base fixture commit and blob.
- Correction runner commit and blob.
- Self-hosting fixture-definition commit and blob.
- Harness execution mode.
- Manifest-required reads `50/50`.
- Historical evidence reads `16/16`.
- Artifact snapshots `11`.
- Fixture checks `16`.
- Validation-result rows `32`.
- Negative cases `44`.
- Self-hosting scenario result `Passed`.
- Certification record result `Failed`.
- Readiness validation result `Failed`.

Under `## 21. Repository Mutation Confirmation`, use this fenced `text` structure:

```text
Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: Yes | No
Testing Repository README Modified: No
```

## Result-format validation

Before committing the result, execute `test/ai/tools/validate_result_format.py` from commit `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c` with expected section count `22`.

The result-format validator must pass.

## Passing rule

Prompt 017 verification passes only when:

- All 50 manifest-required framework files resolve.
- All 16 historical evidence files resolve.
- The immutable fixture definition and both fixture source blobs match.
- The corrected fixture reports passed with 11 snapshots, 16 true checks, and 44 true negative cases.
- All individual artifacts pass applicable schema validation.
- All cross-artifact and persistence semantics pass.
- All 32 validation rows pass.
- All 44 invalid cases reject.
- The self-hosting scenario passes.
- The certification record fails exactly because scenarios 1 and 2 lack tested framework revisions.
- The readiness validation fails and proposes no ready state.
- No human approval is invented.
- No framework or durable-state mutation occurs.
- The result-format validator passes.
- No blocking reusable framework defect remains.

## Next action

When Prompt 017 verification passes with the expected certification evidence gaps, state exactly:

`Create corrected Prompt 001 and Prompt 002 rerun launchers pinned to framework revision 18335e57165a8984adab4790d3a6210355b484ba before consolidated certification.`
