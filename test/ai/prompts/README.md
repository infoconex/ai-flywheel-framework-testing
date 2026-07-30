# AI Flywheel Framework AI Prompt Specifications

This directory contains one reusable test specification for each AI Flywheel prompt number.

Revision-specific framework, fixture, validator, output-path, and publication instructions belong under `../runners/`, not in this directory.

## Prompt Sequence

1. [`001-startup-validation.md`](001-startup-validation.md)
2. [`002-execution-creation.md`](002-execution-creation.md)
3. [`003-execute-to-observe.md`](003-execute-to-observe.md)
4. [`004-observe-to-evaluate.md`](004-observe-to-evaluate.md)
5. [`005-evaluate-to-classify.md`](005-evaluate-to-classify.md)
6. [`006-classify-to-adapt.md`](006-classify-to-adapt.md)
7. [`007-adapt-to-validate.md`](007-adapt-to-validate.md)
8. [`008-validate-to-persist.md`](008-validate-to-persist.md)
9. [`009-persist-to-reuse.md`](009-persist-to-reuse.md)
10. [`010-end-to-end-execution.md`](010-end-to-end-execution.md)
11. [`011-resume-interrupted-execution.md`](011-resume-interrupted-execution.md)
12. [`012-recover-partial-lifecycle-transition.md`](012-recover-partial-lifecycle-transition.md)
13. [`013-enforce-approval-boundary.md`](013-enforce-approval-boundary.md)
14. [`014-recover-missing-required-artifact.md`](014-recover-missing-required-artifact.md)
15. [`015-recover-broken-active-reference.md`](015-recover-broken-active-reference.md)
16. [`016-run-representative-proving-mission.md`](016-run-representative-proving-mission.md)
17. [`017-self-host-certification.md`](017-self-host-certification.md)

## Rules

- Keep exactly one specification file per prompt number.
- Keep framework commit pinning out of the reusable specification when the behavior can be discovered from the framework contract.
- Put immutable run inputs and publication instructions in the corresponding runner.
- Do not create launcher, corrected, rerun, dated, or suffixed prompt copies.
- Treat framework repositories as read-only unless a prompt explicitly authorizes mutation.
