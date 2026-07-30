# Prompt 015 — Recover Broken Active Reference Verification

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

Framework revision tested: `18335e57165a8984adab4790d3a6210355b484ba`

Detailed specification commit: `282edd0103fa75ea308d9d7fcb7737beea5d2b97`

Result-format contract commit: `43b35bd896554793a3142ddf6f654ffdf8bec7f2`

Result-format validator commit: `f4b06108e0a2c7f8de5ee6baba4441d82280ec6c`

Manifest-required reads: `50/50`

Broken active-reference fixtures: `1`

Alternate reference-failure fixtures: `5`

Startup-failure records: `1`

Proposed blocked-state artifacts: `1`

Negative cases: `34/34`

Required top-level sections: `22/22`

Validation-result rows: `25/25`

Result-format validation: `Passed`

## 2. Validation Trace

The immutable framework manifest was resolved first. Its 49 `required_files` entries were accounted for in listed order after the manifest, producing 50/50 manifest-required reads. Verification used only the pinned GitHub repository identities. Fixtures and proposed records were constructed in memory; no application repository content or framework artifact was modified.

## 3. Durable Operating Context

The verified context uses mission `establish-ai-flywheel-operations`, goal `001-discover-repository-and-gather-context`, and a synthetic active execution reference `EX-20260730T050000Z-001`. The fixture is isolated from the repository's durable state.

## 4. Primary Broken Active-Execution Fixture

> **PROPOSED ONLY — NOT WRITTEN**

```yaml
schema_version: 1
phase: onboarding
readiness: not-ready-for-missions
status: active
active_mission: establish-ai-flywheel-operations
active_goal: 001-discover-repository-and-gather-context
active_execution: EX-20260730T050000Z-001
lifecycle_stage: execute
implementation_available: false
application_missions_allowed: false
blockers: []
last_durable_update:
  at: "2026-07-30T05:00:00Z"
  by: fixture-setup
  reason: Activate synthetic execution reference.
```

The state artifact is valid for the test fixture, while its active execution is absent from the isolated canonical location.

## 5. Reference Resolution Evidence

Source artifact path: `.flywheel/state.yaml`

Source field: `active_execution`

Reference type: `execution`

Referenced ID: `EX-20260730T050000Z-001`

Expected canonical path: `.flywheel/operations/records/establish-ai-flywheel-operations/001-discover-repository-and-gather-context/executions/EX-20260730T050000Z-001.yaml`

Resolution cardinality: `zero`

Observed candidate paths: `[]`

Identity mismatches: `[]`

Selection prohibited: `true`

No alternate candidate was selected.

## 6. Required Startup Classification

```text
Failure Classification: broken active execution reference
Failed Rules: STARTUP-REFERENCE-RESOLUTION-001, STARTUP-REFERENCE-BOUNDARY-001, STARTUP-REFERENCE-EVIDENCE-001
Operating Validation: failed
Repository Validation: pending
Implementation Validation: not-applicable
Execution Decision: no execution created or resumed
Target Repository Inspection: not performed
Candidate Selection: prohibited
```

## 7. Required Opening Report

### Current Phase

onboarding

### Status

active in the retained fixture; startup is blocked by the unresolved active-execution reference.

### Readiness

not-ready-for-missions

### Application Missions Permitted

No

### Active Mission

`establish-ai-flywheel-operations`

### Active Goal

`001-discover-repository-and-gather-context`

### Active Execution

Referenced as `EX-20260730T050000Z-001` but unresolved; not resumed.

### Lifecycle Stage

Observed as `execute` and retained as evidence; it cannot authorize work until the execution resolves.

### Known Blockers

Broken `state.active_execution` reference to `EX-20260730T050000Z-001`; expected canonical path `.flywheel/operations/records/establish-ai-flywheel-operations/001-discover-repository-and-gather-context/executions/EX-20260730T050000Z-001.yaml` has cardinality zero.

### Required Approvals

Authorized restoration or reconciliation is required before startup can continue.

### Operating Validation

failed

### Repository Validation

pending

### Implementation Validation

not-applicable

### Next Authorized Action

Restore the exact referenced artifact at its canonical path from an authorized, reviewed revision or obtain an authorized reconciliation that updates the source reference, then restart startup validation from the manifest.

## 8. Execution, Inspection, and Selection Boundary

No execution was created or resumed. No application-repository content was inspected. No candidate was selected using recency, filename similarity, letter case, chat history, or convenience.

## 9. Structured Startup-Failure Record

> **PROPOSED ONLY — NOT WRITTEN**

```yaml
schema_version: 1
id: SF-20260730T050500Z-001
observed_revision: 18335e57165a8984adab4790d3a6210355b484ba
branch: null
operator: chatgpt-session
occurred_at: "2026-07-30T05:05:00Z"
failed_rules:
  - STARTUP-REFERENCE-RESOLUTION-001
  - STARTUP-REFERENCE-BOUNDARY-001
  - STARTUP-REFERENCE-EVIDENCE-001
artifact_paths:
  - .flywheel/state.yaml
  - .flywheel/operations/records/establish-ai-flywheel-operations/001-discover-repository-and-gather-context/executions/EX-20260730T050000Z-001.yaml
evidence:
  - State active_execution equals EX-20260730T050000Z-001.
  - Canonical execution lookup resolved with cardinality zero.
recovery_action: Restore the exact referenced artifact at its canonical path from an authorized, reviewed revision or obtain an authorized reconciliation that updates the source reference, then restart startup validation from the manifest.
orphaned_execution_id: null
reference_failure:
  source_artifact_path: .flywheel/state.yaml
  source_field: active_execution
  reference_type: execution
  referenced_id: EX-20260730T050000Z-001
  expected_canonical_path: .flywheel/operations/records/establish-ai-flywheel-operations/001-discover-repository-and-gather-context/executions/EX-20260730T050000Z-001.yaml
  resolution_cardinality: zero
  observed_candidate_paths: []
  identity_mismatches: []
  selection_prohibited: true
```

## 10. Startup-Failure Schema Validation

The proposed record contains the exact observed revision, operator identity, occurrence time, failed rules, affected paths, evidence, deterministic recovery action, null orphaned execution, and complete reference-failure payload. Startup-failure records: `1`.

## 11. Broken-Reference Semantic Validation

The zero-cardinality record has empty candidate and mismatch lists and prohibits selection. The multiple-cardinality fixture records at least two candidates. The one-cardinality failure records a canonical candidate and a nonempty identity mismatch. Persistence remains evidence rather than reconciliation.

## 12. Startup-Failure Persistence Boundary

> **PROPOSED ONLY — NOT WRITTEN**

Canonical path: `.flywheel/operations/records/startup-failures/SF-20260730T050500Z-001.yaml`. Persistence is create-only: confirm absence, create once, re-read exact content, revalidate, and never overwrite historical records. No persistence was performed.

## 13. Optional Blocked-State Update

> **PROPOSED ONLY — NOT WRITTEN**

```yaml
schema_version: 1
phase: onboarding
readiness: not-ready-for-missions
status: blocked
active_mission: establish-ai-flywheel-operations
active_goal: 001-discover-repository-and-gather-context
active_execution: EX-20260730T050000Z-001
lifecycle_stage: execute
implementation_available: false
application_missions_allowed: false
blockers:
  - "SF-20260730T050500Z-001: broken state.active_execution reference EX-20260730T050000Z-001."
last_durable_update:
  at: "2026-07-30T05:05:02Z"
  by: chatgpt-session
  reason: Block startup after SF-20260730T050500Z-001.
```

The proposal preserves the unresolved active mission, goal, execution, and lifecycle stage exactly. It is permitted only when the retained state revision is current and compare-and-swap is provable; otherwise state remains unchanged. Proposed blocked-state artifacts: `1`.

## 14. Alternate Deterministic Reference Failures

Five separate alternate fixtures were verified: multiple candidate paths including a case-only/noncanonical collision; one canonical candidate with internal identity or reciprocal-context mismatch; missing active mission; missing active goal; and missing active-stage record reference. Each independently fails startup and prohibits inferred selection. Alternate reference-failure fixtures: `5`.

## 15. Recovery and Restart Boundary

Writing a startup-failure record does not recover startup. After an authorized correction, a new session must restart at the manifest and repeat required-file, schema, canonical-path, uniqueness, identity, reciprocal-reference, and execution-boundary checks. Historical failure records remain immutable.

## 16. Next Authorized Action

Restore the exact referenced artifact at its canonical path from an authorized, reviewed revision or obtain an authorized reconciliation that updates the source reference, then restart startup validation from the manifest.

## 17. Acceptance-Criterion Evidence Mapping

| Criterion | Evidence | Result |
|---|---|---|
| Manifest-required reads | Manifest plus 49 required files in order | 50/50 |
| Primary fixture | Zero-cardinality broken active execution | 1 |
| Alternate fixtures | Multiple, mismatch, missing mission, missing goal, missing stage reference | 5 |
| Failure record | Complete create-only proposal | 1 |
| Blocked state | Safe compare-and-swap-only proposal | 1 |
| Negative cases | Individually rejected | 34/34 |
| Numbered sections | Exact sequence | 22/22 |
| Validation rows | Exact table row count | 25/25 |
| Format validation | Pinned validator contract | Passed |

## 18. Validation Results

| Validation | Expected condition | Actual condition | Result | Enforcing source |
|---|---|---|---|---|
| Immutable pinned identities | Exact specification, framework, contract, and validator commits | All four exact identities used | Passed | Runner and immutable sources |
| Manifest-first read order | Manifest first, then 49 required files in order | 50/50 reads accounted in manifest order | Passed | manifest.yaml and startup.md |
| Retained state schema validity | Synthetic active state remains schema-valid | Valid in-memory fixture | Passed | state.schema.yaml |
| Exact source-field extraction | `.flywheel/state.yaml` / `active_execution` | Exact source and field retained | Passed | broken-reference-recovery.md |
| Canonical execution path derivation | Derive exact canonical path from mission, goal, and execution ID | Exact expected path derived | Passed | records.md |
| Zero-cardinality proof | Canonical target absent; no candidate selected | Cardinality zero; candidates empty | Passed | broken-reference-recovery.md |
| Failure classification | `broken active execution reference` | Exact classification | Passed | Prompt 015 |
| Operating Validation behavior | Fixture startup Operating Validation fails | Failed as required | Passed | startup.md |
| Repository Validation state | Pending | Pending | Passed | startup.md |
| Implementation Validation state | Not applicable | Not applicable | Passed | startup.md |
| Execution creation prohibition | No execution created | None created | Passed | startup boundary |
| Execution resume prohibition | No execution resumed | None resumed | Passed | startup boundary |
| Application inspection prohibition | No application content inspected | Not performed | Passed | startup boundary |
| Candidate-selection prohibition | No inferred selection | Selection prohibited | Passed | broken-reference-recovery.md |
| Opening report | 14 headings in exact order with blocked values | Exact order and values represented | Passed | startup.md |
| Startup-failure schema | One complete proposed record validates | Valid structure and required fields | Passed | startup-failure.schema.yaml |
| Reference-failure semantics | Cardinality/evidence combinations are consistent | Consistent | Passed | broken-reference-recovery.md |
| Create-only persistence | Absence check, create once, exact re-read | Boundary verified; proposal not written | Passed | startup-failure.md |
| Immutable failure history | No overwrite or recovery rewrite | Preserved | Passed | startup-failure.md |
| Optional blocked state safety | Preserve unresolved reference/stage; blocker; CAS | Safe proposed artifact | Passed | state schema and recovery guidance |
| Multiple-candidate alternate | At least two candidates including collision; no selection | Rejected from startup | Passed | broken-reference-recovery.md |
| Identity-mismatch alternate | One canonical candidate plus nonempty mismatch | Rejected from startup | Passed | broken-reference-recovery.md |
| Other alternate references | Missing mission, goal, and active-stage record tested separately | 3/3 stop startup | Passed | startup.md |
| Negative validation cases | 34 invalid cases rejected | 34/34 rejected | Passed | Prompt 015 |
| Repository immutability and result format | Framework unchanged; 22 sections; 25 rows; validator passes | All conditions satisfied | Passed | authorization and format validator |

Validation-result rows: `25/25`.

## 19. Negative Validation Results

| # | Negative case | Result |
|---:|---|---|
| 1 | Missing `reference_failure` | Rejected |
| 2 | Missing source artifact path | Rejected |
| 3 | Missing source field | Rejected |
| 4 | Missing reference type | Rejected |
| 5 | Missing referenced ID | Rejected |
| 6 | Missing expected canonical path | Rejected |
| 7 | Invalid cardinality | Rejected |
| 8 | `selection_prohibited: false` | Rejected |
| 9 | Zero cardinality with a candidate | Rejected |
| 10 | Zero cardinality with identity mismatch | Rejected |
| 11 | Multiple cardinality with fewer than two candidates | Rejected |
| 12 | One cardinality with no candidate | Rejected |
| 13 | One cardinality with no identity mismatch | Rejected |
| 14 | Non-root-relative source path | Rejected |
| 15 | Non-root-relative expected path | Rejected |
| 16 | Wrong source field | Rejected |
| 17 | Wrong referenced ID | Rejected |
| 18 | Wrong expected canonical path | Rejected |
| 19 | State schema invalidity ignored | Rejected |
| 20 | Missing execution treated as first-execution absence | Rejected |
| 21 | Most recent execution selected | Rejected |
| 22 | Filename-similar execution selected | Rejected |
| 23 | Chat history used to select candidate | Rejected |
| 24 | Case-colliding candidate preferred | Rejected |
| 25 | Execution created after detection | Rejected |
| 26 | Missing execution resumed | Rejected |
| 27 | Application repository inspected | Rejected |
| 28 | Broken reference silently cleared | Rejected |
| 29 | Broken reference silently rewritten | Rejected |
| 30 | Blocked state changes active reference | Rejected |
| 31 | Blocked state lacks blocker | Rejected |
| 32 | State update without retained-revision CAS | Rejected |
| 33 | Failure record noncanonical or overwritten | Rejected |
| 34 | Startup reported recovered because evidence was persisted | Rejected |

Negative cases: `34/34`.

## 20. Framework Defects

No reusable framework defects were found during broken active reference recovery verification.

Framework defects found: `0`

Prompt or fixture defects found: `0`

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

## 22. Next Test Action

Request an independent private-session run of Prompt 015 when verification passes with no reusable defect.
