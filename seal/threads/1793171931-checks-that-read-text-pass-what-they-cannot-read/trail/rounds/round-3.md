# Review round 3: 1793171931-checks-that-read-text-pass-what-they-cannot-read

target: 9ed8d649, fixes c5eddfb9..9ed8d649

This round verifies the fix pass over round 2, commits `bedaa645` and
`9ed8d649`, and stays inside that diff and the GitHub acts it names. Round
2 gave this round its coordinates: R8's cells at `phase-1.md:34` and
`phase-5.md:36`, the sentence at `phase-5.md:93`, and
`frame/design.md:276-282`. Each was opened again here, and the verdict was
reached again.

## Findings

None. The one finding of round 2 is answered below, and the fix diff
holds no new defect.

## Confirmations

confirms: round-2#1
The close holds. R8's `Fix` cell reads `#1121` at `phase-5.md:36` and
`0.24.1 chain_check.py` at `phase-1.md:34`, the way the other
`chain_check.py` rows read in each file. #1121's row in the issues table
names R3, R8, R9 and R11 (`phase-5.md:81`). The `#1038` sentence names R10,
R37 and R40 alone (`phase-5.md:93`). The sentence added to *R8 and R23
after review round 1* gives the reason from `frame/design.md:276-282`
(`phase-5.md:109-111`). A search of the work item's `gaps.md`, `frame/`
and `trail/phases/` for R8 beside `#1038` found nothing (executed, exit 1).
The answer's ground holds by reading. Refusing a near-miss key changes
`chain_check.py#routing_trailers` and `#trailer_findings` and their tests,
so no shared reader and no new gate is needed. `docs/the-routing-check.md:115-117`
is about a commit with no trailer at all.

The GitHub side holds. Executed: `gh api` read comment 6464431981. It
stands on #1121, which is open in `release: 0.24.1`. It adds R8 with its
probe, measured at `c825fd2c`, and says why the trailer rule at
`docs/the-routing-check.md:115-117` does not cover a near-miss key. It
adds one *Done when* line: `SealRouting:` refused at the pull request,
seen red against `c825fd2c`.

confirms: none
S7 holds after the second patch. Executed:
`gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`
returned a body updated at 2026-10-28T08:36:37Z. `cmp` of it against
`phase-5.md:25-73` exited 0, at 15,378 bytes each.

confirms: none
Both fix-pass commits, `bedaa645` and `9ed8d649`, carry
`Seal-Routing: 1793171931-checks-that-read-text-pass-what-they-cannot-read`
(executed, `git log --format=%(trailers:key=Seal-Routing,valueonly)`).
Round 2's row about the earlier commits is answered by the orchestrator's
decision not to rewrite them, since the round records name their SHAs.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464014816`, then `cmp` of its body against `phase-5.md` lines 25 to 73 | exit 0 for both; 15,378 bytes each; updated at 2026-10-28T08:36:37Z |
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6464431981`; `gh issue view 1121 --json milestone,state` | the comment stands on #1121 and adds R8 with a *Done when* line; #1121 is open in `release: 0.24.1` |
| `grep -rn -E` for R8 beside `#1038` over `gaps.md`, `frame` and `trail/phases` | exit 1, no line |
| `git log --format=%(trailers:key=Seal-Routing,valueonly) c5eddfb9..HEAD` | both commits carry the work item's trailer |
| `bin/seal layout --check` | exit 0; 159 files read, 0 refused |
