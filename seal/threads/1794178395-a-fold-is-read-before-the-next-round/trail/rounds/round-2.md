# Review round 2: 1794178395-a-fold-is-read-before-the-next-round

```seal
target: 75b492af against release/v0.36.0
```

This is a verifying round. It reviewed the branch against `release/v0.36.0`
(`c7bb14ca`) at `75b492af`, in a `git clone --no-local` of the branch
worktree checked out at the target, under the round's scratch directory.
The fix diff is `a0f84d02` (the frame fold of findings 1 and 2), `3586ae30`
(the fix pass of findings 1 and 3) and `d1451a0f` (the close blocks). The
target also holds `75b492af`, the merge of `release/v0.36.0` that brought in
#1443 (`e244aa49`), #1440 (`74211b76`) and #1444 (`c7bb14ca`). As the
orchestrator asked, the round read the whole diff against the base, not
only the fix commits. No `seal/parity.md` is declared, and `seal/config.md`
has no `Record language` row (executed, `grep`), so the record is in
English.

The work item's records that state the present were read whole at the
target: `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. After them
the round read `trail/phases/phase-1.md` and `trail/rounds/round-1.md`.
Carried from round 1 without re-deriving them: G9's regressions as opened at
their tags, the 17 of the phase's 20 mutants round 1 did not re-run, and the
three `## Rule changes` `from:` texts standing in `docs/`. The last of these
holds because `git diff --stat bd7b937c 75b492af -- docs` is empty
(executed). Re-derived this round: every verdict below, the narrow suite,
the new pins' mutants, and the `pr.md` quotes.

The orchestrator's account was read as claims. It claimed that findings 1
and 3 are fixed in `3586ae30`, that finding 2 is fixed by the frame fold
`a0f84d02`, and that `75b492af` merges #1443, #1440 and #1444. `git show
--stat` on each commit lists what the claims say (executed). It also claimed
that #1443 rewrote the version-move paragraph that this item edits. The
combined diff `git show --cc 75b492af` shows the two sides' hunks in that
paragraph and no line that differs from both parents. `git merge-tree
--write-tree d1451a0f c7bb14ca` exits 0 with tree `212b90f5`, which is the
tree of `75b492af` (executed). So the merge is the automatic merge and
resolved no conflict.

## Findings

### 1. The orchestrator's half of a rejected decision is pinned by its first clause only, so the row rewrite and the version-move clause can be deleted with the suite green

```seal
severity: should
location: `tests/text/test_the_rules_have_one_owner.py:374-424`, `skills/implement/orchestration.md:74-84`
evidence: executed `bin/seal mutate skills/implement/orchestration.md --replace "A decision the framer rejects stands as its judgment" "" --replace "record the rejection and what the decision's source takes instead, a" "" --replace "and a prevention home are folded as an owner's decision is, because" "and a prevention home are folded, because" --tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -x"` in the clone: mutant 1 red, mutants 2 and 3 SURVIVED; read `skills/implement/orchestration.md:74-84`, `tests/text/test_the_rules_have_one_owner.py:398-424`, `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:36`, `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:52`
regression: round-1#1
```

The unit is the rejected-decision text that `3586ae30` added to
`skills/implement/orchestration.md:74-84`. The frame's *Scope* item 1,
seventh bullet (`frame/design.md:36`), says the orchestrator rewrites its
*Judgments of the run* row to record the rejection, quotes the framer's
*Alternatives considered* row in `pr.md`, and folds the version move and a
prevention home as an owner's decision. *Scope* item 6 (`frame/design.md:52`)
and the phase-1 row of `frame/plan.md` require each new clause to be seen
red with its sentence deleted. The fix pinned only the clause's lead, "A
decision the framer rejects stands as its judgment"
(`tests/text/test_the_rules_have_one_owner.py:422`). The defect came from
round 1's paste-ready text, which named one pin per case, and the fix pass
took that list as complete.

Why it matters: the row rewrite is the part of finding 1 that kept two rows
of `plan.md` from stating opposite things after a rejection. Deleting it
leaves the case green (mutant 2). Narrowing "folded as an owner's decision
is" to "folded" also leaves it green (mutant 3). On the orchestrator's side,
nothing then says the move and the home cannot stand rejected. The framer's
half of that clause is pinned in `test_the_framer_folds_a_decision_it_is_sent`
(mutant red, `## Probes`). The orchestrator's sentence that reads the
framer's answer is not. Each string below occurs once in the file once runs
of whitespace are collapsed (executed, `## Probes`). The fix pass owes the
seen-red showing of each new pin by contract rule 15.

```python
        # Round 1 of #1442, finding 1: a rejected decision had no route, and
        # the row written before the exchange recorded a fold that did not
        # happen.
        "A decision the framer rejects stands as its judgment",
        # Round 2 of #1442, finding 1: the orchestrator's half of a rejection
        # and the decisions no rejection can stand on.
        "the orchestrator rewrites its row of *Judgments of the run* to "
        "record the rejection and what the decision's source takes instead",
        "quotes the framer's *Alternatives considered* row in the work "
        "item's `pr.md`",
        "The version move and a prevention home are folded as an owner's "
        "decision is",
    ):
        assert said in order, f"the order no longer says {said!r}"
```

```seal
verdict: fixed 3f894d7e
answer: The finding holds. In tests/text/test_the_rules_have_one_owner.py, test_a_decision_after_the_frame_is_folded_into_it now pins each clause of the rejected-decision text. The paste-ready pins were taken with three changes. The lead pin is extended to cover "as a proposal left after the exchange of *The frame is read against the issue at the spawn* does". The row-rewrite pin goes on to "a finding's route or the next spawn's scope,". The version-move pin goes on to the end of the sentence, so the two citations of the rules that give the move and the home to the orchestrator are held too. Each clause was deleted alone by seal mutate after the commit, and each mutant was red on its own pin's assertion message. Round 2's mutants 2 and 3 were re-run word for word, and both are now red (executed). The class was then listed by deleting each sentence this work item added to skills/implement/orchestration.md and skills/implement/SKILL.md, or putting it back to the wording it replaced, run against every module that names those files (executed). Nine sentences had no case reading their meaning; four of the nine went red only on tests/behaviour/test_docs_line_wrap.py, because the mutant left a long line. a4704032 pins eight of them. Six are other clauses of the fold paragraph: its reason, the open list of examples, the orchestrator correcting its row, the one commit, the framer's hand-back sending routing.md and pr.md to the orchestrator, and "a decision's fold is read by the framer that writes it". The seventh is the prevention-home sentence, pinned in test_a_recurring_problem_gets_a_prevention_home. The eighth is the SKILL.md scope sentence, pinned in tests/behaviour/test_a_phase_hands_the_next_one_a_record.py#test_the_skill_names_the_records_one_section. Each of the eight was shown red with only its sentence removed or put back to the removed wording (executed). agents/framer.md's conflict clause from round 1 was also shown red alone (executed). The ninth sentence, the version-move clause of *Orchestrator: how the work is routed*, has no case reading its paragraph. 3989a6a0 records it in gaps.md *Not done*. 82c46f10 corrects a comment of the class pins.
```

### 2. The frame's *Out* item says `session_cost.py` grades a fold exchange, and since the merge of #1440 it grades no segment

```seal
severity: should
location: `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:65`
evidence: executed `grep -n -i grade skills/verify/scripts/session_cost.py` at the target (only "degrades" at `:926` and `:1897`) and the same grep at `94d04d30` (`report_grades` and the grading comments at `:1877`, `:2192`, `:2459`); read `seal/threads/1794178393-the-batching-bars-are-met-or-removed/frame/design.md` `## Rule changes`
```

Why it matters: the *Out* section is not dated to the commit the framer
read, so it states the present. It reads "How `session_cost.py` grades a
fold exchange. That exchange is a framer segment with few reads, and its
grading is #1440's." #1440 landed in `release/v0.36.0` as `74211b76` and
reached this branch through `75b492af`. Its commit takes out "the bars, the
grade and the plain advisory". At the target, `session_cost.py` grades no
segment, and #1440's design removes `docs/running/the-run.md` *The
per-segment bars* at the settle. A sealer that reads the frame against the
tree finds the out-of-scope item naming a grade that does not exist. The
same fact stands in `frame/plan.md` *Technical context*, the #1440 bullet,
which is dated to `7056ee61`, so that bullet is no finding. The fix is a
frame fold.

```markdown
- **A grade for a fold exchange's cost.** `session_cost.py` grades no segment since #1440 (`74211b76`), so a fold exchange is read as a framer row of `seal cost --segments`, and this work adds no grade for it.
```

```seal
verdict: fixed 70c464cf
answer: The orchestrator folded this finding before the fix pass. At 70c464cf, frame/design.md *Out* carries the round's replacement item word for word, and frame/plan.md *Judgments of the run* gains the fold's row. The replacement holds against HEAD. grep -n -i grade over skills/verify/scripts/session_cost.py matches only "degrades" at :926 and :1897 (executed). seal cost --segments labels each segment by the subagent_type of the spawn it opened at, and labels each slice of a resumed agent's transcript by that same agent (skills/verify/scripts/session_cost.py segment_label and segment_slices, read). So a fold exchange is a framer row, whether the framer is resumed or spawned fresh. The fix pass edited no frame file.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the rejected decision has a route. `skills/implement/orchestration.md:74-84`
says a decision the framer rejects stands as its judgment. The
orchestrator rewrites its row to record the rejection and what the
decision's source takes instead, and quotes the *Alternatives considered*
row in `pr.md`. The version move and a prevention home are folded as an
owner's decision, each with the rule that gives it to the orchestrator.
That text sits after the row-correction sentence and before "The
orchestrator then commits", so the row is rewritten before the one commit.
`agents/framer.md:261-264` reads "A decision the owner made, the version
move and a prevention home are folded as they were made, and where you
judge that one of them conflicts with the tree, your hand-back names the
conflict." *Scope* items 1 and 5 carry the same text after `a0f84d02`
(`frame/design.md:36`, `:44`). `changelog.md:3` carries the rejection and
the three decisions folded as made. The heading the fix cites,
*The frame is read against the issue at the spawn*, stands at
`skills/implement/orchestration.md:139`. Its paragraph says what remains
after the one exchange "stands as the framer's judgment, which the
orchestrator quotes in the work item's `pr.md`", so the cited shape matches.
The pin on the lead and the framer's pin were each seen red with their text
deleted (executed, `## Probes`). The fix pass claimed in its close that
each pin was red before the prose changed. The round did not re-run that
showing; the two mutants above settle the same question after the commit.
Finding 1 above is a gap in the pins of this fix, not the route standing
open again.

```seal
confirms: round-1#2
```
What holds: the first rule change's `to:` scopes the clause to the exchange.
At `frame/design.md:96-102` it reads "and the orchestrator edits no frame
file in that exchange", and the sentence after it gives later decisions to
the framer and the crafter-named statements to the orchestrator. The clause
matches its context in `skills/implement/orchestration.md:141-150`, where
"the orchestrator edits no frame file" closes the spawn exchange's sentence.
The `from:` text was not changed by the fold. `a0f84d02` changes only
`frame/design.md` and one row of `frame/plan.md` (executed, `git show`).
Read.

```seal
confirms: round-1#3
```
What holds: the row's reason at `gaps.md:7` ends "and no case runs a framer
through a fold". The row's first clause, the one `pr.md` quotes, is
unchanged, and the quote still matches (executed, `## Probes`). Read.

What matched: the merged version-move paragraph,
`skills/implement/orchestration.md:413-454` (*Which branch the pull request
lands on is decided with the routing question*), read whole. #1443's
sentences stand as `e244aa49` wrote them: the framer spawn prompt naming
the release's other items, the merge order from *Overlap with the release*,
the orchestrator's choice where plans disagree, the carrier first, and the
fallback carrier. This item's clause stands once, at `:439-442`: "the move
is a decision the framer folds into that section, as *Orchestrator: the
order inside a ticket* states, before the orchestrator spawns the last
phase". The old wording "orchestrator folds the move" occurs nowhere in the
file (executed, `grep -c`, 0). The 3-dot diff of the branch against the
base over `agents/`, `skills/` and `tests/` holds only this item's hunks.
#1443's step-4 and hand-back additions in `agents/framer.md` stand beside
the fold half. So the merge dropped and duplicated nothing that the frame or
the changelog claims. Read and executed.

What matched: the clause has one reading beside #1443's text. The same
paragraph has the orchestrator write a chosen merge order as a *Judgments
of the run* row, while the version move goes to the framer as a fold. The
fold paragraph defines a decision by what the frame says the work is or
why, and grounds the fold on a crafter reading the frame
(`skills/implement/orchestration.md:49-58`). The move is folded because "the
crafter reads its version write there" (`:442`). A merge order is read
by the orchestrator at the merge and by no crafter. So the two rules govern
different acts, and the row for an order choice does not read as a
decision to send to the framer. The fold paragraph's "the move by
*Orchestrator: how the work is routed*" still names the rule that gives the
move to the orchestrator: "The orchestrator chooses which work item carries
the move" stands at `:423`. Read.

What matched: the merge's other items collide with nothing this item
claims. #1440's design removes `docs/running/the-run.md` *The per-segment
bars* and `docs/running/measuring-a-run.md` *Measuring a run*. #1443's
design and #1444's state `- nothing` or a change to
`docs/releasing/release-checklist.md`. This item changes *The run* and two
sections of `docs/running/the-agent-set.md`, so no settle operation
overlaps (executed, the `## Rule changes` headers of every design under
`seal/threads/`). The one statement the merge made untrue is finding 2.
Read.

What matched: the `pr.md` quotes. All six were found word for word, with
runs of whitespace collapsed, at the source each coordinate names at the
target (executed, `## Probes`).

Two readings of the records that are not findings. `frame/plan.md` has no
`## Overlap with the release` section: the template gained it in
`e244aa49`, after this plan was framed at `7056ee61`. The plan's *Technical
context*, dated to that commit, states the order (#1443 first), and #1443
has merged. No script reads the section (executed, `git grep "Overlap with
the release"` over `lib`, `skills/*/scripts` and `.github`, no hits). The
*Scope* items give line ranges from the tree before the build, such as
`:49-81` for the fold paragraph that now runs to `:122`. Each item also
names its paragraph by its words, which stand at the target, so a reader
finds each paragraph without the range.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `75b492af`, `unverified` by contract rule 2; this round ran 16 modules that name the touched files and no wider set | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether a framer resumed or spawned for a fold follows the fold half; no case runs one | `agents/framer.md:253-286` | a measurement, `frame/questions.md` Q1 |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the 16 modules under `tests/` that name `skills/implement/orchestration.md` or `agents/framer.md` (from `git grep -l`, `tests/test_conftest.py` left out), `-q`, in the clone at `75b492af` | exit 0, 565 passed |
| `bin/seal mutate skills/implement/orchestration.md` with the three `--replace` pairs of finding 1's `evidence:` line, `--tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -x"` | baseline passed; mutant 1 red, mutants 2 and 3 SURVIVED; file restored |
| the same, mutant 1 alone | red, failing `test_a_decision_after_the_frame_is_folded_into_it` on "the order no longer says 'A decision the framer rejects stands as its judgment'" |
| `bin/seal mutate agents/framer.md --replace "the version move and a prevention home are" "is"` with the same `--tests` | red, failing `test_the_framer_folds_a_decision_it_is_sent` on its "A decision the owner made, the version move and a prevention home are folded as they were made" pin; file restored, `git status --short` empty |
| `python3 -I -c` counting each of finding 1's three proposed pins in `skills/implement/orchestration.md`, with runs of whitespace collapsed | each occurs once |
| `python3 -I -c` matching each `pr.md` quote, with runs of whitespace collapsed, against `changelog.md`, `frame/plan.md` and `gaps.md` | all six found |
| `git merge-tree --write-tree d1451a0f c7bb14ca` | exit 0, tree `212b90f5`, equal to `git rev-parse 75b492af^{tree}` |
| `python3 skills/code-review/scripts/chain_check.py --baseline c7bb14ca --root <the branch worktree> --worktree`, before this record | exit 0; notices for findings 1 and 3 of round 1 and for the target behind HEAD, each saying a verifying round is owed, and for the absent `trail/gate.md` and `guarantee.md`; no notice at `frame/design.md` |
