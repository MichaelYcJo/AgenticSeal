# Feature Specification: 1793157214-the-pr-bodys-facts-come-from-the-records

Issue #1044. The orchestrator writes every pull request body by hand, and
most of what it writes restates a record of the work item: what changed,
how it was built, what the review rounds found, what was not verified and
what is left to decide. The sealer reads that body against the records and
the tree, and most of its withheld verdicts were a body sentence that
restated a record and got it wrong. In 0.22.x, 23 of 27 withheld runs named
the body (the issue body, *The record*). In this release, 4 of 5 did (the
issue's comment of 2026-10-28). This work makes one command write the part
of the body the records hold, by copying them, and leaves the orchestrator
to write only what no record holds, under a marked heading. The sealer then
checks that the copied part is the records' text, and reads only the
orchestrator's part.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1044's body, the owner's decision | The three parts of the change: one command writes the factual part of the body from a work item's records; `skills/code-review/orchestration.md` has the orchestrator run it and add its own part under a marked heading; `agents/sealer.md` step 4 reads only the hand-written part and the records themselves. Its *Done when* asks for a case that pins the output on a fixture item |
| `CLAUDE.md` *The goal a design is chosen against* | The run is unattended. What only the owner can decide is a row of `questions.md` with a default, and the build proceeds on the default |
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source and every other place links to it. A copy the command makes from a record, checked byte for byte against that record, is not a second source. A sentence the orchestrator writes about a record is one, and that is the defect this work removes. A check gates only a fact it reads, so the sealer's new check compares text and judges no meaning |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading* | The heading that separates the two parts is one constant, read by the generator, the orchestrator and the sealer by one spelling, and cited by its coordinate rather than copied |
| `docs/the-review-record.md` *The guarantee* | The sealer runs after the body is written and compares the parties. This work changes when the body is written and what part of it the sealer reads, stated under `## Rule changes` |
| `docs/the-agent-set.md` *What each party writes, and when* | The sealer catches a body that says what the tree does not. After this work only the orchestrator's part of the body can say that, stated under `## Rule changes` |
| `docs/the-record-layout.md` *seal/threads/<work-item-id>/* and `skills/implement/SKILL.md` *Document layout* | Which record holds which fact: `changelog.md` what ships, `frame/plan.md` the phases, `trail/phases/` the phase records, `trail/rounds/` the review rounds, `trail/gate.md` the broad run, `gaps.md` what was not verified and not done, `frame/questions.md` the decisions |
| `skills/implement/SKILL.md` *The language the records are written in* | The records follow `Record language`; field names and headings a checker reads stay English. The generated part copies the records in their language, and its own headings are constants |
| `skills/commit-pr-convention/SKILL.md` *The language is the repository's* | The body follows `Commit and pull request language`. After this work that row governs the orchestrator's part, and the generated part is the records' text |
| `templates/setup/config.md` *What no row governs* and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#_literal_strings` | Every string a checker matches literally is on the list, derived from the checker's constants. The generator's heading and the record headings it reads join the list by the same derivation |
| `seal.py` module docstring, *Every other command of the plugin is a subcommand of this one* | The command is `seal pr-body`, one `TOOLS` entry |
| `CONTRIBUTING.md` *The test layout* and `skills/verify/scripts/test_layout.py` | The module's test file is `tests/skills/test_pr_body.py`, with `TARGET`, one `Test_<name>` class per public function, each with a `test_accepts_` and a `test_refuses_` case, and `test_census = census_case(TARGET)` |
| The owner's verification direction, carried from #1051, #1060 and #857 | `plan.md` *Verification this work item owes* |

## Scope

In:

1. **`seal pr-body`, the generator.** A new module,
   `skills/code-review/scripts/pr_body.py`, run as `seal pr-body` through one
   `seal.py#TOOLS` entry. Given a work item's directory and a body file, it
   writes the generated part of the body: the sections under
   *Data & interfaces* below, each one the text of a record, copied, ending
   with the heading `HEADING` holds. Where the body file already exists, it
   rewrites the part above the heading and keeps the part under it byte
   for byte. With `--check` it writes nothing and says whether the part
   above the heading is what the records give.
2. **The orchestrator writes the body with it.**
   `skills/code-review/orchestration.md` *Orchestrator: the pull request
   opens once the sealer seals* has the orchestrator run `seal pr-body`
   after `trail/gate.md` is committed and before the sealer's spawn, then
   write its own part under the heading, and run the command again after
   any repair of a record. Its own part holds only what no record holds.
3. **The sealer checks the generated part and reads only the orchestrator's
   part.** `agents/sealer.md` runs `seal pr-body --check` on the body file
   the prompt names. A part that differs is withheld. Steps 2 and 4 and the
   *Never* list read the body's part under the heading only.
4. **The prose rules for a body name the two parts.**
   `skills/writing-style/outside-the-review.md` *PR 본문에만 해당하는 것*
   applies to the orchestrator's part, and says the generated part is not
   rewritten. `skills/commit-pr-convention/SKILL.md` *Pull request bodies*
   says where the chain section's table and what the rounds found now
   stand, and which language each part is in.
   `templates/setup/config.md` *Commit and pull request language* says the
   row governs the orchestrator's part of the body.
5. **The literals join the no-row list.** `templates/setup/config.md`
   *What no row governs* holds `HEADING` and the record headings the
   generator reads, and the test that derives the list from the checkers'
   constants derives these from the generator's.
6. **The readers that name the body.** `README.md` and `README.ko.md`, the
   sealer's row; `skills/implement/orchestration.md` *Orchestrator: which of
   these acts runs itself*, the Grounds of the row for *the pull request
   opens once the sealer seals*; and every test that pins a sentence this
   work rewrites.
7. **The sealer's eval fixtures.** `evals/scripts/rule_cases.py` writes each
   sealer case's pull request body in the new shape: the generated part
   from the fixture's own records, then the heading, then the hand-written
   part, which keeps the untrue-body case's untrue sentence. The five
   `scaffold.sh` files are regenerated from it.
8. The changelog fragment of this work item.

Out, and why:

- **The broad run's printed figures in a record.** `trail/gate.md` holds
  one `Broad gate` row, the commit and the base
  (`skills/verify/scripts/broad_gate.py`, docstring, `--record`). The
  suite's counts and the chain check's exit are printed and not recorded,
  so the generated part copies the row and the orchestrator's part states
  the figures. Recording them would change the gate record's grammar and
  `chain_check.py#broad_gate`'s reader, which the issue does not ask for.
- **A check of the body on GitHub.** The pull request opens with the file
  the sealer checked (`gh pr create --body-file <that file>`). A body edited
  on GitHub afterwards is outside the one-issue flow. No CI arm reads it;
  that is a limit sentence in the module's docstring, not a guard.
- **The body of a settle or release pull request.** Neither is a work item
  with a thread (`skills/settle/SKILL.md` *A settle is not a work item*;
  `docs/release-checklist.md`).
- **The title.** It stays the orchestrator's, under
  `skills/commit-pr-convention/SKILL.md` *Pull request titles*. The release
  notes read titles, and nothing about a title changes.
- **The issue's third *Done when* item**, the withholds over the body
  counted across the next three work items and posted on #1044. It is a
  measurement after this work ships. `questions.md` Q2 holds what that
  means for the `Closes` line.
- **A translated generated part.** Translating the records into the body's
  language is a summary by another name, which is the defect this work
  removes. Where the two language rows differ, the generated part is in
  `Record language`, as the records are.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The generated part is the records' text | Given a fixture work item holding `changelog.md`, `frame/plan.md`, two phase records, two round records (one with a finding whose `answer:` paragraph runs over two lines, one with no finding), `trail/gate.md`, `gaps.md` and `frame/questions.md`, one of them with a line in Korean, when `compose` runs, then its text equals the expected text, written out in the test, section for section as *Data & interfaces* lays it out, and it ends with the heading line | `tests/skills/test_pr_body.py` `Test_compose`, an accepting case |
| S2 Nothing in the generated part is the generator's own claim | Given the same fixture, when `compose` runs, then every line of its text is either a line of one of the records (a finding's heading demoted as *Data & interfaces* says) or a line `FIXED` gives, with the work item's name or a record's path filled in, so no count, summary or rewording can appear | `tests/skills/test_pr_body.py` `Test_compose`, a second accepting case that checks each output line against the records and `FIXED` |
| S3 Every round is listed, in number order | Given round records `round-1.md` to `round-10.md`, when `compose` runs, then each appears once, `round-2.md` before `round-10.md`, and no line states how many there are | `tests/skills/test_pr_body.py` `Test_compose`. This is the class of #1051's first withheld body, which counted four rounds where five records stood |
| S4 Every question row is copied | Given a `frame/questions.md` holding one `open` row and one answered row, when `compose` runs, then both rows are in the generated part with their `Status` cells as written | `tests/skills/test_pr_body.py` `Test_compose`. This is the class of #1060's and #857's withheld bodies, each of which left an `open` row out of *Decisions left* |
| S5 A missing record is named, not skipped | Given a work item with no `frame/plan.md`, no `trail/rounds/` and no `frame/questions.md`, when `compose` runs, then each of those sections holds its fixed sentence naming the absent record | `tests/skills/test_pr_body.py` `Test_compose` |
| S6 A record the generator cannot copy faithfully is refused | Given a round record `chain_check.py` refuses, or a record holding a line equal to `HEADING`, when `compose` runs, then it raises `Refused` naming the record's path and line, and the command exits 1 and writes nothing | `tests/skills/test_pr_body.py` `Test_compose` and `Test_main`, refusing cases |
| S7 The two parts split at one line | Given a body, when `split` reads it, then the generated part is everything before the first line equal to `HEADING` and the orchestrator's part everything after that line; a body with no such line is refused | `tests/skills/test_pr_body.py` `Test_split` |
| S8 Writing keeps the orchestrator's part | Given a body file whose generated part is stale and whose part under the heading holds the orchestrator's text, when `seal pr-body <item> --body <file>` runs, then the part above the heading is the records' text and the part under it is unchanged byte for byte; given no file, it writes the generated part alone; given a file with no heading, it refuses and writes nothing | `tests/skills/test_pr_body.py` `Test_main` |
| S9 The check refuses an edited copy | Given the file S8 wrote, when `seal pr-body <item> --body <file> --check` runs, then it exits 0 and writes nothing; with one sentence of the copied changelog changed, it exits 1 and names the body's line and the record's line | `tests/skills/test_pr_body.py` `Test_main`. This is the class of #857's withheld item 5, a changelog fact restated wrongly |
| S10 The command is a `seal` subcommand | Given the tree, when `seal pr-body --help` runs, then `pr_body.py`'s parser answers, and the command is classified where every shipped command is | the existing dispatch cases of `tests/skills/test_seal.py`, and `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` with its new row |
| S11 The literals are on the no-row list | Given the generator's constants, when the list in `templates/setup/config.md` *What no row governs* is read, then `HEADING` and each record heading the generator reads appear as items | `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` `_literal_strings`, extended to the generator's constants |
| S12 The orchestrator generates the body after the broad run's record | Given `skills/code-review/orchestration.md`, when its section on opening the pull request is read, then it runs `seal pr-body` after `trail/gate.md` is committed, writes its own part under the heading, runs the command again after a repair of a record, and says its part restates no record | `tests/text/test_the_rules_have_one_owner.py`, the pin on the body file rewritten, each pinned sentence seen red by deleting it |
| S13 The sealer checks the copy and reads only the orchestrator's part | Given `agents/sealer.md`, when its order of work is read, then a step runs `seal pr-body --check` on the body file and withholds on any exit but 0, and steps 2 and 4 and the *Never* list read the body's part under the heading | `tests/behaviour/test_the_sealer_guarantees.py`, a new case, each pinned sentence seen red by deleting it |
| S14 The sealer's eval fixtures carry a body in the new shape | Given `evals/scripts/rule_cases.py`, when it writes the sealer cases, then each case's `pr-body.md` holds the generated part of its fixture's records, the heading, and the hand-written part; the untrue-body case's untrue sentence stands in the hand-written part | `tests/evals/test_rule_cases.py`, a new case; `tests/behaviour/test_evals_layout.py`'s equality of the committed cases with the generator's output |

## Data & interfaces

**The command.**

```
seal pr-body <item> --body <file>           write the generated part
seal pr-body <item> --body <file> --check   say whether it is the records'
```

`<item>` is the work item's directory, as `seal gate --record` takes it.
`<file>` is the body file, which the orchestrator keeps outside the tree, at
`<scratchpad>/<work-item-id>/pr-body.md`. Exit codes: 0, written, or under
`--check` the part above the heading is what the records give; 1, refused
and nothing written, each cause on a line that opens with `refused:` naming
the file and line; 2, the arguments are unusable, `<item>` is not a
directory, or a module the command loads will not load.

**`pr_body.py`'s public names.**

| Name | What it is |
|---|---|
| `HEADING` | `"## Not from the records"`, the line that ends the generated part and opens the orchestrator's part. `questions.md` Q3 holds its spelling |
| `FIXED` | every fixed line the generated part can hold, so S2 can read them |
| `Refused` | the exception every refusal raises, with its sentence |
| `read_item(item)` | the records' texts by their path under the work item's directory, read with universal newlines and `utf-8` |
| `compose(name, texts)` | the generated part for the work item called `name`, from `read_item`'s mapping, ending with `HEADING` and one blank line |
| `split(body)` | `(generated, own)`: the text before the first line equal to `HEADING`, and the text after that line. `Refused` where no line equals it |
| `main(argv)` | the command |

**How the records are read.** Round records are read through
`skills/code-review/scripts/chain_check.py`'s grammar, the one reader of a
round record, loaded by path as `chain_check.py` loads its own readers: the
`target:` line, the `## Findings` section and its `### <n>.` findings, and
each finding's labelled lines. A round record that reader refuses is
refused here with its sentence. Headings in the other records are found
through `skills/verify/scripts/unverified_check.py`'s `readable` and
`headings`, so a heading inside a fence is no heading. `gaps.md`'s
`## Not verified` heading is that module's `HEADING`. The generator copies
the original lines, never the reader's blanked ones.

**The generated part, in order.** Each section opens with its `##`
heading and one fixed line naming its source, then the copied text. A
blank line separates every block. One kind of copied line changes level:
a finding's `### <n>. <symptom>` heading is written `#### <n>. <symptom>`,
because it stands under its round's `###` heading. Every other copied line
is written as the record holds it. In the block below, a line in angle
brackets says what is copied there, and a line beginning `(repeated` says
which lines repeat.

```
Copied from the records in `seal/threads/<name>/` by `seal pr-body`.

## What changed

From `changelog.md`.

<every line of changelog.md>

## How it was built

From `frame/plan.md`, its *Phases* section.

<the lines of plan.md's `## Phases` section, its heading left out>

The phase records:

- `trail/phases/phase-<N>.md`
(repeated: one bullet for each phase record, in the order of N)

## Review rounds

### `trail/rounds/round-<N>.md`
(repeated: one section for each round record, in the order of N)

<its `target:` line>

<the lines of its `## Findings` section before the first `### ` heading>

#### <n>. <symptom>
(repeated: one block for each finding, in the record's order)

<its `severity:` line>

<its `verdict:` line>

<its `regression:` or `reopens:` line, where it has one>

<its `answer:` paragraph: the `answer:` line and the lines after it up to the first blank line>

## Broad gate

From `trail/gate.md`.

<the lines of trail/gate.md from its first table line to its end>

## Not verified

From `gaps.md`.

<the lines of gaps.md's `## Not verified` section, its heading left out>

## Not done

From `gaps.md`.

<the lines of gaps.md's `## Not done` section, its heading left out>

## Questions

From `frame/questions.md`.

<every table line of frame/questions.md, in order>

## Not from the records
```

N is the positive integer in a file named `phase-<N>.md` or `round-<N>.md`,
compared as a number. A file of `trail/phases/` or `trail/rounds/` named
any other way is not copied. A table line is a line outside a fence whose
first character is `|`. Blank lines at either end of a copied block are
dropped, and nothing inside it is changed.

**The fixed lines for a missing record**, one per section, each naming the
path: `` `changelog.md` is not in this work item. ``,
`` `frame/plan.md` is not in this work item. ``,
`` `trail/phases/` holds no phase record. ``,
`` `trail/rounds/` holds no round record. ``,
`` `trail/gate.md` is not in this work item. ``,
`` `gaps.md` is not in this work item. ``,
`` `gaps.md` has no `## Not verified` section. ``,
`` `gaps.md` has no `## Not done` section. ``,
`` `frame/questions.md` is not in this work item. `` and
`` `frame/questions.md` holds no table line. ``. They are in `FIXED`.

**The orchestrator's part** is everything under the heading, to the end of
the file; `questions.md` Q1 holds the order of the two parts, and Q5 the
count line this layout leaves out. It holds what no record holds: the motivation, a note to
reviewers, a before-and-after table, the `Closes` or `Part of` line, the
broad run's printed figures, a CI run after the rounds, the chain
section's comparison table, and the attribution line. Where it needs a
record's fact, it names the record's path and does not restate it.

**The language.** The generated part copies each record as written, in
`Record language`. Its headings and fixed lines are constants and stay
English, as every heading a checker reads does. Where
`Commit and pull request language` names another language, it governs the
orchestrator's part.

**Limits, stated in the module's docstring, not guarded.**

- GitHub refuses a pull request body over its length limit, and
  `gh pr create` prints the refusal. No guard repeats it. The largest
  thread of this session, #1051's at `4420ebd5` with seven round records,
  measured 33,560 bytes of copied text (executed, by the framer: `wc -c`
  over its `changelog.md` 5,785, the span of its `gaps.md` from
  `## Not verified` to `## Fed back into the spec` 1,280, its whole
  `frame/questions.md` 5,280, its plan's *Phases* section 4,270, and its
  rounds' `target:`, `###`, `severity:`, `verdict:` and `answer:` lines
  16,945). The questions figure is the whole file, more than its table
  lines; the rounds figure leaves out the lines that continue an answer.
- In local mode the records sit under the git directory, so a reader of
  the pull request cannot open the paths the generated part names. The
  copied text still stands in the body.
- A body edited on GitHub after it opens is read by nobody.

## Rule changes

- change
  file: docs/the-review-record.md
  section: The guarantee
  from: It runs after the pull request body and the
    changelog fragment are written and the orchestrator's broad run has written
    `trail/gate.md`, on both routing answers;
  to: It runs after the changelog fragment is written, the orchestrator's
    broad run has written `trail/gate.md`, and the pull request body is
    written from the records, on both routing answers;
- add
  file: docs/the-review-record.md
  section: The guarantee
  to: **The pull request body's facts are the records' own text, and the
    sealer reads only the part the orchestrator writes.** `seal pr-body`
    writes the part of the body above the heading that
    `skills/code-review/scripts/pr_body.py#HEADING` holds, copied from the
    work item's records, and the orchestrator writes under that heading only
    what no record holds. The sealer runs `seal pr-body --check` on the body
    file before it compares the parties, and withholds where the part above
    the heading is not what the records give. That part then gives it
    nothing to compare: the records it copies are what the sealer audits.
    Before this rule, most withheld verdicts were a sentence of a
    hand-written body that restated a record and got it wrong (#1044).
    check: tests/skills/test_pr_body.py tests/behaviour/test_the_sealer_guarantees.py
- change
  file: docs/the-agent-set.md
  section: What each party writes, and when
  from: The
    sealer's reference is the issue body and the tree, so a pull request body, a
    phase record or a review verdict that says what the tree does not is caught
    by a party that wrote none of them.
  to: The
    sealer's reference is the issue body and the tree, so the orchestrator's
    part of a pull request body, a phase record or a review verdict that says
    what the tree does not is caught by a party that wrote none of them.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The sealer's reading of the whole body as a party | `agents/sealer.md` *Order of work*, steps 2 and 4, and *Never*, the clause `the pull request body's list of changes` | The part under `HEADING`, read as a party; the part above it, checked by `seal pr-body --check` |
| The orchestrator writing the body before the preflight | `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the sentence `You take them once you have written the pull request body to a file` | Rewritten in place: the body is written by `seal pr-body` after `trail/gate.md` is committed, because its generated part copies that record |
| The chain section's order, table first | `skills/commit-pr-convention/SKILL.md` *Pull request bodies*, the clause `the comparison table first, then what the rounds found`, and its pin in `tests/text/test_the_chain_section_has_one_shape.py#test_the_section_states_the_chain_sections_shape` | Rewritten in place: what the rounds found is the generated *Review rounds* section, and the comparison table opens the orchestrator's part. The pin moves to the new sentence |
| The rule that every verified thing goes in the body's own table | `skills/writing-style/outside-the-review.md` *검증한 것을 표로 남긴다* | Rewritten in place for the orchestrator's part: what the records hold is copied above the heading, and the table holds what no record does |
| The stored count of subcommands | `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py#test_the_enumeration_is_not_empty`, the `== 13` | The equality `len(SUBCOMMANDS) == len(SEAL.TOOLS)` stays; a stored count is a number kept beside the tree to stay in step with it (`CLAUDE.md` *The rule a mechanism is kept against*) |
| The sealer fixtures' hand-written body | `evals/scripts/rule_cases.py#PR_BODY` | The generated part of each fixture's records, then `HEADING`, then a hand-written part holding `Closes #101.` and, in the untrue-body case, its untrue sentence |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-28 by framer, before the build.
