# Implementation Plan: a fold is read before the next round (#1442)

## Technical context

The tree as read at `7056ee61`.

The work is prose in four instruction files and pins in one test module. There is no code path.

- **`skills/implement/orchestration.md:49-81`** is the fold paragraph that *Scope* item 1 rewrites. It is pinned clause by clause by `tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it` (`:374-402`). Three clauses of that case belong to the crafter-named statements and stay as written: "in a file the crafter does not write, …", "After the fold commit, …" and "the orchestrator hands it to a fix pass …". The bold lead the case pins stays as well. `#test_the_orchestrators_run_judgments_are_rows_of_the_plan` (`:470-499`) asserts that the order section cites `frame/plan.md` *Judgments of the run*, and the rewritten paragraph keeps that citation.
- **`skills/implement/orchestration.md:93-100` and `:389-392`** carry *Scope* items 2 and 3, one sentence each. No test pins either (`git grep` over `tests` and `evals` for "folds the move" and "orchestrator folds it into that work", executed, no hits).
- **`skills/implement/SKILL.md:309-311`** carries *Scope* item 4. No test pins it (the same grep).
- **`agents/framer.md:240-247`** is the rule *Scope* item 5 rewrites. `tests/text/test_the_rules_have_one_owner.py` rule 16 (`:122-126`) needs `agents/framer.md` to carry "`docs/running/the-run.md` *The run* owns that rule", so the regression half keeps that sentence verbatim. The rule's `check:` line names the same module.
- **`skills/code-review/orchestration.md:71-80`**, the fix-pass fold sentence pinned at `test_the_rules_have_one_owner.py:204-208`, is not touched (*Scope* item 9).

**Where this meets the release's other work items.** The sibling file lists are the orchestrator's guess (`unverified`). The overlaps named here were read in this tree.

- **#1443** rewrites the merge-order paragraph inside `skills/implement/orchestration.md` *Orchestrator: how the work is routed*. That paragraph holds the version-move sentence of *Scope* item 3. #1443 also edits `agents/framer.md`, probably a step or rule other than `:240-247`. #1443 should merge first: its subject is that paragraph, and this item changes one clause in it. That clause is then re-applied to #1443's text when this branch integrates #1443's squash.
- **#1440** edits `agents/framer.md` and `docs/running/the-run.md` *The per-segment bars*. This item edits a different rule of `agents/framer.md`. Its change to `docs/running/the-run.md` *The run* is an operation of `frame/design.md` `## Rule changes`, not an edit, so the files do not collide. A fold exchange is a framer segment with few reads, and how its bar grades it is #1440's (`frame/design.md` *Scope*, Out). Neither item has to merge before the other.
- **#1444** may edit `skills/code-review/orchestration.md`, which this item leaves alone (*Scope* item 9). There is no ordering need.
- **#1439 and #1441** touch none of this item's files. #1439's readings are where the second *Done when* bullet is measured (`frame/questions.md` Q1).

**Failure scenario of the chosen approach, six months on.** One kind of failure is cost. Each decision now costs a framer exchange, and a framer resumed late in a long run carries the whole frame reading as context on every turn. The fold segments show that cost in `seal cost --segments` as framer rows. If the regressions they prevent stay fewer than the exchanges are worth, the settle narrows the route. The other kind is a boundary judgment. The orchestrator may treat a decision as a statement that HEAD contradicts and fold it itself, outside the framer's reading. The signal would be a `regression:` line whose grounds trace to an orchestrator fold of a "contradicted statement" that in fact changed what the work is. The reading of Q1 shows it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the structure: the orchestrator writes every fold and then reads the fold commit against HEAD, as #1318 left it (`frame/design.md` G3) | 0.35.0's `1794128303` round 3 (G9 (4)) came after #1318 shipped in 0.31.0. The premise that would keep the structure is that the writer, reading its own fold, catches what a second party would. That premise fails on G9: in each case the fold's defect passed both the orchestrator and the fix pass that built on it | rejected |
| Replace the structure for every fold, statements a crafter names included: the orchestrator writes no frame sentence at all after the frame is committed | A framer exchange at almost every phase boundary. Statements a crafter names are 14 of G10's 23 rows, and none of G9's regressions traces to one. That is cost with no record of a catch (`skills/core/SKILL.md` *The rule a mechanism is kept against*). Its one gain is that a frame file would have a single writer, which the `Written by` column of `skills/implement/SKILL.md` *3. The SDD file set* already does not claim: the orchestrator writes rows of `frame/plan.md` | rejected |
| The fix-pass crafter reads the orchestrator's fold as a claim before building, as it reads paste-ready text (#1286) | G9 (1): the fix pass built from the fold's words, and round 2 found that "nobody opened #1255". The crafter writes no frame file, so a defect it finds goes back to the orchestrator to fold again, and that second fold is unread. A fold placed before a verifying round has no crafter after it | rejected |
| The framer reads the orchestrator's fold and answers it, instead of writing it | Two hops for one sentence. The framer's answer to a defect is a rewrite, which is the chosen approach with an extra message | rejected |
| A check of table shape: count each table row's cells against its header across the work item's records, as `skills/settle/scripts/settle.py#plan_rows` already does for *Judgments of the run* | It catches one of G9's regressions, G9 (4); the other three are defects of meaning. `chain_check.py` runs at the pull request, after the rounds, and no hook fires before a round's spawn. A new mechanism with one catch fails the core's test | rejected |
| Send every decision to the framer's regression route: a reframe with new phase rows and the `Reframed` line | A reframe is a design change, and it restarts the count of finding rounds (`docs/running/the-run.md` *The run*). A fold rewrites sentences in place inside the design that was approved | rejected |
| Leave the fold to the next proofer round, which reads it anyway | The status quo cost: each regression in G9 took a fix pass and a verifying round (`frame/design.md` G8) | rejected |
| A decision's fold is written by the framer, resumed or spawned fresh, in one exchange shaped like G4's. The orchestrator writes the *Judgments of the run* row first, so the framer reads it with `plan.md`. Statements a crafter names stay the orchestrator's (chosen) | The failure scenario in *Technical context* | chosen |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 7 | `tests/text/test_the_rules_have_one_owner.py`, run narrow; each new clause shown red with its sentence deleted (contract rule 15); the crafter's reading of its range and of the work item's records (contract rule 12) | 3bb9e3be |

## Operational impact

None for a deployer. No migration, environment variable or dependency. The version move is not this item's unless the orchestrator assigns it (`skills/implement/orchestration.md` *Orchestrator: how the work is routed*).

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame, why the pull request title takes its prefix, which `pr.md` quotes; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-09 | The pull request's title takes `fix:`, and the kind that came closest is `feat:`. | The work moves an existing act, the fold of a decision, from the orchestrator to the framer, to repair the regressions folds caused; it adds no record format, command or check, and the framer's second route back is a route the frame-read exchange already had. | `skills/commit-pr-convention/SKILL.md` *Commit messages* |
| 2026-11-09 | Round 1's findings 1 and 2 change what the frame says the work is, so the orchestrator folded them before the fix pass, taking the round's reading: *Scope* item 1 gains a seventh thing, what a rejected decision leaves; *Scope* item 5's owner bullet adds the version move and a prevention home; and the first rule change's `to:` scopes "edits no frame file" to the exchange at the spawn. | The framer's rejection had no receiver, and the version move and a prevention home are decided by the orchestrator under other rules (`skills/implement/orchestration.md` *Orchestrator: how the work is routed*); the unscoped clause contradicted the sentence two lines below it (`trail/rounds/round-1.md`). The installed 0.35.1 rules still give this fold to the orchestrator. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
| 2026-11-09 | Round 2's finding 2 names an *Out* item HEAD contradicts after the merge of #1440, so the orchestrator rewrote it to the round's replacement: this work adds no grade for a fold exchange, which is read as a framer row of `seal cost --segments`. | #1440 (`74211b76`) removed the grade from `session_cost.py`, and the *Out* section is not dated, so it states the present (`trail/rounds/round-2.md`). The installed 0.35.1 rules give this fold to the orchestrator. | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* |
