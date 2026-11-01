# Implementation Plan: 1793516191-a-wording-pin-module-leaves-by-rule-changes

## Technical context

The work changes no file a release ships. Its output is this frame's `## Rule changes` (design Scope 1), which the settle after 0.27.1 writes into `docs/`, and the account of the module's 24 cases (design Scope 2). The build rehearses what that settle will meet (design Scope 4), and the orchestrator files the issue that carries the removal (design Scope 3).

What it builds on:

- `.github/scripts/rules.py:43-44`, its docstring: a pending `change` excuses nothing, so `tests/behaviour/test_one_word_one_meaning.py` stays until the settle writes the three `to` values (design G2).
- `skills/settle/scripts/rule_changes.py#parse` reads the block, and `chain-check` asks it at the pull request (design P3, executed).
- `skills/settle/SKILL.md` *The settling session's procedure* steps 2, 6 and 8: the settling session writes each `to` in its own words, runs each rule's `check:` targets, and then the broad gate. Step 8 is where #1216 found eleven pins and four copies. The rehearsal runs those readings here, before the release, so the settle should meet none.

The failure scenario of the chosen approach, six months on: the owner has not called a settle, so the three lines still name the module and the successor issue waits. Nothing is wrong in the tree meanwhile, because every sentence still states a fact that holds. The cost is an open issue in a release milestone, which `.github/scripts/release_completeness_check.py` names when that release is cut (`frame/questions.md` Q1). The other failure is a settle that writes a `to` in other words. The successor's precondition is that the three lines no longer name the module, whatever their words, and `seal rules --check` after the deletion shows it (design S5).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** The three `change` items now. Every place outside `docs/` and the module itself leave in one later change, carried by a successor issue. This pull request closes #1197 | The settle is late, and the successor waits in its milestone (Technical context) | **chosen**. Every sentence in the tree stays true at every commit, and the removal stays one change, as #1197's first *Done when* bullet asks |
| **A2** A1, but change the places outside `docs/` now: the writing-style line to `check: none reader: the proofer at review`, its pin, the shared-guard row, the two comments, the four docstrings and the `.test_durations` rows | Each one states a false fact between this merge and the removal: a rule line saying no test holds a rule the module still runs, a classification table missing a case that exists, and a comment at `hooks/lib/config.py:1414` no longer naming the module that excludes that unit by name. The settle is called by the owner and has no date, so that time has no bound. The `APPLIES_THE_SHARED_GUARD` row cannot go at all, since `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py` reads every scope that derives a path list from git, the module's case among them (read: its comment at lines 60-63) | rejected |
| **A3** Replace the structure: widen `.github/scripts/rules.py` to excuse a refused line that a pending `change` rewrites to drop the missing target, and remove the module in this pull request | The excuse would read the `from`, which `skills/settle/SKILL.md` *Rule changes* says is history and no precondition, so a stale `from` turns the excuse off and the refusal back on. Between this merge and the settle, three lines in `docs/` would name a file the tree does not hold, and a reader who opens one follows a dead path. It changes what a gate refuses, which carries `CONTRIBUTING.md` *What a change to a gate must carry*, and milestone 77 orders the opposite sequence (design G3). The premise that keeps the narrow excuse was checked against `rules.py`'s docstring, which states it: "so the test the line names stays until the settle". A line in `docs/` names a file the tree holds at every commit | rejected |
| **A4** Keep #1197 open: the pull request body names it without a closing keyword, and #1197 moves to the release whose settle applies the changes | It departs from `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* item 3. While #1197 sits in `release: 0.27.1` unclaimed, `release_completeness_check.py` refuses that release, so the move is a write on the owner's milestone made mid-release. No `merged: 0.27.1` label marks the rule changes as shipped (`docs/issues-and-milestones.md` *A label says a ticket is already in, before the release ships*) | rejected; A1's successor cites #1197's list and does not copy it |
| **A5** The settle's own pull request also removes the module and its references | `skills/settle/SKILL.md` *A settle is not a work item*: it opens no frame and no round, and its review is the owner's at its pull request. A refactor across a skill, two pins, two scripts' comments and four test modules would then reach `main` with no frame and no review round. The settle writes no changelog fragment, so the removal would have no line in any release note | rejected |
| **A6** Keep one narrow case for the renamed word: move case 24 into `tests/hooks/test_config.py` | It keeps the sweep #1167 decided goes (design G5): a case that refuses a token in every tracked file turns red where a text quotes the word for any reason. `skills/core/SKILL.md` *The rule a mechanism is kept against* says a reading guessed from words is reported, never used to block | rejected; the word's reader is the proofer, by the writing-style line (design *What each case held*, row 24) |
| **A7** Line 33: drop the module and add nothing | The line's other target, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, reads definitions and documents and runs no gate (read: its case names, lines 54 to 1007). The rule's behaviour, that the run's stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED` and draws nothing, would end on a line whose targets do not run it, though `tests/skills/test_broad_gate.py` does (design G8) | rejected; the line names `tests/skills/test_broad_gate.py` |
| **A8** Line 18: drop the module and keep the sentence | "A case holds other words for them out of the shipped text" is false once the module goes, and the settle writes the sentence as the latest decision states it (design G7) | rejected; the `to` names the proofer |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope 4, with the work item's `gaps.md` | design S2, S3, S4 and S5, run in one scratch clone under `<scratchpad>/1793516191-a-wording-pin-module-leaves-by-rule-changes/`, made with `git clone --no-local` and removed before the hand-back. S3's modules run in one command | 295f701a |

## Operational impact

None in this pull request: it adds the work item's records and nothing else (design S6).

At the settle after 0.27.1, three `check:` lines in `docs/` change and one sentence of `docs/the-pact.md` *The words* is rewritten. No deployer acts on either.

The orchestrator files the successor issue before `seal pr-body` runs, with the body design *The successor issue* lists and in the milestone `frame/questions.md` Q1 gives. The pull request body carries `Closes #1197` and names the successor's number (design S7).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
| 2026-11-01 | Phase 1's three points on the successor issue's text are folded by the orchestrator into design *The successor issue*: the six test lines named with their commit in place of "the four docstrings", the case-name and constant searches with the prose part named open, and the suite after the deletion handed to the successor's phase boundary. Q1 takes its default, `release: 0.27.2`, under the run's automation | The text is the body the orchestrator files, so each place the successor owes stands named in it, as #1147's direction asked of a source a later work item acts on. Automation routes no question to the owner during the run (`hooks/question-gate.py`) | `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source"; `frame/questions.md` Q1 |
