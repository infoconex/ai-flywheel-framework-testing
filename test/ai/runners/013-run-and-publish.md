# Run and Publish AI Flywheel Prompt 013

Use the GitHub repositories as the sources of truth.

# Read the Canonical Prompt

Read and execute the exact Prompt 013 launcher at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/8b9ac773445d3295f377408986dfd5047592593b/test/ai/prompts/013-enforce-approval-boundary.md

Do not use a copied, summarized, cached, or previously generated version.

The launcher directs you to the immutable detailed specification and applies the final framework, in-memory harness, schema-routing, and evidence-durability corrections. Follow the launcher before following the detailed specification.

# Required Source Revisions

The test must use:

```text
Framework revision: 7d18c1dacf02f341f0c464571bc2f99e78a4b4de
Detailed specification commit: d8d8e8e3af3e8f3ea448f318f7746f04f20065e3
Base fixture harness commit: 2fd99b86df229890f8eb53152ea825906c658fe7
Base fixture harness blob: 30b004f49b663e062126551bb1d8958c0a226298
Canonical launcher commit: 8b9ac773445d3295f377408986dfd5047592593b
```

Do not substitute a branch head, later framework commit, alternate prompt, or modified harness.

# Execute the Fixture Harness In Memory

Read the base harness through the GitHub connector:

```text
test/ai/tools/verify_prompt_013_fixtures.py
```

at commit:

```text
2fd99b86df229890f8eb53152ea825906c658fe7
```

Do not attempt to download, mount, or materialize the source through the runtime filesystem.

Use the exact connector-returned source text directly in the Python execution environment:

1. Verify its Git blob SHA is `30b004f49b663e062126551bb1d8958c0a226298`.
2. Verify the obsolete framework-revision assignment occurs exactly once.
3. Replace only that assignment with the final framework revision.
4. Execute the resulting source in memory with `__name__ = "__main__"`.
5. Capture and parse its complete JSON output.

The canonical launcher contains the exact executable procedure.

PyYAML is required. The harness performs no network access or repository writes.

Do not manually substitute, approximate, or invent fixture YAML, hashes, Git blob SHAs, byte counts, timestamps, or record identities.

An inability to resolve `github.com` from the Python runtime is irrelevant because the GitHub connector supplies the source before Python execution.

# Complete Prompt 013 Verification

Follow every instruction in the canonical launcher and detailed specification.

In particular:

1. Read all 20 focused framework files from the pinned revision.
2. Resolve the durable active mission and goal for context.
3. Execute and validate the in-memory harness.
4. Validate all 11 generated artifacts against the applicable pinned schemas.
5. Route new approval records only to `approval-record.schema.yaml`.
6. Route evidence, decision, and finding records to `record.schema.yaml`.
7. Apply the approval semantic rules after schema validation.
8. Prove the action remains blocked before durable approval.
9. Prove chat direction and a decision record do not replace durable approval.
10. Prove the exact owner approval is valid only after its persistence plan is applied and verified.
11. Prove the fresh-session exact-scope authorization result.
12. Evaluate the delegated-authority alternate.
13. Evaluate revocation and supersession as separate repository states.
14. Evaluate the allowed-action and finding-and-approval controls.
15. Reject all 46 negative fixtures deterministically.
16. Produce exactly the required 22 top-level sections.
17. Produce exactly the required 29 validation-result rows.
18. Preserve the exact required summary, mutation confirmation, and final-action forms.

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not modify its branch, files, durable state, records, plans, schemas, or lifecycle.

Do not repair a framework, prompt, or fixture defect during the independent run. Report the defect in the result.

# Overwrite the Canonical Result

Write the complete result to:

```text
test/ai/results/013-enforce-approval-boundary.md
```

The file now exists. Overwrite it in place.

Do not:

- Create a rerun result.
- Add a date, suffix, counter, revision, or alternate filename.
- Retain an additional result-history file.
- Create a second Prompt 013 result.
- Modify `test/ai/README.md`.

Commit only the overwritten canonical result file with this focused commit message:

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
Base fixture harness blob: 30b004f49b663e062126551bb1d8958c0a226298
Harness execution mode: in-memory connector source
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