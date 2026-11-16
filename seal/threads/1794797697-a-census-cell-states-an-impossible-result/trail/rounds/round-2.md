# Review round 2: 1794797697-a-census-cell-states-an-impossible-result

```seal
target: 1881efefc, fixes e9f67c050..1881efefc
```

This is a verifying round. It answers the four findings round 1 closed, reviews the diff `598315485..1881efefc` as code, and reads every record of the work item whole at `1881efefc`, in a `git clone --no-local` of the repository checked out at the target.

Carried from round 1 and not re-established: the preload sizes of `skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` (9,322 and 12,029 bytes; neither file is in the fix diff), the G10 version search at `75a725770`, the `## Removes` and G6 searches, and the coordinates of the cited sections in G5 to G11. Re-established: the size of `agents/framer.md` at each commit, the reach of `9dc095ac6` and `dda87704c`, S8's search at `dda87704c`, every quote of `pr.md`, and the narrow modules.

## Findings

### 1. The pull request body and the plan's mechanism row give the paragraph's cost as 1,226 bytes, and round 1 finding 3's wording made it 1,279

```seal
severity: should
location: `seal/threads/1794797697-a-census-cell-states-an-impossible-result/pr.md:4`, `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/plan.md:49`
evidence: executed `git show <commit>:agents/framer.md | wc -c` at `75a725770`, `19a111be9`, `598315485` and `1881efefc` (14,533, 15,759, 15,759, 15,812); `bin/seal pr-body --body ../body.md seal/threads/1794797697-a-census-cell-states-an-impossible-result` (the body's line 4 carries the 1,226 figure); read `seal/threads/1794797697-a-census-cell-states-an-impossible-result/trail/phases/phase-1.md:6`
regression: round-1#3
```

Why it matters: the unit is the rule paragraph of `agents/framer.md`, which `d66f6eb75` rewrote for round 1 finding 3. The frame asked for C2's first kind to cover a line the build changes. The fix added ", or changes so that the search no longer matches it," to the paragraph, 53 bytes. The records that state the paragraph's size were not touched. The defect came from the gap between the two commits: `414648619` wrote the mechanism row before `d66f6eb75` grew the paragraph.

At `1881efefc`, `agents/framer.md` holds 15,812 bytes against 14,533 at `75a725770`, so the paragraph adds 1,279 bytes. `pr.md:4` quotes "The paragraph adds 1,226 bytes, not the 900 design G14 estimated." The quote is word for word at `trail/phases/phase-1.md:6`, which states phase 1 at `19a111be9` and is right there. In the pull request body the sentence reads as the cost of the change the pull request merges, and that cost is now 1,279. `frame/plan.md:49`, the row added for round 1 finding 1, says "its cost is the bytes `trail/phases/phase-1.md` counts". That row answers *What it removes* of `CONTRIBUTING.md` *What a change to a gate must carry*, which asks what the mechanism catches against what it costs. The settle that weighs the rule reads the cost there.

The fix reaches both statements. `trail/phases/phase-1.md:6` stays as the record of phase 1. Design G14's 900 is an estimate dated at `75a725770` and stays too. The quote below also puts "It removes nothing" into the body in so many words, which round 1 finding 1 asked for and the body still says only through the fold that stays.

```markdown
frame/plan.md:49, the Grounds cell:
Its prompt budget is zero: it puts no question in front of a person. It removes nothing, for the reason `frame/design.md` *Removes* gives, and its cost is 1,279 bytes per framer spawn: `agents/framer.md` holds 15,812 bytes at `d66f6eb75` against 14,533 at `75a725770`, the 1,226 `trail/phases/phase-1.md` counts and the 53 that round 1 finding 3's wording adds (executed: `wc -c`)

pr.md:4, replacing the quote of trail/phases/phase-1.md:
- "It removes nothing, for the reason `frame/design.md` *Removes* gives, and its cost is 1,279 bytes per framer spawn: `agents/framer.md` holds 15,812 bytes at `d66f6eb75` against 14,533 at `75a725770`, the 1,226 `trail/phases/phase-1.md` counts and the 53 that round 1 finding 3's wording adds (executed: `wc -c`)" (`frame/plan.md` *Judgments of the run*, the row titled "What the rule carries as a mechanism")
```

Where the fix pass moves the new quote below `pr.md`'s prompt-budget quote, the two read in the row's order. A later edit of `agents/framer.md` before the pull request owes the same figure again.

```seal
verdict: fixed 22664790a
answer: The finding holds, and the fix takes the proposed text. pr.md quotes the rewritten Grounds cell of the row titled "What the rule carries as a mechanism" in place of the phase record's 1,226-byte sentence, in 5550d6ae7, and the row itself carries the 1,279-byte figure in 22664790a. agents/framer.md holds 15,812 bytes at HEAD and 14,533 at 75a725770 (executed: wc -c). trail/phases/phase-1.md keeps its figure, since it states phase 1 at its own commit. The fix touched this work item's records alone.
```

### 2. Plan row A3 now says #1500 paid a phase-record paragraph and a judgment row for each of three cells, and it paid two of each

```seal
severity: should
location: `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/plan.md:19`
evidence: read `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md:119-120`, `seal/threads/1794530293-three-compatibility-paths-still-stand/trail/phases/phase-2.md:5`, `seal/threads/1794530293-three-compatibility-paths-still-stand/trail/phases/phase-2.md:13-31`; executed `git diff 598315485..1881efefc -- seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/plan.md`
regression: round-1#2
```

Why it matters: the unit is plan row A3, which the framer's fold in `414648619` rewrote for round 1 finding 2. The frame asked for the count of failed cells to be three, stated once in G2. The fold replaced "as #1500 paid twice in one run (G2)" with "as #1500 paid for each cell design G2 lists, in one run". The defect came from carrying the per-cell count into a sentence that counts costs, not cells.

The row says each wrong search costs "a crafter's search for the cause, a paragraph of a phase record, the orchestrator's re-run and a judgment row", and that #1500 paid this for each of G2's three cells. #1500's records show two judgment rows for the three cells: row 1 (`frame/plan.md:119`) folds phase 1's cell, and row 2 (`:120`) folds phase 2's cell and S8 together. Phase 2's crafter found S8 in the same paragraph as phase 2's cell (`phase-2.md:13-31`), opened as "The frame held against the tree, except for two searches" (`:5`). So #1500 paid two paragraphs and two judgment rows, which the old wording "twice" stated correctly. A3 is the cost side of the "no rule" alternative, and the settle that weighs whether the rule stays reads it. A3's verdict compares the rule against one fold's cost, so the verdict stands. Only the account of what #1500 paid is wrong.

```markdown
frame/plan.md:19, the Failure scenario cell of A3:
Each search a framer writes wrong costs a crafter's search for the cause, a paragraph of a phase record, the orchestrator's re-run and a judgment row. #1500 paid this in one run for the cells design G2 lists, and phase 2's cell and scenario S8 shared one crafter, one phase-record paragraph and one judgment row. The cell also reads as a claim no build can satisfy until it is folded
```

The snippet names no count, so G2 stays the one statement of it. G4's "a fold for each cell G2 lists" and plan row 46's "all three folds" hold, since #1500's row 2 folds S8 by name, and the fix leaves them.

```seal
verdict: fixed 22664790a
answer: The finding holds. The framer folded the proposed text into row A3's Failure scenario cell word for word, in 22664790a, and found no other statement of the frame that charges a phase-record paragraph or a judgment row to each cell. G4's fold for each cell stands, since #1500's second judgment row folds phase 2's cell and S8 together by name. The fix touched this work item's records alone.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `frame/plan.md:49` carries the row on what the rule carries as a mechanism. `pr.md:6-8` quote its prompt-budget sentence and two sentences of the `## Removes` why. Each stands word for word at `frame/plan.md:49` and `frame/design.md:68` with whitespace collapsed (read). `bin/seal pr-body` composed the body into the round's scratch directory, exit 0, and the three quotes reach it (executed). The body now says the prompt budget is zero, gives the catch record, and says why the fold that caught the cells stays, which answers *What it removes* through why none can go. Finding 1 of this round names the cost figure the body still gets wrong, and its snippet also puts "It removes nothing" into the body.

```seal
confirms: round-1#2
```
What holds: `changelog.md:3` says "three such cells", and `changelog.md:10` says "Three cells". `frame/plan.md:44` names "the frame cells `frame/design.md` G2 lists". `frame/design.md:68` names the two *Verified by* searches and S8's *Verifiable how* search, and says S8's is the case C3 covers. G2 at `frame/design.md:10` lists the three and states the count once (read). Against #1500's records, S8's cell reads "then 2027-02-07 stands only in #1492's records other than its `changelog.md`" at `9dc095ac6` (executed: `git show` of that `frame/design.md`, line 167). Its search at `dda87704c` prints lines under `seal/threads/1794271937-the-readme-narrates-three-migrations/` alone, its `changelog.md:6` among them, as G3 now says (executed). Finding 2 of this round is the one sentence the fold made wrong.

```seal
confirms: round-1#3
```
What holds: `agents/framer.md:177-178` reads "A line the build removes, or changes so that the search no longer matches it, is named by a *Scope* item or a `## Removes` row." C2 (`frame/design.md:55`), C5 (`:58`), G5 (`:13`) and `changelog.md:3` carry the same kind (read). The five narrow modules passed in the clone at `1881efefc`, line wrap among them (executed, see *Probes*). The paragraph still states C1 to C5 as round 1 read them. `agents/framer.md:181` is 51 columns, a ragged break left by the rewrap, which the line-wrap case allows and no reader acts on. Plan row A5 (`frame/plan.md:21`) still names the kinds as "one the build removes, one the design keeps or one in an excluded file". The row argues that sorting lines into kinds is a judgment of meaning, so no reader takes the kind's boundary from it, and the round opens no finding there.

```seal
confirms: round-1#4
```
What holds: G2 (`frame/design.md:10`) names the squash `c97514d67` and the pull request ref, and G3 (`:11`) cites both commits by name with their paths in prose (read). `git ls-remote origin refs/pull/1549/head` printed `c02ece3f3`, and `git merge-base --is-ancestor` exited 0 for `9dc095ac6` and `dda87704c` against it (executed). `gh pr view 1549` names `c97514d676b7` as the merge commit, merged 2026-11-15T23:51Z, which is 2026-11-16 in the session's zone, as plan row 48 says. `git ls-remote origin refs/heads/refactor/1500-three-compatibility-paths-still-stand` printed nothing (executed). The clone lacked `9dc095ac6` until `git fetch <origin url> pull/1549/head`, and then held both commits (executed), as G2's last sentence says. The close's reason for not taking round 1's `<commit>:<path>` snippet holds: `tests/text/test_a_cited_commit_outlives_the_squash.py#REACHING` counts only `main` and release refs, so that form would be refused (read).

What matched: the records read whole at `1881efefc`. `routing.md`, `frame/questions.md`, `gaps.md` and `trail/phases/phase-1.md` are unchanged since round 1 and still agree with the tree, except phase 1's byte figure, which finding 1 takes up where `pr.md` and the plan carry it. `pr.md`'s other quotes, at `frame/plan.md:11` twice, `:24`, `:44` and `gaps.md:9`, stand word for word (read). Both language keys of `seal/config.json` name English, so no `pr.<lang>.md` is owed and none stands (read).

What matched: `gaps.md` still labels the suite, the lint and the format check `unverified` and names the orchestrator as their answerer. The label is honest, since the orchestrator's account says the full suite and the broad gate have not run.

What matched: the orchestrator's claim that `chain_check.py` exited 0 and named a verifying round as owed. Run before this record, it exited 0 and named findings 2 and 3 of round 1 and commit `d66f6eb75` as owing a verifying round (executed). It printed no notice at a line of a `frame/design.md`.

No new test is in the fix diff, so no case was read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD (contract rule 2) | `seal/config.json` `Broad gate` | the orchestrator, once the rounds settle |
| Whether a framer spawned from 0.38.2 on runs the search before it writes the cell; no paid run was made | `seal/threads/1794797697-a-census-cell-states-an-impossible-result/gaps.md:9` | the settle of 0.38.2, reading the next frames' `## Grounding` |
| G4's count of 11 phase rows in 9 plans, a sample the frame labels as one; carried from round 1 and not recounted | `seal/threads/1794797697-a-census-cell-states-an-impossible-result/frame/design.md:12` | nobody owes it: no claim of the build rests on the number |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_release_hygiene.py tests/text/test_a_cited_commit_outlives_the_squash.py tests/text/test_a_record_carries_no_comment.py -q`, in the clone at `1881efefc` | 168 passed, 5 warnings, exit 0; the warnings are cited-section notices on other work items' pending rule changes |
| `git show <commit>:agents/framer.md \| wc -c` at `75a725770`, `19a111be9`, `598315485`, `1881efefc` | 14,533, 15,759, 15,759, 15,812 |
| `bin/seal pr-body --body ../body.md seal/threads/1794797697-a-census-cell-states-an-impossible-result`, in the clone | exit 0; the body carries `pr.md`'s nine quotes, the 1,226 figure on its line 4 |
| `git grep -n 2027-02-07 dda87704c -- .`, in the clone after `git fetch <origin url> pull/1549/head` | lines under `seal/threads/1794271937-the-readme-narrates-three-migrations/` alone, `changelog.md:6` among them |
| `git ls-remote origin refs/pull/1549/head`; `git merge-base --is-ancestor` of `9dc095ac6` and `dda87704c` against `c02ece3f3`; `git ls-remote origin refs/heads/refactor/1500-three-compatibility-paths-still-stand`, in the main checkout | `c02ece3f3`; exit 0 twice; nothing |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.2 --root <the branch worktree> --worktree`, before the record | exit 0; a verifying round owed for round 1 findings 2 and 3 and for `d66f6eb75`, the gate record and the guarantee missing, no notice on `frame/design.md` |
