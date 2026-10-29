# Phase 1: 1793251204-the-framer-is-handed-the-body-without-its-comments

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 9b5a28bd |

## What this phase was asked

Build `frame/plan.md` *Phases* row 1 as it states it, against the committed
frame at `c1240e0b`, and run the checks its *Verified by* cell names. The
spawn's working rules: edit only through the Edit and Write tools, write
generated case files only through the repository's generator, see a case
red in a scratch copy and never by reverting files in the worktree, and
touch none of the files of #1123, #1127 and #1132.

## What this phase found

**The frame holds against the tree (read).** Every coordinate the plan
names for this phase stands where it says at `c1240e0b`: `base_project`,
`PROBE_ANSWER`, `probe_graders`, `FRAMER_ISSUES`, `framer_case` and
`cases` in `evals/scripts/rule_cases.py`, `Test_framer_case` in
`tests/evals/test_rule_cases.py`, and `MEASUREMENT_ROW` in
`git show 7ac24a06`. `rule_cases.py` is the same file at `0bf22734` and at
`c1240e0b` (executed: `git diff --stat 0bf22734 HEAD -- evals/scripts/rule_cases.py`
printed nothing).

**The revision is computed by running the generator, not stored.** The
frame says the build computes the token by running the case's scaffold and
its generator, and that `shape-answers-by-run` carries it where
`PROBE_ANSWER` carries `STRASSE`. A literal written into `rule_cases.py`
would be a value kept beside the tree, and it would go stale without a word
when `TEXTUTIL` or the generator changed. So `page_revision()` runs the
fixture's `scripts/helpers_page.py` once, through `runpy`, over the files
the scaffold commits, in a temporary directory it removes. The grader file
carries the result as a literal, `d8cac16f`. The case
`test_the_page_case_reads_the_revision_only_a_run_writes` takes the
revision from its own run of the scaffold's files, not from
`page_revision()`.

**The scaffold and the generator, run as an agent would meet them
(executed).** In `<scratchpad>/1158/scaffold-run`, `sh
evals/behaviour/framer/rule-framer-generated-page/scaffold.sh` exited 0 and
left one commit, `base: textutil`, holding `scripts/helpers_page.py` and
`docs/helpers.md` beside the project's files. `python3
scripts/helpers_page.py` exited 0 and printed nothing. It rewrote
`docs/helpers.md` from `Return TEXT upper-cased.` to the docstring's full
sentence, and its last line reads `Revision d8cac16f`, the token in
`graders/shape-answers-by-run.md`. The directory was removed afterwards.

**The sharp-s grader is unchanged.** `PROBE_ANSWER` became
`grounding_answer(token)`, which `probe_graders` calls with `STRASSE`, so
the two cases share one pattern. After regeneration, `git status --short`
listed five `prompt.md` files, the new case directory, the generator and
the test module, and nothing under `rule-framer-sharp-s/graders/`.

**`base_project` takes the case's files as a parameter.** It gained
`extra_files`, committed on `main` with the project's files, and
`framer_case` passes its `files` argument through. The five earlier framer
cases pass none, and their scaffolds are byte for byte what they were.

**Seen red (executed).** The three new cases were run against
`rule_cases.py` at `c1240e0b`, in a `git clone --no-local` under the
scratchpad with the new test module copied in, with the worktree's
`.venv/bin/python -m pytest`. All three failed, and the two existing cases
passed. `test_every_spawn_hands_the_issue_whole` failed with
`AssertionError: loud-flag` because no spawn held the line. The two page
cases failed with `KeyError: 'rule-framer-generated-page'`. The first red
run, in the worktree, was discarded: that case split the prompt at the
first `BEGIN PROMPT`, which the orchestrator's own sentence also holds. The
case now splits at the line `BEGIN PROMPT`, and the clone run above is the
red that counts.

**Mutation (executed, `bin/seal mutate` over `evals/scripts/rule_cases.py`,
each with `bin/test tests/evals/test_rule_cases.py -p no:xdist -q -k
Test_framer_case`).** Each mutation below turned at least one case red:

| Mutation | Red case |
|---|---|
| `has no comments, so its body` to `has no comment, so its body` | `test_every_spawn_hands_the_issue_whole` |
| `MEASUREMENT_ROW` loses `[*`]*` | `test_the_page_case_refuses_a_row_left_to_a_measurement` |
| `**(extra_files or {}),` removed from `base_project` | `test_the_page_case_reads_the_revision_only_a_run_writes` |
| `(?=.*{token})` to `(?=.*)` in `grounding_answer` | that case and `test_refuses_an_answer_in_another_section_or_with_no_label` |
| the `not_contains` of `no_measurement_row` to `contains` | `test_the_page_case_refuses_a_row_left_to_a_measurement` |
| `page_revision` reads `split()[-2]` | `test_the_page_case_reads_the_revision_only_a_run_writes`, after `9b5a28bd` |

The last mutation first passed every case. With it, the grader looked for
the word `Revision`, and each frame text the case tried still read as
before. `9b5a28bd` adds a frame naming another revision, `00000000`, which
the grader must refuse. The same mutation then turned the case red.

**The phase boundary (executed).** `bin/test tests/evals/test_rule_cases.py
tests/behaviour/test_evals_layout.py
tests/text/test_no_case_tells_the_agent_it_is_evaluated.py
tests/github/test_rules.py tests/test_censuses.py
tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py
tests/behaviour/test_every_orchestrator_act_names_its_delivery.py
tests/behaviour/test_the_sealer_guarantees.py
tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py
tests/evals/test_noninferiority.py tests/evals/test_seed_defects.py -q`
exited 0, 588 passed and 2 skipped. That is the plan's five modules and
every other module that `git grep` lists as reading `rule_cases` or
`evals/behaviour`. Its first run failed one census:
`subprocess.run(text=)` in `Test_framer_case.page` named no encoding, so it
reads in cp1252 on the Windows leg. The call now names
`encoding="utf-8"`. `uvx ruff check` and `uvx ruff format --check` over the
two Python files exited 0. `bin/seal layout --pairs` names no pair in
`tests/evals/test_rule_cases.py`.
