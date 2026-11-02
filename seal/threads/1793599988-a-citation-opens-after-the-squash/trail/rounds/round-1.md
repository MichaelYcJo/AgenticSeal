# Review round 1: 1793599988-a-citation-opens-after-the-squash

```seal
target: abe53cce against release/v0.28.1
```

The round read the branch against `origin/release/v0.28.1` (40e6c23e), in a
`git clone --no-local` of the branch worktree checked out at abe53cce, under
`<scratchpad>/1270-round-1/clone`. Such a clone carries the source's local
branches as `refs/remotes/origin/*`, so its `origin/main` was the source's
stale local `main` (57d6665b). The round fetched the source's
`refs/remotes/origin/main` and `refs/remotes/origin/release/*` into the
clone as `refs/remotes/src/*`, then deleted the stale `origin/*` refs, so
the tree case ran with remote-tracking `main` and `release/*` refs alone, as
CI's checkout holds them. Every mutant below was run through `seal mutate`
from #898's unmerged fix, the `bin/seal` of the worktree of
`fix/898-a-mutant-that-does-not-compile-reads-as-caught` at 95e7dea7, which
refuses a mutant that does not compile. The installed `seal` was not used.
This is round 1, so no earlier round's coordinates were carried. No
`seal/parity.md` is declared, so the round block has no `original:` line.

## Findings

### 1. Two of the four reaching-ref patterns are pinned by no case, and one of them is the ref CI reaches a release branch's squash by

```seal
severity: should
location: `tests/text/test_a_cited_commit_outlives_the_squash.py:211-220`, `tests/text/test_a_cited_commit_outlives_the_squash.py:38-43`
evidence: executed `seal mutate tests/text/test_a_cited_commit_outlives_the_squash.py --tests "bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist" --replace '    "refs/remotes/*/release/*",' '' --replace '    "refs/heads/main",' ''`
```

Why it matters: `REACHING` at `:38-43` names four patterns, and *Scope*
item 1 of `frame/design.md:47` makes each of them a reaching ref. Deleting
the `refs/remotes/*/release/*` line leaves the module green, and so does
deleting the `refs/heads/main` line (executed, both SURVIVED). S3 at
`:211-220` is parametrised over `refs/heads/release/v9.9.9` and
`refs/remotes/origin/main` only. S5 at `:252-258` points both local refs at
the cited commit, so either one alone carries it.

The unpinned remote pattern is the one the check needs most. CI's checkout
holds no local branch, and `frame/design.md:23` (G9) rests on its
remote-tracking refs. A squash that sits on the open release branch and is
not yet on `main` is reachable there only through
`refs/remotes/origin/release/*`. That is the case *Scope* item 6 owes, a
citation of a sibling 0.28.1 work item's squash. A later edit that drops or
misspells the pattern would make every such citation red on CI and green on
a contributor's machine, which holds a local `release/*` head. No case would
say why. The phase record claims that S3 "covers the local refs a
contributor has and the remote-tracking refs CI's checkout has"
(`trail/phases/phase-1.md:49-51`). `:211-213` covers one remote-tracking
ref, and that one is not the release ref.

The fix parametrises S3 over one ref of each pattern. `planted`'s default
`BASES` already points `refs/heads/main` and `refs/heads/release/v9.9.9` at
the first commit, and `reach` moves only the named ref to the second, so in
each run exactly one ref contains the cited commit. With this change both
surviving mutants turn red (executed, in the clone; *Probes* row 5).

```python
@pytest.mark.parametrize(
    "ref",
    [
        "refs/heads/main",
        "refs/heads/release/v9.9.9",
        "refs/remotes/origin/main",
        "refs/remotes/origin/release/v9.9.9",
    ],
)
def test_a_citation_of_the_squash_is_accepted(tmp_path, ref):
```

### 2. The tree case's skip, Scope item 3, is pinned by no case: a tree case that returns without skipping stays green

```seal
severity: should
location: `tests/text/test_a_cited_commit_outlives_the_squash.py:261-270`, `tests/text/test_a_cited_commit_outlives_the_squash.py:151-153`
evidence: executed `seal mutate tests/text/test_a_cited_commit_outlives_the_squash.py --tests "bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist" --replace '        pytest.skip(NO_REF)' '        return'`
```

Why it matters: *Scope* item 3 (`frame/design.md:49`) says that in a
checkout with no reaching ref "the tree case skips, and its reason names the
four patterns", and that the skip is printed under `-rfEs`. S6
(`frame/design.md:73`) asks for "the tree case's skip reason names the four
patterns". The case at `:261-270` claims this in its docstring. Its last
assertion, `all(pattern in NO_REF for pattern in REACHING)`, reads two
module constants and never runs the tree case. Replacing `pytest.skip(NO_REF)`
at `:153` with `return` leaves the module green (executed, SURVIVED). A
checkout with no `main` or release ref would then pass the tree case
silently, the outcome item 3 rules out. Replacing it with `pytest.skip("")`
also survives.

The fix runs the tree case against the planted repository and reads the
skip it raises. The tree case reads `ROOT` from its module's globals at
call time, so patching the module attribute reaches it. This needs
`import sys` beside `import subprocess`. With this change the `return`
mutant and the empty-reason mutant both turn red (executed, in the clone;
*Probes* row 5).

```python
def test_no_reaching_ref_judges_nothing(tmp_path, monkeypatch):
    """S6: with no `main` and no release ref, local or remote, a tag and a
    trunk branch notwithstanding, nothing is judged, and the tree case's
    skip names the four patterns."""
    root, commit = planted(
        tmp_path, bases=("refs/tags/v9.9.9", "refs/heads/trunk"), reach=()
    )
    cite(root, {"docs/a.md": citing(commit)})
    assert unreached(root) is None
    monkeypatch.setattr(sys.modules[__name__], "ROOT", root)
    with pytest.raises(pytest.skip.Exception) as skipped:
        test_every_cited_commit_outlives_the_squash()
    assert all(pattern in str(skipped.value) for pattern in REACHING)
```

## Confirmations

```seal
confirms: none
```
What matched: the crafter claimed the tree case failed before *Scope* item 5,
naming `design.md:18 cites 79252e48`, and passes at HEAD. The round reverted
row 18 of `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md`
to the base's citation in the clone and ran the module with `-p no:xdist`.
It failed with 1 failed and 9 passed, naming
`seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18 cites 79252e48`
(executed, exit 1). With the row restored, the module and
`tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` gave 19 passed
and nothing skipped (executed, exit 0).

```seal
confirms: none
```
What matched: the tree case on CI's shape of refs, and with none. With only
`refs/remotes/src/main` and `refs/remotes/src/release/*` standing, the tree
case passed (executed, exit 0). With those deleted as well, it skipped, and
`-rfEs` printed the reason naming all four patterns (executed, exit 0,
`1 skipped`). So *Scope* item 3 holds in the code at `:151-153` as built.
Finding 2 is that no case keeps it so.

```seal
confirms: none
```
What matched: *Scope* item 5 and G15 (`frame/design.md:29`). `79252e48` is
in neither the branch worktree's object store nor the clone's
(`git cat-file -t` exits 128). After fetching `refs/pull/1237/head` from the
GitHub remote into the clone, `79252e48` resolves as a commit, and
`git diff --quiet` of `trail/phases/phase-2.md` of
`seal/threads/1793490088-each-kind-of-restatement-is-measured/` between
`79252e48` and `48d035aa` exits 0. `48d035aa` is an ancestor of
`origin/release/v0.28.1` (`git merge-base --is-ancestor`, exit 0). The
corrected row at `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18`
keeps the bare `79252e48` the issue cited, as item 5 asks (read).

```seal
confirms: none
```
What matched: the crafter's mutants. Six of its ten were planted again
through #898's `seal mutate` over the planted cases: the containment test
inverted to `returncode != 0 or` (its 3), the `trail/` exclusion made
`False` (8), the `guarantee.md` exclusion deleted (7), the line count's
`+ 1` dropped (9), the commit taken as the whole token (10) and the
`evals/behaviour/` exclusion made `if False:` (6). All six were red, 6 of 6
(executed, exit 0). Mutants 1, 2, 4 and 5 were not planted again.

```seal
confirms: none
```
What matched: the `gaps.md:11` row the crafter handed to the proofer, the
eleventh mutant. Deleting `run.returncode == 0 and ` at `:124` SURVIVED
(executed). git 2.50.1 exits 129 for `for-each-ref --contains` on a missing
object, prints `malformed object name` on standard error and nothing on
standard output (executed), so the output half alone refuses it. The round
judges the mutant equivalent under git's behaviour. *Data & interfaces*
(`frame/design.md:86-89`) asks the build to read "the exit code and the
output", and `:124` reads both. Contract rule 13 leaves the exit-code half
unverified until a git that fails and still prints a ref is planted.
`gaps.md` labels it so and names its answerer, and that label is honest. No
finding.

```seal
confirms: none
```
What matched: the departure in `trail/phases/phase-1.md:19-27`. The new
row at `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:92-94`
classifies `cited` under `APPLIES_THE_SHARED_GUARD`. `cited` at `:81-99`
names `on_disk` and judges what it finds, so it skips the missing half, as
the sibling's `corpus` row does (read). That module passes with the row
(executed, in the 19-passed run).

```seal
confirms: none
```
What matched: compliance with the frame's interfaces and scope, read.
`COMMIT_PATH` is imported from `tests/censuses.py:1116` and not copied
(`:32`). The file selection at `:68-78` leaves out `evals/behaviour/`, a
work item's `trail/` subtree and its `guarantee.md`, and reads the rest of
`seal/threads/`, as *Scope* item 1 and S4 state. `reaching` makes one
`for-each-ref` call, and `unreached` makes one `--contains` call per
distinct commit (`:102-126`). The refusal at `:129-141` holds each
`file:line`, the commit, `REPAIR` and `FETCH`, the parts *Scope* item 2
lists. No file under `hooks/`, `skills/`, `agents/`, `templates/` or
`.github/` changes (`git diff --stat`, executed). `tests/censuses.py:1035`
holds a second regex of the form, `HISTORY_PATH`, which matches only
`seal/specs/` paths and so a subset of what `COMMIT_PATH` matches. The
module rightly imports the general one. The `from:` texts of the second and
third rule changes stand verbatim at `docs/one-root-by-lifetime.md:48-50`
and `docs/one-root-by-lifetime.ko.md:48-49`, under the sections they name
(read).

```seal
confirms: none
```
What matched: the quality axes the diff touches. Security: the only inputs
crossing a process boundary are git's output and a hex string the regex
admits, passed as list arguments with no shell (`:58-65`, `:118-123`).
Concurrency does not apply, since the module only reads. Error paths: a
root that is no repository raises from `git` with `check=True`, as the
sibling's `corpus` does. Each new test was read against its group. The
module's cases cover S2 to S7 once each, none covers what another already
does, and no module outside it covers the new reader. `bin/seal layout
--pairs` names no pair in the module (executed, exit 0).
`uvx ruff check` and `uvx ruff format --check` on the two changed modules
exit 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| *Scope* item 6 and `frame/questions.md` Q1: the tree case after `release/v0.28.1` is merged in, and the correction of any citation it refuses then. The branch was judged as it stands, as the spawn asked | `frame/design.md:52`, `frame/questions.md:15` | the orchestrator at that merge, and the round that reads the merge's diff |
| The full suite, the repository-wide lint and the typecheck. The crafter's `unverified` label in `gaps.md:7` is honest: no agent ran them | `gaps.md:7` | the orchestrator, by `seal gate` once the rounds settle |
| The module on the Windows leg | `gaps.md:10` | CI's Windows leg on the pull request |
| G1's and P2's counts at the seven release tags and at `569780ef`, which the weighing rests on. Carried as read, not run again | `frame/design.md:15`, `frame/design.md:36` | the sealer, where it samples the frame's claims |

## Probes

| Command | Result |
|---|---|
| `git fetch` of the source's `refs/remotes/origin/main` and `refs/remotes/origin/release/*` into the clone as `refs/remotes/src/*`, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -rfEs -q` | 19 passed, nothing skipped, exit 0 |
| Row 18 of `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md` reverted to the base's citation through the Edit tool, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -rfEs -q -p no:xdist`, then the row restored | 1 failed, 9 passed, exit 1, naming `design.md:18 cites 79252e48` |
| With the clone's stale `origin/*` refs deleted, `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -k every_cited -rfEs -q -p no:xdist`; then with `refs/remotes/src/*` deleted too, the same command | 1 passed, exit 0; then 1 skipped, exit 0, reason naming the four patterns |
| #898's `seal mutate` on the module with 6 mutants (eleventh mutant, `pytest.skip(NO_REF)` to `return`, and each of the four `REACHING` lines deleted), cases `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist` | 6 mutants, 2 red, 4 SURVIVED: the eleventh, the `return`, `refs/remotes/*/release/*` and `refs/heads/main`. The two red are the `refs/remotes/*/main` and `refs/heads/release/*` deletions |
| The fixes of findings 1 and 2 applied in the clone through the Edit tool, then #898's `seal mutate` with 4 mutants (`return`, `pytest.skip("")`, and the two surviving `REACHING` deletions), then `uvx ruff check` and `uvx ruff format --check` | baseline passed; 4 mutants, 4 red, 0 SURVIVED; ruff exit 0 both |
| #898's `seal mutate` with six of the crafter's mutants over the planted cases (`-k 'not every_cited'`) | 6 mutants, 6 red, 0 SURVIVED, exit 0 |
| `git fetch` of `refs/pull/1237/head` from the GitHub remote into the clone, then `git cat-file -t 79252e48`, `git diff --quiet` of the cited `phase-2.md` between `79252e48` and `48d035aa`, and `git merge-base --is-ancestor 48d035aa refs/remotes/src/release/v0.28.1` | `commit`; exit 0; exit 0 |
| `git for-each-ref --count=1 --format=%(refname) --contains deadbeef1234 refs/heads/` in the clone | exit 129, empty standard output, `malformed object name` on standard error |

Every probe ran in the clone, which was deleted before the hand-back with
everything in it, its `.venv` and the fetched refs included. The last row's
two output files landed one directory above the session's working
directory by a relative redirect, and were deleted once found. Nothing was
written in the branch worktree but this record.
