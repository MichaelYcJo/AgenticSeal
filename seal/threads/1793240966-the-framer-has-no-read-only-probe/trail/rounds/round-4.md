# Review round 4: 1793240966-the-framer-has-no-read-only-probe

target: 062ce1db, fixes e4278641..062ce1db

This round verifies the repair made after the orchestrator's broad run at
`e4278641`. The range holds one commit, `062ce1db`, and it changes
`tests/evals/test_rule_cases.py` alone. No finding named the repair, and
round 3 closed nothing, so no close is owed an answer here. Carried from
earlier rounds without searching again: phase 1's reason for keeping the
grader check as cases in this module (`gaps.md:11`, round 1), and the
removal of `shape-no-measurement-row` at `7ac24a06`. Neither is in this
range. Re-derived here: what each new case pins, whether the two cases hold
every assertion the one case held, whether the layout check now passes,
and when the layout refusal began.

## Findings

None.

## Confirmations

confirms: none
The split keeps every assertion the one case held. Read: the diff
`e4278641..062ce1db` of `tests/evals/test_rule_cases.py`. The removed case
`test_the_sharp_s_case_reads_the_probes_answer_in_grounding_alone` held
four assertions. `test_accepts_a_probes_answer_on_a_grounding_line` at
`tests/evals/test_rule_cases.py:269-275` holds two of them: the grader's
`match` is `contains`, and the pattern finds `PROBED`.
`test_refuses_an_answer_in_another_section_or_with_no_label` at `:277-282`
holds the other two: the pattern finds neither `ELSEWHERE` nor
`UNLABELLED`. The fixtures at `:235-250` and the `graders` helper at
`:254-267` are unchanged. No assertion was rewritten or dropped.

confirms: none
Each case pins what its name and docstring say, and the two together catch
every mutant the one case caught. Executed: two `seal mutate` batches over
`evals/scripts/rule_cases.py` in the round's clone, each running one case
alone with `-k`. Both batches used the same five mutants of
`PROBE_ANSWER` and `probe_graders` at `evals/scripts/rule_cases.py:436-453`:

- 1: the `## Grounding` section bound removed.
- 2: the `executed` lookahead removed.
- 3: the `STRASSE` lookahead removed.
- 4: `STRASSE` changed to `STRASSEX`.
- 5: `match="not_contains"` added to the grader.

The accepting case went red on mutants 4 and 5 and let 1 to 3 survive. The
refusing case went red on mutants 1 to 3 and let 4 and 5 survive. Each
batch exited 1 because of its survivors. So the accepting case pins the
grader's `contains` match and a pattern that finds the probed line. The
refusing case pins the section bound and both lookaheads. Every mutant is
red under one case or the other. The mutation result shows these cases are
tested against these five changes. It does not show the pattern is safe
against an edit outside them. This agrees with the repair's account that
three `seal mutate` runs turned each case red.

confirms: none
The layout check now passes, and the class it refused holds its pair.
Executed in the round's clone at `062ce1db`: `bin/seal layout --check
tests` exited 0, with 161 files read and 0 refused. The case the broad run
failed on, `tests/skills/test_test_layout.py`
`Test_main::test_accepts_this_repositorys_tests`, exited 0 with 1 passed.
`bin/test tests/evals/test_rule_cases.py -q -p no:xdist` exited 0 with 16
passed. `uvx ruff check` and `uvx ruff format --check` over the module each
exited 0. Read against its group: `Test_framer_case` holds only these two
cases, and `bin/seal layout --pairs tests/evals/test_rule_cases.py` exited
0 with 0 pairs. Neither new case covers what the other covers. The
enumeration over the whole `tests/` tree found no other class refused, so
no other instance of the defect stands.

confirms: none
The repair's account dates the refusal wrongly, and the repair is right
regardless. The commit message of `062ce1db` claims the layout check
refused `Test_framer_case` "once its measurement-row case left with the
grader at 7ac24a06". The orchestrator's prompt repeats it. Executed:
`bin/seal layout --check tests/evals/test_rule_cases.py` at `60805e77`, at
the parent of `7ac24a06` and at `e4278641`. Each exited 1 with the same two
lines: the class has no `test_accepts_` case and no `test_refuses_` case.
The class was refused from phase 1's `60805e77`, where its two cases were
named `test_the_sharp_s_case_reads_...` and
`test_the_sharp_s_case_refuses_...`. Neither name opens with either
prefix, and `skills/verify/scripts/test_layout.py:306-311` reads only the
prefix. No record of this work item claims a `layout --check` pass.
Executed: `git grep -n "layout --check"` over the work item exited 1. Phase
1's record at `trail/phases/phase-1.md:74` claims only `bin/seal layout
--pairs`. So the wrong date stands in a commit message and nowhere in the
tree. A record written after this round should not carry that date.

confirms: none
No text in the tree names the removed case. Executed: `git grep -n` at
`062ce1db` for `test_the_sharp_s_case`, `reads_the_probes_answer` and
`in_grounding_alone` exited 1. The work item's prose names the class,
`Test_framer_case`, and never a case in it: `gaps.md:11`,
`trail/phases/phase-1.md:34` and `changelog.md:7`. Each still reads true
of the module at `062ce1db`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch: `unverified`, not run by this round under contract rule 2 | the branch at `062ce1db` | the orchestrator, at `seal gate --base release/v0.24.1 --record 1793240966-the-framer-has-no-read-only-probe` |
| Whether the new rule made the other four framer cases worse: carried from round 1, still unmeasured | `evals/behaviour/framer/` | the owner, at #947's milestone run |

This round leaves nothing open. What comes due is the orchestrator's broad
run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the branch worktree into the round's scratch directory, then a detached checkout of `062ce1db` | exit 0, then 0 |
| `bin/test tests/evals/test_rule_cases.py -q -p no:xdist` | exit 0, 16 passed |
| `bin/seal layout --check tests` | exit 0, 161 files read, 0 refused |
| `bin/seal layout --pairs tests/evals/test_rule_cases.py` | exit 0, 1 file read, 0 pairs |
| `bin/test tests/skills/test_test_layout.py -q -p no:xdist -k test_accepts_this_repositorys_tests` | exit 0, 1 passed |
| `bin/seal layout --check tests/evals/test_rule_cases.py` at `60805e77`, at the parent of `7ac24a06` and at `e4278641`, each a detached checkout in the clone, then back to `062ce1db` | exit 1 at each, with the two `refused:` lines for `Test_framer_case` |
| `bin/seal mutate evals/scripts/rule_cases.py` with the five mutants above, `--tests "bin/test tests/evals/test_rule_cases.py -q -p no:xdist -k test_accepts_a_probes_answer_on_a_grounding_line"` | exit 1; baseline green; mutants 4 and 5 red, 1 to 3 survived |
| The same five mutants with `-k test_refuses_an_answer_in_another_section_or_with_no_label` | exit 1; baseline green; mutants 1 to 3 red, 4 and 5 survived |
| `uvx ruff check` and `uvx ruff format --check` over `tests/evals/test_rule_cases.py` | exit 0 and 0 |
| `git grep -n` at `062ce1db` for the removed case's name in three parts | exit 1, no hit |
| `git grep -n "layout --check"` over the work item | exit 1, no hit |
| `git status --short` in the clone after both mutation batches | exit 0, empty: `seal mutate` restored the file |
