# Run and Publish AI Flywheel Prompt 018

Use GitHub repositories as the sources of truth.

## Immutable sources

Read and execute exactly:

```text
Specification repository: Infoconex/ai-flywheel-framework-testing
Specification path: test/ai/prompts/018-programmatic-reuse-completion.md
Specification commit: 15e528ff06a7d65853f968703cf344f1ccc49a14
Framework repository: Infoconex/ai-flywheel-framework
Framework revision: c8ed28be463665cac4a1c305b02af182432c536f
Result-format contract path: test/ai/RESULT_FORMAT.md
Result-format contract commit: aab08271e3461d6eaeceda443ac0cbbceecd012f
Result-format validator path: test/ai/tools/validate_result_format.py
Result-format validator commit: aab08271e3461d6eaeceda443ac0cbbceecd012f
```

Do not substitute branch heads, later commits, cached content, copied prompts, prior results, inferred revisions, alternate files, a CLI repository, or another implementation.

The pinned framework revision is the sole governing contract. Any auxiliary code used to construct fixtures, calculate digests, or validate artifacts is an execution aid only and is not an implementation under test.

## Mandatory manifest guard

Before executing any scenario:

1. Verify the framework revision is exactly `c8ed28be463665cac4a1c305b02af182432c536f`.
2. Read `.flywheel/manifest.yaml` first.
3. Verify `required_files` contains `.flywheel/operating-model/guidance/completion.md`.
4. Read `completion.md` from the same pinned framework revision in manifest order.

If any guard fails, stop without overwriting or publishing the canonical result.

## Execution method

Perform the verification entirely in memory or in isolated temporary fixtures. Read every manifest-required file in the exact listed order.

Construct complete synthetic governed artifacts from the pinned framework schemas and operating contracts. Do not modify the framework repository or inspect an application repository.

For each rejected operation, retain and compare byte-level digests for the complete governed-file set before and after the rejection. Do not infer atomicity from a rejection message.

For each accepted proposed transaction, validate the complete proposed write set before any modeled write, record retained revisions and write ordering, verify rollback or recovery requirements, and re-read the complete final artifact set.

## Required completion

Do not publish until all requirements pass:

```text
Required scenarios: 9/9
Manifest includes completion.md: Passed
Completion guidance loaded through required_files: Passed
Generic Persist rejection atomicity: Passed
Dedicated persistence and Reuse activation: Passed
Duplicate Reuse identity rejection atomicity: Passed
Whole-set preflight cases: 3/3 rejected before write
Generic Reuse rejection atomicity: Passed
Planned assessment completion rejection atomicity: Passed
Governed completion synchronization: Passed
Structured final-goal mission evaluation: Passed
Mission-objective approval blocking: Passed
External-follow-on approval non-blocking: Passed
Completed mission structure validation: Passed
Complete repository validation: Passed
Unresolved references: 0
Required top-level sections: 15/15
Result-format validation: Passed
Framework repository changes: None
```

A passing result must explicitly verify:

- dedicated persistence atomicity and durability requirements;
- completed reuse-assessment requirements;
- synchronization of execution, goal, mission, and state;
- behavior when the completed goal is the final mission goal;
- structured mission criterion evidence, blockers, and approval evaluation;
- that a pending mission-objective approval prevents mission completion;
- that approval for external work outside the mission objective does not keep an otherwise complete mission active; and
- that a completed mission without a complete and internally consistent completion structure is rejected.

Report every reusable framework defect or ambiguity. Do not compare the framework to the Python CLI or any other implementation.

When none remain, state exactly:

> No reusable framework defects were found during the non-persistent programmatic Reuse-completion verification.

## Publication boundary

Write or overwrite only:

```text
test/ai/results/018-programmatic-reuse-completion.md
```

Do not create, switch, merge, or delete branches. Use the currently checked-out `main` branch. Do not create alternate results, modify README files, modify Prompt 018, or modify the framework repository.

Commit only the canonical result with message:

```text
Replace Prompt 018 verification result
```

Do not merge a pull request, tag, publish, create a release, upload artifacts, or enable hosted automation.

The final response must report the final verdict, every pinned identity, manifest guard result, execution method, scenario and atomicity results, final artifact state, structured mission completion values, repository validation, framework defects, canonical path, overwrite status, result commit SHA, commit message, `README modified: No`, and framework mutation status.