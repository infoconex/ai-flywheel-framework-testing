# AI Flywheel Self-Hosting Certification Execution Launcher

Use this file as the authoritative entrypoint for Prompt 017.

## Detailed specification

Read and execute the immutable detailed specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/8b523d61754fa359a8b12f05a1d80a7e9223dd95/test/ai/prompts/017-self-host-certification.md

Follow every instruction except where this launcher explicitly replaces or clarifies it.

## Immutable sources

```text
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Historical evidence revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Correction runner commit: cf989e59d8822645cff4d3fde109f5e9e871b7e0
Correction runner blob: 74137e6d8aac5997efea75c832dfebc2cf3629d9
Self-hosting fixture commit: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
Self-hosting fixture blob: 4a14008db5ef906999e3f41570192fe3efcc378a
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later commits, alternate fixtures, inferred revisions, or modified source.

## Authorized connector-to-runtime transfer

The GitHub connector and Python runtime may be separate environments. The following transfer is explicitly authorized and is not manual reconstruction:

1. Retrieve each fixture file through the GitHub connector as UTF-8 text.
2. Use the exact connector-returned `content` value as the corresponding Python string, preserving every character and line ending.
3. Do not edit, normalize, summarize, reformat, regenerate, or manually retype the source.
4. Before executing either string, recompute its Git blob SHA in Python using:

```python
import hashlib


def git_blob_sha(source: str) -> str:
    raw = source.encode("utf-8")
    return hashlib.sha1(f"blob {len(raw)}\0".encode("utf-8") + raw).hexdigest()
```

5. Require:

```text
git_blob_sha(base_source) == ea34857e39da0440a5d6f4d555475c91161aac24
git_blob_sha(runner_source) == 74137e6d8aac5997efea75c832dfebc2cf3629d9
```

6. If either digest differs, stop without executing or publishing.

This authorized transfer does not permit downloading from Python, writing temporary files, mounting connector files, editing source, reconstructing omitted text, or executing a truncated connector response. If the complete connector `content` is not available, continue retrieving it through connector-supported full-file or blob reads until the exact complete source is available.

## In-memory execution

After both source digests match, execute:

```python
runner_namespace = {"__name__": "prompt_017_runner"}
exec(compile(runner_source, "run_prompt_017_fixtures.py", "exec"), runner_namespace)
fixture_output = runner_namespace["run"](base_source)
```

The corrected output must identify:

```text
framework_revision: 18335e57165a8984adab4790d3a6210355b484ba
evidence_revision: aceda4a01c27abcdca96bed3319cfa987a0272b5
self_host_evidence_revision: 42461bcc86ea75c3752082b33d7c24dd18a8bd62
execution_mode: in-memory connector source with deterministic correction runner
correction_count: 17
result: passed
```

## Required completion boundary

Do not publish until all requirements in the detailed specification are complete, including:

- Framework manifest resolution `50/50`.
- Historical evidence reads `16/16`.
- Eleven complete snapshots.
- Sixteen true fixture checks.
- Forty-four true negative cases.
- Thirty-two validation-result rows.
- Twenty-two numbered result sections.
- Result-format validation passed.

Do not publish a partial result merely because connector batching is incomplete.

## Expected outcome distinction

The correct passing verification reports:

```text
Self-Hosting Scenario Result: Passed
Certification Record Result: Failed
Readiness Validation Result: Failed
```

The certification and readiness failures are expected safe outcomes caused by missing exact tested framework revisions in retained Prompt 001 and Prompt 002 evidence. Do not infer those revisions, treat the expected failures as framework defects, approve certification, or advance readiness.

## Repository boundaries

Treat `Infoconex/ai-flywheel-framework` as read-only. Do not modify framework files, branch state, durable operating records, or lifecycle state. Do not modify `test/ai/README.md` during the independent run.

Write only the canonical result:

```text
test/ai/results/017-self-host-certification.md
```

Commit only that result with:

```text
Replace Prompt 017 verification result
```
