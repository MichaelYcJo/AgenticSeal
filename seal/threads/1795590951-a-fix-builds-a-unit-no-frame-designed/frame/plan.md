# Implementation Plan: 1795590951-a-fix-builds-a-unit-no-frame-designed (#1614)

## Technical context

The tree as read at `d13c274e1`.

`skills/implement/fix-pass.md` holds five sections, *Read the round records first* (line 12), *A paste-ready fix is read before it is applied* (line 28), *The narrow set, then the read of the range* (line 44), *The close blocks, last* (line 52) and *The changelog fragment comes along* (line 79). *Scope* item 1's section goes between the second and the third, since the stop is a judgment of a finding's fix and comes before the narrow set runs. `skills/implement/fold-and-reframe.md` is one paragraph ending in `check: tests/text/test_the_rules_have_one_owner.py` (41 lines). `tests/text/test_the_rules_have_one_owner.py#test_the_framer_folds_a_decision_it_is_sent` reads that paragraph from its lead to its first `check:`, so *Scope* item 3's paragraph after the check line leaves the case's slice as it is.

`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* holds the paragraphs *Scope* item 2 edits: **A decision made after the frame is committed is folded** (line 61), **The framer writes a decision's fold** (line 70) and **One fold reaches every statement of the fact it changes.** (line 84), whose clause "is folded with the fact it" stands at line 97 and wraps onto line 98. `skills/implement/SKILL.md:107-109` holds *Scope* item 5's clause. `skills/code-review/orchestration.md:70` opens the paragraph *Scope* item 4 extends, and its route table's row 2 stands at line 223. `tests/text/test_the_rules_have_one_owner.py` defines `FIX_PASS_PROCEDURE`, `ORCH_IMPL`, `ORCH`, `FOLD` and `IMPLEMENT` already. Its `test_a_decision_after_the_frame_is_folded_into_it` and `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` pin facts of the sections *Scope* items 2 and 4 edit, and the edits remove none of them.

The failure scenario of the chosen approach, six months on. The stop rests on the crafter's reading of what a unit is. A crafter that reads a new helper as part of the named unit it serves builds it, and the defect the issue counts comes back unseen. A crafter that reads every helper as a unit hands back for folds that design one-line functions, and `frame/design.md` G11 counts how often an owlery `fixed` commit adds a declaration, so the folds come often there. Neither shows in a test. It shows in the round records the follow-up row of `frame/design.md` *Scope* item 8 reads: findings left open for a fold, and whether their units are followed by later findings less often than G11's.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| The order stated as text at the three steps that meet the act: the fix pass's stop in `skills/implement/fix-pass.md`, which the pass opens before it judges the first finding; the orchestrator's sort and the narrowing in `skills/implement/orchestration.md`; the fold's design in `skills/implement/fold-and-reframe.md` | The crafter's reading of a unit errs one way or the other, as *Technical context* says, and only the next release's round records show which | chosen (`frame/design.md` *Scope* items 1 to 5). The text is read at the call, the condition 0.38.8's hook was built to meet (G16), and a unit is a meaning question an agent answers (G1) |
| Keep the current order: the crafter builds the unit in the fix pass, and a fold writes down what it built | A fix that adds a unit is followed by a later finding on what it closed more often than one that adds none, in both repositories, by the counts of `frame/design.md` G11 and G12, and the fold's restatement was a finding twice in #1612 (G13) | rejected |
| Send a unit-needing finding down the framer's route: its close reads `deferred the frame`, the framer adds a phase row, and a fresh crafter builds the unit as a phase | A one-function unit costs a fresh spawn, a phase record and mutation runs, and the redesign restarts the count of finding rounds that bounds the run (`docs/running/the-run.md` *The run*). A `deferred` finding owes the next round nothing (G8), so the round after would not be held to name the finding the unit answers. The premise that keeps the fix pass building it, that the unit answers one finding and the next round reads it as that finding's fix, holds: a `fixed` finding must be named by the next record (`skills/code-review/scripts/chain_check.py`, read) | rejected |
| The orchestrator alone decides, from each finding's paste-ready fix, before the pass | The fix the crafter writes may need a unit the snippet does not show: a fix pass writes a fix in its own words where the snippet fails its reading (G5), as #1612's round 1 close of finding 3 did (G13) | rejected as the only holder. The orchestrator's sort stays as the step that saves a round trip where the snippet shows the unit |
| The crafter alone decides, with no sort before the pass | Each unit a snippet already shows costs a hand-back and a resume that the orchestrator could have saved by sending it with the round's other decisions | rejected |
| The proofer marks in the finding's block whether its fix needs a unit | A new line of the form, a mark `agents/framer.md` *A mark is not the answer to a blocked step* weighs, which has caught nothing. The proofer's snippet is a claim, and the fix pass judges its own fix | rejected |
| The crafter writes the unit's design down before it builds it, in the close block or `gaps.md` | One party designs and builds, which is the defect (`frame/design.md` G2) | rejected |
| Leave private helpers out of what a unit is | In owlery, commits whose only declarations are private helpers are followed about as often as the commits with public ones, by the count of `frame/design.md` G11 | rejected |
| The framer rereads the frame after every fix pass | A framer exchange in every round, whether or not a unit came | rejected |
| A `PreToolUse` or `PostToolUse` `command` hook on `Edit` and `Write`, matched to `agentic:crafter` by `agent_type`, that names in `additionalContext` a declaration an edit adds | Delivery inside a subagent is measured (`frame/design.md` G15). What the hook reads is a declaration grammar per language, a list of spellings that misses the Markdown rules this repository's procedures are made of and every language it does not list. It cannot tell a phase from a fix pass without finding the work item and its newest round record at each edit, the per-edit cost #1612's row on `git worktree list` rejected. It fires at each helper a phase builds to its frame. It reads whether a name was added and not whether the frame names the unit: `_widened`, which #1612's fold designed by what it does, is absent from that frame by name (G12) | rejected |
| A hook on `Write` of a path that does not exist, the one kind of unit a hook reads exactly | A fix that adds a file is rare in both repositories, by the counts of `frame/design.md` G11, so it would catch about nothing | rejected |
| A `SubagentStop` `command` hook on `^agentic:crafter$` that lists the declarations the range added and keeps the crafter working | It reads after the build, so the unit is built before anyone designs it, the defect itself. It reads the same grammar, and the reader is the writer | rejected |
| A `PreToolUse` hook on `SubagentHandback` whose `updatedInput` appends that list to the crafter's report | The same grammar and the same moment after the build. It rewrites another party's report, and it has not been probed | rejected |
| A `seal` subcommand that lists the declarations added since the round's `target:`, for the orchestrator before the next round | After the build, on the same grammar, and a second reader of what `git diff` already shows | rejected |
| A `prompt` or `agent` hook that judges at each crafter edit whether the edit adds a unit the frame does not name | A model call at every edit, with a 30 s or 60 s timeout, judging the frame from one call's input. The rows of `seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/plan.md` *Alternatives considered* on those types weigh the same cost | rejected |
| A fix-pass agent definition with `disallowedTools: Write` | It stops new files alone, which *A hook on `Write`* above counts, and a second crafter definition is preloaded by every spawn of it | rejected |
| A workflow under `workflows/` that runs the fix pass, the fold and the resumed pass in order | A second statement of the run's order beside `skills/implement/orchestration.md`, which #1612's and #1613's rows weighed and rejected | rejected |
| Keep the fold that rewrites a frame sentence with the fact HEAD gives after a fix | It is the restatement the issue counts, and #1612's `frame/plan.md:26` was a finding twice through it (`frame/design.md` G13) | rejected; the clause goes (`frame/design.md` `## Removes`) |
| A script that refuses a fold commit whose frame diff adds more lines than it removes | A count of lines is context and never a criterion (`skills/core/SKILL.md` *The rule a mechanism is kept against*), and a decision's fold adds sentences rightly | rejected |
| Send every statement a crafter's hand-back names in a frame file to the framer, in place of the orchestrator's fold | A framer exchange for each statement HEAD contradicts. The premise that keeps the orchestrator's fold, that it judges nothing of what the work is, holds once it only removes or narrows (*Scope* item 2), and the policy gives it exactly those statements (`frame/design.md` G9) | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 7 | `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/skills/test_passages.py`; each link of `RULES` keys `"32 "` and `"33 "` seen red with that carrier's new citation removed; `git grep -n -F 'is folded with the fact it' -- agents skills docs templates` and `git grep -n -F 'a fold rewrites it with the fact' -- agents skills docs templates` each print nothing. At `d13c274e1` they print `skills/implement/orchestration.md:97` and `skills/implement/SKILL.md:108`, which *Scope* items 2 and 5 rewrite (`frame/design.md` G23) | |

`frame/design.md` *Scope* item 8 is the orchestrator's records commit and no phase's.

## Overlap with the release

#1612 and #1613 merged at this branch's base, `6f4802fa8` and `8d99b99e2`, so neither has a merge order left. #1615 has no branch and no frame (`git branch -a`, executed at `d13c274e1`), so its row reads the issue's body (`gh issue view 1615 --json body`, executed on 2026-11-25), and a section it names is the issue's proposal read against the tree.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1615 | `skills/code-review/orchestration.md`: this item extends *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* and row 2 of the route table in *A regression is routed by comparing the fix with the frame*, inside *Orchestrator: the run ends with a verifying round*, where #1615 changes who reads a records-only fix. A narrowing fold of *Scope* item 2 is a records-only commit, so #1615's records-only reader reads the commits this item shapes, and its record-against-record axis reads the frame sentences those folds narrow | #1614 | `routing.md` orders #1615 after this item. This diff is the procedure text and the test module `frame/design.md` *Scope* items 1 to 6 name, and #1615's count of what the sealer withholds over a records-only defect then reads the folds as this item leaves them |

## Operational impact

No version move: `.claude-plugin/plugin.json` reads `0.39.0` (`frame/design.md` G22). No migration, environment variable or dependency.

A user's agents read the new order at their first fix pass or fold after the update, since each opens `skills/implement/fix-pass.md` or `skills/implement/fold-and-reframe.md` at that step. A fix pass in flight across the update follows the order it read.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
