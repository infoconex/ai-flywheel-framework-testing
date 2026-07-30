#!/usr/bin/env python3
"""Deterministic Prompt 013 approval-boundary fixture generator.

No network access and no repository writes are performed.
"""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from typing import Any

import yaml

FRAMEWORK_REVISION = "ea8f72fd194973f033553f46c59b400ab36c8868"
MISSION = "verify-approval-boundary"
GOAL = "enforce-material-approval"
EXECUTION = "EX-20260730T020000Z-001"
ADAPTATION = "ADAPT-940"
EVIDENCE = "EVID-940"
DECISION = "DECISION-940"
OWNER_APPROVAL = "APPROVAL-940"
DELEGATION_APPROVAL = "APPROVAL-941"
DELEGATE_APPROVAL = "APPROVAL-942"
REVOCATION_APPROVAL = "APPROVAL-943"
APPROVAL_PLAN = "PERSIST-20260730T021000Z-001"
OWNER_AUTHORITY = "AUTH-GITHUB-INFOCONEX"
DELEGATE_AUTHORITY = "AUTH-DELEGATE-ALPHA"
OPERATOR = "chatgpt-session"
ROOT = f".flywheel/operations/records/{MISSION}/{GOAL}"
TARGET_PATH = "src/app/package.yaml"
ADDED_DEPENDENCY = "example-package@1.2.3"


def dump(value: dict[str, Any]) -> str:
    return (
        yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120)
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .lstrip("\ufeff")
    )


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def git_blob_sha(text: str) -> str:
    raw = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(raw)}\0".encode("utf-8") + raw).hexdigest()


def snapshot(value: dict[str, Any]) -> dict[str, Any]:
    text = dump(value)
    return {
        "data": value,
        "yaml": text,
        "sha256": sha256(text),
        "git_blob_sha": git_blob_sha(text),
        "bytes": len(text.encode("utf-8")),
    }


def stage(
    status: str,
    started_at: str | None = None,
    completed_at: str | None = None,
    summary: str | None = None,
    refs: list[str] | None = None,
    reason: str | None = None,
) -> dict[str, Any]:
    return {
        "status": status,
        "started_at": started_at,
        "completed_at": completed_at,
        "summary": summary,
        "refs": refs or [],
        "reason": reason,
    }


def mission() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": MISSION,
        "title": "Verify Approval Boundary",
        "status": "active",
        "objective": "Verify that approval-required work cannot begin before exact durable approval.",
        "constraints": ["Synthetic read-only verification."],
        "success_criteria": [
            {
                "id": "MSC-940",
                "statement": "Approval authority, scope, durability, timing, and invalidation are deterministic.",
            }
        ],
        "goals": [GOAL],
        "approvals_required": [],
    }


def goal() -> dict[str, Any]:
    statements = [
        "Resolve the approval authority registry.",
        "Stop material work before durable approval.",
        "Validate exact owner approval scope.",
        "Validate approval persistence before action.",
        "Resolve delegated authority and containment.",
        "Resolve revocation and supersession.",
        "Reject invalid authorization fixtures.",
        "Preserve repository immutability.",
    ]
    criteria = [
        {"id": f"AC-{940 + index}", "statement": statement}
        for index, statement in enumerate(statements)
    ]
    return {
        "schema_version": 1,
        "id": GOAL,
        "mission_id": MISSION,
        "title": "Enforce Material Approval",
        "status": "active",
        "objective": "Verify the dependency-addition approval boundary.",
        "depends_on": [],
        "blocked_by": [],
        "procedure": [
            "Construct a pending material adaptation.",
            "Resolve exact durable authorization.",
            "Evaluate invalid approval fixtures.",
        ],
        "acceptance_criteria": criteria,
        "evidence_required": [
            {
                "criterion_id": criterion["id"],
                "evidence_types": ["deterministic-fixture-verification"],
            }
            for criterion in criteria
        ],
        "constraints": ["Read-only synthetic verification."],
        "approvals_required": [],
    }


def adaptation(authorized: bool) -> dict[str, Any]:
    return {
        "id": ADAPTATION,
        "type": "configuration",
        "statement": f"Add {ADDED_DEPENDENCY} to {TARGET_PATH}.",
        "classification_refs": ["CLASS-940"],
        "evaluation_refs": ["EVAL-940"],
        "observation_refs": ["OBS-940"],
        "evidence_refs": [EVIDENCE],
        "affected_scope": [TARGET_PATH],
        "rationale": "The synthetic feature requires one new package.",
        "intended_effect": "Provide the required synthetic feature capability.",
        "alternatives": [
            "Implement the capability without a new dependency.",
            "Defer the feature.",
        ],
        "certainty": "confirmed",
        "uncertainty": None,
        "scope_disposition": "within-goal",
        "approval_required": True,
        "approval_status": "approved" if authorized else "pending",
        "approval_refs": [OWNER_APPROVAL] if authorized else [],
        "decision_ref": DECISION if authorized else None,
        "disposition": "approved" if authorized else "proposed",
        "implementation_status": "not-started",
        "validation_status": "not-started",
        "persistence_status": "not-persisted",
        "reuse_status": "not-assessed",
    }


def execution(authorized: bool) -> dict[str, Any]:
    lifecycle = {
        "execute": stage(
            "completed",
            "2026-07-30T02:00:00Z",
            "2026-07-30T02:02:00Z",
            "Constructed the synthetic work request.",
            ["ACT-940"],
        ),
        "observe": stage(
            "completed",
            "2026-07-30T02:02:00Z",
            "2026-07-30T02:04:00Z",
            "Observed the material dependency requirement.",
            ["OBS-940"],
        ),
        "evaluate": stage(
            "completed",
            "2026-07-30T02:04:00Z",
            "2026-07-30T02:05:00Z",
            "Evaluated alternatives and constraints.",
            ["EVAL-940"],
        ),
        "classify": stage(
            "completed",
            "2026-07-30T02:05:00Z",
            "2026-07-30T02:06:00Z",
            "Classified the change as material and approval-required.",
            ["CLASS-940"],
        ),
        "adapt": stage("in-progress", "2026-07-30T02:06:00Z", refs=[ADAPTATION]),
        "validate": stage("pending"),
        "persist": stage("pending"),
        "reuse": stage("pending"),
    }
    return {
        "schema_version": 1,
        "id": EXECUTION,
        "mission_id": MISSION,
        "goal_id": GOAL,
        "status": "in-progress",
        "intended_outcome": "Verify deterministic approval gating for a material dependency addition.",
        "acceptance_criteria": [f"AC-{value}" for value in range(940, 948)],
        "started_at": "2026-07-30T02:00:00Z",
        "completed_at": None,
        "lifecycle": lifecycle,
        "actions": ["ACT-940: Describe the proposed dependency addition without implementing it."],
        "observations": [
            {
                "id": "OBS-940",
                "statement": "The proposed work adds a dependency.",
                "type": "direct",
                "status": "complete",
                "observed_at": "2026-07-30T02:03:00Z",
                "source_or_method": "Synthetic fixture inspection.",
                "evidence_refs": [EVIDENCE],
                "uncertainty": None,
                "conflicts_with": [],
            }
        ],
        "evaluations": [
            {
                "id": "EVAL-940",
                "statement": "The dependency is material and governed by add_dependency.",
                "result": "supports",
                "observation_refs": ["OBS-940"],
                "evidence_refs": [EVIDENCE],
                "criterion_refs": ["AC-941", "AC-942", "AC-943"],
                "rule_refs": ["APPROVAL-DURABLE-001", "ADAPTATION-APPROVAL-001"],
                "limitations": ["Synthetic only."],
                "rationale": "Governance explicitly marks add_dependency approval-required.",
            }
        ],
        "classifications": [
            {
                "id": "CLASS-940",
                "type": "decision",
                "statement": "The dependency addition requires human approval.",
                "evaluation_refs": ["EVAL-940"],
                "evidence_refs": [EVIDENCE],
                "rationale": "The action matrix marks add_dependency approval-required.",
                "certainty": "confirmed",
                "uncertainty": None,
                "conflicts_with": [],
                "related_classification_refs": [],
                "decision_ref": DECISION,
                "finding_ref": None,
                "validation_refs": [],
            }
        ],
        "adaptations": [adaptation(authorized)],
        "blockers": [],
        "approval_refs": [OWNER_APPROVAL] if authorized else [],
        "evidence_refs": [EVIDENCE],
        "decision_refs": [DECISION],
        "finding_refs": [],
        "validation_results": [],
        "outcome": None,
        "completion": {"disposition": None, "rationale": None},
    }


def evidence_record() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": EVIDENCE,
        "kind": "evidence",
        "mission_id": MISSION,
        "goal_id": GOAL,
        "execution_id": EXECUTION,
        "created_at": "2026-07-30T02:07:00Z",
        "created_by": OPERATOR,
        "summary": "Evidence for the requested dependency addition and human decision.",
        "status": "accepted",
        "classification": "approval-evidence",
        "criterion_ids": ["AC-941", "AC-942", "AC-943"],
        "source_refs": ["governance:add_dependency", "human-direction:2026-07-30T02:08:00Z"],
        "artifact_refs": [ADAPTATION, TARGET_PATH],
        "evidence": {
            "evidence_type": "approval-request",
            "supported_claim": "The exact dependency addition was presented for human decision.",
            "source_or_method": "Synthetic durable request and decision capture.",
            "actual_result": "Repository owner approved the exact action and target with a version constraint.",
            "observed_at": "2026-07-30T02:09:00Z",
            "storage_location": f"{ROOT}/evidence/{EVIDENCE}.yaml",
        },
        "decision": None,
        "finding": None,
        "approval": None,
    }


def decision_record() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": DECISION,
        "kind": "decision",
        "mission_id": MISSION,
        "goal_id": GOAL,
        "execution_id": EXECUTION,
        "created_at": "2026-07-30T02:09:00Z",
        "created_by": OWNER_AUTHORITY,
        "summary": "Authorize the exact dependency addition.",
        "status": "accepted",
        "classification": "material-adaptation-decision",
        "criterion_ids": ["AC-942", "AC-943"],
        "source_refs": [EVIDENCE],
        "artifact_refs": [ADAPTATION, TARGET_PATH],
        "evidence": None,
        "decision": {
            "decision": f"Authorize {ADDED_DEPENDENCY} for {TARGET_PATH}.",
            "rationale": "The exact constrained dependency is acceptable for the synthetic goal.",
            "authority": OWNER_AUTHORITY,
            "decided_at": "2026-07-30T02:09:00Z",
            "alternatives_considered": ["Implement without a dependency.", "Defer the feature."],
            "validation_disposition": None,
        },
        "finding": None,
        "approval": None,
    }


def approval_scope(
    action: str,
    targets: list[str],
    constraints: list[str],
    delegate_authority_id: str | None = None,
    delegated_actions: list[str] | None = None,
    delegated_targets: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "mission_id": MISSION,
        "goal_id": GOAL,
        "execution_id": EXECUTION,
        "action": action,
        "target_refs": targets,
        "constraints": constraints,
        "delegate_authority_id": delegate_authority_id,
        "delegated_actions": delegated_actions or [],
        "delegated_target_refs": delegated_targets or [],
    }


def approval_record(
    approval_id: str,
    authority_id: str,
    authority_role: str,
    authorization_basis: str,
    decision: str,
    scope: dict[str, Any],
    created_at: str,
    effective_at: str,
    expires_at: str | None,
    delegation_ref: str | None = None,
    supersedes_ref: str | None = None,
    revokes_ref: str | None = None,
    status: str = "accepted",
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": approval_id,
        "kind": "approval",
        "mission_id": MISSION,
        "goal_id": GOAL,
        "execution_id": EXECUTION,
        "created_at": created_at,
        "created_by": authority_id,
        "summary": f"{decision.title()} approval for {scope['action']}.",
        "status": status,
        "classification": "approval-boundary",
        "criterion_ids": ["AC-942", "AC-943", "AC-944", "AC-945"],
        "source_refs": [EVIDENCE, DECISION],
        "artifact_refs": scope["target_refs"],
        "approval": {
            "authority_id": authority_id,
            "authority_role": authority_role,
            "authorization_basis": authorization_basis,
            "decision": decision,
            "scope": scope,
            "decided_at": created_at,
            "effective_at": effective_at,
            "expires_at": expires_at,
            "evidence_refs": [EVIDENCE],
            "delegation_ref": delegation_ref,
            "supersedes_ref": supersedes_ref,
            "revokes_ref": revokes_ref,
        },
    }


def owner_approval() -> dict[str, Any]:
    return approval_record(
        OWNER_APPROVAL,
        OWNER_AUTHORITY,
        "repository-owner",
        "repository-ownership",
        "approved",
        approval_scope(
            "add_dependency",
            [ADAPTATION, TARGET_PATH],
            [f"Only {ADDED_DEPENDENCY} may be added."],
        ),
        "2026-07-30T02:10:00Z",
        "2026-07-30T02:10:00Z",
        "2026-07-30T03:10:00Z",
    )


def delegation_approval() -> dict[str, Any]:
    return approval_record(
        DELEGATION_APPROVAL,
        OWNER_AUTHORITY,
        "repository-owner",
        "repository-ownership",
        "approved",
        approval_scope(
            "delegate_approval_authority",
            [DELEGATE_AUTHORITY],
            ["Delegation is limited to the synthetic execution."],
            delegate_authority_id=DELEGATE_AUTHORITY,
            delegated_actions=["add_dependency"],
            delegated_targets=[ADAPTATION, TARGET_PATH],
        ),
        "2026-07-30T02:10:10Z",
        "2026-07-30T02:10:10Z",
        "2026-07-30T03:10:00Z",
    )


def delegate_approval() -> dict[str, Any]:
    return approval_record(
        DELEGATE_APPROVAL,
        DELEGATE_AUTHORITY,
        "delegate",
        "delegated-authority",
        "approved",
        approval_scope(
            "add_dependency",
            [ADAPTATION, TARGET_PATH],
            [f"Only {ADDED_DEPENDENCY} may be added."],
        ),
        "2026-07-30T02:10:20Z",
        "2026-07-30T02:10:20Z",
        "2026-07-30T02:40:00Z",
        delegation_ref=DELEGATION_APPROVAL,
    )


def revocation_approval() -> dict[str, Any]:
    return approval_record(
        REVOCATION_APPROVAL,
        OWNER_AUTHORITY,
        "repository-owner",
        "repository-ownership",
        "approved",
        approval_scope(
            "revoke_approval",
            [OWNER_APPROVAL],
            ["Revoke before dependency implementation begins."],
        ),
        "2026-07-30T02:10:30Z",
        "2026-07-30T02:10:30Z",
        None,
        revokes_ref=OWNER_APPROVAL,
    )


def approval_plan(approval_snapshot: dict[str, Any]) -> dict[str, Any]:
    path = f"{ROOT}/approvals/{OWNER_APPROVAL}.yaml"
    return {
        "schema_version": 1,
        "id": APPROVAL_PLAN,
        "mission_id": MISSION,
        "goal_id": GOAL,
        "execution_id": EXECUTION,
        "created_at": "2026-07-30T02:10:00Z",
        "operator": OPERATOR,
        "status": "applied",
        "targets": [
            {
                "id": "PT-001",
                "artifact_type": "approval",
                "path": path,
                "operation": "create",
                "mutability": "create-only",
                "dependency_refs": [],
                "expected_precondition": {"absence": True},
                "proposed_content_digest": approval_snapshot["sha256"],
                "rollback": {"mode": "delete-created", "retained_content_digest": None},
            }
        ],
        "write_order": ["PT-001"],
        "recovery": {"mode": "not-started", "finding_ref": None, "blocker": None},
        "final_verification": {
            "required": True,
            "verified_at": "2026-07-30T02:10:05Z",
            "result": "passed",
        },
    }


APPROVAL_REQUIRED_FIELDS = {
    "authority_id",
    "authority_role",
    "authorization_basis",
    "decision",
    "scope",
    "decided_at",
    "effective_at",
    "expires_at",
    "evidence_refs",
    "delegation_ref",
    "supersedes_ref",
    "revokes_ref",
}
SCOPE_REQUIRED_FIELDS = {
    "mission_id",
    "goal_id",
    "execution_id",
    "action",
    "target_refs",
    "constraints",
    "delegate_authority_id",
    "delegated_actions",
    "delegated_target_refs",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def schema_like_check(record: dict[str, Any]) -> None:
    require(record["kind"] == "approval", "kind must be approval")
    require(record["id"].startswith("APPROVAL-"), "approval identity required")
    require(bool(record["source_refs"]), "source_refs required")
    approval = record["approval"]
    require(APPROVAL_REQUIRED_FIELDS <= approval.keys(), "missing approval field")
    scope = approval["scope"]
    require(SCOPE_REQUIRED_FIELDS <= scope.keys(), "missing scope field")
    require(bool(scope["target_refs"]), "target_refs required")
    require(bool(approval["evidence_refs"]), "evidence_refs required")
    require(
        record["mission_id"] == scope["mission_id"]
        and record["goal_id"] == scope["goal_id"]
        and record["execution_id"] == scope["execution_id"],
        "top-level and scope context must agree",
    )
    if approval["authority_role"] == "repository-owner":
        require(
            approval["authorization_basis"] == "repository-ownership"
            and approval["delegation_ref"] is None,
            "owner authority relationship invalid",
        )
    if approval["authority_role"] == "delegate":
        require(
            approval["authorization_basis"] == "delegated-authority"
            and bool(approval["delegation_ref"]),
            "delegate authority relationship invalid",
        )
    if scope["action"] == "delegate_approval_authority":
        require(
            bool(scope["delegate_authority_id"]) and bool(scope["delegated_actions"]),
            "delegation scope incomplete",
        )
    else:
        require(
            scope["delegate_authority_id"] is None
            and not scope["delegated_actions"]
            and not scope["delegated_target_refs"],
            "non-delegation scope carries delegated authority fields",
        )
    if scope["action"] == "revoke_approval":
        require(bool(approval["revokes_ref"]), "revocation reference required")
    if approval["revokes_ref"] is not None:
        require(scope["action"] == "revoke_approval", "revocation action required")


def rejected_by_shape(base: dict[str, Any], mutate) -> bool:
    item = copy.deepcopy(base)
    mutate(item)
    try:
        schema_like_check(item)
        return False
    except (AssertionError, KeyError, TypeError):
        return True


def main() -> int:
    owner = snapshot(owner_approval())
    artifacts = {
        "mission": snapshot(mission()),
        "goal": snapshot(goal()),
        "execution_pending": snapshot(execution(False)),
        "evidence": snapshot(evidence_record()),
        "decision": snapshot(decision_record()),
        "owner_approval": owner,
        "approval_plan_applied": snapshot(approval_plan(owner)),
        "execution_authorized": snapshot(execution(True)),
        "delegation_approval": snapshot(delegation_approval()),
        "delegate_approval": snapshot(delegate_approval()),
        "revocation_approval": snapshot(revocation_approval()),
    }

    pending_adaptation = artifacts["execution_pending"]["data"]["adaptations"][0]
    authorized_adaptation = artifacts["execution_authorized"]["data"]["adaptations"][0]
    approval_data = owner["data"]

    checks = {
        "pending_implementation_not_started": (
            pending_adaptation["approval_status"] == "pending"
            and pending_adaptation["approval_refs"] == []
            and pending_adaptation["decision_ref"] is None
            and pending_adaptation["implementation_status"] == "not-started"
        ),
        "owner_scope_exact": (
            approval_data["approval"]["scope"]["action"] == "add_dependency"
            and approval_data["approval"]["scope"]["target_refs"] == [ADAPTATION, TARGET_PATH]
        ),
        "approval_plan_applied": (
            artifacts["approval_plan_applied"]["data"]["status"] == "applied"
            and artifacts["approval_plan_applied"]["data"]["final_verification"]["result"] == "passed"
        ),
        "authorized_execution_references_approval": (
            authorized_adaptation["approval_status"] == "approved"
            and authorized_adaptation["approval_refs"] == [OWNER_APPROVAL]
            and authorized_adaptation["decision_ref"] == DECISION
            and authorized_adaptation["implementation_status"] == "not-started"
        ),
        "delegation_scope_structured": (
            artifacts["delegation_approval"]["data"]["approval"]["scope"]["delegate_authority_id"] == DELEGATE_AUTHORITY
            and artifacts["delegation_approval"]["data"]["approval"]["scope"]["delegated_actions"] == ["add_dependency"]
        ),
        "delegate_references_delegation": (
            artifacts["delegate_approval"]["data"]["approval"]["delegation_ref"] == DELEGATION_APPROVAL
        ),
        "revocation_references_owner_approval": (
            artifacts["revocation_approval"]["data"]["approval"]["revokes_ref"] == OWNER_APPROVAL
            and artifacts["revocation_approval"]["data"]["approval"]["scope"]["action"] == "revoke_approval"
        ),
    }

    for name in ["owner_approval", "delegation_approval", "delegate_approval", "revocation_approval"]:
        try:
            schema_like_check(artifacts[name]["data"])
        except AssertionError:
            checks[f"{name}_shape"] = False
        else:
            checks[f"{name}_shape"] = True

    direct_negative_cases = {
        "missing_authority_id": rejected_by_shape(approval_data, lambda value: value["approval"].pop("authority_id")),
        "missing_scope_field": rejected_by_shape(approval_data, lambda value: value["approval"]["scope"].pop("action")),
        "empty_targets": rejected_by_shape(approval_data, lambda value: value["approval"]["scope"].update({"target_refs": []})),
        "missing_evidence_refs": rejected_by_shape(approval_data, lambda value: value["approval"].update({"evidence_refs": []})),
        "owner_with_delegation_ref": rejected_by_shape(approval_data, lambda value: value["approval"].update({"delegation_ref": DELEGATION_APPROVAL})),
        "delegate_without_delegation_ref": rejected_by_shape(delegate_approval(), lambda value: value["approval"].update({"delegation_ref": None})),
        "delegation_missing_delegated_actions": rejected_by_shape(delegation_approval(), lambda value: value["approval"]["scope"].update({"delegated_actions": []})),
        "nondelegation_carries_delegated_fields": rejected_by_shape(approval_data, lambda value: value["approval"]["scope"].update({"delegate_authority_id": DELEGATE_AUTHORITY, "delegated_actions": ["add_dependency"]})),
        "revocation_missing_revokes_ref": rejected_by_shape(revocation_approval(), lambda value: value["approval"].update({"revokes_ref": None})),
        "revocation_ref_with_wrong_action": rejected_by_shape(approval_data, lambda value: value["approval"].update({"revokes_ref": OWNER_APPROVAL})),
        "context_mismatch": rejected_by_shape(approval_data, lambda value: value["approval"]["scope"].update({"goal_id": "wrong-goal"})),
        "missing_source_refs": rejected_by_shape(approval_data, lambda value: value.update({"source_refs": []})),
    }

    checks["all_direct_negative_cases_rejected"] = all(direct_negative_cases.values())
    checks["artifact_count"] = len(artifacts) == 11

    output = {
        "framework_revision": FRAMEWORK_REVISION,
        "result": "passed" if all(checks.values()) else "failed",
        "classification_before_approval": "approval-required action blocked",
        "classification_after_durable_approval": "exact approved action authorized",
        "action": "add_dependency",
        "target_path": TARGET_PATH,
        "dependency": ADDED_DEPENDENCY,
        "action_time": "2026-07-30T02:11:00Z",
        "checks": checks,
        "direct_negative_cases": direct_negative_cases,
        "artifacts": artifacts,
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["result"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
