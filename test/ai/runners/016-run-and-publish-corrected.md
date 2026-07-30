# Run and Publish AI Flywheel Prompt 016 — Corrected

Use the GitHub repositories as the sources of truth.

## Read the canonical launcher

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/4288af8d3b3b722734bf5ae3179727d011a6ed89/test/ai/prompts/016-run-representative-proving-mission-launcher.md

Follow the launcher before the immutable detailed specification.

## Required immutable sources

```text
Framework revision: 1b90e6789109b6693ab0dc5d79dfb1b76cc74585
Detailed specification commit: 03e546596a6113ae9ac9543fbda1d8ea061f48c5
Fixture harness commit: 9aebe151d03d1e2728905cb697336325a67409e9
Fixture harness blob: 93708efaee0a0b3fb1b69b2a8c6133755984cc9b
Canonical launcher commit: 4288af8d3b3b722734bf5ae3179727d011a6ed89
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not use the obsolete Prompt 016 runner or the earlier hard-coded format validator.

## Execute the fixture harness

Retrieve the exact harness source through the GitHub connector and verify its blob SHA. Execute the connector-returned source directly in memory with Python 3 using `exec`. Capture the complete JSON output. PyYAML is required.

## Complete all independent reads

Before drafting or committing the result:

1. Read all 19 focused framework files at the pinned revision.
2. Read the durable active mission and active goal for context only.
3. Read every one of the 47 ordered manifest-required paths at the pinned revision.
4. Retain exact path and successful connector-resolution evidence for each required target.
5. Record missing, duplicate, case-collision, unreadable, or identity anomalies.

The harness inventory and manifest list do not prove that a target was independently resolved. Do not publish with partial counts such as `5/19` or fewer than `47/47` required targets.

If connector batching is needed, perform as many connector calls as required. Do not stop early because the read set is large.

## Complete verification

Follow every launcher and detailed-specification requirement, including:

- Exact ordered manifest-to-fixture equality.
- Schema-valid synthetic mission and goal.
- Stable mission, goal, and execution identity.
- Useful read-only inventory outcome.
- All eight lifecycle stages in canonical order.
- Independent validation of AC-960, AC-961, and AC-962.
- Proposed persistence and reuse without claiming durable writes.
- Exactly 24 validation-result rows.
- All 34 negative cases rejected.
- Exactly 22 numbered level-two sections.
- No framework repository mutation.

## Format validation

Retrieve `test/ai/tools/validate_result_format.py` at commit:

```text
f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Run it against the completed result with section count `22`. It must report success and identify mutation section `20`.

## Canonical result

Write only:

```text
test/ai/results/016-run-representative-proving-mission.md
```

The failed canonical result already exists. Overwrite it in place. Do not create a rerun, dated, suffixed, backup, or history result. Do not modify `test/ai/README.md`.

Commit only the overwritten canonical result with:

```text
Replace Prompt 016 verification result
```

## Required final response

Respond with only:

```text
Prompt: 016-run-representative-proving-mission
Framework revision tested: 1b90e6789109b6693ab0dc5d79dfb1b76cc74585
Detailed specification commit: 03e546596a6113ae9ac9543fbda1d8ea061f48c5
Fixture harness commit: 9aebe151d03d1e2728905cb697336325a67409e9
Fixture harness blob: 93708efaee0a0b3fb1b69b2a8c6133755984cc9b
Harness execution mode: in-memory connector source
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Focused framework reads: 19/19
Manifest-required path reads: 47/47
Required top-level sections: 22
Validation-result rows: 24
Negative cases reported: 34
Result-format validation: Passed | Failed
Result path: test/ai/results/016-run-representative-proving-mission.md
Result commit: <commit SHA>
Result file overwritten: Yes
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the full result into the final chat response.
