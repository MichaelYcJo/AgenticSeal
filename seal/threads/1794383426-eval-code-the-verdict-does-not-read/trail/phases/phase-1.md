# Phase 1: 1794383426-eval-code-the-verdict-does-not-read

## What this phase found

**The frame holds, with one exception, judged before the build against the tree at `af8bccf1f`.** Each unit Scope 1 and 2 name stood where `frame/design.md` *Removes* puts it. `noninferiority.py` imported `replay_targets` for `record_reader` alone, inside `finding_rows`, and `tests/evals/test_rule_cases.py` read `grader_from` at lines 104 and 303 alone (read). The exception is Scope 4's destination, described in the next paragraph.

**`scalar` and `grader_from` moved to `evals/scripts/behaviour.py`, not into `tests/evals/test_rule_cases.py`.** `CONTRIBUTING.md` *The test layout* has `bin/seal layout --check` refuse "a class `Test_<name>` naming no top-level definition of TARGET" (read, `skills/verify/scripts/test_layout.py` docstring). `tests/evals/test_rule_cases.py` declares `TARGET = "evals/scripts/rule_cases.py"`, so its file could not hold *Test_scalar* or *Test_grader_from*. `frame/plan.md` *Alternatives considered*, the row on keeping both in `noninferiority.py`, names `behaviour.py` as equal in cost and lets the build take it where the test module proves awkward. The build took it. The two functions and `SCALAR` keep their bodies, beside `grader`, the writer they invert. Their cases stand in a new `tests/evals/test_behaviour.py`, whose `TARGET` is `behaviour.py`. `tests/evals/test_rule_cases.py` reads `behaviour.grader_from` through `load_script("behaviour")`. Judged against `CONTRIBUTING.md` *The test layout* and `frame/plan.md` *Alternatives considered*. `bin/seal layout --check` over the three changed test files: 0 refused (executed). It reports the other seven functions of `behaviour.py` as having no class, which is a report and refuses nothing.

**The move adds no behaviour, so it owes no new case and no mutant.** `skills/verify/SKILL.md` *The narrow command still has to be able to fail* asks for the moved units' existing cases at the new path, plus a census of the old spelling (row *Names or places only*). The six cases of *Test_scalar* and the three of *Test_grader_from* pass at `tests/evals/test_behaviour.py`, with only `NI.` read as `BEHAVIOUR.` (executed). The census `git grep -n -E "NI\.(scalar|grader_from)|ni\.grader_from|noninferiority\.py#(scalar|grader_from)"` outside `seal/threads/`, `.test_durations` and `evals/behaviour/` prints nothing and exits 1 (executed). The same command run at `af8bccf1f` finds `tests/evals/test_noninferiority.py:2066` and `:2191`, so it can find a hit (executed).

**Removals the frame's *Removes* table did not name.** Each one stood on a unit the frame removes, so `skills/core/SKILL.md` *The rule a mechanism is kept against* removes it in the same commit:

- *Test_compare* `test_accepts_sides_holding_a_grader_whose_target_is_a_string` guarded `reads_record` against a target that is a string. `reads_record` goes, and nothing reads a grader's target.
- *Test_parse_record* `test_a_count_row_spelt_otherwise_is_read_as_naught` and `test_a_count_padded_with_more_spaces_is_read` pinned the `evals/README.md` sentence on how `check` finds the four row counts. Both the rows and the sentence go.
- The `_suites` fixture's `wide`, `kind`, `flag` and `plain` commits served only the cases of `regrade` and its units. *Test_git_bytes* now reads `own` where it read `plain`, and the fixture builds three suites.
- The test module lost its helpers for printed records and traces: `finding_block`, `printed`, `record_of`, `three_findings`, `record_truth`, `printed_side`, `cat`, `graded_side`, `regraded_to` and the side spoilers. It also lost the constants `WIDE`, `REPORT`, `ROWS`, `REFUSED_PATH`, `REFUSED_HOST`, `USER_ROOT`, `FENCE`, `FENCED_FIX` and `UNCLOSED`, and the `subprocess` import.
- `noninferiority.py` lost the `copy`, `functools` and `importlib.util` imports and the `sys.path.insert` that let it import `replay_targets`. `compare` lost its `try`/`except ValueError` around `side_numbers`, which raises no `ValueError` once nothing reads `report_text`.
- The `evals/README.md` paragraph on the point a proofer comparison is taken from became **Two sides compare only over one suite**. That keeps the one claim that still holds, `compare`'s refusal of two suite trees, and drops the claim that both sides keep `report_text`.
- `tests/evals/test_noninferiority.py`'s docstring no longer points at `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py`, which phase 2 deletes (Scope 8).

**Each changed case was seen red first (contract rule 15).** Two methods were used:

- **Against the old code at `af8bccf1f`, before `noninferiority.py` changed (executed).** Six cases went red on the line that names their guard:
  - *Test_annotate* `test_accepts_each_runs_cost_and_calls_and_the_sides_meta` and *Test_run_side* `test_accepts_a_saved_side_again_with_no_eval` failed on `report_text` left in the run's `agentic`.
  - *Test_side_numbers* `test_accepts_a_truth_over_a_round_record_as_the_eval_recorded_it` failed on `['truth', 0, 1]` against `['truth', 1, 1]`.
  - *Test_cost_rows* `test_accepts_both_sides_and_the_derived_row` failed on the `tokens per true find` rows in the last two lines.
  - *Test_compare* `test_accepts_a_side_read_before_986` failed on exit 2 against 0.
  - *Test_main* `test_refuses_arguments_it_cannot_use[the removed regrade]` failed on `FileNotFoundError` raised by the old `regrade`, which is not argparse's exit.
- **By `seal mutate` at `7d718955b` (executed, every run read `red`, exit 0, the file restored by the command):**
  - re-adding `| New false rows | 0 |` to `render` turned *Test_render* `test_accepts_two_sides_as_a_record_that_reads_back` and *Test_compare* `test_accepts_one_suite_at_two_commits_and_writes_the_record` red. Each was run alone, and each failed on its `REMOVED_ROWS` line.
  - re-adding a `tokens per true find` row to `cost_rows` turned *Test_cost_rows* red.
  - counting a truth grader only where it is not a truth, in `side_numbers`, turned `test_accepts_a_truth_over_a_round_record_as_the_eval_recorded_it` red.
  - reading `["report_text"]` from each run in `side_numbers` turned `test_accepts_a_side_as_its_graders_and_its_cost` red on `KeyError`.
  - re-adding `"report_text": ""` in `annotate` turned *Test_annotate* red.
  - re-adding a refusal of a side whose runs keep no `report_text` to `compare` turned `test_accepts_a_side_read_before_986` red.
  - re-adding the `regrade` subparser turned `[the removed regrade]` red on `KeyError: 'regrade'`.
  - making `parse_record` refuse a record carrying `Baseline report rows` turned *Test_check* `test_accepts_a_record_written_before_1487_as_it_was_judged` red. That case passes against the old code, which read those rows, so it was shown red against the guard it names: `parse_record` reading past the removed rows.
  - leaving a graders count unconverted in `parse_record` turned *Test_read_record* `test_refuses_a_record_that_does_not_parse_or_says_otherwise` red. That case's input changed from a removed row to a graders cell `x`. The red is a `TypeError` raised by `verdict` once `parse_record` lets the cell through, not the `does not parse` line itself.
  - `ensure_ascii=True` in `write_side` turned *Test_write_side* `test_accepts_the_annotated_side_as_json_with_its_characters` red. That case now takes its non-ASCII characters from the case name, not from a `report_text`.

**S1 (executed).** `python3 evals/scripts/noninferiority.py regrade --side a.json --suite-rev HEAD --out b.json`, run in the phase's scratch directory, exits 2 with argparse's `invalid choice: 'regrade' (choose from 'run', 'compare', 'check', 'model')`. The exit code was read directly.

**For phase 2.**

- `.test_durations` holds 101 `tests/evals/test_noninferiority.py::` keys that `7d718955b` no longer collects (executed, a `json` read against `--collect-only`). They are the cases of Scopes 1 and 2 and nine renamed or rewritten cases. Scope 12 drops them with the rest, where #1486 has not removed the file first.
- `tests/evals/test_rule_cases.py`'s docstring still names `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py` and the recurred truth entries. Scopes 7 and 8 rewrite both.
- `tests/evals/test_rule_cases.py` still imports `load_script` from `tests/evals/test_replay_targets.py`, now for `rule_cases` and `behaviour`. Scope 7's move to `conftest.load_module` covers both.
- `tests/behaviour/test_no_two_truths_of_a_proofer_case_accept_one_location.py:9` still says the noninferiority half of its old module stands in `tests/evals/test_noninferiority.py`. Scope 8 deletes the file.
