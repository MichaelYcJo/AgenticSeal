# Phase 1: 1793591507-the-settle-reads-what-earlier-settles-judged

## What this phase found

**The frame holds, judged before the build.** Each coordinate it hands the build was opened at `e036886e6` (read): `settle.py#judgments`, `#survey`, `#report`, `#adding_commit`, `#version`, `#git_out` and `PULL_REQUEST_RE` stand as *Technical context* places them, and `tests/skills/test_settle.py#Test_main::test_the_judgments_are_printed_by_the_document_each_stands_on` pins today's block from `JUDGMENTS_HEADING` to `REMOVES_HEADING`. Design G8 was measured again (executed): `git --literal-pathspecs log origin/main --no-renames --full-history --diff-filter=D --name-only -- seal/threads` names the five deleting commits `14bfd9921`, `a92c358b8`, `53f21b542`, `c9b366f15` and `4a8104db5`, and `origin/main` is `57d6665b5`, the local `main`.

**`frame/questions.md` Q1, the work's to answer: the words, pinned in `tests/skills/test_settle.py`.**

- The heading is `settle.py#EARLIER_HEADING`: "the judgments earlier settles removed: the rows of each `frame/plan.md` a commit on `--released-at` deleted, read at that commit's parent and grouped by the document each stands on, with the release each shipped in. The script matches no row to another: whether a row here is one kind with a row above is the settling session's to judge, and it rewrites a section where a kind recurs across releases (`skills/settle/SKILL.md`):". `Test_module::test_the_dry_runs_headings_say_who_decides` pins its last two sentences, and the S1 case pins it whole.
- A work item's line is `<id>  released in v0.1.0; removed by <short> (#7)`. Where no `vX.Y.Z` tag holds the adding commit, the first part is `NO_RELEASE_TAG`, "no `vX.Y.Z` tag holds <short>, the commit that added its plan". Where no commit on the ref adds the plan, it is `NO_ADDING_COMMIT`, "no commit on <ref> adds its plan". A removing commit whose subject ends in no `(#N)` is printed as its short hash alone. The design's example joins the two parts with a comma. A semicolon joins them here, because the no-tag sentence carries a comma of its own.
- A line not read is `<id>  <short>^:seal/threads/<id>/frame/plan.md  not read: <why>`, in the words `plan_rows` gives for a released plan. Where the history's `git log` fails, the line is `not read: <what git said>` with no plan before it, since no plan was listed.

**Departure: a plan whose `git show`, adding-commit read or tag read fails prints none of its rows.** *Scope* item 4 says the failure is named and the dry run goes on, and leaves the plan's rows open. A row printed without its release would read as one whose release is known. So the plan is named as not read, with git's words, and its rows wait for a run where git reads it. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a script names what it did not read and decides nothing on it. Pinned by `test_a_git_that_cannot_read_an_earlier_plan_is_named_and_refuses_nothing` over the three reads.

**Departure: `--no-follow` was built and taken out (`4711da2e8`).** The first build copied it from `adding_commit` against `log.follow`. Measured on this repository (executed): the query lists 55 deleted plans with `log.follow=true` and the flag absent, the same as with it present. The frame does not name the flag, so it went.

**Decisions settled in the code**, each against design *Scope* items 1 to 3 and *Data & interfaces*:

- `settle.py#plan_rows(text)` is the one reader, factored out of `judgments`. It returns `(rows, unread)`, each row with its line in the text. `judgments` adds the round count and the work item id, and `earlier_judgments` adds the `<short>^:` coordinate.
- `earlier_judgments(root, ref, present)` reads the log with `--format=%x00%H%x00%h%x00%s`, so a commit's line starts with a NUL no path starts with. A name is kept only on a full match of `REMOVED_PLAN_RE`. The first time a path is met is its newest deletion, and a later listing of the same path is skipped.
- A root holding no work item prints its settled line and nothing else, as it did. The earlier reading runs inside `survey`, which `main` reaches only where a work item stands. *Scope* item 5 asks that today's output stay as it is, and the settled line is today's output.
- `survey` puts the result in `found["earlier"]`, and `report` prints it after *The judgments* and before the named directories. `apply` and `draft` do not read it.

**The S2 pin (executed).** `test_the_judgments_are_printed_by_the_document_each_stands_on` passes unchanged. Its exact block from `JUDGMENTS_HEADING` to `REMOVES_HEADING` holds no line of the new section, which is where `report` prints it.

**Seen red (contract rule 15), each executed.**

- Against the unchanged code: the eight new cases first written failed, each on `settle.EARLIER_HEADING`, which did not exist.
- S3, with the exclusion of `work_items(records)` alone removed (`if True:` for `if matched.group(1) not in present:`): red at `assert settle.EARLIER_HEADING not in text`.
- S5, with `plan_rows`'s near-heading branch alone removed: red at `assert settle.EARLIER_HEADING in text`, since nothing else in that plan is read. The first run failed at the `split` with an IndexError, so `d474e6c7d` put the assertion before the split, and the mutant was run again.

**Mutations (`seal mutate`), executed.**

- `earlier_judgments` and its print, over the new cases: the parent `^` dropped from the `git show`, the `(#N)` print off, the number never read, the tag not printed, the no-adding-commit sentence emptied, the exclusion inverted, each of the two `git` failure catches turned into a raise, and the section printed always. 9 of 9 red.
- The once-only check and the removal order: both survived the first cases, which removed one plan once. `test_a_plan_is_read_once_at_its_newest_deletion` was added (`f45380d69`, `aef902daf`), and both went red under it.
- `--no-renames` survived. `gaps.md` *Not done* says why no case is added.
- `plan_rows`, over every judgments case: the blank-row skip, the table's refusal, the line offset, and each caller's unread lines dropped. 5 of 6 red. The survivor is the doubled-heading line, a branch #1167 built that this phase only moved; `gaps.md` *Not done* holds it.

**S6, the record replayed (executed).** A `git clone --no-local` of this repository at `4711da2e8` under the scratchpad, where `origin/main` is `57d6665b`, ran `bin/seal settle --released-at origin/main` and exited 0. The new section prints 74 rows in 41 groups from 18 work items, and no line not read. Of the work item lines, 41 name `removed by 14bfd992 (#1269)` and 24 name `removed by a92c358b (#1214)`. The releases named are v0.26.0, v0.27.0, v0.27.1 and v0.27.2. No line names `53f21b54`, `c9b366f1` or `4a8104db`. The two deleting commits removed 20 plans holding the section, and the two not printed, `1793504230-replay-keeps-rounds-on-a-deleted-base` and `1793443708-settle-keeps-a-gaps-file-anywhere`, hold no dated row. The section stands after *The judgments* and before what `--apply` removes. The clone was removed.

**The sweep (contract rule 19).** The method is `git grep -n "one reading"` and a `git grep` for `Judgments of the run`, `dry run prints` and `the judgments` outside `seal/threads/` and `docs/` (executed). The sentence `skills/settle/SKILL.md` *What the dry run shows* stated, "`--apply` removes the plans, so this is the one reading the rows get", was removed in place. The copy in `docs/release-checklist.md` *2b* changes through the design's `## Rule changes`. The other hits say the dry run reads the plans' rows, which still holds: `skills/implement/SKILL.md` *3. The SDD file set*, `skills/implement/acts.md`, `skills/implement/orchestration.md` and `skills/code-review/orchestration.md`. The list is a sample, made from those wordings.

**The boundary run (executed).** At `4711da2e8`, with `gaps.md`, `changelog.md` and the Status cell on disk, one `bin/test -q` ran 108 modules: the plan's named modules, and every test module that at `e036886e6` names `skills/settle`, `settle.py`, a `SKILL.md`, the `skills` directory, `seal/threads`, or walks a tree. It exited 0, 5109 passed and 12 skipped, and again with this record on disk. `bin/seal layout --check tests` exited 0. `uvx ruff check` and `uvx ruff format --check` over `settle.py` and `tests/skills/test_settle.py` exited 0.
