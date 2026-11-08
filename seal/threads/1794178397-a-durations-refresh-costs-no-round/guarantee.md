# Guarantee: 1794178397-a-durations-refresh-costs-no-round

The audit read the branch at `05d86bdc` against the base `release/v0.36.0`,
resolved through `release/v0.36.0@{upstream}` to `94d04d30`. Every re-run
took place in a `git clone --no-local` of the branch at `05d86bdc`. The
clone was removed once its runs were done. The tree under audit was not
changed.

`trail/gate.md` names `run: 8c5217fb against 94d04d30`. `8c5217fb` is an
ancestor of HEAD. `git log --no-merges --name-only 8c5217fb..HEAD ^94d04d30`
lists one commit, `05d86bdc`, which touches only `trail/gate.md` of this work
item (executed). `seal pr-body <item> --body <file> --check` exited 0: the
body is `pr.md` above `## From the records` and the records' own text below
it (executed).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The plan row's three modules pass at HEAD, with the deleted staleness case gone | `trail/rounds/round-2.md` *Probes*, row 3; `frame/plan.md` *Phases* row 2 | `bin/test tests/github/test_durations_union.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/text/test_ci_gives_the_checks_what_they_need.py -q -p no:xdist` at `05d86bdc` | holds: exit 0, 60 passed, 1 skipped (executed) |
| Seen red: against the old script the module fails at collection on `du.STALE_SHARE`; with `AT_THE_SHARE` set to the literal 50, the two `Test_main` cases fail with `SystemExit: 2` and the rest fail with `AttributeError` on `staleness` or `verdict` | `trail/phases/phase-1.md` *Seen red* | `git checkout 94d04d30 -- .github/scripts/durations_union.py`, then `bin/test tests/github/test_durations_union.py -q -p no:xdist`; then `AT_THE_SHARE = 50` and the same run | holds: first run exit 2, collection error `module 'durations_union' has no attribute 'STALE_SHARE'`. Second run exit 1, 10 failed and 15 passed. Two failed with `SystemExit: 2` and eight with `AttributeError` on `staleness` or `verdict`. The 10 are phase 1's 11 cases less the one round 1 deleted (`e1658160`) (executed) |
| Seen red: S4's `test_the_verdict_is_asked_into_main_alone_and_the_upload_outlives_it` fails on `assert run.endswith(" " + ASK_THE_VERDICT)`; S5's rewritten recipe case fails on "A work item never commits `.test_durations`" | `trail/phases/phase-2.md` *Seen red* | `git checkout 94d04d30 -- CONTRIBUTING.md .github/workflows/test.yml`, then `bin/test tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -p no:xdist -k "verdict_is_asked or recipe_names"` | holds: exit 1, 2 failed, each on the line the record names (executed) |
| Mutation: `>=` on the dead side fails `Test_verdict::test_accepts_exactly_the_share_on_each_side` on that side's assertion | `trail/phases/phase-1.md` *Mutation* | `stale.dead_share >= STALE_SHARE` edited into `durations_union.py`, then `bin/test tests/github/test_durations_union.py -q -p no:xdist` | holds: exit 1, that case alone failed on `assert du.verdict(du.staleness(live, gone)) is None` (executed) |
| Mutation: asking the verdict without the switch fails the two `Test_main` cases that read exit 0 over the stale fixture, which is how S2 is held | `trail/phases/phase-1.md` *Mutation*, the last bullet | `sentence = verdict(stale)` in place of the switch's condition, then the same run | holds: exit 1, `test_accepts_the_parts_and_writes_their_union_sorted_with_lf` and `test_the_summary_names_each_parts_seconds_the_spread_and_the_live_sum` failed, on exit 1 against 0 (executed) |
| Mutation: the upload's condition cut to `${{ !cancelled() }}` is red | `trail/phases/phase-2.md` *Mutation* | the edit in `test.yml`, then `bin/test tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -p no:xdist -k "verdict_is_asked or needs_pytest"` | holds: exit 1, the S4 case failed on the upload's `if:` (executed) |
| `frame/design.md` *Removes* rows 1 to 4: the suite case, `unpriced`, `dead`, `staleness`, `REMEDY`, `STALE_SHARE`, `_collection`, `_with_gone`, `FIXTURE_SIZE`, `AT_THE_SHARE` and the seven fixture cases leave the behaviour module | `frame/design.md` *Removes*; `changelog.md:3` "The suite case leaves." | `grep -nE` for each `def` and constant in the module at HEAD; `git grep -n 'prices_the_suite' -- tests` | holds: no hit (executed) |
| *Removes* row 5: `report` no longer counts unpriced and dead entries itself | `frame/design.md` *Removes* | `report`'s body at HEAD searched for `not in committed`, `not in merged`, `sum(committed` | holds: no hit; `report` reads `stale` (executed, and read in the diff) |
| *Removes* row 6: the per-branch refresh recipe | `frame/design.md` *Removes*; `changelog.md:3` "The per-branch refresh steps ... are gone" | `grep -nE 'When to commit it is\|branch.s latest\|gh run rerun\|gh workflow run\|prices_the_suite' CONTRIBUTING.md` | holds: no hit (executed) |
| *Removes* rows 7 and 8: the docstring paragraph and the conftest comment rewritten in place | `frame/design.md` *Removes* | `grep -n 'And it is held to its age'` on the module; `grep -n 'prices_the_suite\|prices the suite' tests/conftest.py` | holds: no hit (executed) |
| No statement of the old per-branch schedule stands elsewhere in the tree | `trail/phases/phase-2.md` *The census* | `git grep -n 'prices_the_suite\|STALE_SHARE' -- ':!seal/threads'`; `git grep -ln 'test_durations\|test-durations' -- ':!seal/threads' ':!.test_durations'`, each other hit read for a refresh schedule | holds: the census lists the script, its cases, `CONTRIBUTING.md:182`, `test.yml:194`, the behaviour module's `:42` and `:333`, and `.test_durations:1234`. The other files only read the file or list it (executed) |
| `.test_durations` keeps one entry for each of the eight cases phase 2 removed, and the diff removes eight `def test_` and does not touch the file | `gaps.md` *Not done* | `grep -c "::<name>\""` for each of the eight; `git diff 94d04d30...HEAD -- tests` for removed `def test_`; `git diff 94d04d30...HEAD -- .test_durations` | holds: 1 for each, 8 removed, the file unchanged (executed) |
| Each quote in `pr.md` stands at its cited source | `pr.md:1-6` | each quote, with runs of whitespace collapsed, searched in `changelog.md`, `frame/plan.md` and `gaps.md` | holds: six of six (executed) |
| The logged crossings each came from one work item that renamed or removed many cases, and that work item then committed the refresh | `changelog.md:3`, the fourth sentence; `pr.md:2` quotes it; `frame/design.md:17` G9 ("Crossings came from one work item renaming or removing many cases, not from slow growth") | `gh issue view 1444`; `gh issue view 1298 --json body,comments`; `git show d57e9ee7 -- tests` for `def test_` lines; the keys of `.test_durations` at `d57e9ee7^` and `d57e9ee7` compared, grouped by module | does not hold for the 0.29.0 crossing. The issue body quotes #1298: "a stale durations file this branch's new cases pushed past the 5% share". `d57e9ee7`, #898's merge, adds 6 `def test_` and removes none. Its refresh prices 327 keys the file lacked, spread across more than a dozen modules (`tests/skills/test_settle.py` 59, `tests/skills/test_unverified_check.py` 47, `tests/skills/test_rule_changes.py` 44, ...). Only 14 of them are #898's own `tests/skills/test_mutation_check.py`. That crossing was growth across the release, pushed past the share by a branch that added cases (executed) |

The phase records' other `executed` claims were not re-run: phase 1's 18
mutants and phase 2's mutants beyond the three above, the 45-module boundary
run, and the PyYAML parse. They are `unverified` by this audit. They stand
as the crafter's claims, and the sample above did not contradict them.

Not verified by anyone before the pull request opens, as `gaps.md` names them:
- whether GitHub evaluates `${{ github.base_ref == 'main' && '--stale-fails' || '' }}` and `hashFiles('union/.test_durations')` as phase 2 reads them: `unverified`, answered by this branch's pull request run and by 0.36.0's release pull request, both read by the orchestrator;
- whether the verdict reads a real four-part union and prints in a real step summary: `unverified`, answered by the `durations` job on 0.36.0's release pull request, read by the orchestrator of that release.

The broad gate is the orchestrator's (`trail/gate.md`), and this audit ran
none of it.

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | The staleness verdict leaves the suite and is asked by `durations_union.py --stale-fails` on a pull request into `main` alone. The upload outlives a red verdict. A release refresh lands by a no-work-item pull request into `release/vX.Y.Z`. *Removes* names eight rows. | the issue's *Done when* and its first *To weigh* item; the diff; both phase records; the rounds | the issue body and `d57e9ee7`, on G9's "Crossings came from one work item renaming or removing many cases, not from slow growth" (`frame/design.md:17`). `frame/plan.md:29`, row F's "only renames crossed", stands on the same reading |
| the build | Phase 1 built `Staleness`, `staleness`, `verdict`, `REMEDY`, `STALE_SHARE` and the exit code 1. Phase 2 wired the switch and the upload's condition, removed the suite case and its helpers, and rewrote the recipe, the docstring and the conftest comment. | the diff; the seen-red and mutation claims sampled above; every *Removes* row; `frame/plan.md`'s Status cells `ef5f8167` and `608f2df7`, each with its `trail/phases/phase-N.md` | none found |
| the last round | Round 2, at `fc0b4b28`: round 1's three findings, all fixed in `e1658160`, hold, and it opens nothing. | the tree at HEAD: `REMEDY`'s code span, `gaps.md`'s eight entries, `Test_staleness`'s two cases | none found. Round 1 carried G9 from the frame without deriving it again, as its preamble says |
| the changelog | A stale `.test_durations` fails only the release pull request, and no work item commits it. The logged crossings each came from one work item that renamed or removed many cases. | the diff, on every mechanism it names: the switch, the exit codes, the upload, `CONTRIBUTING.md`'s paragraph | the issue body and `d57e9ee7`, on its fourth sentence (`changelog.md:3`) |
| the orchestrator's part of the pull request body | `pr.md` quotes four sentences of `changelog.md`, the prefix judgment and one `gaps.md` row, and closes #1444. | each quote stands at its source; the body check exits 0 | the issue body and `d57e9ee7`, through its second quote (`pr.md:2`), the changelog's fourth sentence |

```seal
target: 05d86bdc against 94d04d30
Verdict: withheld reason: the changelog fragment's sentence "The logged crossings each came from one work item that renamed or removed many cases, and that work item then committed a refresh after its build" (`changelog.md:3`, committed in `c3b7b37d`, quoted by the orchestrator at `pr.md:2`) is contradicted by the issue body's 0.29.0 entry ("a stale durations file this branch's new cases pushed past the 5% share") and by `d57e9ee7`, whose refresh prices 327 new keys across more than a dozen modules, only 14 of them #898's own six added cases; rewrite that sentence and `pr.md:2` to what the logs hold, judge whether `frame/design.md:17` G9 and `frame/plan.md:29` row F, which state the same reading, are folded, and regenerate the body
```
