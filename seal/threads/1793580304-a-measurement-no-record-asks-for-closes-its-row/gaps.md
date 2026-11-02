# Closing memo: 1793580304-a-measurement-no-record-asks-for-closes-its-row

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran the modules `trail/phases/phase-1.md` names | the orchestrator, by `seal gate --base <base> --record <item>` once the review rounds settle |
| Whether a settling session closes a row as *a measurement no record asks for* only where nothing on record depends on its answer, and re-homes the rest with the record that needs each answer in the issue body (`frame/design.md` S1 and S2). No settle has run under the rule yet, and no case can read that judgment | the settling session of the settle after this release, and the owner, reading that settle's pull request body, which lists each row by kind with what closed it |
| That `chain-check` reads this design's `## Rule changes` as one `change` and refuses nothing (`frame/design.md` S5). The framer ran probe P1 through the same reader at `0633f9a5`; the build changed no line of the design and did not run the check | `chain-check` in CI at the pull request |

## Not done

No case compares the four kinds that `ROWS_HEADING` names with the four
rows of step 6's table. Each is pinned on its own: the order case reads the
table, and the heading pin reads the constant. A later edit that adds a
fifth kind to one and not the other passes both. `frame/plan.md` weighed
that failure and chose no such case, because a case comparing the two would
be a mechanism with no catch on record (`skills/core/SKILL.md` *The rule a
mechanism is kept against*).

`README.md:265` and `README.ko.md:259` stand as they were. Each `seal
settle` row says the dry run lists every open row, and neither names a kind
(design G15).
