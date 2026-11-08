# Review round 1: 1794178395-a-fold-is-read-before-the-next-round

```seal
target: bd7b937c against release/v0.36.0
```

The round reviewed the branch against `release/v0.36.0` (`94d04d30`), at
`bd7b937c`, in a `git clone --no-local` of the branch worktree checked out
at the target, under the round's scratch directory. No earlier round
exists, so no fact is carried and every coordinate below was opened at the
target. No `seal/parity.md` is declared, and `seal/config.md` has no
`Record language` row, so the record is in English. The work item's records
that state the present were read whole at the target: `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md` and `pr.md`, then `trail/phases/phase-1.md`, against issue
#1442 (0 comments, `gh issue view 1442 --json comments,body`, executed
2026-11-09). The compliance axes were the issue's *Done when* and the
frame's *Scope* items 1 to 10 and `## Removes` rows. The quality axes were
the comparison table's rows that apply to instruction text (state
transitions of the fold exchange, error paths, response shape of the two
hand-backs), plus this change's own: what each party does when the framer
answers a decision with a rejection, and whether each rewritten sentence
has one reading.

The orchestrator's account was read as claims. It claimed `bd7b937c`
writes `pr.md` and one *Judgments of the run* row; `git show --stat
bd7b937c` lists `pr.md` (10 lines added) and `frame/plan.md` (1 line
changed) and nothing else (executed). Each of the six quotes in `pr.md` was
found word for word, runs of whitespace collapsed, at the source its
coordinate names (executed, the probe below).

## Findings

### 1. A decision the framer rejects has no route in the orchestrator's instruction, and the orchestrator's row written before the exchange then records a fold that did not happen

```seal
severity: should
location: `skills/implement/orchestration.md:69-75`, `skills/implement/orchestration.md:118-125`, `skills/implement/orchestration.md:413-418`, `agents/framer.md:245-250`, `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:30-48`, `tests/text/test_the_rules_have_one_owner.py`
evidence: read `agents/framer.md:245-250`, `skills/implement/orchestration.md:49-97`, `skills/implement/orchestration.md:118-125`, `skills/implement/orchestration.md:131-140`, `skills/implement/orchestration.md:413-418`, `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:30-48`; executed `grep -n -i reject skills/implement/orchestration.md`, which returns only lines 136, 137 and 149 of the exchange at the spawn
```

Why it matters: `agents/framer.md:245-248` lets the framer answer any
decision but the owner's with "reject with grounds" and write the rejection
as a row of *Alternatives considered*. The paragraph the orchestrator reads,
`skills/implement/orchestration.md:49-97`, says what it does with the
framer's hand-back in two cases only: a defect the hand-back names in the
orchestrator's row (`:73-74`) and a statement the fold contradicts in a
file the framer does not write (`:75-77`). Nothing says what follows a
rejected decision. Three consequences follow from the text as it stands.
First, the orchestrator wrote the decision's row of *Judgments of the run*
before sending (`:68-71`), so after a rejection that row states a decision
the frame does not carry, while the *Alternatives considered* row states
its rejection. A crafter or the settle reading `plan.md` then holds two rows
that disagree on what the work is. A rejection is not "a defect in the row",
so `:73-74` does not cover it. Second, a round finding whose route changes
the frame goes to a fix pass with no instruction on what that pass builds
once the frame change is refused. Third, two decisions are ones other rules
oblige: the prevention home, which "the work item in progress builds"
(`:121-122`), and the version move, which the crafter "reads its version
write" from (`:413-418`). The framer may reject either, and the paragraphs
that oblige them do not say which side stands. The exchange at the spawn
answers the same question for proposals: "a disagreement left after it
stands as the framer's judgment, which the orchestrator quotes in the work
item's `pr.md`" (`:138-141`). The fold paragraph says it reuses that
exchange's shape (`frame/design.md` G4) but does not carry that sentence.
The frame itself has the same gap: *Scope* item 5's second bullet
(`frame/design.md:42`) grants the rejection and *Scope* item 1's bullets
(`:31-36`) give it no receiver, so the build matches the frame and the
defect is the frame's.

The fix below is one reading; which side stands for the version move and the
prevention home is the framer's judgment to fold. It reaches
`skills/implement/orchestration.md`, `agents/framer.md`, *Scope* items 1
and 5 of `frame/design.md`, and the pins of
`tests/text/test_the_rules_have_one_owner.py`. The changelog fragment's
sentence on how the framer answers each decision would also take the
version move and the prevention home, so the fix pass owes
`changelog.md:3` too.

```markdown
<!-- skills/implement/orchestration.md, after "The orchestrator corrects its
row where the framer's hand-back names a defect in it," (line 73) -->
A decision the framer rejects stands as its judgment, as a proposal left
after the exchange at the spawn does: the orchestrator rewrites its row of
*Judgments of the run* to record the rejection and what the decision's
source takes instead, a finding's route or the next spawn's scope, and
quotes the framer's *Alternatives considered* row in the work item's
`pr.md`. The version move and a prevention home are folded as an owner's
decision is, because other rules give the orchestrator to decide them.

<!-- agents/framer.md, replacing "A decision the owner made is folded as the
owner made it," (line 248-249) -->
A decision the owner made, the version move and a prevention home are
folded as they were made,

<!-- tests/text/test_the_rules_have_one_owner.py, one pin in each case -->
"A decision the framer rejects stands as its judgment",
"A decision the owner made, the version move and a prevention home are folded as they were made",
```

### 2. The `to:` of the first rule change says the orchestrator edits no frame file, and two lines later that it folds statements into them

```seal
severity: should
location: `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:95-100`
evidence: read `seal/threads/1794178395-a-fold-is-read-before-the-next-round/frame/design.md:89-100`, `docs/running/the-agent-set.md:64-71`, `skills/implement/orchestration.md:78-84`
```

Why it matters: the settle writes this `to:` into
`docs/running/the-agent-set.md` *One contract every agent receives, and one
definition each*. In the `from:` text, "the orchestrator edits no frame
file" closes a sentence about the exchange at the spawn, and the paragraph
around it (`docs/running/the-agent-set.md:64-71`) is about that exchange
alone. The `to:` keeps the clause unscoped and then widens the paragraph to
the whole run: "A decision made later in the run is folded by the framer
too, ...; the orchestrator folds only the statements a crafter's hand-back
names as contradicted by HEAD." Folding those statements is an edit of a
frame file (`skills/implement/orchestration.md:78-84`), so a reader of the
settled paragraph holds "edits no frame file" and "folds ... statements"
together and has to choose. The fix scopes the first clause to the
exchange, which is what it said where it stood.

```markdown
  to: The framer judges what the work should be and the orchestrator holds the
    issue, so a frame weaker than the issue asks is found by the party that holds the issue
    and decided by the party that drew the frame, and the orchestrator edits no frame file
    in that exchange. A decision made later in the run is folded by the framer too, so each
    sentence of the frame that says what the work is or why is the framer's; the
    orchestrator folds only the statements a crafter's hand-back names as contradicted by
    HEAD.
```

### 3. `gaps.md` says no case runs a framer, and the framer has behaviour cases

```seal
severity: should
location: `seal/threads/1794178395-a-fold-is-read-before-the-next-round/gaps.md:7`
evidence: executed `ls evals/behaviour/framer/`, which lists six `rule-framer-*` cases; read `evals/behaviour/framer/rule-framer-word-count/case.yaml:1-16`
```

Why it matters: the row's reason ends "and no case runs a framer".
`evals/behaviour/framer/` holds six `rule-framer-*` behaviour cases, and the
one this round opened, `rule-framer-word-count/case.yaml`, names a model,
`max_turns` and the `Agent` tool for its runs. What the row means is that no
case runs a framer through a fold. The sealer reads this row against the
tree, where the literal sentence does not hold. `pr.md` quotes the row's
first clause only, so the quote does not change.

```markdown
| whether a framer resumed or spawned for a fold follows the fold half of `agents/framer.md` *Rules*, and whether `regression:` lines traced to a decision's fold stop recurring; the agents of this release's own runs carry the installed 0.35.1 `agents/framer.md`, which has no fold half, and no case runs a framer through a fold | a measurement: `frame/questions.md` Q1, read on the flow-measurement readings #1439 posts for 0.36.0 and later |
```

## Confirmations

What matched: the fold paragraph at `skills/implement/orchestration.md:49-97`
carries each of the six things *Scope* item 1 lists: the definition of a
decision with its examples called open (`:52-56`), the one message with
grounds and coordinates (`:59-62`), the resumed or fresh framer (`:63-68`),
the row written first and left uncommitted (`:68-71`), the framer's
hand-back routed to the orchestrator for `routing.md` and `pr.md` and to a
fix pass for `gaps.md` and `changelog.md` (`:75-77`, `:92-94`), and the
crafter-named statements kept with the orchestrator, folded in a commit of
its own with no framer (`:78-84`). The sentence "The orchestrator rewrites
the sentence of the frame the decision changes, where it stands" is gone
(`git diff 94d04d30..bd7b937c -- skills/implement/orchestration.md`,
executed). Read.

What matched: `agents/framer.md:240-268` holds the eight things of *Scope*
item 5, and its regression half keeps "`docs/running/the-run.md` *The run*
owns that rule", which rule 16 of `RULES` pins
(`tests/text/test_the_rules_have_one_owner.py:122-126`); the module passes
(executed, probes). *Scope* items 2, 3 and 4 stand at
`skills/implement/orchestration.md:121-125`, `:415-418` and
`skills/implement/SKILL.md:310-312`. Read.

What matched: `## Removes` rows 1 to 6 each match a removal or a rescoping
in the diff, and the diff removes nothing the table does not name. Row 2
says the sentence opening "After the fold commit" stays for crafter-named
statements; it stands at `skills/implement/orchestration.md:89-92` with the
clause "a decision's fold is read by the framer that writes it". Read.

What matched: the phase record's `seen red` claim. Claimed: each new clause
was deleted alone by `seal mutate` and each mutant read red on its own pin.
Three of the 20 mutants were run again: deleting " and spawns no framer"
from the order paragraph failed `test_a_decision_after_the_frame_is_folded_into_it`
at its own pin, and deleting ", and you do not repeat the wide reading of
step 4" and narrowing "folded as the owner made it" in `agents/framer.md`
both read red (executed, probes). The other 17 are carried as the
crafter's claim. The phase record's decision on "After the fold commit"
says "The sentence before it now says that the orchestrator folds such a
statement in a commit of its own"; at `8407aabb` the sentence just before
it is the one on dated sections (`skills/implement/orchestration.md:84-89`),
and the "commit of its own" sentence stands one before that. The scoping
the decision describes holds; only the position is off by one sentence.

What matched: the three `## Rule changes` `from:` texts stand word for word,
whitespace collapsed, at `docs/running/the-agent-set.md:66-69`,
`docs/running/the-agent-set.md:101-103` and `docs/running/the-run.md:65-67`.
The other policy-root sentences on folds read in the class search
(`git grep` for "fold" near "orchestrator", executed) are
`docs/running/the-agent-set.md:130-138`, where folding a decision stays an
orchestrator judgment written as a row, which the change keeps, and
`docs/releasing/issues-and-milestones.md:325-327`, which cites the order
paragraph and states no writer. Read.

What matched: G9 (1) was opened at `v0.27.3`: round 2 of
`1793538230-code-text-brought-to-the-tree` names the orchestrator's fold
`1ac8b651` and its `regression: round-1#1` traced to `frame/design.md:28`
(executed, `git show`). The other G9 rows are carried as the framer's
executed claims. The changelog fragment's "Four regressions in 0.27.3,
0.29.0 and 0.35.0" matches G9; `1794128303`'s round 3 was added in
`591c136c`, which `v0.35.0` contains (executed).

The *Out* item that keeps crafter-named statements with the orchestrator
departs from the issue's first *To weigh* bullet, which names the framer for
the frame. The frame gives its grounds (G10: 14 of 23 fold rows, none of
G9's regressions), and *To weigh* asks for a weighing, not an outcome, so
this round reads it as a judgment with grounds and not a finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The phase-boundary run's figures, 49 modules with 1573 passed and 7 skipped; this round ran one module and no wider set | `trail/phases/phase-1.md:73-77` | the orchestrator's broad run |
| The full suite, the repository-wide lint and the typecheck, `unverified` by contract rule 2 | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether the version-move clause of *Scope* item 3 survives the integration of #1443's squash, which rewrites its paragraph; this round reviewed the branch as it stands | `skills/implement/orchestration.md:413-418` | the orchestrator at the integration, and the round that reads it |
| Whether a framer resumed or spawned for a fold follows the fold half; no case runs one | `agents/framer.md:240-264` | a measurement, `frame/questions.md` Q1 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist` | exit 0, 30 passed |
| `bin/seal mutate skills/implement/orchestration.md --replace " and spawns no framer" "" --tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -x"` | baseline passed; the mutant read red, failing `test_a_decision_after_the_frame_is_folded_into_it` on "the order no longer says 'so the orchestrator folds it in a commit of its own and spawns no framer'"; file restored |
| `bin/seal mutate agents/framer.md --replace ", and you do not repeat the wide reading of step 4" "" --replace "folded as the owner made it" "folded" --tests` (the same command) | 2 mutants, 2 red, 0 survived; file restored, `git status --short` empty |
| a Python script matching each `pr.md` quote, whitespace collapsed, against `changelog.md`, `frame/plan.md` and `gaps.md` | all six found |
| `python3 skills/code-review/scripts/chain_check.py --baseline 94d04d30 --root <the branch worktree> --worktree`, before this record | exit 0; notices only for the absent round record, `trail/gate.md` and `guarantee.md`; no notice at `frame/design.md` |
