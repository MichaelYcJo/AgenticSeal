# Questions for the planner: a red session a late hook hides does not pass (#1301)

The ticket left these judgments open, and the tree answered each of them:

- Whether the refusal is built or decided against: `frame/design.md` G6, and `frame/plan.md` *Alternatives considered*, the fifth row.
- Whether the pass is read off the `end` line or added as one more edge of the exit codes: `frame/plan.md` *Alternatives considered*, the first and second rows.
- Whether the late hook stays a named limit: `frame/design.md` G2 and G3.
- Whether the release seal or the base's words change: `frame/design.md` G9.
- Whether a row that masks or reruns a red pytest keeps passing: `frame/design.md` G6 and G10.

The frame assumes that the `exitstatus` pytest hands `pytest_sessionfinish` is the run loop's exit on every pytest the recorder supports. It was probed on 9.1.1 alone. A different answer on another build would turn the `early-exitstatus-0` shape of S2 red there, and it would not change what gets built.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the new cases of S1, S2 and S3 hold on the ubuntu and Windows legs of the test workflow? Each case starts a pytest subprocess whose conftest holds a hook, or whose row joins pytest to the interpreter by an escaped `\|\|`, which reaches `cmd.exe` on Windows. | a measurement | Green on every leg: nothing changes. Red on one leg: the phase that meets it either narrows the case to the shapes that leg runs, or skips the shell-composition shape where the row runs under `cmd.exe`, and records which. | Write the cases for every leg. The shell-composition shape uses the platform's own spelling or is skipped under `cmd.exe`, as the module's other shell cases are. | answered 2026-11-05 by the orchestrator: `gh workflow run tests` on b5d3d855, run 41924200504, concluded `success` on every leg, the four Windows, three macOS and one ubuntu `pytest` legs among them (executed: `gh run view 41924200504`) |

Q1's reason is that this frame ran on macOS. No probe of another platform's CI leg can run here, so a run of the `tests` workflow on the branch answers it.
