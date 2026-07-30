# AI Flywheel Broken Active Reference Recovery Verification

## Purpose

Verify that a fresh operator deterministically stops when durable state points to a missing active execution, preserves exact reference evidence, does not guess or select a replacement, does not create or resume work, and can construct a valid startup-failure record and safe optional blocked-state update.

# Repository and immutable sources

Repository: `Infoconex/ai-flywheel-framework`

Framework revision: `eb82939f330b76cc64e813feac6b7a97d3d50e9a`

Fixture harness commit: `446f9cf6d5b59780141d09d3754d5fc8d69506b3`

Fixture harness blob: `76692b26583b933ba2eb7e613c7d65840edfac2c`

Read the harness at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/446f9cf6d5b59780141d09d3754d5fc8d69506b3/test/ai/tools/verify_prompt_015_fixtures.py

Retrieve it through the GitHub connector, verify the exact blob SHA, and execute the exact source in memory with Python 3 using `exec`. PyYAML is required. Do not require Python network access or connector-to-filesystem materialization.

The harness passes only when its JSON reports the pinned framework revision, `result: passed`, five complete artifact snapshots, every check true, every harness negative case true, classification `broken active execution reference`, Operating Validation failed, Repository Validation pending, Implementation Validation not-applicable, and no execution, inspection, or candidate selection.

# Authorization

This prompt authorizes synthetic, read-only verification only. Do not modify the framework repository, state, records, branch, or lifecycle. Do not create or resume an execution. Do not inspect application-repository content. All broken-reference states and writes are hypothetical in-memory fixtures.

Label every displayed synthetic artifact:

> **PROPOSED ONLY — NOT WRITTEN**

# Focused resolution

Read these 13 files at the pinned revision:

1. `.flywheel/manifest.yaml`
2. `.flywheel/state.yaml`
3. `.flywheel/operating-model/guidance/startup.md`
4. `.flywheel/operating-model/guidance/startup-failure.md`
5. `.flywheel/operating-model/guidance/broken-reference-recovery.md`
6. `.flywheel/operating-model/guidance/failure-handling.md`
7. `.flywheel/operating-model/guidance/operator.md`
8. `.flywheel/operating-model/guidance/records.md`
9. `.flywheel/operating-model/guidance/certification.md`
10. `.flywheel/operating-model/config/validation.yaml`
11. `.flywheel/operating-model/schemas/state.schema.yaml`
12. `.flywheel/operating-model/schemas/execution.schema.yaml`
13. `.flywheel/operating-model/schemas/startup-failure.schema.yaml`

Also resolve the active mission and active goal for context. Read no application-repository content. Report `13/13` focused resolution.

# Primary zero-cardinality fixture

Use the harness retained state. It points to:

`EX-20260730T050000Z-001`

Expected canonical path:

`.flywheel/operations/records/establish-ai-flywheel-operations/001-discover-repository-and-gather-context/executions/EX-20260730T050000Z-001.yaml`

Represent the canonical lookup as cardinality `zero`. Prove the state itself is schema-valid, the execution path is absent in the isolated representation, and no alternate candidate is selected.

Required classification:

```text
Failure Classification: broken active execution reference
Failed Rules: STARTUP-REFERENCE-RESOLUTION-001, STARTUP-REFERENCE-BOUNDARY-001, STARTUP-REFERENCE-EVIDENCE-001
Operating Validation: failed
Repository Validation: pending
Implementation Validation: not-applicable
Execution Decision: no execution created or resumed
Target Repository Inspection: not performed
Candidate Selection: prohibited
```

Deterministic recovery action:

`Restore the exact referenced artifact at its canonical path from an authorized, reviewed revision or obtain an authorized reconciliation that updates the source reference, then restart startup validation from the manifest.`

# Required opening report

Produce the 14 headings from `startup.md` in exact order. Identify the broken `state.active_execution` reference and expected canonical path under Known Blockers. Active Execution must be reported as referenced but unresolved, not resumed. Lifecycle Stage must remain the observed `execute` value while explaining it cannot be trusted for work until the execution resolves. Use the exact recovery action as Next Authorized Action.

# Structured startup-failure record

Use `SF-20260730T050500Z-001` at:

`.flywheel/operations/records/startup-failures/SF-20260730T050500Z-001.yaml`

Validate the complete harness record against `startup-failure.schema.yaml` and `broken-reference-recovery.md`. The `reference_failure` payload must include the exact source path and field, reference type, referenced ID, expected canonical path, cardinality `zero`, empty candidate and mismatch lists, and `selection_prohibited: true`.

Prove create-only absence check, exact write, re-read verification, immutable history, and that persistence is evidence rather than reconciliation.

# Optional blocked-state update

Validate the harness blocked state. It may be proposed only through retained-revision CAS. It must preserve active mission, goal, execution, and lifecycle stage exactly, set status blocked, add a blocker naming the startup-failure record and broken field, and not rewrite the broken reference. If state cannot remain schema-valid or CAS is unprovable, leave it unchanged.

# Alternate deterministic reference failures

Validate separately:

1. `multiple`: two observed candidate paths, including a case-only/noncanonical collision; selection remains prohibited.
2. `one` with identity mismatch: one canonical candidate exists but its internal ID or reciprocal context disagrees; identity mismatch evidence is nonempty and startup remains failed.
3. Missing active mission.
4. Missing active goal.
5. Active-stage record reference missing.

Do not combine these repository states.

# Negative validation

Report and deterministically reject all 34 cases:

1. Missing `reference_failure` for reference-resolution failure.
2. Missing source artifact path.
3. Missing source field.
4. Missing reference type.
5. Missing referenced ID.
6. Missing expected canonical path.
7. Invalid cardinality.
8. `selection_prohibited: false`.
9. Cardinality zero with a candidate.
10. Cardinality zero with identity mismatch.
11. Cardinality multiple with fewer than two candidates.
12. Cardinality one with no candidate.
13. Cardinality one with no identity mismatch.
14. Non-repository-root-relative source path.
15. Non-repository-root-relative expected path.
16. Wrong source field reported.
17. Wrong referenced ID reported.
18. Wrong expected canonical path reported.
19. State schema invalidity ignored.
20. Missing execution treated as first-execution absence.
21. Most recent execution selected.
22. Filename-similar execution selected.
23. Chat history used to select candidate.
24. Case-colliding candidate preferred automatically.
25. Execution created after detection.
26. Missing execution resumed.
27. Target repository inspected.
28. Broken reference silently cleared.
29. Broken reference silently rewritten.
30. Optional blocked state changes active reference.
31. Optional blocked state lacks blocker.
32. State updated without retained-revision CAS.
33. Failure record written outside canonical directory or overwritten.
34. Startup reported recovered because failure evidence was persisted.

A case that cannot be rejected deterministically is a reusable framework defect.

# Validation results

Create exactly 25 rows with columns:

`Validation | Expected condition | Actual condition | Result | Enforcing source`

Rows, in order:

1. Immutable revision and focused resolution.
2. Harness source identity and execution.
3. Retained state schema validation.
4. Exact source-field reference extraction.
5. Canonical execution path derivation.
6. Zero-cardinality proof.
7. Required reference-failure classification.
8. Operating Validation failure.
9. Repository Validation pending.
10. Implementation Validation not-applicable.
11. Execution creation prohibition.
12. Execution resume prohibition.
13. Target-repository inspection prohibition.
14. Candidate-selection prohibition.
15. Opening-report heading order and values.
16. Startup-failure schema validation.
17. Structured reference-failure schema validation.
18. Broken-reference semantic validation.
19. Deterministic identity and canonical startup-failure path.
20. Create-only persistence and re-read verification.
21. Optional blocked-state validity and reference preservation.
22. Multiple-candidate alternate.
23. Identity-mismatch alternate.
24. Negative validation cases.
25. Repository immutability.

# Required output

Use exactly these 22 numbered top-level sections:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Primary Broken Active-Execution Fixture
5. Reference Resolution Evidence
6. Required Startup Classification
7. Required Opening Report
8. Execution, Inspection, and Selection Boundary
9. Structured Startup-Failure Record
10. Startup-Failure Schema Validation
11. Broken-Reference Semantic Validation
12. Startup-Failure Persistence Boundary
13. Optional Blocked-State Update
14. Alternate Deterministic Reference Failures
15. Recovery and Restart Boundary
16. Next Authorized Action
17. Acceptance-Criterion Evidence Mapping
18. Validation Results
19. Negative Validation Results
20. Framework Defects
21. Repository Mutation Confirmation
22. Next Test Action

Summary field order:

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

`Operating Validation: Passed` means the framework correctly detected and handled the intentionally invalid fixture; the fixture's own startup Operating Validation is failed.

Mutation confirmation:

```text
Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: Yes | No
Testing Repository README Modified: No
```

When no framework defects are found, state:

> No reusable framework defects were found during broken active reference recovery verification.

Final next action must be one of:

- Request an independent private-session run of Prompt 015 when verification passes with no reusable defect.
- Correct the reusable framework defect on the framework testing branch, pin the prompt to the corrected immutable commit, and rerun Prompt 015.
- Correct only the prompt or synthetic fixture when the framework is sufficient, then rerun Prompt 015.

Prompt 015 passes only when the harness passes, all focused reads complete, all five artifacts validate under applicable schemas and semantics, all 34 negative cases reject, all 25 validation rows pass, and the framework repository remains unchanged.