# 1791876667 — handoff

Written 2026-10-13 by the orchestrating session (Opus 5.5). The 0.22.0 run stopped after framing, as the owner asked; `smith` onward runs in a new session on another machine. Read this first, then `plan.md`.

## Where it stands

- `routing.md` committed (a04ba95b): `automation`, pressed by the owner for all three 0.22.0 items. Models: smith Opus 5.5, warden Opus 5.5, sealer Sonnet 5.5.
- Framed by `framer` on Fable 5.1 against #930's committed frame (826b7ec8), in parallel with #929 and without reading #929's frame. Committed here (d3df14ed). `questions.md` has no row only a person can answer.
- The frame removes the release checklist's refresh box and the 35-minute measuring run: every run's Windows shards record their part, a `durations` job unions them into a `test-durations` artifact, and `test_the_durations_file_prices_the_suite` gates both ways (unpriced cases, or dead seconds, past 1/20).
- This branch is pushed. No pull request is open.

## Not run in this segment

- Nothing was built and no check ran in this session. The frame's numbers are the framer's (`executed` at a04ba95b): 460 of 13,914 collected cases unpriced (3.31 %), about 16 PRs of margin to 5 %, shard spread 1.35 Windows / 1.28 macOS median on 16 PR runs.
- Phase 1 needs two CI waits (run, commit the union, run). The smith hands back at each push point and the session pushes and dispatches, as #874 did.

## Next

1. In the new session, put routing question 1 through `AskUserQuestion` again before the first spawn (`skills/implement/orchestration.md` §*Question 1*, the resume paragraph).
2. Show the owner the three `plan.md` files and take the approval. The two judgments the frame names as the owner's to overturn: phase 1 commits the union once, and the check's second direction (dead seconds).
3. Order: #930's phases 1–2 first; this item's phase 1 before #929's first deletion PR (#931 Q5).
4. #914's `workflow_dispatch` input has nothing left to run once this lands; whether #914 closes with this work is the owner's call at the PR.
5. Spawn `smith` on Opus 5.5, then `warden` on Opus 5.5 against `origin/release/v0.22.0`, then the sealer on Sonnet 5.5. The pull request goes into `release/v0.22.0` (squash) and carries `Closes #931`.
