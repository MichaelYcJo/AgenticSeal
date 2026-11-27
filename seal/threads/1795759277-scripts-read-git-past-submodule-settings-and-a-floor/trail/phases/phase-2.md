# Phase 2: 1795759277-scripts-read-git-past-submodule-settings-and-a-floor

## What this phase found

**The frame holds for this phase.** `skills/implement/scripts/range_read.py#_commit` passes `--end-of-options` to `rev-parse`, `README.md` and `README.ko.md` state what a person installs in the paragraph after the install block, and `tests/behaviour/test_release_hygiene.py#test_the_python_floor_is_the_same_number_everywhere` holds the Python number in both editions (read). Two places in the frame read otherwise than the build:

- *Data & interfaces* says `_read` asks `older` before `_commit`, and *Scope* item 5 and S7 say before the first git command, with no `rev-parse` started. `_read` calls `_work_item` before `_commit`, and `_work_item` starts `git rev-parse --show-toplevel` through `lib/optin.py#repo_root` (read). The ask stands at the head of `_read`, before `_work_item`, and asks `older(cwd)`, since `git version` needs no repository. That place is before `_commit` too, so it meets both sentences. The case `test_refuses_a_git_older_than_the_floor_before_its_first_read` asserts that `version` is the one command started, and the mutation that moves the ask after `_work_item` makes it fail (below).
- S6's *Verifiable how* says the refusing case is seen red with the comparison removed. Removing the comparison refuses every version, so the refusing cases still pass and the accepting cases fail. The refusing cases were seen red with the comparison turned round, and the accepting cases with it removed (below).

**Decisions settled while writing the code**, each judged against `frame/design.md` *Data & interfaces* unless the entry names another document:

- `lib/gitcmd.py#VERSION` is `git version ((\d+)\.(\d+)\S*)(?: .*)?`, matched against the whole first line. The version `older` names is the token after `git version `, so `2.39.2.windows.1` is named whole and ` (Apple Git-155)` is not part of it.
- The major and minor numbers are compared as one version against `OLDEST`. The case `a-higher-major`, `git version 3.0.0`, holds it: a comparison of the minor number alone refuses it.
- `older`'s line is `git <version> answers here, and the plugin's scripts need git 2.30 or newer`, and `seal range` prints it after `seal range: `, as it prints its other refusals. `tests/lib/test_gitcmd.py#Test_older` and the S7 case pin the text, as contract rule 14 asks.
- The README sentence reads `` You need `git` 2.30 or newer, `` and `` `git` 2.30 이상과, ``. The S8 case looks for `` `git` 2.30 `` in each edition, so a `2.30` elsewhere in the file does not satisfy it. The English sentence after it now says the `seal` commands are Python scripts that start `git`, which gives the reader the reason both requirements stand together. The paragraph was re-wrapped.
- `older`'s case on the suite's own git, `test_accepts_the_line_the_git_running_the_suite_prints`, matches the real first line against `VERSION`, since a None from `older` alone would also stand for a line `VERSION` does not read.

**Seen red.** Before the code changed, every new case of `Test_older` failed on `AttributeError: ... has no attribute 'older'`, the S7 case failed at `assert code == 2` because `seal range` wrote its file, and the S8 case failed on `has no attribute 'OLDEST'` (executed). Then `seal mutate` ran each mutation as one command over `b68bb5455`, and each line number below is that commit's (executed):

- The `>= OLDEST` test and its `return None` taken out: `red`. Each parameter of `test_accepts_a_git_at_the_floor_or_newer` failed at line 706, `assert gitcmd.older("/r") is None`.
- `>= OLDEST` turned into `< OLDEST`: `red`. Both parameters of `test_refuses_a_git_older_than_the_floor_naming_both` failed at line 684, the assertion of the line.
- The comparison of both numbers replaced by `int(found.group(3)) >= OLDEST[1]`: `red`. `a-higher-major` failed at line 706.
- `VERSION.fullmatch` replaced by `VERSION.search`: `red`. `another-program` failed at line 724.
- `if done.returncode or not found:` replaced by `if not found:`: `red`. `a-non-zero-exit` failed at line 724.
- The ask taken out of `_read`: `red`, at `tests/skills/test_range_read.py:570`, `assert code == 2`.
- The ask moved after `_work_item`: `red`, at `:577`, the assertion that `version` is the one command started.
- `` `git` 2.30 이상과 `` changed to `` `git` 2.29 이상과 `` in `README.ko.md`: `red` for `test_the_git_floor_is_the_same_number_everywhere`, at `tests/behaviour/test_release_hygiene.py:1042`.

**Under git 2.39.3 and git 2.30.** `PATH=/Library/Developer/CommandLineTools/usr/bin:$PATH bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py -q -p no:xdist` printed `104 passed` at `32706b4a9` (executed). The cases of `Test_older` and the S7 case supply what `git version` printed, so none of them starts a git older than the one on `PATH`. What git 2.30 itself does with the commands of the scripts was not run, as `frame/questions.md` Q1 and `gaps.md` hold.

**What building found.** The first boundary run failed `tests/behaviour/test_every_tracked_file_meets_every_census.py::test_every_file_no_module_file_declares_meets_every_census` (executed). The case on the suite's own git started `subprocess.run(text=True)`, which reads in the locale's encoding, cp1252 on the Windows leg. `32706b4a9` names `encoding="utf-8"`, and the census then passed (executed). `119383781` changes two docstrings of the phase's cases, and `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py -q` printed `104 passed` over it (executed).

**The phase boundary set.** `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py tests/github/test_publish_release_note.py $(cat readme-readers.txt) tests/text tests/behaviour -q` printed `3050 passed, 11 skipped` at `32706b4a9`, with this record and `changelog.md` on disk (executed). `readme-readers.txt` lists each test file outside `tests/text` and `tests/behaviour` whose text holds `README`, by `git grep -l -e 'README' -- tests ':!tests/text' ':!tests/behaviour' ':!tests/conftest.py' ':!tests/censuses.py'`, a search by one word and so a sample. `tests/github/test_publish_release_note.py` reads the changelog fragments. `older` is called by `range_read.py` alone at `32706b4a9`, by `git grep -n 'older(' -- lib skills hooks .github evals bin` (executed), so no other script's test file reads it.
