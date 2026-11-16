### Fixed

- **The framer runs each search it writes into a frame cell before the cell states the search's result (#1548).** A *Verified by* cell of `frame/plan.md`, or a *Verifiable how* cell of `frame/design.md`, can hold a search the build is to leave printing nothing, or only named lines. In the run of #1500 the framer wrote two such cells without running either search, and each crafter found that its search could not give the stated result: one matched two names the same plan keeps, the other matched lines the design left in place and the work item's own frame. `agents/framer.md` now has the framer run the search at the frame's commit and account for each line it prints as one the build removes, one the design keeps or one in a file the cell excludes, with the work item's own directory excluded or named. The cell states what that account leaves, and the run is recorded in `## Grounding`.
- The version moves to 0.38.2.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-16 | `agents/framer.md` *Rules*: a search the framer writes into a *Verified by* or *Verifiable how* cell is run at the frame's commit before the cell is written, each printed line is accounted for, and the cell states the result that account leaves | Two cells in #1500's frame stated results no build could give, and each cost a crafter's search for the cause and an orchestrator's fold after the build | https://github.com/MichaelYcJo/AgenticSeal/issues/1548 |
