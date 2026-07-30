# Run and Publish AI Flywheel Prompt 002

Use the GitHub repositories as the sources of truth.

## Immutable Inputs

Use exactly:

```text
Framework repository: Infoconex/ai-flywheel-framework
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Prompt specification commit: b6b553763b4715a0a1382ddd60975d68c3faaaf3
Prompt specification path: test/ai/prompts/002-execution-creation.md
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Read and execute the exact Prompt 002 specification from its pinned commit. Do not substitute branch heads, later commits, cached copies, prior chat content, or another prompt.

Treat the framework repository as read-only.

## Required Completion Boundary

Do not publish until all of these are complete:

```text
Manifest-required reads: 50/50
Proposed execution artifacts: 1
Proposed state artifacts: 1
Negative cases: 16/16
Required numbered sections: 11
Result-format validation: Passed
Framework repository mutations: 0
```

The proposed execution and state must validate against the pinned framework schemas and semantic contracts. The execution must contain the current `evaluations` collection and structured `completion` object. The proposed persistence sequence must include create-only collision retry, retained-state compare-and-swap, final pair verification, and orphaned-execution startup-failure handling.

## Result Formatting

Follow `test/ai/RESULT_FORMAT.md` from commit `43b35bd896554793a3142ddf6f654ffdf8bec7f2`.

Before committing, retrieve and execute `test/ai/tools/validate_result_format.py` from commit `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c` against the completed result with expected section count `11`.

The result cannot pass unless the validator succeeds.

## Repository Boundary

Do not modify the framework repository, durable state, mission, goal, records, execution directory, or lifecycle.

Write only:

```text
test/ai/results/002-execution-creation.md
```

Overwrite the existing canonical result. Do not create another result file and do not modify `test/ai/README.md`.

Commit only the canonical result with:

```text
Replace Prompt 002 verification result
```

## Required Final Response

After committing, respond with only:

```text
Prompt: 002-execution-creation
Framework revision tested: 18335e57165a8984adab4790d3a6210355b484ba
Prompt specification commit: b6b553763b4715a0a1382ddd60975d68c3faaaf3
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Manifest-required reads: 50/50
Proposed execution artifacts: 1
Proposed state artifacts: 1
Negative cases reported: 16
Required top-level sections: 11
Result-format validation: Passed | Failed
Result path: test/ai/results/002-execution-creation.md
Result commit: <commit SHA>
Result file overwritten: Yes | No
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the full result into the final response.