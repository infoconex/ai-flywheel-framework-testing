# Prompt 014 — Recover Missing Required Artifact

## Purpose

Verify that startup deterministically stops when one manifest-required operating artifact is missing, without creating or resuming an execution, inspecting an application repository, inventing replacement content, or modifying the framework repository.

## Authorization

Use the immutable framework revision supplied by the canonical runner. Read `.flywheel/manifest.yaml` first and then every required file in manifest order. Construct the missing-file condition and all proposed recovery artifacts entirely in memory. Label displayed artifacts `PROPOSED ONLY — NOT WRITTEN`.

Do not delete or repair a real file, create or resume an execution, inspect an application repository, update durable state, or mutate the framework repository.

## Required fixture

Construct one isolated fixture in which exactly one path listed by `manifest.required_files` is absent and every other required path remains available. Preserve the exact missing path and prove required-file membership, lookup absence, and framework-revision immutability.

The required classification is `required operating file missing`. Startup Operating Validation for the fixture must fail; Repository Validation remains pending; Implementation Validation is not applicable; no execution is created or resumed; and no target repository is inspected.

## Recovery boundary

The next authorized action is to restore the exact missing artifact from an authorized reviewed framework revision, or perform an approved framework repair, and then restart startup validation from the manifest.

Construct one create-only startup-failure record at the canonical startup-failures path. It must preserve the observed revision, operator, whole-second UTC timestamp, failed rules, exact missing path, evidence, deterministic recovery action, and null orphaned execution.

An optional blocked-state proposal is legal only when retained-revision compare-and-swap is provable and the missing file directly blocks active onboarding work. It must preserve mission and goal, retain null execution and lifecycle stage, remain not ready for application missions, and reference the startup-failure record and missing path. Otherwise leave state unchanged.

## Required verification

Verify manifest-first traversal, exact path membership and absence, stop boundary, startup opening-report values, startup-failure schema and semantics, create-only identity and collision handling, immutable history, optional state safety, restart behavior, and repository immutability.

## Negative validation

Reject at least 30 invalid cases covering malformed startup-failure records, wrong or noncanonical paths, empty evidence or recovery action, invented or substituted content, continued startup, execution creation or resume, repository inspection, record overwrite, ignored collisions, unsafe blocked state, missing compare-and-swap, and false recovery claims.

## Result requirements

Produce exactly 22 numbered top-level sections, exactly 24 validation-result rows, and report:

- Manifest-required reads: 50/50
- Missing required artifacts: 1
- Startup-failure records: 1
- Proposed blocked-state artifacts: 1
- Negative cases: 30/30
- Required top-level sections: 22/22
- Result-format validation: Passed

Report only reusable framework defects. Stop after the next authorized action.