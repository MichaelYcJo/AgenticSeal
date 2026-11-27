# Closing memo: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the format check, the broad gate, over phase 1's tree, whose runs covered the plan row's modules and the phase boundary set | answered: the work item's broad run, `trail/gate.md` at `69e3217ac` against `74ba63423`, on which `guarantee.md` sealed |
| closed The full suite, the repository-wide lint and the format check, the broad gate, over phase 2's tree, whose runs covered the plan row's modules and the 141 test files of its phase boundary set | answered: the work item's broad run, `trail/gate.md` at `69e3217ac` against `74ba63423`, on which `guarantee.md` sealed |
| closed The full suite, the repository-wide lint and the format check, the broad gate, over phase 3's tree, whose runs covered the plan row's modules and the 141 test files of its phase boundary set | answered: the work item's broad run, `trail/gate.md` at `69e3217ac` against `74ba63423`, on which `guarantee.md` sealed |

## Not done

Phase 2 ran no probe over the committed `routing.md` files, as phase 1's
S7 probe did. Phase 2 changes what a reader reads only where a file holds
one of the eight characters `str.splitlines` ends a line at and GFM does
not. `frame/design.md` G9 found none in any tracked `.md` file, and a scan
of the 795 tracked `.md` files at `be0de7118` found none either. The plan's
phase 2 row asks for no such probe.

Phase 3 left `docs/releasing/release-checklist.md` as it stands. Its
backtick lines at `:360-363` and the paragraph at `:365-366` stand six
spaces in under a list item, so a renderer shows them as one indented code
block, the paragraph among it (`trail/phases/phase-3.md`). The paragraph is
meant as prose. Re-indenting it is a change to a release document that this
issue does not ask for.
