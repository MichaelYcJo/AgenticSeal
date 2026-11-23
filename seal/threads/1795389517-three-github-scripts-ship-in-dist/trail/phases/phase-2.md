# Phase 2: 1795389517-three-github-scripts-ship-in-dist

## What this phase found

**The frame held, with three departures.** Each was judged against `frame/design.md` and the tree at `4777ae575`.

- **The floor case that no load reaches `tests/` had to change.** `bin/test` now hands its interpreter `tests/run_tests.py`, so `before_any_floor` starts from a file under `tests/`. `test_a_script_reaches_no_module_under_tests` then failed on its tree line. Executed before the edit: `bin/test tests/behaviour/test_every_entry_point_runs_at_the_floor.py -q -p no:xdist` was red with `assert not ['tests/run_tests.py']`. The line now leaves out what a `bin/` wrapper hands its interpreter, read through `handed_first`, and still refuses any file under `tests/` that a load reaches. The case's docstring and `before_any_floor`'s say so. *Scope* item 6 names only the `ruff.toml` rows, and the rows needed nothing beyond the re-point. The case change was judged against the case's own rule, which its docstring gives: "a path under `tests/` is no load".
- **A8's map lost the two rows this phase moves.** *Scope* item 11 re-points every line that *User scenarios* row 4's search prints, except `docs/releasing/branch-and-release.md`. `tests/behaviour/test_a_cited_section_stands_in_its_file.py:928-929`, two rows of `RUN_BY_A_SHIPPED_COMMAND`, are such lines. Re-pointing them would make A8 fail, because A8 compares the map with the archive's `.github/scripts/`. So the two rows went, and A8's docstring says "each script" where it said "the three". The closer's row, A8 itself and the map stay for phase 3 (*Scope* item 10).
- **`lib/console.py`'s listing command leaves the runner out.** The docstring says its `git grep ... ':!tests'` command "lists every place that spells the loop". `tests/run_tests.py` spells the loop and now stands under `tests/`. The sentence now says "outside the suite" and names the runner beside the command. The frame does not name this line. It changed because HEAD would contradict it otherwise.

**Decisions settled while writing the code.**

- `tests/run_tests.py`'s docstring said why the runner lived under `.github/`. It now says the runner lives under `tests/`, beside the suite, and that `dist` holds `bin/test` with no runner beside it. The sentence "The check below is for the other case, a copy of `bin/` taken on its own" went. `main`'s own check for a `tests/` directory stays, though no copy the plugin ships reaches it any more. `gaps.md` *Not done* says why.
- `chain_check.py`'s two refusal messages keep the reader's path as a literal rather than reading `CHECK_LINES_READER`. `tests/skills/test_chain_check.py` sets the constant to a missing file and expects the message to name the real path, so a message built from the constant would name the missing file. The three messages and the pinned `CHECK_LINE_SAYS` were rewrapped to stay under 88 columns, and their text is unchanged.
- The comment above `CHECK_LINES_READER` keeps "A user's CI clones the plugin whole, so it stands here there too". It is still true at the new path.
- Prose lines that grew past their file's column were rewrapped: `chain_check.py`'s arm docstring and comment, `skills/settle/rule-changes.md:131`, `lib/console.py`, `tests/conftest.py`'s two docstrings, and the comments in `tests/behaviour/test_the_rules_command_reads_each_rule_off_its_test.py`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` and `tests/text/test_every_agent_reads_the_contract.py`. A `check:` line, a table row and a `# No TARGET:` line stay on one line.
- Each re-pointed sentence under `docs/` only names a path. None is a rule change, as `frame/design.md` *Grounding* reads `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*.

**The census of old spellings.** Executed at `4777ae575`:

- `git grep -n -E '\.github[/\\]+scripts[/\\]+(rules|run_tests)\.py' -- ':!seal/threads'` prints only `docs/releasing/branch-and-release.md:168` and `:169`, which *Rule changes* item 2 rewrites at the settle. At `036e7d424` it prints lines in 36 files.
- `git grep -n -E '"\.github", "scripts", "(rules|run_tests)\.py"' -- ':!seal/threads'` prints nothing, exit 1. At `036e7d424` it prints 8 lines.
- `git grep -n -E 'tests/github/test_(rules|run_tests)' -- ':!seal/threads'` prints nothing, exit 1. At `036e7d424` it prints 10 lines.
- `bin/seal rules --check`, exit 0: `seal rules: all 176 check lines in 68 rule files hold.`

**The move check refused, so the mutation tables follow.** Executed: `bin/seal layout --moved 76748be45 --from tests/github/test_rules.py tests/github/test_run_tests.py --to tests/skills/test_rules.py tests/test_run_tests.py`, exit 1. Last line: `seal layout: moved: 63 old cases, 124 items against 124 at 76748be45512, 64 failed`. Neither old file changed between `036e7d424` and `76748be45` (executed: `git diff --stat` printed nothing). Every case failed the names condition alone, `name SCRIPT: its definition differs from the base's`, because the loader names the new path. One case also failed the body condition: `Test_module::test_a_script_copied_alone_exits_2_and_names_what_it_misses` is the one case rewritten. Its expected `lib/sibling.py` path climbs one more `..`, because `ROOT` gained a level. It still guards the sentence a copy of the script taken alone prints. No case was cut.

`bin/seal layout --check tests/skills/test_rules.py tests/test_run_tests.py` exit 0: `2 files read, 0 refused`. Its `report:` lines name functions with no class of their own. They are the same functions the old files left without a class.

**Cases and seconds.** Executed: `.venv/bin/python -m pytest <files> -q -p no:xdist`. The old files ran in a detached worktree of `76748be45` under the scratch directory, removed afterwards: `126 passed in 2.41s`. The new files at `4777ae575`: `126 passed in 2.21s`.

**Real-git cases kept**, found by a search for a `"git"` argument in each case body and in the module helpers it calls. This is a sample, because a fixture that builds a repository, such as `tests/conftest.py`'s `shared`, was not followed. `tests/test_run_tests.py`: `Test_ensure::test_an_adopted_environment_is_hidden_too`, `test_a_refused_environment_is_hidden_too`, `test_a_directory_no_builder_can_finish_is_hidden_too`, `Test_hide_from_git::test_accepts_a_built_environment_and_hides_it_from_git`, `Test_build::test_a_failed_build_still_leaves_no_trace_in_git`, `Test_main::test_an_unwritable_venv_leaves_the_refusal_a_sentence`. `tests/skills/test_rules.py`: `Test_main::test_with_no_root_the_targets_resolve_where_the_command_runs`.

**Mutation table for `skills/settle/scripts/rules.py`.** Executed at `4777ae575`: one `bin/seal mutate` call, tests `bin/test tests/skills/test_rules.py -q -x -p no:xdist`. Last line: `seal mutate: 18 mutants, 18 red, 0 SURVIVED, 0 with no verdict (21.0s)`.

| # | Unit | Mutant | New file | Old files |
|---|---|---|---|---|
| 1 | `ROOT` | up two levels, not three | red | not run |
| 2 | `main` | neither-or-both test always false | red | not run |
| 3 | `main` | `--check` returns 0 | red | not run |
| 4 | `check` | a refusal returns 0 | red | not run |
| 5 | `check` | no excused line printed | red | not run |
| 6 | `check` | no line printed as not read | red | not run |
| 7 | `parse` | an empty target accepted | red | not run |
| 8 | `parse` | a refused symbol accepted | red | not run |
| 9 | `target_problem` | a missing file resolves | red | not run |
| 10 | `target_problem` | an eval case without `case.yaml` resolves | red | not run |
| 11 | `markers` | dot directories walked | red | not run |
| 12 | `refused_lines` | no refusal returned | red | not run |
| 13 | `unresolved` | no refusal excused | red | not run |
| 14 | `render` | no `refused:` line | red | not run |
| 15 | `sibling` | exit 3 where `lib/sibling.py` is absent | red | not run |
| 16 | `policy_documents` | an unreadable index reads as no documents | red | not run |
| 17 | `main` | the root not taken from the repository the command runs in | red | not run |
| 18 | `first_sentence` | the whole paragraph printed | red | not run |

Mutant 1, run alone without `-x`, failed one case: `Test_module::test_a_script_copied_alone_exits_2_and_names_what_it_misses`. That case is the one that holds the level `ROOT` gained.

**Mutation table for `tests/run_tests.py`.** Executed at `4777ae575`: one `bin/seal mutate` call, tests `.venv/bin/python -m pytest tests/test_run_tests.py -q -x -p no:xdist`. Last line: `seal mutate: 14 mutants, 14 red, 0 SURVIVED, 0 with no verdict (9.9s)`.

| # | Unit | Mutant | New file | Old files |
|---|---|---|---|---|
| 1 | `ensure` | an environment below the floor adopted | red | not run |
| 2 | `ensure` | a build with no pytest accepted | red | not run |
| 3 | `hide_from_git` | an existing ignore overwritten | red | not run |
| 4 | `hide_from_git` | an empty ignore written | red | not run |
| 5 | `build` | the standard-library build taken on any interpreter | red | not run |
| 6 | `build` | the failed-step sentence reworded | red | not run |
| 7 | `build` | `uv` installs no packages | red | not run |
| 8 | `main` | no refusal for a tree with no `tests/` | red | not run |
| 9 | `main` | `-n auto` added over the caller's choice | red | not run |
| 10 | `main` | no arguments hand pytest nothing | red | not run |
| 11 | `main` | pytest run from the caller's directory | red | not run |
| 12 | `main` | exit 0 whatever pytest exits | red | not run |
| 13 | `main` | the interpreter not named | red | not run |
| 14 | `repo_root` | up one level, not two | red | not run |

Mutant 14, run alone without `-x`, failed one case: `Test_module::test_the_root_is_the_repository_not_the_scripts_directory`.

**The runner cannot be mutated through `bin/test`.** A first call ran the same 14 mutants with `bin/test tests/test_run_tests.py ...` as its tests. `bin/test` executes `tests/run_tests.py`, so each mutant broke the command that ran the cases: mutant 12 read `SURVIVED` because the broken runner exits 0, and mutant 14 read `red` at exit 2 because the broken runner refused to start. That call measured the runner, not the cases, and is not the table above. A future mutation of the runner calls the virtualenv's interpreter directly.

**Seen red (contract rule 15) for the floor case's changed line.** The line asserts that no load reaches a file under `tests/`, so its guard is `loaded_by`'s `not t.startswith(TESTS)`. Executed: a probe, `<scratchpad>/1795389517-three-github-scripts-ship-in-dist/phase-2/test_tmp_floor_guard.py`, run once. With `TESTS` set to a string no path starts with, the line names `tests/block_shapes.py`, `tests/censuses.py`, `tests/commonmark_oracle.py`, `tests/conftest.py`, `tests/gfm_table_oracle.py` and `tests/workflows.py`. With the guard in place it names nothing. The case's fixture line, unchanged, fails first on the same guard, which is why the probe read the tree line alone.

**For phase 3.** `.gitattributes:11-14` says three scripts under `.github/scripts/` stay in `dist`. One stays from `4777ae575` on, the closer. *Scope* item 7 rewrites that comment with the one `/.github/` line. `docs/releasing/branch-and-release.md:166-171` still names the three, and *Rule changes* item 2 rewrites it at the settle.
