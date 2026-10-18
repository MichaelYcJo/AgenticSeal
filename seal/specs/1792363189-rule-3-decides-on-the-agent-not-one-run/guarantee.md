# 1792363189-rule-3-decides-on-the-agent-not-one-run — guarantee

<!-- seal/specs/<unix-epoch-seconds>-<slug>/guarantee.md, written by the
sealer alone and committed by the orchestrator beside `broad-gate.md`.
`docs/the-review-record.md` §*The guarantee* holds the rules and
`agents/sealer.md` the order of work. -->

| Field | Value |
|---|---|
| Target SHA | a754ab94 against 769f2aa4 |
| Broad gate | 5ababb7e against 769f2aa4 |

The base `release/v0.22.2` resolves through `@{upstream}` to 769f2aa4. The
orchestrator ran the broad gate and this run only read its record.
`broad-gate.md` names 5ababb7e, which is an ancestor of HEAD
(`git merge-base --is-ancestor`, exit 0). The only commit after it is
a754ab94, and that commit touches only
`seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/broad-gate.md`
(`git log --no-merges --name-only 5ababb7e..HEAD ^769f2aa4`). So the run
stands at HEAD. Every re-run below was in two scratch clones of a754ab94
under the scratchpad, `at-base/`, with `evals/scripts/noninferiority.py`
restored from 769f2aa4, and `at-head/`. Both were removed before the
hand-back. The tree under audit was not changed except for this file.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 and S5 seen red against the code before the change | `phases/phase-1.md:65`, `:69` | in `at-base/`: `pytest -p no:xdist -q -rA <test module>::test_the_verdict_is_recomputed_from_the_records_numbers <test module>::test_rule_3_names_the_total_and_each_grader_failing_every_new_run` | holds: both FAILED. The base wrote the old per-grader reasons, "shape grader c1/shape-report-exists passed 1/2 on the new side, less often than the baseline's 2/2 (rule 3)" and the reach equivalent |
| S3's reason entry was also red against the old code | `phases/phase-1.md:67` | same run | holds: `[a grader fails every new run, the total held]` FAILED, as did `[the total falls]` and the order entry |
| S2 seen red with the total check made `if False:`, together with the reach rename, S6 and the order entry | `phases/phase-1.md:66` | in `at-head/`, a scratch driver replaced `if new_total < old_total:` (asserting exactly one match) and ran the same two tests, then restored the file | holds: exit 1, 5 failed. They were the shape rename, the reach rename, S6, `[the total falls]` and the order entry |
| S3 seen red with the naming clause made `if False:` | `phases/phase-1.md:67` | same driver, `if op and not np_:` → `if False:` | holds: exit 1, 3 failed (S3's case, S3's reason entry and the order entry) |
| S4 seen red, alone, with the naming clause naming every 0/n grader | `phases/phase-1.md:68` | same driver, `if op and not np_:` → `if not np_:` | holds: exit 1, 1 failed (S4) |
| S6 seen red, with the order entry, when the totals cover graders the baseline lacks | `phases/phase-1.md:70` | same driver, `and v[2] and v[4]` → `and v[4]` | holds: exit 1, 2 failed (S6 and the order entry) |
| The phase's narrow run: 88 passed | `phases/phase-1.md:76-77`; PR #982 body, §*How it was verified* | in `at-head/`: `pytest -p no:xdist -q tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py` | holds: exit 0, 88 passed |
| The six re-read records are what `compare` writes from #957's committed sides | `phases/phase-2.md:25-27` | in `at-head/`, six times: `noninferiority.py compare --agent <a> --phase <N> --old <#957>/evals/baseline-<a>.json --new <#957>/evals/<name>.json --out <scratch>`, then `cmp` with `evals/957-<name>.md` | holds: compare exited 0 and cmp exited 0 for all six |
| `check` on the six exits 0 for `pass` and 1 for `fail`, and none prints "it says …" | `phases/phase-2.md:59-62` | `noninferiority.py check evals/957-<name>.md`, six times | holds: 0, 1, 0, 0, 1, 1 in S9's order, no "it says" line in any |
| `check` on #957's own `warden-phase-2.md` reports the disagreement | `plan.md:89-96`, `phases/phase-2.md:64-67`, `changelog.md:38-40` | `noninferiority.py check <#957>/evals/warden-phase-2.md` | holds: exit 1, "it says `fail` and its numbers give `pass`" |
| Each `## Graders` section is byte-identical to #957's | `phases/phase-2.md:50-52`; PR body, §*How it was verified* | `diff` of the `## Graders` section cut by `awk`, six times | holds: all exit 0, at 53, 53, 53, 29, 37 and 22 lines |
| S9's verdicts and reasons | `spec.md:121-128`, `changelog.md:28-35` | read `Verdict:` blocks of `evals/957-warden-phase-2-run-1.md` and `evals/957-sealer-phase-3.md` | holds: run 1 fails on the one naming line for `warden seeded-9b644676/shape-findings`. The sealer record fails on the total line (29/30 against 30/30) and on rule 5 |
| Removes 1: the per-grader `elif` and its reason line are gone from `verdict` | `spec.md:173` | `git grep -n -e 'np_ \* oruns < op \* nruns' -e 'less often than the baseline' -- evals/scripts tests evals/README.md`, and `grep -n '^def '` for function bounds | holds: the one hit is `evals/scripts/noninferiority.py:961`, inside `cheaper_model` (941-970), out of scope by `spec.md:66-71`. It is unchanged from base line 938. `verdict` (578-712) has none |
| Removes 2–4: the README and both docstrings no longer state the per-grader clause | `spec.md:174-176` | `git grep -n -i -e 'each shape and reach grader' -e '3 each shape' -- evals tests`; `git grep -n 'at least as often' -- evals tests` | holds: both exit 1, no hit |
| Removes 5: the two old case names are gone | `spec.md:177` | `git grep -n` on both names with their closing quote, whole tree | holds: no hit in `tests` or `evals`. The only hit is `spec.md:177` itself, the Removes row. `.test_durations` is out of scope by `spec.md:79-81` |
| Rules 1, 2, 4, 5, `cheaper_model` and the suite are untouched | `changelog.md:11-13`; PR body | `git diff -U0 769f2aa4...HEAD -- evals/scripts/noninferiority.py \| grep '^@@'`; `git diff --stat 769f2aa4...HEAD -- evals/behaviour` | holds: the hunks are at the module docstring and lines 586-667 of `verdict`, which are rule 3. Nothing under `evals/behaviour/` changed |
| Round 1's finding is fixed in #957's `spec.md` | `rounds/round-1.md:11`, `rounds/round-2.md:9-23` | `git diff 769f2aa4...HEAD -- seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md` | holds: the rule 3 clause now points to `evals/README.md` rule 3 and says #957's phases judged per grader |
| The re-read's input stands in for `run --from-raw` | `spec.md:82-88`, `spec.md:21` | read `seal/specs/1792126889-…/guarantee.md:35-36` | holds: #957's sealer recorded the committed sides as byte-identical to what `run --from-raw` writes (executed by that sealer, read here) |
| PR #982 body: the new cases for "the total, the naming clause, pooled shape and reach, a grader the baseline lacks, and the order of the reason lines" were "each seen failing against the old rule first" | PR #982 body, §*How it was verified*, table row 1 | the `at-base/` run in row 1 | does not hold. Against 769f2aa4's `verdict`, these CASES entries PASSED: `rule 3: a grader the baseline lacks does not offset a lost run` (S6), `rule 3: a grader failing every new run where the baseline passed it, the total held` (S3), `rule 3: a grader the baseline never passed, failing every new run, is not named` (S4), and both renamed total cases. Only S1, S5 and the three `RULE_3_REASONS` entries failed there. S6 has no reason entry, so no case for "a grader the baseline lacks" fails against the old rule. `phases/phase-1.md:59-70` records that S2, S3, S4 and S6 were seen red only under a mutation |

Not re-run, and so `unverified`: phase 1's other mutations. These are
`common` left unsorted, `<` → `<=`, per-kind totals for S5, and each
reason text reworded (`phases/phase-1.md:69`, `:72-74`). Round 1 settled
them by reading, and this run sampled the four above. The narrow
`bin/test tests/test_the_changelog_is_gathered_at_release.py
tests/test_no_passage_is_pasted_into_a_second_file.py` of
`phases/phase-2.md:74-76` was also not re-run. The broad run at 5ababb7e
covers both modules (read, `broad-gate.md`).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The issue (#966 `## Decision`) | Rule 3 aggregates per agent. A side's total shape and reach passes against the baseline's, and a grader failing every new run where the baseline passed it is caught by name. Done when the rule is in `verdict` with its cases, and #957's records are re-read at no cost "from the kept raw output (`run --from-raw`)" | the tree (`verdict` at 660-693), the spec, the build, both rounds, the changelog, the PR body | none in substance. The re-read went through `compare` over the committed sides, not `run --from-raw`, because the raw output is gone. #957's guarantee shows those sides byte-identical to `run --from-raw`'s output, so "at no cost, from the kept output" holds |
| The spec | Pooled total plus naming clause. Graders the baseline lacks stay outside the totals and must pass every new run. Exact reason lines. Five Removes rows. S9's predicted verdicts | the issue, the tree, the build, the changelog | none. Its S2-as-own-case and S8 grep are corrected in `overview.md` §*Where spec and implementation diverged*, and the tree bears both corrections out |
| The build (the diff, `phases/phase-1.md`, `phases/phase-2.md`) | Rule 3 rewritten as the spec says. S1/S5 red against the old code, and S2–S6 red under mutations. 88 passed. Six re-reads match S9 | the issue, the spec, the tree (every sampled claim above holds), the rounds, the changelog | none |
| The last round (`rounds/round-2.md` at 4205fd6e) | Round 1's one `should` is closed at 7d2bc3d1. The sweep of the old rule's statements is complete. Nothing opens | the tree (the #957 `spec.md` diff), the build | none |
| The changelog fragment | Rule 3 now judges the agent. It quotes both reason-line forms. Rules 1, 2, 4, 5, `--runs`, the suite and `model` are unchanged. The case where one run still decides. The six-record table. The `check` disagreement on old records | the tree, the six records, the spec | none |
| The pull request body (PR #982) | What changes, the before/after table, the six-record table, and a verification table whose first row says each new case was "seen failing against the old rule first" | the issue, the tree and the changelog on everything else it states | the build and the tree, on its verification table's row 1. `phases/phase-1.md:59-70` says only S1 and S5 were run against the old code, and that S2, S3, S4 and S6 were seen red under mutations. Against 769f2aa4 the S6 case (a grader the baseline lacks) passes, and so do the S3 and S4 cases (executed, row 1 and the last row above) |

Verdict: withheld — PR #982's body, §*How it was verified* table row 1, says the new cases for "the total, the naming clause, pooled shape and reach, a grader the baseline lacks, and the order of the reason lines" were "each seen failing against the old rule first". Against 769f2aa4's `verdict`, the S6 case `rule 3: a grader the baseline lacks does not offset a lost run` passes, and so do the S3 and S4 cases. Only S1, S5 and the three `RULE_3_REASONS` entries fail there. The phase record (`phases/phase-1.md:59-70`) shows the rest were seen red by mutation. Fix that one row of the PR body to say which cases were red against the old rule and which under a mutation. Nothing in the tree needs to change.
