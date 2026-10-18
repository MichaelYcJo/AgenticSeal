# 1791876667-the-durations-refresh-has-a-schedule — overview

<!-- The closing memo (implement skill, step 4). Opened in phase 1 at the
first divergence, closed in phase 4, the reframe after round 4. -->

📋 implement applied
· spec:     `spec.md` (Grounding, Scope, S1–S9, Data & interfaces, Removes), `plan.md` (phases 1–4, test rows), `questions.md` Q1–Q5, `CONTRIBUTING.md` §Running the checks, `docs/release-checklist.md` §0, `docs/the-reader-registry.md` §*The four classes*
· evidence: the cases T1–T11 of `plan.md`'s test rows and `test_a_job_that_calls_pytest_any_way_is_held_to_the_whole_history`, each seen red through `mutation-check` (34 breaks in phase 1, 14 in phase 2); in phase 4, T8's whole-command assertion red against 9021bc49's `REMEDY`, and `expected_level` broken once, 10 of 159 cases red (`phases/phase-4.md`)
· verified: executed — the narrow modules of each phase, runs 38475370013 and 38477758775 read and their unions reproduced, the restate command as `REMEDY` gives it (phase 4); read — #930's normalisation; unverified — the full suite (the sealer)

## Why this work exists

0.21.1 skipped the refresh its checklist box asked for; every run's Windows shards now measure the file, a job unions the parts, and the staleness case, failing in both directions, is the whole schedule.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| T2's name | `plan.md` named it `the_pytest_line_hands_the_split_then_the_store` (NAME NOT IN TREE); `spec.md` §*Data & interfaces*: "`test_the_pytest_line_hands_the_split_to_pytest` reads the store expression after the split" | the existing name, its body rewritten; `plan.md`'s test rows now carry the names the tree has | released rows in `seal/releases/0.20.0.md` (S4) and `seal/releases/0.21.0.md` (macOS S1) anchor the old name; a rename stops both resolving |
| The shallow-checkout case | the frame does not name `tests/test_ci_gives_the_checks_what_they_need.py#test_every_job_that_runs_pytest_has_the_whole_history`; it read `needs: pytest` as running pytest and failed the `durations` job | the case selects a job by a code line that calls pytest (`RUNS_PYTEST`) | spec silent; executed: old and new rules select the same three jobs and differ only on `test.yml:durations` (`phases/phase-1.md`), and after the rebase onto #930 on `test.yml:budgets` too, whose `fetch-depth: 0` the old rule alone had asked for and which is gone |
| The union's refusals | `spec.md` In 2: "A missing part, an id in two parts or a part that will not parse is exit 2" | those three, plus an empty part, a price that is not a non-negative number, a part that is not UTF-8, no parts directory, and a committed file that does not parse | spec's "never a smaller file" covers each; every one has a case seen red |
| T8's and T9's names | `plan.md` named T8 `the_sentence_names_the_download_and_the_counts` (NAME NOT IN TREE) | `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` carries T8, its body rewritten to the download; T9 keeps its name, its body rewritten to the seconds side | 0.21.1's S2 (`seal/releases/0.21.1.md`) anchors both names |
| The job-count sentence | the frame names only the recipe paragraph | `CONTRIBUTING.md`'s *CI runs five jobs* now says six and names `durations` and `budgets` | the `durations` job made the sentence false; #930's `budgets` job had made it six and #944's removal of the `ledger` job five again, and the sentence counts what `test.yml` and the hygiene workflow run on the tree this branch stands on |
| `test.yml`'s `workflow_dispatch` comment | `spec.md` In 4: "`test.yml`'s comments stay true as written" | one comment rewritten | it called the `--durations` table the only per-case figure for a pushed branch, and the `test-durations` artifact is one now |
| Two values | the frame names neither | `if-no-files-found: error` on both uploads; `timeout-minutes: 5` on the `durations` job | spec silent; the bound stops a hung download and the ordinary run is about a minute (`plan.md` §*Operational impact*); the job took 7 s and 11 s |
| The committed `.test_durations` | `spec.md` In 5 and S5: phase 1 commits the first union | the release branch's file, which #944 took from run 38646055747's unsharded Windows leg with `--clean-durations` (its `overview.md`); the union commit fell out of the rebase onto #944, and `plan.md`'s phase 1 Status names the phase's last commit that remains | #944's file is newer than the union of run 38475370013 and prices the tree as it is, with the cases #944 deleted already gone; the union was the experiment S5 asked for, and its before and after stand in `phases/phase-1.md` and `phases/phase-2.md`. The next refresh the staleness case asks for commits a union |
| Part retention | `spec.md` Data & interfaces, as framed: "Parts retained 1 day, the union 7" | parts and union both `retention-days: 7`, uploaded with `overwrite: true`; `spec.md` rewritten to it | round 1's 🟡 1: re-running failed jobs re-runs the `durations` job, which reads every part again, so a part is kept as long as the union it makes |
| The ledger records | `spec.md` In 6 and S8, as framed: a ledger fragment, `Re-read ·` and `Corrected ·` rows, `survivors.md`, `evidence-check --strict` exit 0 | removed when the branch was rebased onto #944, which took the ledger, `evidence-check` and `survivor-check` out of the plugin; `spec.md` and `plan.md` phase 3 rewritten to the records that remain | nothing reads a ledger fragment or a `survivors.md` on the release branch; `phases/phase-3.md` keeps what the ledger work found as the history of that phase |
| The `slow-file` rows | `spec.md` Out, as framed: "this item decides when that is, and changes nothing in #930's mechanism" | the `slow-file` family is a `report` row in `seal/budgets.md`; `suite-seconds` stays a gate | round 3's 🟡 2, executed: four unions of one tree moved single test files 0.67 to 1.72 times the level, and every union refresh measured put one past the 1.3 band; `slow_file_values` reads only `.test_durations`, so a gate there could fire only on the refresh pull request, which never causes the growth |
| The price level a refresh commits | `spec.md` In 3, as framed: the remedy is "download …, make its line ends LF, commit it" | the remedy and the `CONTRIBUTING.md` recipe also run `budget_check.py --baseline origin/<base> --restate-price`, a flag added to #930's checker, and commit `seal/budgets.md` with the file | round 3's 🟡 1, executed: the tip's union over the tree failed the hygiene workflow's budget step until `## Price level` was restated, and the number to write was printed only in that failure; the flag writes the number `price_problems` computes, so the level has one source and no person copies it |

## Not verified

| Item | Who must answer |
|---|---|
| closed GitHub runs the workflow as written: four `test-durations-<4…7>` parts, one `test-durations` union, the summary, and the Windows job names | run 38475370013, every job green, the five artifacts listed and downloaded 2026-10-14; the summary reproduced byte-for-byte from the parts (`phases/phase-1.md`) |
| closed `gh run download <id> -n test-durations` writes over a `.test_durations` already in the directory | it does not: exit 1, `file exists`, the old file kept — executed 2026-10-14 against run 38475370013 |
| The full suite, lint and typecheck at the branch's tip | the sealer, after the review rounds |
| closed The test rows of the fragment pass in the sealed run; without a suite record `evidence-check` reads them for existence alone | moot: the fragment and `evidence-check` left with #944, and the branch was rebased onto 5b1f6fae; the cases themselves are the full suite's row above |

## Not done

- **Q3's prices.** The job times are measured (7 s and 11 s for `durations`);
  the per-minute price page was not opened.
- **#914.** Its `workflow_dispatch` measuring input has nothing left to run;
  whether it closes with this pull request is the owner's call at the
  merge.
- **The macOS spread** read 1.41 slowest over mean on run 38477758775,
  against 1.05–1.34 on the old file, inside the 15-minute `timeout`. The
  macOS division is out of this item's scope; #929, whose cuts move the
  macOS groups, reads it next.

## Fed back into the spec

- *Inferred during implementation:* a union also refuses an empty part, a
  price that is not a non-negative number, a part that is not UTF-8, no
  parts directory, and a committed file that does not parse (S2).
- *Inferred during implementation:* the shallow-checkout case holds a job
  that calls pytest on a line of its code, not one whose text names pytest.
- *Inferred during implementation:* the remedy downloads into a directory
  of its own and moves the file, because `gh run download` will not
  overwrite (S4).
