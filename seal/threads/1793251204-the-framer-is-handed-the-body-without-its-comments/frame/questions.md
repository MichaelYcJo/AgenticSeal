# Questions for the planner: 1793251204-the-framer-is-handed-the-body-without-its-comments

## Answered by the tree, not to be reopened

- **Issue #1158 has no comments.** Its body is the whole request (executed:
  `gh issue view 1158 --json body,comments` prints `"comments":[]` on
  2026-10-29).
- **Who owes the line on the comments.** The orchestrator does, because it
  already folds a comment's decision into the body before the frame is
  committed (`skills/implement/orchestration.md` *Orchestrator: the order
  inside a ticket*). `agents/framer.md` step 4 cites that section and states
  only what the framer receives (`plan.md` A4).
- **What the line holds.** It holds the body as folded and one line naming
  the comments, with its command and date, not each comment's text. The body
  as folded is the request (`docs/issues-and-milestones.md` *An issue is its
  body and its comments together*; `plan.md` A3).
- **A line the framer cannot open, or no line at all, is not a row.** A line
  `gh` cannot open goes into `## Grounding` as the orchestrator's finding
  (`agents/framer.md` *Rules*, **What the tree can answer, you answer.**). A
  missing line is reported the way a missing `routing.md` is (`plan.md` A5).
- **The sharp-s case does not take the no-row grader.** Round 1 of #1047
  found that no run on either side left a `shout` row, so the grader could
  not be seen red there (`plan.md` A6).
- **The no-row pin is a sixth case whose question is a generator's output.**
  #971's Q3 is a question of that kind which the old definition left as `a
  measurement` (`plan.md` A9).
- **Every framer case takes the comment line.** `framer_case` writes one
  spawn, and that spawn models the production one (`plan.md` A10).
- **How many paid runs.** Four: two of the new case on each side, side A
  first, capped at 15 USD together (`plan.md` R1 to R4). Q1 asks a person to
  accept that spend.
- **The crafter can run `claude plugin eval` from its own environment.**
  #1047's crafter ran both of its sides itself
  (`seal/threads/1793240966-the-framer-has-no-read-only-probe/frame/questions.md`
  Q3, answered by the work).
- **#1047's records are not edited.** The settle after the release closes
  the no-row row in its `gaps.md` *Not verified* as answered, naming this
  work item's side files (`skills/settle/SKILL.md` *The settling session's
  procedure*, step 4).
- **The policy root is `docs/`,** and no unsettled design states a change to
  *An issue is its body and its comments together* (executed, `frame/design.md`
  *Grounding*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How much may this work spend on paid runs to see the new case red on the definition at `c48cd5e3` and green on this work's? A framer run costs about 2.5 USD (executed: #1047's side files, 5.196 and 4.812 USD for two runs each). The tree cannot choose a spend. | a person | (a) Four runs: two of the new case on each side, side A first, capped at 15 USD together with `--max-cost-usd`, about 10 USD expected. This meets contract rule 15 and the issue's last Done-when line for the new case. (b) Six runs: (a) plus two runs of the sharp-s case on the new side, capped at 20 USD, about 15 USD expected. This also shows the sharp-s case still passes `shape-answers-by-probe` with its new spawn line, which `plan.md` R3 judges the line does not bear on. (c) No paid run. The case is committed without being seen red, `gaps.md` *Not verified* names the owner, and the issue's last Done-when line is not met. | (a) | open |
| Q2 | What does the build do if side A, the definition at `c48cd5e3`, fails `shape-no-measurement-row` on neither run, or only on a row that does not ask the generator question? Then the old framer answered the generator question too, and the case does not separate the definitions. Only the paid run can show it, and its spend is Q1's. | a person | (a) Keep the case and its graders as the pin of the no-row half from here on, commit side A's file as the record that it did not separate, and still run side B. `gaps.md` *Not verified* states that the case was not seen red, with the owner as answerer, and the pull request body says the issue's last Done-when line is not met, so the owner decides whether `Closes #1158` stands. (b) Reword the new case's issue once so the generator's output is harder to reach without running it, and run side A again, at most 6 USD more on top of Q1's cap. The rewording is chosen from what side A's traces show, and a second miss falls to (a). (c) Remove the new case and its graders. The no-row half stays unpinned, and `gaps.md` says so. | (a). No second spend on a case that measured what it measured. | open |
