# Prompt 015 — Recover Broken Active Reference

## Purpose

Verify that startup stops when durable state references an active execution that cannot be resolved exactly. The operator must not guess a replacement, start work, inspect an application repository, or change the framework repository.

## Authorization

Use the immutable framework revision supplied by the canonical runner. Read the manifest first and then every required file in manifest order. Build all test fixtures and proposed records only in memory. Mark displayed fixtures `PROPOSED ONLY — NOT WRITTEN`.

Do not change a real reference, create or resume an execution, inspect application content, update durable state, or modify the framework repository.

## Primary fixture

Build one valid state artifact whose `active_execution` points to an expected canonical execution path that is absent from the isolated fixture. Record lookup cardinality zero and prove that no alternate candidate was selected.

Classify the condition as `broken active execution reference`. The fixture's startup Operating Validation fails, Repository Validation remains pending, and Implementation Validation is not applicable. No execution is created or resumed, application inspection is not performed, and candidate selection is prohibited.

## Alternate fixtures

Validate these separately:

- Multiple candidate paths, including a case-only or noncanonical collision.
- One canonical candidate with an internal identity or reciprocal-context mismatch.
- Missing active mission.
- Missing active goal.
- Missing active-stage record reference.

Do not combine these states. Do not choose candidates using recency, filename similarity, letter case, or chat history.

## Recovery boundary

Build one create-only startup-failure record containing the exact source artifact and field, reference type and ID, expected canonical path, observed cardinality, candidate paths, identity mismatches, and `selection_prohibited: true`.

An optional blocked-state proposal may preserve the unresolved reference and lifecycle stage only when retained-revision compare-and-swap is provable. It must include a blocker that references the failure record and must not clear or replace the unresolved reference. Otherwise leave state unchanged.

The next authorized action is to restore the exact referenced artifact at its canonical path from an authorized reviewed revision, or obtain an authorized reconciliation that updates the source reference, then restart startup validation from the manifest.

## Required verification

Verify source-field extraction, canonical-path derivation, cardinality and mismatch evidence, startup stop behavior, opening-report values, startup-failure schema and semantics, create-only persistence, optional state safety, immutable history, restart behavior, and repository immutability.

## Negative validation

Reject at least 34 invalid cases covering incomplete reference evidence, invalid cardinality combinations, wrong source or expected path, ignored state invalidity, guessed candidate selection, execution creation or resume, application inspection, silent clearing or rewriting, unsafe blocked state, missing compare-and-swap, record overwrite, and false recovery claims.

## Result requirements

Produce exactly 22 numbered top-level sections and exactly 25 validation-result rows. Report:

- Manifest-required reads: 50/50
- Broken active-reference fixtures: 1
- Alternate reference-failure fixtures: 5
- Startup-failure records: 1
- Proposed blocked-state artifacts: 1
- Negative cases: 34/34
- Required top-level sections: 22/22
- Result-format validation: Passed

Report only reusable framework defects. Stop after the next authorized action.