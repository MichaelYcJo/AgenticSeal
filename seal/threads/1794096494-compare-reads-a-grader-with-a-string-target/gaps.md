# Closing memo: 1794096494-compare-reads-a-grader-with-a-string-target

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at HEAD. Phase 1 ran the test modules that read a path it changed, on macOS alone | the orchestrator's broad run, `trail/gate.md`, run `d5f42d5a1 against 8c2d60e14`, on which `guarantee.md` sealed at `517b9606e` (settle of 0.32.6 to 0.34.1) |
| closed Whether `compare` reads the paid crafter pair of #1178, the sides at `33ced573b` and `4531133b7`, as `Verdict: pass` at HEAD (`frame/questions.md` Q1). The side files are not in this environment, so phase 1 ran the synthetic case of `frame/design.md` *Scope* item 3 alone | this settle's run at `591c136cc`, executed on the owner's machine, which holds the sides under `SpecSeal-worktrees/paid-0.34.0/`: `python3 evals/scripts/noninferiority.py compare --agent crafter --phase 1 --old crafter-33ced573b.json --new crafter-4531133b7.json` printed `Verdict: pass`, every reach and shape grader 1 of 1 on both sides, `shape-no-probe-left` among them (settle of 0.32.6 to 0.34.1) |
| closed whether `regrade` on a side holding a grader whose target is `files` now exits 0. No case runs `regrade` on such a side, as `frame/design.md` *Scope* puts out; phase 1 read that `regrade` reaches `reads_record` only through `side_numbers(out)` at `evals/scripts/noninferiority.py:1499`, the call the `compare` case covers | `trail/rounds/round-1.md` *Probes* row 3, executed at `b30ca3846`: a probe ran `regrade` on such a side onto the `_suites` fixture's own commit, which exited 0 and printed its `graded on` line, and with the guard of `evals/scripts/noninferiority.py:363` reverted it raised the `AttributeError` through `:1499` |

## Not done

nothing
