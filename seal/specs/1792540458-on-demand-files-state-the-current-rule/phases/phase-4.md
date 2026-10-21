# 1792540458-on-demand-files-state-the-current-rule — phase 4

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 4436e5c5 |


## What this phase was asked

`skills/code-review/orchestration.md` rewritten to the current rule. The
fix-pass section states the rule as it rules at b3154f43, because #945's
rules are not written here (`questions.md` Q2, default (b)). The redesign row
links the approval line's shape in `skills/implement/orchestration.md` *The
plan is approved at the spawn* rather than restating it. The step before the
preflight, which names the work item's `changelog.md`, names the party that
writes the fragment. Section signs of heading citations become the backticked
path and the heading in italics. Every imperative sentence whose actor or
condition the smith had to choose is listed here for the warden.

## What this phase found

**The frame holds for this phase, with one correction.** `spec.md` Scope 3
says the step names `changelog.md` "at the step where the orchestrator writes
it". The orchestrator does not write the fragment in the ordinary flow:
`docs/the-record-layout.md` *A commit after the build brings its changelog
fragment along* says "The build's last phase writes the fragment", and the
orchestrator writes it only for a commit of its own after the build (read).
Policy outranks the frame, so the step names the party that builds the work
item: the smith, or the orchestrator where `routing.md` answers
`Implementation` with `the session`. The docstring phase 3 wrote in
`tests/test_the_changelog_is_gathered_at_release.py` said the orchestrator,
and it is corrected in the same commit. The divergence is in `overview.md`.

**The file is read by the orchestrator alone**, and its opening paragraph
now says so, so its "you" has one reading. Where a sentence named another
party loosely ("the fix pass", "reviewer output", "Reviewer workers", "a
session", "the phase's"), it now names the smith or the warden. The pinned
sentences in "you" stayed in "you".

**The commit gate is not only a `PreToolUse` hook.** *Orchestrator: closing
the cycle* called it "this plugin's PreToolUse hook"; `hooks/gate.py`, which
git's hooks run, reads the `specseal-reviewed` mark too (read, `git grep`).
The sentence now names the gate's review arm and no mechanism.

**No heading changed but the title**, `# code-review — the orchestrator's
half` to `# code-review, the orchestrator's half`. `git grep` of the old title
outside `seal/`, `changelog/` and `docs/` finds nothing, and `docs/` cites it
nowhere (S14, executed), so no `## Rule changes` item is added. Every `##`
heading the act table in `skills/implement/orchestration.md` names is
unchanged, and `tests/test_every_orchestrator_act_names_its_delivery.py`
passes (executed).

**Section signs.** The file holds two, `contract §12` and `contract §2`, both
the contract's numbers (S8, executed `grep`).

**Census (S11): what left, and why it could go.**

| What left | Grounds |
|---|---|
| the opening's account of the five sections moved from `skills/code-review/SKILL.md`, and the headings keeping their prefix (#265) | history; the opening says who reads the file, and the prefix's reader is the act table, which the opening now links |
| *the rediscovery cost the handoff before round 1 exists to bound, paid again in full* | the sentence before it gives the reason: a fresh spawn holds none of what the fixes need |
| the measurement of 282 calls against 30 and 26 (#33, #29, the #57 chain) | measurement kept as anecdote; the rule and its reason stay |
| *The rule decides which to reach for while both options exist* | restated by the bold rule above it |
| *That half used to be retyped from memory every round and drifted*, with its round-2 instance | history; the rule that the prompt holds only the round's half stays |
| #107's account of an orchestrator breaking a rule it had put into every prompt | history; that the contract reaches the orchestrator only when opened stays |
| *That is not an occasional slip*, with the seven defects measured twice | measurement kept as anecdote; the reason, that the last round's fixes have no reader, stays |
| *it was considered and rejected* | history |
| the account of a pull request opened before round 1 (#943) | history; the rule that it opens after the sealer stays |
| `(#638)` and `(#975)` beside two bold rules | issue numbers the sentences stand without |
| *The 0.15.6 run relayed the log* | the reason stays in the present tense: a relayed log shows the person the stamp twice |
| *Filling the row in … is #401: it is what happened* | the reason stays in the present tense: the broad run then covers a command the person never saw |
| *nothing said it of the implementer's until 2026-09-05* | history; the link to *Orchestrator: verify before posting* stays |
| *(this plugin's PreToolUse hook)* | stale, above |
| the verify list's dashes and slashes | rule (a): each item is a sentence with its reason after `because` |
| `handback` | one spelling: `hand-back`, as the contract and the definitions write it |
| the blank header cell of the verifying-round table | `Property` |

**Cases rewritten with the sentences they pinned** (each seen red after the
commit by `mutation-check` on the new text, executed):

| Case | What changed |
|---|---|
| `tests/test_review_axes.py#test_the_fix_pass_resumes_the_implementer` | the measurement's assert retired; it holds the reason, *A fresh spawn holds none of it* |
| `tests/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py#test_the_review_orchestrator_stops_the_run_rather_than_filling_the_row_in` | `#401` replaced by the present-tense reason |
| `tests/test_the_stamp_reaches_the_person_it_is_drawn_for.py#test_the_orchestrator_is_told_the_stamp_is_drawn_for_it` | the bold rule without `(#975)`; the relay sentence with its reason |
| `tests/test_the_rules_have_one_owner.py`, rule 15's link and two cases | `FRAGMENT_LINK` carries the new citation form for this file while `skills/implement/SKILL.md` keeps the old one until phase 9; *once you have written the pull request body to a file*; *hand-back* |
| `tests/test_the_changelog_is_gathered_at_release.py#test_the_documents_send_a_change_to_its_own_fragment` | the docstring corrected, above, and it now holds the sentence naming the fragment's writer (new pin) |
| `tests/test_the_set_a_work_item_always_has.py#test_the_orchestrator_states_the_approval_line_where_it_spawns_the_build` | it also holds the redesign row's link to the approval line's shape (new pin) |

**Imperative sentences whose actor or condition the smith chose.**

| Sentence | What was chosen |
|---|---|
| *You obtain the fix pass for a round's findings by resuming the session that built the branch, and never spawn a fresh one while that session still exists* | the actor is the orchestrator, written "you" because the file has one reader; the condition is the session still existing |
| *the fresh spawn is the only option left, and you hand it the handoff* | the condition is the implementing session gone, on a new day or another machine |
| *An orchestrator in a new session holds no `automation` press until it puts question 1 through `AskUserQuestion` again* | the actor is named, and the citation is *Question 1*, where that rule now stands |
| *The smith's fix pass changes two lines per open finding* | the actor, which the old sentence left as "the fix pass" |
| *For each rule its range reworded or removed, the smith finds every other place stating it … and corrects each or names it in the hand-back* | the actor is the smith, as `agents/smith.md`'s fix-pass rule has it; the old sentence was impersonal |
| *You type only the half of a spawn prompt that changes between rounds* | the actor and the act; the old sentence said whose the other half is not |
| *You route the round on that sentence* | the actor; the old sentence was a bare imperative |
| framer row: *Where `routing.md` answers `Automation` with `yes`, the spawn asks nobody* | the condition is the routing row, spelled without the table pipe |
| redesign row: *you approve it when you spawn `smith` for it, with a second `Approved` line … in the shape … states* | the moment is the spawn, as the linked section has it |
| *You take them once you have written the pull request body to a file and the work item's `changelog.md` states what the work item ships* | the condition is the fragment stating what ships, not merely existing |
| *The party that builds the work item writes that fragment: the smith, or you where `routing.md` answers `Implementation` with `the session`* | the actor is the policy's, against Scope 3's wording |
| *An orchestrator that skips the preflight loses only time* | the actor, which was "a session" |
| *Never post the warden's output as it stands* | the party whose output it is |
| *The warden never writes this mark* | the party, which was "Reviewer workers" |
| *it is yours rather than the smith's* | the other party, which was "the phase's" |

**Restatement pairs of this file** (Scope 10, measured at 4436e5c5 with the
module's own `shared_counts`, executed): every pair of
`skills/code-review/orchestration.md` measures 0, against `BASELINE` entries
of 10 (`README.md`), 3 (`agents/sealer.md`), 14 (`agents/smith.md`), 5
(`skills/code-review/SKILL.md`), 22 (`skills/implement/SKILL.md`), 7
(`skills/implement/orchestration.md`), 5 (`skills/verify/SKILL.md`) and 20
(`templates/sdd-phase.md`). All are drained; phase 9 removes the entries.

**Bytes.** 21,958 at b3154f43, 21,063 at 4436e5c5 (executed `wc -c`).

**Found outside this phase's files.** The docstring of
`tests/test_waiver_decided_at_start.py#test_no_agent_definition_tells_an_agent_to_ask_a_person`
cites `skills/code-review/orchestration.md` *A fix pass adds the unit that
pins it*, a heading no file in the tree carries (executed `git grep`; its last
trace is `changelog/0.8.1.md`). The citation predates this item and was left
as it stands.
