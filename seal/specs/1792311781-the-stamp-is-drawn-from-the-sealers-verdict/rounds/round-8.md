# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 8

target: a38e0b86, fixes 86243d2f..a38e0b86

## Findings

This verifying round raises no finding. Round 7's two closes hold: the
limit now names the clone it holds in wherever the tree states it outside
the frame, and the memo quotes the frame's amend-only limit beside the class
`questions.md` Q9 (a) chose. The diff's other units, the round-3 row's
"Spec says" cell and the new pin, hold as well.

## Confirmations

confirms: round-7#1
§*The stamp* now states the limit for a `sealed` "in a clone that holds no
values file for the work item" and adds that the clone that drew the stamp
keeps its values file, so an amend there draws nothing
(`docs/the-review-record.md:289-294`). The fragment says "another clone, one
that never wrote this work item's stamp values itself" and carries the same
added sentence (`seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/changelog.md:16-23`);
`overview.md`'s round-3 row (line 26) and its Not done bullet (lines 55-62)
take the qualifier. 9a1330e8 changes the docs, fragment, memo and test
paths the finding's `location:` names.

The sentence now agrees with the code (read). `_queue_one` asks
`already_queued` before it queues
(`skills/verify/scripts/seal_stamp.py:1110-1111`), and `already_queued`
matches a values file for the work item's id under any session's directory,
pending or drawn (`seal_stamp.py:990-1015`). Nothing in `seal_stamp.py` or
`hooks/sealer-stamp.py` removes a values file: the only file operations are
the two `os.replace` calls that write and rename one (`seal_stamp.py:810`,
`seal_stamp.py:878`), so "keeps its values file" is true of the code as it
stands. `test_a_recommit_of_the_same_guarantee_queues_no_second_file`
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:667-688`) is an
amend in the clone that queued, queuing nothing.

The class is enumerated (read). `git grep -n -i` of `draws again`, `draws
the stamp again`, `stamp again`, `second stamp`, `queues again`, `had not
fetched` and `rewritten there` outside the round records and `CHANGELOG.md`
finds the limit stated in §*The stamp*, the fragment, the two memo places
and `seal_stamp.py`'s once comment (lines 925-931, which already named the
clone), each now with the qualifier, and otherwise only the framer's
`spec.md:88-94`, `plan.md:145` and `plan.md:157`, which the orchestrator
decided stay as written, and `questions.md` Q9, which says "a second clone"
and is true as it reads.

The pin was seen red (executed). In the round's clone, with
`docs/the-review-record.md` checked out at 86243d2f,
`test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`
failed with `AssertionError: the limit names the clone it holds in`
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1451`);
restored to a38e0b86, that case and the recommit case passed (probe rows 2
and 3).

confirms: round-7#2
`overview.md` carries a new row after the round-3 row, "The double-stamp
limit's extent (round 6)"
(`seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/overview.md:27`),
whose "Spec says" cell quotes `spec.md` §*Scope* and `plan.md` §*Technical
context* and its B1 row, whose Chosen cell names the class with d1af2e22 and
9a1330e8, and whose Grounds cell names Q9 (a) and says the frame's documents
are left as written. That is what `skills/implement/SKILL.md:400-401` asks
of a divergence: both sides quoted, which side won, and the grounds. 1efe22f3
changes `overview.md`, a path the finding's `location:` names.

Each quote is the frame's words (executed): the four quoted spans, matched
with whitespace folded, are present in `spec.md` and `plan.md`, four of four
(probe row 4). Line 145 sits under `plan.md`'s `## Technical context`, as
the row says. The round-3 row's "Spec says" cell now says B1 named nothing
for a second clone at round 3 and names the amend in a second clone since the
reframe after round 5. Both halves hold (read): `plan.md` at b81de037, the
commit that added `rounds/round-3.md`, has no "second clone" in it, and
`plan.md:157` at a38e0b86 names it. The cell's "(the next row)" points at the
new row, which is the next one.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round | — | the orchestrator's broad run, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test` of the stamp module, `test_docs_line_wrap.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_the_changelog_is_gathered_at_release.py` and `test_every_reader_ends_a_line_where_gfm_does.py` with `-q`, in the round's clone at a38e0b86 | 211 passed, exit 0 |
| `docs/the-review-record.md` checked out at 86243d2f in the clone; `bin/test` of the stamp module `-q -k test_the_policy_names_what_enforces` | 1 failed (`AssertionError: the limit names the clone it holds in`), exit 1 |
| the file restored to a38e0b86; `bin/test` of the stamp module `-q -k "test_the_policy_names_what_enforces or recommit"`; `git status --short` | 3 passed, exit 0; clean |
| a Python check of the new memo row's four quoted spans against `spec.md` and `plan.md`, whitespace folded | four of four present |
| this record: staged in the clone, `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py` and `test_docs_line_wrap.py` with `-q`; `chain_check.py --baseline f6ae6db6 --root <the branch worktree> --worktree` | 80 passed, exit 0; exit 0 as a draft, no refusal for this record, beside the absent `broad-gate.md` and `guarantee.md` |
