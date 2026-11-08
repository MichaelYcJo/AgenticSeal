# Implementation Plan: a frame names its overlap with the release's other work items (#1443)

## Technical context

The tree as read at `94d04d30`.

The work edits four instruction files and adds one case. Each edit site:

- `agents/framer.md` lines 54 to 81 are *Order of work* step 4, the framer's wide reading; lines 94 to 110 are step 8, the hand-back list. *Scope* items 2 and 3 add to these two steps and leave the *Rules* section alone.
- `skills/implement/orchestration.md` lines 376 to 394 are the paragraph opening **Which branch the pull request lands on is decided with the routing question** (`frame/design.md` *Grounding* G1). Lines 388 and 389 hold the heuristic `## Removes` names. Nothing in `tests/` or `evals/` quotes this paragraph (`executed`: `git grep -n` for its opening words over `tests` and `evals` exited 1).
- `skills/code-review/orchestration.md` lines 317 to 330 are the paragraph opening **A conflict with the base is integrated by merging the base into the branch, never by a rebase** (G2), whose four phrases `tests/text/test_the_rules_have_one_owner.py` lines 335 to 339 assert. *Scope* item 5 adds sentences and rewrites none of those four phrases.
- `templates/records/sdd-plan.md` line 21 is `## Operational impact`; the new section goes immediately above it. `tests/behaviour/test_the_set_a_work_item_always_has.py` lines 237 to 256 hold the two existing template pins, and the case of *Scope* item 6 joins them in their shape.

Constraints. The policy root is `docs/` and none of these files is in it, so the work edits them in place and states no rule change (G14). A cited section in italics must stand in its file, which `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads, so every new citation of *Overlap with the release* names a heading that exists once the template carries it. `skills/settle/scripts/settle.py` names a heading near *Judgments of the run*; the new heading shares no words with it.

Failure scenario of the chosen approach, six months on. Framers drawn side by side guess each other's files from the issues, as this frame had to (G16). A guessed row can name an overlap the sibling's real diff does not have, or miss one it does. The orchestrator then merges in an order resting on a guess. The rewritten G1 paragraph answers a contradiction between two plans with a *Judgments of the run* row. A miss both plans share still meets at the merge, where G2's paragraph integrates it as it does today, so the worst case costs what today costs. A second failure is habit: the section filled with "none meets" by rote. The settle reads that against the merges that met unnamed, under `skills/core/SKILL.md` *The rule a mechanism is kept against*.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Each framer names its overlap in a new plan section; the orchestrator merges in the stated order and resolves disagreement with a *Judgments of the run* row; the later item of an ordered pair takes the base in before its next round or broad run | Rows built on guessed sibling files (see *Technical context*); a miss both plans share meets at the merge as it does today | Chosen. The framer has read the tree wide already (`skills/core/SKILL.md` *Each agent judges its own target, independently of the others*), the grounds are written where the settle reads them, and the ticket's *Done when* asks that a frame name it. |
| B. Keep the structure: the orchestrator alone chooses which item merges first, by the heuristic in G1, after reading every frame | The orchestrator re-derives six frames' overlaps in its own context at the frame read, as #1283's collision was found (G11), and nothing records the grounds; G10 is this choice made without the overlap in view | Rejected. The premise that keeps it, that the orchestrator sees the overlap before the merge, failed in G9, G10 and G11. |
| C. A script lists the files each frame's *Scope* names and reports pairs that share one | G9's overlap shared no file: #1390 added a check over the whole tree and #1389's content met it, so a path comparison passes it; and a script that reads paths out of prose is the grammar `skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest* rules out | Rejected. Whether two changes meet is a judgment of meaning. |
| D. Codify the owner's pace (G12): an item that shares a file with an item ordered before it waits to build until that item lands | By the spawn's guessed lists (G16), every one of the six items of 0.36.0 shares a file with another, so under the pace the release would build mostly in sequence, though a pair that edits different sections of one file merges without a conflict; the wait costs wall time the take-in of *Scope* item 5 does not | Rejected as a rule. The plan's row tells the orchestrator which items meet and where, so it weighs waiting per release, as this release's `routing.md` records the owner choosing "where their files allow". |
| E. Write the overlap in `frame/design.md` *Grounding* or *Scope* | The merge order is how the work lands, not what it is; the orchestrator reads `frame/plan.md` at the spawn and gives the version move from *Operational impact*, next to which the new section stands | Rejected. |
| F. Require branches to be up to date in the `release` ruleset | `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* gives it: the second item merges the base in after its broad run and seal, and runs both again | Rejected, on that paragraph's grounds (G3). |
| G. Replace G2's merge-on-conflict rule: every branch takes the base in before its broad run wherever the base has moved | Each sibling that lands puts a merge into every open branch, five merges in a six-item release, and each conflict outside the records owes a verifying round, though most squashes bring nothing a branch's checks read | Rejected. G2's rule is kept with the ordered pair's timing added. The premise that keeps it is that an overlap no frame named is rare. That premise was checked against three logged cases only (G9 to G11), each nameable at framing, so it is a sample, and the settle reads it again against the merges of the releases that follow. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6 | The case of *Scope* item 6 shown red with the template section removed, then green; the narrow run `skills/verify/SKILL.md` gives for the changed paths, with `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/text/test_the_rules_have_one_owner.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` among it; *User scenarios* S1 to S5 read against the diff | |

## Overlap with the release

The spawn named five other work items of `release: 0.36.0`: #1439, #1440, #1441, #1442 and #1444. None of their frames stood when this frame was written (G16), so the rows below rest on their issue bodies and the spawn's guessed file lists, and are `unverified` until those frames stand; the orchestrator answers them by reading the six plans. #1439 and #1441 meet this work nowhere: neither issue nor the spawn's list names a file this work edits, and neither changes a rule this work's text reads.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1440 | `agents/framer.md`: this work adds to *Order of work* steps 4 and 8; #1440's issue weighs "a definition step that opens every file it names in one call", which lands in *Order of work* or in the rule *Bound each call, not the reading* | #1443 | This work's edit to the file is two additions to two steps and its whole diff is text; #1440 carries `session_cost.py` and its cases, so its rounds are likelier to run later and can read the integration inside a round they spend anyway. Where both rewrite step 4, the later one's next round reads the merge. |
| #1442 | `skills/implement/orchestration.md`: this work, *Orchestrator: how the work is routed* (G1's paragraph); #1442, the fold paragraph of *Orchestrator: the order inside a ticket*. `skills/code-review/orchestration.md`: this work, G2's paragraph; #1442, the fold paragraph of *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*. Where #1442 routes a fold through the framer, as its issue weighs, it also meets `agents/framer.md` *Rules* | #1443 | The two items edit different sections of both shared files, so git should merge them without a conflict, and neither rule reads the other's. This work's diff is the smaller, which puts the take-in on the item more likely to still be in rounds. |
| #1444 | `skills/code-review/orchestration.md`: this work, G2's paragraph; #1444, by its issue, where a `.test_durations` refresh is read, which may be the paragraph opening **Two commits after the build are yours**, the one that names the commit integrating a sibling's squash | #1443 | Different sections of one file. If #1444 rewrites that paragraph, the merge commit *Scope* item 5 times is still the commit that paragraph names, so the later item reads the earlier one's sentence in its next round; the order costs little either way, and the smaller diff goes first. |

## Operational impact

The work changes instruction text, a template and one case: no migration, no environment variable, no dependency. It carries the release's version move: phase 1's crafter moves `.claude-plugin/plugin.json` from `0.35.1` to `0.36.0` in the commit that adds the work item's `changelog.md`, as `docs/releasing/branch-and-release.md` *The version moves at the start of a release, in the first pull request into `release/vX.Y.Z`* states.

## Judgments of the run

<the orchestrator's row for each judgment it makes in the run: a round spawned past the default or the run ended, a regression's route, a leftover's home, a decision folded into the frame, why the pull request title takes its prefix, which `pr.md` quotes; the grounds in one or two sentences, and the document judged against as its backticked path and italic heading>

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-09 | This work item carries the move to 0.36.0, folded into *Operational impact* before phase 1 spawns. | It is one phase of text and one case, and its *Overlap with the release* orders it before #1440, #1442 and #1444, so it is the item the orchestrator expects to merge first. | `skills/implement/orchestration.md` *Orchestrator: how the work is routed* |
