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
```

Do not substitute a branch head, newer framework revision, alternate prompt, or modified fixture source.

# Execute the Fixture Harness

Retrieve the exact harness source through the GitHub connector.

Verify its Git blob SHA equals:

```text
d264dcce92e5e06ee06801eb15d3e1f8a64a1843
```

Execute the source directly in memory with Python 3 using `exec`. Capture the complete JSON output.

PyYAML is required. Do not require network access from Python, do not download the harness from Python, and do not require connector-to-filesystem materialization.

The harness run is valid only when every condition in the canonical launcher passes.

# Complete Prompt 014 Verification

Follow every instruction in the launcher and detailed specification.

In particular:

1. Read all 12 focused framework files from the pinned revision.
2. Resolve the active mission and goal for context.
3. Validate the complete fixture manifest against `manifest.schema.yaml`.
4. Validate the retained and optional blocked states against `state.schema.yaml`.
5. Validate the startup-failure record against `startup-failure.schema.yaml`.
6. Represent only `approval-validation.yaml` as absent in the isolated fixture.
7. Prove Operating Validation fails while Repository Validation remains pending and Implementation Validation remains not-applicable.
8. Prove no execution is created or resumed.
9. Prove no target-repository inspection occurs.
10. Prove the missing artifact is not invented, substituted, or copied from an unapproved revision.
11. Produce the exact 14-heading startup report.
12. Prove create-only startup-failure persistence and optional blocked-state behavior.
13. Reject all 30 negative cases deterministically.
14. Produce exactly 22 top-level sections.
15. Produce exactly 24 validation-result rows.
16. Preserve the exact summary, mutation-confirmation, and final-action forms.

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not modify its files, branch, state, records, schemas, or lifecycle.

Do not repair any framework, prompt, or fixture defect during the independent run. Report it in the result.

# Overwrite the Canonical Result

Write the complete result to:

```text
test/ai/results/014-recover-missing-required-artifact.md
```

This is the only retained Prompt 014 result path. When it already exists, overwrite it in place.

Do not:

- Create a rerun result.
- Add a date, suffix, counter, revision, or alternate filename.
- Retain an additional result-history file.
- Create a second Prompt 014 result.
- Modify `test/ai/README.md`.

Commit only the canonical result file with:

```text
Replace Prompt 014 verification result
```

# Required Final Response

After committing the result, respond with only:

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
Result file overwritten: Yes | No
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the complete result into the final chat response. The committed canonical result is the review evidence.
