# Feature Specification: a local-mode work item draws no stamp (#976)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #976's body and its comment | Asked: a trigger for a local-mode work item that draws the stamp once, from the sealer's `sealed`, and never from the broad gate's run. Carried by the comment: #975's `questions.md` Q7 gap, a `sealed` over a commit the branch does not hold, after which the work item draws no stamp. Both rank above every file below |
| #975's comment (the owner, 2026-10-18) and `docs/the-review-record.md` §*The stamp* | The stamp means every party verified the work item, the sealer last. It is drawn once per work item from `guarantee.md` reading `sealed`, never from the broad gate's run, never twice. Where the two directions conflict, never twice wins over never missing (#975 `questions.md` Q8, answered 2026-10-18 under the owner's delegation). This work applies that rule to local mode and does not reopen it |
| `skills/agent-contract/SKILL.md` §11, `docs/one-root-by-lifetime.md:307-322` (the local/shared table) | In local mode the root is `$(git rev-parse --git-common-dir)/seal/`, nothing under it is committed, and a repository with both roots is shared. So no `post-commit` can carry a local-mode `guarantee.md`, and the values directory `<git-common-dir>/specseal-stamp/` lives in the same common directory as the local root |
| `CLAUDE.md` §*The goal a design is chosen against* | Between two triggers that draw the same stamp, the one that needs no act of a session wins. This is why #975 put the trigger in a hook, and it rules out a command the orchestrator must remember (`plan.md` A6) |
| `CLAUDE.md` §*The rule a mechanism is kept against*, contract §19 and §20 | The replacement of `post-commit` for both modes was weighed as an equal of a trigger beside it (`plan.md` A2). The sentences that state "local mode draws no stamp" and "the gap #976 carries" are rewritten where they stand, in the same commit as the code that makes them false |
| `skills/settle/SKILL.md:45-46` (*It refuses to run in local mode*) | `settle` never retires a local-mode work item, so every `sealed` guarantee a local-mode clone ever wrote still stands under its root. A trigger that scans the root would draw all of them at once (`plan.md` A3) |
| `agents/sealer.md:36` and `skills/code-review/orchestration.md:221-225` | The sealer works in the clone its prompt names, which can be a `git clone` of the branch worktree. A trigger keyed on where the sealer writes would queue in that clone's git directory, where no main session draws (`plan.md` A2's failure) |
| `hooks/hooks.json` (`PostToolUse`, matcher `Write\|Edit\|NotebookEdit`, group `post-edit`) and `hooks/session-lease.py`'s docstring | The `post-edit` group already runs after every file edit, and a gate in it resolves the repository from the edited file's path, not from `cwd`. The new trigger joins that group and needs no new harness event |
| `hooks/sealer-stamp.py` docstring §*Only the main session's `Stop`* (#400 `questions.md` Q2, measured 2026-09-28) | A subagent's hook payload carries the parent's `session_id`. This work relies on the same holding for a subagent's `PostToolUse`, and `questions.md` Q1 is the measurement that confirms it |
| `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_the_hook_is_registered_for_stop_and_nothing_else` | The drawing hook answers `Stop` alone. The queueing gate is therefore a separate file in `post-edit`, and this test stands unchanged (`plan.md` A9) |
| #957's `spec.md` §*How the rewrite is proved not worse*, `evals/README.md` | An agent whose read set changed is measured again under `noninferiority.py`'s five rules, against the latest side and never an absolute. `agents/sealer.md` changes by one word (S9), so the sealer is measured against #975's phase-4 side |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A hook's output and what a person reads change: the top rung, which is why this frame exists |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` table below, read by the review against the diff |

## Scope

**In.**

- A `post-edit` gate, `hooks/sealer-stamp-queue.py`, registered in
  `dispatch.GROUPS["post-edit"]`. After a `Write` or `Edit` whose
  `file_path` is a local-mode root's `specs/<id>/guarantee.md`, it calls the
  local writer below. A `sealed` verdict then queues one values file for the
  payload's session, and the main session's `Stop` draws it with the
  unchanged `hooks/sealer-stamp.py`.
- A local writer in `skills/verify/scripts/seal_stamp.py`,
  `queue_for_local_guarantee(path, session, now=None)`, sharing the
  verdict reading, the row building and `write_values` with the shared-mode
  writer. Once per work item in local mode is held by four facts (S3, S4).
- The words: `docs/the-review-record.md` §*The stamp* (the drawing rule and
  the unchecked paragraph), `skills/code-review/orchestration.md`'s stamp
  paragraph, `hooks/sealer-stamp.py`'s docstring, `seal_stamp.py`'s
  comments and docstrings, both READMEs' hook tables and side-effect
  sentences, and `agents/sealer.md:99-100` with the test that pins it.
- The #975 Q7/Q8 gap the issue's comment carries. It stays a stated limit
  (`questions.md` Q2's default), and each sentence that hands it to #976 is
  rewritten to say it is a stated limit.
- The sealer measured once against #975's phase-4 side, because one word of
  its definition changes.

**Out, and why.**

- Shared mode's trigger. `post-commit` and its once rules
  (`seal_stamp.queue_for_guarantee`, `_queue_one`, `sealed_before`,
  `already_queued`) keep their behaviour. A replacement for both modes was
  weighed and rejected (`plan.md` A2). The only shared-mode change is that
  the values composition moves into a helper both writers call, so the
  shared cases must stay green byte for byte (S10).
- A clone whose git hooks slot is somebody else's, in shared mode. #975's
  `plan.md` A3 left it a stated silence. The new gate could reach it, but in
  shared mode it would key on the clone the sealer writes in, which is
  A2's failure. It stays as §*The stamp* states it.
- A mechanism that closes the Q7/Q8 gap, for example by patch-equivalence of
  the earlier verdict's target (`plan.md` A8). `questions.md` Q2 holds the
  owner's say, and the default builds none.
- The amend or rewrite of a sealing commit in a second clone (#975
  `questions.md` Q9). It is a shared-mode limit and unchanged here.
- A `guarantee.md` that reaches a local root other than through `Write` or
  `Edit`, such as a shell write, `seal import`, or `seal mode local` moving a
  shared root back. Nothing is queued for it. That is a missing stamp, never
  a false one, and it is stated in §*The stamp* (S7).
- `seal mode shared` moving a local root into the tree. The commit that adds
  the root carries every `guarantee.md` at once, and `post-commit` reads each
  one with the shared rules. That is #975's behaviour at a mode switch. It is
  not a local-mode trigger, and `plan.md` §*Technical context* names it for
  the orchestrator to file if a run shows it.
- Every other place `skills/code-review/orchestration.md` tells the
  orchestrator to commit a record that local mode cannot commit (line 209's
  `Commit guarantee.md`, line 187's `commit broad-gate.md`). That is the
  orchestration's local-mode wording as a whole, not the stamp's trigger.
- `agents/warden.md`, `agents/smith.md`, `agents/framer.md`,
  `agents/scribe.md` and `skills/agent-contract/SKILL.md`. None of them names
  the stamp's trigger (`git grep -n -F stamp -- agents/ skills/agent-contract/`
  at 769f2aa4 hits `agents/sealer.md:99-100` alone), so no other agent is
  measured.

## User scenarios & acceptance *(mandatory)*

One row per scenario. These become the review's stage-1 checklist and the
regression tests' skeleton. "A local-mode item" below means a repository with
no `<repo>/seal/` and a root at `<git-common-dir>/seal/`, holding
`specs/<id>/routing.md` with a `Branch` row and `specs/<id>/guarantee.md`.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A local-mode `sealed` written queues one stamp | Given a local-mode item whose `guarantee.md` reads one `Verdict:` of `sealed`, whose `Target SHA` row names `<sha> against <base>` with no earlier run reading `sealed`, and whose `<sha>` is an ancestor of the `Branch` row's `refs/heads/<branch>`. When `queue_for_local_guarantee(<that path>, <session>)` runs, then one values file `<ns>-<id>-<sha>.json` is written under `<git-common-dir>/specseal-stamp/<session>/` and one line is returned, `QUEUED` formatted with the id and the file. The main session's `Stop` draws that file once | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_a_local_mode_sealed_guarantee_queues_one_stamp` (new, seen red: `seal_stamp` at 769f2aa4 has no local writer); `::test_the_main_sessions_stop_draws_each_undrawn_file_once` over the file it wrote. Protects: #976, a sealed local-mode work item that never draws |
| S2 `withheld` and `undecided` queue nothing in local mode | Given the same item with `Verdict: withheld — …` or `undecided — …`, or two `Verdict:` lines, or an unfilled template, then no file is written and no line returned | `…::test_a_local_mode_withheld_or_undecided_guarantee_queues_nothing` (new). Protects: the finished-work stamp over unfinished work |
| S3 A re-seal after `withheld` draws then, and a second `sealed` draws nothing | Given a `Target SHA` row reading `<sha2> against <base>; earlier run: <sha1> withheld` and a `sealed` verdict, one file is queued. Given a row whose `; earlier run:` chain reads `sealed`, or a values file `*-<id>-*.json` or `.drawn.json` already standing under any session's directory of the clone, nothing is queued | `…::test_a_local_mode_reseal_after_withheld_queues_the_stamp`, `…::test_a_local_mode_second_sealed_queues_nothing` (both new). Protects: #975's never twice, in local mode, where the root and the values directory share one common directory and so the values files are a complete record |
| S4 A verdict over a commit off the work item's branch draws nothing | Given a `sealed` whose `Target SHA` does not resolve in the clone, or is not an ancestor of `refs/heads/<Branch row>`, or whose item has no `routing.md`, no `Branch` row, or a branch the clone no longer holds, then nothing is queued | `…::test_a_local_mode_guarantee_off_its_branch_queues_nothing` (new, one case per given, parametrized). Protects: a stamp for a work item merged and deleted long ago, drawn the first time anyone edits its old guarantee. `settle` never retires local-mode items, so these guarantees stay under the root |
| S5 Shared mode is not the gate's | Given a `Write` to `<repo>/seal/specs/<id>/guarantee.md` reading `sealed`, or to `<git-common-dir>/seal/specs/<id>/guarantee.md` in a repository that also has `<repo>/seal/` (shared, contract §11), then the gate queues nothing. `post-commit` stays the shared trigger | `…::test_the_edit_gate_leaves_shared_mode_to_post_commit` (new). Protects: two stamps for one shared-mode verdict, one at the write and one at the commit |
| S6 The gate runs in `post-edit`, is silent elsewhere, and says the line to the person | Given a `PostToolUse` payload for `Write` or `Edit` whose `tool_input.file_path` is S1's path, when `hooks/dispatch.py post-edit` runs, then the values file is written and stdout is one JSON object whose `systemMessage` is S1's line. A payload carrying `agent_id` (the sealer's own `Write`) queues the same file, since queueing is not drawing. Given any other path, a `NotebookEdit`, a payload that is not JSON, or no `session_id`, then it prints nothing, writes nothing, and runs no `git` and imports no `seal_stamp.py` before the path's shape has matched | `…::test_the_edit_gate_queues_a_local_mode_sealed_guarantee`, `…::test_a_subagents_write_queues_and_draws_nothing`, `…::test_the_edit_gate_is_silent_off_a_guarantee` (all new, through `dispatch.py`); `tests/test_dispatch.py` green. Protects: a gate in a group that runs on every file edit in every repository costing that edit a `git` call |
| S7 The documents say where the stamp comes from in each mode | Given `docs/the-review-record.md` §*The stamp*, then its rule says the stamp is queued at the commit of `guarantee.md` in shared mode and at the `Write` or `Edit` that leaves it reading `sealed` in local mode, with the four local facts of S3 and S4. Its unchecked paragraph no longer names local mode among the places nothing is queued. It names instead a local guarantee that arrived by a shell write or `seal import`, and a verdict over a commit off the item's branch, and it says the line reaches the person as the edit hook's message and that nobody has watched it on a screen. `skills/code-review/orchestration.md`'s stamp paragraph says the same for local mode: the stamp is drawn at the end of the turn in which the sealer's report arrives, and the line to quote is the edit hook's message. Both READMEs carry a `sealer-stamp-queue` row and say the stamp is queued at the commit or, in local mode, at the write | `…::test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does` with its `silence` tuple rewritten (red against the paragraph at 769f2aa4); `…::test_the_orchestrator_is_told_the_stamp_is_drawn_for_it` and `…::test_both_readmes_list_the_stamp_hook` extended; `bin/rules --check` exit 0; `tests/test_docs_line_wrap.py`. Protects: a reader told local mode draws no stamp after it does |
| S8 The gap is named a stated limit, not a pointer to a closed issue | Given the tree after this work, `git grep -n "#976"` hits no file outside this work item's directory, #975's released work item directory and the released `changelog/0.22.1.md`. `docs/the-review-record.md` and `seal_stamp.py`'s once comment, `queue_for_guarantee` and `sealed_before` docstrings each say the work item then draws no stamp, a stated limit, because the history cannot tell that `sealed` from one stamped before a rebase | `…::test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does` asserts the paragraph carries `a stated limit` beside `already read \`sealed\`` and no `#976`. Protects: a pointer to an issue that this work closes, read later as an open promise |
| S9 The sealer is told, and proved not worse | Given `agents/sealer.md`, its `## Never` bullet reads `a stamp is drawn once from your \`sealed\`.` (the word `committed` goes, since a local-mode verdict is never committed). Given phase 4, `evals/sealer-phase-4.md` under this item reads `pass` under the five rules against #975's `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/evals/sealer-phase-4.json`, or `fail` on rule 4 or 5 alone with the cause named | `…::test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it` with its pinned clause rewritten; `tests/test_the_sealer_guarantees.py::TestDefinition`; `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`; `noninferiority.py check` exit 0. Protects: a definition changed and never measured (#967 guard 1) |
| S10 Shared mode draws exactly what it drew | Given the helper both writers now call, the shared-mode cases of `docs/the-review-record.md` §*The stamp*'s `Enforced by:` line pass unchanged, with no edit to their bodies, and `hooks/git/post-commit.py`'s bytes are unchanged | the fourteen cases named on that `Enforced by:` line, untouched; `git diff --stat 769f2aa4 HEAD -- hooks/git/ hooks/commitgate.py` empty. Protects: ten review rounds of #975's once rules regressing under a refactor |

## Data & interfaces

- **The local writer**: `seal_stamp.queue_for_local_guarantee(path, session,
  now=None)` returns a list of zero or one lines. It does five things.
  - It resolves `path` with `os.path.realpath` and requires it to be
    `<common>/seal/specs/<id>/guarantee.md`, where `<common>` is a git
    common directory and `optin.home_at` for that repository answers
    `<common>/seal`. That rules out shared mode and a repository with both
    roots.
  - It reads the file from disk and judges it with `chain_check.py`'s
    readers (`verdicts_of`, `verdict_word`, `target_of`, `table_rows`,
    `field`, `earlier_verdicts`), the same calls `_queue_one` makes.
  - It reads the `Branch` row of `specs/<id>/routing.md` with
    `hooks/routing.py#parse`, which `chain_check.py` already loads as
    `ROUTING`.
  - It refuses in this order: no single `sealed`, no target, an earlier
    `sealed` in the row's chain, `already_queued(common, ident)`, then no
    `Branch` row or `git --git-dir=<common> merge-base --is-ancestor <target>
    refs/heads/<branch>` not exiting 0.
  - It writes with `write_values(common, session, values, now=now,
    key=f"{ident}-{target}")`.
- **The values**: the keys `_queue_one` writes, read from disk. `tree` is the
  target, `base` comes from the row, `branch` is the `Branch` row, and
  `from` and `pr` are None. `item` is the local item directory, `session` is
  the payload's, and `rows` is `guarantee_rows(target, branch, base, ident,
  run, rounds)`. `run` is `chain.newest_run` over `specs/<id>/broad-gate.md`
  read from disk. `rounds` is the count of `rounds/round-<N>.md` in the
  directory.
- **The shared helper**: the part of `_queue_one` from `key = …` to the
  `write_values` call becomes one function both writers call, taking the
  texts and the branch. The function's name is the work's. Its readers stay
  `git show HEAD:<path>` in shared mode and file reads in local mode.
- **The gate**, `hooks/sealer-stamp-queue.py`: it reads the payload, takes
  `tool_input.file_path` for `Write` and `Edit` only, and returns before any
  `git` call or `seal_stamp.py` import unless the normalized path ends in
  `/seal/specs/<segment>/guarantee.md`. It loads `seal_stamp.py` the way
  `commitgate._stamp_module()` does. It passes the payload's `session_id`.
  It prints `{"systemMessage": "<line>"}` where a line came back. It is
  silent on every failure, the shape `implementer-notice.py` and
  `post_commit` have.
- **Registration**: `dispatch.GROUPS["post-edit"]` gains
  `"sealer-stamp-queue.py"` after `session-lease.py`. `hooks/hooks.json` is
  unchanged, because the `post-edit` matcher already covers `Write` and
  `Edit`.
- **The line**: `seal_stamp.QUEUED`, unchanged, so both modes say one
  sentence.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The statement that local mode queues no stamp | `docs/the-review-record.md#"The stamp">"in local mode, where the \`seal/\` root sits under the git directory and no"` (lines 339-340) | §*The stamp*'s rule, which names the local trigger (S7); the paragraph names the local-mode silences that remain |
| The code comment saying the same | `skills/verify/scripts/seal_stamp.py:933-935` (`A local-mode root sits under the git directory and no commit ever carries it, so no stamp is queued there.`) | Rewritten in place: `GUARANTEE_PATH` is the shared-mode path, and `queue_for_local_guarantee` is the local one |
| The pointers that hand the never-twice gap to #976 | `docs/the-review-record.md:344-345` (`the work item's stamp is then the gap #976 carries`); `skills/verify/scripts/seal_stamp.py:924-925`, `:1045`, `:1075` | Rewritten to "a stated limit" (S8, `questions.md` Q2's default); `changelog/0.22.1.md:216, 226` stay, since a released file is history |
| `committed` in the sealer's never-draw clause | `agents/sealer.md:99-100` (`a stamp is drawn once from your committed \`sealed\``); the pinned clause in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:1566` | `a stamp is drawn once from your \`sealed\`` (S9) |
| The orchestrator's sentence that the stamp follows a commit alone | `skills/code-review/orchestration.md:241-242` and `:259-265` (*is committed*, *Wherever the commit's line names*) | Rewritten in place with the local-mode clause (S7) |
| The hook docstring's one-trigger account | `hooks/sealer-stamp.py:1-14` (*in the session that committed its verdict*, *git's \`post-commit\` runs after the commit*) | Rewritten in place: queued at the commit in shared mode and at the write in local mode |
| README sentences that tie the stamp to a commit alone | `README.md:180, 207-210`; `README.ko.md:172, 201-203` | Rewritten in place, and a `sealer-stamp-queue` row added beside `sealer-stamp` in both |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline. Unanswered
questions buried in prose read as decided.

<!-- The line below is the framer's mark, and it is the only evidence in the
     TREE that the framing happened — the existing framer mark lives in the
     repository's git dir, and a git dir does not travel, so CI cannot see it.
     Fill in the date and `<who>`; `<who>` takes the two values the `Planning`
     row of `routing.md` takes, `framer` or `the session`, and a mark that
     disagrees with that row is refused at the pull request rather than
     guessed at.
     The shape — verb, date, who, the moment — is the one `routing.md` and
     `plan.md` already end with, which is what keeps three feet-lines from
     becoming three conventions.
     A reframe adds `Reframed <date> by <who>, after round <N>.` UNDER this
     line when the review chain sends the work item back to its framer. It is
     never in this template; only a reframe writes it. -->

Framed 2026-10-19 by framer, before the build.
