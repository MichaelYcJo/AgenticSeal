# Phase 1: 1794271935-the-releasing-documents-describe-the-note-twice

## What this phase found

**The frame holds against the tree at `5eda5fabd`.** The coordinates
`frame/design.md` *Grounding* names for `docs/releasing/release-checklist.md`
272 to 347, `docs/releasing/branch-and-release.md` 59 to 174 and
`.github/workflows/publish-release.yml` 28 to 51 held the text the frame
describes (read). Milestone 93's description matches the *Grounding* row
(executed, `gh api repos/MichaelYcJo/AgenticSeal/milestones/93`). Every file
the plan row's verification names exists.

**The new case was seen red three ways, and one of its guards first
survived.** `tests/text/test_the_release_tail_does_not_end_at_the_tag.py#test_the_listing_s_hold_carries_its_date_and_whose_decision_it_is`
failed against `5eda5fabd`, where no hold's sentence stands (executed).
After `d025397bc`, `seal mutate` took the date out of the hold's sentence
and the case went red on its date line. It took the owner out and the case
went red on the owner line. It took `dist` out and the case stayed green
(SURVIVED). The cause was the sentence split, `(?<=\.) `. It does not
split after the bold lead's closing `.**`, so the lead, which names `dist`,
stood in the same chunk as the hold's sentence and answered for it.
`de9fe33ca` also splits after `.**`. Run again at `de9fe33ca`, the four
mutations each went red on the line of the guard they broke: the date, the
owner, `dist`, and the phrase "The listing has been on hold" itself
(executed, `seal mutate` on `docs/releasing/branch-and-release.md`, each
with `bin/test tests/text/test_the_release_tail_does_not_end_at_the_tag.py -q -k test_the_listing_s_hold -p no:xdist`).
The tree was clean after each restore (executed, `git status --short`).

**The S2 grep caught a phrase this phase wrote.** The first draft of the
directory box named "the portal's Submissions page for a portal listing",
which `git grep -n -E 'portal listing|…' -- docs/releasing` finds. The box
now says the command prints "the page that answers for each kind of
listing: the portal's Submissions page, and the Console page". The case
`test_the_directory_box_names_the_page_a_person_opens` still finds both
page names (executed).

**One departure from the frame: the workflow's `dist` paragraph changed
too.** `frame/design.md` *Scope* item 2 rewrites only the seal paragraph,
and says the comment keeps "the `dist` job's place and its red". Its last
sentence gave that red the reason "a release that did not reach `dist` is a
release the directory did not get". That is the phrase *Scope* item 3
removes from `docs/releasing/`, so the comment would have been the copy
left behind. The red stays, and its reason now reads "leaves `dist` behind
the tag". Judged against `skills/core/SKILL.md` *The rule a mechanism is
kept against*: a change removes, in the same commit, the copies that stood
on the old fact. No line outside a comment changed (executed, S5's
`git diff` filtered to lines that do not open with `#`, empty).

**The title's fallback is stated as a state, not as make-up.** The old box
said "A missing title line is not one of them: it falls back to the tag
name." *Scope* item 1 keeps "a title that is the bare tag name" as a state
a reader may see. The box now says what that title means and where the log
explains it: "its log gives the shape it expected and the line it found".
`.github/scripts/publish_release_note.py` lines 426 to 429 print that line
(read). Where the title comes from is cited to
`docs/releasing/branch-and-release.md` *Cutting a release*.

**The key's warning keeps the cause and loses "row".** The box says "A
value of `seal/config.json`'s `Release note seal mark` key other than `yes`
is named on a `::warning::` line of its own". What the key's values do is
left to *Cutting a release* and `templates/setup/config.md` *The seal
mark*.

**The hold's passage sits inside the `dist` paragraph, right after the
lead.** `tests/behaviour/test_a_cited_section_stands_in_its_file.py#test_this_repository_s_archive_holds_only_the_scripts_a_shipped_command_runs`
reads the paragraph from the lead to its first blank line for the three
kept scripts. A passage in a paragraph of its own would have cut that
paragraph short (read). The case passes (executed).

**Two sentences on how the directory serves a submission stay.** `gaps.md`
*Not done* holds them with the grounds.

**The check line.** The `dist` paragraph's `check:` line now names
`tests/text/test_the_release_tail_does_not_end_at_the_tag.py`, as *Scope*
item 4 asks.

**Rule 12's census of the statements this phase reworded.** Method: `git
grep` on the words, so each list is a sample, not a whole list.
`git grep -l -E 'Thanks to|seal\.png|Release note seal mark' -- . ':!seal/threads'`
listed 15 files. The two scripts' docstrings are out of scope by
`frame/design.md` *Scope*. `templates/setup/config.md` *The seal mark* is
the key's home. `skills/config/SKILL.md` line 57 is the settings index,
which names the key and what `yes` turns on. `TRADEMARKS.md` and
`assets/seals/README.md` name the image and where it is drawn from.
`seal/config.json` holds the key, and the four test files and
`.test_durations` name it or the image in cases. None restates the
header's make-up. `git grep -i -E 'portal listing|directory
did not get|picks up each new version|#1383' -- . ':!seal/threads'` lists
`.github/scripts/plugin_directory_check.py` and its case, whose printed
lines `frame/design.md` *Scope* keeps, and one comment in the case file
that names the two pages. `.test_durations` line 5973 still keys the
removed case's name. That file is refreshed from a run's union at the
release (#1468), and this phase does not write it.

**For phase 2.** The new case's split, `(?<=\.) |(?<=\.\*\*) `, and the
constant `AFTER_THE_MERGE` sit in the same file that phase 2 renames
headings in. The hold's case reads `## Cutting a release` through
`section()`, which phase 2 does not rename. In the checklist, the note box
no longer says "step 5 prescribes", so the citation list in `frame/plan.md`
*Technical context* has one site fewer: `docs/releasing/release-checklist.md`
line 278 is gone.
