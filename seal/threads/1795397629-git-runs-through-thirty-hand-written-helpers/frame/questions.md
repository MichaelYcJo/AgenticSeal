# Questions for the planner: 1795397629-git-runs-through-thirty-hand-written-helpers

The judgments the issue left open that the tree answered, each with its grounds where it stands:

- The runner's interface: `plan.md` *Alternatives considered* A2, A3 and A4.
- Where the `gh` runner stands: `plan.md` A7.
- The bound one command may take: `plan.md` A5 and A6.
- Which scripts load nothing from `lib/` at import: `frame/design.md` *Grounding* G17.
- The order the call sites move in: `plan.md` A13.
- `seal mode`'s exit code where its stage step did not happen: `plan.md` A10.
- `seal export`'s exit code where git did not answer for a manifest field: `frame/design.md` G12 and `plan.md` A11.
- The closer's `run`: `frame/design.md` G19.
- A census of git and `gh` calls outside the runner: `plan.md` A8.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does any git or `gh` command the suite's cases start take close to `lib/gitcmd.py#TIMEOUT` on the CI legs, the Windows leg above all? No probe here can run another platform's leg; the reads measured on this machine take 0.02 s at most (`frame/design.md` G13) | a measurement: the pull request's CI run and the orchestrator's broad run, where a case failing with the runner's `did not finish within 60 s` line is the answer | None does: `TIMEOUT` stays 60. One does: `TIMEOUT` rises in `lib/gitcmd.py` alone, and the measurement goes beside the constant | 60 | open |
| Q2 | For each case that intercepts a moved call through `<module>.subprocess.run`, or asserts a moved call's argv (`plan.md` *Technical context*, the constraints), does it patch `gitcmd.subprocess.run`, raise at the runner, or assert the arguments after `-C <root>`? Which script keeps `import subprocess` is known only when the phase that moves its calls writes them | the work: the phase that moves the call decides and records it in its phase record | Patch at the runner: the case holds wherever the script's imports end up. Keep the patch on the script's module: it holds only while that module imports `subprocess` | Patch `gitcmd.subprocess.run` where the script no longer imports `subprocess`, and leave the case as it is where it does | open |
