# 1792363189-rule-3-decides-on-the-agent-not-one-run — guarantee

| Field | Value |
|---|---|
| Target SHA | fc310e84 against 769f2aa4; earlier run: a754ab94 withheld |
| Broad gate | 5ababb7e against 769f2aa4 |

The base `release/v0.22.2` resolves through `@{upstream}` to 769f2aa4. The
orchestrator ran the broad gate, and this run only read its record.
`broad-gate.md` names 5ababb7e, which is an ancestor of HEAD. The commits
after it are a754ab94 and fc310e84, and between them they touch only
`seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/broad-gate.md`
and `guarantee.md` (`git log --no-merges --name-only 5ababb7e..HEAD
^769f2aa4`). So the run stands at HEAD. PR #982's head is fc310e84, the
same as `origin/chore/966-rule-3-decides-on-the-agent-not-one-run`.

This is the second run. The first run, at a754ab94, read `withheld` on one
row of the pull request body. The repair was an edit of that body
(`gh pr edit 982`), and the only commit since is fc310e84, which records
the first run's `guarantee.md`. No claim below rests on a coordinate that
commit touched, so none was re-run. The rows marked *earlier run* were
executed by the first run at a754ab94, in two scratch clones, both since
removed: `at-base/`, with `evals/scripts/noninferiority.py` restored from
769f2aa4, and `at-head/`. Those results hold at fc310e84 because the code,
the tests and the records they read are unchanged since then. This run
read the pull request body again whole, and the parties again.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 and S5 seen red against the code before the change | `phases/phase-1.md:65`, `:69`; PR #982 body, §*How it was verified* row 1 | earlier run, in `at-base/`: `pytest -p no:xdist -q -rA <test module>::test_the_verdict_is_recomputed_from_the_records_numbers <test module>::test_rule_3_names_the_total_and_each_grader_failing_every_new_run` | holds: both FAILED. The base wrote the old per-grader reason lines, e.g. "shape grader c1/shape-report-exists passed 1/2 on the new side, less often than the baseline's 2/2 (rule 3)" |
| The new reason lines were red against the old code | `phases/phase-1.md:67`; PR body row 1 | same run | holds: all three `RULE_3_REASONS` entries FAILED |
| The cases the old rule already agreed with pass against it | PR body row 2 | same run | holds: both renamed total cases, S3's case, S4's case and S6's case PASSED at base |
| S2 (the falling total) seen red with the total check made `if False:` | `phases/phase-1.md:66`; PR body row 2 | earlier run, in `at-head/`: a scratch driver substituted `if new_total < old_total:`, asserting exactly one match, ran the same two tests, then restored the file | holds: exit 1, 5 failed. They were the shape rename, the reach rename, S6, `[the total falls]` and the order entry |
| S3 (a grader lost on every run) seen red with the naming clause made `if False:` | `phases/phase-1.md:67`; PR body row 2 | same driver, `if op and not np_:` → `if False:` | holds: exit 1, 3 failed (S3's case, S3's reason entry and the order entry) |
| S4 (naming only that grader) seen red, alone, with the clause naming every 0/n grader | `phases/phase-1.md:68`; PR body row 2 | same driver, `if op and not np_:` → `if not np_:` | holds: exit 1, 1 failed (S4) |
| S6 (a grader the baseline lacks) seen red, with the order entry, when the totals cover graders the baseline lacks | `phases/phase-1.md:70`; PR body row 2 | same driver, `and v[2] and v[4]` → `and v[4]` | holds: exit 1, 2 failed (S6 and the order entry) |
| The narrow run: 88 passed | `phases/phase-1.md:76-77`; PR body row 4 | earlier run, in `at-head/`: `pytest -p no:xdist -q tests/test_a_rewritten_definition_proved_non_inferior.py tests/test_evals_layout.py` | holds: exit 0, 88 passed |
| The six re-read records are what `compare` writes from #957's committed sides | `phases/phase-2.md:25-27` | earlier run, in `at-head/`, six times: `noninferiority.py compare --agent <a> --phase <N> --old <#957>/evals/baseline-<a>.json --new <#957>/evals/<name>.json --out <scratch>`, then `cmp` with `evals/957-<name>.md` | holds: compare exited 0 and cmp exited 0 for all six |
| `check` on the six exits 0 for `pass` and 1 for `fail`, and none prints "it says …" | `phases/phase-2.md:59-62` | earlier run: `noninferiority.py check evals/957-<name>.md`, six times | holds: 0, 1, 0, 0, 1, 1 in S9's order, no "it says" line in any |
| `check` on #957's own `warden-phase-2.md` reports the disagreement | `plan.md:89-96`, `changelog.md:38-40`; PR body | earlier run: `noninferiority.py check <#957>/evals/warden-phase-2.md` | holds: exit 1, "it says `fail` and its numbers give `pass`" |
| Each `## Graders` section is byte-identical to #957's | `phases/phase-2.md:50-52`; PR body row 5 | earlier run: `diff` of the `## Graders` section cut by `awk`, six times | holds: all exit 0, at 53, 53, 53, 29, 37 and 22 lines |
| S9's verdicts and reasons | `spec.md:121-128`, `changelog.md:28-35`; PR body | earlier run: read the `Verdict:` blocks of `evals/957-warden-phase-2-run-1.md` and `evals/957-sealer-phase-3.md` | holds: run 1 fails on the one naming line for `warden seeded-9b644676/shape-findings`. The sealer record fails on the total line (29/30 against 30/30) and on rule 5 |
| Removes 1: the per-grader `elif` and its reason line are gone from `verdict` | `spec.md:173` | earlier run: `git grep -n -e 'np_ \* oruns < op \* nruns' -e 'less often than the baseline' -- evals/scripts tests evals/README.md`, plus the function bounds | holds: the one hit is `evals/scripts/noninferiority.py:961`, inside `cheaper_model` (941-970), out of scope by `spec.md:66-71` and unchanged from base line 938. `verdict` (578-712) has none |
| Removes 2–4: the README and both docstrings no longer state the per-grader clause | `spec.md:174-176` | earlier run: `git grep -n -i -e 'each shape and reach grader' -e '3 each shape' -- evals tests`; `git grep -n 'at least as often' -- evals tests` | holds: both exit 1, no hit |
| Removes 5: the two old case names are gone | `spec.md:177` | earlier run: `git grep -n` on both names with their closing quote, whole tree | holds: the only hit is `spec.md:177` itself. `.test_durations` is out of scope by `spec.md:79-81` |
| Rules 1, 2, 4, 5, `cheaper_model` and the suite are untouched | `changelog.md:11-13`; PR body | earlier run: `git diff -U0 769f2aa4...HEAD -- evals/scripts/noninferiority.py \| grep '^@@'`; `git diff --stat 769f2aa4...HEAD -- evals/behaviour` | holds: the hunks are at the module docstring and lines 586-667 of `verdict`, which are rule 3. Nothing under `evals/behaviour/` changed |
| Round 1's finding is fixed in #957's `spec.md` | `rounds/round-1.md:11`, `rounds/round-2.md:9-23` | earlier run: `git diff 769f2aa4...HEAD -- seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md` | holds: the rule 3 clause now points to `evals/README.md` rule 3 and says #957's phases judged per grader |
| The re-read's input stands in for `run --from-raw` | `spec.md:82-88`, `spec.md:21` | read `seal/specs/1792126889-…/guarantee.md:35-36` | holds: #957's sealer recorded the committed sides as byte-identical to what `run --from-raw` writes (executed by that sealer, read here) |
| No commit since the first run changes anything it audited | the first run's `Target SHA`, a754ab94 | `git log --no-merges --name-only --format='%h %s' a754ab94..HEAD` | holds: one commit, fc310e84, touching `guarantee.md` alone |

`unverified`: phase 1's other mutations, named in PR body row 3. They are
`common` left unsorted, `<` → `<=`, per-kind totals for S5, and each
reason text reworded (`phases/phase-1.md:69`, `:72-74`). Round 1 settled
them by reading, and this audit sampled the four above. Also unverified:
phase 2's narrow run of the changelog modules (`phases/phase-2.md:74-76`).
The broad run at 5ababb7e covers it (read, `broad-gate.md`). The
orchestrator answers both.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| The issue (#966 `## Decision`) | Rule 3 aggregates per agent. A side's total shape and reach passes against the baseline's, and a grader failing every new run where the baseline passed it is caught by name. Done when the rule is in `verdict` with its cases, and #957's records are re-read at no cost "from the kept raw output (`run --from-raw`)" | the tree (`verdict` at 660-693), the spec, the build, both rounds, the changelog, the PR body | none in substance. The re-read went through `compare` over the committed sides, because the raw output is gone. #957's guarantee shows those sides byte-identical to `run --from-raw`'s output, so "at no cost, from the kept output" holds |
| The spec | Pooled total plus naming clause. Graders the baseline lacks stay outside the totals and must pass every new run. Exact reason lines. Five Removes rows. S9's predicted verdicts | the issue, the tree, the build, the changelog | none. The S2 entry and the S8 grep diverged from it, and both are recorded in `overview.md` §*Where spec and implementation diverged*. The tree bears both out |
| The build (the diff, `phases/phase-1.md`, `phases/phase-2.md`) | Rule 3 rewritten as the spec says. S1 and S5 red against the old code, and S2–S6 red under mutations. 88 passed. Six re-reads match S9 | the issue, the spec, the tree (every sampled claim holds), the rounds, the changelog, the PR body | none |
| The last round (`rounds/round-2.md` at 4205fd6e) | Round 1's one `should` is closed at 7d2bc3d1. The sweep of the old rule's statements is complete. Nothing opens | the tree (the #957 `spec.md` diff), the build | none |
| The changelog fragment | Rule 3 now judges the agent. It quotes both reason-line forms. Rules 1, 2, 4, 5, `--runs`, the suite and `model` are unchanged. The case where one run still decides. The six-record table. The `check` disagreement on old records | the tree, the six records, the spec | none |
| The pull request body (PR #982, read again whole at fc310e84) | What changes, the before/after table, the six-record table, and the verification table. Row 1 is now the cases the old rule decides differently, plus the new reason lines, red against the old rule. Row 2 is now the cases the old rule agreed with, passing there and each red under its mutation | the issue, the tree, the build (`phases/phase-1.md:59-70`), the changelog | none. The first run's finding is repaired: rows 1 and 2 now say what the `at-base/` run and the mutation runs showed |

Verdict: sealed
