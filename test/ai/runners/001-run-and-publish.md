# Run and Publish AI Flywheel Prompt 001

Use the GitHub repositories as the sources of truth.

## Immutable Sources

```text
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Prompt 001 specification commit: 1be65ed223e6d2d3327bd4c12c84e1704795076c
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Read and execute exactly:

```text
test/ai/prompts/001-startup-validation.md
```

from the pinned specification commit above.

Do not substitute branch heads, later commits, cached content, earlier prompt versions, or inferred revisions.

## Required Execution

1. Treat the framework revision as read-only.
2. Read `.flywheel/manifest.yaml` first.
3. Follow the pinned framework's startup entrypoint exactly.
4. Read all 50 manifest-required files in exact manifest order.
5. Read the durable active mission and active goal.
6. Read applicable active-goal records from canonical locations.
7. Confirm `active_execution: null` and determine the required execution decision.
8. Validate all applicable YAML artifacts and cross-artifact invariants.
9. Produce the exact 14-heading opening report required by the framework.
10. Stop before execution creation or repository inspection.

Do not publish until these values are established:

```text
Manifest-required reads: 50/50
Required opening-report headings: 14/14
Required numbered result sections: 8
Result-format validation: Passed
```

## Result Formatting

Use `test/ai/RESULT_FORMAT.md` from the pinned format-contract commit.

Run `test/ai/tools/validate_result_format.py` from the pinned validator commit against the completed result with expected section count `8`.

The result cannot pass unless the validator reports success.

## Repository Boundaries

Do not modify the framework repository, durable operating artifacts, or `test/ai/README.md`.

Write or overwrite only:

```text
test/ai/results/001-startup-validation.md
```

Do not create a dated, suffixed, rerun, backup, alternate, or history result.

Commit only the canonical result with:

```text
Replace Prompt 001 verification result
```

## Required Final Response

After committing, respond with only:

```text
Prompt: 001-startup-validation
Framework revision tested: 18335e57165a8984adab4790d3a6210355b484ba
Prompt specification commit: 1be65ed223e6d2d3327bd4c12c84e1704795076c
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Manifest-required reads: 50/50
Required opening-report headings: 14/14
Required top-level sections: 8
Result-format validation: Passed | Failed
Result path: test/ai/results/001-startup-validation.md
Result commit: <commit SHA>
Result file overwritten: Yes
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the complete result into the final chat response.