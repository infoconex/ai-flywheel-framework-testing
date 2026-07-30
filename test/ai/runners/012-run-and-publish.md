# Run and Publish AI Flywheel Prompt 012

Use GitHub repositories as the sources of truth.

Read and execute exactly:

```text
Repository: Infoconex/ai-flywheel-framework-testing
Path: test/ai/prompts/012-recover-partial-lifecycle-transition.md
Specification commit: 5468a1597a837472bd3400793cd12d82fe0d2c45
Framework repository: Infoconex/ai-flywheel-framework
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Fixture harness path: test/ai/tools/verify_prompt_012_fixtures.py
Fixture harness commit: c024651d109eff3a893b5fa1b40bfa1cf832a03a
Fixture harness blob: 6f2e0b840afbc1c1098b29cf1d0c3cb8b3e5a329
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, newer commits, copied prompts, cached content, obsolete fixture instructions, or prior results.

Read the fixture harness through the GitHub connector at the exact commit and verify its blob identity. Execute the retrieved source directly in the Python runtime without writing it to disk. The run is valid only when the process exits successfully, the JSON parses, `framework_revision` equals the pinned framework revision, `result` equals `passed`, every check is `passed`, all fixture negative cases are true, and the reported partial-state classification is `execution written, state not written`.

The completed verification must report:

```text
Fixture harness result: Passed
Manifest-required reads: 50/50
Partial execution artifacts: 1
Partial state artifacts: 1
Transition plans: 1
Proposed recovery execution artifacts: 1
Proposed recovery state artifacts: 1
Recovery findings: 1
Negative cases: 24/24
Required top-level sections: 15/15
Result-format validation: Passed
```

A failed fixture harness makes the verification result failed and must not be reported as Passed.

Write or overwrite only `test/ai/results/012-recover-partial-lifecycle-transition.md`. Do not modify `test/ai/README.md`, create alternate results, or modify the framework repository. Commit only the canonical result with message `Replace Prompt 012 verification result`.

The final response must report all pinned identities, verification and defect results, required counts, format validation, canonical path, overwrite status, commit, commit message, `README modified: No`, framework mutation status, and notes.
