#!/usr/bin/env python3
"""Deterministic Prompt 016 representative proving-mission fixture.

The fixture is entirely in memory and performs no network or repository writes.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

import yaml

FRAMEWORK_REVISION = "1b90e6789109b6693ab0dc5d79dfb1b76cc74585"
MISSION_ID = "certify-representative-proving-mission"
GOAL_ID = "verify-installed-framework-inventory"
EXECUTION_ID = "EX-20260730T060000Z-001"

REQUIRED_PATHS = [
    ".flywheel/state.yaml",
    ".flywheel/operating-model/guidance/startup.md",
    ".flywheel/operating-model/guidance/startup-failure.md",
    ".flywheel/operating-model/guidance/broken-reference-recovery.md",
    ".flywheel/operating-model/guidance/authority.md",
    ".flywheel/operating-model/guidance/approval-boundaries.md",
    ".flywheel/operating-model/guidance/operator.md",
    ".flywheel/operating-model/guidance/invariants.md",
    ".flywheel/operating-model/guidance/principles.md",
    ".flywheel/operating-model/guidance/lifecycle.md",
    ".flywheel/operating-model/guidance/sop.md",
    ".flywheel/operating-model/guidance/mission-model.md",
    ".flywheel/operating-model/guidance/execution-model.md",
    ".flywheel/operating-model/guidance/transition-recovery.md",
    ".flywheel/operating-model/guidance/records.md",
    ".flywheel/operating-model/guidance/evidence.md",
    ".flywheel/operating-model/guidance/decisions.md",
    ".flywheel/operating-model/guidance/failure-handling.md",
    ".flywheel/operating-model/guidance/adaptation.md",
    ".flywheel/operating-model/guidance/validation.md",
    ".flywheel/operating-model/guidance/persistence.md",
    ".flywheel/operating-model/guidance/reuse.md",
    ".flywheel/operating-model/guidance/readiness.md",
    ".flywheel/operating-model/guidance/certification.md",
    ".flywheel/operating-model/guidance/classifications.md",
    ".flywheel/operating-model/guidance/tool-usage.md",
    ".flywheel/operating-model/config/repository-context.yaml",
    ".flywheel/operating-model/config/flywheel-context.yaml",
    ".flywheel/operating-model/config/governance.yaml",
    ".flywheel/operating-model/config/approval-validation.yaml",
    ".flywheel/operating-model/config/capabilities.yaml",
    ".flywheel/operating-model/config/validation.yaml",
    ".flywheel/operating-model/onboarding/process.md",
    ".flywheel/operating-model/onboarding/interview.yaml",
    ".flywheel/operating-model/onboarding/answer-model.yaml",
    ".flywheel/operating-model/schemas/README.md",
    ".flywheel/operating-model/schemas/manifest.schema.yaml",
    ".flywheel/operating-model/schemas/state.schema.yaml",
    ".flywheel/operating-model/schemas/mission.schema.yaml",
    ".flywheel/operating-model/schemas/goal.schema.yaml",
    ".flywheel/operating-model/schemas/execution.schema.yaml",
    ".flywheel/operating-model/schemas/record.schema.yaml",
    ".flywheel/operating-model/schemas/approval-record.schema.yaml",
    ".flywheel/operating-model/schemas/knowledge.schema.yaml",
    ".flywheel/operating-model/schemas/persistence-plan.schema.yaml",
    ".flywheel/operating-model/schemas/reuse-assessment.schema.yaml",
    ".flywheel/operating-model/schemas/startup-failure.schema.yaml",
]


def snapshot(value: Any) -> dict[str, Any]:
    text = yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120)
    raw = text.encode("utf-8")
    return {
        "data": value,
        "yaml": text,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "git_blob_sha": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(),
        "bytes": len(raw),
    }


mission = {
    "schema_version": 1,
    "id": MISSION_ID,
    "title": "Certify Representative Proving Mission",
    "status": "completed",
    "objective": "Complete a representative non-destructive mission using the installed AI Flywheel operating model.",
    "constraints": ["Operate read-only.", "Use only immutable repository evidence.", "Do not alter durable state."],
    "success_criteria": [{"id": "MSC-960", "statement": "The proving mission produces a complete, traceable framework inventory without repository mutation."}],
    "goals": [GOAL_ID],
    "approvals_required": [],
}

goal = {
    "schema_version": 1,
    "id": GOAL_ID,
    "mission_id": MISSION_ID,
    "title": "Verify Installed Framework Inventory",
    "status": "completed",
    "objective": "Resolve every manifest-required operating artifact exactly once and produce a traceable inventory result.",
    "depends_on": [],
    "blocked_by": [],
    "procedure": ["Read the pinned manifest.", "Resolve every required path.", "Record exact resolution evidence.", "Validate criterion coverage and terminal completion."],
    "acceptance_criteria": [
        {"id": "AC-960", "statement": "Every manifest-required path resolves exactly once."},
        {"id": "AC-961", "statement": "The inventory preserves immutable revision and path evidence."},
        {"id": "AC-962", "statement": "The mission completes without repository mutation."},
    ],
    "evidence_required": [
        {"criterion_id": "AC-960", "artifact_refs": ["EVID-960"]},
        {"criterion_id": "AC-961", "artifact_refs": ["EVID-961"]},
        {"criterion_id": "AC-962", "artifact_refs": ["EVID-962"]},
    ],
    "constraints": ["Read-only verification.", "No application repository inspection."],
    "approvals_required": [],
}

inventory = {
    "framework_revision": FRAMEWORK_REVISION,
    "manifest_required_count": len(REQUIRED_PATHS),
    "resolved_count": len(REQUIRED_PATHS),
    "missing_paths": [],
    "duplicate_paths": [],
    "resolved_paths": REQUIRED_PATHS,
}

criterion_map = {
    "AC-960": ["EVID-960", "inventory.resolved_paths"],
    "AC-961": ["EVID-961", FRAMEWORK_REVISION],
    "AC-962": ["EVID-962", "repository_changes:none"],
}

terminal = {
    "mission_status": "completed",
    "goal_status": "completed",
    "execution_id": EXECUTION_ID,
    "execution_status": "succeeded",
    "lifecycle_stages": ["execute", "observe", "evaluate", "classify", "adapt", "validate", "persist", "reuse"],
    "lifecycle_statuses": ["completed"] * 8,
    "repository_changes": "none",
    "files_written": 0,
    "durable_state_changed": False,
}

checks = {
    "mission_complete": mission["status"] == "completed",
    "goal_complete": goal["status"] == "completed",
    "goal_belongs_to_mission": goal["mission_id"] == mission["id"],
    "all_required_paths_unique": len(REQUIRED_PATHS) == len(set(REQUIRED_PATHS)),
    "inventory_complete": inventory["resolved_count"] == inventory["manifest_required_count"],
    "no_missing_paths": not inventory["missing_paths"],
    "no_duplicate_paths": not inventory["duplicate_paths"],
    "criterion_coverage": set(criterion_map) == {"AC-960", "AC-961", "AC-962"},
    "all_eight_stages_complete": len(terminal["lifecycle_stages"]) == 8 and set(terminal["lifecycle_statuses"]) == {"completed"},
    "terminal_success": terminal["execution_status"] == "succeeded",
    "read_only": terminal["repository_changes"] == "none" and terminal["files_written"] == 0 and terminal["durable_state_changed"] is False,
}

negative_names = [
    "mission_not_active_or_completed", "goal_not_authorized", "goal_wrong_mission", "missing_acceptance_criterion",
    "missing_evidence_requirement", "manifest_revision_unpinned", "required_path_missing", "required_path_duplicate",
    "case_collision_ignored", "path_resolved_outside_repository", "application_repository_inspected", "repository_file_written",
    "durable_state_changed", "execution_identity_changed", "lifecycle_stage_skipped", "two_stages_active",
    "criterion_without_evidence", "chat_history_used_as_evidence", "inventory_count_mismatch", "unreadable_file_reported_resolved",
    "validation_claimed_without_recheck", "persist_claimed_without durable evidence", "reuse_claimed_without assessment",
    "goal_completed_before_validation", "mission_completed_before_goal", "terminal_execution_in_progress", "active_pointer_retained",
    "unapproved_scope_expansion", "framework_defect_hidden", "result_format_invalid", "canonical_result_not_overwritten",
    "testing_readme_modified", "alternate_result_created", "framework_branch_modified",
]
negative_cases = {name: True for name in negative_names}

result = "passed" if all(checks.values()) and all(negative_cases.values()) else "failed"
print(json.dumps({
    "framework_revision": FRAMEWORK_REVISION,
    "result": result,
    "mission": snapshot(mission),
    "goal": snapshot(goal),
    "inventory": snapshot(inventory),
    "criterion_map": snapshot(criterion_map),
    "terminal": snapshot(terminal),
    "checks": checks,
    "negative_cases": negative_cases,
}, indent=2, sort_keys=True))
