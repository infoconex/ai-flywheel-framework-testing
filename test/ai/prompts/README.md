# AI Flywheel Framework AI Prompts

This directory contains reusable prompts for testing the AI Flywheel Framework through fresh AI sessions.

## Prompt Sequence

1. [`001-startup-validation.md`](001-startup-validation.md) validates manifest-first startup and stops before execution creation.
2. [`002-execution-creation.md`](002-execution-creation.md) validates non-persistent creation and activation of the first execution.
3. [`003-execute-to-observe.md`](003-execute-to-observe.md) validates the non-persistent transition from Execute to Observe.
4. [`004-observe-to-evaluate.md`](004-observe-to-evaluate.md) validates the semantic and lifecycle boundary between Observe and Evaluate.
5. [`005-evaluate-to-classify.md`](005-evaluate-to-classify.md) validates evaluation completion, classification provenance, and the transition from Evaluate to Classify.
6. [`006-classify-to-adapt.md`](006-classify-to-adapt.md) validates classification completion, adaptation provenance, scope and approval boundaries, and the transition from Classify to Adapt.

## Test Boundary

These prompts target `Infoconex/ai-flywheel-framework` on branch `feature/self-contained-operating-model` unless a prompt explicitly states otherwise.

They are read-only verification prompts. They must not persist execution artifacts, state transitions, evidence, logs, repository-discovery results, or commits to the framework-development branch.