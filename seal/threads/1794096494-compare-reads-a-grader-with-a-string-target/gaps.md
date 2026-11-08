# Closing memo: 1794096494-compare-reads-a-grader-with-a-string-target

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the test modules that read a path it changed, on macOS alone | the orchestrator, at the broad gate |
| Whether `compare` reads the paid crafter pair of #1178, the sides at `33ced573b` and `4531133b7`, as `Verdict: pass` at HEAD (`frame/questions.md` Q1). The side files are not in this environment, so phase 1 ran the synthetic case of `frame/design.md` *Scope* item 3 alone | the repository owner, who holds the side files of #1178 |
| closed whether `regrade` on a side holding a grader whose target is `files` now exits 0. No case runs `regrade` on such a side, as `frame/design.md` *Scope* puts out; phase 1 read that `regrade` reaches `reads_record` only through `side_numbers(out)` at `evals/scripts/noninferiority.py:1499`, the call the `compare` case covers | `trail/rounds/round-1.md` *Probes* row 3, executed at `b30ca3846`: a probe ran `regrade` on such a side onto the `_suites` fixture's own commit, which exited 0 and printed its `graded on` line, and with the guard of `evals/scripts/noninferiority.py:363` reverted it raised the `AttributeError` through `:1499` |

## Not done

nothing
