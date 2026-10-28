# Phase 4: 1793171931-checks-that-read-text-pass-what-they-cannot-read

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | the commit that adds this file; `frame/plan.md`'s Status cell for phase 4 names it |

## What this phase was asked

Audit family D, readers R32 to R43 of `frame/design.md` *The readers to
audit*, at `c825fd2c`: the citation count and its classification (R34),
whether #956's reader shape is precise enough (R35), R36 under
`questions.md` Q2's default, which is to run `git fetch`, read
`origin/release/v0.24.0` and not wait for #1043, and the R37 measurement
`questions.md` Q4 asks for. The probe lives in the scratch directory as
`test_tmp_*`, runs once and is deleted before the phase closes. No tree file
outside the work item directory changes.

## What this phase found

### R34 first: the probe sees the known miss

The wide resolver below reported
`.github/scripts/gather_changelog.py:43` citing `docs/the-record-layout.md`'s
*A marker counts only on a live line*, which that document does not hold,
before anything was classified (S5). The citation is written with a
possessive, `` `docs/the-record-layout.md`'s *…* ``, and the strict resolver,
which is #956's shape, did not recognise it at all.

### The rows

| Row | Reader | Reads and decides | On input it cannot read | Lets through | Probe | Fix |
|---|---|---|---|---|---|---|
| R32 | the `Reads:` lines #905 names | none stand | `skips`: the reader is gone | `no`: no line is read, and nothing is decided on one | `git grep -c -E '^\s*(#\s*)?Reads:' c825fd2c` outside `seal/`, `changelog/` and `CHANGELOG.md`: exit 1, no output; `git log -S'Reads:'` over the same paths: `af9c924b` (#964) is the last commit that removed a line opening `Reads:`; the two later commits it lists add or drop the word mid-line | none |
| R33 | `tests/behaviour/test_the_set_a_work_item_always_has.py#dangling_implement_citations` and `#cited_files`; the contract-rule resolver of `tests/text/test_the_agent_contract_holds_the_universal_rules.py`; the citation pin of `tests/text/test_broad_gate_rule.py:80-86` | citations in the tree's text files; each case fails on a citation of a heading or rule its target lacks | `skips`: a citation wrapped across a `#` comment marker, split across two string literals or written in bold is not recognised; the contract case reads no file outside `agents/`, `skills/`, `docs/`, `templates/`, `hooks/`, `tests/` and `CONTRIBUTING.md`; the pin fails on any rewording (R38) | `yes`: a dangling citation of `implement` wrapped across a comment marker passes the implement case, and a `contract rule <N>` written in `CLAUDE.md`, `.github/` or `evals/` is read by no case | `*9. No such step*` cited on one line: dangling; wrapped across `#`, split across two strings, in bold: not found; `contract rule 99` in a skill: dangling; wrapped across `#` in a hook: not found; the contract case's file walk holds no `CLAUDE.md`, `.github/` or `evals/` path | #1043 removes the implement case and builds its replacement; the contract resolver's reach is 0.24.1 `test_the_agent_contract_holds_the_universal_rules.py` |
| R34 | each `` `<path>.md` *<section>* `` citation at `c825fd2c`, read by a probe resolver | the tracked text files outside `seal/`, `changelog/` and `CHANGELOG.md` | `skips`: no standing case reads a citation of any file but `implement`'s, so an unresolved one fails nothing | `yes`: the real miss at `gather_changelog.py:43` stands at `c825fd2c` with every case green | the wide resolver recognised 411 citations, 55 unresolved: 1 real miss, `gather_changelog.py:43`; 39 paths relative to a work item (`frame/design.md`, `plan.md`, `gaps.md`), which name no file of the tree; 8 citing a heading or bold rule lead by its opening words or its step number (`*2b*`, `*5*`, `*One act, one owner*`, `*Measure the segment*`); 3 f-strings; 2 URLs; 1 literal a test holds; 1 citation stating that its section is gone. #1043's own read was 22 of 329 with 2 real, and named no command; this resolver reads `.py` comments and wrapped strings that read did not | none: #1043 corrects the citation and builds the case |
| R35 | the reader shape #956 describes: a path immediately followed by an italic heading, read across a line break, with markup inside the heading handled | the same files | `mixed`: it refuses every citation wrapped across a `#` comment marker or split across string literals, and it does not recognise a possessive path or the `implement` skill's form | `yes`: the shape is blind to the one real miss, which is written with a possessive, so a case built to it passes `gather_changelog.py:43` | 388 citations recognised, 59 unresolved; at least 13 of those resolve once the comment marker or the string split is undone (`hooks/worktree-guard.py:2098` *A. Branch switch*, `chain_check.py:2059` *At the pull request*, and eleven in `tests/text/`); of the 24 citations the implement case recognises, 3 it does not; so it fails both halves of *precise enough* | none: the measurement is an input to #1043's case, and phase 5's R36 issue carries it |
| R36 | #1043's tree-wide citation case | the same files | not landed at `5287dd42`, the tip of `origin/release/v0.24.0` after `git fetch`: three commits since `c825fd2c`, none of them #1043's, and #1043 is open | not landed | `git rev-parse origin/release/v0.24.0`: `5287dd42`; `git log c825fd2c..origin/release/v0.24.0`: #1118, #1119, #1120 | 0.24.1: add R36's row once #1043 lands (`questions.md` Q2's default) |
| R37 | negative pins: an assert that a spelling is absent, as a class, with the three instances `seal/follow-up.md` names | documents and source read as text | `passes`: every spelling but the one literal passes | `yes`: with `gh issue close` planted in `release_completeness_check.py` across a comment, and `gh issue reopen` in `label_merged_on_release_branch.py`, both cases stay green, and a row whose answerer reads "at the next change to" passes the rider guard | Q4's command at `c825fd2c`: 48, 120, 106, 13, 18 and 0, 305 in all; read with `ast` per match, the asserted-against text comes from a file in 123, a run's output in 41, both in 10, and neither word list in 131; each case loaded with a stand-in for pytest's decorators and its `read` handed the planted text: plain spelling red, comment between the words green, for both scripts; "next time" red, "at the next change to" green | #1038: the sorting of 305 asserts across a dozen modules is no one work item's |
| R38 | positive phrase pins on a rule sentence, as a class | documents | `refuses`: a reworded rule turns the case red | `no`: the rewording fails loud; whether each pin stays is #1111's | `test_the_owner_names_the_row_the_phrase_stood_for` with its document's sentence reworded to the same meaning: red | none: #1111 decides each pin |
| R39 | `tests/censuses.py#_exempted`, `#_held`, `#_trailing` | exemption comments a person writes in source | `refuses`: an exemption it cannot read leaves the flagged line flagged, and a misplaced one is named | `no` | `# exempt from splitlines:` with no reason, `# Exempt from ...`, another census's name, and two names: each leaves line 3 flagged; above a blank line: both lines named; ending the line: named | none |
| R40 | the eval graders under `evals/behaviour/<agent>/<case>/graders/`, as `claude plugin eval` and `evals/scripts/noninferiority.py#grade` read them | files and tool calls the agent under test wrote | `mixed`: a `contains` grader fails a near miss of what it looks for; a `not_contains` grader passes every spelling but the one it names; `grade` refuses a `not_contains` grader with ValueError | `yes`: a probe left behind as `tmp_test_x.py`, `test-tmp-x.py` or `Test_tmp_x.py` passes "No probe file is left behind in the fixture" | `grade` with `seeded-279a580b`'s `truth-2`: the path and line in range, and a range opening in range: found; a range opening below it, the file name alone, and `Location:`: not found; the pattern `test_tmp_` through Python's `re` over four leftovers: only `test_tmp_x.py` matched. How `claude plugin eval` reads a `not_contains` grader whose file is absent was not run | #1038, with R37: an absence written as one spelling |
| R41 | `evals/scripts/noninferiority.py#check` | a comparison record `compare` writes and a person may edit | `mixed`: a `cut short` cell it cannot read is cut short, and the record is no result; a header cell whose spacing it cannot read is read as 0 | `limit`: a record whose numbers give `fail` passes once its verdict line is edited to `pass` and its `New false rows` cell is spaced `\|8\|`; `compare` writes the cells, and the one-issue flow edits none | records from `render`: passing, exit 0; failing, exit 1; failing with its verdict edited to `pass`, exit 1; the same with the cell spaced off, exit 0; `New cut short` reading `No`, exit 1, no result | 0.24.1 limits |
| R42 | `evals/scripts/replay_targets.py#labelled_round`, `#findings`, `#confirmed` | round records, read to make the replay cases' truths | `skips`: a record the check of its commit refuses gives no finding, and a `confirms:` line it cannot read confirms nothing | `no`: a truth it cannot read leaves a case with fewer truths, which measures less and passes nothing the case would have failed | `labelled_round` on a record with `Verdict:` capitalised: refused at line 12; `confirmed` with `confirms: round-1#1`: `{1}`; with `Confirms:` and with `round-1 #1`: nothing | none |
| R43 | `chain_check.py` and `seal_stamp.py`, and every other pair phases 1 to 4 found that read one line with two readers | the line both read | `mixed`: R4 and R5 disagree on a fence nobody closed; every other pair reads through one function and agrees | `yes`: R5's probe, the stamp queued for a guarantee the pull request's arm refuses | R5's probe in `trail/phases/phase-1.md`, R28's twelve bodies in `trail/phases/phase-3.md`, and the pairs each phase record lists | 0.24.1 `seal_stamp.py`, with R5 |

### Pairs for R43, from every phase

- Disagree: R4 and R5 on a fence nobody closed (phase 1).
- Agree through one function: the round record's grammar for R3, `pr_body`
  and R42 (`round_of`); `routing.parse` for the edit gate, the question gate
  and the pull request check; `config_value` for the mode gate, `seal gate`
  and `seal fold`, by kind; `pact_declaration` for `chain_check.py` and
  `seal pact`; `tokens.given` for the guard and the consent writer; the
  closing keyword for R26, R27, the closer and `pr_body` (R28); `check_text`
  for R13 and R31.

### What the frame said that the probe answers

- R32: the frame's claim holds; `af9c924b` removed the last line opening
  `Reads:`.
- R33: the frame names the implement case's floor of ten recognised
  citations. The floor stands, and the probe shows what it cannot see.
- Q4: R37 now carries 305 with the split above in place of the upper bound.
  The word lists are the probe's own heuristic, and 131 matches fit neither,
  so the count of asserts reading a tracked file is between 123 and 264.

### The probe

`TMPDIR=<scratch>/c956 python3 -I <scratch>/c956/test_tmp_4.py > <scratch>/c956/out4.txt 2>&1; echo "exit $?"`
printed `exit 0`. It read every file at `c825fd2c` through `git show`, ran
the readers by path, and called four test cases directly after loading
their modules with a stand-in module for `pytest` that returns each
decorated function unchanged; `tests/conftest.py`'s temporary folders went
under the scratch directory through `TMPDIR` and were removed at exit. The
file, its output and the folder it made were deleted by their recorded paths
before this record was committed.

### Q3

No row of this family reaches either situation `SECURITY.md` names: each
reads the repository's own tests, documents and eval cases.
