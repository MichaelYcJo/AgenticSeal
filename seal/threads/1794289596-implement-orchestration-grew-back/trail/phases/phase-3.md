# Phase 3: 1794289596-implement-orchestration-grew-back

## What this phase found

**The frame holds for this phase.** The frame names `9e9d1087f`, and phases 1 and 2 moved every line after `:22`, so I found each passage of *Removes* rows 9 to 13 and 16 to 19 by its words at `8e49bb39b`, and rows 20 and 21 in the paragraphs phase 2 wrote. Each passage stood as its row quotes it. Each home a row names holds the fact, except one detail below (read). The homes are:

- step 1 and **The orchestrator writes the answer down before the first edit** (row 9);
- **`Automation` is a record** (row 10);
- the bullet **Assume, in writing** (row 11);
- the sentence on a change belonging to no work item, and "the check happens at the pull request and CI sees only what is in the tree" (row 12);
- **The exit is last** in `skills/implement/routing-question.md`, the sentence on the sealer reading the grounds, and `skills/settle/SKILL.md` step 5, which names *Under agentic* (row 13);
- `skills/legacy-parity/SKILL.md` *Recording the comparison* and `docs/running/the-review-and-parity-arms.md` *Parity arm* (row 18);
- `agents/framer.md` *Job* and the **Planning** bullet of *Under agentic* (row 19);
- `agents/framer.md` *You have two routes back* (row 20).

The detail is in row 16. It names the sentence on the sealer reading a route's grounds as the home of "the sealer withholds where `Implementation` names `crafter` and a closed phase has no record". That sentence names `agents/sealer.md` step 4 for another fact. The withholding itself stands in `agents/sealer.md` step 4, which is its owner, and in `lib/routing.py`'s docstring. No party loses the fact, so I removed the sentence as the row says.

**The body holds 5,225 words at `02740215a` (executed, `wc -w skills/implement/orchestration.md`).** That is 17 under S1's bound of 5,242, so no count goes back to the owner. It held 5,704 at `8e49bb39b`, so 479 words left, against `frame/design.md` D3's estimate of 510. The opening went from 207 words to 165 (executed, `sed -n 3,22p` at `8e49bb39b` and `sed -n 3,19p` at `02740215a`, each piped to `wc -w`), against D3's estimate of 120 entering. The release branch at `df775c52c` holds no change to the file (executed, `git log HEAD..release/v0.37.2` prints nothing), so the count after a merge today is the same. #1476 has not reached the release branch, and `gaps.md` *Not verified* names the count after its merge.

**The opening keeps the lead "This file is the orchestrator's".** `tests/behaviour/test_first_setup_asks_once.py#test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap` finds the paragraph by that lead and reads the bootstrap's path and both places the root can be in it, so the sentence that sends a repository with no root to `skills/implement/bootstrap.md` stays in the first paragraph. The paragraph now lists what the body holds after items 1 to 5. It does not name the two new files: D4's sentence names each at the step that opens it, and naming them again would say twice when each is opened. The second paragraph keeps who opens which half and contract rule 11's sentence. The list of `skills/implement/SKILL.md`'s contents is gone (*Removes* row 14).

**Rows 9, 18 and 20 left as their rows say.** Row 9's paragraph left whole, and its sentence "No check refuses an earlier edit; …" now closes the paragraph that opens with the lead *The orchestrator writes the answer down before the first edit*. Row 18's paragraph is one sentence that keeps its bold lead and cites both homes. Row 20's sentence is D1 row 12 as D1 words it.

**Row 21 shortened the body's statement of the dated-section rule to the clauses the orchestrator acts on.** The sentence now reads "In a section the frame dates to the commit it read, a statement of the tree is not folded, and a sentence that says what the work does or concludes is folded with the fact it states; a section that states the tree with no date gets the date and keeps its text", then cites the owner. The reason, that such a section states the commit, is the owner's.

**The three statements of *Scope* item 9 are worded apart.** `tests/text/test_no_passage_is_pasted_into_a_second_file.py` counts a pair of an agent definition and a skill, and refuses a run of 15 shared words. So the owner, the body, `agents/proofer.md` and `agents/crafter.md` share the clause "a sentence there that says what the work does or concludes" and differ after it. The owner says such a sentence is no claim about the commit, that a fold rewrites it and that a reader holds it against HEAD. The proofer reads it "against the target", the word its rule uses for what it reads. The crafter's rule already says a dated section states the commit "not the present", so its sentence says such a sentence "states the present". The module is green on all four (executed).

**The cases that read a sentence item 9 rewords are one module (executed, a script that flattens every tracked file under `tests/` and `evals/` and looks for eight phrases of the four sentences).** Only `tests/text/test_the_rules_have_one_owner.py` holds one, in the fold case's rows 15 and 22. `tests/text/test_a_moved_rule_leaves_its_definition.py` reads the crafter's paragraph and none of the reworded sentence, and it is green. No case reads the owner's new sentence or the two definitions' new clauses, and *Scope* item 9 adds none. So no `seal mutate` run is owed on those three, and a run would only print `SURVIVED`. S8 is read by the proofer.

**The fold case's new phrases were seen red (executed).** First, the case as phase 2 left it, run against the reworded body before the case changed, exited 1 and named rows 12, 15 (both phrases) and 22, and no other row. Then I committed the case's new phrases and ran one `seal mutate` batch of `skills/implement/orchestration.md` at `02740215a` over `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k test_a_decision_after_the_frame_is_folded_into_it`. It printed `3 mutants, 3 red, 0 SURVIVED`, exit 0. `seal mutate` prints a verdict per mutant and not the failing line.

| D1 row | Replaced | With |
|---|---|---|
| 22 | "concludes is folded with the fact it" | "concludes is not folded with the fact it" |
| 15 | "a statement of the tree is not folded" | "a statement of the tree is folded" |
| 12 | "A statement the framer's hand-back names in" | "A statement the crafter's hand-back names in" |

**Other places that state the rules this phase reworded or removed (a sample).** I searched with `git grep` for each removed passage's lead and a phrase of each removed sentence, and over every tracked `.md` and `.py` file, flattened, for "dated to the commit", "dates to the commit", "claim about that commit", "does or concludes", "the tree as read at", "A wrong answer here" and "free-form". The class is open, so this list is a sample, and the part it did not reach is every statement of these rules in other words.

- `agents/framer.md` *You have two routes back* says a section dated to the commit the framer read keeps its date. That agrees with the owner, and it stands.
- `templates/records/sdd-design.md` and `templates/records/sdd-plan.md` open *Grounding* and *Technical context* with "The tree as read at `<commit>`." That names the date and states no exemption, so each stands.
- `lib/routing.py`'s docstring says a wrong `Planning` or `Implementation` answer is read against a record the run left. It is the code's own account and cites `agents/sealer.md` step 4, not the removed sentence, so it stands.
- `docs/checks/the-routing-check.md:16` cites *Orchestrator: the order inside a ticket* for writing `routing.md` before the first edit. Step 1 there states it, so the citation holds after row 9.
- `agents/framer.md` *Job* states where the framer runs, which row 19 names as the home, and it stands.

**S4 still holds after the opening's rewrite (executed, `grep -n` of both paths in the body).** Each new file's path stands once in the body, in the sentence D4 gives it, at lines 222 and 317.

**The set at the phase boundary** was `bin/test tests/text tests/behaviour tests/lib/test_core.py tests/hooks/test_core_start.py -q` (executed, at `02740215a` with this record, `changelog.md`, `gaps.md` and the Status cell in the working tree). `tests/text` and `tests/behaviour` are the tree-wide files `CONTRIBUTING.md` names. They hold every module of the plan row but `tests/lib/test_core.py`, and the one module that reads a sentence item 9 rewords. `tests/lib/test_core.py` and `tests/hooks/test_core_start.py` are S7's two modules. It exited 0, with 1,877 passed and 8 skipped. Its two warnings name one citation, `docs/running/the-review-and-parity-arms.md:56`, as excused by the operation of `frame/design.md` *Rule changes*, which is S6.
