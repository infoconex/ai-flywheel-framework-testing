# AI Flywheel Missing Required Artifact Recovery Verification

## Purpose

Verify that a fresh operator session deterministically stops when one manifest-required operating file is missing, does not create or resume an execution, does not inspect the target repository, does not invent or substitute the missing artifact, and can produce a valid create-only startup-failure record and optional safe blocked-state update.

# Repository

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `923c46baf8d4bb400eef71a3507e07d797dcab87`

Use this exact revision. Do not substitute a branch head or later commit.

# Fixture Harness

Read the exact immutable harness at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/af8beee6f15b8e9081afe0b2d322e4e18f04ebf0/test/ai/tools/verify_prompt_014_fixtures.py

The expected Git blob SHA is:

```text
d3d69cd4736b33779763fb8882260c381ca4cd6a
```

Retrieve the source through the GitHub connector, verify the blob SHA, and execute the exact source in memory with Python 3 using `exec`. PyYAML is required. Do not require network access from Python and do not require connector-to-filesystem materialization.

The harness run is valid only when:

- The process completes successfully.
- The JSON parses successfully.
- `framework_revision` equals the pinned framework revision.
- `result` equals `passed`.
- All four artifact entries contain complete normalized YAML, SHA-256, Git blob SHA, and byte count.
- Every harness check is true.
- Every harness negative case is true.
- `classification` is `required operating file missing`.
- `operating_validation` is `failed`.
- `repository_validation` is `pending`.
- `implementation_validation` is `not-applicable`.
- `execution_created_or_resumed` is false.
- `target_repository_inspected` is false.

# Authorization

This prompt authorizes synthetic, read-only verification only.

Do not modify the framework repository, its branch, state, records, or required files. Do not create or resume an execution. Do not inspect an application repository. Do not actually delete the required file. The missing-file condition must exist only in an isolated in-memory fixture.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

# Focused Resolution

Read these 12 files from the immutable framework revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/startup.md`
4. `.flywheel/operating-model/guidance/startup-failure.md`
5. `.flywheel/operating-model/guidance/failure-handling.md`
6. `.flywheel/operating-model/guidance/operator.md`
7. `.flywheel/operating-model/guidance/records.md`
8. `.flywheel/operating-model/guidance/certification.md`
9. `.flywheel/operating-model/config/validation.yaml`
10. `.flywheel/operating-model/schemas/manifest.schema.yaml`
11. `.flywheel/operating-model/schemas/state.schema.yaml`
12. `.flywheel/operating-model/schemas/startup-failure.schema.yaml`

Also resolve the active mission and active goal for context. Read no application-repository content.

Report the immutable SHA, `12/12` focused resolution, and contextual resolution.

# Isolated Missing-File Fixture

Use the harness-provided fixture manifest and retained state.

The exact missing path is:

```text
.flywheel/operating-model/config/approval-validation.yaml
```

Prove that:

1. The path appears in `manifest.required_files`.
2. The isolated fixture contains no file at that path.
3. Every other fixture-required artifact remains present.
4. The canonical framework revision remains untouched.
5. The missing file is not guessed, regenerated, copied, or substituted.

# Required Startup Classification

The missing required file must produce:

```text
Failure Classification: required operating file missing
Failed Rule: STARTUP-REQUIRED-FILE-001
Operating Validation: failed
Repository Validation: pending
Implementation Validation: not-applicable
Execution Decision: no execution created or resumed
Target Repository Inspection: not performed
```

The exact deterministic recovery action is:

```text
Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.
```

# Opening Report

Produce the startup opening report using the 14 required headings from `startup.md` in exact order.

The report must identify the exact missing path under `Known Blockers`, show no active execution, preserve a null lifecycle stage, report Operating Validation failed, and use the deterministic recovery action as `Next Authorized Action`.

# Startup-Failure Record

Use the harness-provided record:

```text
SF-20260730T040000Z-001
```

Canonical path:

```text
.flywheel/operations/records/startup-failures/SF-20260730T040000Z-001.yaml
```

Validate the complete record against `startup-failure.schema.yaml` and the semantic rules in `startup-failure.md`.

It must contain:

- Exact observed framework revision.
- Exact branch.
- Stable operator identity.
- Whole-second UTC timestamp.
- `STARTUP-REQUIRED-FILE-001`.
- `STARTUP-FAILURE-BOUNDARY-001`.
- Exact missing path.
- Evidence that the manifest required the path and the fixture lookup found it absent.
- The exact deterministic recovery action.
- `orphaned_execution_id: null`.

# Startup-Failure Persistence Boundary

Prove that startup-failure persistence:

- Is a startup action, not goal-directed work.
- Does not require an execution.
- Uses a deterministic `SF-...` identity.
- Uses create-only persistence at the canonical path.
- Confirms absence immediately before creation.
- Re-reads and verifies the exact record after creation.
- Does not authorize repository inspection or execution creation.
- Does not repair the missing artifact.

All writes are hypothetical and must remain in memory.

# Optional Blocked-State Update

Use the harness-provided optional blocked-state artifact.

Prove that it is permitted only when the retained state revision is current and the missing file directly prevents the active onboarding work.

The proposed blocked state must:

- Remain `not-ready-for-missions`.
- Use `status: blocked`.
- Preserve the active mission and goal.
- Keep `active_execution: null`.
- Keep `lifecycle_stage: null`.
- Keep `application_missions_allowed: false`.
- Include a blocker referencing the startup-failure record and exact missing path.
- Use retained-revision compare-and-swap.

If any state-update precondition is unprovable, the correct behavior is to leave state unchanged and still report the startup failure.

# Duplicate and Retry Behavior

Prove that:

- The startup-failure record is never overwritten.
- A create collision requires re-listing and selecting the next lowest unused counter for the same timestamp.
- Repeating the same unresolved observation does not silently mutate the prior record.
- A new record is created only for a materially new observation or changed repository revision.
- After authorized repair, startup restarts from the manifest.
- Prior startup-failure history remains immutable.

# Negative Validation

Evaluate these 30 invalid cases and identify the exact schema or semantic rule that rejects each:

1. Missing startup-failure ID.
2. Invalid startup-failure ID format.
3. Observed revision differs from the fixture revision.
4. Fractional startup timestamp.
5. Empty failed-rules list.
6. Empty artifact-path list.
7. Artifact path is not repository-root-relative and exact.
8. Empty evidence list.
9. Empty recovery action.
10. Non-null orphaned execution when no execution existed.
11. Unknown extra startup-failure field.
12. Empty operator identity.
13. Missing required file is treated as optional.
14. Operator continues Operating Validation as passed.
15. Repository Validation is reported passed.
16. Implementation Validation is reported passed.
17. Execution is created after detecting the missing file.
18. Existing execution is resumed after detecting the missing file.
19. Target repository is inspected.
20. Missing artifact content is invented.
21. Artifact is copied from an unapproved revision.
22. Different path is reported than the manifest-required path.
23. Startup-failure record is written outside the canonical directory.
24. Existing startup-failure record is overwritten.
25. Create collision is ignored or force-written.
26. Optional blocked state introduces an active execution.
27. Optional blocked state introduces a lifecycle stage.
28. Optional blocked state omits a blocker.
29. State is updated without retained-revision CAS.
30. Startup is reported recovered merely because the failure record was persisted.

A case that cannot be rejected deterministically is a reusable framework defect.

# Required Validation Results

Create a table with exactly 24 rows in this order:

1. Immutable revision and focused resolution.
2. Harness source identity and execution.
3. Fixture manifest schema validation.
4. Retained state schema validation.
5. Exact required-file membership.
6. Isolated missing-path proof.
7. Required-file failure classification.
8. Operating Validation failure state.
9. Repository Validation pending state.
10. Implementation Validation not-applicable state.
11. Execution creation prohibition.
12. Execution resume prohibition.
13. Target-repository inspection prohibition.
14. No artifact invention or substitution.
15. Opening-report heading order and values.
16. Startup-failure schema validation.
17. Startup-failure semantic validation.
18. Deterministic identity and canonical path.
19. Create-only absence check and re-read verification.
20. Optional blocked-state validity.
21. Duplicate and collision behavior.
22. Recovery action and restart boundary.
23. Negative validation cases.
24. Repository immutability.

Columns must be:

```text
Validation | Expected condition | Actual condition | Result | Enforcing source
```

# Framework Defects

Report only reusable framework defects. If none are found, state:

> No reusable framework defects were found during missing required artifact recovery verification.

# Required Output

Use exactly these 22 numbered top-level sections in this order:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Isolated Missing-File Fixture
5. Required Startup Classification
6. Required Opening Report
7. Execution and Inspection Boundary
8. Startup-Failure Record
9. Startup-Failure Schema Validation
10. Startup-Failure Semantic Validation
11. Startup-Failure Persistence Boundary
12. Optional Blocked-State Update
13. Duplicate and Collision Handling
14. Recovery and Restart Boundary
15. Alternate Deterministic States
16. Next Authorized Action
17. Acceptance-Criterion Evidence Mapping
18. Validation Results
19. Negative Validation Results
20. Framework Defects
21. Repository Mutation Confirmation
22. Next Test Action

The summary must contain this exact field order:

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

For this test, `Operating Validation: Passed` means the framework correctly detected and handled the intentionally invalid fixture. It does not mean the fixture itself was valid.

The repository mutation confirmation must contain:

```text
Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: Yes
Testing Repository README Modified: No
```

The final next test action must be one of:

- Request an independent private-session run of Prompt 014 when verification passes with no reusable defect.
- Correct the reusable framework defect on the framework testing branch, pin the prompt to the corrected immutable commit, and rerun Prompt 014.
- Correct only the prompt or synthetic fixture when the framework is sufficient, then rerun Prompt 014.

# Acceptance Rule

Prompt 014 passes only when:

- The exact harness passes.
- All 12 focused framework and context reads complete.
- The missing path is proven exact and required.
- Startup deterministically fails at the correct boundary.
- No execution or repository inspection occurs.
- The startup-failure record passes schema and semantic validation.
- Optional blocked-state behavior is safe and conditional.
- All 30 negative cases reject deterministically.
- All 24 validation rows pass.
- No framework repository mutation occurs.
