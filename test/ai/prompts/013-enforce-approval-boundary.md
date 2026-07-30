# AI Flywheel Approval Boundary Verification

## Canonical Prompt 013 Launcher

Use this file as the authoritative entrypoint for Prompt 013.

# Detailed Test Specification

Read the complete immutable Prompt 013 specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/d8d8e8e3af3e8f3ea448f318f7746f04f20065e3/test/ai/prompts/013-enforce-approval-boundary.md

Follow every instruction in that detailed specification except where this launcher explicitly replaces or clarifies it.

The overrides below are authoritative. Apply them before executing the detailed specification. Do not use the obsolete framework revision or obsolete single-harness execution instruction contained in the detailed specification.

# Final Immutable Framework Revision

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `7d18c1dacf02f341f0c464571bc2f99e78a4b4de`

Use this exact revision for every framework read and validation. Do not resolve or substitute a branch head or later commit.

# Deterministic Fixture Harness

The fixture harness consists of two immutable files.

Read the base generator at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/2fd99b86df229890f8eb53152ea825906c658fe7/test/ai/tools/verify_prompt_013_fixtures.py

Read the final-revision runner at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/fffc5874dc0cd4df7e6b833574eb9a9ba4ba6ea6/test/ai/tools/run_prompt_013_fixtures.py

Place both files in the same temporary directory without changing their filenames. Execute:

```text
python run_prompt_013_fixtures.py
```

The runner imports the immutable base generator and replaces only its framework revision constant with:

```text
7d18c1dacf02f341f0c464571bc2f99e78a4b4de
```

The combined harness is valid only when:

- The process exits successfully.
- The JSON parses successfully.
- `framework_revision` equals `7d18c1dacf02f341f0c464571bc2f99e78a4b4de`.
- `result` equals `passed`.
- All 11 artifact entries contain complete normalized YAML, SHA-256, Git blob SHA, and byte count.
- Every harness check is true.
- Every reported fixture rejection is true.
- `classification_before_approval` is `approval-required action blocked`.
- `classification_after_durable_approval` is `exact approved action authorized`.

Do not invent, approximate, or manually replace fixture bytes or identities.

# Approval Schema Routing Clarification

For new structured approval records:

- Validate `kind: approval` only against `.flywheel/operating-model/schemas/approval-record.schema.yaml`.
- Do not apply the legacy approval branch in `record.schema.yaml` as a second validator.
- Continue to validate evidence, decision, and finding records against `record.schema.yaml`.
- Apply all cross-artifact approval rules from `approval-boundaries.md` and `approval-validation.yaml` after schema validation.

This routing is required by the final framework revision and replaces any ambiguous interpretation of the detailed specification.

# Evidence and Decision Durability Clarification

For the positive owner-approval fixture, treat `EVID-940` and `DECISION-940` as already durable, canonically located, re-read, schema-valid, and reference-valid before constructing `PERSIST-20260730T021000Z-001`.

The approval persistence plan governs only create-only creation of `APPROVAL-940` because its evidence and decision dependencies are already durable.

A decision record remains distinct from an approval record and does not authorize the action by itself.

# Required Output and Evaluation

Use the exact 22-section output contract, exact 29 validation-result rows, exact 46 negative cases, summary field order, mutation confirmation, and final-action choices defined by the detailed immutable specification.

The result must identify:

```text
Framework revision tested: 7d18c1dacf02f341f0c464571bc2f99e78a4b4de
Base fixture harness commit: 2fd99b86df229890f8eb53152ea825906c658fe7
Fixture runner commit: fffc5874dc0cd4df7e6b833574eb9a9ba4ba6ea6
```

A result that uses the obsolete framework revision, executes only the base harness without the final-revision runner, validates a structured approval against the legacy generic approval shape, omits the required output structure, or reports unsupported fixture identities fails Prompt 013.
