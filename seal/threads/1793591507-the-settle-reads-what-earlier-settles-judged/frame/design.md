# Design: 1793591507-the-settle-reads-what-earlier-settles-judged

## Grounding

Each row is labelled `executed` where this framer ran the command that gave
it, and `read` where it opened the coordinate.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* (read) | The settle reads the judgments "against what they cost and caught" and "rewrites the guidance where a kind of judgment keeps costing more than it returns". A kind that recurs once per release is that case, and today's dry run cannot show it, because it reads one release's plans. This work gives the settling session the earlier releases' rows. It changes nothing in the core. |
| G2. `skills/core/SKILL.md` *The first value: efficient development through the workflow*, the bold sentence *Judgment is spent where meaning is the question, and a script answers the rest* (read) | The script prints only facts it reads exactly: git's output, and table rows read through the reader today's judgments use. It does not decide whether two rows are one kind, it counts no recurrence, and it does not filter one row by the spelling of another. The settling session makes that judgment. |
| G3. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "Nothing is kept beside the tree to stay in step with it", and "History goes to git, the release notes and the work record." The earlier record is read from git's history of the `--released-at` ref, which is the tree's own history. No file, cache or count is added to carry the judgments from one settle to the next. |
| G4. The owner's decision of 2026-11-02: no numeric cap or threshold decides judgment, stated in #1289's body ("Decided by the owner on 2026-11-02: no numeric ceiling") and in #1288's first *Done when* item (`gh issue view 1289`, `gh issue view 1288`) | No count of recurrences triggers a rewrite, and the reading has no window of releases. Every plan an earlier settle removed is read. |
| G5. #1269's body *The judgments* (executed: `gh pr view 1269 --json body`) | The 0.27.x settle read the rows of its 14 plans. It rewrote two sections for kinds that recurred among them, and it named two kinds it did not rewrite. One of those was the orchestrator folding frame cells in place, which it saw in nine work items. |
| G6. #1214's body *The judgments* (executed: `gh pr view 1214 --json body`) | The 0.26.0 and 0.27.0 settle named four recurring kinds and rewrote no section for them. Two of the four recur in later releases. The first is "regressions chasing one mechanism's edges": #1269 found it again and rewrote `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* for it. The second is "a frame fold after a fix pass reworded a rule". So a recurrence across releases already happens, and each settle saw it only because its own release held enough instances. |
| G7. #1182's body (executed: `gh pr view 1182 --json body`, its `## ` headings) | The 0.24.x settle's body holds no *The judgments* heading. Its headings run from *What this pull request does* to *Verification*. The issue cites #1182 beside #1269, and only #1214 and #1269 hold the section. The plans #1182 removed hold no *Judgments of the run* section (G8). |
| G8. The history of `origin/main` at `57d6665b5` (executed: `git log origin/main --no-renames --full-history --diff-filter=D --name-only -- seal/threads`, then `git show <commit>^:<path>` for each deleted `frame/plan.md`) | Five commits deleted `seal/threads/<id>/frame/plan.md` files: `14bfd9921` (#1269), `a92c358b8` (#1214), `53f21b542` (#1182), `c9b366f15` (#1108) and `4a8104db5` (#1098). Each deleted plan reads whole at its deleting commit's parent. `14bfd9921` removed 14 plans holding the section, with 42 dated rows. `a92c358b8` removed 6 plans holding it, with 32 dated rows. The plans the other three removed hold no section. The query took 0.025s. No earlier layout (`seal/specs/`, a top-level `plan.md`) has to be read, because the section postdates the `frame/` layout. |
| G9. The `Judged against` cells of those 74 earlier rows (executed: the same `git show` reads, the last cell counted by `sort \| uniq -c`) | One section is spelt several ways. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* stands alone in 3 rows, and with a different parenthetical or a second document in 3 more. Grouping by the exact cell is a display order. A script that matched an earlier row to a current one by its cell would split what the settling session reads as one kind. |
| G10. This release's plans (read: `seal/threads/1793573496-the-settle-folds-named-directories-the-person-marks/frame/plan.md` and `seal/threads/1793538228-the-release-pr-opens-after-the-last-merge/frame/plan.md` *Judgments of the run*) and issues #1286, #1288, #1290 (executed: `gh issue view`, titles) | 0.28.0's rows hold a fix pass that "decides what `settle.py#history` reads of each `--cc` status, enumerating every status shape", and frame folds "with the round's paste-ready text". These are the kinds G6 and G5 name from earlier releases. This release is the case the issue describes. This work builds none of their scope. |
| G11. `skills/settle/scripts/settle.py#judgments`, `#survey` and `#report` (read) | `judgments(records, ids)` reads each released plan from the working tree. It names a heading near the section, and a section whose table is not under `JUDGMENTS_HEADER`, as not read. It reads the table through `hooks/lib/config.py#gfm_table` and skips the template's empty row. `report` prints the groups under `JUDGMENTS_HEADING`. The earlier reading reuses that table reader over a plan's text. |
| G12. `skills/settle/scripts/settle.py#adding_commit` and `#version` (read) | #1139 built them as exact readers. `adding_commit` gives the oldest commit on a ref that adds a path, with its `(#N)`. `version` gives the lowest `vX.Y.Z` tag that holds a commit. They give an earlier plan's release, and `PULL_REQUEST_RE` gives the `(#N)` of the commit that removed it. Nothing new parses a version or a pull request number. |
| G13. `skills/settle/SKILL.md` *What the dry run shows*, the bullet *The judgments* (read) | "`--apply` removes the plans, so this is the one reading the rows get." After this work that sentence is false, so the work rewrites it in place. |
| G14. `docs/release-checklist.md` *2b. Settle what earlier releases left behind*, its paragraph opening "Before `seal settle --apply`" (read) | The paragraph says "so this is the one reading they get". That sentence becomes false, so `## Rule changes` changes the paragraph. No unsettled design's operation on *2b* quotes this paragraph (executed: `grep` of every `seal/threads/*/frame/design.md`). |
| G15. `docs/the-review-record.md` *The run*, the paragraph opening "The orchestrator's judgments of a run are rows" (read) | The paragraph says "The settle's dry run prints the rows of every released work item". That reading widens, so `## Rule changes` changes the sentence. `1793542348`'s pending change to *The run* quotes another sentence, so the two do not overlap. |
| G16. `docs/what-a-script-gates.md` *The checks*, the `seal settle` row (read) | The row's cell for what the script reads names `frame/plan.md` *Judgments of the run* and no history, so `## Rule changes` widens that cell. No unsettled design quotes this row (executed: `grep -c "Judgments of the run"` over `1793573444`'s and `1793577579`'s designs gives 0). |
| G17. `skills/settle/SKILL.md` *In local mode* (read) | In local mode, `--apply` removes each directory from the git directory, and no commit holds what it removes. The history therefore holds earlier plans only where the repository once committed its `seal/` root. The earlier reading needs no branch for local mode, and the skill says where it finds nothing. |
| G18. `docs/README.md`, the index (read) | Each `file:` below is picked from it: `docs/the-review-record.md`, `docs/release-checklist.md` and `docs/what-a-script-gates.md` each have their own row. |
| G19. This design's `## Rule changes` (executed: in a `git clone --no-local` of `69d473bc` under `<scratchpad>/1793591507-the-settle-reads-what-earlier-settles-judged/frame/`, a `test_tmp_*` script ran `rule_changes.py#parse` on this file and `rule_changes.py#apply_op` on each operation against the clone's `docs/`, then the directory was removed) | The section parses with no error and no line left unread. Each of the three `change` operations is placed, so each `from` stands once in its section today. |
| G20. Issue #1281 (executed: `gh issue view 1281 --json body,comments`) | The issue has no comments. Its *Done when* lets the frame decide where the earlier record is read from. It asks for four things: the script prints only facts it reads exactly, the settling session judges kind, nothing is kept beside the tree, and a run with no earlier settle prints what it prints today. |

## Scope

In:

1. **The dry run reads the plans earlier settles removed, from the history of
   `--released-at`.** `skills/settle/scripts/settle.py` runs one
   `git log --no-renames --full-history --diff-filter=D --name-only` of the ref over the literal pathspec
   `seal/threads`. It keeps each listed path of exactly the shape
   `seal/threads/<id>/frame/plan.md` whose `<id>` has no directory in
   `work_items(records)`. It reads each such plan once, at the parent of the
   newest commit that deleted it, as `git show <commit>^:<path>` gives it.
   It needs no branch for local mode: a local root's removals leave no
   commit, so there the reading finds only what a shared past committed.
2. **One table reader serves both readings.** The body of
   `settle.py#judgments` that reads a plan's text is factored so that today's
   reading, from the working tree, and the earlier reading, from a blob, run
   the same code. That code names the near heading, reads the table under the
   exact header, and skips the empty row. An earlier plan's line that is not
   read is named in the same words, at its coordinate
   `<short>^:seal/threads/<id>/frame/plan.md`.
3. **What it prints.** A new section, *The judgments earlier settles
   removed*, is printed after *The judgments* and before the named
   directories, and only where it holds a row or a line not read. Its rows
   are grouped by the `Judged against` cell exactly as written, and the
   groups come in the order they are first met. That order walks the removing
   commits newest first and, within one commit, the plans in path order. Each
   work item's line gives:
   - its id;
   - `released in` and the version tag `version(root, adding_commit(...))`
     gives, or a line saying that no `vX.Y.Z` tag holds the commit that
     added its plan;
   - `removed by` and the removing commit's short hash, with its `(#N)` where
     `PULL_REQUEST_RE` reads one.

   Under the work item's line, each row prints its coordinate, date and
   judgment, then its grounds, in the shape today's block uses. The section
   carries no round count, no count of recurrences and no mark of kind.
4. **A git that fails is named, and the dry run goes on.** Where the
   `git log`, a `git show` or a tag read raises, the section prints one
   `not read:` line with the command and what git said, and the dry run
   exits 0 as it does today. The dry run refuses nothing (`skills/settle/SKILL.md`
   *What the dry run shows*, its last paragraph).
5. **A run with no earlier settle prints what it prints today.** Where no
   commit on the ref deleted such a plan, or no deleted plan holds a row, the
   new section is absent. Every line today's dry run prints is unchanged.
   `--apply`, `--draft` and `--from` print what they print today.
6. **`skills/settle/SKILL.md` says it.**
   - *What the dry run shows*: the bullet *The judgments* loses its "one
     reading" sentence, and a bullet *The judgments earlier settles removed*
     states items 1 to 5. The bullet also states two limits that no guard
     covers. A shallow clone lists no plan past its boundary. A plan that only
     a merge commit's own resolution deleted is not listed, because the
     query reads non-merge diffs.
   - *The settling session's procedure*: step 5 reads both sections, and
     rewrites the section a kind stands on where it recurs across work items
     or across releases, as step 4 writes a group's. Whether an earlier row is
     one kind with a current row is the settling session's judgment. Step 11's
     body list adds each kind that recurred across releases, with the releases
     it recurred in.
   - *In local mode* adds one bullet saying where the earlier reading finds
     nothing.
   - The module docstring of `settle.py` and its `JUDGMENTS_HEADING`
     neighbour state the same.
7. **The rule changes below**, written at the settle after the release.
8. **The changelog fragment** `changelog.md` in this work item's directory.

Out:

- Reading earlier settles' pull request bodies, from the script or from `gh`
  (`plan.md` *Alternatives considered*, A2). The dry run prints each
  removing commit's `(#N)`, and the settling session opens that body when a
  row sends it there.
- A file or cache under `seal/` that carries judgments between settles (A3).
- Keeping plans in the tree past `--apply` (A4).
- Matching, filtering or counting rows by kind or by cell (A5, A6).
- The round count of an earlier work item (A7).
- Merging the earlier rows into today's groups (A8).
- The `seal settle` rows of `README.md` and `README.ko.md`. Neither row names
  today's *The judgments*, so neither owes the new section.
- `.claude-plugin/plugin.json`, as the spawn prompt directs.
- The scope of #1286, #1288 and #1290. G10 reads their recurrences as
  grounds and builds none of them.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given a repository where a commit added `seal/threads/<old>/frame/plan.md` with two *Judgments of the run* rows under two `Judged against` cells, a tag `v0.1.0` holds that commit, and a later commit whose subject ends `(#7)` deleted the directory, and one released work item stands in the tree. When the dry run runs, then *The judgments earlier settles removed* lists both cells as groups. Each group names `<old>` as released in `v0.1.0` and removed by that commit's short hash and `(#7)`, and each row prints with its coordinate at the commit's parent, its date, its judgment and its grounds. | a case in `tests/skills/test_settle.py` asserting the section's text exactly |
| S2 | Given a repository whose history deletes no plan, when the dry run runs, then its output is the output it gives today, and the new heading does not appear. | `tests/skills/test_settle.py::Test_main::test_the_judgments_are_printed_by_the_document_each_stands_on`, unchanged and passing, since it pins today's block up to `REMOVES_HEADING`; and an assertion, in a new case or in that one, that the new heading is absent |
| S3 | Given a plan a commit deleted whose work item's directory stands in the working tree, when the dry run runs, then that plan is not read as an earlier one. | a case in `tests/skills/test_settle.py`, shown red with the `work_items` exclusion alone removed |
| S4 | Given a deleted plan whose adding commit no `vX.Y.Z` tag holds, and a removing commit whose subject holds no `(#N)`, when the dry run runs, then the work item's line says no version tag holds the adding commit, and it names the removing commit with no number. | a case in `tests/skills/test_settle.py` |
| S5 | Given a deleted plan whose section heading is near *Judgments of the run* and is not it, when the dry run runs, then it is named as not read at its `<short>^:` coordinate, none of its rows is printed, and the dry run exits 0. | a case in `tests/skills/test_settle.py`, shown red with the shared reader's near-heading branch alone removed |
| S6 | Given this repository at the phase's head, cloned with `git clone --no-local` into `<scratchpad>/1793591507-the-settle-reads-what-earlier-settles-judged/`, when `seal settle --released-at origin/main` runs there, then the new section lists the plans `14bfd9921` and `a92c358b8` removed, and none of the three earlier settles' plans. | replayed by the crafter in the scratch clone, with the output's counts recorded in the phase record |
| S7 | Given the next settle's dry run, when the settling session reads both sections, then it rewrites the section a kind stands on where the kind recurs across releases, and its pull request body names that kind with the releases it recurred in. | read by the owner at the next settle: `skills/settle/SKILL.md` steps 5 and 11 state it, `check: none reader: the owner's settling session at this step` |

## Data & interfaces

- `settle.py`, the new reader: `earlier_judgments(root, ref, present)` returns
  `(groups, unread)`. `groups` has the form `[(judged against, [(id,
  released, removed, [(coordinate line, date, judgment, grounds)])])]`.
  `released` is a tag name, or the adding commit where no tag holds it.
  `removed` is `(short hash, pull request number or None)`. `unread` is
  `[(where, why)]`. `present` is `work_items(records)`. The reader runs
  `git_out`, whose `--literal-pathspecs` makes `seal/threads` a literal path.
  The shape filter is a full match of `seal/threads/[^/]+/frame/plan\.md`
  against each listed name.
- `survey` adds `found["earlier"]` beside `found["judgments"]`. `report`
  prints it. `apply` and `draft` do not read it.
- `settle.py`: a new heading constant for the section, pinned by its case as
  `JUDGMENTS_HEADING` is pinned today.
- The printed shape, with the wording left to the phase and pinned there
  (`frame/questions.md` Q1):

  ```
  <heading: the rows of each frame/plan.md a commit on <ref> deleted, read at
  that commit's parent, grouped by the document each stands on, with the
  release each shipped in; whether one is the kind of a row above is the
  settling session's to judge>

  judged against: <cell>
      <id>  released in v0.27.1, removed by 14bfd99 (#1269)
          14bfd99^:seal/threads/<id>/frame/plan.md:<line>  <date>  <judgment>
              grounds: <grounds>
  ```

## Rule changes

- change
  file: docs/the-review-record.md
  section: The run
  from: The settle's dry run prints the rows of every released work item
    grouped by the document they stand on, and the settling session rewrites
    the section where one kind of judgment keeps costing rounds.
  to: The settle's dry run prints the judgment rows of the released work
    items and, beside them, those earlier settles removed, which the history
    still holds. The settling session rewrites the section where one kind of
    judgment keeps costing rounds, in one release or across several, and
    deciding that two rows are one kind is its own judgment.
- change
  file: docs/release-checklist.md
  section: 2b. Settle what earlier releases left behind
  from: **Before `seal settle --apply`, the settling session reads the dry
    run's *The judgments*, the orchestrators' rows from every released
    `frame/plan.md` grouped by the document each stands on, and rewrites a
    section where one kind of judgment recurs across work items or kept
    costing rounds.** The rows leave with their directories at `--apply`, so
    this is the one reading they get; `skills/core/SKILL.md` *A judgment
    stands on a source document, and is written down with both* says the
    guidance improves from that record and not from memory.
  to: **Before `seal settle --apply`, the settling session reads the dry
    run's *The judgments* and *The judgments earlier settles removed*, and
    rewrites a section where the same kind of judgment came back, within
    this release or over several, or cost rounds each time it was made.** *The judgments* holds the
    orchestrators' rows from every released `frame/plan.md`. *The judgments
    earlier settles removed* holds the rows of every plan an earlier settle
    removed, read from the history with the release each shipped in. Both
    are grouped by the document each row stands on. The pull request body
    names each kind that recurred across releases with the releases it
    recurred in. The rows leave the tree with their directories at
    `--apply`, and the history keeps them for the next settle, so nothing is
    kept beside the tree to carry them; `skills/core/SKILL.md` *A judgment
    stands on a source document, and is written down with both* says the
    guidance improves from that record and not from memory.
- change
  file: docs/what-a-script-gates.md
  section: The checks
  from: open rows, `frame/plan.md` *Judgments of the run*
  to: open rows, `frame/plan.md` *Judgments of the run* of the released plans and, through `git log` and `git show`, of every plan an earlier settle removed

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| "`--apply` removes the plans, so this is the one reading the rows get." | `skills/settle/SKILL.md` *What the dry run shows*, the bullet *The judgments* | rewritten in place by *Scope* item 6: the history keeps the rows, and the next dry run reads them |
| "The rows leave with their directories at `--apply`, so this is the one reading they get" | `docs/release-checklist.md` *2b. Settle what earlier releases left behind* | `## Rule changes` above, written at the settle after the release |
| The orchestrator handing each framer the earlier decisions by issue number, because nothing in the records led there | outside the tree: #1281's body, its third bullet | the settle's rewrite of the section a cross-release kind stands on, which the next framer reads as policy (*Scope* items 1 and 6) |

The work adds no gate, check, hook, line grammar, label or mark. It adds
one printed section to a dry run that refuses nothing.

Framed 2026-11-02 by framer, before the build.
