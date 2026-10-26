# Phase 1: 1792935671-the-routing-check-moves-to-the-sessions-tools

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 4ac2ab09 |

## What this phase was asked

Build phase 1 of `plan.md` *Phases*: settle removes a document. A `remove` with no `from` whose `section` names two headings, one holding the other, removes the outer one, and a document a removal leaves empty is deleted, through `settle --apply`, `replay` and `unverified_check.py#settled`. `skills/settle/SKILL.md` *Rule changes* says so. Verify with `tests/test_rule_changes.py`, `tests/test_settle.py` and `tests/test_fold_check.py`, and with an in-memory replay of the unsettled specs and this one, in merge order. Phases 1 to 4 add and remove nothing the later phases remove. Each new case is seen red against the tree before its code, and `bin/mutation-check` runs after the commit where a refusal has no case to fail yet. Run tests with `bin/test -n auto -q <files>`, and lint each changed Python file with `uvx ruff check` and `uvx ruff format --check` before the commit. The broad gate is the orchestrator's.

## What this phase found

**The frame holds for this phase.** `rule_changes.py#apply_op` refused a `section` naming two headings, as *Technical context* says. `docs/the-commit-gate-inside-git.md` has `# The commit gate inside git` at line 1 and `## The commit gate inside git` at line 13 (read). `docs/commit-review-gate-spec.md` has one heading with its title's text, so its removal already placed, and returned `""` before this phase.

**How a deletion travels.** `apply_op` returns `(None, None)` where a `remove` leaves the text empty. `replay` stores that None in `documents`, so a later operation on the same file reads it as absent, the way `read` reports a missing file. `settle.py#apply` deletes the file and prints `deleted <path>: a removal left it empty`, pinned by the new `tests/test_settle.py` case. `unverified_check.py#settled` drops a None before counting. Without that, the counting raised `TypeError` on the deleted document, which the mutation run below shows.

**The rule is wider than two headings.** `apply_op` takes the first match when its section holds every other match. Two matches are the case the frame names and the case the tests cover; a third nested match is removed with the outer one, and no case runs it. Two sibling headings still refuse, and the sibling `remove` arm added to `test_a_heading_or_a_text_found_twice_is_refused` pins that. `skills/settle/SKILL.md` states the rule in that wider form, in the bullet that says a `section` appears once, and the `remove` row of the table says a document left empty is deleted.

**Only the whole-section arm can empty a document.** A `remove` with `from` searches below the section's heading, so the heading always stays. The deletion is therefore written in the no-`from` arm alone.

**How each new case was seen red, executed before the code.** The two `test_a_remove_naming_nested_headings_takes_the_outer_one` cases and `test_apply_deletes_a_document_its_removal_leaves_empty` failed against the old code, each refused as a heading that appears 2 times. The sibling arm passed against the old code, because it pins what the old code already refused. It was shown red by mutant 1 below.

**`mutation-check`, executed after the commit.** 6 mutants, 6 red, 0 survived:

- `rule_changes.py`, 3: the containment test replaced by `True` (the sibling arm went red), `nested` forced False, and the empty-document return switched off.
- `settle.py`, 1: the `os.remove` replaced by `pass`.
- `unverified_check.py`, 1: the None filter removed (`TypeError` in `settled`).

`git status --short` was clean after each run.

**Tests, executed.** `bin/test -n auto -q` over `tests/test_rule_changes.py`, `tests/test_settle.py`, `tests/test_fold_check.py` and `tests/test_unverified_check.py`: 487 passed. Over `tests/test_docs_line_wrap.py`, `tests/test_settle_reads_before_it_removes.py`, `tests/test_rules.py` and `tests/test_settle_applies_rule_changes_in_place.py`, the modules that read `skills/settle/SKILL.md`: 118 passed, after one wrapped line was rewrapped. `tests/test_fold_check.py` gained no case: a row naming a missing document is already refused by `test_an_index_that_misses_doubles_or_names_nothing_is_refused`, and the new `tests/test_settle.py` case asserts that the after-apply `fold-check` lines are absent once the row goes.

**The in-memory replay, executed after the commit.** A probe script outside the tree parsed every `seal/specs/*/spec.md` with operations and ordered them with `rule_changes.order(root, "HEAD", ids)`. The order: 1792533444, 1792540458, 1792624592, 1792619408, 1792627930, 1792628098, 1792926874, then this work item.

- Applied operation by operation in that order, every placeable earlier operation first, each of this spec's operations placed, and `docs/commit-review-gate-spec.md` and `docs/the-commit-gate-inside-git.md` came out deleted.
- Two earlier operations did not place, the two *Technical context* reports: 1792619408 line 192 (`docs/the-review-record.md` *What the check reads at the pull request*) and 1792627930 line 279 (*The guarantee*). Both `from` texts are older than the document. Line 181 of that file now reads *the `## Rule changes` section of each `spec.md` it parses*, and line 307 already reads `withheld reason:`.
- Replayed spec by spec, as `settle` replays, 1792619408 is refused at that line, and every later spec waits on it, this one included. So this work item cannot settle until those two operations are rewritten or the specs are held. That is a settle question for whoever runs the next settle, and this phase does not act on it.
