# whether a ledger or record line is live has seven rules — questions for the planner

<!-- seal/specs/1791852615-whether-a-ledger-line-is-live-has-seven-rules/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## Decided from the tree, so nobody reopens them

The issue left these judgments open, and the tree answered each one. Each
answer is a judgment a person may overturn by opening the grounds named here.

| # | Judgment | Grounds |
|---|---|---|
| D1 | The seven give three answers, not one and not seven: a line that HOLDS something is read on doubt, a line that EXCUSES or DECLARES something is parked on doubt, a line a record's rows are COUNTED on is blanked the same way on both sides | 1790260566's D1 split the first two and named the readers on each side; `docs/the-evidence-ledger.md` states each direction once (§*The fold* > "A marker counts only on a live line"; > "A retirement would break every ledger row"); `readable`'s docstring states the third ("keeps the two sides of the comparison counting the same table") and its callers are all record readers that refuse an absent table |
| D2 | No two of the seven merge | each pair judged in `plan.md` §*Alternatives considered*; no pair has the same consequence and a behaviour difference worth a change; 0 issues since 0.18.0 in the family (#834 part 8), which the issue itself offers as the ground for stating rather than merging |
| D3 | `claim_lines`' positional scanner is not built | Q1 (a) of 1790260566 is built and documented (`skills/evidence-check/SKILL.md` §*A comment is an aside only where it begins a line*); (b) widens the quiet direction and costs the code-span state `live_lines` paid five rounds for; no issue since reports a mid-line comment |
| D4 | The 46 rows `readable` would blank are the price of a merge refused, not a defect | `readable`'s callers at a8db6161 are the round records, `overview.md`, `--exempt` files and the review-history guard; none hands it a ledger file (`plan.md` §*Technical context*); the figure is #867's, read and re-derived in phase 2 before a ledger row cites it |
| D5 | The statement's home is `docs/the-evidence-ledger.md`, written by the build | the two direction statements it joins are there; #835's build wrote `docs/the-reader-registry.md` directly (dae101ab), so a build writing a statement in `docs/` under its own marker is the precedent; `skills/settle/SKILL.md` §2 is the shape |
| D6 | `## Removes` names the seven census lines and nothing else | no reader, rule sentence or pin leaves; the census lines leave by the registry's rule, and naming them makes the records arm read each as a claim of absence rather than report a divergence (`docs/the-reader-registry.md` §*A frame names what its work removes*) |
| D7 | The direction table is one test module, not a row in each reader's module | the table's value is the seven side by side; seven modules keep seven separate pins and no row where a changed direction is visible against the others |
| D8 | The classes and directions each unit declares start from the inventory's reading and are settled at the unit by the builder | the inventory read six of the seven (E9, E58, S9, rows 72–74, row 96) and this frame reads the rider's; the registry says a helper's direction is read at its callers, which the builder has open and the framer does not |

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Q1 of `seal/specs/1790260566-a-row-inside-a-fence-reads-as-live/questions.md` is still ⬜: *is a comment that opens part-way along a line an aside?* Its default, (a), is built, and this frame records the grounds for leaving (b) unbuilt (D3). Does the owner tick that row closed on this work's grounds, or leave it open? The tree cannot settle it: a framer opens rows and does not own their answers, and that row names the owner | a person | **(a) Tick it** — `settle --retire-process` removes that directory after its release either way, and a ticked row stops the next framer re-reading an open question. **(b) Leave it** — the question stays visible until somebody wants the scanner. Neither answer changes what this work builds | **(b)**: this work edits no released work item's record; the grounds stand in `spec.md` §*Scope* and D3 | ⬜ |
| Q2 | Before and after phase 2, do `evidence-check --strict .`'s anchor counts and verdicts, the records arm's names-read and names-refused counts, and `settle --dry-run`'s anchored rows stay the same on this tree? | a measurement | the three commands at the base and on the branch, counts in `phases/phase-2.md` | proceed; a count that moves is a verdict that moved, which `spec.md` S6 forbids, and the phase answers it before closing | ⬜ |
| Q3 | What are the two figures the issue cites, re-derived on this branch — the rows `quoted_lines` skips against the rows `live_lines` parks over the released ledgers, and the rows `readable` would blank, by file? | a measurement | one `test_tmp_*` probe over `seal/ledger.md` and `seal/releases/*.md`, deleted after; the figures and their moment in `phases/phase-2.md` and the ledger row | proceed; `spec.md`'s Grounding row labels the issue's figures *read* until this is done | ⬜ |
| Q4 | For a shape in the corpus and a reader whose docstring states no answer on it, which of the reader's stated bias and its measured behaviour does the table pin? | the work | the phase has the unit and the shape open; the framer has neither | pin the measured behaviour where it agrees with the stated bias; where it does not, that is a finding — record it in the phase record and in `overview.md` as a divergence, and pin nothing for that cell until a person reads it | ⬜ |
| Q5 | Which direction word does each of the seven `Reads:` lines take where a unit's value feeds two callers that end differently (`live_lines` at the fold against the gather; `hidden_lines` in a hook against the gate)? | the work | the registry says `mixed` where both happen and reads a helper at its callers; the phase has the callers open | `mixed`, with the prose between naming which caller refuses and which passes, as `spec.md` §*Data & interfaces* proposes | ⬜ |

**`Who can answer` takes one of three values and nothing else.** They are
*a person* (only this kind blocks the build, and Q1 does not block it,
because either answer leaves the build unchanged), *a measurement* (a probe,
a command or a count), and *the work* (a question that cannot be known at
framing time).

**The framer opens rows and does not own their answers.** The `Status`
column is ticked by whoever answered, never by whoever asked.

Answered rows feed back into `docs/`, or into the skill document they
concern, before this directory's work merges.
