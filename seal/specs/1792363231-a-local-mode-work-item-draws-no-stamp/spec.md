# Feature Specification: a local-mode work item draws no stamp (#976)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #976's body and its comment | Asked: a trigger for a local-mode work item that draws the stamp once, from the sealer's `sealed`, and never from the broad gate's run. Carried by the comment: #975's `questions.md` Q7 gap, a `sealed` over a commit the branch does not hold, after which the work item draws no stamp. Both rank above every file below |
| #975's comment (the owner, 2026-10-18) and `docs/the-review-record.md` §*The stamp* | The stamp means every party verified the work item, the sealer last. It is drawn once per work item from `guarantee.md` reading `sealed`, never from the broad gate's run, never twice. Where the history cannot tell the two directions apart, never twice wins over never missing (#975 `questions.md` Q8, answered 2026-10-18 under the owner's delegation). This work applies that rule to local mode, and keeps Q8's direction wherever the clone holds no record that settles it |
| `questions.md` Q2, answered (b) 2026-10-19 by the repository owner: "막는 장치를 만들도록 해 — 한계만 적으면 계속 공백인 거잖아"; and the owner's answer of 2026-10-19 after round 2, "설계를 다시" | The #975 Q7 gap gets a mechanism, not a stated limit. After round 2 the mechanism is no longer an inference each clone makes after the fact: in shared mode the commit gate refuses the commit of a `sealed` whose audited commit the branch does not hold, so no such verdict enters the history, and it records the refusal it made, because the sealer's new audit keeps the refused verdict on its `Target SHA` row and the chain reader would otherwise count it (S11–S13; `phases/phase-6.md`). In local mode, where no commit exists to refuse, the refusing writer leaves its record in the clone that holds the root, which is the only clone that ever reads it, and says the line (S14). What no record can settle stays in Q8's never-twice direction and is stated as narrower limits (S8) |
| #975 `rounds/round-4.md` finding 1 and `rounds/round-5.md` finding 1; this item's `rounds/round-1.md` finding 1 and `rounds/round-2.md` findings 1 and 2 | The two failures any condition over ancestry trades: round 4's repaired row that draws nothing (the gap), and round 5's rebase in a second clone that draws twice. This item's rounds 1 and 2 then showed the per-clone refusal record failing both ways once a guarantee travels: a copy by `merge --squash`, `cherry-pick -n` or a `checkout` of the path drew twice (round 1), the guard for that withheld the record behind the branch's own tracking ref after a rebase (round 2, finding 1), and still drew twice where no ref held the source (round 2, finding 2). Each guard opened a path. So the redesign refuses the wrong verdict before it is a fact of the history, and reads nothing new at read time (`plan.md` A14) |
| `CLAUDE.md` §*The rule a mechanism is kept against* ("when fixes chase one mechanism's edge cases, ask what it decides … before a fix adapts to an existing structure, ask whether the structure should change"), contract §19 and §20 | The refusal record in shared mode decided "did this clone draw for this verdict", while the question "once per work item" asks is "did any clone". No clone-local fact answers the second, and rounds 1 and 2 are the measurement. The structure changes: the judgment moves to the one moment the fact is known and the commit can still be stopped. The record's shared-mode code and cases leave in the same work that made them |
| `docs/the-commit-gate-inside-git.md` §*The commit gate inside git* and `hooks/git/pre-commit.py`'s docstring | A commit in a clone carrying the plugin's stubs is judged inside the commit, from the index git is about to commit, in the worktree it lands in, and a refusal is the exit status and the text on stderr, which git prints into the command's output. That is the surface the orchestrator reads at the commit of `guarantee.md`, and the one place a wrong `sealed` can be stopped before it is history. "Deciding at the commit is what stops a release mid-run" (`CLAUDE.md` §*Git*) |
| `docs/the-review-record.md` §*The guarantee* ("A ready pull request passes only where `guarantee.md` names HEAD and reads `sealed`"; "a stale commit fails naming the file") and `agents/sealer.md:134-140` | The pull request's check already refuses the verdict the gate refuses, later and only for a shared-mode item. The gate moves that judgment to the commit, and the way on it names is the one the sealer's definition already has: a new audit at HEAD, which keeps the earlier verdict on the `Target SHA` row. Nothing a person wants is stopped that the pull request would have let through |
| `docs/the-review-and-parity-arms.md` §*The two arms of the commit gate* and `hooks/gate.py#arms_missing` | The arms are opt-ins with a waiver each and a mark that quiets them. The guarantee refusal is none of that: it gates a fact the hook reads from git (the audited commit is not in the history the commit will have), it has no mark and no waiver, and it wakes only on a commit that stages a work item's `guarantee.md`. It is stated beside the arms, not as a third one |
| #975 `questions.md` Q9, answered (a) | A second clone sealing the same item is a second run of it, and stopping that would need a store beside the tree, which the repository's rule refuses. The redesign adds no such store: each record it keeps is a clone's own, about a row that is in that clone and nowhere else — the gate's, for a `sealed` it refused before it was history, and the local writer's, under a root that never leaves its clone |
| `skills/agent-contract/SKILL.md` §11, `docs/one-root-by-lifetime.md:307-322` (the local/shared table) | In local mode the root is `$(git rev-parse --git-common-dir)/seal/`, nothing under it is committed, and a repository with both roots is shared. So no `post-commit` can carry a local-mode `guarantee.md`, no commit gate can refuse one, and the pull request's check never reads one; the values directory `<git-common-dir>/specseal-stamp/` lives in the same common directory as the local root |
| `CLAUDE.md` §*The goal a design is chosen against* | Between two triggers that draw the same stamp, the one that needs no act of a session wins. This is why #975 put the trigger in a hook, and it rules out a command the orchestrator must remember (`plan.md` A6) |
| `skills/settle/SKILL.md:45-46` (*It refuses to run in local mode*) | `settle` never retires a local-mode work item, so every `sealed` guarantee a local-mode clone ever wrote still stands under its root. A trigger that scans the root would draw all of them at once (`plan.md` A3) |
| `agents/sealer.md:36` and `skills/code-review/orchestration.md:221-225` | The sealer works in the clone its prompt names, which can be a `git clone` of the branch worktree. A trigger keyed on where the sealer writes would queue in that clone's git directory, where no main session draws (`plan.md` A2's failure) |
| `hooks/hooks.json` (`PostToolUse`, matcher `Write\|Edit\|NotebookEdit`, group `post-edit`) and `hooks/session-lease.py`'s docstring | The `post-edit` group already runs after every file edit, and a gate in it resolves the repository from the edited file's path, not from `cwd`. The new trigger joins that group and needs no new harness event |
| `hooks/sealer-stamp.py` docstring §*Only the main session's `Stop`* (#400 `questions.md` Q2, measured 2026-09-28) | A subagent's hook payload carries the parent's `session_id`. This work relies on the same holding for a subagent's `PostToolUse`, and `questions.md` Q1 is the measurement that confirms it |
| `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_the_hook_is_registered_for_stop_and_nothing_else` | The drawing hook answers `Stop` alone. The queueing gate is therefore a separate file in `post-edit`, and this test stands unchanged (`plan.md` A9) |
| #957's `spec.md` §*How the rewrite is proved not worse*, `evals/README.md` | An agent whose read set changed is measured again under `noninferiority.py`'s five rules, against the latest side and never an absolute. `agents/sealer.md` changed by one word in phase 4 and was measured in phase 5 (S9). The redesign changes no agent definition, so nothing is measured again |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A hook's output and what a person reads change: the top rung, which is why this frame exists |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` table below, read by the review against the diff |

## Scope

**In.**

- A `post-edit` gate, `hooks/sealer-stamp-queue.py`, registered in
  `dispatch.GROUPS["post-edit"]`. After a `Write` or `Edit` whose
  `file_path` is a local-mode root's `specs/<id>/guarantee.md`, it calls the
  local writer below. A `sealed` verdict then queues one values file for the
  payload's session, and the main session's `Stop` draws it with the
  unchanged `hooks/sealer-stamp.py`. Built in phases 1 and 2; the redesign
  leaves it as it stands.
- A local writer in `skills/verify/scripts/seal_stamp.py`,
  `queue_for_local_guarantee(path, session, now=None)`, sharing the
  verdict reading, the row building and `write_values` with the shared-mode
  writer. Once per work item in local mode is held by four facts (S3, S4).
- **The #975 Q7/Q8 gap the issue's comment carries, closed by a mechanism
  (`questions.md` Q2, answered (b)), redesigned after round 2.** In shared
  mode the commit gate inside git refuses, in `pre-commit`, a commit that
  stages a work item's `guarantee.md` reading one `sealed` whose audited
  commit the commit's own history will not hold, on the branch the item's
  `routing.md` declares (S11). The text names the file, the commit named,
  the branch, HEAD, and the way on: a new audit of the sealer at HEAD. So a
  `sealed` the stamp writer would refuse never enters the history. The new
  audit keeps the refused verdict on its row as `; earlier run: <sha>
  sealed` (`agents/sealer.md` §*Rules*), so the gate records the refusal it
  made, in the clone that made it, and `_queue_one`'s chain refusal skips a
  `sealed` this clone recorded refusing. That record states a fact the gate
  established and infers nothing: the verdict never became history here, and
  an uncommitted row reaches no other clone. `sealed_before` and the ancestry
  refusal stand as #975 left them, and `post-commit` writes no record and
  reads no guard (S10, S13).
- In local mode, where no commit exists to refuse, the local writer keeps
  the refusal record phase 3 built, because there the question the record
  answers, whether this clone drew, is the whole question: a local root
  never leaves its clone. It gains the line a person needs: the edit gate's
  message says that no stamp was queued and why, where the `Branch` row's
  branch stands (S14). Nothing in the tree reads a local-mode guarantee at
  the pull request, so that line is the only place the wrong row is seen.
- The words: `docs/the-review-record.md` §*The stamp* (the drawing rule, the
  refusal rule rewritten, and the unchecked paragraph),
  `docs/the-commit-gate-inside-git.md` (the new refusal, stated beside the
  arms, and its latency bullet), `skills/code-review/orchestration.md`'s
  sealer step and stamp paragraph, `hooks/git/pre-commit.py`'s and
  `hooks/sealer-stamp.py`'s docstrings, `seal_stamp.py`'s comments and
  docstrings, both READMEs' hook tables and side-effect sentences, and the
  changelog fragment (S7, S8). And the mark's grammar: this item's own foot
  carries `Reframed … after phase 6.`, which `chain_check.REFRAME_RE` does
  not read, so the check, the policy sentence and the template widen to the
  route this run took (`plan.md` row 8, `questions.md` head item 12).
- The sealer measured once against #975's phase-4 side, because one word of
  its definition changed in phase 4 (S9, closed in phase 5).

**Out, and why.**

- Shared mode's trigger. `post-commit` stays the trigger, and
  `already_queued`, `sealed_before`, the earlier-run chain and the ancestry
  refusal keep #975's behaviour. A replacement for both modes was weighed
  and rejected (`plan.md` A2). Every shared case that stands at 769f2aa4
  stays green with its body untouched (S10).
- The `reference-transaction` backstop. It judges a `--no-verify` commit for
  the arms and no more. A `sealed` committed with `--no-verify` over a commit
  the branch does not hold lands, the stamp writer refuses it silently, and
  the gap stays for that item: a missing stamp, which is Q8's direction. A
  backstop that read the new commit's guarantee would add a second reader of
  the same fact for a command no agent of this plugin issues, and
  `plan.md` A14's failure scenario states it instead.
- A clone whose git hooks slot is somebody else's, in shared mode. #975's
  `plan.md` A3 left it a stated silence; the stubs do not run there, so
  neither the stamp nor the refusal does. It stays as §*The stamp* and
  `docs/the-commit-gate-inside-git.md` §*Where each state of a repository
  stands* state it.
- The parts of the Q7 gap no refusal can reach. They stay in Q8's
  never-twice direction, and each is stated in §*The stamp* (S8):
  - a `sealed` over a commit the branch does not hold that was committed
    where the stub did not judge it: a foreign hooks slot, `--no-verify`, a
    plugin older than this release, a person's own commit with no session
    behind it, or a clone no session has reached;
  - a `sealed` that drew and whose audited commit a later rebase, amend or
    cherry-pick moved out of the history, which the once readers rightly
    count as stamped; the gate judges the commit's newest verdict alone and
    never the `; earlier run:` chain;
  - in local mode, a guarantee whose values files were removed from the
    common directory by hand, or one carried by `seal import` from a clone
    that drew, then re-sealed here; the record is the clone's, and such a
    guarantee carries none.
- The amend or rewrite of a sealing commit in a second clone (#975
  `questions.md` Q9). It is a shared-mode limit, and the redesign neither
  widens nor narrows it: a commit git makes for its own rebase or
  cherry-pick is not judged (`docs/the-commit-gate-inside-git.md` §*A commit
  git makes for its own rebase, cherry-pick or revert is not judged*), and
  `post-commit` writes no record any more: the only shared-mode record is the
  gate's, for a row that never became history.
- A `guarantee.md` that reaches a local root other than through `Write` or
  `Edit`, such as a shell write, `seal import`, or `seal mode local` moving a
  shared root back. Nothing is queued for it and nothing is said. That is a
  missing stamp, never a false one, and it is stated in §*The stamp* (S7).
- `seal mode shared` moving a local root into the tree. The commit that adds
  the root carries every `guarantee.md` at once, and `post-commit` reads each
  one with the shared rules. That is #975's behaviour at a mode switch. It is
  not a local-mode trigger, and `plan.md` §*Technical context* names it for
  the orchestrator to file if a run shows it. The new refusal does not wake
  on it either: that commit lands on whatever branch the person is on, and
  only an item whose `Branch` row names that branch is judged.
- Every other place `skills/code-review/orchestration.md` tells the
  orchestrator to commit a record that local mode cannot commit (line 209's
  `Commit guarantee.md`, line 187's `commit broad-gate.md`). That is the
  orchestration's local-mode wording as a whole, not the stamp's trigger.
- `agents/sealer.md`, `agents/warden.md`, `agents/smith.md`,
  `agents/framer.md`, `agents/scribe.md` and
  `skills/agent-contract/SKILL.md`. The sealer's definition already says
  what the gate holds it to: the `Target SHA` is the commit audited, and a
  new audit keeps the earlier verdict on the row (`agents/sealer.md:79-85,
  134-140`). The redesign changes no definition, so no agent is measured
  again (S9 stands closed).

## User scenarios & acceptance *(mandatory)*

One row per scenario. These become the review's stage-1 checklist and the
regression tests' skeleton. "A local-mode item" below means a repository with
no `<repo>/seal/` and a root at `<git-common-dir>/seal/`, holding
`specs/<id>/routing.md` with a `Branch` row and `specs/<id>/guarantee.md`.
"The declared branch" means the branch the item's `routing.md` names in its
`Branch` row.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A local-mode `sealed` written queues one stamp | Given a local-mode item whose `guarantee.md` reads one `Verdict:` of `sealed`, whose `Target SHA` row names `<sha> against <base>` with no earlier run reading `sealed`, and whose `<sha>` is an ancestor of the `Branch` row's `refs/heads/<branch>`. When `queue_for_local_guarantee(<that path>, <session>)` runs, then one values file `<ns>-<id>-<sha>.json` is written under `<git-common-dir>/specseal-stamp/<session>/` and one line is returned, `QUEUED` formatted with the id and the file. The main session's `Stop` draws that file once | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_a_local_mode_sealed_guarantee_queues_one_stamp` (seen red: `seal_stamp` at 769f2aa4 had no local writer); `::test_the_main_sessions_stop_draws_each_undrawn_file_once` over the file it wrote. Protects: #976, a sealed local-mode work item that never draws |
| S2 `withheld` and `undecided` queue nothing in local mode | Given the same item with `Verdict: withheld — …` or `undecided — …`, or two `Verdict:` lines, or an unfilled template, then no file is written and no line returned | `…::test_a_local_mode_withheld_or_undecided_guarantee_queues_nothing`. Protects: the finished-work stamp over unfinished work |
| S3 A re-seal after `withheld` draws then, and a second `sealed` draws nothing | Given a `Target SHA` row reading `<sha2> against <base>; earlier run: <sha1> withheld` and a `sealed` verdict, one file is queued. Given a row whose `; earlier run:` chain reads `sealed` over a commit this clone did not record refusing, or a values file `*-<id>-*.json` or `.drawn.json` already standing under any session's directory of the clone, nothing is queued | `…::test_a_local_mode_reseal_after_withheld_queues_the_stamp`, `…::test_a_local_mode_second_sealed_queues_nothing`. Protects: #975's never twice, in local mode, where the root and the values directory share one common directory and so the values files are a complete record |
| S4 A verdict over a commit off the work item's branch draws nothing, and says so where the branch stands | Given a `sealed` whose `Target SHA` does not resolve in the clone, or is not an ancestor of `refs/heads/<declared branch>`, or whose item has no `routing.md`, no `Branch` row, or a branch the clone no longer holds, then nothing is queued. Where the declared branch stands in the clone, the writer records the refusal (S14) and returns one line, `seal_stamp.NOT_ON_BRANCH` (the name is the work's) formatted with the id, the commit named and the branch: that no stamp was queued because the row names a commit the branch does not hold, and that a new audit at the branch's head draws it. Where no `Branch` row stands or the branch is gone, nothing is said: the item is one `settle` never retired, and its old guarantee is being edited | `…::test_a_local_mode_guarantee_off_its_branch_queues_nothing` (one case per given, parametrized; the "off the branch" and "unresolved" givens gain the line assertion and are seen red against the silent writer at 339ac7dc, contract §15; the other givens assert no line). Protects: a stamp for a work item merged and deleted long ago, drawn the first time anyone edits its old guarantee; and a wrong row in local mode that nobody ever sees, since no pull request's check reads a local guarantee |
| S5 Shared mode is not the gate's | Given a `Write` to `<repo>/seal/specs/<id>/guarantee.md` reading `sealed`, or to `<git-common-dir>/seal/specs/<id>/guarantee.md` in a repository that also has `<repo>/seal/` (shared, contract §11), then the gate queues nothing. `post-commit` stays the shared trigger | `…::test_the_edit_gate_leaves_shared_mode_to_post_commit`. Protects: two stamps for one shared-mode verdict, one at the write and one at the commit |
| S6 The gate runs in `post-edit`, is silent elsewhere, and says the line to the person | Given a `PostToolUse` payload for `Write` or `Edit` whose `tool_input.file_path` is S1's path, when `hooks/dispatch.py post-edit` runs, then the values file is written and stdout is one JSON object whose `systemMessage` is S1's line, or S4's where the writer returned that one. A payload carrying `agent_id` (the sealer's own `Write`) queues the same file, since queueing is not drawing. Given any other path, a `NotebookEdit`, a payload that is not JSON, or no `session_id`, then it prints nothing, writes nothing, and runs no `git` and imports no `seal_stamp.py` before the path's shape has matched | `…::test_the_edit_gate_queues_a_local_mode_sealed_guarantee`, `…::test_a_subagents_write_queues_and_draws_nothing`, `…::test_the_edit_gate_is_silent_off_a_guarantee` (through `dispatch.py`); `tests/test_dispatch.py` green. The S4 line through the gate is asserted in the S4 case, which runs the writer, and the gate carries whatever lines the writer returns (`hooks/sealer-stamp-queue.py:82-83`, unchanged). Protects: a gate in a group that runs on every file edit in every repository costing that edit a `git` call |
| S7 The documents say where the stamp comes from in each mode | Given `docs/the-review-record.md` §*The stamp*, then its rule says the stamp is queued at the commit of `guarantee.md` in shared mode and at the `Write` or `Edit` that leaves it reading `sealed` in local mode, with the four local facts of S3 and S4. Its unchecked paragraph no longer names local mode among the places nothing is queued. It names instead a local guarantee that arrived by a shell write or `seal import`, and a verdict over a commit off the item's branch, and it says the line reaches the person as the edit hook's message and that nobody has watched it on a screen. `skills/code-review/orchestration.md`'s stamp paragraph says that in local mode the edit hook's line is shown to the person at the sealer's write and does not reach the orchestrator (round 1 finding 2's wording, kept). Both READMEs carry a `sealer-stamp-queue` row and say the stamp is queued at the commit or, in local mode, at the write | `…::test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`; `…::test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`; `…::test_both_readmes_list_the_stamp_hook`; `bin/rules --check` exit 0; `tests/test_docs_line_wrap.py`. Protects: a reader told local mode draws no stamp after it does |
| S8 The gap's sentences describe the mechanism, not a pointer to a closed issue, and no sentence describes the removed one | Given the tree after this work, `git grep -n "#976"` hits no file outside this work item's directory, #975's released work item directory and the released `changelog/0.22.1.md`. `docs/the-review-record.md` §*The stamp* says that in shared mode a `sealed` over a commit the branch does not hold is refused at its commit (`docs/the-commit-gate-inside-git.md`), so the first `sealed` the history and the earlier-run chain see is one that drew; and that in local mode the refusing writer records the refusal in the clone and the once readers skip a `sealed` this clone refused. Its unchecked paragraph names only the limits §*Scope* lists as left. `git grep -n -e "specseal-stamp-refused" -e "refused_here" -e "record_refusal" -e "_stamped_nowhere_else" -e "_guarantee_on_another_ref" -e "plain_commit" -e "reflog"` over `docs/ skills/ hooks/ README.md README.ko.md agents/` hits only sentences and code about local mode's record, and none about a reflog, a patch-equivalent copy, another ref, or four or three guards. `seal_stamp.py`'s once comment and the `queue_for_guarantee` and `sealed_before` docstrings say the same | `…::test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does` asserts the paragraph names each left limit and carries no `#976`; `…::test_the_policy_states_the_refusal_record_and_names_its_cases` rewritten to hold the new rule sentence, its `Enforced by:` entries, and the absence of the removed guards' words (seen red against the paragraph at 339ac7dc). Protects: a pointer to an issue that this work closes, read later as an open promise; and a reader told of a reflog guard the tree no longer has |
| S9 The sealer is told, and proved not worse | Given `agents/sealer.md`, its `## Never` bullet reads `a stamp is drawn once from your \`sealed\`.` (the word `committed` went in phase 4). Given phase 5, `evals/sealer-phase-5.md` under this item reads `pass` under the five rules against #975's `seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/evals/sealer-phase-4.json`. The redesign leaves `agents/sealer.md` byte for byte as 11b90191 left it | `…::test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it`; `tests/test_the_sealer_guarantees.py::TestDefinition`; `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`; `git diff --stat 11b90191 HEAD -- agents/` empty. Protects: a definition changed and never measured (#967 guard 1) |
| S10 Shared mode draws what it drew, and the once readers are #975's | Given the values helper and the redesign, the shared-mode cases of `docs/the-review-record.md` §*The stamp*'s first `Enforced by:` line that stood at 769f2aa4 pass with no edit to their bodies, round 5's two rebase cases among them. `sealed_before` and the ancestry refusal read what they read at 769f2aa4: no `refused_here`, no record written, no reflog, no other ref, no patch-equivalence. `_queue_one`'s chain refusal keeps its one skip, `refused_here`, over a target the gate recorded (S11), and nothing in `post-commit` writes a record. `hooks/git/` changes in `pre-commit.py`'s docstring alone, and `hooks/commitgate.py` in `pre_commit` and the functions it calls alone; `post_commit` and `reference_transaction` are unchanged | the fourteen cases named on that `Enforced by:` line at 769f2aa4, untouched (an AST comparison, as round 1 ran it); `git diff --stat 769f2aa4 HEAD -- hooks/git/` naming `hooks/git/pre-commit.py` alone, and `git diff 769f2aa4 HEAD -- hooks/git/pre-commit.py` touching its docstring alone; `git diff 769f2aa4 HEAD -- hooks/commitgate.py` touching `pre_commit` and new functions only, read by the review. Protects: ten review rounds of #975's once rules regressing under a refactor and a fourth reading |
| S11 A `sealed` over a commit the branch does not hold is refused at its commit | Given a shared-mode clone carrying the plugin's stubs, on the declared branch, with a Claude session behind the command. When a commit stages `seal/specs/<id>/guarantee.md` reading one `Verdict:` of `sealed` whose `Target SHA` names a commit that does not resolve in the clone (`deadbee`, round 4's measured shape), or resolves but is not an ancestor of HEAD, the parent-to-be (a commit on another branch, S12's old shape), then `pre-commit` exits 1, nothing is committed, HEAD and the index stay as they were, and stderr carries `gate.HEADER` followed by a text that names the file, the commit named, the branch, HEAD's short SHA, and the way on: a new audit of the sealer at HEAD, whose `Target SHA` row keeps the earlier verdict as `; earlier run: <sha> sealed` (`agents/sealer.md:134-140`), and never an edit of the row by hand. The text names no question tool, pressed or not. The same holds through a real `git commit` in a clone where `hooks/hook-install.py` wrote the stubs. At the refusal the gate writes the refusal record `<git-common-dir>/specseal-stamp-refused/<id>-<target>` (`seal_stamp.record_refusal`), and nothing else on the refused path; under `_sequencer_commit` it neither refuses nor records. The new audit the text names keeps the refused verdict on its row as `; earlier run: <sha> sealed`, and its commit lands. `_queue_one`'s chain refusal skips that earlier run because this clone recorded it, and the stamp is then held by what #975 reads: where HEAD's history holds no `sealed` that drew and the clone holds no values file for the item, the repair draws the work item's one stamp; where the history holds a `sealed` that drew (a verdict gone stale under a rebase, then audited again), `sealed_before` counts it and the repair draws nothing | `…::test_a_sealed_over_a_commit_the_branch_does_not_hold_is_refused_at_the_commit` (phase 6, in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, parametrized over the unresolved and the off-branch target, calling `commitgate.pre_commit` on a staged index and then committing the repaired row; at de80c2c2 it pins the repair drawing nothing, and phase 7 turns that assertion to one values file and one record, seen red at de80c2c2); `…::test_a_refused_row_over_a_drawn_seal_does_not_draw_again` (new in phase 7: a `sealed` that drew, then a rebase that orphans its target, then a wrong row refused and recorded, then the new audit; asserts no second values file, which `sealed_before` holds, seen red with `sealed_before` replaced by `False`); `tests/test_the_commit_gate_decides_at_the_commit.py::test_a_sealed_the_branch_does_not_hold_is_stopped_inside_the_commit` (phase 6, through the installed stubs with the `world` fixture, asserting HEAD unmoved and `gate.HEADER` in stderr). Protects: the Q7 gap, a work item never stamped because a wrong row entered the history and the readers counted it |
| S12 The refusal wakes on that one fact and nothing else | Given the same clone, `pre-commit` exits 0, prints nothing and writes no record for each of: a `sealed` whose `Target SHA` names HEAD or an ancestor of HEAD, the normal flow; a `withheld` or `undecided` verdict, two `Verdict:` lines, or an unfilled template over any target; a `sealed` whose newest target is an ancestor while its `; earlier run:` chain names a commit the clone does not hold (a `sealed` that drew, then went stale under a rebase, then was audited again); a commit on a branch other than the declared one, such as `main` after `merge --squash`, `cherry-pick -n` or `checkout <rev> -- <dir>` of the item (round 1's three shapes), which lands, queues nothing at `post-commit` as #975 had it, and whose re-seal there queues nothing by the chain; an item with no `routing.md` or no `Branch` row in the index; a commit that stages no `guarantee.md`; and a `rebase --continue` or a `cherry-pick --continue` whose child commit carries such a guarantee (`commitgate._sequencer_commit`). The commit that stages no `guarantee.md` loads neither `seal_stamp.py` nor `chain_check.py` | `…::test_the_guarantee_refusal_is_quiet_off_its_one_fact` (new, parametrized over each given; the "stages no guarantee" given asserts, with the loader replaced by a recorder as `test_the_edit_gate_is_silent_off_a_guarantee` does, that nothing was loaded); round 1's three shapes assert the commit lands and `queued(other) == []` after the re-seal, which is `test_a_squash_of_a_sealed_item_in_another_clone_queues_nothing`'s assertion over three commands. Protects: a gate that stops the squash a person meant, or a sealed branch's own rebase; and a cost on every commit that touches no guarantee |
| S13 Where the stub does not judge, the gap stays and is stated | Given a `sealed` over a commit the branch does not hold committed with `--no-verify`, then `reference-transaction` passes it as it passes every commit the arms are quiet for, the commit lands, `post-commit` queues nothing and writes no record, and the repair that follows queues nothing (the chain and `sealed_before` count the earlier `sealed`). The same holds in a foreign hooks slot, under a plugin older than this release, for a person's own commit, and in a clone no session has reached. Each is stated in §*The stamp*'s unchecked paragraph and in `plan.md` A14's failure scenario | `…::test_a_sealed_committed_past_the_stub_keeps_the_gap` (new: `--no-verify`, then the repair; asserts no values file and no record, so the limit is pinned as a limit and a later change that closes it is seen); the paragraph's words under S8's case. Protects: a document promising the gate closes what it does not reach |
| S14 Local mode records and repairs in the clone that holds the root | Given a local-mode item whose `sealed` names a commit that is not an ancestor of the declared branch, while that branch exists, then nothing is queued, a refusal record `<common>/specseal-stamp-refused/<id>-<target>` is written, and S4's line is returned. The re-seal whose row reads `; earlier run: <that sha> sealed` then queues one file. Given a refusal because the item has no `Branch` row or the branch is gone, no record is written and nothing is said. The record is per clone and matched as `_same_commit` matches: a prefix at least seven characters long; a shorter or different spelling finds none and the verdict counts as stamped, which is Q8's direction. No guard beyond the branch standing applies: a local root never leaves its clone, so `already_queued` already says whether the work item was stamped | `…::test_a_local_mode_seal_refused_off_its_branch_then_resealed_draws_once` (kept, gaining the line assertion); `…::test_a_refusal_record_skips_only_its_own_verdict` rewritten over `local_guaranteed` and `queue_local`, since its shared-mode fixture no longer reads a record (seen red at 339ac7dc against the local writer with the matcher's floor deleted). Protects: the same gap in the local writer's chain reader, and a record for one work item answering for another |

## Data & interfaces

- **The local writer**: `seal_stamp.queue_for_local_guarantee(path, session,
  now=None)` returns a list of zero or one lines. It does five things.
  - It resolves `path` with `os.path.realpath` and requires it to be
    `<common>/seal/specs/<id>/guarantee.md`, where `<common>` is a git
    common directory, `optin.git_common_dir(<main worktree>)` resolves to
    it, and `optin.home_at` for that repository answers `<common>/seal`.
    That rules out shared mode and a repository with both roots
    (`phases/phase-1.md`).
  - It reads the file from disk and judges it with `chain_check.py`'s
    readers (`verdicts_of`, `verdict_word`, `target_of`, `table_rows`,
    `field`, `earlier_verdicts`), the same calls `_queue_one` makes.
  - It reads the `Branch` row of `specs/<id>/routing.md` with
    `hooks/routing.py#parse`, loaded through `chain.load(chain.ROUTING, …)`.
  - It refuses in this order: no single `sealed`, no target, an earlier
    `sealed` in the row's chain this clone did not record refusing,
    `already_queued(common, ident)`, then no `Branch` row or `git
    --git-dir=<common> merge-base --is-ancestor <target> refs/heads/<branch>`
    not exiting 0. At that last refusal, where `refs/heads/<branch>`
    resolves, it calls `record_refusal(common, ident, target)` and returns
    `[NOT_ON_BRANCH.format(id=ident, target=target, branch=branch)]`.
  - It writes with `write_values(common, session, values, now=now,
    key=f"{ident}-{target}")` through `_queue_values`.
- **The line `NOT_ON_BRANCH`** (the name is the work's), one sentence beside
  `QUEUED`: that no stamp was queued for `<id>` because its `guarantee.md`
  names `<target>`, which `<branch>` does not hold, and that a new audit at
  the branch's head draws it. It names no command: there is no values file
  to draw from, and `seal-stamp --from` is not the way on here.
- **The values**: the keys `_queue_one` writes, read from disk. `tree` is the
  target, `base` comes from the row, `branch` is the `Branch` row, and
  `from` and `pr` are None. `item` is the local item directory, `session` is
  the payload's, and `rows` is `guarantee_rows(target, branch, base, ident,
  run, rounds)`. `run` is `chain.newest_run` over `specs/<id>/broad-gate.md`
  read from disk. `rounds` is the count of `rounds/round-<N>.md` in the
  directory.
- **The shared helper**: `_queue_values`, which both writers call once a
  guarantee has passed their refusals. Its readers stay `git show
  HEAD:<path>` in shared mode and file reads in local mode.
- **The gate**, `hooks/sealer-stamp-queue.py`: it reads the payload, takes
  `tool_input.file_path` for `Write` and `Edit` only, and returns before any
  `git` call or `seal_stamp.py` import unless the normalized path ends in
  `/seal/specs/<segment>/guarantee.md`. It loads `seal_stamp.py` the way
  `commitgate._stamp_module()` does. It passes the payload's `session_id`.
  It prints `{"systemMessage": "<lines>"}` where lines came back. It is
  silent on every failure, the shape `implementer-notice.py` and
  `post_commit` have. Unchanged by the redesign.
- **Registration**: `dispatch.GROUPS["post-edit"]` holds
  `"sealer-stamp-queue.py"` after `session-lease.py`. `hooks/hooks.json` is
  unchanged, because the `post-edit` matcher already covers `Write` and
  `Edit`.
- **The refusal at the commit**, in `hooks/commitgate.py#pre_commit`, after
  `arms_missing` has found nothing missing and before `_leave_mark`
  (`commitgate.guarantee_off_history`, built in phase 6). It takes `cwd`,
  `head` (the parent-to-be, "" on an unborn branch, where nothing is judged)
  and the staged paths (`git diff --cached --name-only`, listed once for the
  arms and the refusal together). A path is a guarantee by a prefix and
  suffix test on `seal/specs/<item>/guarantee.md`, before anything is
  loaded; for each, it reads the index's content with `git show :<path>` and
  judges it with `chain_check.py`'s readers, loaded through
  `commitgate._stamp_module()._chain_check()` only after a path matched.
  Where the content reads one `Verdict:` of `sealed` and `target_of` names
  a commit, it reads the index's `seal/specs/<item>/routing.md` with
  `routing.parse` and the current branch with `routing.current_branch(cwd)`.
  Where the `Branch` row names the current branch and `git merge-base
  --is-ancestor <target> <head>` does not exit 0 (128 for a target that
  does not resolve, 1 for one off the history), the function returns the
  refusal's text; otherwise None. On a text, `pre_commit` calls
  `seal_stamp.record_refusal(common, <id>, <target>)` with the `common`
  `_context` resolved, writes the text to the stream and returns 1, unless
  `_sequencer_commit(cwd)`, in which case it records nothing, leaves the
  mark and returns 0 as it does for the arms. A reading that raises stops
  nothing and records nothing, because the pull request's check refuses the
  same file. The `; earlier run:` chain is not read.
- **The refusal's text**: `gate.HEADER`, a blank line, then one paragraph
  naming `seal/specs/<id>/guarantee.md`, the commit the row names, the
  branch, and HEAD's short SHA; then the way on, which is the sealer's new
  audit at HEAD, keeping the earlier verdict on the row, and never a row
  edited by hand (`agents/sealer.md:134-140`); then `gate.UNCHANGED`. It
  names no question tool, pressed or not: the refusal has no options to put
  to a person, because the pull request's check refuses the same file
  (`docs/the-review-record.md` §*The guarantee*), and `questions.md` Q5
  holds the default that no waiver exists. The text's constants live in
  `hooks/gate.py` beside `STATES`, and the module that pins the arms' texts
  pins this one.
- **Where it is not read**: `reference_transaction` and `post_commit` are
  unchanged. The PreToolUse reading (`hooks/commit-review-gate.py`) judges
  no guarantee: it reads a command's text, and this refusal reads the index.
- **The refusal record**: an empty file
  `<common>/specseal-stamp-refused/<id>-<target>`, with `<target>` as
  `target_of` read it, written by `record_refusal` and asked by
  `refused_here` with `_same_commit`'s seven-character floor. The directory
  is a sibling of `specseal-stamp/`, so `pending`, `already_queued` and the
  `Stop` hook never list it. Two writers and two readers, one pair per mode.
  In shared mode the commit gate writes it at its refusal (above), and
  `_queue_one`'s chain refusal alone asks it: an earlier run reading
  `sealed` whose SHA this clone recorded refusing does not count.
  `sealed_before` asks nothing of it and reads as at 769f2aa4, because a row
  the gate refused never entered the history, and a `sealed` that is in the
  history drew where it was made. `post-commit` writes none. In local mode
  the local writer writes it at its branch refusal where the branch stands,
  and its own chain refusal asks it (S14).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The statement that local mode queues no stamp | `docs/the-review-record.md#"The stamp">"in local mode, where the \`seal/\` root sits under the git directory and no"` (lines 339-340 at 769f2aa4) | §*The stamp*'s rule, which names the local trigger (S7); the paragraph names the local-mode silences that remain. Done in phase 4 |
| The code comment saying the same | `skills/verify/scripts/seal_stamp.py:933-935` at 769f2aa4 (`A local-mode root sits under the git directory and no commit ever carries it, so no stamp is queued there.`) | Rewritten in place in phase 3: `GUARANTEE_PATH` is the shared-mode path, and `queue_for_local_guarantee` is the local one |
| The pointers that hand the never-twice gap to #976 | `docs/the-review-record.md:344-345` at 769f2aa4 (`the work item's stamp is then the gap #976 carries`); `skills/verify/scripts/seal_stamp.py:924-925`, `:1045`, `:1075` at 769f2aa4 | Rewritten in phases 3 and 4 to describe a mechanism (S8); `changelog/0.22.1.md:216, 226` stay, since a released file is history. Phase 8 rewrites them again to the redesign |
| The rule that any earlier `sealed` counts as stamped, in local mode | `docs/the-review-record.md` §*The stamp*'s once sentence and `seal_stamp.py`'s once comment at 769f2aa4 | In local mode an earlier `sealed` counts unless this clone recorded refusing it (S14); in shared mode the rule stands as #975 wrote it, because the gate keeps a refused `sealed` out of the history (S11) |
| `committed` in the sealer's never-draw clause | `agents/sealer.md:99-100` at 769f2aa4; the pinned clause in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` | `a stamp is drawn once from your \`sealed\`` (S9). Done in phase 4 |
| The orchestrator's sentence that the stamp follows a commit alone | `skills/code-review/orchestration.md:241-242` and `:259-265` at 769f2aa4 | Rewritten in place with the local-mode clause (S7). Done in phase 4 and round 1's fix pass |
| The hook docstring's one-trigger account | `hooks/sealer-stamp.py:1-14` at 769f2aa4 | Rewritten in place: queued at the commit in shared mode and at the write in local mode. Done in phase 4 |
| README sentences that tie the stamp to a commit alone | `README.md:180, 207-210`; `README.ko.md:172, 201-203` at 769f2aa4 | Rewritten in place, and a `sealer-stamp-queue` row added beside `sealer-stamp` in both. Done in phases 2 and 4 |
| `post-commit`'s refusal record: its write site and its guards | `skills/verify/scripts/seal_stamp.py:1120-1127` (`PLAIN_COMMITS`), `:1170-1222` (`plain_commit`, `_guarantee_on_another_ref`, `_stamped_nowhere_else`), `:1257-1259` (the `record_refusal` call in `_queue_one`), the sentences of the section comment at `:1106-1118` and of the `record_refusal`, `refused_here` and `queue_for_guarantee` docstrings that describe a record written after a commit under guards, all at 339ac7dc | The commit gate refuses the verdict before it is history and records that refusal itself (S11), so `post-commit` has nothing to record and no guard to read. `record_refusal`, `refused_here`, `_same_commit`, `REFUSED_DIR` and `SHORTEST_SHA` stay, written by the gate in shared mode and by the local writer in local mode (S14); their docstrings say so |
| The skip in the history reader | `seal_stamp.py:1101-1103` (`refused_here` in `sealed_before`) at 339ac7dc | `sealed_before` counts every earlier `sealed` in the history again, as at 769f2aa4 (S10): a row the gate refused never entered the history, so the skip decided nothing there. `_queue_one`'s chain refusal keeps its skip (S11) |
| The refusal record's shared-mode cases | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`: `test_a_seal_this_clone_refused_does_not_count_as_stamped` (three forms), `test_a_seal_over_a_commit_off_the_branch_then_repaired_draws_once`, `test_a_conflicted_rebase_in_another_clone_writes_no_refusal`, `test_an_amend_in_a_fresh_clone_writes_no_refusal`, `test_a_body_edit_over_a_rewritten_seal_writes_no_refusal`, `test_a_seal_whose_target_has_a_copy_writes_no_refusal`, `test_a_seal_brought_from_another_ref_writes_no_refusal` (three forms), `test_guard_two_reads_what_post_commit_sees_in_the_reflog`, and the fixtures only they call (`off_branch_commit`, `rebased_and_cloned_fresh`, `resealed_draws_nothing`, and `refusals` where no kept case calls it) at 339ac7dc | Their shapes are S11's and S12's: the wrong row is refused at the commit, and a copy onto another branch lands and queues nothing by #975's rules. The two shapes they protected, round 4's `deadbee` and the off-branch target, are S11's two parametrized givens. Round 5's two rebase cases, which they were built not to break, stay untouched |
| The refusal record's rule paragraph in the policy, and the guards in every document | `docs/the-review-record.md` §*The stamp*, the second rule (the paragraph opening `**A \`sealed\` a writer refused leaves a refusal record in the clone`) and its `Enforced by:` line; the unchecked paragraph's limit list (`a repair committed in a clone other than the one that refused … a clone whose reflog is off`); `skills/verify/scripts/seal_stamp.py`'s once comment and the `queue_for_guarantee`, `sealed_before` and record docstrings; `README.md:213-215` and `README.ko.md:205-206` (`a \`sealed\` the plugin refused leaves an empty file under … specseal-stamp-refused/`); `changelog.md`'s second entry in this directory; `tests/…::test_the_policy_states_the_refusal_record_and_names_its_cases` and the `silence` tuple of `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`; all at 339ac7dc | Rewritten in place (contract §19) to the redesign: in shared mode the refusal at the commit, which records what it refused, stated in `docs/the-commit-gate-inside-git.md` and pointed to from §*The stamp*; in local mode the writer's record at the write; the chain reader's skip in both; the limits §*Scope* leaves (S8). The README side-effect sentence keeps the directory and says who writes it in each mode |
| `questions.md` Q4's standing as a rule the tree holds | `questions.md` Q4 (the reflog subjects guard 2 read), answered from `phases/phase-3.md` | The reflog is read by nothing after phase 7. The row stays answered, as a record of a measurement; the head of `questions.md` says the guard it served is gone |

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
Reframed 2026-10-19 by framer, after round 2.
Reframed 2026-10-19 by framer, after phase 6.
