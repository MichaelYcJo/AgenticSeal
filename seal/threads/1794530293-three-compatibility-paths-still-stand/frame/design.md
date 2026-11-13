# Design: 1794530293-three-compatibility-paths-still-stand

## Grounding

The tree as read at `dda87704c`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*; `seal/config.json` has no `Policy root` key (executed: `cat seal/config.json`), so the policy root is `docs/` | This work's subject is the code: it takes three compatibility paths out of `lib/`, the scripts, the update skill and their tests. The sentences of `docs/` that state those paths change through `## Rule changes`, for the settle, and are not edited here. `README.md`, `README.ko.md`, `skills/` and `templates/` are outside the policy root and are edited directly |
| G2. The unsettled designs' `## Rule changes` (executed: an `awk` over every `seal/threads/*/frame/design.md` listing each operation's `file` and `section`, then each `from` read where a section matches). Three unsettled items change a section this work changes: `1794289597-pr-md-copies-the-changelog-below-the-fold` (*What the repository decides for itself, and how it is read*, both editions), `1794390764-scripts-load-a-reader-from-its-sibling` (*The fold, and what tells it from a deletion*), `1794383426-eval-code-the-verdict-does-not-read` (*What the check reads at the pull request*) | Each of the three quotes a different sentence from the one this work removes, so the policy in force at each sentence below is `docs/` as read. No unsettled design touches `docs/checks/the-stamp.md` *The stamp* |
| G3. Issue #1500, body as folded on 2026-11-13, and the owner's comment of 2026-11-12T23:57:45Z (executed: `gh issue view 1500 --json body,comments`) | The three paths leave together in this release. The *Done when* items stand: no path stands in the tree; the README *Updating* sections name none; `templates/setup/claude-md-block.md` and `READ_BY_AN_EARLIER_RELEASE` go together; the release note's *Updating* line says what a person still on 0.36.x or earlier does instead. The issue's third column is a sample, and `## Removes` lists the class whole (contract rule 12) |
| G4. How the class was listed (contract rule 12). Built from what each path does, not from the issue's names. (a) The file names each path reads or writes, as literals and as the constants holding them: `config.md` (`lib/config.py#OLD_CONFIG`), `parity.md` (`lib/optin.py#OLD_PARITY_CONFIG`), the old table header (`lib/config.py#OLD_TABLE`), and every user of each constant (executed: `git grep -n -E 'OLD_CONFIG\|old_config_path\|unconverted_config\|unconverted_parity\|PARITY_KEYS\|OLD_TABLE\|OLD_PARITY_CONFIG'`). (b) The strings each update step matches: `<!-- agentic:start -->`, `${CLAUDE_PLUGIN_DATA}/stamp.py`, `4b` (executed: `git grep` on each, and on `launcher`, `preset block`, `claude-md-block`). (c) Every test function whose body names any of (a) or (b), listed by an `ast` walk of every tracked `tests/*.py` (executed: `test_tmp_list_cases.py` in the scratch directory, 57 hits read one by one, the false hits on `seal_stamp.py`, `lib/launch.py` and `templates/setup/config.md` set aside). (d) Prose: `git grep` over the tree outside `seal/threads/` for `config.md`, `parity.md`, `seal mode`, `earlier release`, `convert`, `launcher`, `2027`, `90 days` | `## Removes` holds what (a) to (d) found. The part no method makes whole is prose restating a path in other words; that part stays a sample, and the proofer reads it |
| G5. `lib/config.py#config_pairs` refuses a root holding `config.md` and no `config.json` (read, `:139-141`), and every command that reads a setting reads through it: `seal gate` (`skills/verify/scripts/broad_gate.py#broad_command`, read `:648-662`), `seal fold`, `seal pact`, `seal pr-body`, `seal mode` (read: their cases, `## Removes` R16, R19 and R20) | Taking the arm out of `config_pairs` takes the `config.md` refusal out of every command at once. No command carries a refusal of its own beside it |
| G6. A probe over a root holding only an earlier release's `seal/config.md`, in a `git clone --no-local` under the scratch directory with the `config_pairs` arm taken out (executed: `test_tmp_old_root.sh`). Before: `seal mode --check` prints `key: refused` and the "run `seal mode` once" sentence, exit 2. After: `seal mode --check` prints `key: not declared`, exit 0; `seal gate --base HEAD` exits 2 with "`seal/config.json` has no `Broad gate` key, so there is no command to run", and nothing ran | After the removal an old `config.md` is a file nothing reads. A person who updates from 0.36.x or earlier meets the missing keys one command at a time, and no command names `config.md`. The release note's *Updating* line is the one place that tells them to write `config.json` by hand |
| G7. `skills/code-review/scripts/chain_check.py#originals_of` refuses a `parity.md` git carries with no `parity.json` beside it (read, `:1626-1660`); `seal mode` prints a note for the same file (read, `skills/implement/scripts/seal.py:2183-2187`) | After the removal a `parity.md` alone is no migration config: the parity arm reads nothing and refuses nothing. The release note's *Updating* line tells a migration repository to write `seal/parity.json` |
| G8. `skills/implement/scripts/seal.py` loads `lib/tables.py`, and `lib/blocks.py` before it, for the converter alone: `tables.` is called once, at `#converted` (executed: `grep -n 'tables\.' skills/implement/scripts/seal.py`) | The two loads leave with the converter, and so does `tests/skills/test_seal.py#Test_module`'s case for a `lib/` without `blocks.py`. `lib/tables.py` keeps its other callers: `pact_check.py`, `settle.py`, `rule_changes.py`, `.github/scripts/rules.py` (read, its docstring) |
| G9. The walker's two-cell pass in `tests/lib/test_tables.py` walks `HEADERS["config"]`, the `| Item | Value |` header, and `test_the_config_pass_is_the_config_readers_header` holds it to `lib/config.py#OLD_TABLE` on the premise that "a pass over a header no reader uses would hold nothing" (read, `:107-115`, `:1309-1314`). The walker's other callers hand it three- and four-cell headers: `pact_check.py#ANCHOR_TABLE`, `settle.py#JUDGMENTS_HEADER` (read). The corpus is built from the header's width alone (read, `#corpus`, `#document`, `#plain`) | The two-cell pass and the `_Old_config_table` and `_Old_config_shapes` cases stay as the walker's multi-cell cases, on a header literal the test file holds. The pin to `OLD_TABLE` goes with the constant. `frame/plan.md` A5 weighs this against the alternatives |
| G10. `skills/update/SKILL.md` *4. Take out the preset block.* (read, `:137-213`) and *4b. The launcher an earlier release wrote.* (read, `:215-233`); step 2 sends an already-current update to step 4b (read, `:39-43`); *What this does not do* holds a paragraph on the preset block (read, `:275-278`). The tests that cut the skill by step number read `**3.` to `**4.` and `**4b.` to `**5.` (read, `tests/behaviour/test_update_reads_the_config_directory_in_use.py#step`, `:150`, `:169`) | Both steps leave, step 5 becomes step 4, and step 3's "go on to step 4" then names it. The case that cuts step 3 at `**4.` keeps working |
| G11. `tests/behaviour/test_a_cited_section_stands_in_its_file.py#excuser`: a dangling citation in a `docs/` file is excused while an unsettled `## Rule changes` item's `from` holds it whole and its `to` does not (read, `:225-235`) | `docs/checks/the-stamp.md` cites `skills/update/SKILL.md` *4b. The launcher an earlier release wrote*. The `remove` item below quotes that citation in its `from`, so the citation is excused until the settle writes the section |
| G12. The date. `git grep -n -E '2027\|90 days'` finds 2027-02-07 in no file outside `seal/threads/`; no README sentence gives it (executed). In the tree it stands in #1492's work item: `changelog.md:6`, the *Updating* line, and that item's frame, round, guarantee and `pr.md` records (executed). Outside the tree it stands in the published v0.37.1 note, twice (executed: `gh release view v0.37.1 --json body`, lines 21 and 80); no later note names it (executed, v0.37.2 to v0.38.0) | The text that gives the date and that this work changes is #1492's `changelog.md` *Updating* line (*Scope* item 11). The owner's comment names README sentences too, and none exists. The records of #1492's judgment keep what they said. The published v0.37.1 note is outside the tree; `frame/questions.md` names the assumption |
| G13. `.github/scripts/publish_release_note.py#fragments` reads only fragments the range adds (`--diff-filter=A`) and that the previous tag does not hold (read, `:224-275`) | An edit to #1492's fragment reaches no release note. The 0.38.1 note is built from this work item's own `changelog.md` |
| G14. `docs/releasing/branch-and-release.md` *Work accumulates on a release branch*: the first pull request into `release/vX.Y.Z` moves the version, in the commit that adds its fragment, by the last phase's crafter (read, `:30-45`). The version stands in `.claude-plugin/plugin.json:4` alone (executed: `git grep -n -F 0.38.0` outside `seal/threads/`; `.claude-plugin/marketplace.json` holds no version, read) | *Scope* item 12 moves `.claude-plugin/plugin.json`'s `version` to `0.38.1` in the phase 2 commit that adds `changelog.md` |
| G15. `tests/behaviour/test_release_hygiene.py#test_no_loaded_file_names_a_version_at_or_above_the_running_one` refuses a shipped file naming the running version or above; `seal/threads/` is outside its set (read, `:586-614`) | No README, skill, template or `docs/` text this work writes names 0.38.1. The fragment may |
| G16. `docs/layout/the-record-layout.md` *A change to the way of working writes its process row in its own fragment* names the files whose change owes a `### Process changes` table (read, `:51-60`) | This work changes none of them (`skills/update/SKILL.md`, `skills/config/SKILL.md` and `skills/parity-setup/SKILL.md` are not on the list), so its fragment carries no such table |
| G17. `seal/follow-up.md` holds no row (read). The one `RIDER:` in a file this work changes, `skills/implement/scripts/seal.py:1720`, asks for a change "when this function is next opened", and this work does not open `#other_worktrees` (executed: `git grep -n 'RIDER:'`, read) | Nothing waits on this work |
| G18. This design's `## Rule changes`, parsed by `skills/settle/scripts/rule_changes.py#parse` from the scratch clone, refuses no line and reads five operations, and each `from`, whitespace collapsed, stands in its file (executed) | The settle can place every operation, and each `from` quotes the text as read at `dda87704c` |
| G19. `routing.md` (read): `Planning \| framer`, `Implementation \| crafter`, `Review \| through the review chain` | The frame's mark names `framer` |

## Scope

**In.** Twelve items, built in the two phases of `frame/plan.md`.

1. **`lib/config.py` reads no `config.md`.** `#config_pairs` loses its
   `config.md` arm, so a root holding `config.md` and no `config.json`
   declares nothing, as a root holding no file does. `#OLD_CONFIG`,
   `#OLD_TABLE`, `#old_config_path` and `#unconverted_config` go, and the
   docstrings and comments that state the refusal are rewritten to the
   reader as it stands.
2. **`seal mode` converts nothing and names no old file.**
   `skills/implement/scripts/seal.py#converted` and `#convert` go, with
   `#mode_report`'s three branches over `config.md` and `parity.md` and the
   paragraphs of its docstring that state them, the aliases `OLD_CONFIG`
   and `old_config_path`, the loads of `lib/blocks.py` and `lib/tables.py`
   (G8), the clause of `#mode_refusal`'s docstring naming `config.md`, the
   comment above the aliases, and the help line "first converts an earlier
   release's seal/config.md into seal/config.json".
3. **No check refuses a `parity.md`.** `chain_check.py#originals_of` loses
   its `parity.md` branch and the docstring sentence for it, and the module
   docstring's `original` arm loses its clause.
   `lib/optin.py#OLD_PARITY_CONFIG` goes, with the comment on
   `#PARITY_CONFIG` that names it. `lib/config.py#unconverted_parity` and
   `#PARITY_KEYS` go, with their comment.
4. **The comments that name the converter are rewritten.**
   `broad_gate.py#broad_command`'s docstring clause on `config.md`;
   `lib/tables.py`'s module docstring sentence on `seal mode`'s converter,
   its comment above the walker naming `config.md`, the `gfm_table`
   docstring's "an old `config.md`", and the two comments naming `seal.py`
   as a caller; `lib/blocks.py`'s module docstring clause on `config.md`.
5. **The shipped prose of path 3 goes.** `skills/config/SKILL.md`'s
   paragraph **A `config.md` standing in the root without a
   `config.json`**; `templates/setup/config.md`'s paragraph **An earlier
   release's `config.md` is converted once, by `seal mode`.**, with the two
   sentences on both files standing; `skills/parity-setup/SKILL.md` step 1's
   sentence on an earlier release's `seal/parity.md`.
6. **The tests of path 3 change as `## Removes` lists them.** One case is
   rewritten, not removed: `tests/lib/test_config.py`'s S3 case,
   `test_refuses_a_config_md_standing_alone_and_names_seal_mode`, becomes a
   case that a root holding `config.md` and no `config.json` reads as
   `(None, None)` and `declared_mode` answers `none`. It pins what a person
   now sees (contract rule 14) and is seen red against the reader before
   item 1 (contract rule 15). The walker's two-cell cases in
   `tests/lib/test_tables.py` stay on a header literal the file holds, and
   their docstrings and comments stop naming the converter (G9).
7. **`/agentic:update` takes nothing out and reads no launcher.**
   `skills/update/SKILL.md` steps 4 and 4b go. Step 2's paragraph for an
   update that is already current ends at "say so and stop", with its
   reason that nothing arrived. *What this does not do* loses the paragraph
   **It does not delete anything the user wrote.** Step 5 becomes step 4.
8. **The block's template leaves with its exemption.**
   `templates/setup/claude-md-block.md` and
   `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#READ_BY_AN_EARLIER_RELEASE`
   go in the same commit. `tests/behaviour/test_the_old_block_leaves_through_update.py`
   goes; its two cases on this repository's `CLAUDE.md` importing nothing,
   `test_this_repository_imports_no_core_and_names_the_tree_copy` and
   `test_an_import_line_is_told_from_a_code_span`, with the `IMPORT`
   pattern they read, move to
   `tests/text/test_the_rules_claude_md_names_have_one_home.py`.
9. **The launcher's pins go.** The cases and asserts `## Removes` lists in
   `tests/behaviour/test_update_reads_the_config_directory_in_use.py` and
   `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`.
10. **The READMEs name no path.** `README.md` *Updating*: the paragraph
    opening "An update from an earlier release can leave work behind." goes
    whole, its sentences on the pact's `| Signer |` table and
    `pact-paths.md` with it (`frame/plan.md` A6). `README.md` *What runs on
    your machine*: the sentence from "A release from 0.33.0 to 0.34.1 may
    have left a launcher" to its citation goes. `README.ko.md` *업데이트*
    and *내 컴퓨터에서 도는 것*: the same two passages. Both editions keep
    the same heading outline.
11. **#1492's *Updating* line no longer gives 2027-02-07.** In
    `seal/threads/1794271937-the-readme-narrates-three-migrations/changelog.md`,
    the line opening "Updating: nothing to do for this release itself."
    keeps its first sentence. The sentence that gives the date and the one
    after it become one sentence saying that the three paths left in 0.38.1
    (#1500). Nothing else of that work item changes (G12).
12. **This work item's `changelog.md` and the version move.** A `### Removed`
    section with one entry per path, then the line `- The version moves to
    0.38.1.`, then an *Updating* line. The *Updating* line says that a
    person on 0.37.0 or later has nothing to do, and that a person on 0.36.x
    or earlier does by hand what the removed paths did, each as one clause:
    write `seal/config.json` from `templates/setup/config.md` with the rows
    of `seal/config.md` as its keys and delete `seal/config.md`, since no
    command reads that file and every key reads as absent until then (G6);
    write `seal/parity.json` from `templates/setup/parity.json` where
    `seal/parity.md` stands and delete it, since the parity arm reads no
    `parity.md` (G7); move a `seal/pact.md`'s `| Signer |` table into a
    `Pact signers` key, and `~/.claude/agentic/pact-paths.md` into
    `~/.claude/agentic/pact-paths.json`; delete the lines between
    `<!-- agentic:start -->` and `<!-- agentic:end -->` in
    `~/.claude/CLAUDE.md`, the markers included, which a release from
    0.23.0 to 0.24.2 wrote; remove from
    `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json` the `Stop` entry
    whose command runs `${CLAUDE_PLUGIN_DATA}/stamp.py`, then that file,
    which a release from 0.33.0 to 0.34.1 wrote. `.claude-plugin/plugin.json`'s
    `version` moves from `0.38.0` to `0.38.1` in the commit that adds the
    file (G14).

The rules of `docs/` these paths stated change through `## Rule changes`,
which the settle writes (G1). No phase edits `docs/`.

**Out.**

- The note that a values file in a per-session directory under
  `<git-common-dir>/agentic-stamp/` is neither drawn nor counted
  (`docs/checks/the-stamp.md` *The stamp*, `skills/verify/scripts/seal_stamp.py#already_queued`).
  It is a reading the stamp declines, not one of the three paths the issue
  names.
- The records layout before 0.23.0 that `evals/scripts/replay_targets.py#LAYOUTS`
  reads. It is no update path, and `1794383426-eval-code-the-verdict-does-not-read`
  changes its sentence in `docs/checks/the-pull-request-check.md` (G2).
- Docstrings that recount the block's retirement as history:
  `tests/behaviour/test_first_setup_asks_once.py:614-626`,
  `tests/text/test_the_rules_claude_md_names_have_one_home.py:24-30` and
  `:70-73`, `tests/text/test_broad_gate_rule.py:5`. They state no path, and
  `1794406505-docstrings-recount-their-history` is that class's work item.
- `templates/setup/config.md` **A `Pact notify` key is read by nobody.** and
  `lib/config.py:512`. A key nothing reads is no update path.
- The parametrize ids "an earlier release's table" in
  `tests/lib/test_config.py#Test_baseline_commit` and
  `tests/skills/test_pact_check.py`. Each labels a markdown table handed to
  a JSON parser, which still refuses it.
- The records of #1492's judgment beside its `changelog.md`, and the
  published v0.37.1 release note (G12).
- `docs/experiments/2026-11-06-what-draws-the-stamp-without-a-plugin-hook.md`,
  a dated record that keeps what it measured.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. An old settings table is no file | Given a root holding `seal/config.md` and no `seal/config.json`, when any command reads a setting, then `lib/config.py#config_pairs` answers `(None, None)` and no output names `config.md` or `seal mode` as a converter | the rewritten S3 case of `tests/lib/test_config.py`, seen red before *Scope* item 1; `git grep -n 'config\.md'` outside `templates/setup/config.md` and `seal/threads/` finds no code that opens the file |
| S2. `seal mode` writes from the folder only | Given that root, when bare `seal mode` runs, then it writes a `Mode` key from the folder into a new `config.json`, prints no conversion and no note, and leaves `config.md` as it was | `tests/skills/test_seal.py#Test_mode_report`'s cases for an absent key; the proofer reads `#mode_report` |
| S3. An old migration config is no declaration | Given a pull request whose HEAD carries `seal/parity.md` and no `seal/parity.json`, when `chain-check` runs, then the parity arm reads no migration config and refuses nothing for it | `tests/skills/test_chain_check.py#Test_originals_of`'s case for no config; the proofer reads `#originals_of` |
| S4. The update takes nothing out | Given `/agentic:update`, when a session follows `skills/update/SKILL.md`, then its steps are 1, 2, 2b, 3 and 4, none opens a `CLAUDE.md` or reads `${CLAUDE_PLUGIN_DATA}`, and an already-current update stops at step 2 | `tests/behaviour/test_update_reads_the_config_directory_in_use.py`; `git grep -n -E 'agentic:start\|CLAUDE_PLUGIN_DATA\|4b' skills/update` finds nothing |
| S5. The template and its exemption leave together | Given the tree after phase 2, when `test_every_template_is_named_by_a_document_that_ships` runs, then it exempts no template and finds every template named | that case; `git ls-files templates/setup/claude-md-block.md` lists nothing |
| S6. The READMEs name no path | Given both editions, when a person reads *Updating* / *업데이트* and *What runs on your machine* / *내 컴퓨터에서 도는 것*, then neither names `seal/config.md`, `seal/parity.md`, the `CLAUDE.md` block or the launcher | `git grep -n -E 'config\.md\|parity\.md\|launcher\|실행기\|4b' README.md README.ko.md` finds only `templates/setup/config.md` if anything; `tests/behaviour/test_both_editions_carry_the_same_folds.py` |
| S7. A person on 0.36.x or earlier is told what to do | Given the 0.38.1 note, when `/agentic:update` step 3 prints it, then its *Updating* line names each by-hand act of *Scope* item 12 | the proofer and the sealer read `changelog.md` against *Scope* item 12 |
| S8. No tree text gives the old date | Given the tree after phase 2, when searched, then 2027-02-07 stands only in #1492's records other than its `changelog.md` | `git grep -n 2027-02-07` |
| S9. The version moves with the fragment | Given the phase 2 commit that adds this work item's `changelog.md`, then `.claude-plugin/plugin.json` reads `0.38.1` at that commit | `git show <commit> -- .claude-plugin/plugin.json` |

## Data & interfaces

- `lib/config.py#config_pairs`'s states become two of three: `(None, None)`
  for no `config.json` or a falsy home, `(pairs, None)`, and
  `(None, refusal)` for a `config.json` that will not read or parse. Its
  callers' signatures do not change.
- `seal mode`'s output loses three lines: "`<old>` was converted: …",
  "note: `<old>` stands beside config.json …" and "note:
  `seal/parity.md` …". Its exit codes do not change for any other state.
- `chain-check`'s parity arm loses one refusal line shape,
  `seal/parity.md:0  is the migration config an earlier release read …`.

## Rule changes

- remove
  file: docs/layout/one-root-by-lifetime.md
  section: What the repository decides for itself, and how it is read
  from: A `config.md` that stands in the root without a `config.json` is
    refused by every reader that refuses a file it cannot read, and read as
    no file by the readers of `Policy root` and `Reference specs`, and
    `seal mode` writes `config.json` from its `| Item | Value |` table and
    removes it.
- remove
  file: docs/layout/one-root-by-lifetime.ko.md
  section: 저장소가 스스로 정하는 것, 그리고 그것을 읽는 방법
  from: `config.json` 없이 루트에 서 있는 `config.md` 는 읽지 못하는 파일을
    거절하는 읽는 쪽이 모두 거절하고 `Policy root` 와 `Reference specs` 를
    읽는 쪽은 파일이 없는 것으로 읽으며, `seal mode` 가 그
    `| Item | Value |` 표에서 `config.json` 을 쓰고 지웁니다.
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `lib/tables.py#hidden_lines`, which hides lines for the table readers
    of a record, a pact and the old `config.md` that `seal mode` converts,
    keeps,
  to: `lib/tables.py#hidden_lines`, which hides lines for the table readers
    of a record and a pact, keeps,
- remove
  file: docs/checks/the-pull-request-check.md
  section: What the check reads at the pull request
  from: A `seal/parity.md` that git carries at HEAD without a
    `seal/parity.json` is refused once, naming the keys to write.
- remove
  file: docs/checks/the-stamp.md
  section: The stamp
  from: Where the launcher `skills/update/SKILL.md` *4b. The launcher an
    earlier release wrote* names still runs beside the plugin's hook, a file
    is drawn once, since drawing claims the file first.

## Removes

The table holds 31 rows, grouped by path and then by kind.

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| R1. The `config.md` arm of the settings reader | `lib/config.py#config_pairs`, `:139-141`, and its docstring's `(None, refusal)` clause and closing sentences on `config.md` | Nothing: the owner judged no person on 0.36.x or earlier needs the path (G3); a root holding the file declares nothing (S1) |
| R2. The old file's name, header and path | `lib/config.py#OLD_CONFIG`, `#OLD_TABLE`, `#old_config_path`, and the module docstring's sentences naming `config.md` (`:36-47`) | Their one reader, the converter, goes (R4) |
| R3. The refusal sentence | `lib/config.py#unconverted_config` | Its one caller is R1 |
| R4. The converter | `skills/implement/scripts/seal.py#converted`, `#convert`, the aliases `OLD_CONFIG` and `old_config_path`, the comment above them (`:1380-1386`), "and `convert`" in `#serialized`'s docstring, and the help line at `:23-24` | The release note's *Updating* line gives the by-hand conversion (*Scope* item 12) |
| R5. `seal mode`'s branches over old files | `skills/implement/scripts/seal.py#mode_report`, `:2183-2202`, its docstring's paragraphs **Bare `seal mode` converts an earlier release's `config.md` first** and **An earlier release's `parity.md` is named, never converted**, the `config.md` clause of its refused-file paragraph, and `#mode_refusal`'s docstring clause | Nothing reads either old file (S2) |
| R6. The walker's loads in `seal mode` | `skills/implement/scripts/seal.py:197-201`, the `lib/blocks.py` and `lib/tables.py` loads and their comment | The converter was their one user (G8) |
| R7. The `parity.md` refusal at the pull request | `skills/code-review/scripts/chain_check.py#originals_of`'s `old` and `unconverted` branch and docstring sentence, and the module docstring's clause at `:61-62` | A `parity.md` alone declares nothing (S3) |
| R8. The old migration config's name | `lib/optin.py#OLD_PARITY_CONFIG`, its comment, and the clause of `#PARITY_CONFIG`'s comment naming it | Its two readers go (R5, R7) |
| R9. The sentence naming the keys to write, and its key list | `lib/config.py#unconverted_parity`, `#PARITY_KEYS` and the comment above them | `templates/setup/parity.json` holds the keys; the release note points there |
| R10. Comments naming the converter or the refusal | `skills/verify/scripts/broad_gate.py#broad_command`'s docstring clause (`:652-654`); `lib/tables.py`'s module docstring sentence (`:11-13`), the comment at `:233-235`, `#gfm_table`'s "an old `config.md`" (`:464`), and the comments naming `seal.py` (`:27`, `:36`); `lib/blocks.py`'s docstring clause (`:5-6`) | Rewritten to the callers that stand |
| R11. The config skill's paragraph | `skills/config/SKILL.md`, the paragraph **A `config.md` standing in the root without a `config.json`** (`:32-35`) | Nothing for the skill to say: the file is not read |
| R12. The template's conversion paragraph | `templates/setup/config.md`, the paragraph **An earlier release's `config.md` is converted once, by `seal mode`.** with its two sentences on both files standing (`:55-65`) | Release note (*Scope* item 12) |
| R13. The parity setup's sentence on `parity.md` | `skills/parity-setup/SKILL.md` step 1, `:25-26` | Release note (*Scope* item 12) |
| R14. The converter's shapes | `tests/config_shapes.py`, whole | Its one reader, `tests/skills/test_seal.py#Test_converted`, goes (R16) |
| R15. The old-config writer and its comments | `tests/conftest.py#write_old_config`; the comments at `:884-885` and `:894-898` say the texts are the converter's | The rewritten S3 case writes its file itself. The texts stay as the walker's cases' inputs, their comments rewritten |
| R16. `seal mode`'s converter and old-file cases | `tests/skills/test_seal.py#Test_converted`; `#Test_mode_report`'s `test_converts_an_earlier_releases_config_md_and_removes_it`, `test_refuses_to_convert_a_table_it_cannot_read_whole`, `test_check_refuses_an_unconverted_config_and_names_seal_mode`, `test_reads_config_json_and_names_a_config_md_beside_it`, `test_names_a_parity_md_standing_without_a_parity_json_and_its_keys`; the "a config.md standing alone" shape of `test_refuses_a_file_it_cannot_write_the_key_into_and_leaves_it`; `#Test_module.test_a_lib_without_the_table_walks_reader_exits_2_in_one_sentence`; the imports of `config_shapes` and `PIPED_TABLE`, and `HEAD` and `TWO_MODE_ROWS` where nothing else reads them; the module docstring's sentence on the converter (`:28-29`) | Each holds a unit R4 to R6 remove |
| R17. The settings reader's old-file cases | `tests/lib/test_config.py#Test_module.test_an_old_parity_md_is_named_with_every_key_the_template_holds`; the imports of `write_old_config` and `TABLE`; the module docstring's clause on `config.md` (`:4-8`) | R9's unit goes. The S3 case is rewritten (*Scope* item 6) |
| R18. The walker's ties to the converter | `tests/lib/test_tables.py`: the `config` and `seal` module loads (`:89-96`); `test_the_config_pass_is_the_config_readers_header`; the `seal.converted` assert of `test_a_repeated_header_is_read_as_a_row_and_the_doubled_item_is_refused`; every `config.OLD_TABLE`, in `#walk`, `test_refuses_a_fenced_pipe_line_as_a_line_somebody_wrote` and `test_refuses_a_commented_row_in_either_line_ending`; the docstrings and comments naming `seal mode`'s converter (`:4-10`, `:89-90`, `:111-113`, `:462-467`, the two class docstrings) | The cases walk a header literal the file holds (G9, `frame/plan.md` A5) |
| R19. The gate's old-file cases | `tests/skills/test_broad_gate.py`: the `unconverted` shape of `test_refuses_a_file_that_will_not_read` and its docstring clause; `test_refuses_an_unconverted_config_and_names_seal_mode`; the `config.md` assert and the #1454 premise of `#Test_missing_row.test_refuses_to_send_a_person_to_the_table_no_command_reads` | R1's refusal goes. The last case keeps its first assert, under a name and docstring saying it pins the refusal's `config.json` path: no other case pins that path (executed: `grep -n "has no" tests/skills/test_broad_gate.py`; `:630` and `:2222` match the key's words alone) |
| R20. The fold's, pull request body's and pact's old-file shapes | the `unconverted` shape and its branch in `tests/skills/test_fold_check.py#test_an_unreadable_config_is_refused_not_read_as_no_row`; the `unconverted` shape and its branches in `tests/skills/test_pr_body.py#test_refuses_a_language_row_no_one_reads_naming_no_machine_path`; the "an earlier release's config.md" shape of `tests/skills/test_pact_check.py#test_refuses_a_pact_config_that_will_not_read`; each docstring's clause naming it | R1's refusal goes |
| R21. The parity arm's old-file cases | `tests/skills/test_chain_check.py`: `OLD_PARITY`, `OLD_PARITY_TEXT` and their comment (`:2348-2350`); `test_refuses_an_earlier_releases_parity_md_once_naming_the_keys`; `test_s3_an_earlier_releases_parity_md_under_agentic_seal_is_refused_there` | R7 goes |
| R22. The update's block step | `skills/update/SKILL.md` *4. Take out the preset block.*, `:137-213` | Release note (*Scope* item 12) |
| R23. The update's paragraph on deleting nothing the user wrote | `skills/update/SKILL.md` *What this does not do*, the paragraph **It does not delete anything the user wrote.** | It stated R22's bound |
| R24. The block's template | `templates/setup/claude-md-block.md` | 0.24.x's update step read it; the owner judged that path needs no keeping (G3) |
| R25. The template's exemption | `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#READ_BY_AN_EARLIER_RELEASE`, its comment (`:686-692`), the docstring paragraph (`:716-718`), and its two uses (`:759-760`, `:764`) | Goes with R24 in one commit (G3) |
| R26. The block's test module | `tests/behaviour/test_the_old_block_leaves_through_update.py`, whole | Its cases hold R22 and R24; its two `CLAUDE.md` import cases move (*Scope* item 8) |
| R27. The release-hygiene pin on the marker | `tests/behaviour/test_release_hygiene.py#test_update_names_the_marker_of_the_block_it_takes_out` | R22 goes |
| R28. The update's launcher step | `skills/update/SKILL.md` *4b. The launcher an earlier release wrote.*, `:215-233`, and step 2's clause sending an already-current update to it (`:39-43`) | Release note (*Scope* item 12) |
| R29. The launcher step's case | `tests/behaviour/test_update_reads_the_config_directory_in_use.py#test_step_4b_reads_the_old_launcher_and_writes_nothing`, the module docstring's sentence on step 4b (`:13-15`), and "step 5's" in `test_the_skill_names_no_fixed_claude_directory`'s docstring, which becomes "step 4's" | R28 goes |
| R30. The stamp tests' launcher pins | `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`: the `4b` citation assert of `test_the_policy_names_the_command_the_marker_and_the_command_to_draw` (`:144-147`) and its docstring clause (`:107-108`); the two `README_FACTS` entries for the citation and `/agentic:update` (`:215-220`); the launcher clause of `test_both_readmes_say_what_the_stamp_hook_writes_and_leaves`'s docstring (`:233-234`) | The README sentences and the `docs/checks/the-stamp.md` sentence they pin leave (*Scope* item 10, `## Rule changes`) |
| R31. The READMEs' passages | `README.md` *Updating* (`:95-108`) and *What runs on your machine* (`:362-366`); `README.ko.md` *업데이트* (`:99-111`) and *내 컴퓨터에서 도는 것* (`:359-363`) | Release note (*Scope* item 12) |

The work adds no mechanism: the one case it writes replaces the S3 case
(R1, *Scope* item 6), and every other change takes something out.

Framed 2026-11-13 by framer, before the build.
