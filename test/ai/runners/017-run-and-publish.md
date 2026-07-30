# Run and Publish AI Flywheel Prompt 017

Use the GitHub repositories as the sources of truth.

Read and execute the immutable specification:

`test/ai/prompts/017-self-host-certification.md` at commit `8b523d61754fa359a8b12f05a1d80a7e9223dd95`.

Use these immutable sources:

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

The exact connector-returned UTF-8 source content may be transferred verbatim into in-memory runtime strings. Before execution, recompute each Git blob SHA from the UTF-8 bytes and require exact matches. Do not edit, normalize, reconstruct, download from Python, mount, or write the fixture sources.

After both hashes match, execute the correction runner in memory and call its `run` function with the base fixture source. The corrected output must report framework revision `18335e57165a8984adab4790d3a6210355b484ba`, evidence revision `aceda4a01c27abcdca96bed3319cfa987a0272b5`, self-host evidence revision `42461bcc86ea75c3752082b33d7c24dd18a8bd62`, correction count `17`, and result `passed`.

Do not publish until manifest reads are `50/50`, historical evidence reads are `16/16`, all 11 snapshots and 16 fixture checks are complete, all 44 negative cases reject, all 32 validation rows are reported, exactly 22 numbered sections exist, and format validation passes.

The correct result distinction is:

```text
Self-Hosting Scenario Result: Passed
Certification Record Result: Failed
Readiness Validation Result: Failed
Self-Reported Verification Result: Passed
```

Write or overwrite only:

```text
test/ai/results/017-self-host-certification.md
```

Do not create alternate results or modify `test/ai/README.md`. Commit only the canonical result with message:

```text
Replace Prompt 017 verification result
```

The final response must report all pinned identities, execution mode, outcome distinction, defect counts, required counts, format result, canonical path and commit, overwrite status, and `README modified: No`.
