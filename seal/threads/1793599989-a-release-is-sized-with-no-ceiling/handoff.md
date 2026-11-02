# Handoff: 1793599989-a-release-is-sized-with-no-ceiling (#1289)

Written 2026-11-02 by the orchestrator, to move the work to a new session. The session that takes it over reads this file once and deletes it in its first commit.

## Where it stands

- The rounds have settled. Round 1 opened three `should` findings, all fixed; round 2, the verifying round, confirmed all three and opened nothing. HEAD is 9a67c0a4.
- `seal gate --preflight --base release/v0.28.1` exited 0 at 9a67c0a4 (executed). The broad run has not been taken, so there is no `trail/gate.md` and no `guarantee.md`.
- The branch is pushed. No pull request is open.

## The release around it

- The release milestone was renamed from `release: 0.28.1` to `release: 0.29.0` on 2026-11-02, because #1299 is a `feat:` and a patch carries none (`docs/branch-and-release.md` *Work accumulates on a release branch*). The base branch is `release/v0.29.0`, cut at 40e6c23e. `release/v0.28.1` still stands at the same commit and is not used.
- #898 is the release's first pull request and carries `.claude-plugin/plugin.json` at 0.29.0. This item waits for #898 to merge into `release/v0.29.0`.

## Next steps, in order

1. Put routing question 1 through `AskUserQuestion` again, alone, before the first spawn (`skills/implement/orchestration.md` *Question 1*); `routing.md` already holds the boxes.
2. Once #898 has merged, merge `origin/release/v0.29.0` into this branch (never rebase). A merge that resolved no conflict outside this work item's records owes no verifying round.
3. `seal gate --preflight --base release/v0.29.0`, then `seal gate --base release/v0.29.0 --record 1793599989-a-release-is-sized-with-no-ceiling`; commit `trail/gate.md`.
4. `seal pr-body` into a scratch body file, the orchestrator's part above the heading, then spawn the sealer; on `sealed`, open the pull request into `release/v0.29.0` and squash-merge it once CI is green (the owner's answer for this release).

## Facts a new session needs

- Commits in this shared root end with `Seal-Routing: 1793599989-a-release-is-sized-with-no-ceiling`. The earlier commits of this branch lack it; `docs/the-routing-check.md` *At the pull request* says chain-check does not judge them.
- `frame/plan.md` *Judgments of the run* holds the fold of round 1's findings 1 and 2 into the design's `to`.
- Agents that type a bare `seal` run the installed 0.28.0 plugin, whose `seal mutate` reads a mutant that does not compile as red (#898). Until 0.29.0 is installed, name a worktree's own `bin/seal` that holds #898.
