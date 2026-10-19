# 1792363231-a-local-mode-work-item-draws-no-stamp — review round 2

target: 68d51801, fixes e7439437..68d51801

## Findings

### 1. The other-ref guard withholds the record for the branch's own tracking ref after a rebase, so the repair of a refused sealed draws nothing again

severity: must
location: `skills/verify/scripts/seal_stamp.py:1178-1188`, `skills/verify/scripts/seal_stamp.py:1191-1207`, `skills/verify/scripts/seal_stamp.py:1257`, `docs/the-review-record.md:339-342`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: open
regression: round-1#1

The unit is `_guarantee_on_another_ref` (`seal_stamp.py:1178-1188`), which
e8b71bc2 narrowed to `git log -1 --all --not HEAD -- <path>`. `spec.md` S11
and `questions.md` Q2 (b) frame the refusal record so that the repair in the
refusing clone draws the work item's one stamp. S13 allows withholding the
record only "where the refused `sealed` may have been stamped elsewhere".
The fix withholds it wherever any ref outside HEAD's history changed the
guarantee, and that includes this branch's own remote-tracking ref after a
local rebase. That ref holds only a `withheld` guarantee, which drew no
stamp anywhere. The defect came from dropping the verdict read: the
narrowed guard asks whether a commit changed the guarantee, not whether a
commit read `sealed`.

Why it matters. This repository's flow is to push the branch, commit a
`withheld` guarantee, and rebase onto a base that moved, as this branch's
base did with #966 and #978. After that rebase, `origin/<branch>` still
holds the pre-rebase commit that changed the guarantee, until the next
force push. A `sealed` over a commit the branch does not hold, committed
then, now writes no record. The repair draws nothing, which is the #975
Q7 gap this work exists to close. The documents do not say so either:
`docs/the-review-record.md:400` names "one brought from another branch of
the clone", and here nothing was brought from anywhere.

Executed. The probe `tests/test_tmp_976_round2.py`, run against 68d51801
and then deleted, did the following:

- It built `guaranteed(verdict="withheld — x")` and made a `--no-local`
  clone.
- It moved `main` and rebased `feat/x` onto it.
- It committed a `sealed` over `deadbee`. The result was `post-commit`
  silent, no record, and `git log -1 --all --not HEAD -- <path>` naming a
  commit.
- It then committed the repair with `; earlier run: deadbee sealed`. The
  repair queued nothing: 0 values files.

Read: at d244ece6 the guard also read the verdict. It would have found no
`sealed` on `origin/feat/x`, so it would have let guard 4 record `deadbee`,
and the repair would have drawn.

The subtraction argument does not hold. The verdict check survived
`mutation-check` because no case put a ref outside HEAD's history holding a
change that did not read `sealed`. It did not survive because the check
decides nothing, and this shape is where it decides. Reading the verdict
without the target is the right width. A `sealed` over any target on
another ref may have been stamped. Of the other refs the guard now sees,
only one carrying a `sealed` can have been stamped elsewhere.

The fix restores the verdict read without the target comparison, and plants
the case that kills the mutant. The case is red at 68d51801, as the probe
shows.

```python
def _sealed_on_another_ref(chain, top, path):
    """Whether some ref of this clone holds, outside HEAD's history, a
    commit whose `path` reads one `Verdict:` of `sealed`, over any target.
    HEAD may then have brought that verdict from the branch by a plain
    commit (`merge --squash`, `cherry-pick -n`, `checkout <rev> -- <path>`),
    and the work item may have been stamped where that branch holds its
    audited commit. A ref whose changes to `path` never read `sealed`, such
    as this branch's own tracking ref left behind by a rebase over a
    `withheld` guarantee, was stamped nowhere and withholds nothing."""
    reader = chain.SHARED_READER
    listed = _git(top, "log", "--format=%H", "--all", "--not", "HEAD", "--", path)
    for sha in (listed or "").split():
        text = _git(top, "show", f"{sha}:{path}")
        if not text:
            continue
        verdicts = chain.verdicts_of(reader, text)
        if len(verdicts) == 1 and chain.verdict_word(verdicts[0][1]) == chain.SEALED:
            return True
    return False


# `_stamped_nowhere_else(chain, top, path, target)`, and in its body:
    if _sealed_on_another_ref(chain, top, path):
        return False


# the call in `_queue_one`:
        if _stamped_nowhere_else(chain, top, f"{rel}/guarantee.md", target):
```

```python
def test_a_tracking_ref_left_by_a_rebase_does_not_withhold_the_record(tmp_path):
    """1792363231 S11 after a push and a rebase, round 2's finding 1. The
    `withheld` guarantee was committed and pushed, then the branch was
    rebased onto a moved base, so `origin/feat/x` still holds the
    pre-rebase commit that changed the guarantee. A plain commit then reads
    `sealed` over a commit nobody has. That ref never read `sealed`, so it
    was stamped nowhere: the refusal is recorded, and the repair draws the
    one stamp. Red at 68d51801."""
    repo, _target, base = guaranteed(tmp_path, verdict="withheld — x")
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    (other / "base.txt").write_text("the base moved\n", encoding="utf-8")
    commit_all(other, "the base moved")
    git(other, "switch", "-q", "feat/x")
    git(other, *SIGNED, "rebase", "-q", "main")
    seal_and_commit(other, "deadbee", base, "the sealer's row names a commit nobody has")
    assert after_the_commit(other) == ""
    assert refusals(other) == [f"{ITEM_ID}-deadbee"]
    new = a_fix(other)
    seal_and_commit(
        other,
        new,
        short(other, "main"),
        "the row repaired",
        earlier="; earlier run: deadbee sealed",
    )
    assert after_the_commit(other)
    assert len(queued(other)) == 1, queued(other)
```

```markdown
cherry-pick or a merge. No ref of the clone holds, outside HEAD's history, a
commit whose guarantee reads `sealed`, so the verdict was not brought by a
plain commit from a branch where the work item may have been stamped: a
`merge --squash`, a `cherry-pick -n` or a `checkout` of the path. A ref that
changed the guarantee and never read `sealed`, such as the branch's own
tracking ref after a rebase, withholds nothing. And the
```

The new case joins the rule's `Enforced by:` line. The pinned phrase in
`test_the_policy_states_the_refusal_record_and_names_its_cases` follows the
sentence.

answer:

### 2. A sealed brought by a plain commit from a commit no ref holds still writes a record and draws a second stamp, and the fix pass accepted that in the policy without the frame or the owner

severity: should
location: `skills/verify/scripts/seal_stamp.py:1191-1215`, `docs/the-review-record.md:301-303`, `seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/overview.md`
verdict: open
reopens: round-1#1

Why the close does not hold. Round 1's finding 1 was "a sealed guarantee
brought to another branch by a plain commit writes a refusal record, and the
re-seal there draws a second stamp". The guard covers it only while some
ref still holds the source. That covers a renamed branch, a detached HEAD,
and a ref deleted after the copy (executed, below). It does not cover a
source ref deleted before the copy, such as `git fetch --prune` after the
pull request merged followed by a `cherry-pick -n <sha>`, nor a source
fetched into `FETCH_HEAD` alone. Round 1's proposed guard had the same
limit, so this round names it rather than calling it new.

Executed in the same probe. The first clone drew. The second clone deleted
`refs/remotes/origin/feat/x` and its local `feat/x`, ran `cherry-pick -n`
on the sealing commit's SHA onto `main`, and committed (`commit: …`). Then:

- `post-commit` was silent, and one record, `1799000000-<target>`, was
  written.
- The re-seal keeping `; earlier run: <target> sealed` queued a values file.
  That is two stamps.

For contrast, deleting the refs after the copy, renaming the source branch,
and committing the squash from a detached HEAD each left no record. In each
of those, the re-seal queued nothing.

Why it matters. `spec.md` §*Scope* accepts one double-stamp copy: "a
`sealed` copied by hand from another clone's guarantee into a clone that
never fetched its audited commit". d244ece6 widened that in
`docs/the-review-record.md:301-303` to "or brought there from a commit no
ref of that clone holds". The clone in this shape did fetch the audited
commit. A policy sentence the fix pass wrote is the account citing itself.
`overview.md`'s divergence table records the new guard, but not the wider
class the owner's never-twice rule now gives up.

What tells this shape apart (read). The audited commit resolves, but no ref
contains it, because the branch that carried it is gone. The case's other
shapes keep it on a ref: S12 has it on another branch, and S11's `deadbee`
does not resolve. Withholding the record there closes this shape. Its
price is a missing stamp, never a second one, wherever a clone's own
amend or conflicted rebase left the audited commit on no ref. That is Q8's
direction. The shape that stays is a sealing commit's branch deleted while
the audited commit still stands on some other ref. That is what the policy
sentence should then name, in place of the wider one.

```python
def _target_on_no_ref(top, full):
    """Whether the resolved commit `full` is held by no ref of this clone:
    the branch that carried it was deleted or rewritten, or it arrived in
    `FETCH_HEAD` alone. A verdict over it may have been stamped where that
    branch stood, so it writes no record."""
    held = _git(
        top, "for-each-ref", "--count=1", "--format=%(refname)", f"--contains={full}"
    )
    return held is not None and not held.strip()


# in `_stamped_nowhere_else`, once `full` resolves:
    if not full:
        return True
    if _target_on_no_ref(top, full):
        return False
```

If the fix pass would rather keep the wider limit, it is the owner's to
accept. Then `overview.md` gains a divergence row naming
`docs/the-review-record.md:301-303` against `spec.md` §*Scope*, for the
owner to answer, and the record gains no code.

answer:

## Confirmations

confirms: round-1#2
The orchestration paragraph now says the edit hook's line is shown to the
person at the sealer's write and does not reach the orchestrator. The quote
rule names the commit's line alone, and where no stamp appeared the
orchestrator names the values file and leaves the command to the person
(`skills/code-review/orchestration.md:250-270`, read). The pin carries both
sentences and asserts that "the edit hook's message names" is gone. Executed:
`test_the_orchestrator_is_told_the_stamp_is_drawn_for_it` passed in the
narrow run below. `spec.md` S7's old wording is recorded as a divergence in
`overview.md`, which is the right place for the frame's text.

confirms: round-1#3
Both editions drop the count, "These side effects are worth stating
outright" and "다음 부수 효과는 밝혀 둡니다" (`README.md:207`,
`README.ko.md:200`, read). The pin asserts the new words and the absence of
both old counts. Executed: `test_both_readmes_list_the_stamp_hook` passed.

confirms: round-1#4
`phases/phase-5.md:32-33` names the directory as
`SpecSeal-worktrees/976-phase-5-raw`. Executed: `bin/test
tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py -q -p
no:xdist` exited 0, 46 passed.

confirms: none
The three copy shapes of round 1 now write no record, and the re-seal queues
nothing while the source ref stands. Executed:
`test_a_seal_brought_from_another_ref_writes_no_refusal` passed in the
narrow run. The probe's renamed-branch, detached-HEAD and
ref-deleted-after-copy shapes left no record, and their re-seals queued
nothing. The fix pass argues that the guard reads one fact and does not grow
per command. That half holds: each of those shapes, by three different
commands, is caught by the one listing. The other half, dropping the
verdict, is finding 1.

confirms: none
The fix pass changed only `verdict:` and `answer:` lines in `round-1.md`
(`git diff e7439437..68d51801 -- rounds/round-1.md`, read). Each `fixed`
commit touches a path its finding's `location:` names.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The suite stays `unverified` here | the branch at 68d51801 | the orchestrator's `broad-gate --base <base> --record <item>`, after the rounds settle |
| Whether `git log --all --not HEAD -- <path>`, and finding 2's `for-each-ref --contains`, stay fast in a clone with many refs. Both run only on the refusal path inside `post-commit` | `skills/verify/scripts/seal_stamp.py:1187` | the orchestrator, from the first clone where a refusal is slow |
| Every row of round 1's `## Not judged` | `rounds/round-1.md` | as named there |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_976_round2.py -q -s -p no:xdist` (probe file written, deleted; run twice, because the first run's detached-HEAD fixture named a `main` the clone did not have) | 5 passed. Ref deleted before the copy: one record, and the re-seal queued a second stamp. Ref deleted after the copy, branch renamed, detached HEAD: no record, and the re-seal queued nothing. Stale tracking ref after a rebase over `withheld`: no record, the other-ref listing non-empty, and the repair queued nothing |
| `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q -p no:xdist -k "brought_from_another_ref or orchestrator_is_told or both_readmes or refusal_record_and_names or policy_names_what"` | exit 0, 7 passed |
| `bin/test tests/test_no_real_identifiers.py tests/test_docs_line_wrap.py -q -p no:xdist` | exit 0, 46 passed |
