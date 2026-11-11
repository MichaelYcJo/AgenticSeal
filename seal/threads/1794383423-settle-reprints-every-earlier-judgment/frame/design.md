# Design: 1794383423-settle-reprints-every-earlier-judgment (#1481)

## Grounding

The tree as read at `18a7e18fb`.

Each row is labelled `executed` where this framer ran the command that gave
it, and `read` where it opened the coordinate. The probes ran in a
`git clone --no-local` of this branch under
`<scratchpad>/1794383423-settle-reprints-every-earlier-judgment/frame/`,
with `--released-at 18a7e18fb`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The first value: efficient development through the workflow*, the paragraph *A document is cut by who opens it and at which step* (read) | "A party pays for every byte of each file it opens, on every spawn that opens it." The settling session reads the whole dry run at step 5, so every byte of *The judgments earlier settles removed* is paid at every settle. The bound is what this work owes that sentence. |
| G2. `skills/core/SKILL.md` *The first value*, the paragraph *Judgment is spent where meaning is the question, and a script answers the rest* (read) | The script may bound the section only by a fact git gives exactly. Which commits removed a plan, newest first, is such a fact. Whether a row stands on the same document as another row is a judgment of meaning, so no bound reads a row's cells. |
| G3. `skills/core/SKILL.md` *A judgment stands on a source document, and is written down with both* (read) | The settle reads the judgments to rewrite the guidance where a kind keeps costing. That is the case #1281 built the section for, and the bound has to keep it. |
| G4. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "Nothing is kept beside the tree to stay in step with it." The bound is read from the history at each run, and nothing records which rows were shown before. The same rule asks for one source per fact, so the batched readers replace the per-commit ones and do not stand beside them. |
| G5. #1281's design *Grounding* G4 (read: `git show v0.28.0:seal/threads/1793591507-the-settle-reads-what-earlier-settles-judged/frame/design.md`), and the owner's decisions it cites (executed: `gh issue view 1289` and `gh issue view 1288`) | #1281's framer read the owner's decision of 2026-11-02 as "the reading has no window of releases". #1289's body decides "no numeric ceiling" for a release's size. #1288's first *Done when* item decides no fixed number of review rounds. Neither names what the dry run prints. #1481 is the owner's issue of 2026-11-09, and it names "the last N releases" as a candidate bound. So a window over the history is open to this frame. The window decides what the script prints. It decides no kind and no recurrence, which stay the settling session's. |
| G6. #1281's plan, *Technical context* and *Alternatives considered* (read: `git show v0.28.0:seal/threads/1793591507-the-settle-reads-what-earlier-settles-judged/frame/plan.md`) | Its failure scenario foresaw this growth, "several hundred rows six releases on", and named the settle's own rewrites as the way out. Its A5 rejected a filter by a row's cell or first path, its A6 rejected a count of rows per cell, and its A2 rejected reading earlier settles' pull request bodies. This frame does not argue the three again and builds none of them. |
| G7. Issue #1481 (executed: `gh issue view 1481 --json body,comments`) | No comments. *Done when* asks three things: a default run's output size and git-call count do not grow with the number of releases, a default run here finishes under 2 s, and `skills/settle/SKILL.md` step 5 states the bound. *Change* asks that the calls that remain are batched, one `git cat-file --batch` and one tag lookup. |
| G8. The dry run today (executed: `python3 skills/settle/scripts/settle.py --released-at 18a7e18fb`, and `test_tmp_gitcalls.py` wrapping `subprocess.run`) | The output is 308,261 B, and *The judgments earlier settles removed* is 247,730 B of it. The section holds 316 rows in 138 `judged against` groups, from plans released in 26 versions, v0.26.0 to v0.37.0. The run made 422 git calls: `show` 148, `log` 136, `tag --contains` 134. They took 15.05 s of a 15.92 s run on a loaded machine. The issue measured 6.6 s on its run. |
| G9. The dry run without the section (executed: `test_tmp_stub.py`, `earlier_judgments` replaced by one returning nothing, run twice) | 0.39 s and 0.48 s, with 19 git calls. Everything the run does besides this section fits well under 2 s. |
| G10. The commits that removed plans, and the versions their plans shipped in (executed: the output of G8, each work item line's `released in` and `removed by`) | Ten commits on the ref removed a plan. Seven removed plans that hold *Judgments of the run*: #1214 (v0.26.0 to v0.27.0), #1269 (v0.27.1, v0.27.2), #1310 (v0.27.3 to v0.29.0), #1400 (v0.30.0 to v0.32.5), #1432 (v0.32.6 to v0.34.1), #1466 (v0.35.0 to v0.36.0) and #1495 (v0.37.0). One settle covered from one to eleven releases. |
| G11. What the five settles since #1281 used the section for (executed: `gh pr view <N> --json body` for #1310, #1400, #1432, #1466 and #1495, each body's *The judgments*) | Each kind a body names as recurring across releases rests on rows of the current release and of the two newest removing commits before that settle. The farthest case is #1432: the kind "one mechanism whose edges each fix pass chased" stood in v0.32.6, which was current, and in `1793573496` (v0.28.0), which #1310 removed two settles earlier. #1400's body, the settle between them, names no instance of the kind. With only the newest removing commit read, #1432 would have seen the kind in one row. Older instances a body cites, such as v0.27.1 in #1432 and #1466, sit beside a nearer one that the two newest removing commits hold. |
| G12. The batched reads against today's (executed: `test_tmp_batch.py` over all 134 plans the history lists) | One `git cat-file --batch` gave each plan the text `git show <commit>^:<path>` gives. One `git log -z --no-renames --full-history --diff-filter=A --name-only` of the ref over `seal/threads`, keeping the oldest add of each path, gave each plan the commit `adding_commit` gives. One `git rev-list --parents` of every `vX.Y.Z` tag, each commit labelled by the lowest version first, gave each adding commit the tag `version` gives. There were 0 mismatches in 134. The three batched reads took 0.03 s, 0.03 s and 0.06 s. |
| G13. A prototype of the bounded, batched section (executed: `test_tmp_window.py`, `earlier_judgments` replaced by the prototype, `settle.main` run whole) | With no bound, the output is byte-identical to G8's (`cmp`), in 0.70 s with 24 git calls. With the plans of the two newest removing commits: 0.51 s, 24 git calls, 108,707 B of output, 48,176 B of section, and 8 older removing commits not read. With the newest one alone: 0.50 s, 67,781 B, 7,250 B. The call count is the same at every bound. |
| G14. A filter by document, the issue's second candidate (executed: the rows of G8 counted by the first backticked `.md` path of their `judged against` cell) | `skills/implement/orchestration.md` holds 116 rows from 21 releases, `skills/code-review/orchestration.md` 84 from 18, and `skills/core/SKILL.md` 51 from 15. Those three paths carry 251 of the 316 rows. The groups a settle writes name `docs/` files, and almost no row names one. |
| G15. `skills/settle/scripts/settle.py` (read) | `earlier_judgments` (`:1105-1200`) lists the deletions in one `git log` and reads each plan with three calls (`:1170-1180`): `git show`, `adding_commit` (`:340-384`) and `version` (`:505-515`). `adding_commit` is also read by `notes` (`:625`) and `.github/scripts/publish_release_note.py:286`, and its docstring calls it the one reader of a commit's `(#N)`. `version` is also read by `notes` (`:632`). `git_out` (`:487`) passes no standard input. `plan_rows` (`:1059`) is the one reader of a plan's section. `survey` (`:1374`) and `report` (`:1689-1701`) carry and print the section. `main` (`:1873`) refuses `--draft` beside `--apply` and `--from`, and `--from` beside `--apply`, each with exit 2 and a sentence. |
| G16. `lib/gitcmd.py` (read) | Every `git log` a script under `skills/` starts is built by `argv`. `git_out` builds through it, so the batched `log` reads do too. |
| G17. `skills/settle/SKILL.md` (read) | The command table is at `:43-57`. The bullet *The judgments earlier settles removed* (`:116-139`) says the section holds "every row of every" removed plan. Step 5 (`:199-217`) tells the settling session to read the section. Step 11 asks the body to name each kind that recurred across releases. `skills/settle/local-mode.md:42` stays true, because a local root's removals leave no commit. |
| G18. The policy root (read: `docs/releasing/release-checklist.md` *Settle what earlier releases left behind* `:115-128`, `docs/running/the-run.md` *The run* `:54`, `docs/running/what-a-script-gates.md` *The checks* `:63`; executed: `grep -n -A1` for the three `file:` values over every `seal/threads/*/frame/design.md`) | Each states that the section reads every plan an earlier settle removed. `1794289597` changes another cell of *The checks*, and `1794312072` changes *The release pull request* of the checklist. No unsettled operation quotes the three sentences this work changes. The subject of this work is the code, so the three change through `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). |
| G19. `docs/README.md`, the index (read) | Each `file:` below is picked from it. None of the three documents has a `.ko.md` edition. |
| G20. `tests/skills/test_settle.py` (read) | The #1281 cases stand at `:1371-1615`. `:1580` fails `git_out` by its subcommand, `log`, `show` or `tag`. `:1541` replaces `adding_commit`, and `:2309` replaces it for `notes`. `:3153-3158` pin two phrases of `EARLIER_HEADING`. |
| G21. Whether the tree already batches these reads (executed: `git grep -n -e cat-file -e --batch -e rev-list -e --contains` over `lib`, `skills`, `.github/scripts`, `hooks`, `bin`) | No script reads blobs through `cat-file --batch` or labels commits by a tag graph. `skills/verify/scripts/pact_check.py#ref_holding` asks `for-each-ref --contains` per commit and returns the first ref by name, which is another fact. |
| G22. `seal/follow-up.md`, and the `### Process changes` table of v0.37.3 (executed: `grep -n -i 'settle\|judgment' seal/follow-up.md`, `gh release view --json body`) | No follow-up row and no process change concerns the settle's earlier reading. |
| G23. The rule changes below (executed: `rule_changes.py#parse` on this file and `#apply_op` of each operation against the clone's `docs/`) | The section parses with no error and no line left unread. Each of the three `change` operations is placed, so each `from` stands once in its section at `18a7e18fb`. |

## Scope

In:

1. **The default dry run reads the plans the two newest removing commits
   deleted.** A removing commit is a commit on `--released-at` at which
   `earlier_judgments` reads a plan, after the rule that reads each plan once
   at its newest deletion and after the exclusion of a work item whose
   directory stands. Of those commits, newest first, the plans of the first
   two are read and printed as today. The number two is a constant in
   `settle.py`, with a comment citing G11 for why it is two.
2. **The section names what it did not read.** Where the window leaves out
   a removing commit, the section ends with one line saying how many older
   removing commits it did not read, and that `seal settle --all-earlier`
   reads them. The line holds a count of commits, never of rows. The section
   is printed where it holds a row, a line not read, or this line.
3. **`seal settle --all-earlier` reads every removing commit's plans**, as
   the dry run does today, and prints no line of item 2. It is refused beside
   `--apply` and beside `--draft`, with exit 2 and one sentence each, as
   `--draft` beside `--apply` is refused. It is taken beside `--from`.
4. **The reads are batched, whatever the window.** The deletions are listed
   by today's one `git log`. The plans' texts are read by one
   `git cat-file --batch`, each at `<commit>^:<path>`. Their adding commits
   come from one `git log -z --no-renames --full-history --diff-filter=A`
   of the ref. The lowest `vX.Y.Z` tag of each adding commit comes from one
   read of the tags' history. Two calls are allowed for that read where one
   lists the tags and the other walks them, such as `for-each-ref` and
   `rev-list --parents --stdin`. The printed output for the same plans is
   byte-identical to today's (G12, G13).
5. **One reader per fact.** `adding_commit` and `version` read through the
   batched readers, or are replaced by them, so `notes` and
   `publish_release_note.py` read the same code as the earlier section. What
   each returns to its callers does not change, and neither do the cases at
   `tests/skills/test_settle.py:3031-3051`. The lowest tag stays the lowest
   by number, and a tag of any other shape stays no version.
6. **A batched read that fails is named, and the dry run goes on.** A
   failed `cat-file`, adding-commit `log` or tag read is named once with
   what git said, as the deletion log's failure is today. No row of the plans
   it would have read or labelled is printed. A plan the batch answers as
   `missing`, or as no blob, is named as not read at its
   `<short>^:<path>` coordinate. The dry run exits 0.
7. **`skills/settle/SKILL.md` states the bound.**
   - The command table gains the row for `seal settle --all-earlier`.
   - The bullet *The judgments earlier settles removed* says which plans it
     reads (item 1), the line of item 2, the flag, and the batched reads of
     item 4. It keeps the two limits it states today, the shallow clone and
     the merge's own resolution.
   - Step 5 says the section holds the plans the two newest removing
     commits deleted. It says that where a kind the session reads may have
     come before the window, the session runs `seal settle --all-earlier`
     and reads the rest. A kind standing on a section an older settle
     rewrote is the example.
   - `settle.py`'s module docstring, `EARLIER_HEADING`, the argument's help
     and the exit-2 list say the same. `EARLIER_HEADING` keeps the two
     phrases pinned at `tests/skills/test_settle.py:3153-3158`.
8. **The rule changes below**, written at the settle after the release.
9. **The changelog fragment** `changelog.md` in this work item's directory.
   Its `### Process changes` table gets one row in the shape of
   `templates/records/process.md`, because step 5 changes what the settling
   session reads.

Out:

- A filter or a match of rows by cell or by path, a count of rows per cell,
  and reading earlier settles' pull request bodies. #1281 rejected the three
  (G6), and G14 measures the filter saving little.
- The window's size as an argument (`plan.md` *Alternatives considered*).
- `load` keeping no module between calls, which #1482 owns. With fewer plans
  read by default, `plan_rows` loads its two modules fewer times. This work
  does not change `load`.
- Skipping the earlier reading under `--apply` or `--draft`, which do not
  print it. After item 4 the reading costs a fixed handful of calls.
- `skills/settle/local-mode.md`, which stays true (G17).
- The `seal settle` rows of `README.md` and `README.ko.md`, which name
  neither section.
- `.claude-plugin/plugin.json` and the version move, which #1498 carries.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 | Given three commits that each removed one plan with a row, and one released work item in the tree. When the dry run runs, then the section prints the rows of the two newest removing commits' plans and none of the oldest's. It ends with the line saying one older removing commit was not read, naming `seal settle --all-earlier`. | a case in `tests/skills/test_settle.py` asserting the section's text, shown red with the bound alone removed |
| S2 | Given the history of S1, when `seal settle --all-earlier` runs, then the section prints the rows of all three plans and no line of *Scope* item 2. | a case in `tests/skills/test_settle.py` |
| S3 | Given `--all-earlier` beside `--apply`, or beside `--draft`, when the command runs, then it exits 2 with its sentence and reads nothing. | a parametrized case in `tests/skills/test_settle.py`, each sentence pinned |
| S4 | Given one history with one removed plan in the window and another with three, when the dry run runs on each, then both make the same number of git calls. | a case in `tests/skills/test_settle.py` counting the calls through a wrapped `subprocess.run`, shown red against the per-plan reads |
| S5 | Given the #1281 cases at `tests/skills/test_settle.py:1371-1578`, when they run against the batched reads, then each passes. Each history there removes plans in at most two removing commits, so each pins the batched output as it pinned today's. `:1580` fails each batched call in turn and asserts the one `not read:` line with what git said, and exit 0. | the cases as they stand, with `:1541` and `:1580` changed to replace the batched readers |
| S6 | Given a removed plan the batch answers as `missing`, when the dry run runs, then the plan is named as not read at its coordinate, no row of it is printed, and the run exits 0. | a case in `tests/skills/test_settle.py` |
| S7 | Given this repository at the last phase's head, cloned with `git clone --no-local` under the crafter's scratch directory. When `seal settle --released-at <the release branch's base>` runs there, then it finishes under 2 s, makes the same number of git calls with and without `--all-earlier`, and its section holds the plans of the two newest removing commits alone. | replayed by the crafter, with the time, the call counts and the section's bytes recorded in the phase record |
| S8 | Given the next settle's dry run, when the settling session reads step 5, then it reads the bounded section, and runs `--all-earlier` where a kind it reads may have come before the window. | read by the owner at the next settle. `skills/settle/SKILL.md` step 5 states it, and no case holds it |

## Data & interfaces

- `earlier_judgments(root, ref, present, specs, every=False)` returns
  `(groups, unread, older)`. `groups` and `unread` keep today's shapes.
  `older` is the number of removing commits left out of the window, 0 under
  `every`. The parameter's name is the crafter's.
- `survey` takes the same switch and passes it through. `found["earlier"]`
  carries the three values, and `report` prints `older` last in the section.
- The batched readers return dictionaries keyed by path or by commit, so
  that `adding_commit(root, revisions, path)` and `version(root, commit)`
  stay one call of them each for their callers (*Scope* item 5).
- The printed shape:

  ```
  <EARLIER_HEADING, naming the plans the two newest removing commits deleted>

  judged against: <cell>
      <id>  released in vX.Y.Z; removed by <short> (#N)
          <short>^:seal/threads/<id>/frame/plan.md:<line>  <date>  <judgment>
              grounds: <grounds>

  <n> older commit(s) removed plans this section did not read; `seal settle --all-earlier` reads them
  ```

  The words are the phase's to write and to pin (`frame/questions.md` Q1).

## Rule changes

- change
  file: docs/releasing/release-checklist.md
  section: Settle what earlier releases left behind
  from: *The judgments earlier settles removed* holds the rows of
    every plan an earlier settle removed, read from the history with the
    release each shipped in.
  to: *The judgments earlier settles removed* holds the rows of the plans
    the two newest removing commits deleted, read from the history with the
    release each shipped in, and `seal settle --all-earlier` reads the
    older ones (`skills/settle/SKILL.md` *What the dry run shows*).
- change
  file: docs/running/the-run.md
  section: The run
  from: The settle's dry run prints the judgment rows of the released work
    items and, beside them, those earlier settles removed, which the
    history still holds.
  to: The settle's dry run prints the judgment rows of the released work
    items and, beside them, rows earlier settles removed, which the history
    still holds, as far back as `skills/settle/SKILL.md` *What the dry run
    shows* states.
- change
  file: docs/running/what-a-script-gates.md
  section: The checks
  from: of the released plans and, through `git log` and `git show`, of
    every plan an earlier settle removed
  to: of the released plans and, through `git log` and
    `git cat-file --batch`, of the plans the two newest removing commits
    deleted, or of every removed plan under `--all-earlier`

## Removes

This work adds one mechanism, the `--all-earlier` argument. It takes out in
return the unbounded default reading, which moves behind it, and the
per-plan git calls.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The default reading of every plan an earlier settle removed | `skills/settle/scripts/settle.py#earlier_judgments`, the loop over `deleted` | *Scope* items 1 and 3. Its catch record is G11: every recurrence the settle bodies there name rests on the window's rows. |
| Three git calls per removed plan: `git show`, the `git log` of `adding_commit`, and the `git tag --contains` of `version` | `skills/settle/scripts/settle.py#earlier_judgments`, `#adding_commit`, `#version` | The batched reads of *Scope* items 4 and 5. G12 shows them giving the same facts for all 134 plans. |
| The per-commit `git tag --contains` reader of the lowest version tag | `skills/settle/scripts/settle.py#version` | The batched tag read, which `version` calls (*Scope* item 5), so one reader stays. |
| "every row of every `seal/threads/<id>/frame/plan.md` a commit on `--released-at` deleted", and "Each plan is read once, at the parent of the newest commit that deleted it" as the whole of what the section reads | `skills/settle/SKILL.md` *What the dry run shows*, the bullet *The judgments earlier settles removed* | Rewritten in place by *Scope* item 7. |
| "holds the rows of every plan an earlier settle removed" | `docs/releasing/release-checklist.md` *Settle what earlier releases left behind* | `## Rule changes` above, written at the settle after the release |
| "those earlier settles removed", read as all of them | `docs/running/the-run.md` *The run* | `## Rule changes` above, which cites the skill's bullet instead of stating the bound a second time |
| "through `git log` and `git show`, of every plan an earlier settle removed" | `docs/running/what-a-script-gates.md` *The checks*, the `seal settle` row | `## Rule changes` above |
| The `show` and `tag` parameters of the git-failure case | `tests/skills/test_settle.py::Test_main::test_a_git_that_cannot_read_an_earlier_plan_is_named_and_refuses_nothing` | The same case fails each batched read in turn (S5). |

Framed 2026-11-11 by framer, before the build.
