# Review round 2: 1793599988-a-citation-opens-after-the-squash

```seal
target: 93f8a855, fixes 2f07db72..93f8a855
```

This is a verifying round. It reads the diff of round 1's fix pass,
b01ec5b1 to the test module and 93f8a855 to round 1's record, against
round 1's two findings. The base is `origin/release/v0.29.0`, which stands
at 40e6c23e, the commit `release/v0.28.1` stood at. The branch's merge base
with it is 40e6c23e (executed). The round worked in a `git clone --no-local`
of the branch worktree at 93f8a855, under `<scratchpad>/1270-round-2/clone`.
It fetched the source's `refs/remotes/origin/main` and
`refs/remotes/origin/release/*` over the clone's own `refs/remotes/origin/*`
of those names. It then deleted the one stale reaching ref the clone held
from a local branch of the source, `refs/remotes/origin/release/v0.28.0`.
So the tree case judged with the remote-tracking refs CI's checkout holds,
and did not skip. Every mutant was run through `seal mutate` from #898's
unmerged fix: the `bin/seal` of the worktree of
`fix/898-a-mutant-that-does-not-compile-reads-as-caught` at ef81822e. That
copy refuses a mutant that does not compile. The installed `seal` was not
used. No `seal/parity.md` is declared, so the round block has no
`original:` line.

Carried from round 1 as coordinates, not as verdicts: the `REACHING` tuple
at `:38-43`, S3 (now at `:218-235`), the skip (now in `assert_outlives` at
`:151-153`), and the way to give a clone CI's shape of refs. Every verdict
below was reached again in this round.

## Findings

### 1. The tree case's skip is pinned on one side only: a verdict that skips where reaching refs stand and nothing is refused stays green

```seal
severity: should
location: `tests/text/test_a_cited_commit_outlives_the_squash.py:151-153`, `tests/text/test_a_cited_commit_outlives_the_squash.py:218-235`
evidence: executed `seal mutate tests/text/test_a_cited_commit_outlives_the_squash.py --tests "bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist" --replace '    if found is None:' '    if not found:'`
reopens: round-1#2
```

Why it matters: round 1's close of finding 2 claims the class is whole. It
says the class "was listed by taking the tree case apart into its three
parts, the `unreached` call, the skip and the failure's message; each now
has a case". The skip has two sides, and only one of them has a case. The
first side is that `assert_outlives` skips where no reaching ref stands.
S6 at `:276-287` pins that side. The second side is that it does not skip
where reaching refs stand and no citation is refused. No case pins it.
`if found is None:` at `:152` tells `None`, the state where nothing was
judged, apart from `[]`, the state where everything was judged and passed.
Replacing it with `if not found:` leaves the module green (executed,
SURVIVED, the eighth mutant of *Probes* row 2). S3 at `:218-235` builds
exactly the second state, but it calls `unreached` and never
`assert_outlives`. S6 and S7 are the only cases that call the verdict.
They plant a repository with no reaching ref and one with a refused
citation.

Under that mutant, the tree case skips on every clean checkout that holds
`main` and release refs (read: `found` is `[]`, so `not found` holds). The
skip's reason then tells the person "no ref matching ... stands in this
checkout, so no `<commit>:<path>` citation was judged", which is false. S1
(`frame/design.md:68`) asks that the tree case passes there, and a skip is
not a pass. The check still fails where a citation is refused, so the gate
keeps refusing. What breaks is what it tells a person on a green tree. By
contract rule 12, a list made by taking the artefact apart has to take
apart each part's condition as well as the part. The close handed back a
sample as a whole list. Its fixes of the `return` and the empty-reason
mutants hold (*Confirmations*, second block).

The fix runs the verdict in S3, where one ref of each pattern reaches the
cited commit, and turns a skip into a failure. `pytest.raises` cannot say
"raises nothing", and an uncaught skip would report S3 as skipped, not
failed. So the case catches the skip itself. With this change, the
`if not found:` mutant turns all four S3 parameters red (executed: the
same body in a `test_tmp_*` probe beside the module, *Probes* row 4). It
has no OS-boundary precondition.

```python
def test_a_citation_of_the_squash_is_accepted(tmp_path, ref):
    """S3: a commit that one ref of each pattern in `REACHING` contains, the
    other bases standing at its parent, is named nowhere, and the tree
    case's verdict passes rather than skipping. CI's checkout holds only the
    remote-tracking refs, and an open release branch's squash is reached
    there through `refs/remotes/*/release/*` alone."""
    root, commit = planted(tmp_path, reach=(ref,))
    cite(root, {"docs/a.md": citing(commit)})
    assert cited(root) == [("docs/a.md", 2, commit[:8])]
    assert unreached(root) == []
    try:
        assert_outlives(root)
    except pytest.skip.Exception as skipped:
        pytest.fail(f"the tree case judged nothing where {ref} stands: {skipped}")
```

```seal
verdict: fixed 34c55c1e
answer: The finding holds, and round 1's close of finding 2 handed back a sample as a whole list: it took the tree case apart into its parts and not into each part's condition. This time the list was made from the verdict's inputs. `assert_outlives` answers three: no reaching ref (`unreached` gives `None`), which must skip with `NO_REF`; reaching refs and no refused citation (`[]`), which must pass, neither skipping nor failing; and reaching refs with a refused citation (a non-empty list), which must fail with `refusal(found)`. Each outcome is now read by one case through a new helper, `verdict(root)`, which runs `assert_outlives` and returns `("skipped", reason)`, `("passed", "")` or `("failed", message)`: S6 asserts the first, S3 the second over all four reaching-ref parameters, and S7 the third. The fix is written in my own words rather than the paste-ready `try`/`pytest.fail` in S3, because one helper reads all three outcomes alike. It also closes the edge this round's *Confirmations* fourth block left: S7's `pytest.raises(AssertionError)` let a skip through, so `if not refs:` to `if refs:` skipped S7, and now fails it. Seen red through #898's `seal mutate` at ef81822e, each mutant alone against the case of its outcome (executed, exit 0 each, no case skipped): `if found is None:` to `if not found:` turns all four S3 parameters red; to `if False:` turns S6 red; `if not refs:` to `if refs:` turns S7 red; `pytest.skip(NO_REF)` to `return`, to `pytest.skip("")` and to `assert False, NO_REF` each turn S6 red; `assert not found, refusal(found)` to `assert not found` and to `pass` each turn S7 red, and to `assert found, refusal(found)` turns all four S3 parameters red. Those nine and round 1's four `REACHING` deletions, run as one batch over the whole module, gave 13 red and 0 SURVIVED (executed, exit 0). Round 1's close claimed that no other file states the old two-ref parametrisation, and that claim was wrong: its `git grep` missed `trail/phases/phase-1.md:99`, mutation row 10, which reads "both refs" and holds only at 44b215bc. That row, and `trail/phases/phase-1.md:49-51` and `:56-60`, stand as the phase record wrote them, because a fix pass writes no phase record; this answer and round 1's are their correction. The other statements of the skip, `frame/design.md:49` and `:73` and `frame/plan.md:61`, still hold (executed: `git grep` for `skip`, `both refs`, `pytest.raises` and `assert_outlives` across the work item outside `trail/rounds/`).
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: S3 at `:218-235` is parametrised over `refs/heads/main`,
`refs/heads/release/v9.9.9`, `refs/remotes/origin/main` and
`refs/remotes/origin/release/v9.9.9`, one ref of each `REACHING` pattern
(read). The fix pass claimed that deleting each `REACHING` line turns S3
red. The round ran round 1's evidence line again: deleting
`refs/remotes/*/release/*` and deleting `refs/heads/main` over the whole
module are both red, and so is each of the other two deletions (executed,
*Probes* row 2, mutants 1 to 4). The same four mutants run against S3 alone
with `-k squash_is_accepted` are 4 red (executed, *Probes* row 3). The
`refs/heads/main` deletion was written with its next line as context,
because `    "refs/heads/main",` now also occurs inside S3's list. The fix
pass also claimed that each mutant fails exactly the S3 parameter of its
pattern. That was not executed, because `seal mutate`'s batch mode prints
no case names. Read: `planted` points the base refs at the parent and moves
only the named ref, so each deletion takes away one parameter's only
reaching ref and no other's. The phase record's sentence at
`trail/phases/phase-1.md:49-51` and its mutation row 10 at `:99` ("both
refs") still state the two-ref parametrisation. `agents/crafter.md:164`
says a fix pass "writes no phase record", so leaving them is the policy.
Row 10 is true at 44b215bc, the commit the phase record names. The close
claims "No other file states the old parametrisation", and its `git grep`
did not find `:99`, because that row contains none of the three words the
grep searched for. The claim is inexact, and the record it names is history
that nothing copies: `skills/code-review/scripts/pr_body.py:11-12` copies a
phase record's path, not its text (read). No finding.

```seal
confirms: none
```
What matched: the rest of the fix pass's claims for finding 2 and the
third member it added. The `return` and the `pytest.skip("")` mutants of
`:153` are red over the whole module and against S6 alone. The
`assert not found` mutant of `:154` is red over the whole module and
against S7 alone (executed, *Probes* rows 2 and 3). S6 at `:285-287`
catches `pytest.skip.Exception`, a `BaseException` that `pytest.raises`
accepts. It reads the reason through `str()`, which gives the skip's
message, so the empty-reason mutant fails there (executed). Under pytest's
assertion rewriting, S7's `AssertionError` holds `refusal(found)` ahead of
the rewritten explanation. The bare `assert not found` explanation holds the
repr of `found`, which has neither `docs/a.md:2` nor `REPAIR`. That is why
the mutant is red (executed). The fix pass departed from round 1's
paste-ready text and gave two grounds. One is that no module global is
patched. The other is that the shape is the sibling reader's. Both hold:
`tests/behaviour/test_a_cited_section_stands_in_its_file.py:228-245`
defines `assert_resolved`, and its tree case at `:255` and planted cases at
`:553` and `:605` all call it (read). A paste-ready fix is the proofer's
claim, not the fix, so the departure needs only grounds, and these are
enough.

```seal
confirms: none
```
What matched: *Scope* item 3 (`frame/design.md:49`) on the code as moved.
With CI's shape of refs, the tree case passes. With every reaching ref
deleted from the clone, it skips. `-rs` prints
`tests/text/test_a_cited_commit_outlives_the_squash.py:153` and the reason
naming all four patterns (executed, *Probes* rows 1 and 5). The skip's
line now falls inside `assert_outlives`, in the same file as before.

```seal
confirms: none
```
What matched: S7's `pytest.raises(AssertionError)` does not catch a skip.
When the reaching refs come back empty, S7 reports itself skipped, not
failed: the `if not refs:` to `if refs:` mutant SURVIVED against S7 alone
(executed, *Probes* row 3). Over the whole module, the same mutant is red,
with 10 failed and 2 skipped, the two being S7 and the tree case
(executed, *Probes* row 4). S2 to S6 own that branch, so S7 skipping there
leaves nothing unpinned. No finding.

```seal
confirms: none
```
What matched: the fix pass's narrow run and lint. The phase-boundary set,
the thirteen modules `trail/phases/phase-1.md:131-147` lists, gives 349
passed with nothing skipped, which is the phase's 347 plus S3's two new
parameters (executed, exit 0). `uvx ruff check` and `uvx ruff format
--check` on the module exit 0 (executed). Each new test was read against
its group. S3's two new parameters each cover a pattern that no other case
reaches alone, and S6 and S7 now cover the verdict instead of the module's
constants, so none of them repeats another case. 93f8a855 adds only the
two close blocks to round 1's record, ten lines, and changes no line of
the proofer's (executed: `git diff 2f07db72..93f8a855`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The `unverified` label in `gaps.md:7` is honest: no agent ran them | `gaps.md:7` | the orchestrator, by `seal gate` once the rounds settle |
| *Scope* item 6 and `frame/questions.md` Q1, carried from round 1's *Not judged* and outside the fix diff. The branch's merge base with `origin/release/v0.29.0` is that branch's head, 40e6c23e, so nothing of the release branch is left to merge in today | `frame/design.md:52` | the orchestrator at any later merge of the release branch, and the round that reads that merge's diff |
| The module on the Windows leg | `gaps.md:10` | CI's Windows leg on the pull request |

## Probes

| Command | Result |
|---|---|
| `git fetch` of the source's `refs/remotes/origin/main` and `refs/remotes/origin/release/*` into the clone, the stale `refs/remotes/origin/release/v0.28.0` deleted, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -rfEs -q -p no:xdist` | 21 passed, nothing skipped, exit 0 |
| #898's `seal mutate` on the module with 8 mutants: each `REACHING` line deleted (4), `pytest.skip(NO_REF)` to `return` and to `pytest.skip("")`, `assert not found, refusal(found)` to `assert not found`, and `if found is None:` to `if not found:`; cases `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist` | baseline passed; 8 mutants, 7 red, 1 SURVIVED: `if not found:` |
| The same `seal mutate` per case: the four `REACHING` deletions with `-k squash_is_accepted`; the `return` and empty-reason mutants with `-k no_reaching_ref`; `assert not found` and `if not refs:` to `if refs:` with `-k refusal_says` | 4 red of 4; 2 red of 2; 1 red, 1 SURVIVED (`if refs:`, S7 skipped) |
| A probe `tests/text/test_tmp_round2.py` written through the Write tool, holding finding 1's S3 body; run at HEAD, then `seal mutate` with `if not found:` against it alone; then `seal mutate` with `if refs:` over the whole module | 4 passed; red, all four parameters failing on `pytest.fail`; red, 10 failed and 2 skipped |
| Every reaching ref deleted from the clone, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist -k every_cited -rs`, then the refs fetched back | 1 skipped, exit 0, reason at `:153` naming the four patterns |
| `bin/test` over the thirteen modules of `trail/phases/phase-1.md:131-147` with `-rfEs -q`, then `uvx ruff check` and `uvx ruff format --check` on the module | 349 passed, exit 0; ruff exit 0 both |

The probe file was deleted before the narrow run of row 6. Every probe ran
in the clone, and the clone and everything in it are deleted before the
hand-back, its `.venv`, the fetched refs and the run logs beside it
included. Nothing was written in the branch worktree but this record.
