# Implementation Plan: 1793521561-a-windows-run-names-its-skipped-cases

## Technical context

- `.github/workflows/test.yml:158` is the one pytest line of the `pytest` job. Every leg runs it: ubuntu whole, macOS in three shards, Windows in four (`:69-108`). `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_pytest_line_hands_the_split_to_pytest` holds its end to `${{ matrix.split }} ${{ matrix.store }}`.
- `tests/text/test_ci_gives_the_checks_what_they_need.py#jobs` is the module's reader of a workflow's jobs. The new case reads the `pytest` job through it, the way the shard module does.
- Nothing parses a leg's log. `release-report` reads job lists, and `durations` reads the uploaded `.test_durations` parts (`frame/design.md` *Grounding*).
- `skills/code-review/orchestration.md` *Where the work's risk is platform-specific* gives the dispatched run: push once the build's last code phase closes, then `gh workflow run tests --ref <branch>`, and read that run before the broad run.

Failure scenario of the chosen approach, six months on: a pytest release renames or removes `--no-fold-skipped`. Every leg then stops at the argument parse and goes red on the same pull request. The failure is loud, and it names the option. A quieter failure: the skips grow to hundreds of lines, and a reader skims past the one that matters. The probe's count on run 41207847854 was 35 across the four Windows shards. A list that long is still read by `grep SKIPPED`.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. `-rfEs --no-fold-skipped` on the one pytest line, for every leg, kept after the reading | Covered under *Technical context* | Chosen. One line names every skipped case on every leg. Each leg pays one summary line per skip and no seconds. |
| 2. `-rs` on the Windows legs, as the issue offers ("for one") | The probe shows two failures (`frame/design.md` *Grounding*, the probe row). `-rs` replaces pytest's default `fE`, so a red Windows shard loses its `FAILED <node id>` lines from the short summary. And skips through `symlink_or_skip` fold under `tests/conftest.py:649`, so the three cases are still not named. | Rejected: it would not meet *Done when*, and it would take away a line a person reads today. |
| 3. The same flags on the Windows entries alone, through a matrix key such as `report:` on the four entries | Four entries carry a fifth key. The matrix readers in `tests/text/test_ci_gives_the_checks_what_they_need.py` and the shard module are asked about a key they did not know. A case that skips on macOS or ubuntu stays unnamed. Nothing is saved, because no reader of the other legs' logs exists to be disturbed. | Rejected. |
| 4. Add the flags for this one run and take them out after the reading | The next work item that adds a platform-skipping case defers its Windows row to the legs again. Four work items did: `1793443708-settle-keeps-a-gaps-file-anywhere` and `1793411151-judgment-where-meaning-is-the-question`, whose rows #1214 re-homed here, and `1793457436-row-deletion-check-and-a-symlink` and `1793504229-a-linked-memo-named-as-the-argument`, whose rows are open. Their round records carried the row from round to round. The settle then finds the legs cannot answer, as #1214's did, and files the question again. Under `skills/core/SKILL.md` *The rule a mechanism is kept against*, the flags' record outweighs their cost. On the first run they answer the three cases and two open rows. They cost about one log line per skip and nothing else. | Rejected. The premise that keeps them is that rows keep naming the legs as answerer. It was checked: `git grep -n 1221` lists the open rows of the last two work items, their questions and their round lines (executed), and `frame/design.md` *Grounding* reads the re-homed rows of the first two at `7a8899d5`. |
| 5. Replace the structure: `--junitxml` per shard, uploaded as an artifact | It adds a step per leg, an artifact retention and an XML reader for whoever asks. A row's answerer then has to download and parse a file, where a `grep` of the log answers the same question. | Rejected: more mechanism for the same fact. |
| 6. Replace the structure: `symlink_or_skip` fails instead of skipping where the workflow sets a variable, so the exit code answers | It covers the link helper alone. `fifo_or_skip` and every `skipif` stay unnamed. `tests/conftest.py` strips every `GITHUB_` variable at import, so it needs a new variable and a branch in a helper every link case calls. A runner image that drops the privilege turns every pull request red for code nobody touched, which is the outcome the helper's docstring argues against. It is a new gate with its own argument to make, and no record yet shows a Windows link skip it would have caught. | Rejected now. The reading is the record such a gate would be argued from. Where phase 2 finds a link case skipped, the orchestrator's leftover issue weighs this row (`questions.md` Q2). |
| 7. No pin, only the comment at the line | The line was rewritten for #841, #864 and #931. A rewrite that drops the flags makes the legs silent again. Nothing says so until a settle meets a row the legs cannot answer. | Rejected under contract rule 14, and under the module docstring's own reason for pinning workflow settings. |
| 8. The orchestrator reads the run and writes the result as a row of `## Judgments of the run` | That section holds judgments, with grounds and a document judged against, and `seal settle`'s dry run reads it as such. A reading of a log is a fact, not a judgment. The orchestrator would also be the only witness of a run it started itself. | Rejected. Phase 2 is a crafter's reading, recorded in a phase record that the rounds and the sealer read as a claim. |
| 9. Read the pull request's own CI run instead of a dispatched one | That run starts when the pull request opens, which is after the sealer. The guarantee could not cover the reading, and *Done when* would be met after the seal. | Rejected. The dispatched run is on the same tree, because phase 2 commits records alone. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 and 2 | The new case seen red twice before it is committed: with `--no-fold-skipped` deleted from the line, and with `-rfEs` written `-rs`. Then, in one command, `bin/test tests/text/test_ci_gives_the_checks_what_they_need.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/skills/test_arm_check.py tests/skills/test_deferral_check.py -q`, with every other module `git grep -l 'test\.yml' -- tests` lists that reads the `pytest` job's line, per contract rule 2 | 0773118a |
| 2 | `frame/design.md` *Scope* item 3, from the run the orchestrator dispatches on phase 1's commit and names in the spawn | For each of the four `windows-latest` jobs: `gh run view --job <id> --log`, its `SKIPPED` lines, and `gh run view <run> --json jobs,headSha` for each job's conclusion and the head commit. `gh run download <run> -n test-durations` searched for the three ids. Scenarios S3 and S4 | |

## Operational impact

None to deploy. Each `pytest` leg's log gains one short-summary line per skipped case. No step, job, artifact or dependency is added. CI installs `pytest` unpinned, and the option needs pytest 8.3.0 or later (executed, `frame/design.md` *Grounding*).

The orchestrator's acts between the phases: push the branch after phase 1 closes, run `gh workflow run tests --ref test/1221-a-windows-run-names-its-skipped-cases`, wait for that run, and hand its run id to phase 2's spawn.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
