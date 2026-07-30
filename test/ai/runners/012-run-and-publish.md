# Run and Publish AI Flywheel Prompt 012

Use the GitHub repositories as the sources of truth.

## 1. Read the exact test specification

Read and execute Prompt 012 from this immutable testing revision:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/4ce5952db99d7c473ad76e330353a68c47c69801/test/ai/prompts/012-recover-partial-lifecycle-transition.md

Do not use a copied, summarized, cached, or previously generated version.

The prompt pins framework revision:

```text
fdb270be55d77b2588b7d589021479c5f6e3097f
```

Do not substitute a branch head or newer framework commit.

## 2. Read and run the deterministic fixture harness

Read this exact harness from the testing repository:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/a623027035ebe50d46fc7cb140a69ebd40621228/test/ai/tools/verify_prompt_012_fixtures.py

Execute it with Python 3 in the session's code-execution environment.

The harness requires PyYAML and performs no network access or repository writes. Capture its complete JSON output.

The harness run is valid only when:

- The process exits successfully.
- The JSON parses successfully.
- `framework_revision` equals `fdb270be55d77b2588b7d589021479c5f6e3097f`.
- `result` equals `passed`.
- All ten artifact entries include complete normalized YAML, SHA-256, Git blob SHA, and byte count.
- All checks report `passed`.
- All negative cases 16 through 23 report `true`.
- The reported classification is `execution written, state not written`.
- Rollback reports `state_mutated: false` and `original_pair_restored: true`.

Do not invent, approximate, or manually substitute fixture hashes. Use the values produced by the executed harness.

The harness provides deterministic complete fixture bytes and computed identities. It does not replace reading the pinned framework files or applying the framework's actual schemas and semantic rules.

## 3. Complete Prompt 012 verification

Follow every instruction in Prompt 012.

Use the harness output as the exact source for:

- Mission and goal fixtures.
- Retained execution and state.
- Proposed execution and state.
- Applying original transition plan.
- Structured recovery finding.
- Applied recovery plan.
- Rolled-back original transition plan.
- Normalized YAML bytes.
- SHA-256 digests.
- Synthetic Git blob SHAs.

Independently verify the generated artifacts against the actual framework schemas and semantic rules at the pinned framework revision.

For cases 16 through 23, report whether the actual `record.schema.yaml` directly rejects each invalid fixture. For cases 24 through 28, report the exact semantic rule that rejects each mismatch.

Do not fail merely because exact fixtures and hashes would be difficult to construct manually. The harness exists to produce them reproducibly.

If the harness cannot be executed or its output fails its own checks, report the verification as failed because the test execution is incomplete. Do not classify that inability as a framework defect.

## 4. Preserve repository boundaries

Treat `Infoconex/ai-flywheel-framework` as read-only.

Do not modify the framework, its feature branch, durable framework state, lifecycle records, plans, findings, or schemas.

Writing the completed test result to `Infoconex/ai-flywheel-framework-testing` is a separate authorized administrative action.

## 5. Overwrite the canonical result

Write the complete result to:

```text
test/ai/results/012-recover-partial-lifecycle-transition.md
```

The file already exists. Overwrite it in place.

Do not:

- Create a rerun file.
- Add a suffix, date, counter, or alternate filename.
- Retain another result-history file.
- Create a second Prompt 012 result.
- Modify `test/ai/README.md`.

Commit only the overwritten canonical result file with this focused message:

```text
Replace Prompt 012 verification result
```

## 6. Required final response

After committing the result, respond with only:

```text
Prompt: 012-recover-partial-lifecycle-transition
Framework revision tested: <exact immutable framework SHA>
Fixture harness commit: a623027035ebe50d46fc7cb140a69ebd40621228
Fixture harness result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Result path: test/ai/results/012-recover-partial-lifecycle-transition.md
Result commit: <commit SHA>
Result file overwritten: Yes
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the complete result into the final response. The committed canonical result file is the review evidence.
