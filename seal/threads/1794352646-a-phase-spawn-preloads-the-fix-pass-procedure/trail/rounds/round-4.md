# Review round 4: 1794352646-a-phase-spawn-preloads-the-fix-pass-procedure

```seal
target: ac4930298, fixes 3fd5c59ec..ac4930298
```

This round verifies the merge of `release/v0.37.3` into the branch. #1473
landed there as `af923302c` (#1514), and `ac4930298` merges the base. The
conflict resolution was read with `git show ac4930298`, and the merged tree
with `git diff 3fd5c59ec ac4930298`. That second diff holds #1473's
changes: `agents/framer.md`, the new `skills/implement/fold-and-reframe.md`,
`skills/implement/orchestration.md`, three test files and #1473's work item
directory. #1473's own diff was reviewed in its own rounds. Here it is read
only where it meets this item's code and records.

`routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md`
were each read whole at `ac4930298`. None of them changes in the merge.
Rounds 1 to 3 closed no finding that is still owed an answer: round 3
opened none. So this round carries no `confirms:` line.

## Findings

### 1. The plan still says this item merges before #1473, and no record says why #1473 merged first or where the version move stands

```seal
severity: should
location: `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:44`
evidence: executed `gh pr view 1514 --json baseRefName,mergedAt,state` (MERGED into `release/v0.37.3`), `git show af923302c:.claude-plugin/plugin.json` (`0.37.2`), `git grep -n -i "out of the stated order\|merged first\|before #1471\|after #1473" -- 'seal/threads/*/frame/plan.md'` (no hit); read `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:44`, `:51`, `seal/threads/1794352647-a-first-frame-preloads-the-fold-procedure/frame/plan.md:41`, `:45`, `:53`, the same file's *Judgments of the run*, `skills/implement/merge-order.md`, `docs/releasing/branch-and-release.md:30-48`
```

Why it matters: the sealer and the settle read this plan against the tree,
and the tree now shows the opposite order. Any work item merged out of the
order its plans state owes a recorded judgment. This one also broke the
release's rule for where the version move goes. That leaves a decision with
no grounds in the records, which `skills/core/SKILL.md` *A judgment stands
on a source document, and is written down with both* asks for.

The grounds:

- **Claimed** in `frame/plan.md:44` (*Overlap with the release*, the #1473
  row): "Merges first" is `#1471`. The row's grounds say "#1473's
  integration is a one-hunk merge inside the rounds it spends anyway".
  #1473's plan states the same order (`seal/threads/1794352647-a-first-frame-preloads-the-fold-procedure/frame/plan.md:41`, `:45`)
  and takes no version move (`:53`).
- **Found:** #1473 merged into `release/v0.37.3` first, as `af923302c`. The
  base it left still reads `0.37.2`. This branch did the integration, at
  `ac4930298`.
- **The rule broken:** `skills/implement/merge-order.md` lets the
  orchestrator choose the order "with the item that carries the move still
  first". It also says the orchestrator "merges that item before every
  other item of the release". The move is still this item's (`0083fe9e2`),
  so the first pull request into the branch did not carry it.
- **What is missing:** `merge-order.md` asks for a choice of order like
  this to be written "as a row of `frame/plan.md` *Judgments of the run* in
  the plan of the item it merges out of the stated order". No plan holds
  that row. The search above finds none, and #1473's *Judgments of the run*
  holds only its title row.

Nothing ships wrong because of this. Once this item lands, the release moves
the version. The `hygiene` workflow also fails a release pull request into
`main` that changes `skills/` or `agents/` without moving it
(`docs/releasing/branch-and-release.md:43-48`). So the finding is the
record and the stale row, not the version.

The grounds of the out-of-order choice are the orchestrator's. Only it knows
them, so the snippet marks them and does not supply them. The row below
corrects the #1473 row of *Overlap with the release* in place:

```markdown
| #1473 | `tests/text/test_the_rules_have_one_owner.py`, where this work changes row 15 and the comment at `:277` and #1473 changes the fold's rows; `tests/behaviour/test_docs_line_wrap.py#COVERED`, where this work adds `skills/implement/fix-pass.md` after `merge-order.md` and #1473 adds `skills/implement/fold-and-reframe.md` there | #1473 | Both plans ordered this item first, because it carries the release's version move. #1473 landed first as `af923302c` (#1514), and this branch merged the base at `ac4930298`, keeping both `COVERED` entries; *Judgments of the run* holds why. |
```

The row below is new, appended to *Judgments of the run*:

```markdown
| 2026-11-11 | #1473 merged into `release/v0.37.3` before this item, out of the order both plans state, and the version move stays with this item | GROUNDS NOT IN THE RECORDS: why #1473 merged first is the orchestrator's to state. The first pull request into the branch therefore did not move the version, which `skills/implement/merge-order.md` asks of it; this item's `0083fe9e2` still moves it, and the `hygiene` workflow holds the release pull request into `main` to it. The integration was one conflict in `tests/behaviour/test_docs_line_wrap.py#COVERED`, resolved at `ac4930298` by keeping both entries | `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in* |
```

The snippet does not reach `frame/plan.md:51`. That sentence reads "This work
item is the first ordered to merge into `release/v0.37.3`", and it is still
true of the order the plans state. `merge-order.md` names #1473's plan as
the home of the row. The orchestrator chooses whether the row goes there,
in a directory that has already landed, or here, where the stale row
stands. This record names this plan, because the fix pass and the
orchestrator can reach it on this branch.

## Confirmations

What matched: the merge's one conflict resolution
(`tests/behaviour/test_docs_line_wrap.py:156-165` at `ac4930298`). It keeps
#1473's `skills/implement/fold-and-reframe.md` and then this item's
`skills/implement/fix-pass.md`, both after `skills/implement/merge-order.md`.
Its comment now ends "wrapped as it was", because "the same way" pointed at
an entry that is no longer the one above it. `git show ac4930298` shows that
hunk as the only one the merge resolved by hand. Read.

What matched: `tests/text/test_the_rules_have_one_owner.py` merged with both
sides' edits standing. This item's row 15 carrier `FIX_PASS_PROCEDURE`
(`:27`, `:143`) and its comment at `:283` stand beside #1473's `FOLD`
carrier of row 16 and its rows 4, 8, 12 and 25. Read, and executed in
*Probes* row 1.

What matched: this item's records still state the present after #1473's
change to the tree, apart from finding 1. Each citation into a file #1473
changed still resolves:

- `frame/plan.md:61` cites `skills/implement/orchestration.md` *Orchestrator:
  where a decision or a lesson is written* (`:477`) and its paragraph **A
  lesson seen once is given a home or judged not worth one.** (`:492`).
- `frame/plan.md:63-64` cite *Orchestrator: the order inside a ticket*
  (`:21`) and its paragraphs **A decision made after the frame is committed
  is folded, in place, into** (`:52`) and **One fold reaches every statement
  of the fact it changes.** (`:75`). #1473 changed the paragraph between
  them and not these two.
- The route row (`frame/plan.md:65`) cites
  `skills/code-review/orchestration.md` *A regression is routed by
  comparing the fix with the frame*, which still stands at `:218`.

`frame/design.md` G6 says `agents/framer.md` step 3 reads three sections of
`skills/implement/SKILL.md` and not *5.*. At `ac4930298`,
`agents/framer.md:52-56` still names the same three sections, so the claim
holds after #1473's rewrite of that file. `frame/plan.md:46` says
#1472 later finds a moved sentence at its new path. That row is about
#1472, and #1473's move does not touch this item's files.

Executed for the citations: `git grep -n -F` on each heading and lead.
The cited-section check passes (*Probes* row 1).

What matched: `pr.md` is unchanged by the merge, and its six quotes still
stand word for word in `frame/plan.md` at the rows they name. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Why #1473 merged before this item, against the order both plans state | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/plan.md:44` | the orchestrator, in the row finding 1 asks for |
| The broad gate at the work item's HEAD, which the merge moved; the suite is `unverified` here | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/gaps.md:8` | the orchestrator, by `seal gate --record` after the rounds settle |
| Whether a fix pass, a resumed implementer among them, opens `skills/implement/fix-pass.md` at step 9 (S3) | `seal/threads/1794352646-a-phase-spawn-preloads-the-fix-pass-procedure/frame/design.md:53` | the orchestrator, from the transcript of the first fix pass after the merge |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_waiver_decided_at_start.py -q -p no:xdist` | 373 passed, 2 warnings, exit 0 |
