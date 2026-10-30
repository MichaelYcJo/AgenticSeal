# Phase 3: 1793343707-each-document-serves-one-reader

## What this phase found

**The frame was wrong about one coordinate: `agents/proofer.md:67` is not
the one shipped file that names `CONTRIBUTING.md`.** Row 3's *Verified by*
asks `git grep -l 'CONTRIBUTING' agents skills templates hooks` to print
nothing. The design's Grounding row says the proofer is the one instance
(executed). After this phase the grep prints six files (executed, exit 0):

- `hooks/lib/config.py:410`, a docstring citing *What a change to a gate
  must carry*;
- `hooks/lib/launch.py:55`, the refusal printed when the interpreter is
  too old. It tells the reader to "see CONTRIBUTING.md section 'Running the
  checks'", and in a user's repository that file is not this one;
- `hooks/mode-gate.py:49`, a docstring's bold lead;
- `hooks/version-check.py:24`, a docstring naming the allowed network
  exception;
- `skills/verify/scripts/session_cost.py:3103`, a docstring quoting
  *House rules*;
- `skills/verify/scripts/test_layout.py:15` and `:58`, a docstring citing
  *The test layout*.

The proofer's citation is gone. The six were not touched, because the
spawn named `agents/proofer.md` alone as the scope of this item. The
launch refusal is text a person reads, so changing it also needs a pin
(contract rule 14). `gaps.md` *Not done* holds the six for the
orchestrator.

**The check changed in one place, not two.** The design's *`chain_check.py`*
section says `channel` and the `follows` reading treat a records-only `fixed`
as closed. `follows` already lets a commit pass when it touches only
`seal/threads/<id>/`, so a records-only fix after the last `target:` never
failed it. The refusal came only from `channel`'s last-record loop. That
loop now refuses a `rejected` finding. It also refuses a `fixed` finding
unless a new `read_at_head` predicate passes it. `records` passes the
predicate `records_only(root, item, commit)`, a new function: true where the
commit changed at least one path and every changed path lies under the work
item's directory. `read_at_head` defaults to refusing, so the `Test_channel`
cases stand unchanged.

**One assumption was made under `automation`.** A `fixed` commit that
changed nothing, or one git cannot list, is not records-only, so it still
owes the round. `verdict_problems` already refuses the first, since such a
commit touches no `location:` path.

**The frame missed seven carriers of the old rule, and each was corrected
in place.** They were found with `git grep` on "last record", "`fixed` or
`rejected`" and "verifying round" outside `seal/threads/`:

- `chain_check.py`'s module docstring, its `records` arm row;
- `skills/code-review/orchestration.md`, the run-ends sentence ("holds no
  `open`, `fixed` or `rejected` finding"), and the sentence after it, which
  now owes a verifying round only for a later fix to a file outside the
  records;
- `skills/implement/orchestration.md:472`, the acts row of *the run ends
  with a verifying round*. Phase 4 moves that table to `acts.md` as it
  stands;
- `skills/implement/SKILL.md:511`, the drain table's *Doable within this
  pull request* row;
- `README.md:207-213` and `README.ko.md:201-206`, the paragraph on what
  fails a ready pull request.

**One removal `## Removes` did not name.** `tests/text/test_the_rules_claude_md_names_have_one_home.py`
held `agents/proofer.md` in `LINKED`, so it required the definition to
name `CONTRIBUTING.md` *House rules*. The first boundary run found it. The
entry is gone. The proofer stays in `CARRIERS`, so it still may not restate
the home's sentences. `test_a_removed_link_is_named` now edits
`.github/scripts/plugin_directory_check.py`'s link instead of the
proofer's.

**Some sentences still state the old fact, each on purpose.**

- `docs/the-review-record.md` *What the check reads at the pull request*
  and *The run* still say a `fixed` in the last record owes a round. A pull
  request does not edit the policy root. The design's `## Rule changes`
  holds both new sentences, and the settle writes them.
- `skills/code-review/orchestration.md:60-62` sends a close the
  orchestrator doubts to the verifying round's spawn prompt. `:81-83` says
  the round record is committed before the verifying round is spawned. Both
  describe a round that is spawned, and the orchestrator may still spawn
  one after a records-only fix. Neither says one is owed.
- `agents/proofer.md:114` and `skills/code-review/SKILL.md:106` say how a
  verifying round answers the findings before it. That is still true.

**The sealer's step 4 does not read the commit.** Step 3's case
(`test_step_3_holds_two_acts_and_reads_no_location`) says reading a
`fixed` commit is the check's job. The new step-4 sentence therefore says
the check passes such a finding only where the commit touched nothing
outside `seal/threads/<item>/`. The sealer reads the record at HEAD against
what the finding asked, as the fix pass's claim.

**Five cases were added or rewritten, and each was seen red first.**

- `tests/skills/test_chain_check.py`:
  `test_passes_a_last_records_fixed_finding_that_touched_only_its_records`
  and `test_refuses_a_last_records_fixed_finding_that_also_touched_code`.
  Against the check at `abd6457b` they gave exit 1, `1 failed, 1 passed`.
  The first failed on the records-only `fixed`, which the old check refused
  as owing a verifying round. The second passed, because the old check
  also refuses a mixed fix, as row 3 says (executed).
- `tests/text/test_the_rules_have_one_owner.py`: the run-ends assertion of
  `test_a_close_that_does_not_hold_reopens_it`, rewritten, and the new
  `test_a_fix_pass_to_the_records_alone_owes_no_verifying_round`.
- `tests/behaviour/test_the_sealer_guarantees.py`: the new
  `test_step_4_reads_a_records_only_fix_as_the_fix_passs_claim`.

The last three were run with `skills/code-review/orchestration.md` and
`agents/sealer.md` restored to `abd6457b` through `git stash`, and failed
(executed, exit 1 each time). Then they passed. `seal layout --pairs` over
the three modules found 0 pairs (executed).

**All six mutants went red** (executed, `seal mutate` at `15d85861`). Each
run exited 0 and printed "red: the cases failed against the mutation
(exit 1)", and the tree was clean after the last one. The six:

- `records_only`'s `all(` as `any(`;
- the last-record loop without `not read_at_head(f)`;
- the orchestration's "the pass owes no verifying round";
- its *When* row without "to a file outside the work item's records";
- its run-ends sentence reading "any path in the" for "a path outside the";
- the sealer's "the fix pass's claim with you as its reader".

The proofer's citation is a removal and adds no behaviour. The grep above
covers it. The READMEs, the acts row and the drain row have no case behind
them, and `gaps.md` *Not verified* names their reader.

**The phase-boundary set is 110 modules, run as one command.** It holds
the five modules row 3 names, every module that names a changed path, and
every module that globs `agents/` or `skills/` or reads the tracked tree.
The first run gave exit 1, `1 failed, 5008 passed`: the census above. At
`90d4f3c1` it gave exit 0, `5009 passed, 11 skipped` (executed). The five
named modules, run alone, gave exit 0, `331 passed` (executed). `ruff
check` and `ruff format --check` passed over the five changed Python files
(executed).
