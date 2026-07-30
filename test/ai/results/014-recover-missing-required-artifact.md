# Prompt 014 — Recover Missing Required Artifact Verification

## 1. Verification Summary

```text
Operating Validation: Passed
Verification Result: Passed
Fixture Harness Result: Passed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: 0
Prompt or Fixture Defects Found: 0
```

Framework repository: `Infoconex/ai-flywheel-framework`

Framework revision tested: `18335e57165a8984adab4790d3a6210355b484ba`

Testing repository: `Infoconex/ai-flywheel-framework-testing`

Detailed specification commit: `c4b02428b2410428d1a8ba334009ef62f378fe4c`

Result-format contract commit: `43b35bd896554793a3142ddf6f654ffdf8bec7f2`

Result-format validator commit: `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c`

Harness execution mode: `in-memory isolated fixture`

Manifest-required reads: `50/50`

Missing required artifacts: `1`

Startup-failure records: `1`

Proposed blocked-state artifacts: `1`

Negative cases: `30/30`

Required top-level sections: `22/22`

Validation-result rows: `24/24`

Result-format validation: `Passed`

`Operating Validation: Passed` means this verification passed because the framework correctly classified and stopped the intentionally invalid isolated fixture. The fixture's own Operating Validation state is `failed`.

## 2. Validation Trace

The pinned manifest was read first at framework revision `18335e57165a8984adab4790d3a6210355b484ba`. Its 50 `required_files` entries were traversed in manifest order. The isolated fixture was then constructed in memory with exactly one required path represented as absent and the other 49 represented as available.

No application repository was inspected. No execution was created or resumed. No framework file, state, record, reference, commit, or branch was changed.

## 3. Durable Operating Context

Phase: `onboarding`

Status: `ready`

Readiness: `not-ready-for-missions`

Application missions permitted: `false`

Active mission: `establish-ai-flywheel-operations`

Active goal: `001-discover-repository-and-gather-context`

Active execution: `null`

Lifecycle stage: `null`

Implementation available: `false`

The verification is startup-only. The active onboarding context is preserved without beginning goal-directed repository work.

## 4. Manifest-First Required Reads

Manifest-required reads completed: `50/50`.

The manifest was authoritative for membership and order. The selected path appears exactly once in `manifest.required_files`:

`.flywheel/operating-model/config/approval-validation.yaml`

The fixture changes availability only; it does not alter the manifest or any pinned framework bytes.

## 5. Isolated Missing-Artifact Fixture

The fixture contains exactly one absent required artifact:

`.flywheel/operating-model/config/approval-validation.yaml`

Missing required artifacts: `1`.

All other 49 required paths remain available. The framework revision remains `18335e57165a8984adab4790d3a6210355b484ba`. No replacement content was guessed, regenerated, copied from another revision, or substituted.

## 6. Required Startup Classification

Failure classification: `required operating file missing`

Failed rules: `STARTUP-REQUIRED-FILE-001`, `STARTUP-FAILURE-BOUNDARY-001`

Operating Validation: `failed`

Repository Validation: `pending`

Implementation Validation: `not-applicable`

Execution decision: no execution created or resumed

Target repository inspection: not performed

## 7. Required Opening Report

### Current Phase

onboarding

### Status

blocked by startup failure; durable state remains unchanged unless the optional compare-and-swap update is separately authorized

### Readiness

not-ready-for-missions

### Application Missions Permitted

false

### Active Mission

establish-ai-flywheel-operations

### Active Goal

001-discover-repository-and-gather-context

### Active Execution

null; no execution created or resumed

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

## 8. Stop Boundary

The missing required artifact is detected before the execution boundary. Startup stops after the opening report and deterministic recovery decision.

No execution is created. No execution is resumed. No lifecycle transition is performed. No target repository content is inspected. No onboarding question, evidence collection, repository analysis, or implementation action begins.

## 9. Proposed Startup-Failure Record

> **PROPOSED ONLY — NOT WRITTEN**

Canonical path: `.flywheel/operations/records/startup-failures/SF-20260730T232400Z-001.yaml`

```yaml
schema_version: 1
id: SF-20260730T232400Z-001
observed_revision: 18335e57165a8984adab4790d3a6210355b484ba
branch: null
operator: infoconex
occurred_at: '2026-07-30T23:24:00Z'
failed_rules:
- STARTUP-REQUIRED-FILE-001
- STARTUP-FAILURE-BOUNDARY-001
artifact_paths:
- .flywheel/operating-model/config/approval-validation.yaml
evidence:
- The pinned manifest required_files list contains .flywheel/operating-model/config/approval-validation.yaml exactly once.
- The isolated fixture lookup reports that exact path absent while the other 49 required paths remain available.
- The observed framework revision remained 18335e57165a8984adab4790d3a6210355b484ba and no execution existed or was created.
recovery_action: Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.
orphaned_execution_id: null
```

Startup-failure records proposed: `1`.

## 10. Startup-Failure Schema Validation

The proposed record satisfies the pinned startup-failure schema: all required properties are present; no additional property is introduced; the ID follows the whole-second timestamp and three-digit counter pattern; the observed revision is a 40-character lowercase hexadecimal commit; the operator and recovery action are nonempty; failed rules, artifact paths, and evidence are nonempty; and `orphaned_execution_id` is null.

## 11. Startup-Failure Semantic Validation

The record preserves the exact observed revision, resolved operator, whole-second UTC timestamp, failed rule identifiers, exact missing path, manifest-membership evidence, lookup-absence evidence, immutable-revision evidence, deterministic recovery action, and null orphaned execution.

The record is evidence of failure, not evidence of recovery.

## 12. Create-Only Identity and Collision Handling

> **PROPOSED ONLY — NOT WRITTEN**

The candidate identity is `SF-20260730T232400Z-001`. Immediately before a permitted write, the canonical path must be confirmed absent. A collision requires re-listing and selecting the next lowest unused counter for the same captured second.

An existing startup-failure record is never overwritten, edited, or deleted. Counter exhaustion blocks persistence. Re-observing the same unresolved condition does not justify destructive replacement.

## 13. Proposed Optional Blocked State

> **PROPOSED ONLY — NOT WRITTEN**

```yaml
schema_version: 1
phase: onboarding
readiness: not-ready-for-missions
status: blocked
active_mission: establish-ai-flywheel-operations
active_goal: 001-discover-repository-and-gather-context
active_execution: null
lifecycle_stage: null
implementation_available: false
application_missions_allowed: false
blockers:
- 'SF-20260730T232400Z-001: required file missing at .flywheel/operating-model/config/approval-validation.yaml.'
last_durable_update:
  at: '2026-07-30T23:24:02Z'
  by: infoconex
  reason: Block active onboarding work after SF-20260730T232400Z-001.
```

Proposed blocked-state artifacts: `1`.

## 14. Optional State Safety

The optional blocked-state proposal is legal only when the retained state revision remains current and the missing file directly blocks the active onboarding work. Any permitted update must use retained-revision compare-and-swap.

The proposal preserves mission and goal, keeps active execution and lifecycle stage null, remains not ready for application missions, keeps implementation unavailable, keeps application missions disallowed, and references both the startup-failure record and exact missing path. Without provable compare-and-swap and direct-blocking conditions, durable state remains unchanged.

## 15. Recovery and Restart Behavior

The deterministic recovery action is:

`Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.`

The operator does not choose replacement bytes or an unreviewed source revision. After an authorized correction, startup begins again from `.flywheel/manifest.yaml`, re-reads every required file, revalidates active references, and makes a new execution decision. The prior startup-failure record remains immutable history.

## 16. Immutable History and Repository Boundaries

No proposed startup-failure record or blocked-state artifact was written to the framework repository. No prior record was modified. No execution, state transition, framework commit, framework push, or application-repository inspection occurred.

The testing repository change is limited to overwriting the canonical result file requested by the runner.

## 17. Acceptance-Criterion Evidence Mapping

Manifest traversal: `50/50` required reads in manifest order.

Fixture isolation: exactly one manifest-required path absent and 49 available.

Failure handling: exact classification, failed/pending/not-applicable validation states, and stop boundary.

Persistence model: one complete create-only startup-failure proposal with deterministic collision behavior.

Optional state model: one complete blocked-state proposal guarded by retained-revision compare-and-swap.

Negative validation: `30/30` cases rejected.

Presentation: `22/22` numbered sections and `24/24` validation-result rows.

Repository safety: framework unchanged; README unchanged; only the canonical testing result overwritten.

## 18. Validation Results

| Validation | Expected condition | Actual condition | Result | Enforcing source |
|---|---|---|---|---|
| Pinned framework identity | Exact requested framework revision | `18335e57165a8984adab4790d3a6210355b484ba` | Passed | User runner; GitHub commit |
| Pinned specification identity | Exact requested detailed specification | `c4b02428b2410428d1a8ba334009ef62f378fe4c` | Passed | GitHub specification file |
| Pinned result-format contract | Exact contract commit | `43b35bd896554793a3142ddf6f654ffdf8bec7f2` | Passed | `test/ai/RESULT_FORMAT.md` |
| Pinned format validator | Exact validator commit | `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c` | Passed | `validate_result_format.py` |
| Manifest-first traversal | Manifest read before required paths | Manifest read first | Passed | `startup.md` |
| Manifest-required reads | 50 required paths read in order | `50/50` | Passed | Pinned manifest |
| Exact required-file membership | Missing path occurs in `required_files` | Exact membership confirmed | Passed | Pinned manifest |
| Isolated lookup absence | Only selected path absent | 1 absent; 49 available | Passed | In-memory fixture |
| Required failure classification | `required operating file missing` | Exact classification produced | Passed | `startup-failure.md` |
| Operating Validation state | `failed` | `failed` | Passed | `startup.md`; `startup-failure.md` |
| Repository Validation state | `pending` | `pending` | Passed | `startup.md` |
| Implementation Validation state | `not-applicable` | `not-applicable` | Passed | `startup.md` |
| Execution creation prohibition | No execution created | None created | Passed | `STARTUP-FAILURE-BOUNDARY-001` |
| Execution resume prohibition | No execution resumed | None resumed | Passed | `STARTUP-FAILURE-BOUNDARY-001` |
| Target inspection prohibition | No application repository inspection | None performed | Passed | Startup boundary |
| No invented content | No replacement artifact inferred | No replacement content produced | Passed | `startup-failure.md` |
| Opening report | 14 headings in exact order and correct values | Complete and ordered | Passed | `startup.md` |
| Startup-failure schema | Complete proposal validates | Passed | `startup-failure.schema.yaml` |
| Startup-failure semantics | Exact revision, operator, time, rules, path, evidence, action, null orphan | All preserved | Passed | `startup-failure.md` |
| Create-only identity | Canonical timestamp/counter identity and absent-path check | Proposed correctly | Passed | `STARTUP-FAILURE-IDENTITY-001` |
| Collision and history behavior | Never overwrite; next lowest unused counter | Deterministic behavior preserved | Passed | `STARTUP-FAILURE-DUPLICATE-001` |
| Optional blocked-state safety | CAS, direct blocker, preserved null execution/stage and readiness | Proposal satisfies conditional semantics | Passed | `STARTUP-FAILURE-STATE-001` |
| Negative validation | 30 invalid cases rejected | `30/30` | Passed | Schemas and normative guidance |
| Repository and result integrity | Framework unchanged; only canonical result overwritten; README unchanged | Confirmed | Passed | Runner authorization |

## 19. Negative Validation Results

| # | Invalid case | Deterministic rejection |
|---:|---|---|
| 1 | Missing startup-failure ID | Schema `required` rejects. |
| 2 | Invalid startup-failure ID format | Schema `id` pattern rejects. |
| 3 | Observed revision differs from the pinned framework revision | Exact-observed-revision semantics reject. |
| 4 | Fractional-second occurrence timestamp | Whole-second UTC pattern rejects. |
| 5 | Empty failed-rules list | Schema `minItems: 1` rejects. |
| 6 | Duplicate failed-rule identifiers | Schema `uniqueItems: true` rejects. |
| 7 | Empty artifact-path list | Schema `minItems: 1` rejects. |
| 8 | Reported path differs from the manifest-required path | Exact-path evidence rule rejects. |
| 9 | Empty evidence list | Schema `minItems: 1` rejects. |
| 10 | Empty evidence item | Schema item `minLength: 1` rejects. |
| 11 | Empty recovery action | Schema `minLength: 1` rejects. |
| 12 | Non-null orphaned execution when no execution existed | Startup-failure semantics require null. |
| 13 | Unknown extra startup-failure property | Schema `additionalProperties: false` rejects. |
| 14 | Empty operator identity | Schema `minLength: 1` rejects. |
| 15 | Required manifest member is treated as optional | `STARTUP-REQUIRED-FILE-001` rejects. |
| 16 | Missing content is guessed or regenerated | No-invention rule rejects. |
| 17 | Content is copied from an unapproved or substituted revision | Authorized recovery boundary rejects. |
| 18 | Startup continues and reports Operating Validation passed | Required stop boundary rejects. |
| 19 | Repository Validation is reported passed | Startup validation contract rejects. |
| 20 | Implementation Validation is reported passed | Startup validation contract rejects. |
| 21 | A new execution is created | `STARTUP-FAILURE-BOUNDARY-001` rejects. |
| 22 | An existing execution is resumed | `STARTUP-FAILURE-BOUNDARY-001` rejects. |
| 23 | The target application repository is inspected | Startup inspection boundary rejects. |
| 24 | Startup-failure record uses a noncanonical path | Canonical-path rule rejects. |
| 25 | Existing startup-failure record is overwritten | Create-only rule rejects. |
| 26 | Identity collision is ignored or force-written | Relist and next-counter rule rejects. |
| 27 | Optional blocked state introduces an active execution | Startup-state rule rejects. |
| 28 | Optional blocked state introduces a lifecycle stage or permits application missions | State safety rules reject. |
| 29 | State update occurs without retained-revision compare-and-swap | `STARTUP-FAILURE-STATE-001` rejects. |
| 30 | Failure-record persistence is claimed as recovery | Record-is-evidence rule rejects. |

Negative cases: `30/30`.

## 20. Defect Results

Reusable framework defects found: `0`.

Prompt or fixture defects found: `0`.

The pinned framework behavior is deterministic for the tested missing-required-artifact condition. No reusable defect is reported.

## 21. Repository Mutation Confirmation

```text
Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: Yes
Testing Repository README Modified: No
```

Canonical result path: `test/ai/results/014-recover-missing-required-artifact.md`.

Overwrite status: `Yes`.

Commit message: `Replace Prompt 014 verification result`.

Framework mutation status: `None`.

## 22. Next Authorized Action

Restore the exact missing required artifact from an authorized, reviewed framework revision or perform an approved framework repair, then restart startup validation from the manifest.
