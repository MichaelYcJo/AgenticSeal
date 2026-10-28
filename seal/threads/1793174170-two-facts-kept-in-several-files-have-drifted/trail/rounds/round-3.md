# Review round 3: 1793174170-two-facts-kept-in-several-files-have-drifted

target: 143f80b0, fixes 930665ec..143f80b0

## Findings

### 1. One deleted edition skips the outline comparison of every pair still on disk

severity: should
location: `tests/behaviour/test_both_editions_carry_the_same_folds.py:86-100`
evidence: executed `sed -n 56,110p tests/behaviour/test_both_editions_carry_the_same_folds.py`, `sed -n 100,160p tests/behaviour/test_no_document_names_the_old_roots.py`, `git grep -n "pairs()" -- tests | grep -v "def pairs"`
verdict: fixed c81cb9ff
regression: round-2
answer: The finding holds: `d91641fb` declined the whole case over any deleted half, sweep included. The outline case now compares every pair on disk first. The record's `unread()` then declines only where every unread named pair is explained by a deleted half of it, as `test_no_document_names_the_old_roots.py#uncovered` does. The record's `build_tracked_tree` case was added. Run against the old listing logic, it failed with exit 1 (`assert [] == ['README.md']`), and the module then passed, 7 cases, exit 0. Two mutants survived that case, so `27b8deee` strengthened it. The first made the decline unconditional (`if missing:`): a skip raised inside the case skipped it, which counts as a pass. The second returned every deleted file as missing. The case now fails where `unread()` declines instead of reporting, covers one named pair lost and the other absent, and deletes a file that has no edition. Both mutants then went `red` with exit 0, and so did removing the decline call and emptying `unread()`'s report. `git grep` found no other statement of the walk's scope to correct, outside the 0.14.0 changelog, which is history.

The unit is `test_every_paired_document_carries_the_same_headings`, which
`d91641fb` changed. `frame/plan.md` phase 5 and `frame/design.md` S11 say each
tracked pair is compared, the README pair and a `docs/experiments/` pair among
them. The fix calls `decline_if_shrunken(missing, ...)` on the case's first
line, before any comparison runs, so a tree missing any one tracked
`.ko.md` skips the outline check of every other pair. The defect came from
applying the census's decline to the whole case, where the census's own
precedent applies it to the liveness half alone.

The case does two things. It sweeps every pair on disk for an outline
disagreement, and it asserts two named pairs alive. Only the liveness half is
what `tests/conftest.py#on_disk` says must decline: "A case that reads the
corpus to prove an entry is still ALIVE". A sweep "judges what remains and
ignores it". As written, deleting `docs/one-root-by-lifetime.ko.md` mid-edit
skips the README pair's outline comparison too, and the case reports a skip
where it should report a disagreement. `tests/behaviour/test_no_document_names_the_old_roots.py#uncovered`
names this failure and guards against it. It declines only where every
absent named path is among the missing ones, because "declining over a
neighbour that is merely mid-edit would report it nowhere — the decline
carrying a finding away with it".

No case exercises the decline. `pairs()` has one caller, this case (executed,
the `git grep` above), and it always reads the real tree. The crafter
reports that the mutant removing the call SURVIVED. Every other caller of
`decline_if_shrunken` in this suite is pinned with `build_tracked_tree`
(`tests/behaviour/test_no_document_names_the_old_roots.py:209-260`). This fix
should come with such a case, and it needs `pairs()` to take a root, which
finding 2's fix gives it.

Add `import pytest`, and import `build_tracked_tree` from `conftest`. Then
replace the outline case with:

```python
# The pairs the walk must reach (#1055 S11).
ALIVE = ("README", "docs/experiments/README")


def unread(names, missing):
    """The ALIVE pairs the walk did not read, or `pytest.skip` when every one
    of them is unread only because the working tree deleted one of its halves.

    Conditional, as `test_no_document_names_the_old_roots.py#uncovered` is: a
    decline over a neighbour that is merely mid-edit would carry a real
    finding away with it."""
    absent = [n for n in ALIVE if n not in names]
    halves = {h: n for n in absent for h in (n + ".md", n + ".ko.md")}
    explained = {halves[m] for m in missing if m in halves}
    if absent and set(absent) == explained:
        decline_if_shrunken(
            sorted(m for m in missing if m in halves), "the edition pairs"
        )
    return [n for n in absent if n not in explained]


def test_every_paired_document_carries_the_same_headings():
    """A1, A2. The walk reads at least one pair, so a broken listing cannot
    pass on an empty walk. Every pair on disk is judged before anything
    declines, so a deleted edition takes no other pair's finding with it."""
    names, missing = pairs()
    assert names, "no X.ko.md beside an X.md was read"
    found = []
    for name in names:
        found += disagreements(name, read(name + ".md"), read(name + ".ko.md"))
    assert not found, "\n".join(found)
    # #1055 S11: the pairs outside top-level `docs/` are read too.
    gone = unread(names, missing)
    assert not gone, f"not read: {gone}"


def test_a_deleted_half_of_a_named_pair_declines_and_nothing_else_does(tmp_path):
    """The liveness half declines only over a named pair the working tree
    deleted a half of, and reports one that is simply not there."""
    root = build_tracked_tree(
        tmp_path,
        {
            "README.md": "# A\n",
            "README.ko.md": "# A\n",
            "docs/experiments/README.md": "# B\n",
            "docs/experiments/README.ko.md": "# B\n",
        },
        deleted=("README.md",),
    )
    names, missing = pairs(root)
    assert names == ["docs/experiments/README"], names
    assert missing == ["README.md"], missing
    with pytest.raises(pytest.skip.Exception):
        unread(names, missing)
    assert unread(names, []) == ["README"]
```

### 2. A deleted English edition drops its pair without a word

severity: should
location: `tests/behaviour/test_both_editions_carry_the_same_folds.py:59-73`
evidence: read `tests/behaviour/test_both_editions_carry_the_same_folds.py:59-73`, `tests/conftest.py:266-285`
verdict: fixed c81cb9ff
answer: The finding holds. `pairs(root)` is now the record's text: it lists `*.md` once, runs `on_disk` over the whole listing, and returns each tracked half of a pair the working tree deleted, English halves included. The scope still makes one listing call, and the census module passed, 9 cases, exit 0. With `README.md` deleted in a `build_tracked_tree` repository, the old logic returned no missing half (red, exit 1). The new one returns `["README.md"]`, and with `docs/alone.md` also deleted it still returns `["README.md"]`. A mutant listing `*.ko.md` alone went `red`, exit 0, and so did one returning every deleted file.

`pairs()` lists only `*.ko.md` from git and runs `on_disk` over that list.
It finds the English half with `os.path.isfile`. A tracked `X.md` that the
working tree has deleted is therefore not in `missing`: the pair just drops
out of `names`. For the README pair or `docs/experiments/README`, the case
then fails with "README.ko.md beside README.md was not read". That is the
false alarm `tests/conftest.py#on_disk` says a liveness case must decline
over: "to it a skipped file and a deleted entry are the same evidence". For
the other two pairs, their outline goes unjudged and the case says nothing.

The census in `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`
cannot see this half, because the half is not a git listing. `d91641fb`
guarded the Korean half of the pair and left the English half as it was.
Contract rule 12 asks for the whole class. Phase 5 wrote the `isfile`
check, not this range, so this finding carries no `regression:` line.

Listing `*.md` once covers both halves. The scope still makes one listing
call, so the census's `APPLIES_THE_SHARED_GUARD` count of 1 stays true.
Replace `pairs()` with:

```python
def pairs(root=ROOT):
    """`(names, missing)`: every tracked `X.ko.md` whose tracked `X.md` stands
    beside it, both on disk, as repository-relative names without the
    extension; and each tracked half of such a pair the working tree has
    deleted. The listing is git's, so an untracked file is no pair, and
    `on_disk` keeps a deleted half from ending the walk at its `open` (#432)."""
    listed = git_listing(root, "ls-files", "--", "*.md")
    present, gone = on_disk(root, listed)
    present = set(present)
    korean = sorted(n for n in listed if n.endswith(".ko.md"))
    english = {k: k[: -len(".ko.md")] + ".md" for k in korean}
    names = [k[: -len(".ko.md")] for k in korean if {k, english[k]} <= present]
    halves = set(korean) | set(english.values())
    return names, sorted(n for n in gone if n in halves)
```

The census row's comment, "It returns the missing half, and its caller
asserts two pairs alive", stays true after both fixes. `read` still joins
under `ROOT`, which is what the outline case reads.

## Confirmations

confirms: none
The census row `d91641fb` added is right as it stands. `pairs()` makes one call that lists paths from git and mentions `on_disk`, which is what table 1 of `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` reads, and the row's count is 1 (read, `:89-96`). The census module, the editions module and the modules that name either passed in this round's run (executed). The two cases the broad gate failed at `930665ec` are among them.

confirms: none
The `gaps.md` row `143f80b0` added says what happened. The broad gate at `930665ec` failed two cases of the census. The census reads every test module, so a `git grep` on the changed paths did not name it, and round 1's and round 2's runs missed it the same way. The fix is `d91641fb`. Its grounds quote the census and `on_disk` correctly (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck after the fix of the two findings above. The gate run at `930665ec` was spent by `d91641fb` | the whole tree | the orchestrator, through `seal gate` (contract rule 2) |
| The crafter's two red mutants and the surviving one. This round reasoned from the code and the census, and re-ran none of them | `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` | the sealer, which samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/test_conftest.py tests/hooks/test_root_migrate.py tests/skills/test_seal.py -q -p no:cacheprovider`, the two modules and every module `git grep -l` finds naming either | 529 passed, exit 0 |
| `bin/seal layout --check` | exit 0, 158 files read, 0 refused |
| `bin/test tests/behaviour/test_tmp_round3_pairs.py -q -p no:cacheprovider -p no:xdist`, a probe holding the two findings' `pairs()` and `unread` as written above. It had one case on the real tree, expecting all four pairs and no missing half, and one on a `build_tracked_tree` repository with `README.md` deleted | 2 passed, exit 0. The probe file and its bytecode were deleted after the run |
