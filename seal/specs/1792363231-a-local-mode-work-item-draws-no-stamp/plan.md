# Implementation Plan: a local-mode work item draws no stamp (#976)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer, when `smith` was spawned.
Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer and Q2's answer (b), when `smith` was resumed for phase 2 after the reframe at a7572788: the refusal record (A11) is taken over A8 because A8's read-time patch comparison double-draws after a conflicted rebase, and the owner's ask was a mechanism that closes the gap, not A8's shape.

<!-- The line above is the record that the gate happened. Fill it in at the
spawn: reading this plan and spawning the builder IS the approval, so nothing
extra is being asked for here — only that the approval stop living in a
transcript. A later session, a reviewer and CI all read the tree, and a plan
with nobody's name on it is indistinguishable from one nobody approved.

Where the session builds the work itself, `<who>` is still a person and the
moment is still the first edit rather than a spawn — say so in place of the
clause about `smith`, and keep the shape.

That shape is `templates/sdd-routing.md`'s, whose `Answered <date> by <who>,
before the first edit.` line records the other batch the same way: the verb,
the date, who, and the moment it was given. The two are pinned against each
other, so neither spelling can drift into a second convention for one kind of
fact. -->

## Summary

In local mode the sealer's `guarantee.md` is written under the git directory
and never committed, so #975's `post-commit` trigger never sees it and the
work item draws no stamp. This plan adds a second trigger beside it. A gate in
the `post-edit` group queues the stamp at the `Write` or `Edit` that leaves a
local-mode `guarantee.md` reading `sealed`. The existing `Stop` hook draws it.
Shared mode keeps `post-commit` unchanged. Once per work item in local mode is
held by the values files, which share the local root's common directory, by
the `Target SHA` row's earlier-run chain, and by the audited commit standing
on the work item's branch.

The owner answered `questions.md` Q2 with (b), so this plan also closes the
#975 Q7 gap with a mechanism. Today a `sealed` that a writer refused, because
its audited commit is not on the branch, still counts as stamped, and the
repair that follows draws nothing. From this work, the refusing writer leaves
a refusal record in the clone, under four guards. The once readers skip a
`sealed` this clone refused, so the repair draws the work item's one stamp.

## Technical context

**What this builds on** (all `read` at 769f2aa4):

- `skills/verify/scripts/seal_stamp.py:1037-1150`. `queue_for_guarantee`
  finds committed guarantees with `git diff-tree`. `_queue_one` judges one
  with `chain_check.py`'s readers, refuses in a fixed order, builds the
  values and calls `write_values`. `already_queued` (990-1015) matches
  `<ns>-<id>-<target>.json` under any session's directory.
  `guarantee_rows` (1018-1034) builds the rows.
- `hooks/commitgate.py:315-352`. `_stamp_module()` loads `seal_stamp.py` by
  path, and `post_commit` calls the writer silently on every failure. The new
  gate copies that loader shape.
- `hooks/dispatch.py:80-120`. `GROUPS["post-edit"]` is
  `("lint-python.py", "session-lease.py")`. `merge` (224-280) carries a
  gate's `systemMessage` through. `hooks/hooks.json` runs `post-edit` at
  `PostToolUse` for `Write|Edit|NotebookEdit`.
- `hooks/session-lease.py`'s docstring: a `post-edit` gate resolves the
  repository from the edited file, because the session's `cwd` may be
  elsewhere.
- `hooks/optin.py#home_at` (166-200) is the one reader of where the root is,
  shared first. `hooks/routing.py#parse` reads the `Branch` row.
  `chain_check.py:73` already loads `routing.py` as `ROUTING`.
- `hooks/sealer-stamp.py` draws each undrawn file of the main session's
  directory at `Stop`, and nothing at a subagent's end. It needs no change
  beyond its docstring.

**Why local mode can hold "once" exactly where shared mode cannot.** Shared
mode needed the history (`sealed_before`) because a guarantee travels between
clones and the values files do not. A local root never leaves its clone, and
the values directory sits in the same common directory. So a values file for
the id, pending or drawn, is a complete record of whether this work item was
stamped. The history readers have nothing to read in local mode and are not
used there.

**The guard that keeps old items quiet.** `settle` refuses local mode, so a
local root holds every `sealed` guarantee the clone ever wrote. Those written
before this release have no values file. Without a guard, the first edit of
such a file would draw a stamp for a work item finished months ago. The guard
is that the audited commit is an ancestor of `refs/heads/<Branch row>`. A
merged work item's branch is usually deleted, and then nothing is queued. One
whose branch still stands can still draw late, once, on its first edit. That
is stated in §*The stamp*, and its fail direction is one late stamp, never a
second one.

**Path resolution is the part most likely to go wrong.** On macOS a temporary
directory resolves through `/private`. A linked worktree's common directory is
the main checkout's `.git`. On Windows the path's separators and case differ.
The gate compares `os.path.realpath` on both sides and derives `<common>` from
the path, never from the payload's `cwd`. The cases build both a main checkout
and a linked worktree.

**What fails in six months.** A harness change could make a subagent's
`PostToolUse` carry its own `session_id`. The values file would then land in a
directory no main `Stop` reads, and the stamp would go missing.
`questions.md` Q1 measures today's behaviour. The hand-command line in the
edit hook's message is what a person uses then.

**The refusal record, and the readers it meets.** #975's rounds 3 to 6 moved
one reader back and forth. Round 3 added `sealed_before`: any earlier
`sealed` in the history counts as stamped. Round 4 narrowed it to a `sealed`
whose target was an ancestor of its own commit, and the round 4 fix drew a
second stamp after a rebase in another clone (round 5). The reframe after
round 5 went back to round 3's rule and accepted the gap. Round 6 found the
amend of the sealing commit in a second clone and left it a stated limit
(#975 Q9). The lesson is that **any condition evaluated over ancestry at read
time** fails one direction. A rebase changes ancestry after the fact, so the
reader cannot tell a verdict that was never stamped from one stamped before
the rewrite.

The record avoids that by asking a different question at a different time.
It is written once, at the moment a writer refuses, in the clone that
refused. It is read later only in that same clone. Its claim is narrow: this
clone refused this verdict, so this clone drew nothing for it. Here is what
each reader does with it.

- **`already_queued`** (round 1). Unchanged. It runs before the ancestry
  refusal, so a record is only ever written in a clone that holds no values
  file for the work item. The record lives in its own directory, so it never
  counts as queued and is never drawn.
- **The ancestry refusal** (round 1). Unchanged as a decision. In shared mode
  it becomes the record's only write site.
- **`sealed_before`** (rounds 3 to 5). It gains one skip, keyed on the
  record and never on ancestry. Round 4's failure cannot come back through
  it, because no rebase writes a record (guard 2).
- **The earlier-run chain** (#975 S7). The same skip.
- **Q9's limit** (round 6). An amend or a rewrite writes no record (guard 2),
  so the limit neither widens nor narrows.

**The guard, stated once.** A second stamp needs a second clone that drew
for this work item. That clone drew from a `sealed` whose audited commit was
an ancestor there. So the same verdict text can be refused here only where
the two histories differ for that commit. Each guard closes one way they can
differ.

1. The refusal is the committing commit's own verdict, at the ancestry
   refusal and nowhere earlier.
2. `HEAD`'s newest reflog entry is a plain `commit:` or `commit (initial):`.
   A rebase, a cherry-pick, an amend or a merge rewrites history that may
   have been stamped elsewhere, so none of them writes a record.
3. The guarantee at `HEAD^` did not already read one `sealed` over the same
   target. A body edit over a rewritten `sealed` therefore writes nothing.
4. The target does not resolve, or HEAD's side holds no patch-equivalent copy
   of it (`git rev-list --cherry-pick --right-only --no-merges
   HEAD...<target>` still lists the target). This is where patch-equivalence,
   the fourth reading Q2 named, enters. It runs only on the refusal path,
   after guards 1 to 3, so it can only withhold a record, never write one and
   never queue a stamp.

What is left is a `sealed` copied by hand from another clone into a clone
that never fetched its audited commit, then committed and repaired there.
That joins Q9's stated class, and its fail direction is one more stamp in
that clone. Local mode needs none of guards 2 to 4. A local root never leaves
its clone, so `already_queued` there already says whether the work item was
stamped, and a record only unblocks the chain reader for a verdict the
branch refusal turned away.

**Found while framing and left for the orchestrator to file.** `seal mode
shared` moves a local root into the tree, and the commit that adds it carries
every `guarantee.md` at once. `post-commit` judges each one by the shared
rules. An item stamped under this work's trigger has a values file and stays
quiet. An item sealed before this release whose audited commit is an ancestor
of HEAD would draw then. That happens only where its branch was merged with a
merge commit, since a squash leaves the audited commit off the base. That is
#975's behaviour at a mode switch, not a local-mode trigger, and it is out of
this scope (`spec.md` §*Scope*).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** A `post-edit` gate queues a local-mode `guarantee.md` at the `Write` or `Edit` that leaves it reading `sealed`. `post-commit` stays the shared-mode trigger | A sealer that writes the file through the shell, or a guarantee brought in by `seal import`, queues nothing. That is a missing stamp, never a false one, and contract §9 already sends the sealer's write through the tools. If the sealer wrote `sealed` and then edited the verdict away in the same run, the stamp would already be queued. `agents/sealer.md` step 5 writes the verdict once and step 6 returns, so that requires the sealer to break its own order | **Chosen.** It needs no act of a session, keys on the path the verdict was written to, and leaves the tested shared trigger alone |
| **A2** Replace `post-commit` with A1's gate for both modes, weighed as an equal (contract §20) | What it gains is real. A foreign git hooks slot stops being silent, and an amend or rebase in a second clone stops drawing again, because history operations write no file through a tool. What fails: in shared mode the sealer works in the clone its prompt names (`agents/sealer.md:36`), which can be a `git clone` of the branch worktree (`skills/code-review/orchestration.md:221-225`). The values file would land in that clone's git directory, where no main session's `Stop` reads, so a stamp drawn today goes missing. The stamp would also come before the orchestrator commits the verdict, which is the file the pull request's check reads. The orchestrator would lose the line in the commit's output that it is told to quote. And it re-derives ten rounds of #975's once rules on a new event | Rejected. Its gains are in shared mode, which this issue does not ask about, and its first failure is a lost stamp in the mode that works today |
| **A3** The `Stop` hook scans the local root for `sealed` guarantees with no values file | `settle` never retires a local-mode item (`skills/settle/SKILL.md:45-46`), so the first `Stop` after the upgrade draws every work item the clone ever sealed. A guard would need a marker of "seen before", which is a record kept beside the tree | Rejected |
| **A4** `post-commit` also scans the local root on every commit | The same flood as A3. Local mode may also never commit after the sealer, since there is nothing of the sealer's to commit | Rejected |
| **A5** A `SubagentStop` hook at the sealer's end | The payload names no file, so the hook would have to guess which guarantee from the transcript or from file times. Whether it carries the agent's type is unmeasured. That is a reading guessed from words | Rejected |
| **A6** The orchestrator runs `seal-stamp --queue <item>` after the sealer in local mode | It is an act a session must remember. `CLAUDE.md` §*The goal a design is chosen against* and #975's grounding chose the trigger that needs none | Rejected |
| **A7** Extend A1's gate to shared mode where git's hooks do not run (a foreign hooks slot) | A2's scratch-clone failure applies, and it doubles with `post-commit` wherever `githooks.decides` misjudges the slot. #975's A3 left that silence stated | Rejected for this item |
| **A8** Close the #975 Q7/Q8 gap in `sealed_before` alone: count an earlier `sealed` as stamped only where its target, or a patch-equivalent copy of it, is in the history of its own commit | It is still a condition over ancestry evaluated at read time, which is round 4's shape. A rebase with a conflict on the audited commit changes its patch, so a verdict stamped in another clone reads as never stamped, and the re-seal draws a second stamp. It also leaves round 4's measured shape open: `deadbee` does not resolve, so nothing can be compared, and the fresh clone of a force-pushed branch looks the same | Rejected as the mechanism. Patch-equivalence is kept as guard 4 of A11, where it can only withhold a record |
| **A11** A refusal record written by the refusing writer under four guards, and skipped by the once readers in the clone that holds it (`spec.md` S11–S14) | A repair committed in a clone other than the one that refused still draws nothing. A refused verdict introduced by an amend, a rebase or a cherry-pick, or one whose target has a copy in the history, writes no record and keeps the gap. A hand-copied `sealed` in an unfetched clone can draw a second stamp there, which joins Q9's class. A clone with its reflog off writes no record | **Chosen** under `questions.md` Q2 (b). It closes round 4's measured shape and the off-branch shape in the clone that refused, which is the orchestrator's own clone in this repository's flow, and keeps both of round 5's rebase cases green |
| **A12** A11 without guards 2 to 4 | An amend of the rewritten guarantee commit in a fresh clone of a force-pushed branch refuses a verdict over a target the clone does not hold, writes a record, and the re-seal draws a second stamp. A body edit over a rewritten `sealed` does the same. These are the cases S13 pins, seen red with each guard deleted | Rejected |
| **A13** Tell a rebased copy by its committer date running later than its author date | A reading of timestamps, which a fixture made inside one second, a clock skew, or `--committer-date-is-author-date` defeats. `CLAUDE.md` keeps a check to facts it reads | Rejected |
| **A9** Queue from `hooks/sealer-stamp.py` itself, registered at both `Stop` and `post-edit` | `test_the_hook_is_registered_for_stop_and_nothing_else` holds the drawing hook to `Stop`, so that nothing draws inside a subagent. One file answering two events would loosen that pin | Rejected. A separate gate, `hooks/sealer-stamp-queue.py`, keeps one event per file |
| **A10** Local "once" read from history like shared mode | A local root has no history to read. `git log` over a path under `.git/` returns nothing | Rejected; S3 and S4's four facts instead |

## Phases

Vertical slices, built test-first: each case is seen red against the tree as
it stands before the code that makes it green (contract §15).

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The local writer. Extract `_queue_one`'s values composition (`key` through `write_values`) into one helper both writers call, with no change to the shared cases. Add `queue_for_local_guarantee(path, session, now=None)` with S1–S5's refusals in `spec.md` §*Data & interfaces*' order. Fixtures build a local root under a main checkout and under a linked worktree, with `routing.md`'s `Branch` row and a real branch | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`: `test_a_local_mode_sealed_guarantee_queues_one_stamp`, `test_a_local_mode_withheld_or_undecided_guarantee_queues_nothing`, `test_a_local_mode_reseal_after_withheld_queues_the_stamp`, `test_a_local_mode_second_sealed_queues_nothing`, `test_a_local_mode_guarantee_off_its_branch_queues_nothing`, `test_the_edit_gate_leaves_shared_mode_to_post_commit` (writer half), each seen red first; the fourteen shared cases on §*The stamp*'s `Enforced by:` line green with their bodies untouched (S10) | b701bb53 |
| 2 | The gate. `hooks/sealer-stamp-queue.py` in `GROUPS["post-edit"]`, returning on a path that does not match before any `git` call or import, and printing the `systemMessage`. A `sealer-stamp-queue` row in both READMEs' hook tables, written now because the gate and its row ship together | `test_the_edit_gate_queues_a_local_mode_sealed_guarantee`, `test_a_subagents_write_queues_and_draws_nothing`, `test_the_edit_gate_is_silent_off_a_guarantee`, through `hooks/dispatch.py post-edit`; `test_the_main_sessions_stop_draws_each_undrawn_file_once` over a file this gate wrote; `tests/test_dispatch.py`, `tests/test_a_gate_that_fails_says_so.py` green; `test_both_readmes_list_the_stamp_hook` extended to the new row | |
| 3 | The refusal record (`questions.md` Q2 (b), A11). The two record functions in `seal_stamp.py` and the sibling directory `specseal-stamp-refused/`. The write in `_queue_one` at the ancestry refusal under the four guards of `spec.md` S13, and in the local writer at the branch-ancestry refusal where the branch exists. The skip in `sealed_before`, in `_queue_one`'s chain refusal and in the local writer's chain refusal. Each guard has its own case, seen red with that guard deleted, and the hand-back names which guard turned which case red | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`: `test_a_seal_this_clone_refused_does_not_count_as_stamped` (both row forms), `test_a_seal_over_a_commit_off_the_branch_then_repaired_draws_once`, `test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once`, each seen red at fa0a9488; `test_a_conflicted_rebase_in_another_clone_writes_no_refusal`, `test_an_amend_in_a_fresh_clone_writes_no_refusal` (guard 2), `test_a_body_edit_over_a_rewritten_seal_writes_no_refusal` (guard 3), `test_a_seal_whose_target_has_a_copy_writes_no_refusal` (guard 4); round 5's `test_a_sealed_item_rebased_in_another_clone_queues_nothing` and `test_a_sealed_item_rebased_and_cloned_fresh_queues_nothing` and the other shared cases on §*The stamp*'s `Enforced by:` line green with bodies untouched (S10); `git diff --stat 769f2aa4 HEAD -- hooks/git/ hooks/commitgate.py` empty | |
| 4 | The words, each rewritten in place (contract §19): `docs/the-review-record.md` §*The stamp* (the rule with the local trigger and the refusal record, its `Enforced by:` line gaining the phase 1 to 3 cases, and the unchecked paragraph naming only the limits `spec.md` §*Scope* leaves); `skills/code-review/orchestration.md:241-265`; `hooks/sealer-stamp.py:1-14`; `seal_stamp.py`'s once comment, `GUARANTEE_PATH` comment, and the `queue_for_guarantee` and `sealed_before` docstrings (S8: the mechanism in place of "#976 carries" and "a `sealed` that drew nothing counts too"); both READMEs' side-effect sentences, which gain the refusal record's directory beside `specseal-stamp/`; `agents/sealer.md:99-100` and its pin. The changelog fragment `changelog.md` in this directory | `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does` (its `silence` tuple rewritten, red against 769f2aa4's paragraph), `test_the_policy_states_the_refusal_record_and_names_its_cases` (new), `test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`, `test_both_readmes_list_the_stamp_hook`, `test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it` (pin rewritten), `tests/test_one_word_one_meaning.py`, `tests/test_docs_line_wrap.py`; `bin/rules --check` exit 0; `git grep -n "#976"` as S8 states | |
| 5 | The sealer measured, run by the orchestrator: one side of the sealer's behaviour cases at this branch, compared by `evals/scripts/noninferiority.py` with #975's phase-4 side (`seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/evals/sealer-phase-4.json`), the record written as `evals/sealer-phase-5.md` and `.json` under this directory | `noninferiority.py check` exit 0 on the record; `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`. A `fail` on rule 4 or 5 alone is recorded as it reads | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.

## Operational impact

- No migration, environment variable or dependency. `hooks/hooks.json` is
  unchanged, because the `post-edit` matcher already covers `Write` and
  `Edit`.
- Every `Write` and `Edit` in every repository now runs one more gate in the
  `post-edit` group. It returns on the path's shape before any `git` call or
  import. A process start per edit is the cost the group's two gates already
  pay.
- The refusal record adds one more clone-local write,
  `<git-common-dir>/specseal-stamp-refused/<id>-<target>`, an empty file
  that nothing prunes, the same stance `specseal-stamp/` has. It is written
  only where a writer refused a `sealed`. Its two extra `git` calls (the
  reflog entry and the cherry-pick listing) run only on that path.
- The installed gate is not the tree. This work item's own run draws its
  stamp through the plugin cache's 0.22.1 hooks, and this repository is in
  shared mode, so no run here exercises the local trigger end to end. The
  first real local-mode stamp is read by the owner after updating to 0.22.2
  (`spec.md` S7's unchecked sentence).
