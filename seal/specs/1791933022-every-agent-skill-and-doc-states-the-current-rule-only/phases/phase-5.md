# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 5

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | d3da26dd, the last build commit; this record's commit follows it |

## What this phase was asked

`plan.md`'s row 5, part A's close, with one addition the orchestrator made at
the spawn. **Q7, built with its default**, which the orchestrator took under
the owner's `automation` routing with the owner away: an item is judged at
the pull request that carries it. A pull request into `main` judges the
declarations naming its head branch and the ones its own commits changed,
never an item squashed into the release branch. Mark Q7 answered by default
for the owner to confirm. Build it in `chain_check.py` with cases seen red
first, state it once in `docs/the-review-record.md`, correct
`skills/settle/SKILL.md` where it said squashed records are read at the
release pull request, and re-run phase 4's probe against a scratch merge of
this branch into the release branch.

Then the close: `overview.md` saying what part A did and did not do, its
divergences and its Not verified rows with an answerer each; this item's
`changelog.md` fragment in plain words a plugin user reads; `questions.md`
rows the work answered; `plan.md`'s Status for phase 5. Part B is not
started. No round records, no push, no full suite.

## What this phase found

**"Its own commits" is told from a squash by the commit's signature.** Git
records no pull request for a commit. GitHub's squash merge is committed by
`noreply@github.com` and its subject ends `(#N)`, and both are needed: this
repository's own commits end `(#<issue>)` as well, so the subject alone would
read every commit of an item branch as a squash. `carried_by` returns the
squash only where every commit after the base that touched the declaration
carries both marks; any other commit, an uncommitted edit under
`--worktree`, or no commit leaves the declaration judged. It errs loud for a
squash a person committed and quiet for a commit forged under GitHub's
identity, and `docs/the-review-record.md` says so.

**The rule needed no `main`.** An item branch's range holds no GitHub squash
its base lacks, so applying `carried_by` on every pull request changes
nothing there, and the check names no branch it would have to assume a
plugin user's repository also releases to.

**The probe, on a scratch clone.** This branch at 42167a09 was squashed onto
`release/v0.22.0` (ce448bbe) under GitHub's committer identity as
`chore: #923 part A (#999)`, and judged as a ready pull request with
`GITHUB_HEAD_REF=release/v0.22.0` and `--baseline origin/main` (`executed`):

| Check | Exit | What it printed |
|---|---|---|
| `chain_check.py` at af4d0c31 | 1 | 15 refusals over five items: the four 0.22.0 items' last `Target SHA` *which HEAD does not descend from*, no `broad-gate.md` and no `guarantee.md` for each, and this item's missing round |
| `chain_check.py` at 42167a09 | 0 | five notices, each `judged at its own pull request` with its squash (f975ea66, ce448bbe, 642441fc, 5b1f6fae and the scratch squash), then *declared neither way* |
| the same, after a commit made on the release branch itself appended a line to this item's `routing.md` | 1 | the four 0.22.0 items named and left; this item judged: no round, no `broad-gate.md`, no `guarantee.md` |

**Red first, and the mutations.** Before `carried_by` existed, three of the
four new cases failed: both `TestCarriedBy` cases and the release case, which
refused the squashed item as *which HEAD does not descend from*. The fourth,
`test_an_item_the_release_pull_requests_own_commit_changes_is_judged`, pins
behaviour that already held and passed. Eight breaks through
`mutation-check` were each `red`: the committer test removed, the subject
test removed, the subject's end anchor removed, only the oldest commit read
(the case that passed before the code), the head-branch exception removed,
the `--worktree` edit ignored, the empty-history guard removed, and the
notices never printed.

**New tests, against their groups.** `carried_by` is a new function, so
`TestCarriedBy` is its group, one good case and one with the four inputs
that leave a declaration judged. The two `TestMain` cases are the first in
that group to run a release branch: no earlier case had a squash in its
range.

**The changelog fragment did not exist, and two of the items the spawn listed
for it are stated elsewhere.** `rules --check` and the release table are in
`1791876665…/changelog.md`, which phase 2 rewrote and attributed to #930 and
#923, and no released version carried a budget, so this fragment states
neither (`overview.md`).

**S19 holds over part A.** `grep -c -E "AskUserQuestion|input\("` over the
added lines of `git diff origin/release/v0.22.0...HEAD`, records and
changelog excluded, counted 0 (`executed`).
