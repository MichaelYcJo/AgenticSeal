# 1792368014-the-framer-is-written-anew-from-its-job — review round 2

target: fecbb137, fixes 1bdbb586..fecbb137

This verifying round read the fix range `git diff 1bdbb586..fecbb137`:
5bdad9db changes `agents/framer.md` and two test modules, and fecbb137 writes
round 1's verdict and answer lines, a phase-4 addendum and a changelog note.
Round 1's coordinates were carried, not searched again: the old file's lines
at 2ff7b963, `docs/the-review-record.md:462-536` and
`skills/code-review/orchestration.md:153`. Every verdict below was reached
again on the tree at fecbb137, in a `git clone --no-local` of the branch.

## Findings

### 1. The overview still says a framer spawn carries 26,027 bytes, and it does not record that the fix was left unmeasured

severity: should
location: `seal/specs/1792368014-the-framer-is-written-anew-from-its-job/overview.md:11-14`
evidence: executed `git grep -n -E '26,?027|26,?604' fecbb137 -- seal/specs/1792368014-the-framer-is-written-anew-from-its-job`, `wc -c agents/framer.md skills/agent-contract/SKILL.md`
verdict: fixed c1d02bb3

The overview's opening paragraph says, in the present tense, that *a framer
spawn carries 26,027 bytes at startup instead of 86,353* (`overview.md:11-14`).
At fecbb137 the definition is 10,001 bytes and the contract 16,603, so a
spawn carries 26,604 bytes (executed, `wc -c`). The fix pass's own addendum
says the same: the preload that ships is 26,604 bytes (`phases/phase-4.md:86-89`,
read).

The orchestrator asked that the records say the fix was not measured again.
The changelog says it: *That tree was not measured again* (`changelog.md:38-41`,
read). The phase-4 addendum says it too. The overview says neither the new
figure nor that the shipped definition differs from the measured one. Its
divergence table has a row for each merge and for each removal the frame
did not name, and no row for this one. The phase records' 26,027 figures
are dated to their commits and stay true. The overview's sentence is the
one statement of the current preload, and it is now false.

Why it matters: the overview is the closing memo the sealer reads against
the tree, and the pull request body is written from it. A reader of the
overview learns a size the branch no longer has, and does not learn that
the `pass` measured a definition 577 bytes smaller than the one that ships.
Contract §19 asks that the change correct what stood on the old fact in the
same commit. Neither commit of the fix range touched `overview.md`.

```markdown
## Why this work exists

The framer's definition is written to the shape the smith and the warden
already have and preloads the contract alone, so a framer spawn carries
26,604 bytes at startup instead of 86,353 and opens the two skills by
section at the steps that need them.
```

```markdown
| Round 1's fix, not measured again (5bdad9db) | phase 2's side measured the definition at b434e145, a 26,027-byte preload; round 1's fix adds 577 bytes to `agents/framer.md` | no second side: the preload that ships is 26,604 bytes, and the side stands at b434e145 | the orchestrator's decision, under the owner's word that a side is not run again for the measurement alone (`phases/phase-4.md`, the addendum) |
```

answer: Fixed by the orchestrator in the record it owns, with the round's two paste-ready blocks as written: the overview's opening paragraph now reads 26,604 bytes, and the divergence table gains the row *Round 1's fix, not measured again (5bdad9db)*.

## Confirmations

confirms: round-1#1
Both reading rules are back in step 4. *A rule with a passing test is not a
claim to re-establish* now stands under the `Enforced by:` lines, and *a
decision those rounds argued through is not argued again in your `plan.md`*
under the earlier work items (`agents/framer.md:50-62`, read). The pin
`tests/test_waiver_decided_at_start.py::test_the_framer_inherits_what_the_tree_already_settled`
asserts both phrases. Neither phrase stands in the definition at 1bdbb586,
and each stands once at fecbb137 (executed, a whitespace-folded `grep -c -F`
of each phrase over both revisions). So the claim that the pin was red
before the fix holds as far as reading settles it. The judging rule's
`Enforced by:` names the pin, and `bin/rules --check` resolves it (executed,
exit 0, 550 targets).

confirms: round-1#2
The reframe rule now says to open §*The run*, then rewrite `plan.md` with
new phase rows for the redesign, every closed phase keeping its commit, and
`spec.md` where the scope moves (`agents/framer.md:160-168`, read). It still
ends with the phrase `RUN_OWNS_THE_RULE` pins, and
`tests/test_the_rules_have_one_owner.py` passes (executed). The pin
`test_a_reframe_keeps_every_closed_phase` asserts both clauses, and neither
stood in the definition at 1bdbb586 (executed, the same `grep -c -F`). The
answer says `skills/code-review/orchestration.md:153` keeps its statement of
the rule, *new phase rows; a closed phase keeps its commit*. The two say
the same thing in different words (read).

confirms: round-1#3
Step 8 now labels claims by contract §4. A fact a command gave is
`executed`, what was opened is `read`, and the step says the framer ran no
check of the repository's (`agents/framer.md:73-76`, read). The pin
`tests/test_a_question_says_who_can_answer_it.py::test_the_hand_back_labels_what_the_framer_ran_as_executed`
reads the hand-back step and the person-row rule through `report_of`.
*executed nothing* stood in the definition at 1bdbb586 and is gone at
fecbb137, and *is `executed`* is new (executed, the same `grep -c -F`). So
its first assert was red before the fix. No other definition says every
claim is `read` (round 1's search, carried, and this round's grep over
`agents/`, executed).

confirms: none
The fix grows no shared passage past its allowance. The framer's four
`BASELINE` entries still hold, and the modules that read the definition
pass: `test_no_passage_is_pasted_into_a_second_file`,
`test_a_moved_rule_leaves_its_definition`, `test_every_agent_reads_the_contract`,
`test_docs_line_wrap`, `test_a_reference_root_is_read_and_never_taken` and
the rest of the 12 run below (executed). Within the framer's read set, the
fix range changes `agents/framer.md` alone (executed, `git diff --stat`).

confirms: none
The changelog and the phase-4 addendum say what the orchestrator decided,
and say it in those terms. The measured side is b434e145 with a 26,027-byte
preload. The fix adds 577 bytes, so the shipped preload is 26,604 bytes, and
that tree was not measured again (`changelog.md:38-41`,
`phases/phase-4.md:74-92`, read). The 10,001 and 16,603 byte counts match
`wc -c` at fecbb137 (executed). Finding 1 is the record that does not say it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `mutation-check` runs the answers cite, one per pin. This round showed each pin's phrase absent before the fix by reading, and did not repeat the mutations | `phases/phase-4.md`, the addendum | the smith's claim; the sealer samples it if it chooses |
| The full suite, the repository-wide lint and the typecheck at fecbb137. The suite stays `unverified` here, as contract §2 says | the branch at fecbb137 | the orchestrator's broad gate, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `test_waiver_decided_at_start`, `test_a_question_says_who_can_answer_it`, `test_every_agent_reads_the_contract`, `test_no_passage_is_pasted_into_a_second_file`, `test_a_moved_rule_leaves_its_definition`, `test_the_rules_have_one_owner`, `test_the_handoff_before_round_one`, `test_a_reference_root_is_read_and_never_taken`, `test_docs_line_wrap`, `test_a_language_section_of_writing_style_opens_alone`, `test_chain_hooks_hardening`, `test_the_record_is_written_in_words` | exit 0, 441 passed |
| `bin/rules --check` | exit 0, all 550 targets in 60 rule files resolve |
| a whitespace-folded `grep -c -F` of each pinned phrase over `agents/framer.md` at 1bdbb586 and at fecbb137 | the four restored phrases and *is `executed`* count 0 then 1; *executed nothing* counts 1 then 0 |
| `wc -c agents/framer.md skills/agent-contract/SKILL.md` at fecbb137 | 10,001 and 16,603 bytes, 26,604 in all |
