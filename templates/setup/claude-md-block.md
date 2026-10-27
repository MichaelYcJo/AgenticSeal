<!-- agentic:start -->
## Tooling
- Python: prefer uv. Node.js: prefer pnpm. A project's own manager wins.

## Safety
- **3+ Fix Rule**: after three failed fixes of one bug, stop, rethink the architecture, then ask.
- **Verification Gate**: no claim of done, fixed or passes without running the check that proves it and reading its full output.
- **Verification Scope**: narrow and often; the full suite, the repository-wide lint and the typecheck run once, after the review rounds settle, and an edit after that run spends it.

## Session cost
- **Batch independent reads and runs**: every coordinate a task names in one call, every case from one file in one command. Never cut the investigation.

## Git
- Before each commit, run lint, format and typecheck over the files it changes.
- Worktrees only for concurrent sessions on one tree; otherwise `git switch`.
- **Routing, decided at the start.** Where `seal/`, its `README.md` opening with the marker, exists at neither `<repo>/seal/` nor `$(git rev-parse --git-common-dir)/seal/`, first follow the Bootstrap section of `skills/implement/orchestration.md`; where the root lands is the user's decision. **Ask question 1 alone; the boxes in a second call only under `per axis`.** Its answers are `automation`, `per axis` and `no work item`, and that file's *Orchestrator: how the work is routed* states the question and the boxes. Except under `no work item`, write `seal/threads/<work-item-id>/routing.md` from `templates/records/sdd-routing.md` before the first edit, in a command of its own, then commit it. Under `no work item`, run `seal no-work-item` before the first edit, and where the root is shared (`<repo>/seal/`), end every commit with the trailer `Seal-Routing: no work item`.
<!-- agentic:end -->
