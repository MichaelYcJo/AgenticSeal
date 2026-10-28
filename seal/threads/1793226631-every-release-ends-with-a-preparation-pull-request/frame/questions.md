# Questions for the planner: 1793226631-every-release-ends-with-a-preparation-pull-request

Judgments the ticket left open that the tree answered, so nobody reopens them:

- **The released process archives go, and are not folded into their notes.**
  The tag `v0.23.1` holds all three (executed, `git ls-tree`), the publisher
  never edits a published note, and the owner declined editing published
  notes for #1053 (that work item's `frame/questions.md` Q2). `plan.md`'s
  Alternatives table carries the two other options.
- **The heading a fragment's process rows sit under is `### Process changes`,**
  in the shape `templates/records/process.md` gives, and `section` lifts
  every row into one table of that name at the top of the fragments
  (`frame/design.md` *Scope* items 3 and 4).
- **The tag is a lightweight tag created through the GitHub API, in the
  `publish` job of the existing workflow.** Every tag here is lightweight
  (executed, `git cat-file -t` on `v0.23.1` and `v0.22.4`), and one workflow
  keeps one copy of the publish and seal steps.
- **A re-run passes on a tag that already names the pushed commit.** The
  issue's "nothing otherwise" would leave a re-run after a failed note step
  with no note; the note step never republishes, so the arm is safe.
- **The orchestrator moves the version, in the commit that adds the first
  work item's fragment**, and for 0.24.0 in this work item's.
- **The checklist's remaining headings keep their numbers**, because `*5.*`
  and `*6.*` are cited across the tree.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | When does the orchestrator open a release's pull request into `main`? The issue says the orchestrator opens it and does not say when. A work item's run ends when its own pull request opens, before anyone merges it, so no run sees the release branch complete; and the milestone holds issues whose pull requests merged but which stay open until `main` moves, so "the last open issue" cannot be read from the tracker | a person | (a) With the first work item pull request into `release/vX.Y.Z` that finds none open, left open all release: the release pull request's CI runs on every merge into the branch, and its milestone check is red until the branch carries every milestone issue, then green with no push. (b) With the pull request of the work item that `.github/scripts/release_completeness_check.py`, run against that work item's head, shows to be the last one the branch does not carry: one CI run, but two last work items in flight at once each see the other and neither opens it, so a person starts a session to open it. (c) A session the owner starts after the last merge: an owner act at every release | (a). For 0.24.0 the orchestrator opens it with this work item's pull request, since none is open (executed, `gh pr list --state open`, 2026-10-29). `## Rule changes` writes (a) into `docs/release-checklist.md` *5. The release pull request* | open |
| Q2 | The checklist gives the owner three acts at a release that the issue does not name, and this work leaves them as written: in *5. The release pull request*, "The owner reads the rows whose seconds or cases grew most since the tag and sweeps each such module with one `bin/seal mutate` call"; in *6. After the merge*, reading the plugin directory's page behind his login, which `plugin_directory_check.py` says no script can reach; and the boxes of step 6, which confirm the release note, the directory files and the closed issues. Do they stay the owner's, or move? | a person | (a) They stay as written: the owner's required act is the merge, and these read reports that fail nothing. (b) The release-table read and the sweep move to the orchestrator that opens the release pull request, which then answers growth in the pull request's body and files the cuts into the next milestone; the directory page stays the owner's, since it sits behind his login | (a): this work changes only the preparation steps and the tag push the issue names | open |
| Q3 | Should CI refuse a pull request into `release/vX.Y.Z` whose merged tree does not name `X.Y.Z` in `.claude-plugin/plugin.json`? Without it, a release whose first work item forgot the version is caught only at the release pull request, and its repair is one more pull request into the release branch | a person | (a) No check: `skills/implement/orchestration.md` tells the orchestrator to move it, and the release pull request's version step holds the release. (b) A new step in `hygiene.yml`'s `release` job: it reads a fact exactly and catches the miss at the first pull request, but it adds a row to `skills/verify/scripts/broad_gate.py#PARTITION` and moves the count sentence in `skills/verify/orchestration.md`, which #1111 owns on branch `chore/1111-most-contract-rules-are-proved-by-their-own-wording` | (a) in this work, so no file #1111 owns is edited. (b) can follow as its own issue after #1111 merges | open |
| Q4 | Does creating `refs/tags/vX.Y.Z` through `gh api -X POST repos/<REPO>/git/refs` with the workflow's token under `contents: write` succeed on this repository? No ruleset targets a tag (executed, 2026-10-29), and no run of the new step can happen before 0.24.0's merge into `main` | a measurement | Succeeds: the run tags, publishes and seals. Refused: the tag step exits 1 naming GitHub's error, the release is on `main` untagged, and a tag pushed by hand still fires the same workflow | Build as designed. The reader is the orchestrator, reading `gh run list --workflow publish-release.yml --limit 1` and that run's log after 0.24.0's merge | open |
