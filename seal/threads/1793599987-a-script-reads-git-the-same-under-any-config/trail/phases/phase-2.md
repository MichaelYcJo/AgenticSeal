# Phase 2: 1793599987-a-script-reads-git-the-same-under-any-config

## What this phase found

**The frame holds for this phase.** The six readers `frame/design.md`
*Scope* item 4 names stand where it says, and each split git's output on
newlines without `-z` (read). A search of the shipped scripts for the
literal argv words that list paths (`"ls-tree"`, `"ls-files"`,
`"--name-only"`, `"--name-status"`, `"--porcelain"`, `"diff-tree"`,
`"status"`) found these six and nothing else that takes a path out of the
output and splits it on newlines (executed). The rest already pass `-z`, or
check only whether git printed anything, or print a line without taking a
path out, which *Scope*, Out, leaves as they are. That search is a sample:
a word passed in a variable is not listed. The framer's `ast` walk of 60
calls is the whole list this phase stands on.

**`rule_changes.py#order` marks a commit with U+0001, not NUL.** Under `-z`
a NUL ends every path, so the old `--format=%x00%H` could no longer tell a
commit from a path. The reader now asks for `--format=%x01%H` and reads
the output as `settle.py#earlier_judgments` does: split on NUL, strip the
newline that opens the first path after a commit, and take a field that
opens with U+0001 as the commit. Judged against `frame/design.md` *Scope*
item 4 and #1281's reading in `settle.py#earlier_judgments`, so the two
readers of one shape parse it one way.

**`publish_release_note.py#fragments` splits on NUL alone.** With
`--format=` and `-z`, git prints the paths of every commit NUL-ended, with
no newline between commits. A probe over a scratch repository with a merge
and a non-ASCII directory showed this (executed), so the reader strips
nothing. Only the first `log` in `fragments` changed. #1299 edits the
header helpers of the same file, and this phase touched nothing else in it.
In `tests/github/test_publish_release_note.py` the one change is a new case
in `Test_module`, placed after the case that already calls `fragments`
directly.

**`unverified_check.py#tree_at` drops the empty field after the last NUL.**
`splitlines()` returned none for it, and the disk branch returns none, so
the two branches still list the same paths. The empty field does no harm in
`released`, `overviews_at`, `_moved_main` and `fragments`, because no
prefix, file name or pattern there matches an empty string.

**Each `# exempt from splitlines: git output` above a changed reader is
gone.** `tests/censuses.py` refuses an exemption above a line the census
does not flag, and none of these lines calls `splitlines` now.

**Where each case went.** Each new case went into the group of the function
it covers, as the crafter's definition asks:

- `released` has no `Test_released`. Its cases are the dry-run cases of
  `tests/skills/test_settle.py#Test_report`, such as
  `test_an_unreleased_work_item_is_not_a_candidate`, so its case is there:
  `test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate`.
- `rules.order`'s cases are `Test_module`'s merge-order cases in the same
  module. The new one is
  `test_merge_order_of_an_id_that_is_not_ascii_is_its_designs_add`.
- `tests/skills/test_unverified_check.py#Test_overviews_at` and
  `#Test_tree_at` each gained one accepts case, over a one-commit
  repository whose id is `NON_ASCII`.
- `tests/skills/test_test_layout.py#Test_moved::test_accepts_a_pure_move`
  gained one row. Its module-scoped base gained two files,
  `tests/test_정렬.py` and a case that imports from it, and no other row
  names either file.

`seal layout --pairs` over the four modules read 4 files and found 0 pairs
(executed).

**Seen red against `5dc1f37e` (executed).** The four test modules as they
stand now were copied into a `git clone --no-local` of this worktree checked
out at `5dc1f37e`, in scratch. The six new cases failed there, each at its
own assertion, and they had failed the same way in this worktree before the
readers changed:

| Case | What the base reading gave |
|---|---|
| `Test_report::test_a_released_work_item_whose_id_is_not_ascii_is_a_candidate` | `released at HEAD: 3 work items; 2 unreleased and untouched` |
| `Test_module::test_merge_order_of_an_id_that_is_not_ascii_is_its_designs_add` | the non-ASCII id last, with commit `None` |
| `Test_overviews_at::test_accepts_the_overview_of_an_id_that_is_not_ascii` | `[]` |
| `Test_tree_at::test_accepts_a_directory_whose_id_is_not_ascii` | the path inside git's quotes, its Hangul as octal escapes |
| `Test_module::test_a_fragment_whose_id_is_not_ascii_reaches_the_note` | the ASCII fragment alone |
| `Test_moved::test_accepts_a_pure_move[a-name-imported-from-a-test-file-whose-name-is-not-ascii]` | `name V: its definition differs from the base's`, exit 1 |

**Mutation (executed).** The runs used #898's fixed copy,
`bin/seal mutate` in #898's worktree
at `ef81822e3`, which refuses a mutant that does not compile. Each mutant
ran against the new case of its reader alone, after commit `a77538b81`.
A batch run prints only the verdicts, so each mutant of a batch was also run
on its own, and its failing line was read.

| Reader | Mutant | Result |
|---|---|---|
| `settle.py#released` | `-z` dropped | red, `0 work items; 5 unreleased` |
| `settle.py#released` | the base reading: no `-z`, `splitlines()` | red, `3 work items; 2 unreleased` |
| `rule_changes.py#order` | `-z` dropped | red, the id with commit `None` |
| `rule_changes.py#order` | the newline strip after a commit deleted | red, the id with commit `None` |
| `rule_changes.py#order` | the base reading: no `-z`, `%x00%H`, `splitlines()` | red, the id last with `None` |
| `unverified_check.py#overviews_at` | the base reading | red, `[]` |
| `unverified_check.py#tree_at` | the base reading | red, the quoted path |
| `unverified_check.py#tree_at` | the empty-field filter deleted | red, a trailing `''` |
| `test_layout.py#_moved_main` | the base reading: no `-z`, `split("\n")` | red, `name V: its definition differs` |
| `publish_release_note.py#fragments` | the base reading: no `-z`, `splitlines()` | red, the ASCII fragment alone |

Each run restored the file from the bytes `seal mutate` held, and
`git status` was clean after each (executed).

**Checks at the boundary (executed).** One `bin/test` command ran the four
modules with the new cases and every module under `tests/` that names one of
the five changed scripts, 41 modules: 2969 passed and 10 skipped, exit 0.
The skips are one case of `tests/skills/test_broad_gate.py` that needs
`cmd.exe` and nine of
`tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`
for scripts no shipped document names. `ruff check` and
`ruff format --check` over the nine changed `.py` files passed.
`seal layout --check tests` exited 0.

**One row of `gaps.md` named the old base, and now names the new one.** The
broad-gate row read `--base release/v0.28.1`. The release is now 0.29.0,
and its base is `release/v0.29.0`, cut at the same commit (the
orchestrator's spawn prompt, executed by the orchestrator). The row now
names `release/v0.29.0`.

**The phase ran on macOS with git 2.50.1 alone.** Whether a non-ASCII file
name in these cases reads the same on the Windows and Linux legs of
`.github/workflows/test.yml` is `frame/questions.md` Q1, and `gaps.md` names
who reads those legs.
