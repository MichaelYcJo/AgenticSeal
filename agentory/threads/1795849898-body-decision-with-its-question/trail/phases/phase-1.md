# Phase 1: 1795849898-body-decision-with-its-question

## What this phase found

**The frame held against the tree at `1383f97c`.** The coordinates `frame/design.md` *Grounding* and `frame/plan.md` *Technical context* give were opened before the build: `pr_body.py#_questions` and `#_tables` at lines 865 to 876 and 832 to 834, the docstring clause on line 15, `NO_QUESTION_TABLE` on line 333, the sentence of `skills/code-review/orchestration.md` on lines 373 to 379, the guidance on line 35 of `templates/records/sdd-plan.md`, and `test_accepts_every_question_row_as_written` on lines 470 to 481 of `tests/skills/test_pr_body.py` (read). `pr_body.py` at `1383f97c` is the same blob as at `92b2f13f` (executed: `git diff --quiet 92b2f13f -- skills/code-review/scripts/pr_body.py`, exit 0).

**Departure: the cases say "as 0.41.0 shipped it" where the frame says "at `92b2f13f`".** `tests/text/test_a_cited_commit_outlives_the_squash.py` refused the four docstrings that first named `92b2f13f`, because no `main` or release ref holds that commit and it opens in no clone once the branch is squashed (executed: `bin/test tests/text tests/behaviour -q`, its failing line named `tests/skills/test_pr_body.py:479` and three more). `pr_body.py` at the tag `v0.41.0` is the same blob as at `92b2f13f` (executed: `git diff --quiet v0.41.0 92b2f13f -- skills/code-review/scripts/pr_body.py`, exit 0), so the cases name the code they were seen red against by its release, as the file's earlier cases name 0.37.1 and 0.38.2. Judged against `skills/agent-contract/SKILL.md` rule 19, which keeps a sentence of a published release and refuses one of a state outside the branch.

**Departure: two cases beyond the four the frame lists.** `test_accepts_a_file_with_no_title_whole` pins the clause of `frame/design.md` *Scope* item 2 that a file with no level 1 heading is copied whole. `test_accepts_two_pipe_lines_with_no_delimiter_row_as_written` pins the delimiter test of G7: two lines that open with a pipe and hold no delimiter row are copied as written, and `NO_QUESTION_ROW` does not stand for them. Without them, no case of `Test_compose` held either clause (read, from the fixtures of the frame's four cases, each of which opens with its title and holds a delimiter row in every table). Judged against `skills/implement/SKILL.md` *A new test starts from its group*: each covers a clause nothing in its group covered.

**How each case was seen red.** At `1383f97c`, with the cases written and `pr_body.py` unchanged, `bin/test tests/skills/test_pr_body.py -q -p no:xdist -k Test_compose` exited 1 with 5 failed and 31 passed (executed). Each failing line was read for its guard:

- `test_accepts_a_work_item_as_the_records_text` failed at its `EXPECTED` comparison on the missing `### Rows` line.
- The S2 and S4 case failed at index 4, where the table's header stood in place of `The tree answered these:`.
- The S3 case failed at index 4 the same way, because the two lines of the table with no row were copied.
- The S5 case failed at index 2, where `` `frame/questions.md` holds no table line. `` stood in place of `FROM`.
- The S6 row of `test_refuses_a_record_it_cannot_copy_faithfully` failed on `DID NOT RAISE Refused`.

The no-title case and the pipe-lines case were written after that run. Both were run against the code as it stood at `1383f97c`, in a `git clone --no-local` of that commit under the crafter's scratch directory with the HEAD copy of `tests/skills/test_pr_body.py` (executed: `pytest tests/skills/test_pr_body.py -q -p no:xdist -k` with the two cases, exit 1, 1 failed and 1 passed). The no-title case failed at index 4, where the table's header stood in place of `### Rows`. It was also shown red with the old copy restored as a mutant, `_trimmed(picked)` replaced by `[(raw[i], (QUESTIONS, i + 1)) for i in sorted(tables)]` (executed: `agentic mutate`, mutant 2 of that call red, exit 1). The pipe-lines case passed against the old copy, which copied every line that opens with a pipe, so it takes its red from contract rule 15. With the delimiter test of `_rowless` replaced by `True`, it failed at index 0, where `NO_QUESTION_ROW` stood in place of `| a note |` (executed: `agentic mutate … --tests "… -k test_accepts_two_pipe_lines_with_no_delimiter_row_as_written"`, red, exit 1, its failing line read).

**Mutation.** At `47b8b680`, one call of `agentic mutate skills/code-review/scripts/pr_body.py` with twelve `--replace` pairs and `--tests "bin/test tests/skills/test_pr_body.py -q -x -p no:xdist -k Test_compose"` printed `12 mutants, 12 red, 0 SURVIVED` and exited 0 (executed). The pairs broke these units:

- the title's skip;
- the skip of a delimiter row;
- the `NO_QUESTION_ROW` line;
- the heading's move one level down;
- `NO_QUESTION_TABLE` after a copy with no table;
- the title's level 1;
- the trim of blank ends;
- the whole copy, replaced by the old copy of table lines;
- the grouping of consecutive table lines;
- the run's length of exactly two;
- the delimiter test;
- the words of `NO_QUESTION_ROW`.

**Decisions settled while writing the code.** Each was judged against `frame/design.md` *Scope* item 2 and *Data & interfaces*.

- The title is the first line of `READER.readable` that `heading_level` reads as level 1, wherever it stands. A fenced line is never the title or a heading, because `readable` blanks fenced lines.
- A table with no row is a run of exactly two consecutive table lines whose second line is a delimiter row. Its first line becomes `NO_QUESTION_ROW` in the copy's block and its second is dropped, so the record's own blank lines stand around the fixed line. `READER.is_separator` reads `TABLES.table_cells` of the second line. `pr_body.py` now loads `lib/tables.py` for it, the reader G7 names, and its comment on what it loads says so. `is_separator` answers false for `None`, so no default is passed.
- `NO_QUESTION_TABLE` is a block of its own after the copy, so a blank line stands between the last copied line and it, as `frame/design.md` *Data & interfaces* lays the section out.
- The trim of blank ends moved from `_copied` into `_trimmed`, which `_copied` now calls, so the questions copy drops blank ends the way every other copy does. `_tables` is gone, because `_questions` was its one caller.

**The search of `frame/design.md` G12** printed nothing at `47b8b680` (executed: the command as G12 gives it, from the top level, `git grep` exit 1). Run at `1383f97c`, the same pattern printed the two lines G12 names, `skills/code-review/scripts/pr_body.py:15` and `tests/skills/test_pr_body.py:472`, so it can find what it looks for (executed). The search keeps no line, so the phase has no keep file and changed none.

**The phase-boundary set.** It is the four files the *Verified by* cell names and the tree-wide files of `tests/text` and `tests/behaviour`. No other test file reads a path the phase changed (executed: `git grep -l` for `sdd-plan.md`, `orchestration.md` and `pr_body` under `tests` and `evals`, each hit outside the set read and found to name another file or to name the path in a docstring alone). Every file of the set belongs to the one suite, `bin/test`, so the cell names every suite the set falls in. At `47b8b680`, with this record, `gaps.md`, `changelog.md` and the Status cell written and not yet committed, each command of the cell ran (executed):

- `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py tests/skills/test_agentic.py -q` exited 0, with 776 passed.
- `bin/test tests/text tests/behaviour -q` exited 0, with 891 passed and 10 skipped.
- `uvx ruff check` and `uvx ruff format --check` over `skills/code-review/scripts/pr_body.py` and `tests/skills/test_pr_body.py` each exited 0.

Before `gaps.md` stood, `tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview` failed on this work item, which had no closing memo yet. Writing `gaps.md` is what turned it green.
