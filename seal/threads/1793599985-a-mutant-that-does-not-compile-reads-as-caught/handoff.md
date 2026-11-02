# Handoff: 1793599985-a-mutant-that-does-not-compile-reads-as-caught (#898)

Written 2026-11-02 by the orchestrator, to move the work to a new session. The session that takes it over reads this file once and deletes it in its first commit.

## Where it stands

- Phase 1 (the compile refusal) and phase 2 (the changelog fragment and the version) are built. The orchestrator moved `.claude-plugin/plugin.json` on to 0.29.0 (0b37d14a) after the release was renamed.
- Round 1 opened two `should` findings, fixed at edc09b4c. Round 2, the verifying round, confirmed both and opened two `should` findings: `dont_inherit=True` unpinned (fixed by the crafter at f8532a37) and five stale 0.28.1 sentences in the records (fixed by the orchestrator at dd9ec76d). The fix pass's close blocks are committed at 40c33242.
- One more stale line, `frame/plan.md:14`, which the fix pass named and could not edit, is corrected in the commit that adds this file.
- **A verifying round 3 is owed** for f8532a37, which touched `tests/skills/test_mutation_check.py` and a docstring in `skills/verify/scripts/mutation_check.py`. Its target is `<HEAD>, fixes 46775ced..<HEAD>`.
- No broad run, no `trail/gate.md`, no `guarantee.md`. The branch is pushed. No pull request is open.

## The release around it

- The release milestone was renamed from `release: 0.28.1` to `release: 0.29.0` on 2026-11-02, because #1299 is a `feat:` and a patch carries none. The base branch is `release/v0.29.0`, cut at 40e6c23e. `release/v0.28.1` still stands at the same commit and is not used.
- This is the release's first pull request: #1289 and #1299 wait for it to merge, and the rounds of #883, #1283 and #1270 use this branch's `bin/seal mutate` until 0.29.0 is installed.

## Next steps, in order

1. Put routing question 1 through `AskUserQuestion` again, alone, before the first spawn (`skills/implement/orchestration.md` *Question 1*); `routing.md` already holds the boxes.
2. Spawn the proofer for verifying round 3 on 46775ced..HEAD. Mutants run with this branch's own `bin/seal mutate`.
3. Once the rounds settle: `seal gate --preflight --base release/v0.29.0`, then `seal gate --base release/v0.29.0 --record 1793599985-a-mutant-that-does-not-compile-reads-as-caught`; commit `trail/gate.md`.
4. `seal pr-body`, the orchestrator's part, the sealer, then the pull request into `release/v0.29.0`; squash-merge once CI is green (the owner's answer for this release). Read the Windows legs for `frame/questions.md` Q1.

## Facts a new session needs

- Commits end with `Seal-Routing: 1793599985-a-mutant-that-does-not-compile-reads-as-caught`. The first five commits of this branch lack it; chain-check does not judge them.
- `frame/plan.md` *Judgments of the run* holds the version move and its grounds.
