# Run and Publish AI Flywheel Prompt 014

Use the GitHub repositories as the sources of truth.

## Read the specification

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/087c97c6f95ce36555a5c77aff95eeb16e19c8d3/test/ai/prompts/014-recover-missing-required-artifact.md

The runner requirements below replace obsolete fixture identities or execution details in the specification.

## Immutable sources

```text
Framework revision: 923c46baf8d4bb400eef71a3507e07d797dcab87
Specification commit: 087c97c6f95ce36555a5c77aff95eeb16e19c8d3
Fixture harness commit: e5f47e50b092a44858bf5a1daea22cfcc85f8c94
Fixture harness blob: d264dcce92e5e06ee06801eb15d3e1f8a64a1843
Result-format contract commit: 594b195c514ab434406989af4e67db927d1164d1
Format-validator commit: 891f0d240c15bed3c175639808ff3f3b77f7aab1
```

Do not substitute branch heads, later commits, alternate specifications, or modified fixture source.

## Fixture corrections and execution

Retrieve `test/ai/tools/verify_prompt_014_fixtures.py` at the pinned fixture commit, verify the Git blob SHA, and execute the exact connector-returned source in memory with Python 3 using `exec`. PyYAML is required.

The authoritative fixture corrections are:

1. Use the complete pinned manifest `required_files` list.
2. Include `implementation_available: false` in retained and optional blocked states.
3. Use nonempty string blockers.
4. Represent only `.flywheel/operating-model/config/approval-validation.yaml` as absent.

The harness must parse, report the pinned framework revision and `result: passed`, provide four complete artifact snapshots, and return all checks and all 30 negative cases as true.

## Completion requirements

Complete all specification requirements, including 12 focused framework reads, active mission and goal context, schema validation, exact 14-heading startup report, 24 validation-result rows, 30 negative cases, and exactly 22 numbered sections. Treat the framework repository as read-only.

Validate the completed result with `test/ai/tools/validate_result_format.py` at the pinned validator commit using section count `22`.

## Canonical result

Write or overwrite only:

```text
test/ai/results/014-recover-missing-required-artifact.md
```

Do not create alternate results or modify `test/ai/README.md`. Commit only the canonical result with:

```text
Replace Prompt 014 verification result
```

## Required final response

Respond only with:

```text
Prompt: 014-recover-missing-required-artifact
Framework revision tested: 923c46baf8d4bb400eef71a3507e07d797dcab87
Detailed specification commit: 087c97c6f95ce36555a5c77aff95eeb16e19c8d3
Fixture harness commit: e5f47e50b092a44858bf5a1daea22cfcc85f8c94
Fixture harness blob: d264dcce92e5e06ee06801eb15d3e1f8a64a1843
Harness execution mode: in-memory connector source
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Required top-level sections: 22
Validation-result rows: 24
Negative cases reported: 30
Result path: test/ai/results/014-recover-missing-required-artifact.md
Result commit: <commit SHA>
Result file overwritten: Yes
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```
