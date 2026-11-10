# Phase 2: 1794289596-implement-orchestration-grew-back

## What this phase found

**The frame holds for this phase.** `frame/design.md` *Scope* item 4 names six paragraphs and their order, and D1's Home column gives each of the 24 rows one of them. Each row's clause stood in the fold paragraph of `skills/implement/orchestration.md` at `07a3544aa` (rows 1 to 21), in `frame/design.md` G8 (rows 22 and 23), or in `skills/implement/merge-order.md` at `07a3544aa` (row 24), as D1 says (read). The two citations of the first paragraph's lead, the prevention-home paragraph of the order section and `tests/text/test_the_rules_have_one_owner.py#test_a_recurring_problem_gets_a_prevention_home`, still resolve, because the lead is kept as written.

**The body holds 5,704 words after this phase (executed, `wc -w skills/implement/orchestration.md` at `500d2cb98`).** That is 107 words above phase 1's 5,597. The six paragraphs, lines 55 to 139, hold 979 words (executed, `sed -n 55,139p | wc -w`), against 872 for the one paragraph they replace and against `frame/design.md` D3's estimate of 875. Five bold leads are new, and rows 22 to 24 add about 95 words. D3's rows for *Scope* items 5 and 6 take about 433 words out, so the body after phase 3 would hold about 5,271, about 29 above S1's bound of 5,242. This is a departure from D3's estimate and not from a rule. I cut nothing *Scope* item 4 does not name: the spawn leaves the bound to phase 3's measurement (`frame/questions.md` Q2), and `frame/plan.md` *Phases* hands a count above the bound back as a decision.

**How the six paragraphs differ from the paragraph they replace.** Each clause keeps its words wherever its sentence still reads in its new home. Where a sentence leaned on a neighbour that D1 homes in another paragraph, it now names what it leaned on.

- Row 14, "Such a statement records what the build changed", leaned on row 13's sentence before it. D1 homes row 14 in the paragraph on who writes, which comes before the paragraph on reach, so the sentence now names the statement: "A statement a crafter's hand-back names in a frame file or `routing.md` records what the build changed".
- Row 17, "Where that reading, or the framer's hand-back, finds a statement", leaned on row 16's reading. Row 16 now stands one paragraph later, so the sentence reads "A statement found in a file the crafter writes", D1 row 17's own wording.
- Row 13 opens with its reason, "The statements a crafter's hand-back names are its reading of a file it does not write", because the sentence it followed now stands in another paragraph.
- Row 6 keeps "as a fix pass resumes the implementer" and drops its parenthetical citation of `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*. Row 17's sentence, one paragraph earlier, cites the same section, and one fact keeps one citation (`skills/core/SKILL.md` *The rule a mechanism is kept against*).
- Row 4's reason is the second paragraph's lead, and the sentence after it names the two documents.
- Row 15 and row 22 share one sentence, split at a semicolon: the dated section's statements of the tree are not folded, and a sentence there that says what the work does or concludes is folded.
- Row 23 names the six sections G8 found stale sentences in, as *Scope* item 4 asks.
- Row 20's two sentences are one.

**One sentence outside *Scope* item 4 changed.** The first paragraph of `skills/implement/merge-order.md` said that the routing section "holds the rest", the version move among it. Once row 24 left that file for the order section, that sentence sent a reader to the routing section alone for the move. It now ends with one sentence naming `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* as the place that says where the framer writes the move. The condition D4 gives for opening the file is unchanged. `merge-order.md` now reads "merge as each is sealed. A move made after a work item's last round", as *Scope* item 4 asks, and I left that line short rather than re-wrap the moved paragraph, so that S5's moved-lines diff stays readable.

**The rewritten fold case, run once against the order section as phase 1 left it (executed, at `a5bccf782` with only the test file changed): exit 1, 16 phrases missed, all in one failure.** The case now collects every phrase it misses and names each by its D1 row. It missed rows 4, 6, 8, 9, 13, 14, 15 (both phrases), 16, 17, 18, 19, 20, 22, 23 and 24. It found rows 1, 2, 3, 5, 7, 10, 11, 12 and 21. Those nine phrases are sentences the rewrite keeps word for word, and the case before this phase already pinned each of them. So the run shows red for every row whose wording is new, and the three new rows among them. After the rewrite the module is green.

**The phrases of rows 4, 9 and 19 hold the `**` that closes a lead.** Each pins the lead and the sentence after it together, so a lead re-cut at another sentence boundary turns the case red.

**Each new clause was mutated once and the case went red (executed, `seal mutate` at `500d2cb98`, one command each, `bin/test tests/text/test_the_rules_have_one_owner.py -q -k test_a_decision_after_the_frame_is_folded_into_it -p no:xdist`).** Each run printed `red`, exit 0, and its failure named only the row it broke.

| D1 row | Replaced | With |
|---|---|---|
| 22 | "the work does or concludes is no claim about that commit, and is folded" | "… is a claim about that commit, and is not folded" |
| 23 | "seen, not the whole list." | "seen, the whole list." |
| 24 | "section before the orchestrator spawns the last phase" | "section after the orchestrator spawns the last phase" |

The other 21 rows reword or move clauses, and the run against the old text above is what shows them red. They add no behaviour, so they owe no run (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*).

**Other places that state the rules this phase reworded (a sample).** I searched with `git grep` for "dates to the commit", "dated to the commit", "not the whole list", "fold commit", "folds it in a commit of its own" and "Operational impact", and for every citation of *Orchestrator: the order inside a ticket*. The class is open, so this list is a sample, and the part it did not reach is every statement of the fold that uses other words.

- `agents/crafter.md:186` and `agents/proofer.md:124` say a frame section dated to the commit the framer read states that commit. Neither carries row 22's exception for a sentence that says what the work does or concludes. A proofer reading its rule would not flag the stale *Grounding* conclusion G8 records. Agent definitions are outside *Scope*, so I left both, and `gaps.md` *Not done* names them.
- `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* calls each "present-tense statement of the tree" in the dated sections a claim about the commit. A conclusion about the work is not a statement of the tree, so the sentence agrees with row 22.
- `agents/framer.md` *You have two routes back*, `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, `skills/implement/SKILL.md` *3. The SDD file set* and `agents/crafter.md:27` each state a clause the rewrite kept, and each still holds.

**For phase 3.** The order section now runs from line 24 to the heading at line 156. *Scope* item 5's passages, and the three-row table **Three combinations do not stand**, are found by their words, since every line number the frame gives is of `9e9d1087f`. The count above is the one phase 3 starts from.

**The set at the phase boundary** was `bin/test tests/text tests/behaviour tests/skills/test_settle.py tests/lib/test_core.py -q` (executed, at `500d2cb98` with this record, `gaps.md` and the Status cell staged). `tests/text` and `tests/behaviour` are the tree-wide files `CONTRIBUTING.md` names, and they hold every case of the plan row but one and the test file this phase changed. `tests/skills/test_settle.py` is that remaining case of the plan row, and `tests/lib/test_core.py` is the one file outside them that opens `skills/implement/orchestration.md`. It exited 0, with 2,030 passed and 8 skipped.
