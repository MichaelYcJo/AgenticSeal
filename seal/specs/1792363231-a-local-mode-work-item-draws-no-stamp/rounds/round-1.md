# 1792363231-a-local-mode-work-item-draws-no-stamp — review round 1

target: 601245af against release/v0.22.2

## Findings

### 1. A sealed guarantee brought to another branch by a plain commit writes a refusal record, and the re-seal there draws a second stamp

severity: must
location: `skills/verify/scripts/seal_stamp.py:1240-1241`, `skills/verify/scripts/seal_stamp.py:1178`, `docs/the-review-record.md:331-340`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
verdict: fixed e8b71bc2

Why it matters. The owner's rule is one stamp per work item, and `spec.md`
S13 says no refusal record is written "where the refused `sealed` may have
been stamped elsewhere". The only copy case `spec.md` §*Scope* and
`docs/the-review-record.md:301-302` accept is a `sealed` copied by hand
into a clone that never fetched its audited commit. Three ordinary git
operations reach the same double stamp in a clone that did fetch it, and no
document names them.

The path, read. In a second clone, a person brings the work item onto
another branch with `git merge --squash`, `git cherry-pick -n` or
`git checkout <rev> -- <dir>`, then runs `git commit`. Each commit's reflog
subject is a plain `commit: `, so guard 2 passes. The audited commit
resolves, because the clone fetched the source branch. It is not in HEAD's
history and has no patch-equivalent copy there, because the copy carries the
guarantee and not the audited commit's own patch. So guard 4 passes too.
`_queue_one` reaches the ancestry refusal at `seal_stamp.py:1239` and writes
a record at `:1241`. A later re-seal in that clone names the copied run in
its chain, and `refused_here` lets both the chain reader and `sealed_before`
skip it. `already_queued` finds nothing, because this clone never drew. So
the re-seal queues a second stamp. At 769f2aa4 the chain refused that
re-seal, so this work opened the path.

Executed. The probe `tests/test_tmp_976_copy.py` built the first clone with
`guaranteed()` and drew its stamp there. It then made a `git clone
--no-local`, switched to `main`, brought the work item over by each of the
three operations, committed, and re-sealed with
`; earlier run: <target> sealed`. In all three, `post-commit` queued nothing
at the copy and wrote one record, `1799000000-<target>`. The re-seal then
queued a values file in the second clone while the first clone held its
own. That is two stamps for one work item. The probe was deleted.

What tells the copy apart, executed in the same probe. `git log --all --not
HEAD -- <guarantee path>` listed one commit in each case: the source
branch's sealing commit, reading `sealed` over the same target. S12's shape
has no such commit, since its other branch holds the audited commit and
never touched the guarantee, so a guard on that listing keeps S12's record.
It runs only on the refusal path and can only withhold a record, as guard 4
does.

The fix adds the guard, a case seen red at 601245af (the probe above is
that case's body), and the rule's sentence.

```python
def _sealed_on_another_ref(chain, top, path, target):
    """Whether a commit some ref of this clone holds, outside HEAD's
    history, has `path` reading one `sealed` over `target`. HEAD then
    brought the verdict from that branch by a plain commit (a `merge
    --squash`, a `cherry-pick -n`, a `checkout <rev> -- <path>`), and it may
    have been stamped where that branch holds the audited commit."""
    reader = chain.SHARED_READER
    listed = _git(top, "log", "--format=%H", "--all", "--not", "HEAD", "--", path)
    for sha in (listed or "").split():
        text = _git(top, "show", f"{sha}:{path}")
        if not text:
            continue
        verdicts = chain.verdicts_of(reader, text)
        if (
            len(verdicts) == 1
            and chain.verdict_word(verdicts[0][1]) == chain.SEALED
            and _same_commit(chain.target_of(reader, text), target)
        ):
            return True
    return False


# in `_queue_one`, at the ancestry refusal (seal_stamp.py:1239-1242)
    if _git(top, "merge-base", "--is-ancestor", target, "HEAD") is None:
        if _stamped_nowhere_else(top, target) and not _sealed_on_another_ref(
            chain, top, f"{rel}/guarantee.md", target
        ):
            record_refusal(common, ident, target)
        return None
```

```python
@pytest.mark.parametrize(
    "bring",
    [
        ("merge", "--squash", "origin/feat/x"),
        ("cherry-pick", "-n", "origin/feat/x"),
        ("checkout", "origin/feat/x", "--", f"seal/specs/{ITEM_NAME}"),
    ],
    ids=["merge --squash", "cherry-pick -n", "checkout a path"],
)
def test_a_seal_brought_from_another_ref_writes_no_refusal(tmp_path, bring):
    """1792363231 S13. The guarantee was stamped in one clone. A second
    clone brings it onto `main` by a plain commit from the branch it
    fetched, so the audited commit is not in HEAD's history and has no copy
    there. Another ref still holds the sealing commit, which may have been
    stamped, so no record is written and the re-seal queues nothing."""
    repo, target, _base = guaranteed(tmp_path)
    assert after_the_commit(repo)
    other = tmp_path / "other"
    subprocess.run(
        ["git", "clone", "-q", "--no-local", str(repo), str(other)], check=True
    )
    git(other, "switch", "-q", "main")
    git(other, *bring)
    git(other, *SIGNED, "commit", "-qm", "the item brought over")
    assert after_the_commit(other) == ""
    assert refusals(other) == []
    new = a_fix(other)
    seal_and_commit(
        other,
        new,
        short(other, "origin/main"),
        "the sealer again",
        earlier=f"; earlier run: {target} sealed",
    )
    assert after_the_commit(other) == ""
    assert queued(other) == []
```

```markdown
cherry-pick or a merge. And the target does not resolve, or HEAD's side holds
no patch-equivalent copy of it, so the verdict was not audited before a
rebase moved its commit; and no ref of the clone holds, outside HEAD's
history, a commit whose guarantee reads `sealed` over that target, so the
verdict was not brought from a branch where it may have been stamped (a
`merge --squash`, a `cherry-pick -n` or a `checkout` of the path).
```

The case's name joins the rule's `Enforced by:` line, and
`_stamped_nowhere_else`'s docstring names the third condition.

answer: Fixed, and narrowed from the proposal. `_guarantee_on_another_ref` withholds the record wherever some ref of the clone holds, outside HEAD's history, any commit that changed the guarantee (`git log -1 --all --not HEAD -- <path>`). The proposed form, which read each such commit's verdict and target, was built at d244ece6 without the target comparison, which I dropped on reading because no case holds another ref with a `sealed` over a different target. The rest was dropped at e8b71bc2: replacing its verdict check with `True` survived `mutation-check`, so no case told a `sealed` there from any other change. Withholding a record keeps the gap rather than drawing twice. `test_a_seal_brought_from_another_ref_writes_no_refusal`, in three forms, was red at 601245af on the record assertion and is green. Replacing the guard's call, its `return` with `False`, and its `return` with `True` each turned cases red. §*The stamp*'s rule now says four things must hold; its unchecked paragraph and `seal_stamp.py`'s once comment add "one brought from another branch of the clone" to the gap; and a copy from a commit no ref holds joins the hand-copied class. The fragment and `overview.md` say the same. Weighed against `CLAUDE.md`'s subtraction rule, the record stays. This guard reads one fact that covers a copy from any ref, whatever command made it, so it does not grow with each operation. What stays outside it, a source no ref holds, joins the class Q9 already states. If a later round finds a double-stamp path that no fact in the clone can read, that is the moment to put the record itself back to the owner, whose Q2 (b) asked for a mechanism.

### 2. The orchestration tells the orchestrator to quote a local-mode line it never receives

severity: should
location: `skills/code-review/orchestration.md:241-243`, `skills/code-review/orchestration.md:250-252`, `skills/code-review/orchestration.md:263-265`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:2144-2157`
verdict: fixed d244ece6

Why it matters. The orchestrator acts on this paragraph. It says that in
local mode "the line arrives as the edit hook's message in the turn its
report comes back", and then "Wherever the commit's line or the edit hook's
message names `seal-stamp --from`, quote it as it stands". In shared mode
the line is `post-commit`'s output, which lands in the orchestrator's own
Bash result. In local mode it does not.

Read. The edit gate fires on the sealer's own `Write`, inside the sealer's
run, and prints only `{"systemMessage": …}`
(`hooks/sealer-stamp-queue.py:82-83`). The tree's one measurement of that
surface is the owner's screen (`hooks/sealer-stamp.py`'s docstring, "That
surface was measured on the owner's screen"). Nothing hands the line to the
sealer's report, and nothing hands it to the orchestrator.
`docs/the-review-record.md` says honestly that nobody has watched that
message on a screen. The orchestration states a time and a recipient that
nothing measured. An orchestrator told to quote a line it cannot see either
reports a line it never saw, or quotes nothing where the stamp did not
appear and the person most needs the command.

Rewrite the two local-mode sentences and the quote rule. Then rewrite the
two pinned phrases in `test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`
to match, and see the case red against the old paragraph.

```markdown
your text. In local mode no commit carries `guarantee.md`: the sealer's own
`Write` of it queues the values. The line naming them is the edit hook's
message, shown to the person at that write. It is not in the sealer's report
and does not reach you. So put the result text first in that turn: what was
sealed, the lines worth quoting, and what happens next.
```

```markdown
FAILED` lines. Wherever the commit's line names `seal-stamp --from`, quote
it as it stands: that command is the person's to type, and never yours. In
local mode no such line reaches you. Where no stamp appeared, name the file
under `<git-common-dir>/specseal-stamp/<session>/` whose name holds the work
item's id, and leave `seal-stamp --from <that file>` to the person.
```

answer: Fixed as proposed. The paragraph now says the edit hook's line is shown to the person at the sealer's write and does not reach the orchestrator. The rule on quoting names the commit's line alone. Where no stamp appeared, the orchestrator names the values file and leaves `seal-stamp --from` to the person. I rewrote the case's two pins and saw them red against the old paragraph; a third pin asserts that "the edit hook's message names" appears nowhere in the section. Swept: `docs/the-review-record.md:387,406` and `hooks/sealer-stamp.py:61` say the person sees the line, which holds, so they stand. `spec.md` S7 still says the line to quote is the edit hook's message; that is the frame's text, recorded as a divergence in `overview.md`.

### 3. Both READMEs still count four side effects after adding a fifth

severity: should
location: `README.md:207`, `README.ko.md:200`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:2343`, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:2354`
verdict: fixed d244ece6

Why it matters. This paragraph is the inventory a user reads to learn what
the plugin writes on their machine. Phase 4 added the refusal record's
directory to it. `README.md:207-216` now lists five writes: session-lease,
version-check, the stamp's values, the refusal record and lint-python. It
still opens "Four side effects are worth stating outright". `README.ko.md:200`
opens "네 가지 부수 효과는 밝혀 둡니다" over the same five. The case
`test_both_readmes_list_the_stamp_hook` pins the stale count in both
editions, so it holds the wrong number in place. Phase 2 rewrote the other
two counts this branch made false. This one is the same class, and
`CLAUDE.md` §*The rule a mechanism is kept against* names a stored count as
what goes stale.

Read: `README.md:207-216`, `README.ko.md:199-208`, and the pins at the test
lines above.

Drop the number in both editions, and pin its absence.

```markdown
No gate transmits your code, your paths, or your prompts anywhere. These side
effects are worth stating outright: session-lease writes a timestamp file under
```

```markdown
어떤 게이트도 사용자의 코드나 경로, 프롬프트를 바깥으로 보내지 않습니다. 다만
다음 부수 효과는 밝혀 둡니다. session-lease 는 `.git/specseal-leases/` 아래에,
```

```python
            "These side effects are worth stating outright",
            ...
            "다음 부수 효과는 밝혀 둡니다",
        ...
        for gone in ("Four side effects", "네 가지 부수 효과"):
            assert gone not in text, (edition, gone)
```

answer: Fixed as proposed. Both editions drop the number: "These side effects are worth stating outright" and "다음 부수 효과는 밝혀 둡니다". The case pins the new words and asserts both old counts are gone; I saw it red before the READMEs changed. The gate counts in the same READMEs ("Nine of the twelve", "게이트 열둘 중 아홉") are true at this commit, so they stand.

### 4. phases/phase-5.md carries a real absolute home path, which the repository's identifier scan refuses

severity: must
location: `seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/phases/phase-5.md:32`
verdict: fixed d244ece6

Why it matters. `CONTRIBUTING.md` §*House rules* allows a user path only as
`/Users/x/`, and `tests/test_no_real_identifiers.py` enforces it on every
tracked file. Line 32 names the raw output's directory by a real absolute
path under a real user's home. The broad gate's suite fails on it, and the
hygiene workflow refuses the pull request.

Executed: `bin/test tests/test_no_real_identifiers.py -q -p no:xdist`
exited 1. `test_only_fixture_user_paths` failed, naming
`seal/specs/1792363231-a-local-mode-work-item-draws-no-stamp/phases/phase-5.md:32`.
Five passed. Read: the sentence is the orchestrator's account, written into
the phase record by the smith.

```markdown
kept the raw output in a sibling of the branch worktree, `976-phase-5-raw`,
```

answer: Fixed. The sentence names the raw directory as a sibling of the branch worktree, `SpecSeal-worktrees/976-phase-5-raw`, with no home prefix. `tests/test_no_real_identifiers.py` now exits 0, and `git grep` for `/Users/` outside the fixture path finds only two inventory rows that describe the check itself.

## Confirmations

confirms: none
The builder's divergence on guard 3 holds (`overview.md`, `phases/phase-3.md`).
Read: `_queue_one` calls `_stamped_nowhere_else` only after the chain and
`sealed_before` (`seal_stamp.py:1224-1232`). `sealed_before` returns False
only where every earlier `sealed` in HEAD's history is over a target this
clone recorded. So a `sealed` at `HEAD^` over the same target already has its
record, and guard 3 could withhold nothing. Executed: `mutation-check`
replaced the `sealed_before` call with `if False:`. Then
`test_a_body_edit_over_a_rewritten_seal_writes_no_refusal` went red on one
record, so that case pins guard 1's order, which the hand-back had stated
without showing it red. The tool restored the file.

confirms: none
`spec.md` S10 holds. Executed: an AST comparison of the fourteen #975 cases
on §*The stamp*'s `Enforced by:` line found all fourteen bodies identical at
769f2aa4 and 601245af. The diff touches none of the fixtures they call.
`git diff --stat 769f2aa4 601245af -- hooks/git/ hooks/commitgate.py
hooks/hooks.json` is empty.

confirms: none
`spec.md` S8's grep holds. Executed: `git grep -n '#976' 601245af` outside this
work item's directory, #975's directory and `changelog/0.22.1.md` exited 1
with no hit.

confirms: none
Within one clone the readers cannot draw twice. Read: both writers run
`already_queued` before any record is written (`seal_stamp.py:1232`,
`:1358`). So a clone that drew never records a refusal, and every second
stamp needs a second clone. That is why finding 1's path needs one.
`refused_here` splits a record's name at its first `-`. That is correct,
because `item_value` returns only the digits before the first `-`
(`seal_stamp.py:495-499`), and `already_queued` reads values names the same
way.

confirms: none
The gate matches the path's shape before it loads `seal_stamp.py` or runs
`git` (`hooks/sealer-stamp-queue.py:67-79`). The local writer refuses in
`spec.md` §*Data & interfaces*' order and records only where the `Branch`
row's branch resolves (`seal_stamp.py:1370-1374`). The overview's second
divergence, the `git_common_dir` check that keeps a shared path out, is
needed. `home_at` alone answers `<repo>/seal` for a shared path, as
`phases/phase-1.md` says. Read.

confirms: none
Carried and not re-established: #975's round 4 and round 5 shapes as
`spec.md` and `plan.md` name them, and `questions.md` Q1's and Q4's answers.
Q1 is read. During this round the main checkout's lease directory for this
worktree held one lease, under the main session's id, and it was refreshed
while this warden ran. That fits Q1's answer but is not a measurement of it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The suite stays `unverified` here | the branch at 601245af | the orchestrator's `broad-gate --base <base> --record <item>`, after the rounds settle |
| Windows path comparison in the edit gate and the local writer (`questions.md` Q3) | `hooks/sealer-stamp-queue.py:50-53`, `skills/verify/scripts/seal_stamp.py:1321-1343` | the orchestrator, from CI's Windows leg |
| Reflog subjects on git versions other than 2.50.1 | `test_guard_two_reads_what_post_commit_sees_in_the_reflog` | the orchestrator, from CI's legs |
| Whether a subagent's `PostToolUse` `systemMessage` reaches the person's screen, and when | `hooks/sealer-stamp-queue.py:82-83` | the owner, on the first local-mode run after the release |
| Two `PostToolUse` runs over one local guarantee at once. `already_queued` then `write_values` is not atomic, so two overlapping runs could each queue. Whether the harness ever overlaps a session's post-edit hooks was not measured | `skills/verify/scripts/seal_stamp.py:1358-1392` | the owner, by measurement, or the orchestrator, filing it if it is ever seen |
| The builder's mutation and red-first runs in phases 1 to 4, beyond the one re-run above | `phases/phase-1.md` to `phases/phase-4.md` | read here; the sealer samples them |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_tmp_976_copy.py -q -s -p no:xdist` (probe file written, run once, deleted) | 3 passed. For `merge --squash`, `cherry-pick -n` and `checkout` of the path: reflog subject `commit: …`, nothing queued at the copy, one refusal record, `git log --all --not HEAD` listed one sealing commit, and the re-seal queued a values file in the second clone beside the first clone's own |
| `bin/mutation-check skills/verify/scripts/seal_stamp.py --replace '    if sealed_before(chain, top, f"{rel}/guarantee.md", common, ident):' '    if False:' --tests "bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py -q -p no:xdist -k body_edit_over_a_rewritten_seal"` | exit 0, red: `assert ['1799000000-c68e21b'] == []` at the case's refusal assertion; the tool restored the file and `git status` was clean |
| `python3 -I <scratchpad>/bodies.py <worktree>` (an AST comparison, deleted) | 14 of 14 #975 case bodies found and identical at 769f2aa4 and 601245af |
| `git diff --stat 769f2aa4 601245af -- hooks/git/ hooks/commitgate.py hooks/hooks.json` | empty |
| `git grep -n '#976' 601245af -- . ` with S8's three exclusions | exit 1, no hit |
| `bin/test tests/test_no_real_identifiers.py -q -p no:xdist` | exit 1: 1 failed, 5 passed; `test_only_fixture_user_paths` names `phases/phase-5.md:32` |
