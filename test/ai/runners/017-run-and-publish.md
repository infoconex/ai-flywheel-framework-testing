# Run and Publish AI Flywheel Prompt 017

Use GitHub repositories as the sources of truth.

## Immutable sources

Read and execute exactly:

```text
Specification repository: Infoconex/ai-flywheel-framework-testing
Specification path: test/ai/prompts/017-self-host-certification.md
Specification commit: 7d3dda95851692dab2676888b26dba753a09a4b1
Framework repository: Infoconex/ai-flywheel-framework
Framework revision: 18335e57165a8984adab4790d3a6210355b484ba
Testing evidence revision: 4042369bfe6d1284fbe51de5037d4de7adb85df2
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later commits, cached content, copied prompts, prior results, inferred revisions, or alternate files.

## Canonical certification evidence set

Read these 16 files at testing evidence revision `4042369bfe6d1284fbe51de5037d4de7adb85df2`:

1. `test/ai/prompts/001-startup-validation.md`
2. `test/ai/results/001-startup-validation.md`
3. `test/ai/prompts/002-execution-creation.md`
4. `test/ai/results/002-execution-creation.md`
5. `test/ai/prompts/010-end-to-end-execution.md`
6. `test/ai/results/010-end-to-end-execution.md`
7. `test/ai/prompts/011-resume-interrupted-execution.md`
8. `test/ai/results/011-resume-interrupted-execution.md`
9. `test/ai/prompts/013-enforce-approval-boundary.md`
10. `test/ai/results/013-enforce-approval-boundary.md`
11. `test/ai/prompts/014-recover-missing-required-artifact.md`
12. `test/ai/results/014-recover-missing-required-artifact.md`
13. `test/ai/prompts/015-recover-broken-active-reference.md`
14. `test/ai/results/015-recover-broken-active-reference.md`
15. `test/ai/prompts/016-run-representative-proving-mission.md`
16. `test/ai/results/016-run-representative-proving-mission.md`

These files provide the canonical evidence for certification scenarios 1 through 9. Every scenario evidence revision must equal the pinned testing evidence revision. Do not retain or report an older transformation-embedded evidence revision.

## Deterministic fixture sources

Use these exact sources:

```text
Base fixture path: test/ai/tools/verify_prompt_017_fixtures.py
Base fixture commit: e032b9ed23aca4476c2d4c95557c1fc32121d669
Base fixture blob: ea34857e39da0440a5d6f4d555475c91161aac24
Transformation runner path: test/ai/tools/run_prompt_017_fixtures.py
Transformation runner commit: f91548956e6220585d0554d7d4104b993579e282
Transformation runner blob: 720109e3bb1e5c1ec9f9eafe98f0dbc76f6c6295
Current-evidence wrapper path: test/ai/tools/run_prompt_017_current_evidence.py
Current-evidence wrapper commit: 04082c4fe427ecc20a297cb6a241f7f71a57ab8a
Current-evidence wrapper blob: 1cf1b52edd4ce876dd4f74cb0d2daa8db14fd9f3
Self-hosting fixture commit: 5f1b69df1b5e47f0bad874cbe03238ae3860920b
Self-hosting fixture blob: 1ecc8a3adb14c09e9c804a3f2f2b70f60c0b63d0
```

Retrieve all three Python sources through the GitHub connector and verify their exact blobs. Execute the wrapper in memory and call its `run(base_source, transformation_source)` function. The wrapper must make exactly one evidence-revision correction and return:

```text
evidence_revision: 4042369bfe6d1284fbe51de5037d4de7adb85df2
execution_mode: in-memory connector source with current-evidence wrapper
wrapper_correction_count: 1
```

The underlying transformation must still report its 25 deterministic corrections. Unsupported or ambiguous changes are prompt-or-fixture defects and prevent a passing verification.

## Completion requirements

Do not publish until all requirements pass:

```text
Manifest-required reads: 50/50
Certification evidence reads: 16/16
Certification scenarios: 10/10
Artifact snapshots: 11
Fixture checks: 16/16
Negative cases: 44/44
Validation-result rows: 32/32
Required top-level sections: 22/22
Result-format validation: Passed
```

The required outcome is:

```text
Self-Hosting Scenario Result: Passed
Certification Status: ready-for-approval
Certification Overall Result: pending-approval
Human Approval Status: pending
Readiness Validation Result: pending
Readiness Transition Performed: No
Verification Result: Passed
```

Do not invent approval, mark certification approved, pass readiness, propose a ready-for-missions state, or perform a durable lifecycle transition.

## Publication boundary

Write or overwrite only:

```text
test/ai/results/017-self-host-certification.md
```

Do not create alternate results or modify `test/ai/README.md`. Commit only the canonical result with message:

```text
Replace Prompt 017 verification result
```

The final response must report every pinned identity, the single canonical testing evidence revision, fixture execution and correction results, outcome distinction, defect counts, required counts, format result, canonical path, overwrite status, result commit, commit message, `README modified: No`, framework mutation status, and notes.