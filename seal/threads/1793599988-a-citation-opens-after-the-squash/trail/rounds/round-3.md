# Review round 3: 1793599988-a-citation-opens-after-the-squash

```seal
target: 3e810200, fixes 6ca6bb52..3e810200
```

This is a verifying round. It reads the diff of round 2's fix pass,
34c55c1e to the test module and 3e810200 to round 2's record, against
round 2's one finding. The base is `origin/release/v0.29.0` at 40e6c23e,
and the branch's merge base with it is 40e6c23e (executed). The round
worked in a `git clone --no-local` of the branch worktree at 3e810200,
under `<scratchpad>/1270-round-3/clone`. It fetched the source's
`refs/remotes/origin/main` and `refs/remotes/origin/release/*` over the
clone's refs of those names. It then deleted the one stale reaching ref the
clone held from a local branch of the source,
`refs/remotes/origin/release/v0.28.0`. So the tree case judged with the
remote-tracking refs CI's checkout holds, and did not skip. Every mutant
was run through `seal mutate` from #898's unmerged fix: the `bin/seal` of
the worktree of `fix/898-a-mutant-that-does-not-compile-reads-as-caught`,
which now stands at f8532a37, not at the ef81822e the fix pass names. The
installed `seal` was not used. No `seal/parity.md` is declared, so the
round block has no `original:` line.

Carried from rounds 1 and 2 as coordinates, not as verdicts: the
`REACHING` tuple at `:38-43`, `assert_outlives` at `:147-154`, the way to
give a clone CI's shape of refs, and round 2's reading that
`agents/crafter.md:164` has a fix pass write no phase record. Every verdict
below was reached again in this round, against the three inputs the fix
pass listed and inside the fix diff.

## Findings

None. Round 2's one finding is answered under *Confirmations*.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the tree case's verdict now has one case for each of its three
inputs, and each case reads the outcome it expects. The fix adds
`verdict(root)` at `tests/text/test_a_cited_commit_outlives_the_squash.py:157-169`.
It runs `assert_outlives` and returns `("skipped", reason)` where a skip is
raised, `("failed", message)` where an `AssertionError` is raised, and
`("passed", "")` otherwise (read). The three inputs are these. Where no
reaching ref stands, `unreached` gives `None`, and S6 at `:302-304` asserts
`skipped` and the four patterns in the reason. Where refs stand and nothing
is refused, `unreached` gives `[]`, and S3 at `:252` asserts
`("passed", "")` over all four reaching-ref parameters. Where a citation is
refused, `unreached` gives a non-empty list, and S7 at `:312-315` asserts
`failed` and the message's five parts (read). Because `verdict` catches the
skip, none of the three cases can end as skipped. A verdict that skips in
the wrong state now turns its case red instead of skipped.

Round 2's evidence line was run again. `if found is None:` to
`if not found:` is red over the whole module (executed, *Probes* row 2,
mutant 1). The same mutant, planted by hand through the Edit tool, fails
all four S3 parameters on `assert ('skipped', ...) == ('passed', '')`. It
also makes the tree case skip on the clone's clean checkout, the false
message round 2's finding named (executed, *Probes* row 4). The fix pass
claimed thirteen mutants red as one batch over the module. The round
planted the same thirteen and got 13 red and 0 SURVIVED (executed,
*Probes* row 2). The fix pass also claimed each mutant red against the case
of its outcome alone. The round ran each group against its case alone.
Against S3 alone, `if not found:`, `assert found, refusal(found)` and the
four `REACHING` deletions gave 6 red of 6. Against S6 alone, `if False:`,
`return`, `pytest.skip("")` and `assert False, NO_REF` gave 4 red of 4.
Against S7 alone, `if not refs:` to `if refs:`, `assert not found` and
`pass` gave 3 red of 3 (executed, *Probes* row 3). Each batch's baseline
passed, and each red was exit 1, so each red is a failed case and not an
empty selection. Round 2's fourth confirmation block found that `if refs:`
left S7 skipped. That mutant now fails S7 instead.

The fix pass departed from round 2's paste-ready `try`/`pytest.fail` in S3
and gave its grounds: one helper reads all three outcomes alike. The
grounds hold. The helper also closes the S7 skip that the paste-ready text
left open. The repository's other cases catch `pytest.skip.Exception`
inline, as in
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:480-486` and
`tests/test_conftest.py:268-271`, and none of them offers a helper this
module could import instead (executed: `git grep` for `skip.Exception`
under `tests/`). A mutation score licenses *tested*, never *safe*: these
reds say each outcome is read by a case, not that the verdict is right in a
state no case plants.

```seal
confirms: none
```
What matched: the close's account of the other statements of the skip and
the outcomes. `frame/design.md:49` (*Scope* item 3), `frame/design.md:73`
(S6) and `frame/plan.md:61` still describe the code as it stands (read).
`git grep` for `assert_outlives`, `pytest.raises`, `both refs` and
`verdict` across the work item outside `trail/rounds/` lists only
`frame/design.md:16`, `frame/plan.md:39` and `trail/phases/phase-1.md:99`
(executed). The first two are unrelated uses of the word "verdict". The
third is mutation row 10, which round 2's first confirmation block already
judged as history true at 44b215bc. The sentence at
`trail/phases/phase-1.md:56-60`, that S7 asserts the module's own
constants, still holds: S7 now reads them from `verdict`'s message
(read). The close names these three phase-record coordinates as corrected
by the round records. `agents/crafter.md:164` still says a fix pass writes
no phase record (read), so leaving them is the policy. No finding.

```seal
confirms: none
```
What matched: the fix pass's narrow run and lint. The phase-boundary set,
the thirteen modules `trail/phases/phase-1.md:131-147` lists, gives 349
passed with nothing skipped (executed, exit 0). That count is the same as
round 2's, since the fix adds no case and no parameter. `uvx ruff check`
and `uvx ruff format --check` on the module exit 0 (executed). The diff
adds no test function. It changes the last assertions of S3, S6 and S7 and
adds a helper that pytest does not collect, so no new test repeats another
case. 3e810200 adds only the close block to round 2's record, five lines,
and changes no line of the proofer's (executed: `git diff
6ca6bb52..3e810200`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The `unverified` label in `gaps.md:7` is honest: no agent ran them. This round leaves nothing open, so what comes due is the orchestrator's broad run and the sealer's spawn after it | `gaps.md:7` | the orchestrator, by `seal gate` once the rounds settle |
| *Scope* item 6 and `frame/questions.md` Q1, carried from rounds 1 and 2 and outside the fix diff. The merge base with `origin/release/v0.29.0` is still 40e6c23e, so nothing of the release branch is left to merge in today | `frame/design.md:52` | the orchestrator at any later merge of the release branch, and the round that reads that merge's diff |
| The module on the Windows leg | `gaps.md:10` | CI's Windows leg on the pull request |

## Probes

| Command | Result |
|---|---|
| `git fetch` of the source's `refs/remotes/origin/main` and `refs/remotes/origin/release/*` into the clone, the stale `refs/remotes/origin/release/v0.28.0` deleted, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -rfEs -q -p no:xdist` | 21 passed, nothing skipped, exit 0 |
| #898's `seal mutate` at f8532a37 on the module with 13 mutants: `if found is None:` to `if not found:` and to `if False:`; `if not refs:` to `if refs:`; `pytest.skip(NO_REF)` to `return`, to `pytest.skip("")` and to `assert False, NO_REF`; `assert not found, refusal(found)` to `assert not found`, to `pass` and to `assert found, refusal(found)`; each `REACHING` line deleted, `refs/heads/main` with its next line as context; cases `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist` | baseline passed; 13 mutants, 13 red, 0 SURVIVED, exit 0 |
| The same `seal mutate` per case: `if not found:`, `assert found, refusal(found)` and the four `REACHING` deletions with `-k squash_is_accepted`; `if False:`, `return`, `pytest.skip("")` and `assert False, NO_REF` with `-k no_reaching_ref`; `if refs:`, `assert not found` and `pass` with `-k refusal_says` | each baseline passed; 6 red of 6, 4 red of 4, 3 red of 3, each red exit 1 |
| `if found is None:` changed to `if not found:` in the clone through the Edit tool, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist -rfEs`, then the line restored through the Edit tool | 4 failed, 7 passed, 1 skipped, exit 1: all four S3 parameters fail on `('skipped', ...) == ('passed', '')`, and the tree case skips at `:153` with `NO_REF` |
| `bin/test` over the thirteen modules of `trail/phases/phase-1.md:131-147` with `-rfEs -q`, then `uvx ruff check` and `uvx ruff format --check` on the module | 349 passed, exit 0; ruff exit 0 both |

Every probe ran in the clone. `git status` was clean after the restore in
row 4. The clone and everything in it, its `.venv`, the fetched refs and
the run logs beside it are deleted before the hand-back. Nothing was
written in the branch worktree but this record.
