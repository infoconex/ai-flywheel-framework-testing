# AI Flywheel Self-Hosting Certification Verification

## Purpose

Verify certification scenario 10 by using the AI Flywheel's own operating contracts to assemble, validate, classify, and govern its certification package.

The specification is reusable. The canonical runner supplies the immutable framework, evidence, fixture, tool, result-format, and validator revisions for a particular run.

## Authorization and isolation

This prompt authorizes an isolated, in-memory verification. It may read pinned framework and testing evidence, execute pinned fixture sources in memory, construct proposed operating artifacts, validate them, and publish only the canonical testing result.

It does not authorize framework mutation, durable lifecycle changes, human approval, readiness advancement, application-repository inspection, or modification of the testing README.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

## Framework resolution

1. Read `.flywheel/manifest.yaml` first at the runner-supplied framework revision.
2. Resolve every manifest path relative to the repository root.
3. Read `.flywheel/state.yaml` and all 50 `required_files` entries in manifest order.
4. Resolve the active mission and active goal for context only.
5. Treat the framework repository as read-only.

Report `50/50` manifest-required reads. A missing, duplicate, ambiguous, or unreadable required path fails verification.

## Certification evidence audit

Read these 16 canonical files at the runner-supplied testing evidence revision:

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
11. `test/ai/prompts/014-recover-missing-required-artifact.md`
12. `test/ai/results/014-recover-missing-required-artifact.md`
13. `test/ai/prompts/015-recover-broken-active-reference.md`
14. `test/ai/results/015-recover-broken-active-reference.md`
15. `test/ai/prompts/016-run-representative-proving-mission.md`
16. `test/ai/results/016-run-representative-proving-mission.md`

Report `16/16` evidence reads. For each certification scenario, preserve the distinction between:

- The immutable framework revision tested.
- The immutable testing revision containing its retained evidence.

A passed scenario requires nonempty evidence references and an exact tested framework revision. Do not infer revisions from branch names, chronology, chat history, or repository heads.

## Fixture execution

The canonical runner supplies:

- The immutable base fixture source and expected blob.
- The immutable approval-ready transformation runner and expected blob.
- The immutable self-hosting fixture definition and expected blob.
- The authorized connector-to-runtime transfer procedure.

Verify all source identities before execution. Execute entirely in memory. Do not normalize, edit, reconstruct, download from Python, mount, or write fixture source.

The harness must return:

- The runner-supplied framework revision.
- The runner-supplied testing evidence revision.
- The runner-supplied self-host fixture revision.
- The expected execution mode and correction count.
- `result: passed`.
- Exactly 11 artifact snapshots.
- Exactly 16 true fixture checks.
- Exactly 44 true negative cases.

## Required synthetic artifacts

Independently validate the returned artifacts using YAML 1.2 and JSON Schema Draft 2020-12 with format enforcement:

- One mission.
- One goal.
- One execution.
- Four evidence records.
- Two finding records.
- One decision record.
- One certification record.
- One readiness validation.
- One reuse assessment.
- One persistence plan.
- One state artifact.

Validate cross-artifact identities, references, provenance, criterion coverage, lifecycle ordering, terminal execution consistency, persistence dependencies and digests, approval boundaries, readiness boundaries, and state agreement.

## Expected outcome

All ten certification scenarios must pass with exact immutable evidence identities.

The self-hosting verification must then produce:

```text
Self-Hosting Scenario Result: Passed
Certification Status: ready-for-approval
Certification Overall Result: pending-approval
Human Approval Status: pending
Readiness Validation Result: pending
Readiness Transition Performed: No
```

This is a successful Prompt 017 result. Certification must not become `approved` or `passed` without a durable approval record and authority identity. Readiness must not pass or propose a ready-for-missions state before approved certification exists.

The synthetic execution may succeed with `completion.disposition: goal-blocked` because the certification package is complete while the goal remains blocked by human authority.

## Required validation results

Report exactly 32 validation-result rows covering, in order:

1. Framework revision and manifest resolution.
2. Contextual mission and goal resolution.
3. Testing evidence revision and 16-file resolution.
4. Prompt 001 tested-framework identity.
5. Prompt 002 tested-framework identity.
6. Self-host fixture identity.
7. Base fixture identity.
8. Transformation runner identity and correction count.
9. Harness result, snapshot count, and checks.
10. Mission schema.
11. Goal schema.
12. Execution schema.
13. Evidence-record schema.
14. Finding-record schema.
15. Decision-record schema.
16. Certification-record schema.
17. Readiness-validation schema.
18. Reuse-assessment schema.
19. Persistence-plan schema.
20. State schema.
21. Ten-scenario identity and order.
22. Scenario revision semantics.
23. Scenarios 1 and 2 evidence sufficiency.
24. Scenarios 3 through 9 evidence sufficiency.
25. Scenario 10 self-hosting result.
26. Self-hosting provenance.
27. Eight-stage lifecycle and execution consistency.
28. Acceptance-criterion evidence sufficiency.
29. Approval-ready certification state.
30. Pending readiness and authority boundary.
31. Persistence completeness, ordering, digests, and recovery semantics.
32. Negative cases, result format, and repository immutability.

Every row must pass.

## Negative validation

Enumerate all 44 harness negative cases in harness order and identify the enforcing schema or semantic rule. A negative case passes only when invalid behavior is rejected.

At minimum the cases must reject missing or duplicate scenarios, passed scenarios without evidence or tested revisions, inferred revision identities, approval invention, certification passage without approval, readiness advancement before approval, lifecycle inconsistencies, broken provenance, incomplete persistence, unplanned writes, alternate result creation, README modification, and invalid result format.

## Result format

Use the runner-supplied result-format contract and validator. Produce exactly 22 numbered top-level sections and the required machine-readable summary.

Write or overwrite only:

```text
test/ai/results/017-self-host-certification.md
```

Do not create alternate results. Commit only the canonical result. Stop after publishing and reporting the required completion summary.
