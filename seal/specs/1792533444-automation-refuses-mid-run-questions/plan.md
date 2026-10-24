# Implementation Plan: under automation, a mid-run question is refused

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-21 by the orchestrator, under the owner's `automation` answer, when `smith` was spawned for phases 1 and 2.

## Summary

A new `PreToolUse` gate, `hooks/question-gate.py`, runs in its own dispatch
group on `AskUserQuestion`. It reads the checked-out branch's declaration
through `hooks/routing.py#declared`, the same call the commit gate's
PreToolUse reading makes. Where that declaration reads `Automation` `yes`, the
gate denies every call except the routing question put alone, and that one
only until this session has answered it from this clone, and its reason
tells the session where the default goes instead. The two copies of the
routing-question test in `hooks/worktree_consent.py` become one predicate,
which the gate shares. The prose that said nothing can hold a run to the row
is rewritten in place to point at the gate, and the rule gets its one home in
`docs/the-review-record.md` §*The run*.

## Technical context

Existing code this builds on (`read` unless marked):

- `hooks/routing.py#declared`, `#for_branch`, `#item_dir`, `#current_branch`,
  `#parse`. `parse` already returns `automation` as `yes`, `no` or `None`.
  This is the only reader of the file.
- `hooks/gate.py#arms_missing` calls `routing.declared(cwd, top)`, with `top`
  from `optin.repo_root`. The new gate makes the identical call, which is
  what makes a linked worktree, local mode and a detached HEAD resolve the
  same way for both.
- `hooks/gate.py#declaration_hint` shows how a path is printed relative to
  the root, with the absolute fallback on Windows.
- `hooks/worktree_consent.py#leading_phrase`, `ROUTING_LABELS`,
  `#_routing_preset`, `#_routing_answer`. The label comparison appears inline
  in both of the last two. `tests/test_the_guard_asks_once_per_session.py`
  pins `wc.ROUTING_LABELS` against the orchestration table, so the predicate
  stays in this module.
- `hooks/review-skill-gate.py` is the shape of a small PreToolUse gate: its
  payload parse, `decide()`, and silence on anything unexpected.
  `tests/test_review_skill_gate.py` is the shape of its tests, driven through
  `conftest.run_hook` and `decision_of`.
- `hooks/dispatch.py#GROUPS` and `hooks/hooks.json`. `pre-skill` and
  `post-agent` are the precedents for a group with one gate.
- `README.md`'s gate table: one row per gate, with columns
  *Gate · Fires · Does · Where*.

**Failure scenario of the chosen approach, six months out.** A session runs
the orchestrator from the main checkout on a release branch, while the work
items live in linked worktrees. Its mid-run question passes, because the main
checkout's branch is declared nowhere. That is the stated limit. It is
acceptable because the flow this plugin runs is one issue under automation on
its own branch, switched to in place (the owner's 2026-10-19 direction, a
machine memory note, `read`). The limit sentence in the rule is what a later
reader finds.

A second scenario: the harness renames `AskUserQuestion`, or stops running
PreToolUse hooks for it. Then the gate goes inert and the run is back to
today's prose rule. Nothing breaks, and nothing says so. `questions.md` Q1 is
the measurement that would notice.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the prose rule alone (`skills/implement/SKILL.md` §1, plus a memory note) | Already failed: four questions in 0.22.3 with the section loaded (the issue). A rule nobody reads at the moment of the call does not hold | **replaced**. The premise that would keep it, that a loaded rule is obeyed, was checked against the 0.22.3 run and is false |
| **Gate on the branch's `routing.md` `Automation` row** (chosen) | An orchestrator whose checkout is not on the declared branch is not held. A model that edits the row to `no` escapes, in a diff the review reads | **chosen**. The row is the promise itself, for both the preset and `per axis` with box 1 checked. Reading it only to refuse means a forged row binds only its forger |
| Gate on the transcript press (`worktree_consent.automation_answered`) | `per axis` with box 1 checked writes `Automation` `yes` and leaves no press, so its questions pass. A resumed session has no press until question 1 is put again. The press is session-wide, so it would refuse questions on unrelated branches after the run ends | rejected. It reads consent, which must be harness-written. This needs the promise, which the row holds |
| Gate on the press OR the row | Covers the main-checkout orchestrator. But it is two sources for one fact, a transcript scan on every call, and a refusal that outlives the run for the whole session | rejected. The added case sits outside the normal flow, and the owner's direction is that such a case gets a limit sentence, not a mechanism |
| No exemption: refuse the routing question too | A resumed run cannot put question 1 again, so the worktree guard and the commit gate find no press and `ask` the person. That is #894's shape coming back, at more than one prompt per resume | rejected. The tree prescribes the re-ask (`skills/implement/orchestration.md` §*Question 1 — single-select*) |
| Exempt any call that *contains* the routing question | One call per resume would carry any other question past the gate | rejected. The question goes alone, and the resume sentence is rewritten to say so |
| Move `ROUTING_LABELS`, `leading_phrase` and the predicate into `hooks/routing.py` (replacing the structure) | `tests/test_the_guard_asks_once_per_session.py` reads `wc.ROUTING_LABELS` and `wc.PRESET`, so the move needs a re-export, a second name for one constant, or an edit to those cases. The press reader and the new gate would then both depend on `routing.py` for a fact about the question rather than the file | weighed as an equal and **not taken**. The premise for keeping: `worktree_consent.py` is where the routing question is recognised today, and that is checked by the pin above. Loading it costs the gate one import of `cmdline_base` on a call that is rare |
| Deny once per session, then pass | The first deny is spent, and every later question reaches the person. A subagent has no `AskUserQuestion`, so nothing else spends it, but the session itself retries | rejected. Under automation every stop is a deny, the inherited rule (`docs/commit-review-gate-spec.md`) |
| Fail closed on an unreadable declaration | An attended branch with a broken file would refuse every question, which is an outage `CONTRIBUTING.md` names, all for a promise nobody can read | rejected. The review arm already stops the next commit on that branch |

## Phases

Vertical slices. Each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The gate and its registration. `hooks/question-gate.py`; `worktree_consent.is_routing_question`, with `_routing_preset` and `_routing_answer` calling it; `GROUPS["pre-question"]`; the `hooks.json` entry; `tests/test_an_automation_run_puts_no_question.py` covering S1 to S13, each case seen red first | `tests/test_an_automation_run_puts_no_question.py`, `tests/test_the_guard_asks_once_per_session.py`, `tests/test_an_automation_run_meets_no_commit_prompt.py`, `tests/test_dispatch.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_a_script_says_which_interpreter_it_needs.py` | 30cf4f44 |
| 2 | The prose points to the gate. One sentence in `skills/implement/SKILL.md` §1. The audit-trail paragraph and the resume clause in `skills/implement/orchestration.md`, rewritten in place. The `AUTOMATION` comment and the `parse` docstring clause in `hooks/routing.py`. The `Automation` comment in `templates/sdd-routing.md`. The `README.md` gate row. The pin for S14 in the new module. The work item's changelog fragment (`docs/the-record-layout.md` §*A change writes fragments, never a shared file*) | the new module's S14 case, `tests/test_waiver_decided_at_start.py`, `tests/test_one_word_one_meaning.py`, `tests/test_routing_is_recorded.py` (the template still parses), and `git grep` for each sentence `## Removes` lists, empty | c93f76b0 |

## Operational impact

- No migration, env var or dependency.
- A new hook entry in `hooks/hooks.json`. It takes effect when a release
  carrying it is installed, not when this branch merges (hooks run from the
  plugin cache).
- Behaviour change for every repository that declares `Automation` `yes`:
  `AskUserQuestion` is refused on that branch for the rest of the work item's
  life. Once the release is installed that includes this branch, and so
  includes any later session that has checked out a declared branch.
- After the install, the orchestrator removes the machine-local memory note
  `automation-means-no-mid-run-questions.md`, which this gate replaces.
