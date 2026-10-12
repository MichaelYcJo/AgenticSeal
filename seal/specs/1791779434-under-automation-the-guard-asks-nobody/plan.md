# Implementation Plan: under automation, the guard asks nobody

<!-- seal/specs/1791779434-under-automation-the-guard-asks-nobody/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. Framed by `specseal:framer` on Fable 5.1 for #894. -->

Approved 2026-10-12 by the repository owner, when `smith` was spawned.

## Summary

Two stops reached the owner in a run routed `automation`. One was the
unrecognised-shape stop with no press readable on this machine; the other was
the dirty-tree row, which reads no press at all. The frame answers them
asymmetrically, on purpose.

- **The dirty-tree row** gets the shape every other stop already has under
  the press: a `deny` to the model whose reason names commit-first and
  stash, each as a command of its own, and no question tool (`spec.md` In 2).
  Code, in one block of `hooks/worktree-guard.py#main`.
- **The missing press** gets no new reader and no new evidence, because none
  exists that survives a machine move and that the model cannot forge
  (`spec.md` In 1). What changes is the procedure: a resumed run puts
  question 1 through `AskUserQuestion` again, so the fact is recorded where
  the existing reader reads it (In 3). Prose, in `orchestration.md`.

The design reads recorded facts and predicts nothing. The press reader
(`hooks/worktree_consent.py#automation_answered`) and the commit gate are
byte-identical to the base after this work.

## Technical context

- `hooks/worktree-guard.py#main`: the switch ladder. `automation_pressed`
  is called once, at the `stop_unrecognised` call, with
  `repo_paths(cwd)[0]` — the session's own root — `session_id` and
  `transcript_path`. The tracked-changes row is the `if entries:` block
  near the end of `main`; it builds `lead`, `listing`, `note` and responds
  `ask`. The deny goes there, after `entries` is known and before
  `respond`, reading the press the same way the stop does.
- `hooks/worktree-guard.py#automation_pressed`: the wrapper; every way of
  not reading the press is False. Unchanged.
- `hooks/worktree-guard.py#stop_unrecognised`: the model text for a deny
  under the press — *Re-issue the command in a plain spelling* — and the
  commit gate's `AUTOMATION_WAYS` in `hooks/commit-review-gate.py` are the
  two existing voices for "the ways on that need nobody". The new text
  follows their register: the ways on first, no question tool, *re-issuing
  unchanged meets the same refusal*.
- `hooks/worktree_consent.py#transcript_for`, `#automation_answered`: the
  reader, and the four conditions. Read, not touched. Its `PROJECTS_ROOT`
  is monkeypatched by `tests/conftest.py#_no_real_transcripts` to an empty
  directory in every case; `tests/test_the_guard_asks_once_per_session.py`'s
  `projects` fixture, `ask_entries` and `write_transcript` are how a case
  plants a press, and `tests/test_worktree_guard.py#pressed_root` reuses
  them.
- Tests that pin today's `ask` and must move or be seen red:
  `tests/test_the_guard_asks_once_per_session.py#test_the_plain_retry_meets_todays_rows`
  (S6 — asserts `ask` after the plain retry under the press),
  `tests/test_worktree_guard.py#test_switch_dirty_single_asks` (no press;
  stays), `#test_the_dirty_tree_row_names_what_was_measured` (no press;
  stays), `#test_the_token_does_not_answer_the_dirty_tree_question` (no
  press; stays). `seal/releases/0.20.0.md` row S6 cites the first at
  `@f3fe716e` and claims the `ask`; the ledger is frozen from `1790993141`,
  so the correction is a `Corrected ·` citing row in this item's fragment
  (`docs/the-evidence-ledger.md` §*A released row is read again in the
  branch's fragment*).
- Listed shapes, for S4: `git stash` and `git stash pop` are listed unless
  the word after `stash` is `branch`; `git commit` is listed. So each way on,
  issued alone, is silent in every tree (`docs/worktree-guard-spec.md` §A,
  *Which commands reach these rows*).
- `skills/implement/orchestration.md` §*Orchestrator: how the work is
  routed*: the home of question 1. The whole file is the orchestrator's and
  is kept out of every preloaded `skills:` list by
  `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py`.
  `skills/code-review/orchestration.md`'s *When the implementing session no
  longer exists — a new day, another machine* paragraph is where a resume is
  described, and it is where the link to In 3 goes.
- Language: `seal/config.md` has no `Record language` row, so the records
  are English; the guard's text is `tr(en, ko)` and both halves are pinned.
- Test runner: `bin/test <files>`; in a fresh worktree `uv run --frozen
  pytest` cannot start pytest (handoff of `1791384157`).

**The failure scenario of the chosen approach, six months out.** A run is
resumed on another machine, the resuming session forgets In 3's paragraph and
accepts the owner's typed "automation as before", and the first stop of the
run is an `ask` again — exactly #894. What this design buys is that the ask
is then correct (no press on this machine), the owner sees it once, and the
remedy is one click rather than a code change. What it does not buy is a
guard that knows the run is automated when the only record saying so is one
the model wrote. That is In 1's conclusion, written where a reader meets the
failure.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A. Read the press from the other main transcripts of this machine** (fall back from this session's file to the latest routing answer among `<PROJECTS_ROOT>/*/*.jsonl` whose `cwd` is this clone) | Two sessions in one clone cross-talk: the owner's interactive `per axis` for a hotfix in the main tree takes the automation run's press back, and the run's smith then asks the owner from a worktree; or the reverse, and an interactive session's switch is denied with text written for a model. Cost: 511 main transcripts on the owner's machine on 2026-10-03, each scanned at about 0.09 s per 17 MB, on every stop that reads the press. And it would not have changed #894: the earlier session was on another machine | **refused**; P2 lets the owner overturn it, with the own-transcript-first ordering named there |
| **B. A PostToolUse hook on `AskUserQuestion` writing a press record under the git common directory, keyed by clone** | The same locality as the transcript — a git directory does not travel to a new machine — plus A's cross-talk, keyed by clone rather than session; plus a shape nobody has measured, the PostToolUse `tool_response` of `AskUserQuestion`, which §13 refuses to build on unread. A new writer wired into `hooks/hooks.json` for a fact the transcript already holds | **refused** |
| **C. Read `routing.md`'s `Answer pressed` row as a fallback when no press is in the transcript** | §*Creation consent*'s own sentence: *a fallback the model can satisfy by writing a file is `[worktree-ok]`'s standing under another name*. It would make the measured run deny instead of ask, and it would make every run deny whose model wrote the row | **refused** |
| **D. Deny the dirty row whenever the command comes from a subagent** (the payload's `transcript_path` naming a `subagents/` file) | Predicts a harness shape — where a subagent's payload path points — that is measured only as the thing `transcript_for` falls back from, not as a rule; and attended, the person at the keyboard can answer a subagent's prompt, as the owner did | **refused** |
| **E. The dirty row becomes a choice site for everyone** — deny once per session per direction with an `AskUserQuestion` instruction naming carry / commit first / stash (#21) | Changes the attended prompt's shape and spends the switch direction's budget, which rows 1-b and 2 already draw on; under the press the first attempt's text would still name the question tool. A bigger change for a different issue | **out of scope**; #21 stays open and inherits In 2's words |
| **F. The dirty row under the press is a `deny` naming commit-first and stash, each as a command of its own; attended it stays `ask`** | A model that follows neither way on and re-issues the switch unchanged loops on the deny. The bound is the reason's text, as the commit gate's is (`docs/commit-review-gate-spec.md`, *whether it holds is a measurement owed at the next automation run*); M3 owes it | **chosen** (In 2) |
| **G. A resumed run puts question 1 through the tool again** | The resuming session does not read the paragraph. The ask that follows is then correct, and costs one click (the six-months scenario above) | **chosen** (In 3) |
| **H. Both `choose` rows deny every attempt under the press, naming the worktree split as the way that needs nobody** | What needs nobody at those rows is a product decision: the model deciding on its own that idle sessions are forgotten tabs is the judgment the row exists to hand a person. Not in #894's measurement | **out of scope**; P1 |

## Phases

Vertical slices — each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The dirty-tree row under the press is a `deny` to the model: `hooks/worktree-guard.py#main`'s `if entries:` block reads `automation_pressed` against the session's own root (W2) and answers `deny` with the ways on (W1's text, English and Korean), no question tool, and the re-issue sentence; the module docstring's row says so. Cases S1, S3, S5, S7 new and seen red at `c38f97d7`; S6's case rewritten and seen red; S2's assertion added; S4 run with real git in the fixture. M1 measured once, outside the suite | `bin/test tests/test_the_guard_asks_once_per_session.py tests/test_worktree_guard.py tests/test_worktree_guard_signals.py` green; the handover names how each new case was shown red; `git diff c38f97d7 -- hooks/commit-review-gate.py hooks/worktree_consent.py hooks/cmdline_base.py` empty (S8) | 8bdd6680 |
| 2 | The documents and the fragments: `docs/worktree-guard-spec.md` §A's tracked-changes row and *The stop has two readers* carry In 2 with `Enforced by:` lines; §*Known limits* carries In 1 and names a resumed run's press (M2's wording); `skills/implement/orchestration.md` gains In 3's paragraph and `skills/code-review/orchestration.md` the link; `seal/ledger/1791779434-….md` holds S1–S10's rows and the `Corrected ·` row for 0.20.0 S6; `changelog.md` says what a person sees differently | `bin/test tests/test_a_folded_statement_names_what_enforces_it.py tests/test_docs_line_wrap.py tests/test_a_section_marked_for_one_role_reaches_only_that_role.py` green; `bin/evidence-check seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` clean; the survivor sweep at the pull request | 4e733f57 |

Two phases, not three: the budget measurement at the next automation run (M3)
is a `questions.md` row for that run's orchestrator, not a phase of this
build, and nothing here waits on it.

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

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
**Re-read the column after any rebase**, or it names commits that resolve in
one clone and nowhere else. The evidence ledger has no such problem: a ledger
row names a symbol and a content hash, so there is no commit in it for a
rebase to orphan.

## Operational impact

- No migration, no new file under the git directory, no new environment
  variable, no change to `hooks/hooks.json`.
- **What a person sees differently.** In a session whose person pressed
  `automation`, a `git switch` over uncommitted tracked changes no longer
  opens a yes/no window; the model gets a refusal naming commit-first and
  stash. Attended sessions see today's prompt, unchanged.
- **What an orchestrating session does differently.** A run resumed in a new
  session or on another machine asks question 1 again through the tool, once,
  before the first spawn (In 3).
- **Compatibility.** The guard's installed copy runs from the plugin cache
  (`hooks/hooks.json` names `${CLAUDE_PLUGIN_ROOT}`), so this release's own
  run is still guarded by 0.20.0's hooks; the change protects the run after
  this one. Nothing here depends on another 0.21.0 item: the ten pull
  requests merged into `release/v0.21.0` so far left the dirty row and the
  press reader as they were (#881 moved `worktree_consent.place`, which this
  work does not touch).
