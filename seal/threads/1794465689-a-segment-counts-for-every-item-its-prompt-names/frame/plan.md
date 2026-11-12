# Implementation Plan: 1794465689-a-segment-counts-for-every-item-its-prompt-names

## Technical context

The tree as read at `c26981960`.

`seal cost --work-item <dir>` is `skills/verify/scripts/session_cost.py#work_item` (`:3215-3291`). It reads the item's two keys with `work_item_keys` (`:3055-3074`), walks every segment transcript on the machine (`segment_transcripts`, `:3077-3085`), and counts one where `names_key` (`:3118-3121`) finds either key in its spawn prompt. It leaves out each segment a comment on the open log names (`posted_names`, `:3158-3172`), and `report_work_item` (`:3175-3212`) prints the rest, which `post` sends as one comment. The release's four framer segments are each counted for all four items (`frame/design.md` G4), and no field outside the prompt names the item a segment ran for (G6).

The build adds a reader of the other work items' `routing.md` (D1), one more value per counted transcript in `work_item`'s `reading` dict (D2), and lines in `report_work_item` (D3). `routing.parse` is loaded through `lib_module("routing")`, as `work_item_keys` loads it. The git reads are `rev-parse`, `for-each-ref`, `ls-tree` and `cat-file`, none of which `lib/gitcmd.py` holds a key for, so they need no `gitcmd.argv`. Each runs from the parent directory, so no path relative to the top level is formed.

**The failure scenario of the chosen approach.** Six months on, an orchestrator runs two items side by side and deletes the first item's branch once its pull request merges, before the second run's read. The second item's directory is not yet in the first one's tree, and the first one's directory is not in the second's, so the second page no longer reaches the first item. The shared framer segment then reads as the second item's alone, as it does at `c26981960`. The count line of D3 shows how many other items were read, which is where a reader sees the reach shrink. The second scenario: a repository holds hundreds of local branches. The read then runs one `git ls-tree` per distinct tip, which costs seconds on a command run once per run. G8 measured 0.13 seconds over 5 tips.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Count the segment for the item whose key the prompt names first | An orchestrator writes "builds on `chore/1516-…`" above "Frame work item `<dir>`", and the segment goes to #1516. Position in prose is a reading guessed from words, which `skills/core/SKILL.md` *The rule a mechanism is kept against* reports and never decides on | rejected |
| B. Count the segment only for the items whose directory the prompt names, and by branch only where it names no directory | Right in this release (G5). Wrong where the other items' frames are committed, because `skills/implement/merge-order.md` then has the prompt name their frame paths, which hold their directories: the release G13 of `1794312072` read named all four by directory, and all four count again | rejected |
| C. A line the orchestrator writes in every spawn prompt, `Work item: <dir>`, which the command reads exactly and which outranks the key match | Replaces the structure: attribution moves from what the prompt happens to name to a declared line. It is a new grammar every spawn rule of every agent must carry, a rule an orchestrator can forget, and a forgotten line falls back to counting for every item, silently. Transcripts written before it carry no line. What it would catch is a reading filed under one run's comment instead of another's, and no reading is lost either way (G1). The premise that keeps the key match was checked: the spawn prompt is the only text a segment carries that names its work item (G6) | rejected |
| D. A field the harness writes: `gitBranch`, `cwd` or the `.meta.json` `description` | `gitBranch` and `cwd` are the session's checkout, the same for all four framers (G6). `description` is free text | rejected |
| E. Remove the cause: `skills/implement/merge-order.md` has the framer prompt name the other items by issue number alone | The framer then has to find each item's branch and frame from an issue number, which no record maps exactly, and contract rule 5 asks for coordinates in their place. A prompt that names another item's branch for any other reason still matches that item | rejected |
| F. Name on the page each counted segment whose prompt also names another work item, read from the siblings on disk and from every local branch's `routing.md` | The first scenario under *Technical context*: an item whose branch is gone and whose directory is in neither tree is not reached, and the count line shows the reach | chosen |
| G. As F, from the siblings on disk alone, with no git read | At a run's end the release's other items are on unmerged branches (G8). The first run to post, the one that takes the shared framer segments, would read none of them and name nothing, which is the case the issue describes | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6 | S1, S2, S3 and S5 as new cases of `Test_work_item`, each seen red against `c26981960`; S4 by the narrow run of `tests/skills/test_session_cost.py`; S6 read by the proofer; S7 at the orchestrator's read of the run | `3102602f1` |

## Overlap with the release

The spawn named three other work items, #1516 (`chore/1516-feature-prs-wait-on-the-macos-runner`), #1496 (`feat/1496-a-passing-release-note-reads-like-a-failure`) and #1494 (`feat/1494-the-orchestrator-polls-ci-by-hand`). Each branch holds only its `routing.md` at the time of reading (`git diff --stat 79f815a74 <branch>`, executed), and each issue's file list was read. None meets this work: #1516 changes `.github/workflows/test.yml` and `CONTRIBUTING.md`, #1496 changes `.github/scripts/publish_release_note.py`, `release_seal.py` and `docs/releasing/branch-and-release.md`, and #1494 adds `seal pr-wait` to `skills/implement/scripts/seal.py` and changes `skills/code-review/orchestration.md`. This work changes `session_cost.py`, its tests and `skills/verify/orchestration.md`, and adds no check that reads the whole tree. So no row below orders this item against another. #1516 merges first because it carries the version move (`skills/implement/merge-order.md`). This item and #1496 then merge as each is sealed, and #1494 last, as the milestone orders it.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|

## Operational impact

No migration, no new environment variable and no new dependency. `seal cost --work-item` now also runs `git rev-parse`, `git for-each-ref`, `git ls-tree` and `git cat-file` in the work item's repository. All four only read, and none reaches the network. This pull request does not move the version: #1516 carries the move. Until a release holding this change is installed, the release's own run posts read the four framer segments as G4 shows, and the orchestrator's `--says` sentence is where a reader learns it.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
