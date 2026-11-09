# Closing memo: 1794178393-the-batching-bars-are-met-or-removed

## Not verified

| Item | Who must answer |
|---|---|
| closed The broad gate at the branch's head: the full suite, the repository-wide lint and the format check | answered by the work item's broad gate, `trail/gate.md` `run: 8d0dab73 against 94d04d30`, which names no failing case and on which `guarantee.md` sealed |
| closed Whether a reader outside this repository reads `kind` or `bar` from a `session_cost.py --segments --json` row | a measurement no record asks for: the answer would decide whether the two removed keys need a note for an outside reader; no user report, open issue, failed run or other work item's rule waits on it, and nothing is opened |

## Not done

`.test_durations` keeps the timing entries of the cases this work removed. `frame/design.md` *Scope* leaves the file unedited, and `bin/test tests -q -k test_the_durations_file_prices_the_suite` passes with them in place (`trail/phases/phase-1.md`), so refreshing it is left to #1444 and the usual refresh rules.
