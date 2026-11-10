# Phase 2: 1794271935-the-releasing-documents-describe-the-note-twice

## What this phase found

**The frame holds against the tree at `eb2d6c11a`, with the coordinates
moved.** The three greps `frame/plan.md` *Technical context* names were run
again at `eb2d6c11a` (executed, `git grep -n` outside `seal/threads/` on the
path `release-checklist`, on each heading's words, and on `step (0|2b|5|6)`).
They list the same sites as the table, with three differences, each the
result of phase 1. The checklist's "step 5 prescribes" (old line 278) is
gone, as `trail/phases/phase-1.md` said. In
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py` the four
sites stand at lines 45, 80, 86 and 223, not 42, 77, 83 and 217. In
`docs/releasing/branch-and-release.md` the wrapped citation stands at lines
241 to 242, not 233 to 234. The `#51` sites in
`docs/releasing/issues-and-milestones.md` stood at lines 62, 72, 102, 329
and 334, as *Grounding* says (executed, `git grep -n '#51' -- docs`).
Issue #51 is closed and #1464 is open with the `flow-baseline` label
(executed, `gh issue view`).

**The census was seen red with one old citation left in place.** With every
other site rewritten and `docs/layout/the-record-layout.md` line 126 still
citing `docs/releasing/release-checklist.md` *2b*, `bin/test
tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:xdist -k
every_cited_section` failed two cases, the tree reading and the archive
reading, each naming that one line and no other (executed). After the line
was rewritten, the same command passed. A rename adds no case, as
`skills/verify/SKILL.md` *The narrow command still has to be able to fail*
says, so no case was written new.

**The `--help` line is pinned by the census, and was seen red.** The
`argparse` description of `.github/scripts/finding_counts.py#main` is now
three adjacent string literals that cite the settle section. `seal mutate`
put `2b. ` back in front of the heading's words, and the census's tree
reading failed on `.github/scripts/finding_counts.py:184` (executed, `bin/seal
mutate .github/scripts/finding_counts.py --replace '*Settle what earlier
releases "' '*2b. Settle what earlier releases "'`, red). The tree was clean
after the restore (executed, `git status --short`). `python3
.github/scripts/finding_counts.py --help` prints the citation (executed).
This is the case contract rule 14 asks for, and the design names the census
as it.

**Each prose mention of a step inside the checklist names the heading or
drops the number.** "goes red at step 5" became "goes red when it opens",
because the sentence names the release pull request already and the
heading is the same words. "the boxes of step 6" became "the boxes of
*After the merge*". "step 0's milestone box" became "the milestone box of
*Before starting*". `grep -n -E 'step [0-9]' docs/releasing/release-checklist.md`
finds nothing (executed).

**The #1148 sentence names #1148 once.** The old text named it twice, once
with its history ("which removed the records' copies of one another") and
once in "#1148 is measured by this count falling". Both now read: "The four
numbers measure records that restate one another, and #1148 is the reason
they are counted. ... The count is expected to fall, so a count that holds
level is read as one that rose". Judged against `frame/design.md` *Scope*
item 6. No case pinned the old sentence (executed, `git grep` of its
phrases under `tests` and `.github`).

**The `log:` paragraph says why the milestone never closes without naming
an issue.** It says either log can close: the rolling log is closed and
replaced when a release ships, and the durable log is a ledger that can
roll to a new issue. One of each kind is always open, so the milestone
never closes. The two facts stand on
`.github/scripts/roll_flow_measurement_issue.py`, which rolls the
`flow-measurement` issue only where a new version shipped and holds the
`flow-baseline` label to the same exactly-one-open invariant (read,
`BASELINE_AMBIGUOUS_NOTE`). The paragraph does not say why #51 rolled,
because nothing this work item read says why. The last of the five sites
said "`#51`'s own body says so at the top". #1464's body says so in its
second paragraph, in bold (executed, `gh issue view 1464 --json body`), so
the sentence keeps "at the top" for the open `flow-baseline` issue.

**One sentence outside the frame's list stated the old rule, and changed.**
`docs/releasing/issues-and-milestones.md` *Closing one of these by hand
breaks the next release* said "A milestone holding two issues that never
close". After *Scope* item 7's rewrite, each issue can close, so it now
says "two issues that stay open". It was found by `git grep` on
`log: measurement`, `durable log`, `never closes` and `neither closes`
outside `tests/` (executed), and `git grep -i 'never close' --
docs/releasing` at `c44121bff` lists no other sentence about the logs. Judged against `skills/core/SKILL.md` *The rule a
mechanism is kept against*: a change removes, in the same commit range, the
copies that stood on the old fact. This is a departure from the frame's
list of sites.

**A stale step number outside the scope stays.** `gaps.md` *Not done*
holds `tests/behaviour/test_release_hygiene.py`'s "at step 3" with the
grounds.

**Rule 12's census of the renamed headings.** Method: the three greps of
*Technical context*, run at `c44121bff`, plus `git grep` on each old
heading with its number. That builds the list from what produces the
defect, a citation that writes the path or the heading's words, so it is
whole for those two spellings. It is a sample for a prose mention that
names neither, which no method lists whole. What stands at
`c44121bff` (executed): `git grep -n -E 'release-checklist\.md`? (step
|\*(0|2b|5|6)[.*])' -- . ':!seal/threads'` and `git grep -n '#51' -- docs`
find nothing. `git grep -n -E '0\. Before starting|2b\. Settle|5\. The
release pull|6\. After the merge|step 2b'` finds two kinds of line. The
first is two lines of the census's own fixture in
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, lines 518 and
523, which test short-form resolution against a file under `manual/` and
cite no real file. The second is the three lines
on `skills/update/SKILL.md`'s own step `2b.`, which *Scope* puts out of
scope. `git grep -n -i 'checklist'` outside the path found one more step
number, the "step 3" above.

**What the next reader needs.** #1464's body still cites
`docs/releasing/release-checklist.md` *2b*. `frame/plan.md` *Operational
impact* names it for the orchestrator or the owner.
