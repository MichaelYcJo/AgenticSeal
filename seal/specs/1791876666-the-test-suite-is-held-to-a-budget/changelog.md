### Changed

- **Every `bin/` command but `bin/test` refuses a Python older than 3.12 the
  same way, before it reads anything (#929).** Six commands — `round-record`,
  `settle`, `fold-check`, `broad-gate`, `payload-meter` and `seal-stamp` —
  each carried its own copy of that refusal, and eight others ran on
  whatever `python3` they found. All fourteen wrappers and their `.cmd` twins
  now run their script through one launcher, `hooks/launch.py`, which holds
  the floor once. Below 3.12 it prints the sentence the six printed: the
  floor, the version and interpreter it found, *Nothing was read and nothing
  was written*, and the hint that macOS ships python 3.9 as `python3`. Then
  it exits 2 before the script is read. At or above the floor the script
  runs exactly as if it had been run directly. `bin/test` still starts on
  any `python3`, because its runner is what builds a virtualenv at the floor
  from an older one. The plugin's hooks do not go through the launcher, so a
  hook on an older `python3` behaves as before.
  (`1791876666-the-test-suite-is-held-to-a-budget`, #929)
- **The Stop hook draws the sealer's stamp on a `python3` older than 3.12
  too (#929).** The hook loads `seal_stamp.py` in its own process, and that
  file's copy of the floor check made it draw nothing there. The copy is
  gone with the others, so a 3.9 `python3` draws the same stamp 3.12 draws.
  Where `python3` cannot load the file at all, the hook still draws nothing
  and says nothing.
  (`1791876666-the-test-suite-is-held-to-a-budget`, #929)

### Added

- **A new or changed test case has to prove itself on the pull request
  (#929).** A `cases` job in the test workflow runs
  `.github/scripts/case_check.py` against the base branch. For each test
  function the pull request adds or changes, it draws up to twelve mutants:
  from the lines the case runs and its siblings do not, the units of its own
  file it names, and the shipped lines the pull request changed. Under each
  mutant it runs the cases that ran that line. A case passes when it is its
  file's only killer of at least one mutant; otherwise the job names it and
  fails. Mutants of changed code that no case kills are listed and fail
  nothing. The proof is bounded at five minutes, and a file whose proof
  would take longer is named with `restructure: test the decision directly`.
  Nothing is annotated by hand, and `CONTRIBUTING.md` says what a case owes.
  `mutation-check --baseline-passed` skips the run against the unmutated
  file for a caller that has already run it; a call without it is unchanged.
  (`1791876666-the-test-suite-is-held-to-a-budget`, #929)

### Fixed

- **On Windows, `mutation-check` and `arm-check` kept a `--tests` command's
  backslashes (#929).** The command line was split as POSIX shell words, so
  an interpreter's path such as `C:\hostedtoolcache\...\python.exe` lost its
  separators and could not start. A backslash is a path separator there now.
  (`1791876666-the-test-suite-is-held-to-a-budget`, #929)

### Removed

- **The commit-gate test file replays 35 sampled shapes instead of 226
  (#929).** Its S2 case ran every row of the shape corpus against an
  undeclared repository, though the hook sees the commit and not the shape.
  It now runs `SAMPLE`, one or more representatives of each corpus subgroup.
  A sampled row that commits nowhere fails instead of skipping, and a case
  fails when a subgroup has no sampled row. A table of five mutations of the
  gate, the stub installer, the lease reader and the stub's shell shows each
  still caught after the cut. The file holds 178 cases where it held 367, and
  its price in `.test_durations` fell from 1,334 to 441 Windows seconds. The sealer
  file's six corpus layouts that differed from a kept twin only by a junit
  option leave with their 12 ids, and so do the floor-guard cases the
  launcher replaced. 227 ids leave `.test_durations`. The interpreter census
  over every shipped file gives way to one over the code that runs before any
  floor is checked: the hooks, the git hooks, the launcher, `bin/test`'s
  runner and every module they load, which `ruff.toml` now lints at Python
  3.9, so the linter no longer asks that code for a `zip(strict=)` or a
  `datetime.UTC` its `python3` may lack.
  (`1791876666-the-test-suite-is-held-to-a-budget`, #929)
