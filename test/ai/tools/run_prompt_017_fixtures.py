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
        '        "tested_framework_revision": FRAMEWORK_REVISION,\n        "evidence_revision": EVIDENCE_REVISION,',
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

    parsed["execution_mode"] = "in-memory connector source with deterministic correction runner"
    parsed["base_framework_revision"] = BASE_FRAMEWORK_REVISION
    parsed["correction_count"] = 12
    return parsed
