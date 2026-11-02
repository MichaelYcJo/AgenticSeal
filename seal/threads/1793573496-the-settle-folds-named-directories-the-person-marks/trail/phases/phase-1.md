# Phase 1: 1793573496-the-settle-folds-named-directories-the-person-marks

## What this phase found

**The frame holds, with one sentence of the plan wider than the tree.** At
the base, `settle.py#main` runs from line 1056 and returns the settled line
before `survey` where the root holds no work item, as design G13 says.
`rule_changes.py#order` stands at lines 350 to 379 and reads the first `A`
line of each design. `SHIPPED` classifies `seal settle` as `PINNED`. The
plan's *Technical context* says each heading constant of `settle.py` is read
by `test_the_dry_runs_headings_say_who_decides`. That case reads four of them
(`GROUPS_HEADING`, `UNORDERED`, `ROWS_HEADING` and `JUDGMENTS_HEADING`), and
not `WHOLE_HEADING`, `MISPLACED_HEADING`, `REMOVES_HEADING` or
`READERS_HEADING`. The build is unchanged by it: the new `DOCUMENTS_HEADING`
joins that case, with the two phrases that say the session proposes and the
person marks.

**One departure from the frame: a working-tree change is read from `git
diff HEAD`, not from `git status`.** Design *Data & interfaces* and P1 name
`git status --porcelain -z`. That command prints a staged rename as two
fields, the new path and then its source. The first build consumed the
source field in a branch of its own, and no case could see that branch,
because a source path never names a listed document. A mutation of it would
have stayed green. `git diff HEAD --name-only -z --no-renames` answers the
same fact: a tracked path whose working tree differs from its last commit,
staged or not. It prints one path per field, so the branch is gone. The
listing prints what the design asks for. Judged against `agents/crafter.md`
*Mutation-test every unit that adds behaviour*, and `skills/core/SKILL.md`
*The rule a mechanism is kept against*: a script reads only a fact it reads
exactly.

**Decisions settled while writing the code**, each against design *Scope*
items 1 to 3:

- A file two named directories hold is listed under the first directory
  named that holds it. *Scope* item 1 says the file is listed once and does
  not say where. Argument order is the person's own, so the first directory
  named takes the file.
- A directory named twice is listed twice, and the second listing holds 0
  documents. The first build dropped a repeated name, and no case could see
  the difference, so that line went. The second listing is true as printed.
- The refusals are checked in this order: no directory in the working tree,
  then outside the repository, then the `seal/` root or a path under it. A
  path that does not exist outside the repository gets the first sentence.
  `--from` beside `--apply` is refused straight after the arguments are
  parsed, before the root is resolved, so nothing is read.
- A document no commit adds includes a file staged and never committed, as
  well as an untracked one. Both print `no commit adds it` and nothing about
  the working tree.
- `--from` at a directory above the `seal/` root, such as `--from .` at the
  repository's top, is accepted, and the listing then holds the root's own
  files. *Scope* item 2 refuses a path at or under the root, not one above
  it. The build follows the frame. `gaps.md` *Not done* holds what was left.

**Each new case was seen red at the base before the code was written.** One
command ran the 22 cases its `-k` selected against the tree at `777a8d197`.
13 failed. The cases for A2 to A6 failed on argparse's exit 2 for the unknown
`--from`, and the cases for A1 and the heading failed on `AttributeError` for
`DOCUMENTS_HEADING`. Each refusal's own sentence is held by the mutation runs
below, not by that first red. A2 later gained a staged file that no commit
adds, which `ls-files` prints after the untracked one. Its pin on the path
order was seen red by mutating the sort.

**`seal mutate` turned each unit that adds behaviour red, one run each, at
`0a45cebf7`, and the settled-root unit again at `8578438c1`:**

| Unit | Break | Cases |
|---|---|---|
| `named_directory`, no directory | `if not os.path.isdir(path):` to `if False:` | `-k refuses_a_from` |
| `named_directory`, outside | `if not inside(path, top):` to `if False:` | `-k refuses_a_from` |
| `inside` | `return os.path.commonpath([path, top]) == top` to `return True` | `-k refuses_a_from` |
| `named_directory`, the root | `if inside(path, os.path.realpath(home)):` to `if False:` | `-k refuses_a_from` |
| `main`, the pair | `if args.named and args.apply:` to `if False:` | `-k refuses_from_beside_apply` |
| `history`, the last change | `last[field] = commit` to `last.setdefault(field, commit)` | `-k gits_order` |
| `history`, the last add | `if status == "A":` to `if status:` | `-k gits_order` |
| `history`, the status field | `field = field.lstrip("\n")` to `pass` | `-k gits_order` |
| `history`, the commit field | `commit = field[1:]` to `commit = None` | `-k gits_order` |
| `changed` | its return to `return set()` | `-k gits_order` |
| `documents`, once | `if p and p not in seen:` to `if p:` | `-k listed_once` |
| `documents`, commit order | `key=lambda p: added[p][0]` to `key=lambda p: p` | `-k gits_order` |
| `documents`, path order | the `sorted` of the undated paths to a list | `-k gits_order` |
| `write_documents`, the change | `said = f"  {CHANGED}" if touched else ""` to `said = ""` | `-k gits_order` |
| `main`, the settled listing | `write_documents(listed, sys.stdout)` to `pass` | `-k root_with_no_work_item` |
| `main`, the dry run's listing | `found["documents"] = listed` to `pass` | `-k gits_order` |
| `report`, the block | `if "documents" in found:` to `if False:` | `-k gits_order` |
| `main`, the read | `listed = documents(root, named) if named else None` to `listed = None` | `-k 'gits_order or root_with_no_work_item'` |

Each run printed `red: the cases failed against the mutation (exit 1)` and
exited 0. Each ran `bin/test tests/skills/test_settle.py -p no:xdist -q -k
<cases>`.

**A5 reads the settled line by its words, not by its root.** `main` takes
the root from `git rev-parse --show-toplevel`, which spells it with forward
slashes on Windows, and CI runs the suite on `windows-latest`. A case that
matched `SETTLED.format(root=str(repo))` exactly would fail there for a
reason that is not the behaviour. The case holds the listing exactly, then
the settled line's opening and words, and the line count.

**The phase-boundary set ran green in one command at `8578438c1`**, exit 0,
962 passed and 8 skipped: `tests/skills/test_settle.py` and
`tests/behaviour/test_a_reference_root_is_read_and_never_taken.py`, the
plan's row, with every module that reads, imports or globs a changed path:
`tests/text/test_settle_reads_before_it_removes.py`,
`tests/behaviour/test_unverified_rows_close.py`,
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`,
`tests/skills/test_seal.py`,
`tests/behaviour/test_a_release_is_sized_by_a_criterion.py`,
`tests/behaviour/test_no_document_names_the_old_roots.py`,
`tests/behaviour/test_release_hygiene.py`,
`tests/behaviour/test_the_old_block_leaves_through_update.py`,
`tests/hooks/test_launch.py`, `tests/test_censuses.py`,
`tests/behaviour/test_the_release_check_watches_what_ships.py` and
`tests/github/test_rules.py`. The list came from `grep -rl` over `tests/`
for the script's path and for the modules that walk `skills/` or every
tracked file. It is a sample of the readers, and the broad gate is the
whole.

**For phase 2.** The new heading points at `skills/settle/SKILL.md` for the
procedure, which phase 2 writes. `settle.py`'s module docstring and the
`--from` help name the flag. The skill's usage block and the two README rows
do not name it yet. `questions.md` Q1 is built on its default (a): no case
drives a settling session.
