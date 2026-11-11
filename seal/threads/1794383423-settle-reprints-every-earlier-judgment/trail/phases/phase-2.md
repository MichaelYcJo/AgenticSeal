# Phase 2: 1794383423-settle-reprints-every-earlier-judgment

## What this phase found

**The frame holds against the tree at `75ee43aff`.** `earlier_judgments`
listed the deletions newest first into one list, `deleted`, before
`blobs` was asked, as phase 1's record says. So the window of *Scope*
item 1 is a filter of that list, and the batched reads stay as phase 1 left
them. `survey`, `report` and `main` held the shapes `frame/design.md`
*Data & interfaces* and `frame/plan.md` *Technical context* give, and
`main` refused `--draft` beside `--apply` and `--from`, and `--from` beside
`--apply`, in that order (read). The two `EARLIER_HEADING` pins that design
*Scope* item 7 cites at `tests/skills/test_settle.py:3153-3158` stood in
`Test_module::test_the_dry_runs_headings_say_who_decides`, at
`:3338-3342` at `75ee43aff`, because phase 1 added cases above them. Both
pass against the new heading (executed).

**The words of `frame/questions.md` Q1, as this phase wrote and pinned
them.** The orchestrator closes the row; this phase does not write
`frame/questions.md`.

- `EARLIER_HEADING`: "the judgments earlier settles removed: the rows of
  each `frame/plan.md` deleted by one of the two newest commits on
  `--released-at` that deleted a plan, or by any such commit under
  `--all-earlier`, read at that commit's parent and grouped by the document
  each stands on, with the release each shipped in. The script matches no
  row to another: whether a row here is one kind with a row above is the
  settling session's to judge, and it rewrites a section where a kind
  recurs across releases (`skills/settle/SKILL.md`):". The clause new to
  it is pinned in `test_the_dry_runs_headings_say_who_decides`.
- The line of *Scope* item 2, `EARLIER_OLDER`: "`<n>` older commit(s)
  removed plans this section did not read; `seal settle --all-earlier`
  reads them". It is printed last in the section, after a blank line, and
  `plural` gives "commit" for one and "commits" for more. S1's case pins it
  whole.
- The help of `--all-earlier`: "the dry run, with the judgments of the
  plans every commit on --released-at removed, where the dry run alone
  reads those of the two newest such commits. Refused beside --apply and
  --draft".
- The refusals: "settle: --all-earlier and --apply cannot be given
  together: --apply prints none of the judgments earlier settles removed,
  so nothing was read and nothing was removed." and "settle: --all-earlier
  and --draft cannot be given together: the draft prints none of the
  judgments earlier settles removed, so nothing was read and nothing was
  written.". S3's case pins each whole.

**Departures from the frame and decisions made while building.**

- **The heading names `--all-earlier` beside the two newest removing
  commits.** *Data & interfaces* gives one heading "naming the plans the
  two newest removing commits deleted", and the section prints it under
  `--all-earlier` too. A heading that says "the two newest" above the rows
  of every removed plan would state a bound the run did not apply. One
  constant that is true under both runs keeps one heading for the cases to
  split on. Judged against `skills/writing-style/SKILL.md` *에이전트와
  검사가 읽는 글은 한 가지로만 읽히게 쓴다*, since the settling session
  acts on the heading.
- **A batched read that fails keeps the line of older commits.** Phase 1
  left this open. The count comes from the deletions' `git log`, which
  succeeded, so the line still states a fact git gave, and design *Scope*
  item 2 has the section name what it did not read. Where the deletions'
  `git log` itself fails, nothing is counted and `older` is 0, so the one
  `not read:` line stands alone. `test_a_batched_read_that_fails_keeps_the_line_of_older_commits`
  holds the first branch.
- **A removing commit is counted from `deleted`, after both of its
  filters.** Design *Scope* item 1 defines it as a commit at which a plan
  is read, after the rule that reads each plan once at its newest deletion
  and after the exclusion of a standing directory. The commits are listed
  once each, in the order the log meets them, by
  `dict.fromkeys`. `test_a_plan_is_read_once_at_its_newest_deletion`
  already held the first filter's effect on the window: its history has
  three commits that delete a plan, and the middle one deletes only a plan
  deleted again later, so the window reads the other two and the case
  asserts the oldest's rows. `test_a_removing_commit_that_deleted_two_plans_is_one_commit_of_the_window`
  holds the once-each listing.
- **The section is printed where it holds only the line.** Design *Scope*
  item 2 says so, and `test_prints_the_section_where_it_holds_only_the_line_of_older_commits`
  holds it: the two newest removing commits' plans hold no section of
  judgments, and the section prints the heading and the line.
- **The new refusals follow the three that stood.** A run given `--draft`,
  `--apply` and `--all-earlier` gets `DRAFT_WITH_APPLY`, as it did before
  the flag existed.
- **The bullet of `skills/settle/SKILL.md` keeps phase 1's clause and drops
  "The section counts nothing".** The section now counts commits, so the
  sentence says only that it matches no row to another. The reason the
  window is two stands in the comment over `EARLIER_WINDOW`, citing #1481's
  design *Grounding* G11, and not in the skill: the skill ships to every
  repository, and no other sentence of it cites an issue of this one.
- **The line names the bare command.** `gaps.md` `## Not done` says why it
  prints no `--released-at`.

**Each new case was seen red, and how (executed).**

- S1, `test_reads_the_plans_of_the_two_newest_removing_commits_and_names_the_rest`,
  S2, `test_all_earlier_reads_the_plans_of_every_removing_commit`, both
  parameters of S3,
  `test_refuses_all_earlier_beside_apply_or_draft_and_reads_nothing`, and
  the new clause of `test_the_dry_runs_headings_say_who_decides` failed
  against `settle.py` at `75ee43aff`, run before the code was written: S1
  on the section's text, S2 and S3 on the argument the parser did not
  know, and the pin on the heading's text. S1 also went
  red with the bound alone removed (the mutation table below).
- The three cases added at `cd4e2d9fa` pass against the code they were
  written after, so each was seen red under the mutation its docstring
  names, in the table below.

**Every unit that adds behaviour went red under `seal mutate`**, each on
`skills/settle/scripts/settle.py` with `bin/test
tests/skills/test_settle.py -q -p no:xdist -k <cases>` (executed). The tree
was clean after each restore (executed, `git status --short`).

| Unit | Break | Red in |
|---|---|---|
| the window | `if False:` in place of the bound | S1 |
| the window's size | `EARLIER_WINDOW = 3` | S1 |
| the count of older commits | `older = 0` | S1 |
| the commits listed once each | one entry per plan, not per commit | `test_a_removing_commit_that_deleted_two_plans_is_one_commit_of_the_window` |
| `every` in `earlier_judgments` | `not every` dropped from the bound | S2 |
| `every` through `survey` | the argument not passed | S2 |
| the section printed for the line alone | `or older` dropped | `test_prints_the_section_where_it_holds_only_the_line_of_older_commits` |
| the count kept on a batched failure | `0` returned | `test_a_batched_read_that_fails_keeps_the_line_of_older_commits` |
| the line printed | the `write` replaced by `pass` | S1 |
| the line's words | "were not read" in place of "removed plans this section did not read" | S1 |
| the heading's new clause | "the newest" in place of "the two newest" | `test_the_dry_runs_headings_say_who_decides` |
| the refusal beside `--apply` | `if False:` | S3 `[apply]` |
| the refusal beside `--draft` | `if False:` | S3 `[draft]` |
| the refusal's words | "clash" in place of "cannot be given together" | S3 `[apply]` |

**S7, replayed (executed).** In a `git clone --no-local` of this branch at
`cd4e2d9fa` under the crafter's scratch directory, with the tags fetched,
`settle.main` ran with `--released-at 18a7e18fb`, the base the branch was
cut from, through a `test_tmp_*` probe that wraps `subprocess.run`, run
once with two runs of each form.

| Run | Time | Git calls | Output | Section |
|---|---|---|---|---|
| the dry run | 0.91 s, 1.04 s | 24 | 108,893 B | 47,844 B |
| `--all-earlier` | 1.28 s, 1.46 s | 24 | 308,350 B | 247,301 B |

The dry run's section names `8657297d (#1495)` and `e5370691 (#1466)` as
its removing commits, and its last line reads "8 older commits removed
plans this section did not read; `seal settle --all-earlier` reads them".
Under `--all-earlier` the section names the seven removing commits whose
plans hold rows, #1214, #1269, #1310, #1400, #1432, #1466 and #1495, and
ends on a row's grounds, with no such line. The section is 47,844 B where
the framer's prototype measured 48,176 B, and the whole output under
`--all-earlier` is 89 B longer than phase 1's 308,261 B: the heading is
longer, and the rows are the same.
