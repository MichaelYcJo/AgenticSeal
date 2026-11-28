# Phase 2: 1795841830-find-leftovers-before-a-round

## What this phase found

**The frame holds, with one departure.** The crafter opened every coordinate `frame/plan.md` *Technical context* names for this phase and the fold's additions read at `d216647a`, and each named the text the design describes (`read`). The departure stands in a frame line the crafter does not write, so it goes to the orchestrator in the hand-back as well, judged against `skills/implement/SKILL.md` *The frame is judged before it is built to*.

- `frame/design.md` *Data & interfaces* *The range file and a keep file* has a keep file print "the lines `git diff` prints for it with the command's `DIFF` options, `-U0` and `--inter-hunk-context=0`, unwidened". `git diff -U0` writes a function line after each hunk header, and with no diff driver set that line is the nearest earlier line that opens with a letter, `_` or `$`: in a keep file, a kept line the range did not change. The design's scenario *A phase that changes one keep line meets that line alone in its range file* asks that the range file print "none of the file's other lines". So the keep branch prints each hunk header with no function line after it, as the branches for `.md` and other text paths print the headers they build. The case's first assertion fails on that function line where the header is printed as git gives it (`agentic mutate`, below).

**Decisions of the build.**

| Decision | Grounds | Judged against |
|---|---|---|
| `lib/optin.py#KEEP` is the compiled pattern `frame/keep-[0-9]+(?:-paths)?\.txt`, matched whole against the path after the work item's directory, and `optin.py` imports `re` for it | the design asks one constant beside `FRAME` for the names' shape; a phase's number is digits, so a name with no number, such as `frame/keep-notes.txt`, is another text path | `frame/design.md` *Data & interfaces* *The range file and a keep file* |
| The keep branch of `range_read.py#_read` stands after the checks for a deleted, a submodule and a binary path, and before the `.md` branch | the design puts it before the branch for other text paths, and keeps a deleted keep file `DELETED`; a keep file git reads as binary has no lines to print | the same section |
| A keep file's hunk header prints with no function line | the departure above | `frame/design.md` *User scenarios & acceptance*, its fifth row |
| The paragraph on suites stands below the table of *Scope: cheap and often, broad and once*, after the paragraph on the tree-wide test files, opened by a bold sentence | Scope item 6 puts it below the table; the paragraphs before it say which files join the set, and this one says which command runs each | `frame/design.md` *Scope* item 6 |
| The framer's rule on suites stands in `agents/framer.md` *Rules* after the rule on searches in a cell | both rules govern what a *Verified by* cell states | `frame/design.md` *Scope* item 7 |
| The paragraph on separate work items stands in *Under agentic* after the list of rows, before the three combinations | the split is weighed before `routing.md` is written, as each row is | `frame/design.md` *Scope* item 9 |
| The records' overview writes `frame/keep-N.txt, frame/keep-N-paths.txt` with a bare `N` | the overview writes `phase-N.md` and `round-N.md` the same way | `frame/design.md` *Scope* item 13 |
| `tests/skills/test_range_read.py` *Test_main* `test_accepts_a_local_root_reading_the_records_on_disk` now commits a change to `f.txt` and holds that it prints under the head line of other text paths | with no change in its range, the case reached no path, and `agentic mutate` that took `rel is None` out of `_keep` survived; with the change, the same break raises `TypeError` in `_keep` | `skills/implement/SKILL.md` *Mutation-test every unit that adds behaviour, one command each*; contract rule 15 |

**The case of Scope item 12, seen red.** `test_accepts_a_keep_file_of_the_work_item_at_its_own_lines` was run against `range_read.py` and `lib/optin.py` as `d216647a` holds them, in a `git clone --no-local` checked out at `d216647a` with the case copied in, and failed on `assert line + "\n" not in own` with `docs/file-1.md:a kept line 1` printed under the keep file's path (`executed`). The line is the case's guard: a kept line the range did not change.

**`agentic mutate`, one break each, `--tests "bin/test tests/skills/test_range_read.py -q -k keep_file -p no:xdist"`, at `f2fdd58f`** (`executed`):

- `elif _keep(path, rel):` to `elif False:`: red.
- the hunk header's function line kept: red.
- `not path.startswith(rel + "/")` to `False`: red, since the other work item's directory name is as long as this one's.
- `optin.KEEP.fullmatch(...) is not None` to `True`: red, by `frame/keep-notes.txt`.
- `(?:-paths)?` removed from `lib/optin.py#KEEP`: red.
- `keep-[0-9]+` to `keep-[^/]+` in `lib/optin.py#KEEP`: red.
- `-U0` to `-U3` in `_own_lines`: red.
- `KEEP_HEAD`'s text shortened: red, since the case spells the head line.
- `if rel is None or not` to `if not`, with `-k 'keep_file or local_root'`: survived at `f2fdd58f`; red at `d16a7f37`, after the local-root case above.

Three breaks survived at `5f023ef3`, before `f2fdd58f` widened the case: the prefix check, the name check, and the head line's text, which the case then read from `RANGE.KEEP_HEAD`.

**The other test files that open a file this phase changed.** `tests/skills/test_agentic.py` copies `templates/setup/agentory-README.md` into a root (line 3211) and hands `agentic range` to `range_read.py` (line 3729); `tests/lib/test_optin.py` opens the same template and loads `lib/optin.py`; `tests/lib/test_gaps.py` opens `skills/implement/SKILL.md`, as phase 1 found. The list came from `git grep -l` over `tests` for `optin`, `range_read`, `agentory-README`, `follow-up.md` and the changed skill and agent files' names, with `tests/text/` and `tests/behaviour/` filtered out, and each hit was read (`executed`). The others name a changed path without opening it: `tests/conftest.py` line 1206 and `tests/skills/test_agentic.py` write `follow-up.md` into fixtures, `tests/github/test_release_mark.py` line 586 holds it in a fixture string, `tests/skills/test_chain_check.py` line 4535 names the marker `fix-pass-two-lines`, and `tests/skills/test_session_cost.py` line 768 is a comment. The list is a sample by contract rule 12: a case that reaches a changed file through a glob, with no spelling of its path, is outside it, and the tree-wide files the set runs are the ones that glob the tree.

**`lib/optin.py` is loaded by every test file, and the set does not run every one.** `tests/conftest.py` line 459 loads it, so every test file loads it through another test file. The change adds a constant and an import, which move no result of a case that reads neither. Every file of the set loads `conftest.py`, so the set holds the import, and the cases that read `KEEP` are in `tests/skills/test_range_read.py`. Every file that loads `conftest.py` is the whole suite, which is the broad gate's (contract rule 2). Judged against `skills/verify/SKILL.md` *Scope: cheap and often, broad and once*, its sentence that a file whose result the change cannot move does not read the path.

**What the phase verified.**

- The set, as the *Verified by* cell names it with the files above: `bin/test tests/text tests/behaviour tests/skills/test_range_read.py tests/lib/test_optin.py tests/skills/test_agentic.py tests/lib/test_gaps.py -q`. At `e1ba1218`, before this record and the corrections of `a3c135ba`, it printed `1447 passed, 10 skipped, 1 warning`, the warning about `skills/code-review/SKILL.md:263`, a file this work does not change (`executed`). The run after this record is committed is the hand-back's.
- `uvx ruff check` and `uvx ruff format --check` over `lib/optin.py`, `skills/implement/scripts/range_read.py` and `tests/skills/test_range_read.py` passed at each commit that changed them (`executed`).
- `diff templates/setup/agentory-README.md agentory/README.md` printed nothing and exited 0 at `a3c135ba` (`executed`).
- `S3` of `frame/design.md` *Data & interfaces* *The searches* printed nothing and exited 1 at `a3c135ba`; at `63b9bfed` it printed `agents/crafter.md:62`, `skills/implement/SKILL.md:203`, `skills/implement/fix-pass.md:97` and `skills/verify/SKILL.md:199`, which shows that it can fail (`executed`). `S1` and `S2` still print nothing (`executed`).
- The phase's prose in `agents/` and `skills/` adds no behaviour a case holds, so it writes no case for it (`frame/design.md` *Out*); the tree-wide files of the set parse those files.
- This frame keeps no line, so the phase wrote no line of a keep file (`frame/design.md` *Data & interfaces* *The searches*).
- The suites of this phase's set: `bin/test` alone. The eval harness owns no file of the set (G12).
