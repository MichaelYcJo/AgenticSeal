# Implementation Plan: 1794271937-the-readme-narrates-three-migrations

## Technical context

The tree as read at `20f97977c`.

The work rewrites prose and the cases that pin it. `README.md` *Updating*
(lines 69–120) and *What runs on your machine* (lines 348–412) and their
Korean twins in `README.ko.md` carry the narration. `docs/checks/the-stamp.md`
*The stamp* carries the launcher's description at lines 94–98 and the
measurement's attribution at lines 125–127. The homes the README links to
stand and do not change: `skills/update/SKILL.md` steps 3, 4 and 4b, and
`skills/config/SKILL.md` *A `config.md` standing in the root without a
`config.json`* (`frame/design.md` G3 to G5).

Constraints the build meets:

- Both READMEs keep the same heading outline
  (`tests/behaviour/test_both_editions_carry_the_same_folds.py`), and both
  stay under the wrap `tests/behaviour/test_docs_line_wrap.py` holds.
- No shipped file names an untagged version at or above 0.37.1 (G9). The
  removal date is a date, and it is written only in `changelog.md` and this
  frame.
- A citation of the update step is written as `skills/update/SKILL.md` *4b.
  The launcher an earlier release wrote*, a bold lead that
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py` resolves (G11).

The failure scenario of the chosen approach, six months on: the removal is
not filed or not taken, and the paths stand past 2027-02-07. The README's
one paragraph stays true, because it names no date. The release note of
0.37.1 then states an expiry nobody kept, and `/agentic:update` keeps
repeating it to every person who updates across 0.37.1. The removal's issue,
filed when this pull request opens, is what keeps the date from being only a
sentence (*Operational impact*).

`routing.md` *Why this way* says the diff touches the two READMEs and
`docs/checks/the-stamp.md`. This frame also adds the `docs/experiments/`
record of `frame/design.md` *Scope* item 5, with its entry in
`tests/behaviour/test_docs_line_wrap.py`, and the test edits of *Scope* item
6. Each is text no party acts on or a case pinning that text. Phase 1 also
exempted `templates/setup/claude-md-block.md` by name in
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_every_template_is_named_by_a_document_that_ships`,
a change to a check, so the orchestrator routed the review through the
review chain (`routing.md` *Why this way*).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Keep the README's three narrations as they stand (keeping the structure) | Each fact stands in three to four places (issue #1492's list). The README's `config.md` paragraph is the 0.37.0 release note word for word, so when the conversion leaves, the README, the note and the update step disagree until someone finds every copy. The premise that would keep it, that a person who never runs `/agentic:update` has nowhere else to learn the steps, holds only for the `seal mode` line and the files rewritten by hand, which the chosen approach keeps | rejected |
| A2. One paragraph that names what `/agentic:update` does for an earlier release and links to the update skill, keeping the `seal mode` line and the files rewritten by hand; one linking sentence for the launcher in *What runs on your machine* (replacing the structure) | A person updating by hand from 0.24.x is not told the `CLAUDE.md` block is there. They meet it at their next `/agentic:update`, whose step 4 removes it, and the README's paragraph says so | chosen |
| A3. Drop every earlier-release sentence from the README and rely on the release notes | A person who updates by hand never sees a release note and never learns that `seal mode` must run, so every `seal gate` in that repository exits 2 until they find it. The issue keeps that line | rejected |
| A4. Drop the launcher from *What runs on your machine* entirely | The section's last paragraph says the two hooks are the only things that run without the person starting them, which is false for a person who still holds the launcher | rejected |
| A5. Remove the compatibility paths in this work item | The `config.md` path is one day old (`frame/design.md` G6). Removing any path changes `lib/config.py`, `seal.py`, the update skill and their cases, which is a code change the routing's grounds do not cover | rejected |
| A6. Schedule the removal by release count, such as the second minor after each path's release | Releases are cut most days (`frame/design.md` G8), so a count expires within days and says nothing about how long a person goes between updates | rejected |
| A7. Schedule the removal at 1.0.0 | No version 1.0.0 is planned anywhere in the tree or the milestones, so the paths stay with no date and keep costing every `/agentic:update` run its steps 4 and 4b | rejected |
| A8. A date per path, by the harm a leftover does (the launcher sooner, the settings later) | Three dates for the owner to set and three removal items, where the paths stopped between 2026-10-30 and 2026-11-09 (`frame/design.md` G6); one date keeps the earliest path ten days past its own 90 | rejected |
| A9. One date, 90 days after the latest path's release, all paths removed together (`frame/design.md` *Scope* item 7) | 90 days rests on no measurement of update lag (G7). A person who stays on 0.36.x longer meets the plain refusal of an unknown file after the removal. The owner sets the number at the pull request | chosen |
| A10. State the removal date in the README or the update skill | A version in a shipped file is refused (G9), and a date in the update skill is text no agent acts on. The release note is where step 3 already reads expiries | rejected |
| A11. Record the removal in `seal/follow-up.md`, or as a rule in `docs/releasing/` through `## Rule changes` | `seal/follow-up.md` says this repository has a tracker and should hold no schedulable item (G13), and #1493 is emptying it. A standing rule on how long every compatibility path stays is a new mechanism with no record of what it would have caught, and `docs/releasing/` is #1490's | rejected |
| A12. `the-stamp.md` cites issue #1376's comment for the measurement | No document under `docs/checks/`, `docs/running/` or `docs/layout/` cites an issue (G10), and `docs/experiments/README.md` names `docs/experiments/` as the home of a platform fact | rejected |
| A13. Drop the measurement clause from `the-stamp.md` | The clause is the only evidence the paragraph gives that a `Stop` command hook runs from a plugin, and its last sentence says nobody has watched the plugin's hook draw on a screen yet | rejected |
| A14. A dated record under `docs/experiments/`, transcribed from the comment, cited by `the-stamp.md` | The comment's method is a summary, so the record cannot be re-run from its *Method*; its *What it did not establish* says so | chosen |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6, and *Scope* item 7's *Updating* sentence in `changelog.md` | `bin/test -q` over `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_the_old_block_leaves_through_update.py` and `tests/text/test_the_mode_is_a_row_and_a_command.py`; each new assert of *Scope* item 6 seen red against the sentence it replaces; the greps of `frame/design.md` *User scenarios & acceptance* | `11ea31d92` |

## Overlap with the release

The spawn names #1490, #1491 and #1493, and none has a frame. None meets
this work: this work changes no file the spawn lists for them, changes no
rule or check they read, and reads none of theirs. One reading to keep in
view: #1490 edits `tests/behaviour/test_release_hygiene.py`, whose version
check reads the README and `docs/experiments/` text this work adds. #1490's
issue names the release-note documents and not that check, so the two do not
meet unless #1490's frame changes the check.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|

## Operational impact

No migration, environment variable, dependency or compatibility break. The
version stays at 0.37.1, which #1495 set in `.claude-plugin/plugin.json`.

Phase 1's `changelog.md` carries one *Updating* sentence: the compatibility
for an earlier release's `CLAUDE.md` block, its stamp launcher and its
`seal/config.md` stays until the first release cut on or after 2027-02-07
(`frame/design.md` *Scope* item 7). The removal needs an issue that carries
that date and the table of *Scope* item 7. The orchestrator files it when the
pull request opens, or the owner does when they set the date there.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-10 | The title takes `docs:` | The diff changes the two READMEs, a policy document, a new experiment record and the cases that pin their text; the one change to a check exempts a template no session bootstraps, and no shipped behaviour changes | `~/.claude/skills/commit-pr-convention/SKILL.md` |
