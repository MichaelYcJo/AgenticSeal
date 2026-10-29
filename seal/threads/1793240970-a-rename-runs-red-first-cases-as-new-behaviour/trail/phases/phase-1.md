# Phase 1: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 771ab8c4 |

## What this phase was asked

Build `plan.md` row 1: the crafter rename case of `frame/design.md` *Data &
interfaces*, added to `cases()` in `evals/scripts/rule_cases.py`, with the
module docstring's crafter line corrected and no other line of that file
touched, because sibling #1047 edits the same file. The case directory is
written by running the generator, and no other case changes. Then show the
case red against the base's crafter definition, paying as `frame/questions.md`
Q1's default says, with `--max-cost-usd 15` on the call.

## What this phase found

The frame held, except for one spelling. The plan's command passes
`--case rule-crafter-rename` to `noninferiority.py run`, which hands it to
`claude plugin eval --case`. That flag is a glob over the case's `name:`
field, and the generator writes the name as `crafter rule-crafter-rename`.
The first call matched no case and spent nothing (`No eval cases found
matching --case "rule-crafter-rename"`, `costUsd` 0). The run that counts
used `--case '*rule-crafter-rename'`. Phase 2's two runs need the same glob.
`gaps.md` records it as a divergence.

The three graders every crafter case ends with, the phase record, the
commit and no probe left behind, moved into `crafter_closing`. That move is
proved the way the new verify row says a move is proved: the generator ran
and `git status --short evals/behaviour` listed only
`evals/behaviour/crafter/rule-crafter-rename/`, so the four build cases came
out byte for byte as committed (executed).

The new unit is `crafter_rename_case`. No pytest case reads the crafter
cases the generator writes; `tests/behaviour/test_evals_layout.py` compares
only the sealer cases with the generator's output. So `seal mutate` was run
with `--tests` regenerating the suite and then running the layout and word
cases, and the generator was run once more after both runs to put the
committed case back. Both mutants went red (executed):

- `{HERE}` dropped from the rename case's spawn paragraph:
  `test_a_behaviour_prompt_says_where_the_repository_is` failed.
- `fixture` added to the rename case's design text:
  `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` failed.

The graders' patterns are proved only by the paid runs below.

`bin/test tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py
tests/text/test_no_case_tells_the_agent_it_is_evaluated.py -q`: 30 passed,
exit 0 (executed). `uvx ruff check` and `uvx ruff format --check` over
`evals/scripts/rule_cases.py`: exit 0 (executed).

The case was seen red against the base's definitions (executed):
`python3 evals/scripts/noninferiority.py run --agent crafter --rev 1e82fd0a
--suite-rev HEAD --case '*rule-crafter-rename' --runs 2 --max-cost-usd 15`,
exit 0, at a suite of 771ab8c4. Both runs failed `shape-no-mutation`, and
every other grader passed on both. Run 0 called `seal mutate src/textutil.py`
once, and run 1 called it twice, each time to break the renamed `exclaim`.
Neither run wrote a second test function. So `frame/questions.md` Q2 reads
red on both runs, and the case is planted as it stands. The side cost
$1.12 in all, $0.55 and $0.57 a run, 67 and 69 seconds. Its saved output is
`base-rename.json` and `base-rename.raw/` in the session's scratchpad, under
`1793240970-a-rename-runs-red-first-cases-as-new-behaviour/`. Q3 reads that
the crafter can start `noninferiority.py run` from its own environment.
