# AI Flywheel Framework Testing

This repository contains the repeatable test assets used to evaluate and improve the AI Flywheel Framework.

It keeps framework testing separate from the framework implementation so prompts, fixtures, runners, expected behavior, and captured results can evolve without becoming part of the distributed framework itself.

## Purpose

The repository is used to:

- define repeatable AI-driven framework tests
- preserve immutable test inputs and source revisions
- capture durable test results and evidence
- validate framework behavior across normal, boundary, failure, and recovery scenarios
- expose defects and improvement opportunities before framework changes are accepted

## Related Repositories

- [AI Flywheel Specification](https://github.com/Infoconex/ai-flywheel-spec) — defines the concepts, principles, lifecycle, and requirements of the AI Flywheel.
- [AI Flywheel Framework](https://github.com/Infoconex/ai-flywheel-framework) — provides the framework implementation tested by this repository.

## Repository Structure

Testing assets are maintained under `test/ai/`, including prompts, runners, fixtures, and published results.

Each test should identify the exact immutable revisions it evaluates so its outcome can be reproduced and traced to the corresponding framework and test definitions.
