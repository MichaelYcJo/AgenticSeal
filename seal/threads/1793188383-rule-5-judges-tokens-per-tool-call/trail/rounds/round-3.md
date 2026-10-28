# Review round 3: 1793188383-rule-5-judges-tokens-per-tool-call

target: 90643a05, fixes 68ba0f4e..90643a05

This is the verifying round after round 2. The fix range holds two commits.
`217209f3` adds round 2's entry to `VERDICTS` in
`tests/evals/test_noninferiority.py`. `90643a05` commits round 2's record
with the fix pass's `verdict:` and `answer:` lines. The range touches no
file under `evals/` (read, `git diff 68ba0f4e..90643a05 --stat`: two files,
the test module and round 2's record). The runs below went in a
`git clone --no-local` of the branch at `90643a05`. `seal/parity.md` is not
declared, so no `original:` line is written.

Carried from earlier rounds as coordinates and not established again here:
round 1's confirmations of the rule 5 code, its reason line, its docstrings
and the 17 `check` runs, and round 2's sweep of the class, which found three
float tolerances in `evals/scripts/noninferiority.py` (rule 2's at `:851`,
rule 5's at `:898`, `SCORE_ERROR` at `:1241`). The fix range changes none of
those lines. This round re-ran the three-mutant batch over the whole module
only to see rule 2's deletion go red.

## Findings

No finding.

## Confirmations

confirms: round-2#1
The close `fixed 217209f3` holds. Claimed: `217209f3` adds the round's entry
unchanged between the two rule 2 entries, and the entry went red with the
term deleted. Found: the entry stands at
`tests/evals/test_noninferiority.py:1477-1480` with the name, numbers and
expected verdict round 2 gave, between "rule 2: false rate up by exactly
the margin" and "rule 2: false rate up past the margin" (read). Round 2's
first command, three mutants over the whole module, now gives 3 red and 0
SURVIVED. At `22cf7b81` rule 2's deletion SURVIVED in that batch (executed,
`## Probes`). The entry is the case that catches it. With it deselected
(`-k 'not 0.35'`), rule 2's deletion SURVIVED over the other 254 cases.
Run alone, the entry went red with `('fail', [...]) == ('pass', [])` at
`:1596` (executed). Against the tree it passed as
`Test_verdict::test_accepts_a_new_side_no_worse_than_the_baseline[rule 2:
exactly the margin, where 0.35 + 0.05 falls short of 0.40]` (executed). The
float fact in its name holds: `7/20 + 0.05` comes out as
0.39999999999999997, below `8/20` (executed). `verdict` computes the rate
as `old_false / old_rows` and adds `FALSE_MARGIN` and `1e-9` at
`evals/scripts/noninferiority.py:845-851` (read), so the entry exercises
the same sum.

confirms: none
The fix left nothing standing on the old fact, that rule 2's edge had no
case. `git grep` for "rule 2", `FALSE_MARGIN` and "false-finding rate" over
the work item outside its round records, and over `evals/README.md`, finds
no sentence saying rule 2's edge is unpinned (executed). The sentences
that cite rule 2's `1e-9` as precedent, `frame/design.md:37-38` and `:111`,
`frame/questions.md:25-27` and the comment at
`evals/scripts/noninferiority.py:895`, state that a rate exactly at the
margin passes. A case now pins that, so each is truer than before (read).
The fix pass's answer says no phase record, `gaps.md` or `changelog.md`
needed a correction. That matches this search. The fix pass changed only
the `verdict:` and `answer:` lines of round 2's finding 1 (read,
`git diff 68ba0f4e..90643a05`). `docs/the-review-record.md` allows the fix
pass those two lines.

confirms: none
The new entry was read against its group, the rule 2 entries of `VERDICTS`.
"rule 2: false rate up by exactly the margin" moves 2 in 20 to 3 in 20.
There `0.1 + 0.05` comes out as 0.15000000000000002, above `3/20`, so that
entry passes with or without the term (executed). The new entry covers the
side the old one cannot. The mutant run with it deselected SURVIVED, and
with it alone went red (executed). `bin/seal layout --pairs` exited 0 and
names no pair in `tests/evals/test_noninferiority.py` (executed).

confirms: none
The new case's identifier has no price in `.test_durations`, as round 1
found for the cases renamed by phase 1. `test_the_durations_file_prices_the_suite`
passed over the whole collection at `90643a05` (executed). So the missing
price unbalances the shards and drops no case, as `CONTRIBUTING.md` says,
and the refresh stays with CI.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch, the format of the new entry among them | the branch at `90643a05` | the orchestrator, at its one `seal gate` run (contract rule 2) |
| The `check` rows of the nine records round 1 did not re-run, carried from round 1 and outside this fix range | `seal/threads/1793188383-rule-5-judges-tokens-per-tool-call/trail/phases/phase-2.md` | the sealer, in its sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate evals/scripts/noninferiority.py`, three mutants (rule 2's term deleted, `SCORE_ERROR = 0`, rule 5's term deleted) over `bin/test tests/evals/test_noninferiority.py -q -p no:xdist` | exit 0: baseline green; 3 mutants, 3 red, 0 SURVIVED |
| `bin/seal mutate` with rule 2's term deleted, over `-k 'not 0.35'` | exit 1, SURVIVED: 254 passed, 1 deselected |
| `bin/seal mutate` with rule 2's term deleted, over `-k 0.35` | exit 0, red: the new entry failed at `:1596` with `('fail', [...]) == ('pass', [])` |
| `bin/test tests/evals/test_noninferiority.py -q -p no:xdist -k 0.35 -rA` against the tree | exit 0, 1 passed |
| `python3 -c` printing `0.1 + 0.05`, `3/20`, `7/20 + 0.05`, `8/20` and whether the third is below the fourth | 0.15000000000000002, 0.15, 0.39999999999999997, 0.4, True |
| `bin/seal layout --pairs` | exit 0, no pair in `tests/evals/test_noninferiority.py` |
| `bin/test tests -q -p no:xdist -k test_the_durations_file_prices_the_suite` | exit 0, 1 passed |
| `git status --short` in the clone after each mutation run | nothing printed: every mutant was restored |
| `bin/test tests/evals/test_noninferiority.py tests/behaviour/test_a_rewritten_definition_proved_non_inferior.py tests/behaviour/test_evals_layout.py tests/evals/test_rule_cases.py -q` in the branch worktree with this record on disk | exit 0, 284 passed. This is not the full suite |
| `bin/seal layout --check` in the branch worktree | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` in the branch worktree | exit 0, all 266 check lines in 55 rule files hold |
| `chain_check.py --baseline origin/release/v0.24.0 --root <worktree> --worktree` | exit 0. Its two lines name `gate.md` and `guarantee.md`, which are not yet written |
