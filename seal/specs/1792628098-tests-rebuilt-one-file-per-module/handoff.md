# Handoff: 1792628098-tests-rebuilt-one-file-per-module (#942)

Written 2026-10-22 by the orchestrator, when the owner paused the build after phase 5's first proof under the new rule, and brought up to date on 2026-10-23 by the smith spawns that rebuilt the modules since. The branch is `chore/942-tests-rebuilt-one-file-per-module`, cut from `release/v0.22.3` at 6046f062. The tree this file describes is b770ca64 and the commit that updates this file.

## Where the build stands

| Phase | State |
|---|---|
| 1 to 4 | built: `bin/test-layout`, the slow-case report, the censuses in `tests/censuses.py`, the helper twins in `tests/conftest.py` |
| 5 | closed at b770ca64: 11 modules rebuilt, plus the `mutation-check` batch mode |
| 6 and 7 | not started |
| Review | round 1 covered phases 1 to 4 at 8aa42bf8; its nine findings are answered, eight fixed at c6d2bfc4 and one deferred to phase 7; no verifying round has run yet |

The phase records `phases/phase-1.md` to `phases/phase-5.md` hold each module's cases, mutants and cut lines. `overview.md` holds the divergences from the frame.

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

## What the new proof costs

The owner replaced the 100-mutant table on 2026-10-22 (`spec.md` *The proof of equal protection*). Under the old rule one module took one to two hours, most of it four full runs per mutant.

| Measure | Old rule | New rule, `commit-review-gate.py` |
|---|---|---|
| Mutants per module | about 100 | 32 |
| Runs per mutant | four: a baseline and a mutated run, in the old and the new column | one, after one baseline per batch; the old column only for survivors |
| Module, first read to record commit | one to two hours | 26 minutes |
| Mutation runs | most of the module's time | 119.5 s for the new column, 181.4 s for the old column's 4 survivors |

## What is red, and why

- `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite` fails on every CI run of this branch: the rebuilt cases have no price in `.test_durations`. Phase 7 refreshes the file once, from the final CI run's `test-durations` artifact (round 1 finding 8, deferred by the orchestrator).
- CI run 39748911321 at 281873fb failed on four of nine pytest legs. Lint passed. Two causes:
  - the durations case above, on three legs, with 1,200 of 7,120 collected cases unpriced;
  - three cases of the rebuilt `tests/test_broad_gate.py`, on Windows shard 1 only, each expecting a printed path with forward slashes where Windows prints backslashes: two the record's path, one the workflow's. 0e6a02b3 builds both expectations with the platform's separator, as the cases at 6046f062 did, and CI run 39866987196 at dde8ccd1 passed them on Windows (`executed` by the orchestrator).
- CI run 39866987196 at dde8ccd1 failed two other Windows cases, each fixed and run on macOS only: the commit flow's per-case copy wrote over the hidden `.git` file of its linked worktree, 43 setup errors on shard 1, fixed at 7efbd4c6; and `Test_walk_command`'s cd case in `tests/test_worktree_guard.py` expected a path the walk normalises, shard 4, fixed at 3e5cbb59 (`phases/phase-5.md` *The commit flow's stubs, hardlinked* and *The worktree guard's cd case on Windows*).

## Decisions taken today

- `--pairs` leaves out a call with an argument that reads a name the case assigns or takes as a parameter, and a call with no argument. Leaving out only the one argument named 31 non-pairs and was dropped (`plan.md` *Alternatives*).
- The proof of equal protection is a decision-point sample, about 30 mutants per module in one `mutation-check` batch call, with the old column run only for survivors.
- The owner chose on 2026-10-22 to finish all seven phases in 0.22.3, and answered Q1 and Q2 with their defaults.

## Left for the next session

1. See the commit flow's 43 cases and the worktree guard's cd case, which 7efbd4c6 and 3e5cbb59 fixed, `tests/test_seal.py`, `tests/test_noninferiority.py` and `tests/test_unverified_check.py`, pass on the Windows legs of the next CI run.
2. Place `hooks/root-migrate.py#move`'s empty directory, which the rebuild found and pinned as it is (`overview.md` *Not done*).
3. A `## Rule changes` item, the framer's, for `docs/one-root-by-lifetime.md` and its Korean twin: the `check:` lines that name `seal.py`'s two old files (`overview.md` *Not done*). The worktree guard's sentences are in `spec.md` *Rule changes* since 099119b8.
4. Phase 6, the remaining shipped modules one commit per directory, its first step the move check, and phase 7, `--all`, the `.test_durations` refresh and the closing memo.
5. A verifying round over round 1's fixes and phase 5, then a round over phases 6 and 7, the broad gate, the sealer, the pull request into `release/v0.22.3`, and then the release preparation.

## How a smith spawn for the next modules reads

Each spawn so far took one or two modules. The prompt that worked names:

- the worktree, the branch and HEAD, and that the routing is automation through the review chain;
- what to read first: `spec.md`, `plan.md`, `questions.md`, every phase record, `overview.md`, `rounds/round-1.md`, `CONTRIBUTING.md` *The test layout* and `skills/writing-style/SKILL.md`;
- the modules to rebuild, one commit each, stopping at a module boundary rather than starting one it cannot finish with a complete record;
- the proof: decision-point mutants in one `mutation-check` batch call with `-x` in `--tests`, the old column only for survivors;
- the copy rule: a file git or a shell executes inside a copied world is hardlinked from a template that ran it once, as `tests/e2e/commit/test_commit_flow.py#_link_or_copy` does, and a case that changes such a file writes a new one;
- a module whose old file and new file share no name leaves the old file's listing scopes to `tests/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE`, which names each scope that lists paths from git;
- the runs at each commit: the module and its importers, `tests/test_censuses.py` and every file `git grep -l "git_listing\|tracked_text_files\|ls-files" tests/` lists, `tests/test_chain_hooks_hardening.py`, the shards module over the whole collection, `bin/test-layout --check`, `bin/rules --check`, `bin/unverified-check seal/specs/`, and ruff one changed file at a time;
- edits through the Edit or Write tool only, git as `git -C <worktree>`, no HTML comment and no section sign, no edit under `docs/`, commit and no push;
- a hand-back with the commits, the timings, the counts and seconds, the mutation results, the modules remaining and the frame sentences to change.
