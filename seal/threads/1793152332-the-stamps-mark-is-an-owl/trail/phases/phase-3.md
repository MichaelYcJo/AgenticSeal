# Phase 3: 1793152332-the-stamps-mark-is-an-owl

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | cefb7abe |

## What this phase was asked

Build `frame/plan.md` row 3 and nothing of phase 4. Remove Pillow, because
no file of the tree reads it after phase 1. The row covers the pin and its
repair in `.github/scripts/run_tests.py`, the install lines of the two
workflows, `CONTRIBUTING.md` *Running the checks*, the census's `PIL.Image`
entry, and the cases that pinned the pin. `frame/design.md` *Removes* is the
list. Before removing, confirm with `git grep` that no module imports `PIL`.
The phase writes no new case, owes no red run for a removed case or a
removed Pillow half, and runs no `seal mutate`. One `bin/test` command closes
it.

## What this phase found

**No module imports Pillow.** `git grep -n -e "import PIL" -e "from PIL"` at
`ea1330ea` matched two lines. One is `frame/plan.md`'s own sentence quoting
the command. The other is the fixture string
`"from PIL import Image\nImage.open(p)"` in `tests/test_censuses.py`, which
is the census case this phase removes. No module imports `PIL`, so the frame
holds and the removal went ahead.

**What was removed, by file.**

- `.github/scripts/run_tests.py`: `PILLOW_VERSION`, `PILLOW` and their
  comment, `has_pillow`, `add_pillow`, the call in `main` with its comment,
  `PILLOW` in `PACKAGES` and the comment's clause on it, and the docstring
  paragraph. The next paragraph, on `cmarkgfm`, now opens "A second" instead
  of "A third".
- `.github/workflows/test.yml`: `pillow==12.3.0` from the install line, and
  the three comment lines on it.
- `.github/workflows/publish-release.yml`: `pillow==12.3.0` from the install
  line. The step is renamed `install the suite's packages`, and its comment
  no longer names Pillow.
- `CONTRIBUTING.md` *Running the checks*: rewritten in place for three
  packages, pytest, the parser and the renderer. `bin/test` now "acquires all
  three once". Both fallback commands lose `pillow==12.3.0`.
- `tests/censuses.py`: `PIL.Image` from `NOT_A_FILE_OPENER`, and the
  clause "with PIL's `Image` beside them" from the comment above it.
- `tests/test_censuses.py`: the parameter `PIL Image.open is binary`.
- `tests/github/test_run_tests.py`: the `pillow` argument of `fake_venv` and
  its docstring sentence, and the two cases
  `test_an_adopted_environment_is_given_the_pinned_pillow_once` and
  `test_a_failed_pillow_install_is_a_sentence_and_pytest_is_still_called`.
- `tests/behaviour/test_release_hygiene.py`: the row
  `("CONTRIBUTING.md", "12.3.0")`. The `cmarkgfm` row said its class was "the
  two rows above", and now says "the row above's".
- `tests/behaviour/test_a_release_publishes_its_note.py`: the
  install-before-draw order and its docstring sentence. The order existed
  because the draw imported Pillow. The count of five steps and the
  `apt-get` assertion stay.

**The Pillow halves were rewritten, not only dropped.** `frame/design.md`
S10 says the rewritten cases show that no install line and no fallback
command names Pillow. So four halves that asserted the pin is present now
assert that no word of the line starts with `pillow`:

- `test_ci_installs_the_parser_the_runner_pins` reads the pytest job of
  `test.yml`.
- `test_the_section_names_the_parser_and_where_it_is_pinned` reads
  `CONTRIBUTING.md`'s section, and the fallback commands are held to the
  parser's and the renderer's pins alone.
- `test_the_publishing_workflow_installs_the_pins_the_runner_holds` reads
  `publish-release.yml`.
- `test_a_fresh_build_installs_the_pinned_parser` reads the runner's
  install step.

The verification direction exempts a case that loses its Pillow half from a
red run, so none of the four absence assertions was seen red.

**One sentence beyond the list.** The docstring of
`tests/skills/test_seal_stamp.py#Test_module.test_imports_nothing_outside_the_standard_library`
said the hook loads the stamp module "where Pillow is absent". After this
phase no environment of the tree installs Pillow, so the contrast says
nothing. The docstring now says "where nothing beyond the standard library
is installed". `frame/design.md` *Removes* does not name this sentence. It
was reworded, and nothing was removed.

**The row's closing grep cannot match only the README.** `frame/plan.md` row
3 expects `git grep -n -i -e pillow -e 'import PIL' -e 'from PIL'` outside
`changelog/`, `CHANGELOG.md` and `seal/` to match only
`assets/seals/README.md`'s sentence on the previews. After this commit it
matches three other groups as well, and each one stays for a stated reason:

- `docs/branch-and-release.md` line 63 and `docs/release-checklist.md` line
  272 are in the policy root. The frame's `## Rule changes` holds their new
  wording for the settle to write, so this pull request does not edit them.
- `.test_durations` holds seven keys of removed cases. The plan's
  *Operational impact* leaves that file to the orchestrator's broad run.
- The four absence assertions above, and their comments, name `pillow`
  because S10 asks them to.
- `assets/seals/README.md` line 24 is the sentence the row expects.

**Existing cases relied on.** The rest of the modules below ran unchanged.
`tests/skills/test_seal_stamp.py`'s cases ran under the reworded docstring.

**The run.** One `bin/test` command ran 563 cases and exited 0: 561 passed
and 2 were skipped. It covered the six modules the row names, the modules
`git grep -l -i pillow -- tests` listed before the phase
(`tests/skills/test_seal_stamp.py` beyond the named six), and the test
modules `git grep -l run_tests -- tests` lists (`tests/hooks/test_launch.py`
and `tests/skills/test_arm_check.py` beyond those). It also ran
`tests/text/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`,
which reads the census table this phase changed. `uvx ruff check` and
`uvx ruff format --check` passed over the nine Python files the commit
changes. The modules that read `test.yml`, `publish-release.yml` or
`CONTRIBUTING.md` for other facts were not run. The orchestrator's broad run
answers them.
