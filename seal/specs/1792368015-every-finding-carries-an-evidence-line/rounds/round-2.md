# 1792368015-every-finding-carries-an-evidence-line — review round 2

target: 555ef5ed, fixes 480c6917..555ef5ed

This verifying round read the fix diff `480c6917..555ef5ed` and nothing
outside it. It carried round 1's coordinates rather than searching again:
the two readers of merged records (`release_seal.py#chain_counts` and
`replay_targets.py#targets`), the mutation at `replay_targets.py:597`, and
the row's `executed` shape at `docs/the-review-record.md:46`. Every verdict
below was reached again on the code at 555ef5ed. All three closes hold, and
this round opens nothing.

## Findings

## Confirmations

confirms: round-1#1
e4837c2b rewrites `docs/the-review-record.md:235-250` in place, with the
round's text. The check judges no merged record at a pull request again, and
the paragraph names `.github/scripts/release_seal.py#chain_counts` and
`evals/scripts/replay_targets.py` as the two readers that still open merged
records (read). The two sentences
`tests/test_review_axes.py::test_a_record_written_before_a_line_was_added_is_no_finding`
pins stand unchanged, and that module passes (executed, the narrow run in
`## Probes`). The answer names the other places that said the same thing. The
fragment now says "judged at a pull request again"
(`seal/specs/1792368015-every-finding-carries-an-evidence-line/changelog.md:39-42`).
The three fixture comments now say the check's reader refuses the old table
(`tests/test_broad_gate.py:125`, `tests/test_the_release_seal_is_drawn.py:412`,
`tests/test_chain_check.py:131`). Each is true: the case beside it shows the
reader refusing that record (read, `tests/test_broad_gate.py:135-146`,
`tests/test_the_release_seal_is_drawn.py:552-563`). My own search for the
class found no other statement in the tree that nothing reads a merged round
record. The frame's `spec.md:21`, `:48` and `plan.md:138` say "no check reads
them again". Those lines are the frame's account of the check and are not
edited by a review (executed, the search in `## Probes`). The fix also went
to the changelog and three test files, which `location:` does not name. The
answer names them instead of appending them to `location:`, which
`docs/the-review-record.md:130-131` asks of a fix pass. Nothing reads the
appended coordinates for this finding, so I record it here and not as a
finding.

confirms: round-1#2
8b9aa8a6 adds round 1's case unchanged at
`tests/test_a_rewritten_definition_proved_non_inferior.py:1632-1673`. I
changed `evals/scripts/replay_targets.py:597` to `confirmed(nxt, n,
following)` in the round's clone, and the case failed. With the line
restored, the module passes (executed, the mutation row in `## Probes`). The
commit's new sentence in `written_at`'s docstring (`replay_targets.py:187-191`)
answers round 1's second `## Not judged` row: a record's own time is the
last commit that wrote it. That is the orchestrator's decision under the
owner's `automation` answer, and it is carried as given. Its reasoning
holds against the record document. A merged record is never rewritten
(`changelog.md:39-42`). An item in flight that respells a renamed line has
already been told to carry every added line (`docs/the-review-record.md:245-249`).
So the respelling commit's grammar asks nothing that the respelled record
lacks (read). Round 1's first `## Not judged` row is answered too: the
orchestrator ran `--list` in the worktree, where the target commits resolve,
and reports 31 targets and 56 left out. That count is the orchestrator's
`executed`, which this round did not repeat.

confirms: round-1#3
04de490b adds the sentence to the paragraph the warden opens at step 7
(`docs/the-review-record.md:102-110`). A command that holds a backtick is
written and run with `$(printf '\140')` in place of the character (read).
The spelling works in this shell: `printf` with octal 140 writes one
backtick byte, and `grep` finds it in a file (executed, the stand-in row in
`## Probes`). `test_both_evidence_forms_and_their_lists_read` now reads the
sentence from the document and holds that the row's shape accepts a command
spelt that way (`tests/test_chain_check.py:1275-1283`, read). I deleted the
sentence in the clone and the case failed. With the sentence restored, the
module passes (executed). `agents/warden.md` is unchanged, so the preload
stays at 27,168 bytes. As in finding 1, the answer names the test file
instead of appending it to `location:`, and this round records that here.

confirms: none
The other fix commits change only what their messages name. 604d4f42 changes
round 1 in its three `verdict:` lines and three `answer:` lines and nothing
else (executed, `git diff 480c6917..555ef5ed` over the record). 555ef5ed adds
one sentence to the fragment, the backtick stand-in, which matches the
document's sentence (read, `changelog.md:11-13`). The three `fixed` commits
each touch a path that their finding's `location:` names (read, `git diff
--stat` of each commit).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 555ef5ed, which this round did not run (`unverified`) | the branch | the orchestrator's `broad-gate` run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_chain_check.py tests/test_review_axes.py tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist` | 197 passed |
| `bin/test tests/test_chain_check.py tests/test_a_rewritten_definition_proved_non_inferior.py -q -p no:xdist -k "targets_reads_the_next_round or both_evidence_forms"`, with `replay_targets.py:597` changed to `confirmed(nxt, n, following)` and the stand-in sentence deleted from `docs/the-review-record.md`, both in the round's clone, then restored | both cases failed: 2 failed |
| `printf 'a%sb\n' "$(printf '\140')"` into a scratch file, then `grep -c "$(printf '\140')"` and `od -c` over it, file removed | 1 match; the bytes are `a`, U+0060, `b`, newline |
| `git grep -n -i -E "nothing reads\|no reader reads\|read by nothing\|read again\|is read by no" -- . ':!seal' ':!.test_durations' ':!changelog'`, and the same words over this item's frame | no statement about round records outside the frame; the frame's `spec.md:21`, `:48` and `plan.md:138` |
