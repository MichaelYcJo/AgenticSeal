# Review round 1: 1793188383-rule-5-judges-tokens-per-tool-call

target: 3a222053 against origin/release/v0.24.0

This is round 1, so no earlier round's coordinates are carried. Every fact
below was opened or run this round. The code, the cases and the records
were read at `3a222053`. The `check` and mutation runs went in a clone of
the branch at that commit. The base runs used the same clone at `8a1173c8`.
`seal/parity.md` is not declared, so no `original:` line is written.

## Findings

### 1. Rule 5's `1e-9` term has no case: deleting it leaves every case green

severity: should
location: `tests/evals/test_noninferiority.py:1588`, `evals/scripts/noninferiority.py:898`
evidence: executed `bin/seal mutate evals/scripts/noninferiority.py --replace "bar = 1 + TOKEN_MARGIN + 1e-9" "bar = 1 + TOKEN_MARGIN" --replace "    if new_t > old_t * bar and new_t * old_c > old_t * new_c * bar:" "    if False:" --tests "bin/test tests/evals/test_noninferiority.py -q -p no:xdist -k 'Test_verdict or Test_check_record'" --timeout 600`, `bin/seal mutate evals/scripts/noninferiority.py --replace "    if new_t > old_t * bar and new_t * old_c > old_t * new_c * bar:" "    if False:" --replace "bar = 1 + TOKEN_MARGIN + 1e-9" "bar = 1 + TOKEN_MARGIN" --tests "bin/test tests/evals/test_noninferiority.py -q -p no:xdist -k 'exactly and margin'"`, `bin/seal mutate evals/scripts/noninferiority.py --replace "bar = 1 + TOKEN_MARGIN + 1e-9" "bar = 1 + TOKEN_MARGIN" --tests "bin/test tests/evals/test_tmp_rule5_epsilon_case.py -q -p no:xdist"`
verdict: open

The phase 1 record claims that every unit added has a case behind it. Its
mutant table turns `+ 1e-9` into `- 1e-9` and shows S5 go red. That mutant
moves the bar below the margin. It does not test whether the term is
needed. With the term deleted (`bar = 1 + TOKEN_MARGIN`), the whole
`Test_verdict` and `Test_check_record` batch stays green, and so does S5
run alone (the deletion is reported SURVIVED in both runs).

The term cannot matter at the shipped margin. In binary floating point,
`1 + 0.07` comes out just above 1.07. Token and call counts are integers,
so an integer times that bar never rounds below the exact edge. At 0.07,
the term changes no verdict, and no case at 0.07 can pin it. It does matter
at other margins. At `TOKEN_MARGIN = 0.13`, a baseline of 100 tokens over
100 calls against 113 tokens over 100 calls passes with the term and fails
without it (executed, the third command above: red on the mutant). S5 does
not cover that either: at 0.13 its 1000000-token baseline passes with or
without the term (executed arithmetic, `## Probes`).

`frame/questions.md` Q1 is still open, so the margin can change. The frame
says a figure exactly at the margin passes (`frame/design.md` *Scope* 1 and
*Data & interfaces*, "The rule"). For some margins the term is the only
thing that keeps that true, and today nothing would notice its removal.
`agents/crafter.md` *Mutation-test every unit you added* says a unit that
stays green while broken has nothing behind it.

Add this case to `Test_verdict`. It was seen red against the term deleted
(the third command above). The pass half is the arithmetic in `## Probes`
for the same values. The fix pass runs the case once against the tree to
see it green.

```python
    def test_passes_a_figure_exactly_at_a_margin_whose_float_falls_short(
        self, monkeypatch
    ):
        """1 + 0.13 comes out just below 1.13 in binary floating point, so a
        baseline of 100 tokens times it falls under 113; the 1e-9 in rule 5's
        bar is what passes a side exactly at that margin."""
        monkeypatch.setattr(NI, "TOKEN_MARGIN", 0.13)
        assert NI.verdict(numbers(old_tokens=100, new_tokens=113)) == ("pass", [])
```

answer:

## Confirmations

confirms: none
Rule 5 is built as `frame/design.md` *Data & interfaces* states it. The
comparison at `evals/scripts/noninferiority.py:896-899` fails a side only
where the total and the figure per call both exceed the baseline's times
`1 + TOKEN_MARGIN`. It stays cross-multiplied, and a figure exactly at the
margin passes. The reason line at `:900-906` matches the frame's template
word for word, and for S3 it gives the frame's sentence
(`tests/evals/test_noninferiority.py:1646-1650`). `TOKEN_MARGIN = 0.07` sits
beside `FALSE_MARGIN` at `:102-108`, with the comment naming its source.
The no-result guard at `:822-831` returns before rule 5 wherever either
side's calls are None or zero, so the two divisions in the reason line
cannot divide by zero. `bin/test tests/evals/test_noninferiority.py -q`
exited 0 with 253 passed (executed).

confirms: none
The phase 2 table matches `check` runs this round took itself, on 8 of the
17 records: `957-framer-p3`, `957-sealer-p3`, `957-warden-p2`,
`967-framer-p4`, `967-warden-p4`, `943-sealer-p3b`, `969-sealer-model` and
`968-framer-p2`. Each was extracted with `git show <commit>:<path>` at the
coordinate the table names, then run at `3a222053` and at the base
`8a1173c8`. Every exit code, verdict and rule 5 line agrees with
`trail/phases/phase-2.md` and with phase 1's base column. After the change,
`957-framer-p3` prints the new rule 5 line and exits 1. `957-sealer-p3`
keeps only its rule 3 line, and `969-sealer-model` keeps its rule 3 and
rule 4 lines. `967-framer-p4`, `967-warden-p4` and `943-sealer-p3b` print
"it says `fail` and its numbers give `pass`" and exit 1. `968-framer-p2`
exits 0 with nothing printed (executed). S9's prediction holds on these 8.

confirms: none
The `gaps.md` divergence on `check`'s exit code holds. Claimed: `check`
exits 1 whenever a record's stated verdict differs from the one its numbers
give, so phase 2 read the computed verdict from the printed line. Found:
the module docstring at `evals/scripts/noninferiority.py:60-62` says exit
1 means "the record's verdict is not `pass`, or it disagrees with its
numbers". `957-warden-p2` exits 1 with "it says `fail` and its numbers give
`pass`" both at the base and after. The three records turned to `pass` do
the same (executed). The plan's cell, "0 for `pass` and 1 for `fail`", was
the error. Reading the printed line was the right reading, and the
divergence row says so with its grounds.

confirms: none
S7 and S8 go red with rule 5's comparison removed. Claimed: `seal mutate`
showed both red after commit `c6e47cfe`, not before it, against contract
rule 15. Found: the mutant `if False:` in place of the comparison turned
S7 red when run alone (`-k 'past and margin'`) and S8 red when run alone
(`-k test_refuses_an_edited_cell_the_verdict_does_not_follow`) (executed).
The base fails both scenarios too, so neither could be shown red against
the tree as `agents/crafter.md` step 5 asks. The ordering is a fact about
the build, not a defect in the tree: neither case passes against the defect
it was written for. The S8 case also checks that rule 5 is named
(`tests/evals/test_noninferiority.py:1865`), as the frame's S8 row asks.

confirms: none
Every sentence outside `seal/`, `changelog/` and `CHANGELOG.md` that states
rule 5 now states the new rule. `git grep` over the tree for "rule 5",
"per tool call", "tokens per call", "judge nothing", "tokens read", "pass
rules", "tokens fall", "noninferior" and "not worse", and over the Korean
files for "규칙 5", "도구 호출" and "토큰", finds rule 5 stated only in
`evals/README.md:47-53` and in `evals/scripts/noninferiority.py` (the
module docstring at `:51-53`, `#tool_calls` at `:428-434`, `#verdict` at
`:783-786` and the `#cost_rows` docstring at `:980-982`) (executed). Each
states both figures and the margin. The phase 1 grep for the old wording
prints nothing. `README.ko.md` and `docs/` state no pass rule. Three test
docstrings name rule 5 or the figure per call
(`tests/evals/test_noninferiority.py:98-101`, `:158-159`, `:1017-1018`),
and each stays true under the new rule (read). The one copy of the rule
outside those files is the seeded case
`evals/behaviour/proofer/seeded-8a100e13/scaffold.sh`. It pins its own
revision, `4279671d`, so this branch's line numbers do not reach it (read).

confirms: none
The `#cost_rows` docstring line is 107 columns, not about 99 as the hand-off
says (`evals/scripts/noninferiority.py:982`, executed `awk`). `ruff.toml:53`
selects `E4`, `E402`, `E7` and `E9` and not `E501`, and `ruff format` does
not wrap a docstring, so neither CI step refuses the line (read). The base
already carried a 94-column docstring line at `:52`, which this change
removed. The line only reads badly, so it is no finding. A rewrap that
breaks it after "which judges nothing." would match the docstrings around
it.

confirms: none
`.test_durations:1616-1618` still name the three old case identifiers.
`CONTRIBUTING.md:166-183` says this unbalances the shards and drops no
case, and that `test_the_durations_file_prices_the_suite` decides when the
file is refreshed: it fails only when more than one collected case in
twenty has no price. That case passed against the whole collection at
`3a222053` (executed, `bin/test tests -q -k
test_the_durations_file_prices_the_suite`, exit 0). Leaving the file to CI,
as the frame's *Out* list says, is safe.

confirms: none
`TOKEN_MARGIN`'s source resolves. `git show
0ed5dd3b:seal/specs/1792251842-the-smith-is-written-anew-from-its-job/overview.md`
reads at its lines 53-55 that the same `writing-style` text gave 6.0% below
the baseline in one take and 0.8% above it in the other, "two takes 6.8
points apart" (executed). 0.07 is the smallest whole percent above that.

confirms: none
The design's *Out* claim that `#cheaper_model` is untouched holds on the
one record it reads. `noninferiority.py model` on `969-sealer-model` at
`3a222053` exits 0 and prints `opus` with its shape-grader line, because
the record's stated `fail` still agrees with its numbers after rule 5's
line drops (executed).

confirms: none
Each new or rewritten case was read against its group. S5, "both figures
exactly at the margin", is the only entry at the edge. S4 sits at 5%, and
the sign-flip mutant turns S5 alone red. S7, "both figures past the
margin", sits 0.1 points past the edge. S3's 10% stays red under any bar
up to 1.10, so S3 does not pin the edge. The rewritten S8 pins a record
that says `pass` while its numbers give `fail`, and
`test_refuses_anything_but_pass[fail]` pins one that says `fail`: these are
different states. `bin/seal layout --pairs` exited 0 and names no pair in
`tests/evals/test_noninferiority.py` (executed).

confirms: none
Issue #992's *Done when* is met. The statistic is chosen in `#verdict`, and
its cases stand in `VERDICTS`, `Test_verdict` and `Test_check_record`. The
recorded sides of #957, #967, #969, #975, #976, #943 and #985, with #968's,
are read again with no paid run in `trail/phases/phase-2.md`. The issue's
section *The same shape on rules 1 and 2* sits under `gaps.md` *Not done*
on `frame/questions.md` Q2's default, which the frame keeps out of scope.
`gaps.md` labels the suite, the lint and the typecheck `unverified`, with
the orchestrator as their answerer (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `check` rows of the nine records this round did not re-run: `957-smith-p3`, `957-warden-p2-run-1`, `957-warden-p3`, `967-smith-p4`, `969-sealer-p4`, `975-sealer-p4`, `976-sealer-p5`, `943-sealer-p3` and `985-warden-p3` | `seal/threads/1793188383-rule-5-judges-tokens-per-tool-call/trail/phases/phase-2.md` | the sealer, in its sample of the crafter's claims |
| The full suite, the repository-wide lint and the typecheck over the branch | the branch at `3a222053` | the orchestrator, at its one `seal gate` run (contract rule 2) |

## Probes

| Command | Result |
|---|---|
| `git show <commit>:<path>` for 8 of the 17 records into the round's scratch directory, then `python3 evals/scripts/noninferiority.py check <record>` in the clone at `3a222053` and again at `8a1173c8` | 16 runs. Exit 1 on every record except `968-framer-p2`, which exits 0 both times. Every printed line matches `trail/phases/phase-1.md` and `trail/phases/phase-2.md` |
| `python3 evals/scripts/noninferiority.py model <969-sealer-model>` at `3a222053` | exit 0, `opus` |
| `bin/seal mutate` with the term deleted and the comparison as `if False:`, over `-k 'Test_verdict or Test_check_record'` | exit 1: baseline green; term deleted SURVIVED; `if False:` red |
| the same two mutants over S7 alone, S8 alone and S5 alone | S7: deleted SURVIVED, `if False:` red. S8: `if False:` red. S5: both SURVIVED |
| `test_tmp_rule5_epsilon.py`, S5's fixture at margins 0.07 and 0.15 with the bar computed with and without `1e-9` | exit 0; both margins give `pass` either way, so S5's fixture cannot see the term. File deleted |
| `test_tmp_rule5_epsilon_case.py`, finding 1's case, under `bin/seal mutate` with the term deleted | red: `('fail', [...]) == ('pass', [])`. File deleted |
| `python3 -c` over margins 0.07, 0.11, 0.13 and 0.15 and baselines 100, 1000 and 1000000, rule 5's comparison with and without `1e-9` | only margin 0.13 at a baseline of 100 differs: `fail` without the term and `pass` with it |
| `bin/test tests/evals/test_noninferiority.py -q` | exit 0, 253 passed |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` in the clone | exit 0, 1 passed |
| `bin/seal layout --pairs` | exit 0, no pair in `tests/evals/test_noninferiority.py` |
| `bin/test <modules> -q` over the 107 test modules that `git grep -l` under `tests/` finds for a changed path or its basename, in the branch worktree with this record on disk | exit 0, 5941 passed and 16 skipped. This is not the full suite: 160 test files exist |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `chain_check.py --baseline origin/release/v0.24.0 --root <worktree> --worktree` | exit 0. The one refusal on this record is finding 1's `verdict: open`. `gate.md` and `guarantee.md` are not yet written |
