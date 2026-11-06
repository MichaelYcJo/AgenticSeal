# Phase 7: 1793935041-the-directory-refuses-every-command-hook

## What this phase found

**The frame holds for this phase, except on the floor table and on the
grep that closes it.** `hooks/lib/` moved to `lib/` and `tests/hooks/` to
`tests/lib/` with `git mv`, and every path string that named them followed,
in `b010ad88`: 128 files, 855 lines added and 883 removed. `e6e2003c`
renames one more case, after the read of the range. The build used
the Edit tool and `git mv` alone. `frame/plan.md` allows this phase a
substitution script, and the spawn prompt narrowed that to the Edit tool.
After the commit, `git ls-files hooks/` printed nothing.

**Q3: the derivation lists eight of `lib/`'s nine modules, so the floor
table holds `lib/*.py`.** `frame/questions.md` Q3 defaults to (a),
`lib/launch.py` alone, and its default cell says phase 7 "sets the floor to
what it lists". The list is not `lib/launch.py` alone.
`tests/lib/test_launch.py#before_any_floor` at `b010ad88` lists
sixteen files. Eight of them are `lib/blocks.py`, `config.py`, `fields.py`,
`gate.py`, `gitcmd.py`, `launch.py`, `optin.py` and `routing.py`: the
stamp's launcher loads `seal_stamp.py`, which loads `lib/optin.py`,
`lib/gitcmd.py` and `chain_check.py`, and those load the rest. Only
`lib/console.py` is outside the set. The table therefore holds
`"lib/*.py" = "py39"`, which is option (b) and the form the table held
before as `"hooks/*.py"`. Listing the eight files instead would leave
`console.py` the one module of `lib/` linted at 3.12, with nothing gained.
`#test_what_runs_before_any_floor_is_linted_at_the_floor` holds the table
to the set both ways, and it passed. Judged against `frame/questions.md` Q3
and `CONTRIBUTING.md` *Running the checks*. `frame/design.md` *Scope* item
11 says the per-file floor "names `lib/launch.py`", and HEAD's table does
not; that line is the framer's.

**The frame's grep cannot read empty outside `seal/threads/`, and what it
lists is history kept on purpose.** `git grep -n 'hooks/lib\|"hooks",
"lib"\|tests/hooks'` lists these files at `b010ad88`:

- `.test_durations`, 850 lines. The test identifiers there go stale at
  every rename. `frame/plan.md`'s judgment row of phase 1 leaves them to
  CI's rebuild, and this phase does the same.
- `evals/behaviour/proofer/seeded-7a8899d5/scaffold.sh` and
  `graders/truth-seeded.md`. This recorded case checks out commit
  `968f5ac`, which holds `hooks/lib/blocks.py`. The census passes over
  recorded cases.
- `evals/scripts/replay_targets.py#CHECK_FILES` and its comment. The
  module is copied from the path the replayed commit holds it at, so
  `hooks/lib/blocks.py`, `fields.py` and `gitcmd.py` stay beside the new
  `lib/` paths. Each old path carries a `# exempt from vacated_paths:`
  line naming the commits that hold it.
- `tests/censuses.py#VACATING` and the comment and docstring that explain
  it. These are the entries that make the old spellings an error.
- `tests/test_censuses.py`, four planted lines that test those entries.
- `tests/evals/test_replay_targets.py`, the `hooks/lib/blocks.py`
  parameter and its docstring.

**Three units adding behaviour, each needed for the move to hold.**

- `tests/censuses.py#SHIPPED` read `("hooks/", "skills/",
  ".github/scripts/")`. After the move, the `splitlines` and
  `heading_rule` censuses would have read no file under `lib/` and passed
  without saying so. No case failed on it, because a census over a file it
  does not read returns nothing. `SHIPPED` now reads `lib/`. The cases in
  `tests/test_censuses.py` that plant a shipped file now plant `lib/x.py`.
  Before `SHIPPED` changed, six `Test_judge` cases ran red.
- `tests/censuses.py#VACATING` gained `("lib/", "hooks/lib/")`,
  `("lib/", "hooks/")` and `("tests/lib/", "tests/hooks/")`, and
  `TEST_AREAS` names `lib` in place of `hooks`. The old
  `("hooks/lib/", "hooks/")` entry read a directory that no longer exists.
  The `("lib/", "hooks/")` entry keeps flagging the pre-#1060 spellings
  such as `hooks/blocks.py`, so the two exemptions for that path still
  excuse a line. `plant_moved` and
  `#test_refuses_the_spelling_each_moved_file_vacated` plant the new
  moves. With the new entries in place, the real tree's census listed 71
  lines in 24 files still naming an old path. That list is how this phase
  found the documents below.
- `evals/scripts/replay_targets.py#CHECK_FILES` gained `lib/blocks.py`,
  `lib/fields.py` and `lib/gitcmd.py`. A round record written after this
  commit reviews a tree whose `chain_check.py` loads `lib/`. Without these
  entries, the copy `checks_at` builds would hold no module, and the
  check would fail to load its reader. The parameter `"lib/blocks.py"` of
  `tests/evals/test_replay_targets.py#test_a_commit_has_its_fence_module_copied_where_it_holds_it`
  ran red before the entry was added.

**Two cases read `hooks/` on disk and would have failed on a clean
clone.**

- `tests/behaviour/test_chain_hooks_hardening.py#test_the_plugin_registers_no_hook_and_writes_none_into_git`
  listed `hooks/` and asserted that `hooks/lib/optin.py` stands. It now
  asserts that no file stands under `hooks/`, passing over `__pycache__`,
  and that `lib/optin.py` stands. At `23b5ef19` it ran red, listing the
  nine modules under `hooks/lib/`.
- `tests/behaviour/test_no_document_names_the_old_roots.py#test_no_hook_names_the_0_3_x_roots`
  ran `os.listdir` on `hooks/` and `hooks/lib/`. On a checkout with no
  `hooks/` directory, that raises. It is now
  `#test_no_lib_module_names_the_0_3_x_roots` and reads `lib/`.

**Names that stated a thing that is not there were renamed.** The frame
names `seal.py#HOOKS` and `HOOK_PURPOSES`. Each other rename was judged by
whether the name now states something absent:

- `HOOKS` became `LIB` in `seal.py`, `chain_check.py`, `pact_check.py`,
  `unverified_check.py` and `tests/conftest.py`. `pr_body.py` reads
  `CHAIN.LIB`.
- `HOOK_PURPOSES` became `LIB_PURPOSES`, and `refuse_without_hooks` became
  `refuse_without_lib`.
- `load_hook_module` became `load_lib_module`, which takes a file name
  under `lib/`. `unverified_check.py#_load_hook` became `_load_lib`.
- Test names that said hook:
  - `test_a_hook_reader_copied_without_the_walk_names_it` in two modules
  - `test_a_hook_reaches_the_modules_under_lib`
  - the two `..._no_hooks_beside_it` cases and `..._are_the_hooks` in
    `tests/skills/test_unverified_check.py`
  - `Test_refuse_without_hooks` and its case
  - `test_reads_the_pairs_hooks_lib_console_holds_from_the_file` and
    `test_refuses_a_block_without_an_answer_outside_hooks` in
    `tests/test_censuses.py`
  - the replay case above
- `tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` became
  `test_the_readers_hide_what_a_renderer_hides.py`.

Judged against `frame/design.md` *Scope* item 11, whose ground is that a
name stating a thing that is not there misleads its reader.
`tests/behaviour/test_chain_hooks_hardening.py` keeps its name, as
`trail/phases/phase-5.md` judged under Q4. The `hooks` key that
`seal_stamp.py` writes into a person's `settings.json` is Claude Code's
own key and keeps its name.

**The two comments `gaps.md` carried were rewritten.**
- `lib/optin.py:97` now says the caller exited with no answer where it
  should have read the repository as not opted in.
- `lib/routing.py:410` now says that its callers, `seal settle` and the
  release scripts, read the checkout they run in.

The paragraph in `gaps.md` *Not done* that carried them is gone.

**Statements edited beyond the Delivers cell, each of which named
`hooks/` as a place.**
- `CONTRIBUTING.md:47` and `.github/PULL_REQUEST_TEMPLATE.md:29`: the
  higher bar covers "anything under `lib/`".
- `CONTRIBUTING.md:81`: "the hook readers" is now "the readers under
  `lib/`".
- `CONTRIBUTING.md:119`: "a git hook" was dropped from the set that runs
  before the floor, because no git hook of the plugin has run a script
  since #1027. `ruff.toml` and `tests/censuses.py` say the same set the
  same way.
- `docs/running/what-a-script-gates.md:25`: a script "under `lib/`".
- `templates/setup/config.md:49`: "the hooks act on it" is now "the
  checks".
- `tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py`: the
  oracle's list of paths it must not reach names `lib/` where it named
  `hooks/`.

**One fixture became a live citation when `lib/` appeared.**
`tests/behaviour/test_a_cited_section_stands_in_its_file.py` used
`lib/manual/b.py#gone` as a citation that moves its file under a longer
path. Once a top-level `lib/` existed, the case's own census read the
string as a citation of this repository, and
`#test_every_cited_name_stands_in_its_file` failed on its three lines. The
fixture is now `moved/manual/b.py#gone`, which keeps the longer path.

**`seal layout --moved` reports every moved file, because the move rewrote
its path strings.** The command run was `seal layout --moved 23b5ef19`,
with the nine `tests/hooks/` files and
`tests/behaviour/test_the_hooks_hide_what_a_renderer_hides.py` in `--from`
and their new paths in `--to`. It exited 1: 225 old cases, 605 items
against 605 at the base, 228 reported. The item count is equal.

- 115 reports name a definition that differs: `HOOKS`/`LIB`,
  `load_hook_module`/`load_lib_module`, `load_hook`/`load_lib`, and
  `LAUNCH` and `launcher` in `test_launch.py`.
- Thirteen old case bodies changed, each by a path string or a renamed
  identifier alone, as `git diff -M 23b5ef19` shows per file:
  - four in `test_config.py`, two in `test_console.py`, four in
    `test_launch.py` and two in `test_routing.py`
  - the oracle case in the renamed behaviour module

The proof of the move is the moved modules passing at the new paths, the
set below, as `skills/verify/SKILL.md` *The narrow command still has to be
able to fail* asks of a rename.

**A leftover on this machine could have hidden a broken path, so the move
was also run in a clean tree.** The main checkout keeps an untracked,
ignored `hooks/__pycache__/` that this phase did not create. A worktree at
`b010ad88`, which has no `hooks/` directory, ran `bin/seal --help` with
exit 0. In the same worktree, `bin/test tests/lib
tests/behaviour/test_chain_hooks_hardening.py
tests/behaviour/test_no_document_names_the_old_roots.py
tests/skills/test_seal.py tests/skills/test_unverified_check.py
tests/skills/test_chain_check.py tests/test_censuses.py` passed 1,621 with
exit 0. The worktree was removed.

**The changelog fragment is not written here.** `frame/plan.md`
*Operational impact* gives the fragment to the orchestrator after the
build, in the commit that moves `plugin.json` to 0.33.0.

**Seen red, and the mutation runs.** Each `seal mutate` run below was made
after `b010ad88` and exited 0 with the verdict `red`:

- `evals/scripts/replay_targets.py` without `"lib/blocks.py"` in
  `CHECK_FILES`, against `-k fence_module_copied`: 1 failed, `[lib]`.
- `tests/censuses.py` with `SHIPPED` lacking `lib/`, against
  `-k Test_judge`: 6 failed.
- `tests/censuses.py` without each of the three new `VACATING` entries,
  one run each, against `-k Test_vacated_paths`: 1 failed each.

**The phase boundary set.** At `b010ad88`, from the repository root:

- `bin/seal --help` exited 0.
- `seal layout --check` exited 0: 132 files read, 0 refused.
- `bin/test tests/lib tests/behaviour/test_the_release_check_watches_what_ships.py
  tests/skills/test_seal.py` passed 914, exit 0.
- `bin/test tests/behaviour/ tests/text/ tests/github/ tests/skills/
  tests/evals/ tests/test_censuses.py tests/test_conftest.py` passed 5,378
  with 10 skipped, exit 0.
- `seal rules --check` exited 0 over 217 check lines in 69 rule files.
- `uvx ruff check` and `uvx ruff format --check` over the 99 changed
  Python files exited 0.
- `git ls-files hooks/` printed nothing.

At `e6e2003c`, `git archive HEAD | tar -t` lists `lib/` with its nine
modules and no path under `hooks/`. Also at `e6e2003c`, `bin/test tests/test_censuses.py` passed 215, exit 0, and
`uvx ruff check` and `uvx ruff format --check` over that file exited 0.
