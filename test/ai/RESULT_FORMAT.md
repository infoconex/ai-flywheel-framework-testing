# Canonical AI Test Result Format

This document defines the required Markdown presentation for every canonical result under `test/ai/results/`.

Prompts and run instructions MUST reference this contract. A result that contains the correct facts but violates this contract is incomplete until its formatting is corrected.

## Document structure

1. Begin with one descriptive level-one title:

   ```markdown
   # Prompt NNN — Descriptive Verification Title
   ```

2. Use exactly one blank line after the title.
3. Render every numbered top-level result section as a level-two heading:

   ```markdown
   ## 1. Verification Summary
   ## 2. Validation Trace
   ```

4. Do not use level-one headings for numbered sections.
5. Preserve exactly one blank line before and after headings, paragraphs, fenced blocks, blockquotes, lists, and tables.

## Verification Summary

Under `## 1. Verification Summary`, render the required summary fields inside one fenced `text` block. The fence is mandatory and is not merely an example:

```text
Operating Validation: Passed | Failed
Verification Result: Passed | Failed
Fixture Harness Result: Passed | Failed
Repository Changes: None
Files Written: 0
Commit Required: False
Framework Defects Found: <count>
Prompt or Fixture Defects Found: <count>
```

After the summary fence:

- Put each source identity, revision, commit, blob, execution-mode, or count statement in its own paragraph.
- Separate every metadata paragraph with exactly one blank line.
- Format immutable identifiers and compact values with inline code.
- Do not compress metadata into an unspaced line sequence or bullet list unless the prompt explicitly requires a table.

Example:

```markdown
Framework revision tested: `0123456789abcdef0123456789abcdef01234567`

Detailed specification commit: `89abcdef0123456789abcdef0123456789abcdef`

Harness execution mode: `in-memory connector source`
```

## Structured artifacts

- Put complete YAML artifacts inside fenced `yaml` blocks.
- Put literal multi-line status, mutation, command, or identity output inside fenced `text` blocks.
- Keep `> **PROPOSED ONLY — NOT WRITTEN**` on its own line immediately before a proposed artifact or persistence description.
- Do not change normalized artifact bytes merely for presentation.

## Tables and lists

- Use standard Markdown tables with one header separator row.
- Leave exactly one blank line before and after each table.
- Use bullets only for actual collections, not for metadata that is conventionally rendered as separate paragraphs.
- Do not collapse required individually reported validation or negative cases into prose.

## Repository Mutation Confirmation

Render the complete mutation confirmation inside one fenced `text` block under the numbered section titled `Repository Mutation Confirmation`:

```text
Target Framework Repository Changes: None
Target Framework Files Written: 0
Target Framework Commits Created: 0
Target Framework Pushes Performed: 0
Durable Lifecycle Transitions Performed: 0
Testing Repository Canonical Result Overwritten: Yes | No
Testing Repository README Modified: No
```

The prompt defines the section number and position. This shared format contract does not require a fixed section number for Repository Mutation Confirmation.

## Final section

The final numbered section contains only the allowed next-test action unless the prompt explicitly requires additional explanation.

## Acceptance

A canonical result conforms only when:

- It has one level-one document title.
- All numbered top-level sections use level-two headings in the required order.
- The verification summary is inside a fenced `text` block.
- Metadata items are separated by one blank line.
- Complete YAML artifacts use `yaml` fences.
- The repository mutation confirmation is inside a fenced `text` block under its prompt-defined numbered heading.
- Tables, lists, and paragraphs use consistent blank-line separation.
- The required substantive section, row, and case counts remain unchanged.
