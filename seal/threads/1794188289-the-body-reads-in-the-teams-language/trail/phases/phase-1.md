# Phase 1: 1794188289-the-body-reads-in-the-teams-language

## What this phase found

**The frame holds for this phase, with two statements the tree
contradicts.** `b0c63c8c` differs from `28fe66be`, the commit the frame
read, only by the three frame files (executed: `git diff --stat 28fe66be
b0c63c8c`). The issue's comment is the owner's decision as G1 states it
(executed: `gh issue view 1453 --comments`). Two statements did not hold at
`28fe66be`:

- `frame/design.md` G7, *Scope* item 5 and the *Removes* row on
  `skills/config/SKILL.md` place the sentence "Every row but `Mode` and
  `Broad gate` has a default" in *Procedure* step 1. It stood in the
  skill's opening paragraph, above *Where the file is*. Step 1 held the
  paragraph opening "Every way of not naming a language lands on English".
  The phase rewrote both places (read).
- `frame/design.md` G8 and *Scope* item 1 say `/agentic:config` step 3 adds
  a language row as a row alone. Step 3 told a session to copy a missing
  language row "with its `## Broad gate` section ... rather than writing a
  bare row" (read). The phase built item 1 as the frame states it, and
  rewrote step 3 in `6bc1b75f` so that a missing language row is added as a
  row alone and the `Broad gate` section is copied for the `Broad gate` row
  only. Judged against `frame/design.md` G9: the stub's comment already
  names `templates/setup/config.md` as the documentation of every row.

**Departures: statements of the old rule that `## Removes` did not name,
each rewritten in this phase.** Each one stated a fact the phase changed,
so leaving it would have left two answers in the tree. Judged against
`skills/core/SKILL.md` *The rule a mechanism is kept against*: a change
removes what stood on the old fact in the same commit.

- `templates/setup/config.md`, the paragraph opening **This file is
  optional, and an absent row is not an error, with two exceptions**. It
  now names four exceptions, the two language rows among them, and no
  longer calls the file optional. The case
  `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_the_template_says_the_file_is_optional`
  pinned the word `optional`. It is rewritten as
  `#test_the_template_names_the_rows_an_absent_one_is_refused_for`.
- `templates/setup/config.md`, the *Record language* paragraph opening
  **Independent of the row above**, which gave as its reason that "an
  absent row's default is what every repository got"; and the *Mode*
  sentence "Every other item here falls back to what repositories got
  before the row existed".
- `skills/writing-style/outside-the-review.md`, the paragraph opening
  **리뷰 체인을 거친 작업 항목의 PR 본문은 두 부분이고**. It said the first
  part is `pr.md` and that the orchestrator never translates either part.
  It now names `pr.<lang>.md` as the opening of the first part where the
  rows differ, and keeps the translation in that record, not in the body
  file.
- `skills/code-review/orchestration.md`, the verifying round's `Target`
  row, and `skills/implement/orchestration.md` *Orchestrator: the order
  inside a ticket* step 2. Both list what the orchestrator writes or what a
  round reads, and both now name `pr.<lang>.md`. Neither is a paragraph of
  the section #1452 changes.
- `agents/sealer.md`'s `description`, and the convention's sentence "one
  that says nothing writes English".

**Decision: the unattended default and the batch question cite the
bootstrap rather than restate it.** The first draft of the batch
paragraph in `skills/implement/orchestration.md` repeated the bootstrap's
sentence on the titles. `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
refused the pair at 20 shared words (executed). The batch paragraph now
says the batch asks "as `skills/implement/bootstrap.md` step 1 asks for
them at first setup". The convention's description of `pr.<lang>.md` was
refused against `skills/code-review/orchestration.md` the same way. It now
points at that section, which is the one home of the file's shape. Judged
against `skills/core/SKILL.md` *The rule a mechanism is kept against*: a
fact has one source.

**Decision: the mirror cases read both rows, and the refused name is the
record language's.** Where the rows differ, `pr.<lang>.md` is named for
the commit language, so a file named for the record language holds what
`pr.md` holds and is no mirror. `mirror_to_refuse` now takes the record
language. The new helper `the_mirror(commit, record)` gives the expected
name where the rows differ and `None` where they name one language.
`configured_language` reads either row. `#test_a_korean_row_is_what_flips_the_refused_mirror_name`
is rewritten as `#test_rows_that_differ_name_the_mirror_for_the_commit_language`,
with both directions as parameters. Judged against `frame/design.md`
*Scope* items 4 and 7 and the *Removes* row on that case.

**Seen red.** Before any prose changed, against `b0c63c8c`, the four new
or changed prose cases failed on the line each names (executed):

- `tests/behaviour/test_first_setup_asks_once.py#test_the_broad_command_rides_the_question_that_already_stops_the_session`,
  at line 150, on "four questions";
- `#test_the_one_call_asks_for_the_two_language_rows_with_the_titles_beside_them`,
  at line 174, on `` `Commit and pull request language` ``;
- `tests/behaviour/test_waiver_decided_at_start.py#test_the_batch_asks_for_the_language_rows_and_names_where_a_default_is_recorded`,
  at line 816, on the same row;
- `tests/text/test_the_settings_have_a_front_door.py#test_the_door_gives_a_language_row_no_default`,
  both parameters, at line 67, on the Default cell `English`.

Each then passed after the prose edits (executed).

**Mutation, `seal mutate` over `36c334c7`, 15 mutants, 15 red, 0
survived (executed).**

- `skills/implement/bootstrap.md`: four mutants, run against the two
  bootstrap cases. They were "four" put back to "two", the two row names
  taken out of step 1, the `gh pr list` command taken out, and the bold
  lead **Then the two language rows.** renamed.
- `skills/implement/orchestration.md`: three mutants, run against the
  batch case. They were `routing.md` *Why this way* cut to `routing.md`,
  the `gh pr list` command taken out, and the two row names replaced by
  "the two language rows".
- `skills/config/SKILL.md`: three mutants, run against the door case. Each
  of the two Default cells was put back to `English`, alone. The opening
  sentence was put back to "Every row but `Mode` and `Broad gate` has a
  default" while the cells stayed new, which shows the absence assertion
  red on its own.
- `templates/setup/config.md`: two mutants, run against the template case.
  They were "four exceptions" put back to "two", and "This file is
  optional" put back; the second shows the absence assertion red on its
  own.
- The language module's helpers: three mutants, run against the mirror
  cases. They were `the_mirror` returning the record language's name,
  which is the old rule, its equality test inverted, and
  `configured_language` reading the commit row whatever row it is given.

One call is not mutated. In
`#test_the_existing_mirrors_are_consistent_with_the_rule`,
`mirror_to_refuse(record)` and `mirror_to_refuse(commit)` give the same
name in this repository, whose two rows both read `English`, so that
mutant would be equivalent here. The rows-that-differ case pins what the
helper does with each language.

**Not pinned: `skills/config/SKILL.md` step 3's correction in
`6bc1b75f`.** No case reads that bullet, and the frame asks for none. The
rounds read it.

**For phase 2.**

- Until phase 2 lands, the prose in this phase says `seal pr-body` refuses
  without either row and writes `pr.<lang>.md` above `pr.md`, and
  `skills/code-review/scripts/pr_body.py` at `6bc1b75f` does neither.
  The plan orders the two this way (*Overlap with the release*).
- `lib/config.py`'s module docstring still says "The file is optional, and
  every absent row but two has a default". It is true of the code until
  phase 2's refusal lands, and `gaps.md` *Not done* hands it to phase 2.
- `frame/design.md` G20 says the listing finds ten files under `tests/`
  and ten under `evals/`. The same command at `b0c63c8c` lists eleven and
  eleven; `evals/scripts/rule_cases.py` is one of the eleven (executed).
  At `6bc1b75f` it lists twelve under `tests/`, because a docstring this
  phase wrote names `seal pr-body`. A file that only names the command
  builds no fixture, so phase 2 lists the set again and reads each file.
- `.test_durations` still names
  `test_a_korean_row_is_what_flips_the_refused_mirror_name`. A work item
  does not commit `.test_durations` (`CONTRIBUTING.md`, the paragraph on
  its refresh), so the entry stays.

**Census of the *Removes* sentences this phase rewrites (executed: `git
grep` outside `seal/threads/`).** "links it from the body", "So not under
the git directory", "That folder sits under the root, which is resolved",
"already touches", "keeps a Korean mirror", "keeps an English mirror",
"carrying **two" and "`Mode` and nothing else, so the" each return
nothing. "Every row but `Mode` and `Broad gate` has a default" returns only
the absence assertion of `tests/text/test_the_settings_have_a_front_door.py`.
`test_a_korean_row_is_what_flips` returns only `.test_durations`.

**Phase boundary (executed, exit 0): 3289 passed, 9 skipped.** The one
command was `bin/test tests/text tests/behaviour tests/lib/test_config.py
tests/lib/test_optin.py tests/lib/test_core.py
tests/skills/test_broad_gate.py tests/skills/test_fold_check.py
tests/skills/test_seal.py tests/skills/test_passages.py
tests/skills/test_payload_meter.py tests/github/test_rules.py
tests/evals/test_rule_cases.py tests/skills/test_pact_check.py
tests/skills/test_settle.py -q`. It ran at `6bc1b75f` with this work
item's `gaps.md` written and not yet committed.
`tests/behaviour/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`
needs that file. The files beyond the tree-wide pair are the ones that
read a changed path: this repository's `seal/config.md`, the config
template, the core, an agent definition or a skill this phase changed. The
files that only write those names into a fixture are left out
(`skills/verify/SKILL.md` *Scope: cheap and often, broad and once*). The
suite is unverified; the orchestrator answers it at the broad gate.
