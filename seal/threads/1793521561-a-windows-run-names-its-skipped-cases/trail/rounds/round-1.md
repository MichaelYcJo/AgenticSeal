# Review round 1: 1793521561-a-windows-run-names-its-skipped-cases

```seal
target: bbb6dc69dbc63a55fc74822fd9977cf0199bcd2b against release/v0.27.2
```

The branch was read against its base `813665f0`, which is also the merge base. Everything this round ran, it ran in a `git clone --no-local` of the branch worktree at the target. No earlier round exists, so no fact was carried from one, and every coordinate below was opened in this round. The axes fixed before starting were the table's rows that bear on a workflow line and a text case (inputs, exclusions and boundaries, error paths, response shape), and three of this change's own: the pytest version the flags need, the other pytest lines of the workflows (the class of legs that name no skip), and whether the records' sentences match the run they cite. No `seal/parity.md` is declared, so no legacy comparison applies and the round block carries no `original:` line.

## Findings

### 1. The changelog fragment says more than the change and the run show

```seal
severity: should
location: `seal/threads/1793521561-a-windows-run-names-its-skipped-cases/changelog.md:3`
evidence: executed `gh run view -R MichaelYcJo/AgenticSeal --job 124799569313 --log`, `gh run view -R MichaelYcJo/AgenticSeal --job 124799569266 --log`
```

Why it matters: the fragment becomes the release note, which a person reads as what the release does. Two of its sentences are wrong.

The first is the bold opening sentence: "Each leg of this repository's test workflow names every case it skipped". Only the `pytest` job's line changed (`.github/workflows/test.yml:166`). The `arms-grammar` job of the same workflow has two legs, and its line is still `pytest tests/skills/test_arm_check.py -q` (`.github/workflows/test.yml:243`). Phase 1 leaves that line alone on grounds the frame's *Scope* item 1 supports. But the sentence still covers it. Run 41290162769 shows the gap. The `arms-grammar (3.13)` leg (job 124799569313) ends `97 passed, 2 skipped in 11.42s` and prints no `SKIPPED` line, so its log names neither skipped case. The `(3.14)` leg ends `99 passed`.

The second is the last sentence: "the three link cases it names passed on every Windows shard". Each case runs in one shard only. The comment at `.github/workflows/test.yml:72-73` says each shard "runs its own disjoint part". Phase 2 also says no more than that each case passed on the Windows leg: no log line names a case that passed, so it cannot say which shard ran each one.

The module docstring and the case say "each `pytest` leg" (`tests/text/test_ci_gives_the_checks_what_they_need.py:42`, `:647`), meaning the legs of the `pytest` job, as `test_every_pytest_leg_has_a_timeout_and_the_job_reads_it` (`:626`) does. The fragment should use the same limit.

```markdown
- **Each leg of the `pytest` job in this repository's test workflow names every case it skipped, with pytest's reason, and still names every case that failed (#1221).** The `pytest` job of `.github/workflows/test.yml` ran with `-q` alone, which prints a count of skipped cases and no case. The cases one helper skips were folded under the helper's line, so a Windows shard's log could not say whether the link cases of `tests/conftest.py#symlink_or_skip` ran there. Rows that deferred that question to the Windows legs therefore stayed open. The line now passes `-rfEs --no-fold-skipped`, so the short summary carries one `SKIPPED <node id> - Skipped: <reason>` line per skipped case. `-r` replaces pytest's default `fE`, so the default is written out, and each `FAILED <node id>` line stays. A case in `tests/text/test_ci_gives_the_checks_what_they_need.py` pins both flags. The option needs pytest 8.3.0 or later, and CI installs pytest unpinned. The first run with the flags answered #1221: the three link cases it names passed on the Windows leg, and no case of `tests/skills/test_unverified_check.py` skipped there.
```

```seal
verdict: fixed 74c3bb00
answer: The finding holds. `.github/workflows/test.yml:243` runs `pytest tests/skills/test_arm_check.py -q` with no flag, and the comment at `:72-73` gives each Windows shard a disjoint part, so the fragment overstated both scopes. The paste-ready text was applied as given, and `changelog.md:3` now matches it line for line. `git grep` over the work item's records for "every Windows shard", "each leg" and "every leg" found one more sentence of the same kind outside the fragment: `trail/phases/phase-2.md:5` says "Every leg that skipped a case printed one" `SKIPPED` line, which the `arms-grammar (3.13)` leg does not meet. A fix pass writes no phase record, so it stands, and the hand-back names it.
```

### 2. The closing memo still says the orchestrator will choose a home for the three skipped link cases, after the orchestrator chose #1247

```seal
severity: should
location: `seal/threads/1793521561-a-windows-run-names-its-skipped-cases/gaps.md:15`
evidence: read `seal/threads/1793521561-a-windows-run-names-its-skipped-cases/gaps.md:15`, `seal/threads/1793521561-a-windows-run-names-its-skipped-cases/frame/plan.md:44`, `seal/threads/1793521561-a-windows-run-names-its-skipped-cases/frame/questions.md:15`
```

Why it matters: `gaps.md` *Not done* is where a leftover is handed over. `skills/implement/SKILL.md` says each leftover is named in the pull request body "because a leftover nobody can find was not handed over". At `gaps.md:15` the memo still says "The orchestrator judges their home, and `trail/phases/phase-2.md` holds an issue draft", which reads as a judgment not yet made. That judgment was made at `bbb6dc69`. `frame/plan.md:44` and the Q2 answer at `frame/questions.md:15` home the three cases of `tests/skills/test_agentic_pytest_record.py` in #1247. `gh issue view 1247` shows it open, in milestone `backlog: release & platform`, with phase 2's draft as its body (executed). The commit that made the judgment changed `plan.md` and `questions.md` and did not touch `gaps.md`. So the memo the sealer and the settle read disagrees with the plan they also read, and a settle that reads the memo alone finds a leftover with no home. Contract rule 19 asks for the sentence to be rewritten in the same change.

```markdown
The three link cases of `tests/skills/test_agentic_pytest_record.py` that skip on the Windows legs through `skipif(os.name == "nt")` are not moved onto `tests/conftest.py#symlink_or_skip`. Run 41290162769 shows the runner can make links, so they go unproved there for a reason that does not hold. `frame/design.md` *Scope*, *Out* keeps every case under `tests/` out of this work. The orchestrator filed them as #1247 in `backlog: release & platform` (`frame/plan.md` *Judgments of the run*), from the draft in `trail/phases/phase-2.md`.
```

```seal
verdict: fixed e7726f5d
answer: The finding holds. `frame/plan.md` *Judgments of the run* and the Q2 Status at `frame/questions.md:15` home the three cases in #1247, and `gh issue view 1247` shows it open in milestone `backlog: release & platform` with phase 2's draft as its body (executed). The paste-ready text was applied as given, and `gaps.md:15` now matches it. The same commit limits two other sentences of the memo to the `pytest` job's legs, the class finding 1 names: the closed S1 row's answer at `gaps.md:7` ("every leg of the `pytest` job installed", "each of those legs that skipped") and the open `FAILED` row at `gaps.md:8` ("every leg of that run's `pytest` job installed"). Neither row's Item cell or open or closed state changed.
```

## Confirmations

```seal
confirms: none
```
What matched: frame *Scope* item 1 and scenario S5. `.github/workflows/test.yml:166` reads `pytest tests/ -q -n auto --durations=50 -rfEs --no-fold-skipped ${{ matrix.split }} ${{ matrix.store }}`. The flags stand before the split, so the line still ends as `test_the_pytest_line_hands_the_split_to_pytest` requires. The reason is written into the comment above the line (`:155-162`) and not in a second place (read). `git diff release/v0.27.2...HEAD -- .github` changes only that step's comment and line, so the `durations` and `release-report` jobs are as they were (executed). No script under `.github/`, `bin/`, `skills/` or `hooks/` reads a leg's log: a `git grep` for `--log`, `passed in` and `short test summary` lists none (executed). The design's claim that nothing parses the summary holds.

```seal
confirms: none
```
What matched: the flags do what the comment says they do. The pytest in the clone's environment is 9.2.0, and its `_pytest/terminal.py:79` sets `_REPORTCHARS_DEFAULT = "fE"` as the default of `-r` (`:201`), so `-r` replaces it rather than adding to it (read). `uvx --from pytest==8.2.2 pytest --help` lists no `--no-fold-skipped`, and 8.3.0 lists it once (executed). That re-derives the framer's version probe and the comment's "8.3.0 or later". Every leg of run 41290162769 installed 9.2.0 (executed, the install line of each of the eight `pytest` job logs).

```seal
confirms: none
```
What matched: frame *Scope* item 2 and S2. The case `test_every_pytest_leg_names_each_case_it_skipped_and_each_it_failed` (`tests/text/test_ci_gives_the_checks_what_they_need.py:647-665`) reads the `pytest` job through the module's `read` and `jobs`. `read` strips comment lines (`:79-97`), so the comment above the line, which also holds both flags, cannot satisfy it. The case requires exactly one `- run: pytest ` line and requires each flag as a whole word of it. Phase 1 claims the case was seen red with `--no-fold-skipped` deleted and with `-rfEs` written `-rs`. Reading confirms both edits make the `missing` list non-empty, so no probe was run for it (read). The docstring now counts four settings and says "all but the third failed silently" (`:1-5`). Of the four paragraphs, only cancelling (`:28`) did not fail silently, so the count is right (read). Read against its group: the other cases on the `pytest` job's line check its timeout (`:626`), its history depth (`:527`) and its end (the shard module). None of them checks report flags. `bin/seal layout --pairs` names no pair for either module, so the case duplicates nothing (executed).

```seal
confirms: none
```
What matched: phase 2's reading of run 41290162769, taken as a claim and re-read from the run. `gh run view 41290162769 --json headSha,conclusion,event,headBranch,status,jobs` gives `workflow_dispatch`, this branch, head `585234f6bdcec52cc28024c1543d904eeca302be`, `completed` and `success`. The four Windows job ids are the ones phase 2 names, and each concluded `success`. Across the four Windows logs: the `SKIPPED` lines count 14, 7, 14 and 0, which matches each shard's last line (`3082 passed, 14 skipped`, `594 passed, 7 skipped`, `1217 passed, 14 skipped`, `1321 passed`). No `SKIPPED` line lacks a `::` node id, no `FAILED` or `ERROR` line stands, and none of the `SKIPPED` lines names `test_settle.py::Test_misplaced`, `test_a_work_item_whose_rounds_cannot_be_listed` or `test_unverified_check`. Three lines carry a link reason, the three cases of `tests/skills/test_agentic_pytest_record.py`. The `test-durations` artifact holds 6,249 ids, which is the four shards' passed and skipped counts added together. It holds the three cases of #1221 at 0.0123 s, 0.0178 s and 0.9440 s, 390 ids of `tests/skills/test_unverified_check.py`, and the three skipped link cases at under 0.0003 s. The ubuntu and macOS figures phase 2 gives (11, 11, 0 and 0) also match (all executed: each job's `gh run view --job <id> --log`, `gh run download 41290162769 -n test-durations` and a `python3 -I` read of the file). So the Q1 answer at `frame/questions.md:14` is right. The Q2 answer at `:15` is right that no row is owed for Q1's cases, because none of them skipped.

```seal
confirms: none
```
What matched: the `gaps.md` labels are honest, and `seal unverified` reads the memo as two open rows and one closed (executed). The closed row answers the `SKIPPED` half of S1 and the option from the run. The open `FAILED` row is right that no case failed on any leg, so the run cannot answer it (executed, the `FAILED` count above). Its answerer, the first red `pytest` leg, will exist, because every pull request runs those legs. The suite row names the orchestrator through `seal gate`, which matches the spawn's label `unverified`. The modules that read the changed workflow (`git grep -l 'test\.yml' -- tests`, seven) passed in one narrow run, `227 passed, 2 skipped` (executed). The two skips are the shard module's whole-suite cases, which only the broad gate collects.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, and the repository-wide `ruff check` and `ruff format --check`, at the target | the whole tree | the orchestrator, through `seal gate` after the rounds |
| Whether a red `pytest` leg on a runner keeps its `FAILED <node id>` lines under `-rfEs`. The pytest source and the framer's local probe say it does, and no runner has shown it | `.github/workflows/test.yml:166`, `gaps.md:8` | a measurement: the first `pytest` leg that goes red, as the open `gaps.md` row names |
| Phase 1's mutation runs and its seventeen-module boundary run, beyond the seven workflow-reading modules this round ran | `trail/phases/phase-1.md:17-25` | read as claims and not re-run. The case's red-ness was settled by reading. The sealer samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_ci_gives_the_checks_what_they_need.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py -q -rfEs --no-fold-skipped` | exit 0, `41 passed, 2 skipped`. The two skips are the shard module's whole-suite cases |
| `bin/test` over the seven modules `git grep -l 'test\.yml' -- tests` lists, `-q -rfEs --no-fold-skipped` | exit 0, `227 passed, 2 skipped` |
| `bin/seal layout --pairs` | exit 0. No pair names either test module |
| `bin/seal unverified --baseline 813665f0` on the work item's `gaps.md` | exit 0, `2 open · 1 closed · 0 unreadable` |
| `uvx --from pytest==8.2.2 pytest --help` and the same at 8.3.0, each counted for `no-fold-skipped` | 0 at 8.2.2, 1 at 8.3.0 |
| `gh run view 41290162769 --json headSha,conclusion,event,headBranch,status,jobs` | head `585234f6`, `workflow_dispatch`, `success`. Every `pytest` and `arms-grammar` job concluded `success` |
| `gh run view --job <id> --log` for the eight `pytest` jobs and the two `arms-grammar` jobs | `SKIPPED` lines 14, 7, 14, 0 (Windows), 11 (ubuntu), 11, 0, 0 (macOS) and 0, 0 (`arms-grammar`), with `arms-grammar (3.13)` ending `97 passed, 2 skipped`. No `FAILED` or `ERROR` line in any log |
| `gh run download 41290162769 -n test-durations`, then a `python3 -I` read of `.test_durations` | 6,249 ids. The three cases of #1221 are present, `test_unverified_check.py` holds 390 ids, and the three skipped link cases are present at under 0.0003 s |
| `gh issue view 1247` | open, milestone `backlog: release & platform`, with phase 2's draft as its body |

Each run's leavings were in the round's scratch directory: the clone, its `.venv`, the downloaded logs and the artifact. They were removed before the hand-back.
