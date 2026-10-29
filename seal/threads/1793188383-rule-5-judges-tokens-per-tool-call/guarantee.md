# Guarantee: 1793188383-rule-5-judges-tokens-per-tool-call

| Field | Value |
|---|---|
| Target SHA | 20c1491c against 8a1173c8 |
| Broad gate | 7450dc6a against 8a1173c8 |

The base `release/v0.24.0` resolves through `release/v0.24.0@{upstream}` to
`8a1173c8` (executed, `git rev-parse --verify --quiet`). `trail/gate.md`
names `7450dc6a against 8a1173c8`. `7450dc6a` is an ancestor of HEAD
(executed, `git merge-base --is-ancestor`, exit 0), and
`git log --no-merges --name-only 7450dc6a..HEAD ^8a1173c8` names one commit,
`20c1491c`, which touches only
`seal/threads/1793188383-rule-5-judges-tokens-per-tool-call/trail/gate.md`
(executed). The gate's pass counts are the orchestrator's run and are not
in the record, so they are not judged here (unverified, the orchestrator).
`seal pr-body seal/threads/1793188383-rule-5-judges-tokens-per-tool-call
--body <scratchpad>/992-pr-body.md --check` exited 0 with the installed
`seal` and with the tree's `bin/seal` (executed). `seal/parity.md` is not
in git (executed, `git ls-files`), and routing is `through the review
chain`, so no `original:` line is owed.

The runs below went in a `git clone --no-local` of the branch at
`20c1491c`, under the scratchpad, removed after the audit. The base code was
restored there with `git checkout 8a1173c8 --
evals/scripts/noninferiority.py`, and restored to HEAD after each use.
Term deletions were applied to the module's source text in memory, and no
file was written for them.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The test module passes at the audited commit | `trail/rounds/round-3.md` *Probes*, the run over `tests/evals/test_noninferiority.py` | `.venv/bin/python -m pytest tests/evals/test_noninferiority.py -q -p no:xdist` in the clone at `20c1491c` | holds: exit 0, 255 passed (executed) |
| With the cases written and the code at the base, the module refused to collect, exit 2, `AttributeError` on `TOKEN_MARGIN` | `trail/phases/phase-1.md:90-92` | the same pytest command with `evals/scripts/noninferiority.py` restored from `8a1173c8` | holds: exit 2, `AttributeError: module 'noninferiority_under_test' has no attribute 'TOKEN_MARGIN'`, raised by S5's entry (executed) |
| S1, S4, S5 and S6 go red against the base's rule 5, S3's line differs, and S7 passes at the base | `trail/phases/phase-1.md:93-99`; `frame/design.md:90-97` | `python -c` loading the base `noninferiority.py` and calling `verdict` on each scenario's `numbers()`, extracted from the test module with `ast` | holds: S1, S4, S5 and S6 give `fail` where each case expects `pass`; S3 gives the old per-call line, not the new one; S2 gives `pass`; S7 gives `fail`, so the base could not show it red, as the record says (executed) |
| Round 1's case at `TOKEN_MARGIN` 0.13 goes red with rule 5's `1e-9` deleted, and S5 cannot see the term | `trail/rounds/round-1.md:60`; `trail/phases/phase-1.md:126-134` | `python -c` executing HEAD's module text with `bar = 1 + TOKEN_MARGIN + 1e-9` replaced by `bar = 1 + TOKEN_MARGIN`, then `verdict(numbers(old_tokens=100, new_tokens=113))` at margin 0.13 and S5's numbers at 0.07 | holds: `pass` against the tree, `fail` with the term deleted; S5 gives `pass` either way (executed) |
| Round 2's rule 2 entry, 7 against 8 false in 20, goes red with rule 2's `1e-9` deleted | `trail/rounds/round-2.md:82` | `python -c` executing HEAD's module text with `old_rate + FALSE_MARGIN + 1e-9:` replaced by `old_rate + FALSE_MARGIN:`, then `verdict(numbers(old_false=7, new_false=8))` | holds: `pass` against the tree, `fail` with the term deleted (executed) |
| The 17 records' `check` exit codes, verdicts and rule 5 lines at the base and after, including the nine no round re-ran | `trail/phases/phase-1.md` *What this phase found*, the table of 17; `trail/phases/phase-2.md:20-52` | `python3 evals/scripts/noninferiority.py check <(git show <commit>:<path>)` for each of the 17 coordinates, once with the code at `20c1491c` and once with it restored from `8a1173c8` | holds on all 17 at both commits: after the change only `957-framer-p3` prints a rule 5 line; `967-framer-p4`, `967-warden-p4`, `943-sealer-p3b` and `957-warden-p2` print "it says `fail` and its numbers give `pass`" and exit 1; `957-sealer-p3` keeps rule 3, `969-sealer-model` rules 3 and 4, `943-sealer-p3` rule 4, `985-warden-p3` rules 1 and 2; the seven `pass` records exit 0 (executed) |
| Every `TOKEN_MARGIN` from 0.01 to 0.18 gives the same 17 rule 5 verdicts | `frame/questions.md:54`; `frame/design.md:175-176` | `python -c` parsing the 17 records with HEAD's `parse_record` and calling `verdict` at each margin from 0.00 to 0.25 | holds: 0.01 to 0.18 give the verdicts of 0.07, where rule 5 fails `framer-phase-3.md` of #957 alone; 0.00 and 0.19 and above differ (executed) |
| The old rule's wording printed five lines at the base and none at the phase commit | `trail/phases/phase-1.md:144-156` | `git grep -c -i -e "tool call below" -e "total tokens, tokens per true find" -e "tool call are fewer" 8a1173c8 -- evals tests`, and the same over `HEAD` | holds: two lines in `evals/README.md` and three in `evals/scripts/noninferiority.py` at the base; none at HEAD (executed) |
| Every `## Removes` row of `frame/design.md` and every removal `changelog.md` names is gone from the tree | `frame/design.md:200-206`; `changelog.md:3` | `git grep` at HEAD outside `seal/`, `changelog/` and `CHANGELOG.md` for the removed wording, the reason "Rule 5 divides", the clause "which rule 5 judges from", the old rule 5 reason line, the two old `VERDICTS` names and the `New tool calls \| 90` edit; the diff `8a1173c8...HEAD` read for each docstring and README sentence | holds: nothing stands in a file the rows name. The two old case names stand only in `.test_durations:1616` and `:1618`, a price cache the frame's *Out* list leaves to CI, which states no rule (executed, read) |
| #957's framer side rose 49.7% in all and 18.9% a call | `changelog.md:4` | the `check` run above on `framer-phase-3.md` at `2fc33333` | holds: 4736908 over 3164345 tokens and 33595.1 over 28253.1 a call (executed) |

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the spec | `frame/design.md`: rule 5 fails only where the total and the figure per call both rose past `TOKEN_MARGIN = 0.07`, a figure exactly at the margin passes, the reason line as given, the cases S1 to S10, the 17 records re-read with no paid run; rules 1 and 2 out of scope on Q2's default | the issue's *Done when*, which names rule 5's statistic, its cases in `#verdict`, and the re-read of #957, #967, #969, #975, #976, #943 and #985 at no cost; the tree, where the comparison, the constant and the reason line match *Data & interfaces* (read, the diff) | none |
| the build | the diff and `trail/phases/phase-1.md` and `phase-2.md`: the rule, the constant, the reason line, the cases, the docstrings and README item 5 rewritten in place, and S9's prediction holding on all 17 records | the spec; the re-runs above; the issue's figures for #943's second sealer side (2883649 over 81 against 2585256 over 72) and #967's framer side (120 calls to 109) | none. The plan's phase 2 cell "0 for `pass` and 1 for `fail`" disagreed with `check`'s exit, and `gaps.md` *Where spec and implementation diverged* names it with its grounds, which the re-run confirms |
| the last round | `trail/rounds/round-3.md`: round 2's close `fixed 217209f3` holds, nothing opened; `trail/rounds/round-2.md` confirms round 1's close `fixed a0fc6988` | the tree, where both `1e-9` cases stand and each goes red with its term deleted (executed, above) | none |
| the changelog | `changelog.md`: the new rule at 7%, the new reason line, total tokens now judged through rule 5, the 17 records re-read with one rule 5 fail and three records turning to `pass`, `check` exiting 1 on those three | the build, the `check` re-runs and the diff of `evals/README.md` | none |
| the orchestrator's part of the pull request body | under `## Not from the records`: `Closes #992` | the issue's *Done when*, which names rule 5 alone and is met | none. The issue's section *The same shape on rules 1 and 2* widens its question to rules 1 and 2, and the work defers that to `frame/questions.md` Q2's default, `gaps.md` *Not done*; closing the issue is consistent with *Done when*, and what is left of the wider question is the owner's (below) |

Left to the owner, none of which holds the seal: `frame/questions.md` Q1
(`TOKEN_MARGIN`'s size, built on 0.07), Q2 (rules 1 and 2 against a
baseline drawn high, built on "rule 5 alone") and Q3 (the measured spread
of the total, which the margin is applied to unmeasured) stay `open`. Once
`Closes #992` closes the issue, Q2's row in this work item is the only
place the rules 1 and 2 question stands: `seal/follow-up.md` names neither
#992 nor that question (executed, `grep`).

Verdict: sealed
