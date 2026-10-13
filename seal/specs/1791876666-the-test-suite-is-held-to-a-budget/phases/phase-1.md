# 1791876666-the-test-suite-is-held-to-a-budget — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | cf77665c |
| Ran by | smith on Opus 5.5, as `routing.md` and `handoff.md` name it |

## What this phase was asked

The commit-gate file `tests/test_the_commit_gate_decides_at_the_commit.py`:
a per-family representative `SAMPLE` beside `CORPUS`, S2 run on `SAMPLE`, a
sampled row that commits nowhere failing instead of skipping, T1–T3, the
mutation table m1–m4 before and after, the removed ids taken out of
`.test_durations`. Verified by local before and after (the frame's figures:
78.19 s wall, 445 s CPU, 297 passed / 70 skipped), the removed ids' Windows
seconds (≥ 737), and every mutation red before and after, with "before"
re-measured at this branch's SHA first. Coverage must not drop: a case is
removed only where the mutation table proves another case kills what it
killed. Say first whether the frame holds against the tree. #930's
`seal/budgets.md` is not on this branch, so the numbers are recorded here,
and the later of the two pull requests lowers the rows. Phase 2 is not
started.

## What this phase found

**Whether the frame holds.** Most of it holds. At b93109a7 the file is 297
passed and 70 skipped. All 70 skips are S2 rows, and the frame's m1 and m2
reproduce (below). One part does not hold: S3's "the sample's rows all land in
`main` or `u` without hooks", read as true on every leg. Which rows are
vacuous depends on the platform, and the frame measured macOS only:

- The 70 macOS skips are mostly programs macOS lacks (`setsid`, `ionice`,
  `flock`, …). The `g`-prefixed GNU tools, `caffeinate` and `arch` land on
  macOS and are absent on ubuntu or Windows.
- `.test_durations` (Windows seconds, `read`) splits in two. A row that ran
  both sandboxes costs 4.9–8.7 s, and one that skipped after the bare run
  costs 2.1–3.8 s. Every `env -i` row is in the low band, as are `zsh -c`,
  `command -p`, the 500-substitution row, `chmod 000` and the `&&` forms of
  `#686: command cd`, `time cd` and `pushd`.
- `env -i` cannot find git on Windows, which the S9 case's comment already
  records (#692's Windows pass). Yet the `env -i` rows are the only S2 rows
  that kill m4 and m5.

So the sample is chosen as follows. A row is in it only if it landed on macOS
(`executed`), sits in the two-sandbox band on Windows (`read`), and uses
nothing but bash, git and POSIX tools. Two `env -i` rows are kept with a
named Windows skip, `NO_GIT_UNDER_ENV_I`, beside the existing
`NO_HOOK_UNDER_LD_PRELOAD`. Every other row that commits nowhere undeclared
fails the test (T2). Ubuntu was not measured row by row; see `overview.md`.

**The battery is m1–m5, not m1–m4** (Q6, drawn from the docstrings before
anything was removed). Under `env -i` the session is found in two places:
the stub's shell decides whether to start Python at all, and `hooksession`
reads the lease. m4 breaks the second place. m5 breaks the first, in
`hooks/githooks.py#_P2`. Both are killed by the same 19 rows before the
change, so the sample keeps two of them.

**The mutation table.** It was run with `bin/mutation-check`, the file's
cases under `bin/test … -q -rf`. Each cell is the verdict and the number of
killers, S2 rows plus other cases.

| # | Mutation | Before, b93109a7 | After, cf77665c |
|---|---|---|---|
| m1 | the review arm never missing: `and not routing.declared(cwd, top)` → `and False and …` in `hooks/gate.py#arms_missing` | red · 204 (156 + 48) | red · 83 (35 + 48) |
| m2 | a declaration ignored: the same clause → `and True` | red · 5 (0 + 5) | red · 5 (0 + 5) |
| m3 | the stub written without its execute bit: `os.chmod(tmp, 0o755)` → `0o644` in `hooks/hook-install.py#write_stubs` | red · 190 (156 + 34) | red · 69 (35 + 34) |
| m4 | the lease not read: `sid = from_lease(common, claude_pid(environ))` → `sid = ""` in `hooks/hooksession.py#session` | red · 22 (19 + 3) | red · 5 (2 + 3) |
| m5 | the stub never sees a lease: `l=1` → `l=` in `hooks/githooks.py#_P2` | red · 21 (19 + 2) | red · 4 (2 + 2) |
| T1 | both `#686 ;` rows taken out of `SAMPLE` | — | red · `test_every_corpus_family_has_a_sampled_row` |
| T2 | the `pytest.skip` put back before the assertion in `_lands_nothing_undeclared` | — | red · `test_a_sampled_row_that_commits_nowhere_undeclared_fails_rather_than_skips` ("was skipped") |
| T3 | `handed: <<<x git` misspelt in `SAMPLE` | — | red · `test_every_sampled_name_is_a_corpus_row` |

Every count of other-case killers is the same before and after. So the cases
removed were S2 rows only, and for each mutation the remaining S2 rows still
include a killer. `git status` was clean after every run.

In m1's before run, 69 cases skipped where the baseline had 70. One vacuous
row landed in that run alone, so a vacuous row's outcome varied from one run
to the next. The sample holds no such row.

**The sample, 35 rows across all 13 subgroups.** `ns` has four kinds
(measured, r1, r2, r3), `shape` has two (wrapped, reserved) and `handed` has
four (HANDED, SUBSTITUTED, REDIRECTED, EVALS). `position`, `#686` and
`#686 ;` are one subgroup each. Across the subgroups the sample covers:

- commits landing in `main` and in `u`;
- the session found by the variable and, under `env -i`, by the lease;
- `exec`, a pipeline, child shells, substitutions and a redirected stdin;
- `stdbuf`.

The names are in `SAMPLE`. To keep `CORPUS` byte-identical, `corpus()` now
also returns each name's subgroup. A probe showed `CORPUS` equal to the old
one, keys in the same order.

**Timing, local** (`executed`, macOS arm64, 12 cores, `bin/test <file> -q`).
The machine was shared with two other builds, and the load average is given
beside each run.

| | Result | Wall | CPU (user + sys) | Load average |
|---|---|---|---|---|
| before, b93109a7 | 297 passed, 70 skipped | 87.61 s | 444.6 s (173.0 + 271.6) | 13.4 → 29.2 |
| after, cf77665c | 179 passed, 0 skipped | 29.18 s | 143.1 s (58.9 + 84.2) | 9.9 → 14.0 |

**Windows seconds, the committed `.test_durations`** (`read`; the ids were
removed by a script that asserted 191 ids and that each was present; the diff
is 191 deleted lines and nothing else):

| Row | Before | After | Owed by the frame |
|---|---|---|---|
| `slow-file:tests/test_the_commit_gate_decides_at_the_commit.py` | 1,137.0 s | 368.2 s | ≤ 400 s |
| the removed ids' sum | — | 768.82 s | ≥ 737 s |
| `suite-seconds` | 7,861.7 s | 7,092.9 s | falls by the removed sum |

T1–T3 are unpriced until #931's refresh. T1 and T3 run no subprocess. T2
builds one bare sandbox, about 2 s here. The file's Windows cost after the
sample is Q4's and stays unmeasured. `test_the_durations_file_prices_the_suite`,
`test_the_durations_file_parses_and_names_cases` and
`test_every_group_of_each_sharded_leg_runs_exactly_once` pass on the pruned
file (`executed`).

**The ledger: one re-read owed, written in phase 4.** S2's new text drifts
the coordinate in G4 of `seal/releases/0.17.0.md`. That is the only drift,
and `evidence-check` exits 1. The claim was re-read and holds: a commit bash
makes into an undeclared repository does not land, save the Windows limits
the row names. `--reverify --into` writes this row:

    | Re-read · G4 · `pre-commit` judges a commit in the worktree it lands in with `hoo… | `seal/releases/0.17.0.md#"### 1790815613-a-gate-decides-at-the-moment-of-the-action-not-from-the-text">"G4 ·"@e8bdea1f`, `tests/test_the_commit_gate_decides_at_the_commit.py#test_s2_a_commit_bash_makes_into_an_undeclared_repository_does_not_land@561885aa` | re-read against the code at the hashes in this row, and the cited row's claim holds | 2026-10-14 | … |

The row is not committed. Once `seal/ledger/1791876666-….md` exists, the work
item counts as live, and the records arm reads `plan.md`. It then refuses six
names there, and `evidence-check` exits 2 instead of 1:

- T1–T3, written without their `test_` prefix;
- T4 and T5, which are not built yet;
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD` in alternative F.

`plan.md` is the framer's file, so whoever writes the fragment in phase 4
first corrects those names, or marks the lines `NAME NOT IN TREE`.

Two things the next phase would otherwise learn the hard way:

- A mutation run rewrites a source file in place for minutes. Any reader of
  that file in the meantime, including `evidence-check --reverify`, reads the
  mutated text. A re-read run during this phase's battery stamped
  `hooks/gate.py#arms_missing` with the mutated hash, and that row was
  discarded.
- `bin/test` on the whole suite with `-k` collects the suite and runs only
  the named cases. That is how the durations case runs at all, since it
  declines on one module.
