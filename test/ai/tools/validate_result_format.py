#!/usr/bin/env python3
"""Validate canonical AI test-result Markdown formatting.

Usage:
    python test/ai/tools/validate_result_format.py <result-file> <section-count>

This validator checks presentation only. It does not validate substantive test evidence.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"FAILED: {message}")
    raise SystemExit(1)


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: validate_result_format.py <result-file> <section-count>")

    path = Path(sys.argv[1])
    try:
        expected_sections = int(sys.argv[2])
    except ValueError:
        fail("section-count must be an integer")

    if not path.is_file():
        fail(f"result file does not exist: {path}")

    text = path.read_text(encoding="utf-8")
    if "\r" in text:
        fail("result must use LF line endings")
    if not text.endswith("\n"):
        fail("result must end with one newline")

    lines = text.splitlines()
    if not lines or not re.fullmatch(r"# Prompt \d{3} — .+", lines[0]):
        fail("first line must be one level-one Prompt NNN title")

    numbered_h1 = [line for line in lines if re.match(r"# \d+\. ", line)]
    if numbered_h1:
        fail("numbered top-level sections must use level-two headings, not level one")

    numbered_h2 = [line for line in lines if re.match(r"## \d+\. ", line)]
    if len(numbered_h2) != expected_sections:
        fail(f"expected {expected_sections} numbered level-two sections; found {len(numbered_h2)}")

    observed_numbers = [int(re.match(r"## (\d+)\. ", line).group(1)) for line in numbered_h2]
    if observed_numbers != list(range(1, expected_sections + 1)):
        fail("numbered sections are missing, duplicated, or out of order")

    summary_match = re.search(
        r"## 1\. Verification Summary\n\n```text\n(?P<body>.*?)\n```\n",
        text,
        re.DOTALL,
    )
    if not summary_match:
        fail("Verification Summary must be inside one fenced text block")

    required_summary_fields = [
        "Operating Validation:",
        "Verification Result:",
        "Fixture Harness Result:",
        "Repository Changes:",
        "Files Written:",
        "Commit Required:",
        "Framework Defects Found:",
        "Prompt or Fixture Defects Found:",
    ]
    summary_lines = summary_match.group("body").splitlines()
    if len(summary_lines) != len(required_summary_fields):
        fail("Verification Summary contains an unexpected number of lines")
    for line, prefix in zip(summary_lines, required_summary_fields, strict=True):
        if not line.startswith(prefix):
            fail(f"Verification Summary field order mismatch at {prefix}")

    summary_end = summary_match.end()
    section_two = text.find("\n## 2. ", summary_end)
    if section_two == -1:
        fail("section 2 was not found")
    metadata = text[summary_end:section_two].strip("\n")
    if metadata:
        metadata_paragraphs = metadata.split("\n\n")
        if any("\n" in paragraph for paragraph in metadata_paragraphs):
            fail("summary metadata items must be separate one-line paragraphs")

    mutation_heading_matches = list(
        re.finditer(r"^## (?P<number>\d+)\. Repository Mutation Confirmation$", text, re.MULTILINE)
    )
    if len(mutation_heading_matches) != 1:
        fail("expected exactly one numbered Repository Mutation Confirmation section")

    mutation_number = mutation_heading_matches[0].group("number")
    mutation_match = re.search(
        rf"## {mutation_number}\. Repository Mutation Confirmation\n\n```text\n(?P<body>.*?)\n```\n",
        text,
        re.DOTALL,
    )
    if not mutation_match:
        fail("Repository Mutation Confirmation must be inside one fenced text block")

    required_mutation_fields = [
        "Target Framework Repository Changes:",
        "Target Framework Files Written:",
        "Target Framework Commits Created:",
        "Target Framework Pushes Performed:",
        "Durable Lifecycle Transitions Performed:",
        "Testing Repository Canonical Result Overwritten:",
        "Testing Repository README Modified:",
    ]
    mutation_lines = mutation_match.group("body").splitlines()
    if len(mutation_lines) != len(required_mutation_fields):
        fail("Repository Mutation Confirmation contains an unexpected number of lines")
    for line, prefix in zip(mutation_lines, required_mutation_fields, strict=True):
        if not line.startswith(prefix):
            fail(f"Repository Mutation Confirmation field order mismatch at {prefix}")

    if re.search(r"```yaml\n.*?\n```", text, re.DOTALL) is None:
        fail("result must contain at least one fenced YAML artifact")

    if re.search(r"\n{3,}", text):
        fail("result contains more than one blank line between blocks")

    print(
        "PASSED: canonical result formatting; "
        f"sections={expected_sections}; summary_fenced=true; "
        f"mutation_section={mutation_number}; mutation_fenced=true"
    )


if __name__ == "__main__":
    main()
