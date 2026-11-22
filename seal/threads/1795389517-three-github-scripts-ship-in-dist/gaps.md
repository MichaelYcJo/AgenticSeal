# Closing memo: 1795389517-three-github-scripts-ship-in-dist

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's HEAD after phase 1, which no agent runs (contract rule 2) | the orchestrator, at the broad gate |

## Not done

Phase 1: no case was written for `lib/closing.py#CLOSING`'s trailing `\b`, which mutant 3 of `trail/phases/phase-1.md` showed no case watches. It was within reach: one assertion that `Closes #12abc` claims nothing. The old file misses it too, so it is an old gap. `CONTRIBUTING.md` *The test layout* asks a rebuilt module's record to name an old gap, and asks a new case only where the old files kill a mutant the new file lets survive. Writing one here would add behaviour coverage beyond a move, which the phase's Delivers cell does not ask for.
