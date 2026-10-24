# Feature Specification: the stamp is drawn from the sealer's verdict (#975)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate. -->

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #975's body and its comment (the owner, 2026-10-18) | The final stamp means every party verified the work item, the sealer last, and the work is done. It is drawn once per work item, from `guarantee.md` reading `sealed`, never from the broad gate's run and never twice for one item; a re-seal after `withheld` draws it then, a second `sealed` draws nothing new. The gate's pass line never says `SEALED`/`sealed`: the word is the sealer's verdict alone. These rank above every file below as they stand |
| `CLAUDE.md` §*The goal a design is chosen against* | Between two triggers that draw the same stamp, the one that needs no act of a session is chosen; a stamp nobody has to remember to draw |
| `CLAUDE.md` §*The rule a mechanism is kept against — subtract before you add* | What stood on the old fact leaves in the same change: the gate's values-file write, its terminal drawing, its `SEALED` lines, the `scale` key, and the policy section that described them. A fact has one source: the stamp's rule moves to the document that owns the verdict it is drawn from |
| `CLAUDE.md` §*a thing more than one party can have is named with whose* and `tests/test_one_word_one_meaning.py` §*"the seal"* | `seal`/`sealed` name the sealer's verdict; the gate's output and the files that describe the gate say neither. The sweep's `SEAL_SWEPT` list is the check, and this work extends it (S1) |
| `docs/the-review-record.md` §*The guarantee* | The verdict words `sealed`, `withheld — <reason>`, `undecided — <question>`; a ready pull request passes only where `guarantee.md` names HEAD and reads `sealed` (`chain_check.py#guarantee`). The stamp's fact is this file's fact, read at the same commit |
| `docs/the-broad-gate.md` §*One act, one owner* | The run judges nothing and the orchestrator runs it before the sealer is spawned. Unchanged; one sentence is added saying what the run prints and that it draws nothing |
| `docs/the-broad-gate.md` §*Where the stamp is drawn* | The `Stop`-hook mechanics that survive: a values file under `<git-common-dir>/specseal-stamp/<session>/`, drawn once by the main session's `Stop`, a subagent's end draws nothing, the message under `MESSAGE_BUDGET`, claim before print. The section itself leaves this document (S13); what survives moves with its markers |
| `docs/the-commit-gate-inside-git.md` §*The commit gate inside git* | `post-commit` runs in the git process, in the worktree the commit landed in, after a commit `pre-commit` judged; `CLAUDE_CODE_SESSION_ID` reaches git's hooks; a clone whose hooks slot is foreign runs none of the stubs. This is where the trigger lives (S4) and why it can know which worktree and which session |
| `skills/verify/SKILL.md` §*The hand-back's labels carry the claims, and the one seal is the sealer's* | The one seal over the whole project is the sealer's `guarantee.md`; the stamp is its drawing and nothing else's. The **Form** bullet there is rewritten to say so (S13) |
| `skills/implement/SKILL.md` §*3. The SDD file set* | A hook's output, a gate's printed line, an agent's instructions and the words a person reads all change: the top rung, which is why this frame exists |
| `docs/the-reader-registry.md` §*A frame names what its work removes* | The `## Removes` table below, read by the review against the diff |
| #969's `plan.md` §*Alternatives considered*, row 4 | The hook's name was kept because no reader had decided whether the stamp is the gate's or the sealer's. This item is that reader: the stamp is the sealer's, so `hooks/sealer-stamp.py` and `bin/seal-stamp` keep their names and the words inside them change (S11) |
| #957's `spec.md` §*How the rewrite is proved not worse*, #969's body (guards 1–3), `evals/README.md` | An agent whose read set changed is measured again under the five rules of `noninferiority.py#verdict`, against the latest reference and never an absolute. The sealer's reference is #969's `evals/reference-sealer.json` (rev `1483d8ba`, `suite_tree` `5c3e8119…`) |
| `questions.md` Q5, Q7 and Q8, answered 2026-10-18 by the orchestrator under the owner's delegation; `rounds/round-3.md` finding 2, `rounds/round-4.md` finding 1, `rounds/round-5.md` finding 1 | Once per work item takes the never-twice direction. The history alone cannot tell a `sealed` that drew nothing from one whose stamp was drawn before its history was rewritten, so any earlier commit of HEAD's history whose guarantee read one `Verdict:` of `sealed` counts as stamped, whatever that verdict's `Target SHA` named, and a work item that then draws no stamp is the gap #976 carries. The reframe after round 5 stands on these rows, and S7, S8, S10 and `plan.md` B1 read as they do because of them |

## Scope

**In.**

- The broad gate (`skills/verify/scripts/broad_gate.py`, `bin/broad-gate`,
  `bin/broad-gate.cmd`) prints a pass line that does not say `SEALED`, writes
  no stamp values file, and draws nothing on any stream.
- The stamp is queued at the commit of a `guarantee.md` whose one `Verdict:`
  reads `sealed`, by the plugin's git `post-commit` hook
  (`hooks/git/post-commit.py` → `hooks/commitgate.py#post_commit`), once per
  work item, and drawn by `hooks/sealer-stamp.py` at the end of the main
  session's turn as today.
- Once per work item in the never-twice direction (Q8): the four facts S7
  and S8 name, read from the clone and the tree with no count beside them,
  and the gaps that direction accepts stated once where a person looks for
  a stamp that did not appear (S10).
- The words: `hooks/sealer-stamp.py`, `hooks/dispatch.py`, `bin/seal-stamp`,
  `bin/seal-stamp.cmd`, `skills/verify/scripts/seal_stamp.py`, both READMEs,
  `docs/the-broad-gate.md`, `docs/the-review-record.md`,
  `docs/the-commit-gate-inside-git.md`, `skills/code-review/orchestration.md`,
  `skills/verify/SKILL.md`, `agents/sealer.md`, and the test that pins the
  bin inventory's one-line descriptions.
- `tests/test_one_word_one_meaning.py` holds the gate's files to never saying
  `SEALED`, and sweeps the files this work touches for the bare `the seal`.
- The sealer measured once, against #969's reference, because one clause of
  its definition changes.

**Out, and why.**

- `.github/scripts/release_seal.py` and `tests/test_the_release_seal_is_drawn.py`:
  the release seal is a PNG the tag push draws over a release that shipped
  (#718, #832), not a stamp over a work item and not the gate's line; #975's
  rule is about the work item's stamp and the gate's pass line. Whether the
  word `SEALED` may stand on it is a question for the owner, named in the
  report and not asked here.
- Renaming `hooks/sealer-stamp.py`, `bin/seal-stamp`, `seal_stamp.py` or the
  `specseal-stamp/` directory: the names now say the true thing (S11), and a
  rename is a hook-registration change (`dispatch.GROUPS["stop"]`, the
  README rows, `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_the_hook_is_registered_for_stop_and_nothing_else`)
  that buys nothing a reader needs.
- The stamp's drawing itself — the disc, the letter twin, the budget, the
  claim: unchanged. What changes is who writes the values and from what.
- `agents/warden.md`, `agents/smith.md`, `agents/framer.md`,
  `agents/scribe.md`, `skills/agent-contract/SKILL.md`: none names the stamp
  or the gate's line (`git grep -n -F stamp -- agents/ skills/agent-contract/`
  at `a09ed4ce` hits `agents/sealer.md:99-100` alone), so no other
  definition changes and no other agent is measured.
- A person's own commit of a `sealed` guarantee, with no Claude session
  behind it: `commitgate._context` returns None without a session and the
  stub short-cuts on the variable (`docs/the-commit-gate-inside-git.md`
  §*A commit with no Claude session behind it*), so nothing is queued. The
  stamp is the drawing at a session's turn end, and a person at a keyboard
  has no turn; the pull request's check says the work was sealed.
- A clone whose git hooks slot is somebody else's (`core.hooksPath`, a hook
  file without the marker): the stubs do not run there, so no stamp is
  queued. Stated in §*The stamp*'s unchecked paragraph; no second trigger is
  added for it (`plan.md` Alternatives, row A3).
- A trigger or a repair for the gaps the never-twice direction accepts: a
  `sealed` committed where nothing could draw (a foreign hooks slot, a
  person's own commit, local mode) or over a commit the branch does not hold
  reads as stamped from then on, so no later commit of that history draws the
  work item's stamp. Q5, Q7 and Q8 accept each, #976 carries them, and S10
  states them; building a way out here would reopen the direction Q8 closed.
- The amend of the sealing commit itself in a second clone, which draws the
  stamp again there: its parent predates the guarantee and its row is the one
  just written, so none of S7's four facts sees it. Round 3 named it and the
  orchestrator left it standing (`rounds/round-3.md` §*Not judged*,
  `overview.md`'s round-3 row); Q8 was not asked about it and this reframe
  does not decide it. It stays a stated limit, and its fail direction is one
  more stamp in that clone.

## User scenarios & acceptance *(mandatory)*

One row per scenario — these become the review's stage-1 checklist and the
regression tests' skeleton. The word rule for the gate's heads is
`BROAD GATE PASSED` / `BROAD GATE FAILED`, chosen beside the gate's own
`PREFLIGHT PASSED` / `PREFLIGHT FAILED` (`broad_gate.py:2886-2887`), and
`questions.md`'s head says why that was a decision and not a question.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The gate's lines never say `sealed` | Given a green tree, when `broad-gate --base <base> --record <item>` runs, then its stdout opens `BROAD GATE PASSED   <branch> @ <tree> against <ref> @ <base>` and holds no line beginning `SEALED`; on a red tree it opens `BROAD GATE FAILED   <names>` with the failing checks under it, and no `NOT SEALED`. The token `SEALED` and the phrases `NOT SEALED`, `a sealed run`, `the sealed run`, `a recorded seal`, `seals nothing`, `nothing is sealed`, `is sealed`, `was sealed` appear nowhere in `broad_gate.py`, `bin/broad-gate`, `bin/broad-gate.cmd` or `docs/the-broad-gate.md` | `tests/test_one_word_one_meaning.py::test_the_gate_never_says_sealed` (new, seen red against `a09ed4ce`); `tests/test_the_seal_is_taken_once_by_the_sealer.py` — the cases that read the head (`test_a_green_tree_is_sealed_with_every_check_run_in_order`, `test_a_failing_test_is_not_sealed_and_is_new_when_the_base_passes`, `signal_lines`, `head_of`) rewritten to the new heads; `tests/test_the_gate_asks_the_range_ci_will_ask.py:450,565,573-579`; `tests/test_the_gate_names_every_step_ci_runs.py:396,413,740`. Protects: a reader taking a green suite for the sealer's verdict, which #967's run showed a person on 2026-10-18 |
| S2 The gate draws nothing and writes no values file | Given a green recorded run, when it ends, on a terminal or a pipe, with or without `--record`, then no file appears under `<git-common-dir>/specseal-stamp/`, no half-block or letter-twin drawing is printed, and `broad-gate.md` is written as before | `tests/test_the_seal_is_taken_once_by_the_sealer.py`: `test_a_recorded_seal_on_a_pipe_signals_and_draws_nothing`, `test_the_values_file_holds_this_runs_panel`, `test_a_run_with_no_session_says_so_and_names_the_hand_command`, `test_values_that_cannot_be_written_leave_the_seal_standing`, `test_a_person_at_a_terminal_sees_the_stamp_drawn_once`, `test_a_terminal_run_with_no_record_draws_nothing` replaced by one case per stream asserting the values dir stays absent and the output is S3's form (seen red: the old gate writes the file). Protects: a stamp drawn while the sealer has read nothing (#975's finding on #967, 977b0408 → 830a7209) |
| S3 The gate's report has one form | Given any run, when it prints, then the head of S1, then the panel rows as plain text — `tree`, `base`, `item`, `gate`, a blank, `suite`, `chain`, `CI also`, `rounds` with the owner's `✓ · →` marks and `fit`/`wrapped` widths, no `SEALED` title row and no disc — then the `broad-gate.md … not committed` line where git still sees it; the same bytes on a terminal and a pipe, the letter twin's ASCII marks on a console that is not UTF-8 | the panel cases of `tests/test_the_seal_is_taken_once_by_the_sealer.py` (`test_no_value_on_the_panel_is_wider_than_the_frame_gives`, `test_the_suite_carries_its_counts_and_nothing_under_them`, `test_the_result_rows_carry_a_tick_and_a_blank_row_stands_before_them`, `test_rounds_counts_the_records_and_what_was_deferred`, `test_a_capped_run_is_sealed_with_its_deferral_on_the_stamp` renamed) with the title row dropped from their expectations; `test_a_recorded_seal_says_the_file_is_written_and_not_committed`, `test_the_line_is_absent_where_the_file_is_committed` kept; `tests/test_the_gate_names_every_step_ci_runs.py::test_the_stamp_says_how_many_steps_the_seal_did_not_answer` re-pointed at the printed rows. Protects: the counts a person read off the stamp's panel leaving the tree with the drawing |
| S4 A `sealed` guarantee's commit queues one stamp | Given a clone carrying the plugin's stubs and a Claude session, when a commit adds or changes `seal/specs/<id>/guarantee.md` whose one `Verdict:` reads `sealed` and whose `Target SHA` row carries no earlier run reading `sealed`, then `post-commit` writes one values file under `<git-common-dir>/specseal-stamp/<session>/`, named `<ns>-<id>-<target sha>.json`, and prints one line naming the file and `seal-stamp --from <quoted path>`; the main session's `Stop` draws it once after the turn's text | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_a_sealed_guarantees_commit_queues_one_stamp` (new, seen red: `a09ed4ce`'s hook queues nothing), the existing `test_the_main_sessions_stop_draws_each_undrawn_file_once` over the file it wrote; `tests/test_the_commit_gate_decides_at_the_commit.py` §*post-commit* gains the line's case. Protects: a verdict committed and never drawn |
| S5 `withheld` and `undecided` queue nothing | Given the same commit with `Verdict: withheld — …` or `undecided — …`, then no file is written and nothing printed about a stamp | `…::test_a_withheld_or_undecided_guarantee_queues_nothing` (new). Protects: the finished-work stamp over unfinished work |
| S6 A re-seal after `withheld` draws the stamp then | Given a `guarantee.md` whose `Target SHA` reads `<sha2> against <base>; earlier run: <sha1> withheld` and whose verdict reads `sealed`, when committed, then one file is queued | `…::test_a_reseal_after_withheld_queues_the_stamp` (new). Protects: #975 item 3's first half |
| S7 A second `sealed` draws nothing new, in any clone | Given a commit whose `guarantee.md` reads one `Verdict:` of `sealed`, when its `Target SHA` row's `; earlier run:` chain carries a run reading `sealed`, or the guarantee read one `Verdict:` of `sealed` at any earlier commit of HEAD's history (`git log HEAD^ -- <path>`, each read as committed), whatever that earlier verdict's `Target SHA` named and whether or not that commit's history held it, then nothing is queued and nothing printed, in the clone that drew the first stamp or another of the same branch, after a rebase of the branch among them. A `sealed` that drew nothing counts the same, and the work item draws no stamp afterwards: the gap Q5, Q7 and Q8 accept and #976 carries. As reframed after round 5 | `…::test_a_second_sealed_verdict_queues_nothing` (the row; kept), `…::test_a_sealed_item_recommitted_in_another_clone_queues_nothing` (round 3; kept), `…::test_a_sealed_item_rebased_in_another_clone_queues_nothing` (new: `rounds/round-5.md` finding 1's fenced case, body unchanged, placed after round 3's; red against `seal_stamp.py` as a226da11 left it, which 96cd142b still carries, green with the loop body round 3 gave). `…::test_a_seal_that_queued_nothing_does_not_count_as_stamped` leaves the module and gets no twin: what it held is the gap this row accepts. Protects: #975 item 3's second half, the owner's never twice, held by the tree's own history and row and no stored count |
| S8 A stamped work item's guarantee queues no second file in the clone that drew it, and a verdict carried off its branch queues none | Given a values file `*-<id>-<any target>.json` or its `.drawn.json` under any session's directory of the clone, when a commit touches that work item's `guarantee.md` again (an amend, a re-commit, a re-seal whose row was written fresh at a new commit), then nothing is queued and nothing printed. Given a `sealed` whose `Target SHA` is not in the committing commit's own history (a squash or a cherry-pick elsewhere, or a SHA the clone does not hold), then nothing is queued. As round 1's fix (33a5b676) built it | `…::test_a_recommit_of_the_same_guarantee_queues_no_second_file`, `…::test_a_reseal_whose_row_lost_its_earlier_run_queues_nothing`, `…::test_a_squash_of_a_sealed_item_in_another_clone_queues_nothing` (all kept). Protects: two stamps from one verdict in the clone that drew the first; a stamp for a verdict stamped where it was made |
| S9 The stamp names what was sealed | Given the queued file, when drawn, then its label reads `SEALED <branch> @ <target sha> against <base> · <id>` and its rows are `SEALED`, `tree` (the branch on the row under), `base`, `item`, `gate ✓ <run>` from `broad-gate.md`'s newest run, `rounds <N>` from the item's `rounds/round-*.md` at HEAD; `scale` is not written | `…::test_the_guarantee_stamps_rows_are_read_from_the_records` (new); `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_stamp_draws_byte_for_byte_what_it_drew_at_the_default_scale` kept; `test_a_values_file_draws_whatever_scale_it_carries` kept (older files still draw). Protects: a stamp that says less than the pull request's check knows; `questions.md` Q1 is the owner's to overturn |
| S10 The hook's silence is stated where a person looks | Given no stamp appeared, when a person reads `docs/the-review-record.md` §*The stamp*'s unchecked paragraph, then it names where nothing is queued — a foreign hooks slot, local mode, a person's own commit (the build added the last two, `overview.md`), and, since the reframe, a guarantee whose history already read `sealed` and whose verdict then drew nothing, a `sealed` over a commit the branch does not hold among them, with #976 as where that gap is carried — then where the hook draws nothing from a file it wrote (a `python3` that cannot load `seal_stamp.py`, a main session outside the clone, a plugin older than the hook) and `seal-stamp --from <path>` for those. The clause the reframe adds carries the phrase `already read \`sealed\` and that verdict drew nothing` | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`, whose `silence` tuple gains that phrase (red against the paragraph as it stands); `tests/test_docs_line_wrap.py`. Protects: a missing stamp read as a missing seal, and the never-twice gap met with no sentence saying it was chosen |
| S11 The names say what draws the stamp | Given `hooks/sealer-stamp.py`'s docstring, `bin/seal-stamp`'s header, `seal_stamp.py`'s docstring and `main`'s description, `hooks/dispatch.py`'s `stop` comments, both READMEs' `sealer-stamp` rows and side-effect sentences, and the bin inventory's description, when read, then each says the stamp is the sealer's, drawn from a `sealed` guarantee at its commit, and none says the broad gate draws or writes it | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_both_readmes_list_the_stamp_hook` with its pinned clauses rewritten; `tests/test_a_reference_root_is_read_and_never_taken.py:192` (`"draws the sealer's stamp from a sealed guarantee"`); `tests/test_a_gate_that_fails_says_so.py::test_the_walk_agrees_with_its_twin_in_sealer_stamp` kept; `tests/test_one_word_one_meaning.py`'s `SEAL_SWEPT` extended to `hooks/sealer-stamp.py`, `hooks/dispatch.py`, `hooks/commitgate.py`, `bin/seal-stamp`, `bin/broad-gate`, `docs/the-broad-gate.md`. Protects: #969 row 4's open question closing the wrong way by silence |
| S12 The sealer is told, and proved not worse | Given `agents/sealer.md`, when read, then its `## Never` bullet says it draws no stamp and that the stamp is drawn in the orchestrator's session from the sealer's committed `sealed` verdict, once per work item; `from its own run` is gone. Given the build, when phase 4 runs, then `evals/sealer-phase-4.md` reads `pass` under the five rules against #969's `evals/reference-sealer.json`, or `fail` on rule 4 or 5 alone with the cause named | `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_the_sealer_is_told_the_gate_draws_nothing_and_neither_does_it` rewritten; `tests/test_the_sealer_guarantees.py::TestDefinition` green; `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`; `noninferiority.py check` exit 0. Protects: a definition changed and never measured (#967 guard 1) |
| S13 The documents say it once, where it is read | Given `docs/the-review-record.md`, then a `## The stamp` section stands between `## The guarantee` and `## The run`, carrying the drawing rule with its `Enforced by:`, the budget paragraph under #717's marker, and the unchecked paragraph; `docs/the-broad-gate.md` has no `## Where the stamp is drawn` and §*One act, one owner* says the run prints `BROAD GATE PASSED`/`FAILED` and draws nothing; `skills/code-review/orchestration.md`'s stamp paragraph says the stamp is drawn at the end of the turn in which `guarantee.md` reading `sealed` was committed, and the orchestrator draws none; `skills/verify/SKILL.md`'s **Form** bullet says the sealer's seal is drawn from its `sealed` guarantee's commit and the gate draws nothing | `…::test_the_policy_states_the_budget_and_names_its_case`, `…::test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`, `…::test_the_orchestrator_is_told_the_stamp_is_drawn_for_it`, `…::test_the_form_bullet_says_what_draws_the_final_seal` re-pointed and rewritten; `tests/test_the_sealer_guarantees.py::TestDefinition::test_the_orchestration_quotes_what_only_the_gate_can_tell` kept; `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_documents_say_where_the_panel_now_carries_each_name`, `::test_the_docstrings_describe_the_letter_and_the_rows_it_carries`, `::test_the_documents_name_the_ci_also_row` rewritten; `bin/rules --check` exit 0 (every `Enforced by:` resolves); `tests/test_docs_line_wrap.py` green. Protects: two documents stating the drawing rule, one of them stale |
| S14 The stubs are not rewritten | Given the installed stubs, when `hook-install.py` runs, then it rewrites nothing: `hooks/git/post-commit.py`'s bytes are unchanged and the second duty lives in `commitgate.post_commit` | `tests/test_the_hooks_are_installed_where_git_runs_them.py` green; `git diff --stat <base> HEAD -- hooks/git/` empty. Protects: a release whose first commit in every clone rewrites three hooks |

## Data & interfaces

- **The values file** (`seal_stamp.write_values`): keys unchanged for the
  hook — `rows`, `branch`, `tree`, `base`, `from`, `item`, `pr`, `session` —
  with `tree` the guarantee's `Target SHA` commit, `base` its base, `from`
  None (the guarantee names a commit, not a ref), `branch` the committing
  worktree's branch (`broad_gate.py#branch_name`'s reading, moved beside the
  writer), `pr` None, `item` the work item's directory. `scale` is not
  written: 0.22.1 is the first release after 0.21, which
  `docs/the-broad-gate.md:177-181` named as when the key stops. The file's
  name is `<time ns>-<id>-<target sha>.json`, so `pending`'s name sort stays
  oldest first and S8's twin check is a suffix match over
  `<git-common-dir>/specseal-stamp/*/`.
- **The writer**: a function in `skills/verify/scripts/seal_stamp.py`,
  `queue_for_guarantee(top, common, session)`, which asks git for the paths
  the commit at HEAD touched (`git diff-tree --no-commit-id --name-only -r
  HEAD`), reads each matching `seal/specs/*/guarantee.md` as committed
  (`git show HEAD:<path>`), and judges it with
  `skills/code-review/scripts/chain_check.py`'s own readers — `verdicts_of`,
  `verdict_word`, `target_of`, `newest_run`, `EARLIER_RUN` — plus one new
  reader there, `earlier_verdicts(cell)`, so the `Target SHA` row has one
  grammar. Called from `hooks/commitgate.py#post_commit` after the notice,
  through the same loader shape `_notice_module()` uses; a failure inside it
  prints nothing and returns 0, the shape the notice already has.
- **The once reader, as reframed**: `seal_stamp.sealed_before(chain, top,
  path)` is True where `path` read one `Verdict:` of `sealed` at any commit
  `git log --format=%H HEAD^ -- <path>` lists, each read as committed with
  `git show <sha>:<path>` and judged with `chain.verdicts_of` and
  `chain.verdict_word` alone. It asks nothing of that verdict's `Target SHA`:
  no `target_of`, no `merge-base`. `_queue_one`'s order of refusals stays as
  the rounds left it — no `sealed`, no target, the row's chain reads
  `sealed`, `sealed_before`, `already_queued`, the target not an ancestor of
  HEAD — and the last of those is the only ancestry test left, on the
  committing commit's own verdict.
- **The line `post-commit` prints** on stdout, where git prints it into the
  command's output:
  `specseal: the stamp for <id> is drawn at the end of this turn from <path>; where none appears, \`seal-stamp --from <quoted path>\` draws it`.
- **The gate's heads**: `GATE_PASSED = "BROAD GATE PASSED   {names}"` and
  `GATE_FAILED = "BROAD GATE FAILED   {names}"` in `broad_gate.py`, beside
  `PREFLIGHT_PASSED`/`PREFLIGHT_FAILED`; `seal_stamp.sealed_names` stays the
  one composer of `<branch> @ <tree> against <ref> @ <base>` (the stamp's
  label uses it too); `seal_stamp.not_sealed` moves to `broad_gate.py` as the
  failure form under the new head.
- **The panel's text rules** — `PANEL_VALUE_WIDTH`, `ELISION`, `fit`,
  `wrapped`, `SEP`/`ARROW`/`TICK`/`DOT`, `item_value` — move from
  `broad_gate.py` to `seal_stamp.py`, which draws them and whose writer now
  composes rows; the gate imports them through `stamp_module()` for its plain
  report. `rounds_rows` stays the gate's (it reads the deferral homes the
  gate's `chain` arm knows); the stamp's `rounds` row is a count.
- **`chain_check.py`**: `SEALED = "sealed"` unchanged — it is the verdict
  word; `earlier_verdicts(cell)` added.

## Rule changes

- nothing
  why: written: the gate draws nothing and the stamp is drawn from the sealer's verdict, in
    docs/the-broad-gate.md and docs/the-review-record.md.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The gate's values-file write and the names of its outcomes | `skills/verify/scripts/broad_gate.py#signal`, `SESSION_VAR`, `NOTHING_RECORDED`, `VALUES_UNWRITTEN`, `NO_SESSION_FOUND`, `DRAWN_AT_TURN_END`, `SCALE_FOR_OLDER_HOOKS`, `common_dir` | `seal_stamp.queue_for_guarantee`, called by `hooks/commitgate.py#post_commit`; the `scale` key is written by nothing (first release after 0.21) |
| The gate's terminal drawing and the terminal/pipe fork | `broad_gate.py#main` lines 3084-3093 (`if terminal and item is not None`), the `is_terminal` import and `console_is_terminal` argument | One form (S3); `seal_stamp.is_terminal` stays for `pick_shape`'s callers if any still need it, else goes with its case |
| `SEALED` / `NOT SEALED` as the gate's heads | `broad_gate.py#signal` (`head = f"SEALED   …"`), `seal_stamp.py#not_sealed` (`NOT SEALED   …`), `broad_gate.py:2883-2885`'s comment | `GATE_PASSED`/`GATE_FAILED` in `broad_gate.py`; the failure form moves there |
| The panel's `SEALED` title row in the gate's rows | `broad_gate.py#panel` (`rows = [("SEALED", ""), …]`) | The gate's report has no title row; `seal_stamp.TITLE_ROW` stays for the stamp, written by the writer |
| `docs/the-broad-gate.md` §*Where the stamp is drawn* (three paragraphs, two markers) | `docs/the-broad-gate.md:117-185` | `docs/the-review-record.md` §*The stamp*, rewritten to the new trigger; the budget paragraph moves with #717's marker; one sentence stays in §*One act, one owner* |
| The orchestrator's stamp paragraph as it stands | `skills/code-review/orchestration.md:241-260` (*The stamp is drawn for you … (#400)*) | Rewritten in place: the stamp is drawn at the end of the turn in which `guarantee.md` reading `sealed` was committed; `broad-gate`'s lines are quoted as `BROAD GATE PASSED`/`FAILED`; the `seal-stamp --from` line is `post-commit`'s |
| The sealer's clause *from its own run* | `agents/sealer.md:99-100` | Rewritten: the stamp is drawn in the orchestrator's session from the sealer's committed `sealed` verdict, once per work item |
| The **Form** bullet's account of the gate drawing | `skills/verify/SKILL.md:252-258`, and `:426` (*the `SEALED` line names it as*) | Rewritten in place to the guarantee's commit; `:426` names the gate's pass line |
| The hook's docstring sentences about the gate's `SEALED` line | `hooks/sealer-stamp.py:2-12, 53-59`; `hooks/dispatch.py:27-29, 115-118, 566-578` comments | Rewritten in place |
| The bin header and the module docstring saying the gate stamps | `bin/seal-stamp:2-8`, `bin/seal-stamp.cmd`, `skills/verify/scripts/seal_stamp.py:1-70, 857-864` (`description="Print the broad gate's stamp…"`) | Rewritten in place |
| README sentences saying the gate leaves the stamp | `README.md:180, 209-210`; `README.ko.md:172, 200-202` | Rewritten in place; the pinned clauses of `test_both_readmes_list_the_stamp_hook` follow |
| The bin inventory's description | `tests/test_a_reference_root_is_read_and_never_taken.py:192` (`"draws the broad gate's stamp"`) | `"draws the sealer's stamp from a sealed guarantee"` |
| Six gate cases about the values file and the terminal drawing | `tests/test_the_seal_is_taken_once_by_the_sealer.py:2909-3047` (named in S2) | Replaced by S2's cases; the hook's own cases in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` stay and gain S4–S9 |
| *Reframed after round 5.* `sealed_before`'s condition on the earlier commit's own target, and the case that held it | `skills/verify/scripts/seal_stamp.py:1078-1080` at 96cd142b (`target = chain.target_of(reader, text)` and the `merge-base --is-ancestor` on it), the clause `over a commit then in its history` in its docstring, in `queue_for_guarantee`'s docstring (1035) and in the once comment (920-921); `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py:772-789` (`test_a_seal_that_queued_nothing_does_not_count_as_stamped`); the same clause in `docs/the-review-record.md:286-288` and that case's entry on the `Enforced by:` line at 292 | The loop body round 3 gave (`rounds/round-5.md` finding 1's first fenced block); the case gets no twin, because what it held is the gap Q8 accepts, and `test_a_sealed_item_rebased_in_another_clone_queues_nothing` takes its place on the `Enforced by:` line; the sentence returns to round 3's words (`rounds/round-5.md` finding 1's second fenced block) |
| *Reframed after round 5.* The fragment's clause that a repaired row draws the stamp | `changelog.md:19-20` under this directory (`a later commit that corrects that row in place draws the stamp`) | Rewritten in the same commit as the code: after a `sealed` over a commit the branch does not hold, the work item draws no stamp, and #976 carries the gap (`docs/the-record-layout.md` §*A commit after the build brings its changelog fragment along*) |

## Open questions → questions.md

Anything a planner must answer lives in questions.md, not inline — unanswered
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

Framed 2026-10-18 by framer, before the build.
Reframed 2026-10-18 by framer, after round 5.
