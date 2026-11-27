# Phase 1: 1795742080-a-session-is-bound-by-the-crafters-rules

## What this phase found

**The frame holds for this phase, with two places it does not name.** `skills/implement/scripts/seal.py#TOOLS`, the list of tools in `tests/skills/test_seal.py`'s `Test_main`, and `lib/gitcmd.py#argv` and `#git` stand where `frame/design.md` G7 and `frame/plan.md` *Technical context* put them (read). The two places:

- `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py#SHIPPED` classifies every `seal` subcommand `seal.py#TOOLS` names, and its case `test_every_shipped_command_is_classified` goes red on one it does not classify. The phase adds the row for `seal range`, which walks no `specs/` directory. The row was seen red by `seal mutate` renaming it to `seal ranged` (executed).
- *User scenarios & acceptance* S6 says an uncommitted path is named "as not printed", and *Data & interfaces* says it is named "as not read". The command builds to *Data & interfaces*: the file prints HEAD's text of such a path, so what it misses is the change on disk, which it did not read.

**Decisions settled while writing the code**, each judged against `frame/design.md` *Data & interfaces* unless the entry names another document:

- In local mode the records are read on disk, under a line that says the root is local. *Data & interfaces* reads the records "whole as HEAD holds it", and refuses only an `<item>` that is not under a marked root. The local root is marked (`skills/core/SKILL.md`, its opening paragraph) and no commit holds it, so the records exist only on disk.
- A rename is read with `--no-renames`, as the old path deleted and the new path added. *Data & interfaces* names a deleted path and gives a rename no form of its own, and this reading prints every line of the new path.
- A `.md` path's print opens with the header lines `git diff -U0` gives it, then each hunk widened to its paragraph under a hunk header in git's form, with the `-` and `+` lines in place. Hunks whose paragraphs meet print as one. A reader then sees what changed beside the paragraph around it. A `.md` path HEAD holds empty prints git's own hunks.
- The summary names a record HEAD does not hold as `not printed: <path>, absent`, since *Data & interfaces* asks for each path the command named and did not print.
- Each tracked path with a change no commit holds, staged or not, is named, read from `git status --porcelain=v1 -z --no-renames --untracked-files=no`. An untracked file is not named.
- Every `git diff` runs with `--no-color`, `--no-ext-diff`, `--no-textconv` and `--no-renames`, the `-U0` read with `--inter-hunk-context=0`, and every pathspec is read literally. The grounds are `docs/running/what-a-script-gates.md` *Which gate a script holds*: a script reads git the same under any configuration. The cases run under a configuration that sets each of those against the command.
- A file that cannot be written ends at exit 2 with its own line. The exit list of *Data & interfaces* does not name it, and the command writes nothing in that case.

**What building found.** A `.md` path emptied at HEAD printed its deleted lines without the hunk header git gave them. The case on an emptied file went red on it, and `18c7a48f2` fixed it.

**Seen red.** Each case of `tests/skills/test_range_read.py` was first run against the tree without the script, where collection fails (executed). Then `seal mutate` ran 36 mutants over `skills/implement/scripts/range_read.py` in one call, at `7efa46e24`, each against `bin/test tests/skills/test_range_read.py -q -x -p no:xdist` (executed):

- Mutant 1 put a print of `git diff -U3` in place of the paragraph print, as S4 asks, and read `red`.
- Mutants 2 to 4 removed the bound backward, the bound forward and the joining of hunks whose paragraphs meet. Mutants 6 to 8 broke a header's zero count, its one-line count and the offset a hunk after a deletion carries. All read `red`.
- Mutants 9 to 14 removed each switch against the configuration, and mutants 15 to 19 the binary, deletion, uncommitted, untracked and staged-rename readings. All read `red`.
- Mutants 20 to 24 removed the ancestor refusal, the refusal of a commit that does not resolve, the work-item check, the local-mode branch and the absent-record branch. Mutants 25 to 36 broke the range line, the line count, the `-W` print, the emptied-file branch, three entries of `RECORDS`, the blank-line test, the final-LF trim, a hunk's default count, the local absent line and the ancestor call. All read `red`.
- Mutant 5 read `SURVIVED`. It numbered a deletion that opens the file from line 0. `b6997dc65` added a deletion of the file's first line to the case of deleted lines, and the same mutant then read `red` (executed).

The path in `seal.py#TOOLS` read `red` against the `range` row of `tests/skills/test_seal.py` (executed).

**What the next phase needs.** The command line a builder types is `seal range <item> --from <commit> --out <file>`, and `--from` takes any name `git rev-parse` resolves to a commit. A local-mode item's records print under `ON_DISK`. Phase 2 cites the subcommand in `skills/implement/SKILL.md`. Once a shipped document names `range_read.py` or `seal range`, `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py` reads that document.
