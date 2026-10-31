# Design: 1793438028-pre-0-23-upgrade-readings-removed

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| The owner's comment on #1154, 2026-10-31 (read, `gh issue view 1154 --json body,comments`) | A straight upgrade from a release before 0.23.0 is no longer supported. Each reading kept for one goes with its pins, its census items, and the code and README section it describes. None is kept with a comment. A person on such a release upgrades through an intermediate release or moves their files by hand. |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* | A mechanism stays only while what it caught outweighs what it costs. A change removes, in the same commit, what stood on the old fact: a check, an exception, a comment, a copy. So every citation of a removed file is rewritten in the commit that removes the file. |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The pull request does not edit `docs/`. The three policy documents that describe these readings change through `## Rule changes` below, and the settle after 0.27.0 writes them. |
| `.github/scripts/rules.py` module docstring (read) and `skills/settle/SKILL.md` *A rule has one shape* | `seal rules --check` refuses a check line that names a file the tree no longer holds. It excuses such a line only inside a section that a pending `remove` with no `from` takes out. A pending `change`, or a `remove` with a `from`, excuses nothing, "so the test the line names stays until the settle". `docs/the-routing-check.md` names `tests/hooks/test_stub_remove.py` in two check lines of *Where the routing is checked*, so that section is removed whole and its one surviving paragraph is added to the document's opening section (`plan.md` Alternatives C). |
| `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser` (read) | A citation in `docs/` of a section the diff removes, such as README.md *Coming up from 0.3.x*, is excused where a pending item's `from` holds the citation and its `to` does not. Every docs citation of a removed README section stands inside such a `from` below. |
| `tests/behaviour/test_no_document_names_the_old_roots.py#KEEP` (read) | Each entry is checked to still occur somewhere. The four entries that name the README's 0.3.x section leave with it. The two entries for the policy sentence `specs/` or `.specseal/` stay, because that sentence stays in both editions. |
| `docs/the-record-layout.md` *A change writes fragments, never a shared file* | The diff changes `skills/implement/bootstrap.md` and `agents/proofer.md`, so `changelog.md` ends with `### Process changes` in the shape of `templates/records/process.md`. |
| Claude Code, *Host and maintain a marketplace*, *Migrate users with a renames map* (read, fetched 2026-10-31 from `code.claude.com/docs/en/plugins/host-marketplace.md`) | "Treat `renames` as append-only history. Keep old entries after everyone has migrated." The `renames` entry of `.claude-plugin/marketplace.json` is the platform's, and it stays. |
| Claude Code, *Host and maintain a marketplace*, *Host your marketplace* (read, fetched 2026-10-31 from `code.claude.com/docs/en/plugins/host-marketplace.md`), and *Create a marketplace*, *Remove the marketplace to start over* (read, fetched 2026-10-31 from `code.claude.com/docs/en/plugin-marketplaces.md`) | "To pin a branch or tag of a GitHub or git-URL marketplace, tell users to append `#<ref>`, as in `your-org/your-marketplace#stable`." And: "`claude plugin marketplace remove my-marketplace` … removes the marketplace and uninstalls its plugins." These two sentences are all the release note's upgrade path stands on. Neither page says how a pinned install moves off its ref, and nobody has run the path end to end (*Scope*, *The release note*). |
| Precedent: work item 1793240969, `frame/questions.md` at `53f21b54^` (read) | A `KEPT_OLD_NAMES` item stays while a line of the policy root spells it, because the pull request cannot edit that line. Its comment is rewritten to name the readers left. Q1 there is the question the owner's comment answers now. |
| `hook-install.py` left in v0.22.4 (executed: `git tag --contains 61a8455a` lists v0.22.4 first) | The git hook stubs were written only by releases up to 0.22.3. `hooks/stub-remove.py` has taken them out at every session start since 0.22.4. A clone a release from 0.23.0 on has started a session in holds none. Its own docstring sets its sunset at "once no clone a supported release reaches still carries a stub", and the owner's decision meets it. |
| `install.sh` and `uninstall.sh` left in v0.25.0 (executed: `git tag --contains 334189fd`) | The issue's coordinates for the old CLAUDE.md markers predate #1186. The markers now stand in `skills/update/SKILL.md` step 4's `PAIRS`, in `tests/behaviour/test_the_old_block_leaves_through_update.py`, and in `tests/censuses.py#KEPT_OLD_NAMES`. The file the issue names, `test_the_installer_writes_the_block_from_its_template.py`, no longer exists. |
| The issue's other coordinates, reopened 2026-10-31 (read) | `skills/implement/bootstrap.md:33-38` and `:40-51` hold the two paragraphs. `skills/implement/scripts/seal.py:1489` holds `OLD_PLUGIN_CLONE`. `templates/setup/hygiene.yml:8-9` and `README.md` *Coming from `specseal@specseal`* describe it. |
| Unsettled designs' `## Rule changes` (read, every `seal/threads/*/frame/design.md`) | None touches the text changed below. 1793343707 changes other rows of `docs/the-record-layout.md` *seal/threads/<work-item-id>/*, a different sentence of the same section. |
| `seal/follow-up.md` (read) | No row waits on this work. |

## Scope

**The class.** A reading of this class is code, text or a test kept only so
that a repository, a clone, a machine or an install last run under a release
before 0.23.0 reaches the current layout with no step of its own. The list
was built from what makes the class, the releases that changed something in
a person's tree, clone, machine or install. That is 0.23.0's rename (its
release notes' *Changed*, *Compatibility* and *Removed* entries, read),
0.22.4's removal of the git hooks (#1027), and the 0.3.x layout. Each name
those changes replaced was then searched with `git grep` (executed): `specseal`
case-folded, `0.3.x`, `seal/specs`, `EARLIER_HEADINGS`, `root-migrate`,
`stub-remove`, `OLD_START`, `OLD_PLUGIN_CLONE`, `KEPT_OLD_NAMES`, `before the
rename` and `earlier release`. The release notes of 0.20.0 through 0.25.0
were also read for `Compatibility` and `next minor` lines. The method lists
every change a release note names. A reading added for a release earlier
than 0.20.0 and named in no note is outside what it lists, so the list is
whole for 0.20.0 onward and a sample before that.

**In scope, as the issue lists them:**

1. The CLAUDE.md block markers a release before the rename wrote:
   `skills/update/SKILL.md` step 4's second pair in `PAIRS` and the clause
   naming it, the old-marker half of
   `tests/behaviour/test_the_old_block_leaves_through_update.py`, and their
   `KEPT_OLD_NAMES` items.
2. The old workflow clone line: `seal.py#OLD_PLUGIN_CLONE`, the second arm
   of `#carries_clone`, the `old_slug` path of `#install_workflow` with its
   "rewrote … before the rename" message, the clause of
   `templates/setup/hygiene.yml`'s header, the paragraph in `README.md`
   (it stands inside *Coming from `specseal@specseal`*, item 6), the two
   cases of `tests/skills/test_seal.py` built on `OLD_CLONE`, and its
   `KEPT_OLD_NAMES` item.
3. The bootstrap's 0.3.x paragraph and `README.md` *Coming up from 0.3.x*,
   with both READMEs' editions of that section.
4. The bootstrap's paragraph on a root an earlier release wrote, with
   `hooks/lib/optin.py#EARLIER_HEADINGS`, `#earlier`, and
   `hooks/root-migrate.py` whole.

**In scope, found beyond the issue's list:**

5. `hooks/stub-remove.py` and `tests/hooks/test_stub_remove.py`, with the
   `session-start` entry in `hooks/dispatch.py#GROUPS`. It reads git hook
   stubs that only releases up to 0.22.3 wrote (*Grounding*).
6. `README.md` *Coming from `specseal@specseal`* and its Korean edition: the
   commands that move an install made before the rename. Its
   `KEPT_OLD_NAMES` items `specseal@specseal` and `marketplace remove
   specseal` go with it.
7. The readers of `optin.earlier` outside the bootstrap:
   `seal.py#earlier_root` with its three callers (`no_root`, `import_`,
   `install_workflow`), `skills/config/SKILL.md` *Where the file is*'s
   paragraph "A root from a release before the rename", and the exception
   sentence of `templates/setup/seal-README.md` and `seal/README.md`.
8. `hooks/root-migrate.py`'s state rename (`rename_state`): each
   `specseal-` file under the git directory and `~/.claude/specseal/` take
   the plugin's name at every session start. It goes with the file. A
   machine last run under 0.22.x keeps its old state files, which nothing
   reads.
9. Every text that cites a removed unit, rewritten so it stands without
   it. These are the `seal.py` docstrings that cite `hooks/root-migrate.py#under`,
   `#dirty` and the 0.3.x carry-over, `agents/proofer.md`'s check line
   naming `tests/hooks/test_root_migrate.py`, and the docstrings and entries
   in tests that cite a removed unit (*Removes*).
10. The policy text that describes items 3, 4, 5 and 8, in
    `docs/one-root-by-lifetime.md` and its Korean edition,
    `docs/the-record-layout.md` and `docs/the-routing-check.md`, as
    `## Rule changes` below.

**Out of scope, found and kept:**

- The `renames` entry of `.claude-plugin/marketplace.json` and its
  `KEPT_OLD_NAMES` item. The platform reads it, and its reference says to
  keep it as append-only history (*Grounding*).
- `skills/settle/scripts/rule_changes.py#EARLIER`. It places a thread
  whose design was first added under `seal/specs/` by that commit. Such a
  thread exists in a repository that took the supported path through
  0.23.0's move and has not settled since, so it is not a straight-upgrade
  reading.
- `skills/verify/scripts/unverified_check.py#OLD_MARK`, the U+2705 a closed
  row opened with before 0.22.1. It reads a base revision, which is history
  any repository may compare against, not a state a person upgrades from.
- `chain_check.py`'s absent reading of the `SpecSeal-Routing:` trailer, and
  its pin `tests/skills/test_chain_check.py#Test_routing_trailers`. #1142
  removed the reading, and the pin holds that an unknown trailer key is not
  judged. The `KEPT_OLD_NAMES` item stays for that case. Its comment's
  clause on `docs/the-routing-check.md` is stale (that sentence was
  settled out) and is corrected in place, since phase 3 edits that tuple.
- The cases that pin an old name as unread: `tests/hooks/test_optin.py`'s
  legacy-directory and legacy-address cases,
  `tests/behaviour/test_release_hygiene.py#test_this_repository_has_one_root_laid_out_by_lifetime`,
  `tests/behaviour/test_the_set_a_work_item_always_has.py`'s `.specseal/tasks`
  case, and the `legacy` fixture in `tests/conftest.py`. They read nothing
  old. Each docstring that says `hooks/root-migrate.py` reads the name is
  corrected (item 9).
- History that names the old layout as the reason for a current rule:
  `hooks/lib/config.py#reference_roots`'s docstring on 0.3.x,
  `templates/setup/config.md`'s row for no root, `seal.py`'s module
  docstring on #104, `hooks/lib/routing.py`'s note on a `rounds` file, and
  `tests/behaviour/test_chain_hooks_hardening.py`'s "seen red at
  `5287dd42`". The rule each justifies stands on its own.
- The evals' generators and recorded cases that read `seal/specs/` at a
  tag of this repository. They read this repository's history.
- `SPECSEAL_LINT` and `SPECSEAL_LANG`. They are the variables' current
  names, and nothing reads a second name.

**The release note.** `changelog.md` says that a straight upgrade from a
release before 0.23.0 is no longer supported. It names the two ways
through, and states of the first only what the platform's reference
supports (*Grounding*, the row on the `#<ref>` form):

- Go through 0.26.0, the last release that carries every reading this
  work removes. The reference supports these steps: remove the old
  marketplace, which uninstalls its plugins; add
  `MichaelYcJo/AgenticSeal#v0.26.0`, the `#<ref>` form pinning a tag; and
  install `agentic@agenticseal` from it. Then start a session in each
  clone, commit the move, and run `/agentic:update`. Reaching 0.27.0
  afterwards is said only as removing the pinned marketplace, adding it
  again without the ref and installing `agentic@agenticseal` again, since
  the remove uninstalls the plugin; the reference names the first two acts,
  and the third is the install the first step already uses. The note does
  not promise that the path works end to end. It says nobody has run it on
  a machine holding such an install, as 0.23.0's note said of its own
  three commands.
- Move the files by hand.

It also names the one leftover a person sees on the second way: git hook
stubs, deleted by removing the hook files whose second line starts with the
old marker. The first way leaves none, because 0.26.0's session start runs
`hooks/stub-remove.py` in each clone the way starts a session in.

This path is the one thing the frame leaves unverified on purpose. Running
it would change this machine's plugin configuration, so no party runs it.
Phase 3 re-opens the two pages and quotes the sentences, with each URL and
the date read, in its phase record. `gaps.md` *Not verified* carries one
row for the path as a whole, unrun end to end, answered by the repository
owner at the 0.27.0 release.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. No session start moves anything | Given a clone whose tree holds `seal/specs/<id>/` under a `seal/README.md` opening with a heading 0.22.x wrote, when a session starts, then the `session-start` group runs `version-check.py` alone and nothing is staged or said | `tests/hooks/test_dispatch.py`'s group case asserts `GROUPS["session-start"] == ("version-check.py",)`; `git ls-files hooks/root-migrate.py hooks/stub-remove.py` prints nothing |
| S2. A root an earlier release wrote reads as a project's own | Given that `seal/`, when the bootstrap or a `seal` subcommand meets it, then it is a `seal/` whose README does not open with the marker: first setup writes nothing into it and offers the root under the git directory, and `seal import`, `seal mode` and `seal pr-checks install` answer as they answer for any directory without the marker | `tests/behaviour/test_first_setup_asks_once.py` reads the bootstrap's one paragraph on a `seal/` without the marker, and no paragraph on an earlier heading; `tests/skills/test_seal.py` holds no case calling `earlier_root` |
| S3. The update takes out one pair of markers | Given a user `CLAUDE.md` holding a block under `<!-- agentic:start -->`, when step 4 of `/agentic:update` runs, then that block goes after a backup; the step names no other pair | `tests/behaviour/test_the_old_block_leaves_through_update.py`, its either-markers case rewritten over the one pair |
| S4. The workflow install reads one clone line | Given `.github/workflows/hygiene.yml` that does not carry `PLUGIN_CLONE`, when `seal pr-checks install` runs, then it is somebody else's file and is kept, whatever repository it clones | `tests/skills/test_seal.py`'s existing case of a workflow without the clone line; the two `OLD_CLONE` cases are gone |
| S5. The READMEs give no straight-upgrade path | Given either README edition, when a person reads *Install*, then no section moves an install, a layout or a workflow from before 0.23.0, and the gate table has no row for a script `GROUPS` does not register | `tests/behaviour/test_chain_hooks_hardening.py#test_the_gate_table_has_one_row_for_each_script_groups_registers`; `tests/behaviour/test_no_document_names_the_old_roots.py`, whose `KEEP` entries are each checked to occur |
| S6. No living file spells a removed name, and each kept spelling names a reader | Given the tree after the build, when `old_names` reads it, then no line spells an old name outside `KEPT_OLD_NAMES` and the records, and each item left names a file that still spells it | the suite case that runs `tests/censuses.py#old_names` over the tree, and `tests/test_censuses.py` with its fixture rewritten |
| S7. The policy's rule changes stand pending, and nothing dangles until the settle | Given this design pending, when `seal rules --check` and the citation case read the tree, then the check lines of *Where the routing is checked* print as excused by this work item, and each docs citation of a removed README section is excused by an item below | `tests/github/test_rules.py`; `tests/behaviour/test_a_cited_section_stands_in_its_file.py` |
| S8. A person on a release before 0.23.0 learns the path | Given the 0.27.0 release note, when that person reads it, then it says the straight upgrade is unsupported, names the two ways and the stub leftover, says no more of the first way than the quoted reference supports, and says it was not run end to end (*Scope*, *The release note*) | `changelog.md`, read by the sealer against the quotes in phase 3's record; `gaps.md` *Not verified*'s row for the path, answered by the repository owner at the release |

## Data & interfaces

- `hooks/dispatch.py#GROUPS`: `session-start` becomes `("version-check.py",)`,
  and the comment naming the stubs goes.
- `hooks/lib/optin.py`: `EARLIER_HEADINGS` and `earlier` leave the module's
  public names. A `seal/` is the plugin's root where `marked` is true, and
  every other `seal/` is a project's own.
- `skills/implement/scripts/seal.py`: `earlier_root`, `OLD_PLUGIN_CLONE` and
  the `old_slug` branch of `install_workflow` leave. `carries_clone` reads
  `PLUGIN_CLONE` alone, so it may fold into its callers; the build decides.
  The message `rewrote <workflow>, which cloned the plugin from the
  repository's name before the rename, …` is no longer printed. The line
  `<root>/ is this plugin's root from a release before the rename, …` is no
  longer printed by `seal import`, `seal mode` or `seal pr-checks install`.
- `skills/update/SKILL.md` step 4's command: `PAIRS` holds one pair.
- Nothing is added: no new mark, check, hook or line grammar.

## Rule changes

- change
  file: docs/one-root-by-lifetime.md
  section: The root and its lifetimes
  from: and no code of the plugin opens a
    top-level `specs/` or `.specseal/`: the 0.3.x layout moves by hand, with the
    commands README.md *Coming up from 0.3.x* gives, and that section says it is
    the only path.
  to: and no code of the plugin opens a
    top-level `specs/` or `.specseal/`.
- change
  file: docs/one-root-by-lifetime.md
  section: The opt-in signal is the root itself
  from: The marker is
    the first line of `templates/setup/seal-README.md`, written at first setup and by
    the migration of a repository installed before the plugin was renamed
    AgenticSeal. The hooks look at the
    two places in that order; whichever exists with the marker says both "on"
    and which mode. A `seal/` whose README opens with a heading an earlier
    release wrote (`hooks/lib/optin.py#EARLIER_HEADINGS`) is that release's root,
    which the session-start migration rewrites to the marker; until it does,
    it reads as not opted in, and first setup creates no second root beside
    it. A `seal/` whose README opens with neither is a project's own directory,
  to: The marker is
    the first line of `templates/setup/seal-README.md`, written at first setup.
    The hooks look at the
    two places in that order; whichever exists with the marker says both "on"
    and which mode. A `seal/` whose README does not open with the marker is a
    project's own directory,
- remove
  file: docs/one-root-by-lifetime.md
  section: What first setup asks
  from: A repository still on
    the 0.3.x layout is told, not asked, that it moves by hand with the commands
    README.md *Coming up from 0.3.x* gives (`skills/implement/bootstrap.md`). A repository installed before the plugin was renamed
    AgenticSeal has its work items moved into the thread layout by the
    session-start hook, on each branch whose tree still holds them. No stamp
    stands between a branch and its move. So in a repository that left shared
    mode for local mode, a branch cut before the switch has its own `seal/`
    moved and marked in the tree, and the hooks read that root first
    (`hooks/root-migrate.py`, its boundaries).
- remove
  file: docs/one-root-by-lifetime.ko.md
  section: 루트와 그 안의 수명
  from: 0.3.x 배치는 README.md *Coming up
    from 0.3.x* 가 주는 명령으로 손으로 옮기고, 그 절은 그것이 유일한 길이라고
    말합니다.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 옵트인 신호는 루트 자체다
  from: 표식은
    `templates/setup/seal-README.md` 의 첫 줄이고, 처음 설정과, 플러그인 이름이 AgenticSeal 로
    바뀌기 전에 설치된 저장소의 이전이 이것을 씁니다. 훅은 두 자리를 그 순서로 보고, 표식과 함께
    있는 쪽이 "켜졌다" 와 "어느 모드인가" 를 함께 말해 줍니다. README 가 이전
    릴리스가 쓴 제목(`hooks/lib/optin.py#EARLIER_HEADINGS`)으로 시작하는 `seal/` 은
    그 릴리스의 루트이고, 세션 시작의 이전이 표식으로 다시 씁니다. 그 전까지는
    옵트인하지 않은 것으로 읽고, 처음 설정은 그 옆에 두 번째 루트를 만들지
    않습니다. README 가 그 어느 쪽으로도 시작하지 않는
    `seal/` 은
  to: 표식은
    `templates/setup/seal-README.md` 의 첫 줄이고, 처음 설정이 이것을 씁니다. 훅은
    두 자리를 그 순서로 보고, 표식과 함께
    있는 쪽이 "켜졌다" 와 "어느 모드인가" 를 함께 말해 줍니다. README 가 표식으로
    시작하지 않는 `seal/` 은
- remove
  file: docs/one-root-by-lifetime.ko.md
  section: 처음 설정에서 무엇을 묻는가
  from: 0.3.x 배치에 머물러 있는
    저장소에는 묻지 않고, README.md *Coming up from 0.3.x* 의 명령으로 직접
    옮긴다고 알리기만 합니다(`skills/implement/bootstrap.md`).
    플러그인 이름이 AgenticSeal 로 바뀌기 전에 설치한 저장소는 트리에 앞선
    배치가 남아 있는 브랜치마다 세션 시작 훅이 작업 항목을 스레드 배치로
    옮깁니다. 이미 옮겼다는 기록이 브랜치의 이동을 막지 않습니다. 그래서 shared
    모드에서 local 모드로 옮긴 저장소에서는 전환 전에 만든 브랜치의 `seal/` 이
    트리 안에서 옮겨지고 표식이 붙으며, 훅은 그 루트를 먼저 읽습니다
    (`hooks/root-migrate.py` 의 경계).
- change
  file: docs/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: go with the directory, whole, when the settle removes it. A
    repository installed before the plugin was renamed AgenticSeal holds the
    files at their old names in the earlier layout, which
    `hooks/root-migrate.py#THREAD_PATHS` maps onto this one, and the hook moves them into this layout
    at the session start of each branch whose tree still holds them, as staged
    `git mv` in shared mode and as renames under the git directory in local mode
    (*The fold, and what tells it from a deletion* above, and
    `docs/release-checklist.md` *2b*).
  to: go with the directory, whole, when the settle removes it
    (*The fold, and what tells it from a deletion* above, and
    `docs/release-checklist.md` *2b*).
- remove
  file: docs/the-routing-check.md
  section: Where the routing is checked
- add
  file: docs/the-routing-check.md
  section: The routing check
  to: **A session's routing is checked where the session acts, at its edit tools
    before the first edit, and again at the pull request; this plugin writes
    nothing into a clone's git hooks.** The routing governs a session, and
    git's hooks run for every commit made in the clone, a person's own from a
    terminal included. The hooks slot is also where husky, the pre-commit
    framework and lefthook live, and a line or an entry in their committed
    configuration reaches every teammate. A check at git's level reaches people
    who do not use this plugin, with an experience they did not ask for (the
    owner, 2026-10-25).
    check: tests/hooks/test_routing_edit_gate.py tests/hooks/test_dispatch.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The session-start move of an earlier layout, its README rewrite and its state rename | `hooks/root-migrate.py` | Nowhere. A repository a release from 0.23.0 on started a session in was moved then; a straight upgrade is unsupported (owner, 2026-10-31) |
| The move's cases | `tests/hooks/test_root_migrate.py`, `tests/behaviour/test_the_root_migrates_itself.py` | Go with the code they read |
| The git hook stub remover and its cases | `hooks/stub-remove.py`, `tests/hooks/test_stub_remove.py` | Nowhere. Stubs were written up to 0.22.3 and removed at every session start since 0.22.4; the release note says how a person deletes one by hand |
| Both scripts' registration | `hooks/dispatch.py#GROUPS`, the `session-start` entries and the stub comment | The group keeps `version-check.py` |
| The headings 0.22.x's root README opened with | `hooks/lib/optin.py#EARLIER_HEADINGS`, `hooks/lib/optin.py#earlier`, and the module docstring's "except one whose README opens with one of `EARLIER_HEADINGS`" | `hooks/lib/optin.py#marked` alone decides; a `seal/` without the marker is a project's own |
| The refusal beside an earlier root | `skills/implement/scripts/seal.py#earlier_root` and its calls in `#no_root`, `#import_` and `#install_workflow`; `tests/skills/test_seal.py#Test_import_` `test_refuses_beside_a_root_an_earlier_release_wrote` | The answer for a directory without the marker, which each of the three already gives |
| The bootstrap's two paragraphs, and "nor one of those headings" in the third | `skills/implement/bootstrap.md` *Orchestrator: Bootstrap* | The third paragraph, on a `seal/` without the marker |
| The paragraph on a root from before the rename | `skills/config/SKILL.md` *Where the file is* | The paragraph "No root at either place" and the bootstrap |
| The exception sentence on an earlier heading | `templates/setup/seal-README.md` and `seal/README.md`, the paragraph on the marker before *Export rules* | Nowhere; the two files stay byte for byte equal |
| The old CLAUDE.md markers | `skills/update/SKILL.md` step 4, the pair `<!-- specseal:start -->`/`<!-- specseal:end -->` in `PAIRS` and the clause naming it; `tests/behaviour/test_the_old_block_leaves_through_update.py#OLD_START` and the old-marker block of `test_step_4_takes_out_a_block_under_either_markers_whatever_it_holds` | Step 4 takes out the `agentic` pair, which 0.23.0 to 0.24.x wrote |
| The old workflow clone line | `skills/implement/scripts/seal.py#OLD_PLUGIN_CLONE`, its arm in `#carries_clone`, the `old_slug` path of `#install_workflow` and its message; the header clause of `templates/setup/hygiene.yml`; `tests/skills/test_seal.py#OLD_CLONE` and the two cases built on it | A workflow without `PLUGIN_CLONE` is somebody else's, pinned by the existing case for one |
| The README sections for a straight upgrade | `README.md` *Coming from `specseal@specseal`* and *Coming up from 0.3.x*; `README.ko.md` *`specseal@specseal` 에서 오는 경우* and *0.3.x 에서 올라오는 경우* | The 0.27.0 release note (*Scope*, *The release note*) |
| The gate table rows for the two scripts | `README.md` *The gates* and `README.ko.md`'s edition, rows `stub-remove` and `root-migrate` | Nowhere; the table lists what `GROUPS` registers |
| The 0.3.x case | `tests/behaviour/test_first_setup_asks_once.py#test_the_0_3_x_layout_is_sent_to_the_by_hand_path_and_the_bootstrap_goes_on`, `#OLD_LAYOUT`, `#EARLIER_SEAL` and the assertions on it | Nowhere |
| Census items for removed spellings | `tests/censuses.py#KEPT_OLD_NAMES` items for the two markers, `MichaelYcJo/SpecSeal.git`, `specseal@specseal` and `marketplace remove specseal`; `#KEPT_FILES` entries for the three root-migrate files; the matching lines of `tests/test_censuses.py`'s kept-names fixture | No living file spells them after the build. The items `# specseal-git-hook` and `.specseal` stay with their comments rewritten: `docs/the-routing-check.md` and `docs/one-root-by-lifetime.md` spell them until the settle, and the absence cases spell `.specseal` after it |
| `KEEP` entries for the README's 0.3.x section | `tests/behaviour/test_no_document_names_the_old_roots.py#KEEP`: `` `.specseal/scratch` ``, `` (`.specseal/`, `specs/<id>/`) ``, `git mv .specseal/`, `git mv specs/<id>` | Each entry must occur, and its line leaves with the section |
| Entries and citations of removed units | `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#LISTS_A_FIXTURE` entries for the root-migrate files; `agents/proofer.md`'s check target `tests/hooks/test_root_migrate.py`; the `seal.py` docstrings citing `hooks/root-migrate.py#under` and `#dirty` and the 0.3.x carry-over; the docstrings of `tests/hooks/test_optin.py`, `tests/hooks/test_dispatch.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_first_setup_asks_once.py` and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` that name either script | Each is rewritten to stand without the unit, or removed where it was only about it; `tests/hooks/test_dispatch.py`'s cases that plant a fake gate under either script's name take a registered name |
| The policy sentences on these readings | `docs/one-root-by-lifetime.md`, `docs/one-root-by-lifetime.ko.md`, `docs/the-record-layout.md`, `docs/the-routing-check.md`, as `## Rule changes` states | The settle after 0.27.0 writes them |

Framed 2026-10-31 by framer, before the build.
