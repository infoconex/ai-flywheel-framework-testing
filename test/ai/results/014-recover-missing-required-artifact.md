# Prompt 014 — Recover Missing Required Artifact Verification

## 1. Verification Summary

Operating Validation: Passed
Verification Result: Passed
Fixture Harness Result: Passed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: 0
Prompt or Fixture Defects Found: 0

Framework revision tested: 923c46baf8d4bb400eef71a3507e07d797dcab87
Detailed specification commit: 087c97c6f95ce36555a5c77aff95eeb16e19c8d3
Fixture harness commit: e5f47e50b092a44858bf5a1daea22cfcc85f8c94
Fixture harness blob: d264dcce92e5e06ee06801eb15d3e1f8a64a1843
Canonical launcher commit: aead473368cd2f7243ba473af08d9656d21950a2
Harness execution mode: in-memory connector source

`Operating Validation: Passed` means the framework correctly detected and handled the intentionally invalid isolated fixture. The fixture's operating validation state is `failed`.

## 2. Validation Trace

The canonical launcher was read first. It replaced the obsolete harness reference in the detailed specification. The corrected source was retrieved through the GitHub connector, its connector-reported Git blob SHA matched the required blob, and the exact source was executed in memory with Python 3 using `exec`. The complete JSON output parsed successfully.

Harness facts: `result: passed`; framework revision matched; four artifact snapshots each contained data, complete normalized YAML, SHA-256, Git blob SHA, and byte count; all harness checks were true; all 12 harness-generated record mutation checks were true. Independent schema validation also passed for the fixture manifest, retained state, optional blocked state, and startup-failure record.

Focused framework resolution: 12/12 files read from the pinned revision. Contextual resolution: active mission and active goal read from the same pinned revision. No application-repository content was read.

## 3. Durable Operating Context

- Phase: onboarding
- Readiness: not-ready-for-missions
- Durable status: ready
- Active mission: `establish-ai-flywheel-operations`
- Active goal: `001-discover-repository-and-gather-context`
- Active execution: null
- Lifecycle stage: null
- Implementation available: false
- Application missions allowed: false

The active mission is “Onboard Repository to AI Flywheel.” The active goal is “Discover Repository and Gather Context.” This verification is startup-only and does not authorize the goal's target-repository inspection procedure.

## 4. Isolated Missing-File Fixture

The isolated fixture represents exactly one absent artifact:

`.flywheel/operating-model/config/approval-validation.yaml`

The path appears in the complete fixture `manifest.required_files`. Every other required fixture artifact remains represented as present. The canonical framework revision is untouched. No missing content was guessed, regenerated, copied, or substituted.

## 5. Required Startup Classification

Failure Classification: required operating file missing
Failed Rule: STARTUP-REQUIRED-FILE-001
Operating Validation: failed
Repository Validation: pending
Implementation Validation: not-applicable
Execution Decision: no execution created or resumed
Target Repository Inspection: not performed

Boundary rule: `STARTUP-FAILURE-BOUNDARY-001`.

## 6. Required Opening Report

### Current Phase

onboarding
### Status

blocked (startup failure; retained durable state remains ready unless optional CAS update is authorized)
### Readiness

not-ready-for-missions
### Application Missions Permitted

false
### Active Mission

establish-ai-flywheel-operations
### Active Goal

001-discover-repository-and-gather-context
### Active Execution

None; no execution created or resumed
### Lifecycle Stage

null
### Known Blockers

Required operating file missing: `.flywheel/operating-model/config/approval-validation.yaml`
### Required Approvals

Authorization to restore the exact artifact from a reviewed framework revision or to perform an approved framework repair
### Operating Validation

failed
### Repository Validation

pending
### Implementation Validation

not-applicable
### Next Authorized Action

Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.

## 7. Execution and Inspection Boundary

The retained state has no active execution. Detection of the missing manifest-required artifact occurs before the execution boundary. Therefore no execution may be created or resumed, no goal-directed action may begin, and no target-repository content may be inspected. Harness outputs explicitly report `execution_created_or_resumed: false` and `target_repository_inspected: false`.

## 8. Startup-Failure Record

> **PROPOSED ONLY — NOT WRITTEN**

Canonical path: `.flywheel/operations/records/startup-failures/SF-20260730T040000Z-001.yaml`

```yaml
schema_version: 1
id: SF-20260730T040000Z-001
observed_revision: 923c46baf8d4bb400eef71a3507e07d797dcab87
branch: feature/resilience-and-recovery-testing
operator: chatgpt-session
occurred_at: '2026-07-30T04:00:00Z'
failed_rules:
- STARTUP-REQUIRED-FILE-001
- STARTUP-FAILURE-BOUNDARY-001
artifact_paths:
- .flywheel/operating-model/config/approval-validation.yaml
evidence:
- Manifest required_files contains .flywheel/operating-model/config/approval-validation.yaml.
- Fixture path lookup returned absent for .flywheel/operating-model/config/approval-validation.yaml.
- No execution existed or was created before the failure was observed.
recovery_action: Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved
  framework repair, then restart startup validation from the manifest.
orphaned_execution_id: null
```

## 9. Startup-Failure Schema Validation

The complete proposed record validates against the pinned Draft 2020-12 `startup-failure.schema.yaml`. Required fields are present, additional fields are absent, the ID and revision patterns match, the timestamp is whole-second UTC, nonempty arrays and strings satisfy constraints, and `orphaned_execution_id` is null.

## 10. Startup-Failure Semantic Validation

The record contains the exact observed framework revision, branch `feature/resilience-and-recovery-testing`, stable operator `chatgpt-session`, timestamp `2026-07-30T04:00:00Z`, rules `STARTUP-REQUIRED-FILE-001` and `STARTUP-FAILURE-BOUNDARY-001`, the exact missing path, manifest-membership and absent-lookup evidence, the exact recovery action, and no orphaned execution.

## 11. Startup-Failure Persistence Boundary

> **PROPOSED ONLY — NOT WRITTEN**

Persistence is a startup action and requires no execution. The deterministic identity is `SF-20260730T040000Z-001`. The canonical path must be confirmed absent immediately before create-only persistence. The record is then created once, re-read, and verified for exact content and schema validity. Persistence does not authorize repository inspection, execution creation or resume, goal-directed work, or repair of the missing artifact. All persistence behavior in this verification remained hypothetical and in memory.

## 12. Optional Blocked-State Update

> **PROPOSED ONLY — NOT WRITTEN**

```yaml
schema_version: 1
readiness: not-ready-for-missions
phase: onboarding
status: blocked
active_mission: establish-ai-flywheel-operations
active_goal: 001-discover-repository-and-gather-context
active_execution: null
lifecycle_stage: null
implementation_available: false
application_missions_allowed: false
blockers:
- 'SF-20260730T040000Z-001: required file missing at .flywheel/operating-model/config/approval-validation.yaml.'
last_durable_update:
  at: '2026-07-30T04:00:02Z'
  by: chatgpt-session
  reason: Block active onboarding work after SF-20260730T040000Z-001.
```

The update is permitted only when the retained state revision is still current and the missing artifact directly prevents the active onboarding work. It remains `not-ready-for-missions`, sets `status: blocked`, preserves mission and goal, keeps execution and lifecycle stage null, keeps application missions disallowed, and includes a nonempty blocker naming the startup-failure ID and exact path. It requires retained-revision compare-and-swap. If either precondition is unprovable, state remains unchanged while the startup failure is still reported.

## 13. Duplicate and Collision Handling

Startup-failure records are immutable and never overwritten. Before creation, absence is rechecked. A collision requires re-listing and selecting the next lowest unused counter for the same timestamp. Repeating the same unresolved observation does not silently mutate the prior record. A new record is justified only by a materially new observation or changed repository revision. Prior failure history remains immutable.

## 14. Recovery and Restart Boundary

The failure record is evidence, not recovery. The exact recovery action is:

`Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.`

After authorized repair, a new session restarts startup validation from the manifest, re-reads all required files, revalidates state and references, and makes a new execution decision.

## 15. Alternate Deterministic States

Retaining the current schema-valid state is correct when blocked-state preconditions cannot be proven. A schema-valid optional blocked state is correct only under retained-revision CAS and direct-prevention proof. No alternate state may introduce an execution or lifecycle stage. Repository and implementation validation cannot advance from `pending` and `not-applicable` during this startup failure.

## 16. Next Authorized Action

Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.

## 17. Acceptance-Criterion Evidence Mapping

- Exact revisions: connector reads pinned the launcher, specification, harness, and all framework artifacts.
- Focused resolution: all 12 required framework files plus active mission and goal resolved.
- Fixture isolation: the complete fixture manifest contains the exact path and represents only that path absent.
- Boundary behavior: harness output and normative guidance establish failed/pending/not-applicable states and prohibit execution and inspection.
- Record validity: independent Draft 2020-12 schema validation and semantic checks passed.
- Optional state: independent schema validation passed; CAS and direct-prevention preconditions are explicit.
- Negative behavior: 30/30 invalid cases are deterministically rejected below.
- Immutability: the framework repository received no writes, commits, pushes, or lifecycle transitions.

## 18. Validation Results

| Validation | Expected condition | Actual condition | Result | Enforcing source |
|---|---|---|---|---|
| Immutable revision and focused resolution | Pinned revision; 12 focused files plus active mission and goal resolve | 923c46baf8d4bb400eef71a3507e07d797dcab87; 12/12; mission and goal resolved | Passed | launcher; detailed specification; startup.md |
| Harness source identity and execution | Corrected commit/blob; in-memory `exec`; JSON result passed | Commit e5f47e50b092a44858bf5a1daea22cfcc85f8c94; blob d264dcce92e5e06ee06801eb15d3e1f8a64a1843; passed | Passed | canonical launcher |
| Fixture manifest schema validation | Complete fixture manifest validates | Draft 2020-12 validation passed | Passed | manifest.schema.yaml |
| Retained state schema validation | Retained state validates | Validation passed, including `implementation_available: false` | Passed | state.schema.yaml |
| Exact required-file membership | Exact missing path is in required_files | Membership true | Passed | fixture manifest; framework manifest |
| Isolated missing-path proof | Only approval-validation.yaml absent; all other required artifacts present | Harness fixture representation confirms exact isolated absence | Passed | canonical launcher fixture corrections |
| Required-file failure classification | Classification is required operating file missing | Exact classification produced | Passed | startup-failure.md |
| Operating Validation failure state | Operating Validation failed | failed | Passed | startup.md; startup-failure.md |
| Repository Validation pending state | Repository Validation pending | pending | Passed | startup.md; validation.yaml |
| Implementation Validation not-applicable state | Implementation Validation not-applicable | not-applicable | Passed | startup.md; validation.yaml |
| Execution creation prohibition | No execution created | false | Passed | STARTUP-FAILURE-BOUNDARY-001 |
| Execution resume prohibition | No execution resumed | false | Passed | STARTUP-FAILURE-BOUNDARY-001 |
| Target-repository inspection prohibition | No target inspection | false | Passed | startup.md; startup-failure.md |
| No artifact invention or substitution | No guessed, regenerated, copied, or substitute artifact | No artifact content produced; recovery requires authorized source/repair | Passed | startup-failure.md |
| Opening-report heading order and values | 14 exact headings and required states | 14 headings in exact order; blocker, null stage, validations, and action correct | Passed | startup.md |
| Startup-failure schema validation | Complete record validates | Draft 2020-12 validation passed | Passed | startup-failure.schema.yaml |
| Startup-failure semantic validation | Exact revision, branch, operator, timestamp, rules, path, evidence, action, null orphan | All required semantics satisfied | Passed | startup-failure.md |
| Deterministic identity and canonical path | SF timestamp/counter identity at canonical path | SF-20260730T040000Z-001 at canonical startup-failures path | Passed | STARTUP-FAILURE-IDENTITY-001 |
| Create-only absence check and re-read verification | Hypothetical persistence uses absence check, create once, re-read exact | Proposed sequence satisfies boundary; no actual framework write | Passed | STARTUP-FAILURE-RECORD-001 |
| Optional blocked-state validity | Schema-valid only with current retained revision and direct blocker | Fixture blocked state validates; CAS and direct-prevention conditions remain mandatory | Passed | STARTUP-FAILURE-STATE-001 |
| Duplicate and collision behavior | Never overwrite; relist and lowest unused counter; new record only for material change | Deterministic behavior proven from normative contract | Passed | STARTUP-FAILURE-DUPLICATE-001 |
| Recovery action and restart boundary | Exact action; startup restarts from manifest after authorized correction | Exact action preserved; record persistence does not recover startup | Passed | startup-failure.md |
| Negative validation cases | All 30 deterministically rejected | 30/30 rejected by schema or semantic rules | Passed | schemas and normative guidance |
| Repository immutability | No framework mutation, execution, inspection, lifecycle transition | 0 framework files written; 0 commits; 0 pushes | Passed | authorization and fixture isolation |

## 19. Negative Validation Results

| # | Invalid case | Deterministic rejection |
|---:|---|---|
| 1 | Missing startup-failure ID | Schema `required` rejects. |
| 2 | Invalid startup-failure ID format | Schema `id` pattern rejects. |
| 3 | Observed revision differs from fixture revision | `STARTUP-FAILURE-EVIDENCE-001` and exact-observed-revision semantic rule reject. |
| 4 | Fractional startup timestamp | Schema whole-second timestamp pattern rejects. |
| 5 | Empty failed-rules list | Schema `minItems: 1` rejects. |
| 6 | Empty artifact-path list | Schema `minItems: 1` rejects. |
| 7 | Artifact path is not repository-root-relative and exact | `STARTUP-REQUIRED-FILE-001` exact-path rule rejects. |
| 8 | Empty evidence list | Schema `minItems: 1` rejects. |
| 9 | Empty recovery action | Schema `minLength: 1` rejects. |
| 10 | Non-null orphaned execution when no execution existed | Startup-failure semantic rule requires null. |
| 11 | Unknown extra startup-failure field | Schema `additionalProperties: false` rejects. |
| 12 | Empty operator identity | Schema `minLength: 1` rejects. |
| 13 | Missing required file is treated as optional | Manifest membership and `STARTUP-REQUIRED-FILE-001` reject. |
| 14 | Operator continues Operating Validation as passed | Required stop boundary rejects. |
| 15 | Repository Validation is reported passed | Startup validation-state contract rejects. |
| 16 | Implementation Validation is reported passed | Startup validation-state contract rejects. |
| 17 | Execution is created after detecting the missing file | `STARTUP-FAILURE-BOUNDARY-001` rejects. |
| 18 | Existing execution is resumed after detecting the missing file | `STARTUP-FAILURE-BOUNDARY-001` rejects. |
| 19 | Target repository is inspected | Startup inspection boundary rejects. |
| 20 | Missing artifact content is invented | Startup-failure no-invention rule rejects. |
| 21 | Artifact is copied from an unapproved revision | Authorized-source recovery rule rejects. |
| 22 | Different path is reported than the manifest-required path | Exact-path evidence rule rejects. |
| 23 | Startup-failure record is written outside the canonical directory | Canonical-path rule rejects. |
| 24 | Existing startup-failure record is overwritten | Create-only rule rejects. |
| 25 | Create collision is ignored or force-written | Collision relist/next-counter rule rejects. |
| 26 | Optional blocked state introduces an active execution | State semantic and startup-failure state rule reject. |
| 27 | Optional blocked state introduces a lifecycle stage | State schema null-stage condition rejects. |
| 28 | Optional blocked state omits a blocker | State schema blocked `minItems: 1` rejects. |
| 29 | State is updated without retained-revision CAS | `STARTUP-FAILURE-STATE-001` rejects. |
| 30 | Startup is reported recovered merely because the failure record was persisted | Completion/retry rule rejects; record is evidence, not resolution. |

All 30 cases reject deterministically. The first 12 are also represented by true harness negative-case results; cases 13–30 are enforced by the pinned normative startup, startup-failure, failure-handling, state, and record contracts.

## 20. Framework Defects

> No reusable framework defects were found during missing required artifact recovery verification.

No prompt or fixture defects remain after applying the canonical launcher's corrected fixture-harness requirements.

## 21. Repository Mutation Confirmation

Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: No
Testing Repository README Modified: No

The canonical result path did not exist on the testing repository default branch, so it was created at the sole required path rather than overwritten. No alternate or history result was created.

## 22. Next Test Action

Request an independent private-session run of Prompt 014 when verification passes with no reusable defect.
