# Phase 5: 1794406505-docstrings-recount-their-history

## What this phase found

**The count falls by 136 hit lines and 34 prose lines, and only prose
changed.** The phase is 15 commits from `ef9b0a7c1` to `a01158430`, started
at `cc75e05a2`. Each of the 16 files of design *Scope* item 6 was read and
edited, one commit per file, except `rules.py` and `release_report.py`,
which share one commit. The counting command of design *Data &
interfaces*, taken from that file into the phase's scratch directory and
run with `python3 -I`, printed `{'files': 50, 'lines': 33313, 'blank':
2776, 'prose': 13038, 'code': 17499, 'hits': 361}` at `cc75e05a2`. Its
`--hits` listing held 178 lines under `.github/scripts/` there, the figure
design *Scope* item 6 gives. At `a01158430` it prints `{'files': 50,
'lines': 33279, 'blank': 2776, 'prose': 13004, 'code': 17499, 'hits':
225}`, and 42 of those hit lines are under `.github/scripts/` (executed).
The code command over design S1's pathspecs, `cc75e05a2..a01158430` with
`lib hooks .github/scripts skills`, printed `16 .py files differ in text;
code differs in: none` and exited 0. The same range with no pathspec
printed the same line and exited 0 (executed). The phase changed no test
file.

**What the count leaves for phase 6.** 117 of the 225 hit lines are in the
files of design *Scope* item 7, as at the base. The other 108 stand in the
files phases 1 to 5 rewrote. Design S2's threshold of 150 is met when
phase 6 leaves fewer than 42 of its 117 (read: arithmetic over the two
listings).

**The files are not ones #1489 edits.** `git diff
38123f839...test/1489-test-files-declare-no-target` and the same against
`origin/test/1489-test-files-declare-no-target`, over `.github/scripts`,
printed nothing. The local branch stands at `5edd82e59`, and
`origin/release/v0.37.4` still stands at `38123f839` (executed, after a
`git fetch`).

**No case reads the prose of these 16 files.** Pins were looked for by
design G9's method and not taken from its list. `git grep -n -E
'__doc__|get_docstring|getdoc' -- tests evals` names no case on a file
under `.github/scripts/`, and each test file that says "docstring" and
names one of the scripts was read at the line. A `test_tmp_*` probe listed
each string constant of four or more characters, in the tracked
`tests/*.py` and `evals/*.py`, that occurs in a changed file at
`cc75e05a2` and not at `a01158430`. It listed 333 entries (executed). All
are short words or fixture values a test uses for its own purpose: the
`GRAPHQL_REFUSAL` stderr fixture in `tests/github/test_close_issues_on_release.py`,
the monkeypatched name `_issue_api`, the parameter ids `"indented under a
list item"` and `"the second name"`, and `"make it writable"`, which
`tests/github/test_run_tests.py` asserts is absent from the printed refusal,
not from the docstring (read: each named case). A case that reads a
script's text by a regular expression is outside the probe, so this list is
a sample. The boundary run below reads every test file that names one of
the 16 scripts.

**Every docstring and comment of the 16 files was read, not only the hit
lines.** Eight files were read whole. For the other eight, every docstring
and comment line was printed with its line number by a scratch script that
uses the counting command's own rule, and each was read with the code at
its line where the sentence named it. Each sentence was judged by design
*Scope* item 1. Outside the hit listing, these went or were rewritten:

- coordinates into work items' records: `questions.md` Q6 and Q8 in
  `release_seal.py`, `release_completeness_check.py` and
  `label_merged_on_release_branch.py`; "`frame/design.md` *Judgments* 11"
  and "`gaps.md` records the divergence" in `tracker_labels.py`; "phase 1
  of this work item" in `roll_flow_measurement_issue.py`; "the ticket and
  `frame/design.md`" in `plugin_directory_check.py`; "the reading #874's S5
  took" in `durations_union.py`;
- review coordinates: "round 1 named it", "round 1 found", "Round 1,
  finding 3" and `release_seal.py`'s "(round 1's 🔴 1)";
- release markers given as the provenance of a present fact, such as
  `publish_release_note.py#fragments`' "(0.22.4)" and "(0.15.3)", as phase 3
  treated `adding_commits`' "(0.22.4)";
- former states: "the comment that stood here withheld it" and "ran it
  serially for ten releases" in `run_tests.py`, "the gathered changelog
  carried until #1053" in `publish_release_note.py`, "until these
  functions existed" in `label_merged_on_release_branch.py`, "before the
  second name" in `rules.py` and `release_report.py`, and the
  `docs/flow.md` bullet in `release_completeness_check.py`.

A removed coordinate was sometimes the only place a reason was said. There
the reason is now stated in the present tense, in the same docstring or
comment. Examples: `close_issues_on_release.py#spend_label` now says why one
copy serves three call sites, and `run_tests.py#hide_from_git` now states
the guarantee over exits with the four paths a list would have to name.

**One present-tense count was wrong about the tree, and the phase removed
it.** `release_completeness_check.py#milestone_titles` said "33 here today,
so it is reachable by growth rather than now". The repository now holds
104 milestones, more than one page of 100 (executed: `gh api --paginate
.../milestones?state=all&per_page=100 -q length` printed 100 and 4). The
count was history, so the sentence went, and the reason `--paginate` is
there stays. The "single list of 33" a few lines below is the gh 2.92
measurement and stays as K3.

**One cross-reference was wrong about the code, and the phase corrected
it.** `issue_claims_check.py`'s module docstring said the closer states its
reading "in a comment two lines above its own regex". At `cc75e05a2` that
comment stood at lines 87 to 89 of `close_issues_on_release.py` and
`CLOSING` at line 101 (read). The sentence now says "in the comment above
its `KEYWORDS`". `.github/workflows/hygiene.yml` says the same thing and is
outside this work's files; `gaps.md` *Not done* names it.

**An owner decision kept as K4, with its issue as the one coordinate.**
`publish_release_note.py`'s comment over the badge colours now says "The
owner chose the stamp's reds for every colour of the seal (#857)". Issue
#857's body records that decision under *Decided by the owner on
2026-10-28*: "Every colour is one of the stamp's reds" (executed: `gh issue
view 857`). The other issue numbers beside the seal and its badges, #718,
#832, #1153, #1204 and #1299, gave a present fact's provenance, and went.
`release_seal.py`'s "the owner's 0.17.0 seal is the drawing" carries no
hit and names an owner's decision by the release that shipped it; it
stays as written.

**Kept as K3, K2 and K1.** These hit lines remain, and the hits are their
keep classes.

- K3, an observation of a thing with no version, its date kept as the
  bound of the claim: `plugin_directory_check.py`'s "Measured 2026-10-07"
  for the directory's pages, "read 2026-10-07 and 2026-10-08" for its
  documentation, "Measured 2026-09-22" for the two marketplace files, and
  `closing`'s "(measured 2026-10-07)". Design *Scope* item 1 names the
  directory's web pages as its example of this class.
- K3, evidence with the tool version and no date: `run_tests.py`'s pytest
  9.1.1 and pytest-xdist 3.8.0 exits, and
  `release_completeness_check.py`'s "measured rather than assumed" on gh
  2.92.
- K2: `durations_union.py`'s "measured on every run" and *measured seconds*,
  `release_completeness_check.py`'s range "measured TO" and "measured
  FROM", and `roll_flow_measurement_issue.py`'s "a cycle that measured
  nothing" in three places.
- K1: the `Closes #1, #2`, `feat: … (#100)`, `Closes #88`, `Closes<!--
  -->#4` and `(#61)` samples in `close_issues_on_release.py`;
  `publish_release_note.py`'s `... (#572)` and `(#572) (#574)`; and every
  hit left in `issue_claims_check.py`. There `Closes #153 and #150` is now
  the sample body the module states the defect with, and the rest of the
  docstring already used `#153`, `#150.` and `#22` as running examples.

**Sentences no class fitted cleanly, and what each became.** Each took
`frame/questions.md` Q1's default and was kept, rewritten in the present
tense.

- `close_issues_on_release.py`'s comment on how GitHub reads an HTML
  comment named a probe pull request after each shape it states, `(#1402,
  #1403)` to `(#1410)`, and named #1181 as the issue the probes were made
  for. The probe pull requests are closed and still open on GitHub, each
  titled for the shape it probes (executed: `gh pr view 1402`, `1404`,
  `1410`). They are the evidence itself, not the provenance of a decision,
  and GitHub's reading has no version. So the comment keeps one coordinate,
  "the throwaway pull requests #1402 to #1410 into `main`, each titled for
  the shape it probes", and the per-shape numbers and #1181 went. This
  keeps one hit line.
- Stories of a past failure became the failure stated as a case that can
  happen, as phase 4 did for `deferral_check.py`. Examples:
  `issue_claims_check.py`'s "PR #162's body wrote `Closes #153 and #150`.
  At the 0.8.0 release ..."; `roll_flow_measurement_issue.py`'s 0.8.1 roll
  that closed #166 and opened #172; `tracker_labels.py`'s "Why it was
  nobody's"; and `close_issues_on_release.py`'s `DRY_RUN` incident.
- Evidence counts stay without their issue: "of three merged that way,
  none fired" (the closer), "`size: now` went uncreated across three
  releases" (`tracker_labels.py`), "one of the two has gone twenty-eight
  days without a commit" (`plugin_directory_check.py`), and "one session
  segment paid that on all seventeen of its test calls" (`run_tests.py`).
- `rules.py`'s and `release_report.py`'s "an unmarked `seal/` reads as it
  did before the second name" became "is read under the name `seal`", the
  present behaviour of `optin.home_name(root) or optin.HOME`.

**Printed strings stay, per design *Scope* Out.** Four string constants in
this phase's files carry an issue number: `durations_union.py`'s report
heading, its other heading and its argparse description, each "(#931)",
and `roll_flow_measurement_issue.py#empty_log_note`'s "(#198)". The module
docstring's first line of `durations_union.py` lost its "(#931)"; no
`__doc__` reader prints it (executed: `grep -n __doc__ .github/scripts/*.py`
names only `issue_claims_check.py`, `release_report.py` and `rules.py`,
whose first lines this phase did not change). `gaps.md` *Not done* names
the four.

**No unit adds behaviour, so no `seal mutate` run is owed.** The edits are
comments and docstrings. That is the *A comment or docstring inside source*
row of `skills/verify/SKILL.md` *The narrow command still has to be able to
fail*. No case was written or changed.

**Line width.** One line the range adds is over 79 columns (executed: a
scan of `git diff -U0 cc75e05a2 a01158430 -- .github/scripts`). It is
`run_tests.py`'s 80-column "# The CommonMark parser the suite's oracle
reads (`tests/commonmark_oracle.py`).", where the line it replaces was 80
columns too.

**S6, S5 and the phase boundary run.** `uvx ruff check` and `uvx ruff
format --check` exit 0 over the 16 files at `a01158430` (`16 files already
formatted`) (executed). The phase boundary set ran as one command at
`a01158430`: `bin/test tests/text tests/behaviour` and the 23 test files
outside those two directories that name one of the 16 scripts or
`.github/scripts`. It printed 3812 passed, 8 skipped, and exited 0
(executed). G10's module,
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, is in the
set.
