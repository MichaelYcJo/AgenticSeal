# 1792533444-automation-refuses-mid-run-questions — review round 5

target: bbac7245, fixes efd90497..bbac7245

This is a verifying round. It read the fix diff efd90497..bbac7245 in a
`git clone --no-local` checked out at bbac7245. The diff holds one test line,
from a3a88a39, and the fix pass's two lines in `rounds/round-4.md`, which
close round-4#1 and answer it. Nothing else in that record changed. The fix diff adds no case and changes no code, so round 4's sweep of
the module's `deny` cases stands as round 4 ran it. This round re-ran that
sweep's executed line, the mutation, rather than carrying its result.

This round opens nothing. What comes due is the orchestrator's broad run at
bbac7245, and the sealer's spawn after it.

## Findings

## Confirmations

confirms: round-4#1
`test_an_unreadable_call_is_refused` now writes the transcript after
`declare(repo)` (`tests/test_an_automation_run_puts_no_question.py:323`), as
its two neighbours do. The input shaped like question 1 with `options` None is
now refused by the options guard in `is_routing_question`
(`hooks/worktree_consent.py:177-179`), and no longer by `UNREAD`. I re-ran
round 4's mutation, which changes the guard from `return False` to
`return True`, twice. Against this case alone: 1 failed. Against the module:
1 failed, 22 passed, the failure being this case. Unmutated, the module
passes 23. This was executed by `bin/mutation-check hooks/worktree_consent.py`
against `bin/test tests/test_an_automation_run_puts_no_question.py -q` and
its `-k test_an_unreadable_call_is_refused` form.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the lint and the typecheck at bbac7245, labelled `unverified`. The recorded broad run precedes efd90497 and a3a88a39 | CI run 39515654037; `bin/broad-gate` | the orchestrator: the relay of run 39515654037, then the broad run before the sealer runs again |
| Whether the harness runs the hook and honours its deny | `seal/specs/1792533444-automation-refuses-mid-run-questions/questions.md` Q1 | the orchestrator, by the measurement after install |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_an_automation_run_puts_no_question.py -q` | 23 passed |
| `bin/mutation-check hooks/worktree_consent.py`, options guard `return False` to `return True`, against `test_an_unreadable_call_is_refused` alone and then against the module | 1 failed, and 1 failed with 22 passed; the failing case was `test_an_unreadable_call_is_refused` both times, and the file was restored |
