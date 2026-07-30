# Run and Publish AI Flywheel Prompt 015

Use the GitHub repositories as the sources of truth.

# Read the canonical prompt

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/1f8ace648e262fffbae17fb6cd441c8eeb54ffe4/test/ai/prompts/015-recover-broken-active-reference.md

Do not use a copied, summarized, cached, or earlier version.

# Required immutable sources

```text
Framework revision: eb82939f330b76cc64e813feac6b7a97d3d50e9a
Prompt commit: 1f8ace648e262fffbae17fb6cd441c8eeb54ffe4
Fixture harness commit: 446f9cf6d5b59780141d09d3754d5fc8d69506b3
Fixture harness blob: 76692b26583b933ba2eb7e613c7d65840edfac2c
```

Do not substitute branch heads, newer revisions, alternate prompts, or modified fixture source.

# Execute the harness

Retrieve the exact harness source through the GitHub connector, verify its blob SHA, and execute the source directly in memory with Python 3 using `exec`. Capture the complete JSON output. PyYAML is required. Do not require Python network access or connector-to-filesystem materialization.

# Complete verification

Follow every prompt instruction. In particular:

1. Read all 13 focused files at the pinned framework revision.
2. Resolve active mission and goal context.
3. Validate all five harness artifacts against applicable schemas and semantic rules.
4. Prove the schema-valid retained state points to a missing active execution.
5. Derive the exact canonical execution path.
6. Prove zero-cardinality resolution without selecting a candidate.
7. Produce the exact 14-heading startup report.
8. Validate the structured startup-failure record.
9. Prove no execution creation, resume, application inspection, or reference rewrite occurs.
10. Validate the optional blocked state only under retained-revision CAS.
11. Evaluate multiple-candidate and identity-mismatch states separately.
12. Evaluate missing mission, goal, and active-stage references.
13. Reject all 34 negative cases deterministically.
14. Produce exactly 22 top-level sections and 25 validation rows.
15. Preserve the exact summary, mutation confirmation, and final-action forms.

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not repair defects during the independent run; report them.

# Canonical result

Write only:

```text
test/ai/results/015-recover-broken-active-reference.md
```

If it exists, overwrite it. Do not create rerun, dated, suffixed, backup, or history results. Do not modify `test/ai/README.md`.

Commit only the canonical result with:

```text
Replace Prompt 015 verification result
```

# Required final response

Respond with only:

```text
Prompt: 015-recover-broken-active-reference
Framework revision tested: eb82939f330b76cc64e813feac6b7a97d3d50e9a
Prompt commit: 1f8ace648e262fffbae17fb6cd441c8eeb54ffe4
Fixture harness commit: 446f9cf6d5b59780141d09d3754d5fc8d69506b3
Fixture harness blob: 76692b26583b933ba2eb7e613c7d65840edfac2c
Harness execution mode: in-memory connector source
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Required top-level sections: 22
Validation-result rows: 25
Negative cases reported: 34
Result path: test/ai/results/015-recover-broken-active-reference.md
Result commit: <commit SHA>
Result file overwritten: Yes | No
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the full result into the final chat response.