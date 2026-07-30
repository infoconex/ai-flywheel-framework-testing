# Run and Publish AI Flywheel Prompt 015 — Corrected Revision

Use the GitHub repositories as the sources of truth.

Read and execute the canonical launcher at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/d9a8ba167f4e9d3bb0d5c975ce1a8f1271cadcc7/test/ai/prompts/015-recover-broken-active-reference-launcher.md

Use exactly these immutable sources:

```text
Framework revision: 291f87fb4485a2cfaa4f1580a8157a2842d08317
Detailed specification commit: 1f8ace648e262fffbae17fb6cd441c8eeb54ffe4
Fixture harness commit: 446f9cf6d5b59780141d09d3754d5fc8d69506b3
Fixture harness blob: 76692b26583b933ba2eb7e613c7d65840edfac2c
Canonical launcher commit: d9a8ba167f4e9d3bb0d5c975ce1a8f1271cadcc7
```

Retrieve the exact harness source through the GitHub connector and verify its blob SHA. Apply exactly the one framework-revision replacement required by the launcher, then run the resulting source in memory with Python 3. Make no other source changes.

Complete every requirement from the launcher and detailed specification, including:

- 13 focused framework reads at the corrected revision.
- Five complete fixture artifacts.
- Schema validation of the corrected optional blocked state.
- Zero, multiple, and identity-mismatch resolution states.
- Exact 14-heading startup report.
- 34 deterministic negative cases.
- 25 validation-result rows.
- Exactly 22 top-level sections.
- No framework repository mutation.

Write only:

```text
test/ai/results/015-recover-broken-active-reference.md
```

Overwrite the existing canonical result. Do not create another result file and do not modify `test/ai/README.md`.

Commit only the result with:

```text
Replace Prompt 015 verification result
```

Return only:

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
