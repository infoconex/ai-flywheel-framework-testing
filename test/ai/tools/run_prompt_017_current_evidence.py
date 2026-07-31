#!/usr/bin/env python3
"""Execute the pinned Prompt 017 transformation with the runner-pinned evidence revision."""
from __future__ import annotations

from typing import Any

OLD_EVIDENCE_REVISION = "021e10fe9577df11017f4ea1def4f83358aaed3d"
CURRENT_EVIDENCE_REVISION = "4042369bfe6d1284fbe51de5037d4de7adb85df2"


def run(base_source: str, transformation_source: str) -> dict[str, Any]:
    old_assignment = f'EVIDENCE_REVISION = "{OLD_EVIDENCE_REVISION}"'
    new_assignment = f'EVIDENCE_REVISION = "{CURRENT_EVIDENCE_REVISION}"'

    if transformation_source.count(old_assignment) != 1:
        raise ValueError("expected exactly one retained evidence revision assignment")

    corrected_source = transformation_source.replace(old_assignment, new_assignment, 1)
    namespace: dict[str, Any] = {"__name__": "prompt_017_transformation"}
    exec(compile(corrected_source, "run_prompt_017_fixtures.py", "exec"), namespace)

    result = namespace["run"](base_source)
    if result.get("evidence_revision") != CURRENT_EVIDENCE_REVISION:
        raise ValueError("transformation did not return the runner-pinned evidence revision")

    result["execution_mode"] = "in-memory connector source with current-evidence wrapper"
    result["wrapper_correction_count"] = 1
    return result
