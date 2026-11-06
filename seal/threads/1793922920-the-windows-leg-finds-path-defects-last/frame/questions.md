# Questions for the planner: 1793922920-the-windows-leg-finds-path-defects-last

The judgments the issues left open that the tree answered, each with its
grounds where it stands:

- Whether the census reads literal arguments only, or constants too: `plan.md` *Alternatives considered*, rows 1, 2 and 3.
- Whether the census covers the four roots #103 names or every tracked `.py`: `frame/design.md` *Grounding*, the row on `tests/censuses.py` and the `encoding` census.
- Whether #103's second ask, the checklist question, is built: `plan.md` *Alternatives considered*, row 8.
- Whether the Windows claim is dropped: `plan.md` *Alternatives considered*, row 6.
- Which of #32's named units still stand, and whether its exemption for `chain_check.py` is owed: `frame/design.md` *Grounding*, the row on #32 against the tree.
- Which path tests are gated on the platform: `frame/design.md` *Grounding*, the row on the `git grep` of every platform gate.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Do the three link cases of Scope item 5 pass on the `windows-latest` shards once their platform gate goes? The tree cannot say, because they have never run there, and no probe can run on Windows from this machine | a measurement | Passed: phase 2 is done. Failed: the case or `skills/verify/scripts/pytest_record/agentic_pytest_record.py`'s reading of a linked path is wrong on Windows, and the defect is repaired in this work item before the rounds settle, as `skills/code-review/orchestration.md` *Where the work's risk is platform-specific* says. Skipped: the runner lost the privilege #1221 read, and the skip is recorded with pytest's reason | They pass. The orchestrator reads them on the dispatched run of `tests` before the broad run | open |
| Q2 | Should every work item routed to open a pull request run the other platforms by `workflow_dispatch` before the broad run, and not only one whose risk is platform-specific? This departs from the owner's decision recorded in #943 (`b196fe9b`), so the tree cannot answer it: no document outranks that decision, and only its maker can reverse it. The reading of the 60 failed runs of 2026-10-16 to 2026-11-05 (`frame/design.md` *Grounding*) found four branches whose Windows-only failure arrived at the pull request, after the sealer: 1374, 1177, 1051 and 969. A fifth, 986, found its own on a dispatched run before its pull request | a person | Keep the stated limit: nothing changes, and a one-platform defect in work nobody expected to be platform-specific keeps costing a verifying round, a broad run and a second sealer. Make the step unconditional in this repository: the paragraph of `skills/code-review/orchestration.md` that opens *Where the work's risk is platform-specific* is rewritten in a work item of its own, and each work item pays one run of every leg while its rounds run | Keep the stated limit. This work item builds nothing for it | open |
