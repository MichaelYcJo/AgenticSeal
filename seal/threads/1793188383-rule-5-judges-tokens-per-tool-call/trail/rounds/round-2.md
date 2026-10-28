# Review round 2: 1793188383-rule-5-judges-tokens-per-tool-call

target: 22cf7b81, fixes 8935f33c..22cf7b81

This is the verifying round after round 1. The fix range holds three
commits: `a0fc6988` adds round 1's case to `tests/evals/test_noninferiority.py`,
`aa768a6b` corrects phase 1's record, and `22cf7b81` commits round 1's
record with the fix pass's lines. The fix range touches no file under
`evals/` (executed, `git diff --quiet 8935f33c 22cf7b81 -- evals`, exit 0).
So round 1's confirmations of the rule 5 code, the reason line, the
docstrings and the 17 `check` runs are carried as coordinates and not
judged again here. The runs below went in a clone of the branch at
`22cf7b81`. `seal/parity.md` is not declared, so no `original:` line is
written.

The orchestrator's prompt reported a second instance of round 1's class,
rule 2's `1e-9` term, which stands outside the fix range at the base. It is
judged below as finding 1, under contract rule 12.

## Findings

### 1. Rule 2's `1e-9` term has no case: deleting it leaves every case green

severity: should
location: `tests/evals/test_noninferiority.py:1476-1477`, `evals/scripts/noninferiority.py:851`
evidence: executed `bin/seal mutate evals/scripts/noninferiority.py --replace "    if new_rate > old_rate + FALSE_MARGIN + 1e-9:" "    if new_rate > old_rate + FALSE_MARGIN:" --replace "SCORE_ERROR = 1e-9" "SCORE_ERROR = 0" --replace "bar = 1 + TOKEN_MARGIN + 1e-9" "bar = 1 + TOKEN_MARGIN" --tests "bin/test tests/evals/test_noninferiority.py -q -p no:xdist" --timeout 600`, `bin/seal mutate evals/scripts/noninferiority.py --replace "    if new_rate > old_rate + FALSE_MARGIN + 1e-9:" "    if new_rate > old_rate + FALSE_MARGIN:" --tests "bin/test tests/evals/test_tmp_rule2_epsilon.py -q -p no:xdist" --timeout 300`, `python3 -c "print(0.1 + 0.05, 3/20, 0.35 + 0.05, 8/20, 100 * (1 + 0.13))"`
verdict: open

Rule 2 passes a false-finding rate that rose by exactly `FALSE_MARGIN`. The
`1e-9` in its comparison (`evals/scripts/noninferiority.py:851`) is what
keeps that true where the float sum of the old rate and the margin comes
out just below the exact edge. No case notices the term's removal. Deleting
it SURVIVED over the whole module, while deleting rule 5's term and zeroing
`SCORE_ERROR` each went red in the same batch (executed, the first command
above).

This is round 1's finding again, in its second instance. The cause is the
same: the case named for the edge sits where float arithmetic rounds the
safe way. The entry "rule 2: false rate up by exactly the margin"
(`tests/evals/test_noninferiority.py:1476`) moves a rate of 2 in 20 to 3 in
20. `0.1 + 0.05` comes out as 0.15000000000000002, above `3/20`, so it
passes with or without the term. This is S5's position at 0.07, which round
1 found (executed, the third command above).

The branch rests its own rule on this unpinned fact. `frame/design.md:37-38`
and `:111` say a figure exactly at `TOKEN_MARGIN` passes as a rate exactly
at `FALSE_MARGIN` passes rule 2. `frame/questions.md:25-27` lists that
under "Answered by the tree" and cites rule 2's `1e-9`. The comment at
`evals/scripts/noninferiority.py:895` says the same. Contract rule 12 owes
the fix to every instance of one cause. The frame's *Out* list keeps rules
1 and 2 against a baseline drawn high out of scope. That item is a question
about which sides form the baseline. A case pinning rule 2's edge changes
no rule and no behaviour, and it goes in a file this branch already edits.
So the instance is within the work item's reach, and it is the first rung
of the filing ladder.

The term decides real inputs. The orchestrator's prompt carried the
crafter's count of 67 rate pairs up to 60 rows. This round's own count,
`Fraction` arithmetic over every pair of up to 60 rows a side, gives 67
too (executed, `## Probes`). One of them uses the fixture's own 20 rows: a
baseline of 7 false in 20, 0.35, against 8 false in 20, 0.40. `0.35 + 0.05`
comes out as 0.39999999999999997, below `8/20`. So without the term rule 2
fails a side exactly at the margin. The case below was seen red with the
term deleted (the second command above, verdict red). It passed against the
tree as it stands (`## Probes`). The probe asserted
`NI.verdict(numbers(old_false=7, new_false=8)) == ("pass", [])`, which is
what `Test_verdict::test_accepts_a_new_side_no_worse_than_the_baseline`
asserts for an entry of `PASSING`.

Add this entry to `VERDICTS`, between the two rule 2 entries at
`tests/evals/test_noninferiority.py:1476-1477`:

```python
    "rule 2: false rate up by exactly the margin": (numbers(new_false=3), "pass"),
    "rule 2: exactly the margin, where 0.35 + 0.05 falls short of 0.40": (
        numbers(old_false=7, new_false=8),
        "pass",
    ),
    "rule 2: false rate up past the margin": (numbers(new_false=4), "fail"),
```

answer:

## Confirmations

confirms: round-1#1
The close `fixed a0fc6988` holds. Round 1's case stands unchanged as
`Test_verdict::test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short`
at `tests/evals/test_noninferiority.py:1594-1601` (read). Round 1's third
command used a probe file. This round re-ran that command with the
committed case in the probe's place. With `bar = 1 + TOKEN_MARGIN` the case
went red: `bin/seal mutate evals/scripts/noninferiority.py --replace "bar =
1 + TOKEN_MARGIN + 1e-9" "bar = 1 + TOKEN_MARGIN" --tests "bin/test
tests/evals/test_noninferiority.py -q -p no:xdist -k
test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short"`, verdict
red (executed). Round 1's first command, deleting the term over the whole
module, also went red now, where at `3a222053` it SURVIVED (executed, the
first command of finding 1, mutant 3). The case's docstring states the
float fact it rests on: `100 * (1 + 0.13)` comes out as
112.99999999999999, below 113 (executed, the third command of finding 1). The case
monkeypatches its own margin, so it does not read `TOKEN_MARGIN`'s value.
`frame/questions.md` Q1 and the `gaps.md` *Not verified* row still hold:
a change of Q1's answer changes one constant, and no case changes with it.

confirms: none
The fix left nothing standing on the old fact. Phase 1's claim that each
unit added has a case behind it is rewritten in place at
`trail/phases/phase-1.md:109-111`, naming the `1e-9` as the exception, and
`:126-134` says why the sign-flip mutant missed it and which case now pins
it (read). The mutant table at `:116-122` still lists the `- 1e-9` mutant
turning S5 red, which is still true. `git grep -n -i -e "case behind" -e
"every unit" -e "each unit" -e "1e-9"` over `evals`, `tests` and the work
item finds no other sentence stating that every unit had a case (executed).
`changelog.md` states no case and needs no change. The fix pass appended the
phase record's path to round 1's `location:` line and said so in its
answer. `docs/the-review-record.md` *The fix pass writes two lines per
finding and nothing else in the file* allows that append (read).

confirms: none
The new case was read against its group. S5, "rule 5: both figures exactly
at the margin", sits at 0.07, where the term changes no verdict, and it
SURVIVED the term's deletion in round 1. The new case went red on the same
mutant. So it covers what its group did not. `bin/seal layout --pairs`
exited 0 and names no pair in `tests/evals/test_noninferiority.py`
(executed).

confirms: none
The class was enumerated over the tree. `git grep -n -E
"1e-[0-9]+|1E-[0-9]+|EPSILON|math\.isclose|sys\.float_info"` over `*.py`
and `*.sh` finds three float tolerances, all in
`evals/scripts/noninferiority.py`: rule 2's at `:851`, rule 5's at `:898`,
and `SCORE_ERROR` at `:1241` (executed). `SCORE_ERROR = 0` went red over
the module and rule 5's deletion went red. Rule 2's deletion survived, and
it is finding 1 (executed, the first command of finding 1).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch, the format of the new case among them | the branch at `22cf7b81` | the orchestrator, at its one `seal gate` run (contract rule 2) |
| The `check` rows of the nine records round 1 did not re-run, carried from round 1 and outside this fix range | `seal/threads/1793188383-rule-5-judges-tokens-per-tool-call/trail/phases/phase-2.md` | the sealer, in its sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `git diff --quiet 8935f33c 22cf7b81 -- evals` | exit 0: the fix range changes no file under `evals/` |
| `bin/seal mutate` over `bin/test tests/evals/test_noninferiority.py -q -p no:xdist`, three mutants: rule 2's term deleted, `SCORE_ERROR = 0`, rule 5's term deleted | exit 1: baseline green; rule 2's deletion SURVIVED; `SCORE_ERROR = 0` red; rule 5's deletion red |
| `bin/seal mutate` with rule 5's term deleted, over `-k test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short` | exit 0, red: `Test_verdict::test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short` failed at `:1601` |
| `test_tmp_rule2_epsilon.py`, one case asserting `NI.verdict(numbers(old_false=7, new_false=8)) == ("pass", [])`, under `bin/seal mutate` with rule 2's term deleted | exit 0, red: `'fail' != 'pass'` |
| `bin/test tests/evals/test_tmp_rule2_epsilon.py -q -p no:xdist` against the tree | exit 0, 1 passed. File deleted after the run |
| `python3 -c` over every rate pair of up to 60 rows a side, counting the pairs `Fraction` puts exactly at the margin whose float verdict differs with and without the term | 67 pairs, among them 1 in 3 against 23 in 60 and 7 in 20 against 8 in 20 |
| `python3 -c` printing `0.1 + 0.05`, `3/20`, `0.35 + 0.05`, `8/20`, `100 * (1 + 0.13)` | 0.15000000000000002, 0.15, 0.39999999999999997, 0.4, 112.99999999999999 |
| `bin/seal layout --pairs` | exit 0, no pair in `tests/evals/test_noninferiority.py` |
