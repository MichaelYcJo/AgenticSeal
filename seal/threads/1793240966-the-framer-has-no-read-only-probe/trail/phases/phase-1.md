# Phase 1: 1793240966-the-framer-has-no-read-only-probe

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 60805e77 |

## What this phase was asked

Build `frame/plan.md` *Phases* row 1 against the frame at `d76aec0f`,
under the owner's automation answer, with `frame/questions.md` Q1, Q2 and
Q3 on their defaults. `evals/scripts/rule_cases.py` gains a fifth
`FRAMER_ISSUES` entry, `sharp-s`, whose issue asks what `shout` returns for
`straße` without giving the answer. `framer_case` takes a case's own
graders, and `sharp-s` has two: `shape-answers-by-probe` and
`shape-no-measurement-row`. The docstring's framer line says five issues.
`evals/behaviour/framer/rule-framer-sharp-s/` is the generator's output.
Sibling #1091 edits the same file, so this phase's change to it stays in
the framer case and the docstring's framer line.

## What this phase found

**The frame holds against the tree (read, at `b06716cb`).** The coordinates
the plan names resolve to the text it describes: `agents/framer.md:23-25`,
`:76`, `:86-88`, `:107-108` and `:136-137`; `rule_cases.py:432-505`;
`tests/text/test_a_question_says_who_can_answer_it.py:188-205`. Before the
edit, `rule_cases.py --out <scratchpad>` exited 0 and `diff -r` of its
`framer/`, `crafter/` and `sealer/` against `evals/behaviour/` exited 0
(executed).

**The grader regexes are pinned by two cases, not by a deleted probe.** The
plan's *Verified by* cell asks for a `test_tmp_*` probe, run once and
deleted, showing each regex against a hand-written frame. This phase wrote
the same check as `Test_framer_case` in `tests/evals/test_rule_cases.py`,
the module that already reads `rule_cases.py`'s graders back through
`noninferiority.py#grader_from`. A regex that stops confining its match to
`## Grounding`, or a `not_contains` that loses its `match`, would otherwise
pass every case in the tree, and `seal mutate` needs a case to go red.
`gaps.md` records the divergence.

**How the cases were seen red (executed).** Against `rule_cases.py` at
`b06716cb`, `bin/test tests/evals/test_rule_cases.py -q -p no:xdist -k
framer_case` exited 1 with both cases failing on `KeyError:
'rule-framer-sharp-s'`. After the change it exited 0.

**The patterns hold under the runner's engine too (executed).** The runner
reads a grader's pattern as a JavaScript regex. A `node -e` over the two
committed grader files, against a frame answering in `## Grounding`, one
with the answer in `## Scope`, one with no label, and three questions rows,
printed `true false false true true false`, the same verdicts the Python
cases give.

**`shape-answers-by-probe` accepts `Executed` as well as `executed`.** A
cell may open with the label capitalised. The word `STRASSE` stays
case-sensitive, so `straße` in the issue's own text never matches it.

**`shape-no-measurement-row` reads a cell that opens with `a measurement`**,
backticked or bold or not, and not a cell that mentions a measurement
inside its prose. A question cell saying a measurement would settle it is
not a row left to a measurement.

**Mutation (executed).** One `seal mutate` batch over `rule_cases.py`, six
mutants: the extra graders dropped from `framer_case`, the section bound
removed, the `executed` lookahead removed, the `STRASSE` lookahead removed,
`match="not_contains"` removed, and the answerer word changed. The baseline
passed and all six went red; exit 0.

**The narrow run (executed).** `bin/test tests/evals/test_rule_cases.py
tests/behaviour/test_evals_layout.py
tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q` exited 0,
32 passed. `python3 evals/scripts/rule_cases.py` left `git status --short`
listing only the script, the test module and the new case directory.
`uvx ruff check` and `uvx ruff format --check` over the two Python files
exited 0. `bin/seal layout --pairs` exited 0.
