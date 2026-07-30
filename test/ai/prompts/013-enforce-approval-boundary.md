# AI Flywheel Approval Boundary Verification

## Canonical Prompt 013 Launcher

Use this file as the authoritative entrypoint for Prompt 013.

# Detailed Test Specification

Read the complete immutable Prompt 013 specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/d8d8e8e3af3e8f3ea448f318f7746f04f20065e3/test/ai/prompts/013-enforce-approval-boundary.md

Follow every instruction in that detailed specification except where this launcher explicitly replaces or clarifies it.

The overrides below are authoritative. Apply them before executing the detailed specification. Do not use the obsolete framework revision or obsolete harness-materialization instructions contained in the detailed specification.

# Final Immutable Framework Revision

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `7d18c1dacf02f341f0c464571bc2f99e78a4b4de`

Use this exact revision for every framework read and validation. Do not resolve or substitute a branch head or later commit.

# Deterministic Fixture Harness

Read the immutable base generator through the GitHub connector at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/2fd99b86df229890f8eb53152ea825906c658fe7/test/ai/tools/verify_prompt_013_fixtures.py

Expected Git blob SHA:

```text
30b004f49b663e062126551bb1d8958c0a226298
```

Do not require the connector-returned source to be downloaded, mounted, or written as a file.

Execute the retrieved source directly in the Python runtime using this exact in-memory procedure:

1. Preserve the connector-returned UTF-8 source text exactly.
2. Verify its Git blob SHA equals `30b004f49b663e062126551bb1d8958c0a226298` using the Git blob formula `sha1("blob <byte-count>\0" + bytes)`.
3. Replace exactly one occurrence of:

```text
FRAMEWORK_REVISION = "ea8f72fd194973f033553f46c59b400ab36c8868"
```

with:

```text
FRAMEWORK_REVISION = "7d18c1dacf02f341f0c464571bc2f99e78a4b4de"
```

4. Assert that exactly one replacement occurred.
5. Execute the resulting source in memory with `__name__` set to `__main__`.
6. Capture the complete standard output as JSON.

Conceptually, the execution is equivalent to:

```python
source = connector_returned_source
old = 'FRAMEWORK_REVISION = "ea8f72fd194973f033553f46c59b400ab36c8868"'
new = 'FRAMEWORK_REVISION = "7d18c1dacf02f341f0c464571bc2f99e78a4b4de"'
assert source.count(old) == 1
source = source.replace(old, new, 1)
exec(compile(source, "verify_prompt_013_fixtures.py", "exec"), {"__name__": "__main__"})
```

The immutable helper runner at commit `fffc5874dc0cd4df7e6b833574eb9a9ba4ba6ea6` documents the same revision substitution but is no longer required to be materialized or imported at runtime.

The harness is valid only when:

- The source Git blob SHA matches the expected value.
- The revision substitution count is exactly one.
- Execution completes successfully.
- The output parses as JSON.
- `framework_revision` equals `7d18c1dacf02f341f0c464571bc2f99e78a4b4de`.
- `result` equals `passed`.
- All 11 artifact entries contain complete normalized YAML, SHA-256, Git blob SHA, and byte count.
- Every harness check is true.
- Every reported fixture rejection is true.
- `classification_before_approval` is `approval-required action blocked`.
- `classification_after_durable_approval` is `exact approved action authorized`.

Do not invent, approximate, or manually replace fixture bytes or identities.

An inability to download or mount GitHub files is not a valid reason to skip the harness because connector-returned source can be executed in memory. If the source cannot be read through the connector or the Python runtime itself is unavailable, report the run as incomplete rather than as a framework defect.

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
Base fixture harness blob: 30b004f49b663e062126551bb1d8958c0a226298
Harness execution mode: in-memory connector source
```

A result that uses the obsolete framework revision, skips the in-memory harness, fails to verify the base source blob, validates a structured approval against the legacy generic approval shape, omits the required output structure, or reports unsupported fixture identities fails Prompt 013.