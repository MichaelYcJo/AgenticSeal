# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 9ad38d66 |


## What this phase was asked

First, fix the stale count in `hooks/dispatch.py` ("Seven of the eleven
`__main__` blocks") in its own commit. This branch adds a block, so the fix
is this branch's: re-count from the tree, rewrite the sentence in place, and
update any test that pins the number.

Then build the refusal record (`plan.md` A11) test-first, per `spec.md`
S11 to S14 at a7572788. The red cases come first:
`test_a_seal_this_clone_refused_does_not_count_as_stamped` in both row
forms, `test_a_seal_over_a_commit_off_the_branch_then_repaired_draws_once`
and `test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once`.
Each guard's case is seen red by removing that guard. #975 round 5's two
rebase cases stay green with their bodies unchanged. Answer `questions.md`
Q4, the reflog subject inside `post-commit`, by the cases on real git, and
write what was observed here.

## What this phase found

**The dispatch comment, e7c7fa9f.** The tree holds 21 `__main__` blocks
under `hooks/`, and 16 of them belong to gates that `GROUPS` names, which
the dispatcher loads in-process. The sentence now names that class instead
of a count, because a stored count is what had gone stale. No test pinned
the number.

**Q4, observed on git 2.50.1 (Apple Git-155).** A real `post-commit` hook
logged `git reflog -1 --format=%gs HEAD` after each kind of commit, and
each subject began as follows.

| Commit | Subject begins |
|---|---|
| initial | `commit (initial): ` |
| plain | `commit: ` |
| `commit --amend` | `commit (amend): ` |
| `cherry-pick` | `cherry-pick: ` |
| a rebase's pick | `rebase (pick): ` |
| `rebase --continue` after a conflict | `rebase (continue): ` |
| `commit` concluding a conflicted merge | `commit (merge): ` |

So inside `post-commit` the reflog already names the commit that triggered
the hook. `test_guard_two_reads_what_post_commit_sees_in_the_reflog`
asserts each prefix and guard 2's reading of it, and it runs on every CI
leg. A git version whose subjects differ fails there and names the subject.
Other git versions are therefore read off CI, not here.

**Guard 3 was not built, because it could not decide anything.**
`spec.md` S13 lists four guards. The second mutation pass deleted guard 3
(HEAD^'s guarantee did not read one `sealed` over the same target), and all
39 selected cases stayed green. The reason is the order guard 1 fixes. A
record is considered only at the ancestry refusal, after `sealed_before`
has returned False. That means every `sealed` in HEAD^'s history, the one
at HEAD^ included, is already one this clone refused. So guard 3 could only
withhold a record that already exists. 9ad38d66 removed it, following
`CLAUDE.md`'s subtraction rule. `_stamped_nowhere_else`'s docstring states
why HEAD introduced the verdict without it.

`test_a_body_edit_over_a_rewritten_seal_writes_no_refusal` stays. Its shape
is the one the frame gives guard 3, and `sealed_before` refuses it before
the ancestry refusal is reached. That case was green at f6ad0b2c, so it
pins an outcome rather than a guard.

**Which guard turned which case red.** Each guard was removed with
`mutation-check`, one run each, at 9ad38d66.

- Guard 2, the reflog subject, turned two cases red:
  `test_a_conflicted_rebase_in_another_clone_writes_no_refusal` and
  `test_an_amend_in_a_fresh_clone_writes_no_refusal`. Replacing
  `plain_commit` by `True` turned those two and the Q4 case red.
- Guard 4's copy check turned
  `test_a_seal_whose_target_has_a_copy_writes_no_refusal` red.
- Guard 4's unresolved branch turned all three forms of
  `test_a_seal_this_clone_refused_does_not_count_as_stamped` red.
- Guard 1 is the call site's position, and it has no line of its own to
  delete. The body-edit case above is what it holds.

The other units went red too:

- the shared record write, the local record write, and the local writer's
  rule of recording only where the branch stands;
- the skip in `sealed_before`, and the chain skip in each writer;
- the record's owner, its seven-character floor and its prefix rule.

The last three survived the first pass, so 9ad38d66 added
`test_a_refusal_record_skips_only_its_own_verdict` and a third S11 row
form, in which the row keeps the refused run spelled longer.

**Red against the tree as it stood.** At c6552f91, the four S11, S12 and
S14 runs as first written failed on the record assertion: no record was
written. The Q4 case failed because `plain_commit` did not exist. The
guard cases passed there, because no record was ever written.

**The Q4 case was flaky in its first form, and the cause was in the
fixture.** A cherry-pick onto the side commit's own parent, made in the
same second, recreated that commit byte for byte. The rebase then had
nothing to pick, so the case read `commit: more on side`. Main now moves
before the cherry-pick, and three repeated runs exited 0.

**What phase 4 meets.** `seal_stamp.py`'s once comment, the
`GUARANTEE_PATH` comment, and the `queue_for_guarantee` and `sealed_before`
docstrings were rewritten in this phase. The code changed what they stated,
so contract §19 put them in the same commit. They name the refusal record
and the limits `spec.md` §*Scope* leaves. `git grep -n "#976"` outside the
three places S8 exempts now hits only `docs/the-review-record.md:345`,
which is phase 4's. This phase's test docstrings name the work item by its
id rather than its issue, so that S8 check holds.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
