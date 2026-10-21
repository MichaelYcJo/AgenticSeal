<!-- specseal:start -->
## Tooling
- Python: prefer uv. Node.js: prefer pnpm. A project's own manager wins.

## Safety
- **3+ Fix Rule**: after three failed fixes of one bug, stop, rethink the architecture, then ask.
- **Verification Gate**: no claim of done, fixed or passes without running the check that proves it and reading its full output.
- **Verification Scope**: narrow and often; the full suite, lint and typecheck run once, after the review rounds settle, and an edit after that run spends it.

## Session cost
- **Batch independent reads and runs**: every coordinate a task names in one call, every case from one file in one command. Never cut the investigation.

## Git
- Run lint, format and typecheck before committing.
- Worktrees only for concurrent sessions on one tree; otherwise `git switch`.
- **Routing, decided at the start.** Where `seal/` exists at neither `<repo>/seal/` nor `$(git rev-parse --git-common-dir)/seal/`, first follow the Bootstrap section of `skills/implement/orchestration.md`; where the root lands is the user's decision. **Ask question 1 alone; the boxes in a second call only under `per axis`.** Its answers are `automation`, `per axis` and `no work item`. Before the first edit, write `seal/specs/<work-item-id>/routing.md` from `templates/sdd-routing.md` in a command of its own, then commit it. Under `no work item`, every commit carries `: '[no-review]';` in front of it, `[no-parity]` too where a migration config is declared.
<!-- specseal:end -->
