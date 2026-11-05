# Questions for the planner: the directory tracks a dist branch (#1374)

The tree or a probe answered these judgments the ticket left open, and nobody reopens them:

- Whether the directory picks up a new version from its tracked branch without a resubmission: `frame/design.md` *Grounding*, the row on `claude.com/docs/plugins/submit`.
- Which census reads cited paths, and how it reads the archive: `frame/design.md` *Grounding*, the row on `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, and `frame/plan.md` *Alternatives considered*, the rows on the census.
- Whether `bin/` and `assets/` stay in `dist`: `frame/design.md` *Grounding*, the rows on `bin/test` and on `assets/`.
- Which readers in the tree break once paths are marked `export-ignore`: `frame/design.md` *Grounding*, the row on the two readers that build a tree with `git archive`.
- Where the step that writes `dist` runs: `frame/plan.md` *Alternatives considered*, the row on the `dist` step inside the `publish` job.
- Whether the plugin moves into a subfolder instead: `frame/plan.md` *Alternatives considered*, the row on replacing the structure.

The Console listing, the portal submission of `@dist`, a ruleset on `dist` and the scratch repository's deletion are the owner's acts after the release. Their answers change nothing that gets built, so they stand in `frame/plan.md` *Operational impact* and not here.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which identity authors and commits each `dist` commit? The workflow writes it with `git commit-tree`, and git takes whatever name and email it is given, so the choice is a value somebody is accountable for and not something the tree decides. The owner's rule that only `zenith.m.jo@gmail.com` authors this repository's commits was stated for commits a session makes, and whether it reaches a commit a workflow makes on `dist` is the owner's to say. | a person | The GitHub Actions bot, `github-actions[bot]` with `41898282+github-actions[bot]@users.noreply.github.com`: the commit says a machine made it, as the tag the workflow creates through the API does. The owner's name and `zenith.m.jo@gmail.com`: every commit in the repository carries the owner's identity, written by a workflow the owner did not run. Either is one pair of environment values in the `dist` job. | The GitHub Actions bot. | open |
