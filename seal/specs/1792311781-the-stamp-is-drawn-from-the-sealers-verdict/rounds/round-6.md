# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — review round 6

target: 1f1e795b, fixes 96cd142b..1f1e795b

## Findings

### 1. The double-stamp limit is stated as one amend while every rewrite of the sealing commit draws a second stamp, and the policy states no limit at all

severity: should
location: `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/changelog.md:14-18`, `docs/the-review-record.md:286-288`, `skills/verify/scripts/seal_stamp.py:924-927`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1393-1396`
verdict: open

The unit is the statement of the once rule's limit, which phase 6 built as
the frame wrote it. It is new work of the redesign, so this finding names no
earlier finding as its cause.

Why it matters. The fragment, which a plugin user reads, says "the one
exception is a second clone amending the sealing commit itself". The code
comment, `spec.md` §*Scope* and the memo's round-3 row say the same: an
amend. The policy, `docs/the-review-record.md` §*The stamp*, states no limit:
its rule sentence ends "was stamped then, which holds across clones", and its
unchecked paragraph names only the missing-stamp gap. The mechanism behind
the limit is wider than an amend. `sealed_before` reads HEAD's history, so
any `sealed` committed over a history that carries no earlier `sealed`, in a
clone that holds no values file for the work item, queues the stamp again.
An amend is one such commit. A sealing commit rewritten over its own parent
by a rebase is another, and so is a second seal made on a copy of the branch
that had not fetched the first. A reader who meets the second stamp after a
`rebase -i` looks in the fragment and the policy, finds "the one exception"
or nothing, and concludes the mechanism is broken rather than at a stated
limit. The policy is where the frame's own S10 sends a person who asks why a
stamp behaved as it did.

Executed (probe rows 1 and 2, a `test_tmp_*` file over the stamp module's
helpers, run in the round's clone at 1f1e795b and deleted):

- One clone seals and queues. A second clone amends the sealing commit:
  `post-commit` queues a second values file there. The stated limit holds as
  stated.
- The same, but the second clone runs `git rebase --force-rebase <the audited
  commit>`, which rewrites the sealing commit over the same parent without an
  amend: a second values file is queued.
- A second clone made before the first `sealed`, which then commits its own
  `sealed` over its own fix before fetching: a second values file is queued.

Read: `seal_stamp.py:924-927` gives the amend's cause as "its parent
predates the guarantee and its row is the one just written". Where a
`withheld` came first the parent does carry the guarantee; what the three
cases share is that the history holds no earlier `sealed`.
`docs/the-commit-gate-inside-git.md:128` says an `--amend` typed at a paused
rebase is a commit the hooks judge, so an `edit` stop in `rebase -i` reaches
`post-commit` the same way. `git grep -n -F` of `one exception`, `holds
across clones` and `amending the sealing commit` under `tests/` finds no pin
for these sentences, so the fix moves no case.

The fix states the class once in each place. In the fragment, lines 14-18
become:

```markdown
  commit the new verdict names. That holds in another clone of the same
  branch too, since its history shows the guarantee already read `sealed`.
  It does not hold where a clone commits a `sealed` over a history that
  carries no earlier `sealed`: the sealing commit amended or rewritten
  there over its own parent, or a second seal on a copy of the branch that
  had not fetched the first. That clone draws the stamp again. A squash or
  a cherry-pick of the guarantee onto another branch draws nothing, and
  neither does a
```

In `docs/the-review-record.md`, lines 286-288 become:

```markdown
guarantee elsewhere, queues nothing; and a guarantee that read `sealed` at an
earlier commit of that history, or whose `Target SHA` row's `; earlier run:`
chain reads `sealed`, counts as stamped then, which holds across clones. It
does not hold for a `sealed` committed over a history that carries no earlier
`sealed`, which draws the stamp again in that clone: the sealing commit amended
or rewritten there over its own parent, or a second seal on a copy of the branch
that had not fetched the first. The stamp
```

In `seal_stamp.py`, the once comment's last sentence (924-927, from
`carries. An amend`) becomes:

```python
# carries. A `sealed` committed over a history that carries no earlier
# `sealed` is caught by neither, so it queues again in a clone that holds
# no values file for the work item: the sealing commit amended or rewritten
# there over its own parent, or a second seal on a copy of the branch that
# had not fetched the first. Its row is the one just written.
```

And the pin, in
`test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`,
after the assertion on the rule's bold sentence, seen red before the docs
sentence lands:

```python
    assert "draws the stamp again in that clone" in rule, (
        "the double-stamp limit is stated where the rule is"
    )
```

answer:

### 2. The fragment names one instance of the missing-stamp gap, and a guarantee sealed by a person or in a clone with foreign hooks suppresses every later stamp unsaid

severity: should
location: `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/changelog.md:19-22`, `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/changelog.md:27-32`
verdict: open

The unit is the fragment's clause that phase 6 rewrote (`plan.md` row 6).
It is new work of the redesign.

Why it matters. The policy's unchecked paragraph
(`docs/the-review-record.md:334-338`) and `spec.md` §*Scope* state the class:
no stamp is queued where the guarantee's history already read `sealed` and
that verdict drew nothing. The fragment states one instance, a `sealed` whose
`Target SHA` names a commit the branch does not hold. Its second paragraph
says a clone whose git hooks slot is somebody else's "draws no stamp and
prints no line", which reads as a fact about that clone. It does not say that
such a `sealed`, or one a person committed outside a Claude session, also
stops every later commit from drawing the stamp, in any clone, a re-seal from
a clone that carries the hooks among them. A user who commits the guarantee
by hand, sees no stamp, and expects the next session's re-seal to draw it is
told nothing in the release note that says otherwise.

Executed (probe row 1): a `sealed` guarantee committed with no `post-commit`
run, as a person's own commit or a foreign hooks slot leaves it, then a fix
and a `sealed` row written fresh, committed in a session: `post-commit`
prints nothing and queues no file. The code does what the policy says; the
fragment says less.

Read: `git grep -n -F` of the fragment's sentences under `tests/` finds no
pin.

Lines 19-22 of the fragment become:

```markdown
  `sealed` whose `Target SHA` names a commit the branch does not hold. That
  `sealed` still counts as the work item's one stamp, and so does a
  `sealed` that queued nothing because it was committed by a person outside
  a Claude session or in a clone whose git hooks slot is somebody else's:
  no later commit of that history draws the stamp, a corrected row or a
  re-seal from a clone that carries the hooks among them. The history cannot
  tell such a `sealed` from a stamp drawn before a rebase, and #976 carries
  that gap. The stamp's rows
```

answer:

### 3. No case holds the never-twice direction against the narrower form the frame rejected, which passes every case

severity: should
location: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:809`, `docs/the-review-record.md:291`
verdict: open

The unit is phase 6's set of cases for `sealed_before`. It is new work of
the redesign.

Why it matters. `plan.md` B4 rejects counting an earlier `sealed` only where
its target resolves in the clone (`rev-parse -q --verify <target>^{commit}`),
because a fresh clone of a force-pushed branch does not hold the pre-rebase
commit and queues a second stamp. Q8 (a) chose never twice for that reason.
No case in the module holds it. Phase 6's rebase case rebases inside the
second clone, which still holds the pre-rebase commit, so it passes under B4
as well. `test_a_seal_that_queued_nothing_does_not_count_as_stamped` left the
module, and nothing replaced it on the other side. A later edit that adopts
B4 as a refinement turns nothing red and reopens the doubled stamp that round
5 found.

Executed (probe rows 3 and 4): with `sealed_before` changed in the clone to
the B4 form, `bin/test` of the stamp module and
`tests/test_the_commit_gate_decides_at_the_commit.py` reads 229 passed. The
case below, from a `test_tmp_*` file, passes at 1f1e795b and fails under the
B4 form: the fresh clone printed the queued line. `git cat-file` of the
pre-rebase commit in the fresh clone exits 128. `uvx ruff format --diff` of
the case reports it already formatted. Phase 6's rebase case fails with
96cd142b's `seal_stamp.py` put back, so it holds round 4's form (B3), and the
case below adds B4.

The case, after `test_a_sealed_item_rebased_in_another_clone_queues_nothing`:

```python
def test_a_sealed_item_rebased_and_cloned_fresh_queues_nothing(tmp_path):
    """#975 round 6, once per work item. The guarantee was stamped in one
    clone, which then rebased the branch onto a moved base. A fresh clone
    of the rebased branch does not hold the commit the first `sealed`
    audited, and the sealer's re-run there writes its row fresh. The
    rewritten `sealed` still counts, so nothing is queued. Red with
    `sealed_before` counting a `sealed` only where its target resolves in
    the clone (`plan.md` B4): the fresh clone queued a second stamp."""
    repo, target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    git(repo, "switch", "-q", "main")
    (repo / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(repo, "the base moved")
    git(repo, "switch", "-q", "feat/x")
    git(
        repo,
        "-c",
        "user.name=e",
        "-c",
        "user.email=e@example.com",
        "rebase",
        "-q",
        "main",
    )
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    held = subprocess.run(
        ["git", "-C", str(other), "cat-file", "-e", target], capture_output=True
    )
    assert held.returncode != 0, "the fresh clone holds the pre-rebase commit"
    (other / "x.txt").write_text("a fix after the rebase\n", encoding="utf-8")
    commit_all(other, "a fix")
    new = git(other, "rev-parse", "--short", "HEAD").stdout.strip()
    base = git(other, "rev-parse", "--short", "origin/main").stdout.strip()
    item = other / "seal" / "specs" / ITEM_NAME / "guarantee.md"
    item.write_text(guarantee_text(new, base, "sealed"), encoding="utf-8")
    commit_all(other, "the sealer again in a fresh clone, its row written fresh")
    assert after_the_commit(other) == ""
    assert queued(other) == []
```

On the `Enforced by:` line at `docs/the-review-record.md:291`, after the
rebased case's entry:

```text
tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_a_sealed_item_rebased_and_cloned_fresh_queues_nothing,
```

answer:

## Confirmations

confirms: none
The redesign builds S7 as reframed. `sealed_before`
(`skills/verify/scripts/seal_stamp.py:1062-1071`) counts one `Verdict:` of
`sealed` at any commit `git log HEAD^ -- <path>` lists, with no `target_of`
and no `merge-base`, and `_queue_one`'s refusals stand in the order
`spec.md` §*Data & interfaces* gives (read). The claim in `phases/phase-6.md`
that the rebase case is red against the module 96cd142b carries holds: it
fails with that `seal_stamp.py` put back and passes at 1f1e795b, and the stamp
module's 50 cases pass (executed, probe rows 2 and 5). The case
covers what its group does not: round 3's recommitted case passes under round
4's form and this one does not (executed, probe row 5).

confirms: none
Round 5's finding 1 stands `deferred the frame`, and the redesign answers it
as the frame said. Its rebase case is in the module with its body unchanged
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:772-808`, read
against `rounds/round-5.md:97-135`). Its fresh-clone shape, round 5's probe
row 3, queues nothing at 1f1e795b (executed, probe row 1, the case of finding
3). Its sentence is in `docs/the-review-record.md:286-288` as its second
fenced block gave it, and the rebase case replaced round 4's on the
`Enforced by:` line (read). The answer line at 1f1e795b is the one change to
round 5's record (read, the diff).

confirms: none
The unchecked paragraph's new sentence (`docs/the-review-record.md:334-338`)
carries the phrase the `silence` tuple pins
(`tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1416`), and the
fragment no longer says a corrected row draws the stamp (read). `bin/rules
--check` exits 0, `uvx ruff check` and `uvx ruff format --check` of
`seal_stamp.py` and the stamp module exit 0, and `tests/test_docs_line_wrap.py`
with `tests/test_one_word_one_meaning.py` read 64 passed (executed, probe row
6). Phase 6's note that the frame's last `git grep` cannot print nothing as
written, because `plan.md` and `spec.md` quote the removed phrases, is true of
the command as `plan.md` row 6 gives it (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified` by this round | — | the orchestrator's broad run, after the rounds settle |
| Whether the rewrite class of finding 1 stays a stated limit or is closed in the mechanism. `spec.md` §*Scope* keeps the amend out and says Q8 was not asked about it; finding 1 asks only that the limit be stated as the class it is | `spec.md:88-94`, `skills/verify/scripts/seal_stamp.py:924-927` | the orchestrator, under the owner's delegation |
| Whether git's sequencer runs `post-commit` for a plain pick during a rebase. Probe row 1's second case calls `post-commit` by hand after the rewrite; an `edit` stop's `--amend` reaches it by the documents' own account | `docs/the-commit-gate-inside-git.md:128` | the work of #976, where a stamp trigger is reconsidered |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_round6_probe.py -q -s -p no:xdist` at 1f1e795b: an amend in a second clone; `rebase --force-rebase <audited commit>` in a second clone; a second `sealed` on a clone made before the first; a person's `sealed` with no `post-commit`, then a session's fresh `sealed` row; a fresh clone of the rebased, force-pushed branch then a fresh `sealed` row | a second values file queued in each of the first three; nothing queued in the fourth and the fifth; `git cat-file` of the pre-rebase commit in the fresh clone exit 128; 5 passed |
| the same probe beside `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, before a fixture error in the probe was corrected | 1 failed (the probe's own `rev-parse main` in a clone with no local `main`), 54 passed |
| `sealed_before` changed in the clone to count a `sealed` only where `rev-parse -q --verify <target>^{commit}` succeeds (`plan.md` B4); `bin/test` of the stamp module and `tests/test_the_commit_gate_decides_at_the_commit.py -q`; the probe; the file restored by `git checkout` | 229 passed; the fresh-clone case failed, 4 passed |
| finding 3's case in `tests/test_tmp_round6_case.py`: `uvx ruff format --diff`; `bin/test` at 1f1e795b; the same under the B4 form, then restored | already formatted; 1 passed; 1 failed, the fresh clone printed the queued line |
| `seal_stamp.py` replaced by 96cd142b's in the clone; `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q -k 'rebased or recommitted'`; restored | the rebased case failed, the recommitted case passed |
| `bin/rules --check`; `uvx ruff check` and `uvx ruff format --check` of `seal_stamp.py` and the stamp module; `bin/test tests/test_docs_line_wrap.py tests/test_one_word_one_meaning.py -q`; both `test_tmp_*` files deleted, `git status --short` | exit 0; exit 0, exit 0; 64 passed; clean |
| this record: `chain_check.py --baseline f6ae6db6 --worktree` on the branch worktree; staged in the clone, `bin/test` of `test_no_real_identifiers.py`, `test_the_record_is_written_in_words.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py` with `-q` | three refusals for this record, each finding's `verdict: open`, beside the absent `broad-gate.md` and `guarantee.md`; 40 passed |
