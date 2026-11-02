# Review round 3: 1793599985-a-mutant-that-does-not-compile-reads-as-caught

```seal
target: 4a9ab347, fixes 46775ced..4a9ab347
```

This is a verifying round. Its target is the fix diff `46775ced..4a9ab347`. It holds four commits. `dd9ec76d` is the orchestrator's correction of five stale version sentences, which answers finding 2. `f8532a37` is the fix pass's new case and docstring sentence for finding 1. `40c33242` adds the fix pass's close blocks. `4a9ab347` corrects `frame/plan.md:14` and adds `handoff.md`. The base is `release/v0.29.0`, at `40e6c23e`. The work happened in a `git clone --no-local` of the branch worktree at `4a9ab347`, under `<scratchpad>/898-round-3/clone`. Every mutation run used that clone's own `bin/seal mutate`, which resolves the clone's `skills/implement/scripts/seal.py` and so the branch's `skills/verify/scripts/mutation_check.py`, not the installed 0.28.0 copy. No `seal/parity.md` is declared, so the round block has no `original:` line.

Carried from earlier rounds without re-running: that `bin/seal layout --pairs` names no pair for `tests/skills/test_mutation_check.py` (round 1), and the round-2 probe that showed 3.12.9 and 3.13.9 refuse `x: (y := 1) = 2` only under `__future__.annotations.compiler_flag`, while 3.15.0 refuses it both ways. That probe was re-derived in part this round, for the exact line the new case uses (`## Probes`, row 4). Re-derived this round: the module's run, both mutants of the compile call, the version search over the work item's records, and every verdict below.

The implementer's account was read as claims. The fix pass claimed 67 passed in the module; this round ran it and got 67 passed, none skipped, under the clone's 3.13.9 virtualenv. It claimed that `dont_inherit=True` to `dont_inherit=False` reads red at the new case; this round ran that mutant and a second one that drops the argument, and both read red at that case alone. It claimed a narrow set of 1444 passed and 11 skipped; this round did not re-run that set. It ran the five modules that name the changed files instead (`## Probes`, row 5).

## Findings

None. Both of round 2's findings are closed as their close blocks say, and the diff adds no defect this round found.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `dont_inherit=True` at `skills/verify/scripts/mutation_check.py:226` is now pinned by `Test_main::test_a_mutant_is_compiled_without_the_scripts_own_future_flags` at `tests/skills/test_mutation_check.py:804-831`. The case was read as code. It replaces `OTHER = 2` with `ANNOTATED`, the line `OTHER: (y := 1) = 2` (`:237`). Its cases command is `red_on`, which fails only while the target holds `(y := 1)`, so the baseline passes and only the mutant run can be red. It asserts exit 0 and a first word of `red: `. With the argument in place, the compile accepts the line and the cases go red. With the script's own `from __future__ import annotations` (`mutation_check.py:120`) inherited, the compile refuses the line at exit 2 and the case fails. `run` calls `main` in the test's own process (`:177-181`), so the skip condition and the compile under test see the same interpreter.

The skip is computed at `:240-254`. It runs the case only where the line compiles with no flags and is refused under the flag. That is the one condition under which the mutant is not equivalent for this input, so a skip never hides a live mutant. The skip condition was evaluated outside pytest. It is true under 3.12.9 and false under 3.15.0, where the line is refused both ways (executed, `## Probes` row 4). So the case runs on CI's `windows-latest` legs on 3.12 and under the repository's 3.13 virtualenv, and skips under 3.15. The test module itself holds no `from __future__` import: its line 21 is `import __future__`, the module, so the helper's own `dont_inherit=True` at `:246` inherits nothing either way (read).

The case ran and passed under 3.13.9, with the module at 67 passed and no skip reported under `-rs` (executed, `## Probes` row 1). It was seen red under two mutants of the call, through the clone's `bin/seal mutate`: `dont_inherit=False`, and the argument dropped, which defaults to the same inheritance. Both read `red (exit 1, ...)` in one batch. Run alone, the dropped argument failed this case and no other, with the refusal text `named expression cannot be used within an annotation` (executed, `## Probes` rows 2 and 3). Against its group in `Test_main`, the case covers what no other case did: round 2 showed the module green under this mutant (`mutant 4: SURVIVED`, round 2 `## Probes` row 2). Contract rule 15 holds.

The docstring sentence at `mutation_check.py:217-220` says the flag "under 3.12 and 3.13 ... refuses a named expression in an annotation, which a target holding no such import compiles". That matches row 4 for 3.12.9 and round 2's probe for 3.13.9. The sentence names no 3.14 or 3.15 behaviour, so it claims nothing this repository has not measured. The case pins the behaviour the sentence states. `uvx ruff check` and `uvx ruff format --check` over the two changed Python files exit 0 (executed, `## Probes` row 6). The case's docstring cites "(round 2, finding 1)", a record the settle removes. Twenty-three other lines of comments and docstrings in `skills/` and `tests/` cite a round the same way (executed: `git grep -n -E "\(round [0-9]+, finding [0-9]+\)" -- skills tests`, which misses the new citation because it breaks across two lines). That is this repository's practice, and it is no finding.

```seal
confirms: round-2#2
```
What holds: `git show dd9ec76d` changes the five lines the finding listed, each to the replacement the finding gave or to wording that says the same (read). G11 (`frame/design.md:19`) says the installed plugin stays 0.28.0 until 0.29.0 is released, and the worktree is cut from `release/v0.29.0`. G12 (`:20`) names the first pull request into `release/v0.29.0`, renamed from `release/v0.28.1`. The plan's phase 2 row (`frame/plan.md:39`) reads `0.29.0` at HEAD (S9). *Operational impact* (`:46`) says a bare `seal` gets the fix once 0.29.0 is released. `gaps.md:7` names `seal gate --base release/v0.29.0`. The fix pass named one more line, `frame/plan.md:14`, which neither the finding nor `dd9ec76d` reached. `4a9ab347` rewrites it to say *Cutting a release* "puts the move to the release's version, now `0.29.0`, in the release's first pull request". That matches `docs/branch-and-release.md:31-32` (read).

To check that the class is whole, this round ran `git grep -n -E 'v?0\.28\.1'` at `4a9ab347` over the work item's directory (executed). Every hit that remains records what happened at the time or quotes the finding: design G4's milestone read (`:12`), G12's renamed-from clause (`:20`), *Scope* item 6's history clause (`:33`), the plan's *Judgments of the run* row (`:53`), `routing.md:17`, `handoff.md:8` and `:15`, the phase-2 record, and the round-1 and round-2 records. None of these tells a reader to act on 0.28.1. Round 2 noted that the class of spellings is unbounded. Its search covered the two spellings these files use, and this round's pattern covers both in one pass.

```seal
confirms: none
```
What holds: `handoff.md` in the work item's directory is allowed by `skills/implement/orchestration.md:67-70`, which has the orchestrator that hands the work over write one, and the one that takes it over delete it once it has read it. Its step 1, putting routing question 1 through `AskUserQuestion` again before the first spawn, is what `skills/implement/orchestration.md:159-163` asks of a run resumed in a new session (read). Its facts agree with the tree on the points this round opened: the four commits of the fix diff, `release/v0.29.0` at `40e6c23e` as the base, and round 3 being owed on f8532a37 (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `4a9ab347`. `gaps.md` labels the broad run `unverified` and names the orchestrator, which is honest. This round leaves nothing open, so the orchestrator's broad run is what comes due, and the sealer's spawn after it. | `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/gaps.md` | the orchestrator's broad run, `seal gate --base release/v0.29.0 --record` this work item |
| The fix pass's narrow count of 1444 passed and 11 skipped, read and not re-run. | `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/trail/rounds/round-2.md` | the orchestrator's broad run |
| Whether the new case passes on CI's four `windows-latest` legs on Python 3.12, where it runs and is not skipped (`frame/questions.md` Q1; carried from rounds 1 and 2). | `tests/skills/test_mutation_check.py` | the orchestrator, reading the pull request's CI run |
| Whether `handoff.md` is deleted by the orchestrator that takes the work over before the sealer reads the work item. No check refuses it kept (`skills/implement/acts.md:62`). | `seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught/handoff.md` | the orchestrator |
| Whether the five commits without a `Seal-Routing:` trailer are rewritten before the pull request, or left for the squash to replace (carried from rounds 1 and 2). | `skills/commit-pr-convention/SKILL.md:185-187` | the orchestrator |
| The pull request body's statements that `CONTRIBUTING.md` *What a change to a gate must carry* asks for. No body exists at this round (carried from rounds 1 and 2). | `CONTRIBUTING.md` | the sealer, reading `seal pr-body`'s file |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_mutation_check.py -q -p no:xdist -rs`, in the clone at `4a9ab347`, under the runner's `.venv` (Python 3.13.9) | 67 passed, no skip reported, exit 0 |
| `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'compile(source, path, "exec", dont_inherit=True)' 'compile(source, path, "exec", dont_inherit=False)' --replace 'compile(source, path, "exec", dont_inherit=True)' 'compile(source, path, "exec")' --tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist -x"`, from the clone | baseline passed; `mutant 1: red (exit 1, 7.6s)`; `mutant 2: red (exit 1, 7.2s)`; `2 mutants, 2 red, 0 SURVIVED`; exit 0. `git status --short` was empty after the run |
| `bin/seal mutate skills/verify/scripts/mutation_check.py --replace 'compile(source, path, "exec", dont_inherit=True)' 'compile(source, path, "exec")' --tests "bin/test tests/skills/test_mutation_check.py -q -p no:xdist"`, from the clone | `red: the cases failed against the mutation (exit 1)`, exit 0. `1 failed, 66 passed`; the one failure was `Test_main::test_a_mutant_is_compiled_without_the_scripts_own_future_flags`, against `assert code == 0`, on the refusal `line 2: named expression cannot be used within an annotation`. `git status --short` was empty after the run |
| The skip condition of `tests/skills/test_mutation_check.py:240-254`, retyped as a `python3 -I -c` one-liner, run under `python3` (3.15.0) and `/opt/homebrew/bin/python3.12` (3.12.9). It wrote no file | 3.15.0: compiles with no flags `False`, under the flag `False`, case runs `False`. 3.12.9: `True`, `False`, `True` |
| `bin/test` over `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py`, `tests/skills/test_arm_check.py`, `tests/skills/test_mutation_check.py`, `tests/skills/test_seal.py` and `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py`, the modules that `git grep -l -E 'mutation_check'` lists under `tests/` plus the one the plan names, at `4a9ab347` | 610 passed, 11 skipped, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_mutation_check.py` and `skills/verify/scripts/mutation_check.py`, in the clone | exit 0 and exit 0 |
| `git grep -n -E 'v?0\.28\.1' 4a9ab347 -- seal/threads/1793599985-a-mutant-that-does-not-compile-reads-as-caught`, in the clone | the hits listed under the round-2#2 confirmation, each a record of the time or a quote of the finding |
