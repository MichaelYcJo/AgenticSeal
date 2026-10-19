# Implementation Plan: a local-mode work item draws no stamp (#976)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer, when `smith` was spawned.
Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer and Q2's answer (b), when `smith` was resumed for phase 2 after the reframe at a7572788: the refusal record (A11) is taken over A8 because A8's read-time patch comparison double-draws after a conflicted rebase, and the owner's ask was a mechanism that closes the gap, not A8's shape.
Approved 2026-10-19 by the orchestrator, under the owner's `automation` answer, the owner's choice to redesign after round 2, and Q5's answer (a), when `smith` was spawned for phase 6 after the reframe at d33e1021.

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
fact.

The reframe after phase 6 owes a fourth line here, written by the orchestrator
at the spawn of phase 7, in the same shape. -->

## Summary

In local mode the sealer's `guarantee.md` is written under the git directory
and never committed, so #975's `post-commit` trigger never sees it and the
work item draws no stamp. This plan adds a second trigger beside it. A gate in
the `post-edit` group queues the stamp at the `Write` or `Edit` that leaves a
local-mode `guarantee.md` reading `sealed`. The existing `Stop` hook draws it.
Shared mode keeps `post-commit` unchanged. Once per work item in local mode is
held by the values files, which share the local root's common directory, by
the `Target SHA` row's earlier-run chain, and by the audited commit standing
on the work item's branch. Phases 1, 2 and 5 built and measured that, and
their commits stand.

The owner answered `questions.md` Q2 with (b), so this plan also closes the
#975 Q7 gap with a mechanism. Phases 3 and 4 built one: a refusal record each
clone kept of the `sealed` it had refused, under guards, which the once
readers skipped. Rounds 1 and 2 found the record failing in both directions
wherever a guarantee travelled between branches or clones, one new path per
guard, and the owner chose a redesign over a third guard ("설계를 다시").

**The redesign, after round 2.** A `sealed` over a commit the branch does not
hold is a wrong verdict: the pull request's check refuses it as stale, and the
stamp writer refuses it as off the history. Today both refuse after the fact,
and the writer's refusal is silent, so the wrong `sealed` becomes a fact of
the history that every clone then reads as a stamp drawn. The redesign refuses
it one step earlier, in `pre-commit`, inside the commit that would make it a
fact, with the way on in the command's output: a new audit of the sealer at
HEAD. Phase 6 built that and found the one thing the frame had missed: the
new audit keeps the refused verdict on its `Target SHA` row as `; earlier
run: <sha> sealed`, as `agents/sealer.md` §*Rules* tells it to, and the
chain reader counts every earlier `sealed` no record names, so the repair
drew nothing (`phases/phase-6.md`). So the gate records the refusal it makes,
in the clone that makes it. That record is a fact the gate established and
not an inference: the row never became history here, and an uncommitted row
reaches no other clone, which is what the guards of rounds 1 and 2 could
never establish about a row that had. `_queue_one`'s chain refusal skips a
`sealed` this clone recorded refusing; `sealed_before`, the ancestry refusal
and `post-commit` are #975's again. In local mode no commit exists to
refuse, and no pull request ever reads the guarantee, so the local writer
keeps its record, which there answers the whole question because a local root
never leaves its clone, and it says the line a person needs at the write.
Phases 7 and 8 finish that and take `post-commit`'s record and its guards
out.

## Technical context

**What this builds on** (all `read` at 339ac7dc unless a commit is named):

- `hooks/commitgate.py#pre_commit` (226-244): `_context` resolves the
  repository, the common dir and the session, and returns None for a
  repository that does not opt in or a commit with no session behind it;
  `gate.arms_missing` judges the arms with the staged paths read lazily by
  `git diff --cached --name-only`; `_sequencer_commit` leaves a rebase's or
  a cherry-pick's child commit alone; `_leave_mark` passes the backstop.
  `_stamp_module()` (315-328) loads `seal_stamp.py` by path, and
  `seal_stamp._chain_check()` loads `chain_check.py`'s readers.
- `hooks/gate.py`: `HEADER`, `STATES`, `UNCHANGED`, `refusal` (286-320),
  the texts the arms print; `routing.current_branch(cwd)` and
  `routing.parse(text)` (the `Branch` row).
- `docs/the-commit-gate-inside-git.md`: a commit is judged inside the commit,
  from the index, in the worktree it lands in; a refusal is the exit status
  and the stderr text git prints into the command's output; `--no-verify`
  is met by `reference-transaction` for the arms; a commit git makes for its
  own rebase or cherry-pick is not judged.
- `skills/verify/scripts/seal_stamp.py:1052-1420`: `queue_for_guarantee`,
  `sealed_before`, the record section (1106-1222), `_queue_one`,
  `_queue_values`, `queue_for_local_guarantee`. `GUARANTEE_PATH` (950) is
  the shared-mode path's pattern.
- `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`: the
  fixtures `guaranteed`, `seal_and_commit`, `a_fix`, `after_the_commit`,
  `queued`, `refusals`, `local_guaranteed`, `queue_local`, and
  `commitgate_module()` (518), which loads `hooks/commitgate.py` for a case
  to call its hooks directly.
- `tests/test_the_commit_gate_decides_at_the_commit.py`: the `world`
  fixture (120-170) installs the stubs and runs real commits through the
  Bash tool's shell shape, asserting HEAD and `gate.HEADER` in stderr.
- `hooks/sealer-stamp-queue.py`, `hooks/dispatch.py`, `hooks/optin.py`,
  `hooks/routing.py`, as phases 1 and 2 found them (`phases/phase-1.md`,
  `phases/phase-2.md`).

**Why the judgment moves to the commit.** The once readers answer "was this
work item's stamp drawn" from the history, because a guarantee travels
between clones and the values files do not. A `sealed` in the history is read
as drawn where it was made. That reading is wrong exactly when the writer
refused it, and the refusal was silent, so the history records a verdict and
not the refusal. #975's rounds 3 to 6 tried to tell the two apart at read
time by ancestry and failed one direction each time; this item's phases 3 and
4 recorded the refusal per clone and rounds 1 and 2 found that a guarantee
copied, rebased or pruned under the record defeats a per-clone answer. The
one moment the fact is known to the party that can act is the commit of the
wrong verdict, in the clone that commits it, before it is history. The commit
gate already runs there, already reads the index, and already prints into
the command's output the orchestrator reads. So the wrong verdict is stopped,
the next commit carries the right one, and nothing downstream has to tell
them apart.

**What the gate judges, and what it does not.** One fact: the commit's newest
`sealed` names a commit the commit's own history will not hold, on the branch
the item declares. It does not read the `; earlier run:` chain, because a
`sealed` that drew and then went stale under a rebase is rightly counted as
drawn, and its re-seal must not be stopped. It does not judge a commit on
another branch, because a `merge --squash` or a `cherry-pick -n` of a sealed
item onto `main` is a copy a person meant, and #975's ancestry refusal
already keeps `post-commit` from drawing for it. It does not judge a commit
git makes for its own rebase or cherry-pick, which `_sequencer_commit` already
excludes for the arms. It is not an arm: no opt-in beyond `seal/`, no mark,
no waiver, because there is no commit of this shape a person wants that the
pull request would accept (`questions.md` Q5 holds that default).

**Why the gate's record is not round 1's record.** Phase 3's record was
written by `post-commit` for a row that had just become history, and the
rounds showed that such a row travels: a `merge --squash` carries it to a
branch where its target is absent, a rebase leaves a copy of it on the
tracking ref, a `fetch --prune` takes its source ref away. Each guard tried
to tell, from the clone, whether the row had drawn somewhere else, and each
was a guess. The gate's record is written for a row that is not history and
will not be: `pre-commit` refused it, the index and the working tree keep it
uncommitted, and the next commit the text asks for replaces it with the new
audit. An uncommitted row is in one clone and nowhere else, so "did this
clone draw for it" and "did any clone" are the same question, which is the
property local mode had and shared mode lacked. The record therefore needs
no guard, and the chain reader's skip over it can only unblock a verdict
that drew nowhere. What it cannot unblock is a verdict in the history: a
`sealed` that drew and then went stale under a rebase stays in HEAD's
history, `sealed_before` counts it with no skip, and the repair draws
nothing, which is Q8's direction and `spec.md` S11's last clause.

**Every path rounds 1 and 2 found, walked under the gate's record** (read
from the code at de80c2c2 and the rule above; phase 7's cases run them).

- *A copy by `merge --squash`, `cherry-pick -n` or `checkout <rev> -- <dir>`
  onto `main` in a second clone, then a plain commit* (round 1). `main` is
  not the item's declared branch, so the gate is quiet and records nothing;
  the commit lands; `post-commit` meets the ancestry refusal, writes no
  record (phase 7), queues nothing. A re-seal there names the copied run as
  `; earlier run: <X> sealed`; no record names X, so the chain refusal
  counts it, and nothing is queued. One stamp, the branch's own.
- *Push, then a rebase onto a moved base, then a wrong row* (round 2,
  finding 1). The rebase's picks are the sequencer's and are not judged; the
  tracking ref keeps the pre-rebase commit, which the gate never reads. The
  wrong row over `deadbee` is refused on the declared branch and recorded.
  The new audit keeps `; earlier run: deadbee sealed`; the chain refusal
  skips it; `sealed_before` reads the rebased history, which holds the
  `withheld` and no `sealed`, so the repair draws once. Where that history
  held a `sealed` that drew before the rebase, `sealed_before` counts it and
  the repair draws nothing: never twice.
- *A source no ref holds: `fetch --prune`, then `cherry-pick -n <sha>` onto
  `main`* (round 2, finding 2). Not the declared branch, so quiet, no record,
  and the re-seal on `main` queues nothing by the chain, as in the first
  path.
- *Round 5's two shapes, a rebase in a second clone and a fresh clone of a
  force-pushed branch.* Neither commits a wrong row on the declared branch
  through `pre-commit`: the rebase is the sequencer's, and the fresh clone's
  amend stages no change to the guarantee. Their cases stand untouched
  (S10). A body edit of such a rewritten `sealed`, a plain commit staging a
  row over an orphaned target, is refused by the gate as the stale row it
  is and recorded; the new audit's chain entry is skipped, and
  `sealed_before` then finds the rewritten `sealed` in HEAD's history and
  counts it, so nothing is drawn twice (`spec.md` S11's second case).
- *What is left to double.* A wrong row that names, by coincidence, the
  very commit a copy of the item on another branch was sealed and drawn
  over, in a clone whose declared branch never drew. That needs the copy to
  draw on its branch, which #975 accepts as a second run of the item
  (`questions.md` Q9 of #975), and the sealer to name a commit that is not
  its HEAD. It doubles without the record too, since the restore of A19 or
  the row rule of A20 leaves the same first draw on the copy. It joins Q9's
  class and is stated in §*The stamp*.

**The limits the gate leaves, stated once.** Where the stub does not run, the
wrong `sealed` lands as it did under #975: a foreign hooks slot,
`--no-verify`, a plugin older than this release, a person's own commit, a
clone no session has reached. Each is a missing stamp for that item, Q8's
direction, and the backstop is not extended for it (A14's failure scenario,
`spec.md` S13). In both modes the record is sound for the same reason: the
clone that refused is the clone that re-seals, because no other clone has the
refused row, uncommitted in shared mode and under a root that never leaves
its clone in local mode. Local mode's own limits are a values directory
emptied by hand and a `seal import` of a guarantee that drew elsewhere.

**Path resolution is the part most likely to go wrong** in the local writer,
as phase 1 found; the gate reads the index by path relative to the worktree
root, which `pre-commit` runs in, and derives nothing from `cwd`.

**What fails in six months.** A harness change could make a subagent's
`PostToolUse` carry its own `session_id`; `questions.md` Q1 measured today's
behaviour. A git version whose `pre-commit` no longer exports
`GIT_INDEX_FILE` for a pathspec commit would make `git show :<path>` read the
wrong index; #692's M2 measured four gits, and `questions.md` Q6 names the
case that would show it.

**Found while framing and left for the orchestrator to file.** `seal mode
shared` moves a local root into the tree, and the commit that adds it carries
every `guarantee.md` at once. `post-commit` judges each one by the shared
rules. An item stamped under this work's trigger has a values file and stays
quiet. An item sealed before this release whose audited commit is an ancestor
of HEAD would draw then. That happens only where its branch was merged with a
merge commit, since a squash leaves the audited commit off the base. That is
#975's behaviour at a mode switch, not a local-mode trigger, and it is out of
this scope (`spec.md` §*Scope*). The new refusal does not wake on that commit
unless an item's `Branch` row names the branch it lands on.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** A `post-edit` gate queues a local-mode `guarantee.md` at the `Write` or `Edit` that leaves it reading `sealed`. `post-commit` stays the shared-mode trigger | A sealer that writes the file through the shell, or a guarantee brought in by `seal import`, queues nothing. That is a missing stamp, never a false one, and contract §9 already sends the sealer's write through the tools | **Chosen** for the trigger; built in phases 1 and 2 |
| **A2** Replace `post-commit` with A1's gate for both modes, weighed as an equal (contract §20) | In shared mode the sealer works in the clone its prompt names (`agents/sealer.md:36`), which can be a `git clone` of the branch worktree. The values file would land in that clone's git directory, where no main session's `Stop` reads, so a stamp drawn today goes missing. It would also draw before the orchestrator commits the verdict the pull request's check reads | Rejected |
| **A3** The `Stop` hook scans the local root for `sealed` guarantees with no values file | `settle` never retires a local-mode item, so the first `Stop` after the upgrade draws every work item the clone ever sealed | Rejected |
| **A4** `post-commit` also scans the local root on every commit | The same flood as A3. Local mode may also never commit after the sealer | Rejected |
| **A5** A `SubagentStop` hook at the sealer's end | The payload names no file, so the hook would have to guess which guarantee from the transcript or from file times | Rejected |
| **A6** The orchestrator runs `seal-stamp --queue <item>` after the sealer in local mode | It is an act a session must remember. `CLAUDE.md` §*The goal a design is chosen against* and #975's grounding chose the trigger that needs none | Rejected |
| **A7** Extend A1's gate to shared mode where git's hooks do not run (a foreign hooks slot) | A2's scratch-clone failure applies, and it doubles with `post-commit` wherever `githooks.decides` misjudges the slot | Rejected for this item |
| **A8** Close the #975 Q7/Q8 gap in `sealed_before` alone: count an earlier `sealed` as stamped only where its target, or a patch-equivalent copy of it, is in the history of its own commit | A condition over ancestry evaluated at read time, which is round 4's shape. A rebase with a conflict on the audited commit changes its patch, so a verdict stamped in another clone reads as never stamped, and the re-seal draws a second stamp. `deadbee` does not resolve, so nothing can be compared | Rejected |
| **A9** Queue from `hooks/sealer-stamp.py` itself, registered at both `Stop` and `post-edit` | `test_the_hook_is_registered_for_stop_and_nothing_else` holds the drawing hook to `Stop`, so that nothing draws inside a subagent | Rejected. A separate gate, `hooks/sealer-stamp-queue.py`, keeps one event per file |
| **A10** Local "once" read from history like shared mode | A local root has no history to read. `git log` over a path under `.git/` returns nothing | Rejected; S3 and S4's four facts instead |
| **A11** A refusal record written by the refusing writer under guards, and skipped by the once readers in the clone that holds it | Built in phases 3 and 4 and reviewed twice. Round 1: a `sealed` brought to another branch of a second clone by `merge --squash`, `cherry-pick -n` or a `checkout` of the path is refused there, recorded, and its re-seal draws a second stamp. Round 2, after the other-ref guard: the branch's own tracking ref, left behind by a rebase over a `withheld`, withholds the record, so the repair of a wrong row in the orchestrator's own clone draws nothing, which is the gap again; and a source no ref holds (`fetch --prune`, `FETCH_HEAD`) still draws twice. The record answers "did this clone draw", and the rule asks "did any clone" | **Taken out of shared mode by phase 7**, on the owner's "설계를 다시" after round 2. **Kept in local mode**, where the two questions are one: a local root never leaves its clone, so the clone that refused is the only clone that reads the record (`spec.md` S14) |
| **A12** A11 without guards 2 to 4 | An amend of the rewritten guarantee commit in a fresh clone of a force-pushed branch refuses a verdict over a target the clone does not hold, writes a record, and the re-seal draws a second stamp | Rejected, and moot under A14 |
| **A13** Tell a rebased copy by its committer date running later than its author date | A reading of timestamps, which a fixture made inside one second, a clock skew, or `--committer-date-is-author-date` defeats | Rejected |
| **A14** Refuse the wrong verdict at its commit. `pre-commit` reads each staged `seal/specs/<id>/guarantee.md`; where it reads one `sealed` whose `Target SHA` names a commit HEAD does not hold (unresolved, or not an ancestor), and the item's `Branch` row names the current branch, the commit is refused with the way on: a new audit of the sealer at HEAD. **As phase 6 found it must be completed:** the gate records the refusal it made, and `_queue_one`'s chain refusal skips a `sealed` this clone recorded, because the new audit keeps the refused verdict on its row. `sealed_before`, the ancestry refusal and `post-commit` are #975's | Where the stub does not judge, the wrong `sealed` lands and the gap stays for that item: a foreign hooks slot, `--no-verify` (the backstop judges the arms alone), a plugin older than this release, a person's own commit with no session, a clone no session has reached. Each is a missing stamp, Q8's direction, and `seal-stamp --from` cannot repair it because nothing was queued; the repair is a new audit, which the pull request's check forces anyway in shared mode. A sealer whose row is wrong twice meets the refusal twice, and the orchestrator reads it twice. One `git diff --cached --name-only` is added to every judged commit, and one `git show` plus the `chain_check.py` import to a commit that stages a guarantee (`questions.md` Q7 measures it) | **Chosen.** It closes round 4's `deadbee` shape and the off-branch shape in the clone that commits them, which in this repository's flow is the orchestrator's own clone and the only clone that ever commits a verdict. It leaves no per-clone inference for a git operation to defeat, because the fact it reads is the commit's own history at the moment the commit is made, and that history is what the commit will carry everywhere. Round 1's three copy shapes and round 2's two shapes each either are refused (a wrong row on the declared branch) or land and queue nothing by #975's rules (a copy onto another branch), with no record in either |
| **A15** Keep A11 with round 2's two guards: read the verdict on the other ref (finding 1) and withhold where no ref contains the resolved target (finding 2) | The next shape in the same class, read from the tree: the branch pushed with a `sealed` that drew, the base moved, the branch rebased, so the tracking ref holds a `sealed` over the old target; then the sealer writes a wrong row. The verdict-reading guard finds a `sealed` on another ref and withholds the record, and the repair of that wrong row in the orchestrator's own clone draws nothing. That is round 2's finding 1 with `sealed` in place of `withheld`, and it is this repository's own flow. Each guard reads one more fact of the clone to approximate "did any clone draw", and rounds 1 and 2 are two guards and two new paths | Rejected. The structure, not the guard count, is what each round found (`CLAUDE.md` §*The rule a mechanism is kept against*) |
| **A16** Remove A11 and state the gap as a limit | The owner rejected a stated limit on 2026-10-19 ("한계만 적으면 계속 공백인 거잖아"), and the cost is concrete: round 4's measured shape, a wrong row in the orchestrator's clone, leaves the work item unstamped with nothing to draw by hand, since no values file exists. What the owner asked is whether anything cheaper than A11 closes the common case; A14 does, with less code than A11 and no new reader at read time | Rejected as the mechanism; its words are what A14's limits keep for the cases the stub cannot reach |
| **A17** Record "stamped" or "refused" where every clone reads it: `pre-commit` writes a line under the verdict into the index's `guarantee.md`, or `post-commit` writes it into the working tree for the next commit to carry | A positive marker ("drawn") makes its absence read as "not drawn", so every `sealed` committed under a plugin without the marker, and every work item in flight across the upgrade, draws again on its re-seal: the doubled direction Q8 forbids. A negative marker ("refused") written into a copy of a guarantee that drew on its own branch (`merge --squash` onto `main`, then a plain commit) says the verdict never drew, which is false, and the re-seal there draws twice: round 1's shape again. Either marker has a hook rewrite the sealer's document, which the sealer's next run must preserve, and that is a change to `agents/sealer.md` and an evaluation. The post-commit form leaves the working tree dirty after the orchestrator's commit | Rejected. A record that travels with the file is read everywhere, but it has to be written by the party that knows, and the only party that knows at a copy is the branch the copy came from |
| **A19** The refusal's way-on text tells the session to restore `guarantee.md` to HEAD's copy before the new audit, so the refused verdict never reaches the chain (phase 6's first candidate) | It is an act a session must perform between the refusal and the spawn, and `CLAUDE.md` §*The goal a design is chosen against* prefers the design that needs none. Where the sealer runs in the orchestrator's own worktree and the restore is skipped, the new audit keeps the refused run and the repair draws nothing, silently: the gap stays, and nothing in the tree can tell a restore that happened from one that did not. It also erases the only trace that a wrong audit was made. Where the sealer runs in a scratch clone the restore is moot, since a clone carries HEAD and not the working tree | Rejected. A written step to a session where a mechanism exists, and its failure is the gap itself |
| **A20** `agents/sealer.md` tells the sealer to list on its row only verdicts committed at HEAD, so an uncommitted refused run is never kept (the orchestrator's candidate) | A written rule to an agent in place of a mechanism, and a change to a definition that owes a run against #975's phase-4 side (about 4 USD, S9). A sealer that reads the working tree's row anyway, once, reopens the gap for that item with nothing to catch it. It erases the wrong audit's trace as A19 does | Rejected. The gate already holds the fact at the moment it is known; the rule would ask the sealer to re-derive it |
| **A21** Accept the repair drawing nothing as a stated limit (phase 6's third candidate) | The owner refused a stated limit for Q2, and this is round 4's measured shape in the orchestrator's own clone, the common case | Rejected, as A16 |
| **A18** The sealer writes the marker itself, or `git notes` carry it | The sealer cannot know whether a stamp was drawn, and a value it writes for that is an answer nobody gave. Notes are a ref each clone keeps and git neither pushes, fetches nor carries across a rebase by default, so they are the per-clone record of A11 keyed to a SHA the rewrite destroys | Rejected |

## Phases

Vertical slices, built test-first: each case is seen red against the tree as
it stands before the code that makes it green (contract §15). Phases 1 to 5
closed before the reframe and keep their commits; the shared-mode half of
phase 3 is what phase 7 takes out.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The local writer. Extract `_queue_one`'s values composition (`key` through `write_values`) into one helper both writers call, with no change to the shared cases. Add `queue_for_local_guarantee(path, session, now=None)` with S1–S5's refusals in `spec.md` §*Data & interfaces*' order. Fixtures build a local root under a main checkout and under a linked worktree, with `routing.md`'s `Branch` row and a real branch | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`: `test_a_local_mode_sealed_guarantee_queues_one_stamp`, `test_a_local_mode_withheld_or_undecided_guarantee_queues_nothing`, `test_a_local_mode_reseal_after_withheld_queues_the_stamp`, `test_a_local_mode_second_sealed_queues_nothing`, `test_a_local_mode_guarantee_off_its_branch_queues_nothing`, `test_the_edit_gate_leaves_shared_mode_to_post_commit` (writer half), each seen red first; the fourteen shared cases on §*The stamp*'s `Enforced by:` line green with their bodies untouched (S10) | b701bb53 |
| 2 | The gate. `hooks/sealer-stamp-queue.py` in `GROUPS["post-edit"]`, returning on a path that does not match before any `git` call or import, and printing the `systemMessage`. A `sealer-stamp-queue` row in both READMEs' hook tables, written now because the gate and its row ship together | `test_the_edit_gate_queues_a_local_mode_sealed_guarantee`, `test_a_subagents_write_queues_and_draws_nothing`, `test_the_edit_gate_is_silent_off_a_guarantee`, through `hooks/dispatch.py post-edit`; `test_the_main_sessions_stop_draws_each_undrawn_file_once` over a file this gate wrote; `tests/test_dispatch.py`, `tests/test_a_gate_that_fails_says_so.py` green; `test_both_readmes_list_the_stamp_hook` extended to the new row | bf996b89 |
| 3 | The refusal record (`questions.md` Q2 (b), A11). The two record functions in `seal_stamp.py` and the sibling directory `specseal-stamp-refused/`. The write in `_queue_one` at the ancestry refusal under the guards of `spec.md` S13 as it then read, and in the local writer at the branch-ancestry refusal where the branch exists. The skip in `sealed_before`, in `_queue_one`'s chain refusal and in the local writer's chain refusal | As the row read at a7572788; `phases/phase-3.md` records which guard turned which case red, and `overview.md` records guard 3 not built. Phase 7 removes the shared-mode half | 9ad38d66 |
| 4 | The words, each rewritten in place (contract §19), as the row read at a7572788: `docs/the-review-record.md` §*The stamp*, `skills/code-review/orchestration.md`'s stamp paragraph, `hooks/sealer-stamp.py:1-14`, `seal_stamp.py`'s comments and docstrings, both READMEs, `agents/sealer.md:99-100` and its pin, the changelog fragment | As the row read at a7572788; phase 8 rewrites the refusal record's sentences again | 12855a96 |
| 5 | The sealer measured, run by the orchestrator: one side of the sealer's behaviour cases at this branch, compared by `evals/scripts/noninferiority.py` with #975's phase-4 side, the record written as `evals/sealer-phase-5.md` and `.json` under this directory | `noninferiority.py check` exit 0 on the record; `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers` | 11b90191 |
| 6 | The refusal at the commit (A14, `spec.md` S11–S13). In `hooks/commitgate.py#pre_commit`, after `arms_missing` and before `_leave_mark`, one function over the staged paths: for each `seal_stamp.GUARANTEE_PATH` match, `git show :<path>`, the `chain_check.py` readers through `_stamp_module()._chain_check()`, the index's `routing.md` through `routing.parse`, `routing.current_branch(cwd)`, `git rev-parse --verify -q <target>^{commit}` and `git merge-base --is-ancestor <target> <head>`; the text's constants in `hooks/gate.py` beside `STATES` (`gate.HEADER` first, the file, the commit named, the branch, HEAD's short SHA, the way on, `gate.UNCHANGED` last; no question tool); exit 1 unless `_sequencer_commit`. Loaded only after a staged path matched; nothing on an unborn branch. `hooks/git/pre-commit.py`'s docstring gains the third thing it judges, in the same commit (contract §19) | New, each seen red at 339ac7dc: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit` (parametrized: unresolved target, off-branch target; asserts exit 1, `gate.HEADER` and the four named facts in the text, no question tool, HEAD and index unmoved, then the repaired row's commit queues one file), `…::test_the_guarantee_refusal_is_quiet_off_its_one_fact` (parametrized over S12's givens, the "stages no guarantee" given with the loader replaced by a recorder), `…::test_a_sealed_committed_past_the_stub_keeps_the_gap` (S13, `--no-verify`), `tests/test_the_commit_gate_decides_at_the_commit.py::test_a_sealed_the_branch_does_not_hold_is_stopped_inside_the_commit` (through the installed stubs); the module that pins the arms' texts extended to the new text; `tests/test_the_commit_gate_decides_at_the_commit.py` and `tests/test_the_hooks_are_installed_where_git_runs_them.py` green; the latency of a judged commit with and without the new listing, measured as #975's phase 2 measured it and written into the phase record (`questions.md` Q7) | de80c2c2 |
| 7 | The gate's record, `post-commit`'s record taken out, and the local line (`spec.md` S4, S10, S11, S13, S14, `## Removes`). First the record: in `hooks/commitgate.py#pre_commit`, where `guarantee_off_history` returned a text and `_sequencer_commit` is false, `seal_stamp.record_refusal(common, <id>, <target>)` is called before the text is written, the item and target being the ones the refusal named; `test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit`'s last assertions turn from "the repair queues nothing" to one values file and the record `<id>-<target>`, and `test_the_guarantee_refusal_is_quiet_off_its_one_fact` asserts no record for each quiet given. Then the removal, in `seal_stamp.py`: `PLAIN_COMMITS`, `plain_commit`, `_guarantee_on_another_ref`, `_stamped_nowhere_else` and the `record_refusal` call in `_queue_one` deleted; the `refused_here` skip in `sealed_before` deleted, so it reads as at 769f2aa4; the skip in `_queue_one`'s chain refusal kept; the record section's comment and the docstrings of `record_refusal`, `refused_here`, `_same_commit`, `queue_for_guarantee` and `sealed_before` rewritten to the two writers (the gate, the local writer) and the one shared reader (the chain refusal). `NOT_ON_BRANCH` added beside `QUEUED` and returned by the local writer at its branch refusal where the branch stands. The ten `post-commit` record cases and the fixtures only they call deleted; `test_a_refusal_record_skips_only_its_own_verdict` rewritten over `local_guaranteed`; `test_a_local_mode_guarantee_off_its_branch_queues_nothing` and `test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once` gain the line assertion; `test_a_refused_row_over_a_drawn_seal_does_not_draw_again` (S11's second case) and `test_a_sealed_committed_past_the_stub_keeps_the_gap` (S13, which phase 6 left for this commit) planted. `overview.md`'s divergence rows that describe guard 3 and the other-ref guard are closed by the builder, since the units they describe are gone | The repair's assertion seen red at de80c2c2 (where it pins the gap) before the record is written; `test_a_refused_row_over_a_drawn_seal_does_not_draw_again` seen red with `sealed_before` replaced by `False`; `test_a_sealed_committed_past_the_stub_keeps_the_gap` red until `post-commit`'s write goes; `test_a_local_mode_guarantee_off_its_branch_queues_nothing` and `test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once` seen red on the line; `test_a_refusal_record_skips_only_its_own_verdict` seen red with the matcher's floor deleted; the fourteen #975 cases and phases 1 and 2's nine cases green with bodies untouched (an AST comparison against 769f2aa4 for the fourteen); `bin/mutation-check` over the gate's record write, the chain skip, the local write site, the local skip and the line, one run each; `git diff --stat 769f2aa4 HEAD -- hooks/git/` naming `pre-commit.py` alone; `git grep -n -e plain_commit -e _stamped_nowhere_else -e _guarantee_on_another_ref -e PLAIN_COMMITS` exit 1 | |
| 8 | The words, each rewritten in place (contract §19), to the redesign (`spec.md` S7, S8): `docs/the-review-record.md` §*The stamp*, the second rule rewritten to the refusal at the commit in shared mode (pointing at `docs/the-commit-gate-inside-git.md`), which records what it refused, the record at the write in local mode, and the chain reader's skip in both, its `Enforced by:` line carrying phases 6 and 7's cases and none of the deleted ones, and the unchecked paragraph naming only the limits `spec.md` §*Scope* leaves, the Q9-class coincidence of `plan.md` §*Technical context*'s walk among them; `docs/the-commit-gate-inside-git.md`, a new rule under this item's marker stating the refusal beside the arms, what it reads, that it records the refusal under `<git-common-dir>/specseal-stamp-refused/`, what it does not judge, and that it is no arm, with its `Enforced by:` line, and the latency bullet gaining phase 6's figures (268 against 260 ms an ordinary commit, 310 against 283 ms a guarantee's); `skills/code-review/orchestration.md`'s sealer step (line 209's paragraph) gaining the sentence that a commit refused for a row naming a commit the branch does not hold is answered by spawning the sealer again at HEAD, never by editing the row; `hooks/sealer-stamp.py`'s docstring where it names the record; both READMEs' side-effect sentences (the record's directory, local mode) and the git-hooks row (the third refusal); `changelog.md`'s second entry in this directory; the pins: `test_the_policy_states_the_refusal_record_and_names_its_cases` rewritten, `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`'s `silence` tuple rewritten, `test_both_readmes_list_the_stamp_hook` extended, and a pin for the new rule in `docs/the-commit-gate-inside-git.md` where that document's test module keeps them. Also the mark's grammar, because this item's own `spec.md` ends with `Reframed 2026-10-19 by framer, after phase 6.` and `chain_check.REFRAME_RE` (`skills/code-review/scripts/chain_check.py:204`) reads `after round <N>` alone, so the pull request's check refuses this item's declaration at 8b685982's tree (executed by the framer, quoted in `questions.md` head item 12): `REFRAME_RE` and the refusal's sentence at `chain_check.py:1484` accept `after phase <N>.` beside `after round <N>.`, `docs/the-review-record.md` §*The run* gains the sentence that a build phase whose record says the frame does not hold goes back to the framer the same way and writes `after phase <N>`, `templates/sdd-spec.md`'s foot comment and `agents/framer.md` §*You have no interactive phase* name both shapes, and `tests/test_chain_check.py` gains the case that reads this item's own foot (seen red at 8b685982) | Each pin seen red against the documents at the start of the phase; `bin/rules --check` exit 0; `tests/test_docs_line_wrap.py`, `tests/test_one_word_one_meaning.py`, `tests/test_no_real_identifiers.py` green; S8's two `git grep` runs as stated; `git diff --stat 11b90191 HEAD -- agents/` empty (S9) | |

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

- No migration, environment variable or dependency. `hooks/hooks.json` and
  `hooks/git/` are unchanged: the refusal runs inside the `pre-commit` stub
  the installer already writes.
- Every `Write` and `Edit` in every repository runs one more gate in the
  `post-edit` group. It returns on the path's shape before any `git` call or
  import.
- Every judged commit in an opted-in clone now lists its staged paths once
  (`git diff --cached --name-only`), where before only a commit the parity
  arm asked about did. A commit that stages a work item's `guarantee.md`
  reading `sealed` pays one `git show`, the `chain_check.py` import, one
  `git rev-parse` and one `git merge-base` more. Phase 6 measures both
  against `docs/the-commit-gate-inside-git.md`'s latency bullet
  (`questions.md` Q7).
- The refusal record's directory, `<git-common-dir>/specseal-stamp-refused/`,
  is written by `pre-commit` at a refused commit in shared mode and by the
  local writer at a refused write in local mode, from phase 7; `post-commit`
  writes it no more. A shared-mode clone that wrote files under 339ac7dc's
  `post-commit` keeps them, and the chain reader still honours them for the
  item and target they name; nothing prunes them, the stance
  `specseal-stamp/` has.
- The installed gate is not the tree. This work item's own run draws its
  stamp and judges its commits through the plugin cache's 0.22.1 hooks, so
  no run here exercises the new refusal or the local trigger end to end. The
  first real refusal is read by the owner after updating to the release
  that carries this work (`spec.md` S7's unchecked sentence; `overview.md`
  §*Not verified*).
