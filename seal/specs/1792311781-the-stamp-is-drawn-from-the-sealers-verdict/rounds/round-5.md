# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 5

target: 5943f1d7, fixes eb4303b4..5943f1d7

## Findings

### 1. A rebase of a sealed branch in a second clone, then a re-seal whose row lost its earlier run, draws the work item's stamp a second time

severity: should
location: `skills/verify/scripts/seal_stamp.py:1079`, `docs/the-review-record.md:286`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:772`
verdict: deferred the frame
regression: round-4#1

The unit is `seal_stamp.sealed_before`, whose loop condition a226da11
changed. The frame holds once per work item by the `Target SHA` row's earlier
run and the values file's name (`plan.md` B1), `spec.md` S7 says any earlier
run reading `sealed` queues nothing, and `questions.md` Q7's answer (a) says
the owner's rule forbids a second stamp and accepts a missing one as a gap
carried to #976; the fix counted an earlier `sealed` only where its audited
commit is an ancestor of that commit, which also drops a `sealed` whose
history was rewritten after it was stamped, so the defect came from the fix
(round 4's own paste-ready fix, applied as written), and the choice between
the two failures it trades is the frame's.

Why it matters. A rebase rewrites the sealing commit. The rewritten commit
still reads `sealed`, but its `Target SHA` names the pre-rebase commit, which
is no longer in its history. At eb4303b4 `sealed_before` took any earlier
`sealed` as the stamp's trace, so a second clone that rebased the branch and
then committed a re-seal row written fresh queued nothing. At 5943f1d7 the
rewritten `sealed` fails `merge-base --is-ancestor`, is skipped, and the
second clone queues a second stamp for a work item the first clone already
stamped. Rebasing a feature branch onto a moved base is an ordinary step in a
repository that uses this plugin, and the stale `Target SHA` it leaves is
exactly what sends the sealer back for a re-run. The same-clone shape stays
held by `already_queued`; the earlier-run chain holds the row that keeps
`; earlier run: <sha> sealed` (executed, probe row 2, second case).

The class. The history alone cannot tell a `sealed` that never drew (round
4's case: a row naming a commit the branch does not hold) from a `sealed`
that drew before its history was rewritten (a rebase, or a fresh clone of a
force-pushed branch). Any condition over ancestry fails one of them: round 3's
toward a missing stamp, round 4's toward a doubled one. Q7's answer (a) names
the doubled direction as the one the owner's rule forbids, and accepts the
missing one as Q5's kind of gap.

Executed (a `test_tmp_*` file over the stamp module's own helpers, run in the
round's clone and deleted; probe rows 2 to 4):

- One clone seals and queues. A second clone moves `main`, rebases `feat/x`
  onto it, commits a fix and a guarantee reading `sealed` over the new HEAD
  with no earlier run. At 5943f1d7 that commit queues a second values file;
  with eb4303b4's `seal_stamp.py` it queues nothing.
- The same, but the rebase is made in the first clone and the second clone
  is a fresh clone of the rebased branch, which does not hold the pre-rebase
  commit (`git cat-file` exits 128). At 5943f1d7 it queues a second file;
  with eb4303b4's module nothing.
- The rebased sealed commit itself, should `post-commit` run during the
  rebase, queues nothing at either state, since its audited commit is not in
  its history.

Read: a narrower alternative counts an earlier `sealed` wherever its target
resolves to a commit in the clone (`rev-parse -q --verify <target>^{commit}`)
rather than wherever it is an ancestor. Executed in the round's clone, it
keeps round 4's case green and holds the first rebase shape, and the stamp
module stays green, 52 passed with the probe; the fresh clone of a
force-pushed branch still queues a second stamp, so it shrinks the doubled
direction without closing it (probe row 4).

The fix that matches Q7's answer (a), in `skills/verify/scripts/seal_stamp.py`,
`sealed_before`'s loop body as it stood at eb4303b4:

```python
        verdicts = chain.verdicts_of(reader, text)
        if len(verdicts) == 1 and chain.verdict_word(verdicts[0][1]) == chain.SEALED:
            return True
    return False
```

With it, `test_a_seal_that_queued_nothing_does_not_count_as_stamped` no
longer holds and leaves the module; round 4's case joins Q7 as an accepted
missing stamp, and `docs/the-review-record.md` §*The stamp*, the docstrings,
the module's once comment, `overview.md`'s round-3 row and §*Fed back into
the spec*, and the fragment return to round 3's sentence. The sentence at
`docs/the-review-record.md:286`, with the case below replacing round 4's on
its `Enforced by:` line:

```text
guarantee elsewhere, queues nothing; and a guarantee that read `sealed` at an
earlier commit of that history, or whose `Target SHA` row's `; earlier run:`
chain reads `sealed`, was stamped then, which holds across clones. The stamp
```

The case, after `test_a_sealed_item_recommitted_in_another_clone_queues_nothing`.
Its body is probe row 2's first case, red at 5943f1d7 and green with
eb4303b4's module:

```python
def test_a_sealed_item_rebased_in_another_clone_queues_nothing(tmp_path):
    """#975 round 5, once per work item. The guarantee was stamped in one
    clone. A second clone rebases the branch, so the sealed commit is
    rewritten over a history that no longer holds its audited commit, and
    the sealer's re-run writes its row fresh. The rewritten `sealed` is the
    stamp's trace, so nothing is queued. Red at 5943f1d7: `sealed_before`
    skipped the rewritten commit and the second clone queued a second
    stamp."""
    repo, _target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    (other / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(other, "the base moved")
    git(other, "switch", "-q", "feat/x")
    git(
        other,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "rebase",
        "-q",
        "main",
    )
    (other / "x.txt").write_text("a fix after the rebase\n", encoding="utf-8")
    commit_all(other, "a fix")
    new = git(other, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(other, "rev-parse", "--short", "main").stdout.strip()
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(guarantee_text(new, base, "sealed"), encoding="utf-8")
    commit_all(other, "the sealer again after the rebase, its row written fresh")
    assert after_the_commit(other) == ""
    assert queued(other) == []
```

answer: the run went back to the framer (Q8 (a), never twice); the reframed plan rebuilt `sealed_before` on round 3's condition in phase 6 (b2f97fb1), with this finding's rebase case as its proof, and phase 7 (ffefb57e) brought the memo along.

## Confirmations

confirms: round-4#1
The case round 4 named holds at 5943f1d7: a `sealed` over a commit the
branch does not hold queues nothing, and the later commit that repairs the
row queues the work item's one stamp.
`test_a_seal_that_queued_nothing_does_not_count_as_stamped` passes at HEAD
and fails with eb4303b4's `seal_stamp.py` put back (executed, probe rows 1
and 2). The docstrings of `sealed_before` and `queue_for_guarantee`, the
module's once comment, the sentence and `Enforced by:` line in
`docs/the-review-record.md` §*The stamp*, the memo's two rows and the
fragment all say that condition (read, the fix diff); `git grep -n -F` of
the changed sentence and of the fragment's new clause finds no pin under
`tests/`, `bin/rules --check` exits 0, and `uvx ruff check` and `uvx ruff
format --check` of the two Python files exit 0 (executed, probe row 5). The
close holds for what the finding named; finding 1 above is what the same
change does to a rewritten history.

confirms: none
`questions.md` Q7 states the earlier-run instance the fix pass enumerated and
its answer (a), and `test_a_second_sealed_verdict_queues_nothing` still
holds it with `bbb2222`, a SHA its repository does not hold (read; executed
in probe row 1). Per the spawn prompt that instance is accepted and is not a
finding here.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round | — | the sealer's broad run, after the rounds settle |
| Which failure the stamp takes where the history cannot tell a `sealed` that never drew from one rewritten after it drew: round 3's missing stamp, round 4's doubled one, or the narrower `rev-parse --verify` form that still doubles in a fresh clone of a force-pushed branch. Finding 1's fix follows Q7's answer (a); reversing round 4's close is a frame decision | `skills/verify/scripts/seal_stamp.py:1079`, `questions.md` Q7 | the orchestrator, under the owner's delegation |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q` in the round's clone at 5943f1d7 | 50 passed, exit 0 |
| `tests/test_tmp_round5_probe.py` with `-s -p no:xdist`, at 5943f1d7 and with eb4303b4's `seal_stamp.py`, beside the stamp module filtered to round 4's case and round 3's second-clone case: a rebase in a second clone then a fresh `sealed` row; the same keeping `; earlier run: <sha> sealed` | at 5943f1d7: the fresh row queued a second file, the kept earlier run queued nothing, the rebased sealed commit queued nothing; at eb4303b4: all three queued nothing, round 4's case failed (the repaired commit said nothing), round 3's case passed |
| the same probe with a third case: the rebase made in the first clone, then a fresh clone of the rebased branch and a fresh `sealed` row | at 5943f1d7: a second file queued, the pre-rebase commit absent (`git cat-file` exit 128); at eb4303b4: nothing queued |
| the probe and the stamp module with `sealed_before`'s condition changed to `rev-parse -q --verify <target>^{commit}` in the clone, then restored | 52 passed, 1 failed: the fresh clone of the rebased branch queued a second file |
| finding 1's case, taken from this record's fenced block into a `test_tmp_*` file, at 5943f1d7 and with eb4303b4's `seal_stamp.py`; `uvx ruff format --diff` of the case alone | 1 failed; 1 passed; already formatted |
| this record staged in the clone: `chain_check.py --baseline f6ae6db6 --worktree`; `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py` with `-q` | one refusal for this record, finding 1's `verdict: open`, beside the absent `broad-gate.md` and `guarantee.md`; 40 passed |
| `git grep -n -F` of `over a commit then in its history` and of `corrects that row in place` under `tests/`; `bin/rules --check`; `uvx ruff check` and `uvx ruff format --check` of `seal_stamp.py` and the stamp test module; `bin/test tests/test_the_commit_gate_decides_at_the_commit.py tests/test_chain_check.py -q`; the probe deleted, `seal_stamp.py` restored, `git status --short` | no match, no match; exit 0; exit 0, exit 0; 257 passed; clean |
