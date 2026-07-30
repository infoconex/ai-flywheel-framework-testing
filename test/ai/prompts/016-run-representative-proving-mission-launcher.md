# AI Flywheel Representative Proving Mission Verification

## Canonical Prompt 016 Launcher

Use this file as the authoritative entrypoint for Prompt 016.

## Detailed specification

Read the immutable detailed specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/03e546596a6113ae9ac9543fbda1d8ea061f48c5/test/ai/prompts/016-run-representative-proving-mission.md

Follow every instruction except where this launcher clarifies the result-format validator and independent-read completion requirements.

## Immutable sources

```text
Framework revision: 1b90e6789109b6693ab0dc5d79dfb1b76cc74585
Detailed specification commit: 03e546596a6113ae9ac9543fbda1d8ea061f48c5
Fixture harness commit: 9aebe151d03d1e2728905cb697336325a67409e9
Fixture harness blob: 93708efaee0a0b3fb1b69b2a8c6133755984cc9b
Result-format contract commit: 43b35bd896554793a3142ddf6f654ffdf8bec7f2
Result-format validator commit: f4b06108e0a2c7f8de5ee6baba4441d82280ec6c
```

Do not substitute branch heads, later framework revisions, alternate fixture source, or an earlier result-format validator.

## Corrected format-validation contract

The detailed specification correctly places `Repository Mutation Confirmation` at section 20.

Use `test/ai/tools/validate_result_format.py` at commit `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c`. This validator locates the numbered `Repository Mutation Confirmation` section by its title and does not assume a fixed section number.

A result fails formatting when the validator fails. The prior validator commit `891f0d240c15bed3c175639808ff3f3b77f7aab1` is obsolete for Prompt 016.

## Independent-read completion boundary

The proving mission is incomplete until the independent session has successfully read and retained evidence for:

1. All 19 focused framework files listed in the detailed specification.
2. The durable active mission and active goal used as context only.
3. Every one of the 47 ordered `manifest.required_files` targets at the pinned framework revision.

Do not infer resolution from the harness inventory, the manifest list, prior chat, search snippets, or successful reads of only selected files.

For each of the 47 required paths, retain at minimum:

- Exact repository-relative path.
- Pinned framework revision.
- Successful connector resolution.
- Connector-reported blob identity when available.
- Any missing, duplicate, case-collision, unreadable, or identity anomaly.

The result may be written only after `19/19` focused reads and `47/47` required-path reads have completed. If either count is incomplete, do not publish a result yet; continue connector reads until complete or report an actual connector failure without committing a canonical result.

## Required result

Use the detailed specification's exact 22-section order, including:

```text
18. Result-Format Validation
19. Framework Defects
20. Repository Mutation Confirmation
21. Certification Scenario Result
22. Next Test Action
```

Prompt 016 passes only when all 24 validation rows pass, all 34 negative cases reject, the corrected format validator passes, all required reads complete, no blocking framework defect remains, and the framework repository remains unchanged.
