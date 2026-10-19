# 1792368013-the-scribe-is-written-anew-from-its-job — review round 2

target: 98c5729d, fixes 7bf8af10..98c5729d

## Findings

None. The fix range has two commits. 22187f49 changes
`skills/legacy-parity/SKILL.md` and `tests/test_review_axes.py`, and 98c5729d
rewrites round 1's three `verdict:` and `answer:` lines. Read: the diff of
`rounds/round-1.md` changes those six lines and nothing else.

## Confirmations

confirms: round-1#1
The close holds. `skills/legacy-parity/SKILL.md:38` now names
`tests/test_review_axes.py::test_the_resolution_order_ends_with_the_caller_asking`.
That case reads the section's own text: `parity-paths.md`, the caller asking
and recording, `original not found` for a reader that cannot ask, and the
guessed-original sentence (`tests/test_review_axes.py:87-102`, read). Its
group is the module's two other `legacy-parity` cases, and neither reads this
section.

Executed, in a `git clone --no-local` at 98c5729d. I replaced lines 35-37 with
the base's *Where none resolves, ask the user and record the answer.*, and the
case failed (exit 1, *the resolution order lost …*). With the file restored by
`git checkout`, it passed (exit 0). This is the mutation round 1 showed no
case caught. The fix pass claimed a second mutation, the guessed-original
sentence deleted alone, was seen red. I did not re-run that one; the clause
is one of the four the case asserts (read).

confirms: round-1#2
The close holds. Read: `skills/legacy-parity/SKILL.md:67-68` now reads
"Start every comparison there instead of searching the original; the caller
pins what it settles with a test". So none of the three sections the scribe's
step 1 names (`agents/scribe.md:27-28`) asks its reader for a write. The
section's `Enforced by: nothing — no case declares seal/parity.md` is
unchanged, as the answer says.

confirms: round-1#3
The close holds. Read: `skills/legacy-parity/SKILL.md:59-61` now says a
mid-layer condition that never changes the response "is reported as such and
needs no reproduction". It also says "Read the original's history: a later
fix is its intent". Both steps are back in the section the scribe's step 4
sends it to. Executed: `tests/test_docs_line_wrap.py` passed, so the rewrapped
lines are inside 88 columns.

confirms: none
The read set still holds after the fixes. Executed:
`bin/payload-meter --root <clone> --agent scribe` at 98c5729d printed
`agents/scribe.md` 3,319, `skills/agent-contract/SKILL.md` 16,603 and a total
of 34,697 B. `wc -c skills/legacy-parity/SKILL.md` printed 5,695. The agent's
share is 3,319 + 16,603 + 5,695 = 25,617 B against 25,691, and the read set
is 34,697 + 5,695 = 40,392 B. Both match the figures `changelog.md` now
carries.

confirms: none
Nothing else in the fix range breaks a check. Executed: `bin/test` over
`tests/test_review_axes.py`, `tests/test_docs_line_wrap.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/test_the_record_is_written_in_words.py` and
`tests/test_a_moved_rule_leaves_its_definition.py` exited 0 (284 passed).
`bin/rules --check` exited 0.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck on this branch | the branch at 98c5729d | the orchestrator's broad gate, now due |
| Whether a scribe spawn follows its step 1 and returns `original not found` where no original resolves. No case runs the scribe (#957's Q3) | `agents/scribe.md` | the repository owner, at the first parity run |

## Probes

| Command | Result |
|---|---|
| `bin/payload-meter --root <clone> --agent scribe` | exit 0; total 34,697 B, `agents/scribe.md` 3,319, `skills/agent-contract/SKILL.md` 16,603 |
| `bin/test tests/test_review_axes.py tests/test_docs_line_wrap.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_the_record_is_written_in_words.py tests/test_a_moved_rule_leaves_its_definition.py -q -p no:xdist` | exit 0; 284 passed |
| `bin/rules --check --root <clone>` | exit 0 |
| `skills/legacy-parity/SKILL.md:35-37` replaced with the base's wording, then `bin/test tests/test_review_axes.py::test_the_resolution_order_ends_with_the_caller_asking` | exit 1, the case reports a lost clause |
| the same case after `git checkout` restored the file | exit 0 |
