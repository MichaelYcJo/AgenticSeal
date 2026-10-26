# Phase 3: 1792993972-settle-writes-each-sections-latest-decision

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 98e261ea |

## What this phase was asked

The reframe after round 3's finding 1. Rewrite steps 6 and 8 of
`skills/settle/SKILL.md` *The settling session's procedure* in place to
`spec.md` S13's target text, and leave step 7 as it is. Update
`tests/test_settle_reads_before_it_removes.py::test_the_skill_states_the_settling_sessions_procedure`
as the plan's phase 3 row says: drop the strings that pin the searched set,
its command and step 8's "once", add the five new strings in order, assert
that the procedure holds no `git grep`, and rewrite the docstring. Change the
changelog fragment's clause to match. See the case red against `27177bf2`'s
skill text, then green, and run the plan's *Verified by* command. Phase 3 is
the last phase, so correct `overview.md` where it states the old step 6 or 8.

## What this phase found

**The frame holds** (`read`, then `executed`). The skill text at `4f74c220`
is the text at `27177bf2`, since the reframe touched only this work item's
records (`git diff --quiet 27177bf2 -- skills/settle/SKILL.md`, exit 0). The
plan says no file outside the frame states step 6's set or step 8's "once".
A `git grep` for the set's sentence, its command, "row once." and "every
test module naming", outside the round records and `changelog/`, found only
the skill, the case and the changelog fragment. `overview.md` states neither
step, so it gains one divergence row and no correction.

**The docstring keeps round 1's row half** (the work). The plan says the
docstring's sentences on rounds 1 and 2 give way to one on round 3. Round 1's
sentence held two facts: a row that fits two kinds has one reading, and step
6 names its set. The case still asserts the first, through the string "A row
that fits more than one kind takes the first that fits". So the docstring
keeps that half and drops the half about the set. `overview.md` records the
divergence.

**Steps 6 to 8 are S13's text byte for byte** (`executed`): `diff` of
`spec.md` lines 182 to 198 against `skills/settle/SKILL.md` lines 203 to 219,
exit 0.

**Red, then green** (`executed`). With the rewritten case and `27177bf2`'s
skill text, `bin/test tests/test_settle_reads_before_it_removes.py -q -p
no:xdist -k test_the_skill_states_the_settling_sessions_procedure` exited 1:
1 failed, with all five new strings missing. After the skill edit the same
command exited 0: 1 passed.

**Mutations** (`executed`, `mutation-check` over `skills/settle/SKILL.md`,
the case above as its tests, at `98e261ea`): 6 mutants, 6 red, 0 survived.
The mutants dropped step 6's done condition, put `git grep` back into step
6, changed "step 8 runs every" to "most", put "once" back into step 8,
dropped step 8's done condition, and replaced the `check:` targets with "the
modules that read what you wrote".

**The narrow checks** (`executed`, exit 0). The plan's *Verified by*
command, `bin/test tests/test_settle_reads_before_it_removes.py
tests/test_no_passage_is_pasted_into_a_second_file.py
tests/test_docs_line_wrap.py tests/test_one_heading_rule_holds_to_commonmark.py
-q`, gave 66 passed. The other modules that name the settle skill,
`tests/test_a_document_has_room_for_the_next_fold.py`,
`tests/test_a_phase_hands_the_next_one_a_record.py`,
`tests/test_a_reference_root_is_read_and_never_taken.py`,
`tests/test_rule_changes.py`, `tests/test_rules.py`, `tests/test_settle.py`,
`tests/test_settle_applies_rule_changes_in_place.py`,
`tests/test_the_rules_command_reads_each_rule_off_its_test.py`,
`tests/test_unverified_rows_close.py` and
`tests/test_waiver_decided_at_start.py`, gave 259 passed. `uvx ruff check`
and `uvx ruff format --check` over the changed test file report nothing, and
`bin/test-layout --pairs` over it names no pair.
