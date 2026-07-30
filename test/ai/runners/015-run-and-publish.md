# Run and Publish AI Flywheel Prompt 015

Use the GitHub repositories as the sources of truth.

## Read the specification

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/1f8ace648e262fffbae17fb6cd441c8eeb54ffe4/test/ai/prompts/015-recover-broken-active-reference.md

The runner requirements below replace obsolete framework-revision, fixture-execution, blocked-state, and result-format details in the specification.

## Immutable sources

```text
Framework revision: 291f87fb4485a2cfaa4f1580a8157a2842d08317
Specification commit: 1f8ace648e262fffbae17fb6cd441c8eeb54ffe4
Fixture harness commit: 446f9cf6d5b59780141d09d3754d5fc8d69506b3
Fixture harness blob: 76692b26583b933ba2eb7e613c7d65840edfac2c
Result-format contract commit: 594b195c514ab434406989af4e67db927d1164d1
Format-validator commit: 891f0d240c15bed3c175639808ff3f3b77f7aab1
```

Do not substitute branch heads, later commits, alternate specifications, or modified fixture source.

## Fixture execution

Retrieve `test/ai/tools/verify_prompt_015_fixtures.py` at the pinned fixture commit and verify its blob SHA. Before execution, replace exactly one assignment:

```text
FRAMEWORK_REVISION = "eb82939f330b76cc64e813feac6b7a97d3d50e9a"
```

with:

```text
FRAMEWORK_REVISION = "291f87fb4485a2cfaa4f1580a8157a2842d08317"
```

Make no other source change. Execute the resulting source directly in memory with Python 3 using `exec`.

At the corrected revision, a non-null `active_execution` may coexist with state status `active` or `blocked`. A blocked state must retain the unresolved execution and lifecycle stage, include at least one blocker, and use retained-revision compare-and-swap.

## Completion requirements

Complete all specification requirements, including 13 focused framework reads, five complete fixture artifacts, corrected blocked-state schema validation, zero/multiple/identity-mismatch resolution states, the exact 14-heading startup report, 25 validation-result rows, all 34 negative cases, and exactly 22 numbered sections. Treat the framework repository as read-only.

Validate the completed result with `test/ai/tools/validate_result_format.py` at the pinned validator commit using section count `22`.

## Canonical result

Write or overwrite only:

```text
test/ai/results/015-recover-broken-active-reference.md
```

Do not create alternate results or modify `test/ai/README.md`. Commit only the canonical result with:

```text
Replace Prompt 015 verification result
```

## Required final response

Respond only with:

```text
Prompt: 015-recover-broken-active-reference
Framework revision tested: 291f87fb4485a2cfaa4f1580a8157a2842d08317
Detailed specification commit: 1f8ace648e262fffbae17fb6cd441c8eeb54ffe4
Fixture harness commit: 446f9cf6d5b59780141d09d3754d5fc8d69506b3
Fixture harness blob: 76692b26583b933ba2eb7e613c7d65840edfac2c
Harness execution mode: in-memory connector source with one revision replacement
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Required top-level sections: 22
Validation-result rows: 25
Negative cases reported: 34
Result path: test/ai/results/015-recover-broken-active-reference.md
Result commit: <commit SHA>
Result file overwritten: Yes
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```
