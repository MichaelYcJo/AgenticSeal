# Review round 8: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 3a0342f23, fixes 96f432ef5..3a0342f23
```

This verifying round read the diff `96f432ef5..3a0342f23`. That diff holds the fix pass over round 7: one test commit (`d0992cfd8`, `tests/skills/test_passages.py`), the orchestrator's judgment row (`59b2f9d2c`, `frame/plan.md:62`), round 7's record (`620b1afae`) and its close block (`3a0342f23`). Round 7 closed its one finding `fixed d0992cfd8`, and this round answers it below. Probes ran in a `git clone --no-local` of the main clone checked out at `3a0342f23`, under the round's scratch directory. Each mutation went through `bin/seal mutate`, which writes the mutant and restores the file from held bytes. The clone and every output file were removed before hand-back.

Carried as coordinates and not re-established: where the corpus guard lives (`skills/settle/scripts/passages.py#in_corpus`, with `TOP_FILES` and `TOP_DIRS` at `passages.py:29-30`); round 7's result that the `tests/` and `hooks/` mutant survives the four modules that read the corpus, and that `git ls-files` lists no tracked `.md` under `tests/` or `hooks/`; and round 4's `bin/seal layout --pairs` result that no duplicate pair names `tests/skills/test_passages.py`. The diff changes the parameters and the comment of one case and adds no test module, so the pairs were not printed again. The close's account of its `seal mutate` runs, the judgment row and the comment above the case were read as claims. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round confirms round 7's close. Each of the three restored paths goes red, alone, under its own directory added to `TOP_DIRS`, and the four one-guard parameters still go red each under its own guard alone. It opens one finding, a `should`, on a `regression:` line, and no `must`. The commit added three paths and kept the comment's opening count, "One path per guard". With seven paths over four guards that count is now false, and it is the reading round 7 named as the cause of the regression it found.

## Findings

### 1. The case's comment still opens "One path per guard" over seven paths and four guards, and "fails exactly its paths" claims more than a prefix widening does

```seal
severity: should
location: `tests/skills/test_passages.py:49-50`
evidence: executed `bin/seal mutate skills/settle/scripts/passages.py --replace 'TOP_DIRS = ("docs/", "skills/", "agents/", "templates/")' 'TOP_DIRS = ("docs", "skills", "agents", "templates")' --tests "bin/test tests/skills/test_passages.py -q -rf --tb=no -p no:xdist -p no:cacheprovider"`
regression: round-7#1
```

Why it matters: the unit is `Test_in_corpus::test_refuses_a_path_one_guard_alone_refuses` (`tests/skills/test_passages.py:49-85`), which fix commit `d0992cfd8` changed. The frame's row (`frame/plan.md:62`) has the fix pass apply round 7's paste-ready change: restore the three `TOP_DIRS` parameters with ids, and narrow the comment to say the directory list is a sample. The fix did exactly that. The paste-ready text it applied rewrote the comment's second line and kept its first. So the defect came from round 7's own text, which amended the sentence on the old fact (four paths, one per guard) but left the count that stood on that fact.

The comment now reads, at `:49-50`: "One path per guard of `in_corpus`, each refused by that guard alone, so widening a guard at a boundary named here fails exactly its paths." The case holds seven paths (`:58-72`, read) over four guards (`passages.py:57-61`, read). The prefix guard holds four of them: `docs-old/notes.md`, `tests/README.md`, `hooks/notes.md` and `seal/threads/1-x/frame/design.md`. So "one path per guard" is false as a count.

"Fails exactly its paths" has two readings. Read as the guard's paths, it says that dropping the prefix's slash fails all four prefix paths. Executed in the scratch clone at `3a0342f23`: `TOP_DIRS` written without slashes fails only `[top-dirs-slash]`, 1 failed and 18 passed. Read as the boundary's paths, it holds. The inner comment at `:66-69` gives the second reading for the directory paths, but the header is what a reader meets first.

This is a sentence an agent reads and acts on. Round 7 traced its regression to reading "one parameter per guard" as "only one per guard". That reading made round 6's fix delete the three directory paths. The header now opens with that same count over a case that holds more, so the next pass that tidies the case to the header deletes them again.

It is no `must`. No assertion changed, and every parameter fails under its own boundary and no other (see the confirmation of round-7#1). The fix touches the comment alone, so it owes no red case.

```python
    # Paths each refused by one guard of `in_corpus` alone, one or more per
    # guard, so widening a guard at a boundary named here fails exactly that
    # boundary's paths. Membership in `TOP_FILES` and the `TOP_DIRS` prefix
    # are the two sides of one `or`, so each is widened at its boundary:
    # membership to every top-level path, the prefix to its directory names
    # without their slash and to a directory it does not list.
```

## Confirmations

```seal
confirms: round-7#1
```
What holds: the close `fixed d0992cfd8`. Claimed: the paste-ready change applied as written, and each restored path fails alone under its directory added, while the four one-guard parameters still fail alone. Read: the diff `96f432ef5..3a0342f23` over `tests/skills/test_passages.py` is round 7's paste-ready block line for line, the three paths at `:70-72` and their ids at `:79-81`. Executed in the scratch clone at `3a0342f23`, one `bin/seal mutate` run per mutant over `tests/skills/test_passages.py` with `-rf`, each run 1 failed and 18 passed:

- `TOP_DIRS` with `"tests/"` added: the failure `[top-dirs-not-tests]`.
- `TOP_DIRS` with `"hooks/"` added: the failure `[top-dirs-not-hooks]`.
- `TOP_DIRS` with `"seal/"` added: the failure `[top-dirs-not-records]`.
- `rel.endswith(".md")` replaced by `True`: the failure `[the-md-suffix]`.
- `and not rel.endswith(".ko.md")` replaced by `and True`: the failure `[the-ko-exclusion]`.
- `rel in TOP_FILES` replaced by `"/" not in rel`: the failure `[top-files]`.
- `TOP_DIRS` written without trailing slashes: the failure `[top-dirs-slash]`.

Round 7's `tests/` and `hooks/` mutant, which survived at `96f432ef5`, is now red under either directory alone, and each failure names its own id. No restored path is also held by membership or by the slash, since neither of those mutants fails a restored id. The comment's new sentence calling the directory paths a sample matches what the runs show: each path pins the one directory it names. The count at `:49` is finding 1.

```seal
confirms: none
```
What matched: the change as code. The seven ids follow the seven parameters in order (read, `:58-81`). The three new ids are cited nowhere in the tree outside `seal/` but the case (executed, `git grep`). The unmutated module passes, 19 cases (executed). `uvx ruff check` and `uvx ruff format --check` over the file each exit 0 (executed). The three restored paths are the ones `2f5d5f060` held (read, round 7's probe of that version). Within `tests/skills/test_passages.py` they cover what no other case covers there, since round 7 found the directory mutants survived this module at `96f432ef5` (carried).

```seal
confirms: none
```
What matched: the judgment row (`frame/plan.md:62`). It closes round 7's `should` as fixed rather than `deferred seal/follow-up.md`, and it cites `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* (read, `:102-123`). That section's verifying round reads the fix diff. A fix located in code is read by a round whatever its fix touched (`:111-112`), so this round is owed. Finding 1 is located in a test file, so that sentence applies to its fix as well.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `3a0342f23`. This round ran one module and the changed file's lint, so the suite is `unverified`. Finding 1 is open, and its route comes before the broad run. | the branch at `3a0342f23` | the orchestrator, at `seal gate` after the rounds settle |
| Whether finding 1 is fixed, which owes a verifying round under `orchestration.md:111-112`, or deferred under the cap the row at `frame/plan.md:61` set and the row at `:62` kept in substance | `frame/plan.md:61-62` | the orchestrator |
| The changed case on the Windows leg | `tests/skills/test_passages.py:49-85` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/settle/scripts/passages.py` over `bin/test tests/skills/test_passages.py -q -rf --tb=no -p no:xdist -p no:cacheprovider`, one run each: `TOP_DIRS` plus `"tests/"`, plus `"hooks/"`, plus `"seal/"` | each run red, 1 failed and 18 passed: `[top-dirs-not-tests]`, `[top-dirs-not-hooks]`, `[top-dirs-not-records]` in that order |
| the same command, one run each: the suffix to `True`, the edition exclusion to `True`, `rel in TOP_FILES` to `"/" not in rel`, `TOP_DIRS` without slashes | each run red, 1 failed and 18 passed: `[the-md-suffix]`, `[the-ko-exclusion]`, `[top-files]`, `[top-dirs-slash]` in that order |
| `bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider`, unmutated | exit 0, 19 passed |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_passages.py` | exit 0 both |
| `git grep -n -e top-dirs-not -e one_guard_alone -- ':!seal'` | four lines, all in `tests/skills/test_passages.py` (`:79-81`, `:84`) |
