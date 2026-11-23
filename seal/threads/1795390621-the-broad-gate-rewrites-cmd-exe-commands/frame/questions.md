# Questions for the planner: the broad gate rewrites cmd.exe commands (#1577)

The judgments the issue left open that the tree answered, each with its grounds where it is held:

- Which forms the refusal reads: `plan.md` *Alternatives considered*, the first row, with `design.md` *Grounding* G2 and G13.
- Where the refusal lives: `plan.md` *Alternatives considered*, the row that keeps `not_as_written` as the one refusal.
- Where the documents say what is refused on Windows: `design.md` *Grounding* G7 and G15.
- What *this repository's own `Broad gate` row still runs on every leg of CI* asks of this work: `design.md` *Grounding* G9.
- How this repository's key is spelt: `plan.md` *Alternatives considered*, the row for `uv run --no-project tests/run_tests.py -q`, with `design.md` *Grounding* G10 to G12.
- Which of the rewriter's cases go: `design.md` *Removes*.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| M1 | Does `uvx ruff check . && uvx ruff format --check . && uv run --no-project tests/run_tests.py -q` run the suite under `cmd.exe` on Windows, with `PYTHONPATH` and `PYTEST_ADDOPTS` kept as the gate sets them? This environment has no Windows shell, so no probe here can run it, and CI runs no `seal gate`, so no CI leg runs the key either (`design.md` G9). `design.md` G12 is the macOS run | a measurement: one `seal gate` run on a Windows machine, such as the one #448 was measured on | It runs: nothing changes. It fails: the key takes another spelling with no directory in front of the suite command, from `plan.md` *Alternatives considered*, and the refusal is unchanged | The spelling of `design.md` *Scope* item 9 stands | open |
