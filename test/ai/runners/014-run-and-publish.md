# Run and Publish AI Flywheel Prompt 014

Use the GitHub repositories as the sources of truth.

# Read the Canonical Prompt

Read and execute the exact Prompt 014 launcher at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/aead473368cd2f7243ba473af08d9656d21950a2/test/ai/prompts/014-recover-missing-required-artifact-launcher.md

Do not use a copied, summarized, cached, or previously generated version.

The launcher directs you to the immutable detailed specification and applies the corrected fixture-harness requirements. Follow the launcher before following the detailed specification.

# Required Source Revisions

Use exactly:

```text
Framework revision: 923c46baf8d4bb400eef71a3507e07d797dcab87
Detailed specification commit: 087c97c6f95ce36555a5c77aff95eeb16e19c8d3
Fixture harness commit: e5f47e50b092a44858bf5a1daea22cfcc85f8c94
Fixture harness blob: d264dcce92e5e06ee06801eb15d3e1f8a64a1843
Canonical launcher commit: aead473368cd2f7243ba473af08d9656d21950a2
Result-format contract commit: 594b195c514ab434406989af4e67db927d1164d1
Format-validator commit: 891f0d240c15bed3c175639808ff3f3b77f7aab1
```

Do not substitute a branch head, newer framework revision, alternate prompt, or modified fixture source.

# Execute the Fixture Harness

Retrieve the exact harness source through the GitHub connector and verify its Git blob SHA equals `d264dcce92e5e06ee06801eb15d3e1f8a64a1843`.

Execute the source directly in memory with Python 3 using `exec`. Capture the complete JSON output. PyYAML is required. Do not require Python network access or connector-to-filesystem materialization.

# Complete Prompt 014 Verification

Follow every instruction in the launcher and detailed specification. In particular:

1. Read all 12 focused framework files from the pinned revision.
2. Resolve the active mission and goal for context.
3. Validate the complete fixture manifest against `manifest.schema.yaml`.
4. Validate the retained and optional blocked states against `state.schema.yaml`.
5. Validate the startup-failure record against `startup-failure.schema.yaml`.
6. Represent only `approval-validation.yaml` as absent in the isolated fixture.
7. Prove the required failed, pending, and not-applicable startup validation states.
8. Prove no execution creation, resume, target-repository inspection, invention, or unauthorized substitution occurs.
9. Produce the exact 14-heading startup report.
10. Prove create-only startup-failure persistence and optional blocked-state behavior.
11. Reject all 30 negative cases deterministically.
12. Produce exactly 22 numbered top-level sections and 24 validation-result rows.
13. Preserve the exact summary, mutation-confirmation, and final-action values.

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not repair defects during the independent run; report them.

# Canonical Result Formatting

Read and follow:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/594b195c514ab434406989af4e67db927d1164d1/test/ai/RESULT_FORMAT.md

The formatting contract is mandatory. Before committing, verify:

- One level-one Prompt 014 document title.
- All 22 numbered sections use level-two headings.
- Verification Summary is inside a fenced `text` block.
- Each summary metadata item is its own paragraph separated by one blank line.
- Complete synthetic artifacts use fenced `yaml` blocks.
- Repository Mutation Confirmation is inside a fenced `text` block.

Run the format validator from commit `891f0d240c15bed3c175639808ff3f3b77f7aab1` against the completed result with expected section count `22`. A formatting-validator failure makes the result incomplete even when substantive evidence passes.

# Overwrite the Canonical Result

Write only:

```text
test/ai/results/014-recover-missing-required-artifact.md
```

Overwrite it in place. Do not create another result or modify `test/ai/README.md`.

Commit only the result with:

```text
Replace Prompt 014 verification result
```

# Required Final Response

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

Do not paste the complete result into the final chat response.
