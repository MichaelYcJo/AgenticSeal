# Handoff: 1793599990-each-result-is-a-badge (#1299)

Written 2026-11-02 by the orchestrator, to move the work to a new session. The session that takes it over reads this file once and deletes it in its first commit.

## Where it stands

- The rounds have settled. Round 1 opened two `should` findings, fixed at 2a82f15a; round 2, the verifying round, confirmed both and opened one `should` located in the frame (*Scope* item 6), which the orchestrator fixed at 9db877db and the fix pass closed `fixed 9db877db`. The orchestrator then folded the unescaped badge URL into *Scope* item 2 (a1116ee9), a records-only commit. HEAD is a1116ee9.
- `chain_check.py --baseline origin/release/v0.28.1 --root . --worktree` exited 0 at a1116ee9 and named only the missing `trail/gate.md` and `guarantee.md` (executed). The broad run has not been taken.
- The branch is pushed. No pull request is open.

## The release around it

- This item is the release's one `feat:`. The owner placed it in the release, and the release milestone was renamed from `release: 0.28.1` to `release: 0.29.0` on 2026-11-02 so it can carry it (`docs/branch-and-release.md` *Work accumulates on a release branch*); 0.29.0 and 0.30.0 moved one step forward. The base branch is `release/v0.29.0`, cut at 40e6c23e.
- #898 is the release's first pull request and carries `.claude-plugin/plugin.json` at 0.29.0. This item waits for #898 to merge.
- #1283 edits the `git log` calls of `.github/scripts/publish_release_note.py` and stubs in `tests/github/test_publish_release_note.py`, beside this item's header helpers and cases. Whichever lands second merges the release branch in; a conflict resolved outside this work item's records owes a verifying round on the resolution.

## Next steps, in order

1. Put routing question 1 through `AskUserQuestion` again, alone, before the first spawn (`skills/implement/orchestration.md` *Question 1*); `routing.md` already holds the boxes.
2. Once #898 has merged, merge `origin/release/v0.29.0` into this branch (never rebase).
3. `seal gate --preflight --base release/v0.29.0`, then `seal gate --base release/v0.29.0 --record 1793599990-each-result-is-a-badge`; commit `trail/gate.md`.
4. `seal pr-body` into a scratch body file, the orchestrator's part above the heading, then spawn the sealer; on `sealed`, open the pull request into `release/v0.29.0` and squash-merge it once CI is green.

## Facts a new session needs

- `frame/questions.md` Q1 (a browser shows the `alt` text when a badge cannot be served) stays open as a measurement after the release: the owner opens 0.29.0's note with images blocked.
- Commits in this shared root end with `Seal-Routing: 1793599990-each-result-is-a-badge`. The earlier commits of this branch lack it; chain-check does not judge them.
- Agents that type a bare `seal` run the installed 0.28.0 plugin, whose `seal mutate` reads a mutant that does not compile as red (#898). Until 0.29.0 is installed, name a worktree's own `bin/seal` that holds #898.
