# Implementation Plan: 1793251204-the-framer-is-handed-the-body-without-its-comments

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 to 3.
The build takes the defaults of `frame/questions.md` Q1 and Q2, answer (a) for each, and the owner may overturn them at the pull request.

## Summary

Folding the comments into an issue's body before the frame is drawn is
already the orchestrator's duty. No sentence says what the framer's spawn
then tells it about the comments, and `agents/framer.md` step 4 says only
"The ticket and its comments". In #1047's paid runs the framer was handed the
body alone and `gh` could not read the comments in the runner, so it asked
about them. Those rows were the only ones `shape-no-measurement-row` ever
caught, and the grader was removed. This work closes the gap in four places:

- The orchestration section says the spawn hands the body as folded, with
  one line on the comments.
- The framer's step 4 says what it receives and what it does when it cannot
  open that line.
- Every framer case's spawn carries that line.
- A sixth case pins the no-row half of #1047's rule on a question the old
  definition leaves as a row. It is seen red on the definition at `c48cd5e3`
  and green on this work's, in four paid runs capped at 15 USD.

## Technical context

- `agents/framer.md`: 212 lines and 11,889 bytes at `0bf22734` (executed:
  `wc -l`, `wc -c`). Step 4's clause "The ticket and its comments" is at
  `:69-70`. The `check:` line of **A question a command answers is answered
  by running it.** is at `:149`. No test reads the clause (executed:
  `git grep`, `frame/design.md` *Grounding*).
- `skills/implement/orchestration.md`: the folding paragraph is `:37-47`,
  and the acts table's row *Orchestrator: the order inside a ticket* is
  `:452`. `tests/text/test_the_rules_have_one_owner.py:363-447` pins step 2's
  opening `2. The framer writes`, the run of step 2 from "spawns the crafter"
  to "the pull request opens (", and the folding paragraph's phrases, "folds
  the decision into the issue body" among them. The new sentence goes after
  that paragraph's last sentence and leaves each pinned phrase whole.
- `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refuses a run
  of `WINDOW` consecutive words two rule files share. Step 4 cites the
  orchestration section and words its own sentence afresh.
- `evals/scripts/rule_cases.py` (980 lines): `base_project` at `:198`,
  `PROBE_ANSWER` and `probe_graders` at `:551-572`, `FRAMER_ISSUES` at
  `:575`, `framer_case` at `:600-656`, and `cases` at `:945-950`. The item
  id is `179000002{index}-{slug}`, so the sixth case is
  `1790000026-generated-page`. `write` refuses a text that holds
  `AGENTIC_EOF`. The generator reproduces the committed framer cases byte for
  byte (executed, `frame/design.md` *Grounding*).
- `7ac24a06` removed `MEASUREMENT_ROW`, the `no-measurement-row` grader in
  `probe_graders`, and its case in `tests/evals/test_rule_cases.py`
  (executed: `git show 7ac24a06`). The pattern comes back from that diff
  unchanged.
- `tests/evals/test_rule_cases.py` `Test_framer_case` (`:253-285`) reads a
  case's graders back the way a side records them, through
  `noninferiority.py#grader_from`. The new cases follow its two existing
  ones.
- `seal rules` (`tests/github/test_rules.py`) refuses a `check:` line that
  names a path that does not exist. The new case directory therefore lands in
  phase 1, before phase 2's `check:` line names it.
- `evals/scripts/noninferiority.py run` copies the plugin tree at `--rev`,
  puts the suite at `--suite-rev` into it, runs `claude plugin eval` with one
  `--case` glob, and saves every run's trace under `<out>.raw/` (read:
  `:1-60`, `:612-660`). The case's name is `framer rule-framer-<slug>`, so
  the glob takes a leading `*`, as #1047's phase 3 found
  (`seal/threads/1793240966-the-framer-has-no-read-only-probe/gaps.md`,
  divergence 4).
- A framer run costs about 2.5 USD: 5.196 and 4.812 USD for two runs each in
  #1047's side files (executed).

**The chosen approach's failure scenario.** In six months, a comment lands
between the spawn and the frame's commit. The spawn's line said "no
comments", and the frame is drawn from a body that is no longer current. The
folding paragraph already covers this case: before the frame is committed,
the orchestrator folds the decision into the body, and after the commit, into
the frame. The line records what was true when it was read, and its date
says when. A second failure: a model update makes framers under the old
definition probe a generator too. Then a later old-side run of the new case
reads green, and the case stops showing the difference it showed here. A
behaviour case can only show a difference that holds on the model it ran on.
The side files record the model and the date.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Give the runner a way to read comments: a stub `gh` in `noninferiority.py#write_git_shim`, or `gh` authenticated in the runner | The framer still starts from the body alone and fetches the rest itself. A production framer with no `gh` access, or one on a repository with another tracker, asks the same question again. The stub is machinery kept only for the runner, and what it prints is a second copy of the case's issue. | Rejected. The issue puts the cause in the framer's input, and the orchestrator has already read the comments by the time it spawns the framer. |
| A2. Keep the structure: the framer reads the comments itself (step 4 as it reads), and the definition only tells it never to ask about them | Where the framer cannot read them, a comment that carries a decision not yet folded is silently dropped, and the frame is drawn against a request nobody approved. | Rejected as the whole answer. The premise that keeps the framer reading them, that `gh` can read the issue in a production framer's environment, holds (executed: `gh issue view 1158` in this session). So the framer still reads the comments where it can, and the spawn's line covers the case where it cannot. |
| A3. The spawn carries each comment's text verbatim | The spawn grows with every reading a comment holds. A measurement comment, which `docs/issues-and-milestones.md` keeps as a reading and not a decision, sits beside the body as though it were part of the request. Two versions of the request then reach the framer. | Rejected. The body as folded is the request, and the line links the comments for whoever opens them. |
| A4. The orchestrator hands the body as folded and one line on the comments with its command and date. The framer's step 4 cites that duty, carries a line it cannot open into `## Grounding`, and reports a missing line as it reports a missing `routing.md` | See the failure scenario above. | Chosen. |
| A5. A missing line becomes an `a person` row in `frame/questions.md` | The orchestrator answers it from one `gh` call, so a person is the wrong instrument. The row also holds the plan until somebody reads it. | Rejected. The report is where the orchestrator reads it, before it approves the plan. |
| A6. Restore `shape-no-measurement-row` on the sharp-s case, once its spawn carries the comment line | No run on either side of #1047 left a `shout` row, so the grader would pass on the old definition and could not be seen red. | Rejected. Round 1 of #1047 settled this (`trail/rounds/round-1.md:98-116`), and it is not argued again here. |
| A7. A grader that reads a question cell's words, such as one refusing a row that names the generator | It decides from the words a framer chose. #1047's `gaps.md` *Not done* rejected the same grader for `shout`, and `CLAUDE.md` *The rule a mechanism is kept against* calls a reading guessed from words a report. | Rejected. |
| A8. A grader that refuses any row at all in `frame/questions.md` | A framer may open a correct `a person` row, about a spend for example, or a `the work` row, and the grader would refuse it. | Rejected. `shape-no-measurement-row` refuses only the answerer value a probe replaces. |
| A9. A sixth case whose question is a generator's output, with `shape-no-measurement-row` and `shape-answers-by-run` | The old definition may also run the generator, and then side A is not red (`questions.md` Q2). | Chosen. #1047's issue records #971's Q3, a generator-output question, left as `a measurement` under the old definition. The second grader stops a framer that writes no row and gives no answer from passing. |
| A10. Only the sharp-s case's spawn gains the line, through a parameter of `framer_case` | The other four cases then hand the framer a request in a shape the orchestration section no longer allows, and the generator has two spawn shapes to keep. | Rejected. `framer_case` writes one spawn for every framer case, and that spawn models the production one. |
| R1. Paid runs: one run on each side | One old-side run that is not red cannot tell a case that does not separate from one unlucky run. One new-side run reads "no correct row refused" on a single framer. | Rejected. |
| R2. Two runs of the new case on each side, side A first, capped at 15 USD together | About 10 USD. A side with two runs can still miss a rare red, and Q2 holds that outcome. | Chosen. Two is `case.yaml`'s `runs` and the count #1047's S8 was read on. A third run on either side decides nothing the first two do not, because S6 needs one red run and S5 needs every new-side run green. |
| R3. Also run the sharp-s case on the new side, two runs | About 5 USD more. Its prompt gains one line about the comments. Its grader reads `## Grounding`, which that line does not bear on, and the new case's no-row grader already reads a comments row should one appear. | Rejected. |
| R4. The whole framer suite, six cases, two runs on each side | About 60 USD, to re-read graders whose inputs did not change. #947 takes that reading at the end of the milestone. | Rejected. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `evals/scripts/rule_cases.py`: the comment line in `framer_case`'s spawn for every framer case; `MEASUREMENT_ROW` and the `shape-no-measurement-row` grader restored from `7ac24a06`'s diff; the sixth `FRAMER_ISSUES` entry `generated-page`, with its two files added to `base_project`'s and its graders `shape-no-measurement-row` and `shape-answers-by-run`; the docstring's framer line for six issues. `evals/behaviour/framer/` regenerated: five prompts gain the line, and `rule-framer-generated-page/` is new. `tests/evals/test_rule_cases.py` `Test_framer_case`: the S3 and S4 cases | The token `shape-answers-by-run` reads is computed by running the new case's `scaffold.sh` and then `python3 scripts/helpers_page.py` in a directory under the scratchpad, and the command and its output go in the phase record. `python3 evals/scripts/rule_cases.py` regenerates the tree, and `git status --short` then lists only `evals/behaviour/framer/`, the script and the test module. The S3 and S4 cases are seen red against `rule_cases.py` at `0bf22734`. Then `bin/test tests/evals/test_rule_cases.py tests/behaviour/test_evals_layout.py tests/text/test_no_case_tells_the_agent_it_is_evaluated.py tests/github/test_rules.py tests/test_censuses.py -q` in one command | 9b5a28bd |
| 2 | `skills/implement/orchestration.md`: the sentence after the folding paragraph's last sentence, and the acts table row's *Grounds* for *Orchestrator: the order inside a ticket*. `agents/framer.md`: step 4's clause rewritten as `frame/design.md` *Data & interfaces* says, and the `check:` line at `:149` naming `evals/behaviour/framer/rule-framer-generated-page/` | `bin/test` in one command over every module that `git grep -l -e framer.md -e orchestration.md -e '"framer"' -- tests/` lists, `tests/github/test_rules.py` and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` among them. `agents/framer.md`'s byte count before and after, recorded in the phase record for the pull request body | |
| 3 | Side A: `python3 evals/scripts/noninferiority.py run --agent framer --rev c48cd5e3 --suite-rev <phase 2 commit> --case '*rule-framer-generated-page' --runs 2 --max-cost-usd 8 --out <scratchpad>/1793251204-the-framer-is-handed-the-body-without-its-comments/sides/baseline-framer-generated-page.json`. Then side B: the same command with `--rev <phase 2 commit>`, `--max-cost-usd` set to 15 less side A's recorded spend, and `framer-phase-2-generated-page.json`. Each side file is written into `seal/threads/1793251204-the-framer-is-handed-the-body-without-its-comments/evals/` with `run --from-raw`, so the traces stay under the scratchpad. On Q1's default | S6: side A fails `shape-no-measurement-row` on at least one run. The failing row is quoted from that run's trace, from the `Write` and `Edit` inputs for `frame/questions.md`, and it asks the generator question. Q2's default applies where it does not. S5: side B passes both graders on both runs. S7: every side B failure of `shape-no-measurement-row` is quoted with its row and read as `frame/design.md` S7 says. The phase record holds each side's grader results, its spend, `cut_short`, and the model the side file records | |

## Operational impact

None for a deployer. No migration, environment variable or dependency is
added. From this release, the orchestrator's spawn of the framer carries one
more line, and `agents/framer.md` grows by step 4's sentence. The release
table's preload row shows the growth, and the pull request body states the
bytes before and after (`docs/release-checklist.md` *Read the release table
before the merge*). Every framer case's prompt changes. A non-inferiority
baseline for the framer saved before this work's suite therefore reads other
prompts. #947 takes its framer sides with `--suite-rev` at or after this
work's merge. The changelog fragment carries a `### Process changes` row,
because what the framer is handed changes for every later work item.
