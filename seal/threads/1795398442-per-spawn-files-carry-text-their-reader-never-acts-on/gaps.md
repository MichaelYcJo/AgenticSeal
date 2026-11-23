# Closing memo: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check, the broad gate, over phase 1's tree | the orchestrator, at the broad run after the review rounds settle |
| The same broad gate over phase 2's tree, whose runs covered only the plan row's modules and the phase boundary set | the orchestrator, at the broad run after the review rounds settle |

## Not done

Phase 1 adds no case that refuses a retired-number list written back into
the contract's preamble. `frame/design.md` S8 holds that absence with
`git grep -n -F 'retired numbers' -- skills`, run once at the build, and
*Scope* item 9 asks the case only to read the list from
`docs/running/the-agent-set.md`. A copy in the contract would sit beside
the one the case reads and leave it green, and catching that copy is
review's reading.
