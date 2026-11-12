# Design: 1794465689-a-segment-counts-for-every-item-its-prompt-names

## Grounding

The tree as read at `c26981960`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. Issue #1510, read with `gh issue view 1510 --json body,comments` (executed; the issue has no comments) | The request: a segment whose spawn prompt names two work items is counted for the item the run is about by a rule a script reads exactly, or the `--work-item` page names it as matching more than one item. It names `session_cost.py` (`names_key`, `report_work_item`), `tests/skills/test_session_cost.py` and `skills/verify/orchestration.md` *Measure the run, and feed the flow log*. |
| G2. `routing.md` of this work item (read, committed at `c26981960`) | Planning `framer`, Implementation `crafter`, through the review chain, Automation `yes`, Branch `refactor/1510-a-segment-counts-for-every-item-its-prompt-names`. Its grounds leave the choice between the two designs of G1 to the framer, judged against `skills/core/SKILL.md` *The rule a mechanism is kept against*. |
| G3. `skills/verify/scripts/session_cost.py#work_item` `:3215-3291`, `#names_key` `:3118-3121`, `#spawn_prompt` `:3088-3115`, `#work_item_keys` `:3055-3074` (read) | A segment transcript is the work item's where the text of its first `type: user` entry names the item's directory name, or the `Branch` row of its `routing.md`, as a whole token (`:3249-3255`). Nothing else about the segment is read, so a prompt that names several work items counts for each. |
| G4. Probe: `python3 skills/verify/scripts/session_cost.py --work-item <dir>` for each of the four work items of release 0.38.0, each `routing.md` copied from its branch with `git show`, run from a `git clone --no-local` at `c26981960` under this framer's scratch directory (executed, exit 0 four times) | 2,202 segment transcripts walked on this machine. Each of the four readings names the same four transcripts, the framers of #1516, #1510, #1496 and #1494, so each framer segment is counted for all four items. `gh` in the clone resolves no repository, so the log state read `unreadable` and nothing was left out. |
| G5. Probe: `test_tmp_matches.py` over the four framer prompts of G4, matching each item's two keys with the clone's `names_key` (executed) | Each framer's prompt names its own item by directory and by branch, and each other item by its branch alone. In this release a rule "the directory over the branch" would pick the right item. It would not in the release that `seal/threads/1794312072-the-cost-comment-is-posted-per-segment/frame/design.md` G13 read, whose framer prompt named all four items by directory and by branch, because `skills/implement/merge-order.md` has the prompt name each other item's frame path where that frame is committed. |
| G6. Probe: the entry fields of the four framer transcripts of G4 and their `.meta.json` files (executed) | Every entry's `gitBranch` is `chore/1516-feature-prs-wait-on-the-macos-runner` and every `cwd` is the main clone, for all four framers. Both are the session's checkout, not the work item's. The `.meta.json` `description` is the orchestrator's free text (`Frame #1510 segment attribution`). No field the harness writes names the work item a segment ran for. |
| G7. Probe: `test_tmp_multi.py`, each walked transcript's spawn prompt matched against the keys of the 29 work items whose `routing.md` this tree or the branches of G4 hold (executed) | 155 transcripts name at least one of those items, and 28 of them name more than one. 27 of the 28 items with any segment share at least one segment with another item. This is a sample: items settled out of every reachable tree are not in it. |
| G8. Probe: the three other items' directories on their branches (`git ls-tree --name-only <branch> seal/threads/`, executed), and `test_tmp_others.py`, a prototype of *Data & interfaces* D1 against this worktree (executed) | None of the three side-by-side items' directories is in this tree: each stands on its own branch until it merges. Read from the directory's siblings and from each `refs/heads` tip, the prototype found 5 distinct tips and 28 other work items in 0.13 seconds. It named each of the four framer transcripts as also naming the release's other three items. |
| G9. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A reading that is noisy or guessed from words is reported, never used to decide. Nothing is kept beside the tree to stay in step with it. G1's *Change* applies it here: which run a segment belongs to is a judgment about its prompt, so the command reports the match and picks no owner. |
| G10. `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in* (read) | Every framer prompt of a release with several work items names the other items by issue, branch and committed frame path, so the match of G4 recurs at every such release. `agents/framer.md` step 4 reads those coordinates to judge where the items meet. |
| G11. The texts that state how `--work-item` finds a segment (`git grep -n -i 'spawn prompt'` outside `seal/threads` and `tests`, executed, then each hit read) | `skills/verify/orchestration.md:165-168`; `docs/running/measuring-a-run.md` *Where a reading goes* `:132-135`; the `session_cost.py` comment `:3022-3029`, its usage line `:31-33` and its `argparse` help `:3323-3325`; `README.md:423` and `README.ko.md:419`. The unsettled design `1794312072-the-cost-comment-is-posted-per-segment` changes the `measuring-a-run.md` sentence, and its `to` keeps the sentence "It finds a segment by its spawn prompt naming the work item's directory or its branch." |
| G12. `session_cost.py#posted_names` `:3158-3172` and `POSTED_NAME` `:3032` (read) | A comment on the log names a segment only by a fenced line that is exactly `# <name>.jsonl`. A line the page adds is posted inside the same fence, so it must not take that shape, or the next run would read it as a posted segment. |
| G13. `docs/running/measuring-a-run.md` *Where a reading goes* `:137-150` (read) | The posted body carries file names, never a path, a prompt or command text. The page's first line already names the work item's directory and branch, so another work item's directory name is the same kind of text. |
| G14. `lib/routing.py#parse` `:156-243` and `skills/code-review/scripts/chain_check.py#tracked_declarations` `:1904-1919` (read) | `routing.parse` is the one reader of a declaration, and `work_item_keys` already loads it through `lib_module`. `tracked_declarations` reads declarations at `HEAD` with `git ls-tree`, in another script and at one ref. Nothing in the tree reads the declarations of every local branch. |
| G15. `tests/skills/test_session_cost.py` `Test_work_item` `:5251-5620` (read) | Each case lays out the item under `tmp_path/repo/seal/threads/<NAME>`, with no git repository and no `seal/README.md` marker, and stubs `run_gh`. So where the directory is in no git repository, the read of local branches must give nothing and change no exit. |
| G16. `seal/follow-up.md` (read), the latest release's body (`gh release view --json body`, executed) and the `### Process changes` tables of the fragments under `seal/threads/` (read) | `follow-up.md` holds no row. The v0.37.5 body has no `### Process changes` heading. The fragment of `1794312072-the-cost-comment-is-posted-per-segment` has the run post once with `seal cost --work-item`, which is the reading this work extends. |
| G17. `docs/README.md:35` (read) and `ls docs/running` (executed) | `docs/running/measuring-a-run.md` has no `.ko.md` edition, so its rule change carries no second operation (`skills/settle/rule-changes.md` *Rule changes*). |
| G18. The operation under `## Rule changes`, read by `skills/settle/scripts/rule_changes.py#parse` and placed by `#apply_op` after the operation of `1794312072` that precedes it (executed from the clone of G4) | `parse` returns one operation with no error and no line named as not read. `apply_op` places it in *Where a reading goes* of `docs/running/measuring-a-run.md` once that earlier operation is applied. |

## Scope

In scope:

1. **`--work-item` reads the keys of every other work item it can reach** (D1): the directory's siblings on disk, and the work items on each local branch where the records root is inside the repository. A source it cannot read gives nothing and changes no exit code.
2. **The reading names each segment whose prompt also names another work item, and which items** (D2, D3). The read without `--post` and the posted comment both carry it, inside the fence. A segment already on the log is listed and marked as such, so a later run's reading still shows a segment it no longer posts. The count line prints whether or not any segment matched another item.
3. **The command decides no owner.** Every segment it counts now, it still counts, and every exit code stays as G3 reads it. Which run a segment belongs to is the orchestrator's judgment, written in its `--says` sentence.
4. **The texts of G11 that state how `--work-item` finds a segment and what it prints are rewritten in place**: `skills/verify/orchestration.md:165-168` (D4), the module's usage line `:31-33`, the comment `:3022-3029`, the `argparse` help `:3323-3325`, and the docstrings of `work_item` and `report_work_item`. `docs/running/measuring-a-run.md` changes through `## Rule changes`.
5. **The cases of `Test_work_item` that S1, S2, S3 and S5 name**, each seen red against `c26981960` (contract rule 15).
6. **The work item's `changelog.md`**, written by the last phase's crafter, with a `### Process changes` row, because the diff changes `skills/verify/orchestration.md` (`docs/layout/the-record-layout.md:52`).

Out, each with its ground:

- **Counting the segment for one work item.** No exact read gives the owner (G5, G6), and a line the orchestrator writes for the purpose is a new grammar every spawn must carry (`frame/plan.md` *Alternatives considered* rows A to D).
- **`skills/implement/merge-order.md`.** The rule hands the framer the coordinates it judges the overlap from (G10). Naming the other items by issue alone moves the guess to the framer, and other prompts still name other items' branches in prose (row E).
- **`refs/remotes` and other machines.** The transcripts read are this machine's, and the orchestrator that ran them made the items' branches here (G8). A branch deleted before the run's read is not reached, and the count line of D3 says how many items were read.
- **Which segments a post leaves out.** A segment a comment already names stays out of the next post (G12). This work adds lines to the page and changes no count.
- **`README.md:423` and `README.ko.md:419`.** Each says the command gives one row per segment found by its spawn prompt naming the item's directory or branch, which stays true. The reader of the page is sent to the skill's section, which D4 changes.
- **A key that is an ordinary word.** A `routing.md` whose branch is `main` matches every prompt that says "main", for this item's count as for the new line. That is the key's behaviour since #1439, and this work leaves it.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A shared segment is named on both pages | Given two work items whose directories are siblings, and a segment whose prompt names both, When `--work-item` reads either item, Then its page names that segment's file as also naming the other item's directory. With `--post`, the comment carries the same line inside its fence, and `posted_names` over that body reads only the `# <name>.jsonl` lines | A new case of `Test_work_item`, seen red against `c26981960`. It asserts the printed line, the posted line, and `Test_emit.named_in_fence` over the posted body |
| S2. A later run still shows the segment it does not post | Given the shared segment of S1 already named on the open log, When the other item's run reads, Then its page lists that file, marked as already in the log, with the item it also names. Where every segment of the item is in the log, the read without `--post` still prints that line above "every segment transcript that names it is already in the log" | A new case, seen red against `c26981960` |
| S3. An item on another local branch is read | Given a git repository whose checked-out branch holds this item, and a second local branch whose tree adds another item's `routing.md`, When `--work-item` reads this item and a segment's prompt names the other item's branch, Then the page names that segment as also naming the other item | A new case that builds the repository under `tmp_path` with `git`, seen red against `c26981960` |
| S4. No git, nothing breaks | Given the fixture of G15, with no git repository, When every case of `Test_work_item` runs, Then each passes as at `c26981960` and no exit code changes | Executed by the crafter: the narrow run of `tests/skills/test_session_cost.py` |
| S5. A segment that names one item says so | Given only segments whose prompts name this item alone, When `--work-item` reads it, Then the count line of D3 says none of them names another item and gives the number of other items read, and no per-segment line prints | A new case, seen red with the count line's print removed |
| S6. The section says what the page now names | Given `skills/verify/orchestration.md` after the build, When a reader opens *Measure the run, and feed the flow log*, Then it says that a segment whose prompt names several work items is counted for each and named as such, and that the orchestrator's `--says` sentence judges which run it belongs to | Read by the proofer against D4 |
| S7. This release's framers are named | Given the four framer transcripts of G4 on this machine, When the orchestrator reads this item's run with `seal cost --work-item` at the build's head, Then each of the four is named as also naming the release's three other items | Executed by the orchestrator at the run's read, before the post |

## Data & interfaces

**D1. The other work items' keys.** A function beside `work_item_keys` takes the work item's directory and its name. It returns each other work item's directory name with the branch or branches its `routing.md` names, and the number of items found. It reads two sources:

1. The directory's siblings on disk: each entry of its parent directory that holds a `routing.md` `routing.parse` reads. This covers local mode, where the root sits under the common git directory that every worktree shares, and every item merged into the checkout.
2. Each local branch, in shared mode. `git rev-parse --show-toplevel` runs from the parent directory, and where the parent lies inside that top level, its path relative to it is taken in git's form (`lib/gitcmd.py#git_path`). `git for-each-ref --format=%(objectname) refs/heads` lists the tips. For each distinct tip, `git ls-tree -z --name-only <tip> -- <rel>/` lists the item directories. One `git cat-file --batch` reads each `<tip>:<rel>/<dir>/routing.md` not yet read, and `routing.parse` reads each. A path holding a newline is skipped, because `cat-file --batch` would read it as two requests.

The work item's own directory name is left out of both sources. A git that is missing, fails or exits non-zero gives nothing from the second source. A directory found at several tips keeps every branch they name.

**D2. The match.** A segment `work_item` counts also names another item where `names_key` finds that item's directory name, or one of its branches, in the segment's spawn prompt. This is the test that counted it for this item (G3). For each counted transcript, the reading gains the sorted directory names of the other items it names. It also gains the number of other items D1 read.

**D3. The page.** `report_work_item` prints the following under the two count lines and before either early return:

- one line, always: how many of the counted segments also name another work item, out of how many other items were read beside this one;
- then, for each counted segment that names another item, one line: its file name, `already in the log` where a comment names it, and the directory names of the other items.

No added line is a `# <name>.jsonl` line (G12). The exact wording is the crafter's, and its cases pin it (contract rule 14). The posted body takes the page through `post` as before, so the lines are inside the fence. No exit code changes.

**D4. The section's sentence.** `skills/verify/orchestration.md:165-168` keeps "The command finds the work item's segments by their spawn prompts naming its directory or the branch its `routing.md` names." After it, the section adds what follows. A segment whose prompt also names another work item, as a framer's prompt names the release's other items (`skills/implement/merge-order.md`), is counted for each, and the reading names it with those items. Which run it belongs to is the orchestrator's judgment, written in the `--says` sentence.

## Rule changes

- change
  file: docs/running/measuring-a-run.md
  section: Where a reading goes
  from: It finds a segment by its spawn prompt naming the work item's directory or its branch.
  to: It finds a segment by its spawn prompt naming the work item's directory or its branch. A segment whose prompt names several work items is counted for each, and the reading names it beside the other work items it names, because which run it belongs to is a judgment about the prompt and not a match a script reads.

## Removes

- nothing
  why: The work adds lines to an existing reading and the read of other work items' `routing.md` behind them, and no gate, check, hook, or form a party writes. The sentences it amends are rewritten in place (*Scope* item 4).

Framed 2026-11-12 by framer, before the build.
