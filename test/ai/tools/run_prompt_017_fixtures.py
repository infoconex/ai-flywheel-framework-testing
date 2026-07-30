#!/usr/bin/env python3
"""Apply final Prompt 017 fixture corrections and execute the base source in memory."""
from __future__ import annotations

import contextlib
import io
import json
import re
from typing import Any

FINAL_FRAMEWORK_REVISION = "18335e57165a8984adab4790d3a6210355b484ba"
BASE_FRAMEWORK_REVISION = "c0f779eedc97963283e2798a988c628df63ddcbe"
SELF_HOST_EVIDENCE_REVISION = "42461bcc86ea75c3752082b33d7c24dd18a8bd62"
SELF_HOST_FIXTURE_PATH = "test/ai/fixtures/017-self-host-certification.yaml"


def run(base_source: str) -> dict[str, Any]:
    if base_source.count(f'FRAMEWORK_REVISION = "{BASE_FRAMEWORK_REVISION}"') != 1:
        raise ValueError("base framework revision assignment must occur exactly once")

    corrected = base_source.replace(
        f'FRAMEWORK_REVISION = "{BASE_FRAMEWORK_REVISION}"',
        f'FRAMEWORK_REVISION = "{FINAL_FRAMEWORK_REVISION}"',
        1,
    )

    missing_revision_pattern = '        "source_revision": EVIDENCE_REVISION,'
    if corrected.count(missing_revision_pattern) != 2:
        raise ValueError("expected exactly two legacy scenarios with unknown tested revisions")
    corrected = corrected.replace(
        missing_revision_pattern,
        '        "tested_framework_revision": None,\n        "evidence_revision": EVIDENCE_REVISION,',
    )

    static_pattern = re.compile(r'        "source_revision": "([0-9a-f]{40})",')
    static_matches = static_pattern.findall(corrected)
    if len(static_matches) != 7:
        raise ValueError(f"expected seven static tested framework revisions; found {len(static_matches)}")
    corrected = static_pattern.sub(
        lambda match: (
            f'        "tested_framework_revision": "{match.group(1)}",\n'
            '        "evidence_revision": EVIDENCE_REVISION,'
        ),
        corrected,
    )

    self_host_pattern = '        "source_revision": FRAMEWORK_REVISION,'
    if corrected.count(self_host_pattern) != 1:
        raise ValueError("expected exactly one self-hosting framework revision")
    corrected = corrected.replace(
        self_host_pattern,
        (
            '        "tested_framework_revision": FRAMEWORK_REVISION,\n'
            f'        "evidence_revision": "{SELF_HOST_EVIDENCE_REVISION}",'
        ),
        1,
    )

    old_evidence_fixture_refs = (
        '        "fixture_definition_refs": ["test/ai/prompts/010-end-to-end-execution.md", '
        '"test/ai/prompts/016-run-representative-proving-mission-launcher.md"],'
    )
    if corrected.count(old_evidence_fixture_refs) != 1:
        raise ValueError("expected one combined evidence-completeness fixture reference")
    corrected = corrected.replace(
        old_evidence_fixture_refs,
        '        "fixture_definition_refs": ["test/ai/prompts/016-run-representative-proving-mission-launcher.md"],',
        1,
    )

    old_evidence_result_refs = (
        '        "evidence_refs": ["test/ai/results/010-end-to-end-execution.md", '
        '"test/ai/results/016-run-representative-proving-mission.md"],'
    )
    if corrected.count(old_evidence_result_refs) != 1:
        raise ValueError("expected one combined evidence-completeness result reference")
    corrected = corrected.replace(
        old_evidence_result_refs,
        '        "evidence_refs": ["test/ai/results/016-run-representative-proving-mission.md"],',
        1,
    )

    old_evidence_actual = (
        '        "actual_result": "Acceptance-criterion evidence mapping passed in the end-to-end lifecycle '
        'and representative proving mission results.",'
    )
    if corrected.count(old_evidence_actual) != 1:
        raise ValueError("expected one combined evidence-completeness actual result")
    corrected = corrected.replace(
        old_evidence_actual,
        '        "actual_result": "Acceptance-criterion evidence mapping passed in the representative proving mission result.",',
        1,
    )

    old_fixture_ref = '        "fixture_definition_refs": ["test/ai/prompts/017-self-host-certification.md"],'
    if corrected.count(old_fixture_ref) != 1:
        raise ValueError("expected exactly one obsolete self-hosting fixture reference")
    corrected = corrected.replace(
        old_fixture_ref,
        f'        "fixture_definition_refs": ["{SELF_HOST_FIXTURE_PATH}"],',
        1,
    )

    duplicate_source_refs = '        "source_refs": [item for scenario in scenario_specs for item in scenario["evidence_refs"]],'
    if corrected.count(duplicate_source_refs) != 1:
        raise ValueError("expected one non-deduplicated scenario evidence source list")
    corrected = corrected.replace(
        duplicate_source_refs,
        '        "source_refs": list(dict.fromkeys(item for scenario in scenario_specs for item in scenario["evidence_refs"])),',
        1,
    )

    old_negative = '"scenario_source_revision_not_immutable"'
    if corrected.count(old_negative) != 1:
        raise ValueError("expected one obsolete scenario revision negative case")
    corrected = corrected.replace(old_negative, '"scenario_revision_identities_invalid"', 1)

    buffer = io.StringIO()
    namespace = {"__name__": "__main__"}
    with contextlib.redirect_stdout(buffer):
        exec(compile(corrected, "verify_prompt_017_fixtures.py", "exec"), namespace)

    output = buffer.getvalue()
    parsed = json.loads(output)
    if parsed.get("framework_revision") != FINAL_FRAMEWORK_REVISION:
        raise ValueError("corrected fixture reported the wrong framework revision")
    if parsed.get("result") != "passed":
        raise ValueError("corrected fixture did not pass")

    scenarios = parsed["artifacts"]["certification_record"]["data"]["scenarios"]
    if len(scenarios) != 10:
        raise ValueError("corrected certification record must contain ten scenarios")
    if [item["tested_framework_revision"] for item in scenarios[:2]] != [None, None]:
        raise ValueError("legacy scenarios must preserve unknown tested framework revisions as null")
    if any(not item["evidence_revision"] for item in scenarios):
        raise ValueError("every scenario must identify its immutable evidence revision")
    if any(item["result"] == "passed" and not item["tested_framework_revision"] for item in scenarios):
        raise ValueError("every passed scenario must identify its tested framework revision")
    if scenarios[7]["fixture_definition_refs"] != ["test/ai/prompts/016-run-representative-proving-mission-launcher.md"]:
        raise ValueError("evidence-completeness scenario must use one revision-consistent fixture")
    if scenarios[7]["evidence_refs"] != ["test/ai/results/016-run-representative-proving-mission.md"]:
        raise ValueError("evidence-completeness scenario must use one revision-consistent result")
    if scenarios[9]["fixture_definition_refs"] != [SELF_HOST_FIXTURE_PATH]:
        raise ValueError("self-hosting scenario must reference the immutable fixture definition")
    if scenarios[9]["evidence_revision"] != SELF_HOST_EVIDENCE_REVISION:
        raise ValueError("self-hosting scenario must use the fixture-definition revision")

    evidence_audit = parsed["artifacts"]["evidence_records"]["data"][0]
    if len(evidence_audit["source_refs"]) != len(set(evidence_audit["source_refs"])):
        raise ValueError("scenario evidence audit source references must be unique")

    parsed["execution_mode"] = "in-memory connector source with deterministic correction runner"
    parsed["base_framework_revision"] = BASE_FRAMEWORK_REVISION
    parsed["self_host_evidence_revision"] = SELF_HOST_EVIDENCE_REVISION
    parsed["correction_count"] = 17
    return parsed
