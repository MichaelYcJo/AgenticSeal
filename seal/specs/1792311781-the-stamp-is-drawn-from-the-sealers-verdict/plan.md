# Implementation Plan: the stamp is drawn from the sealer's verdict (#975)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-18 by the orchestrator, under the owner's `automation` answer, when `smith` was spawned.
Approved 2026-10-18 by the orchestrator, under the owner's `automation` answer, when `smith` was spawned for the reframe after round 5.

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

The stamp moves from the broad gate's run to the sealer's verdict. The gate
prints `BROAD GATE PASSED` or `BROAD GATE FAILED`, shows its panel as plain
text, and writes no values file and no drawing on any stream. The plugin's
git `post-commit` hook, which already runs after every judged commit in the
worktree the commit landed in, reads the committed `guarantee.md`: where its
one `Verdict:` reads `sealed` and its `Target SHA` row carries no earlier run
reading `sealed`, it writes one values file for the session, named by the
work item and the audited commit, and the `Stop` hook draws it at the end of
the turn exactly as today. Once per work item is held by what the clone and the
tree carry, with no stored count, and as reframed after round 5 it takes the
never-twice direction: the values file's name carries the work item's id; the
audited commit stands in the committing commit's history; the guarantee read
`sealed` at no earlier commit of that history, whatever that verdict named;
and the `Target SHA` row's `; earlier run:` chain reads no `sealed`. A
`sealed` that drew nothing counts as stamped all the same, and the work item
that then draws none is the gap `questions.md` Q5, Q7 and Q8 accept and #976
carries. The file names
`hooks/sealer-stamp.py` and `bin/seal-stamp` stay, because they now say the
true thing; the words inside them, the READMEs, three documents, the
orchestration file and one clause of `agents/sealer.md` are rewritten in
place, and the sealer is measured once against #969's reference because its
definition changed.

## Technical context

Existing code this builds on (file:line coordinates at `a09ed4ce`), constraints,
and the failure scenario of the chosen approach.

- **The gate's seal path.** `skills/verify/scripts/broad_gate.py#main`
  (3084-3110) forks on `terminal`: on a terminal it draws
  `stamp.stamp(rows, shape)`; on a pipe it prints `signal(...)` (3195-3245),
  which writes the values file through `seal_stamp.write_values` and returns
  `SEALED   <names>` plus one of `NOTHING_RECORDED`, `VALUES_UNWRITTEN`,
  `NO_SESSION_FOUND`, `DRAWN_AT_TURN_END` (3127-3147). The panel's rows come
  from `panel` (2640-2720), whose first row is `("SEALED", "")`. The failure
  form is `seal_stamp.not_sealed` (621-639), head `NOT SEALED   <names>`.
  The preflight's heads `PREFLIGHT PASSED`/`PREFLIGHT FAILED` (2886-2887)
  are the precedent for the new heads.
- **The drawer.** `hooks/sealer-stamp.py` runs in `dispatch.GROUPS["stop"]`
  (`hooks/dispatch.py:118`), only on the main session's `Stop`, reads
  `seal_stamp.pending(values_dir(common, session))`, draws each file whole
  before claiming it, holds the message under `MESSAGE_BUDGET`. None of this
  changes. `seal_stamp.py` owns the file (`write_values` 720-737,
  `read_values` 739-775, `pending` 777-791, `claim` 793-807, `label` 809-829)
  and the drawing (`stamp` 517, `fitted` 569). `label` reads `branch`,
  `tree`, `base`, `from`, `pr`, `item` — the keys the writer keeps.
- **The commit hook.** `hooks/git/post-commit.py` calls
  `hooks/commitgate.py#post_commit(cwd, environ, stream)` (315-326):
  `_context` (49-61) resolves the top, the common dir and the session, and
  returns None for a clone not opted in or a commit with no Claude session;
  then `_notice_module().notify(cwd, session)` prints the implementer notice
  and every exception returns 0. The second duty goes in after the notice,
  in the same shape. `CLAUDE_CODE_SESSION_ID` reaches git's hooks
  (`hooks/hooksession.py:6, 48`; `docs/the-commit-gate-inside-git.md` §*A
  commit with no Claude session behind it*). The stub's bytes are
  `hooks/hook-install.py`'s and do not change, so no clone's hooks are
  rewritten (S14). Latency today: 209–400 ms a judged commit
  (`docs/the-commit-gate-inside-git.md:233-236`); the new reader adds one
  `diff-tree` and, only where a `guarantee.md` was touched, one `show` and
  the record reads — `questions.md` Q2 measures it.
- **The verdict's readers.** `skills/code-review/scripts/chain_check.py`:
  `SEALED = "sealed"` (84), `EARLIER_RUN = "; earlier run: "` (101),
  `target_of` (1355), `newest_run` (1364), `verdicts_of` (1597),
  `verdict_word` (1607), `guarantee` (1619). One new reader,
  `earlier_verdicts(cell)`, splits the `Target SHA` cell on `EARLIER_RUN`
  and yields `(sha, word)` per earlier run, so S7 reads the row with the
  grammar the check already has.
- **The policy's pins.** `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`
  pins the documents at 934-1144 (five cases) and the registration at 491;
  `tests/test_the_seal_is_taken_once_by_the_sealer.py` pins the gate's lines
  (57 `SEALED` hits), the documents at 3228, 3608, 3694, 3774, and the sealer
  at 8217-8492; `tests/test_the_sealer_guarantees.py::TestDefinition`
  pins `agents/sealer.md`; `tests/test_a_reference_root_is_read_and_never_taken.py:192`
  pins the bin description; `tests/test_one_word_one_meaning.py:187-237`
  holds `SEAL_SWEPT`. `bin/rules --check` resolves every `Enforced by:`.
- **The sealer's reference.** #969's `evals/reference-sealer.json`: rev
  `1483d8ba`, `suite_tree` `5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447`,
  preload 24,702 bytes, 37,080.5 tokens per tool call, 3.3898 USD, 68 of 68
  graders (`seal/specs/1792252400-…/phases/phase-6.md:70-77`, `read`). At
  `a09ed4ce`, `git rev-parse HEAD:evals/behaviour/sealer` prints
  `5c3e81195bb9d2319018e2f3abfd5aaf1d9e5447` and `git diff --stat 4a6e24f6
  HEAD -- evals/behaviour/sealer` is empty (`executed`), so a new side run
  with `--suite-rev <build commit>` has the reference's suite tree and
  `compare` accepts it. `1483d8ba` resolves in this clone (`executed`).
- **The milestone's rule.** `routing.md`: the owner pressed `automation`;
  smith, warden and sealer on Opus 5.5. #967 guard 1: an agent whose read set
  changed is measured here. Only `agents/sealer.md` changes; every other
  definition preloads the contract alone (`agents/*.md` `skills:` lists,
  `read`) and the contract is untouched.

- **The once reader as the rounds built it** (coordinates at 96cd142b,
  `read`). `already_queued` (983-1010) matches the work item's id alone in
  every session's directory. `_queue_one` (1084-1136) refuses in this order:
  no single `sealed`, no target, the row's `; earlier run:` chain reads
  `sealed`, `sealed_before`, `already_queued`, the target not an ancestor of
  HEAD. `sealed_before` (1060-1081) walks `git log --format=%H HEAD^ --
  <path>` and reads each commit's guarantee with `git show`; at a226da11 it
  counts a `sealed` only where `merge-base --is-ancestor <its target> <that
  commit>` holds. Round 5 measured that condition queueing a second stamp
  after a rebase in a second clone and in a fresh clone of a force-pushed
  branch, and the `rev-parse -q --verify <target>^{commit}` form still
  queueing one in the fresh clone (`rounds/round-5.md` probe rows 2-4,
  `executed` there). Round 3's form, eb4303b4's loop body, queued nothing in
  all three and failed round 4's case, the repaired row (same record, probe
  row 2). Those two records are the whole measurement this reframe stands
  on; nothing was run here.

**What breaks in six months.** The trigger rests on the plugin's git stubs
being the clone's hooks. A clone that sets `core.hooksPath`, or a hook file
without the marker, runs no stub, so a `sealed` guarantee committed there
draws nothing and says nothing, and the pull request's check is the only
statement that the work was sealed. After the reframe the same is true of a
`sealed` over a commit the branch does not hold: the history then reads
`sealed`, so the commit that repairs the row draws nothing either, and a
person who expected a stamp finds the sentence in §*The stamp*'s unchecked
paragraph and #976. The failure direction is a missing stamp, never a false
or doubled one, with one limit round 3 stated and this reframe leaves: an
amend of the sealing commit itself in a second clone draws again there. The
orchestration file and §*The stamp* name the silences.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1. The trigger is the git `post-commit` hook** reading the committed `guarantee.md` (chosen) | A foreign hooks slot draws nothing; a person's own commit draws nothing | **Chosen.** It is on the commit's own path, so no act stands between the verdict and the drawing; it runs in the worktree the commit landed in, so a main checkout on another branch is not a problem; the session reaches it; the hook already exists and already has the shape (`post_commit`), so no hook is registered and no stub rewritten. The fail direction is a missing stamp |
| **A2. The orchestrator types a command** after committing `guarantee.md` (`seal-stamp --record <item>` or the like) | The orchestrator forgets, and nothing tells it; one more step in a 314-line procedure; the command is a new flag on a script whose name says it draws | Rejected: `CLAUDE.md`'s first goal prefers the design that asks nothing of a session, and `hooks/implementer.py`'s stance is that a hook catches a session forgetting |
| **A3. Both A1 and A2**, the command for foreign-hook clones | Two writers of one file; the idempotent name saves the double draw, but two paths is the surface the next defect hides in | Rejected; the foreign-hook case is stated, not mechanised |
| **A4. The `Stop` hook reads the tree** for a `sealed` guarantee at HEAD | It cannot know the work item or the worktree: the main session's `cwd` is often the main checkout while the commit landed in a linked worktree; and it starts `git` at every turn's end where today it starts none | Rejected |
| **A5. The `post-bash` PostToolUse hook** reads HEAD after each Bash call | Same worktree problem as A4; a git call per Bash call in an opted-in clone, paid on every command | Rejected |
| **B1. Once per item is held by what the clone and the tree carry**, in the never-twice direction (chosen; as it reads after rounds 1 and 3 and the reframe after round 5). Four facts, no count beside them: the values file's name `<ns>-<id>-<target sha>` matched on the id alone, whatever commit it named (`already_queued`, round 1); the audited commit standing in the committing commit's history (`merge-base --is-ancestor <target> HEAD`, round 1); the guarantee having read one `Verdict:` of `sealed` at no earlier commit of HEAD's history, whatever that verdict's `Target SHA` named (`sealed_before` as round 3 gave it); and the `Target SHA` row's `; earlier run:` chain reading no `sealed` (the frame's original fact) | A `sealed` that drew nothing — committed where no stub runs, by a person with no session, in local mode, or over a commit the branch does not hold — reads as stamped from then on, so no later commit of that history draws the work item's stamp (`questions.md` Q5, Q7, Q8: accepted, #976). An amend of the sealing commit itself in a second clone draws again there (round 3's stated limit, left standing). `tests/test_the_sealer_guarantees.py::TestTemplate::test_the_target_row_keeps_an_earlier_run` holds the row | **Chosen.** The owner's rule says never twice; where the history cannot tell a `sealed` that drew nothing from one rewritten after it drew, the direction that can be wrong is the one the rule accepts, and the gap is stated where a person looks (S10). The third and fourth facts hold across clones; the first two in the clone that drew |
| **B2. A `drawn` marker file per item** under the git dir | A stored fact kept in step with the tree, which `CLAUDE.md` refuses; a new marker beside the one `claim` already writes | Rejected |
| **B3. `sealed_before` counts an earlier `sealed` only where its target is an ancestor of that commit** — a226da11, round 4's fix, the never-missing direction | A rebase rewrites the sealing commit and leaves its `Target SHA` outside its history, so a second clone that rebased the branch, or a fresh clone of the force-pushed branch, queues the work item's stamp a second time (`rounds/round-5.md` finding 1, probe rows 2-3, `executed` there). Rebasing a feature branch onto a moved base is an ordinary step here | Rejected by Q8 (a): the direction it saves, a stamp after a repaired row, is the one the owner's rule accepts losing, and the one it costs is the one the rule forbids |
| **B4. `sealed_before` counts an earlier `sealed` where its target resolves in the clone** (`rev-parse -q --verify <target>^{commit}`) | Holds round 4's repaired row and the rebase made in the same clone; a fresh clone of a force-pushed branch does not hold the pre-rebase commit and queues a second stamp anyway (`rounds/round-5.md` probe row 4: 52 passed, 1 failed) | Rejected: it shrinks the doubled direction without closing it, and a reader cannot say in one sentence which `sealed` counts |
| **C1. Keep the file names `hooks/sealer-stamp.py`, `bin/seal-stamp`, `seal_stamp.py`, `specseal-stamp/`; rewrite the words** (chosen) | A reader who opens `bin/seal-stamp` for the gate's stamp finds the sealer's | **Chosen.** The stamp is the sealer's now, so the names are true; #969 row 4's rename went the other way and is answered |
| **C2. Rename to `guarantee-stamp`** | `dispatch.GROUPS["stop"]`, `test_the_hook_is_registered_for_stop_and_nothing_else`, both README rows, `.test_durations` and every document naming the file | Rejected: a hook-registration change for a name a reader does not need |
| **D1. The gate's report is one form on every stream** — head, panel rows as text, uncommitted line (chosen) | A person at a terminal loses the drawing they saw before | **Chosen.** The drawing was the stamp, and the gate draws none; one form removes the `is_terminal` fork and the case per stream |
| **D2. Keep a terminal drawing of the panel without the disc** | Two forms for one report, and the drawing reads as a stamp | Rejected |
| **E1. The stamp's panel is read from the records**: `tree`+branch, `base`, `item`, `gate ✓ <run>`, `rounds <N>` (chosen) | The owner designed the 2026-10-07 panel with the suite's counts and the deferral homes; those leave the stamp | **Chosen**, as `questions.md` Q1's default: the owner put the stamp apart from the test suite, and the counts stay in the gate's report; Q1 is theirs to overturn |
| **E2. The gate writes its rows to a file the writer picks up** at the guarantee's commit | The gate writes a stamp's rows again, keyed to a run the sealer may yet withhold; two files to keep in step | Rejected |
| **F1. The stamp's policy moves to `docs/the-review-record.md` §*The stamp*** (chosen) | Two tests re-pointed; the markers move | **Chosen.** `docs/the-broad-gate.md` is "the standing account of who takes [the run], what it runs, and what it is allowed to say" (its line 5), and the stamp is no longer something the run says |
| **F2. Rewrite §*Where the stamp is drawn* in place** | The gate's document keeps describing a drawing the gate never makes | Rejected |
| **G1. Measure the sealer alone** against #969's reference (chosen) | A rule-4 fail on a longer clause | **Chosen.** Only its preload changes; #969 §*What a fail means here* governs a fail on rule 4 or 5 alone. About 3.4 USD |
| **G2. Measure nothing**, since the clause is one line | A definition changed and never measured, the thing #967 guard 1 exists to refuse | Rejected |
| **H1. Also change `.github/scripts/release_seal.py`'s `SEALED` label** | A different object (the release's PNG), outside #975's rule, and the owner has not said | Out of scope; named in the report |

## Phases

Vertical slices — each phase ends with something runnable and verified. Each
rule names the test that holds it; for every document sentence a phase
changes, the pins are listed so the smith runs them.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | **The gate stops sealing.** `broad_gate.py`: `GATE_PASSED`/`GATE_FAILED` beside the preflight heads; `signal` reduced to the head and the uncommitted line, writing no file; `main`'s terminal fork gone, one form printing the head, `panel`'s rows as plain text (no title row, the owner's marks, the twin's ASCII where `pick_shape` says so) and the uncommitted line; `not_sealed` moved in as the failure form; `SESSION_VAR`, `SCALE_FOR_OLDER_HOOKS`, `common_dir` and the four outcome strings gone; `PANEL_VALUE_WIDTH`, `ELISION`, `fit`, `wrapped`, `SEP`/`ARROW`/`TICK`/`DOT`, `item_value` moved to `seal_stamp.py` and imported back; the module docstring (75-115), `bin/broad-gate`'s header. `tests/test_one_word_one_meaning.py::test_the_gate_never_says_sealed` written first and seen red | `test_the_gate_never_says_sealed` red at `a09ed4ce`, green after; `bin/test tests/test_the_seal_is_taken_once_by_the_sealer.py tests/test_the_gate_asks_the_range_ci_will_ask.py tests/test_the_gate_names_every_step_ci_runs.py tests/test_a_gate_that_fails_says_so.py -q` green with S1–S3's cases rewritten (the six of S2 replaced, `signal_lines`/`head_of` re-pointed, the panel cases without the title row, `test_the_panel_value_width_is_what_the_stamp_actually_gives` re-pointed at `seal_stamp`); `broad-gate --preflight --base origin/release/v0.22.1` exit 0 on this branch | fe201329 |
| 2 | **The stamp is queued at the guarantee's commit.** `chain_check.py#earlier_verdicts`; `seal_stamp.queue_for_guarantee(top, common, session)` with the file name `<ns>-<id>-<target sha>.json`, the twin check over every session directory, the rows of S9 and the line of S4; `commitgate.post_commit` calling it after the notice through a loader like `_notice_module`, every failure silent and exit 0; `hooks/git/post-commit.py` byte-unchanged; the `scale` key written by nothing | S4–S9's cases in `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, each seen red first (a `sealed` commit queues one; `withheld`/`undecided` none; re-seal after `withheld` one; second `sealed` none; re-commit none; the rows read from the records); `tests/test_the_commit_gate_decides_at_the_commit.py` §*post-commit* gains the printed line's case; `tests/test_chain_check.py` gains `earlier_verdicts`' cases; `tests/test_the_hooks_are_installed_where_git_runs_them.py` green; `git diff --stat a09ed4ce HEAD -- hooks/git/` empty; Q2's latency measured and written in the phase record | 0dd09a37 |
| 3 | **The words and the documents.** `docs/the-review-record.md` §*The stamp* between §*The guarantee* and §*The run* (the drawing rule with its `Enforced by:` naming phase 2's cases; #717's budget paragraph moved with its marker; the unchecked paragraph with the four silences of S10); `docs/the-broad-gate.md` §*Where the stamp is drawn* removed and one sentence in §*One act, one owner*; `docs/the-commit-gate-inside-git.md:14, 233-236` naming `post-commit`'s second duty; `skills/code-review/orchestration.md:241-260` rewritten; `skills/verify/SKILL.md:252-258, 426`; `agents/sealer.md:99-100`; `hooks/sealer-stamp.py` and `hooks/dispatch.py` docstrings; `bin/seal-stamp`, `bin/seal-stamp.cmd`, `seal_stamp.py`'s docstring and `main`'s description; `README.md:180, 209-210`, `README.ko.md:172, 200-202`; `tests/test_a_reference_root_is_read_and_never_taken.py:192`; `SEAL_SWEPT` extended (S11) | The pins, each run: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py` 934-1144 (five cases re-pointed and rewritten, `test_both_readmes_list_the_stamp_hook`'s clauses with them); `tests/test_the_seal_is_taken_once_by_the_sealer.py::test_the_documents_name_the_line_that_says_to_commit_the_cell`, `::test_the_documents_say_where_the_panel_now_carries_each_name`, `::test_the_docstrings_describe_the_letter_and_the_rows_it_carries`, `::test_the_documents_name_the_ci_also_row`, and 8217-8492 (the sealer carries no section's own words); `tests/test_the_sealer_guarantees.py::TestDefinition`; `tests/test_the_rules_have_one_owner.py`; `tests/test_one_word_one_meaning.py`; `tests/test_docs_line_wrap.py`; `tests/test_every_agent_reads_the_contract.py`; `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`; `bin/rules --check` exit 0; `git grep -n -F SEALED -- ':!CHANGELOG.md' ':!changelog/' ':!assets/' ':!seal/specs/' ':!.test_durations' ':!.github/scripts/release_seal.py' ':!tests/test_the_release_seal_is_drawn.py'` hitting only `seal_stamp.py`'s title row and label, `chain_check.py`'s constant and the test modules | dddcdfdc |
| 4 | **The sealer measured.** `python3 evals/scripts/noninferiority.py run --agent sealer --rev <phase 3's commit> --suite-rev <phase 3's commit> --out seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/evals/sealer-phase-4.json --runs 2 -j 4 --max-cost-usd 10`, raw output kept outside the tree; `compare --agent sealer --phase 4 --old seal/specs/1792252400-the-sealer-reads-the-gate-the-orchestrator-ran/evals/reference-sealer.json --new <that json> --out …/evals/sealer-phase-4.md`; the phase record quotes the five rules' rows and the spend. A `fail` on rule 4 or 5 alone is recorded as it reads with the clause named (#969 §*What a fail means here*); a `fail` on rules 1–3 is a cause in the clause, fixed once in one commit, and the side run a second time; no third run | `evals/sealer-phase-4.md` reading `pass`, or `fail` with the cause named and this row saying what was done; `noninferiority.py check` exit 0; `tests/test_a_rewritten_definition_proved_non_inferior.py::test_the_verdict_is_recomputed_from_the_records_numbers`; the Opus side's first trace naming `message.model` as Opus | 826cd0da |
| 5 | **The close.** `overview.md` (one line of purpose, divergences, `## Not verified`, fed-back clauses); `changelog.md` under this directory: the paragraph a plugin user reads (the stamp is the sealer's, drawn once at the commit of a `sealed` guarantee; the gate's line reads `BROAD GATE PASSED`/`FAILED` and draws nothing; `seal-stamp --from` unchanged; a clone with foreign git hooks draws no stamp) and the sealer's row of the per-agent table — `1483d8ba` (24,702 bytes, 37,080.5 tokens per call, 3.3898 USD, 68 of 68) against phase 4's figures, each read from the records with `noninferiority.py#side_numbers`; `questions.md` rows the work and the measurement answered, in words | `bin/rules --check` exit 0; `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.1 --root <worktree> --worktree` exit 0; `bin/unverified-check` on this item; the fragment's figures traced to their records in the phase record | 55747b46 |
| 6 | **Once per work item takes the never-twice direction** (the reframe after round 5, Q8 (a); `spec.md` S7, S8, S10 and B1 above). The case first: `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py::test_a_sealed_item_rebased_in_another_clone_queues_nothing`, `rounds/round-5.md` finding 1's fenced case with its body unchanged, placed after `test_a_sealed_item_recommitted_in_another_clone_queues_nothing`, seen red against `seal_stamp.py` as 96cd142b carries it. Then `seal_stamp.sealed_before`'s loop body returns to round 3's (the first fenced block of the same finding): one `Verdict:` of `sealed` at any earlier commit counts, the `target_of` call and its `merge-base` go; `sealed_before`'s docstring, `queue_for_guarantee`'s docstring and the once comment (920-927) lose `over a commit then in its history` and say instead that a `sealed` that drew nothing counts too and the work item's missing stamp is #976's gap; `test_a_seal_that_queued_nothing_does_not_count_as_stamped` (772-789) leaves the module with no twin. `docs/the-review-record.md` §*The stamp*: the sentence at 286-288 returns to round 3's words (the finding's second fenced block), and on its `Enforced by:` line the removed case's entry becomes the new case's; the unchecked paragraph (330-342) gains one sentence after `which has no turn to draw at.`: `No stamp is queued either where the guarantee's history already read \`sealed\` and that verdict drew nothing, a \`sealed\` over a commit the branch does not hold among them: once per work item reads the history, and the work item's stamp is then the gap #976 carries.`, wrapped as the file wraps; `test_the_policy_names_what_enforces_the_drawing_and_what_nothing_does`'s `silence` tuple (1393-1399) gains `already read \`sealed\` and that verdict drew nothing`, seen red before the sentence lands. `changelog.md:17-20` under this directory: `and neither does a \`sealed\` whose \`Target SHA\` names a commit the branch does not hold; a later commit that corrects that row in place draws the stamp` becomes a clause saying such a `sealed` draws nothing and the work item draws no stamp afterwards, the gap #976 carries; in the same commit as the code (`docs/the-record-layout.md` §*A commit after the build brings its changelog fragment along*). No agent definition changes, so nothing is measured | The new case red at 96cd142b's module (its assertion `after_the_commit(other) == ""` failing on the fresh row), green after; the pin's new phrase red before the sentence, green after; the removed case absent (`grep -c does_not_count_as_stamped` of the module 0); `sealed_before`'s call in `_queue_one` made `if False:` turns the rebase case and round 3's case red, then restored; `bin/test tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/test_the_commit_gate_decides_at_the_commit.py tests/test_chain_check.py tests/test_the_sealer_guarantees.py tests/test_every_reader_ends_a_line_where_gfm_does.py tests/test_a_script_says_which_interpreter_it_needs.py tests/test_docs_line_wrap.py -q` green; `bin/test tests/test_no_real_identifiers.py tests/test_the_record_is_written_in_words.py tests/test_the_changelog_is_gathered_at_release.py tests/test_one_word_one_meaning.py tests/test_no_passage_is_pasted_into_a_second_file.py tests/test_release_hygiene.py -q` green; `bin/rules --check` exit 0; `uvx ruff check` and `uvx ruff format --check` of `seal_stamp.py` and the test module exit 0; `git grep -n -F -e 'over a commit then in its history' -e 'corrects that row in place' -- ':!seal/specs/*/rounds/' ':!seal/specs/*/overview.md'` printing nothing | b2f97fb1 |
| 7 | **The close, again.** `overview.md`: the round-3 row of §*Where spec and implementation diverged* says the condition as built (any earlier `sealed`, whatever it named; round 4's narrowing undone by the reframe, with `rounds/round-5.md` and Q8 as grounds; the amend limit kept), §*Fed back into the spec*'s first bullet says the same, and `## Not done` gains the accepted gap with Q7, Q8 and #976; `phases/phase-6.md` and `phases/phase-7.md` from `templates/sdd-phase.md`, phase 6's recording how the case was seen red and what the mutation showed; nothing in `questions.md` (Q8 is answered and no row is new) | `bin/unverified-check` on this item exit 0; `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.1 --root <worktree> --worktree` exit 0, the foot's `Reframed` line read against `routing.md`'s `Planning \| framer`; `bin/test tests/test_the_record_is_written_in_words.py tests/test_no_real_identifiers.py tests/test_a_phase_hands_the_next_one_a_record.py -q` green; `git grep -n -F 'over a commit then in its history' -- seal/specs/1792311781-the-stamp-is-drawn-from-the-sealers-verdict/overview.md` printing nothing | |

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

- **This item's own run draws no stamp.** The gate that runs here is the
  tree's copy (redirected by the installed 0.22.0 gate), so it prints `BROAD
  GATE PASSED` and writes no values file; the installed plugin's
  `post-commit` is 0.22.0's and queues nothing. The first stamp drawn from a
  `sealed` guarantee appears after the plugin is updated to 0.22.1, and the
  owner reads it on the first real run (§*The stamp*'s unchecked paragraph).
- **A clone whose git hooks slot is foreign** draws no stamp and prints no
  line; the pull request's check is what says the work was sealed.
- **A work item whose guarantee's history already read `sealed` draws no
  stamp afterwards**, in any clone, whatever that verdict named and whether
  or not it drew (the reframe after round 5). A `sealed` over a commit the
  branch does not hold, repaired at the next commit, is the case a person is
  most likely to meet; §*The stamp*'s unchecked paragraph says so and #976
  carries it. A rebase of a sealed branch in another clone, followed by a
  re-seal, draws nothing more — the case this reframe exists for.
- **A values file an older gate left pending** still draws: the hook's readers
  are unchanged, and `scale` is read as nothing since #853.
- **No hook is registered, no stub rewritten, no new dependency**: the second
  duty lives in `commitgate.post_commit` and `seal_stamp.py`, which the stubs
  already reach.
- **One paid evaluation**, about 3.4 USD (#969's reference side: 3.3898 USD
  for 10 runs), under the sealer's cases as they stand.
