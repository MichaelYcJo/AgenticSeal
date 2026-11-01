# Design: 1793521561-a-windows-run-names-its-skipped-cases

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `skills/implement/SKILL.md` *3. The SDD file set*, the ladder's top rung (read) | The change alters text a person reads and acts on: the short summary each `pytest` leg of `.github/workflows/test.yml` prints, which the orchestrator reads with `gh run view --log` when a row defers to a leg. It is one line of a workflow, and the rung is decided by behaviour, not by size ("One file, and it qualifies"). So this work item gets `frame/design.md` and `plan.md` before the build, then the closing memo. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | It decides whether the flags stay after the reading (`plan.md` *Alternatives considered*, rows 1 and 4). They stay. Their cost is one summary line per skipped case on each leg and no seconds. On a green run of 41207847854 that is 14, 7, 14 and 0 lines on the four Windows shards, 11 on ubuntu, and 11 on macOS group 1 (executed: each job's `gh run view --job <id> --log`, the `passed` line). Their record on the first run is the three cases of #1221 and the open Windows rows of two released work items (row below). Taking them out after the reading would bring back the state #1214's settle found, where rows were deferred to legs that could not answer them. |
| `skills/code-review/orchestration.md` *Where the work's risk is platform-specific, run the other platforms before the broad run* (read) | The Windows run is a `workflow_dispatch` run of `tests` on this branch. The orchestrator starts it after phase 1 closes, and phase 2 reads it before the rounds and the broad run. The pull request's own CI run comes after the sealer and is not the run this work is read on. |
| `skills/core/SKILL.md` *The first value*, "What a script answers exactly ... stays a script" (read) | Whether a case skipped is a fact pytest prints. The summary line `SKIPPED <node id> - Skipped: <reason>` is read, and no parser of it is built. Nothing in the tree reads the legs' logs. `release-report` reads job lists only (`.github/workflows/test.yml:237-280`, read), and `durations` reads the `.test_durations` parts (`:186-205`, read). |
| Contract rule 14, *A fix that changes what a person sees documents it and pins it* (read) | The flags are documented in the comment above the pytest line. One case pins them in `tests/text/test_ci_gives_the_checks_what_they_need.py`, whose docstring says why workflow settings are pinned there: "the alternative is a comment in the workflow asking the next editor to remember" (read, `:43-44`). |
| executed: a probe at `<scratchpad>/1793521561-a-windows-run-names-its-skipped-cases/frame/`, pytest 9.2.0 with pytest-xdist 3.8.0 and pytest-split 0.11.0 through `uvx`. Three cases skip through a conftest helper's `pytest.skip`, and one fails | `-q -rs` prints `SKIPPED [3] conftest.py:3: <reason>`. The skips are folded under the helper's line, and no case is named. `-v` and `-vv` fold the same way. `-rs --no-fold-skipped` prints one `SKIPPED <node id> - Skipped: <reason>` line per case, under `-n 2` and under `--splits 2 --group 1` alike. **`-rs` alone also drops the `FAILED <node id> - <message>` line**, because `-r` replaces pytest's default `fE` rather than adding to it. `-rfEs --no-fold-skipped` prints the FAILED line and every SKIPPED line. |
| executed: `uvx --from pytest==<v> pytest --help`, then a count of `no-fold-skipped` | 0 at pytest 8.2.2 and 1 at 8.3.0. CI installs `pytest` unpinned (`.github/workflows/test.yml:149`, read), so it takes a version that has the option. A pytest without the option stops at the argument parse, so every leg goes red at once. |
| read: `tests/conftest.py#symlink_or_skip` (`:626-649`) | The helper skips at its own `pytest.skip`, so a folded summary names `tests/conftest.py:649` and not the case. Its docstring says a GitHub `windows-latest` runner holds the privilege to make links. That is the claim the reading tests. |
| read: `tests/skills/test_settle.py:702-718`, `:1136-1162` | The three cases of #1221: `Test_misplaced::test_accepts_a_file_or_a_link_to_one_at_another_path`, `Test_misplaced::test_refuses_a_directory_a_link_to_nothing_and_another_spelling`, and `Test_main::test_a_work_item_whose_rounds_cannot_be_listed_is_not_counted_as_none[link]`. |
| read: `seal/threads/1793457436-row-deletion-check-and-a-symlink/gaps.md:7` and `seal/threads/1793504229-a-linked-memo-named-as-the-argument/gaps.md:7` | Two released work items, not yet settled, each hold an open row: whether the link cases of `tests/skills/test_unverified_check.py` run or skip on the Windows legs, with "Naming a skip there is #1221's". The same reading answers them. The settle closes them, not this work. |
| read: `git show 7a8899d5:seal/threads/1793443708-settle-keeps-a-gaps-file-anywhere/gaps.md:8` and `…/1793411151-judgment-where-meaning-is-the-question/gaps.md:13`, re-homed here at the 0.27.1 settle (#1214) | Both rows named the `windows-latest` legs as the answerer. Under `-q` those legs could not answer, which is the defect this work removes. |
| read: `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_pytest_line_hands_the_split_to_pytest` | The pytest line must end with `${{ matrix.split }} ${{ matrix.store }}`, so the new flags go before `${{ matrix.split }}`. |
| executed: `grep -l` over the frame files of the four sibling work items (1793521558, 1793521559, 1793521560, 1793521562, in their worktrees) for `workflows/test.yml`, `test_ci_gives_the_checks_what_they_need` and `test_the_windows_leg_runs_in_shards` | No hit. No sibling frame names `.github/workflows/test.yml` or the two test modules. The milestone note "it edits only .github/workflows/" gives its reason as "so it goes beside the others". The pin's one test file keeps that reason. It is read at framing time, and sibling frames still being written could change it. |
| executed: `gh release view --json body` (v0.27.1) and `grep 'Process changes'` over `seal/threads/*/changelog.md` | No `### Process changes` table stands in either place, so no change to the way of working bears on this. |
| read: `seal/follow-up.md` | No row there is about the legs or skipped cases. |
| read: `routing.md` | `Planning` framer, `Implementation` crafter, `Automation` yes. Nobody is asked anything after the routing. |

## Scope

In:

1. The one pytest line of the `pytest` job in `.github/workflows/test.yml` (`:158`) passes `-rfEs --no-fold-skipped` on every leg, before `${{ matrix.split }}`. The line reads `pytest tests/ -q -n auto --durations=50 -rfEs --no-fold-skipped ${{ matrix.split }} ${{ matrix.store }}`. The comment above it (`:153-157`) gains the reason, rewritten in place. The flags make each leg name every skipped case with its reason, beside every failed case. `-r` replaces pytest's default `fE`, so the default is written out. Without `--no-fold-skipped`, skips through one helper fold under the helper's line.
2. One case in `tests/text/test_ci_gives_the_checks_what_they_need.py` reads the pytest job's `- run: pytest ` line and requires `-rfEs` and `--no-fold-skipped` on it. The module docstring gains one paragraph, *Which cases a leg names*, saying why. Where the docstring's opening count of settings counts this one, it is rewritten.
3. The reading. The orchestrator pushes the branch after phase 1 closes and runs `gh workflow run tests --ref test/1221-a-windows-run-names-its-skipped-cases`. Phase 2 reads that run's four `windows-latest` shard logs and its `test-durations` artifact. It writes into `trail/phases/phase-2.md`:
   - the run's id, its head commit, and the four job ids
   - each of the three cases of #1221, read as passed or as skipped with pytest's reason
   - every other `SKIPPED` line the four shards print
   - for the two open rows of the released work items named in *Grounding*, whether any case of `tests/skills/test_unverified_check.py` skipped

Out:

- `tests/conftest.py#symlink_or_skip` and every case under `tests/`. Whether the runner holds the privilege is what the reading measures, and nothing here changes it (`plan.md` *Alternatives considered*, row 6).
- Editing the open rows of `1793457436-row-deletion-check-and-a-symlink` and `1793504229-a-linked-memo-named-as-the-argument`. Each row belongs to its own work item, and the settle decides it with phase 2's record as its source.
- The pytest line of `.github/workflows/publish-release.yml` (`:147`). It runs on ubuntu at a release, and no row defers a platform question to it.
- Repairing any case the reading finds skipped. A skip meets the *Done when* as "read as skipped, with the reason". Where the repair goes is the orchestrator's leftover judgment (`questions.md` Q2).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given the workflow at phase 1's commit, when any `pytest` leg runs, then its short summary has one `SKIPPED <node id> - Skipped: <reason>` line per skipped case and keeps one `FAILED <node id> - <message>` line per failed case | The probe in *Grounding* (executed at framing), and phase 2's reading of the dispatched run's Windows logs |
| S2 | Given the case of Scope item 2, when `--no-fold-skipped` is deleted from the line, or `-rfEs` is written `-rs`, then the case fails | Seen red both ways before the case is committed (contract rule 15) |
| S3 | Given the dispatched run on phase 1's commit, when phase 2 reads it, then each of the three cases is recorded as passed or as skipped with pytest's reason, and the record names the run id, the head commit and the job ids it was read from | The sealer runs `gh run view --job <id> --log` again on each job id `trail/phases/phase-2.md` names |
| S4 | Given a case the run does not name as skipped, when phase 2 calls it passed, then all four Windows shards of that run concluded `success` and the case's id stands in that run's `test-durations` union | `gh run view <id> --json jobs`, and the downloaded artifact searched for the three ids |
| S5 | Given the existing readers of the pytest line, when the flags are added, then the line still ends with `${{ matrix.split }} ${{ matrix.store }}`, and `durations` and `release-report` are unchanged | `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` green, and `git diff` of the two jobs empty |

## Data & interfaces

- `.github/workflows/test.yml:158`: the pytest command line. Its output gains `SKIPPED` lines in the short summary. No file, artifact or job output changes.
- `tests/text/test_ci_gives_the_checks_what_they_need.py`: one case, reading the line through the module's own `jobs` reader.
- `seal/threads/1793521561-a-windows-run-names-its-skipped-cases/trail/phases/phase-2.md`: the reading, the record the settle and the sealer open.

## Rule changes

- nothing
  why: No document of the policy root states which report flags a CI leg passes to pytest, and none states that a leg names its skipped cases. The reason for the flags stands at the line in `.github/workflows/test.yml`, where that workflow's other settings keep theirs, and the pin's reason stands in its module's docstring.

## Removes

- nothing
  why: The work adds two flags to a step that exists and one case to a module that already pins this workflow's settings. No text in the tree stood on the legs naming no skipped case except the open rows of two released work items, which say "Naming a skip there is #1221's". The settle closes those rows with phase 2's record, in their own work items. No check, comment or copy stated the folded summary, so nothing else goes. The case is kept for what it would catch: the line was rewritten for #841, #864 and #931 (read, the comments at `.github/workflows/test.yml:70-101`). A rewrite that dropped the flags would make the legs silent again, and nothing would say so until a settle met an unanswerable row, as #1214's did.

Framed 2026-11-01 by framer, before the build.
