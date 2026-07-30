# Run and Publish AI Flywheel Prompt 003

Use the GitHub repositories as the sources of truth.

Read and execute the immutable specification:

```text
Repository: Infoconex/ai-flywheel-framework-testing
Path: test/ai/prompts/003-execute-to-observe.md
Commit: 2eb7afc9cfe582151e82ad6660e12521444c1e27
```

Use these immutable sources:

```text
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later commits, copied specifications, cached content, inferred revisions, or alternate result formats.

Perform the specification entirely as a non-persistent in-memory verification against the pinned framework revision. Read the manifest first and all required files in order. Construct one proposed starting execution/state pair and one proposed post-transition execution/state pair. Do not mutate the framework repository.

Do not publish until all requirements are complete:

```text
Manifest-required reads: 50/50
Starting execution artifacts: 1
Starting state artifacts: 1
Proposed execution artifacts: 1
Proposed state artifacts: 1
Negative cases: 12
Required top-level sections: 11
Result-format validation: Passed
```

Write or overwrite only:

```text
test/ai/results/003-execute-to-observe.md
```

Do not create alternate results or modify `test/ai/README.md`. Commit only the canonical result with message:

```text
Replace Prompt 003 verification result
```

The final response must report the prompt name, framework revision, specification commit, result-format identities, verification result, defect counts, all required counts, format result, canonical path and commit, overwrite status, `README modified: No`, and notes.