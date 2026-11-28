# Questions for the planner: 1795849901-number-read-at-cut

The judgments #1671 left open, and one this frame met, that the tree
answered. Each points at its grounds, so none is reopened here.

- What `merged:` says between a squash and the cut: `merged: next`, taken
  off at the close. `frame/plan.md` *Alternatives considered* A7.
- The unnumbered branch's name: `release/next`, which the `release`
  ruleset already holds. `frame/design.md` G4.
- Where that branch is cut again after a release: nowhere; it is cut from
  `main` once. `frame/design.md` G5 (a), and `frame/plan.md` A1 and A2.
- Which pull request moves the version: the last into `release/next`
  before the release pull request opens. `frame/plan.md` A9.
- Whether the open `release: 0.41.1`, `release: 0.42.0` and
  `release: 0.43.0` milestones are renamed by goal, as #1671's *Done when*
  asks: each ships under its number before or with this change, so its
  title states a shipped release and is kept. The tracker act after the
  merge renames only a `release:` milestone of a release not yet cut.
  `frame/plan.md` *Operational impact*. Either answer builds the same
  files.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How `publish_release_note.py#merged_pulls` asks `gh` for the pull requests the range names: one `gh pr view` per number, or one call that lists several | the work | per number costs one call for each pull request of a release and fails one at a time; one call costs a query whose limit a long release can pass. The frame cannot weigh the two without the code in front of it, and the result is the same set in the same shape either way | the form that keeps today's fallback: where any call cannot answer, the note goes out as the theme line and the fragments alone, and the log says so | open |
| Q2 | Whether the hotfix route into `main`, the row *a hotfix branch, `main`, 3-way merge* of `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, is removed. #1671 does not ask for it. The tree shows what each shape costs under the rulesets as they stand (`frame/design.md` G4, G5 (d)), and the rulesets are the owner's settings outside the tree, so which cost the release process takes is the owner's | a person | **(a) Removed.** An urgent fix squashes into `release/next` and the release is cut then; `release/next` holds cleared work alone, so cutting early ships nothing unfinished, and it costs one version pull request's wait. **(b) Kept for a change outside what ships.** A hotfix into `main` that changes no path the version step's list holds (`skills`, `agents`, `hooks`, `lib`, `templates`, `bin`, `docs`, `.claude-plugin`) moves no version: the version step prints *nothing that ships changed* and exits 0 (`.github/workflows/hygiene.yml`, read), `tag_release.py` tags nothing, and `plugin.json` does not conflict. A shipping fix still goes by (a): one that moved no version would be refused by the version step, and merged it would reach every installed copy untagged and unannounced. `release/next` lacks the fix until the next release merges, and a line both changed conflicts then. **(c) Kept as today, with a version move.** The next release pull request conflicts on `plugin.json` (G5 (d)), and no pull request into `release/next` can resolve it while the `release` ruleset takes squashes alone, so it needs a ruleset change, such as a merge method or a bypass actor on `release/**/*`. Under (b) or (c), `release_completeness_check.py`'s `L \ D` arm also needs to be judged only where the head is `release/next`, since a hotfix's `D` holds none of the `merged: next` issues and the arm would fail it | (a), as `frame/design.md` builds it. No phase's code reads the answer except that one arm. The hotfix row, the paragraph on it and the sentence *Nothing reaches `main` but the release pull request* are rule changes the settle writes. So (b) or (c) is a fold of those three `## Rule changes` operations and one guard on *Scope* item 3's arm, due before the last round reads the build | answered 2026-11-28 by the owner: (a) |
