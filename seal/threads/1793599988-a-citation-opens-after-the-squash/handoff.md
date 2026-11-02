# Handoff: 1793599988-a-citation-opens-after-the-squash (#1270)

Written 2026-11-02 by the orchestrator, to move the work to a new session. The session that takes it over reads this file once and deletes it in its first commit.

## Where it stands

- Phase 1 is built: `tests/text/test_a_cited_commit_outlives_the_squash.py`, and #1235's frame citation moved to the squash 48d035aa.
- The rounds have settled. Round 1 opened two `should` findings; round 2 confirmed one and reopened the other; round 3 confirmed round 2's fix and opened nothing. `frame/plan.md` *Judgments of the run* records why the run stopped there.
- No broad run, no `trail/gate.md`, no `guarantee.md`. The branch is pushed. No pull request is open.

## The release around it

- The release milestone was renamed from `release: 0.28.1` to `release: 0.29.0` on 2026-11-02 (#1299 is a `feat:`). The base branch is `release/v0.29.0`, cut at 40e6c23e.
- #898 goes first. This item's new check runs in every branch's suite: once #898 and any sibling merge, a frame or shipped file citing a feature branch's own `<sha>:<path>` fails it.

## Next steps, in order

1. Put routing question 1 through `AskUserQuestion` again, alone, before the first spawn; `routing.md` already holds the boxes.
2. Once #898 has merged, merge `origin/release/v0.29.0` into this branch (never rebase) and run the tree case. That answers *Scope* item 6 and `frame/questions.md` Q1: a citation it refuses is fixed here the way item 5 was, listed in a record, and owes a verifying round where it touched a file outside the records.
3. `seal gate --preflight --base release/v0.29.0`, then `seal gate --base release/v0.29.0 --record 1793599988-a-citation-opens-after-the-squash`; commit `trail/gate.md`.
4. `seal pr-body`, the sealer, the pull request into `release/v0.29.0`, squash-merge on green CI. Read the Windows leg.

## Facts a new session needs

- The open issue bodies #1234, #1236, #1255 and #1256 still cite 79252e48; the frame leaves them to the orchestrator, and no tree check reads them.
- Commits end with `Seal-Routing: 1793599988-a-citation-opens-after-the-squash`. The earliest commits of this branch lack it; chain-check does not judge them.
