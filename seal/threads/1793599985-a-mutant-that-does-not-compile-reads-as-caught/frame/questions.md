# Questions for the planner: a mutant that does not compile reads as caught (#898)

The issue left these judgments open, and the tree answered each one. They are not reopened here:

- Compile the mutant first, and with what: `compile` over the bytes the write would put on disk, not `py_compile` and not `ast.parse` (`plan.md` *Alternatives considered* A1, A3 and A4; design G8c and G8d).
- The word a non-compiling mutant is refused with: the existing `refused` at exit 2, not a new `UNCOMPILED` (`plan.md` A2).
- Whether a red that came from a collection or import error is reported apart: each red line carries the cases' exit code, and the command decides nothing from it (design *Scope* item 4 and G5; `plan.md` A6 and A11).
- A batch holding one mutant that does not compile is refused whole (`plan.md` A7).
- A `.py` file that does not compile as it is gets no compile step and says so (`plan.md` A8; design *Scope* item 2).
- Only a `.py` target is compiled (design *Scope* item 3 and G10).
- How the rounds of #883 and #1283 reach the fixed command: through their worktree's `bin/seal` (design G11).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the new cases S1 to S7 pass on CI's `windows-latest` legs? | a measurement | Pass: nothing changes. Fail: the work fixes the case or the code before the sealer runs. No probe can answer it here, because this environment has no Windows interpreter. The compile itself is platform-independent Python, and the cases build their targets with `tmp_path`. | The build proceeds. The orchestrator reads the four Windows legs on the pull request's CI run. | open |
