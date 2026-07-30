# AI Flywheel Missing Required Artifact Recovery Verification

## Canonical Prompt 014 Launcher

Use this file as the authoritative entrypoint for Prompt 014.

# Detailed Test Specification

Read the complete immutable Prompt 014 specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/087c97c6f95ce36555a5c77aff95eeb16e19c8d3/test/ai/prompts/014-recover-missing-required-artifact.md

Follow every instruction in that detailed specification except where this launcher explicitly replaces or clarifies it.

# Final Immutable Framework Revision

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `923c46baf8d4bb400eef71a3507e07d797dcab87`

Use this exact revision for every framework read and validation.

# Corrected Deterministic Fixture Harness

Read the exact corrected harness at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/e5f47e50b092a44858bf5a1daea22cfcc85f8c94/test/ai/tools/verify_prompt_014_fixtures.py

Expected Git blob SHA:

```text
d264dcce92e5e06ee06801eb15d3e1f8a64a1843
```

The corrected harness replaces the obsolete harness reference in the detailed specification.

Retrieve the source through the GitHub connector, verify the exact blob SHA, and execute the source in memory with Python 3 using `exec`. PyYAML is required. Do not require Python network access, a temporary source file, or connector-to-filesystem materialization.

The harness is valid only when:

- Execution succeeds.
- The JSON parses successfully.
- `framework_revision` equals `923c46baf8d4bb400eef71a3507e07d797dcab87`.
- `result` equals `passed`.
- All four artifact entries contain complete normalized YAML, SHA-256, Git blob SHA, and byte count.
- Every harness check is true.
- Every harness negative case is true.
- The fixture manifest validates against the pinned manifest schema.
- The retained and optional blocked states validate against the pinned state schema.
- The startup-failure record validates against the pinned startup-failure schema.

# Fixture Corrections

The corrected harness makes these authoritative fixture corrections:

1. The fixture manifest contains the complete pinned `required_files` list rather than a shortened test list.
2. The retained and optional blocked states include `implementation_available: false`.
3. State blockers are nonempty strings, as required by `state.schema.yaml`.
4. Only `.flywheel/operating-model/config/approval-validation.yaml` is represented as absent in the isolated fixture repository.

These corrections change only the synthetic fixture. They do not change the framework contract or the intended test outcome.

# Required Output and Evaluation

Use the exact 22-section output contract, exact 24 validation-result rows, exact 30 negative cases, summary field order, repository-mutation confirmation, and final-action choices defined by the detailed specification.

The result must identify:

```text
Framework revision tested: 923c46baf8d4bb400eef71a3507e07d797dcab87
Detailed specification commit: 087c97c6f95ce36555a5c77aff95eeb16e19c8d3
Fixture harness commit: e5f47e50b092a44858bf5a1daea22cfcc85f8c94
Fixture harness blob: d264dcce92e5e06ee06801eb15d3e1f8a64a1843
```

A result that uses the obsolete harness, shortens the fixture manifest, omits `implementation_available`, uses object blockers, modifies the framework repository, omits the required output structure, or reports unsupported fixture identities fails Prompt 014.
