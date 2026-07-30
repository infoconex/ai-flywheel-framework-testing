# Run and Publish AI Flywheel Prompt 017

Use the GitHub repositories as the sources of truth.

## Read the canonical prompt

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/8b523d61754fa359a8b12f05a1d80a7e9223dd95/test/ai/prompts/017-self-host-certification.md

Do not use a copied, summarized, cached, or earlier version.

## Required immutable sources

```text
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Historical evidence revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
Detailed specification commit: 8b523d61754fa359a8b12f05a1d80a7e9223dd95
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Correction runner commit: 9f995a90f95ba87b1301b286a4ea2683dab1e8e3
Correction runner blob: 1106d396ab13aeb4c79451ed96c6f3e367cec657
Self-hosting fixture commit: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
Self-hosting fixture blob: 4a14008db5ef906999e3f41570192fe3efcc378a
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later commits, alternate prompts, inferred revisions, or modified fixture source.

## Required completion boundary

Do not publish a result until all of these are complete:

- Framework manifest resolution is `50/50`.
- Durable active mission and goal context resolve.
- Historical certification evidence reads are `16/16`.
- Self-hosting fixture blob matches.
- Base fixture and correction runner blobs match.
- The corrected harness executes successfully in memory.
- All 11 snapshots are complete.
- All 16 fixture checks are true.
- All 44 fixture negative cases are true.
- All individual schema validations complete.
- All cross-artifact semantic validations complete.
- Exactly 32 validation-result rows are reported.
- Exactly 44 negative cases are reported.
- Exactly 22 numbered level-two sections are produced.
- Result-format validation passes.

Do not publish a partial result because connector batching is incomplete. Continue reading until all required framework and evidence files have been resolved.

## Expected outcome distinction

The correct passing Prompt 017 result must report:

```text
Self-Hosting Scenario Result: Passed
Certification Record Result: Failed
Readiness Validation Result: Failed
```

Prompt 017 verification passes when the self-hosting process correctly detects that Prompt 001 and Prompt 002 lack exact tested framework commit SHAs, fails certification and readiness safely, creates corrective actions, and preserves the human approval and readiness boundaries.

Do not reinterpret the expected certification failure as:

- A failed Prompt 017 verification.
- A reusable framework defect.
- A current Prompt 017 fixture defect.
- Permission to infer the missing revisions.
- Permission to approve certification or change readiness.

## Fixture execution

Retrieve the base fixture and correction runner through the GitHub connector and verify both blob SHAs.

Execute both sources directly in memory:

```python
runner_namespace = {"__name__": "prompt_017_runner"}
exec(compile(runner_source, "run_prompt_017_fixtures.py", "exec"), runner_namespace)
fixture_output = runner_namespace["run"](base_source)
```

Do not download, mount, write, manually edit, or manually recreate either fixture source.

The corrected output must identify:

```text
framework_revision: 18335e57165a8984adab4790d3a6210355b484ba
evidence_revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
self_host_evidence_revision: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
execution_mode: in-memory connector source with deterministic correction runner
correction_count: 16
result: passed
```

## Result formatting

Follow `test/ai/RESULT_FORMAT.md` exactly.

Before committing, execute `test/ai/tools/validate_result_format.py` from commit `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c` against the completed result with section count `22`.

The result cannot pass unless the validator reports success.

Manually confirm:

- One level-one Prompt 017 title.
- All 22 numbered sections use `##` headings.
- Verification Summary is inside a fenced `text` block.
- Summary metadata uses separate one-line paragraphs with one blank line between them.
- Complete proposed artifacts use fenced `yaml` blocks.
- Repository Mutation Confirmation is inside a fenced `text` block.
- Validation and negative-case counts remain exact.

## Repository boundaries

Treat `Infoconex/ai-flywheel-framework` as read-only.

Do not modify:

- The framework branch or any framework file.
- Durable framework state, missions, goals, executions, records, or lifecycle.
- The detailed prompt, fixture, correction runner, format contract, or validator.
- `test/ai/README.md`.

Do not repair Prompt 001 or Prompt 002 during this run. Report the expected corrective actions only.

## Canonical result

Write only:

```text
test/ai/results/017-self-host-certification.md
```

When the path exists, overwrite it in place.

Do not create a rerun, dated, suffixed, backup, alternate, or history result.

Commit only the canonical result with:

```text
Replace Prompt 017 verification result
```

## Required final response

After committing the canonical result, respond with only:

```text
Prompt: 017-self-host-certification
Framework revision tested: 18335e57165a8984adab4790d3a6210355b484ba
Historical evidence revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
Detailed specification commit: 8b523d61754fa359a8b12f05a1d80a7e9223dd95
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Correction runner commit: 9f995a90f95ba87b1301b286a4ea2683dab1e8e3
Correction runner blob: 1106d396ab13aeb4c79451ed96c6f3e367cec657
Self-hosting fixture commit: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
Self-hosting fixture blob: 4a14008db5ef906999e3f41570192fe3efcc378a
Harness execution mode: in-memory connector source with deterministic correction runner
Fixture harness result: Passed | Failed
Self-hosting scenario result: Passed | Failed
Certification record result: Passed | Failed
Readiness validation result: Passed | Failed
Self-reported verification result: Passed | Failed
Framework defects reported: <number>
Prompt or fixture defects reported: <number>
Manifest-required reads: 50/50
Historical evidence reads: 16/16
Artifact snapshots: 11
Fixture checks: 16
Required top-level sections: 22
Validation-result rows: 32
Negative cases reported: 44
Result-format validation: Passed | Failed
Result path: test/ai/results/017-self-host-certification.md
Result commit: <commit SHA>
Result file overwritten: Yes | No
README modified: No
Notes: <one concise statement identifying anything requiring review, or None>
```

Do not paste the full result into the final chat response. The committed canonical result is the review evidence.
