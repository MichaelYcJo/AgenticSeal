# Phase 2: 1794142458-config-dir-readers

## What this phase found

**The frame holds for this phase.** `skills/verify/scripts/payload_meter.py`
and `tests/skills/test_payload_meter.py` did not change between
`b2a04d6d9` and `f6bbfb0f9` (executed: `git diff --stat b2a04d6d9
f6bbfb0f9` over the two files prints nothing). So the coordinates of
phase 2's row stood as the frame states them: the docstring at `:8` and
`:69`, the shadow at `:461` and `:464`, the pair at `:480`, `measure` at
`:761`, `imports_of` at `:369-400` and `main`'s `home` at `:1176` (read).
The module docstring's first paragraph is the one `main` hands argparse
(`__doc__.split("\n\n")[0]`, read), so the edits at `:8` and `:69` change
no `--help` text.

**The meter has a caller the frame does not name:
`.github/scripts/release_report.py#preloads`.** It loads `payload_meter.py`
by path from the last tag's tree and from this one, and calls
`composition(root, root, agent, definition, False)` with five arguments
(read: `:123-134`). The first build gave `composition` a required sixth
argument, and the phase boundary run failed 10 cases of
`tests/github/test_release_report.py` on a `TypeError` (executed). The
phase's first search for callers covered `tests`, `skills`, `lib`, `bin` and
`evals`, not `.github`, and under `git grep -E` on this machine its `\b`
matched nothing, so it listed not even the meter's own calls.
Run again as `git grep -n -P
'\b(composition|pair_rows|session_composition|user_dir|imports_of)\('`
over the whole tree, outside `seal/threads`, it lists that call and the
meter's own (executed).

**`user` is optional for `composition` alone.** `measure` computes
`user_dir(home, config)` once and passes the pair to
`session_composition`, `composition` and `pair_rows`, as `frame/design.md`
*Data & interfaces* says. `pair_rows` and `session_composition` take it
with no default, since `measure` is their one caller. `session_composition`
loses the default of `sections`, because a required argument cannot follow
it. `composition` defaults `user` to `user_dir(home, None)`, because the
release report calls the tag's meter and this one alike with five
arguments (commit `1711f3625`). The release report reads only the agent
share, so the default changes none of its figures. The docstring first
named the report by its path, and
`tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_every_cited_name_stands_in_what_the_archive_holds`
refused it, since `.github/` is not in the archive (executed). It names
the report in words since commit `e6652dacf`. Judged against
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a fact has
one source, and `user_dir` stays the one place that decides the directory.

**The cases stand in `Test_module`, beside the JSON case that runs the
script.** What they reach is `main`'s read of the variable, and only a run
through `run` reaches it. `run` gains `extra`, the variables added to the
child's environment. `two_user_dirs` builds `a_tree` with a config
directory beside its home. It rewrites the home's `CLAUDE.md` at 315
bytes, because `a_tree` writes it at 17 bytes, the size of `beta`'s
`SKILL.md`. S3's check that no row carries the home file's bytes would
otherwise fail on `beta`. `seal layout --pairs
tests/skills/test_payload_meter.py` names 4 pairs before the build and 4
after, all in `Test_imports_of` and none of them a new case (executed).

**Departure: S5 runs through `run` with the variable unset as well as
empty.** The S5 row gives the unset value to the existing in-process cases.
Those cases call `measure` with no `config`, so none reaches `main`. A
`main` that passed `os.path.join(os.path.expanduser("~"), ".claude")` as
the variable's default would label every row `$CLAUDE_CONFIG_DIR/…` on an
unset machine and leave them green. So the case is parametrized over
`[unset]` and `[empty]`, and the mutant below shows `[unset]` red. Judged
against `agents/crafter.md` *Mutation-test every unit that adds behaviour*.

**Departure: S6 does not pass against the old code.** The S6 row says it
does. The old meter never reads the config directory's `CLAUDE.md`, so the
case fails on its label line there. It was also shown red as the row asks.

**Seen red** (each executed):

- S3, `test_the_pair_reads_the_claude_md_of_the_config_directory_in_use`,
  red against `:480` as it stood. Its failing line is the label list, which
  read `~/.claude/CLAUDE.md` in the session's table.
- S4, `test_a_skill_shadow_is_read_in_the_config_directory_in_use`, red
  against `:461` and `:464` as they stood. The shadow read
  `~/.claude/skills/alpha/SKILL.md` at 514 bytes, against 616 expected.
- S5 `[unset]` and `[empty]` pass against the old code, which reads no
  variable. `[empty]` was shown red with `user_dir`'s `if config:` written
  `if config is not None:`, and the run named only `[empty]`. `[unset]` was
  shown red with `main` passing the variable with a default, as above, and
  the run named only `[unset]`. Each failed on the label line.
- S6, `test_an_import_from_home_stays_under_the_home_directory`, red with
  `pair_rows` handing `imports_of` the config directory in place of `home`.
  Its failing line is the bytes line: 91 bytes, the config directory's
  `shared.md`, against 69, the home's.

**Mutation runs, after commit `f10111fa6`** (executed, `seal mutate` over
`payload_meter.py`, each restored from its held bytes; `git status
--short` was empty after the runs):

- `user_dir`: `if config:` as `if config is not None:`, `"$CLAUDE_CONFIG_DIR"`
  as `config`, and the fallback's `".claude"` as `"claude"`. All three red.
- `main`: the variable read replaced by `None`, and the read given a
  default. Both red.
- `pair_rows`: the user file read under `home`'s `.claude`, its label fixed
  at `~/.claude/CLAUDE.md`, and `imports_of` given `directory`. All three
  red. As a control, the first of these against S4 alone `SURVIVED`, so S3
  is what watches the pair.
- `composition`: the shadow read under `home`'s `.claude`, and its label
  fixed at `~/.claude/skills/…`. Both red against S4.
- `composition`'s default, after commit `1711f3625`: `user = user or
  user_dir(home, None)` as `pass`, against
  `tests/github/test_release_report.py -k
  test_the_table_reads_this_tree_against_the_last_tag`: red.
- `tests/conftest.py`: the pop as `pass`, under an outer
  `CLAUDE_CONFIG_DIR`, against the whole of `tests/skills/test_payload_meter.py`:
  red, on `[unset]` and on the session JSON case.

**S7, for item 2** (executed: G2's second search on the tree at
`f10111fa6`, and again at `30f271afb` with the same five files). It lists
five lines, and none is the docstring, shadow or pair line of item 2. Two
are this module's code: `:440` at `f10111fa6`, `imports_of`'s `"~"`, and
`:1201`, `main`'s `expanduser("~")`, which is the home a `@~/`
import resolves against (G6). The other three are `session_cost.py:90`,
phase 1's fallback, `pact_check.py:613`, which *Scope* Out leaves, and
`skills/settle/scripts/settle.py:908`. That line refuses a path a record
names when it opens with `/`, `~` or `-`, and builds no path into Claude
Code's directory, so it is not in the class.

**S8, for `tests/skills/test_payload_meter.py`** (executed): under an outer
`CLAUDE_CONFIG_DIR` naming a scratch directory that holds a `CLAUDE.md`
and a shadow of `alpha`, `bin/test tests/skills/test_payload_meter.py
tests/test_conftest.py -q` passed 113 cases. Unlike phase 1's module, this
run can fail on the `conftest.py` pop (the last mutation run above).

**The conftest comment names both readers.** Phase 1's sentence named
`session_cost.py#projects_dir` as the one reader of the variable. It now
names `payload_meter.py#main` beside it, rewritten in place.

**The fragment carries a process row.** Phase 1's diff changes
`skills/verify/orchestration.md`. `docs/layout/the-record-layout.md` *A
change writes fragments, never a shared file* asks a fragment whose work
item changes a `skills/*/orchestration.md` file to end with `### Process
changes`. The row names that sentence. The version moves to `0.35.1` in the
commit that adds the fragment, `dfb42e4e2`, as `frame/plan.md`
*Operational impact* says.
