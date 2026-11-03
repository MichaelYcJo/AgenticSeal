# Review round 2: 1793661729-each-document-is-cut-by-who-opens-it

```seal
target: 350048ba0, fixes 316c608b4..350048ba0
```

This verifying round read the fix diff 316c608b4..350048ba0: the three fix
commits 170372c72, d990b38b5 and b204b7e8b, and 350048ba0, which commits
round 1's close blocks and one row of `frame/plan.md` *Judgments of the
run*. It ran its probes in a `git clone --no-local` of the repository
checked out at 350048ba0. `seal/parity.md` is not declared, so no
`original:` line is owed.

Carried from round 1 as coordinates, not re-established: the base,
`origin/release/v0.30.0` at 95cbd99a4; the replay script's text in
`trail/phases/phase-7.md`, whose filter this round's transcript probe
copied; and the nine lines naming `docs/the-review-record.md` at an earlier
commit, which no fix touched. Every verdict below was reached this round.

## Findings

### 1. The new judgment row says phase 1's rewrite falls inside one of 33 ranged reads and names one passage, where it falls inside nine reads and spans two passages

```seal
severity: should
location: `seal/threads/1793661729-each-document-is-cut-by-who-opens-it/frame/plan.md:99`
evidence: executed `python3 -I test_tmp_ranges.py /Users/x/.claude/projects/<project>`, `git diff -U0 2d38c75af 29d8ca6a4^ -- docs/the-review-record.md`
regression: round-1#3
```

Why it matters: the unit is the row 350048ba0 added to `frame/plan.md`
*Judgments of the run* (`frame/plan.md:99`). The frame (D8 *Comparable*)
counts a call whose path is gone against the file its cited section moved
into. Phase 7 instead counted each ranged read of the deleted review record
at its base bytes, on the premise that those lines moved unchanged
(`trail/phases/phase-7.md:73-76`). The row records where that premise fails
with only finding 3's coordinate, *The guarantee*'s opening, and not the
fix pass's own word diff, which also named *The run*'s question-gate
paragraph (round 1, finding 3's `answer:`).

The row says the rewrite "moves a few words inside one of 33 ranged reads".
What phase 1 changed in `docs/the-review-record.md` before phase 5 deleted
it is two passages (executed, the diff on the evidence line). One is base
lines 288-291, *The guarantee*'s opening, two lines at HEAD. The other is
base lines 531-544, *The run*'s question-gate paragraph, cut from fourteen
lines to three at 4c4925bff. This round wrote a read-only probe over the
same transcripts, with phase 7's filter, and listed every ranged read of
that document that returned file lines. It found 28 of phase 7's 33. The
proofer's 7 and the sealer's 3 match phase 7's per-type counts. Nine of the
28 cover a changed line. Four cover the guarantee's opening: two sealer
reads, one framer read and one crafter read. Five cover the question-gate
paragraph: three framer reads, one crafter read and one proofer read.

The row's conclusion survives. Both edits shortened the text, so counting
at base charges HEAD more than it now holds. That is the direction that
does not flatter the cut, and no reading in phase 7 moves toward `worse`
because of it. Its grounds do not survive. `skills/settle/scripts/settle.py`
lists every row of *Judgments of the run* for the settling session, which
weighs each judgment against what it cost and caught. A row that puts the
gap at one read and one passage tells that session the premise failed
almost nowhere. The route is an ordinary fix pass: the defect is in how the
row was written, and the frame is not in question.

```markdown
frame/plan.md:99, the whole row:
| 2026-11-03 | `trail/phases/phase-7.md` keeps counting each ranged read of the deleted `docs/the-review-record.md` at its base bytes, though phase 1 (4c4925bff) rewrote two passages of it: *The guarantee*'s opening (base lines 288-291) and *The run*'s question-gate paragraph (base lines 531-544, cut to three lines) | the round-1 fix pass's word diff found both (`trail/rounds/round-1.md` finding 3). Of phase 7's 33 ranged reads of a deleted file, 28 read this document, and 9 of those cover a changed line: 4 the guarantee's opening and 5 the question-gate paragraph (`trail/rounds/round-2.md` *Probes*). Both edits shortened the text, so counting at base charges HEAD more than it holds, which does not flatter the cut, and no reading in that record moves toward `worse`. The reading is kept with the gap named here rather than replayed | `docs/running/measuring-a-run.md` |
```

```seal
verdict: fixed 540cb8515
answer: The row at frame/plan.md:99 is rewritten in other words than the paste-ready text, since that text holds only phase 1's two passages and says counting at base does not flatter the cut. A word diff of each deleted document at 2d38c75af against the files holding its text at b1880c1db, the replay's HEAD (executed), found that phase 5 and its group commits lengthened the review record's moved text by 149 bytes in seven places, and phases 3 and 5 the record layout's by 20 bytes in three re-pointed paths, so the base count also leaves bytes out. The row now names phase 1's two passages with their sizes (129 and 778 bytes shorter), the lengthened places, the 28 and 5 ranged reads of the two documents and the nine this round found over a shortened passage, and the bound: at most 149 bytes a read, so the proofer's +0 of 375,093 lies between 276 fewer and 1,043 more, since its one read over the question-gate paragraph starts at base line 541 and covers 276 of the paragraph's 956 bytes (the sealer found this; this pass first wrote 778 fewer and 265 more, as if the read covered the whole paragraph), and every other type falls by more than the gap can add. trail/phases/phase-7.md, gaps.md and changelog.md state no size for the gap, so none was changed.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `README.md:119` and `README.ko.md:114` hold round 1's
paste-ready text word for word (read). The six other places the fix pass
named now state the subject boundary of `skills/implement/SKILL.md:73`, or
drop the premise that only a design's rule changes reach the policy root.
They are `skills/implement/orchestration.md:472` and `:489`,
`skills/implement/SKILL.md:146-149`, `skills/settle/SKILL.md:17-21`,
`skills/settle/rule-changes.md:11-15`,
`skills/settle/named-directories.md:51-55`, and the docstring at
`tests/text/test_the_rules_have_one_owner.py:450-456` (read). The
section `skills/implement/SKILL.md:146-149` points to "above" stands above
it at line 66 (read). The fix pass called its list a sample, as contract
rule 12 asks of a scan over spellings. This round listed the class by a
different method. It ran a `git grep` over every tracked file for
sentences naming rule changes, the policy root or a policy document beside
a negation or a quantifier, and a second for "baseline", "policy in force"
and "settle writes" in both editions. Then it read each hit in context
(executed). Every remaining hit states what the settle writes, or what a
design's operations reach at the settle, and neither is false under the
boundary. Examples are `docs/checks/the-pull-request-check.md:150` and
`:168`, `docs/checks/the-fold.md:175`, `seal/README.md:6`,
`templates/setup/config.md:487` and `agents/framer.md:187-192` (read).
`skills/settle/named-directories.md:51-55` leaves to the settling session
how it tells a settle's commit from a work item's among the commits that
changed the policy root. That is a judgment the session makes, and the
sentence is not wrong, so it is no finding.

```seal
confirms: round-1#2
```
What holds: `docs/layout/the-record-layout.md:123-124` holds round 1's
paste-ready text, and `docs/checks/the-fold.md:6` holds the heading it
cites (executed, round 1's two `grep` commands run again). The fix pass's
one other instance, `skills/code-review/scripts/chain_check.py:78-81`, now
names `docs/forms/the-round-record.md` and `docs/forms/the-guarantee.md`
with their headings, and the cited-section module passes over it
(executed). This round checked the class by two read-only probes of its
own. The first listed every heading or bold rule lead of a `.md` file
under `docs/` or `skills/` at the base that stands at HEAD in another file
(439), and every italic citation of one at HEAD outside `seal/threads/`
and `CHANGELOG.md` (205). It then printed each whose paragraph names no
backticked path of a file holding it at HEAD. Eleven came back, and each
resolves (read). `README.md:355` names a heading of `README.md` itself.
`evals/scripts/replay_targets.py:24-25` names the `v0.22.0:` path. The
two in `skills/code-review/orchestration.md:142` and `:211` follow
`docs/running/the-run.md` named at `:134` and `:201`.
`skills/verify/scripts/seal_stamp.py:4` names an issue's section. The
six in tests sit beside a path in the same docstring or a module constant
holding the path, or in a docstring path-less at the base too. The second
probe read every italic span followed by "above" or "below" at HEAD (22).
It found one not on the stated side of its own file, a string
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:195`
asserts another file holds, which this branch did not touch. Both probes
match a reference spelt as the heading in italics, so a reference in other
words stays outside them (see `## Not judged`).

```seal
confirms: round-1#3
```
What holds: the policy-root item of
`seal/threads/1793661729-each-document-is-cut-by-who-opens-it/changelog.md:5`
now names "two passages that now cite where their text stands", and the
passages item at `changelog.md:8` names both. It names
`hooks/question-gate.py`'s docstring with *The run* citing it, and now
*The guarantee*'s opening citing `agents/sealer.md` *Job* (read). Round
1's evidence line, the word diff of the base *The guarantee* against
`docs/forms/the-guarantee.md`, was run again. It shows the rewritten
opening and the re-pointed *The stamp* citation, and nothing else
(executed). The fix pass's reason for not taking item 5's paste-ready text
holds. That text said "the next item", which is the item on group
directories, and the sentence that stands says "below" and names the
passages item (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the lint and the typecheck at HEAD. This round ran 95 modules narrow (see `## Probes`) | the whole tree | the orchestrator's `seal gate` run after the rounds settle |
| A path-less reference to a moved section written in other words than its heading in italics. Both probes under round-1#2 match only that spelling, and the domain of other wordings is unbounded | the tracked files outside `seal/threads/` | a reader who follows one |
| Whether a settling session under the installed 0.30.0 finds the last settle's pull request by the sentence at `skills/settle/named-directories.md:51-55`, and whether a framer under it reads the boundary from the six rewritten places; no agent of this run receives them | `frame/questions.md` Q1 | the orchestrator of the first work item run under the installed 0.30.0 |

## Probes

| Command | Result |
|---|---|
| `bin/test -q --no-header` over the 93 modules a `git grep -l` under `tests/` lists for the paths and names the fix diff changed: the READMEs, the record layout, `chain_check`, the implement and settle skill files, the one-owner module, the changelog, the plan, the line-wrap and the passage modules | 4559 passed, 12 skipped, exit 0 |
| `bin/test -q --no-header tests/test_censuses.py tests/text/test_the_record_is_written_in_words.py` | 179 passed, exit 0 |
| `test_tmp_ranges.py`, read-only over the transcripts with phase 7's spawn filter, listing each ranged read of `docs/the-review-record.md` that returned file lines and whether it covers base lines 288-291 or 531-544 | 28 ranged reads: crafter 6, framer 12, proofer 7, sealer 3. Nine cover a changed line, 4 the first range and 5 the second. Exit 0; deleted |
| `test_tmp_moved_citations.py 95cbd99a4 350048ba0`, read-only | 439 anchors moved, 205 italic citations of them, 11 with no holder's path in their paragraph, each resolved in round-1#2. Exit 0; deleted |
| `test_tmp_above_below.py 350048ba0`, read-only | 22 italic spans followed by "above" or "below", one unresolved, a test's string literal. Exit 0; deleted |
| `git diff -U0 2d38c75af 29d8ca6a4^ -- docs/the-review-record.md` | two hunks, base lines 288-291 and 531-544 |
| `git diff --no-index --word-diff=plain` of the base *The guarantee* section against `docs/forms/the-guarantee.md`'s, each cut with one `awk` | the opening rewritten and the *The stamp* citation re-pointed |
