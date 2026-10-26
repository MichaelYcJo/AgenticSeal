# Questions for the planner: settle writes each section's latest decision (#1033)

## Answered by the tree

The ticket left these open, and the tree answers them. Each names where the
answer was read, so a reviewer can overturn it by opening the same place.

1. **A1 The `## Rule changes` grammar does not change.** The refusals came
   from the precondition `settle` put on `from` (`rule_changes.py#apply_op`
   lines 262 to 272 refuse a `from` that is not found exactly once), not from the
   shape of an operation. Every `spec.md` in the tree parses (executed:
   `rule_changes.py#parse` over each), so a second grammar would only add a
   second reader. `from` now locates the text the framer read and is no
   precondition; `skills/settle/SKILL.md` *Rule changes* says so.
2. **A2 The pull request's check reads what it reads today.**
   `chain_check.py#rule_changes_read` parses and never places a `from`
   (lines 1583 to 1597), and a section that does not parse is still worth
   refusing at the pull request, because the settle cannot group it. Only
   `RULE_CHANGES_SAYS` changes, since "`settle` applies nothing from this
   spec" stops being the consequence.
3. **A3 #952's class moves to the settle, and nothing is added at the pull
   request.** The three shapes (a pin, a README copy, a long line) arose
   because the settle wrote `to` text verbatim and could write no sentence
   by hand (`round-1.md` finding 3, `round-2.md` finding 1, `round-3.md`
   finding 1 of `1792976216`). The settling session now writes the text and
   runs the documents' checks over it. A pull-request check of a spec's `to`
   texts would read text the settle will reword, which `CLAUDE.md` *The rule
   a mechanism is kept against* calls a reading guessed from words: a
   report, never a gate.
4. **A4 The split between script and agent.** The script does what reads a
   fact from git or the tree: which items are released, the merge order,
   which places overlap, whether a `from` or a `to` is found in a section,
   which open rows each record holds, whether a path a row names exists, and
   the removal. The settling session does what judges: which decision is
   latest, whether the code has moved past it, how the section reads, and
   whether a row is moot, answered or a measurement. Owner's direction steps
   2 to 5 put the reading on the agent (#1033 body); the script writes no
   policy document, so one writer holds `docs/`.
5. **A5 What replaces "The spec decides; the command applies. The step moves
   and does not verify."** "The specs say what was decided and in what
   order, the code says what holds now, and the settling session writes each
   section as the latest decision the code bears out. The script reads and
   removes; it neither writes `docs/` nor judges." What verifies the result
   is `plan.md` *Technical context*, the table under *How a settle's result
   is verified*.
6. **A6 The CI predicate drops its open-row and replay conditions.** Both
   would keep the settle's pull request and the release pull request red:
   `hygiene.yml` asks at `origin/<base_ref>`, and on the release pull request
   that is `main`, where the 41 records hold their rows open (executed:
   `git ls-tree origin/main seal/specs/`). Reading the removing commit's
   parent fails under the squash into `release/vX.Y.Z` (`CLAUDE.md` *Repo
   rule: the merge method is fixed per direction*). `plan.md` *Alternatives
   considered* holds each with its failure scenario.
7. **A7 This item does not run the settle.** `skills/settle/SKILL.md` *A
   settle is not a work item*, and the 0.22.4 release settle
   (`docs/release-checklist.md` *2b. Settle what earlier releases left
   behind*) runs it on the preparation branch after this item merges into
   `release/v0.22.4`, with the tree's script (`plan.md` *Operational
   impact*). The backlog settle #1024 is the precedent: a `no work item`
   pull request into `release/v0.22.4` whose body states each answer
   (`git show 4d5a6917`).
8. **A8 `1792935671` is not released at `origin/main`** (executed:
   `git ls-tree --name-only origin/main seal/specs/`), so the 0.22.4 settle
   leaves it, with every other 0.22.4 work item, for the next release's
   settle. The issue's done-when names it among the three refused specs; two
   of the three (`1792619408`, `1792627930`) are released.
9. **A9 The settle may change a file outside `docs/` that a written section
   leaves standing on the old fact**, such as a pin under `tests/` or a
   README copy, and names each in its pull request body. Contract rule 19
   asks that of whoever changes a fact, and the tree already expects it of a
   settle: `tests/test_the_retired_rules_await_their_settle.py`'s docstring
   says the pull request that settles `1792935671` deletes that file.
10. **A10 #602's base condition goes from `settle`.** It existed because the
    CI readers asked rows at the merge base (`settle.py` module docstring,
    *The rule arm*). Once the predicate no longer asks rows there, a closure
    in the working tree is the only fact `--apply` needs.
11. **A11 The settle runs the repository's `Broad gate` row once before its
    pull request.** `seal/config.md` names it, and the backlog settle ran the
    same commands (#1024's body, *How it was checked*). A settle is not a
    work item, so `broad-gate --record` does not apply to it.
12. **A12 A spec with no `## Rule changes`, and one whose section does not
    parse, leave like any other.** Today the first stays forever and the
    second is refused. None of the 41 released specs is either (executed: a
    shell walk), so the change costs the corpus nothing, and the settling
    session reads such a spec whole, as owner's direction step 5 asks.

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How is a row naming a measurement nobody has taken re-homed: one issue per row, or one issue per distinct measurement listing every row it would answer? The tree holds no rule for the shape of a re-homed row beyond "closed naming where it went" (`docs/the-record-layout.md` *The fold, and what tells it from a deletion*), and the choice is how the owner wants the tracker to read | a person | One issue per row: each row keeps its own thread, and the 0.22.4 settle opens dozens of issues. One issue per measurement: a Windows run or a paid evaluation is one issue listing each work item and row text, and each closure names that issue. Either way the code is the same; only the procedure's sentence in `skills/settle/SKILL.md` differs | One issue per distinct measurement, its body listing each row's work item, row text and answerer | open |
| Q2 | Does this item's pull request close #1033, or does the 0.22.4 settle's pull request? The issue's done-when includes settling the 41 held and the refused specs, which this item does not do (A7), and the tree holds no rule for which pull request closes an issue split this way | a person | This item's body says `Part of #1033` and the settle's body closes it: the issue stays open until the corpus is settled. This item closes it: the mechanism is the issue, and the settle is the checklist's step | This item's body says `Part of #1033`; the 0.22.4 settle's pull request closes it | open |
| Q3 | How many open `## Not verified` rows do the 41 released records hold, as the reader counts them? The framer's count, about 62, is an `awk` walk that is not `unverified_check.py#open_record_rows` | a measurement | The phase 1 dry run over the real tree (S10) prints every open row through the reader | S10's output, recorded in phase 1's record | open |
| Q4 | The exact headings and line shapes of the dry run and of `--apply`'s output. `spec.md` *In* items 1 and 2 name what each holds, and nothing in the tree fixes the words | the work | Phase 1 chooses them and pins each with a case, as contract rule 14 asks | Phase 1's choice | open |
