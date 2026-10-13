# 1791876667-the-durations-refresh-has-a-schedule — overview

<!-- The closing memo (implement skill, step 4). Opened in phase 1 at the
first divergence; phase 3 closes it. -->

## Why this work exists

0.21.1 skipped the refresh its checklist box asked for; every run's Windows shards now measure the file, a job unions the parts, and the staleness case becomes the schedule.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| T2's name | `plan.md` names it `the_pytest_line_hands_the_split_then_the_store`; `spec.md` §*Data & interfaces*: "`test_the_pytest_line_hands_the_split_to_pytest` reads the store expression after the split" | the existing name, its body rewritten | released rows in `seal/releases/0.20.0.md` (S4) and `seal/releases/0.21.0.md` (macOS S1) anchor the old name; a rename stops both resolving |
| The shallow-checkout case | the frame does not name `tests/test_ci_gives_the_checks_what_they_need.py#test_every_job_that_runs_pytest_has_the_whole_history`; it read `needs: pytest` as running pytest and failed the `durations` job | the case selects a job by a code line that calls pytest (`RUNS_PYTEST`) | spec silent; executed: old and new rules select the same three jobs and differ only on `test.yml:durations` (`phases/phase-1.md`) |
| The union's refusals | `spec.md` In 2: "A missing part, an id in two parts or a part that will not parse is exit 2" | those three, plus an empty part, a price that is not a non-negative number, a part that is not UTF-8, no parts directory, and a committed file that does not parse | spec's "never a smaller file" covers each; every one has a case seen red |
| T8's and T9's names | `plan.md` names T8 `the_sentence_names_the_download_and_the_counts`; T9 is kept by name in the plan too | `test_one_more_unpriced_fails_and_names_the_counts_and_the_recipe` carries T8, its body rewritten to the download; T9 keeps its name, its body rewritten to the seconds side | 0.21.1's S2 (`seal/releases/0.21.1.md`) anchors both names |
| The job-count sentence | the frame names only the recipe paragraph | `CONTRIBUTING.md`'s *CI runs five jobs* now says six and names `durations` | the `durations` job made the sentence false; #930 rewrites the same sentence, so the pull request landing second merges by hand |
| `test.yml`'s `workflow_dispatch` comment | `spec.md` In 4: "`test.yml`'s comments stay true as written" | one comment rewritten | it called the `--durations` table the only per-case figure for a pushed branch, and the `test-durations` artifact is one now |
| Two values | the frame names neither | `if-no-files-found: error` on both uploads; `timeout-minutes: 5` on the `durations` job | spec silent; the bound stops a hung download and the ordinary run is about a minute (`plan.md` §*Operational impact*) |

## Not verified

| Item | Who must answer |
|---|---|
| ✅ GitHub runs the workflow as written: four `test-durations-<4…7>` parts, one `test-durations` union, the summary, and the Windows job names | run 38475370013, every job green, the five artifacts listed and downloaded 2026-10-14; the summary reproduced byte-for-byte from the parts (`phases/phase-1.md`) |
| ✅ `gh run download <id> -n test-durations` writes over a `.test_durations` already in the directory | it does not: exit 1, `file exists`, the old file kept — executed 2026-10-14 against run 38475370013 |
| The full suite, lint and typecheck at the branch's tip | the sealer, after the review rounds |

## Not done

Phases 2 and 3.

## Fed back into the spec

none
