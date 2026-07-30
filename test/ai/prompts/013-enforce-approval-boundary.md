# Prompt 013 — Enforce Approval Boundary

## Purpose

Verify, without modifying the framework repository, that a fresh operator session enforces exact durable approval before any material dependency action begins, including authority, scope, persistence, delegation, revocation, expiry, and invalid authorization cases.

## Authorization

Use the immutable framework revision and fixture identities supplied by the canonical runner. Read the manifest first and all required files in manifest order. Resolve durable state, mission, goal, execution, decisions, approvals, findings, and authority records only from pinned repository artifacts. Construct all fixtures in memory and label displayed artifacts `PROPOSED ONLY — NOT WRITTEN`.

Do not perform the dependency action, invent approval, alter durable records, inspect an application repository, create framework commits, or push changes.

## Required fixture

Construct one material dependency action that requires approval and one complete approval chain. The chain must include stable identities, approving authority, subject, action and resource scope, decision provenance, evidence, issuance time, effective time, expiry when applicable, delegation lineage when applicable, revocation status, and durable canonical location.

Construct the proposed execution and state behavior for both authorized and unauthorized conditions. Unauthorized work must remain blocked without beginning implementation, validation, persistence, or reuse.

## Required verification

Verify:

- The exact action requires approval under governance and goal constraints.
- Approval exists durably before the action begins.
- Approver authority covers the subject, action, resources, risk, and time window.
- Decision, approval, delegation, and evidence references resolve.
- Approval is not expired, revoked, superseded, reused outside scope, or inferred from chat text.
- Execution, state, adaptation, decision, and approval statuses agree.
- Approval-required work cannot be marked approved or started without the exact authorization.
- Retained-SHA compare-and-swap, deterministic write order, final verification, and partial-write recovery are valid for any proposed durable update.
- Verification performs no framework mutation.

## Negative validation

Demonstrate deterministic rejection of at least 32 invalid cases covering missing approval, wrong approver, missing authority, wrong subject/action/resource scope, stale or future approval, expiry, revocation, supersession, invalid delegation, missing decision or evidence, non-durable approval, chat-only consent, approval reuse, scope expansion, approval after action start, mismatched execution or adaptation status, stale CAS, incomplete final verification, partial transition without recovery, and actual framework mutation.

## Result requirements

Produce exactly 16 numbered top-level sections:

1. Verification Summary
2. Validation Trace
3. Durable Operating Context
4. Material Dependency Action
5. Approval Requirement Decision
6. Authority and Delegation Findings
7. Durable Approval Record
8. Approval Scope and Validity Results
9. Authorized Execution and State Behavior
10. Unauthorized and Revoked Behavior
11. Schema and Cross-Artifact Results
12. Compare-and-Swap and Recovery Results
13. Negative Validation Results
14. Framework Defects
15. Repository Mutation Confirmation
16. Next Authorized Action

Report only reusable framework defects. Stop after the next authorized action.