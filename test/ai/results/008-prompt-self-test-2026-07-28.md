# Prompt 008 Self-Test — 2026-07-28

## Purpose

Verify that Prompt 008 itself is executable before asking for another external run.

## Result

```text
Prompt Verification: Passed after correction
Framework Verification: Not run to completion by this self-test
Repository Changes to Framework: None
Testing Prompt Changes: Yes
```

## What the self-test found

The prior Prompt 008 design repeated the complete 39-file cold-start traversal already covered by Prompt 001 before performing Validate-to-Persist verification. That made the prompt operationally fragile: several runs exhausted their inspection effort or stopped at startup before reaching the lifecycle boundary.

This was a prompt-design defect, not a framework defect.

## Correction

Prompt 008 now:

- Resolves an immutable framework revision first.
- Reads a bounded set of 22 transition-relevant repository items.
- Treats Prompt 001 as the dedicated full startup verification.
- Explicitly authorizes synthetic, read-only in-memory lifecycle verification.
- Resolves current state, mission, and goal for structural context without allowing their scope to block the synthetic test.
- Preserves all Validate-to-Persist positive, negative, schema, reference, persistence, compare-and-swap, rollback, and immutability checks.
- Prohibits all repository mutation.

## Self-test evidence

The self-test successfully resolved:

- Framework commit `6b87fd864781c4da92ec813ce7feaeb0bc3b28ed`.
- Manifest and current state.
- The active onboarding mission.
- The active repository-discovery goal.
- The prompt's synthetic-verification authorization boundary.
- The transition-relevant framework contracts previously shown to be available at the immutable revision.

## Decision

The revised prompt is suitable for another Prompt 008 framework verification. This self-test does not mark Prompt 008 as passed; the framework transition still requires a fresh run using the revised prompt.

## Next Action

Run revised Prompt 008 unchanged against framework revision `6b87fd864781c4da92ec813ce7feaeb0bc3b28ed`.
