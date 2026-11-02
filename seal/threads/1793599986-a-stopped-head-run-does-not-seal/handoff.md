# Handoff: 1793599986-a-stopped-head-run-does-not-seal (#883)

Written 2026-11-02 by the orchestrator, to move the work to a new session. The session that takes it over reads this file once and deletes it in its first commit.

## Where it stands

- Phase 1 is built. Round 1 opened three `should` findings, all fixed; round 2, the verifying round, confirmed them and opened two `should` findings, both `regression: round-1#2` (the limit sentence held only for a row running pytest once, and the `to:` copied rule 3). The orchestrator routed them to an ordinary fix pass (`frame/plan.md` *Judgments of the run*, 2336ffb3). The fix pass fixed both at 3de5c6c8, and its close blocks are committed with this file.
- **Not yet done: the frame fold.** The round-2 close blocks' `answer:` lines carry exact replacements for `frame/design.md:72-79` (the end of the `to:`, which must name the two kinds of stop and point to `templates/setup/config.md` rule 3 rather than repeat it) and, optionally, the last sentence of the *Scope* Out bullet at `:37`. Fold them in a commit of its own, with one `frame/plan.md` *Judgments of the run* row, and run `rule_changes.parse` over the design with root `docs` and `rule_changes.copies` against rule 3 (the fix pass measured 0 shared 15-word runs for the proposed text).
- **Then a verifying round 3 is owed** on 3de5c6c8 and the fold: target `<HEAD>, fixes c00169dc..<HEAD>`.
- No broad run, no `trail/gate.md`, no `guarantee.md`. The branch is pushed. No pull request is open.

## The release around it

- The release milestone was renamed from `release: 0.28.1` to `release: 0.29.0` on 2026-11-02 (#1299 is a `feat:`). The base branch is `release/v0.29.0`, cut at 40e6c23e.
- #898 goes first; until 0.29.0 is installed, mutants run with `/Users/michael/Documents/GitHub/SpecSeal-worktrees/fix/898-a-mutant-that-does-not-compile-reads-as-caught/bin/seal mutate`, or this branch's own `bin/seal` once `release/v0.29.0` holds #898 and is merged in.
- #1283 changes only the `git` wrapper and the helper import in `skills/verify/scripts/broad_gate.py`; whichever lands second merges the release branch in.

## Next steps, in order

1. Put routing question 1 through `AskUserQuestion` again, alone, before the first spawn; `routing.md` already holds the boxes.
2. The frame fold above, then verifying round 3.
3. Once the rounds settle and #898 has merged, merge `origin/release/v0.29.0` in, then `seal gate --preflight --base release/v0.29.0` and `seal gate --base release/v0.29.0 --record 1793599986-a-stopped-head-run-does-not-seal`. That broad run also answers `frame/questions.md` Q1 (whether this repository's own `bin/test -q` leaves a stopped session at HEAD, which the new arm would fail).
4. `seal pr-body`, the sealer, the pull request into `release/v0.29.0`, squash-merge on green CI.

## For the owner to weigh (not this item's scope)

- The fix pass read, without a probe, that a `pytest_sessionfinish` hook running after the recorder's can turn a red session's exit of 1 into 0; the record keeps exit 1, which `RAN_TO_ITS_END` accepts, so the gate would pass that run on the row's exit. It predates #883. Whether it becomes its own issue is the owner's call.
- `broad_gate.py#NO_RECORD_CAUSES` does not name a configure-time stop; `gaps.md` *Not done* records it.

## Facts a new session needs

- Commits end with `Seal-Routing: 1793599986-a-stopped-head-run-does-not-seal`. The earliest commits of this branch lack it; chain-check does not judge them.
