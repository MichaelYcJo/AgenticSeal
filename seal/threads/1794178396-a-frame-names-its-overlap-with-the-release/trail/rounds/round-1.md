# Review round 1: 1794178396-a-frame-names-its-overlap-with-the-release

```seal
target: 729b83e9 against release/v0.36.0
```

The base is `release/v0.36.0` at `94d04d30` (executed: `git log --oneline 94d04d30..729b83e9` lists the seven commits of the branch). This is a finding round over the whole branch, worked in a `git clone --no-local` of the branch worktree at `729b83e9`. No earlier round exists, so this round carried no fact and re-established every one it uses. `seal/parity.md` is absent, so no parity comparison applies, and `seal/config.md` has no `Pact` row. The record language is English, since `seal/config.md` has no `Record language` row.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/phases/phase-1.md` whole at `729b83e9`. The issue has no comments, as the spawn prompt states and `frame/design.md` *Grounding* G13 records; this round did not re-run `gh issue view 1443`.

The axes named for this change, beyond the table: the version move's place in the release's merge order, and whether each statement of the new "meet" definition reads the same. Each *Grounding* and *Technical context* coordinate the frame dates to `94d04d30` was opened at that commit (executed: `git show 94d04d30:<path>` over `skills/implement/orchestration.md` lines 376, 388 to 389 and 402, `skills/code-review/orchestration.md` lines 317 and 330, `templates/records/sdd-plan.md` line 21, `tests/text/test_the_rules_have_one_owner.py` lines 335 to 339, `tests/behaviour/test_the_set_a_work_item_always_has.py` lines 237 and 256, `tests/skills/test_pr_body.py` line 39), and each holds what the frame says it holds.

## Findings

### 1. The rewritten merge order lets an item no plan orders merge before the item that carries the version move

```seal
severity: must
location: `skills/implement/orchestration.md:395-397`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:34`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/changelog.md:3`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/changelog.md:6`
evidence: read `skills/implement/orchestration.md:379-397`, `docs/releasing/branch-and-release.md:30-42`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:34`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:80`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:38`
```

Why it matters: `docs/releasing/branch-and-release.md:30-42` states that the version moves "in the first pull request into `release/vX.Y.Z`", moved by the party that writes "the changelog fragment of the release's first work item". The same paragraph of `skills/implement/orchestration.md` says so at line 381: "the version moves to that name in the first pull request into the branch". At `94d04d30` the paragraph held that order with "it chooses the one it will merge first, the one likeliest to be sealed first, often the smallest diff, and merges it first" (lines 388 to 389). The branch replaces it with "The move goes to the item first in that order, and items that no plan orders against each other merge as each is sealed" (lines 395 to 397). That second clause lets an item no plan orders merge as soon as it is sealed, also before the item that carries the move. This release shows it. `frame/plan.md:38` says #1439 and #1441 meet this work nowhere, so no row orders them against #1443, the item that carries the move. If #1439 is sealed first, the rewritten paragraph merges it first, and the first pull request into `release/v0.36.0` does not move the version. "The item first in that order" also names no item where the plans order no pair, or order two pairs that do not touch (A before B, C before D). `frame/design.md` *Removes* (`:80`) names only the heuristic as removed, not "and merges it first", so the frame never weighed dropping that guarantee. The defect stands in the frame too: *Scope* item 4 (`:34`) states the same clause, and the build followed it. `frame/design.md` *Rule changes* states that no policy changes, and this clause contradicts the policy it says stays true.

The fix restores the guarantee and keeps the plans' order. Four statements carry the fact, and the fix pass owes all four. The orchestrator folds `frame/design.md` *Scope* item 4 and writes the *Judgments of the run* row for it. The fix pass rewrites the orchestration paragraph and the two sentences of `changelog.md`. Scenario S3 (`frame/design.md:51`) says "gives the version move to the item first in it" and stays true under the fix.

`skills/implement/orchestration.md`, lines 395 to 397, from "The move goes to the":

```markdown
plan of the item it merges out of the stated order. The move goes to an
item that no plan orders after another, which the orchestrator chooses
where several are, and the orchestrator merges that item before every
other item of the release, because the first pull request into the branch
carries the move. Once it has landed, items that no plan orders against
each other merge as each is sealed. Where a crafter builds that work item
```

`frame/design.md` *Scope* item 4, its last sentence:

```markdown
The version move goes to an item that no plan orders after another, which the orchestrator chooses where several are, and the orchestrator merges that item before every other item of the release; once it has landed, items that no plan orders against each other merge as each is sealed.
```

`changelog.md` line 3, the sentence that opens "The version move goes to the item first in that order":

```markdown
The version move goes to an item no plan orders after another, and the orchestrator merges it before every other item of the release; once it has landed, items no plan orders against each other merge as each is sealed.
```

`changelog.md` line 6:

```markdown
Updating: nothing to do. A plan framed before this release has no *Overlap with the release*, so no plan orders its item against another, and the orchestrator merges it as it is sealed, once the item carrying the version move has landed.
```

### 2. The plan template defines where two items meet more narrowly than `agents/framer.md` step 4, and leaves out the overlap of a check and the content it reads

```seal
severity: should
location: `templates/records/sdd-plan.md:23`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:62`
evidence: read `templates/records/sdd-plan.md:23`, `agents/framer.md:84-87`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:18`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:32`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:62`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/design.md:69`, `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/changelog.md:3`
```

Why it matters: `agents/framer.md:84-87` says two items meet "where both change the same file, or where one changes a rule, a check or a fact that the other's change reads or adds content to, as a check that reads the whole tree meets the content another item adds". `changelog.md:3` and *Scope* item 2 (`frame/design.md:32`) say the same. The template's placeholder (`templates/records/sdd-plan.md:23`) says "one changes a rule, a check or a fact the other's change reads", without "or adds content to". *Grounding* G9 (`frame/design.md:18`) is the record the section is kept against: #1390 added a check over the whole tree, and #1389's content met it. Under the template's wording that pair does not meet, because #1389's change does not read #1390's check; #1389 adds content the check reads. So the template's definition misses the one overlap kind the design names as wider than a shared file. `frame/design.md:69` says "The meaning of each column stands in the placeholder, so a framer starting from the template reads it there". A framer, or a session that plans where `Planning` is `the session` and reads only the template, then holds two definitions of one term and can take the narrower one. The template's next sentence ("the rule or check and what of the other's change it reads") already describes the G9 direction, so the placeholder disagrees with itself as well.

The fix adds the missing words to both statements of the placeholder. `frame/design.md` *Data & interfaces* shows the placeholder as the template carries it, so the orchestrator folds the same line there.

`templates/records/sdd-plan.md` line 23 and `frame/design.md` line 62:

```markdown
<each other open work item of the release that this work meets, as the spawn names them and as their frames stand where committed: both change the same file, or one changes a rule, a check or a fact that the other's change reads or adds content to. A row names the file and the section both change, or the rule or check and what of the other's change it reads; the item that merges first, by its issue number; and why that order costs less. Where none meets, one sentence naming the items read and saying none meets this work; where the spawn names none, one sentence saying so>
```

## Confirmations

What matched: `agents/framer.md:81-92` holds *Scope* item 2: the reading of the other items the spawn names, the meet definition, the statement in `frame/plan.md` *Overlap with the release*, and the heuristic now in the framer's weighing. Lines 117 to 118 hold *Scope* item 3's hand-back bullet. Read.

What matched: `skills/implement/orchestration.md:386-397` holds *Scope* item 4's spawn-prompt sentence, the merge in the plans' order and the *Judgments of the run* row for a departure. The heuristic `## Removes` names is gone from the tree (executed: `git grep -n -i -e likeliest -e "smallest diff" -e "merges it first"` at `729b83e9` finds it nowhere outside this work item but in the framer's weighing; the one other `likeliest`, `skills/implement/bootstrap.md:109`, is unrelated). Finding 1 is about the clause after it. Read.

What matched: `skills/code-review/orchestration.md:321-326` holds *Scope* item 5's timing for an ordered pair. The paragraph's four phrases that `tests/text/test_the_rules_have_one_owner.py` pins all stand, and the module passed (executed, the narrow run under *Probes*). The paragraph's opening "merges once" now stands beside a second merge, the ordered pair's. This round reads "once" as bound to the conflict case it names, so it found no contradiction there. Read.

What matched: `templates/records/sdd-plan.md:21-27` places the section immediately before `## Operational impact`, with the heading and header *Data & interfaces* gives. The placeholder is word for word the one `frame/design.md:62` shows, which the fold `2cddb7e1` made true; finding 2 is about the wording both share. `skills/code-review/scripts/pr_body.py:179` and `skills/settle/scripts/settle.py:213` read the plan by the headings `## Phases` and *Judgments of the run*, and the new section sits between neither pair in a way that changes what they read. Read.

What matched: phase 1 claimed the new case `test_the_plan_template_carries_the_overlap_table` was seen red before the template changed, failing at its line 270. Re-run with the template at `94d04d30`, it failed at `tests/behaviour/test_the_set_a_work_item_always_has.py:270` with "the plan template has no `## Overlap with the release`" (executed, under *Probes*). The case covers a section no other case of its group (`:237`, `:245`) reads, so it is no duplicate. The two `seal mutate` runs phase 1 reports were not re-run; the case's lines 272 and 276 are the header and placement assertions it names. Read.

What matched: phase 1 claimed `test_the_top_rung_names_behaviour_rather_than_a_count` refused "one file" in the template line. `tests/behaviour/test_the_set_a_work_item_always_has.py:107-132` scans `templates/records/sdd-plan.md` with a pattern that matches "one file", so the claim holds by reading, and "the same file" is no match. Read.

What matched: phase 1's correction of the frame's line ranges (step 8 lines 94 to 108; the G1 paragraph lines 376 to 402) holds at `94d04d30`, and `frame/plan.md` *Technical context* now states those ranges. Read.

What matched: every quote in `pr.md` stands word for word at the coordinate it names: the first, second and third quotes in `changelog.md:3`, the fourth at `changelog.md:4`, the fifth at `frame/plan.md:59`, the sixth at `gaps.md:8`. Read.

What matched: `.claude-plugin/plugin.json` moves from `0.35.1` to `0.36.0` in `355cbf97`, the commit that adds `changelog.md`, as `frame/plan.md` *Operational impact* states. `changelog.md` ends with three `### Process changes` rows, one per instruction file the diff changes. Read.

What matched: `gaps.md` labels the full suite, the lint and the format check `unverified` and names the orchestrator at the broad gate as their answerer, so the label is honest. Its second row and `frame/questions.md` Q1 name a measurement as the answerer for whether framers and the orchestrator act on the new text. Read.

What matched: `frame/plan.md` *Judgments of the run* row 3 says neither place of `docs/layout/the-record-layout.md` that `gaps.md` *Not done* names was a whole list before this work. `docs/layout/the-record-layout.md:108` and `:153` name neither *Operational impact* nor the overlap, so the claim holds. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the overlap rows for #1440, #1442 and #1444, and "none meets" for #1439 and #1441, match those items' real diffs; they rest on issue bodies and guessed file lists | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/frame/plan.md:36-44` | the orchestrator, reading the six plans, as `frame/design.md` G16 names |
| The full suite, the repository-wide lint and the format check at `729b83e9`; contract rule 2 keeps them out of a round | `seal/threads/1794178396-a-frame-names-its-overlap-with-the-release/gaps.md:7` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_set_a_work_item_always_has.py tests/text/test_the_rules_have_one_owner.py tests/behaviour/test_a_cited_section_stands_in_its_file.py -q -p no:randomly`, in the clone at `729b83e9` | exit 0, 103 passed |
| `git checkout 94d04d30 -- templates/records/sdd-plan.md`, then `bin/test tests/behaviour/test_the_set_a_work_item_always_has.py -q -k overlap -p no:xdist`, then `git checkout HEAD -- templates/records/sdd-plan.md`, in the clone | exit 1; an `AssertionError` at line 270 saying the plan template has no Overlap with the release heading; the clone was clean afterwards |
