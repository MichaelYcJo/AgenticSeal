# 1792533444-automation-refuses-mid-run-questions — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | c93f76b0 |

## What this phase was asked

The prose points to the gate. One sentence in `skills/implement/SKILL.md` §1
names the hook and the rule's home. In `skills/implement/orchestration.md`
the "`Automation` is an audit trail, not a gate" paragraph and the resume
clause are rewritten in place. The `AUTOMATION` comment and the `parse`
docstring clause in `hooks/routing.py`, and the `Automation` comment in
`templates/sdd-routing.md`, stop saying that nothing can hold a run to the
row. `README.md` gains a gate row. The new module gains the S14 pin, and the
work item gains its changelog fragment.

The same direction and boundary checks as phase 1, with every module naming
a changed document.

## What this phase found

- **The gate row went to both READMEs.** `CONTRIBUTING.md` §*House rules*
  says both editions move together, and `README.ko.md` carries the same gate
  table; the plan named only `README.md`. A row of `overview.md`.
- **The resume sentence lost two more clauses than `## Removes` named.**
  "That is the one call question 1 shares" is false where the declaration
  answers `yes`, and "at the start of a work item question 1 goes alone, as
  above" restated the paragraph above it. A row of `overview.md`.
- **The new sentence in §1 closes its paragraph rather than following the
  bold opening**, so the paragraph still opens on the rule, and
  `tests/test_waiver_decided_at_start.py#test_the_session_runs_to_the_pull_request`
  passes unedited.
- **S14 reads each file with its whitespace collapsed**, so a removed
  sentence that a later edit rewraps across lines still turns it red. Each of
  the four documents was mutated back to its old sentence, or had the new one
  deleted, through `mutation-check`, and each run came back red.
- **The `git grep` sweep for each sentence `## Removes` lists is empty
  outside `seal/specs/`.** Other work items' `routing.md` copies still carry
  the old template comment; `spec.md` *Out* leaves them as records. One copy
  of the label comparison remains, in `is_routing_question`.
