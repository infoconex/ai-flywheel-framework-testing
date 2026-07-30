# AI Flywheel Self-Hosting Certification Verification Launcher

Use this file as the authoritative entrypoint for Prompt 017.

## Detailed specification

Read and follow the immutable detailed specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/8b523d61754fa359a8b12f05a1d80a7e9223dd95/test/ai/prompts/017-self-host-certification.md

Follow every instruction except where this launcher explicitly replaces or clarifies it.

## Final immutable framework revision

```text
18335e57165a8984adab4790d3a6210355b484ba
```

Use this revision for every framework read and validation.

## Historical evidence revision

```text
aceda4a01c27abcdca96bed3319cfa987a0272b5
```

Use this revision only for the 16 historical testing evidence reads. Do not treat it as a tested framework revision.

## Immutable fixture sources

Base fixture:

```text
Commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Blob: ea34857e39da0440a5d6f4d555475c91161aac24
Path: test/ai/tools/verify_prompt_017_fixtures.py
```

Final correction runner:

```text
Commit: cf989e59d8822645cff4d3fde109f5e9e871b7e0
Blob: 74137e6d8aac5997efea75c832dfebc2cf3629d9
Path: test/ai/tools/run_prompt_017_fixtures.py
```

Self-hosting fixture definition:

```text
Commit: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
Blob: 4a14008db5ef906999e3f41570192fe3efcc378a
Path: test/ai/fixtures/017-self-host-certification.yaml
```

The final correction runner supersedes the correction-runner commit and blob stated in the detailed specification.

## Final corrected harness contract

Execute the exact base fixture and final correction runner directly in memory as directed by the detailed specification.

The output is valid only when:

```text
framework_revision: 18335e57165a8984adab4790d3a6210355b484ba
evidence_revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
self_host_evidence_revision: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
execution_mode: in-memory connector source with deterministic correction runner
correction_count: 17
result: passed
```

The final runner also requires the scenario evidence audit's `source_refs` to be order-preserving and unique. This replaces the detailed specification's obsolete `correction_count: 16` requirement.

All other expected counts remain:

```text
Artifact snapshots: 11
Fixture checks: 16
Negative cases: 44
Manifest-required reads: 50/50
Historical evidence reads: 16/16
Validation-result rows: 32
Numbered result sections: 22
```

## Expected outcome

The passing verification outcome remains:

```text
Self-Hosting Scenario Result: Passed
Certification Record Result: Failed
Readiness Validation Result: Failed
```

The certification and readiness failures are expected evidence-boundary outcomes, not a failed Prompt 017 verification.

## Result format and mutation boundary

Use the result-format contract and validator identified in the detailed specification.

Write or overwrite only:

```text
test/ai/results/017-self-host-certification.md
```

Do not modify the framework repository, durable state, detailed prompt, fixture sources, this launcher, or `test/ai/README.md` during the independent run.
