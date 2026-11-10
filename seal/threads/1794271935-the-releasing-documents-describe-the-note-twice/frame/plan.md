# Implementation Plan: 1794271935-the-releasing-documents-describe-the-note-twice

## Technical context

The tree as read at `763256a8a`.

The work edits text: three documents of `docs/releasing/`, one workflow
comment, the citations of the checklist's steps in scripts and tests, and
one case. No executed line of code changes except the `argparse` description
of `.github/scripts/finding_counts.py#main`, which `--help` prints.

**Where each statement goes.** `docs/releasing/branch-and-release.md`
*Cutting a release* keeps the note's make-up (lines 59 to 115) and gains the
listing's hold after the bold lead at line 144. `docs/releasing/release-checklist.md`
*6. After the merge* keeps commands, the states of a failed or partial
result, and the repairs (lines 272 to 346). `frame/design.md` *Scope* items
1 to 3 state what each box keeps and loses.

**Text that cases and citations hold, which the build keeps word for word.**

- The bold lead **A GitHub Release exists at `vX.Y.Z`**, which `tests/behaviour/test_the_release_seal_is_drawn.py#test_the_checklist_box_says_where_a_missing_seal_is_explained` splits on, and in that box the five phrases it asserts (lines 55 to 66): "the same workflow's `seal` job attaches `seal.png`", "says why on a `::warning::` line", "`DRY_RUN=1 python3 .github/scripts/release_seal.py`", "`gh release upload`", and "then apply the note it prints with `gh release edit --notes-file`".
- "Two acts come after the tag", which `tests/text/test_the_release_tail_does_not_end_at_the_tag.py#after_the_tag` indexes, and in the boxes after it the two commands, `publish-release.yml`, `gh run list`, "Submissions page" and "Console page" (lines 113 to 159 of that file).
- The bold lead **The plugin directory reads `dist`**, which `.gitattributes` line 14 cites and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` lines 947 to 954 require, with the three kept scripts and their runners in the paragraph up to its first blank line.
- In `branch-and-release.md`, the span from **What breaks when the last row is squashed.** to **Two rulesets enforce the merge methods.** must still cite the checklist's after-the-merge section and say "`plugin_directory_check.py` reads the name out of `.claude-plugin/plugin.json`" (`tests/text/test_the_release_tail_does_not_end_at_the_tag.py#squash_rule`).
- `release-checklist.md` stays under `tests/behaviour/test_docs_line_wrap.py`'s wrap limit, which lists it at line 159.

**Every place that cites a checklist step by its number or its heading.**
Fifteen files hold a citation that moves, listed below by the heading each cites. The list was built with `git grep -n` (executed, outside `seal/threads/`) on three patterns: the path `release-checklist`, each heading's words, and `step (0|2b|5|6)`. It is whole for every citation that writes the path, or a heading's words on one line, which the second pattern found where a citation wraps between the path and the section (`branch-and-release.md` lines 233 to 234). A prose mention that names neither the path nor the heading's words is outside what the three patterns list, and the proofer reads for one.

| Heading at `763256a8a` | Heading after this work | Sites |
|---|---|---|
| `## 0. Before starting` | `## Before starting` | `docs/releasing/issues-and-milestones.md` line 205; `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py` line 353, the heading string `section()` reads; `docs/releasing/release-checklist.md` line 172, "step 0's milestone box" |
| `## 2b. Settle what earlier releases left behind` | `## Settle what earlier releases left behind` | `docs/layout/the-record-layout.md` line 126, `*2b*`; `.github/scripts/finding_counts.py` line 2, lines 35 to 36 and line 181, the last printed by `--help`; `tests/github/test_finding_counts.py` line 2; `tests/text/test_the_direct_answer_owes_the_sealers_record.py` line 97, the heading string `in_force()` reads, and lines 102 to 103, its message |
| `## 5. The release pull request` | `## The release pull request` | `docs/releasing/branch-and-release.md` lines 66 to 67; `.github/scripts/publish_release_note.py` lines 47 to 48 and line 166; `.github/workflows/test.yml` line 229; `tests/behaviour/test_a_release_publishes_its_note.py` line 30, `*5*`, and line 41, the heading string it indexes; `tests/github/test_publish_release_note.py` lines 617 to 618; `docs/releasing/release-checklist.md` line 30, "at step 5", and line 278, "step 5 prescribes" |
| `## 6. After the merge` | `## After the merge` | `docs/releasing/branch-and-release.md` line 135 and lines 233 to 234; `.github/scripts/plugin_directory_check.py` line 9; `tests/behaviour/test_the_release_seal_is_drawn.py` line 43; `tests/text/test_the_release_tail_does_not_end_at_the_tag.py` line 42, the constant `AFTER_THE_MERGE`, line 77, line 83, the heading string `section()` reads, and line 217; `docs/releasing/release-checklist.md` lines 139 to 140, "the boxes of step 6" |
| `### What a release pull request is held to` | unchanged | `docs/releasing/issues-and-milestones.md` line 116 and `tests/behaviour/test_release_hygiene.py` line 1123 keep their citation |

The `*2b*` in #1464's body is a citation outside the tree, and
*Operational impact* below names it. `skills/update/SKILL.md`'s `**2b.` and
the cases that read it (`tests/behaviour/test_release_hygiene.py` lines
1061 to 1081, `tests/behaviour/test_update_reads_the_config_directory_in_use.py`)
are another document's step, and the grep's hits there are not this list's.

**The dedupe moves no heading and no cited bold lead.** The bold leads the
cell keeps are listed above, and `git grep` on each bold lead of the two
boxes and of the bullet (executed) finds no other citation of them.

**The failure scenario of the chosen approach.** In six months a step is
added to the checklist. With unnumbered headings it is added under its own
name and no citation moves. What can still break is a heading reworded
later: its citations then dangle, and the census names each one, as it does
today. The second failure is the hold's passage outliving the hold. When the
listing resumes, the passage in `branch-and-release.md` is the one place to
remove, and the replaced case names its date so a reader can tell how old it
is.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Renumber the checklist's headings 1 to 4, as #1490 *Change* words it | The next step added or removed either renumbers every later heading, which moves the citations in the files *Technical context* lists, or takes a number such as `2b` to avoid that move. The second is how the present `0, 2b, 5, 6` arose: steps 1 to 4 were removed and 2b was inserted, each time without renumbering | rejected. The number is a copy of the heading's position, kept by hand in every citation, which `skills/core/SKILL.md` *The rule a mechanism is kept against* asks a fix to question before it adapts to |
| Headings that carry no number, the order given by their position (chosen) | A person can no longer say "step 3" aloud; a citation names the heading's words instead. A reworded heading still moves its citations, and the census catches each one as it does now | chosen: an insertion or a removal moves no citation, and the gap the issue reports cannot recur |
| Keep the numbers and only fill the gap, writing `## 1. Settle …` and leaving 0, 5 and 6 | Still a gap from 1 to 5, and the same cost at the next insertion | rejected |
| The note's make-up stated in the checklist, with `branch-and-release.md` citing it | The document a person reads before a merge to learn why would send that reader to the list for the day, and the checklist's opening sentence (lines 3 to 5) would stop being true | rejected; #1490 *Change* and the checklist's opening agree on `branch-and-release.md` |
| Leave the workflow's header comment as it is, since the issue's *Done when* names `docs/releasing/` alone | The comment restates `release_seal.py`'s output and the key's values. The next change to the header updates `branch-and-release.md` and the script, and the comment is the copy left behind, which is the stale "row" this frame finds in the checklist | rejected; the comment keeps how the jobs run and cites the document for what the note holds |
| Remove the workflow's whole header comment | `created`, the header guard and the reason every `seal` step is `continue-on-error` are stated nowhere else for a person who changes the workflow | rejected |
| Trim the docstrings of `publish_release_note.py` and `release_seal.py` too | Each docstring describes its own unit for the person who changes that unit. Trimming them sends that person to a policy document for how the code behaves | rejected; *Scope*'s out-of-scope list holds the grounds |
| State the hold in the checklist's directory box | The box is the act on the day; the hold is why the act's answer is known in advance. When the listing resumes, the reader of `branch-and-release.md`'s `dist` paragraph would still read a live directory unless that paragraph also changed, so the hold would be stated twice | rejected |
| State the hold nowhere in `docs/` and leave it to milestone 93 | #1490 *Decided* says the documents say the listing is on hold. A reader of the `dist` paragraph would read a directory that takes each release | rejected |
| Remove the case that pinned the portal-listing sentence, and pin nothing in its place | The hold's sentence can lose its date in a later edit, and a reader cannot then tell how old the statement is. That is the defect #858 A6 wrote the case against | rejected; the case moves to the hold's sentence |
| Name #1464 in place of #51 | The ledger rolled once and can roll again, and the number would go stale as #51 did. The code looks the log up by its label (`roll_flow_measurement_issue.py#BASELINE_LABEL`) | rejected; "the open `flow-baseline` issue" is the lookup key |
| Keep `finding_counts.py`'s `--help` line in prose, "the settle step" | The census reads no prose, so the next heading change leaves the printed line stale, as "step 2b" is about to be | rejected; the string names the section as a citation, which the census reads in `.py` string literals |
| Merge the checklist into `branch-and-release.md`, one document instead of two | The day-of order of commands would be spread across the paragraphs that argue for them. The premise that keeps two documents, that the checklist is opened on the day and `branch-and-release.md` before a merge, holds: `docs/README.md` *docs/releasing/* gives the two different questions (read) | rejected; the structure is kept |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1, 2, 3 and 4 | The narrow run of `tests/text/test_the_release_tail_does_not_end_at_the_tag.py`, `tests/behaviour/test_the_release_seal_is_drawn.py`, `tests/behaviour/test_a_release_publishes_its_note.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_docs_line_wrap.py`; the new case seen red with the date taken out of the hold's sentence; the greps of scenarios S1, S2 and S5 | `de9fe33ca` |
| 2 | `frame/design.md` *Scope* items 5, 6 and 7 | The narrow run of `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and of each test file *Technical context* lists, with `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` and `tests/behaviour/test_docs_line_wrap.py`; a rename adds no case, so the census is shown able to fail by one old citation left in place and seen red; the greps of scenarios S3 and S4 | |

## Overlap with the release

The spawn names three other items of 0.37.1, and none meets this work.
#1491 changes `docs/layout/one-root-by-lifetime.ko.md` and
`skills/settle/rule-changes.md`. #1492 changes `README.md`, `README.ko.md`
and `docs/checks/the-stamp.md`. #1493 changes `seal/follow-up.md`,
`skills/implement/SKILL.md`, and under `tests/` the files its issue names:
`tests/behaviour/test_waiver_decided_at_start.py`,
`tests/text/test_a_rider_reaches_its_file.py`,
`tests/github/test_release_completeness_check.py` and
`tests/github/test_label_merged_on_release_branch.py`. None of those files is
among the files this work changes. A `git grep` of the files #1491, #1492
and #1493 name for `docs/releasing/`, `#51`, `flow-baseline`, the plugin
directory and `Release note seal mark` finds nothing (executed), so no item of
the four changes a rule, a check or a fact another of them reads. The census reads the
whole tree, and none of the four items adds it. Read: #1491, #1492 and #1493
with `gh issue view` (executed), and their branches, each one routing commit
past `origin/release/v0.37.1` (executed).

## Operational impact

No migration, environment variable, dependency or compatibility break. The
version is not moved here: #1495 moved `.claude-plugin/plugin.json` to 0.37.1.

`python3 .github/scripts/finding_counts.py --help` prints the settle
section's new heading.

#1464's body cites `docs/releasing/release-checklist.md` *2b* for where the
finding counts come from. After this work merges, that citation names a
heading that no longer exists. Issue bodies are outside the tree, and an
agent posts nothing (contract rule 6), so the orchestrator or the owner
edits that line with `gh issue edit 1464`.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
