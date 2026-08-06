# Prompt 018: Programmatic Reuse Completion

Use the framework repository and the Python CLI implementation under test as immutable sources of truth for the selected run.

## Purpose

Certify the programmatic lifecycle boundary from Validate through Persist, Reuse, governed completion, goal closure, mission evaluation, and final state cleanup.

## Required scenarios

1. **Direct Persist completion is rejected**
   - Place an execution at `lifecycle_stage: persist`.
   - Attempt to use the generic lifecycle-advance operation.
   - Verify deterministic rejection directs the operator to the dedicated persistence operation.
   - Verify no governed file changes.

2. **Persistence activates Reuse atomically**
   - Run the dedicated persistence operation.
   - Verify creation of a terminal persistence record and one planned reuse assessment.
   - Verify execution and state move to Reuse together.
   - Verify content digests and compare-and-swap preconditions cover the governed mutable set.

3. **Duplicate reuse identity is rejected atomically**
   - Pre-create the requested reuse assessment identity.
   - Retry persistence.
   - Verify rejection and no partial mutation.

4. **Whole-set schema preflight is enforced**
   - Exercise transitions with a missing classification finding reference, missing applicable validation result, and incomplete reuse linkage.
   - Verify each proposed mutation is rejected before writing.
   - Correct the complete proposed execution and verify the transition succeeds.

5. **Generic Reuse advancement requires governed AI work**
   - Place a valid execution in Reuse with a planned assessment.
   - Invoke the generic lifecycle-advance operation.
   - Verify the implementation returns the governed-AI fallback category and does not mutate the repository.

6. **Completed reuse assessment is required**
   - Attempt completion while the required assessment remains planned.
   - Verify atomic rejection.
   - Complete the assessment with disposition, provenance, applicability, limitations, guidance, rationale, timestamp, and assessor.

7. **Governed completion closes the execution and goal atomically**
   - Run the dedicated completion operation.
   - Verify Reuse, execution, and goal become terminal together.
   - Verify the next eligible dependent goal is readied at most once.
   - Verify state clears active goal, active execution, and lifecycle stage.

8. **Final-goal mission evaluation is explicit**
   - Complete a mission's final goal.
   - Verify the mission is completed when its success criteria are supported and no mission-level blocker or required approval remains.
   - Verify the mission remains active only when a concrete governed or approval-bound reason is recorded.
   - Verify approval for external work outside the mission objective does not incorrectly keep a preparation mission active.

9. **Final repository validation passes**
   - Re-read every changed artifact.
   - Run schema and semantic validation over the complete repository.
   - Verify no active execution or lifecycle stage remains after terminal completion.

## Required evidence

Record:

- immutable framework and implementation revisions;
- exact commands or operation invocations;
- structured result category and reason for every rejection;
- before-and-after digests for atomicity checks;
- persistence and reuse identities;
- final execution, goal, mission, and state values;
- repository validation results;
- any divergence between framework requirements and implementation behavior.

## Pass conditions

Pass only when every scenario behaves as required, every rejected mutation is demonstrably atomic, all final references resolve, and framework and implementation completion semantics agree.
