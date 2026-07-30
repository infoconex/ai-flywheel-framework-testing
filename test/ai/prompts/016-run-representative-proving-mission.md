# AI Flywheel Representative Proving Mission Verification

## Purpose

Verify certification scenario 9 by completing a representative, useful, non-destructive mission with the installed AI Flywheel operating model.

## Repository and immutable revision

Repository: `Infoconex/ai-flywheel-framework`

Framework revision: `1b90e6789109b6693ab0dc5d79dfb1b76cc74585`

Use this exact revision for every framework read. Do not substitute a branch head or later commit.

## Authorization and isolation

This prompt authorizes an isolated, in-memory certification mission. It does not authorize changes to the framework repository, durable state, application repository, or framework branch.

Construct and validate proposed mission, goal, evidence, lifecycle, validation, persistence, reuse, and terminal artifacts entirely in memory. Label displayed artifacts:

> **PROPOSED ONLY — NOT WRITTEN**

The synthetic mission must explicitly authorize certification scenario 9 and the exact read-only inventory work. Do not reuse the durable onboarding goal as authorization.

## Required framework reads

Read these files at the pinned revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/certification.md`
4. `.flywheel/operating-model/guidance/mission-model.md`
5. `.flywheel/operating-model/guidance/execution-model.md`
6. `.flywheel/operating-model/guidance/lifecycle.md`
7. `.flywheel/operating-model/guidance/evidence.md`
8. `.flywheel/operating-model/guidance/validation.md`
9. `.flywheel/operating-model/guidance/persistence.md`
10. `.flywheel/operating-model/guidance/reuse.md`
11. `.flywheel/operating-model/guidance/records.md`
12. `.flywheel/operating-model/config/validation.yaml`
13. `.flywheel/operating-model/schemas/manifest.schema.yaml`
14. `.flywheel/operating-model/schemas/mission.schema.yaml`
15. `.flywheel/operating-model/schemas/goal.schema.yaml`
16. `.flywheel/operating-model/schemas/execution.schema.yaml`
17. `.flywheel/operating-model/schemas/record.schema.yaml`
18. `.flywheel/operating-model/schemas/persistence-plan.schema.yaml`
19. `.flywheel/operating-model/schemas/reuse-assessment.schema.yaml`

Also resolve the durable active mission and goal for context only. Report `19/19` focused resolution.

## Deterministic fixture harness

Use the exact harness source:

`test/ai/tools/verify_prompt_016_fixtures.py`

Harness commit: `9aebe151d03d1e2728905cb697336325a67409e9`

Harness blob: `93708efaee0a0b3fb1b69b2a8c6133755984cc9b`

Retrieve it through the GitHub connector, verify the blob SHA, and execute the connector-returned source directly in memory with Python 3 using `exec`. PyYAML is required. Capture the complete JSON output.

The harness must report `result: passed`, five complete artifact snapshots, all checks true, and all 34 negative cases true.

## Representative mission

Use the harness mission and goal identities:

```text
Mission: certify-representative-proving-mission
Goal: verify-installed-framework-inventory
Execution: EX-20260730T060000Z-001
```

The useful mission output is a framework inventory that:

- Uses the pinned immutable framework revision.
- Reads the actual manifest at that revision.
- Compares the actual `manifest.required_files` list to the harness-required list.
- Resolves every manifest-required path exactly once.
- Records missing paths, duplicates, case collisions, and unreadable targets.
- Produces criterion evidence for `AC-960`, `AC-961`, and `AC-962`.
- Does not inspect an application repository.
- Does not change any repository artifact or durable state.

The independent session, not the harness alone, must read the actual manifest and verify that its required-file count and exact ordered paths equal the fixture inventory. A mismatch is either a prompt/fixture defect or a framework defect depending on which source is wrong; do not silently adjust the list.

## Lifecycle and terminal proof

Construct a coherent synthetic execution across all eight stages. Prompt 010 already certified the detailed lifecycle mechanics; Prompt 016 must prove that this representative mission applies those mechanics to useful work.

Require:

- Stable mission, goal, and execution identities.
- Eight lifecycle stages in canonical order.
- Inventory observations backed by immutable repository reads.
- Evaluation of completeness and path uniqueness.
- Classification of the result as validated learning when complete, or finding/defect when incomplete.
- A read-only adaptation disposition of `not-applicable` or an equivalent schema-valid no-change plan with an explicit reason.
- Criterion-level validation results.
- Proposed persistence of evidence, inventory result, execution, mission, goal, and terminal state through applicable persistence semantics.
- A reuse assessment that classifies the inventory method as reusable guidance without changing the framework repository.
- Terminal execution `succeeded`, goal `completed`, mission `completed`, and cleared synthetic active pointers.

Do not claim durable persistence occurred. This is a proposed, non-persistent certification fixture.

## Acceptance criteria

1. `AC-960`: Every manifest-required path resolves exactly once.
2. `AC-961`: Inventory evidence preserves immutable revision, exact path, and resolution result.
3. `AC-962`: The representative mission completes without repository mutation.

Each criterion must map to durable-shaped evidence references and pass validation independently.

## Required validation results

Report exactly 24 validation-result rows:

1. Immutable revision and focused resolution.
2. Harness source identity and execution.
3. Actual manifest schema validation.
4. Fixture manifest-list equality.
5. Synthetic mission schema validation.
6. Synthetic goal schema validation.
7. Explicit proving-mission authorization.
8. Stable execution identity.
9. Execute-stage scope compliance.
10. Observation evidence completeness.
11. Evaluation provenance.
12. Classification correctness.
13. Adaptation no-change rationale.
14. Validation criterion coverage.
15. AC-960 evidence sufficiency.
16. AC-961 evidence sufficiency.
17. AC-962 evidence sufficiency.
18. Persistence semantics.
19. Reuse assessment semantics.
20. Eight-stage lifecycle completeness.
21. Terminal execution, goal, mission, and state consistency.
22. All 34 negative cases.
23. Result-format contract compliance.
24. Repository immutability.

## Negative validation

Reject all 34 harness negative cases deterministically. In the result, enumerate them in harness order and state the enforcing schema or semantic rule.

A negative case that cannot be rejected deterministically is a reusable framework defect.

## Framework defects

Report only reusable framework defects. Do not treat fixture mistakes, result-format mistakes, unavailable optional tools, or inability to mutate the read-only repository as framework defects.

When none are found, state:

> No reusable framework defects were found during representative proving mission verification.

## Required result format

Follow `test/ai/RESULT_FORMAT.md` at commit `594b195c514ab434406989af4e67db927d1164d1`.

Use exactly these 22 numbered level-two sections beneath one level-one document title:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Proving Mission Authorization
5. Synthetic Mission and Goal
6. Actual Manifest Inventory
7. Inventory Resolution Evidence
8. Stable Execution Identity
9. Lifecycle Application Trace
10. Observation, Evaluation, and Classification
11. Adaptation and Validation
12. Acceptance-Criterion Evidence Mapping
13. Persistence and Reuse Proposal
14. Terminal Mission Form
15. Useful Mission Outcome
16. Validation Results
17. Negative Validation Results
18. Result-Format Validation
19. Framework Defects
20. Repository Mutation Confirmation
21. Certification Scenario Result
22. Next Test Action

Under `## 1. Verification Summary`, reproduce this completed structure inside a fenced `text` block:

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

After the summary block, place each source identity, execution mode, focused-read count, artifact count, validation-row count, and negative-case count in its own paragraph separated by one blank line.

Under `## 20. Repository Mutation Confirmation`, use a fenced `text` block with:

```text
Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: Yes | No
Testing Repository README Modified: No
```

The result passes only when all 24 validation rows pass, all 34 negative cases reject, the result-format validator passes, no blocking framework defect remains, and the framework repository remains unchanged.

## Next action

When verification passes with no reusable defect, state:

`Request an independent private-session run of Prompt 016 when verification passes with no reusable defect.`
