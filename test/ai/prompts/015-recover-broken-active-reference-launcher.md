# AI Flywheel Broken Active Reference Recovery Verification

## Canonical Prompt 015 Launcher

Use this file as the authoritative entrypoint for Prompt 015.

# Detailed Test Specification

Read the complete immutable Prompt 015 specification at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/1f8ace648e262fffbae17fb6cd441c8eeb54ffe4/test/ai/prompts/015-recover-broken-active-reference.md

Follow every instruction in that detailed specification except where this launcher explicitly replaces or clarifies it.

# Corrected Immutable Framework Revision

**Repository:** `Infoconex/ai-flywheel-framework`

**Immutable revision:** `291f87fb4485a2cfaa4f1580a8157a2842d08317`

Use this exact revision for every framework read and validation. It replaces the obsolete framework revision in the detailed specification.

# Fixture Harness Execution

Read the immutable base harness at:

https://raw.githubusercontent.com/Infoconex/ai-flywheel-framework-testing/446f9cf6d5b59780141d09d3754d5fc8d69506b3/test/ai/tools/verify_prompt_015_fixtures.py

Expected Git blob SHA:

```text
76692b26583b933ba2eb7e613c7d65840edfac2c
```

Retrieve the source through the GitHub connector and verify the blob SHA. Before executing it in memory, replace exactly this one assignment:

```text
FRAMEWORK_REVISION = "eb82939f330b76cc64e813feac6b7a97d3d50e9a"
```

with:

```text
FRAMEWORK_REVISION = "291f87fb4485a2cfaa4f1580a8157a2842d08317"
```

Require exactly one replacement and make no other source changes. Execute the resulting source directly in memory with Python 3 using `exec`.

# Corrected Blocked-State Contract

At the corrected framework revision, `state.schema.yaml` permits a non-null `active_execution` with `status: active` or `status: blocked`.

The following rules remain mandatory:

- `status: active` requires a non-null active execution.
- A non-null active execution requires non-null active mission, active goal, and lifecycle stage.
- `status: blocked` requires at least one blocker.
- Broken-reference recovery preserves the unresolved active execution and lifecycle stage as evidence.
- The optional blocked-state update still requires retained-revision compare-and-swap and direct proof that the failure prevents active work.

Validate the harness-provided blocked state against the corrected schema. It must pass.

# Required Output and Evaluation

Use the exact 22-section output contract, exact 25 validation-result rows, exact 34 negative cases, summary field order, mutation confirmation, and final-action choices defined by the detailed specification.

The result must identify:

```text
Framework revision tested: 291f87fb4485a2cfaa4f1580a8157a2842d08317
Detailed specification commit: 1f8ace648e262fffbae17fb6cd441c8eeb54ffe4
Fixture harness commit: 446f9cf6d5b59780141d09d3754d5fc8d69506b3
Fixture harness blob: 76692b26583b933ba2eb7e613c7d65840edfac2c
```

A result that uses the obsolete framework revision, fails to perform exactly one in-memory revision replacement, rejects the corrected blocked-state fixture, modifies the framework repository, omits the required output structure, or reports unsupported fixture identities fails Prompt 015.
