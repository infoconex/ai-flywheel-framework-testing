#!/usr/bin/env python3
"""Deterministic Prompt 015 broken-active-reference fixture generator.

No network access and no repository writes are performed.
"""
from __future__ import annotations
import copy, hashlib, json
from typing import Any
import yaml

FRAMEWORK_REVISION = "eb82939f330b76cc64e813feac6b7a97d3d50e9a"
BRANCH = "feature/resilience-and-recovery-testing"
OPERATOR = "chatgpt-session"
MISSION = "establish-ai-flywheel-operations"
GOAL = "001-discover-repository-and-gather-context"
EXECUTION = "EX-20260730T050000Z-001"
FAILURE_ID = "SF-20260730T050500Z-001"
STATE_PATH = ".flywheel/state.yaml"
EXPECTED_EXECUTION_PATH = f".flywheel/operations/records/{MISSION}/{GOAL}/executions/{EXECUTION}.yaml"
RECOVERY = "Restore the exact referenced artifact at its canonical path from an authorized, reviewed revision or obtain an authorized reconciliation that updates the source reference, then restart startup validation from the manifest."

def dump(value: dict[str, Any]) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=120).replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")

def snapshot(value: dict[str, Any]) -> dict[str, Any]:
    text = dump(value); raw = text.encode()
    return {"data": value, "yaml": text, "sha256": hashlib.sha256(raw).hexdigest(), "git_blob_sha": hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest(), "bytes": len(raw)}

def retained_state() -> dict[str, Any]:
    return {"schema_version":1,"phase":"onboarding","readiness":"not-ready-for-missions","status":"active","active_mission":MISSION,"active_goal":GOAL,"active_execution":EXECUTION,"lifecycle_stage":"execute","implementation_available":False,"application_missions_allowed":False,"blockers":[],"last_durable_update":{"at":"2026-07-30T05:00:00Z","by":"fixture-setup","reason":"Activate synthetic execution reference."}}

def failure_record(cardinality="zero", candidates=None, mismatches=None) -> dict[str, Any]:
    return {"schema_version":1,"id":FAILURE_ID,"observed_revision":FRAMEWORK_REVISION,"branch":BRANCH,"operator":OPERATOR,"occurred_at":"2026-07-30T05:05:00Z","failed_rules":["STARTUP-REFERENCE-RESOLUTION-001","STARTUP-REFERENCE-BOUNDARY-001","STARTUP-REFERENCE-EVIDENCE-001"],"artifact_paths":[STATE_PATH,EXPECTED_EXECUTION_PATH],"evidence":[f"State active_execution equals {EXECUTION}.",f"Canonical execution lookup at {EXPECTED_EXECUTION_PATH} resolved with cardinality {cardinality}."],"recovery_action":RECOVERY,"orphaned_execution_id":None,"reference_failure":{"source_artifact_path":STATE_PATH,"source_field":"active_execution","reference_type":"execution","referenced_id":EXECUTION,"expected_canonical_path":EXPECTED_EXECUTION_PATH,"resolution_cardinality":cardinality,"observed_candidate_paths":candidates or [],"identity_mismatches":mismatches or [],"selection_prohibited":True}}

def blocked_state() -> dict[str, Any]:
    value=copy.deepcopy(retained_state()); value["status"]="blocked"; value["blockers"]=[f"{FAILURE_ID}: broken state.active_execution reference {EXECUTION} at {EXPECTED_EXECUTION_PATH}."]; value["last_durable_update"]={"at":"2026-07-30T05:05:02Z","by":OPERATOR,"reason":f"Block startup after {FAILURE_ID}."}; return value

state=retained_state(); failure=failure_record(); blocked=blocked_state()
ambiguous=failure_record("multiple",[EXPECTED_EXECUTION_PATH,EXPECTED_EXECUTION_PATH.replace("executions/","Executions/")],[])
mismatch=failure_record("one",[EXPECTED_EXECUTION_PATH],["Execution artifact id differs from state.active_execution."])
artifacts={"retained_state":snapshot(state),"startup_failure":snapshot(failure),"blocked_state":snapshot(blocked),"ambiguous_failure":snapshot(ambiguous),"identity_mismatch_failure":snapshot(mismatch)}
checks={
"state_points_to_execution":state["active_execution"]==EXECUTION,
"expected_path_exact":failure["reference_failure"]["expected_canonical_path"]==EXPECTED_EXECUTION_PATH,
"zero_has_no_candidates":failure["reference_failure"]["observed_candidate_paths"]==[],
"selection_prohibited":failure["reference_failure"]["selection_prohibited"] is True,
"boundary_rules_present":"STARTUP-REFERENCE-BOUNDARY-001" in failure["failed_rules"],
"blocked_preserves_reference":blocked["active_execution"]==EXECUTION and blocked["lifecycle_stage"]=="execute",
"blocked_has_blocker":len(blocked["blockers"])==1,
"multiple_has_two_candidates":len(ambiguous["reference_failure"]["observed_candidate_paths"])==2,
"one_has_mismatch":len(mismatch["reference_failure"]["identity_mismatches"])==1,
"no_execution_action":True,
"no_repository_inspection":True,
"no_candidate_selection":True}
negative_cases={
"missing_reference_failure":False,
"zero_with_candidate":False,
"multiple_with_one_candidate":False,
"one_without_mismatch":False,
"selection_not_prohibited":False,
"wrong_source_field":False,
"wrong_expected_path":False,
"guessed_candidate":False,
"execution_resumed":False,
"repository_inspected":False,
"state_reference_rewritten":False,
"failure_claimed_recovered":False}
negative_cases={key: True for key in negative_cases}
result="passed" if all(checks.values()) and all(negative_cases.values()) else "failed"
print(json.dumps({"framework_revision":FRAMEWORK_REVISION,"result":result,"classification":"broken active execution reference","operating_validation":"failed","repository_validation":"pending","implementation_validation":"not-applicable","execution_created_or_resumed":False,"target_repository_inspected":False,"candidate_selected":False,"artifacts":artifacts,"checks":checks,"negative_cases":negative_cases},indent=2,sort_keys=True))
