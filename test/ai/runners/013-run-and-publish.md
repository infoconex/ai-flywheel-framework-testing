# Run and Publish AI Flywheel Prompt 013

Use the GitHub repositories as the sources of truth.

# Read the Canonical Prompt

Read and execute the exact Prompt 013 launcher at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/0688c4de5453ace310929176a8eebfa5d0fe203b/test/ai/prompts/013-enforce-approval-boundary.md

Do not use a copied, summarized, cached, or previously generated version.

The launcher directs you to the immutable detailed specification and applies the final framework, harness, schema-routing, and evidence-durability corrections. Follow the launcher before following the detailed specification.

# Required Source Revisions

The test must use:

```text
Framework revision: 7d18c1dacf02f341f0c464571bc2f99e78a4b4de
Detailed specification commit: d8d8e8e3af3e8f3ea448f318f7746f04f20065e3
Base fixture harness commit: 2fd99b86df229890f8eb53152ea825906c658fe7
Fixture runner commit: fffc5874dc0cd4df7e6b833574eb9a9ba4ba6ea6
Canonical launcher commit: 0688c4de5453ace310929176a8eebfa5d0fe203b
```

Do not substitute a branch head, later framework commit, alternate prompt, or modified harness.

# Execute the Fixture Harness

Retrieve these two files into the same temporary directory without changing their filenames:

```text
verify_prompt_013_fixtures.py
run_prompt_013_fixtures.py
```

Execute:

```text
python run_prompt_013_fixtures.py
```

PyYAML is required. The harness performs no network access and no repository writes.

Capture its complete JSON output. The harness run is valid only when every condition in the canonical Prompt 013 launcher passes.

Do not manually substitute, approximate, or invent fixture YAML, hashes, Git blob SHAs, byte counts, timestamps, or record identities.

# Complete Prompt 013 Verification

Follow every instruction in the canonical launcher and detailed specification.

In particular:

1. Read all 20 focused framework files from the pinned revision.
2. Resolve the durable active mission and goal for context.
3. Validate all 11 generated artifacts against the applicable pinned schemas.
4. Route new approval records only to `approval-record.schema.yaml`.
5. Route evidence, decision, and finding records to `record.schema.yaml`.
6. Apply the approval semantic rules after schema validation.
7. Prove the action remains blocked before durable approval.
8. Prove chat direction and a decision record do not replace durable approval.
9. Prove the exact owner approval is valid only after its persistence plan is applied and verified.
10. Prove the fresh-session exact-scope authorization result.
11. Evaluate the delegated-authority alternate.
12. Evaluate revocation and supersession as separate repository states.
13. Evaluate the allowed-action and finding-and-approval controls.
14. Reject all 46 negative fixtures deterministically.
15. Produce exactly the required 22 top-level sections.
16. Produce exactly the required 29 validation-result rows.
17. Preserve the exact required summary, mutation confirmation, and final-action forms.

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not modify its branch, files, durable state, records, plans, schemas, or lifecycle.

Do not repair a framework, prompt, or fixture defect during the independent run. Report the defect in the result.

# Overwrite the Canonical Result

Write the complete result to:

```text
test/ai/results/013-enforce-approval-boundary.md
```

This is the only retained Prompt 013 result path.

When the file already exists, overwrite it in place.

Do not:

- Create a rerun result.
- Add a date, suffix, counter, revision, or alternate filename.
- Retain an additional result-history file.
- Create a second Prompt 013 result.
- Modify `test/ai/README.md`.

Commit only the canonical result file with this focused commit message:

```text
Replace Prompt 013 verification result
```

# Required Final Response

After committing the canonical result, respond with only:

```text
Prompt: 013-enforce-approval-boundary
Framework revision tested: 7d18c1dacf02f341f0c464571bc2f99e78a4b4de
Detailed specification commit: d8d8e8e3af3e8f3ea448f318f7746f04f20065e3
Base fixture harness commit: 2fd99b86df229890f8eb53152ea825906c658fe7
Fixture runner commit: fffc5874dc0cd4df7e6b833574eb9a9ba4ba6ea6
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Required top-level sections: 22
Validation-result rows: 29
Negative cases reported: 46
Result path: test/ai/results/013-enforce-approval-boundary.md
Result commit: <commit SHA>
Result file overwritten: Yes
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the complete result into the final chat response. The committed canonical result file is the review evidence.
