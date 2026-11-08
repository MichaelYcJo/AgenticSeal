# Design: a frame names its overlap with the release's other work items (#1443)

## Grounding

The tree as read at `94d04d30`. A row marked `executed` was read by a
command the framer ran on 2026-11-09; every other row was opened and read.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, the paragraph opening **Which branch the pull request lands on is decided with the routing question** | The orchestrator alone chooses which of the release's side-by-side work items merges first, by the heuristic "the one likeliest to be sealed first, often the smallest diff", and gives that item the version move. Nothing records the grounds of that choice, and no party reads where the items meet before the merge. This is the paragraph *Scope* item 4 rewrites. |
| G2. `skills/code-review/orchestration.md` *Orchestrator: the pull request opens once the sealer seals*, the paragraph opening **A conflict with the base is integrated by merging the base into the branch, never by a rebase** | The orchestrator merges the base in once, after the branch whose changes conflict has landed. Where the merge resolved a conflict outside the records, a verifying round reads it, and the broad gate, `seal pr-body` and the sealer run again. `tests/text/test_the_rules_have_one_owner.py` lines 335 to 339 pin four phrases of this paragraph, among them "after the branch whose changes conflict with this one has landed" (`executed`: `grep -n`). *Scope* item 5 keeps every pinned phrase. |
| G3. `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*, the paragraph opening **Both rulesets require the `lint` job** | Neither ruleset requires a branch to be up to date with its base, because that would make the second of two side-by-side items merge the base in after its broad run and seal. That rationale stays true under this work, so the paragraph is not changed. |
| G4. `agents/framer.md` *Order of work* step 4 | The framer reads the policy, the `check:` lines, `seal/follow-up.md`, earlier work items, the latest *Process changes*, the ticket and `seal/parity.md`. It reads nothing of the release's other open work items, and step 8's hand-back names no overlap. This is the gap *Scope* items 2 and 3 fill. |
| G5. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, the paragraph opening **A decision made after the frame is committed is folded** | Its last sentence states what the framer's spawn prompt carries: the issue whole and one line on its comments. The list of the release's other work items is an input to the merge order, so *Scope* item 4 states it in G1's paragraph and leaves this sentence as it stands. |
| G6. `templates/records/sdd-plan.md` and its readers | The template holds *Technical context*, *Alternatives considered*, *Phases*, *Operational impact* and *Judgments of the run*. `tests/behaviour/test_the_set_a_work_item_always_has.py` pins the Phases header and the *Judgments of the run* heading and header. `skills/settle/scripts/settle.py` reads *Judgments of the run* by its heading and names a heading near it. `tests/skills/test_pr_body.py` line 39 uses *Operational impact* in a fixture. `agents/crafter.md` line 27 reads *Operational impact* for the version move (`executed`: `git grep -n`). A new section placed before *Operational impact* moves none of these readers. |
| G7. `skills/core/SKILL.md` *Each agent judges its own target, independently of the others* and *A document is cut by who opens it and at which step* | The framer judges what the work should be and has already read the tree wide. Where this work meets another item is part of that judgment, so the framer writes it, and the orchestrator reads one section of each plan instead of re-deriving it from six frames. |
| G8. `skills/core/SKILL.md` *The rule a mechanism is kept against* and `agents/framer.md` *A mark is not the answer to a blocked step* | The work adds a template section and a rule, so `## Removes` names what goes in return. The record the new section is kept against is G9 to G11. |
| G9. #1380, comment of 2026-11-05T06:41:27Z (`executed`: `gh issue view 1380 --json comments`) | 0.32.4: "#1390 took the most: the sealer withheld twice (... then a bare commit #1389's squash added to the base), so it ran four rounds, three broad runs and three sealer spawns. The second withholding was a sibling's defect that only the merged tree shows; the broad run reads the branch's own tree, so a branch that has not taken in its moved base meets it first at the sealer." `git log --oneline v0.32.3..v0.32.4` (`executed`) shows #1389's squash `703ab88c` landing before #1390's `3f6f2004`, and #1390's subject says it refuses a bare hash no main or release branch holds. So the two items did not share a file: #1390 added a check that reads the whole tree, and #1389's content met it. An overlap is therefore wider than a shared file. |
| G10. #1280, comment of 2026-11-02T03:40:11Z (`executed`: `gh issue view 1280 --json comments`) | 0.28.0: "A conflict made by #1139 merging first cost one round, a broad run and a sealer, which ordering #1217 before #1139 would have avoided." |
| G11. #1298, its second comment (`executed`: `gh issue view 1298 --json body,comments`) | 0.29.0: #1283 took two proposals at the frame read "on grounds of review load in the hooks and collisions with #883 and #1299 building in parallel". The collision was found by the orchestrator at the frame read, after six frames were drawn without knowing each other. |
| G12. The owner's pace of 2026-10-19, as the spawn prompt states it | Work items whose files do not meet run in parallel, and ones that share a file wait for the first to land. No document of the tree states it (`executed`: `git grep -n -i` for "share a file", "run in parallel" and "wait for the first" over `skills`, `docs`, `agents`, `templates` and `CONTRIBUTING.md` found no such rule). This release's `routing.md` *Why this way* records the owner's choice for 0.36.0: run side by side "where their files allow". `unverified` beyond the spawn's statement; the orchestrator answers it. |
| G13. The ticket's comments | None. The spawn's line says so, and `gh issue view 1443 --json comments` printed a count of 0 on 2026-11-09 (`executed`). |
| G14. The policy root and the unsettled designs | The policy root is `docs/` (no `Policy root` row in `seal/config.md`), indexed by `docs/README.md`. The three unsettled designs under `seal/threads/` each state the no-change block (`executed`: `sed` over their `## Rule changes`). No document of `docs/` states which side-by-side item merges first or what a framer reads (`executed`: `git grep -n` for "merges it first", "smallest diff" and "likeliest to be sealed" found only G1). |
| G15. The latest release's *Process changes* (`executed`: `gh release view --json body`) | Two rows of 2026-11-08: the transcript path under the config directory, and the parity surface read forward. Neither touches the merge order or the framer's reading of other work items. `seal/follow-up.md` holds no row on either. |
| G16. The release's other work items, as read on 2026-11-09 | Each sibling worktree held only an untracked `frame/design.md` skeleton with no scope written (`executed`: `ls` and `sed` over the five sibling frame directories). The overlap this frame states for itself (`frame/plan.md` *Overlap with the release*) therefore rests on the five issue bodies (`executed`: `gh issue view`) and the spawn's guessed file lists, and is `unverified` until their frames stand; the orchestrator answers it by reading the six plans. |

## Scope

In:

1. `templates/records/sdd-plan.md` gains a section `## Overlap with the release`, placed immediately before `## Operational impact`. Its shape is *Data & interfaces* below.
2. `agents/framer.md` *Order of work* step 4 reads the release's other open work items its spawn prompt names: each one's issue, and its frame where it stands, committed on its branch or merged on the release branch. The framer judges where its own work meets each of them. Two items meet where both change one file, or where one changes a rule, a check or a fact that the other's change reads or adds content to (the G9 shape). For each item it meets, the framer states which merges first and why, weighing which order puts the integration inside rounds the later item spends anyway. The heuristic the orchestrator used (G1) moves here as part of that weighing: the item likelier to be sealed first, often the smaller diff, goes first, and an item that adds a check reading the whole tree goes after the items whose content that check reads.
3. `agents/framer.md` *Order of work* step 8 gains one bullet: the hand-back names the overlap rows and the merge order the plan states.
4. `skills/implement/orchestration.md`, G1's paragraph, is rewritten in place to say four things. Where several work items of a release run side by side, the orchestrator's prompt that spawns each framer names the release's other work items: the issue, the branch, and the frame's path where it is committed. The orchestrator merges the items in the order their plans' *Overlap with the release* sections state. Where two plans state opposite orders for one pair, or where the item ordered first cannot be sealed before the other, the orchestrator chooses the order and writes the choice as a row of *Judgments of the run* in the plan of the item it merges out of the stated order. The version move goes to the item first in that order, and items that no plan orders against each other merge as each is sealed.
5. `skills/code-review/orchestration.md`, G2's paragraph, gains the timing for an ordered pair. Where a plan orders this branch after another item, the orchestrator merges the base into this branch once that item has landed, before this branch's next round, or before its broad run where its rounds have ended. So a round already owed reads the resolution, and the broad run and the sealer read the merged tree once. Every phrase G2 says the test pins stays.
6. One case in `tests/behaviour/test_the_set_a_work_item_always_has.py` pins the new section's heading and table header in the template, shown red with the section removed (contract rule 15).

Out:

- The version move to 0.36.0. The orchestrator assigns it (spawn prompt).
- A script that computes overlap from the frames' paths. Whether two changes meet is a judgment of meaning, and G9's overlap shared no file (`frame/plan.md` *Alternatives considered*, row C).
- Holding a later item's build until the first lands. The orchestrator weighs that per release from the plans' rows (`frame/plan.md` *Alternatives considered*, row D).
- Any change to `docs/releasing/branch-and-release.md`. G3's rationale stays true.
- The framer re-reading sibling frames after it hands back. A pair one plan alone names is ordered by that plan (*Scope* item 4).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A framer spawned beside other work items of its release | Given a spawn prompt that names the release's other open work items, when the framer writes `frame/plan.md`, then its *Overlap with the release* holds one row for each item its work meets, naming where both change, which merges first and the grounds, and the hand-back repeats the order. | Read `agents/framer.md` step 4 and step 8 and the template against *Scope* items 1 to 3. The case of *Scope* item 6 passes, and was shown red with the section removed. |
| S2. A framer whose work meets none of the named items, or whose spawn names none | When it writes the plan, then *Overlap with the release* holds one sentence naming the items read and saying none meets this work, or saying the spawn named none. | Read the template's placeholder text. |
| S3. The orchestrator merges the release's items | Given plans that state an order for a pair, when the orchestrator merges, then it merges in that order and gives the version move to the item first in it. | Read G1's paragraph as rewritten. |
| S4. Two plans disagree, or the first item stalls | Given opposite orders for one pair, or a first item that cannot be sealed first, when the orchestrator merges, then it writes a *Judgments of the run* row in the plan of the item it merges out of the stated order. | Read G1's paragraph as rewritten. |
| S5. The later item of an ordered pair while the first lands | Given a plan that orders this branch after another item, when that item lands, then the orchestrator merges the base into this branch before its next round, or before its broad run where its rounds have ended. | Read G2's paragraph; `tests/text/test_the_rules_have_one_owner.py` still passes on its four pinned phrases. |

## Data & interfaces

The new template section, as `templates/records/sdd-plan.md` will carry it:

```markdown
## Overlap with the release

<each other open work item of the release that this work meets, as the spawn names them and as their frames stand where committed: both change one file, or one changes a rule, a check or a fact the other's change reads; where none meets, or the spawn names none, one sentence saying which items were read and that none meets>

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| | | | |
```

`Where both change` names the file and the section, or the rule or check and what of the other's change it reads. `Merges first` names this work item or the other by its issue number. `Grounds` says why that order costs less.

## Rule changes

- nothing
  why: the rules this work changes stand in `agents/framer.md`, `skills/implement/orchestration.md`, `skills/code-review/orchestration.md` and `templates/records/sdd-plan.md`, all outside the policy root `docs/`; no document the index `docs/README.md` names states which side-by-side item merges first or what a framer reads (G14), and `docs/releasing/branch-and-release.md` *Work accumulates on a release branch* stays true (G3).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The orchestrator's heuristic for which item merges first: "the one likeliest to be sealed first, often the smallest diff" | `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, the paragraph opening **Which branch the pull request lands on is decided with the routing question** | `agents/framer.md` *Order of work* step 4, as part of the framer's weighing (*Scope* item 2); the order itself lands in each plan's *Overlap with the release*. |

The work adds a template section and a rule, and nothing more can go in
return. The merge-on-conflict rule of G2 stays, because an overlap no frame
named still meets at the merge and that paragraph is how it is integrated.
The new section's record is G9 to G11: three releases in which an overlap
between side-by-side items cost rounds, broad runs or sealers that an order
chosen at framing would have spent once.

Framed 2026-11-09 by framer, before the build.
