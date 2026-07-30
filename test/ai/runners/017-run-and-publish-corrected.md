# Run and Publish AI Flywheel Prompt 017 — Corrected Execution Boundary

Use the GitHub repositories as the sources of truth.

## Read the authoritative launcher

Read and execute exactly:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/7d85caab0ddcab6680fa1da21dbe9cecc576181f/test/ai/prompts/017-self-host-certification-execution-launcher.md

Do not use a copied, summarized, cached, or earlier version.

The launcher directs you to the immutable detailed specification and replaces the connector-to-runtime execution boundary. Follow the launcher before the detailed specification.

## Required immutable sources

```text
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Historical evidence revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
Detailed specification commit: 8b523d61754fa359a8b12f05a1d80a7e9223dd95
Execution launcher commit: 7d85caab0ddcab6680fa1da21dbe9cecc576181f
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Correction runner commit: cf989e59d8822645cff4d3fde109f5e9e871b7e0
Correction runner blob: 74137e6d8aac5997efea75c832dfebc2cf3629d9
Self-hosting fixture commit: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
Self-hosting fixture blob: 4a14008db5ef906999e3f41570192fe3efcc378a
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later revisions, alternate prompts, modified fixtures, or inferred historical framework revisions.

## Execute fixture source in memory

Retrieve the complete base fixture and correction runner through the GitHub connector.

The exact connector-returned UTF-8 `content` may be transferred verbatim into Python string variables. This transfer is explicitly authorized and is not manual source reconstruction.

Before execution, recompute both Git blob SHAs in Python. Do not execute unless both match the required blobs exactly.

Do not:

- Download either source from Python.
- Write or mount temporary fixture files.
- Edit, normalize, summarize, reformat, or manually recreate source.
- Execute truncated connector output.

Then execute the two exact strings with the in-memory procedure defined by the launcher.

## Complete verification

Do not publish until all requirements are complete:

```text
Manifest-required reads: 50/50
Historical evidence reads: 16/16
Artifact snapshots: 11
Fixture checks: 16
Correction count: 17
Validation-result rows: 32
Negative cases: 44
Required top-level sections: 22
Result-format validation: Passed
```

The correct outcome distinction is:

```text
Fixture Harness Result: Passed
Self-Hosting Scenario Result: Passed
Certification Record Result: Failed
Readiness Validation Result: Failed
Self-Reported Verification Result: Passed
```

Certification and readiness must fail safely because Prompt 001 and Prompt 002 do not identify exact tested framework commit SHAs. Do not infer those revisions or reinterpret the safe failures as a Prompt 017 or framework failure.

## Repository boundaries

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not modify framework files, durable state, missions, goals, executions, records, plans, schemas, or lifecycle.

Write only:

```text
test/ai/results/017-self-host-certification.md
```

When the path exists, overwrite it. Do not create dated, suffixed, rerun, backup, alternate, or history result files. Do not modify `test/ai/README.md`.

Commit only the canonical result with:

```text
Replace Prompt 017 verification result
```

## Required final response

After committing, respond with only:

```text
Prompt: 017-self-host-certification
Framework revision tested: 18335e57165a8984adab4790d3a6210355b484ba
Historical evidence revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
Detailed specification commit: 8b523d61754fa359a8b12f05a1d80a7e9223dd95
Execution launcher commit: 7d85caab0ddcab6680fa1da21dbe9cecc576181f
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Correction runner commit: cf989e59d8822645cff4d3fde109f5e9e871b7e0
Correction runner blob: 74137e6d8aac5997efea75c832dfebc2cf3629d9
Self-hosting fixture commit: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
Self-hosting fixture blob: 4a14008db5ef906999e3f41570192fe3efcc378a
Harness execution mode: verbatim connector content transferred to in-memory runtime with pre-execution Git blob verification
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
Correction count: 17
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

Do not paste the full result into the final chat response.
