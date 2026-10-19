# 1792363231-a-local-mode-work-item-draws-no-stamp — phase 7

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 2759a60d |


## What this phase was asked

The orchestrator resumed the smith after the framer's correction at
59c65527, which took candidate 2 of `phases/phase-6.md`. It approved the
correction at 1e956838. The phase was to build `plan.md` row 7 as it reads
there:

- the commit gate records the refusal it makes;
- `post-commit`'s record and its guards are taken out, `sealed_before` goes
  back to #975's reading, and the shared chain reader keeps its
  `refused_here` skip;
- the local writer says `NOT_ON_BRANCH` at its branch refusal;
- the ten `post-commit` record cases go, and S11's second case and S13's
  case are planted;
- round 2's two findings are closed with `fixed <phase-7 commit>` and their
  `answer:` lines;
- `overview.md`'s guard-3 and other-ref rows are closed as the units go.

## What this phase found

**The corrected frame holds (read, then executed).** The gate's record is
written for a row that `pre-commit` refused and that never became history.
I read the path walk in `plan.md` §*Technical context* against the code, and
each of round 2's two shapes now runs as a case (below).

**What was built (executed).**

- In `hooks/commitgate.py`, `guarantee_off_history` returns the text, the
  work item's id and the target. `pre_commit` records the refusal through
  `_record_refusal` before it writes the text, unless `_sequencer_commit`.
  A record that cannot be written leaves the refusal standing.
- In `skills/verify/scripts/seal_stamp.py`, these are deleted: `PLAIN_COMMITS`,
  `plain_commit`, `_guarantee_on_another_ref`, `_stamped_nowhere_else` and the
  record write in `_queue_one`. `sealed_before` is back to its 769f2aa4
  signature and body. `_queue_one`'s chain refusal keeps its skip. The
  local writer returns `NOT_ON_BRANCH` where the branch stands. The once
  comment, the record section's comment and five docstrings now name the two
  writers and the chain readers.
- `hooks/git/pre-commit.py`'s docstring says the hook leaves a record when
  it refuses. `git diff --stat 769f2aa4 HEAD -- hooks/git/` names that file
  alone.

**Where the build departs from row 7.**

- §*The stamp*'s second rule, its `Enforced by:` line and its pin
  (`test_the_policy_states_the_refusal_record_and_names_its_cases`) were
  rewritten in 061dfdc2, not in phase 8. Deleting the ten cases left eight
  `Enforced by:` targets that did not resolve (`bin/rules --check` exit 1).
  The pin also asserted the deleted names and the guards' words, so contract
  §19 put the paragraph in the same commit. The pin was seen red against
  1e956838's paragraph first.
- §*The stamp*'s first rule still said that the history reader skips a
  refused `sealed`. It also still carried the double-stamp class round 2's
  finding 2 named at `docs/the-review-record.md:301-303`. cf0e60e8 rewrites
  both, and the pin in
  `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`
  was seen red first.
- Two cases beyond the row run round 2's own shapes under the gate's record
  (2759a60d), so the two `fixed` verdicts rest on executed shapes. Each was
  red at 1e956838: its tree was exported to the scratchpad and the case file
  run against it, then the copy was removed.
  - `test_a_tracking_ref_left_by_a_rebase_withholds_nothing` is finding 1.
    At 1e956838 the gate recorded nothing.
  - S12's `cherry-pick -n of a commit no ref holds` is finding 2. At
    1e956838 `post-commit` wrote a record and the re-seal drew a second
    stamp.
- `test_a_refusal_record_skips_only_its_own_verdict` now has three local
  givens. A row cannot spell a SHA shorter than seven characters, because
  `chain_check.SHA_RE` reads seven or more. So the floor given is a
  six-character record of which the row's SHA is an extension.
- The fixtures were kept where kept cases call them: `off_branch_commit`,
  `refusals`, `a_fix` and `seal_and_commit`. `rebased_and_cloned_fresh` and
  `resealed_draws_nothing` were deleted.
- Row 7's check `git grep -n -e plain_commit … -e PLAIN_COMMITS` cannot exit 1
  over the whole tree. Released round records and this item's own records
  quote the names, and `test_a_plain_commit_carries_no_chdir` contains the
  substring. Over `hooks skills tests` with `-w` it exits 1.

**Seen red (executed).**

| Case | How |
|---|---|
| S11's two shapes, record and repair | at the code before the change: no record (`[] == ['1799000000-deadbee']`) |
| `test_a_refused_row_over_a_drawn_seal_does_not_draw_again` | before the change, no record; with `sealed_before` returning `False`, a second stamp |
| `test_a_sealed_committed_past_the_stub_keeps_the_gap` | before the change, `post-commit` wrote a record |
| `test_a_local_mode_guarantee_off_its_branch_queues_nothing`, two givens | before the change, `NOT_ON_BRANCH` did not exist |
| `test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once` | before the change, the writer returned `[]` |
| `test_a_refusal_record_skips_only_its_own_verdict` | `_same_commit`'s floor replaced by `False` |
| the two round 2 shapes | at 1e956838's tree, as above |

**Mutations (executed, `bin/mutation-check`, one run each, all red).**

| Unit | Turned red |
|---|---|
| The gate's record write, replaced by `pass` | S11's two shapes, S11's second case |
| The shared chain skip deleted | S11's two shapes |
| The local write site deleted | the local refused-then-resealed case |
| The local chain skip deleted | the same |
| `NOT_ON_BRANCH` returned as `[]` | the two local off-branch givens, the local refused case |
| `sealed_before` returning `False` | S11's second case |
| `_same_commit`'s floor replaced by `False` | the six-character given |
| The branch-standing check deleted | `a branch the clone no longer holds`, the local refused case |

**S10's AST comparison (executed, a probe run once and deleted).** The
fourteen cases on §*The stamp*'s first `Enforced by:` line at 769f2aa4 are
unchanged node for node. Against bf996b89, with docstrings set aside,
phases 1 and 2's nine cases are unchanged but one. That one is
`test_a_local_mode_guarantee_off_its_branch_queues_nothing`, which row 7
asks to gain the line. Every one of the nine has a docstring changed in
phase 4, when `#976` became the work item's id.

**Narrow runs (executed, `bin/test <module> -q`, one module a command).**
`test_the_stamp_reaches_the_person_it_is_drawn_for.py` 101 passed,
`test_the_commit_gate_decides_at_the_commit.py`,
`test_the_hooks_are_installed_where_git_runs_them.py`,
`test_the_hook_surface_git_offers.py`, `test_dispatch.py` and
`test_docs_line_wrap.py` each exited 0. `bin/rules --check` exited 0, with
all 514 `Enforced by:` targets resolving. `bin/unverified-check --baseline
origin/fix/976-a-local-mode-work-item-draws-no-stamp` exited 0. `ruff check`
and `ruff format --check` passed on the changed Python files. The full suite
is unverified here, and the orchestrator's broad gate answers it.

<!-- #107, #121: what a phase discovers reaches the next phase only if the
orchestrator retypes it by hand into the next spawn prompt, and it goes
missing without a trace when the orchestrator doesn't. This section is that
discovery's durable, committed home instead.

What a work item takes out of the tree is not recorded here. It is named
once, at the frame, in `spec.md`'s `## Removes` section, which the review
reads against the diff (#835). A
removal this phase made that the frame did not name is a divergence, and it
goes where divergences go: `overview.md`. -->
