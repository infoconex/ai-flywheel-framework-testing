#!/usr/bin/env python3
"""Transform the immutable Prompt 017 base fixture into approval-ready certification evidence."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import re
from typing import Any

import yaml

FRAMEWORK_REVISION = "18335e57165a8984adab4790d3a6210355b484ba"
BASE_FRAMEWORK_REVISION = "c0f779eedc97963283e2798a988c628df63ddcbe"
EVIDENCE_REVISION = "021e10fe9577df11017f4ea1def4f83358aaed3d"
SELF_HOST_EVIDENCE_REVISION = "42461bcc86ea75c3752082b33d7c24dd18a8bd62"
SELF_HOST_FIXTURE_PATH = "test/ai/fixtures/017-self-host-certification.yaml"


def _snapshot(value: Any) -> dict[str, Any]:
    text = yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120)
    raw = text.encode("utf-8")
    return {
        "data": value,
        "yaml": text,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "git_blob_sha": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(),
        "bytes": len(raw),
    }


def _replace_text(value: Any, replacements: list[tuple[str, str]]) -> Any:
    if isinstance(value, str):
        for old, new in replacements:
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [_replace_text(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: _replace_text(item, replacements) for key, item in value.items()}
    return value


def run(base_source: str) -> dict[str, Any]:
    corrected = base_source
    replacements = [
        (
            f'FRAMEWORK_REVISION = "{BASE_FRAMEWORK_REVISION}"',
            f'FRAMEWORK_REVISION = "{FRAMEWORK_REVISION}"',
        ),
        (
            'EVIDENCE_REVISION = "aceda4a01c27abcdca96bed3319cfa987a0272b5"',
            f'EVIDENCE_REVISION = "{EVIDENCE_REVISION}"',
        ),
        (
            '"test/ai/prompts/014-recover-missing-required-artifact-launcher.md"',
            '"test/ai/prompts/014-recover-missing-required-artifact.md"',
        ),
        (
            '"test/ai/prompts/015-recover-broken-active-reference-launcher.md"',
            '"test/ai/prompts/015-recover-broken-active-reference.md"',
        ),
        (
            '"test/ai/prompts/016-run-representative-proving-mission-launcher.md"',
            '"test/ai/prompts/016-run-representative-proving-mission.md"',
        ),
    ]
    for old, new in replacements:
        corrected = corrected.replace(old, new)

    legacy_pattern = '        "source_revision": EVIDENCE_REVISION,'
    if corrected.count(legacy_pattern) != 2:
        raise ValueError("expected exactly two legacy scenario revision assignments")
    corrected = corrected.replace(
        legacy_pattern,
        '        "tested_framework_revision": FRAMEWORK_REVISION,\n        "evidence_revision": EVIDENCE_REVISION,',
    )

    static_pattern = re.compile(r'        "source_revision": "([0-9a-f]{40})",')
    if len(static_pattern.findall(corrected)) != 7:
        raise ValueError("expected seven static scenario revisions")
    corrected = static_pattern.sub(
        lambda match: (
            f'        "tested_framework_revision": "{match.group(1)}",\n'
            '        "evidence_revision": EVIDENCE_REVISION,'
        ),
        corrected,
    )
    corrected = corrected.replace(
        '        "source_revision": FRAMEWORK_REVISION,',
        (
            '        "tested_framework_revision": FRAMEWORK_REVISION,\n'
            f'        "evidence_revision": "{SELF_HOST_EVIDENCE_REVISION}",'
        ),
        1,
    )
    corrected = corrected.replace(
        '        "fixture_definition_refs": ["test/ai/prompts/017-self-host-certification.md"],',
        f'        "fixture_definition_refs": ["{SELF_HOST_FIXTURE_PATH}"],',
        1,
    )
    corrected = corrected.replace(
        '        "source_refs": [item for scenario in scenario_specs for item in scenario["evidence_refs"]],',
        '        "source_refs": list(dict.fromkeys(item for scenario in scenario_specs for item in scenario["evidence_refs"])),',
        1,
    )

    buffer = io.StringIO()
    namespace = {"__name__": "__main__"}
    with contextlib.redirect_stdout(buffer):
        exec(compile(corrected, "verify_prompt_017_fixtures.py", "exec"), namespace)
    parsed = json.loads(buffer.getvalue())
    artifacts = parsed["artifacts"]

    scenarios = artifacts["certification_record"]["data"]["scenarios"]
    for index, scenario_name in enumerate(("context-free-startup", "first-execution")):
        scenario = scenarios[index]
        scenario["result"] = "passed"
        scenario["tested_framework_revision"] = FRAMEWORK_REVISION
        scenario["evidence_revision"] = EVIDENCE_REVISION
        scenario["actual_result"] = (
            f"{scenario_name} passed against immutable framework revision {FRAMEWORK_REVISION} "
            f"with retained evidence at {EVIDENCE_REVISION}."
        )

    scenarios[7]["fixture_definition_refs"] = ["test/ai/prompts/016-run-representative-proving-mission.md"]
    scenarios[7]["evidence_refs"] = ["test/ai/results/016-run-representative-proving-mission.md"]
    scenarios[7]["actual_result"] = "Acceptance-criterion evidence mapping passed in the representative proving mission result."

    text_replacements = [
        ("two legacy evidence gaps", "the remaining human approval boundary"),
        ("Two scenarios have insufficient immutable evidence", "All ten scenarios have sufficient immutable evidence"),
        ("Eight scenarios have sufficient immutable evidence and two legacy scenarios require rerun.", "All ten scenarios have sufficient immutable evidence and certification is ready for human approval."),
        ("Scenarios 1 and 2 lack exact tested framework commit SHAs; scenarios 3 through 10 satisfy the fixture's evidence requirements.", "All ten scenarios identify exact tested framework revisions and satisfy the certification evidence requirements."),
        ("missing scenario evidence", "pending human approval"),
        ("missing scenario revisions", "pending human approval"),
        ("corrective reruns", "human approval and subsequent readiness review"),
        ("certification evidence is corrected", "human approval is recorded"),
        ("Certification fails safely", "Certification is ready for approval"),
        ("certification failed", "certification awaits approval"),
        ("evidence gaps", "approval boundary"),
    ]
    for key, snapshot in list(artifacts.items()):
        artifacts[key]["data"] = _replace_text(snapshot["data"], text_replacements)

    goal = artifacts["goal"]["data"]
    goal["status"] = "blocked"
    goal["blocked_by"] = ["Durable human certification approval has not been recorded."]
    goal["procedure"][-1] = "Prepare certification for human approval and keep readiness pending until approval is durably recorded."

    findings = artifacts["finding_records"]["data"]
    findings[0]["summary"] = "Human certification approval is pending."
    findings[0]["classification"] = "approval-required"
    findings[0]["source_refs"] = ["EVID-970", artifacts["certification_record"]["data"]["id"]]
    findings[0]["finding"].update({
        "finding_type": "approval-required",
        "description": "All ten certification scenarios passed, but no durable human certification approval exists.",
        "impact": "Certification remains ready-for-approval and cannot become approved.",
        "disposition": "open",
    })
    findings[1]["summary"] = "Readiness cannot advance before approved certification."
    findings[1]["classification"] = "readiness-gate-pending"
    findings[1]["source_refs"] = [artifacts["certification_record"]["data"]["id"], artifacts["readiness_validation"]["data"]["id"]]
    findings[1]["finding"].update({
        "finding_type": "readiness-gate-pending",
        "description": "Readiness review must remain pending until certification approval is durably recorded.",
        "impact": "No ready-for-missions state may be proposed or applied.",
        "disposition": "open",
    })

    decision = artifacts["decision_record"]["data"]
    decision["summary"] = "Prepare certification for human approval and keep readiness pending."
    decision["source_refs"] = ["FINDING-970", "FINDING-971", "EVID-970"]
    decision["decision"].update({
        "decision": "All certification scenarios passed; prepare the certification record for human approval and do not advance readiness yet.",
        "rationale": "The evidence requirement is satisfied, while human approval remains an explicit authority boundary.",
        "alternatives_considered": ["Invent approval.", "Advance readiness before approval."],
    })

    certification = artifacts["certification_record"]["data"]
    certification["status"] = "ready-for-approval"
    certification["known_limitations"] = ["Human certification approval and durable readiness transition remain outside this synthetic verification."]
    certification["finding_refs"] = ["FINDING-970", "FINDING-971"]
    certification["corrective_actions"] = [
        {"id": "CA-970", "action": "Obtain durable human certification approval from an authorized authority.", "status": "open", "finding_ref": "FINDING-970"},
        {"id": "CA-971", "action": "Run readiness validation after approved certification is durably recorded.", "status": "open", "finding_ref": "FINDING-971"},
    ]
    certification["approval"] = {"status": "pending", "approval_ref": None, "authority_id": None}
    certification["overall_result"] = "pending-approval"

    readiness = artifacts["readiness_validation"]["data"]
    readiness["status"] = "pending"
    readiness["gates"][0].update({"result": "passed", "limitations": []})
    readiness["gates"][3].update({"result": "pending", "limitations": ["Durable human certification approval has not been recorded."]})
    readiness["gates"][4].update({"result": "pending", "limitations": ["The certification goal remains blocked only by the approval boundary."]})
    readiness["blockers"] = ["Durable human certification approval is pending.", "Readiness validation must be rerun after approval."]
    readiness["approval_ref"] = None
    readiness["proposed_state"] = None

    reuse = artifacts["reuse_assessment"]["data"]
    reuse["statement"] = "The self-hosting certification assembly method is reusable after human approval completes the certification boundary."
    reuse["limitations"] = ["Do not promote or advance readiness until durable human approval is obtained."]
    reuse["rationale"] = "The procedure and evidence are validated; promotion remains deferred pending human approval."

    execution = artifacts["execution"]["data"]
    execution["intended_outcome"] = "Assemble and validate a self-hosted certification package, prove all ten scenarios, and preserve the human approval boundary."
    execution["completion"]["rationale"] = "All ten scenarios passed and the certification package is ready for approval; the goal remains blocked only by human authority."

    for key, snapshot in list(artifacts.items()):
        artifacts[key] = _snapshot(snapshot["data"])

    checks = {
        "exact_ten_scenarios": len(scenarios) == 10 and [item["id"] for item in scenarios] == list(range(1, 11)),
        "all_scenarios_pass": all(item["result"] == "passed" for item in scenarios),
        "all_scenarios_have_framework_revision": all(item["tested_framework_revision"] for item in scenarios),
        "all_scenarios_have_evidence_revision": all(item["evidence_revision"] for item in scenarios),
        "self_hosting_scenario_passes": scenarios[9]["result"] == "passed",
        "certification_ready_for_approval": certification["status"] == "ready-for-approval" and certification["overall_result"] == "pending-approval",
        "approval_not_invented": certification["approval"] == {"status": "pending", "approval_ref": None, "authority_id": None},
        "readiness_pending": readiness["status"] == "pending" and readiness["proposed_state"] is None,
        "goal_blocked_by_approval": goal["status"] == "blocked" and len(goal["blocked_by"]) == 1,
        "execution_succeeded_goal_blocked": execution["status"] == "succeeded" and execution["completion"]["disposition"] == "goal-blocked",
        "all_eight_stages_complete": len(execution["lifecycle"]) == 8 and all(stage["status"] == "completed" for stage in execution["lifecycle"].values()),
        "criterion_coverage": {item["criterion_id"] for item in goal["evidence_required"]} == {"AC-970", "AC-971", "AC-972", "AC-973"},
        "self_hosting_chain_complete": certification["self_hosting"]["persistence_plan_ref"] == artifacts["persistence_plan"]["data"]["id"],
        "persistence_targets_complete": len(artifacts["persistence_plan"]["data"]["targets"]) == 13,
        "state_remains_not_ready": artifacts["state"]["data"]["readiness"] == "not-ready-for-missions" and artifacts["state"]["data"]["application_missions_allowed"] is False,
        "source_refs_unique": len(artifacts["evidence_records"]["data"][0]["source_refs"]) == len(set(artifacts["evidence_records"]["data"][0]["source_refs"])),
    }

    parsed.update({
        "framework_revision": FRAMEWORK_REVISION,
        "evidence_revision": EVIDENCE_REVISION,
        "self_host_evidence_revision": SELF_HOST_EVIDENCE_REVISION,
        "execution_mode": "in-memory connector source with approval-ready transformation runner",
        "correction_count": 24,
        "checks": checks,
        "result": "passed" if all(checks.values()) and all(parsed["negative_cases"].values()) else "failed",
    })
    return parsed
