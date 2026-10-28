# Phase 1: 1793140810-each-directory-holds-everything-in-one-level

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 8fcc543b |

## What this phase was asked

Build `frame/plan.md` row 1 and nothing of phases 2 to 5:

- the census `tests/censuses.py#vacated_paths`, joined to `CENSUSES`, with
  its cases in `tests/test_censuses.py`;
- `templates/` moved by `git mv` into `templates/records/` and
  `templates/setup/`, as `frame/design.md` sets them;
- every reader of a template path at its new path: the code joins,
  `install.sh`, the `$CLAUDE_PLUGIN_ROOT` paths, the gate messages and the
  tests that pin them, and every prose citation;
- `docs/README.md`'s table grouped into one table per subject, with every
  row unchanged (`frame/questions.md` Q1's default).

Records that keep the old path stay as they are. The census is the one new
behaviour. It is seen red once, against the template citations after the
move and before their sweep, and then green. A moved path owes no new case,
no red run and no `seal mutate`. The phase ends with one `bin/test` command
over the row's named modules and the modules `git grep -l templates` finds.

## What this phase found

**The frame holds, with three readers it did not list.** Three readers
build their file set from `templates/` one level deep. After the move each
one matched nothing:

- `.github/scripts/rules.py#RULE_FILES` globbed `templates/*.md`. No
  template holds a `check:` line today, so that glob would have shrunk
  without failing.
- `tests/test_the_record_is_written_in_words.py#CORPUS` globbed the same
  pattern. It asserts that each pattern names a file, so it would have
  failed.
- `tests/test_a_record_carries_no_comment.py#templates` globbed
  `templates/sdd-*.md` and `templates/process.md`. It asserts nine files, so
  it would have failed.

The first two now read `templates/*/*.md`. The third reads
`templates/records/*.md`, because that directory is now exactly the record
templates. Its fixture puts `config.md` under `templates/setup/`.

**Decisions taken while writing the census.**

- It lists the subdirectories on disk, not `git ls-files`. The design says
  "each tracked file". The disk listing keeps the cases free of git, as
  every other census's cases are. An untracked file in a subdirectory
  vacates its spelling too. The only such file met here is `.DS_Store`, and
  no line spells `templates/.DS_Store`.
- A spelling counts as a path's start where a shell variable stands before
  it, so `$CLAUDE_PLUGIN_ROOT/templates/config.md` is refused. Any other
  longer path is not refused. One such citation stood in the tree,
  `~/.claude/plugins/marketplaces/agenticseal/templates/claude-md-block.md`
  in `skills/update/SKILL.md`. It was found by `git grep` and rewritten.
- A path cited at a commit passes in any form, `<commit>:<path>`, not only
  the `seal/specs/` form `HISTORY_PATH` reads.
- No file needs to keep a vacated `templates/` spelling, so the census has
  no kept-files constant yet. Phase 2 adds it with
  `hooks/lib/cmdline_base.py`, which is the first file to need one.

**The census pins the changed messages.** The gate messages in
`hooks/routing-edit-gate.py` are pinned by `tests/test_routing_edit_gate.py`.
`seal.py#NEW_CONFIG` is the comment `seal mode` writes into a new
`seal/config.md`, and no case pins its text. The census refuses
`templates/config.md` over `seal.py` through `test_seal.py`'s
`census_case`, so reverting the message to the old path fails. The same
holds for `install.sh`'s two error messages, through the sweep.

**The red, and the green.** The four new cases of `Test_vacated_paths`
failed before the census existed, with `AttributeError`. After the
`git mv`, the census found 231 lines in 75 files. Those 231 lines were
measured by running `vacated_paths` over every tracked file. Once the sweep
finished it found none, and the four cases pass.

**Two failures predate this phase, and this phase cannot answer them.**

- `tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census`
  fails on `frame/plan.md:87`, which writes a real user path that
  `real_identifiers` refuses. The line has stood since the frame's commit
  `1e983c72`. The phase's writes do not include that line.
- `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`
  fails because the thread has a frame and no `gaps.md`. The thread had
  none at `498b8c41` either.

**`docs/README.md`** holds four tables in #1060's order: the process, the
records, the agents and the review, the checks. #1060 names no place for
`the-routing-check.md` and `the-session-hooks.md`, so both go under the
checks. `seal fold`'s index reader reads every table, which is why
`test_fold_check.py` stays green.

**New case:** `tests/test_censuses.py::Test_vacated_paths`, four cases.
**Existing cases relied on:** the 58 modules of the narrow run. They are
the row's seven named modules, `tests/test_rules.py` for `RULE_FILES`,
`tests/test_mode_gate.py`, and every test file `git grep -l templates`
lists.
