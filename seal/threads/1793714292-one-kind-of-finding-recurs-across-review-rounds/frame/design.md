# Design: one kind of finding recurs across review rounds (#1020)

## Grounding

Each row is labelled `read` where the framer opened the text, and `executed` where a command printed the fact.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A check or an exchange stays only while its record of what it caught outweighs what it costs. So each candidate is weighed by what it would have caught on the recorded chains (G8 to G10), against its cost (G11). |
| G2 `skills/core/SKILL.md` *Judgment is spent where meaning is the question* (read) | Whether two findings are one kind of defect is a question of meaning. A script that decides it from a shared `location:` file, or from a `regression:` line, re-encodes that judgment as a grammar rule, and the core rules that out. A reading guessed from words may be reported and never used to block. |
| G3 `docs/running/the-run.md` *The run* (read) | The tree already holds three of the issue's candidates. The cap counts finding rounds from the last design change, and a verifying round that opens a finding counts toward it (candidate 3). A second regression on one unit after a fix-pass route goes to the framer (candidate 2's framer route). Every decision to go on at or past the third finding round is a row of `frame/plan.md` *Judgments of the run*. |
| G4 `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* (read) | The home of what a recurrence owes. Its signals row names "one kind of finding returns with a new instance, each fix pass having fixed the coordinate it was handed". Its paragraph opening **Where the signal is one mechanism whose edges each fix pass chased** has the next fix pass decide what the mechanism reads, and states what the judgment rows of seven work items of 0.27.x to 0.29.0 showed about that signal. |
| G5 `skills/agent-contract/SKILL.md` rule 12, and `agents/crafter.md` *A fix pass appends close blocks and writes no phase record* (read) | Every fix owes the class, recurring or not, and names its method. This is the duty the issue's `class:` line would have tagged. #1318 rewrites both texts in this release. |
| G6 `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A problem that recurs within a run gets a prevention home at once** (read) | A problem seen a second time in one run already gets a home from the orchestrator before the next spawn. |
| G7 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read); the four unsettled designs' `## Rule changes` (executed: `sed -n '/^## Rule changes/,/^## Removes/p'` over each, each printing `- nothing`) | This work changes no code. Its only shipped edits are sentences of two policy-root documents, so its subject is the policy root's text, and it edits `docs/` directly. The policy in force is `docs/` at HEAD, and no unsettled design names a section this work edits. |
| G8 #1038's record, `git show 569780eff:seal/threads/1793521558-the-record-decides-each-proposed-verifier/trail/phases/phase-2.md`, *The decisions* row C11 and *Instances C11* (read) | For the 17 work items merged after PR #1191 through #1244 there were 111 findings, 30 of them recurring, 20 of those reaching shipped text. Four chains had three or more findings: #1201, #1203, #1230 and #1241. In three of them, the judgment rows took the structural question. #1201's plan holds no *Judgments of the run* section. |
| G9 #947's record, `git show 783a7fe8a:seal/threads/1793528484-the-process-measured-on-0-27-2/trail/phases/phase-3.md`, *The measures* (read) | #1201 merged before `96c11614`, the commit that brought the current *The run* paragraph, so none of G8's four chains ran under that paragraph without a row. #1223's chain of three had its row at the third finding round, and round 4 found nothing. The framer confirmed the ancestry fact (executed: `git log -1 --format=%cI 96c11614` printed `2026-10-31T16:16:17+09:00`, and `git merge-base --is-ancestor 96c11614 HEAD` exited 0). |
| G10 The framer's probe over the 34 work-item pull requests merged after 2026-11-01T09:19:59Z through #1322, with settles and release merges left out (executed: `gh pr list --state merged --search "merged:>2026-11-01T09:19:59Z"`, then a script that fetched each `pull/<n>/head` in a `--no-local` clone and parsed each round's `regression:`, `reopens:` and `location:` lines in the way G8's *Command C11* does) | There were 114 findings, 32 of them recurring, 13 in the records alone and 19 reaching shipped text. Five chains had three or more findings: #1252 (#1223), #1276 (#1263), #1284 (#1054), #1287 (#1216) and #1320 (#1313). Each of those plans holds a judgment row at or before the chain's third finding. One run did not converge, #1287's ten rounds. Its rounds 5 to 10 were spent on one helper test's parameters, comment and name, and carry no `reopens:` line. Its causes are #1288's (a stop that later rows overrode) and #1286's (a paste-ready text applied as given). |
| G11 #1020's comment of 2026-10-29 (read) | The 0.24.0 build of the issue's design (a `class:` line, a `recurrence` refusal in `chain_check.py`, a framer route and a cap change) added 808 lines outside `seal/`. Its round 1 opened five findings, mostly about the design's own restatements, and the owner stopped it. "A check for recurrence stays only if what is left after the structure change still shows the loop." |
| G12 #97's three remaining levers, read against the tree (read: `docs/running/what-a-script-gates.md`, the row for the cases under `tests/text/` and `tests/behaviour/`; `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*; contract rules 14 and 15; `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#_round_record_fields`) | *Gate the pin on what breaks* is in the tree: "a case pins a fact a reader acts on; one that pins wording goes", and "A rule no case can hold carries no check line, and review reads it". *A pin must derive, or not exist* is in the tree: the core's "Nothing is kept beside the tree to stay in step with it", and #97's own instance, `ROUND_RECORD_FIELDS`, is now read from the template and the checker's fields. *Defer the pin to its own ticket* is decided against by the tree: a case comes first and is seen red, and a fix that changes what a person sees pins it in the same commit. |
| G13 `seal/follow-up.md` (read) | No row there waits on this work. |

## Scope

In. Each item is a sentence of `docs/` that the decision makes untrue or that states a fact twice:

1. `docs/releasing/release-checklist.md` *2b. Settle what earlier releases left behind*, the flow-baseline step. The sentence "#1020's check is then the next step, and #1020 is the issue that follows, so the session files no other." goes, because this work builds no such check. In its place, the settling session files one issue that names each stale copy that kept the count up, the record it stood in, and the file the lesson belongs in. An issue naming that file is where `skills/implement/orchestration.md` *Orchestrator: where a decision or a lesson is written* writes a lesson whose home no work item in progress changes.
2. `docs/running/the-run.md` *The run*, the paragraph opening **The orchestrator ends the rounds when they stop paying**. Its sentence "A round that opens nothing needing a fix is the loop having converged and counts toward nothing." goes, because the section's first paragraph states the same fact with its reason.
3. The same paragraph's sentence on a regression's fix pass cites "the invariant Table B of the core". The core names no table B. The citation becomes `skills/core/SKILL.md` *Judgment is not licence to skip a party*, the section whose table holds that invariant.

Decided, and nothing is built for it:

4. No recurrence check, no `class:` line and no refusal in `chain_check.py` (G1, G2, G8 to G11; `frame/plan.md` *Alternatives considered*).
5. No mediated exchange at a finding's first `reopens:` (the same grounds and the same table).
6. The issue's candidate 3 (a verifying round that opens a finding counts toward the cap) and the framer route on a second regression are in the tree already (G3). Candidate 4 (the orchestrator runs the check before a fix pass) has no check to run.
7. The issue's *Done when*. The first bullet, fixture records seen red under a check, falls with item 4. For the second bullet, what a recurrence owes stands once: per fix in contract rule 12 (G5), and per run in G4's section, whose rows are the record. For the third bullet, *The run* states the cap once after item 2, and cites G4's section for the signals.
8. #97. This work absorbs *Gate the pin on what breaks* and *A pin must derive, or not exist*, which the tree already answers (G12). It leaves *Defer the pin to its own ticket*, which the tree decided against (G12), so #97 stays open and the pull request body carries no `Closes #97`. The shape #97 measured, a fix's new test producing the next round's finding, recurs in #1287's rounds 5 to 10 (G10), and #1288's third *Done when* bullet owns it.

Out:

- `skills/code-review/orchestration.md`. #1288 rewrites its stop judgment in this release, and #1318 rewrites its fold rule. Its restatements of *The run*, such as the regression route's table, are left for them to meet as 0.30.1 left them.
- `agents/crafter.md` and contract rule 12. #1286 and #1318 edit both.
- `README.md`. #1102's body expects "0.29.0's recurrence check in the review chain (#1020)", and the rewrite describes the tree as it stands, which holds none.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The settle has no check to wait for | Given the tree after this work, when a settling session reads the flow-baseline step and finds the count `worse`, then the step names one issue to file and names no check of #1020's | `git grep -n '#1020' -- docs skills agents templates` prints nothing; the step's new sentence is read at its line |
| S2 *The run* states the zero-finding round once | Given `docs/running/the-run.md` after this work, when the orchestrator reads *The run*, then the fact that a round opening nothing needing a fix counts toward nothing stands in the first paragraph alone | `grep -c 'loop having converged' docs/running/the-run.md` prints `1` |
| S3 The cap paragraph's citation opens | Given the regression sentence of *The run*, when a reader follows its citation, then it names a heading `skills/core/SKILL.md` holds | `git grep -n 'Table B' -- docs` prints nothing, and `grep -n '^\*\*Judgment is not licence to skip a party' skills/core/SKILL.md` prints one line |
| S4 No mechanism is added | Given the branch's diff, when it is listed outside `seal/`, then it holds the two documents of *Scope* items 1 to 3 and nothing else | `git diff --stat <base>...HEAD -- ':!seal/'` |
| S5 The cases that read the two documents still hold | Given the edits, when the narrow cases that read either document run, then they pass | the crafter's narrow run of `git grep -l -e 'the-run.md' -e 'release-checklist.md' -- tests`, `tests/github/test_finding_counts.py` and `tests/behaviour/test_chain_hooks_hardening.py` among them |

## Data & interfaces

No script, form, field, template or hook changes.

## Rule changes

- nothing
  why: This work item's subject is the policy root's text. It changes no code, and it edits the three sentences of *Scope* items 1 to 3 in `docs/` directly in its pull request under `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, so the settle has no decision to gather (G7).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the sentence naming #1020's check as the flow-baseline step's next step | `docs/releasing/release-checklist.md` *2b. Settle what earlier releases left behind* | the issue-filing sentence of *Scope* item 1 replaces it; this work builds no check |
| the second statement that a round opening nothing counts toward nothing | `docs/running/the-run.md` *The run*, the paragraph opening **The orchestrator ends the rounds when they stop paying** | the first paragraph of the same section holds the fact and its reason |
| the citation of a "Table B" of the core | `docs/running/the-run.md` *The run*, the same paragraph | `skills/core/SKILL.md` *Judgment is not licence to skip a party*, which *Scope* item 3 cites in its place |

This work adds no gate, check, hook, CI step, rule, line grammar, label or mark, so it owes no removal in return for one.

Framed 2026-11-03 by framer, before the build.
