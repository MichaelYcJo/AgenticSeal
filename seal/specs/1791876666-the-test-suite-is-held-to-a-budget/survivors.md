# 1791876666-the-test-suite-is-held-to-a-budget — survivors

| Path | Quote | Grounds |
|---|---|---|
| seal/specs/1791270161-the-broad-gate-reads-a-record-its-pytest-plugin-wrote/spec.md | `_pytest/runner.py` `call_and_report` (236) calls the first and then `pytest_runtest_logreport` in the same process | another work item's account of pytest's own runner, which still calls `pytest_runtest_logreport` after `pytest_runtest_makereport`; phase 3 moved the tracer's hook off it and corrected nothing that sentence states |
