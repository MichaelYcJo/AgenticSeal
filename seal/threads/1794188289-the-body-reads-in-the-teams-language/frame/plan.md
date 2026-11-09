# Implementation Plan: 1794188289-the-body-reads-in-the-teams-language

## Technical context

The tree as read at `28fe66be`. #1452's frame is read at `d949a652` on
`origin/fix/1452-the-body-carries-the-seal-mark`.

The body's composer is `skills/code-review/scripts/pr_body.py`: `read_own`
reads `pr.md` as its bytes stand, `compose` builds the part below `HEADING`,
`split` cuts a body file at the first `HEADING` line, `_check` compares, and
`main` writes or checks. The `Pull request seal mark` row reaches it through
`lib/config.py#declared_value`, the one reader of `config.md`'s table, and the
two language rows reach it the same way. #1452 is moving `main --check`'s
composition and comparison into one function its `body` arm in
`chain_check.py` calls, so this work's change to the first part lands inside
that function and nowhere else.

The orchestrator's side is prose: `skills/implement/bootstrap.md` step 1,
whose one call already carries two questions and whose text already has the
orchestrator add a row to the stub `seal mode` wrote;
`skills/implement/orchestration.md` *Orchestrator: what needs a person is
asked in one batch, before the first edit*, where the two rows become part
of the batch; `skills/code-review/orchestration.md` *Orchestrator: the pull
request opens once the sealer seals*, where `pr.md`'s shape is stated and
`pr.<lang>.md` joins it; `skills/commit-pr-convention/SKILL.md`, whose
*Every way of not naming a language lands on English* and *Pull request
bodies* sections state today's rule; `templates/setup/config.md` and
`skills/config/SKILL.md`, which document the rows to a person; and the two
agent definitions that read the first part, `agents/proofer.md` and
`agents/sealer.md`.

The constraint that shapes the design: a script may read whether a row or a
file is present and may compare two values, and it may not read which
language a text is in (`frame/design.md` G3). So the rows are required, the
translated file is required where they differ, and whether the file renders
`pr.md` is the rounds' and the sealer's judgment.

The failure scenario of the chosen approach, in six months: a repository
whose two rows differ opens a pull request whose `pr.<lang>.md` renders the
quotes loosely or in the wrong order, and no round names it, so a reader of
the team reads a body that says less than the records do. The catch is the
rounds' read of the file against `pr.md`, which the design makes a finding;
if that read keeps missing, the next frame weighs a script comparing the
two files' coordinates, which is exact, against the cost of one more reader.
A second scenario: a downstream repository on an older `hygiene.yml` pin
runs no body arm, so a body sent by hand with the translation left out
passes CI there; `seal pr-body --check` at the sealer stays its catch.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Both rows required: asked in the bootstrap's one call and in the batch before a work item's first edit, written as a default from the recent titles where nobody answers, refused by `seal pr-body` where absent; `pr.<lang>.md` holds the quotes rendered in the commit language and `seal pr-body` places it first where the rows differ (chosen) | *Technical context* states it: a rendering no round reads closely; an older CI pin runs no body arm | chosen: the owner decided the rows are required (design G1); presence is the one fact a script reads exactly here (G3); the file every round reads is the one the body opens with, which is the 0.35 decision kept (G13); #1452's arm passes what the composer places (G14) |
| B. Replacing the structure: no `pr.<lang>.md`; `pr.md` holds each quote followed by its rendering in the commit language, and `seal pr-body` changes only to refuse without the rows | Nothing exact says a rendering exists: where the rows differ and the orchestrator writes the quotes alone, the body opens in the records' language and only a proofer reading the rows against the file catches it, which is the issue's own class of miss. The mirror convention, its tests and the paragraph in three documents would leave for a rule no script holds | rejected. The premise that keeps the structure, that a file's presence can be required by the composer while a line's language cannot, holds at design G3 and G12 |
| C. `pr.md` holds one summary part in the commit language, written by the orchestrator before the first round | The 0.35 record (G13): #1103's subject at `5e5275e5`, the sealer withheld most verdicts over a hand-written body that restated a record wrongly, and #1419 made the first part quotes alone so that no sentence reaches the sealer unread. A summary read by every round still restates, and a wrong restatement in the team's language is the one the team acts on | rejected. The issue's reading-order complaint is answered by the order the orchestrator quotes in, which nothing fixes; a summary returns only by the owner's decision, which this design does not ask for |
| D. Drop the claim that `Commit and pull request language` governs the body; the body is the records' language | The team reads none of the body, which is the issue's second *Done when* item unmet, and the row's name says something false | rejected |
| E. Warn when a row is absent instead of requiring it | The owner's grounds (G1): the first gap went through every party with no warning, and a warning nobody reads does the same | rejected by the owner |
| F. The refusal in `chain_check.py` as an arm that fails a ready pull request whose repository lacks the rows | Reached in CI alone, after the sealer; local mode and the sealer's check read nothing; a second reader of `config.md` beside the one that acts on the rows | rejected: `seal pr-body`'s refusal reaches the sealer, local mode and, through #1452's arm, the pull request |
| G. No script refusal; the orchestrator's rule alone | The issue's record: every party passed two English bodies with no rule broken, because no document said the row was required and nothing read it | rejected: the owner's grounds name presence as the exact fact a script reads |
| H. `seal mode` writes the two rows, or a `seal config` subcommand sets them | `skills/implement/bootstrap.md` says no command does this and none is being added; `skills/config/SKILL.md` *What this does not do* refuses a generic setter for a file people edit by hand (G8, G9) | rejected |
| I. Keep today's placement: the translation is linked from the end of the body | The team reads the link last; under #1452's arm the link line passes only inside `pr.md`, so the hand step stays; the second *Done when* item asks for a body the team reads, not a link to one | rejected |
| J. The script derives the file name from the row, `Korean` to `pr.ko.md` | A table of language names to codes inside a script is a list of spellings (G3); a language the table lacks is refused for its name | rejected: the script lists `pr.*.md` and reads nothing from the name |
| K. The unattended default writes `Record language` as `English` and only the commit row from the titles | The owner's decision writes both rows from the titles (G1); a split default is a second rule for the same moment | rejected: both rows take the titles' language, and the owner overturns it through the quote in `pr.md` |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, 4 in its prose part (every file the item names other than `pr_body.py`), 5 and 6, and the text cases of item 7 | each new text case seen red against the sentence as it stands, then green; `tests/text/test_the_settings_have_a_front_door.py` and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` green in narrow runs; `git grep` for each sentence of `frame/design.md` *Removes* that this phase rewrites finds none | |
| 2 | *Scope* item 3, the `pr_body.py` docstring of item 4, the script cases and the fixtures of item 7, and item 8 | each new case in `tests/skills/test_pr_body.py` seen red against `pr_body.py` as the merged base leaves it, then green; `tests/skills/test_pr_body.py`, `tests/skills/test_chain_check.py`, `tests/behaviour/test_the_sealer_guarantees.py`, `tests/evals/test_rule_cases.py` and `tests/skills/test_seal.py` green in narrow runs; the sealer cases under `evals/behaviour/sealer/` written again from `evals/scripts/rule_cases.py` and `tests/behaviour/test_evals_layout.py` green | |

Phase 2 is spawned after #1452 has landed on the base and the base has been
merged into this branch (*Overlap with the release*). Phase 1 touches no file
#1452's phases write except `skills/code-review/orchestration.md`, where the
two edit different paragraphs of one section, and that merge is the
orchestrator's in the order below.

## Overlap with the release

#1452 is built beside this work, from the frame at `d949a652`.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1452 | `skills/code-review/scripts/pr_body.py`: #1452 moves the composition and the comparison into one function; this work's phase 2 changes what that function composes as the first part and adds the rows' refusal. `tests/skills/test_pr_body.py` and `tests/skills/test_chain_check.py`: #1452 adds cases whose fixtures write a `config.md` with the mark row; this work adds the two language rows to every fixture that runs the command (design G20). `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*: #1452 adds what a red body arm asks; this work rewrites the `pr.md` paragraphs | #1452 | The function #1452 exposes is the structure phase 2 edits, and phase 2's refusal turns every fixture of #1452's arm red until the rows are added, so building phase 2 on the merged base costs one pass over the fixtures. The reverse order costs #1452 a merge of its function over a changed first part and the fixture edits in both items. Phase 1 holds no shared code and is built now |

## Operational impact

No version move: #1443 moved it to 0.36.0. No new dependency.

A repository on this release whose `config.md` lacks either language row
is asked for both at its next work item's start, and `seal pr-body`
refuses until the rows are written; `/agentic:config` writes them at any
time. A commit is never refused. This repository's `seal/config.md` gains
both rows in phase 1 (`frame/design.md` *Scope* item 6), before any pull
request of this branch is ready, so #1452's arm and the sealer read a
repository that declares its languages.

A downstream repository whose `hygiene.yml` is pinned to an earlier release
runs no body arm, as #1452's *Operational impact* states; `seal pr-body`'s
refusals run wherever the installed plugin runs.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
