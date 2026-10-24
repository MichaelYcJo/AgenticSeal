# 1792533444-automation-refuses-mid-run-questions — review round 4

target: efd90497, fixes 045812ac..efd90497

This is a verifying round on efd90497, the fix written after the sealer
withheld at 00f95bb1. It read the fix diff in a `git clone --no-local`
checked out at efd90497. The diff's only file outside this item's records is
`tests/test_an_automation_run_puts_no_question.py`.

Round 3 missed what the sealer found. It checked that the silent cases now
write a transcript, but it did not check whether the `deny` cases reach their
assertion only through `UNREAD`. This round checked every `deny` case in the
module. It carried nothing from round 3 as a verdict. The sealer's withheld
verdict (`seal/specs/1792533444-automation-refuses-mid-run-questions/guarantee.md:38`)
was read as a claim and re-run as mutations.

## Findings

### 1. The unreadable-call case still reaches its routing-shaped deny only through UNREAD, so the options guard is held by no case

severity: should
location: `tests/test_an_automation_run_puts_no_question.py:321-332`, `hooks/worktree_consent.py:177-179`
evidence: executed `bin/mutation-check hooks/worktree_consent.py --replace "<options guard returning False>" "<returning True>" --tests "bin/test tests/test_an_automation_run_puts_no_question.py tests/test_the_guard_asks_once_per_session.py tests/test_an_automation_run_meets_no_commit_prompt.py -q"`, `bin/mutation-check hooks/worktree_consent.py --replace "<the same>" "<the same>" --tests "bin/test tests/test_tmp_round4_probe.py -q"`
verdict: fixed a3a88a39
regression: round-2#1

The unit is `test_an_unreadable_call_is_refused`, and the defect is the one
the sealer found in its two neighbours. c4aa0c8b, the fix for round-2#1,
made `last_routing_answer` return `UNREAD` where no transcript can be read,
and the gate refuses `UNREAD`. It wrote a transcript into the silent cases,
but not into the cases whose `deny` shows a shape is not question 1. efd90497
added the transcript to two of those three cases. It left this one out.

One of its five inputs is shaped like question 1:
`{"questions": [{**ROUTING_QUESTION, "options": None}]}`. Without a
transcript, that input is refused as `UNREAD` before the options guard in
`is_routing_question` decides anything (`hooks/worktree_consent.py:177-179`).
I mutated that guard to `return True` and ran three suites:

- this case alone: passed;
- the whole module (23 cases): passed;
- the module with both press-reader modules (143 cases): passed.

No case holds the guard. I then ran the same input, with an empty transcript
written first, as a probe. It passes unmutated and fails under the mutation,
`silent` against an expected `deny`.

The module's other four inputs here are held anyway. A mutation of the other
guards on those paths makes the gate raise. The gate then prints nothing,
and `deny` fails. Of the module's other `deny` cases, I checked each for a
shape assertion that only `UNREAD` carries:

- S1, S2, S6, S7 and the dispatcher case put the framer question. What they
  pin is the declaration read and its resolution. A mutation there turns
  them silent.
- `test_the_routing_question_is_refused_where_no_transcript_can_be_read`
  pins `UNREAD` itself.
- The routing question with company, the near miss, and the "only until it
  is answered" case now write transcripts.

So this is the class's last instance in the module.

The frame says, in `spec.md` S10, that an unreadable call under S1 is
`deny`. `plan.md` phase 1 says every case was seen red. The fix pass
followed that frame. The defect came from how it was written: the
transcript went into the silent cases and not into the deny cases that hold
a shape. The fix is the same line efd90497 wrote into the other two cases.

```python
def test_an_unreadable_call_is_refused(repo):
    declare(repo)
    write_the_transcript(repo)
    for tool_input in (
```

answer: The orchestrator's a3a88a39 adds `write_the_transcript(repo)` after `declare(repo)` in `test_an_unreadable_call_is_refused`, the line efd90497 gave its two neighbours, so the routing-shaped input with `options` None is refused by `is_routing_question`'s options guard rather than by `UNREAD`. The guard mutated to `return True` now reads 1 failed, 22 passed against the module (`bin/mutation-check`, exit 0); the module with `tests/test_gates_do_not_fail_open.py` and `tests/test_the_guard_asks_once_per_session.py` passes, 132.

## Confirmations

confirms: none
efd90497 holds for what it changed. With `write_the_transcript(repo)` in
`test_the_routing_question_with_company_is_refused` and
`test_a_near_miss_of_the_routing_question_is_refused`, the exemption's three
shape conditions are each held again. Each of these mutations of
`hooks/question-gate.py` turned exactly one case of the module red:

- `len(questions) != 1` to `< 1`;
- `multiSelect is False` to `True`;
- the string-`question` check to `True`.

The new pin of "is not yours to answer" in
`test_the_refusal_says_where_the_default_goes` turns red when the reason
says "is yours to answer". This was executed by `bin/mutation-check`, four
runs against `bin/test tests/test_an_automation_run_puts_no_question.py -q`,
each reading 1 failed, 22 passed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the typecheck at efd90497, labelled `unverified`. The broad run recorded at 045812ac precedes this test edit | CI run 39515009082; `bin/broad-gate` | the orchestrator: the relay of run 39515009082, then a new broad run before the sealer runs again |
| Whether the harness runs the hook and honours its deny | `seal/specs/1792533444-automation-refuses-mid-run-questions/questions.md` Q1 | the orchestrator, by the measurement after install |

## Probes

| Command | Result |
|---|---|
| `bin/mutation-check hooks/worktree_consent.py`, options guard `return False` to `return True`, against `test_an_unreadable_call_is_refused` alone, then the module, then the module with `tests/test_the_guard_asks_once_per_session.py` and `tests/test_an_automation_run_meets_no_commit_prompt.py` | 1 passed, 23 passed, 143 passed: the mutation survived every run, and the file was restored |
| `bin/test tests/test_tmp_round4_probe.py -q`, the options-None input with an empty transcript written first, unmutated and then under the same mutation | 1 passed unmutated. 1 failed under the mutation (`silent` where `deny` was expected). The file was deleted |
| `bin/mutation-check hooks/question-gate.py` on `len(questions) != 1`, `multiSelect is False`, the string `question` and "is not yours to answer", each against the module | each run read 1 failed, 22 passed |
