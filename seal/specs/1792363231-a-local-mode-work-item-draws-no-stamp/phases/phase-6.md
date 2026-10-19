# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 6

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | de80c2c2 |


## What this phase was asked

The orchestrator spawned the smith after the reframe at d33e1021, with
`plan.md` approved for phase 6 at 37f96f7a and `questions.md` Q5 answered
(a), no waiver. The phase was to build the refusal at the commit (`plan.md`
A14, `spec.md` S11 to S13):

- one function in `hooks/commitgate.py#pre_commit`, after `arms_missing`
  and before `_leave_mark`, reading each staged guarantee from the index
  and exiting 1 where it holds one `sealed` whose `Target SHA` HEAD's
  history does not hold, on the branch the item's `Branch` row names;
- skipped on `_sequencer_commit`, and loading nothing where no guarantee
  is staged;
- the text running from `gate.HEADER` to `gate.UNCHANGED` and naming the one
  way on, the sealer's new audit at HEAD, with no waiver;
- cases first, each seen red: the refusal's shapes (S11), every quiet case
  (S12, round 1's three copy shapes among them), the `--no-verify` limit
  (S13), and one case through the installed stub;
- the latency measured as #975's phase 2 measured it (Q7), and the index
  read under `commit -a` and a pathspec commit (Q6), both recorded here.

Phases 7 and 8 were to follow unless a phase's frame did not hold.

## What this phase found

**The frame does not hold at S11's last clause, so the work stops after
this phase.** S11 says the commit after the refusal, "whose row names HEAD,
lands and draws the work item's one stamp". It lands, and it draws nothing.
The sealer's new audit keeps the refused verdict on its row as `; earlier
run: <sha> sealed` (`agents/sealer.md` §*Rules*, "keeps the earlier verdict
on the `Target SHA` row"). `_queue_one`'s chain refusal counts every earlier
`sealed` that no refusal record names. Because `pre-commit` stops the wrong
row, `post-commit` never runs for it, and no record is written. The chain
then reads the refused verdict as the stamp it never drew.

This is the #975 Q7 gap again, in round 4's measured shape and in the clone
that commits it. Before this phase, the same shape drew once, because the
wrong row landed and phase 3's record skipped it. Phase 7, as framed, takes
the record out of shared mode altogether, so it keeps the gap open.

Executed at 37f96f7a by a probe, run once and deleted:

| Shape | Values files after the repair | Records |
|---|---|---|
| The wrong row over `deadbee` lands, then the repair keeps `; earlier run: deadbee sealed` | 1 | `1799000000-deadbee` |
| The wrong row is never committed, as the refusal leaves it, then the same repair | 0 | none |

`test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit`
pins the second row as a limit, the way S13 pins its own: the repair lands,
`post-commit` says nothing, and nothing is queued. The change that closes
the gap turns that assertion red. Choosing the change is a decision for the
framer or the owner, because each candidate rewrites part of the frame:

- The refusal's way on could restore the guarantee to what HEAD holds before
  the new audit. The sealer's earlier verdict would then be HEAD's, and the
  refused one would never reach the chain. This is S3's re-seal-after-withheld
  shape, which `test_a_reseal_after_withheld_queues_the_stamp` already shows
  drawing. It costs the text's way-on sentence, the orchestration sentence
  phase 8 writes, and any trace of the refused audit on the row.
- `pre-commit` could write the refusal record when it refuses, and phase 7
  could keep the `refused_here` skip in shared mode's chain reader. The
  record would then stand only where the verdict never entered this clone's
  history, which is the fact the post-commit guards of rounds 1 and 2 could
  not establish. It brings back a per-clone record in shared mode, and a
  repair committed in another clone would still draw nothing.
- The gap could be accepted as a stated limit. The owner refused that for Q2.

**What was built holds on its own (executed).** `guarantee_off_history`
reads each staged `seal/specs/<item>/guarantee.md` and the item's
`routing.md` from the index. It refuses where the guarantee reads one
`sealed`, the `Branch` row names the current branch, and `git merge-base
--is-ancestor <target> HEAD` does not exit 0. The text lives in
`hooks/gate.py` as `GUARANTEE_STATE` and `GUARANTEE_WAY_ON`, rendered by
`guarantee_refusal`. `pre_commit` lists the staged paths once for the arms
and the refusal together. A reading that raises, such as a `seal_stamp.py`
that will not load, stops nothing, because the pull request's check refuses
the same file.

**Where the build departs from the phase row.**

- `seal_stamp.GUARANTEE_PATH` is not used. Matching with it means loading
  `seal_stamp.py`, which S12 forbids for a commit that stages no guarantee.
  The item is therefore taken from a prefix and suffix test before anything
  is loaded. After that test, the match decided nothing a case could see:
  an item with no declaring `routing.md` beside it is not judged anyway.
- `git rev-parse --verify -q <target>^{commit}` is not run. `merge-base
  --is-ancestor` exits 128 for a target that does not resolve and 1 for one
  off the branch, so one call answers both.
- `hooks/git/pre-commit.py`'s docstring now names the third thing the hook
  judges, as the phase row asks (contract §19). That leaves `git diff --stat
  769f2aa4 HEAD -- hooks/git/` non-empty, where S10 and phase 7's row
  expect it empty. Only the docstring changed. The orchestrator owns
  `overview.md`'s divergence row for it, because the phase row did not ask
  this phase to write `overview.md`.
- S13's case, `test_a_sealed_committed_past_the_stub_keeps_the_gap`, is not
  planted. At this tree `post-commit` still writes a record for a wrong row
  committed past the stub, so the repair draws once. A case asserting no
  record and no draw is red until phase 7 removes the shared write, and it
  belongs to that commit.
- The S12 quiet givens pass at 37f96f7a by nature, because `pre-commit`
  refused nothing there once the arms were quiet. Each was seen red by
  mutating the unit it holds (below). Red at 37f96f7a: S11's two shapes, the
  stub case's four refused shapes, and the loader control in S12's
  `the target is HEAD` given.

**Q6, answered (executed on git 2.50.1, Apple Git-155, through the stubs
`hooks/hook-install.py` wrote).**
`tests/test_the_commit_gate_decides_at_the_commit.py::test_a_sealed_the_branch_does_not_hold_is_stopped_inside_the_commit`
is refused for `git add` then `git commit`, for `git commit -a`, and for
`git commit -- <path>`. A `sealed` staged and then put back to `withheld` on
disk is refused too, so the index is what is read. A pathspec commit of
another file lands, and the guarantee stays staged, because git's temporary
index for that commit does not carry it. CI's other legs run the same case.

**Q7, measured (executed).** The method was #975's phase 2: one fixture
clone per plugin copy, the stubs installed, a declaration in force, 12
`git commit` calls of each kind, the first dropped, medians of the other 11.
Git was 2.50.1 on this machine, not under load.

| Commit | Without the refusal (37f96f7a) | With it (de80c2c2) |
|---|---|---|
| An ordinary change | 260 ms | 268 ms |
| One staging a `sealed` guarantee over HEAD | 283 ms | 310 ms |

An ordinary judged commit pays about 8 ms, inside the spread of the 11
runs. That is the one `git diff --cached --name-only` now read on every
commit the arms let through, where before only the parity arm read it. A
guarantee's commit pays about 27 ms: `seal_stamp.py` and `chain_check.py`
loaded in `pre-commit`, two `git show` calls, one `rev-parse --abbrev-ref`,
one `merge-base` and one `rev-parse --short`. The probe also showed that
the HEAD copy refused a row over `deadbee` and the 37f96f7a copy did not.
Its first run measured nothing: both fixtures' stubs named the first copy,
because `githooks` stayed cached in the probe's interpreter. That run was
discarded, and each copy's installer was run in its own interpreter.

**Mutations (executed, `bin/mutation-check`, one run each).** Eleven were
red. Two survived:

| Unit | Mutation | Verdict |
|---|---|---|
| Nothing judged on an unborn branch | guard deleted | red: `an unborn branch` loaded `seal_stamp.py` |
| The shape test before loading | `or True` | red: `no guarantee staged` |
| One `Verdict:` of `sealed` | the word test deleted | red: `withheld`, `undecided` |
| No `Target SHA` | guard deleted | SURVIVED |
| The `Branch` row names this branch | comparison made `False` | red: the three copy shapes |
| No declaration in the index | `not declared` deleted | SURVIVED |
| HEAD's history holds the target | test inverted | red |
| The sequencer's own commit | `_sequencer_commit` dropped | red |
| A failed reading stops nothing | catch narrowed to `ZeroDivisionError` | red |
| The guarantee read from the index | read from disk | red, once the `staged, then put back on disk` shape was added |
| The `routing.md` read from the index | read from disk | red: both index givens |
| The way on named | `spawn the sealer again at HEAD` deleted | red |
| The branch and HEAD named | clause deleted | red |

The two survivors guard the normal path of an item with no `Target SHA` or
no declaration. Without them, a `TypeError` is raised, and
`_guarantee_refused`'s catch turns it into the same silence. So no case can
tell either guard from its absence. They stay, so that a common input does
not travel through an exception. The memoised listing and the arms-first
order were not mutated, because no observable output depends on them.

**Narrow runs (executed, `bin/test <module> -q`, one module a command).**
`test_the_stamp_reaches_the_person_it_is_drawn_for.py` 107 passed,
`test_the_commit_gate_decides_at_the_commit.py` 184,
`test_the_hooks_are_installed_where_git_runs_them.py` 23,
`test_the_hook_surface_git_offers.py` 12, `test_dispatch.py` 10,
`test_one_word_one_meaning.py` 26,
`test_every_reader_ends_a_line_where_gfm_does.py` 28,
`test_a_script_says_which_interpreter_it_needs.py` 6,
`test_no_real_identifiers.py` 6, each exit 0. One earlier parallel run of
the installer module failed once, on
`test_a_clone_that_does_not_opt_in_gets_nothing_and_loses_ours[no seal root]`,
and passed serially and in parallel on two reruns. `ruff check` and `ruff
format --check` passed on the five files changed. The full suite is
unverified here, and the orchestrator's broad gate answers it.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
