# Phase 1: 1793174169-a-round-with-fixes-costs-three-record-commits

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 749cb56c |

## What this phase was asked

Build the plan's one phase. Rewrite in place the paragraph of `skills/code-review/orchestration.md` at `:54-58`. Add `answer:` and one commit to the *The record* cell of the table at `:155`. Add the one-commit sentence to `agents/crafter.md:148-157`. Add one sentence to the Grounds cell at `skills/implement/orchestration.md:666`. Write the changelog fragment. Write the S1 to S3 clauses in `tests/text/test_the_rules_have_one_owner.py` and `tests/text/test_a_moved_rule_leaves_its_definition.py`, and see each red at `5287dd42` first.

Do not edit `docs/`; the frame's `## Rule changes` item belongs to the settle. Do not edit `chain_check.py`. Build on `frame/questions.md` Q1's default (a), no check; the owner has not answered and is not asked. Record in `gaps.md` that `routing.md`'s *Why this way* says the chain check's acceptance changes and the frame decided it does not, citing `frame/questions.md` head item 1. Do not edit the files of #1055, #1056 or #956.

Run the two modules and ruff on the changed Python files, every module that reads a changed file, `bin/seal layout --check` and `bin/seal rules --check`. The broad gate is the orchestrator's.

## What this phase found

**Each new case was seen red against the text at `5287dd42`.** The commits after `5287dd42` touch only this work item's records, so the working tree with the new cases and no new text was the base text. `bin/test tests/text/test_the_rules_have_one_owner.py -p no:xdist -q -k "19 or fix_pass_reads or framers_route"` exited 1 with 3 failed: rule 19's sentence, the fix-pass section's first new clause, and row *The record*'s `answer:` clause. `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -p no:xdist -q -k crafters_fix_pass` exited 1 with 1 failed, on the crafter's one-commit sentence.

**After the commit, `seal mutate` broke each unit the phase added.** Five mutants of `skills/code-review/orchestration.md` were all red under `tests/text/test_the_rules_have_one_owner.py`: the bold sentence, the one-commit sentence, the doubted close's destination, the clause that the orchestrator does not rewrite the line, and row *The record*'s new words. Removing the crafter's sentence was red under its case. Removing the sentence added to the `Grounds` cell in `skills/implement/orchestration.md` SURVIVED under `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, which reads only that the cell exists. `gaps.md` *Not verified* names the proofer as its reader.

**The frame's transcript line numbers count from zero.** `grep -n` finds each spawn-prompt sentence `frame/design.md` *Scope* item 4 cites one line below the number it gives: 7832, 8016 and 8972. The changelog fragment cites those, and `gaps.md` holds the divergence.

**Row *The record* names its writer as `you`.** The table's other rows address the orchestrator as `you`, and `skills/code-review/orchestration.md` is the orchestrator's half of the review skill, so the cell does the same. The rewritten paragraph names `the orchestrator` instead, because it sets the orchestrator's act beside the crafter's.

**The cap's `deferred <home>` takes no sentence in `skills/code-review/orchestration.md`.** `frame/design.md` *Scope* item 2 leaves that case to the policy sentence in `## Rule changes`, and the phase followed it.
