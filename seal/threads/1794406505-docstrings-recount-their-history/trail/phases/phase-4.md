# Phase 4: 1794406505-docstrings-recount-their-history

## What this phase found

**The count falls by 170 hit lines and 33 prose lines, and only prose
changed.** The phase is 14 commits from `ab61362d3` to `e455a72e8`. Eleven
files were rewritten, one commit each, and three more commits rewrap or
re-tense lines those commits left. The twelfth file of design *Scope* item
5, `skills/settle/scripts/passages.py`, was read whole and needed no edit.
The counting command of design *Data & interfaces*, taken from that file
into the phase's scratch directory and run with `python3 -I`, printed
`{'files': 50, 'lines': 33346, 'blank': 2776, 'prose': 13071, 'code':
17499, 'hits': 531}` at `20c499837`. Its `--hits` listing held 204 lines of
the twelve files there, the figure design *Scope* item 5 gives. At
`e455a72e8` it prints `{'files': 50, 'lines': 33313, 'blank': 2776,
'prose': 13038, 'code': 17499, 'hits': 361}`, and 34 of those hit lines
are in the twelve files (executed). The code command over design S1's
pathspecs, `20c499837..e455a72e8` with `lib hooks .github/scripts skills`,
printed `11 .py files differ in text; code differs in: none` and exited 0.
The same range with no pathspec printed the same line and exited 0
(executed). The phase changed no test file.

**Two frame statements are wrong about the tree, and phase 3's record
already names both.** Neither changes what this phase builds.

- Design G9 lists four cases that read a script's prose. A fifth,
  `tests/skills/test_settle.py#test_surveys_docstring_does_not_invite_the_mutation_that_reopens_finding_4`,
  reads `settle.py`, which this phase does not touch. This phase looked
  for pins with G9's command and the probe below, not with G9's list. The
  two cases on `seal_stamp.py` that plan row 4 names are the only pins on
  this phase's files that the command found (read).
- Design G13 says no hit line is a `# RIDER:` comment, and phase 3 met one
  whose hit lines run over several lines. No `# RIDER:` comment stands in
  this phase's twelve files (executed: `git grep -n RIDER` over them at
  `20c499837`).

**The files are not ones #1489 edits.** `git diff
38123f839...test/1489-test-files-declare-no-target` and the same against
`origin/test/1489-test-files-declare-no-target`, over the eleven changed
paths, printed nothing. `origin/release/v0.37.4` still stands at
`38123f839` (executed, after a `git fetch`).

**Every docstring and comment of the twelve files was read, not only the
hit lines.** Each file was read whole, and each sentence was judged by
design *Scope* item 1. Outside the hit listing, these went or were
rewritten:

- issue numbers given as a present fact's provenance, such as `(#867)`,
  `(#1167)`, `(#1012)`, `(#1452)` and `(#1198)`, and a module docstring's
  opening "Issue #647." or "#641, with #129.";
- review coordinates such as "(round 1, finding 2)", "(round 1 of #647,
  white 9)" and the round-and-severity markers of `mutation_check.py` and
  `seal_stamp.py`;
- coordinates into work items' records: `frame/design.md` sections,
  `questions.md` rows, and `trail/phases/phase-1.md` of work items
  1791270161 and 1791384158;
- dates of measurements, such as "Measured 2026-10-02", "probe D,
  2026-09-28" and "the owner's rule of 2026-10-02";
- former states, such as "used to read as no skills at all", "the label it
  always drew", "every gate before #975 wrote", and `seal_stamp.py`'s
  paragraph on the scale that #853 removed;
- one sentence that pointed a reader elsewhere for the body's layout,
  `pr_body.py`'s "`frame/design.md` *Data & interfaces* of the work item
  that last reshaped this lays out the body line for line". The module
  docstring states that layout itself, so the pointer went whole.

A removed coordinate was sometimes the only place a reason was said. There
the reason is now stated in the present tense, in the same docstring or
comment. A consequence the code prevents is in the conditional: for
example, `fold_check.py#main` now says that without the walk up "the run
would pass having checked nothing".

**Owner decisions kept as K4, each with its issue as the one coordinate.**
Each was checked against the question that recorded it.

- `fold_check.py`: "The owner chose a report over a failure (#953)". Q6 of
  #953's work item was answered by the repository owner, and the date of
  that answer went.
- `seal_stamp.py`: the grid, the open layout, the panel's characters and
  `SEALED`'s red (#832); the little owl and the red wax seal (#1174); a
  seal keeping its disc (#717, Q6 of that work item, answered by the
  owner); continuation rows over a wider panel (#666; the sentence named
  the owner, and its `questions.md` Q1 coordinate became the issue); and
  the record of a refused `sealed` over a limit stated in prose (#976, Q2
  of work item 1792363231, answered (b) by the owner). The label width
  ("the owner's seven"), the rule ("the owner's reference's thirty") and
  the gap ("the owner's three") stand under the layout comment that names
  #832, so they carry no number of their own.

**Decisions that were not the owner's lost their coordinate, and the
reason is now stated in place.**

- `seal_stamp.py#guarantee_rows` lost "`questions.md` Q1's answer (a)" of
  #975. `sealed_before` and `record_refusal` lost "#975 Q8". Both
  questions were answered by the orchestrator under the owner's
  delegation. `sealed_before` and `record_refusal` now state the direction
  Q8 chose: a work item is never stamped twice, and a missed stamp is the
  failure accepted over one drawn twice.
- `payload_meter.py#imports_of` lost "(#1185, `frame/questions.md` Q1)".
  That question was still open and ran on its default. The reason now
  stands in the sentence: the meter follows the docs, so a later Claude
  Code release cannot make it wrong where the docs did not move.
- `mutation_check.py#DEFAULT_TIMEOUT` lost "`questions.md` Q4 of work item
  1790815610". That question was delegated to the build. The grounds it
  held, twice the slowest run (158 s) and a sixth of a 32-minute hang,
  stay in the comment.

**Kept as K3, K2, K1 and K5.** These hit lines remain, and the hits are
their keep classes.

- K3, evidence with the tool version and no date:
  - `seal_stamp.py#MESSAGE_LIMIT`: "Measured on Claude Code 2.1.287", with
    its sizes, now in the present tense. The date and "round 1's fix
    pass" went.
  - The recorder: "Measured on pytest 7.4, 8.0, 8.1 and 9.1" and "measured
    on pytest 6.1, 7.0 and 9.1".
  - `payload_meter.py`: the calibration figures over three measured agents.
  - `passages.py`'s `WINDOW`: "the smallest real copy measured".
  - `rule_changes.py#LITERAL_WORDS`: "the 0.27.1 settle's record names 44
    pins against 26", with the lister's issue and the design coordinate
    removed.
- K2, "measured" for what the code measures now:
  - `mutation_check.py`'s "measured nothing" in six places.
  - `payload_meter.py`'s exit codes, `_shown` and its sibling comment.
  - `seal_stamp.py`'s "measured from the centre", "measured over there",
    "say they measured" and "nothing measured again".
- K1: `seal_stamp.py#wrapped`'s `", #664"`, a sample of a list piece.
- K5:
  - `pact_check.py` keeps "0.23.x", which the printed INLINE refusal also
    names.
  - `pr_body.py` keeps "a body 0.25.0 wrote among them".
  - `seal_stamp.py#read_values` and `#label` keep their older-file branches.
    The sentences now say "an older gate's file" and "the older label", in
    place of "every gate before #975" and "the label it always drew".
  - `seal_stamp.py#_guarantee_read` now says "as one whose fields stand
    outside any block does", in place of "as one written before #1198
    does".

Both `2.1.318` in `payload_meter.py` and `2.1.287` in `seal_stamp.py` stay.
So the two exemptions in `tests/behaviour/test_release_hygiene.py` still
match (executed: `grep -c`).

**Sentences no class fitted cleanly, and what each became.** Each took
`frame/questions.md` Q1's default and was kept, rewritten in the present
tense.

- The recorder's module docstring: "a rule with more branches than three
  review rounds of #825 could enumerate" became "more branches than a copy
  of it here could keep up with". The reason why no path is built from a
  node id stays. The rounds went.
- `seal_stamp.py`'s comment over `REFUSED_DIR`: "which is what #975's rounds
  3 to 6 kept regressing on" became "an ancestry check at read time has
  regressed in each of four review rounds". This is an evidence count
  without the issue.
- `pr_body.py`'s module docstring: "#1044. A body written by hand restated
  the records, and most of the sealer's withheld verdicts were a sentence
  of it that restated one wrongly" became the same claim in the present
  tense, without the issue.
- `deferral_check.py`'s and `unverified_check.py`'s module docstrings each
  told one failure as a story in the past tense. Each now states the
  failure as a case that can happen, in the present tense.
  `unverified_check.py` also lost the coordinate of the work item whose
  memo held the row. "Dozens were open the day it was written" became
  "Many are open at any time".
- `mutation_check.py`'s module docstring held a table of three failures,
  each with its issue. It is now in the present tense with the issues
  removed. The 32-minute hang stays as evidence. "#313 measured it, and the
  case for S5 re-measures it here" became a pointer to the case that
  measures it now,
  `tests/skills/test_mutation_check.py#test_a_run_past_the_bound_is_timed_out_and_leaves_nothing_it_started`
  (read). "a copy on disk is #312" went, and #312 is closed.

**No unit adds behaviour, so no `seal mutate` run is owed.** The edits are
comments and docstrings. That is the *A comment or docstring inside source*
row of `skills/verify/SKILL.md` *The narrow command still has to be able to
fail*. No case was written or changed.

**A probe for a pin the phase could have broken found none.** A
`test_tmp_*` probe listed each string constant of four or more characters,
in the tracked `tests/*.py` and `evals/*.py`, that occurs in a changed
file at `20c499837` and not at `4846bae5b`. It listed 107 entries. All are
short tokens a fixture shares with the prose, such as `frame/design.md`,
`questions.md`, `round` and `windows-latest`. Others are values a test
uses for its own purpose: the test id `"no verdict block"` and the
argument `"--scale"` in `tests/skills/test_seal_stamp.py`, and the date
`2026-10-02` a fixture in `tests/skills/test_settle.py` writes (executed:
the probe; read: each named case). A case that reads a script's text by a
regular expression is outside the probe, so this list is a sample. The
boundary run below reads every test file that names one of the twelve
scripts.

**Line width.** Some Edit calls ended mid-line and joined two lines. That
made lines of 85 to 137 columns. Each was rewrapped before its file's
commit or in a later one (`d61d9800b`, `069e6e9fc`, `e455a72e8`). One
line the range adds is over 79 columns (executed: a scan of `git diff -U0
20c499837 e455a72e8`). It is the 80-column banner `# --- placing one
operation in one document's text ---…` in `rule_changes.py`, where every
banner is 80 columns at `20c499837`. `seal_stamp.py#admitted`'s docstring
is at most 78 columns, which the 79-column case below holds. Three banners
lost a parenthetical, and each kept its file's width at `20c499837`.

**S6, S5 and the phase boundary run.** `uvx ruff check` and `uvx ruff
format --check` exit 0 over the eleven changed files at `e455a72e8` (`All
checks passed!`, `11 files already formatted`) and over `passages.py`
(executed). The phase boundary set ran as one command at `4846bae5b`. It is
`bin/test tests/text tests/behaviour` and the 29 test files outside those
two directories that name one of the twelve scripts. It printed 4710 passed, 9
skipped, and exited 0 (executed). G10's module,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, is in the
set. So are `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`,
whose case needs `` `seal-mark.txt` `` in the stamp's docstring, and
`tests/skills/test_seal_stamp.py`, whose case holds `admitted`'s docstring
to 79 columns. `e455a72e8` changed three prose lines after that run. The
same set ran again as one command over the tree this record is committed
with, since it also reads the work item's records (executed).
