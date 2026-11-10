# Implementation Plan: 1794289595-the-verifying-round-rule-has-four-owners

## Technical context

The tree as read at `0d73b6ed3`.

The work edits text in seven rule files, one test file and
`.claude-plugin/plugin.json`. The rule files are `skills/core/SKILL.md`,
`skills/code-review/SKILL.md`, `skills/code-review/orchestration.md`,
`skills/implement/orchestration.md`, `agents/proofer.md`,
`docs/running/the-run.md` and `docs/checks/the-pull-request-check.md`. No
line of a script changes.

**Where each part of the rule stands after the work.** `frame/design.md`
*Scope* states what each file keeps and loses. The owners are:

| Part | Owner | Who cites it |
|---|---|---|
| What a round writes to answer a closed finding: the three lines, a `regression:` line's reference and its grounds | `skills/code-review/SKILL.md` *Earlier rounds* | `agents/proofer.md`, `skills/code-review/orchestration.md`, `docs/running/the-run.md` |
| The bound of a verifying round: its target, the fix diff, new units | `agents/proofer.md` *Rules*, the rule **A verifying round answers the closed findings** | `skills/code-review/orchestration.md` |
| The orchestrator's judgment: when a round counts, the weighing at the third round, the signals, the stop row, the routes of a regression, the framer's route | `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* | `docs/running/the-run.md`, in one sentence |
| The policy: a run ends with a verifying round, three finding rounds by default from the last design change, what a regression is, the `Reframed` line, the homes, the judgment rows | `docs/running/the-run.md` *The run* | `skills/code-review/orchestration.md`, and the files outside the four that cite *The run* today |
| The records-only exception | `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the row *No fix that no round reads* | the sites of `frame/design.md` *Scope* item 5 |

Each part has one owner, and a citation goes from a file that needs a part
to the file that owns it. `the-run.md` and `proofer.md` cite `SKILL.md`.
`orchestration.md` cites `SKILL.md`, `proofer.md` and, for the policy,
`the-run.md`. `the-run.md` cites `orchestration.md` for the weighing.
`SKILL.md` cites none of the other three for a rule.

**Text that cases hold, which the build keeps word for word.** The list
comes from the probe of `frame/design.md` *Grounding* G8 and from reading
each case it named.

- `docs/running/the-run.md`: "three finding rounds by default" and "follow-up.md" (`tests/behaviour/test_chain_hooks_hardening.py` lines 1039 to 1052); the bold leads "A leftover finding goes where somebody will act on it, and the orchestrator writes why there." and "A regression is routed by comparing the fix with the frame." (`tests/text/test_the_rules_have_one_owner.py` lines 101 and 124); the sentence on the `Reframed` line, which `agents/framer.md` lines 287 to 288 and `skills/implement/SKILL.md` line 284 cite as owned by *The run*; and the three `check:` lines at lines 13, 16 and 42.
- `skills/code-review/orchestration.md`: "so it runs close to a finding round" (`tests/text/test_the_verifying_round_is_bounded_not_cheapest.py` line 34); the headings `## Orchestrator: the run ends with a verifying round` and `### A regression is routed by comparing the fix with the frame`; "as one row of `frame/plan.md` *Judgments of the run*" before that `###` heading; the table row that opens "the unit already had a regression", holding `frame/plan.md` *Judgments of the run*, and the line "The framer's route:" after it (`tests/text/test_the_rules_have_one_owner.py` lines 571 to 600); in the framer's route, "you append a close block to every open finding", "its `verdict:` reading `deferred the frame`", "its `answer:` naming the regression that sent the work item back" and "commit every such block in one commit" (lines 235 to 250); and `skills/core/SKILL.md` *The rule a mechanism is kept against* in the one-mechanism paragraph (`tests/behaviour/test_waiver_decided_at_start.py` line 649).
- `skills/code-review/SKILL.md`: the headings `## Earlier rounds` and `## The record`, and "Where you weigh an earlier finding, re-run its `evidence: executed` line rather than re-deriving the claim" (`tests/text/test_review_axes.py` lines 188 to 190); "where `reopens:` stands" (`tests/skills/test_chain_check.py` line 4730); and in *The record*, the bullet from "Each finding's section holds one finding block" to "The check refuses a finding whose block", naming each key of a finding block (lines 4686 to 4708).
- `agents/proofer.md`: "The reason is the round's job, not its price" and "instead of answering the finding that came back" (`tests/text/test_the_verifying_round_is_bounded_not_cheapest.py` lines 39 and 50); step 7 from "7. Write the record" to `## Never`, naming each key (`tests/skills/test_chain_check.py` lines 4686 to 4708); and `chain_check.py --baseline <base> --root <the branch worktree> --worktree` (`tests/text/test_a_moved_rule_leaves_its_definition.py` line 363).
- Every citation written as a backticked path and a section in italics has to name a heading or a bold lead of that file (`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `PATH_CITED` at line 112). `skills/code-review/SKILL.md` *Earlier rounds* is a heading, and `skills/core/SKILL.md` *Judgment is not licence to skip a party* is a bold lead that `orchestration.md` line 149 already cites.
- A passage of 15 words that stands in two rule documents fails `tests/text/test_no_passage_is_pasted_into_a_second_file.py`. A sentence that moves from `proofer.md` or `the-run.md` to `SKILL.md` leaves its source in the same commit.

**The case that changes.**
`tests/text/test_the_rules_have_one_owner.py#test_a_close_that_does_not_hold_reopens_it`
carries the marker `run-ends-with-verifying-round`, which
`docs/running/the-run.md` line 13 names. `tests/skills/test_chain_check.py`
carries the same marker at lines 1295, 1322, 4083, 4111, 4138 and 4166, so
the marker keeps a carrier whatever the case becomes.

**The failure scenario of the chosen approach.** In six months a fix adds a
sentence about a `regression:` line to `orchestration.md`, because the
orchestrator needed it once. The `RULES` row holds the owner's sentence and
the three links, and it does not see a new statement beside a link. The
proofer's read of the diff is what catches that, as it is today. The second
failure is the core's row: it now carries both conditions, so a change to
what the check passes in the last record has to change that cell, and a
person who edits `chain_check.py` and reads only
`docs/checks/the-pull-request-check.md` finds a citation there instead of
the condition.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| `the-run.md` cites `orchestration.md` once, for the orchestrator's weighing, as #1476 *Change* words it ("cites both"), and `orchestration.md` cites *The run* for the policy (chosen, folded from the orchestrator's reading of the frame, 2026-11-10) | A reader who takes #1476 *Done when* bullet 1 file by file finds the two files naming each other. A later edit could also grow the one sentence into a summary of the signals, which is a second statement again | chosen. Bullet 1 says "as the owner", and neither file names the other as the owner of a part it states itself (`frame/design.md` *Grounding* G6). A person who reads the policy paragraph on ending the rounds is told where the stopping is weighed |
| `the-run.md` names `orchestration.md` nowhere, and only the skill cites the policy | A person reading *The run* has no pointer to the signals and the routes, and #1476 *Change* is not carried out | rejected. This was the frame at `5b6734b52`; it met bullet 1 on a reading stricter than the bullet's words |
| `orchestration.md` stops citing `the-run.md` altogether | It still needs *The run* for the homes at lines 142, 163 and 168, for *The handoff* at line 22, and for the document a judgment row names, which the settle groups by (`frame/design.md` *Grounding* G10). Meeting that would move the homes table and the handoff into `orchestration.md`, which changes every citation of *The run* for them, `docs/releasing/issues-and-milestones.md` line 87 and the `RULES` row at `tests/text/test_the_rules_have_one_owner.py` line 101 among them | rejected |
| Keep the four statements and add a sentence to each naming one owner | Four texts still drift, which is what #161 and this issue report. The premise that would keep the structure, that each party needs the whole rule in its own file, does not hold: the proofer opens `SKILL.md` at step 1 and the orchestrator reads `orchestration.md` before round 1 (`frame/design.md` *Grounding* G2) | rejected |
| Define the three lines in `agents/proofer.md`, which is preloaded, and have `SKILL.md` cite it | Every proofer spawn pays for the definition whether its round is a first round, which writes none of the lines, or a verifying one. `SKILL.md` *Earlier rounds* is opened by every proofer at step 1 too, and a session that reviews without the agent reads `SKILL.md` and not the definition | rejected; #1476 *Change* names `SKILL.md` |
| Have `SKILL.md` cite `docs/forms/the-round-record.md` for the three relations, since the policy root already states them | The proofer opens one more document of 107 lines at every round to read one paragraph, and that paragraph holds neither what a `regression:` line's grounds hold nor that a build phase's unit takes no line | rejected. The form states what the check reads; *Earlier rounds* states what the proofer writes. `frame/design.md` *Grounding* G7 |
| The exception's text in `skills/code-review/orchestration.md`, with the core's row citing it | The core would send every agent to a file the proofer never opens for half of an invariant, and the row would be false without its second clause | rejected |
| The exception's text in `skills/code-review/orchestration.md`, with the core's row left as it reads | Two statements stand, the core's looser than the other: by the row, a finding located in code and closed by a commit that touched records alone owes no round, and the check refuses it (`frame/design.md` *Grounding* G4) | rejected |
| The exception's text in `docs/checks/the-pull-request-check.md`, which `the-run.md` line 8 cites today | The orchestrator would open a document written for a person who changes the check, to decide whether to spawn a round | rejected |
| The exception's text in the core's row, with the second condition added (chosen) | Every agent's preload grows by the words of one clause. A later change to the check's last-record arm has to change the core | chosen. The exception is part of an invariant every party already holds, `orchestration.md` lines 148 to 150 and `the-run.md` line 15 already cite that table, and the row becomes as exact as the check |
| Remove the copy notice: `rule_changes.py#copies`, the documents half of `chain_check.py#_read_tree`, `COPY_SAYS`, their cases and the paragraphs that describe them | The notice was added on 2026-11-02 for one settle where four `to` values copied a passage (`30ba21373`). Its record is eight days and the designs of four tags, in which it named nothing (`frame/design.md` *Grounding* G12). A copy in a later design would again meet `tests/text/test_no_passage_is_pasted_into_a_second_file.py` first at the settle, after the pull request that could answer it has merged. The removal is a change to what the check reads, in a work item whose review reads rule text | rejected for this work item. The record is too short to tell a notice that has nothing to catch from one that has not met its case yet, and the quotes *Scope* item 6 keeps are what a later count reads |
| Keep the copy notice (chosen) | The check reads every rule document on each run of a design that states operations, and step 7 of the proofer's definition keeps one clause for a notice that has caught nothing so far | chosen, with a reader named for its record: the issue *Operational impact* words, which gives the command, the count that decides and the tag it is read at |
| Write the re-reading of the copy notice's catches as a row of `seal/follow-up.md`, or as an `add` in `frame/design.md` *Rule changes* (the orchestrator's reading of the frame, 2026-11-10) | `seal/follow-up.md` lines 5 to 7 keep that file for a repository with no tracker, and its lines 9 to 13 refuse a row whose answerer comes with a condition, which "at the settle after 0.38.0" is. This work item edits the policy root directly, so its *Rule changes* holds the no-change block, and a dated one-off reading is no rule of the policy | rejected as the home, agreed as the need. The home is an issue in the tracker, which names its answerer and its milestone |
| Remove the sentence on quoting a notice from `agents/proofer.md` | A finding taken from a notice no longer names it, and the count #1476 made of the pin notice, six round records, could not be made again. The core keeps a mechanism by its record of what it caught, and this is the only place that record is written | rejected |
| Give the quote a reader at the settle: the dry run counts the notices the round records quote | A new reading in `skills/settle/scripts/`, with its cases, for a count one `git grep` gives | rejected. `agents/framer.md` *A mark is not the answer to a blocked step* asks what a new mechanism takes out, and this one would take out nothing |
| Keep `test_a_close_that_does_not_hold_reopens_it` as it reads | It fails as soon as three of the four files stop naming `confirms:` and `regression:`, which *Scope* items 2 to 4 require | rejected; the case holds the old structure |
| Remove the case and add nothing | A later edit could name two of the lines in a sentence and leave out the third, the defect the case was written for (S9 and S26 of work item 1791933022), and nothing would hold `SKILL.md` as the owner | rejected. The case keeps its conditional half, and `RULES` holds the owner and its links |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 4, and of item 7 the changed case and the `RULES` row for the three lines. Each statement of the exception that item 5 lists stays as it reads until phase 2 | The narrow run of `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_the_verifying_round_is_bounded_not_cheapest.py`, `tests/text/test_review_axes.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_chain_hooks_hardening.py`, `tests/behaviour/test_waiver_decided_at_start.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/skills/test_chain_check.py`; the changed case seen red with the defining sentence taken out of *Earlier rounds*, and the `RULES` row seen red with one link taken out; the greps of scenarios S1, S2, S4 and S5 | e15ed537d |
| 2 | `frame/design.md` *Scope* items 5, 6 and 8, and of item 7 the `RULES` row for the exception | The narrow run of `tests/text/test_the_rules_have_one_owner.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_ci_gives_the_checks_what_they_need.py` and `tests/lib/test_core.py`; the `RULES` row seen red with the second condition taken out of the core's cell; the greps of scenarios S3, S6 and S7 | 54ebe2e74 |

## Overlap with the release

The spawn names three other items of 0.37.2. This work meets each of them in
a file. Read: #1477, #1478 and #1479 with
`gh issue view` (executed, 2026-11-10; none has a comment). #1477's frame
is committed on its branch at `9d4270617` and was read there (executed,
`git log`; its `frame/plan.md` *Overlap with the release* and
`frame/questions.md` Q1, read); #1478 and #1479 have no branch (spawn
prompt).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1477 | `skills/implement/orchestration.md`. This work changes one row of the table in *Orchestrator: drain the rows before the broad run, and keep the records* (line 648), which #1477's frame leaves. #1477 rewrites the fold paragraph at lines 55 to 128 and moves the routing question and the merge-order paragraph out. Lines 55 to 128 hold no statement of the exception and do not name a verifying round (executed, `sed -n '55,128p' \| grep -n -i`). This work does not change lines 485 to 489, the sentence on a late version move's verifying round that #1477 moves to `skills/implement/merge-order.md`: it states that a change after the last round owes a round, and not the exception, so #1477's `frame/questions.md` Q1 is answered "unchanged". `tests/text/test_the_rules_have_one_owner.py`: this work changes `RULES` and the case at lines 541 to 565, and #1477 rewrites the fold case | #1476 | This work's change to the shared file is one row, it carries the release's version move, and #1477's frame names the same order. #1477 merges the release branch afterwards, inside rounds it spends anyway, and the two changes stand in different sections of both files. A sentence #1477 writes about a fix that owes no verifying round cites the core's row and restates no condition (*Scope* item 5) |
| #1478 | `skills/code-review/orchestration.md` and `agents/proofer.md`. This work rewrites *Orchestrator: the run ends with a verifying round*, the sealer's repair at lines 496 to 505, a sentence of the paragraph **On the broad run's exit 1 spawn nothing** inside *Orchestrator: the pull request opens once the sealer seals*, step 7's notice sentence and the rule **A verifying round answers the closed findings**. #1478 rewrites what `pr.md` holds at lines 402 to 451 and the proofer's read of `pr.md`. The *Target* row this work writes cites two of the proofer's rules by their opening words, **A verifying round answers the closed findings** and **Every round reads the work item's records that state the present**, either of which #1478 may reword | #1476 | #1478's issue says it builds after #1476, and its branch is not cut. Cut from the release branch after this merge, it starts from the rewritten sections, and the citation census names the *Target* row's citation if #1478 rewords that lead |
| #1479 | `skills/implement/orchestration.md`, lines 166 to 171 against this work's line 648. `skills/verify/orchestration.md` line 22 cites *The run* for "three finding rounds by default", which stays word for word | #1476 | #1479 builds after #1477, which merges after this work. The two changes stand in different sections of the file |

## Operational impact

No migration, environment variable, dependency or compatibility break.

**This pull request moves the version.** It is the first pull request into
`release/v0.37.2`, and the orchestrator assigned the move to this work item.
Phase 2's crafter moves `.claude-plugin/plugin.json` from `0.37.1` to
`0.37.2` in the commit that adds `changelog.md`
(`docs/releasing/branch-and-release.md` lines 30 to 40).

`skills/core/SKILL.md` is read in every repository that installs the
plugin. After the release, the row *No fix that no round reads* states both
conditions of the exception, and no behaviour of the check changes.

**The copy notice's record is read again, by an issue the orchestrator
files.** An agent posts nothing (contract rule 6), so no phase writes it.
Before the pull request opens, the orchestrator files one issue, assigned to the repository's owner, in
the milestone it judges holds work read once `v0.38.0` is tagged, and names
its number in `pr.md`. The issue holds:

- The command, run at the `v0.38.0` tag:
  `git grep -l -F 'repeats a passage of' v0.38.0 -- 'seal/threads/*/trail/rounds/*'`,
  and the same at each tag from `v0.34.0` on, since a settle removes a
  released work item's records.
- What decides. One round record or more that quotes the notice on a
  finding closed `fixed`: the notice stays and the issue closes. None,
  across tags that hold at least one `frame/design.md` stating an `add` or
  a `change`: the issue becomes the removal of `rule_changes.py#copies`,
  the documents half of `chain_check.py#_read_tree`, `COPY_SAYS`, their
  cases and the clause in step 7 of `agents/proofer.md`. None, and no such
  design since `v0.37.0`: the reading moves one release on.
- The record so far, `frame/design.md` *Grounding* G12.

A proofer or an orchestrator spawned in this repository before the release
receives the installed plugin's copy of the core and of its definition, the
0.37.1 text. The rounds of this work item are run under that text.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-10 | The title takes `refactor:` | The diff moves statements of one rule to one owner each, adds to the core's row a condition the check already held, and changes no line of a script; no rule's meaning changes (`frame/design.md` *Rule changes*) | `~/.claude/skills/commit-pr-convention/SKILL.md` |
| 2026-11-10 | The copy notice's record is read again in #1506, assigned to the owner, in the milestone `backlog: review chain & agents` | `frame/plan.md` *Operational impact* asks the orchestrator to file the issue before the pull request opens and name its number in `pr.md`; that milestone holds the check's other open items | `frame/plan.md` *Operational impact*; `skills/verify/SKILL.md` *The answerer has to exist* |
| 2026-11-10 | Round 1 findings 1 and 3 are folded into the frame by the framer before the fix pass. Finding 1: *Scope* item 1's "exactly one line" leaves no line for a fix that holds for its own finding and breaks its unit; the definition drops "exactly" and says a `confirms:` line stands beside the `regression:` line in that case. Finding 3: *Technical context* counts six rule files where the diff edits seven. Finding 2 (`changelog.md`) goes to the fix pass. | `trail/rounds/round-1.md` findings 1 to 3 (proofer). The base text, `df775c52c` `agents/proofer.md:136-141`, said "is named this round" with no "exactly", and `docs/forms/the-round-record.md:64-74` gives the relations side by side (read by the orchestrator) | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the fold paragraph |
| 2026-11-10 | The fix pass is a fresh crafter on Opus, not a resume of the phase 2 implementer | The owner asked on 2026-11-10 that only the framer of this item run on Fable and every later agent on Opus (milestone `release: 0.37.2`, *Model*); the implementer ran on Fable, and a resume keeps its model | `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* |
