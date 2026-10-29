# Design: 1793251204-the-framer-is-handed-the-body-without-its-comments

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Verification through an automated workflow is the first goal. A framer that receives only the issue's body asks whether comments change it, and that question waits for a party who already read the comments. The orchestrator hands the request whole, so the framer never needs to ask. |
| `docs/issues-and-milestones.md` *An issue is its body and its comments together* (read, `:288-301`) | The body is what answers *what does this ticket now ask for*, and a decision a comment carries is folded into the body in place. The clause's `check:` line reads `none reader: the framer at every frame`. Nothing in the clause says what the framer is handed. This work's `## Rule changes` adds that. |
| `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (read, `:37-47`) | "Before the frame is committed, the orchestrator folds the decision into the issue body instead." Folding the comments before the frame is therefore already the orchestrator's duty. What the orchestrator's spawn tells the framer about the comments is in no sentence. Step 2's opening and the folding paragraph's phrases are pinned by `tests/text/test_the_rules_have_one_owner.py:363-447` (read), so the new sentence goes after "folds the decision into the issue body instead" and leaves step 2 as it reads. |
| `agents/framer.md` *Order of work* step 4 (read, `:69-70`) | "The ticket and its comments" is all the definition says. It names neither what the spawn carries nor what the framer does when it cannot read the comments. No test pins the phrase (executed: `git grep -n -e 'ticket and its comments' -- tests/ evals/ skills/ agents/ docs/` lists only `docs/issues-and-milestones.md:288`, the heading). |
| `agents/framer.md` *Rules*, **What the tree can answer, you answer.** | "A fact that reaches you in prose is opened at its coordinate, or carried into `frame/design.md` labelled as nobody's finding with its answerer named." The orchestrator's line on the comments is such a fact. Where `gh` cannot open it, it goes into `## Grounding` with the orchestrator as its answerer, and it does not become a row. |
| Contract rule 5 and `docs/the-review-record.md` *The handoff* | A fact the orchestrator hands over carries its coordinate or its label. The line on the comments therefore names the command that read them, `gh issue view <N> --json body,comments`, and the date. |
| `seal/threads/1793240966-the-framer-has-no-read-only-probe/trail/phases/phase-3.md` *What this phase found* (read) | In #1047's four paid runs, `shape-no-measurement-row` caught three rows. Each asked whether issue #105's comments change the request, because `gh` could not read them in the runner. "In four runs the grader caught no row about `shout`." |
| `seal/threads/1793240966-the-framer-has-no-read-only-probe/trail/rounds/round-1.md` *Confirmations* (read, `:98-116`) | Round 1 weighed giving the sharp-s case a readable issue thread and restoring the grader there: "No run on either side left a `shout` row, so a restored grader would pass on the old definition and could not be seen red (contract rule 15)." That round settled it, and this frame does not argue it again. The no-row pin therefore needs a question the old definition does leave as a row, so it is a new case, not the sharp-s case. |
| `seal/threads/1793240966-the-framer-has-no-read-only-probe/gaps.md` *Not verified* and `guarantee.md` (read) | The no-row half has "nobody after round 1" as its reader. The owner answered on 2026-10-29 that "the pin of the no-row half is #1158". The row stays in #1047's record. The settle after the release closes it as answered and names this work item's side files (`skills/settle/SKILL.md` *The settling session's procedure*, step 4). |
| `git show 7ac24a06` (executed) | The removed grader was a `regex` over `frame/questions.md` with `match: 'not_contains'`. Its pattern, `MEASUREMENT_ROW` at `7ac24a06^:evals/scripts/rule_cases.py`, finds a table cell whose text opens with the words a measurement, backticked, bold or plain. It reads the `Who can answer` value, which the template fixes, and not a question's words. This work restores that pattern for the new case. |
| Issue #1047's body, *The record* (executed: `gh issue view 1047`) | Across 0.22.x, framers under the old definition left questions about a generator's output as `a measurement` rows. One example is #971's Q3, "whether the generators regenerate the nine proofer cases ... byte for byte". The new case asks a question of that kind. |
| `agents/framer.md` *Rules*, **A question a command answers is answered by running it.** | "a generator's output" is one of the writes that runs under `<scratchpad>/<work-item-id>/frame/`, and the repository's code runs from a `git clone --no-local` there. A framer under this definition can answer the new case's question. A framer at `c48cd5e3` could not run a script without writing outside its three files. |
| Contract rule 15 and rule 18 | A new case is seen red before it is relied on, here on the definition at `c48cd5e3`, the old side #1047 ran. A grader that refuses a correct row is fixed, not worked around. |
| `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py:27-28` (read) | `prompt.md` and `scaffold.sh` refuse words that start with `eval`, `grader`, `judg`, `fixture` or `scenario`. The spawn's new line and the new case's issue use none of them. |
| `evals/scripts/noninferiority.py` (read, `:1-60`, `:612-660`) | `run` takes one `--case GLOB`, `--rev`, `--suite-rev`, `--runs` and `--max-cost-usd`, and it saves every run's trace under `<out>.raw/` before anything reads it. A row's text can therefore be read from the traces after the run, as round 1 of #1047 did. |
| Probe: the issue's comments | executed: `gh issue view 1158 -R MichaelYcJo/AgenticSeal --json body,comments` prints `"comments":[]` on 2026-10-29. The body is the whole request. |
| Probe: the generator reproduces the committed framer cases | executed: in a `git clone --no-local` of the worktree at `0bf22734` under the scratchpad, `PYTHONDONTWRITEBYTECODE=1 python3 evals/scripts/rule_cases.py --out <scratch>/cases` exits 0, and `diff -r <scratch>/cases/framer evals/behaviour/framer` exits 0. |
| Probe: the cost of a framer run | executed: `costUsd` in the two committed side files of #1047 is 5.196 USD (old side) and 4.812 USD (new side), each for two runs of the sharp-s case. That is about 2.5 USD a run. |
| `seal/config.md` (read) | No `Policy root` row, so the policy root is `docs/`. No unsettled design's `## Rule changes` names *An issue is its body and its comments together* (executed: an `awk` over every `seal/threads/*/frame/design.md`). |
| The parallel work items (the spawn prompt, not opened) | #1123 edits `skills/verify/scripts/deferral_check.py`, #1127 a case in `tests/text/`, and #1132 `skills/verify/scripts/pact_check.py`. This work edits none of those paths. |

## Scope

In:

- The orchestrator's duty. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* says that the framer's spawn hands the issue whole. That means the body as folded, and one line naming the comments the issue has (none, or each one's link), with the command that read them and the date.
- What the framer receives. `agents/framer.md` step 4 replaces "The ticket and its comments" with what the spawn hands it, citing the orchestration section rather than restating it. It also says what the framer does when it cannot open the line. Where `gh` cannot open the line here, the framer carries it into `## Grounding` as the orchestrator's finding. Where the spawn gives no such line and `gh` cannot read the comments either, the framer reports that, as it reports a missing `routing.md`. In neither case does it write a row asking whether a comment changes the request.
- The cases hand the request whole. `evals/scripts/rule_cases.py#framer_case` writes the comment line into every framer case's spawn, the sharp-s case's among them, and the six cases are regenerated.
- A sixth framer case, `rule-framer-generated-page`, whose question only running the repository's generator answers. It has two graders of its own. `shape-no-measurement-row` is the removed pattern, restored. `shape-answers-by-run` reads a line of `## Grounding` that holds `executed` and a token only the generator's run prints.
- Paid runs: two runs of the new case on the definition at `c48cd5e3`, then two on this work's definition, capped at 15 USD together (`plan.md` phase 3 and *Alternatives considered*, R1 to R4).
- The policy sentence, as a `## Rule changes` item for the settle.

Out:

- Restoring `shape-no-measurement-row` on the sharp-s case. Round 1 of #1047 settled that it could not be seen red there.
- Re-running the sharp-s case or the other four framer cases. Their prompts gain one line about the comments, and none of their graders reads anything that line bears on (`plan.md` R3). #947 reads the whole suite at the end of the milestone.
- Giving the runner a way to read issue comments, such as a `gh` stub in `noninferiority.py#write_git_shim` (`plan.md` A1).
- Any check over a production spawn prompt. No check reads what the orchestrator writes into a spawn, and the row for *Orchestrator: the order inside a ticket* in the orchestration acts table says so after this work.
- Editing #1047's records. The settle closes its `## Not verified` row.
- The files of #1123, #1127 and #1132.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The orchestrator hands the request whole | Given `skills/implement/orchestration.md` after this work, when the orchestrator spawns the framer, then its prompt holds the issue's body as folded and one line naming the comments with the command that read them and the date | read: the sentence. No check reads a production spawn, and the acts table's row for *Orchestrator: the order inside a ticket* names that limit |
| S2. The framer's definition says what it receives | Given `agents/framer.md` step 4 after this work, when a framer reads it, then it names the issue as the spawn hands it, cites the orchestration section, and says that a line `gh` cannot open goes into `## Grounding` and that a missing line is reported, never a row | read: the step. `bin/test` over every module that reads `agents/framer.md` passes |
| S3. Every framer case hands the issue whole | Given the generator after this work, when it writes the framer cases, then every case's spawn holds the comment line before the issue's body | a new case in `tests/evals/test_rule_cases.py` that reads each framer case's prompt, seen red against `rule_cases.py` at `0bf22734` |
| S4. The new case's graders read what they claim | Given hand-written `frame/questions.md` and `frame/design.md` texts, when each new grader's pattern is applied, then `shape-no-measurement-row` refuses an `a measurement` cell, plain, backticked or bold, and accepts `a person` and `the work` cells and a mention of the words outside a table cell; and `shape-answers-by-run` accepts the token on an `executed` line of `## Grounding` and refuses it elsewhere or unlabelled | new cases in `tests/evals/test_rule_cases.py` `Test_framer_case`, seen red against `rule_cases.py` at `0bf22734` |
| S5. A question a probe answers leaves no row | Given the new case and this work's definition, when the framer frames it, then `frame/questions.md` names no `a measurement` answerer and `## Grounding` holds the generator's token on a line labelled `executed` | phase 3, side B: both graders pass both runs |
| S6. The case is seen red on the definition before #1047 | Given the new case and the definition at `c48cd5e3`, when the framer frames it, then `shape-no-measurement-row` fails at least one of two runs, on a row that asks the generator question | phase 3, side A: the grader's result, and the failing row quoted from the run's trace (the `Write` and `Edit` inputs for `frame/questions.md`). A failure on a row about anything else is not counted as red. `questions.md` Q2 says what the build does when side A is not red |
| S7. No correct row is refused | Given a side B run that fails `shape-no-measurement-row`, when the build reads the row from the trace, then a row no probe could answer in the runner makes the grader wrong (contract rule 18: narrowed or removed, and recorded in `gaps.md`), and a row a probe could answer is a defect of the definition, recorded in `gaps.md` | phase 3's record quotes every failing row and its reading |
| S8. Nothing else that reads a changed path breaks | Given phases 1 and 2, when the modules that read `evals/scripts/rule_cases.py`, `evals/behaviour/framer/`, `agents/framer.md` or `skills/implement/orchestration.md` run, then each passes | `bin/test` over those modules in one command at each phase boundary (contract rule 2) |

## Data & interfaces

- `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*:
  - The paragraph opening **A decision made after the frame is committed is folded** gains one sentence after "folds the decision into the issue body instead (`docs/issues-and-milestones.md` *An issue is its body and its comments together*)." The sentence says that the orchestrator's spawn prompt for the framer holds the issue's body as folded. It also holds one line naming the comments the issue has, none or each one's link, with the command that read them, `gh issue view <N> --json body,comments`, and the date. Every phrase `tests/text/test_the_rules_have_one_owner.py:363-447` reads stays, step 2's opening `2. The framer writes` among them.
  - The acts table's row *Orchestrator: the order inside a ticket*: its *Grounds* cell lists what nothing reads under the steps. A framer spawned with no line on the comments joins "a decision left in an issue comment" there (contract rule 19).
- `agents/framer.md`:
  - Step 4, `:69-70`. "The ticket and its comments" becomes the ticket as the spawn hands it, whole. It cites `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* for what the orchestrator owes and does not restate it. The framer reads the comments with `gh issue view <N> --json body,comments` where `gh` can read the issue in its environment. Where it cannot, the spawn's line goes into `## Grounding` as the orchestrator's finding. Where the spawn has no such line and `gh` cannot read the comments, the report says so. No row asks whether a comment changes the request.
  - *Rules*, **A question a command answers is answered by running it.**: its `check:` line names `evals/behaviour/framer/rule-framer-generated-page/` beside the sharp-s case and the scratch-naming test.
  - The wording does not copy a run of `WINDOW` words from `skills/implement/orchestration.md` (`tests/text/test_no_passage_is_pasted_into_a_second_file.py`).
- `evals/scripts/rule_cases.py`:
  - `framer_case`'s spawn gains the comment line between `{HERE}` and the issue. Along these lines: "Issue #{N} has no comments, so its body is the whole request (executed by the orchestrator on <date>: `gh issue view {N} --json body,comments`). The body reads: {issue}". The date is a constant of the module, so the generator stays deterministic. No word in it starts with a stem `tests/text/test_no_case_tells_the_agent_it_is_evaluated.py` refuses.
  - `MEASUREMENT_ROW` comes back with the pattern `7ac24a06` removed, together with a function that returns the `shape-no-measurement-row` grader for a work item's folder. The sharp-s case does not take it.
  - `FRAMER_ISSUES` gains a sixth entry, slug `generated-page`, item `1790000026-generated-page`, issue #106. `framer_case` takes the files a case adds to `base_project`'s. The new case adds `scripts/helpers_page.py`, a stdlib generator that writes `docs/helpers.md` from the docstrings in `src/textutil.py`, prints nothing, and ends the page with a line no reading of the source gives, such as a `zlib.crc32` digest of what it wrote. It also adds a committed `docs/helpers.md` that the generator would change. The issue asks whether running the generator today changes the page and what the page then reads, without the answer. Along these lines: "`docs/helpers.md` is written by `python3 scripts/helpers_page.py` from the docstrings in `src/textutil.py`. Before we add a helper, the page should be current: say whether running the script today changes it, and what it reads after."
  - The new case's own graders are `shape-no-measurement-row` over `frame/questions.md` and `shape-answers-by-run` over `frame/design.md`. The second has the shape of `PROBE_ANSWER`, with the generator's token where `STRASSE` stands. The build computes the token by running the case's scaffold and the generator under its scratch directory, and records the command in the phase record.
  - The module docstring's framer line says six issues and names what the sixth grades.
- `evals/behaviour/framer/`: all six cases are the generator's output. Five `prompt.md` files gain the comment line. `rule-framer-generated-page/` is new.
- `tests/evals/test_rule_cases.py` `Test_framer_case`: cases for S3 and S4, each docstring opening `Guards #1158`.

## Rule changes

- change
  file: docs/issues-and-milestones.md
  section: An issue is its body and its comments together
  from: Once an item is framed, its frame is what the builder reads, and a
    later decision is folded into the frame instead
    (`skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket*).
  to: The framer is handed the request whole: the body as folded, and the
    orchestrator's line naming the comments the issue has, read with
    `gh issue view` on the day of the spawn. So no framer asks whether a
    comment changes the request. Once an item is framed, its frame is what
    the builder reads, and a later decision is folded into the frame instead
    (`skills/implement/orchestration.md` *Orchestrator: the order inside a
    ticket*).

## Removes

- nothing
  why: The work adds a sentence to the orchestration section, rewrites one clause of the framer's step 4 in place, restores one grader pattern for a new case, and adds a line to the framer cases' spawn. It takes nothing out of the tree.

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
