# 1792533444-automation-refuses-mid-run-questions — review round 3

target: d8bc086f, fixes 067a37a8..d8bc086f

This is a verifying round. It read the fix diff 067a37a8..d8bc086f in a
`git clone --no-local` checked out at d8bc086f. Carried from round 2: the
callers of `automation_answered` it listed, which this round found again
with the same search, and the probe in its `## Probes` row. That probe was
written again and re-run, not trusted from the earlier record. Every verdict
below is this round's own.

This round opens nothing. What comes due is the orchestrator's broad run,
and the sealer's spawn after it.

## Findings

## Confirmations

confirms: round-2#1
The bound now fails closed. `last_routing_answer` returns `UNREAD` in three
cases: no transcript resolves, the clone cannot be resolved, or the read
fails (`hooks/worktree_consent.py:338-343`, `hooks/worktree_consent.py:399-400`).
It returns None only after it read a transcript and found no routing answer
from this clone. The gate's condition is still `is None`
(`hooks/question-gate.py:105-111`), so `UNREAD` is refused. I re-ran round
2's probe on a branch declared `yes`, with the framer question dressed in
question 1's labels each time:

- No `session_id`: deny, then deny again.
- A transcript path that names no file: deny.
- A readable transcript with no entries: silent. This is the resume the
  exemption is for.
- The same transcript holding the routing answer: deny.
- The same path made unreadable: deny, and the reader returns `UNREAD`.

All four of round 2's states now deny. This was executed by
`bin/test tests/test_tmp_round3_probe.py -q -s -n0`.

confirms: round-2#2
`plan.md`'s summary now bounds the exemption until this session has
answered it from this clone
(`seal/specs/1792533444-automation-refuses-mid-run-questions/plan.md:14-16`).
That matches `spec.md` scope item 3. The summary leaves out the
readable-transcript condition, which `spec.md` carries, but it does not
contradict it. This was read.

confirms: none
No caller treats `UNREAD` as truthy or as an answer, though `object()` is
truthy. I searched with `git grep` for `last_routing_answer`,
`automation_answered` and `UNREAD` across `hooks`, `bin`, `skills` and
`.github`:

- `last_routing_answer` has two callers. The gate compares with `is None`.
  `automation_answered` compares with `is True`
  (`hooks/worktree_consent.py:285`), so it still returns a bool.
- Every other caller goes through `automation_answered`:
  `hooks/worktree-guard.py:2617`, `hooks/commit-review-gate.py:857`,
  `hooks/commitgate.py:100` and `hooks/worktree_consent.py:420`. So none of
  them sees `UNREAD`.

The probe also showed `automation_answered` returning True for the answered
transcript and False for the unreadable one. This was executed.

confirms: none
The new cases read against their group cover what the group did not:

- `test_the_routing_question_is_refused_where_no_transcript_can_be_read`
  covers the first and third `UNREAD` returns through the gate.
- `test_the_press_reader_reads_nothing_for_a_root_that_is_no_clone` covers
  the clone return at the reader, which the gate cannot reach because its
  root is always a clone.
- The two silent cases now write an empty transcript first, so they test the
  None branch and not the unread branch.

This was read at `tests/test_an_automation_run_puts_no_question.py:215-244`.

confirms: none
The framer's amendment d8bc086f describes the build. `spec.md` scope item 3,
S8, the exemption paragraph and the rule's `to:` text all state None as
"read, and not answered" and `UNREAD` as refused. They also carry the limit
that any routing answer from this clone spends the exemption, which the
gate's docstring states too (`hooks/question-gate.py:29-32`). `questions.md`
agrees. This was read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the typecheck at d8bc086f, labelled `unverified` | CI run 39512251059; `bin/broad-gate` | the orchestrator: the relay of run 39512251059, then its broad run |
| Two `AskUserQuestion` calls in one assistant message both pass before either answer is in the transcript | `hooks/question-gate.py:105-111` | the orchestrator, beside the `questions.md` Q1 measurement (carried from round 2) |
| Whether the harness runs the hook and honours its deny | `seal/specs/1792533444-automation-refuses-mid-run-questions/questions.md` Q1 | the orchestrator, by the measurement after install |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round3_probe.py -q -s -n0` | Round 2's probe written again, plus one more case: the readable transcript with no entries. Branch declared `yes`, with the framer question dressed in question 1's labels each time. No `session_id`: deny, then deny again. A path that names no file: deny. A readable transcript with no entries: silent. A readable transcript holding the routing answer: deny, the reader returning True, and `automation_answered` True. The same path made unreadable: deny, the reader returning `UNREAD`, and `automation_answered` False. The file was deleted |
