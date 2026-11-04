# Guarantee: 1793795305-the-behaviour-suite-is-a-smoke-run

Audited at `30a74c55e` against `release/v0.32.0`, which resolves to
`479a79d15` (executed: `git rev-parse --verify --quiet` on
`release/v0.32.0@{upstream}`, the first form that answered). The audit
worked in two clones under the session's scratchpad, one at HEAD and one
at-base clone, both removed after their runs.

`trail/gate.md` names the run `267057237 against 479a79d15`. `267057237`
is an ancestor of HEAD, and `git log --no-merges --name-only
267057237..HEAD ^479a79d15` lists one commit, `30a74c55e`, touching only
`seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run/trail/gate.md`
(executed). `seal pr-body seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run --body <the prompt's file> --check`
exits 0, with both the installed copy and the tree's `bin/seal`
(executed). `seal/parity.md` is absent at HEAD (executed: `ls`), so no
comparison with an original is owed. No earlier `guarantee.md` stands.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The S4 cases, committed before `verdict` changed, give 14 failed and 50 passed against the base's verdict, each failure a case D1 to D5 reworked (`seen red`) | `trail/phases/phase-1.md`, *How each changed case was shown red*, first item | In the at-base clone at HEAD with `evals/scripts/noninferiority.py` restored from `479a79d15` (HEAD's test module equals `4a9e1dd56`'s, executed: `git diff --quiet`): `bin/test -q -p no:xdist tests/evals/test_noninferiority.py -k "Test_verdict or Test_render or Test_read_record or Test_check_record or Test_parse_record or Test_cheaper_model or Test_check or Test_model or Test_tokens_read"` | Holds (executed, exit 1): 14 failed, 50 passed. The eight converted rows fail `== ("pass", [])` on `fail` (recall, false rate, bytes, tokens) or on `no result` (the four unknown figures); the two order cases and `Test_render` fail on the `(rule 3)` suffix and the `non-inferiority` title; the A1 case fails on rule 5's line; the edited-cell case fails on `any("(rule 1)" ...)` |
| The spelt-otherwise row-count case goes red with the row pattern loosened alone (`seen red`, a not-read case, rule 15) | `trail/phases/phase-1.md`, mutant 6 | At-base clone, HEAD's code, `header_field`'s pattern changed to accept any spaces around the pipes, name and value; `bin/test -q -p no:xdist tests/evals/test_noninferiority.py -k Test_parse_record` | Holds (executed, exit 1): the four ids of `test_a_count_row_spelt_otherwise_is_read_as_naught` fail on `assert NI.parse_record(edited)[0]["new_false"] == 0` (`15 == 0`), the guard it names |
| The padded row-count case goes red with the value made to refuse a space alone (`seen red`) | `trail/phases/phase-1.md`, mutant 7 | At-base clone, HEAD's code, `(?P<v>[^|]*)` changed to `(?P<v>[^| ]*)`; same command | Holds (executed, exit 1): `test_a_count_padded_with_more_spaces_is_read` fails on `== 15` (`0 == 15`) |
| `model_numbers`' own verdict fails rule 3 alone, and goes red with rule 3's test broken (`seen red`) | `trail/phases/phase-1.md`, D3 and mutant 3 | At-base clone, HEAD's code, `np_ < nruns` changed to `np_ < 0` at `evals/scripts/noninferiority.py:834`; `bin/test -q -p no:xdist tests/evals/test_noninferiority.py -k Test_cheaper_model` | Holds (executed, exit 1): `test_accepts_sonnet_where_every_grader_holds_and_it_spent_less` fails on its verdict assertion, `('pass', []) == ('fail', [...])` |
| The record cases of gap 1 fail their record through rule 1 (`seen red`) | `trail/phases/phase-1.md`, D3 and mutant 5 | At-base clone, HEAD's code, `if new_total < old_total:` changed to `if False:`; `bin/test -q -p no:xdist tests/evals/test_noninferiority.py -k "Test_read_record or Test_check_record or Test_check or Test_model"` | Holds (executed, exit 1): exactly the five the record names fail, `Test_read_record`, `Test_check_record[fail]`, the edited-cell case, `Test_check` and `Test_model[edited]` |
| The plan row's nine modules pass at the phase's tree (`executed`) | `trail/phases/phase-1.md`, *The phase-boundary run*; `frame/plan.md` *Phases* | HEAD clone: `bin/test -q` over the plan row's nine modules and `tests/text/test_a_cited_commit_outlives_the_squash.py` | Holds (executed, exit 0): 412 passed |
| `VERDICTS` went from 35 rows to 25 | `trail/phases/phase-1.md` D1; `frame/design.md` *Removes* | `git show <rev>:tests/evals/test_noninferiority.py`, the keys of `VERDICTS` counted at `479a79d15` and at HEAD | Holds (executed): 35 and 25 |
| A Sonnet record with an unknown token count prints `sonnet` where it printed `opus` | the orchestrator's part of the pull request body, *Behaviour a reader may notice*; `trail/rounds/round-1.md` | `python3 -I` loading the script from `479a79d15` and from HEAD, `verdict` and `cheaper_model` on one record with `new_tokens=None`, every grader held, spend 5.0 against 10.0 | Holds (executed): base `no result`, `opus`; HEAD `pass`, `sonnet` |
| Every `## Removes` row stands nowhere in the tree: rules 1, 2, 4 and 5, the unknown-figure `no result`, `FALSE_MARGIN`, `TOKEN_MARGIN`, the rule 5 reasoning, the README's pass rules 1, 2, 4 and 5, the old `VERDICTS` rows and cases, the old module name | `frame/design.md` *Removes*; `changelog.md` | HEAD clone: `git grep -n -E 'FALSE_MARGIN\|TOKEN_MARGIN' -- ':!seal/' ':!CHANGELOG.md'`; `git grep -n -i -E '\(rule [45]\)\|five pass\|non-inferiority\|recall fell\|false-finding rate rose\|not below the' -- evals/ tests/evals/ README.md README.ko.md`; `grep` for the unknown-figure reason in the script; `git ls-files '*non_inferior*'`; `git grep -n proved_non_inferior -- ':!seal/'`; and the diff read | Holds (executed): the first three print nothing (exit 1); the listing prints nothing; the old module name stands only in `.test_durations:139`, a timing entry `frame/design.md` *Grounding* leaves to the runner, which is no statement of the suite's purpose |
| The `## Rule changes` `from` text stands in `docs/running/measuring-a-run.md` | `frame/design.md` *Rule changes*, acceptance A8 | `python3 -I`, the `from` text searched in the file with whitespace collapsed | Holds (executed): present |
| The measure is cited at a commit `main` reaches, and it is #1038's | `frame/plan.md` *Judgments of the run*; the orchestrator's part of the body | `git merge-base --is-ancestor 569780eff origin/main`; `git show 569780eff:<the measure's phase-1.md>`, row C8; `gh pr view 1257` | Holds (executed): ancestor; row C8 states 28 records, 15 fails, one confirmed defect read by rule 3's shape graders, decision `narrow`; #1257 closes #1038 |
| `release_report.py` prints each agent's preload bytes against the last tag on a pull request into `main` | `evals/README.md:49-51`; `frame/design.md` *Removes*, rule 4 row | read `.github/scripts/release_report.py:1-16` and `.github/workflows/test.yml:259` | Holds (read) |
| The version moves to `0.32.0` in the commit that adds the fragment | `frame/plan.md` *Operational impact* | `git log --name-status 479a79d15..HEAD` | Holds (executed): `9c36bbdac` changes `.claude-plugin/plugin.json` and adds `changelog.md`; `479a79d15` holds `0.31.2` |
| The broad run passed at `267057237`: 6315 passed, 12 skipped, chain exit 0 | the orchestrator's part of the pull request body, last paragraph | none; the broad gate is the orchestrator's (contract rule 2) | `unverified` by this audit; `trail/gate.md` records the run (read), and the orchestrator answers for its output |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | `verdict` keeps old rule 3's three clauses as rules 1 to 3 and judges nothing else; unknown figures give a verdict; the title reads `smoke run`; S5 rewrites the README bullet, the module name and four docstrings; the `docs/` sentence goes through `## Rule changes` | the issue's *What changes*, *What stays* and *Done when*; the diff; the phase record; the last round | none |
| the build | The diff does S1 to S5, folded at `c6b0fecb6` to gaps 1 and 2 and D1 to D7; every changed case was seen red, and the not-read cases with their one guard removed | the design; the re-runs above; the tree | none |
| the last round | `trail/rounds/round-1.md` at `c6b0fecb6`: no finding; one surviving mutant (`np_ <= nruns`) also survives at the base in unchanged code; the `model` result changes with `verdict`'s narrower `no result` | the diff; the re-runs above. HEAD descends from `c6b0fecb6` by records only | none |
| the changelog | `changelog.md`: the verdict keeps three rules on the shape and reach graders; the other figures judge nothing; unknown figures get a verdict; the title and reason suffixes change; and "`evals/README.md` *The behaviour suite* and the README bullet in both editions say the same, and say that the proofer's reading of the diff judges whether a rewrite means the same" | the diff and the issue on every clause but the last | The tree: the README bullet in both editions says nothing of the proofer. `README.md:356-359` reads "holds the cases of a smoke run, through `claude plugin eval`, that catches a rewrite of an agent's definition breaking the shape of its output. CI checks their shape.", and `README.ko.md:362-365` says the same in Korean. Only `evals/README.md:21-22` says the proofer's reading judges it |
| the orchestrator's part of the pull request body | The three rules and the figures that judge nothing; the version move; the enumeration method and its sample; the two gaps and the ten rows; the frame fold and re-cited measure; round 1 opened nothing; the `model` change a reader may notice; `refactor:`; the broad run | the design, the build, the round, `trail/gate.md` and the re-runs above | none; the broad run's printed figures are its own, `unverified` here |

The one disagreement is the changelog's last clause against
`README.md:356-359` and `README.ko.md:362-365`, which the tree decides. The
fix is to that sentence of
`seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run/changelog.md`
alone, so that it says only `evals/README.md` *The behaviour suite* names
the proofer's reading, and then the pull request body's records copy is
written again by `seal pr-body`. A commit that touches only the work item's
directory leaves `trail/gate.md`'s run standing.

```seal
target: 30a74c55e against 479a79d15
Verdict: withheld reason: changelog.md says the README bullet in both editions says that the proofer's reading of the diff judges whether a rewrite means the same, and README.md:356-359 and README.ko.md:362-365 say nothing of the proofer
```

## Re-audit at `b31d26cd3`

Audited at `b31d26cd3` against `release/v0.32.0`, which still resolves to
`479a79d15` (executed: `git rev-parse --verify --quiet` on
`release/v0.32.0@{upstream}`, the first form that answered). The audit
read the repository's tree at HEAD and checked out nothing.

`trail/gate.md` still names the run `267057237 against 479a79d15`.
`267057237` is an ancestor of HEAD (executed: `git merge-base
--is-ancestor`, exit 0), and `git log --no-merges --name-only
267057237..HEAD ^479a79d15` lists three commits, `30a74c55e`
(`trail/gate.md`), `2dfc67b3b` (`guarantee.md`) and `b31d26cd3`
(`changelog.md`), each touching only
`seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run/` (executed).
`seal pr-body seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run --body <the prompt's file> --check`
exits 0, with both the installed copy and the tree's `bin/seal`
(executed). `seal/parity.md` is not tracked at HEAD (executed: `git
ls-files`), so no comparison with an original is owed.

Since the earlier block's `target:` `30a74c55e`, `git diff --stat
30a74c55e HEAD` changes `changelog.md` (one line) and `guarantee.md`
alone (executed). No claim of the earlier block has a coordinate outside
the work item's directory that a commit since touched, so the earlier
re-runs stand for the code at HEAD and none is run again; the changelog's
claims and the parties are read again.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| `evals/README.md` *The behaviour suite* says the verdict's three rules and the figures that judge nothing, and says that the proofer's reading of the diff judges whether a rewrite means the same | `changelog.md`, last sentence, first clause | read `evals/README.md:15-58` at HEAD | Holds (read): lines 17-22 state the smoke run and that the proofer's reading judges it; lines 37-44 state rules 1 to 3; lines 46-48 say recall, the false-finding rate, the tokens and the preload's bytes judge nothing |
| The README bullet in both editions says the cases are a smoke run for gross breakage | `changelog.md`, last sentence, second clause | read `README.md:356-359` and `README.ko.md:362-365` at HEAD, and `git diff 479a79d15...HEAD -- README.md README.ko.md` | Holds (read): both say the cases are a smoke run that catches a rewrite breaking the shape of an agent's output, which is the gross breakage the issue's *What changes* defines as output "broken in a way its shape graders read"; neither says anything of the proofer, and the changelog no longer says they do |
| The changelog's other clauses: the five old rules, the 28 records and one confirmed defect, the three rules, the figures that judge nothing, unknown figures given a verdict, the record title and the reason suffixes | `changelog.md`, all but the last sentence | `git diff 30a74c55e HEAD -- seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run/changelog.md` | Holds (executed): those clauses are unchanged since `30a74c55e`, where the earlier block re-ran them against the tree |
| The pull request body's records copy carries the repaired sentence | the body file, line 28 | `seal pr-body ... --check`, exit 0; read the body file | Holds (executed, read) |
| The broad run passed at `267057237`: 6315 passed, 12 skipped, chain exit 0 | the orchestrator's part of the pull request body, last paragraph | none; the broad gate is the orchestrator's (contract rule 2) | `unverified` by this audit; `trail/gate.md` records the run (read), and the orchestrator answers for its output |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged since `30a74c55e` (executed: `git diff --stat`): S1 to S5, the three rules, the `## Rule changes` sentence | the issue, the diff, the phase record, the last round | none |
| the build | unchanged since `30a74c55e`: the diff does S1 to S5 as folded at `c6b0fecb6` | the design; the earlier block's re-runs; the tree | none |
| the last round | `trail/rounds/round-1.md` at `c6b0fecb6`: no finding. HEAD descends from it by the work item's records only | the diff; the earlier block's re-runs | none |
| the changelog | the same account as before, and its last sentence now says `evals/README.md` *The behaviour suite* states the smoke run and names the proofer's reading, while the README bullet in both editions states the smoke run for gross breakage | the issue's *What changes*; `evals/README.md:17-48`; `README.md:356-359`; `README.ko.md:362-365`; the diff | none |
| the orchestrator's part of the pull request body | unchanged in substance: the three rules, the version move, the enumeration method, the two gaps, the frame fold, round 1 opened nothing, the `model` change, `refactor:`, the broad run | the design, the build, the round, `trail/gate.md`, the changelog | none; the broad run's printed figures are its own, `unverified` here |

The disagreement the earlier block withheld on is gone: the changelog's
last sentence now says of the README bullet only what `README.md:356-359`
and `README.ko.md:362-365` state, and the body's records copy is the
records' text at HEAD.

```seal
target: b31d26cd3 against 479a79d15
Verdict: sealed
```
