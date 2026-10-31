# Implementation Plan: 1793438028-pre-0-23-upgrade-readings-removed

## Technical context

The readings sit at three places a person's state lives, and each phase
takes one place whole.

- **The repository.** `hooks/root-migrate.py` (640 lines) runs in
  `hooks/dispatch.py:95`'s `session-start` group. It rewrites a `seal/README.md`
  that opens with `hooks/lib/optin.py:80`'s `EARLIER_HEADINGS`, moves
  `seal/specs/<id>/` into `seal/threads/<id>/` (`THREAD_PATHS`), and renames
  the `specseal-` state files and `~/.claude/specseal/` (`rename_state`). It
  calls `skills/implement/scripts/seal.py#workflow_at` to name a workflow
  written before the rename. `optin.earlier` (`hooks/lib/optin.py:228`) is
  read by `seal.py:786` (`no_root`), `:1093` (`import_`) and `:2027`
  (`install_workflow`), each printing `seal.py:759`'s `earlier_root` line.
  The bootstrap states both repository readings at
  `skills/implement/bootstrap.md:33-38` and `:40-51`, and
  `skills/config/SKILL.md:23-27` restates the second. `README.md:380-415`
  and `README.ko.md:373-408` hold the 0.3.x by-hand commands, whose last
  step leaves the work items at `seal/specs/<id>/` for `root-migrate.py` to
  finish.
- **The clone.** `hooks/stub-remove.py` (115 lines) runs in the same group
  and deletes hook files whose second line starts with
  `# specseal-git-hook`.
- **The install and the workflow.** `skills/update/SKILL.md:142-145`'s
  `PAIRS` holds the `specseal` marker pair. `seal.py:1489`'s
  `OLD_PLUGIN_CLONE` is read by `carries_clone` (`:1949`), which
  `workflow_at` (`:1974`) and `remove_workflow` (`:2150`) call, and
  `install_workflow` rewrites such a file through its `old_slug` path
  (`:2036-2043`, `:2106-2110`). `README.md:309-339` and
  `README.ko.md:303-333` hold the reinstall commands and the workflow
  paragraph.

Two constraints the tree sets on the build:

- The pull request does not edit `docs/`. A `docs/` check line naming a
  deleted test is refused by `seal rules --check` unless a pending `remove`
  with no `from` takes out its section. `frame/design.md`'s `## Rule
  changes` removes `docs/the-routing-check.md` *Where the routing is
  checked* whole for that reason. The probe below shows both of its check
  lines excused.
- `tests/censuses.py#old_names` reads every living file, `docs/` included.
  A `KEPT_OLD_NAMES` item stays while a line the build cannot edit spells
  it.

**Executed probe, 2026-10-31.** From a `git clone --no-local` of this
branch at `b212e774`, with this design copied in,
`skills/settle/scripts/rule_changes.py#parse` read `## Rule changes` with
no error and no unread line. Each of the seven items with a `from` found it
in its section by `#pattern`. `#removed_by` returned this work item for
`docs/the-routing-check.md` lines 20 and 32, the two check lines naming
`tests/hooks/test_stub_remove.py`.

**What breaks in six months.** A person who skipped every release from
0.23.0 to 0.26.x and updates straight to 0.27.0 or later gets no move and no
message. Their `seal/` reads as a project's own, so first setup offers a
second root under the git directory. Their CLAUDE.md block stays, and a
workflow cloning the old repository name passes every pull request having
examined nothing. Git hook stubs keep running the old plugin copy at each
commit for as long as that copy is on disk. The release note is the one
place that tells them (`frame/design.md` *Scope*, *The release note*). The
owner accepted this cost on 2026-10-31.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Remove only the readings the issue lists, and keep `hooks/stub-remove.py` | The stub remover reads stubs only releases up to 0.22.3 wrote, the class the owner ended support for. It keeps running at every session start in every git repository, opted in or not, and keeps its policy paragraph, its test and its census item. Its own docstring's sunset condition is met (`frame/design.md` *Grounding*) | Rejected. Contract rule 12 asks for the class, and the owner's principle covers it |
| B. Keep `hooks/root-migrate.py`'s state rename alone and drop the layout move | The rename is the same class: a machine last run under 0.22.x. Keeping it keeps the file, its census exemption and its tests for a rename every supported machine has already had | Rejected |
| C1. `docs/the-routing-check.md`: remove *Where the routing is checked* whole, and add its one surviving paragraph to the document's opening section *The routing check* | The opening section's first sentence already summarises the paragraph it receives, so the settled document says the routing is checked at the edit tools and the pull request twice, a summary and the rule. The settling session may fold the two | Chosen. It is the one shape `seal rules --check` excuses, so the hook and its test leave in the same pull request. Only `hooks/stub-remove.py:4` cites the section, and it leaves too (`git grep`, executed) |
| C2. Remove only the stub paragraph with a `from`, and keep the hook and `tests/hooks/test_stub_remove.py` until the settle after 0.27.0 | The hook ships in 0.27.0 against a decision made before it, and a second work item is owed after the settle for code that could have gone now | Rejected |
| C3. Delete the hook and keep its test file until the settle | The test loads the hook it tests, so it fails at once | Not possible |
| D. Delete the pins of a removed reading | A future change could bring an old reading back with nothing red. That is the case for any removed code. The behaviour left, such as a workflow without `PLUGIN_CLONE` reading as somebody else's, is already pinned by existing cases | Chosen |
| E. Rewrite each pin into its opposite, as work item 1793240969 did (its Alternatives B and C, at `53f21b54^`) | An opposite pin asserts that an unsupported install's file is left alone, which is no contract anyone keeps. It also keeps the old spelling and its census item alive in a living file | Rejected. 1793240969's readings read records of work in flight, where an opposite pin protected a behaviour still promised. Here nothing is promised |
| F. Remove the `renames` entry of `.claude-plugin/marketplace.json` too | The platform's reference says to keep `renames` as append-only history, and removing it could break name resolution for an install that still enables the old name | Rejected. Kept, with the premise read from the platform's page on 2026-10-31 |
| G. Remove `skills/settle/scripts/rule_changes.py#EARLIER` too | A repository that took the supported path through 0.23.0's move and has not settled since holds a thread whose design was first added under `seal/specs/`. Its settle would place that thread at the move's one commit, out of merge order | Rejected. Kept: the premise is that the supported path leaves such threads, read in 0.23.0's release note ("The settle places a moved thread by the commit that first added its `spec.md`") |
| H. One phase for the whole removal | One commit spans hooks, the `seal` command, two skills, two templates, both READMEs and over a dozen test modules across three unrelated mechanisms, so a failure in one leaves no green point to bisect from | Rejected. Three phases, one per place where the state lives |
| I. Keep the policy sentence's `.specseal/` and drop only the 0.3.x clause | It keeps the old name in the policy, though "no code opens `.specseal/`" stays true | Chosen. Dropping the name would leave `test_no_document_names_the_old_roots.py#KEEP`'s two policy entries unmatched after the settle, and the settling session would meet a red it did not cause |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The repository's earlier layouts: `frame/design.md` *Scope* items 3, 4, 7 and 8, the part of item 9 that cites `hooks/root-migrate.py`, `optin.EARLIER_HEADINGS` or the 0.3.x section, both READMEs' 0.3.x section and `root-migrate` gate row, and the *Removes* rows that name them, `KEPT_FILES` and the `.specseal` item's comment among them | `tests/hooks/test_optin.py tests/hooks/test_dispatch.py tests/skills/test_seal.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/test_censuses.py`, and the module whose `test_census` reads each changed file | a47cdca3 |
| 2 | The clone's git hook stubs: `frame/design.md` *Scope* item 5, both READMEs' `stub-remove` gate row, the `# specseal-git-hook` item's comment rewritten to name `docs/the-routing-check.md` until the settle, and the *Removes* rows that name them | `tests/hooks/test_dispatch.py tests/behaviour/test_chain_hooks_hardening.py tests/github/test_rules.py tests/test_censuses.py`, with `seal rules --check` showing the two lines of *Where the routing is checked* excused | adc65876 |
| 3 | The install's and the workflow's old names: `frame/design.md` *Scope* items 1, 2 and 6, the rest of item 9, `KEPT_OLD_NAMES` cut to the items a living file still spells, the `SpecSeal-Routing` item's stale docs clause corrected, and `tests/test_censuses.py`'s fixture matched to it; the two platform pages of `frame/design.md` *Grounding* re-opened and quoted in the phase record with each URL and the date read, and `gaps.md` *Not verified*'s row for the upgrade path, as `frame/design.md` *Scope*, *The release note* states | `tests/behaviour/test_the_old_block_leaves_through_update.py tests/skills/test_seal.py tests/test_censuses.py tests/behaviour/test_no_document_names_the_old_roots.py`, and `git grep -n -i -E 'specseal@|specseal:start|SpecSeal\.git'` outside the records listing only `KEPT_OLD_NAMES` and the recorded eval cases | 1e568e6f |

## Operational impact

- **A compatibility break.** A straight upgrade from a release before 0.23.0
  stops working, as the owner decided. The changelog fragment the
  orchestrator writes says so, with the way through 0.26.0 and the by-hand
  way (`frame/design.md` *Scope*, *The release note*). The way through
  0.26.0 is stated only as far as the platform's reference supports it,
  and is unrun end to end: `gaps.md` carries that row for the repository
  owner at the release.
- **A process row is owed.** The diff changes `skills/implement/bootstrap.md`
  and `agents/proofer.md`, so `changelog.md` ends with `### Process changes`
  (`docs/the-record-layout.md` *A change writes fragments, never a shared
  file*).
- **The settle after 0.27.0** writes this design's nine items. After it, the
  `# specseal-git-hook` item in `tests/censuses.py#KEPT_OLD_NAMES` is spelt
  only by the census files, and the settling session removes it with the
  docs line. `test_no_document_names_the_old_roots.py#KEEP`'s two policy
  entries stay matched (Alternatives I).
- **`.test_durations`** holds entries for the deleted test modules. The test
  runner rewrites that file, and the build leaves it to the runner.
- No new environment variable, dependency or migration.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-10-31 | The `add` item of `## Rule changes` for `docs/the-routing-check.md` *The routing check* names `tests/hooks/test_dispatch.py` beside `tests/hooks/test_routing_edit_gate.py` on its `check:` line | Phase 2 moved the assertions that no group installs into git and that `hooks/git/` does not exist into `tests/hooks/test_dispatch.py#Test_module.test_no_group_installs_into_git_or_reads_a_commit_before_it_runs` (commit 77a3d523), so that case now holds the paragraph's "this plugin writes nothing into a clone's git hooks"; the crafter named it in `gaps.md` *Not done* and does not edit the frame | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (a decision after the frame is folded in place); `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* |
