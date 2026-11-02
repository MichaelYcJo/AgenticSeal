# Review round 9: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

```seal
target: 113acbe19, fixes 3a0342f23..113acbe19
```

This verifying round read the diff `3a0342f23..113acbe19`. That diff holds the fix pass over round 8: one test commit (`22d2fa3bc`, the comment at `tests/skills/test_passages.py:49-57`), the orchestrator's judgment row (`9b55e4a32`, `frame/plan.md:63`), round 8's record (`de22127b2`) and its close block (`113acbe19`). The judgment row bounds this round to that comment, read against `skills/settle/scripts/passages.py#in_corpus` and the case's parameters. Round 8 closed its one finding `fixed 22d2fa3bc`, and this round answers it below. Probes ran in a `git clone --no-local` of the main clone checked out at `113acbe19`, under the round's scratch directory. Each mutation went through `bin/seal mutate`, which writes the mutant and restores the file from held bytes. `git status` in the clone was empty after the runs, and the clone was removed before hand-back.

Carried as coordinates and not re-established: where the corpus guard lives (`passages.py:57-61`, with `TOP_FILES` and `TOP_DIRS` at `passages.py:29-30`); round 8's result that the three new ids are cited nowhere outside `seal/` but the case; and round 4's `bin/seal layout --pairs` result that no duplicate pair names `tests/skills/test_passages.py`. The diff changes one comment and adds no test, so the pairs were not printed again. The close's account of its `seal mutate` runs was read as a claim, and every run it names was run again here. `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` holds no `Record language` row, so the record is English.

This round confirms round 8's close: each sentence of the new comment holds against a mutant run here. It opens one finding, a `should`, on a `regression:` line, and no `must`. The finding is the case's name, which still says each path is refused by "one guard alone". The fix pass's own answer judged that claim false in the comment and rewrote it there, and the name keeps it. The finding is on wording, not an assertion, so under the judgment row at `frame/plan.md:63` it goes to `deferred seal/follow-up.md`.

## Findings

### 1. The case is still named `test_refuses_a_path_one_guard_alone_refuses`, the claim the fix pass judged false in the comment above it

```seal
severity: should
location: `tests/skills/test_passages.py:87`
evidence: executed `bin/seal mutate skills/settle/scripts/passages.py --replace 'rel in TOP_FILES' 'True' --tests "bin/test tests/skills/test_passages.py -q -rf --tb=no -p no:xdist -p no:cacheprovider"`
regression: round-6#1
```

Why it matters: the unit is `Test_in_corpus::test_refuses_a_path_one_guard_alone_refuses` (`tests/skills/test_passages.py:87`), which fix commit `16e94d923` named; `git log -S` finds no earlier commit holding the name. The frame's row (`frame/plan.md:61`) asks for "one parameter that guard alone refuses" per guard. The fix named the case after that phrase. So the defect came from the frame row's wording, which counts each side of an `or` as a guard that can refuse a path alone.

`in_corpus` refuses a path that is a `.md` and no edition only when both sides of `rel in TOP_FILES or rel.startswith(TOP_DIRS)` refuse it (`passages.py:60`). Five of the seven parameters are refused that way, by two guards at once. Executed: `rel in TOP_FILES` widened to `True` fails `[top-files]`, `[top-dirs-slash]`, `[top-dirs-not-tests]`, `[top-dirs-not-hooks]` and `[top-dirs-not-records]`, 5 failed and 14 passed. `rel.startswith(TOP_DIRS)` widened to `True` fails the same five. Only `[the-md-suffix]` and `[the-ko-exclusion]` are refused by one guard alone.

Round 8's close says the same of the comment. Claimed there: "Paths each refused by one guard of `in_corpus` alone" claims more than the case shows, since those paths fall outside both sides of the `or` at once. The fix rewrote the comment to "let through by widening one guard ... at one boundary", and the name directly under it kept the old reading. Two texts over one case now hold two readings of "refuses". The comment's reading is about widening, and the name's is the plain boolean one. Under the boolean reading the name is false for five parameters. A tidy that takes the name at its word would remove those five. That is the deletion round 7 traced to the comment's old count.

It is no `must`. No assertion is wrong: every parameter fails under its own boundary and no other (see the confirmation of round-8#1). The fix is a rename. The name is cited nowhere outside `seal/` but its own line (executed, `git grep -n one_guard_alone -- ':!seal'`), and the round records that cite it are history and stay as they are. A rename owes no red case.

```python
    def test_refuses_a_path_one_widened_boundary_alone_lets_through(self, rel):
        assert not passages.in_corpus(rel)
```

## Confirmations

```seal
confirms: round-8#1
```
What holds: the close `fixed 22d2fa3bc`. Claimed: the header now reads "Paths each let through by widening one guard of `in_corpus` at one boundary named here and by no other, one or more per guard", and each named boundary fails exactly its own parameter. Read: the diff `3a0342f23..113acbe19` over `tests/skills/test_passages.py` touches the comment at `:49-57` alone. No parameter, id or assertion changed. Each sentence was checked against a run in the scratch clone at `113acbe19`, one `bin/seal mutate` run per mutant over `tests/skills/test_passages.py` with `-rf` (executed):

- "Paths each let through by widening one guard ... at one boundary named here and by no other". The comment names seven boundaries, and each run below is 1 failed and 18 passed, its own id and no other. The suffix to `True` fails `[the-md-suffix]`. The edition exclusion to `True` fails `[the-ko-exclusion]`. Membership to every top-level path (`rel in TOP_FILES` to `"/" not in rel`) fails `[top-files]`. The prefix without its slash fails `[top-dirs-slash]`. `"tests/"`, `"hooks/"` and `"seal/"` added to `TOP_DIRS` fail `[top-dirs-not-tests]`, `[top-dirs-not-hooks]` and `[top-dirs-not-records]`. No path fails under two of them, so "and by no other" holds.
- "one or more per guard": the suffix, the edition exclusion and membership hold one path each, and the prefix holds four (read, `:61-75`).
- "so widening a guard at a boundary named here fails exactly that boundary's paths": holds for the seven runs above. `"lib/"` added to `TOP_DIRS`, a directory the paths do not name, survives with 19 passed. The inner comment at `:69-72` says so, since a directory these paths do not name fails none.
- "Membership in `TOP_FILES` and the `TOP_DIRS` prefix are the two sides of one `or`": read, `passages.py:60`.
- "a side widened to `True` lets through what the other side refuses": membership to `True` fails five, `[top-files]` and the four prefix ids. The prefix to `True` fails the same five. Each run was 5 failed and 14 passed.
- "membership to every top-level path, the prefix to its directory names without their slash and to a directory it does not list": these are the seven boundaries above.

One part of the close's account does not match the runs, and it is no finding, since it is the close's account and not the tree. Claimed: `SECURITY.md` and the three directory paths fall outside both sides of the `or` at once. Executed: `docs-old/notes.md` does too, since both `True` runs fail `[top-dirs-slash]`. The comment as written does not depend on that count.

```seal
confirms: none
```
What matched: the change as code. The unmutated module passes, 19 cases, exit 0 (executed). `uvx ruff check` and `uvx ruff format --check` over the file each exit 0 (executed). The judgment row at `frame/plan.md:63` bounds this round and decides how a wording finding closes. It cites `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* (read, the row).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `113acbe19`. This round ran one module and the changed file's lint, so the suite is `unverified`. Finding 1 is open, and its close comes before the broad run. | the branch at `113acbe19` | the orchestrator, at `seal gate` after the rounds settle |
| Whether finding 1 is closed `deferred seal/follow-up.md`, as the row at `frame/plan.md:63` sets for a wording finding, or renamed in a fix pass. A rename touches a test file, so it owes a verifying round under the section that row cites | `frame/plan.md:63` | the orchestrator |
| The case on the Windows leg | `tests/skills/test_passages.py:49-88` | the pull request's `.github/workflows/test.yml` run |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/settle/scripts/passages.py` over `bin/test tests/skills/test_passages.py -q -rf --tb=no -p no:xdist -p no:cacheprovider`, one run each: the suffix to `True`, the edition exclusion to `True`, `rel in TOP_FILES` to `"/" not in rel`, `TOP_DIRS` without slashes | each run red, 1 failed and 18 passed: `[the-md-suffix]`, `[the-ko-exclusion]`, `[top-files]`, `[top-dirs-slash]` in that order |
| the same command, one run each: `TOP_DIRS` plus `"tests/"`, plus `"hooks/"`, plus `"seal/"`, plus `"lib/"` | the first three red, 1 failed and 18 passed each: `[top-dirs-not-tests]`, `[top-dirs-not-hooks]`, `[top-dirs-not-records]`; `"lib/"` survived, 19 passed |
| the same command, one run each: `rel in TOP_FILES` to `True`, `rel.startswith(TOP_DIRS)` to `True` | each run red, 5 failed and 14 passed: `[top-files]`, `[top-dirs-slash]`, `[top-dirs-not-tests]`, `[top-dirs-not-hooks]`, `[top-dirs-not-records]` |
| `bin/test tests/skills/test_passages.py -q -p no:xdist -p no:cacheprovider`, unmutated | exit 0, 19 passed |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_passages.py` | exit 0 both |
| `git grep -n one_guard_alone -- ':!seal'` | one line, `tests/skills/test_passages.py:87` |
| `git log -S test_refuses_a_path_one_guard_alone_refuses -- tests/skills/test_passages.py` | one commit, `16e94d923` |
