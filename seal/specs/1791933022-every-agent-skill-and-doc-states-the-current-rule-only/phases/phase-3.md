# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 1912e63d, the last build commit; this record's commit follows it |

## What this phase was asked

`plan.md`'s row 3: the record is the warden's file and the check reads five
facts. Built in two spawns. The first rebuilt `chain_check.py`, wrote the new
round template, moved the broad run to `broad-gate.md`, removed
`round_record.py`, `bin/round-record{,.cmd}`, `hooks/review-history-guard.py`
and the `tests-todo.md` reader with the modules whose subject they were, and
wrote `docs/the-review-record.md`.

The second was asked to finish it: delete `docs/round-record-spec.md`,
`docs/review-chain-spec.md` and `docs/review-handoff-protocol.md` and re-point
every reference; repair the doc-pin modules, keeping what still guards
something; rewrite `docs/the-record-layout.md` §*seal/specs/<work-item-id>/*,
the cell paragraphs of `docs/the-broad-gate.md` and `docs/the-agent-set.md`
§*What each party writes*; move the warden's eval graders to
`rounds/round-N.md`, drop the two field graders, make rule 3 of
`noninferiority.py#verdict` read shape on the new side, and leave the sealer's
cases failing loudly where they still assume the old record; sweep S10; drop
the hygiene pull-heads fetch if the check no longer reads it; rewrite S9 in
place to `questions.md` Q1. In `agents/*.md`, the contract, the two skills and
the two orchestration files: delete what describes a removed mechanism, and
where a step still needs the record, one sentence pointing at
`docs/the-review-record.md` — no rewrite, which is part B's.

## What this phase found

**What left, against `spec.md` §*Removes*.** 28 test modules, 25,235 lines,
890 cases and 3,063 recorded seconds (`.test_durations`, read; the file was
not refreshed by this phase). Each module's guard, and where it stands now:

| Module | Lines · cases · s | What it guarded | Now |
|---|---|---|---|
| `test_a_finding_id_is_a_bare_integer.py` | 1,156 · 39 · 174.8 | the generator refusing a non-integer id | `test_chain_check.py::TestOpenFindings` reads the id; the template shows it |
| `test_a_fix_of_a_fix_is_counted.py` | 714 · 22 · 365.5 | the `Fix of a fix` count and its `second` stop | the warden's mark; nothing mechanical (S9) |
| `test_a_fix_pass_may_add_a_unit.py` | 242 · 9 · 0.1 | the depth-1 unit rule | left with `New units` |
| `test_a_fragment_left_behind_is_named.py` | 800 · 26 · 194.7 | `fragment_left_behind`'s notice | the rule stays in `docs/the-record-layout.md`, enforced by nothing; the warden and the sealer read it |
| `test_a_new_returnable_value_is_a_contract_change.py` | 368 · 8 · 16.1 | `Contract changes` | left with the field |
| `test_a_note_closes_once_at_the_runs_end.py` | 889 · 25 · 134.7 | ⬜ notes and `notes --at` | left with the severity |
| `test_a_range_owns_what_git_lists_for_it.py` | 238 · 7 · 16.2 | `own_commits` | left with the fix range |
| `test_a_record_precedes_the_fixes_it_commissions.py` | 1,568 · 53 · 193.6 | the record committed before its fixes | left with `Written late` |
| `test_a_record_says_what_ran_it.py` | 776 · 25 · 65.6 | `Ran by` | left, in the round and the phase template |
| `test_a_record_says_why_it_was_written_late.py` | 341 · 8 · 18.9 | `Written late`'s reason | left with the field |
| `test_a_runner_reached_unit_reads_pytest_only.py` | 497 · 16 · 8.8 | the fix surface's call-site reach | left with `Contract changes` |
| `test_a_segments_record_says_what_it_was_asked.py` | 319 · 11 · 0.1 | the round record's *What this round was asked* | the phase record's section stays, pinned by `test_a_phase_hands_the_next_one_a_record.py` |
| `test_a_signers_ci_prints_its_pact.py` | 289 · 8 · 64.8 | `pact_notices` at a signer's pull request | `docs/the-pact.md` says nothing reads the pact at a pull request |
| `test_chain_check_at_the_pull_request.py` | 3,830 · 148 · 422.6 | every arm of the old check | `test_chain_check.py`, one group per function; its two retirement cases rebuilt there as `TestRetired` |
| `test_handoff_outlives_the_merge.py` | 604 · 34 · 4.7 | the handoff protocol's record location | the location is the template's comment and `docs/the-review-record.md` |
| `test_new_says_when_head_is_not_the_target.py` | 357 · 8 · 19.8 | `round_record.py new`'s HEAD notice | left with the generator |
| `test_the_broad_gate_cell_keeps_every_run.py` | 103 · 3 · 0.1 | the cell's newest-first runs | `test_broad_gate.py::TestKeptRuns` |
| `test_the_chain_goes_back_to_its_framer.py` | 462 · 24 · 134.0 | the count's reframe gate | `test_chain_check.py::TestFrame` reads the `Reframed` line |
| `test_the_fixes_close_the_record.py` | 2,981 · 96 · 560.3 | `close` and the fix table | the fix pass fills two cells; nothing applies them |
| `test_the_fixes_name_their_surface.py` | 1,055 · 31 · 50.8 | `New units` and `Contract changes` | left with the fields |
| `test_the_last_rounds_fixes_are_checked.py` | 1,332 · 55 · 147.1 | `Fixes checked by` | `test_chain_check.py::TestFollows`, the last record at HEAD |
| `test_the_range_rule_states_no_shape.py` | 129 · 3 · 0.1 | the range rule's carriers | left with the rule |
| `test_the_record_is_generated.py` | 3,132 · 118 · 219.8 | `round_record.py new` | the warden writes the record |
| `test_the_record_is_held_to_the_floor_and_the_depth.py` | 1,514 · 65 · 198.5 | the floor, the depth, the cap arms | the cap is the orchestrator's rule; nothing mechanical |
| `test_the_reopening_is_one.py` | 663 · 20 · 40.9 | the one reopening | left with the floor |
| `test_the_report_standard_is_one_in_three_places.py` | 159 · 7 · 0.1 | the report shapes copied into four carriers | the shapes are the template's alone |
| `test_the_reviewers_report_reaches_the_record.py` | 401 · 10 · 10.5 | the report file the generator copied | the report is the record |
| `test_the_run_stops_at_the_last_finding.py` | 316 · 11 · 0.3 | the floor's quiet round | left with the floor |

**Two modules the frame named whole held more than the guard.**
`test_chain_hooks.py` and `test_chain_hooks_hardening.py` carried 77 cases on
the commit gate, the session lease, `hooks.json`, the parity arm and the
READMEs beside 21 on the review-history guard. They came back at ed63c3af
with the guard's cases and two pins on the deleted spec taken out; the
deletion had left `docs/the-review-and-parity-arms.md`'s `Enforced by:` and
the gate's parity cases pointing at nothing.

**Cases removed from modules that stay**, each for a removed mechanism:
`test_the_rules_have_one_owner.py` 24 of its 29 functions and 9 of its 18
rules, the other nine rules re-pointed at `docs/the-review-record.md`;
`test_broad_gate_rule.py` 5 (the carriers' `Pass` link, the reviewer carrying
the gate state, the preflight's `seal --check` three times);
`test_a_phase_hands_the_next_one_a_record.py` 3 (`Ran by`);
`test_one_word_one_meaning.py`'s case on the cycle's definition, which only
the deleted spec stated, narrowed to its absence half;
`test_the_suite_has_a_command_that_is_cheap_twice.py` 1 (the
protocol's measurement); `test_the_handoff_names_the_form_it_ran.py` 1 (the
protocol's requirement count); `test_the_set_a_work_item_always_has.py` 2
(the `tests-todo.md` layout); `test_settle_reads_before_it_removes.py` 1;
`test_console_is_not_utf8.py` 1 parametrised case (the post-bash reminder
with an em dash: no plain-text post-bash gate prints non-ASCII now, and the
dispatcher's `reconfigure` is unchanged); `test_the_stamp_reaches_the_person_it_is_drawn_for.py`
the `close --broad-gate` phrase.

**S12 reads 1,482 s**, under 1,500, summed from `.test_durations` over the 40
modules naming `chain_check` or `broad_gate` (`read`). Three of them,
`test_chain_check.py` and `test_broad_gate.py` among them, have no entry yet,
and the rest are measurements from before this phase. The executed figure is
the sealer's broad run.

**The hygiene pull-heads fetch stays, though the check no longer needs it.**
`chain_check.py#follows` requires a record's `Target SHA` to be HEAD's
ancestor, so a commit only a `refs/pull/<N>/head` carries is refused either
way. Removing the step reaches `broad_gate.py`'s step list,
`tests/test_the_gate_names_every_step_ci_runs.py`,
`tests/test_first_setup_asks_once.py`, `docs/release-checklist.md` §2 and
`docs/branch-and-release.md`; it is left for the next spawn, and the two
workflow comments that described the old refusals now describe the new ones.

**A deleted declaration paired with an added one reads as a rename.**
`chain_check.py#changed` diffs with `-M`, and two `routing.md` files from one
template are similar enough to pair, so a branch that adds its own declaration
and removes another's sees neither the deletion nor its retirement. The two
`TestRetired` cases pad the removed declaration to stay under git's
similarity threshold. Whether the old check paired them the same way is
unverified.

**What S10's grep still finds, and why it stays.** History in test docstrings
and comments (`tests-todo row 5`, `round_record.py#…`), the class the overview
already leaves for ⬜ citations; the replay cases' prompts, which quote the
asked paragraph of a past round verbatim; `truth-2` of `replay-1791384160-r2`,
which cites `docs/round-record-spec.md:693` at the commit that case clones;
and stale `.test_durations` entries for deleted modules. `evals/scripts/replay_targets.py`
reads the asked paragraph from `## What this round was asked`, which records
written from now on do not carry, so a replay of a new round needs that
paragraph from somewhere else (part B).

**The sealer's three cases are phase 4's.** Their fixture record is the new
template and their file grader reads `broad-gate.md`; `rule-sealer-record-open`
expects `refused`, which `broad-gate` no longer says over an open record, and
its grader says it fails by design. How the runner treats `not_contains` on a
file that was never written is unverified.
