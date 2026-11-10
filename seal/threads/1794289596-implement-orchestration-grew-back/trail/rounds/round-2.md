# Review round 2: 1794289596-implement-orchestration-grew-back

```seal
target: 10fc3a7f7, fixes 9c17b22bc..10fc3a7f7
```

This round answers round 1's three closed findings and reviews the fix
range `9c17b22bc..10fc3a7f7`. The range holds the framer's fold
(`bee4a509c`), the fix pass (`f07bd7f60`, `44c22ee4f`), the orchestrator's
rewrite of counts (`d37fafaa9`), round 1's record (`3d86761db`), the merge
of `release/v0.37.2` at `1959c3ea1` (`a1a93b3b1`) and the orchestrator's row
on that merge (`10fc3a7f7`). The chain check reads no merge commit, so this
round read what the merge produced in `agents/proofer.md`,
`skills/implement/orchestration.md` and
`tests/text/test_the_rules_have_one_owner.py`. It applies the tree's
`agents/proofer.md` at `10fc3a7f7`, not the installed 0.37.1 copy it was
spawned with. The two differ in the dated-section sentence at `:126-130`
and in the verifying-round paragraph at `:140-142`, which now cites
`skills/code-review/SKILL.md` *Earlier rounds*.

Carried from round 1 as coordinates and not re-derived: the homes of
*Removes* rows 9 to 21, the S5 sentence comparison of the two new files,
and S2's read of the order section against D1. None of their files changed
in the range, except the body at the merge (the drain's first row) and at
`f07bd7f60` (the sentence of finding 1). Every verdict below is this
round's own.

## Findings

### 1. The changelog's first item and its `pr.md` quote say the body holds 5,223 words, and at the target it holds 5,233

```seal
severity: should
location: `seal/threads/1794289596-implement-orchestration-grew-back/changelog.md:3`, `seal/threads/1794289596-implement-orchestration-grew-back/pr.md:1`, `seal/threads/1794289596-implement-orchestration-grew-back/gaps.md:7`
evidence: executed `wc -w skills/implement/orchestration.md` at `10fc3a7f7` (5233), and `git show <commit>:skills/implement/orchestration.md | wc -w` at `f07bd7f60` (5223), `9c17b22bc` (5225), `1959c3ea1` (7321), `df775c52c` and `v0.37.1` (7311 each); read `changelog.md:3`, `pr.md:1`, `gaps.md:7`, `frame/design.md:61`, `frame/plan.md:60`, `frame/plan.md:82`
regression: round-1#1
```

The unit is the count in the first *Changed* item of `changelog.md`, which
`f07bd7f60`, the fix to round 1 finding 1, set to 5,223, and the `pr.md`
quote of it, which `d37fafaa9` set to match. S1 (`frame/design.md:61`)
counts the body at HEAD with the release branch merged in, and
`frame/plan.md:60` takes that count after the merge. The fix recorded the
count before the merge, the merge at `a1a93b3b1` added #1476's 10 words, and
`10fc3a7f7` recorded 5,233 in `frame/plan.md:82` alone. So the defect came
from the merge's count reaching one record of four.

Why it matters: the item is the release note a person reads. It says
"holds 5,223", and the file at the target holds 5,233. `pr.md` quotes the
same sentence, so the pull request body says it too. `gaps.md:7` still
lists S1 after the merge under *Not verified*. Its two answerers have now
answered it: the orchestrator at `frame/plan.md:82`, and this round by the
same count. A sealer reading the open row reads S1 as unanswered.

The fix reaches the three statements below. `frame/design.md:114-116` and
`gaps.md:20` give 5,225 at `02740215a`, which that commit holds, so they
stand. `frame/questions.md:18` says the count after the merge "is read again
then, by the orchestrator", which `frame/plan.md:82` did, so it stands. The
three locations are records alone.

```markdown
<!-- changelog.md:3, the second sentence of the first item -->
It held 7,311 words at 0.37.1 and holds 5,233.

<!-- pr.md:1, the quote of that item, rewritten with it -->
- "**`skills/implement/orchestration.md`, which every orchestrating session opens before its first edit, is back under 0.30.0's size (#1477).** It held 7,311 words at 0.37.1 and holds 5,233." (`changelog.md` *Changed*, the first item)

<!-- gaps.md:7, the row closed in place -->
| closed `frame/design.md` S1 once the release branch, #1476's change among it, is merged in. The body holds 5,233 words at `a1a93b3b1`, the merge of the release branch at `1959c3ea1`, 9 under the bound of 5,242 (5,223 at `f07bd7f60`, 5,225 at `02740215a`). | the orchestrator, by `wc -w skills/implement/orchestration.md` at `a1a93b3b1` (`frame/plan.md` *Judgments of the run*, the row of the merge), and the proofer by the same count at `10fc3a7f7` (`trail/rounds/round-2.md`) |
```

### 2. `frame/plan.md` *Alternatives considered* row 20 counts round 1's wording at 54 words and the body at 5,236, where a like-for-like count gives 52 and 5,234

```seal
severity: should
location: `seal/threads/1794289596-implement-orchestration-grew-back/frame/plan.md:40`
evidence: executed `sed -n '67,71p' trail/rounds/round-1.md | wc -w` (52, the offered sentence alone); `git show 9c17b22bc:skills/implement/orchestration.md | sed -n '316,319p' | wc -w` (45, the old sentence's four lines, which end with the next sentence's "Where the"); `wc -w` on the old sentence alone (43) and on the built sentence alone (41); read `frame/plan.md:40`, `frame/plan.md:81`, `frame/design.md:123`
regression: round-1#1
```

The unit is row 20, which the framer's fold for round 1 finding 1 added at
`bee4a509c` and whose counts the orchestrator rewrote at `d37fafaa9`.
`frame/plan.md:81` says the framer took D4's wording (`frame/design.md:123`)
over round 1's because round 1's would pass S1 once #1476 merges in, and
row 20's counts are that reason. `bee4a509c` wrote "44 words to 54" and
5,235, and `d37fafaa9` rewrote it to "43 words to 54" and 5,236. The defect
came from counting the two sentences two ways: 43 is the old sentence alone,
and 54 is the four lines the offered sentence would fill, which carry the
next sentence's first two words. The same lines at `9c17b22bc` give 45.

Why it matters: the row labels its counts `executed`, and two of them do
not reproduce. The verdict still stands, by a narrower margin than the row
gives. The offered sentence adds 9 words, not 11, so the body would hold
5,234 at `9c17b22bc` and 5,244 after #1476's 10 words, 2 over the bound.
The count "41 words (`f07bd7f60`)" in the Verdict cell holds (executed).

The snippet cites `1959c3ea1`, the release branch's commit with #1476
squashed in, which gives the same 7,321 (executed). The location is a frame
file, so the orchestrator routes the fold.

```markdown
<!-- frame/plan.md:40, row 20's Failure scenario cell -->
The body's sentence grows from 43 words to 52 (executed, `wc -w` on each sentence alone), the body from 5,225 to 5,234, and #1476's merge adds 10 more (executed, `git show 1959c3ea1:skills/implement/orchestration.md \| wc -w`, 7,321 against 7,311), which passes S1's bound of 5,242 by 2 words.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the condition for opening `skills/implement/merge-order.md` is
the start of a work item in a release that holds another, before its first
edit, in all four places the finding named. The body at
`skills/implement/orchestration.md:316-319` reads it in D4's words
(`frame/design.md:123`), and `merge-order.md:3-4` says it in its own. The
first *Changed* item and the first *Process changes* row of `changelog.md`
say the same (read). "Before its first edit" covers a framer's spawn:
`skills/implement/SKILL.md:285` places the routing answer "before the first
edit, and so before a framer is spawned" (read). `git grep` for
"first framer" and "two or more work items" finds only records quoting the
old wording (executed). `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
is green on the two openings (executed, below). Findings 1 and 2 above also
name this finding, on their `regression:` lines, for units its fix made.

```seal
confirms: round-1#2
```
What holds: `frame/plan.md:15` holds the paste-ready sentence word for word,
naming `#test_the_orchestration_offers_the_vocabulary_the_parser_accepts`
and saying no case reads the values the boxes write (read). No case was
added. *Alternatives considered* row 19 (`frame/plan.md:39`) records why,
and its claim that no case read those values before this work either is
round 1's probe result. So `frame/design.md:163` stands as written (read).

```seal
confirms: round-1#3
```
What holds: `frame/plan.md:9`, G10's last sentence at `frame/design.md:18`
and the Verdict cell at `frame/plan.md:23` hold the paste-ready text, the
last two naming *Scope* items 1, 2, 3, 5, 6 and 9 as D3 counts them (read).
The fold also dated *Overlap with the release* (`frame/plan.md:56`) and
rewrote *Alternatives considered* row 1's verdict to the new condition. It
also rewrote G18's last sentence to say that *Removes* row 17 takes two
other sentences of the ladder. Each agrees with the target (read).

What matched: S1 after the merge. The body holds 5,233 words at
`10fc3a7f7`, 9 under the bound of 5,242 (executed). `10fc3a7f7` changes
`frame/plan.md` alone, so the count at `a1a93b3b1` that `frame/plan.md:82`
claims is the same.

What matched: the merge in the three shared files. `git diff 1959c3ea1
a1a93b3b1` on `agents/proofer.md` and `tests/text/test_the_rules_have_one_owner.py`
shows this item's changes alone: the dated-section sentence at
`agents/proofer.md:126-130` and the fold case (executed). `git diff
3d86761db a1a93b3b1` on the three files shows #1476's alone: the notice
sentence at `agents/proofer.md:63-66`, the verifying-round paragraph at
`:140-142`, the drain's first row of the body, which now cites the core's
row *No fix that no round reads*, and the rules 21 and 22 of the owner case
with their carriers (executed). Neither side's text is lost. S8 holds in
the merged `agents/proofer.md:126-130` (read). The four modules
`frame/plan.md:82` names exit with 151 passed (executed), as it claims.

What matched: `frame/questions.md` Q1's answer. The merge changes the body
at the drain's first row alone (executed, the diff above), so the late
move's sentence that moved to `merge-order.md` was not changed by #1476.

What matched: `pr.md`. Each of its nine quotes stands word for word, runs
of whitespace collapsed, in the file its coordinate names (executed, a
`python3` comparison). Quote 1 stands at its source and shares that source's
count, which finding 1 corrects in both. `Commit and pull request language`
is English, so no `pr.<lang>.md` is owed.

What matched: the records that state the present. `routing.md`, the three
frame files, `gaps.md` and `changelog.md` were read whole at `10fc3a7f7`.
Outside the two findings, no sentence is contradicted by the target (read).
`frame/design.md` D3 (`:112-116`) gives 5,225 at `02740215a`, which that
commit holds.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD. The narrow modules this round ran are not it, and contract rule 2 leaves it to the orchestrator, so the suite is `unverified` here. | `seal/config.json` `Broad gate` | the orchestrator, by `seal gate --record` |
| S7: `tests/lib/test_core.py` and `tests/hooks/test_core_start.py` were not run. The range touches neither `lib/core.py` nor the hook. | `tests/lib/test_core.py`, `tests/hooks/test_core_start.py` | the orchestrator, in the broad run |
| The body's count at the release. `frame/plan.md:61-62` merges #1478 and #1479 after this item, and each edits the body, so the count in this item's changelog item can change before the release ships it. | `seal/threads/1794289596-implement-orchestration-grew-back/changelog.md:3` | the orchestrator, when #1478 and #1479 merge |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_waiver_decided_at_start.py tests/text/test_review_axes.py tests/behaviour/test_the_set_a_work_item_always_has.py -q -p no:cacheprovider`, in the branch worktree at `10fc3a7f7` | exit 0, 199 passed, 2 warnings, both the citation at `docs/running/the-review-and-parity-arms.md:56` excused by this item's *Rule changes* (S6) |
| `bin/test` on the first four modules above, `-q -p no:cacheprovider`, at `10fc3a7f7` | 151 passed, 2 warnings, the count `frame/plan.md:82` claims |
| A `python3 -I` script under the round's scratch directory comparing each `pr.md` quote, whitespace collapsed, with the file its coordinate names | 9 of 9 found. The script was removed after the run. |
