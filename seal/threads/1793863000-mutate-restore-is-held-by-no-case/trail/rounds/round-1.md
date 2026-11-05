# Review round 1: 1793863000-mutate-restore-is-held-by-no-case

```seal
target: 831e7d6b against 5f5d7471
```

The round reviewed `git diff 5f5d7471..831e7d6b` and the frame as committed in `fe793f03`, `0528bb3a` and `f4b89053`, read whole at HEAD with the fold `831e7d6b` makes. It worked in a `git clone --no-local` of the branch checked out at `831e7d6b` in the round's scratch directory. No round ran before this one, so no fact was carried from an earlier record. `seal/config.md` has no `Pact` row and no `Record language` row, and the repository declares no `seal/parity.md`.

The axes walked were the frame's own: the restore's reach on each exit of a baseline that measured nothing, in both shapes (one pair and a batch); the message `restore` raises and every statement of what `not restored` means; whether any code line other than D4's string changed; and whether each new case holds a path no other case holds. Of the table's axes, error paths and state transitions apply. The diff adds no failure path, because S7 below shows the code is unchanged but for one string. Authorization, query scope, ordering, concurrency and security do not apply: the diff changes one printed string, comments, docstrings and cases.

## Findings

### 1. The phase record's D4 class paragraph hands back part of its grep as the whole list, and lists a rewritten comment among the hits that stay

```seal
severity: should
location: `seal/threads/1793863000-mutate-restore-is-held-by-no-case/trail/phases/phase-1.md:17`
evidence: executed `git grep -n -i 'mutated module\|not restored\|NotRestored\|NOT_RESTORED\|mutated file' 5f5d7471 -- ':!seal/threads'` in the clone; read `tests/skills/test_mutation_check.py:303-306`, `:975-981` and `:1726-1731` at `5f5d7471`, and `skills/verify/scripts/mutation_check.py:723-729` at `831e7d6b`
```

Why it matters: the paragraph names its grep, says each hit was read in place, and sorts the hits into the ones the phase changed and "the other hits stay". The sealer reads it as the phase's account of the class (contract rule 12), and the pull request body copies phase records. The same grep at the merge `5f5d7471` returns four lines of `tests/skills/test_mutation_check.py` that neither list names: 305, 527, 571 and 980. Each is true as it stands. Lines 305, 527 and 571 name the mutated file's bytecode, and line 980 is the docstring of `test_a_replacement_that_mutates_nothing_is_refused`, which names the unmutated file. So no code is owed. The account is. Contract rule 12 makes a list of a closed set handed back as whole, when the set's method did not produce it, a finding on the method even where every listed instance was handled. The list also names `mutation_check.py` line 721 among the lines that stay. At the merge, line 721 is "`-- a failed restore raises NotRestored instead, and is reported`", inside the `KeyboardInterrupt` comment that D2 rewrote at `4aa0aa4c`, so HEAD contradicts that sentence of the record. The changed list also leaves out the D4 case's own `pytest.raises` line, 1730, which `4aa0aa4c` changed to capture the message.

The paragraph that replaces line 17 of the phase record, whole:

```markdown
**The D4 class at the merge, by `git grep -n -i 'mutated module\|not restored\|NotRestored\|NOT_RESTORED\|mutated file' -- ':!seal/threads'`, each hit read in place (executed).** The phase changed these hits: `mutation_check.py` line 48, `restore`'s docstring and message, `NotRestored`'s docstring, `main`'s interrupt comment at line 721 (D2), `seal-mutate.md` line 61, the test docstring at lines 1109 to 1112, and the case at lines 1718 to 1730. The other hits stay. `mutation_check.py`'s "mutated file" at lines 11, 34 and 94, `seal-mutate.md` line 85, the behaviour module's lines 6 and 50, and the test module's lines 305, 527 and 571 each name the file whose bytecode is cleared. The test module's line 980 is the docstring of the case on a replacement that mutates nothing, and names the unmutated file. `mutation_check.py` lines 137, 210, 453, 505, 608, 613, 623, 629 to 630, 711 to 713 and 735, and the test module's lines 1079, 1095, 1099 to 1101, 1106, 1132 and 1223, state that a restore did not land or describe their own case's scenario. `agents/crafter.md` line 80 is the rule against a restore from HEAD. `.test_durations` line 3709 is a case's timing, keyed by a name that did not change.
```

The paragraph is the only statement of this list in the work item. `changelog.md` and `gaps.md` name no line of the class, so the snippet reaches every statement of the fact.

## Confirmations

The implementer's account was read whole, and each claim it makes about the code was checked as follows.

What matched: the crafter claimed that each of the five new parameters is red under its own mutant and green under the other four. Executed: each mutant of the phase record's table, applied by `bin/seal mutate` over `skills/verify/scripts/mutation_check.py` with only the new case selected, read `red`, and the verbose run listed one FAILED parameter: Mb `one-pair-no-baseline`, Mc `one-pair-timed-out`, Mbb `batch-no-baseline`, Mcb `batch-timed-out`, Mib `batch-interrupt`. The other four PASSED in each run. Each failure is at `tests/skills/test_mutation_check.py:1748`, the file-bytes assertion, with "after `<verdict>` the file holds what the cases wrote: b'VALUE = 99\n'". So the case's red is the guard it names (contract rule 15).

What matched: the frame's *Grounding* row on which cases drive those paths was read, not run, and claimed that a skip on any of the five paths leaves every case green. Executed: the same five mutants as one batch, over `tests/skills/test_mutation_check.py` and `tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py` with the new case deselected, read `SURVIVED` for all five. So the new case holds five paths that no case of either module held, which is what the rule on reading a new test against its group asks. `bin/seal layout --pairs tests/skills/test_mutation_check.py` names 0 pairs (executed). This is a probe over the two modules, not a seal of the suite.

What matched: D4's case was claimed red with the old sentence back. Executed: `bin/seal mutate` put "measured against a mutated module" back into `restore`'s message (`skills/verify/scripts/mutation_check.py:221-225`). `test_a_restore_whose_bytes_do_not_hash_to_the_original_raises` then failed at `tests/skills/test_mutation_check.py:1839`, the clause assertion, and the command read `red`.

What matched: S7, that no code line changed but D4's string. Executed: a probe script parsed `mutation_check.py` at `5f5d7471` and at `831e7d6b`, dropped every docstring, and compared `ast.dump`. The only string constant unique to each side is D4's sentence, and with those two replaced by one value the dumps are equal.

What matched: S8 and the claim of 78 passed. Executed: `bin/test tests/skills/test_mutation_check.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py -q` in the clone gave 78 passed, exit 0.

What matched: the fold `831e7d6b`. Its *Grounding* row cites #1393's frame at `4a3ed47c`. `origin/release/v0.32.5` holds that commit (executed: `git branch -a --contains 4a3ed47c`). At that commit, the cited frame's *Scope* items 1 and 2 and its out-of-scope line on #706 say what the row quotes (read: `git show 4a3ed47c:seal/threads/1793862998-seal-arms-is-run-by-nothing/frame/design.md`). `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q` gave 17 passed, exit 0, in the clone with the release and main refs fetched (executed). That is the failure the crafter's boundary run reported, and the fold answers it.

What matched: D2 at `skills/verify/scripts/mutation_check.py:723-729`. An interrupt raised inside `run_cases` ends the process (`:426-428`) and passes through the `finally` of `mutation_run` (`:489-490`) or of `batch_run` (`:527-528`, `:542-545`), which call `_put_back`. `_put_back` turns a failed write or a wrong hash into `NotRestored` (`:627-637`). So the printed sentence that the file holds its first bytes is true wherever the interrupt lands. The comment names no round and no commit (read).

What matched: D3's four statements, at `skills/verify/scripts/mutation_check.py:48-50`, `:256-258`, `skills/verify/seal-mutate.md:61-62` and `tests/skills/test_mutation_check.py:1134-1137`, each say the restore did not land and the file may hold the break or what the cases wrote. The test docstring keeps its own scenario. A `git grep -n -i 'not restored'` over the tree at HEAD finds no other description of the verdict outside the work item (executed).

What matched: D4's message and `restore`'s docstring (`skills/verify/scripts/mutation_check.py:203-225`) keep "was not restored" and both hashes, and drop "mutated module" and "mutated file". The new assertions at `tests/skills/test_mutation_check.py:1837-1843` pin the hashes, the new clause and the absence of "mutated module", as S9 asks.

What matched: D1's four assertions are in the new case at `tests/skills/test_mutation_check.py:1738-1751`. They are the stand-in's log line, exit 2, the first line's verdict, and the file's bytes. The batch parameters also assert that no `mutant ` line is printed (S3), and the interrupt parameter asserts the "holds the bytes" sentence (S5). The timed-out and interrupt parameters carry `POSIX_ENDING` (`:366-368`), as the plan's Windows row decides. `changelog.md` and `gaps.md` say the same of the case and of the skips.

Two observations are not findings. `NotRestored`'s docstring at `skills/verify/scripts/mutation_check.py:257-258` ends "and is restored from the commit made before the run", which reads as a statement that something restores the file, not as the act the verdict table and `seal-mutate.md` ask a person to take. The docstring is read by whoever next edits the script, not by a party at a step. `POSIX_ENDING` at `tests/skills/test_mutation_check.py:366-368` is a second spelling of the `skipif(os.name == "nt", ...)` that four neighbouring cases write inline, with its own reason. It changes no behaviour.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. This round ran three narrow modules; the suite is `unverified` | the tree at `831e7d6b` | the orchestrator, at the broad gate (`seal/config.md` *Broad gate*) |
| The crafter's fifteen-module boundary run of 1589 passed, 8 skipped and 1 failed. Not re-run; only its one failure was checked, through the fold above | `trail/phases/phase-1.md:39` | the orchestrator, at the broad gate |
| Whether the two `no baseline` parameters pass on Windows (`frame/questions.md` Q1), and whether the 1-second bound leaves the timed-out parameters' stand-in time to write on a loaded Linux runner | `tests/skills/test_mutation_check.py:1680-1700` | the pull request's CI run on its `ubuntu-latest` and `windows-latest` legs |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_mutation_check.py tests/behaviour/test_a_mutation_clears_one_files_bytecode_and_ends_at_a_timeout.py -q` | 78 passed, exit 0 |
| `bin/seal mutate skills/verify/scripts/mutation_check.py` with the five mutants Mb, Mc, Mbb, Mcb and Mib as one batch, `--tests` over both modules with `-k "not test_what_the_cases_wrote_in_a_baseline_with_no_verdict_is_put_back"` | five `SURVIVED`, exit 1 |
| the same batch, `--tests` selecting only the new case | five `red`, exit 0 |
| each mutant alone, `--tests "bin/test tests/skills/test_mutation_check.py -v -p no:xdist -k test_what_the_cases_wrote_in_a_baseline_with_no_verdict_is_put_back"` | each `red`, with only its own parameter FAILED, at `:1748` |
| `bin/seal mutate skills/verify/scripts/mutation_check.py` putting D4's old sentence back, `--tests` selecting `test_a_restore_whose_bytes_do_not_hash_to_the_original_raises` | `red`, exit 0, failed at `:1839` |
| a probe script comparing the docstring-free `ast.dump` of `mutation_check.py` at `5f5d7471` and `831e7d6b` | differs only in D4's string constant; equal once both are replaced |
| `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q`, with `origin/release/v0.32.5` and `origin/main` fetched into the clone | 17 passed, exit 0 |
| `bin/seal layout --pairs tests/skills/test_mutation_check.py` | 1 file read, 0 pairs |
