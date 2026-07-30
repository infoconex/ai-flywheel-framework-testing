# Run and Publish AI Flywheel Prompt 017

Use the GitHub repositories as the sources of truth.

Read and execute the immutable specification:

```text
Repository: Infoconex/ai-flywheel-framework-testing
Path: test/ai/prompts/017-self-host-certification.md
Commit: 759a5cf1a8cfc7c0b66f0fcc4e29ab507afd5eb5
```

## Immutable sources

```text
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Testing evidence revision: 021e10fe9577df11017f4ea1def4f83358aaed3d
Base fixture path: test/ai/tools/verify_prompt_017_fixtures.py
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Base fixture line count: 503
Transformation runner path: test/ai/tools/run_prompt_017_fixtures.py
Transformation runner commit: f91548956e6220585d0554d7d4104b993579e282
Transformation runner blob: 720109e3bb1e5c1ec9f9eafe98f0dbc76f6c6295
Transformation runner line count: 223
Self-hosting fixture commit: 5f1b69df1b5e47f0bad874cbe03238ae3860920b
Self-hosting fixture blob: 1ecc8a3adb14c09e9c804a3f2f2b70f60c0b63d0
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later commits, alternate fixtures, inferred identities, or modified source.

## Verified source retrieval

A complete-file connector response may be truncated. Retrieve each source using these inclusive UTF-8 line ranges:

```text
Base fixture: 1-175, 176-350, 351-503
Transformation runner: 1-120, 121-223
```

When a range is truncated, subdivide only that range until all requested lines are returned completely. Reject any response containing a truncation notice or omitted content.

Join adjacent chunks in line order with one LF between chunks. Do not trim or alter any returned line. Compute the Git blob SHA for the joined UTF-8 bytes and for the same bytes with one final LF. Exactly one candidate must match the pinned blob SHA. Use only the matching candidate. If no unique match exists, stop without publishing.

After both sources match their pinned blobs, perform the specification's in-memory fixture execution using the verified source strings.

The output must report:

```text
framework_revision: 18335e57165a8984adab4790d3a6210355b484ba
evidence_revision: 021e10fe9577df11017f4ea1def4f83358aaed3d
self_host_evidence_revision: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
execution_mode: in-memory connector source with approval-ready transformation runner
correction_count: 25
result: passed
```

## Completion requirements

Do not publish until all requirements are complete:

```text
Manifest-required reads: 50/50
Testing evidence reads: 16/16
Artifact snapshots: 11
Fixture checks: 16
Negative cases: 44
Validation-result rows: 32
Required top-level sections: 22
Result-format validation: Passed
```

The correct outcome distinction is:

```text
Self-Hosting Scenario Result: Passed
Certification Status: ready-for-approval
Certification Overall Result: pending-approval
Human Approval Status: pending
Readiness Validation Result: pending
Readiness Transition Performed: No
Self-Reported Verification Result: Passed
```

Do not invent approval, mark certification approved, pass readiness, or propose a ready-for-missions state.

Write or overwrite only:

```text
test/ai/results/017-self-host-certification.md
```

Do not create alternate results or modify `test/ai/README.md`. Commit only the canonical result with message:

```text
Replace Prompt 017 verification result
```

The final response must report every pinned identity, execution mode, outcome distinction, defect counts, required counts, format result, canonical result path and commit, overwrite status, `README modified: No`, and notes.