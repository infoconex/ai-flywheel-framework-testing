# Run and Publish AI Flywheel Prompt 016

Use the GitHub repositories as the sources of truth.

## Read the canonical prompt

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/03e546596a6113ae9ac9543fbda1d8ea061f48c5/test/ai/prompts/016-run-representative-proving-mission.md

Do not use a copied, summarized, cached, or earlier version.

## Required immutable sources

```text
Framework revision: 1b90e6789109b6693ab0dc5d79dfb1b76cc74585
Prompt commit: 03e546596a6113ae9ac9543fbda1d8ea061f48c5
Fixture harness commit: 9aebe151d03d1e2728905cb697336325a67409e9
Fixture harness blob: 93708efaee0a0b3fb1b69b2a8c6133755984cc9b
Result-format contract commit: 594b195c514ab434406989af4e67db927d1164d1
```

Do not substitute branch heads, later revisions, alternate prompts, or modified fixture source.

## Execute the harness

Retrieve the exact harness through the GitHub connector and verify the blob SHA. Execute the connector-returned source directly in memory with Python 3 using `exec`. Capture the complete JSON output. PyYAML is required. Do not require Python network access or connector-to-filesystem materialization.

## Complete verification

Follow every instruction in the canonical prompt. In particular:

1. Read all 19 focused framework files at the pinned revision.
2. Resolve durable mission and goal context without using them as proving-mission authorization.
3. Validate the actual manifest against its schema.
4. Compare the actual ordered `required_files` list to the harness inventory exactly.
5. Validate the synthetic mission and goal against their schemas.
6. Prove explicit proving-mission authorization.
7. Apply the eight-stage lifecycle to the representative read-only inventory work.
8. Validate AC-960, AC-961, and AC-962 independently.
9. Validate proposed persistence and reuse semantics without claiming durable writes.
10. Reject all 34 negative cases deterministically.
11. Produce exactly 24 validation-result rows.
12. Produce exactly 22 numbered level-two sections beneath one level-one title.
13. Preserve repository immutability.
14. Follow `test/ai/RESULT_FORMAT.md` exactly.

## Format validation

Before committing, retrieve and execute:

```text
test/ai/tools/validate_result_format.py
```

from commit:

```text
891f0d240c15bed3c175639808ff3f3b77f7aab1
```

Run it against the completed Prompt 016 result with expected section count `22`. The result cannot pass unless the validator reports success.

Also manually confirm:

- One level-one document title.
- All 22 numbered sections use `##` headings.
- Verification Summary is inside a fenced `text` block.
- Summary metadata items are separate paragraphs with one blank line between them.
- Complete artifacts use fenced `yaml` blocks.
- Repository Mutation Confirmation is inside a fenced `text` block.

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not repair defects during the independent run; report them.

## Canonical result

Write only:

```text
test/ai/results/016-run-representative-proving-mission.md
```

If it exists, overwrite it. Do not create rerun, dated, suffixed, backup, or history results. Do not modify `test/ai/README.md`.

Commit only the canonical result with:

```text
Replace Prompt 016 verification result
```

## Required final response

Respond with only:

```text
Prompt: 016-run-representative-proving-mission
Framework revision tested: 1b90e6789109b6693ab0dc5d79dfb1b76cc74585
Prompt commit: 03e546596a6113ae9ac9543fbda1d8ea061f48c5
Fixture harness commit: 9aebe151d03d1e2728905cb697336325a67409e9
Fixture harness blob: 93708efaee0a0b3fb1b69b2a8c6133755984cc9b
Harness execution mode: in-memory connector source
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Required top-level sections: 22
Validation-result rows: 24
Negative cases reported: 34
Result-format validation: Passed | Failed
Result path: test/ai/results/016-run-representative-proving-mission.md
Result commit: <commit SHA>
Result file overwritten: Yes | No
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the full result into the final chat response.
