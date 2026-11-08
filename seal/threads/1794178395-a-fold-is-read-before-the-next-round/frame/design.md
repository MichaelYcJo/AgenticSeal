# Design: a fold is read before the next round (#1442)

## Grounding

The tree as read at `7056ee61`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *Each agent judges its own target, independently of the others* | The framer judges what the work should be. A decision made after the frame is committed changes what the work is or why, so it is the framer's judgment to write. Today the orchestrator writes it, and no other party reads it before the next round (G3). |
| G2. `skills/core/SKILL.md` *The rule a mechanism is kept against* | A route or a check stays only while what it catches outweighs what it costs. The cost of sending a fold to the framer is weighed against the regressions G9 lists, and against how many folds there are (G10). |
| G3. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A decision made after the frame is committed is folded** (`:49-81`) | The orchestrator rewrites the frame sentence a decision changes, writes the decision's row of `frame/plan.md` *Judgments of the run* in the fold commit, folds each statement a crafter's hand-back names as contradicted by HEAD (reading each such file whole), and after the fold commit reads that commit and the work item's records whole against HEAD. #1318 (*Scope* item 5 of `1793721630-the-party-that-fixes-checks-its-fix-first`, read at `v0.31.0`) added the reading. The issue calls that reading written guidance with no mechanism behind it. |
| G4. Same file, *The frame is read against the issue at the spawn* (`:102-134`) | Before the first build, the orchestrator sends its reading of the frame to the framer as proposals, in one exchange. The framer answers each with agree, agree with a change, or reject with grounds. It folds what it agreed and writes each rejection as a row of *Alternatives considered*. "The orchestrator edits no frame file." This work reuses that exchange's shape for a decision made after the frame is committed. |
| G5. `agents/framer.md` *Rules*, the rule opening **The one route back is the review chain's** (`:240-247`) | The framer is spawned again only when the orchestrator routes a `regression:` to it, and it then adds `Reframed <date> by <who>, after round <N>.` under its mark. The rule carries "`docs/running/the-run.md` *The run* owns that rule", which `tests/text/test_the_rules_have_one_owner.py` rule 16 pins (`:122-126`, read). |
| G6. `docs/running/the-run.md` *The run* | A regression is a defect that a fix pass's own commit introduced. Where the fix built what the frame says and the defect still stands, the work item goes back to the framer. Each fold is a row of *Judgments of the run*. An owner's remark made during the run is folded into the frame or the code when it arrives (`:63-67`). |
| G7. `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* | Resuming a finished agent with its context intact is an act the run already performs. Where the session is gone, the run spawns a fresh agent instead and hands it the records. The paragraph opening **The fix pass then finds what the fixes left standing** (`:71-80`) has the orchestrator fold, in a commit of its own, the frame statements that a fix pass's hand-back names. These statements are G3's crafter-named kind. |
| G8. Same file, *Orchestrator: the run ends with a verifying round* (`:98-125`) | A fix confined to the work item's records owes no verifying round, because the sealer reads it. A fix that touches code owes one. Each regression in G9 reached code or a shipped document through the fix pass that built on the fold, so each one cost a fix pass and a verifying round. |
| G9. The regressions traced to a fold, opened at their release tags with `git show` (executed) | Of the five work items the issue names, four were opened. (1) #1235: `1793538230-code-text-brought-to-the-tree` round 2, findings 1 and 2, at `v0.27.3`. The fold `1ac8b651`, written after round 1, misstated #1255's scope in a parenthetical at `frame/design.md:28`. The fix pass then wrote the fold's words into a docstring, and round 2 found that "nobody opened #1255". (2) #1299: `1793655640-the-orchestrators-part-of-a-body-cites-its-records` round 2, at `v0.29.0`. The trigger was the *Scope* item and the `## Removes` row that `36fce349` folded. (3) #898: `1793599986-a-stopped-head-run-does-not-seal` round 2, at `v0.29.0`. The trigger was the `to:` that `f66eca7f` folded. (4) `1794128303-the-plugin-ships-two-hooks-again` round 3 finding 1, in the tree. The fold `a19d215ea` wrote a design change decided after round 2 into two *Grounding* cells, and the orchestrator's *Judgments of the run* row and the `pr.md` quote carried the same text, all with an unescaped `\|\|`. Each one is a decision folded after a round's finding and before the fix pass that built on it. The fifth, #1216 (0.28.0), was not opened: it rests on the issue's account (#1280), `unverified`, and nothing in this design depends on it. |
| G10. A probe (executed): the *Judgments of the run* rows that mention a fold, counted with `grep -i fold` over every `frame/plan.md` at `v0.34.1` and `v0.35.1` | Over the 8 work items at those tags, 23 rows mention a fold. Of those, 14 name a phase's hand-back (`grep -i 'hand-back named'`), and 6 name a round. Of the 23, 13 come from the two work items that ran the most phases. The split by keyword is a sample: a row that words its trigger differently is miscounted. None of the regressions G9 opened traces to a statement a crafter named. |
| G11. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, and `docs/README.md` | The subject of this work is what the skills and the agent definitions instruct, which stand outside the policy root. So the policy-root sentences that state who folds take `## Rule changes` operations, and the settle writes them. The unsettled designs on the branch, `1794128303`, `1794142458` and `1794142459`, each state `- nothing` (read), so no operation collides. |
| G12. Contract rule 12; `agents/crafter.md` *Rules*, the paste-ready paragraph (#1286) and **Before you hand back, your range and the work item's records are read whole against HEAD** (#1318) | The party that fixes reads its own fix and each present-tense file of the work item whole. A framer that folds is such a party. Its rule cites rule 12 and does not restate it. A crafter applies paste-ready text only after reading it against the frame and the code. The fold in G9 (1) was taken as the frame, and its words passed through the fix pass unread. |
| G13. `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals* (`:395-424`); #1415 | `pr.md` is the orchestrator's. Every round reads it, and the orchestrator rewrites a quote whose source a fold changes. Nothing here changes it. A quote copies the framer's sentence once the framer writes it. |
| G14. `agents/framer.md` *A count of a list is stated once, beside the list* (#1401) | It binds the framer's fold as it binds the first frame. |
| G15. `skills/code-review/orchestration.md:182-196`, the guidance the settle of #1432 added (read) | It is about one mechanism whose edges successive fix passes chased, and it does not touch folds. Nothing here changes it. |
| G16. The ticket and its comments | `gh issue view 1442 --json comments` returned 0 comments on 2026-11-09 (executed). The body is as filed. The latest Release's `### Process changes` table (`gh release view`, executed) holds no row about folds. `seal/follow-up.md` holds no row that this work is a prerequisite of (read). |

## Scope

In:

1. **`skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A decision made after the frame is committed is folded** (`:49-81`), rewritten in place so that the framer writes a decision's fold.** The bold lead and its reason (a crafter reads the frame and not the issue's comments) stay. The sentence "The orchestrator rewrites the sentence of the frame the decision changes, where it stands" goes. In its place the paragraph says seven things:
   - **What a decision is.** A decision is anything that changes what the frame says the work is or why. Examples: a round finding whose route changes the frame, a round finding located in a frame file, an owner's remark, an issue comment, a prevention home, a scope a spawn gives beyond a plan row, and the version move. These are examples of the rule, and the paragraph does not list them as a closed set.
   - **Who receives it, and when.** The orchestrator sends every decision pending at that point to the framer in one message, before the spawn that will read them. Each decision carries its grounds and the coordinates it stands on: the finding, the comment, or the owner's words.
   - **Which framer.** The framer of the work item is resumed while its session still exists, as the fix pass resumes the implementer in G7. Otherwise it is spawned fresh and handed the decisions and the commit at which the frame was last written. No context threshold is stated: none has been measured for a framer.
   - **The judgment row first.** Before it sends, the orchestrator writes the decision's row of `frame/plan.md` *Judgments of the run* and leaves it uncommitted, so the framer reads that row when it reads `plan.md` whole. The orchestrator then commits the framer's files and its own row in one commit, before the spawn that reads them.
   - **The framer's hand-back.** The hand-back names each statement the fold contradicts in a file the framer does not write. A statement in `gaps.md` or `changelog.md` goes to a fix pass, as the paragraph already says for those files. A statement in `routing.md` or `pr.md` is the orchestrator's to repair.
   - **A rejected decision.** A decision the framer rejects stands as its judgment, as a proposal left after the exchange at the spawn does. The orchestrator rewrites its *Judgments of the run* row to record the rejection and what the decision's source takes instead, a finding's route or the next spawn's scope, and quotes the framer's *Alternatives considered* row in the work item's `pr.md`. The version move and a prevention home are folded as an owner's decision is, because other rules give the orchestrator to decide them.
   - **What stays the orchestrator's.** The orchestrator still folds a statement a crafter's hand-back names as contradicted by HEAD, as G3 has it: it reads each file whole, then reads the fold commit and the records after it. That reading is now scoped to those statements. The paragraph's other sentences stay: the dated sections, the one pending line in `plan.md`, the fold into the issue body before the frame is committed, and the issue handed whole to the framer.
2. **Same file, the paragraph opening **A problem that recurs within a run gets a prevention home at once** (`:93-100`).** The sentence "The orchestrator folds it into that work item's frame, as any decision after the frame is folded" changes so that the home is folded into the frame as *Scope* item 1 folds any decision, by the framer. The orchestrator still records the home in a comment on the issue.
3. **Same file, *Orchestrator: how the work is routed*, the version-move sentence (`:389-392`).** "the orchestrator folds the move into that section before it spawns the last phase" changes so that the framer folds the move, as *Scope* item 1 states, before the orchestrator spawns the last phase. This paragraph is the one #1443 rewrites (`frame/plan.md` *Technical context*).
4. **`skills/implement/SKILL.md` *3. The SDD file set*, the sentence at `:309-311`.** "a scope a spawn gives beyond it is a decision the orchestrator folds into the plan before the spawn" changes so that the framer folds it, citing `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*.
5. **`agents/framer.md` *Rules*, the rule opening **The one route back is the review chain's** (`:240-247`), rewritten in place as the framer's two routes back: a fold, and the review chain's regression.** The fold half says eight things:
   - **How it starts.** The framer is resumed or spawned again with the decisions the orchestrator sends.
   - **Answering a decision.** The framer answers each decision of the orchestrator's with agree, agree with a change, or reject with grounds, as the exchange in G4 does. It writes each rejected decision as one row of *Alternatives considered*.
   - **An owner's decision.** A decision the owner made, the version move and a prevention home are folded as they were made. Where the framer judges that it conflicts with the tree, it names the conflict in its hand-back.
   - **Opening before writing.** Before it writes what a decision says, the framer opens each coordinate the decision cites, such as an issue it restates. This is the framer's existing rule that a fact reaching it in prose is opened at its coordinate.
   - **Rewriting in place.** The framer rewrites in place every sentence of its three files that the decision changes, reading each file whole, as contract rule 12 asks of the party that fixes. It reads the orchestrator's uncommitted *Judgments of the run* row with `plan.md` and names any defect in that row in its hand-back.
   - **What it does not write.** The framer writes no line under its mark, no Status cell and no *Judgments of the run* row. A section dated to the commit it read keeps its date.
   - **A fresh spawn.** A fresh spawn reads the three frame files, the coordinates the decisions cite, and the diff since the frame's commit over the paths the decisions name. It does not repeat the wide reading of step 4.
   - **The hand-back.** The framer hands back each sentence it changed, by coordinate, and each statement the fold contradicts in a file it does not write.

   The regression half stays as written, including the sentence "`docs/running/the-run.md` *The run* owns that rule".
6. **Tests.** `tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it` gains the clauses of *Scope* item 1: the framer folds the decision, the judgment row is written before the framer reads `plan.md`, and the framer is resumed or spawned fresh. Its pins on the crafter-named statements stay. A case in the same module pins the fold half of *Scope* item 5 in `agents/framer.md`. The rule's `check:` line already names that module. Each new clause is seen red with its sentence deleted (contract rule 15).
7. **The work item's `changelog.md`**, with one `### Process changes` row for *Scope* items 1 to 5. Its *Why* cell cites G9 by path and heading.

Decided, and nothing is built for it:

8. **No check, hook or mark.** A script cannot tell who wrote a frame sentence, because the orchestrator commits every frame file. The fold adds no line under the `Framed` mark: the *Judgments of the run* row already records it, and `Reframed` stays the regression route's line.
9. **`skills/code-review/orchestration.md` stays as it is.** Its fix-pass paragraph (`:71-80`) folds the crafter-named statements that *Scope* item 1 keeps with the orchestrator. Its `pr.md` paragraph (`:416-424`) stays true (G13).
10. **The policy root.** The policy-root sentences that state who folds take the operations in `## Rule changes` below (G11).

Out:

- **Statements a crafter names as contradicted by HEAD.** They stay the orchestrator's to fold. They are 14 of G10's 23 rows, none of the regressions in G9 traces to one, and a framer exchange for each would cost without a record of what it catches (G2). `frame/plan.md` *Alternatives considered* weighs the uniform route.
- **A check of table shape over the work item's records**, counting each row's cells against its header. It would catch one regression in G9, and it would run at the pull request, after the rounds (`frame/plan.md` *Alternatives considered*).
- **How `session_cost.py` grades a fold exchange.** That exchange is a framer segment with few reads, and its grading is #1440's.
- **`pr.md`, `routing.md`, and the orchestrator's own rows of `frame/questions.md`.** These are the orchestrator's own files and rows.
- **The issue's second *Done when* bullet**, that regression lines traced to a fold stop recurring on the readings #1439 posts. It is a count taken after the release (`frame/questions.md` Q1).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| A round's finding changes the frame | Given a round whose finding the orchestrator routes to a fix pass with a frame change, when the orchestrator decides it, then the orchestrator writes the *Judgments of the run* row and sends the decision to the framer, the framer writes the frame sentence, and the fix pass builds from the framer's text | read `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*; the case of *Scope* item 6 |
| The framer reads the orchestrator's row | Given the uncommitted *Judgments of the run* row, when the framer folds, then it reads `plan.md` whole and names any defect in that row in its hand-back, and the orchestrator commits the row and the fold together | read `agents/framer.md` *Rules*, the fold half |
| A statement a crafter names | Given a hand-back that names a frame statement HEAD contradicts, when the orchestrator folds it, then the orchestrator reads the file whole as today, and no framer is spawned | read the rewritten paragraph; the existing pins of `test_a_decision_after_the_frame_is_folded_into_it` stay green |
| No framer session remains | Given a new session or a new day, when a decision is pending, then a fresh framer is spawned with the decisions and the frame's commit, and it reads only what the fold half names | read `agents/framer.md` *Rules*, the fold half |
| An owner's remark | Given an owner's remark during an automated run, when it is taken up, then the framer folds it as the owner made it and names any conflict with the tree | read the fold half; `## Rule changes` item 3 |
| No new mark | Given a fold, when the framer writes it, then no line is added under `Framed`, and `Reframed` stays the regression route's | read `agents/framer.md`; `skills/code-review/scripts/chain_check.py` unchanged in the diff |
| After the release | Given the readings #1439 posts for 0.36.0 and later, when they are read, then no `regression:` line traces to a decision's fold | a measurement after the release (`frame/questions.md` Q1) |

## Data & interfaces

No schema changes. Two message shapes change hands, and both are prose in the run:

- **The fold message** (orchestrator to framer): each decision with its grounds and the coordinates it stands on, and the commit at which the frame was last written.
- **The framer's fold hand-back**: its answer to each decision, each sentence it changed by coordinate, any defect in the uncommitted *Judgments of the run* row, and each statement the fold contradicts in a file it does not write.

## Rule changes

- change
  file: docs/running/the-agent-set.md
  section: One contract every agent receives, and one definition each
  from: The framer judges what the work should be and the orchestrator holds the
    issue, so a frame weaker than the issue asks is found by the party that holds the issue
    and decided by the party that drew the frame, and the orchestrator edits no frame file.
  to: The framer judges what the work should be and the orchestrator holds the
    issue, so a frame weaker than the issue asks is found by the party that holds the issue
    and decided by the party that drew the frame, and the orchestrator edits no frame file
    in that exchange. A decision made later in the run is folded by the framer too, so each
    sentence of the frame that says what the work is or why is the framer's; the
    orchestrator folds only the statements a crafter's hand-back names as contradicted by
    HEAD.
- change
  file: docs/running/the-agent-set.md
  section: What each party writes, and when
  from: A
    scope a spawn gives beyond the plan's row is a decision the orchestrator folds into the
    plan before the spawn
  to: A
    scope a spawn gives beyond the plan's row is a decision the framer folds into the
    plan before the spawn
- change
  file: docs/running/the-run.md
  section: The run
  from: A question or a remark the owner raises
    during the run is taken up when it arrives: the orchestrator folds it into
    the frame or the code, and never defers it to the pull request body.
  to: A question or a remark the owner raises
    during the run is taken up when it arrives: the framer folds it into the
    frame, or it goes into the code, and it is never deferred to the pull
    request body.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The orchestrator as the writer of a decision's fold: "The orchestrator rewrites the sentence of the frame the decision changes, where it stands" | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* | `agents/framer.md` *Rules*, the fold half (*Scope* item 5) |
| The orchestrator's reading of its own fold commit, for a decision's fold | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the sentence opening "After the fold commit" | The framer reads its fold as the party that fixes (contract rule 12). The sentence stays for statements a crafter names (*Scope* item 1). |
| "The orchestrator folds it into that work item's frame" | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the prevention-home paragraph | *Scope* item 1, by the framer |
| "the orchestrator folds the move into that section" | `skills/implement/orchestration.md` *Orchestrator: how the work is routed* | *Scope* item 1, by the framer |
| "a decision the orchestrator folds into the plan before the spawn" | `skills/implement/SKILL.md` *3. The SDD file set* | *Scope* item 1, by the framer |
| The claim that the framer has one route back | `agents/framer.md` *Rules*, the lead "The one route back is the review chain's." | The rule names both routes, and its regression half keeps the citation of *The run* that rule 16 pins |

The work adds a route, the framer's fold. In return it takes out the orchestrator's authorship of a decision's fold and its reading of that fold. It adds no check and no mark (*Scope* item 8).

Framed 2026-11-09 by framer, before the build.
