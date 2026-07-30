#!/usr/bin/env python3
"""Deterministic Prompt 014 missing-required-artifact fixture generator.

No network access and no repository writes are performed.
"""
from __future__ import annotations

import copy
import hashlib
import json
from typing import Any

import yaml

FRAMEWORK_REVISION = "923c46baf8d4bb400eef71a3507e07d797dcab87"
BRANCH = "feature/resilience-and-recovery-testing"
OPERATOR = "chatgpt-session"
OCCURRED_AT = "2026-07-30T04:00:00Z"
FAILURE_ID = "SF-20260730T040000Z-001"
MISSING_PATH = ".flywheel/operating-model/config/approval-validation.yaml"
FAILURE_PATH = f".flywheel/operations/records/startup-failures/{FAILURE_ID}.yaml"


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


def manifest() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "framework": {
            "name": "AI Flywheel",
            "version": "0.1.0-development",
            "mode": "manual-bootstrap",
            "specification": "https://github.com/Infoconex/ai-flywheel-spec",
        },
        "path_base": "repository-root",
        "entrypoint": ".flywheel/operating-model/guidance/startup.md",
        "locations": {
            "state": ".flywheel/state.yaml",
            "operating_model": ".flywheel/operating-model",
            "missions": ".flywheel/operations/missions",
            "records": ".flywheel/operations/records",
            "knowledge": ".flywheel/operations/knowledge",
            "schemas": ".flywheel/operating-model/schemas",
        },
        "required_files": [
            ".flywheel/state.yaml",
            ".flywheel/operating-model/guidance/startup.md",
            ".flywheel/operating-model/guidance/startup-failure.md",
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
            MISSING_PATH,
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
        ],
        "onboarding": {"mission": "establish-ai-flywheel-operations", "status": "active"},
        "implementation": {"status": "not-created", "manifest": None},
        "compatibility": {
            "application_missions_require_readiness": "ready-for-missions",
            "manual_operation_permitted": True,
        },
    }


def retained_state() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "readiness": "not-ready-for-missions",
        "phase": "onboarding",
        "status": "ready",
        "active_mission": "establish-ai-flywheel-operations",
        "active_goal": "001-discover-repository-and-gather-context",
        "active_execution": None,
        "lifecycle_stage": None,
        "implementation_available": False,
        "application_missions_allowed": False,
        "blockers": [],
        "last_durable_update": {
            "at": "2026-07-29T00:00:00Z",
            "by": "framework-bootstrap",
            "reason": "Initialize onboarding state.",
        },
    }


def startup_failure() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "id": FAILURE_ID,
        "observed_revision": FRAMEWORK_REVISION,
        "branch": BRANCH,
        "operator": OPERATOR,
        "occurred_at": OCCURRED_AT,
        "failed_rules": [
            "STARTUP-REQUIRED-FILE-001",
            "STARTUP-FAILURE-BOUNDARY-001",
        ],
        "artifact_paths": [MISSING_PATH],
        "evidence": [
            f"Manifest required_files contains {MISSING_PATH}.",
            f"Fixture path lookup returned absent for {MISSING_PATH}.",
            "No execution existed or was created before the failure was observed.",
        ],
        "recovery_action": (
            "Restore the exact missing required artifact from an authorized, reviewed framework revision "
            "or perform an approved framework repair, then restart startup validation from the manifest."
        ),
        "orphaned_execution_id": None,
    }


def blocked_state() -> dict[str, Any]:
    value = retained_state()
    value["status"] = "blocked"
    value["blockers"] = [f"{FAILURE_ID}: required file missing at {MISSING_PATH}."]
    value["last_durable_update"] = {
        "at": "2026-07-30T04:00:02Z",
        "by": OPERATOR,
        "reason": f"Block active onboarding work after {FAILURE_ID}.",
    }
    return value


def invalid_cases(valid_record: dict[str, Any]) -> dict[str, bool]:
    cases: dict[str, bool] = {}

    def reject(name: str, mutate, predicate) -> None:
        candidate = copy.deepcopy(valid_record)
        mutate(candidate)
        cases[name] = bool(predicate(candidate))

    reject("01_missing_id", lambda x: x.pop("id"), lambda x: "id" not in x)
    reject("02_invalid_id", lambda x: x.__setitem__("id", "SF-INVALID"), lambda x: not x["id"].startswith("SF-20260730T040000Z-"))
    reject("03_wrong_revision", lambda x: x.__setitem__("observed_revision", "0" * 40), lambda x: x["observed_revision"] != FRAMEWORK_REVISION)
    reject("04_fractional_timestamp", lambda x: x.__setitem__("occurred_at", "2026-07-30T04:00:00.1Z"), lambda x: "." in x["occurred_at"])
    reject("05_missing_rule", lambda x: x.__setitem__("failed_rules", []), lambda x: not x["failed_rules"])
    reject("06_missing_path", lambda x: x.__setitem__("artifact_paths", []), lambda x: not x["artifact_paths"])
    reject("07_wrong_path", lambda x: x.__setitem__("artifact_paths", ["approval-validation.yaml"]), lambda x: x["artifact_paths"] != [MISSING_PATH])
    reject("08_missing_evidence", lambda x: x.__setitem__("evidence", []), lambda x: not x["evidence"])
    reject("09_empty_recovery", lambda x: x.__setitem__("recovery_action", ""), lambda x: not x["recovery_action"])
    reject("10_orphaned_execution_invented", lambda x: x.__setitem__("orphaned_execution_id", "EX-20260730T040000Z-001"), lambda x: x["orphaned_execution_id"] is not None)
    reject("11_unknown_field", lambda x: x.__setitem__("repair_content", "invented"), lambda x: "repair_content" in x)
    reject("12_missing_operator", lambda x: x.__setitem__("operator", ""), lambda x: not x["operator"])

    return cases


def main() -> None:
    artifacts = {
        "fixture_manifest": snapshot(manifest()),
        "retained_state": snapshot(retained_state()),
        "startup_failure": snapshot(startup_failure()),
        "optional_blocked_state": snapshot(blocked_state()),
    }

    checks = {
        "missing_path_is_manifest_required": MISSING_PATH in artifacts["fixture_manifest"]["data"]["required_files"],
        "missing_path_is_exact": artifacts["startup_failure"]["data"]["artifact_paths"] == [MISSING_PATH],
        "required_rule_present": "STARTUP-REQUIRED-FILE-001" in artifacts["startup_failure"]["data"]["failed_rules"],
        "boundary_rule_present": "STARTUP-FAILURE-BOUNDARY-001" in artifacts["startup_failure"]["data"]["failed_rules"],
        "no_orphaned_execution": artifacts["startup_failure"]["data"]["orphaned_execution_id"] is None,
        "retained_state_has_no_execution": artifacts["retained_state"]["data"]["active_execution"] is None,
        "blocked_state_has_no_execution": artifacts["optional_blocked_state"]["data"]["active_execution"] is None,
        "blocked_state_has_null_stage": artifacts["optional_blocked_state"]["data"]["lifecycle_stage"] is None,
        "blocked_state_references_failure": FAILURE_ID in artifacts["optional_blocked_state"]["data"]["blockers"][0],
        "recovery_does_not_invent_content": "Restore the exact missing required artifact" in artifacts["startup_failure"]["data"]["recovery_action"],
    }

    negatives = invalid_cases(artifacts["startup_failure"]["data"])
    result = "passed" if all(checks.values()) and all(negatives.values()) else "failed"

    output = {
        "framework_revision": FRAMEWORK_REVISION,
        "branch": BRANCH,
        "result": result,
        "classification": "required operating file missing",
        "operating_validation": "failed",
        "repository_validation": "pending",
        "implementation_validation": "not-applicable",
        "execution_created_or_resumed": False,
        "target_repository_inspected": False,
        "missing_path": MISSING_PATH,
        "startup_failure_id": FAILURE_ID,
        "startup_failure_path": FAILURE_PATH,
        "artifacts": artifacts,
        "checks": checks,
        "negative_cases": negatives,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
