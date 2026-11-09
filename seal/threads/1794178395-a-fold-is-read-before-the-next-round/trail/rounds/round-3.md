# Review round 3: 1794178395-a-fold-is-read-before-the-next-round

```seal
target: 0e4d0775 against release/v0.36.0
```

This is a verifying round. It reviewed `0e4d0775` against `release/v0.36.0`
(`c7bb14ca`), in a `git clone --no-local` of the branch worktree checked out
at the target, under the round's scratch directory. The diff since round 2's
target `75b492af` was read whole. It holds `2885dfa3` (round 2's record),
`70c464cf` (the frame fold of round 2's finding 2), `3f894d7e` (the fix of
round 2's finding 1), `a4704032` and `82c46f10` (the class pins and a comment
correction), `3989a6a0` (a `gaps.md` *Not done* row) and `0e4d0775` (round
2's close blocks). Since `75b492af` the diff changes no file under
`skills/`, `agents/` or `docs/`, and of the work item's records only
`frame/design.md`, `frame/plan.md` and `gaps.md` (executed, `git diff
--stat`). No `seal/parity.md` is declared, and `seal/config.md` has no
`Record language` row, so the record is in English.

The work item's records that state the present were read whole at the
target. These are `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. The round also
read `trail/phases/phase-1.md` and rounds 1 and 2. Carried from round 2
without re-deriving them: the merge `75b492af` is the automatic merge, the
merged version-move paragraph reads with one meaning, and no sibling
`## Rule changes` collides with this item's. None of the files those facts
rest on changed since `75b492af`. Re-derived this round: each fix, each new
pin's mutant, the `gaps.md` row's mutant, and the `pr.md` quotes.

The fix pass's account was read as claims. It claims the four finding pins
were widened past round 2's paste-ready text in three places, and that each
was red alone under `seal mutate`. It claims a class listing deleted each
sentence this work item added to `skills/implement/orchestration.md` and
`skills/implement/SKILL.md` and found nine with no case reading their
meaning. It claims eight of the nine were pinned and each was shown red, and
that the ninth, the version-move clause, is recorded in `gaps.md`. The round
re-ran one mutant per new pin, twelve in all, and the ninth sentence's
mutant (executed, `## Probes`). Each result matches the claim.

## Findings

None. This round leaves nothing open.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the orchestrator's half of a rejected decision is now held
clause by clause.
`tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it`
pins four strings. One is the lead with its citation of the spawn exchange.
One is the row rewrite through "a finding's route or the next spawn's
scope,". One is the `pr.md` quote. The last is the version-move and
prevention-home sentence, through both of its citations
(`tests/text/test_the_rules_have_one_owner.py:424-436`). The three places the
pins go past round 2's paste-ready text each hold more of the same sentence
and nothing outside it. Each string occurs in
`skills/implement/orchestration.md:74-84`. A mutant of each, run alone,
fails the case on that string's own assertion message. Round 2's mutants 2
and 3, which survived, are covered by the second and fourth pins. Executed.

```seal
confirms: round-2#2
```
What holds: `frame/design.md:65` now reads "A grade for a fold exchange's
cost. `session_cost.py` grades no segment since #1440 (`74211b76`), so a fold
exchange is read as a framer row of `seal cost --segments`, and this work
adds no grade for it." That is round 2's replacement word for word, written
by the orchestrator's fold at `70c464cf` under the installed 0.35.1 rules.
`frame/plan.md:55` adds the fold's *Judgments of the run* row. The row names
the trigger, the grounds and the document judged against, and gives the
round record as its source. `skills/verify/scripts/session_cost.py` still
holds no grade (executed, `grep -n -i grade`, only "degrades" at `:926` and
`:1897`). Segments are labelled from the spawn's `subagent_type`
(`:1348`), and `segment_slices` (`:1652`) slices a resumed agent's
transcript, so the item's "framer row" holds whether the framer is resumed
or spawned fresh. Read and executed.

What matched: the eight class pins of `a4704032`. Six stand in the same case
as the finding pins. They cover the fold's reason, the open list of
examples, the orchestrator correcting its row, the one commit, the framer's
hand-back sending `routing.md` and `pr.md` to the orchestrator, and "a
decision's fold is read by the framer that writes it". The seventh is the
prevention-home sentence, in `test_a_recurring_problem_gets_a_prevention_home`
(`tests/text/test_the_rules_have_one_owner.py:526-530`). The eighth is the
scope sentence of `skills/implement/SKILL.md:310-312`, in
`tests/behaviour/test_a_phase_hands_the_next_one_a_record.py:209-214`. Each
mutant, a deletion or the old wording put back, failed the case on that
pin's own assertion message (executed, `## Probes`).

Read against their groups, no new pin repeats a pin of its case. The open-list
pin starts where the older "A decision is anything that changes what the
frame says the work is or why" pin ends. The lead pin replaces the older
shorter one rather than standing beside it. The SKILL.md pin joins a case
that already reads the same paragraph of *3. The SDD file set*. Every pin is
a whole-sentence string that the source must contain, which is the shape of
every older pin in these cases. So each pin holds the sentence's wording,
and a rewording that keeps the meaning fails it, as it fails the older pins.
Read.

What matched: the class method. The fix pass took apart this work item's
own sentences in the two skill files, one deletion or reversion per
sentence. That is rule 12's second method over a closed set, and it is a
whole list, not a sample. `agents/framer.md`'s fold half was outside that
listing. Its sentences are held by the twelve pins of
`test_the_framer_folds_a_decision_it_is_sent`, each shown red in phase 1. The
round re-ran one of them in round 2 and found it red. Read.

What matched: the `gaps.md` *Not done* row on the version-move clause of
*Scope* item 3 (`skills/implement/orchestration.md:439-442`) is right under
the frame. Its facts hold. With "move is a decision the framer folds into
that section" put back to "orchestrator folds the move into that section",
the mutant survives all 12 modules under `tests/` that name the file
(executed, `## Probes`). A search for the paragraph's distinctive phrases
over `tests` and `evals` finds no case that reads the paragraph. Its one
hit is a docstring (executed, `git grep`; a sample of six phrases, with the
mutant as the deciding evidence). Its judgment holds too. *Scope* item 6
(`frame/design.md:52`) asks for pins of *Scope* item 1's clauses and of
*Scope* item 5's fold half. It names no pin for *Scope* items 2 to 4, and
`frame/plan.md` *Technical context* records that no test pins those
sentences. The rule the clause restates is held where it lives: the fold
paragraph's example list ends "or the version move", and its sentence on the
move and the home folded as an owner's decision is pinned. So a reversion of
the routing clause would leave a second statement that contradicts a pinned
first one. Reading the tree finds that; no case does, and the frame asks
for none. Pinning *Scope* items 2 and 4 went past the frame, and adding no
case for item 3 departs from nothing. The row ends "Who answers: the
orchestrator, by a route of its choosing". This round's reading is that no
case is owed, so leaving the clause unpinned is a complete answer to that
row. Read and executed.

What matched: the `pr.md` quotes. All six were found word for word, with
runs of whitespace collapsed, at the source each coordinate names at the
target (executed, `## Probes`). The records that state the present
contradict nothing at the target. The *Scope* items name no exclusive home
for the pins. The dated *Technical context* states `7056ee61`. The
changelog's "No check, hook or mark is added" still holds, because the diff
adds pins to existing cases and no check. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `0e4d0775`, `unverified` by contract rule 2; this round ran three modules under mutation and no wider set | `seal/config.md` `Broad gate` row | the orchestrator's broad run |
| Whether a framer resumed or spawned for a fold follows the fold half; no case runs one | `agents/framer.md:253-286` | a measurement, `frame/questions.md` Q1 |

Nothing is open in this round's findings. What comes due is the
orchestrator's broad run at HEAD, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/implement/orchestration.md --replace <fragment> <change> --tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist"`, run once per mutant, eleven mutants, one inside each sentence the new pins of `test_a_decision_after_the_frame_is_folded_into_it` and `test_a_recurring_problem_gets_a_prevention_home` hold | each red, "1 failed, 29 passed", failing on the assertion message that quotes its own pin; file restored |
| `bin/seal mutate skills/implement/SKILL.md --replace "a scope a spawn gives beyond it is a decision the framer folds into the" "a scope a spawn gives beyond it is a decision the orchestrator folds into the" --tests "bin/test tests/behaviour/test_a_phase_hands_the_next_one_a_record.py -q -p no:xdist"` | red, "1 failed, 9 passed", at `test_a_phase_hands_the_next_one_a_record.py:211` on the scope pin |
| `bin/seal mutate skills/implement/orchestration.md --replace "move is a decision the framer folds into that section, as *Orchestrator:" "orchestrator folds the move into that section, as *Orchestrator:" --tests "bin/test <the 12 modules under tests/ that name skills/implement/orchestration.md, tests/test_conftest.py left out> -q"` | SURVIVED, 552 passed |
| `git grep` over `tests` and `evals` for six phrases of the paragraph *Which branch the pull request lands on is decided with the routing question* | two hits: a docstring at `tests/behaviour/test_the_set_a_work_item_always_has.py:263`, and the new pin at `tests/text/test_the_rules_have_one_owner.py:434`, which reads the fold paragraph |
| `python3 -I -c` matching each `pr.md` quote, with runs of whitespace collapsed, against `changelog.md`, `frame/plan.md` and `gaps.md` | all six found |
| `git -C <clone> status --short` after the mutants | empty |
