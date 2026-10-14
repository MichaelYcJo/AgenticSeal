# 1791876667-the-durations-refresh-has-a-schedule — overview

<!-- The closing memo (implement skill, step 4). Opened in phase 1 at the
first divergence, closed in phase 3. -->

📋 implement applied
· spec:     `spec.md` (Grounding, Scope, S1–S8, Data & interfaces, Removes), `plan.md` (phases 1–3, test rows), `questions.md` Q1–Q5, `CONTRIBUTING.md` §Running the checks, `docs/release-checklist.md` §0, `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* and §*A claim held by a test*, `docs/the-reader-registry.md` §*The four classes*
· evidence: `seal/ledger/1791876667-the-durations-refresh-has-a-schedule.md` — S1–S7 and C1, held by their tests; `Corrected ·` rows for 0.21.1's S1, S2 and S4 (work item 1791852613) and 0.21.0's S5 (work item 1791384162); 17 `Re-read ·` rows for the released rows the branch's edits drifted
· verified: executed — the narrow modules of each phase, every new case red through `mutation-check` (34 in phase 1, 14 in phase 2), runs 38475370013 and 38477758775 read and their unions reproduced, `evidence-check --strict` and lenient exit 0; read — the released claims re-read, #930's normalisation; unverified — the full suite (the sealer)

## Why this work exists

0.21.1 skipped the refresh its checklist box asked for; every run's Windows shards now measure the file, a job unions the parts, and the staleness case, failing in both directions, is the whole schedule.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| T2's name | `plan.md` named it `the_pytest_line_hands_the_split_then_the_store` (NAME NOT IN TREE); `spec.md` §*Data & interfaces*: "`test_the_pytest_line_hands_the_split_to_pytest` reads the store expression after the split" | the existing name, its body rewritten; `plan.md`'s test rows now carry the names the tree has | released rows in `seal/releases/0.20.0.md` (S4) and `seal/releases/0.21.0.md` (macOS S1) anchor the old name; a rename stops both resolving |
| The shallow-checkout case | the frame does not name `tests/test_ci_gives_the_checks_what_they_need.py#test_every_job_that_runs_pytest_has_the_whole_history`; it read `needs: pytest` as running pytest and failed the `durations` job | the case selects a job by a code line that calls pytest (`RUNS_PYTEST`) | spec silent; executed: old and new rules select the same three jobs and differ only on `test.yml:durations` (`phases/phase-1.md`) |
| The union's refusals | `spec.md` In 2: "A missing part, an id in two parts or a part that will not parse is exit 2" | those three, plus an empty part, a price that is not a non-negative number, a part that is not UTF-8, no parts directory, and a committed file that does not parse | spec's "never a smaller file" covers each; every one has a case seen red |
| T8's and T9's names | `plan.md` named T8 `the_sentence_names_the_download_and_the_counts` (NAME NOT IN TREE) | `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` carries T8, its body rewritten to the download; T9 keeps its name, its body rewritten to the seconds side | 0.21.1's S2 (`seal/releases/0.21.1.md`) anchors both names |
| The job-count sentence | the frame names only the recipe paragraph | `CONTRIBUTING.md`'s *CI runs five jobs* now says six and names `durations` | the `durations` job made the sentence false; #930 rewrites the same sentence, so the pull request landing second merges by hand |
| `test.yml`'s `workflow_dispatch` comment | `spec.md` In 4: "`test.yml`'s comments stay true as written" | one comment rewritten | it called the `--durations` table the only per-case figure for a pushed branch, and the `test-durations` artifact is one now |
| Two values | the frame names neither | `if-no-files-found: error` on both uploads; `timeout-minutes: 5` on the `durations` job | spec silent; the bound stops a hung download and the ordinary run is about a minute (`plan.md` §*Operational impact*); the job took 7 s and 11 s |
| No S8 row in the fragment | `spec.md` S8: "the fragment carries S1–S7" and the re-reads and corrections | S1–S7, C1, the corrections and the re-reads; S8 itself is no row | S8 is a claim about the fragment and the checker's exit, and a row grounded in this work item's own records would break when `settle` retires the directory; `evidence-check --strict` exit 0 is its evidence, in `phases/phase-3.md` |

## Not verified

| Item | Who must answer |
|---|---|
| ✅ GitHub runs the workflow as written: four `test-durations-<4…7>` parts, one `test-durations` union, the summary, and the Windows job names | run 38475370013, every job green, the five artifacts listed and downloaded 2026-10-14; the summary reproduced byte-for-byte from the parts (`phases/phase-1.md`) |
| ✅ `gh run download <id> -n test-durations` writes over a `.test_durations` already in the directory | it does not: exit 1, `file exists`, the old file kept — executed 2026-10-14 against run 38475370013 |
| The full suite, lint and typecheck at the branch's tip | the sealer, after the review rounds |
| The test rows of the fragment pass in the sealed run; without a suite record `evidence-check` reads them for existence alone | the sealer's `broad-gate`, which hands the ledger arm the sealed run's record |

## Not done

- **Whether the refresh recipe names `## Price level`.** After the rebase
  onto #930 the row reads 1073, the number `budget_check.py --baseline
  origin/release/v0.22.0` names: the median over test files of the price
  ratio on the 13,454 ids both files hold, where `phases/phase-2.md`'s
  seconds-weighted 1.0706 had predicted about 1071. `REMEDY` and the
  `CONTRIBUTING.md` recipe do not name the row; the `budgets` job names it
  on the pull request that commits a refresh, with the number to write.
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
  that calls pytest on a line of its code, not one whose text names pytest
  (C1 in the fragment).
- *Inferred during implementation:* the remedy downloads into a directory
  of its own and moves the file, because `gh run download` will not
  overwrite (S4).
