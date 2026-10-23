# Handoff: 1792628098-tests-rebuilt-one-file-per-module (#942)

Written 2026-10-22 by the orchestrator, when the owner paused the build after phase 5's first proof under the new rule, and brought up to date on 2026-10-23 by the smith spawns that rebuilt the modules since. The branch is `chore/942-tests-rebuilt-one-file-per-module`, cut from `release/v0.22.3` at 6046f062. The tree this file describes is 4e987021 and the commits that update this file.

## Where the build stands

| Phase | State |
|---|---|
| 1 to 4 | built: `bin/test-layout`, the slow-case report, the censuses in `tests/censuses.py`, the helper twins in `tests/conftest.py` |
| 5 | closed at b770ca64: 11 modules rebuilt, plus the `mutation-check` batch mode |
| 6 | closed at 52ce0e03: the move check at 6e7214be, its two sets at 43324e4e; Batch B's `hooks/` groups 1 to 26, from 0a86c1b4 to da3eae09, 28 modules placed, `hooks/config.py` in groups 21 to 23 and `hooks/cmdline.py` last in groups 24 to 26, the creation flow in `tests/e2e/creation/`, the worktree guard's light files in its one file, the commit gate's guarantee arm in `tests/test_commitgate.py`, and every commit gate case the work moves in its file. The framer's survey at 0b134a29 gave every `check:` line the remaining groups meet a verdict in `spec.md`; the installer's line, for `hooks/githooks.py` and `hooks/hook-install.py`, waits on `questions.md` Q10, whose default is wait. `hooks/cmdline_base.py` and `hooks/git/` have nothing to move. `skills/verify/scripts/`'s groups 27 to 35, from ffb0bd4b to 2272cd1e, placed seven modules and the light files of `broad_gate.py` and `unverified_check.py`; `seal_stamp.py` and `pact_check.py` had none to move. Group 36, at 19c01e3b, placed `skills/code-review/scripts/chain_check.py`'s light files. Group 37, at 809408e5, placed `skills/settle/scripts/`'s three modules, and group 38, at 4f350b0f, `seal.py`'s last light cases. Groups 39 to 49, from 46e1ec4c to a4a113f6, placed `.github/scripts/`'s fourteen modules, and group 50, at 52ce0e03, `evals/scripts/`'s three generators. Over the 50 groups 1,055 mutants ran, 136 survived and 125 of them are old gaps (`phases/phase-6.md` *The phase's close*) |
| 7 | closed at 3c6b9e0d: the move check drops nested docstrings at cc391101 (S14), and group 44's check passes; S10 stays open under `questions.md` Q9's default, with the 115 undeclared files and their reasons in `overview.md` *Not done*; the cases of `tests/conftest.py`'s workflow readers and `gh` block moved to `tests/test_conftest.py` at 099cd54d by the move check as it stood at its commit; `.test_durations` refreshed from CI run 39964746967 at 3c6b9e0d. Locally the suite ran in 183.9 s at the base and 91.4 s at 6a54be98 (`phases/phase-7.md`) |
| Review | round 1 covered phases 1 to 4 at 8aa42bf8; its nine findings are answered, eight fixed at c6d2bfc4 and one deferred to phase 7. Round 2 verified round 1's closes and reviewed phase 5 at cfb846b2; its four findings are fixed, answered in `rounds/round-2.md` at ac965ee7. Two commit-flow gaps from the orchestrator's kill matrix (issue #1014) are closed at 5a207e20. Round 3 confirmed round 2's closes and reviewed phases 6 and 7 at 425d052a; the framer reframed at 79f9c3fd, and round 3's fix pass answered both findings: the move check reads the names a moved case reads (S15, 2f681b9c to 8dd97a30), every recorded move check ran again under it and the modules it sent ran their mutants, one lost protection answered at 56d2f856 (`phases/phase-6.md` and `phases/phase-7.md`, each *The move checks re-run with the name condition*), the overview's pairs and wall-time sentences name their trees, the pact case's ids are fixed at 208803e6, and the shrunken corpus file's helper cases moved at 4e987021 |

The phase records `phases/phase-1.md` to `phases/phase-6.md` hold each module's cases, mutants and cut lines. `overview.md` holds the divergences from the frame.

## Phase 5, module by module

| Module | Commit | Cases before | Cases after | Proof |
|---|---|---|---|---|
| `skills/verify/scripts/broad_gate.py` | 8f4b7431 | 421 in three files, 45.6 s | 262 in three files, 7.2 s | old rule: 104 mutants, all red |
| `skills/verify/scripts/seal_stamp.py` | 94660204 | 186 in two files, 13.5 s | 245 in three files, 8.1 s | old rule: 100 mutants; 23 old gaps closed, 2 equivalent |
| the commit flow, `tests/e2e/commit/` | c7f38def, 7efbd4c6 | 189, 157.5 s serial | 181, 60.1 s serial; 43.4 s at 7efbd4c6 against 53.1 s at dde8ccd1, its stubs hardlinked | 34 mutants under the old rule, 6 under the new; 4 survive both files and are recorded as old gaps |
| `skills/verify/scripts/mutation_check.py` batch mode | 29cd8544, 4a509442 | none | its cases in `tests/test_mutation_check.py` | 20 mutants, 18 red, the 2 survivors red after two assertions |
| `hooks/commit-review-gate.py` | 54c9e803, af336515 | 1,000 in three files, 124.3 s serial | 670 in four files, 11.0 s serial | new rule: 32 mutants in one batch, 4 survivors, all red after a row each |
| `hooks/worktree-guard.py` | 8ecb8d32 | 251 in two files, 39.8 s serial | 210 in the same two, 6.9 s serial | new rule: 35 mutants, all red |
| `skills/code-review/scripts/chain_check.py` | c9e2f5be | 126 in one file, 52.7 s serial | 186 in the same file, 32.7 s serial | new rule: 37 mutants; 2 survivors, one an equivalent old gap, one red after a row |
| `skills/verify/scripts/pact_check.py` | 7c2fff8c | 68 in one file, 20.9 s serial | 106 in the same file, 4.6 s serial | new rule: 43 mutants, all red |
| `hooks/root-migrate.py` | df5136f1, 95db3498 | 54 in one file, 13.5 s serial | 72 in `tests/test_root_migrate.py` and 6 left in the old file, 9.4 s serial | new rule: 41 mutants; 1 survivor, an old gap, red after a row |
| `skills/implement/scripts/seal.py` | ef95b457 | 183 in two files, 24.0 s serial | 315 in `tests/test_seal.py` and 13 left in the two old files, 11.4 to 13.4 s serial | new rule: 101 mutants over 53 classes; 1 survivor, an equivalent old gap; 1 more old gap closed by a row |
| `evals/scripts/noninferiority.py` | 452cbeb6, 136c8923 | 133 in one file, 98 of them this module's, 14.8 s serial | 252 in `tests/test_noninferiority.py` and the generators' 35 left in the old file, 8.3 to 8.7 s serial | new rule: 91 mutants over 62 classes; 1 survivor, an old gap, red after a row |
| `skills/verify/scripts/unverified_check.py` | 984a5cd2, b770ca64 | 236 in one file, 8.3 to 8.5 s serial | 313 in `tests/test_unverified_check.py` and 43 left in the old file, 7.0 to 7.4 s serial | new rule: 123 mutants over 56 classes; 4 survivors, 2 old gaps and 2 the old file killed, each red after a row |

Seconds are macOS wall time on a shared machine, from each module's record.

## Phase 6, group by group

| Group | Commit | Modules | Move check's last line | Proof |
|---|---|---|---|---|
| 1 | 0a86c1b4 | `hooks/lint-python.py`, `hooks/version-check.py`, `hooks/review-skill-gate.py`, `hooks/question-gate.py` | `73 old cases, 74 items against 73 at 43324e4e104e, 17 failed` | each failure a merge or a split; 40 mutants over the four, 8 survivors, every one an old gap |
| 2 | ccca432d | `hooks/launch.py`, `hooks/one_heredoc.py` | `20 old cases, 147 items against 147 at 0a86c1b4c088, 0 failed` | the move check at its commit; with the name condition, 13 mutants over `hooks/one_heredoc.py`, 2 old gaps |
| 3 | e6700896 | `hooks/session-lease.py` | `108 old cases, 119 items against 119 at ccca432d83a7, 3 failed` | one merge; 15 mutants, 6 survivors, every one an old gap |
| 4 | 714f2df2 | `hooks/mode-gate.py` | `66 old cases, 180 items against 180 at e945c57c16fc, 4 failed` | one merge; 16 mutants, 4 survivors, every one an old gap |
| 5 | 04115ed2 | `hooks/answers.py`, `hooks/answer-write.py`, `hooks/answer-clear.py` | `17 old cases, 37 items against 37 at 714f2df2eff1, 0 failed` | the move check at its commit; with the name condition, 25 mutants over the three, 3 old gaps, and a17 a lost protection, red after a case at 56d2f856 |
| 6 | df48707c | `hooks/hooksession.py` | `18 old cases, 28 items against 28 at 04115ed2da4d, 0 failed` | the move check at its commit; with the name condition, 21 mutants over `hooks/hooksession.py` and `hooks/session-lease.py`, 7 old gaps |
| 7 | 9c70ddbf | `hooks/dispatch.py`, `hooks/console.py`, the creation flow | `51 old cases, 59 items against 59 at 5639d076e5d3, 2 failed` | one helper call renamed; 53 mutants over the two modules, 3 survivors, every one an old gap |
| 8 | 4f50aee0, 6c126f35 | `hooks/routing.py` | `51 old cases, 69 items against 70 at 459d7944c0d4, 4 failed` | one merge; 16 mutants, 5 survivors, 3 old gaps and 2 red after a case each |
| 9 | d8bba633 | `hooks/implementer-mark.py`, `hooks/implementer-notice.py` | `24 old cases, 24 items against 24 at 8dedf9e4698c, 3 failed` | one merge; 22 mutants over the two hooks and `hooks/implementer.py`, 8 survivors, every one an old gap |
| 10 | 449feefb | `hooks/optin.py` | `46 old cases, 47 items against 47 at 9197c897c376, 6 failed` | three cases request the file's fixture; 15 mutants, 5 survivors, every one an old gap |
| 11 | e94c6826 | `hooks/worktree_consent.py` | `100 old cases, 165 items against 165 at 167950a6e8bb, 0 failed` | the move check at its commit; with the name condition, group 17's table, 4 old gaps, and k25 red on a case at the head |
| 12 | c512b123 | `hooks/worktree-guard.py`'s light files | `219 old cases, 358 items against 358 at 56fb82e0646c, 123 failed` | 110 lines the autouse fixture alone, five helper renames, one merge; 70 mutants, all red |
| 13 | 5d6640b2 | `hooks/sealer-stamp.py`, `hooks/sealer-stamp-queue.py`, `hooks/commitgate.py`'s guarantee arm, written anew | none: rule 3 | 43 mutants over the three, 4 survivors, every one an old gap; 62 items in 35.96 s before, 91 in 10.98 s after |
| 14 | f5185d67 | `hooks/commit-review-gate.py`'s light cases, less those holding the rules of five lines with no item | `144 old cases, 187 items against 187 at 9818ee1a991f, 90 failed` | 32 lines the autouse fixture alone, the routing helper renamed, two merges; 40 mutants, 6 survivors: 4 old gaps, and 2 the old files kill through cases that did not move |
| 15 | f1d13be0 | `hooks/blocks.py` | `31 old cases, 142 items against 142 at 06d0f55453fc, 0 failed` | the move check at its commit; with the name condition, 15 mutants over `hooks/blocks.py`, 1 old gap |
| 16 | b8e201e1 | `hooks/commitgate.py`'s parity case | `56 old cases, 71 items against 71 at 0b134a29b35e, 0 failed` | the move check at its commit; with the name condition, 7 mutants over `hooks/commitgate.py`, all red |
| 17 | 67a86c57 | `hooks/commit-review-gate.py`'s cases the five lines held, `hooks/worktree_consent.py`'s one beside them | `292 old cases, 409 items against 409 at b8e201e1f012, 115 failed` | 66 lines the autouse fixture alone, 2 its class override, 18 helper renames and one nested docstring, two merges; 44 mutants over the gate, 2 survivors, both old gaps, and g9, g11, g13 and g38 red now; 25 over the consent writer, 5 survivors, every one an old gap |
| 18 | 95991e42 | `hooks/gate.py` | `27 old cases, 27 items against 27 at 67a86c5730f0, 0 failed` | the move check at its commit; with the name condition, 3 mutants over `hooks/gate.py`, 1 old gap |
| 19 | e1e39bf7 | `hooks/tokens.py` | `2 old cases, 19 items against 19 at 95991e42b3d5, 0 failed` | the move check at its commit; with the name condition, 8 mutants over `hooks/tokens.py`, 1 old gap |
| 20 | 6277911e | the local-mode file's two cases, to `hooks/implementer-notice.py`'s and `hooks/optin.py`'s files | `53 old cases, 55 items against 55 at e1e39bf7b23d, 0 failed` | the move check at its commit; with the name condition, 15 mutants over `hooks/implementer-notice.py` and `hooks/optin.py`, 3 old gaps |
| 21 | 1b3e6978 | `hooks/config.py`'s reference roots, policy root, normaliser, baseline and row reader, from six small files | `193 old cases, 803 items against 803 at fb0c5dfccd2f, 0 failed` | the move check at its commit; with the name condition, groups 23's and 36's tables over its old files, 8 old gaps, and config's c55, c57, c62 to c65 and c67 red on oracle cases that stand |
| 22 | 10f6ad94 | `hooks/config.py`'s 33 reader cases of the mode question file | `65 old cases, 190 items against 190 at 92add28be86b, 0 failed` | the move check at its commit; with the name condition, group 23's table over its old files, 12 old gaps |
| 23 | ca726662 | `hooks/config.py`'s pact readers, from the signer file and the seven cases `tests/test_pact_check.py` held | `134 old cases, 333 items against 333 at c6c1d8b03de3, 7 failed` | two bodies read `PACT_TEXT`, one merge; 87 mutants over the module, 12 survivors: 5 old gaps, and 7 the oracle file kills through cases that did not move |
| 24 | 93bf39da | the heredoc-data file: S4 and S5 to `hooks/cmdline.py`'s new file, S6 to `hooks/tokens.py`'s | `4 old cases, 215 items against 215 at 687388b5ae85, 0 failed` | the move check at its commit; with the name condition, group 26's table over its old files, 17 old gaps |
| 25 | eb207a6d | `hooks/cmdline.py`'s cases of the walk, reserved-word, wrapper and no-shape files | `65 old cases, 661 items against 661 at 3cf118239946, 0 failed` | the move check at its commit; the module's mutants run in group 26; with the name condition, group 26's table over its old files, 17 old gaps |
| 26 | da3eae09 | `hooks/cmdline.py`'s cases of the reader and path files, and the reader file's S13 to the guard's file | `367 old cases, 1189 items against 1189 at 0e561e86de7a, 26 failed` | thirteen bodies renamed apart; 120 mutants over `hooks/cmdline.py`, 17 survivors, every one an old gap; 70 over the guard, all red |
| 27 | ffb0bd4b | `skills/verify/scripts/deferral_check.py` | `11 old cases, 11 items against 11 at 300abe340a60, 0 failed` | the move check |
| 28 | b16613b3 | `skills/verify/scripts/mutation_check.py`'s single-pair cases, and `agents/smith.md` lines 109 and 123 | `40 old cases, 54 items against 54 at 6b884f5f9f41, 0 failed` | the move check at its commit; with the name condition, 22 mutants over `mutation_check.py`, 1 old gap |
| 29 | 31aed13b | `skills/verify/scripts/coordinates.py` | `29 old cases, 50 items against 50 at 7cd34d46115a, 0 failed` | the move check at its commit; with the name condition, one line on a case of an undeclared file, no module |
| 30 | 666cedbb | `skills/verify/scripts/payload_meter.py` | `24 old cases, 25 items against 25 at 2f2d21c97c4f, 0 failed` | the move check |
| 31 | 391c7857 | `skills/verify/scripts/pytest_record/specseal_pytest_record.py` | `34 old cases, 46 items against 46 at 17ee85328290, 0 failed` | the move check |
| 32 | bf6df24b | `skills/verify/scripts/arm_check.py`, and its docstring's citation of a removed case | `63 old cases, 95 items against 95 at 6df0950bb66f, 0 failed` | the move check |
| 33 | c9af3c38 | `skills/verify/scripts/session_cost.py`'s three files, and `token_thirds`' docstring naming the new file | `194 old cases, 221 items against 221 at 95d02cc818d9, 8 failed` | `Test_emit`'s own `transcript` and one assertion renamed; 63 mutants, 13 survivors, every one an old gap |
| 34 | 5966150b, ffd898ec | `skills/verify/scripts/broad_gate.py`'s two light files, and the scan's docstring naming the new file | `198 old cases, 314 items against 315 at 10667b32ad71, 45 failed` | 28 lines the autouse fixture alone, two renames, two merges; 113 mutants, 4 survivors, every one an old gap |
| 35 | 2272cd1e | `skills/verify/scripts/unverified_check.py`'s two oracle cases of `heading_level`; `seal_stamp.py` and `pact_check.py` had none | `171 old cases, 329 items against 329 at ffd898ec87dc, 0 failed` | the move check at its commit; with the name condition, 6 mutants over `unverified_check.py`, all red |
| 36 | 19c01e3b | `skills/code-review/scripts/chain_check.py`'s cases of the sealer file and the local-mode file, and `agents/sealer.md` line 144 | `116 old cases, 246 items against 246 at c30f7d9521c6, 8 failed` | the `item` fixture and one template renamed; 54 mutants, 3 survivors, every one an old gap |
| 37 | 809408e5 | `skills/settle/scripts/fold_check.py`, `rule_changes.py` and `settle.py`, and `skills/writing-style/SKILL.md` line 268's settle file | `116 old cases, 174 items against 174 at db6541fc96b0, 0 failed` | the move check at its commit; with the name condition, 53 mutants over `rule_changes.py` and `settle.py`, 5 old gaps |
| 38 | 4f350b0f | `skills/implement/scripts/seal.py`'s writer and re-export cases | `174 old cases, 330 items against 330 at 809408e5ec2e, 0 failed` | the move check |
| 39 | 46e1ec4c | `.github/scripts/issue_claims_check.py` | `38 old cases, 50 items against 50 at 4f350b0f9144, 17 failed` | three merges of pairs; 34 mutants, 10 survivors, every one an old gap |
| 40 | 565de415 | `.github/scripts/release_report.py`'s other cases | `9 old cases, 15 items against 15 at 409d8037ab94, 0 failed` | the move check at its commit; with the name condition, 14 mutants over `release_report.py`, 3 old gaps |
| 41 | 56a8ac20 | `.github/scripts/rules.py`, and `skills/writing-style/SKILL.md` line 268's other file | `22 old cases, 61 items against 61 at 565de4152a2c, 0 failed` | the move check at its commit; with the name condition, one line on a case of an undeclared file, no module |
| 42 | 5e26a264 | `.github/scripts/release_completeness_check.py` | `25 old cases, 30 items against 30 at 56a8ac20bf30, 0 failed` | the move check |
| 43 | 0cc2609c | `.github/scripts/plugin_directory_check.py` | `12 old cases, 17 items against 17 at 5e26a264b9d6, 0 failed` | the move check |
| 44 | 222bf69a | `.github/scripts/roll_flow_measurement_issue.py` | `35 old cases, 35 items against 35 at 0cc2609cad5a, 2 failed` | one nested docstring the formatter re-indents; 38 mutants, 4 survivors, every one an old gap |
| 45 | efc3a79f | `.github/scripts/close_issues_on_release.py`, `label_merged_on_release_branch.py` and `tracker_labels.py` | `94 old cases, 102 items against 102 at bc2b976ffa97, 21 failed` | the refusal file's fake renamed, one merge; 77 mutants over the three, 17 survivors, every one an old gap |
| 46 | b68d41d1 | `.github/scripts/durations_union.py` | `24 old cases, 33 items against 33 at efc3a79f8793, 0 failed` | the move check |
| 47 | 503e2f5e | `.github/scripts/gather_changelog.py` | `42 old cases, 52 items against 52 at b68d41d1caa8, 0 failed` | the move check |
| 48 | f7ef43cc | `.github/scripts/publish_release_note.py` and `release_seal.py` | `47 old cases, 80 items against 80 at 503e2f5e32f4, 0 failed` | the move check at its commit; with the name condition, two lines on cases of an undeclared file, no module |
| 49 | a4a113f6 | `.github/scripts/run_tests.py` | `60 old cases, 95 items against 95 at f7ef43ccac39, 0 failed` | the move check at its commit; with the name condition, five lines on cases of an undeclared file, no module |
| 50 | 52ce0e03 | `evals/scripts/replay_targets.py`, `rule_cases.py` and `seed_defects.py` | `26 old cases, 35 items against 35 at f19395a52bea, 0 failed` | the move check at its commit; with the name condition, 29 mutants over `rule_cases.py`, `replay_targets.py#truths_with` and `seed_defects.py`, 5 old gaps |

`hooks/cmdline_base.py`, `hooks/git/` and `evals/scripts/behaviour.py` have no case of their own to move, and their records say why. `hooks/githooks.py` and `hooks/hook-install.py` keep their cases in the installer file under `questions.md` Q10's default.

`phases/phase-6.md` holds each group's command, cases and seconds, mutants and cases left in place.

## What the new proof costs

The owner replaced the 100-mutant table on 2026-10-22 (`spec.md` *The proof of equal protection*). Under the old rule one module took one to two hours, most of it four full runs per mutant.

| Measure | Old rule | New rule, `commit-review-gate.py` |
|---|---|---|
| Mutants per module | about 100 | 32 |
| Runs per mutant | four: a baseline and a mutated run, in the old and the new column | one, after one baseline per batch; the old column only for survivors |
| Module, first read to record commit | one to two hours | 26 minutes |
| Mutation runs | most of the module's time | 119.5 s for the new column, 181.4 s for the old column's 4 survivors |

## What is red, and why

- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite` failed on every CI run of this branch up to run 39964746967 at b2c300c9, because the rebuilt cases had no price in `.test_durations` (round 1 finding 8, deferred by the orchestrator to phase 7). 3c6b9e0d replaced the file from that run's `test-durations` artifact, and the case passes locally with 19 cases unpriced, 0.25%, the ones 099cd54d moved.
- CI run 39748911321 at 281873fb failed on four of nine pytest legs. Lint passed. Two causes:
  - the durations case above, on three legs, with 1,200 of 7,120 collected cases unpriced;
  - three cases of the rebuilt `tests/test_broad_gate.py`, on Windows shard 1 only, each expecting a printed path with forward slashes where Windows prints backslashes: two the record's path, one the workflow's. 0e6a02b3 builds both expectations with the platform's separator, as the cases at 6046f062 did, and CI run 39866987196 at dde8ccd1 passed them on Windows (`executed` by the orchestrator).
- CI run 39866987196 at dde8ccd1 failed two other Windows cases, each fixed and run on macOS only: the commit flow's per-case copy wrote over the hidden `.git` file of its linked worktree, 43 setup errors on shard 1, fixed at 7efbd4c6; and `Test_walk_command`'s cd case in `tests/test_worktree_guard.py` expected a path the walk normalises, shard 4, fixed at 3e5cbb59 (`phases/phase-5.md` *The commit flow's stubs, hardlinked* and *The worktree guard's cd case on Windows*).

## Decisions taken today

- `--pairs` leaves out a call with an argument that reads a name the case assigns or takes as a parameter, and a call with no argument. Leaving out only the one argument named 31 non-pairs and was dropped (`plan.md` *Alternatives*).
- The proof of equal protection is a decision-point sample: one or two mutants per class at the decision points where a case accepts or refuses, and one more for each further decision point, so the count follows the module's classes (`spec.md` *The proof of equal protection*). They run in one `mutation-check` batch call, with the old column run only for survivors.
- The owner chose on 2026-10-22 to finish all seven phases in 0.22.3, and answered Q1 and Q2 with their defaults.

## Left for the next session

1. Round 4 is next: a round verifying round 3's fix pass, the name condition and the re-run's mutants among it, at the tree this file describes. Then the broad gate, the sealer, the pull request into `release/v0.22.3`, and the release preparation.
2. See the files phase 7 and round 3's fix pass changed after b2c300c9 pass on the Windows and ubuntu legs of the next CI run (`overview.md` *Not verified*). CI run 39964746967 at b2c300c9 passed every file written before it on those legs, apart from the durations case.
3. The framer answers `overview.md` *Not verified*'s row on the 20 cases the name condition names in files that declare no `TARGET`.
4. Place `hooks/root-migrate.py#move`'s empty directory, which the rebuild found and pinned as it is (`overview.md` *Not done*).
5. The `## Rule changes` items for `docs/one-root-by-lifetime.md` and its Korean twin are in `spec.md` since 93a009c6, and the worktree guard's since 099119b8.
6. The `## Rule changes` items the fifth spawn found missing are in `spec.md` since 0b134a29, with *The check lines the remaining groups meet* for the lines outside `docs/`; groups 16 to 20 moved on them, and the framer's lines that named too little were settled at 9e92e4e8.

## How a smith spawn for the next modules reads

Each spawn so far took one or two modules. The prompt that worked names:

- the worktree, the branch and HEAD, and that the routing is automation through the review chain;
- what to read first: `spec.md`, `plan.md`, `questions.md`, every phase record, `overview.md`, `rounds/round-1.md`, `CONTRIBUTING.md` *The test layout* and `skills/writing-style/SKILL.md`;
- the modules to rebuild, one commit each, stopping at a module boundary rather than starting one it cannot finish with a complete record;
- the proof: decision-point mutants in one `mutation-check` batch call with `-x` in `--tests`, the old column only for survivors; for phase 6, the move check first, `bin/test-layout --moved <the commit before the group> --from <every old file> --to <every new file and every old file that keeps cases>`, and the mutants only for a module whose cases fail it;
- that `TARGET` must be the first statement after the imports, so a hook module the cases import by name is loaded through `load_hook_module`, and that the edit hook runs `ruff check --fix`, which drops an import nothing uses yet, so the census line goes in with its import;
- the copy rule: a file git or a shell executes inside a copied world is hardlinked from a template that ran it once, as `tests/e2e/commit/test_commit_flow.py#_link_or_copy` does, and a case that changes such a file writes a new one;
- a module whose old file and new file share no name leaves the old file's listing scopes to `tests/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE`, which names each scope that lists paths from git;
- the runs at each commit: the module and its importers, `tests/test_censuses.py` and every file `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists, `tests/test_chain_hooks_hardening.py`, the shards module over the whole collection, `bin/test-layout --check`, `bin/rules --check`, `bin/unverified-check seal/specs/`, and ruff one changed file at a time;
- edits through the Edit or Write tool only, git as `git -C <worktree>`, no HTML comment and no section sign, no edit under `docs/`, commit and no push;
- a hand-back with the commits, the timings, the counts and seconds, the mutation results, the modules remaining and the frame sentences to change.
