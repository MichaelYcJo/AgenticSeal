# Questions for the planner: each entry links its pull request (#1139)

The tree answered these judgments, which the ticket left open. Their grounds
stand where each line points:

- Which commit gives an entry its number: `frame/design.md` *Grounding*, the
  executed probe row, and `plan.md` *Alternatives considered*, the first
  two rows.
- Whether the hidden marker stays beside the link: `plan.md` *Alternatives
  considered*, "Keep the hidden marker beside the new link".
- How the settle recognises an entry, including in notes published before
  this change: `plan.md` *Alternatives considered*, "Drop the marker and read
  only the link in the settle" and "Recognise the entry by the fragment's
  text".
- Whether the check belongs in `seal settle --apply` or in this repository's
  release tooling: `plan.md` *Alternatives considered*, "Put the check in
  this repository's own release tooling".
- Whether the dry run reads the note: `plan.md` *Alternatives considered*,
  "Read the note in the dry run too".
- How the release list is read: `frame/design.md` *Grounding*, the executed
  `gh api` row, and `plan.md` *Alternatives considered*, "Ask
  `releases/tags/<tag>` once per version".

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Where `--apply` can read no note for a released work item, does it keep the directory? The cases are: no `changelog.md`, an adding commit that names no pull request, no `vX.Y.Z` tag on that commit, or no published release at the tag. The tree cannot decide this. The issue's words ("keeps … when the GitHub Release of the version that shipped it does not carry its entry") read either way for a release that does not exist, and the cost falls on users' repositories, which no probe here can see. | a person | (a) Name the case on a line under `removed`, and remove the directory as the open-row rule decides. A repository that does not tag, or tags without publishing Releases, settles as it does today. In this repository a release that was never published is caught at checklist step 6, and the history still rebuilds its note. (b) Keep and name the directory. A missing release becomes a hold too, and a repository that tags without publishing Releases never settles a tagged work item. | (a) | open |
| Q2 | A shared-mode repository has a `vX.Y.Z` tag on a candidate's adding commit, and `gh` cannot be asked there (not installed, or a host that is not GitHub). Does `--apply` stop? The issue asks for the stop, and it says local mode already stops this way. What it did not weigh is that this reaches users' shared-mode repositories, where `seal settle` never asked `gh` before. | a person | (a) Stop with exit 2 and remove nothing, as the issue says. A repository like that settles only after it installs `gh` or removes its directories by hand. (b) Name the note as not read and remove as before. A repository with no `gh` never gets the check. | (a) | open |
| Q3 | Which module holds the one reader of a fragment's adding commit and its pull request number (*Scope* item 2)? The options are `skills/settle/scripts/settle.py`, which the renderer would load by path as it loads `unverified_check.py`, a new module beside it, or `hooks/lib/`. Where it lands decides whether `ruff.toml`'s py39 table and `tests/hooks/test_launch.py` apply. | the work | Any of the three gives one source. The phase that builds it decides, and records the choice in its phase record. | A function in `skills/settle/scripts/settle.py`, loaded by path from the renderer | open |
