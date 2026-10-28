# Questions for the planner: 1793188384-the-release-notes-are-kept-twice

The issue left these judgments open, and the tree answered them. They are not
reopened. The grounds of each are in `frame/design.md` or in `plan.md`'s
Alternatives table.

- **Where the release's work items are found at the tag, once the settle has
  removed their directories** (the issue's last check before building). From
  the history: every fragment a commit after the previous version tag added,
  each read at the newest commit of the range that holds it. Executed for
  0.19.0 to 0.23.1, it gives each released file's markers exactly, 0.22.4
  included, whose fragments the settle removed before its tag.
- **What #728 and #557 protected.** #728 made one file per release so a
  reader of one release reads one file; the GitHub Release page is one
  release, and the files stay readable at their own tags (read: #728's
  body). #557 fixed `survivor_check.py`'s reading of `CHANGELOG.md`; that
  script is no longer in the tree (executed: `git grep -l survivor_check`
  finds it only in two released files under `changelog/`). Neither is
  needed after the removal.
- **Whether the hygiene step is replaced.** It goes, and nothing replaces
  it. The empty range is refused at the tag, and the #584 and #586
  refusals guarded a gathered file and a section reader that no longer
  exist (`plan.md`, Alternatives).
- **What the theme is when a description carries no `Purpose:`, or none at
  all.** Its first sentence without the label; and no theme line, logged,
  never a failure (`frame/design.md` *Scope* item 2, S3 and S4).
- **Whether the note keeps the `<!-- specs/<work-item-id> -->` markers.**
  It does. They cost a reader nothing and stay the one link from a
  released entry back to its work item.
- **Which notes lack their file, and by what criterion.** Executed on
  2026-10-28 over the 58 released versions: 26, listed in `frame/design.md`
  *Scope* item 5, by paragraph containment with whitespace collapsed.
- **How the `docs/` `check:` lines that name the removed tests keep
  resolving until the settle.** The two files stay with no case and a
  caseless class carries `second-gather-appends`, as work item 1792935671
  did for #1027 (`tests/test_the_retired_rules_await_their_settle.py` at
  `de11df75^`).
- **What becomes of the two `seal/follow-up.md` rows that name
  `changelog/0.12.2.md`.** Their coordinate becomes the v0.12.2 GitHub
  Release. Their question and their answerer stay.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | An installed copy at 0.23.1 or earlier runs its own `update` skill to take the release carrying this work. Its step 2b reads `CHANGELOG.md` in the new install, finds no file, and stops with *a mismatch* although the update landed. Is that one false stop accepted, or is `CHANGELOG.md` kept for one release? The tree cannot answer it: the owner decided the file goes (#1053, 2026-10-27), and the cost falls on users whose number nothing in the tree records | a person | (a) Remove the file as decided. This work item's `changelog.md` says that an update from 0.23.1 or earlier reports a mismatch once at step 2b, that the update has landed, and that `.claude-plugin/plugin.json` in the installed copy names the version. Nothing is kept beside the tree. (b) Keep `CHANGELOG.md` for one release, holding only that release's `## X.Y.Z` heading and a line naming the GitHub Releases, and remove it in the release after. Someone has to write that heading at the release, which is the gather step this work removes and #1117's flow has no step for | (a) | open |
| Q2 | The republish of the 26 notes that lack their file's text: does the file's text replace each note, or is it appended below it? The tree cannot answer it: the issue says "republished from the file", which reads either way, and some of the 26 notes were written by hand | a person | (a) Append, folded under the summary today's notes use. Nothing a person wrote is lost, and every note then holds its file. (b) Replace with the file's text. Each note then matches the shape of the newer ones, and any hand-written text in it is lost | (a), done by the orchestrator in phase 5 | open |
| Q3 | Can the tag's job list the milestones with `contents: write` alone? The tree cannot answer it: the job lists pull requests that way (executed: the v0.23.1 note carries its pull request summary), but no run has read a milestone under that token | a measurement | (a) Change nothing now, and read the log of the tag run of the release carrying this work. Where it says the milestone list was refused, a follow-up adds `issues: read` and changes the scope assertion in `tests/behaviour/test_a_release_publishes_its_note.py`. (b) Add `issues: read` now, and change that assertion now, for a scope that may not be needed | (a). The orchestrator reads that run's log | open |
| Q4 | `skills/implement/orchestration.md:530` says the accumulated entries "are gathered and dated", and `:578` names "the marker the changelog gather writes". Both are stale after this work, and the file belongs to #1041's work item, which this work item may not edit. Who carries the two sentences? | a person | (a) This work item leaves the file alone, and the orchestrator names both sentences in this work item's pull request body and hands them to #1041's work item. (b) This work item edits the two sentences and the two work items reconcile at merge | (a) | open |
