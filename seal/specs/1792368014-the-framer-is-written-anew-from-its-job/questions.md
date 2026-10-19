# the framer is written anew from its job (#968) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## What the tree answered, so nobody reopens it

The issue left these open, and the repository settled them. The grounds are
in `spec.md` and in `plan.md`'s Alternatives table.

- **No baseline run.** The four preload files hash the same at 43cbc361 as
  in #967's last framer side, the three templates the framer opens are
  untouched, and the cited sections are unchanged (`spec.md` §*The baseline,
  decided by guard 1*; Alternative E).
- **No new grader.** The suite is af9c924b's for every issue, so a grader
  added now is run by no side; a test pin holds the replace-or-keep sentence
  (Alternative F). Q5 keeps the grader for when the suite moves.
- **`implement` and `writing-style` are not edited.** An edit would
  re-measure the smith for a sentence that is not false (Alternative H).
- **The opening's skeleton, per-call bound and read-by-range rule stay**, as
  rules without their release readings, because batching is the half of
  rule 5 the rewrite does not control (Alternative G).
- **`confidence-check` and `feature-planner` stay named in one step**, since
  `tests/test_chain_hooks_hardening.py::test_each_utility_skill_is_callable_from_exactly_one_definition`
  holds the framer as their one home.
- **The framer keeps no `model:` key**; a model change would be measured as
  a definition change.
- **Removing the agent** (`Planning` = `the session` everywhere) was weighed
  as the replacing alternative and rejected on the grounds in Alternative D.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **What does *the residue … leave* mean in #968's body?** The body says *the residue, the emoji and the proof block leave*. #957's `plan.md` phase 4 lists *the residue* among the framer's rules that stay. The emoji and the proof block are already gone from the framer's read set (`executed`: no emoji and no `applied` block in the four preload files or the three templates). The tree cannot say which sentence the owner meant | a person — the owner | **The restatement leaves, the rule stays** (default): the framer's explanation of the three answerers leaves, because `templates/sdd-questions.md` owns it and the framer opens that template; the rule that each row says why the tree could not answer it, and the head listing what the tree answered, stay as one rule paragraph with their pin · **The rule leaves too**: the definition says nothing about `questions.md` beyond its template; `tests/test_waiver_decided_at_start.py::test_questions_md_is_the_residue_and_every_row_says_why` is removed as narration | the restatement leaves, the rule stays | answered 2026-10-19 by the repository owner: the restatement leaves, the rule stays |
| Q2 | **At a rebase, is the framer's read set compared by file or by section?** Guard 1 counts *every skill or section its steps open*; guard 3 counts *a change to a file in this issue's agent's read set*. #976 and #985 both edit `docs/the-review-record.md`, in sections the framer does not open; the framer opens §*The run* only on a reframe, which no eval case exercises. The guards are the owner's words, and they disagree on this file | a person — the owner | **By section** (default): a rebase bringing #976's §*The stamp* or #985's §*The round record* re-measures nothing; a change to any of the seven whole files or to §*The run* re-measures, about $17 each · **By file**: each of #976 and #985, if it merges first, forces one re-measure, about $17 each | by section | answered 2026-10-19 by the repository owner: neither — the measurement waits. Phase 1 (the rewrite, $0) is built now; phase 2's paid side runs once, on the tree rebased after #976 and #985 have merged, so no merge can move the read set after it and no re-measure is owed |
| Q3 | **Which pins on `agents/framer.md` pin a rule, and which pin narration?** (#957's Q7, for this file.) Sorting needs the new sentences, which do not exist yet | the work — phase 1 sorts them, re-pointing a pin on a rule that stays and removing one on narration with one line in `phases/phase-1.md` | — | — | answered 2026-10-19 by the orchestrator, from `phases/phase-1.md` (2cb43374): pins on rules that stay were re-pointed to the new sentences, and three narration pins were removed, each named there with one line |
| Q4 | **Do the eval traces give the framer's requests, tool calls and tokens per request?** S10 needs them to decompose rule 5. `session-cost --segments` reads one agent's span, calls and tokens from a transcript; whether it reads the eval's `trace.jsonl` shape is read off the first saved run | a measurement — phase 2, on the kept raw output | — | `session-cost --segments` over each trace; where it cannot read the shape, a count of the subagent's assistant events, their `usage` and their `tool_use` blocks | open |
| Q5 | **Is the replace-or-keep grader added to the framer's cases when the suite moves past af9c924b?** #957's frame names the framer cases' `shape-` graders as a holder of the rule. This milestone cannot run one, and the tree cannot say when the suite moves | a person — the owner, when the suite next moves | **Add it then**: one grader per case reading the Alternatives table for a replacing row · **Leave the pin alone**: the sentence is held, and the behaviour is not | the pin alone in 0.22.x; nothing is built for the grader here | open |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip. Measured: six probes at about three seconds each answered a row that
  had been written into the human batch, and they showed the ticket's own
  instruction was wrong.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer, which would spend the interruption the framing phase exists to spend
  once.

**The framer opens rows and does not own their answers.** A row is a question
put to somebody else, so opening one costs little and closes nothing — and the
`Status` column is written by whoever answered, as `answered <date> by <who>`,
never by whoever asked. Sorting the rows this way is also what keeps the
batch short enough to answer in one sitting: two of the three kinds never
needed a person at all.

No row blocks the build: Q1 and Q2 run on their defaults, Q3 and Q4 are
phases 1 and 2's own work, and Q5 waits for a later suite.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
