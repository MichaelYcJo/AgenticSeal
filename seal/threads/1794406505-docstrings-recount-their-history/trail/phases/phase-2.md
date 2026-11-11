# Phase 2: 1794406505-docstrings-recount-their-history

## What this phase found

**The count falls by 142 lines, and only prose changed.** The phase is two
commits, one per file: `963b9227f` rewrites
`skills/verify/scripts/broad_gate.py` and `ead171191` rewrites
`skills/code-review/scripts/chain_check.py`. The counting command of design
*Data & interfaces*, taken from that file into the phase's scratch directory
and run with `python3 -I`, printed `{'files': 50, 'lines': 33407, 'blank':
2776, 'prose': 13132, 'code': 17499, 'hits': 755}` at `c89224c96`, and its
`--hits` listing held 154 lines of the two files, the figure design *Scope*
item 3 gives. At `ead171191` it prints `{'files': 50, 'lines': 33379,
'blank': 2776, 'prose': 13104, 'code': 17499, 'hits': 613}`, and 12 of those
lines are `broad_gate.py`'s; `chain_check.py` holds none (executed). The
code command over design S1's pathspecs, `c89224c96..ead171191` with `lib
hooks .github/scripts skills`, printed `2 .py files differ in text; code
differs in: none` and exited 0, and so did the same range with no pathspec
(executed). The phase changed no test file, so S1 and `frame/plan.md`
*Phases*' allowance for a pinning case did not meet here.

**The frame holds against the tree for this phase.** Neither file is one
#1489's branch edits: `git diff 38123f839...origin/test/1489-test-files-declare-no-target`
over the two paths printed nothing, and `origin/release/v0.37.4` still
stands at `38123f839` (executed). `broad_gate.py`'s module docstring keeps
the paragraph that carries both `origin/<base>` and `upstream`, which design
G9's first case reads, and that case passed (executed, below). No frame
statement is contradicted at HEAD by this phase.

**Every docstring and comment of both files was read, not only the hit
lines.** Each file was read whole, start to end, and each sentence was
judged by design *Scope* item 1. Sentences outside the hit listing went or
were rewritten where they recount: coordinates into other work items'
records, such as a section of their `frame/design.md` or `plan.md`, row W1
of a `questions.md`, the `trail/phases/phase-1.md` of 1791270161 and
1791384158, and alternatives A4 and A9; review rounds and findings with no
issue number beside them; and "was", "used to", "until", "since",
"before this existed", "again" and "the last time" where they set the
present against a former state. Where a removed coordinate or round was
the only place a reason was said, the reason was restated in the present
tense in the same docstring or comment: `branch_name` says why the line
names the branch, `a_runner_could_hold` says why git is asked rather than
a pattern, `missing_row` says why the message names no command, `quote`
says why the platform is an argument, and the comment over the reactive
base comparison says why the gate records rather than infers.

**The 12 hit lines that stay, each with its keep class.** Every one is in
`broad_gate.py` at `ead171191`.

| Line | Class | Why it stays |
|---|---|---|
| 56, 1499, 1500 | K2 | "no run measured it", "not measured": the `new?` words the gate prints for a file the base run did not measure |
| 279, 364 | K2 | "measured by the copy", "the copy that measured the tree": the gate copy that runs the arms now |
| 494 | K2 | "what they are measured against": the ahead and behind counts `moved_line` prints |
| 1176 | K2 | "a measured run": a run the gate hands its recorder |
| 1502 | K2 | "the measured word": `EARNS_THE_WORD`, which the gate prints |
| 1552 | K2 | "`new` is not measured": why `UNPLACED_AT_BASE` replaces `new` |
| 1323 | K3 | the pytest versions (6.1, 7.0, 9.1, pytest-xdist 3.8) the exits of `RAN_TO_ITS_END` were measured on, with their issue and record coordinate removed |
| 1890 | K4 | the owner's design of the panel's ticks and blank row, its issue (#832) as the one coordinate; the date of the decision and the record coordinate went |
| 1908 | K4 | the owner's choice of continuation rows over a wider stamp, its issue (#666) as the one coordinate; the `questions.md` row went |

**Sentences no class fitted cleanly, and what each became.** Each took
`frame/questions.md` Q1's default and was kept, rewritten in the present
tense.

- `gate_copy`'s docstring said the `gate` row printed on every stamp from
  0.15.1 and told nobody anything. It now says a row printed on every run
  would read `tree <version>` every time in this repository, which is the
  reason the row prints only where the copies differ. Its closing "the
  *carries no information* case the owner named" gave no coordinate for
  the owner's decision, so the reason stays and the attribution went: K4
  keeps an owner's decision with its issue, and there was none to keep.
- `panel`'s docstring said two rows "left with #666" and how `from` and
  `row` were folded away. The rows that do not exist are no part of the
  present panel, so that history went. Its last clause, why no row says
  `lint`, is a present reason and stays as its own paragraph.
- `missing_row`'s docstring told how a session met the old message and
  chose a command itself (#401). The issue went and the observation stays,
  as K3's evidence a branch rests on: it is why the message names no
  command.
- The comment over a `trail/gate.md` with no run block and the one over a
  `guarantee.md` with no verdict block said "one written before the run
  stood in a block (#1198, *Scope* item 9)". Read as K5, each now names the
  older shape the arm still meets, a field written outside any block, in
  place of the issue and the record coordinate.
- `root_name`'s docstring said a committed `seal/` with no marker "is read
  as this check read it before the marker decided the root". Read as K5,
  it now says that root is still read under that name.

**What stays outside the rule, by design *Scope* item 1's own line.** The
`--preflight` help text in `broad_gate.py` ends "(#638)", and
`chain_check.py`'s `NO_ROUND_BLOCK`, `NO_RUN_BLOCK` and `NO_VERDICT_BLOCK`
print "since #1198". Each is a string constant a person reads at a terminal,
which design *Scope* Out keeps as it is, so neither changed and neither is
in the count. `broad_gate.py`'s comment over `NO_RECORD_CAUSES` still names
"the module's case A5", which points at a case of
`tests/skills/test_broad_gate.py`; it recounts nothing, so it stays as
written.

**No unit adds behaviour, so no `seal mutate` run is owed.** The edits are
comments and docstrings, the *A comment or docstring inside source* row of
`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*, and no case was written or changed.

**A probe for a pin the phase could have broken found none.** A
`test_tmp_*` probe listed each string constant of the tracked `tests/*.py`
and `evals/*.py` that occurs in either file at `c89224c96` and not at
`ead171191`. Its 185 lines are short tokens a fixture shares with the prose,
such as `proofer`, `rejected` and `design.md`, and one phrase,
`before any check has finished`, which
`tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py`
reads in `templates/setup/config.md` and not in the script (executed: the
probe; read: the listing and that case). A case that reads a script's text
by a regular expression is outside the probe, so the list is a sample; the
boundary run below reads every test file that loads either script.

**S6, S5 and the phase boundary run.** `uvx ruff check` and `uvx ruff
format --check` over `broad_gate.py` at `963b9227f` and over
`chain_check.py` at `ead171191` each exit 0, and each run read the one file
it was given (`All checks passed!`, `1 file already formatted`) (executed).
The phase boundary set ran as one command, `bin/test tests/text
tests/behaviour tests/skills/test_broad_gate.py
tests/skills/test_chain_check.py tests/skills/test_agentic_pytest_record.py
tests/skills/test_seal_stamp.py tests/skills/test_pr_body.py
tests/github/test_release_seal.py tests/lib/test_config.py -q`: 2739
passed, 9 skipped, exit 0 at `ead171191` (executed). The six files beside
the two tree-wide directories are those that import or load either script;
a test file that names a path only in a parameter or a docstring, such as
`tests/skills/test_seal.py`, does not read it and is not in the set. G10's
module, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, and
design G9's first case,
`tests/behaviour/test_the_gate_asks_the_range_ci_will_ask.py#test_the_gates_own_docstring_says_the_base_is_resolved`,
are in it. The two tree-wide directories ran again as one command,
`bin/test tests/text tests/behaviour -q`, over the tree this record is
committed with, since they read the work item's records (executed). One
citation is new: the comment over `broad_gate.py`'s
`__main__` block now points at `skills/verify/scripts/seal_stamp.py#pick_shape`
for why stdout is asked before the streams move to UTF-8, where it said
"`seal_stamp.py` measured why".
