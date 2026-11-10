# Design: 1794289596-implement-orchestration-grew-back

## Grounding

The tree as read at `9e9d1087f`. Every line number of `skills/implement/orchestration.md` in this file and in `frame/plan.md` is a line of that commit.

| Policy clause | What it fixes for this work |
|---|---|
| G1 `skills/core/SKILL.md` *A document is cut by who opens it and at which step* (read) | A party pays for every byte of each file it opens. A passage the orchestrator needs only on one condition belongs in a file opened on that condition, and the file every run opens names each such file with the step that opens it. |
| G2 `skills/core/SKILL.md` *A rule is guidance for a judgment, not a sequence to execute* (read) | The fold rule is written as what the orchestrator weighs, one judgment to a paragraph, where it now reads as one sequence of acts. |
| G3 `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A fact has one source. Less text means nothing said twice. History goes to git. Nothing is kept beside the tree to stay in step with it, such as a stored count, so this work adds no check on the file's size. |
| G4 `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | This work's subject is a shipped skill's text and not the policy root, so the one policy sentence it makes stale is an operation in `## Rule changes`, and every file outside the policy root is edited in the pull request. |
| G5 size of `skills/implement/orchestration.md` (executed, `git show <tag>:skills/implement/orchestration.md \| wc -w`, and `wc -w` on the worktree) | 7,835 words at `v0.24.0`, 5,242 at `v0.30.0`, 7,311 at `9e9d1087f`. `git diff --stat ba4d85629 HEAD -- skills/implement/orchestration.md` prints nothing, so the issue's line numbers hold at `9e9d1087f`. The issue's "about 5,200 words" is 5,242. |
| G6 where the growth since `v0.30.0` stands (executed, one `awk` word count per heading at both commits) | *Orchestrator: the order inside a ticket* grew from 560 to 1,324 words, almost all of it the fold paragraph at `:55-128` (872 words). *Under agentic* is new, 821 words. The batch section grew from 577 to 770, the language-key paragraph at `:205-223` being 216 words. *What the answer writes* grew from 1,406 to 1,628. |
| G7 issue #1477 (executed, `gh issue view 1477 --json comments --jq '.comments\|length'` on 2026-11-10) | The issue has no comments. The body is the request whole. |
| G8 the 0.37.0 records the issue cites (executed, `git show v0.37.0:seal/threads/<item>/trail/rounds/round-N.md` and `git show 5656e5239:seal/threads/1794200907-agents-write-commands-the-parser-reads/guarantee.md`) | Each finding names a frame sentence that a fold left stating the old fact while another sentence of the same frame stated the new one. `1794200905` round 1 finding 3: an *Alternatives considered* row and a *Scope* bullet. `1794200906` round 2 finding 1: an *Alternatives considered* row. `1794200907` round 1 finding 5: a *Technical context* sentence and an *Alternatives considered* row. `1794200907` round 3 finding 1: a *Removes* reason and a *Judgments of the run* row. `1794201840` round 2 finding 1: the conclusion of a *Grounding* row. The withheld guarantee: "line 63 is the old statement the fold left beside its correction". The *Grounding* and *Technical context* sentences said what the work does, not what the tree held at the dated commit. |
| G9 the fold paragraph's clauses and where each came from (read: `:55-128`, the comments of `tests/text/test_the_rules_have_one_owner.py:374-455`, and issues #1368, #1401 and #1442 through `gh issue view`) | *Data & interfaces* D1 lists the clauses. #1401's lesson is the framer's count rule in `agents/framer.md` and added no clause of the orchestrator's that D1 does not already list. |
| G10 what a rewrite of the fold rule that keeps every clause weighs (executed, `wc -w` on a throwaway draft under the scratchpad, written to D1 and removed) | 829 words, against 872 now. The clauses are the weight, and the form is not. Rewriting the paragraph therefore frees almost none of the words G5 asks for: *Data & interfaces* D3 gives the arithmetic, and *Scope* items 1, 2, 5 and 6 find them. |
| G23 how often a frame is folded after its commit (executed, `git log --all --format='%h %s' -- 'seal/threads/<id>*/frame/design.md' 'seal/threads/<id>*/frame/plan.md'` for each of the last eight work items, the four of 0.37.0 and the four of 0.37.1; the orchestrator's count of their *Judgments of the run* rows, 3, 1, 3, 1 and 1, 1, 1, 3, re-run with one `awk` and matched) | Seven of the eight have at least one commit that folds the frame after the commit that framed it; `1794271936` alone has none. At least six of the seven hold a fold of a decision, such as an owner's request, a round finding located in a frame file, a prevention home or a merge order, and not only a statement a crafter named. A fold is the common case of a run, so every clause of the fold rule stays in the body every run reads (G1), and no file is cut for it. |
| G11 every citation of a section of `skills/implement/orchestration.md` (executed, a probe that flattens each tracked text file outside `seal/threads/` and reads each backticked path followed by italics) | Cited from outside the file: *Orchestrator: the order inside a ticket*, *The frame is read against the issue at the spawn*, *Orchestrator: what needs a person is asked in one batch, before the first edit*, *Orchestrator: how the work is routed*, *Question 1*, *What the answer writes*, *Under agentic*, *Orchestrator: when a work item is required*, *Orchestrator: drain the rows before the broad run, and keep the records* and *Orchestrator: where a decision or a lesson is written*. Only *Question 1* leaves the file. Its one citation is `docs/running/the-review-and-parity-arms.md:56`. |
| G12 the citations whose heading stays and whose sentence this work makes inexact (read) | `README.md:154-157` and `README.ko.md:156` say *Orchestrator: how the work is routed* gives each answer. `skills/implement/multi-repository.md:9-10` says that section states the question's shape. `skills/commit-pr-convention/SKILL.md:86-89` cites the batch section for the two language keys. |
| G13 `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser` (read) | A citation that dangles is excused where a pending `## Rule changes` item names its file, holds the citation whole in `from` and does not hold it in `to`. The citation is read as its italic text, so a `to` that still holds `*Question 1*` excuses nothing. The landing heading therefore differs from `Question 1` (*Data & interfaces* D2). |
| G14 `skills/settle/rule-changes.md` *Rule changes* (read) | An operation's `file` is a `.md` file of the policy root. `README.md`, `README.ko.md` and the skills are outside it and are edited in the pull request. `docs/running/the-review-and-parity-arms.md` has no `.ko.md` edition (executed, `ls docs/running`). |
| G15 the cases that read the passages this work moves or rewords (executed, a probe that reads each string literal of the tracked `.py` files against `:55-128` and `:255-517`; then read) | `tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it` holds one phrase for each clause of the fold paragraph, read from the order section. `tests/behaviour/test_waiver_decided_at_start.py` reads the two question tables, the ceiling, the lead **Ask question 1 alone**, the mark and the language-key paragraph from the file. `tests/text/test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape` reads the same lead and **What is checked is the answer**. No case reads a sentence of `:466-489` (executed, `git grep` on seven of its phrases under `tests/` finds nothing). |
| G16 `tests/behaviour/test_docs_line_wrap.py#COVERED` (read) | `skills/implement/orchestration.md`, `multi-repository.md` and `bootstrap.md` are each on the list, entered at birth because each was cut from covered prose. A file cut from the same prose by this work joins the list the same way. |
| G17 `lib/core.py#START` and `tests/lib/test_core.py:179-184` (read) | The `SessionStart` hook's last line sends a session to *Orchestrator: the order inside a ticket*. That heading and the file's path stay. |
| G18 `tests/behaviour/test_the_set_a_work_item_always_has.py:134-148` (read) | The ladder's sentence citing issue #35 is held by a case whose docstring records that the citation was kept on purpose. The ladder section is not this work's. |
| G19 `docs/layout/the-record-layout.md:51-59` (read) | A work item whose diff changes a `skills/*/orchestration.md` file ends its `changelog.md` with `### Process changes` and a table in the shape of `templates/records/process.md`. |
| G20 the unsettled designs under `seal/threads/` (executed, one `awk` over each `frame/design.md`) and `seal/follow-up.md` (read) | Each of the four holds the no-change block, so the policy in force is the baseline. Both tables of `seal/follow-up.md` are empty, so this work is no row's prerequisite. |
| G21 the latest release's `### Process changes` (executed, `gh release view --json tagName,body`) | One row, on the Status cell's value `deferred #N`. It changes nothing this work reads. |
| G22 issues #1476, #1478 and #1479 (executed, `gh issue view <N> --json title,body,comments,state`) and `refactor/1476-the-verifying-round-rule-has-four-owners` (executed, `git ls-tree -r`) | Each is open with no comments. #1476's branch holds its `routing.md` and no frame. `frame/plan.md` *Overlap with the release* reads each against this work. |

## Scope

In:

1. **The routing question moves to `skills/implement/routing-question.md`.** The file receives, with their sentences unchanged except where a sentence points at a passage by "above" or "below", the passages *Removes* rows 1 to 5 and 15 name, under the headings D2 gives. `skills/implement/orchestration.md` *Orchestrator: how the work is routed* keeps its heading and opens with the sentence D4 gives for the file. Each case that reads a moved sentence reads it in the new file.
2. **The language-key paragraph moves to the same file.** `:205-223` lands there with its bold lead unchanged. The body states no rule of its own for the keys: D4's sentence for the file names the condition. The case `tests/behaviour/test_waiver_decided_at_start.py#test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded` reads the paragraph in the new file.
3. **The merge order moves to `skills/implement/merge-order.md`.** `:466-489`, from "Where several work items of the release run side by side" to "the verifying round it owes.", lands there. The body paragraph **Which branch the pull request lands on is decided with the routing question** keeps what precedes and follows that range, the sentence "The orchestrator chooses which work item carries the move." among it, and gains D4's sentence for the file.
4. **The fold rule becomes paragraphs of judgment, in place.** `:55-128` is rewritten as the paragraphs D1's Home column names, in the order this sentence lists them, each with one judgment and the clauses D1 homes in it: what a decision is, who writes the fold, how far one fold reaches, what the orchestrator records and when, what a rejection leaves, and what is folded before the frame is committed. The first keeps its bold lead as written, because `:141` and `tests/text/test_the_rules_have_one_owner.py:529` cite it. The paragraph on reach names the sections G8 found stale sentences in, and holds D1 rows 22 and 23. No clause leaves the body (G23). The case of G15 holds one phrase per row of D1, read from the order section.
5. **The body states once what it states twice, and keeps no sentence no party acts on.** The passages *Removes* rows 9 to 13 and 16 to 18 name leave or shrink, and each row names the statement that stays. The third row of the table under **Three combinations do not stand** at `:564` then ends at "`chain_check.py` refuses it", because row 16 removes the sentence it pointed at.
6. **The opening of the file describes this file alone.** `:3-22` is rewritten to say what the body holds after items 1 to 5. The sentence that sends a repository with no `seal/` root to `skills/implement/bootstrap.md`, with both places the root can be, stays, and so does contract rule 11's sentence on `seal/` paths. The list of `skills/implement/SKILL.md`'s contents at `:15-19` leaves (*Removes* row 14).
7. **The sentences of G12 say where the passage now stands.** `README.md` and `README.ko.md` name `skills/implement/routing-question.md` for each answer and keep *Orchestrator: how the work is routed* for the rows. `skills/implement/multi-repository.md` names the new file for the question's shape. `skills/commit-pr-convention/SKILL.md` cites `skills/implement/routing-question.md` *The two language keys join the batch wherever either is missing*.
8. **Each new file is covered for line wrap.** The files D2 lists join `tests/behaviour/test_docs_line_wrap.py#COVERED`, each with a comment naming this issue (G16).

Out:

- **The ladder**, *Orchestrator: when a work item is required*, apart from *Removes* row 17; its sentence citing issue #35 stays (G18). Every section this list does not name is out too: the batch section's other paragraphs, *The frame is read against the issue at the spawn*, *Under agentic* apart from *Removes* row 13, the drain and the lesson table.
- **`agents/framer.md`.** Its rule *You have two routes back* cites *Orchestrator: the order inside a ticket* for the fold. The heading stands and the section keeps every clause, so no sentence of the definition becomes false.
- **Step 2's `pr.md` sentence at `:41-50`, the flow-log sentence at `:166-171` and the drain's first row at `:648`.** Issues #1478, #1479 and #1476 change them (`frame/plan.md` *Overlap with the release*).
- **The version.** #1476 carries the move.
- **A check on the file's size** (G3).
- **A direct edit of `docs/`** (G4).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 the body is at 0.30.0's size | Given the work item's HEAD with the release branch merged in. When the body is counted. Then it holds at most 5,242 words. | `wc -w skills/implement/orchestration.md`, run by the crafter at the last phase and by the proofer. |
| S2 the fold rule is judgments | Given the order section. When it is read from the lead **A decision made after the frame is committed is folded** to the paragraph before **Where a work item stands**. Then it is the paragraphs *Scope* item 4 names, each opening with a bold lead and holding one judgment. | Read by the proofer against *Scope* item 4. |
| S3 no clause of the fold rule is lost | Given D1. When each row is looked for at the home D1 names. Then each stands there once. | `tests/text/test_the_rules_have_one_owner.py` green, its fold case holding one phrase per row of D1; the case shown red before the rewrite, as `frame/plan.md` phase 2 says. The proofer reads D1 against the order section. |
| S4 each moved file is named with when it is opened | Given the body. When each path D2 lists is searched for. Then one sentence of the body says when the orchestrator opens that file, in the words D4 fixes, and each new file's first paragraph says the same of itself. | `grep -n` of each path in `skills/implement/orchestration.md`, read by the proofer. |
| S5 a moved passage says what it said | Given *Removes* rows 1 to 7 and 15. When each passage is compared with its landing text. Then they differ only where a sentence pointed by "above" or "below" at a passage now in another file. | `git diff --color-moved=zebra 9e9d1087f HEAD -- skills/implement/`, read by the proofer; the cases of G15 green against the new files. |
| S6 every citation resolves | Given the tree. When the citation check runs. Then it names nothing dangling, and it names `docs/running/the-review-and-parity-arms.md:56` as excused by this work item. | `tests/behaviour/test_a_cited_section_stands_in_its_file.py` green (G13). |
| S7 the hook's line still leads to the order | Given a session in a repository with a `seal/` root. When the hook prints. Then its last line names `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, and that heading stands. | `tests/lib/test_core.py` and `tests/hooks/test_core_start.py` green, unchanged. |

## Data & interfaces

**D1. The clauses of the fold rule, and where each stands after this work.** The rows are the paragraph at `:55-128` taken apart in its own order, then the two clauses G8 adds. The Home column names the paragraph of *Scope* item 4 that holds the clause.

| # | Clause | Came from | Home |
|---|---|---|---|
| 1 | A decision made after the frame is committed is folded, in place, into `frame/design.md` or `plan.md` before the next crafter spawns. | #945 | Body, what a decision is |
| 2 | A crafter reads the frame and not the issue's comments, so the decision has to stand in the frame. | #1442 round 2 | Body, what a decision is |
| 3 | A decision is anything that changes what the frame says the work is or why; the list of examples at `:59-62`; they are examples and not a closed list. | #1442 | Body, what a decision is |
| 4 | The framer writes a decision's fold, because the framer judges what the work should be. | #1442 | Body, who writes |
| 5 | The orchestrator sends every decision then pending to the framer in one message, each with its grounds and the coordinates it stands on. | #1442 | Body, reach |
| 6 | The orchestrator resumes the work item's framer while that session exists, and otherwise spawns a fresh framer with the decisions and the commit at which the frame was last written. | #1442 | Body, record |
| 7 | Before it sends, the orchestrator writes each decision as a row of `frame/plan.md` *Judgments of the run* and leaves it uncommitted, so the framer reads it with `plan.md` whole; the rewritten sentence keeps no reason, and the settle reads the row. | #1442, #1167 | Body, record |
| 8 | The orchestrator corrects its row where the framer's hand-back names a defect in it. | #1442 round 2 | Body, record |
| 9 | A decision the framer rejects stands as its judgment; the orchestrator rewrites its row to record the rejection and what the decision's source takes instead, and quotes the framer's *Alternatives considered* row in `pr.md`. | #1442 rounds 1 and 2 | Body, rejection |
| 10 | The version move and a prevention home are folded as an owner's decision is, because another rule gives each to the orchestrator to decide. | #1442 round 2 | Body, rejection |
| 11 | The orchestrator commits the frame files the framer changed and its own rows in one commit, before the spawn that reads them. | #1442 | Body, record |
| 12 | A statement the framer's hand-back names in `routing.md` or `pr.md` is the orchestrator's to repair. | #1442 | Body, who writes |
| 13 | Where a crafter's hand-back names a statement in a frame file or `routing.md`, the orchestrator reads each such file whole against HEAD, not only the named line, and rewrites every statement HEAD contradicts: the crafter's list is its reading of a file it does not write. | #1318, after #1234 | Body, reach |
| 14 | Such a statement records what the build changed and not what the work is, so the orchestrator folds it in a commit of its own and spawns no framer. | #1442 | Body, who writes |
| 15 | A statement of the tree in a section the frame dates to the commit it read is a claim about that commit and is not folded; a section that states the tree with no date gets the date and keeps its text. | #1368 | Body, reach |
| 16 | After a fold commit of its own, the orchestrator reads that commit and each file of the work item's directory that states the present whole against HEAD; a decision's fold is read by the framer that writes it. | #1327, #1442 | Body, reach |
| 17 | A statement found in `gaps.md` or `changelog.md` goes to a fix pass before the next round or phase, and the fix pass is the crafter that wrote the last build or fix commit. | #1318 round 1, #1327 | Body, who writes |
| 18 | Until the decision is folded, the orchestrator keeps one line of its own in `plan.md` naming the comments to fold, below the title, and deletes it in the commit that folds them. | #945 | Body, record |
| 19 | Before the frame is committed, the orchestrator folds the decision into the issue body, in place, and the comment that carried it records why. | #945 | Body, before the frame |
| 20 | Why in place: a body that contradicts a comment, or an update block above the old text, leaves the reader two versions; GitHub keeps the body's history. | #945 | Body, before the frame |
| 21 | The prompt that spawns the framer hands it the issue whole: the body as folded, one line naming the comments, the command that read them and its date. | #1166 | Body, before the frame |
| 22 | A sentence of a dated section that says what the work does or concludes is not a claim about the commit, and is folded with the fact it states. | G8, `1794201840` round 2 finding 1 and `1794200907` round 1 finding 5 | Body, reach |
| 23 | The fact a decision changes stands in more sections than the one the decision names, so the orchestrator's message names the fact and says that the coordinates it gives are the statements it has seen and not the whole list. | G8 | Body, reach |

**D2. The new files, each under `skills/implement/`.** Each opens with one paragraph saying who opens it and on which condition, as `multi-repository.md:3-5` does.

| File | Title | Headings, in order |
|---|---|---|
| `routing-question.md` | `# implement, the routing question` | `## Orchestrator: why the routing question is asked once, at the start`; `## Question 1, the mode`; `## Question 2, the boxes`; `## What each answer writes`; `## Orchestrator: a question in the batch names its answers`; `## Orchestrator: the two language keys` |
| `merge-order.md` | `# implement, the merge order of a release` | `## Orchestrator: the order the work items of a release merge in` |

**D3. The size, by part.** The first number of each row is counted at `9e9d1087f` (executed, `sed -n '<a>,<b>p' \| wc -w`). The second is an estimate.

| Part | Leaves the body | Enters the body |
|---|---|---|
| *Scope* item 1: `:225-229`, `:257-276`, `:278-341`, `:345-346`, `:375-378`, `:404-419` | 1,324 | 55 |
| *Scope* item 2: `:205-223` | 216 | 40, inside item 1's sentence |
| *Scope* item 3: `:466-489` | 290 | 45 |
| *Scope* item 4: `:55-128` | 872 | 830 |
| *Scope* item 5 | 404 | 58 |
| *Scope* item 6: `:3-22` | 207 | 120 |

The estimate of the body after the six parts is about 5,150 words, against S1's bound. Without items 2, 5 and 6 it is about 5,750.

**D4. When each new file is opened.** The body says each condition in one sentence, and the file's first paragraph says the same.

| File | Opened by the orchestrator |
|---|---|
| `routing-question.md` | when it puts the batch of questions, the routing question among them, to a person, and where either of the two language keys is missing from `config.json` under the `seal/` root, which it reads before the routing commit |
| `merge-order.md` | where the release holds two or more work items, before it spawns the first framer of the release |

## Rule changes

- change
  file: docs/running/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: is routed there under its answer `agentic`, in
    `skills/implement/orchestration.md` *Question 1*.
  to: is routed there under its answer `agentic`, in
    `skills/implement/routing-question.md` *Question 1, the mode*.

## Removes

Every coordinate is in `skills/implement/orchestration.md`.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| 1. Why the routing question is one question at the start, and **Ask question 1 alone** | `:257-276` | `skills/implement/routing-question.md` *Orchestrator: why the routing question is asked once, at the start* |
| 2. `### Question 1`, whole | `:278-311` | `skills/implement/routing-question.md` *Question 1, the mode* |
| 3. `### Question 2`, whole, **The ceiling** among it | `:313-341` | `skills/implement/routing-question.md` *Question 2, the boxes* |
| 4. The two paragraphs that map answers to rows: "Question 1's first three options" and **`complete` writes all four party rows** | `:345-346`, `:375-378` | `skills/implement/routing-question.md` *What each answer writes* |
| 5. **The routing question is the orchestrator's, whether or not a framer runs**, its block and the paragraph after it | `:404-419` | `skills/implement/routing-question.md` *Orchestrator: why the routing question is asked once, at the start* |
| 6. **The two language keys join the batch wherever either is missing** | `:205-223` | `skills/implement/routing-question.md` *Orchestrator: the two language keys* |
| 7. The merge order of side-by-side work items, the late move's verifying round among it | `:466-489` | `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in* |
| 8. The fold paragraph as one paragraph of ordered acts | `:55-128` | Rewritten in place as *Scope* item 4's paragraphs, every row of D1 among them |
| 9. **The first edit waits for the routing answer, and the orchestrator holds that** | `:231-236` | Step 1 at `:26-27` and **The orchestrator writes the answer down before the first edit** at `:421-427` state it. Its sentence "No check refuses an earlier edit; …" joins the paragraph at `:421-427`. |
| 10. "On a branch whose `routing.md` answers `Automation` with `yes`, the rule for a question that arises mid-run is the paragraph …" | `:245-248` | **`Automation` is a record, and no script decides anything on it** at `:380-383` names the same paragraph of `docs/running/the-run.md`. |
| 11. "The test for whether something is a question or a row: …" | `:250-253` | The bullet **Assume, in writing, whatever would not change what you build** at `:197-199` states it. |
| 12. "Under `direct`, … no declaration is written, and the trailer is the record." and "The declaration is what CI reads at the pull request, for **either** review answer." | `:425-427`, `:448-449` | "A change belonging to no work item writes no declaration, …" at `:450-453` states the first. "because the check happens at the pull request and CI sees only what is in the tree" at `:423-424` states the second. |
| 13. **A wrong choice stays visible** | `:591-597` | Its first sentence is **The exit is last** (`:296-301`, landing by row 2). Its second is the sentence at `:370-373` on the sealer reading the grounds. Its third is `skills/settle/SKILL.md` *The settling session's procedure* step 5, which names *Under agentic* as the section to rewrite. |
| 14. The list of what `skills/implement/SKILL.md` holds | `:15-19` | That file's own headings. The sentences on who opens which half stay. |
| 15. **A question in this batch names its answers, and every answer continues** | `:225-229` | `skills/implement/routing-question.md` *Orchestrator: a question in the batch names its answers*; the orchestrator writes a question only when it puts the batch to a person, which is when it opens that file (D4) |
| 16. "A wrong answer here is read against the record the run left: …" | `:399-402` | The third row of **Three combinations do not stand** at `:564` states the check's refusal, and the sentence at `:370-373` names the sealer's step 4. |
| 17. "What it costs: …" through "… keeps the judgment from being free-form." | `:627-631` | It can go: the two sentences say why a judgment was preferred to a count, and no party acts on them. The sentences after them, on naming the value, stay. |
| 18. The paragraph **Where a migration config is declared, the comparison with the original is recorded where the answer puts it**, shortened to one sentence | `:440-446` | `skills/legacy-parity/SKILL.md` *Recording the comparison* and `docs/running/the-review-and-parity-arms.md` *Parity arm* state where the comparison is recorded and which shapes leave code uncompared. The sentence that stays cites both. |

This work adds no gate, check, hook, mark or case, so it owes no removal in return. The cases of G15 keep what they hold and read it where it now stands. No case is removed.

Framed 2026-11-10 by framer, before the build.
