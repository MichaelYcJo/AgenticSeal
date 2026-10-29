# Design: 1793273065-the-core-reaches-no-users-repository

The plugin's core, the two sections `CLAUDE.md` opens with, is read by
nobody outside this repository: a plugin user's session reads the preset
block and an agent reads `agent-contract`, and neither carries it (#1177).
This design moves the core into one shipped file, `skills/core/SKILL.md`,
and gives every reader one way to reach it: an agent through its
definition's `skills:` list, a session through one `@` line in the preset
block, and a session here through that same block plus a rule in
`CLAUDE.md` saying which copy governs.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The rule a mechanism is kept against* (read at `8db7dadd`): "A fact has one source, and every other place links to it" | The core is one file. The block links to it, `CLAUDE.md` links to it, and no file keeps a copy: `tests/text/test_no_passage_is_pasted_into_a_second_file.py` reads `skills/` and `CLAUDE.md` for copies |
| `CLAUDE.md` *The first value: efficient development through the workflow* (read): "this file holds what all of them share" | The core is not split into an agent's side and a session's side. It moves whole, headings unchanged, so every citation of a section moves by path alone |
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each* (read): the file every agent receives arrives through `skills:` | The core is the second entry of every definition's `skills:` list, before `agent-contract`. `tests/text/test_every_agent_reads_the_contract.py#shape_problems` pins the list as `agent-contract` alone and the opening sentence verbatim; both change with the list |
| `docs/the-record-layout.md` *A change writes fragments, never a shared file* (read): a diff that changes `CLAUDE.md` or `agents/*.md` ends its fragment with `### Process changes` | This diff changes both. The fragment carries one process row, and the rule's file list gains `skills/core/SKILL.md` (*Rule changes* below) |
| `docs/branch-and-release.md` *Cutting a release* (read): the version moves in the first pull request into `release/vX.Y.Z`, in the commit that adds the fragment | This is the first pull request into `release/v0.25.0`: `.claude-plugin/plugin.json` moves from `0.24.2` to `0.25.0` in the commit that adds `changelog.md` (plan phase 4) |
| `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py` (read): the block is the template's marker region byte for byte; `CLAUDE.md` here carries no copy because a session here reads the installed block | The block stays a template the installer copies, so it holds a fixed path and no per-machine value. `CLAUDE.md` here holds no `@` line: it would load the core a second time beside the installed one |
| `skills/implement/SKILL.md` *1. Read the documents that outrank the code first* (read): a ticket is a request, ranked above the code and below the ratified documents | The issue's candidate, a link in the block, is weighed against replacing the block (`plan.md` *Alternatives considered* A5) and taken as the default; the replacement is Q1 of `questions.md` |
| The issue's comments: `gh issue view 1177 --json comments --jq '.comments \| length'` prints `0` (executed, 2026-10-29) | The body is the whole request |
| `bin/seal payload` at `8db7dadd` (executed, 2026-10-29): the `CLAUDE.md` pair is 7,716 B, 2,411 tokens estimated at 3.2 B/token; `skills/agent-contract/SKILL.md` is 12,267 B, 3,833 tokens; each agent's total is between 22,888 B (tracer) and 32,471 B (framer). `skills/verify/scripts/payload_meter.py#composition` reads the pair as two flat files and follows no `@` line (read) | The meter cannot see an imported core today. Phase 3 teaches it the `@` line, or the "after" number the issue asks for is false by construction |
| Probe a, executed 2026-10-29 with Claude Code 2.1.312, `claude -p --model sonnet --no-session-persistence --tools ""` in scratch projects: a project `CLAUDE.md` holding `@docs/core.md`, the target inside the working directory, puts the file's line in the model's context | An `@` import of a file under the importing file's own tree loads in a headless session |
| Probe b, same run: `@docs/link.md`, a symlink to `core.md`, loads the target | Symlinks are followed. A3 of the plan rests on this and is still rejected |
| Probe c, same run, twice: `CLAUDE.md` and `CLAUDE.local.md` of one project both holding `@docs/core.md` put the imported line in context once | Claude Code reads a file once when two memory files inside the working directory import it by one path. The design never imports the core twice, so this answers the issue's first probe question without changing the build |
| Probe d, same run: an import whose target resolves outside the working directory, `@../core.md` from an ancestor `CLAUDE.md` with the session in a subdirectory, an absolute path, and `@~/orca/workspaces/…`, loads nothing in a headless session; the `@` line stays visible | A project-level file cannot carry the link: from there the import is external, and the docs (next row) say an interactive approval gates it. `install.sh --project` goes (*Removes*) |
| Probe e, same run: `@docs/not-there.md` loads nothing and leaves no error in context | A dangling link is silent, so `install.sh` warns when the file the block imports is absent beside the target it wrote |
| Probe f, same run: a `SessionStart` hook in a project's `.claude/settings.json` running `cat core.md` puts the file in context | A plugin hook can deliver the core without a `CLAUDE.md` block (plan A5, `questions.md` Q1) |
| Not executed: an import from the user-scope file. The only `~/.claude/CLAUDE.md` on this machine is the owner's, and a session under a scratch `CLAUDE_CONFIG_DIR` printed `Not logged in` | Q2 of `questions.md` names the measurement; the design rests on the two docs sentences below for it |
| code.claude.com/docs/en/memory.md (read 2026-10-29 through the `claude-code-guide` agent): "Both relative and absolute paths are allowed. Relative paths resolve relative to the file containing the import, not the working directory. Imported files can recursively import other files, with a maximum depth of four hops."; "An import in a project-level memory file is external when its path resolves outside your working directory"; "The first time Claude Code encounters external imports in a project, it shows an approval dialog listing the files. If you decline, the imports stay disabled and the dialog doesn't appear again."; "User-scope memory files, such as ~/.claude/CLAUDE.md and ~/.claude/rules/, are files you wrote yourself. Except in Cowork sessions on your desktop, Claude Code loads their imports without the dialog."; the page's own example is `@~/.claude/my-project-instructions.md` | The block's line is a relative path, resolved against `~/.claude/CLAUDE.md`, so it needs no `~` and follows `CLAUDE_CONFIG_DIR`; a user-scope import needs no approval; the meter follows at most four hops |
| code.claude.com/docs/en/plugins/loading.md and env-vars.md (read, same agent): the plugins root is `~/.claude/plugins` unless `CLAUDE_CODE_PLUGIN_CACHE_DIR` names another; `marketplaces/<name>/` holds the clone of a marketplace added from GitHub; a marketplace added from a local directory has no copy there; `CLAUDE_CONFIG_DIR` moves settings, sessions and plugins together. On this machine `~/.claude/plugins/known_marketplaces.json` names `installLocation: /Users/yc/.claude/plugins/marketplaces/agenticseal`, that clone is at `475be4a` (the v0.24.2 merge), and `installed_plugins.json` installs `cache/agenticseal/agentic/0.24.2` (executed, `cat` and `git -C … log -1`) | The import path `plugins/marketplaces/agenticseal/skills/core/SKILL.md` is where the clone is on a default machine; a machine with another plugins root, or a local-directory marketplace, has no file there and gets the installer's warning |
| code.claude.com/docs/en/hooks.md (read, same agent): a `SessionStart` hook's stdout is added as context; it fires on `startup`, `resume`, `clear` and `compact`; a plugin's `hooks/hooks.json` registers one. `hooks/hooks.json` already registers `session-start` (read) | The hook route in A5 is a real alternative, not a guess |
| `~/.claude/CLAUDE.md` on this machine carries the block (the orchestrator's finding, read); its `Language` section is the owner's own | Nothing in this work writes that file. The owner takes the 0.25.0 block through `/agentic:update` as every user does, after the release |

## Scope

**In.**

1. **The core becomes `skills/core/SKILL.md`.** The two sections of
   `CLAUDE.md`, *The first value: efficient development through the
   workflow* and *The rule a mechanism is kept against*, move there whole,
   with their headings, under a skill frontmatter in the shape of
   `skills/agent-contract/SKILL.md`'s: `name: core`, a description that says
   it is not a command to run and names its two readers, and no
   `disable-model-invocation` line, so a session that wants it by name can
   load it. The title line is `# The core`. The name `core` is the word the
   issue, milestone 69 and `routing.md` use for it. One sentence is added to
   the paragraph *Asking a person is the most expensive judgment*: the one
   question is the routing question, asked by the session that spawns the
   work, as `skills/implement/orchestration.md` *Orchestrator: how the work
   is routed* states, and `hooks/routing-edit-gate.py` refuses the first edit
   until it is answered. That sentence is what the block's routing bullet
   carried that no mechanism reaches: a session that has never opened a
   skill learns where the question is. The vocabulary, the boxes and the
   write stay the section's alone. Nothing else in the core is reworded:
   #1170 moves the single-rule applications out, and #1148 reads every
   document against the core; both start from the text as #1172 left it.
2. **`CLAUDE.md` keeps what is this repository's own.** The title, then one
   section, *The core*, saying: the core is `skills/core/SKILL.md`, one file
   for every party; an agent receives it through `skills:`; a session
   receives it through the preset block in `~/.claude/CLAUDE.md`, which
   imports the marketplace clone's copy, the last release's; this file does
   not import it, because a session here would then read it twice; where the
   branch changes `skills/core/SKILL.md`, which `git diff --stat
   <base>...HEAD -- skills/core/SKILL.md` shows, the tree's copy governs and
   a session here opens it before judging by the installed one; where the
   branch does not change it, the two are one text. A session here between
   this merge and the 0.25.0 release has no installed core at all, because
   the 0.24.2 clone holds no `skills/core/SKILL.md`; the same sentence covers
   it, since the branch changes the file. No link row of the old `CLAUDE.md`
   stays: the one row the tests pinned, the batch rule's link to
   `skills/implement/SKILL.md` *1. Read the documents that outrank the code
   first*, is inside the paragraph that moves.
3. **Every agent receives it.** Each `agents/*.md` lists `core` then
   `agent-contract` under `skills:`, and its opening sentence becomes
   "`skills/core/SKILL.md` and `skills/agent-contract/SKILL.md` bind you, and
   both arrived before your first tool call." The order is values before
   rules, which is the order a reader needs them in.
4. **The block holds the link and nothing else.** The template becomes the
   two markers around one line, `@plugins/marketplaces/agenticseal/skills/core/SKILL.md`.
   Each rule the block holds today moves to the one file that applies it,
   or is already stated there (*Removes* row 1 names each home). `install.sh`
   writes the block to `~/.claude/CLAUDE.md` or to the path given; the
   `--project` scope, the interactive scope prompt and the overlap warning go;
   after writing, it warns when
   `<target's directory>/plugins/marketplaces/agenticseal/skills/core/SKILL.md`
   is not a file, naming the path, because a dangling import loads nothing and
   says nothing (probe e). `uninstall.sh` is unchanged. `preset-setup` keeps
   the steps that write or replace the block and loses the ones that classify
   overlaps, since a one-line block overlaps nothing. `update` step 4 keeps
   its diff and its rows, loses the `--project` sentence and the overlap
   paragraph, and says, when the block differs, that the core arrived. The
   README rows and sentences that describe the block's rules, its two scopes
   and the overlap merge say the new thing in their place.
5. **`seal payload` sees the imported core.** `payload_meter.py#composition`
   follows the `@` lines of each file in the `CLAUDE.md` pair: a token `@`
   at the start of a line or after whitespace, followed by a path that runs
   to the next whitespace; a quoted path is not an import; a leading `~`
   expands to the home the meter was given; a relative path resolves against
   the importing file's directory; at most four hops; a path that is not a
   file is a `missing` row; one real path is counted once across the pair.
   Each imported file is a row of the harness share, displayed as the
   importing file's display name, an arrow and the imported path. The JSON
   carries the same rows; `render` names them in the pair's line. The
   before/after numbers the issue asks for come from two runs of the meter
   against a scratch home: one holding today's block, one holding the new
   block and a `plugins/marketplaces/agenticseal` directory that is a copy of
   the tree. Both numbers go into phase 3's record and the pull request body.
6. **The release shape.** `changelog.md` with a `### Fixed` entry saying the
   core arrived in every session and every agent, and a `### Process changes`
   row; `plugin.json` to `0.25.0` in the same commit.
7. **What stood on the old fact is corrected in the same commit** (contract
   rule 19): `CONTRIBUTING.md:368` and `:381` cite the sections by their new
   path; `CONTRIBUTING.md:473` says "the core, which every session loads" in
   place of "the CLAUDE.md block"; `install.sh`'s header stops saying a
   plugin cannot carry a `CLAUDE.md` block; `hooks/mode-gate.py:16-19` and
   `skills/verify/scripts/broad_gate.py:4-5` stop describing the block's
   rules and name the rules' homes; `skills/implement/orchestration.md:458`
   says the core, loaded in every session, names the routing section;
   `skills/verify/orchestration.md:146` cites `agents/crafter.md` *Three
   failed fixes stop the work* instead of "the 3+ Fix Rule";
   `.github/scripts/release_report.py#DOCUMENTS` gains `skills/core/SKILL.md`,
   so the release report measures the core where it measured `CLAUDE.md`;
   `tests/text/test_a_rider_reaches_its_file.py:66` and
   `tests/behaviour/test_chain_hooks_hardening.py:773` name the core's path
   where they name `CLAUDE.md`'s.

**Out.**

- The wording of the values. #1170 and #1148 own it; this work moves text
  and adds the one sentence item 1 names.
- The `<!-- specseal:start -->` markers and how long a straight upgrade from
  before 0.23.0 stays supported: #1154 (0.25.2).
- The README rewritten for a first reader: #1102 (0.25.1). Only the rows
  and sentences this change makes false are rewritten here.
- Writing `~/.claude/CLAUDE.md` on this machine, or any machine. The block
  reaches a user through `/agentic:update` after the release.
- A `SessionStart` hook as the core's carrier, retiring the block. It is
  weighed in `plan.md` A5 and put to the owner as Q1; the build proceeds on
  the link.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 An agent receives the core | Given any definition under `agents/`, when the harness spawns it, then its context holds `skills/core/SKILL.md` and then `skills/agent-contract/SKILL.md` before its first tool call, and its opening sentence names both | `tests/text/test_every_agent_reads_the_contract.py`: `skills:` is `core` then `agent-contract` in every definition and the sentence is the new one; `bin/seal payload` lists `skills/core/SKILL.md` as a row of every agent |
| S2 A session in a plugin user's repository receives the core | Given a machine whose `~/.claude/CLAUDE.md` holds the 0.25.0 block, when a session starts in any repository, then the core from `~/.claude/plugins/marketplaces/agenticseal/skills/core/SKILL.md` is in its context, once | A case in `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py` pins the block to the two markers and the one `@` line; the import's loading itself is Q2's measurement, run on an installed machine after the release |
| S3 A session in this repository reads one core and knows which governs | Given this repository with the owner's block installed, when a session starts, then it reads the installed core through the block and no second copy, and `CLAUDE.md` tells it to open `skills/core/SKILL.md` where the branch changes it | `test_this_repository_carries_no_copy_of_the_block` stays green; a new case pins that `CLAUDE.md` holds no `@` line and names `skills/core/SKILL.md`; `tests/text/test_no_passage_is_pasted_into_a_second_file.py` finds no shared run between `CLAUDE.md` and the core |
| S4 The block carries no rule | Given the template, when it is read, then between its markers stands the `@` line and nothing else, and each of the eight rules it held stands in one home | The case of S2; the homes' own cases: `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafters_four_rules_stand_with_their_enforcers` for the three-fix rule, `tests/text/test_the_agent_contract_holds_the_universal_rules.py` for rules 2, 4 and 10, a case reading `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* for the tooling and lint sentences, a case reading `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* for the worktree sentence, and a case reading the core for the routing section's name |
| S5 The cost of loading the core is measured | Given the tree before and after, when `seal payload` runs against a scratch home holding each block, then the pair's row names the imported core and its bytes, and the pull request states both totals | `tests/skills/test_payload_meter.py`: an `@` line in either file of the pair adds a harness row; a `~` path and a relative path resolve; a symlink resolves to its target; a missing target is a `missing` row; the same real path imported twice is one row; depth stops at four; phase 3's record carries the two numbers |
| S6 `/agentic:update` brings the block | Given a machine on 0.24.2, when `/agentic:update` runs after the 0.25.0 release, then step 4 finds the block differs, replaces it, and names the core as what arrived | `tests/behaviour/test_release_hygiene.py#test_update_tells_the_user_when_the_preset_block_changed` stays green against the rewritten step; the `### Fixed` entry says the core arrived |
| S7 The installer says when the link cannot load | Given a target whose directory holds no `plugins/marketplaces/agenticseal/skills/core/SKILL.md`, when `install.sh` writes the block there, then it exits 0 and prints a warning naming that path | A case in `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py` runs the installer against a scratch target and reads the warning; a sibling case plants the file and reads no warning |
| S8 The release carries the version and the process row | Given the first pull request into `release/v0.25.0`, when its fragment commit lands, then `plugin.json` says `0.25.0` and the fragment ends with the process table | `tests/github/test_publish_release_note.py` reads the fragment's shape; `.github/workflows/hygiene.yml` holds the version at the release pull request |

## Data & interfaces

- `templates/setup/claude-md-block.md` after the change, whole:

  ```
  <!-- agentic:start -->
  @plugins/marketplaces/agenticseal/skills/core/SKILL.md
  <!-- agentic:end -->
  ```

  Relative to the file that holds it: from `~/.claude/CLAUDE.md` it reads
  `~/.claude/plugins/marketplaces/agenticseal/skills/core/SKILL.md`; from
  `$CLAUDE_CONFIG_DIR/CLAUDE.md` it reads the clone under that directory,
  which is where the docs put it. A `~` form would not follow
  `CLAUDE_CONFIG_DIR`.
- `skills/core/SKILL.md`: frontmatter (`name: core`, `description: |` of
  about six lines), `# The core`, then the two sections as `CLAUDE.md`
  holds them at `8db7dadd`, with the one added sentence of *Scope* item 1.
  The two `##` headings are unchanged, so a citation `CLAUDE.md` *The rule a
  mechanism is kept against* becomes `skills/core/SKILL.md` *The rule a
  mechanism is kept against* and nothing else.
- `agents/*.md` frontmatter: `skills:` with `- core` then
  `- agent-contract`. `tests/text/test_every_agent_reads_the_contract.py#SENTENCE`
  and `#shape_problems` pin the new list and sentence; `GOOD` and the
  planted cases follow.
- `CLAUDE.md` after: `# AgenticSeal`, `## The core`, the sentences *Scope*
  item 2 lists, and no other section.
  `tests/text/test_the_rules_claude_md_names_have_one_home.py#LINKED` moves
  its `CLAUDE.md` entry to `skills/core/SKILL.md` and `#CARRIERS` gains that
  path; `tests/text/test_a_language_section_of_writing_style_opens_alone.py:178-187`
  reads the core for the writing rules' name and keeps the block clean of it.
- `install.sh`: usage `bash install.sh [<target-CLAUDE.md>]`, default
  `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md`; after the write, the
  file-exists check of *Scope* item 4 and its `warn` line.
- `payload_meter.py`: `imports_of(path, home, depth)` returning
  `[(display, real_path)]`; `composition` appends one harness row per
  imported file; `file_row` gains an optional `via` field the JSON carries;
  `render` prints the pair's bytes as the two files plus their imports and
  names each import.
- `.github/scripts/release_report.py#DOCUMENTS`: `("skills/core/SKILL.md",
  "CLAUDE.md", "CONTRIBUTING.md", "docs/*.md")`;
  `tests/github/test_release_report.py#tree` plants the core.
- `changelog.md`: `### Fixed` with one entry, then `### Process changes`
  with one row, date `2026-10-29`, change "the core is one shipped file every
  agent preloads and every session imports through the preset block, which
  holds that one line and no rule", why "the values that make the workflow
  reached no repository but this one", source the issue.

## Rule changes

- change
  file: docs/the-agent-set.md
  section: One contract every agent receives, and one definition each
  from: **The rules true of every agent live in one file every agent receives before its first tool call, without a prompt asking for it.**
  to: **The core every party shares and the rules true of every agent each live in one file every agent receives before its first tool call, without a prompt asking for it: `skills/core/SKILL.md`, then `skills/agent-contract/SKILL.md`, in that order in every definition's `skills:` list.**
- change
  file: docs/the-record-layout.md
  section: Every kind of record, at a glance
  from: | The repository's rules | `CLAUDE.md` for the rules a session must hold, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
  to: | The repository's rules | `skills/core/SKILL.md` for the core every party reads, `CLAUDE.md` for how a session in this repository reaches it and which copy governs, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
- change
  file: docs/the-record-layout.md
  section: A change writes fragments, never a shared file
  from: A work item whose diff changes `CLAUDE.md`, an `agents/*.md` file, a `skills/*/orchestration.md` file or `skills/implement/bootstrap.md` ends its `changelog.md`
  to: A work item whose diff changes `skills/core/SKILL.md`, `CLAUDE.md`, an `agents/*.md` file, a `skills/*/orchestration.md` file or `skills/implement/bootstrap.md` ends its `changelog.md`
- change
  file: docs/the-record-layout.md
  section: The root records
  from: | `CLAUDE.md` | the rules a session in this repository must hold, each linking to its home |
  to: | `CLAUDE.md` | how a session in this repository reaches the core, `skills/core/SKILL.md`, and which copy governs where the installed one and the tree's differ; any rule this repository alone asks of a session, each linking to its home |
- change
  file: docs/branch-and-release.md
  section: Cutting a release
  from: a red nobody here can act on is what `CLAUDE.md`'s first goal is against.
  to: a red nobody here can act on is what `skills/core/SKILL.md` *The first value: efficient development through the workflow* is against.
- change
  file: docs/release-checklist.md
  section: 6. After the merge
  from: a red nobody can act on is what `CLAUDE.md`'s first goal is against.
  to: a red nobody can act on is what `skills/core/SKILL.md` *The first value: efficient development through the workflow* is against.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The eight rule bullets of the preset block | `templates/setup/claude-md-block.md` (its `Tooling`, `Safety`, `Session cost` and `Git` sections) | Tooling (uv, pnpm, the project's own manager wins): one sentence in `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*, beside the commit cadence. 3+ Fix Rule: `agents/crafter.md` *Three failed fixes stop the work* already states it, and `skills/verify/orchestration.md` *Three returns and stop* cites it by path. Verification Gate: `skills/verify/SKILL.md`'s `Use when` and its `executed` label already state it, with contract rule 4. Verification Scope: contract rule 2, `docs/the-broad-gate.md` and `skills/verify/orchestration.md` *Nothing edits between the broad run and the PR* already state it. Batch independent reads and runs: contract rule 10 already states it; the orchestrating session's trips are measured by `docs/the-review-record.md` *The per-segment bars*, and no always-on sentence replaces the one that goes. Lint, format and typecheck before each commit: one sentence in `skills/implement/SKILL.md` *2.*, with `hooks/lint-python.py` named as what already runs ruff on each edit where the project configures it. Worktrees only for concurrent sessions, otherwise `git switch`: one sentence in `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, step 1, where the branch is made. Routing, decided at the start: `skills/implement/orchestration.md` *Orchestrator: how the work is routed* and `hooks/routing-edit-gate.py` already hold it; the core's added sentence names the section |
| The two sections of `CLAUDE.md` | `CLAUDE.md` *The first value: efficient development through the workflow*, *The rule a mechanism is kept against* | `skills/core/SKILL.md`, same headings, the one sentence of *Scope* item 1 added |
| The `--project` scope, the interactive scope prompt and the overlap warning loop | `install.sh:22-42`, `:106-116`, `:123-125` | From a project-level file the import is external: an interactive approval gates it and a headless session never loads it (probe d, docs). The loop warned about rules the block no longer holds. The README's "pick ONE scope" lines (`README.md:293-300`, `:270`, `:361-366`; `README.ko.md` the same rows) go with them |
| The installer's header claim that a plugin cannot carry a `CLAUDE.md` block | `install.sh:4-9` | A hook can carry context (probe f); what the block carries now is the one line a user's own memory file holds. The header says that |
| `preset-setup`'s scope question and overlap classification | `skills/preset-setup/SKILL.md` *Procedure* steps 0, 3 and 4, and "with semantic dedup" in its description | The skill keeps the back-up, the write or replacement of the block under either marker pair, and the confirmation; nothing is left to classify |
| `update` step 4's `--project` sentence and its overlap paragraph | `skills/update/SKILL.md` *4. Take the preset block if it moved* | The diff, its four rows and the pointer to `preset-setup` stay; the step says the core arrived when the block differs |
| The clause saying the block carries the routing question's shape | `skills/implement/orchestration.md` *Orchestrator: which of these acts runs itself*, the row `Orchestrator: how the work is routed` | The core, loaded in every session, names the section; the hook refuses the first edit |
| The docstring sentences describing the block's rules | `hooks/mode-gate.py#module docstring` lines 16-19, `skills/verify/scripts/broad_gate.py#module docstring` lines 4-5 | Each names the rule's home instead: the core's sentence for the routing question, contract rule 2 and `docs/the-broad-gate.md` for the scope |
| Cases that pin a rule to the block | `tests/text/test_broad_gate_rule.py#test_the_preset_block_states_the_rule_the_loaded_files_assume`; `tests/text/test_review_axes.py#test_the_preset_block_carries_the_routing_decision`, `#test_implement_and_the_preset_block_do_not_drift`; `tests/behaviour/test_first_setup_asks_once.py#test_the_preset_sends_a_fresh_repository_to_the_bootstrap`, `#test_the_preset_writes_no_declaration_under_no_work_item`, `#test_the_preset_names_both_places_the_root_can_be`, `#test_the_preset_says_whose_decision_the_place_is`, `#test_what_the_installer_copies_carries_it`, and the comment block above them at `:780-797`; `tests/behaviour/test_waiver_decided_at_start.py#test_the_preset_block_carries_it_too` | Their premise, that the block is the one copy a session always reads, is replaced by the core. What each guarded moves to a case that reads the core's routing sentence for the section's name, and to the orchestrator-half cases that already read `orchestration.md` (`#test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap` stays). `tests/behaviour/test_release_hygiene.py#test_update_tells_the_user_when_the_preset_block_changed` and `tests/behaviour/test_chain_hooks_hardening.py#test_the_always_on_block_is_described_without_counts` stay as they are |
| The `## Tooling` edit the installer's update case uses to make a stale block | `tests/behaviour/test_the_installer_writes_the_block_from_its_template.py#test_install_sh_replaces_an_older_block_from_the_template` | The case edits the `@` line instead |
| The README sentence that the block's rules are "loaded every turn" and the cheat-sheet switch `[--project]` | `README.md:45`, `:270`; `README.ko.md:45`, `:265` | The row says the block is one `@` line that imports the core from the marketplace clone, its one source still `templates/setup/claude-md-block.md` |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-29 by framer, before the build.
