# Phase 3: 1794406505-docstrings-recount-their-history

## What this phase found

**The count falls by 82 lines, and only prose changed.** The phase is two
commits, one per file: `f518317b2` rewrites
`skills/implement/scripts/seal.py` and `4ac403501` rewrites
`skills/settle/scripts/settle.py`. The counting command of design *Data &
interfaces*, taken from that file into the phase's scratch directory and run
with `python3 -I`, printed `{'files': 50, 'lines': 33379, 'blank': 2776,
'prose': 13104, 'code': 17499, 'hits': 613}` at `222da5706`, and its
`--hits` listing held 83 lines of the two files, the figure design *Scope*
item 4 gives. At `4ac403501` it prints `{'files': 50, 'lines': 33346,
'blank': 2776, 'prose': 13071, 'code': 17499, 'hits': 531}`. One of those
lines is `settle.py`'s, and `seal.py` holds none (executed). The code
command over design S1's pathspecs, `222da5706..4ac403501` with `lib hooks
.github/scripts skills`, printed `2 .py files differ in text; code differs
in: none` and exited 0. The same range with no pathspec printed the same
line and exited 0 (executed). The phase changed no test file.

**Two frame statements are wrong about the tree, at the base and at HEAD.**
Neither changes what this phase builds.

- Design G9 says four cases read a script's prose. A fifth does:
  `tests/skills/test_settle.py#test_surveys_docstring_does_not_invite_the_mutation_that_reopens_finding_4`
  reads `settle.py`'s function docstrings through `ast.get_docstring`. It
  requires `survey`'s docstring to hold "does not take its candidates from
  here" and not "the retirement are both derived from", and `apply`'s to
  hold "not taken from `survey`" (read). The case stands at `38123f839`
  too (executed: `git show` of the test file at that commit). G9's own
  command, `git grep -n -E '__doc__|get_docstring|docstring' -- tests evals`,
  lists its line 3685. Both sentences state the present: `apply` reads its
  candidates from the tree again. So this phase left both docstrings as
  they were. The case passed in the boundary run below. The plan's
  *Technical context* constraints and the *Verified by* cell of row 3 do not
  name it.
- Design G13 says no hit line is a `# RIDER:` comment. At `38123f839`,
  `seal.py:1744-1745` are hit lines ("Measured 2026-09-08") inside the
  rider comment that opens at `seal.py:1742`. `grep -c RIDER` over the hit
  listing sees only a comment's first line. This phase took out the date and
  the clause about a round-1 fix pass. The rider's instruction stays as it
  was written: filter the list by common git directory when the function is
  next opened. `gaps.md` *Not done* says why the phase did not do it.

**The two files are not ones #1489 edits.** `git diff
38123f839...test/1489-test-files-declare-no-target` over the two paths
printed nothing. The local branch stands at `edc9ba6e0`; `origin/` holds that
branch only at its routing commit `b9ca37404`. `origin/release/v0.37.4`
still stands at `38123f839` (executed, after a `git fetch`).

**Every docstring and comment of both files was read, not only the hit
lines.** Each file was read whole, start to end, and each sentence was
judged by design *Scope* item 1. The following sentences were outside the
hit listing. Each recounted history, and each went or was rewritten:

- coordinates into work items' records: `frame/design.md` *What the switch
  touches* and *Order, and what a stopped run leaves*, a `questions.md` Q1,
  a work item's `gaps.md`, and "the line the design specifies";
- a first version of the code: "the first cut of this", "a first cut
  branched on `mine is None`", "this ticket's own defect";
- a former state of the code: "Round 1's guard", "Round 3 graded", "used to
  sit inside the `--into` branch", "the one call site left", and
  "`README.md`'s *Shared or local* section carried both directions as two
  shell lines";
- `adding_commits`' "(0.22.4)": the plugin release where the merge shape was
  met, given as the provenance of a present fact.

A removed coordinate was sometimes the only place a reason was said. There
the reason is now stated in the present tense, in the same docstring or
comment. `refusals` names what the switch touches, read from its body. The
key, a submodule under the root, the root, the place it moves to, the index
under it and the config file stand in the order the body checks them.
`plural` keeps why `check()`'s line stays as quoted acceptance text.

**Three statements in these files were wrong about HEAD, and the phase
corrected each one.**

- `porcelain`'s docstring said the switch also stages the workflow file. At
  HEAD `switch`'s docstring leaves `.github/` to `seal pr-checks`. Both
  callers pass the root alone (read: `seal.py#refusals`, `seal.py#switch`).
  The docstring now says PATHS are the root alone.
- The rider over `other_worktrees` named its caller as `mode_switch`. No
  function has that name. The caller is `switch`.
- `hand_over`'s docstring compared it with "a `bin/` wrapper", in the past
  tense, from when each tool had its own wrapper (executed: `git log
  --diff-filter=D -- bin/` lists those wrappers removed at `ab14194b1`). It
  now names `bin/seal`'s `exec` and `bin/seal.cmd`, which stand at HEAD
  (read).

**The hit line that stays, with its keep class.** `settle.py:358` is K1. It
holds "as `... (#7) (#42)` does", a sample of the commit subject
`adding_commits` reads.

**Kept as K3 without their dates.** These sentences keep their evidence
and the tool version they name: CPython 3.12 to 3.14 for `extractall`, git
2.50.1 in `remote_url` and in `remove_workflow`, and the zip sizes behind
`MEMBER_LIMIT`, `ARCHIVE_LIMIT` and `MEMBER_COUNT_LIMIT`. Their dates went,
and so did a CI run id. Both `2.50.1` tokens stay in `seal.py`, so the
`(seal.py, "2.50.1")` exemption of `tests/behaviour/test_release_hygiene.py`
still matches.

**Sentences no class fitted cleanly, and what each became.** Each took
`frame/questions.md` Q1's default. Each was kept, rewritten in the present
tense.

- `write_zip`: "Seven review rounds and the broad gate all ran on macOS and
  none of them could see it" became "A run on macOS alone cannot see that".
  The rounds went. The reason why only the Windows leg can see the race
  stays.
- `git_asked`: "#111 found four call sites doing the second, one of which
  switched off `seal import`'s refusal" became what reading "" as a fact
  costs: a failure read as *no remote* switches off that refusal.
- `EARLIER_WINDOW`'s comment in `settle.py` named five settle pull requests
  by number and the design of the issue that set the window. Read as K3,
  the evidence stays as a count: across five settle pull requests, every
  recurring kind rests on the current release and the two newest removing
  commits. The pull request numbers and the design coordinate went.
- `settle.py`'s marker `<!-- specs/<id> -->`, three times: "the notes
  published before #1139 carry". Read as K5, it is now "the line older
  notes carry". The marker's own shape tells a reader which notes carry it,
  so no release is named.
- The comments that said "Measured 2026-09-03: …" over a guard now state
  what the code does without the guard, in the present conditional. An
  example is "Unguarded, the switch exits 0 and `git status` in the moved
  root dies". The date went. The observation each guard rests on stays.

**No unit adds behaviour, so no `seal mutate` run is owed.** The edits are
comments and docstrings. That is the *A comment or docstring inside source*
row of `skills/verify/SKILL.md` *The narrow command still has to be able to
fail*. No case was written or changed.

**A probe for a pin the phase could have broken found none.** A
`test_tmp_*` probe listed each string constant of four or more characters,
in the tracked `tests/*.py` and `evals/*.py`, that occurs in either file at
`222da5706` and not at `4ac403501`. It listed 204 lines. All are short
tokens a fixture shares with the prose, such as `gaps.md`, `issue`,
`passed`, `Order` and `windows`, or fixture values, such as the
`2026-09-03` date `tests/skills/test_seal.py#Test_zip_stem` hands
`zip_stem` (executed: the probe; read: the listing and that case). A case
that reads a script's text by a regular expression is outside the probe, so
this list is a sample. The boundary run below reads every test file that
loads either script.

**S6, S5 and the phase boundary run.** `uvx ruff check` and `uvx ruff
format --check` exit 0 over `seal.py` at `f518317b2` and over `settle.py`
at `4ac403501`. Each run read the one file it was given (`All checks
passed!`, `1 file already formatted`) (executed). The phase boundary set
ran as one command at `4ac403501`: `bin/test tests/text tests/behaviour
tests/skills/test_seal.py tests/skills/test_settle.py
tests/lib/test_config.py tests/lib/test_tables.py
tests/e2e/teammate/test_teammate_flow.py -q`. It printed 2555 passed, 8
skipped, and exited 0 (executed). The five files beside the two tree-wide
directories load or run either script. G10's module,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, is in the
set, and so is the fifth pin above. The two tree-wide directories ran again
as one command, `bin/test tests/text tests/behaviour -q`, over the tree this
record is committed with, since they read the work item's records
(executed).
