# Phase 2: 1793174169-a-round-with-fixes-costs-three-record-commits

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 44f37009 |

## What this phase was asked

Rework phase 1's build to the owner's answer of 2026-10-28 (`guarantee.md:40`), against the frame at `33c43d2e`. The fix pass writes the `verdict:` and `answer:` lines last and commits neither. The orchestrator commits the round record as the pass left it, in one commit for the whole pass, before it spawns the verifying round, and changes none of its lines. Rewrite in place `skills/code-review/orchestration.md:78-80`, `agents/crafter.md:156-158` and the last sentence of the `Grounds` cell at `skills/implement/orchestration.md:666`. Add a `RULES` entry for the orchestrator's new bold sentence. Replace the clauses at `tests/text/test_the_rules_have_one_owner.py:192-193` and `tests/text/test_a_moved_rule_leaves_its_definition.py:512-514`. Rewrite the first bullet of `changelog.md`. Add the rework's divergence row to `gaps.md`. See each new clause and entry red against the text at `aa8b54cb` before the text lands, and measure S7 with `longest_run`.

Do not edit `guarantee.md`, any round record, or anything under `frame/` but the phase 2 Status cell. Run every module that reads a changed file, `bin/seal layout --check` and `bin/seal rules --check`. The broad gate is the orchestrator's.

## What this phase found

**The frame held at every coordinate the phase 2 row names.** `git diff aa8b54cb HEAD` before the build touched only the three frame files, so the text files were the text at `aa8b54cb`. The lines quoted at `skills/code-review/orchestration.md:78-80`, `agents/crafter.md:156-158`, `skills/implement/orchestration.md:666` and the two test coordinates were there as the frame quotes them. `git grep` found no other statement of the fix pass committing its own lines outside `seal/`.

**Each new case was seen red against the text at `aa8b54cb`, on its first new clause.** With the new cases written and no text changed, `bin/test tests/text/test_the_rules_have_one_owner.py -p no:xdist -q -k "20 or fix_pass_reads"` exited 1 with 2 failed: rule 20's sentence, and the fix-pass section's clause "Last, the fix pass writes the `verdict:` and `answer:` lines of every finding it answered, after its fix commits and those corrections". `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -p no:xdist -q -k crafters_fix_pass` exited 1 with 1 failed, on the crafter's new sentence.

**The clauses after the first in each loop were seen red by `seal mutate` after the commit.** An assertion loop stops at its first failure, so the base run showed one clause per case. Over `skills/code-review/orchestration.md`, six mutants were all red under the first command above. They covered the fix pass's write clause, "and leaves the round record uncommitted", "That commit holds `trail/rounds/round-N.md` alone.", the bold sentence removed, "changes none of its lines" weakened, and the old sentence "the fix pass commits the two lines" put back beside the new text, which only the `not in` assertion reads. Over `agents/crafter.md`, three mutants were all red under the second command: the sentence removed, "do not commit them" turned to "commit them", and the old "Then commit the `verdict:` and `answer:` lines" put back. Removing the rewritten `Grounds` sentence SURVIVED under `tests/behaviour/test_every_orchestrator_act_names_its_delivery.py`, as phase 1's did. That module reads only that the cell exists, and `gaps.md` *Not verified* names the proofer as the sentence's reader.

**S7 holds: the `to:` text shares no 15-word run with either rewritten file.** `longest_run` from `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, over `rule_changes.parse(frame/design.md, "docs").ops[0].new` (1 op, 0 errors), found 0 against `skills/code-review/orchestration.md` and against `agents/crafter.md` at `44f37009`. It also found 0 against `docs/the-review-record.md` and `skills/implement/orchestration.md`, and 0 between the two rewritten files.

**The new bold sentence ends the paragraph with one more short sentence, that the commit holds the round record alone.** `frame/design.md` *Scope* item 1 states it. It is pinned in `test_the_fix_pass_reads_the_implementers_context_before_it_resumes`, so the commit cannot quietly widen to carry a fix.

**`gaps.md` held two sentences the rework made false or misnumbered, and the phase corrected them.** *Why this work exists* said the fix pass commits both lines, and now says the orchestrator commits them. Two rows cited `frame/design.md` *Scope* item 4 for the cause, which the reframe moved to item 5. The *Not verified* row now cites item 5. The divergence row on the line numbers now says the first frame's item 4 made that citation.
