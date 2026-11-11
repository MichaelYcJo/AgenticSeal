# Phase 1: 1794383423-settle-reprints-every-earlier-judgment

## What this phase found

**The frame holds against the tree at `d2040b335`.** The coordinates
`frame/design.md` *Grounding* G15 and G20 and `frame/plan.md` *Technical
context* name in `skills/settle/scripts/settle.py` and
`tests/skills/test_settle.py` held what the frame says of them: the per-plan
`git show`, `adding_commit` and `version` calls inside one `try`, `git_out`
passing no standard input, and the #1281 cases with the `git_out` patch at
`:1580` and the `adding_commit` patch at `:1541` (read). The framer's batched
reads gave today's facts for every plan (G12), and this phase measured the
same of its own code (below).

**The output is byte-identical and the git calls fall from 422 to 24.** In a
`git clone --no-local` of this branch at `f8d2cd0a0` under the crafter's
scratch directory, the dry run with `--released-at 18a7e18fb` printed
308,261 B with the script at `d2040b335` and with the script of this phase,
and `cmp` of the two found no difference. The script at `d2040b335` made 422
git calls, `show` 148, `log` 136 and `tag` 134, in 8.40 s. This phase's made
24, among them one `cat-file`, three `log`, one `for-each-ref` and one
`rev-list`, in 0.72 s (executed, a `test_tmp_*` probe wrapping
`subprocess.run`, run once). The section stays unbounded in this phase, so
the size is today's, as `frame/plan.md` *Phases* row 1 says.

**Each new or changed case was seen red, and how.**

- `test_the_git_calls_do_not_grow_with_the_plans_read` (S4) failed at
  `d2040b335`: 14 git calls with three removed plans against 8 with one
  (executed).
- `test_a_plan_git_holds_no_text_for_is_named_and_none_of_its_rows_printed`
  (S6) failed at `d2040b335` on its sentence line, where the plan was named
  with `git show`'s `bad object` message. With the branch that names a plan
  the batch gave no text for replaced by `if False:`, it failed with a
  `TypeError` in `plan_rows`, which reads `None` there (executed). The guard
  is what keeps that `None` from the reader, so the crash is its red.
- The five parameters of
  `test_a_git_that_cannot_read_an_earlier_plan_is_named_and_refuses_nothing`
  failed at `d2040b335`, where `git_run` does not exist. With the batched
  readers' failure branch replaced by `raise`, the four parameters of the
  batched reads failed on `RuntimeError: git said no`, and the deletions'
  parameter, whose own branch was left in place, passed (executed).
- `test_names_a_plan_no_tag_holds_and_a_removal_no_number_names[no commit]`
  failed at `d2040b335`, where `adding_commits` does not exist (executed).
- `test_a_plan_added_where_another_is_deleted_names_its_release` passes at
  `d2040b335`, whose per-path `git log` sees no rename. It failed with
  `--no-renames` alone removed from `adding_commits` (executed).
- `Test_versions` and `Test_blobs` read functions `d2040b335` lacks. Each
  case went red on its assertion under the mutations its docstring names
  (executed, below).

**Every unit that adds behaviour went red under `seal mutate`**, each on
`skills/settle/scripts/settle.py` with `bin/test tests/skills/test_settle.py
-q -p no:xdist -k <case>`, or the whole two modules where named (executed):

| Unit | Break | Red in |
|---|---|---|
| `adding_commits`, the oldest add | `added[field] = commit` kept the newest | `tests/github/test_publish_release_note.py::Test_main::test_each_entry_links_the_pull_request_that_added_it` |
| `adding_commits`, `--no-renames` | removed | `test_a_plan_added_where_another_is_deleted_names_its_release` |
| `versions`, the peel | `tip = oid` | `Test_versions::test_accepts_…`, on `labels[first]` |
| `versions`, a tag on a tree | `else oid` | `Test_versions::test_refuses_…`, on the set of labels |
| `versions`, lowest first | `sorted(tips, reverse=True)` | `Test_versions::test_accepts_…`, on `labels[first]` |
| `versions`, by number | `number = matched.group(1)` | `Test_versions::test_accepts_…`, on `labels[first]` |
| `blobs`, the read past a text | one byte short | `Test_blobs::test_accepts_…` |
| `blobs`, the kind of object | `if True else` | `Test_blobs::test_refuses_…` |
| `decoded`, the line endings | translation removed | `Test_blobs::test_accepts_…` |
| `git_run`, the standard input | `input=None` | S4, with a `ValueError` in `blobs` |
| `notes`, the tag read | `labels = {}` | `test_apply_keeps_a_directory_its_published_note_does_not_carry`, which then removed the directory |

The tree was clean after each restore (executed, `git status --short`).

**Departures from the frame.**

- **`version` is removed, not kept as a caller of the batched read.**
  `frame/design.md` *Removes* row 3 and *Data & interfaces* say `version`
  stays and calls the batched read. `notes` now reads `versions` once per
  `--apply`, the first time a work item reaches the tag, so nothing called
  `version` any more. *Scope* item 5 allows the readers to be "replaced by
  them", and `skills/core/SKILL.md` *The rule a mechanism is kept against*
  keeps no function with no caller. `notes` went from one `git tag
  --contains` per work item to two calls per run; what it returns did not
  change, and its cases pass.
- **`blobs` returns a list in the order of the names, not a dictionary.**
  The section reads each plan once, at one name, and pairs the answers with
  the deletions by position. A dictionary would key the same pairs by a
  string built twice.
- **`git_run` is the one runner under `git_out`.** `cat-file --batch` gives
  each object's size in bytes, so its output is read as bytes. `decoded`
  turns bytes into the text `subprocess.run` gave `git_out` before: UTF-8
  with each bad byte replaced, and every `\r\n` and `\r` a newline. A
  `git_out` caller reads what it read before. The S5 case patches `git_run`,
  which every git call of the section reaches.
- **`adding_commit` now builds through `git_out`.** Its pathspec is
  literal, and a failure names the whole `git log -z …` command instead of
  `git log <revisions> -- <path>`. No case pins the old message: the two
  cases that make it raise patch `adding_commit` itself.
- **`skills/settle/SKILL.md` gained one clause in this phase.** The bullet
  *The judgments earlier settles removed* now says a plan whose text git does
  not hold is named as not read at its coordinate, with what git answered.
  `frame/plan.md` puts the bullet's rewrite in phase 2 (*Scope* item 7), and
  contract rule 14 asks that a line a person sees be documented in the
  commit that changes it. Phase 2 keeps the clause when it rewrites the
  bullet.

**What phase 2 needs.** The batched reads cost the same at every window, so
the bound of *Scope* item 1 is a slice of `deleted` before `blobs` is asked,
and the older-commit count is the number of removing commits past it. A
batched failure returns one `not read:` line with no coordinate and no row,
so the line of *Scope* item 2 has to be printed beside it or not at all, and
phase 2 decides which. `docs/running/what-a-script-gates.md` *The checks*
still says the section reads through `git show`; the design's
`## Rule changes` replaces that sentence at the settle.

**The phase boundary run.** At `84f811a3b`, one `bin/test` of
`tests/skills/test_settle.py`, `tests/github/test_publish_release_note.py`,
`tests/github/test_release_report.py`, `tests/github/test_rules.py`,
`tests/skills/test_fold_check.py`, `tests/skills/test_passages.py`,
`tests/skills/test_rule_changes.py`, `tests/skills/test_seal.py`,
`tests/skills/test_unverified_check.py`, `tests/test_censuses.py`,
`tests/text` and `tests/behaviour` passed 3,261 cases and failed one,
`test_every_spec_directory_that_reached_the_ladder_has_an_overview`, which
asks for this work item's `gaps.md`; the commit that adds this record adds
it (executed). The modules beside the two tree-wide directories are those
`git grep -l` at `d2040b335` finds naming `settle.py`, `skills/settle` or
`"settle"`, with `tests/github/test_publish_release_note.py`, which loads
`settle.py` through the script it tests. An earlier run at `f8d2cd0a0` also
failed `Test_seal_layout::test_accepts_this_repositorys_tests`, because
`Test_versions` and `Test_blobs` held no `test_accepts_` and `test_refuses_`
case; `84f811a3b` splits each (executed). `uvx ruff check` and
`uvx ruff format --check` passed on the two changed Python files (executed).
The full suite is `unverified`; the orchestrator's broad gate answers it.
