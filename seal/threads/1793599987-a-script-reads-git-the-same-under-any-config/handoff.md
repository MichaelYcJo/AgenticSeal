# Handoff: 1793599987-a-script-reads-git-the-same-under-any-config (#1283)

Written 2026-11-02 by the orchestrator, to move the work to a new session. The session that takes it over reads this file once and deletes it in its first commit.

## Where it stands

- Both phases are built. Phase 1 (af574e8c to a5d80c7a): `hooks/lib/gitcmd.py#argv` holds five `-c` keys, and the 15 `log` and `status` calls in nine scripts go through it. Phase 2 (a77538b8, records at ac582265): six readers pass `-z`. `changelog.md` is written.
- The frame was settled in one exchange: the orchestrator proposed narrowing the helper from all 60 git calls to the `log` and `status` calls a measured key changes, and a reader in place of an `ast` pin; the framer agreed (the first) and agreed with a change (the second). The rejected first draft stands in `frame/plan.md` *Alternatives considered*.
- **No review round has run.** Round 1 is next, over the branch against `release/v0.29.0`.
- The branch is pushed. No pull request is open.

## The release around it

- The release milestone was renamed from `release: 0.28.1` to `release: 0.29.0` on 2026-11-02 (#1299 is a `feat:`). The base branch is `release/v0.29.0`, cut at 40e6c23e.
- #898 goes first. Until 0.29.0 is installed, mutants run with `/Users/michael/Documents/GitHub/SpecSeal-worktrees/fix/898-a-mutant-that-does-not-compile-reads-as-caught/bin/seal mutate`, or this branch's own `bin/seal` once `release/v0.29.0` holds #898 and is merged in.
- Files shared with siblings: `skills/verify/scripts/broad_gate.py` (#883; this item changes only the `git` wrapper and the helper import), `.github/scripts/publish_release_note.py` and `tests/github/test_publish_release_note.py` (#1299; this item changes `git`, `commit_message`, `fragments`' first `log`, one import, the stubs that matched `("git", "log")`, and one case). Whichever lands second merges the release branch in; a conflict resolved outside the work item's records owes a verifying round on the resolution.

## Next steps, in order

1. Put routing question 1 through `AskUserQuestion` again, alone, before the first spawn; `routing.md` already holds the boxes.
2. Spawn the proofer for round 1. Point it at `gaps.md`'s proofer rows: that every `log` and `status` call is built by `argv`, and that no other script takes paths out of git's output without `-z` (both crafters' searches were word samples).
3. Fix passes and verifying rounds until the run settles; then, with #898 merged, merge `origin/release/v0.29.0` in, `seal gate --preflight --base release/v0.29.0`, `seal gate --base release/v0.29.0 --record 1793599987-a-script-reads-git-the-same-under-any-config`.
4. `seal pr-body`, the sealer, the pull request into `release/v0.29.0`, squash-merge on green CI. Read the Windows and Linux legs for `frame/questions.md` Q1.

## Facts a new session needs

- Commits end with `Seal-Routing: 1793599987-a-script-reads-git-the-same-under-any-config`. The routing and frame commits lack it; chain-check does not judge them.
- The changelog's claim that the release workflow stops on signature words under `log.showSignature` comes from the framer's table and was not run (phase 2's hand-back).
