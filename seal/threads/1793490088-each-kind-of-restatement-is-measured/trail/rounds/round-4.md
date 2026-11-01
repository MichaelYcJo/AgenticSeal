# Review round 4: 1793490088-each-kind-of-restatement-is-measured

```seal
target: 291e56b7, fixes be61bfac..291e56b7
```

This is the verifying round over round 3. It reads every commit after round 3's target `be61bfac`: `ee466b3e`, the round 3 record; `39e5dab8`, the orchestrator's fold of findings 1 and 3 and of finding 2's frame half; `69b5f806`, the crafter's fix pass, with its sweeps of each finding's class; and `291e56b7`, the orchestrator's second fold, of the framer cells the closes left for it, together with the close blocks. The base is `origin/release/v0.27.1` at `bf9efcba`. The two folds and the fix pass answer round 3's findings, so a defect in a unit they made takes a `regression:` line.

Carried from earlier rounds, and not run again: round 3's reading of S7 over all 78 pairs; its readings of the bodies of #238, #390 and #506; its opening of the six K13 coordinates the fix pass over round 2 added; and round 2's regeneration of the proofer cases. Re-derived this round: every verdict below, the command blocks *Probes* names, the states of the ten open issues the records place, and the plan's named case.

The stop the orchestrator set in `frame/plan.md` *Judgments of the run*, its last row, is the orchestrator's judgment, and this round does not weigh it. Both findings below are located in the work item's own records. By `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, a fix pass whose findings all stand in the records, and whose commits touch nothing else, owes no verifying round, because the sealer reads every record at HEAD.

## Findings

### 1. The design row that gives D8 code text's lists and figures names as its instances six drifts that the record it cites calls no list or figure

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:135`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:984`
evidence: read `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:135`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/design.md:93`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:904`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:906`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:976`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md:984`, `seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-3.md:30`
regression: round-3#2
```

The unit is the design row *P12 with P8, its lists and figures*, its last cell. `39e5dab8` added the row as the design half of round 3 finding 2's fix, and `291e56b7` rewrote the cell's first clause and kept its second. The frame gives P12 with P8 to K13 (design *The kinds*, row K13, `frame/design.md:93`), and phase 2 *Instances K13* reads the six drifts that open issues hold as that pair's docstrings, "no coordinate, list or figure" (`trail/phases/phase-2.md:906`). The fold added a row that carries only the lists and figures of the pair, and then wrote those six drifts into its known-instance cell. So the defect came from how the fold wrote the cell, not from the frame: the frame's row K13 and the record agree with each other.

Why it matters: D8's answerer reads this row to learn what the audit met in the pair. The row tells it that six drifts held by open issues are instances of a pair D8 carries. D8's *Scope* says three open issues, #238, #390 and #506, hold an instance in its pairs (`trail/phases/phase-2.md:976`). Phase 3 places four of the six, #146, #317, #706 and #1228, in "a pair a kind already reads", K13 (`trail/phases/phase-3.md:30`). Three records give three answers. An answerer who takes the row's answer cannot close the pair as showing no drift. D8's *Scope* also says "A drift a measurement finds is filed as an issue of its own", so that answerer may file again what #146, #315, #317, #706, #710 and #1228 hold.

The grounds:

- The cell says: "the drifts `trail/phases/phase-2.md` *Instances K13* reads from open issues are its instances" (`frame/design.md:135`).
- *Instances K13* says of those six: "It shares no run with another file and is no coordinate, list or figure, so no command here lists it." Each of the six is a sentence about what the code of its own file does (`trail/phases/phase-2.md:906`). Row K13's *Grounds* says the same of them.
- The row's own column says what can stand in both parts: "a list of an enumerable source, or a figure, in a docstring, a comment or a printed message". None of the six is such a list or figure.
- The record does hold one figure in code text out of step with the tree: `hooks/lib/console.py:46`, "The five scripts under `skills/*/scripts/`", where 14 do. *Instances K13* found it by reading K12's instances, and D7 repairs it (`trail/phases/phase-2.md:904`). That figure is the row's known instance, and the row does not name it.
- D8's *Proposed milestone* says each drift the design names "is held by an open issue, was repaired, or stands in #1147's own body" (`trail/phases/phase-2.md:984`). Once the row names the `console.py` figure, that list misses D7.

Effect on the readers. The defect affects D8, one of the filed issues. It does not affect #1038: the comment's table is unchanged by it, and D6 does not cite the row.

```markdown
frame/design.md, *Pairs no command of this audit reads*, row *P12 with P8, its lists and figures*, its last cell:
what K13 reads in code text is stated in `trail/phases/phase-2.md` *The table*, row K13; the figure at `hooks/lib/console.py:46`, which `trail/phases/phase-2.md` *Instances K13* found by reading K12's instances, is its known instance, and D7 repairs it

trail/phases/phase-2.md *Drafts*, D8, *Proposed milestone*, its second sentence:
No work item needs these pairs measured before it starts: each drift in them that the design and `trail/phases/phase-3.md` *Whether the frame holds* name is held by an open issue, was repaired, is D7's, or stands in #1147's own body, which closes with #1147 (design G10).
```

```seal
verdict: fixed 0732bcee
answer: The finding holds. The orchestrator rewrote the third cell of the row *P12 with P8, its lists and figures* in `frame/design.md` in place: its known instance is now the figure at `hooks/lib/console.py:46`, which D7 repairs, and the six drifts *Instances K13* reads, none of them a list or figure, are no longer named there. D8's *Proposed milestone* in `trail/phases/phase-2.md` counts D7 among the holders of the drifts it names. `frame/plan.md` *Judgments of the run* records the fold.
```

### 2. The second fold changed four framer cells and no row of *Judgments of the run* records it

```seal
severity: should
location: `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md:69`
evidence: executed `git show --word-diff=plain 291e56b7 -- seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/`, `git show bf9efcba:docs/the-review-record.md`
regression: round-3#1
```

The unit is `frame/plan.md` *Judgments of the run*, its last row. `39e5dab8`, the commit round 3 finding 1 closes `fixed`, added the row, and `291e56b7` changed its grounds. The frame's rule for the table is `docs/the-review-record.md` *The run* at `bf9efcba`: "a decision folded into the frame after the frame was committed" is a judgment, and the orchestrator writes it as a row (`docs/the-review-record.md:493`). `291e56b7` folded four cells and changed the row's grounds, but left its judgment naming only the first fold. So the defect came from how the fold was written, and the frame holds.

Why it matters: the settle reads these rows, grouped by the document they stand on, to rewrite guidance where one kind of judgment keeps costing rounds. This run's folds are such a kind. A fold with no row is not counted there. One of the four cells changes what D8 measures, and no record gives its grounds. The defect does not affect #1038 or the filed issues.

The grounds, from the word diff of `291e56b7` over the frame (executed):

- Design *Pairs no command of this audit reads*, its opening: D8's method "measures the pair with the command of the kind nearest it" became "by the method its *Scope* states". The closes of round 3 findings 1 and 4 left this cell for the orchestrator.
- The row *P12 with P9*: "a coordinate or figure" became "a coordinate, list or figure". No finding asked for this, and the change widens what D8 measures. It does match phase 3's placement of #506's test-docstring enumeration in that pair (`trail/phases/phase-3.md:15`).
- The row *P12 with P8, its lists and figures*: its citation of phase 3 became a citation of phase 2's row K13. The close of finding 6 left this cell for the orchestrator.
- Plan row A10: "design G4's three answers" became "the answers design G4 defines" (the close of finding 6).
- The last row's judgment still reads "Round 3's findings 1 and 3, and finding 2's frame half, are folded by the orchestrator in place". It names none of the four cells.

```markdown
frame/plan.md *Judgments of the run*, a row after the last:
| 2026-11-01 | The framer cells that the closes of round 3's findings 1, 4 and 6 left for the orchestrator are folded in place. Design *Pairs no command of this audit reads* cites D8's *Scope* for its method. Its row *P12 with P9* names a list beside a coordinate and a figure, and its row *P12 with P8, its lists and figures* cites `trail/phases/phase-2.md` *The table* row K13 for what K13 reads in code text. Plan row A10 cites the answers G4 defines, with no count | Each cell stated, a second time, a fact whose home is another record, as those closes say. The *P12 with P9* row was narrower than the instance `trail/phases/phase-3.md` *Whether the frame holds* places in it, #506's test-docstring enumeration. As with the earlier folds, none moves a decision of the frame | `docs/the-review-record.md` *The run*; `docs/the-record-layout.md` *A fact of a work item has one record, and every other record cites it by path and heading* |
```

```seal
verdict: fixed 0732bcee
answer: The finding holds. A row of `frame/plan.md` *Judgments of the run* now records the four cells the fold at `291e56b7` changed, with the grounds for widening *P12 with P9* to lists: phase 3 places #506's test-docstring enumeration in that pair, and the row's second column named only coordinates and figures.
```

## Confirmations

```seal
confirms: round-3#1
```
What holds: the fourth bullet after *The kinds* no longer cites G10 (`frame/design.md:107`). The issue's *Order* line against the milestone's order is answered once, in the row *P11 with P11* (`frame/design.md:133`). The section's opening no longer states D8's method itself: it cites D8's *Scope* (`frame/design.md:112`). So the second statement of the method that the close left for a fold is gone too. A `grep -n nearest` over the frame files, `gaps.md` and the phase records prints nothing (executed).

```seal
confirms: round-3#2
```
What holds: lists and figures in code text now have an answerer, the row *P12 with P8, its lists and figures* (`frame/design.md:135`). Row K13's *Held twice* cell names that row, and its *Decision* reads "nothing for the lists in shipped `.md`" (`trail/phases/phase-2.md:29`). *Instances K13*'s open part names "a figure or a list in code text" and gives it to D8 (`trail/phases/phase-2.md:925`). The close's two further instances hold as well. `audit2.py#lists` and `#figures` take `.md` files and leave out `.ko.md` (read in the setup's `audit2.py`), while `#coordinates` reads every shipped file, so the cell's "they read the coordinates" holds for the editions and the template. The four `.ko.md` files at `bf9efcba` are the four pairs *Command K4* prints (executed). `templates/setup/hygiene.yml` at `bf9efcba` holds no figure about the tree and no list of a source's members (read, its 90 lines). Finding 1 of this round is a defect the fold wrote into the row's last cell. It is not the defect this finding named.

```seal
confirms: round-3#3
```
What holds: G4 now says "The list is whole over the parts because every pair is answered", and that the parts are not the whole tree and the files no part holds are D8's (`frame/design.md:10`). Plan row A8 claims only that every pair is answered, and gives the files no part holds to D8 (`frame/plan.md:39`). The preamble names the files in no part as D8's (`trail/phases/phase-2.md:994`). G4's first sentence still reads "a method that makes it whole". The same cell narrows the claim two sentences later, so a reader of G4 meets no claim the cell leaves standing. *Command comment*, run again at `291e56b7`, prints what phase 3 states (*Probes*).

```seal
confirms: round-3#4
```
What holds: D8's *Scope* now gives each kind of row its own method (`trail/phases/phase-2.md:976`). Rows that name a kind, a kind's reader or a kind's mechanism use that kind's command. Rows that name none use a command D8's framer writes. Either kind of row may be closed with the reason no record shows drift. Each row of `frame/design.md:116-136` falls under one of the two (read). The P4 with P9 row names K6's pins, a mechanism. The P8 with P10 row names *Command regenerate*, a reader. The P12 with P8 row names K13. The P8 with P9 and P11 with P11 rows name an instance and no kind, so they take the second method. D8's title no longer says "nearest".

```seal
confirms: round-3#5
```
What holds: `trail/phases/phase-1.md` *Instances K5* names #379 among its overlaps and gives the case's repair to #379 (`trail/phases/phase-1.md:561`). Phase 2's *Command tracker* list holds #315 and #379 (`trail/phases/phase-2.md:829`). Phase 3's *Command tracker*, run again, does not return #315 or #710 (executed). So the four K13 issues phase 3 lists are the ones its loop returns. The ten open issues the records place, #146, #238, #315, #317, #379, #390, #506, #706, #710 and #1228, are all open, in the milestones the records give them (executed: `gh issue view`).

```seal
confirms: round-3#6
```
What holds: phase 3's *Phase-boundary run* names the modules with no count (`trail/phases/phase-3.md:68`). Its milestone paragraph cites *Command tracker*'s line (`:32`). D8's *Proposed milestone* cites phase 3 for the counts (`trail/phases/phase-2.md:984`). Phase 3's item on #238 reads the line "against #238's measure" (`trail/phases/phase-3.md:15`). The close's further corrections also stand, each now a citation (read in the word diff of `69b5f806`): *Instances K14* to *Instances K5*, *Instances K11* to design row K9, phase 3's *What this phase changed* to round 2 finding 2's close, and D8's *Scope* to phase 3. The three framer copies the close left for the orchestrator were folded at `291e56b7`, and the plan's last row no longer counts the rounds' findings. A search over the frame files, `gaps.md` and the phase records for the milestone's count and the comment's length finds each once, at its home (executed: `grep -n -i`). The two "1641 passed" lines are each their own run's result.

```seal
confirms: none
```
What matched: each command block run again from a clone at `291e56b7` printed the figure its record states (executed; *Probes*). *Command comment* printed `join exit 0`, 26989 bytes and 26987 characters, which is what `trail/phases/phase-3.md:70` states, and each of its 16 table lines stands whole in the two records. Phase 1's *Command K3* printed `K3: 2 passages over 422 file pairs`. Its *Command K4* printed `outline same` for four pairs and `sections whose tokens or figures differ: 10`. Phase 2's *Command coordinates* printed `path:line coordinates 9; path#name coordinates 113; printed for reading 3`, *Command lists* `blocks naming three or more and half of a source 33`, *Command figures* `figure candidates with no moment on their line 33`, and *Command nones* `check: none lines 49 in 40 sections, naming 26 readers`. Phase 3's *Command parts* printed the eleven files phase 3 names. Phase 3's *Command tracker* exited 0 with no stderr. Its `grep -c` printed 0, its log line was `8350c578`, and its milestone line was `backlog: docs drift open=0 closed=9`. Every figure reproduced.

```seal
confirms: none
```
What matched: the rest of what blocks a seal. No decision of the records stands against the policy at `bf9efcba`. The stop in the plan's last row is a judgment `docs/the-review-record.md` *The run* leaves to the orchestrator, written as a row with its grounds. The homes it names, `gaps.md` in the diff and the pull request body, are rungs 1 and 4 of that section's table. No draft duplicates an open issue: phase 3's tracker, run again, returns no open issue that carries a whole pair D8 names. D6 is a comment for #1038, and D7 leaves the six drifts open issues hold to those issues. Finding 1 is the one place where D8's answerer is pointed toward what open issues hold. The claims of coverage stand narrowed where round 3 found them, and the gaps they leave are named in `gaps.md` *Not done* and in D8. Both *Done when* bullets of #1147 can be met by the records. The table is the preamble and the 14 rows *Command comment* joins, 26987 characters, under the 65,536 that design S5 gives. Each decision that changes the tree has a draft, D2 to D8, which the orchestrator files after the seal (design G3, G8).

```seal
confirms: none
```
What matched: S6 and the plan's named case. `git diff --name-only bf9efcba..HEAD` prints eleven paths, each under `seal/threads/1793490088-each-kind-of-restatement-is-measured/` (executed). `bin/test tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview -q` in the clone printed `1 passed` (executed). The pull request changes no path outside `docs/` and `seal/`, and the repository declares no `seal/parity.md`, so the round block carries no `original:` line.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check. The records hand them over as `unverified` and name the orchestrator, which is an honest label. This round leaves two findings open, so what comes due is the orchestrator's choice: fix or defer them, then the broad run and the sealer's spawn | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate` once the rounds settle, then the sealer's spawn |
| How findings 1 and 2 are closed under the stop the plan's last row sets: fixed in place, or `deferred` with a close block naming the home. Both stand in the records alone. Finding 1 changes a framer file and a phase record, and finding 2 changes `frame/plan.md`, whose rows the orchestrator writes. Each regression's route is the orchestrator's, from the sentence each finding's grounds give | `seal/threads/1793490088-each-kind-of-restatement-is-measured/frame/plan.md` *Judgments of the run* | the orchestrator, by `docs/the-review-record.md` *The run* |

## Probes

| Command | Result |
|---|---|
| `git clone -q --no-local <worktree> <scratch>/round-4/clone`, checked out at `291e56b7`, `origin` set to the GitHub remote | the clone, 67 tags |
| `python3 -I <scratch>/round-4/test_tmp_extract.py <records> <scratch>/round-4/blocks <scratch>/round-4/S`: writes each `#### Command <X>` sh block of the three phase records to a file, with phase 1's `mktemp` line pointing at the round's scratch directory | 38 blocks |
| phase 1's and phase 2's *Command setup*, then *Command comment*, phase 1's *Command K3* and *Command K4*, phase 2's *Command coordinates*, *Command lists*, *Command figures* and *Command nones*, and phase 3's *Command parts*, each with `sh` from the clone | exit 0 each, no stderr; the figures under *Confirmations* |
| a `grep -qxF` of each table line of the joined comment over the two phase records | 16 lines, no miss |
| phase 3's *Command tracker*, whole | exit 0, 67 lines, no stderr; #315 and #710 not among the first loop's returns |
| `gh issue view` 146, 238, 315, 317, 379, 390, 506, 706, 710 and 1228 | each open, in the milestone the records give it |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview -q` in the clone | 1 passed |
| `git show bf9efcba:templates/setup/hygiene.yml`; `git ls-tree -r --name-only bf9efcba` filtered to `.ko.md` | no figure about the tree and no list of a source; four editions |
| `git show --word-diff=plain` of `39e5dab8`, `69b5f806` and `291e56b7` over the work item; `git show bf9efcba:docs/the-review-record.md`, *The run*; `git show bf9efcba:skills/code-review/orchestration.md`, *Orchestrator: the run ends with a verifying round* | the diffs and the policy text findings 1 and 2 quote |
| `git diff --name-only bf9efcba..HEAD` | eleven paths, all under the work item |
