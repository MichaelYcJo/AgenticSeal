# Review round 1: 1794289596-implement-orchestration-grew-back

```seal
target: 9c17b22bc against release/v0.37.2
```

This round reviews `df775c52c..9c17b22bc`, the branch against the tip of
`release/v0.37.2`. It reads the tree's text of `agents/proofer.md`,
`agents/crafter.md` and `skills/implement/SKILL.md` from the diff, not the
installed 0.37.1 copies the proofer was spawned with. The installed
`agents/proofer.md` says a frame section dated to the commit the framer
read "states that commit, and the target does not contradict it", whole.
The tree's sentence at `agents/proofer.md:124-128`, which this diff ships
and `frame/design.md` S8 asks for, reads a sentence there that says what
the work does or concludes against the target. This round applies the
tree's sentence. Findings 2 and 3 rest on it for `frame/plan.md:9`,
`frame/plan.md:15` and `frame/design.md:18`; `frame/plan.md:23` is not in
a dated section and is a finding under either sentence.

Round 1 has no earlier record, so no fact is carried from one. Every
verdict below is this round's own.

## Findings

### 1. The body and `merge-order.md` time the file's opening to "the first framer of the release", an event a later work item finds past and a release with no framer never reaches

```seal
severity: should
location: `skills/implement/orchestration.md:316-319`, `skills/implement/merge-order.md:3-4`, `seal/threads/1794289596-implement-orchestration-grew-back/frame/design.md:123`, `seal/threads/1794289596-implement-orchestration-grew-back/changelog.md:3`
evidence: executed `git grep -n "first framer"` (four hits, the four locations); read `skills/implement/merge-order.md:1-34`, `skills/implement/orchestration.md:305-326`, `agents/framer.md:85-95`, `frame/plan.md:52-60`
```

Why it matters: before this diff, the merge order stood in the body, which
every orchestrating session reads. Now an orchestrator reads it only by
opening `skills/implement/merge-order.md`, and both the body
(`orchestration.md:316-318`) and the file's first paragraph
(`merge-order.md:3-4`, "before it spawns the first framer of the release,
and not otherwise") tie the opening to one moment of the release. Two
ordinary runs miss that moment.

- A work item that joins the release after another item's framer has
  spawned. This release is one: `frame/plan.md:54` records that #1478 and
  #1479 were "not started" when #1476 and this item were framed. The
  session that starts #1478 meets a condition whose deadline has passed,
  and "and not otherwise" tells it not to open the file. Its framer's
  prompt then names none of the release's other items, which
  `merge-order.md:15-17` asks of "each framer" and `agents/framer.md:85-95`
  reads to write *Overlap with the release*.
- A release whose items have no framer. Under `agentic` a `Planning` row of
  `the session` or no row is ordinary (`orchestration.md:373-376`). With no
  framer the moment never comes, yet the file's rules still bind: the item
  that carries the version move merges first, and a move made after an
  item's last round owes a verifying round (`merge-order.md:28-34`).

The file's content is needed at each work item's start while the release
holds another, so the condition should name that start, not the release's
first framer. The fix reaches four statements: the body's sentence, the
file's first paragraph, the changelog's first item, which a `pr.md` quote
does not cover, and `frame/design.md` D4. D4 is a frame file, so its row is
a decision for the orchestrator to fold through the framer, and S4 asks the
body to keep D4's words. The two openings must still share no run of 15
words (`tests/text/test_no_passage_is_pasted_into_a_second_file.py`); the
two below share none.

```markdown
<!-- skills/implement/orchestration.md:316-319 -->
Where the release holds another work item, the orchestrator opens
`skills/implement/merge-order.md` when it starts this one, before it
spawns this item's framer or, where no framer runs, before its first
edit: that file holds what each framer's prompt names, the order the
items merge in, and which of them takes the move.

<!-- skills/implement/merge-order.md:3-4 -->
The orchestrator opens this file when it starts a work item of a release
that holds another, before that item's framer is spawned or, where none
runs, before the item's first edit, and not otherwise.

<!-- frame/design.md:123, D4's cell -->
where the release holds another work item, when it starts this one, before it spawns this item's framer or, where no framer runs, before its first edit

<!-- changelog.md:3, the clause on merge-order.md -->
the orchestrator opens it when it starts a work item of a release that holds another, before that item's framer spawns or its first edit.
```

```seal
verdict: fixed f07bd7f60
answer: The fix follows `frame/design.md` D4 as the framer folded it at `bee4a509c`, not the paste-ready wording, whose length `frame/plan.md` *Alternatives considered* row 20 rejects. The body's sentence now reads "Where the release holds another work item, the orchestrator opens `skills/implement/merge-order.md` when it starts this one, before its first edit", in D4's words as S4 asks. The first paragraph of `merge-order.md` says the same condition in its own words: "when it starts a work item of a release that holds another, before that item's first edit, and not otherwise". The first *Changed* item and the first `### Process changes` row of `changelog.md` say the same, and the item gives the body's count as 5,223. `tests/text/test_no_passage_is_pasted_into_a_second_file.py` exits 0 on the two openings (executed). The D4 cell was fixed at `bee4a509c`. `git grep` for "first framer" and "two or more work items" at HEAD finds no statement outside the records' quotes of the old wording (executed).
```

### 2. `frame/plan.md` *Technical context* names a case that reads the routing question's tables against `lib/routing.py`, and no case does

```seal
severity: should
location: `seal/threads/1794289596-implement-orchestration-grew-back/frame/plan.md:15`, `tests/behaviour/test_waiver_decided_at_start.py:882-892`
evidence: executed `bin/test tests/behaviour/test_waiver_decided_at_start.py tests/text/test_review_axes.py tests/behaviour/test_docs_line_wrap.py -q -p no:cacheprovider` in a scratch clone at `9c17b22bc` with `skills/implement/routing-question.md:100` and `:102` changed to write `Automation` = `always` and `Review` = `skip the review`: exit 0, 86 passed; read `tests/behaviour/test_waiver_decided_at_start.py:144-162`, `:183-392`, `:454-506`, `:882-892`
```

Why it matters: the third risk of *What breaks in six months* is the one
this diff creates. The question's tables now stand in a file opened only
when the batch is put, apart from the body's table of rows. The sentence
says the risk is guarded: "`tests/behaviour/test_waiver_decided_at_start.py`
reads both against `lib/routing.py` and fails on that." It is a sentence
of a dated section that says what the work does, so it is read against the
target, and the target contradicts it.

`test_the_orchestration_offers_the_vocabulary_the_parser_accepts`
(`:882-892`) reads `AXES` in the body only. The cases that import `routing`
(`:183-392`) read `templates/records/sdd-routing.md`. The box cases
(`:454-506`) compare the labels and the unchecked halves with literals in
the test. The probe changed two of the eight values the boxes write to
words `lib/routing.py` rejects, and every module that reads
`routing-question.md` stayed green. Before this diff no case read the box
table's values either, so no guard was lost. The defect is the frame's
claim: the next reader of the risk is told a case catches the drift, and
none does.

The fix below corrects the sentence. A case that reads each
`` `<Row>` = `<answer>` `` pair of the box table against
`lib/routing.py`'s answer tuples would make the original sentence true
instead. It would contradict `frame/design.md:163`, "This work adds no
gate, check, hook, mark or case", so it is a decision for the framer, and
the fix pass owes that sentence too where the case is chosen.

```markdown
<!-- frame/plan.md:15, the third risk -->
Third, the routing question is opened only when asked, so a change to the row vocabulary in the body can leave the question's tables behind. `tests/behaviour/test_waiver_decided_at_start.py#test_the_orchestration_offers_the_vocabulary_the_parser_accepts` reads the body's vocabulary against `lib/routing.py`, and no case reads the values the boxes of `skills/implement/routing-question.md` write, so the drift shows only to a reader of that file.
```

```seal
verdict: fixed bee4a509c
answer: The framer's fold at `bee4a509c` rewrote `frame/plan.md:15` to the paste-ready sentence word for word (read at HEAD). It added no case. `frame/plan.md` *Alternatives considered* row 19 records why, so `frame/design.md:163` stands as written. `git grep` for "reads both against" in the work item's directory finds nothing at HEAD (executed). This pass changed nothing for this finding.
```

### 3. Three sentences of the frame state a conclusion about the work that the frame's own D3 or the target contradicts

```seal
severity: should
location: `seal/threads/1794289596-implement-orchestration-grew-back/frame/plan.md:9`, `seal/threads/1794289596-implement-orchestration-grew-back/frame/design.md:18`, `seal/threads/1794289596-implement-orchestration-grew-back/frame/plan.md:23`
evidence: executed a `python3` read of the 26 phrases of `test_a_decision_after_the_frame_is_folded_into_it` at `df775c52c` against the order section of `skills/implement/orchestration.md` at `9c17b22bc`: 16 still present; read `frame/design.md:108-116`, `frame/design.md:18`, `frame/plan.md:9`, `frame/plan.md:23`, `trail/phases/phase-2.md:22`
```

Why it matters: this is the class `frame/design.md` G8 records and this
diff's new rule names: a sentence that says what the work does or
concludes, left stating the old fact while another sentence of the same
frame states the new one.

- `frame/plan.md:9` says the case's phrases "are the paragraph's present
  wording, so the rewrite turns each red until the case names the new
  wording". The rewrite kept 16 of the old case's 26 phrases word for word.
  `trail/phases/phase-2.md:22` found the same from the other side: nine of
  the new case's rows matched the old section.
- `frame/design.md:18` (G10) says "*Scope* items 1, 2, 5 and 6 find" the
  words, and `frame/plan.md:23` says "The words come from
  `frame/design.md` *Scope* items 1, 2, 5 and 6." D3 (`frame/design.md:112`
  and `:114`) counts the words that left by "items 1, 2 and 3" and "items
  5, 6 and 9". Item 3 moved the merge order out, and item 9's *Removes*
  row 21 shortened the fold rule's dated-section sentence. The fold at
  `8e49bb39b` added item 9 and *Removes* rows 19 to 21 and left both
  sentences as they were.

All three locations are frame files, so the fix is the orchestrator's fold
through the framer. It touches nothing outside the records.

```markdown
<!-- frame/plan.md:9, the sentence after the slice -->
The phrases are that paragraph's wording, so the rewrite turns red each phrase whose words it changes, until the case names the new wording.

<!-- frame/design.md:18, G10's last sentence -->
Rewriting the paragraph therefore frees almost none of the words G5 asks for: *Data & interfaces* D3 gives the arithmetic, and *Scope* items 1, 2, 3, 5, 6 and 9 find them.

<!-- frame/plan.md:23, the last sentence of the Verdict cell -->
The words come from `frame/design.md` *Scope* items 1, 2, 3, 5, 6 and 9.
```

```seal
verdict: fixed bee4a509c
answer: The framer's fold at `bee4a509c` rewrote all three sentences to the paste-ready text: `frame/plan.md:9`, G10's last sentence at `frame/design.md:18`, and the Verdict cell at `frame/plan.md:23` (read at HEAD). `git grep` for "present wording, so the rewrite", "turns each red" and "items 1, 2, 5 and 6" in the work item's directory finds nothing at HEAD (executed). This pass changed nothing for this finding.
```

## Confirmations

What matched: S1 at the target. `wc -w skills/implement/orchestration.md`
prints 5,225, under the bound of 5,242 (executed). Phase 3's record claimed
5,225 at `02740215a`, and the file is unchanged since.

What matched: the count after #1476's merge, which `gaps.md:7` leaves to
the orchestrator. `refactor/1476-the-verifying-round-rule-has-four-owners`
at `aa0708383` changes the body by +10 words, the drain's first row alone
(executed: `git show <ref>:skills/implement/orchestration.md | wc -w` gives
7,321 against 7,311 on the release branch). The body would then hold about
5,235, under the bound, if the merge is clean. The same diff leaves the
late move's sentence at the old `:485-489` unchanged, so
`frame/questions.md` Q1's answer at that commit is "unchanged" (executed:
`git diff -U1 release/v0.37.2...<ref> -- skills/implement/orchestration.md
agents/proofer.md`). #1476 changes `agents/proofer.md` at `:62-64` and
`:134-146`, beside this diff's `:124-128`; whether git merges them cleanly
was not run.

What matched: S2 and S3. The order section holds six paragraphs from the
lead **A decision made after the frame is committed is folded** to the one
before **Where a work item stands** (`orchestration.md:52-134`), each
opening with a bold lead, in the order *Scope* item 4 lists. Each of D1's
24 rows stands in the paragraph its Home column names (read, row by row).
The fold case holds one phrase per row, and its module is green (executed,
below).

What matched: S4. `grep -n` finds each new file's path once in the body,
at `:222` and `:317`, in D4's words (executed). Phase 3's record claimed
lines 222 and 317.

What matched: S5. A `python3` read split each paragraph of
`routing-question.md` and `merge-order.md` into sentences and looked for
each in `orchestration.md` at `9e9d1087f`, flattened (executed). The only
sentences not found are the two first paragraphs, the headings, and the
two pointer sentences phase 1's Exception 2 names in `routing-question.md`
(`:13-16`, `:77-82`). Phase 1 claimed this; it holds.

What matched: S6. `tests/behaviour/test_a_cited_section_stands_in_its_file.py`
is green and its two warnings name `docs/running/the-review-and-parity-arms.md:56`
as excused by this work item's *Rule changes* (executed). The operation's
`from` stands at `:54-55` of that file (read).

What matched: S8. `skills/implement/SKILL.md:117-123`, `agents/proofer.md:124-128`
and `agents/crafter.md:185-190` each exempt a dated section's coordinates
and statements of the tree, read a sentence there that says what the work
does or concludes against the present, and the two definitions cite the
owner (read). `agents/framer.md:276` says a dated section keeps its date,
which none of the three contradicts (read).

What matched: the homes of *Removes* rows 9 to 21. Each removed passage's
fact stands where its row says: step 1 and `orchestration.md:275-281`
(row 9), `:258-261` (row 10), `:203-205` (row 11), `:299-303` and `:277`
(row 12), `routing-question.md:70-75` and `orchestration.md:399-405`
(row 13), the ladder's opening at `orchestration.md:423-427` (row 19),
`skills/legacy-parity/SKILL.md:153-171` (row 18), the third row of
**Three combinations do not stand** at `orchestration.md:394` (row 16),
and `agents/framer.md` *You have two routes back* (row 20) (read).

What matched: the citations of moved passages. `git grep` on the moved
headings and leads outside `seal/threads/` finds each citation pointing at
a heading or lead that stands: `README.md:154-157`, `README.ko.md:155-158`,
`skills/implement/multi-repository.md:9-10`,
`skills/commit-pr-convention/SKILL.md:88-89`,
`skills/implement/bootstrap.md:206-208`, `CONTRIBUTING.md:409-412`,
`skills/implement/SKILL.md:159-162` and `:260-261`, and
`docs/releasing/branch-and-release.md:41` (executed, then read). This is a
sample over the headings' and leads' words; a statement of the moved rules
in other words is outside it.

What matched: `pr.md`. Each of its nine quotes stands word for word, runs
of whitespace collapsed, at the source and item its coordinate names
(executed, a `python3` comparison). `Commit and pull request language` is
English, so no `pr.<lang>.md` is owed.

What matched: the records that state the present. `routing.md`,
`frame/questions.md`, `gaps.md` and `changelog.md`, each read whole at the
target, hold no other sentence the target contradicts. The changelog's
count of nine removed statements matches *Removes* rows 9 to 13, 16, 19 and
20 (read).

A case whose comment names a fact the frame does not state: the comment of
`test_a_decision_after_the_frame_is_folded_into_it`
(`tests/text/test_the_rules_have_one_owner.py:379-384`) cites "that work
item's `frame/design.md` D1", which leaves with the directory at the
settle; the issue number beside it still leads there.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD. The narrow modules this round ran are not it, and contract rule 2 leaves it to the orchestrator: the suite is `unverified` here. | `seal/config.json` `Broad gate` | the orchestrator, by `seal gate --record` |
| S1 once the release branch, #1476 among it, is merged in. The +10 above is a reading of #1476's ref at `aa0708383`, not of a merge. | `skills/implement/orchestration.md` | the orchestrator, by `wc -w` after the merge, as `gaps.md:7` says |
| S7: `tests/lib/test_core.py` and `tests/hooks/test_core_start.py` were not run. The diff touches neither `lib/core.py` nor the hook, and the heading the hook's line names stands at `orchestration.md:21` (read). | `tests/lib/test_core.py`, `tests/hooks/test_core_start.py` | the orchestrator, in the broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_waiver_decided_at_start.py tests/text/test_review_axes.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_first_setup_asks_once.py -q`, in the branch worktree at `9c17b22bc` | exit 0, 237 passed, 2 warnings, both the excused citation of S6 |
| In a `git clone --no-local` of the worktree at `9c17b22bc`, `skills/implement/routing-question.md:100` and `:102` changed to write `Automation` = `always` and `Review` = `skip the review`, then `bin/test tests/behaviour/test_waiver_decided_at_start.py tests/text/test_review_axes.py tests/behaviour/test_docs_line_wrap.py -q -p no:cacheprovider` | exit 0, 86 passed: no case reads the values the boxes write (finding 2). The clone was removed after the run. |
