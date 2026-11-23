# Closing memo: 1795405728-lib-routing-splits-a-row-on-an-escaped-pipe

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check, the broad gate, over phase 1's tree, whose runs covered the plan row's modules and the phase boundary set | the orchestrator, at the broad run after the review rounds settle |
| The full suite, the repository-wide lint and the format check, the broad gate, over phase 2's tree, whose runs covered the plan row's modules and the 141 test files of its phase boundary set | the orchestrator, at the broad run after the review rounds settle |

## Not done

Phases 1 and 2 took none of the items of phase 3 of `frame/plan.md`
*Phases*, which a later crafter builds.

Phase 2 ran no probe over the committed `routing.md` files, as phase 1's
S7 probe did. Phase 2 changes what a reader reads only where a file holds
one of the eight characters `str.splitlines` ends a line at and GFM does
not. `frame/design.md` G9 found none in any tracked `.md` file, and a scan
of the 795 tracked `.md` files at `be0de7118` found none either. The plan's
phase 2 row asks for no such probe.
