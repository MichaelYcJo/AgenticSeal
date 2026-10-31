# Phase 3: 1793438028-pre-0-23-upgrade-readings-removed

## What this phase found

**The frame holds against the tree.** Every unit phase 3's row and `frame/design.md` *Removes* name stood at b074601f (read). Some line numbers in `frame/plan.md` *Technical context* had moved, because phases 1 and 2 edited the same files. `OLD_PLUGIN_CLONE` stood at `seal.py:1468`, not `:1489`. `carries_clone` stood at `:1923`, not `:1949`. *Coming from `specseal@specseal`* stood at `README.md:307-337` and `README.ko.md:301-330`. `skills/update/SKILL.md:142`'s `PAIRS` stood where the plan says. No unit was missing, so nothing was built differently.

**The README section went first, in its own commit.** Commit 2b493b5a removed *Coming from `specseal@specseal`* from both editions before any code changed. That section described all three readings: the install, the old CLAUDE.md markers and the old workflow. Had it gone last, each earlier commit would have left a README sentence describing a reading that commit had removed, against `skills/core/SKILL.md` *The rule a mechanism is kept against* ("in the same commit removes what stood on the old fact"). The same commit dropped the `specseal@specseal` and `marketplace remove specseal` items from `tests/censuses.py#KEPT_OLD_NAMES`, which nothing else spells. It also dropped "and which README.md *Install* names" from the old-marker item's comment. The markers themselves left in 43be43d3 and the clone line in db3dedf1.

**`frame/questions.md` Q1 is answered (b): `carries_clone` is folded into its two callers.** Once its second arm went, the helper's body was `PLUGIN_CLONE in text`, and its docstring could only say "True where TEXT carries this plugin's clone line". The comment above `PLUGIN_CLONE` already says what a file carrying that line means. `install_workflow` already tested `PLUGIN_CLONE not in found` inline, so the module now states the test one way in all three places. The question's default was (a) "unless phase 3 finds the helper's docstring has nothing left to say", and that condition is met. Commit db3dedf1. The fold changes no behaviour. Two `seal mutate` runs show that the existing cases still watch both inlined tests (executed):

- `bin/seal mutate skills/implement/scripts/seal.py --replace '    if PLUGIN_CLONE not in text:\n        return "other"' '    if False:\n        return "other"' --tests "bin/test tests/skills/test_seal.py -q -p no:xdist -k workflow_at"` printed `red`.
- `bin/seal mutate skills/implement/scripts/seal.py --replace 'if PLUGIN_CLONE not in staged:' 'if False:'` printed `SURVIVED` with `-k remove_workflow`. The case for that arm is `Test_pr_checks.test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand`, which that selection did not pick. Run again with `-k test_refuses_a_staged_file_without_the_clone_line_deleted_by_hand`, it printed `red`. The survival was a selection miss, not a gap in the suite.

**The update case was rewritten over the one pair and seen red.** `test_step_4_takes_out_a_block_under_either_markers_whatever_it_holds` is now `test_step_4_takes_out_a_block_whatever_it_holds`. It plants one block under the `agentic` pair that holds rule lines and an `@` line. No other case of the module plants a block with lines inside it. The module docstring now says releases from 0.23.0 to 0.24.x wrote the block, which matches *Removes*' row for the markers. `bin/seal mutate skills/update/SKILL.md --replace 'elif inside in line:' 'elif inside in line or line.startswith("- "):' --tests "bin/test tests/behaviour/test_the_old_block_leaves_through_update.py -q -p no:xdist"` printed `red`, and the rewritten case was among the two that failed (executed). Commit 43be43d3.

**`KEPT_OLD_NAMES` now holds four items, and a living file spells each one.** `git grep -F -i` outside the records, `.test_durations`, the recorded eval cases and the two census files lists the following (executed after 1e568e6f):

- `SpecSeal-Routing`: `tests/skills/test_chain_check.py:3236-3243`.
- `# specseal-git-hook`: `docs/the-routing-check.md:25`, until the settle.
- the `renames` entry: `.claude-plugin/marketplace.json:15`.
- `.specseal`: both `docs/one-root-by-lifetime` editions, `tests/behaviour/test_first_setup_asks_once.py:688` and `tests/behaviour/test_no_document_names_the_old_roots.py`.

The `SpecSeal-Routing` item's comment said `docs/the-routing-check.md` *At the pull request* spells the key. `git grep` finds the key in no file under `docs/` (executed), so that clause was removed and the comment names the one case left. Commit 1e568e6f.

**Departure: the fixture's `.specseal` line changed wording.** `tests/test_censuses.py`'s kept-names fixture gave `.specseal` as `git mv .specseal/README.md seal/README.md`. That was the 0.3.x move by hand, and no README gives it now. The line now reads as the policy sentence that keeps the name. The case only needs a line that spells the item, so it tests the same thing. The fixture lost its lines for the five removed items, one in each of the three commits that removed them. Commit 1e568e6f.

**The plan's `git grep` lists the recorded eval cases alone.** `git grep -n -i -E 'specseal@|specseal:start|SpecSeal\.git' -- ':!seal/threads'` prints four lines, each `evals/behaviour/proofer/replay-*/scaffold.sh:3` (executed after 1e568e6f). The plan's cell expected `KEPT_OLD_NAMES` lines in the output too. No such line is left, because every item that matched one of the three patterns has left the tuple. The result is a subset of what the cell allows.

**Gaps fold.** Phase 2 wrote a paragraph in `gaps.md` *Not done* saying the check line of the `add` item for `docs/the-routing-check.md` *The routing check* did not name `tests/hooks/test_dispatch.py`. At b074601f the orchestrator added that module to the line in `frame/design.md` (read: the item's `check:` line names `tests/hooks/test_routing_edit_gate.py tests/hooks/test_dispatch.py`) and recorded the judgment in `frame/plan.md` *Judgments of the run*. The paragraph no longer describes an open item, so this phase removed it from `gaps.md`.

**The platform pages, re-opened 2026-10-31 at 10:20 UTC.** Both pages were fetched with `curl` as Markdown, and each sentence below was found by `grep -F` and copied from the file (executed).

- `https://code.claude.com/docs/en/plugins/host-marketplace.md`, *Host and maintain a marketplace*, *Host your marketplace*: "To pin a branch or tag of a GitHub or git-URL marketplace, tell users to append `#<ref>`, as in `your-org/your-marketplace#stable`."
- The same page, *Migrate users with a renames map*: "Treat `renames` as append-only history. Keep old entries after everyone has migrated."
- `https://code.claude.com/docs/en/plugin-marketplaces.md`, *Create a marketplace*, *Remove the marketplace to start over*: "To remove everything and start over, run `claude plugin marketplace remove my-marketplace` in your shell. The command removes the marketplace and uninstalls its plugins."

The frame says neither page explains how a pinned install moves off its ref. A `grep -i` of both files for `unpin`, `move off`, `change the ref`, `remove.*ref` and `update.*#` found no sentence that does (executed). That search is a sample: the pages were not read whole. The `gaps.md` *Not verified* row for the path names the repository owner at the 0.27.0 release.

**How the class was enumerated (contract rule 12).** The list was built from the names the removed units define and the names that cite them. `git grep -n -i -E` over the tree, outside the records, `.test_durations` and the recorded eval cases, searched for `before the rename`, `old slug`, `old_slug`, `OLD_CLONE`, `carries_clone`, `OLD_PLUGIN`, `marketplace remove`, `old install`, `old markers`, `specseal:`, `Coming from`, `오는 경우`, `rewrote {` and `rewritten workflow` (executed after 1e568e6f). Every remaining hit is of a kind the frame keeps:

- the `SpecSeal-Routing` pin and its census comment (`frame/design.md` *Out of scope, found and kept*);
- `tests/test_censuses.py:22`'s history of when `old_names` was seen red;
- `tests/hooks/test_routing.py:135`, which pins a routing answer written before the rename as unread. *Out of scope* does not name it, but it is the same kind as the cases that pin an old name as unread, and it reads nothing old, so it stays.

The method lists spellings of the removed units' names. A sentence that describes the install move, the old markers or the old workflow in other words is outside it, so the list is a sample for paraphrase. `gaps.md` already gives the proofer a row for that kind of sample.

**The phase-boundary set.** One `bin/test` command ran 115 modules at 1e568e6f, before this record, `gaps.md` and the Status cell were written. The set is the four modules in the plan's Verified-by cell, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/github/test_rules.py`, plus every test module whose text names a README, `update`, `seal.py`, `hygiene.yml`, the census module, `skills` or `templates`, or that walks the tree (`rglob`, `os.walk`, `ls-files`). That includes `tests/e2e/teammate/test_teammate_flow.py`, whose target is `templates/setup/hygiene.yml`. Result: 5081 passed, 9 skipped, exit 0 (executed). Each changed file's census case runs in `tests/test_censuses.py` or in the module that targets the file. `bin/seal rules --check` exited 0, with the same two lines of *Where the routing is checked* excused (executed).

**No `seal mutate` run for the removals.** A removal adds no behaviour (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*), and the existing cases prove it: the case for a workflow without the clone line (`Test_workflow_at`'s `no clone line`, `Test_install_workflow`'s `a file there`) holds S4. The three mutation runs above cover the case this phase rewrote and the two tests it inlined.

**`.test_durations` still lists the three removed cases.** These are `test_accepts_a_file_cloning_the_old_slug_as_its_own`, `test_accepts_its_own_file_under_the_old_slug_by_rewriting_it` and `test_step_4_takes_out_a_block_under_either_markers_whatever_it_holds`. `frame/plan.md` *Operational impact* leaves that file to the test runner.
