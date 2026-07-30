#!/usr/bin/env python3
"""Run the immutable Prompt 013 fixture generator against the final framework revision."""
from __future__ import annotations

import sys

import verify_prompt_013_fixtures as fixtures

fixtures.FRAMEWORK_REVISION = "7d18c1dacf02f341f0c464571bc2f99e78a4b4de"

if __name__ == "__main__":
    sys.exit(fixtures.main())
