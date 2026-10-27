# Review round 1: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

target: a0bf9209 against origin/release/v0.23.0

This is the first round, so no coordinate or fact was carried from an earlier record. Every claim below was opened in the tree at the target commit, in a clone of it. `frame/plan.md` *Verification this work item owes* binds the round: no finding asks for red-first evidence or a mutation run on a moved name or path.

## Findings

### 1. A branch checked out after the first move keeps its work item at `seal/specs/<id>/`, where no reader looks

severity: must
location: `hooks/root-migrate.py:31-35`, `hooks/root-migrate.py:544-545`, `hooks/root-migrate.py:603-607`, `tests/test_root_migrate.py:667-678`
evidence: executed `bin/test <scratch>/probe/test_tmp_round1_probe.py -s -q -p no:xdist`
verdict: open

Every work item of this plugin lives on its own branch, so a repository upgraded mid-work holds 0.22.x work items on branches other than the one its first session starts on. The move stamps the repository once (`hooks/root-migrate.py:603-607`), and every later session start returns at `attempted(root)` before it lists anything. So those branches never move.

The frame rests on the opposite. `frame/plan.md:93` rejects reading both layouts because "the migration runs at session start before any gate, so no session meets the old layout after it". The probe shows a session does meet it. In a repository whose `main` holds work item `1-a` and whose branch `feat/b` holds work item `2-b`, a session start on `main` moved `1-a` and stamped the repository. A session start on `feat/b` then printed nothing, and `optin.home_at` answered "" there, because the branch's `seal/README.md` still opens with the old heading. After `main` was merged into `feat/b`, `home_at` found the marked root, `seal/specs/2-b/routing.md` was still in place, and `routing.declarations` returned only `seal/threads/1-a/routing.md`.

From there the branch is stuck. `hooks/routing-edit-gate.py` finds no declaration naming `feat/b` and refuses every edit. `chain_check.py` from the tree reads the branch's `SpecSeal-Routing: 2-b` trailers as naming an undeclared work item and fails the pull request. The settle never sees the item. No text tells the person how to move it by hand. A `seal import` of a 0.22.x export into a stamped repository ends the same way.

The stamp guarded the 0.3.x move, which created `seal/` in the tree, and local mode keeps the tree clean. This move never creates a root: every unit comes from a root `ours` already accepts, under the directory the branch itself carries. The refusal over uncommitted work stays, and it is the one guard the branch needs.

```python
# hooks/root-migrate.py#main: no stamp stands between a branch and its move.
# The move runs inside a root `ours` accepts, so it never puts a root into a
# tree local mode keeps clean, which is what the 0.3.x move's stamp guarded.
    units = moves(root)
    if not units:
        common = optin.git_common_dir(root)
        if common:
            migrate_local(root, common)
        return
    if dirty(root, units):
        ...  # unchanged

# hooks/root-migrate.py#migrate_local: the same line goes.
#     if attempted(root):
#         return True
#
# Then `attempted`, `stamp`, `MARKER`, `has_root` and the docstring's
# "once per repository" boundary go, replaced by "wherever the layout
# stands, on any branch". `tests/test_root_migrate.py:667-678` becomes a
# case where a branch cut before the move, checked out after the move was
# committed, moves at its own session start.
```

answer:

### 2. A clone whose tree another person moved keeps `.git/specseal-scratch` and `~/.claude/specseal/`, and the opt-out stops working

severity: must
location: `hooks/root-migrate.py:452-497`, `hooks/root-migrate.py:546`, `hooks/root-migrate.py:616`, `tests/test_stub_remove.py:187`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/gaps.md:16`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/changelog.md:11`
evidence: executed `bin/test <scratch>/probe/test_tmp_round1_probe.py -s -q -p no:xdist`
verdict: open

In shared mode one person commits the move and everyone else pulls it. The state files are not in the tree. They are per clone (`.git/specseal-*`) and per machine (`~/.claude/specseal/`). `rename_state` runs only inside a move that has units (`hooks/root-migrate.py:546`, `:616`), so a clone that pulls an already moved tree never renames its own state.

The probe built that clone: a committed root opening with the marker, `seal/threads/1-a/`, `.git/specseal-scratch` and an old `pact-paths.md` in the state directory. The session start printed nothing. `.git/specseal-scratch` stayed and `.git/agentic-scratch` was not made, so `optin.home_at` answered the root: the person's throwaway opt-out no longer turns the gates off. `pact-paths.md` stayed in the old directory. `skills/verify/scripts/pact_check.py:89` reads it from `~/.claude/agentic/`, and the parity path in `skills/legacy-parity/SKILL.md:31` is read from the same new directory. Both are things a person typed.

What was claimed: `changelog.md:11` says "The migration renames each one it meets", and `frame/design.md` *The migration* says each state file beside the root is renamed. `gaps.md:16` narrows that to a move with units. Its reason is that the suite runs the real session-start group under the machine's own `HOME` (`tests/test_stub_remove.py:187`), so a rename at every session start would move this developer's installed state during the run. That is a defect of one test's isolation, not a reason to leave every pulling clone unrenamed. The same row says the merge already handles a new directory that stands. One more effect: `hooks/version-check.py` writes `~/.claude/agentic/version-check` before this hook runs, so the old directory always keeps its own `version-check`, and `os.rmdir` at `:495` never removes it.

```python
# hooks/root-migrate.py#main, right after `root` is resolved and before the
# symbolic-link check. The state is the clone's and the machine's, not the
# tree's, so it is renamed wherever it stands, whether or not this tree has
# anything left to move. `rename_state` is silent and renames only where the
# new name is free, so a second run does nothing.
    rename_state(root)
# ...and the two calls at `rename_state(root)` before `run_moves` go.
#
# hooks/root-migrate.py#rename_state: `version-check` is a cache that
# `hooks/version-check.py` rewrites daily, so where the new directory holds
# one, the old one is removed and the old directory can go.
#
# tests/test_stub_remove.py#test_the_dispatcher_carries_the_message runs the
# dispatcher with HOME under tmp_path (monkeypatch.setenv("HOME", ...)
# before the subprocess), so no case reaches the machine's own ~/.claude/.
# Precondition: os.rename within ~/.claude/, one filesystem, as today.
```

answer:

### 3. The bootstrap reads a root an earlier release wrote as the project's own, and puts a second root under the git directory

severity: must
location: `skills/implement/orchestration.md:116-127`, `docs/one-root-by-lifetime.md:65-68`, `skills/config/SKILL.md:26-28`, `hooks/root-migrate.py:72-75`
evidence: read `skills/implement/orchestration.md:116-127`, `templates/claude-md-block.md:16`, `hooks/root-migrate.py:248-253`, `docs/one-root-by-lifetime.md:65-68`
verdict: open

Two readers decide whether a `seal/` is the plugin's, and they disagree. `hooks/root-migrate.py#ours` (`:248-253`) accepts the marker or one of the two headings an earlier release wrote (`OLD_HEADINGS`, `:72-75`). The bootstrap (`skills/implement/orchestration.md:116-127`) and the policy (`docs/one-root-by-lifetime.md:65-68`) say that any `<repo>/seal/` whose README does not open with the marker is the project's own: write nothing into it and put the root under the git directory. `templates/claude-md-block.md:16` sends a session to that bootstrap whenever no marked root stands.

A session meets an unmarked plugin root in two states. One is a move refused over work in progress: the probe left an uncommitted round record under `seal/specs/1-a/`. The hook printed "the old layout under seal/specs/ holds uncommitted changes" and `home_at` answered "". The other is the branch of finding 1. In both, the bootstrap follows its text and creates `.git/seal/` in local mode. Once the person commits and the move marks `<repo>/seal/`, both roots are marked. `seal import` and `seal mode` then refuse (`skills/implement/scripts/seal.py:1036`, `:2425`), and `home_at` reads the shared root first, so what the session wrote under `.git/seal/` goes unread. `gaps.md:15` records the departure for the migration and does not carry it to the bootstrap.

```markdown
<!-- skills/implement/orchestration.md, before the paragraph "A `<repo>/seal/`
whose `README.md` does not open with the marker is the project's own." -->
**A `<repo>/seal/` whose `README.md` opens with a heading an earlier release
of the plugin wrote is the plugin's root, waiting for its move.** The headings
are `hooks/root-migrate.py#OLD_HEADINGS`. The session-start move rewrites the
README and moves the work items. Where it was refused, its line says why. The
orchestrator creates no root and asks nothing. It tells the person in one
line, *"`<repo>/seal/` is this plugin's root from before the rename: commit
the work in progress under it and start a new session, and the move runs"*,
and stops.

<!-- The next paragraph, and docs/one-root-by-lifetime.md:65 and
skills/config/SKILL.md:28, then read "whose `README.md` opens with neither the
marker nor one of those headings". -->
```

answer:

### 4. A hygiene workflow pinned before the rename passes every pull request after the move, having examined nothing, and no upgrade text says so

severity: must
location: `README.md:311-330`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/changelog.md:6`, `hooks/root-migrate.py:531-535`
evidence: executed `git show v0.22.4:skills/code-review/scripts/chain_check.py`, `git show v0.22.4:hooks/optin.py`
verdict: open

A repository that ran `seal pr-checks install` before the rename holds `.github/workflows/hygiene.yml`, which clones the plugin at the release it was pinned to (`templates/hygiene.yml:55`, `--branch v<version>`) and runs that release's `chain_check.py`. At `v0.22.4` that reader takes declarations from `seal/specs/` (`hooks/optin.py:41`, `WORK_ITEMS = "specs"`) and the trailer key `SpecSeal-Routing` (`chain_check.py:2054`). After the move commits `seal/threads/`, it finds no declaration for the branch and prints "examined nothing", and `return 1 if problems and strict else 0` at `:2234` passes. New commits carry `Seal-Routing:`, which it does not read, so no trailer problem arises either. The pull-request check goes off without a word.

`frame/plan.md` *Operational impact* says "A workflow this plugin wrote under the old slug is rewritten by `seal pr-checks install`". No text a user reads carries that step: not README.md *Coming from `specseal@specseal`* (`:311-330`), not the changelog fragment (`changelog.md:6`), and not the move's notice (`hooks/root-migrate.py:531-535`).

```markdown
<!-- README.md, at the end of *Coming from `specseal@specseal`*, and its
twin in README.ko.md -->
Where `.github/workflows/hygiene.yml` is the workflow an earlier release
wrote, run `seal pr-checks install` and commit the result with the
session-start move. That workflow clones the release it was pinned to, and
that release reads work items under the old directory and the old trailer,
so after the move it finds no declaration and passes every pull request
having examined nothing.

<!-- changelog.md, a Compatibility bullet under ### Changed -->
- **Compatibility (#1051).** A `.github/workflows/hygiene.yml` written by a
  release before the rename checks nothing once the move is committed, and
  passes. `seal pr-checks install` rewrites it pinned to this release.
```

```python
# hooks/root-migrate.py#moved_line, where `seal.py#workflow_at` reads
# `plugin` and `pinned()` names a release other than the running one: the
# tail gains " — and run `seal pr-checks install`, since the workflow
# pinned to an earlier release examines nothing after this move".
```

answer:

### 5. A work item in flight whose `routing.md` answers `smith` loses the implementer notice after the move

severity: should
location: `hooks/routing.py:72-74`, `hooks/routing.py:251`, `hooks/implementer-notice.py:56-61`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/gaps.md:20`
evidence: read `hooks/routing.py:72-74`, `hooks/routing.py:251-270`, `hooks/implementer-notice.py:56-61`
verdict: open

`gaps.md:20` says a declaration that still answers `smith` reads as unanswered, and that this is fine because "the row was always optional and decides nothing (`hooks/routing.py#parse`)". The row decides one thing. `hooks/implementer-notice.py:56-61` prints its line only where `implementation` equals `routing.BY_CRAFTER`, and `parse` turns `smith` into None (`hooks/routing.py:270`). The move copies each `routing.md` byte for byte, so every 0.22.x work item in flight that was routed to `smith` loses the notice at its next commit. `frame/design.md` *Scope* says "No gate, check or agent's job changes". The trailer got a reading of its old spelling for one minor release for the same kind of reason. This answer is a value a committed file carries, and it has none.

```python
# hooks/routing.py
BY_CRAFTER = "crafter"
# exempt from old_names: the answer a declaration written before the rename carries; the next minor release removes this reading
OLD_BY_CRAFTER = "smith"

# hooks/routing.py#parse, after `implementation = found.get(IMPLEMENTATION)`
    if implementation == OLD_BY_CRAFTER:
        implementation = BY_CRAFTER
```

answer:

### 6. The settle orders every moved thread by the move's one commit instead of by its own merge

severity: should
location: `skills/settle/scripts/rule_changes.py:270-296`, `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/gaps.md:40`
evidence: read `skills/settle/scripts/rule_changes.py:270-296`
verdict: open

`order` takes each thread's place from the first commit that adds `seal/threads/<id>/frame/design.md`, with `--no-renames --diff-filter=A` (`:277-281`). The move adds that file for every 0.22.x thread in one commit, so every moved thread gets the same commit. Their order is then the path order of that commit's listing, which is the order of their ids, not the order their pull requests merged. The settle writes each section as its group's latest decision in this order. In a user's repository where two released but unsettled work items changed one section and merged out of id order, it writes the older decision as the latest.

`gaps.md:40` lists this under *Not verified* and leaves it to the session that runs the 0.23.0 settle. That home covers this repository only. Every user repository the move reaches holds the same history, and no session there knows to read the order by hand. The reader can take each thread's first add at either layout, since the old path is history git still holds.

```python
# skills/settle/scripts/rule_changes.py
# Where a thread's design stood before the session-start move brought it into
# `seal/threads/`: read for history only, so a moved thread counts as added
# where its `spec.md` was first added and not at the move's one commit.
# exempt from old_names: the 0.22.x path, read from history
EARLIER = ("seal/specs", "spec.md")


def order(root, ref, ids, specs="seal/threads"):
    r = subprocess.run(
        [
            "git", "-C", root, "log", "--full-history", "--topo-order",
            "--reverse", "--no-renames", "--diff-filter=A", "--name-only",
            "--format=%x00%H",
            ref, "--", specs, EARLIER[0],
        ],
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )  # fmt: skip
    first, commit = {}, None
    # exempt from splitlines: git output
    for line in r.stdout.splitlines():
        if line.startswith("\0"):
            commit = line[1:]
            continue
        for base, name in ((specs, DESIGN), EARLIER):
            parts = line[len(base) + 1 :].split("/", 1)
            if line.startswith(base + "/") and len(parts) == 2 and parts[1] == name:
                first.setdefault(parts[0], commit)
    known = [i for i in first if i in ids]
    return [(i, first[i]) for i in known] + [(i, None) for i in ids if i not in first]
```

answer:

### 7. Citations of released work items were rewritten to thread paths that no commit has ever held

severity: should
location: `seal/follow-up.md:43`, `seal/follow-up.md:47`, `skills/writing-style/SKILL.md:285`, `skills/verify/scripts/unverified_check.py:7`, `hooks/cmdline_base.py:12`, `.github/workflows/test.yml:85`, `.github/workflows/test.yml:91`, `.github/workflows/test.yml:137`, `tests/block_shapes.py:1`, `tests/config_shapes.py:1`, `tests/test_a_section_marked_for_one_role_reaches_only_that_role.py:33`, `tests/test_chain_hooks_hardening.py:445`, `tests/test_chain_hooks_hardening.py:540`, `tests/test_chain_hooks_hardening.py:634`, `tests/test_chain_hooks_hardening.py:771`, `tests/test_every_reader_ends_a_line_where_gfm_does.py:14`, `tests/test_first_setup_asks_once.py:4`, `tests/test_mode_gate.py:7`, `tests/test_no_passage_is_pasted_into_a_second_file.py:36`, `tests/test_routing.py:73`, `tests/test_the_hook_surface_git_offers.py:7`, `tests/test_the_hooks_hide_what_a_renderer_hides.py:3`, `tests/test_the_installer_writes_the_block_from_its_template.py:12`, `tests/test_the_rules_claude_md_names_have_one_home.py:26`, `tests/censuses.py`
evidence: executed `git log --all --oneline -1 -- seal/specs/1791270165-the-windows-test-leg-is-measured-and-cut/phases/phase-3.md`, `git log --all --oneline -1 -- seal/threads/1791270165-the-windows-test-leg-is-measured-and-cut/trail/phases/phase-3.md`, `git grep -nE 'seal/threads/1[0-9]{9}-' -- ':!seal/threads' ':!changelog' ':!CHANGELOG.md' ':!evals'`
verdict: open

A path like `seal/specs/1791270165-the-windows-test-leg-is-measured-and-cut/phases/phase-3.md` is a coordinate into git history. The work item was settled and its directory removed, so a reader opens the record with `git log -- <path>` and then `git show`. The sweep rewrote these coordinates to the thread layout. The old path answers `5f11923f`, and the new path answers nothing in any commit. The grep above lists the class: outside `evals/` and the fixtures (`1790000000`, `1790000012`, `1788000000`, `17999…`, `17000…`), the listed lines cite released work items at paths that never existed. Two are text a person acts on now. `seal/follow-up.md:43` tells the owner that "the measurement and the draft are in" a round record, and `:47` points at a `frame/questions.md`. `skills/writing-style/SKILL.md:285` is text every agent reads. `frame/design.md` *Scope* lists the readers of a live work item path and is silent on a citation of a removed one. `tests/censuses.py#old_names` refuses `seal/specs/` everywhere outside its exemptions, which is what pushed the rewrite.

```text
1. Restore each listed coordinate to its spelling at the commit that held
   it: `seal/specs/<id>/<name>`, with `spec.md`, `plan.md`, `phases/`,
   `rounds/`, `overview.md` and `broad-gate.md` as they were. `git grep`
   over the command on the evidence line enumerates them, and
   `git log --all -1 -- <old path>` confirms each one resolves.
2. tests/censuses.py#old_names passes a `seal/specs/<unix-seconds>-<slug>/`
   path whose id has no directory under `seal/threads/`. The comment above
   the rule says why: such a path is a coordinate into git history, which
   the move does not rewrite. Its case pins one coordinate passing and one
   bare `seal/specs/` refused.
```

answer:

## Confirmations

confirms: none
The trailer holds as the frame states. `skills/code-review/scripts/chain_check.py:2061-2065` names `Seal-Routing` and `OLD_TRAILER = "SpecSeal-Routing"`, and `routing_trailers` (`:2084-2120`) passes both keys to git's own trailer parser in one `%(trailers:key=...,key=...)` format, with the author-equals-committer rule unchanged. The CLAUDE.md block (`templates/claude-md-block.md:16`) and `skills/commit-pr-convention/SKILL.md:140` write the new key. Read.

confirms: none
The marker has one reader and no reader still answers by a directory test. `hooks/optin.py:192-257` answers a root only where `README.md`'s first line, its end stripped, equals `MARKER`, and every `home_paths` caller outside `optin` (`skills/verify/scripts/broad_gate.py:638-640`, `skills/implement/scripts/seal.py:1036`, `:1990`, `:2425`, `skills/code-review/scripts/chain_check.py:1986`, `hooks/mode-gate.py:219`) either joins `marked` or reads a root `home_at` already answered. `hooks/gate.py:16` classifies diff paths by the string `seal/` and decides only the parity arm, whose config is read at the shared root. Executed `git grep -n 'home_paths\|optin.HOME\|optin\.marked\|marked('`, then read each hit.

confirms: none
The command line dispatches every tool. Each of the thirteen `skills/implement/scripts/seal.py#TOOLS` entries names a script that exists, executed by a parse of `TOOLS` and a file test of each path. `main` (`:2822-2823`) hands a tool's arguments on before argparse sees them, so `--help` reaches the script. `hand_over` (`:2800-2814`) replaces the process on POSIX and returns `subprocess.call`'s code on Windows, which `sys.exit(main())` carries out through `hooks/launch.py`. `bin/seal.cmd` passes `%*` and ends with `exit /b %errorlevel%` on both interpreters. `ls bin/` lists the four files the frame names. Read, and the Windows run is a row of `## Not judged`.

confirms: none
The plugin identity matches #1051's mapping as `frame/design.md` *The names* states it. `.claude-plugin/plugin.json` holds `name` `agentic` and `displayName` `AgenticSeal`, and `.claude-plugin/marketplace.json` holds `name` `agenticseal`, the plugin entry `agentic`, `renames` `{"specseal": "agentic"}` and the one sentence in both descriptions. Read.

confirms: none
The shared and local moves of a 0.22.x root, the README rewrite, a stopped move's resume and the old-block replacement in `install.sh` hold as pinned. Executed `bin/test tests/test_root_migrate.py tests/test_optin.py tests/test_seal.py -q`: 521 passed. Read `install.sh:77-101`: the old markers are matched only where the new ones are absent, and the damaged-block refusal reads the found end marker.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `bin/seal.cmd` and the `os.name == "nt"` branch of `hand_over` running a subcommand and returning its exit code | `bin/seal.cmd`, `skills/implement/scripts/seal.py:2800-2814` | the orchestrator, reading the Windows shards of `.github/workflows/test.yml` on the pull request |
| whether the three upgrade lines carry a `specseal@specseal` install to `agentic@agenticseal`, and what `renames` does under a marketplace whose own `name` changed | `README.md:311-330`, `.claude-plugin/marketplace.json` | the owner, on a machine installed at 0.22.4 after the release (`frame/questions.md` Q4) |
| whether each exemption in `tests/censuses.py#old_names` is justified; the spawn prompt put spellings out of this round | `tests/censuses.py` | the next round |
| Q2, Q3 and Q4 of `frame/questions.md` stand `open`, and the build ran on each default | `seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/frame/questions.md` | the owner |
| the full suite, the repository-wide lint and the typecheck over this branch | the branch | the orchestrator's broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test <scratch>/probe/test_tmp_round1_probe.py -s -q -p no:xdist`, three cases over fixture repositories with `HOME` state patched to the case directory | 3 passed, with printed results. Second branch: the first start moved `1-a`; on `feat/b` the start printed nothing and `home_at` was empty; after merging `main`, `home_at` found the root, `seal/specs/2-b/routing.md` stood, and `declarations` listed only `seal/threads/1-a/routing.md`. Moved clone: nothing printed, `.git/specseal-scratch` stayed, `.git/agentic-scratch` absent, `home_at` non-empty, the old `pact-paths.md` not moved. Uncommitted round record: the move refused, `home_at` empty. The probe file was deleted after the run |
| `bin/test tests/test_root_migrate.py tests/test_optin.py tests/test_seal.py -q` | 521 passed; the `~/.claude/agentic/` directory the run created was removed |
