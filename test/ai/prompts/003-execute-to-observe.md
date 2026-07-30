# Prompt 003 — Execute to Observe

## Purpose

Verify, without mutating the framework repository, that a valid active execution can transition from Execute to Observe under the current AI Flywheel lifecycle, execution, state, schema, timestamp, and compare-and-swap contracts.

The revision-specific runner supplies the immutable framework revision, this specification commit, result-format identities, and canonical result path.

## Authorization and boundaries

Use `Infoconex/ai-flywheel-framework` as the framework source of truth.

This verification may read the pinned framework, resolve the manifest-required operating model, construct complete proposed artifacts in memory, validate them, and publish only the canonical testing result.

It must not mutate the framework repository, activate an execution, inspect an application repository, perform goal-directed repository work, persist lifecycle records, invent evidence, or create alternate results.

Every synthetic artifact displayed in the result must be labeled:

> **PROPOSED ONLY — NOT WRITTEN**

## Startup and starting snapshot

1. Read `.flywheel/manifest.yaml` first and then every required file in manifest order.
2. Resolve state, active mission, and active goal at the pinned revision.
3. Construct one schema-valid proposed starting execution representing the activation snapshot:
   - status `in-progress`;
   - Execute is the sole `in-progress` stage;
   - Observe through Reuse are `pending`;
   - execution and Execute `started_at` values are equal;
   - mission, goal, intended outcome, acceptance-criterion order, and state references agree;
   - all collections required by the current execution schema exist;
   - `outcome`, `completed_at`, and completion disposition/rationale are null.
4. Construct the corresponding proposed starting state with status `active`, the execution ID, and lifecycle stage `execute`.

Use concrete deterministic identities and whole-second UTC timestamps. Do not persist either starting artifact.

## Proposed transition

Capture one whole-second UTC transition instant and construct the complete proposed post-transition pair in memory:

- Execute becomes `completed` with non-null completion timestamp and summary.
- Observe becomes the sole `in-progress` stage with `started_at` equal to or later than Execute completion.
- Evaluate through Reuse remain `pending`.
- Execution remains `in-progress` and resumable.
- State remains `active`, references the same mission, goal, and execution, and sets `lifecycle_stage: observe`.
- `state.last_durable_update` records the transition instant, stable operator identity, and a concrete reason.
- All unrelated state fields remain unchanged.

No observation record is required merely to activate Observe. Observation and evidence requirements apply before Observe may complete.

## Validation requirements

Validate the starting and proposed artifacts using YAML 1.2, JSON Schema Draft 2020-12 with format enforcement, and all current semantic rules.

Confirm:

- manifest-required resolution is complete;
- execution and state schema conformance;
- exactly one in-progress lifecycle stage;
- canonical stage ordering;
- Execute completion and Observe activation semantics;
- timestamp monotonicity;
- mission, goal, execution, intended-outcome, and acceptance-criterion agreement;
- state stage equals the execution’s sole active stage;
- retained-SHA prechecks for both existing artifacts;
- execution-first/state-second compare-and-swap ordering;
- final pair verification;
- exact execution rollback and durable finding behavior if the state update fails after execution update;
- no framework mutation.

## Required negative cases

Report exactly these 12 invalid cases and demonstrate deterministic rejection:

1. Execute completed while Observe remains pending.
2. Execute and Observe are both in progress.
3. No lifecycle stage is in progress.
4. Observe starts before Execute completes.
5. Execute completion timestamp is missing.
6. Observe start timestamp is missing.
7. A later successor stage is not pending.
8. Execution status is terminal or otherwise incompatible with the active transition.
9. State lifecycle stage is null or does not equal `observe`.
10. Mission, goal, or execution identity differs between state and execution.
11. Either retained artifact SHA changes before the first write.
12. Repository or goal-directed work begins before the transition is durably verified.

For each case include the invalid condition, expected rejection, observed result, and enforcing contract.

## Result format

Produce exactly these 11 top-level numbered sections:

1. Verification Summary
2. Validation Trace
3. Starting Operating Snapshot
4. Transition Decision
5. Proposed Execution Artifact
6. Proposed State Artifact
7. Schema and Invariant Results
8. Persistence-Sequence Results
9. Negative Validation Results
10. Framework Defects
11. Repository Mutation Confirmation

The summary must report the pinned framework revision, specification commit, result-format contract and validator commits, manifest read count, proposed artifact counts, negative-case count, repository changes, defect counts, and format-validation result.

If no reusable framework defect is found, state exactly:

> No reusable framework defects were found during the non-persistent Execute-to-Observe lifecycle verification.

Only the revision-specific runner may authorize writing the canonical result.