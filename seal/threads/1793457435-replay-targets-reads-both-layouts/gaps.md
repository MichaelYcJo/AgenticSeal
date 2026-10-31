# Closing memo: 1793457435-replay-targets-reads-both-layouts

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and format check at the work item's head: phases 1 and 2 each ran its phase-boundary set and checked its changed files alone (contract rule 2) | the orchestrator, by `seal gate` after the review rounds settle |
| Scenario 4's clone run over v0.27.0 and v0.26.0 after round 1's fix pass. It was not run again. The fix pass changes `blocked` only for a record in which the parser accepts no `seal` block, and round 1 found that each of the 10 records holding a `seal` opener at any release tag parses (read, not executed) | the sealer, when it samples the crafters' claims |

## Not done

`seed_defects.py --case` names nothing on stderr for a name that no shipped commit answers while another named commit holds a round 1 record. With `--list` it then exits 0, and without it exits 1. `replay_targets.py` now names such a name in both runs. The frame's scope item 4 gives `seed_defects.py` the empty-read line alone, and naming each case there adds a stderr line that the frame does not give. The fix pass for round 1's finding 1 left it for the orchestrator to place.
