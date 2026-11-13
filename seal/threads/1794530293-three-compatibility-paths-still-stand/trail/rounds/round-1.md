# Review round 1: 1794530293-three-compatibility-paths-still-stand

```seal
target: c97122644 against release/v0.38.1
```

The base is `release/v0.38.1` at `8f6acbb0e`, the merge base of the target
(executed: `git merge-base c97122644 8f6acbb0e`). No earlier round record
exists, so no fact was carried: every coordinate below was opened at the
target or at the base. `seal/parity.json` is not declared here, so no parity
comparison was made.

The work item's records were read whole at `c97122644`: `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md`, `pr.md`, `trail/phases/phase-1.md` and
`trail/phases/phase-2.md`. No `pr.<lang>.md` stands, since both language
keys of `seal/config.json` read `English` (read).

## Findings

### 1. The 0.38.1 Updating line tells a person on 0.37.0 or later that nothing is left to do, and a machine or a repository on that release can still hold what the removed paths dealt with

```seal
severity: should
location: `seal/threads/1794530293-three-compatibility-paths-still-stand/changelog.md:8`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/design.md:105-125`
evidence: read `seal/threads/1794530293-three-compatibility-paths-still-stand/changelog.md:8`, `8f6acbb0e:skills/update/SKILL.md:39-43`, `8f6acbb0e:README.md:95-101`, `8f6acbb0e:lib/config.py:139-141`, `seal/threads/1794530293-three-compatibility-paths-still-stand/frame/plan.md:92-97`; executed `git show <tag>:lib/config.py` and `git show <tag>:skills/update/SKILL.md` for v0.35.0, v0.36.0, v0.37.0, v0.37.1 and v0.38.0
```

Why it matters: this line is the one place that tells a person what to do
after this release (`frame/plan.md:39-41`), and `/agentic:update` step 3
prints it. It opens "nothing to do if you are on 0.37.0 or later". That
version is the plugin's, on one machine. What each removed path dealt with
is a file on that machine or in one repository, and none of those files was
taken out by reaching 0.37.0.

- The launcher and the `CLAUDE.md` block. Until this release, step 2 of
  `/agentic:update` ran step 4b even on an update that was already current,
  "because a person who reached this release by `claude plugin update` alone
  may still hold the launcher an earlier release wrote"
  (`8f6acbb0e:skills/update/SKILL.md:39-43`). Steps 4 and 4b stand in every
  tag from v0.35.0 to v0.38.0 (executed). So a person who went from 0.24.x
  or 0.34.x to 0.37.x with `claude plugin update` alone is on 0.37.0 or
  later and still holds the block or the launcher.
- `seal/config.md`. In 0.37.0 to 0.38.0, `lib/config.py#config_pairs`
  refused the file only when a command read a setting in that repository
  (`8f6acbb0e:lib/config.py:139-141`), and only `seal mode` converted it. A
  repository where no such command ran while the plugin was on 0.37.x still
  holds it. The README this work removes said it per repository: "Run
  `seal mode` once in each repository that still holds `seal/config.md`"
  (`8f6acbb0e:README.md:99-100`).

Such a person reads the 0.38.1 note, is told nothing is to do, and every key
of that repository then reads as absent with no command naming why
(`frame/design.md` G6). The frame states the scope correctly elsewhere:
`frame/plan.md:92-95` names "a repository last set up by 0.36.x or earlier,
or a machine last updated by 0.24.2 or earlier, or by 0.33.0 to 0.34.1".
The Updating line, and *Scope* item 12 it was written from
(`frame/design.md:107-109`, "a person on 0.37.0 or later has nothing to
do"), turn that into a plugin version.

What the build claimed: phase 2 says the line "gives one sentence for each
act *Scope* item 12 names" (`trail/phases/phase-2.md`). That holds, and
`gaps.md` hands S7 to this round for that reason. Each act is there, and
the defect is the condition the line opens with.

The fix replaces the first two sentences of the line and keeps the five
acts after them as they read. Then the opening of *Scope* item 12's
*Updating* sentence (`frame/design.md:107-109`) says the same thing, so the
frame and the fragment agree. That frame edit is a fold, and the fix pass
owes it too:

```markdown
Updating: nothing to do where none of what follows stands, whichever release you are on. Releases up to 0.36.0 left each of them, and until this release `/agentic:update` and `seal mode` dealt with them only where they ran, so a machine that reached 0.37.0 or later through `claude plugin update` alone, or a repository where no command read a setting on 0.37.x, can still hold one. Write `seal/config.json` from `templates/setup/config.md`, with the rows of `seal/config.md` as its keys, and delete `seal/config.md`, since no command reads that file and every key reads as absent until then. Where `seal/parity.md` stands, write `seal/parity.json` from `templates/setup/parity.json` and delete `seal/parity.md`, since the parity arm reads no `parity.md`. Move the `| Signer |` table of a `seal/pact.md` into a `Pact signers` key of that repository's `seal/config.json`, and `~/.claude/agentic/pact-paths.md` into `~/.claude/agentic/pact-paths.json`. Delete the lines between `<!-- agentic:start -->` and `<!-- agentic:end -->` in `~/.claude/CLAUDE.md`, the markers included, which a release from 0.23.0 to 0.24.2 wrote. Remove from `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/settings.json` the `Stop` entry whose command runs `${CLAUDE_PLUGIN_DATA}/stamp.py`, then that file, which a release from 0.33.0 to 0.34.1 wrote.
```

For `frame/design.md` *Scope* item 12, the sentence opening "The *Updating*
line says that a person on 0.37.0 or later has nothing to do" becomes:

```markdown
The *Updating* line says that nothing is to do where none of the files
below stands, whatever release the plugin is on, and that a person who
holds one does by hand what the removed paths did, each as one clause:
```

### 2. The comment above `lib/tables.py`'s import of `blocks` lists three callers that load the walker through `lib/sibling.py`, and a fourth does

```seal
severity: should
location: `lib/tables.py:23-26`, `seal/threads/1794530293-three-compatibility-paths-still-stand/trail/phases/phase-1.md:43-44`
evidence: read `lib/tables.py:10-11`, `lib/tables.py:23-26`, `.github/scripts/rules.py:107-120`, `seal/threads/1794530293-three-compatibility-paths-still-stand/trail/phases/phase-1.md:43-44`; executed `git grep -n -E 'load\(.*tables|TABLES\b' -- skills .github lib`
```

Why it matters: *Removes* R10 asks that the comment be "Rewritten to the
callers that stand". Phase 1 claims it "names the scripts that load the
walker through `lib/sibling.py`: `pact_check.py`, `settle.py` and
`rule_changes.py`" (`trail/phases/phase-1.md:43-44`). `.github/scripts/rules.py`
loads `lib/tables.py` through `lib/sibling.py#load` too, as its `SIBLINGS`
map names (`.github/scripts/rules.py:107-120`). The module docstring of
`lib/tables.py` already names `rules.py` as a reader (`lib/tables.py:10-11`).
So the list handed back as whole is a sample. A maintainer who edits the
`sys.path` line below reads the comment for who depends on it, and is
told three of four. A list kept beside the tree goes out of step again at
the next caller, so the fix drops it rather than adding the fourth name:

```python
# `lib/blocks.py` is a sibling, found by this file's own directory, so a
# script that loads this module through `lib/sibling.py` finds it too.
# `lib/routing.py` reaches `optin.py` the same way.
```

The phase record's sentence at `trail/phases/phase-1.md:43-44` states the
same list, and the fix pass owes it too: either the same rewording, or a
clause that `rules.py` was missed.

## Confirmations

What matched: S1. `lib/config.py#config_pairs` returns `(None, None)` for a
root without `config.json` whatever else stands there, and nothing in it
opens `config.md` (read, `lib/config.py:95-130`). The rewritten case
`tests/lib/test_config.py::Test_config_pairs::test_reads_a_config_md_standing_alone_as_no_file`
passes (executed). By reading the base arm (`8f6acbb0e:lib/config.py:139-141`),
it would fail its first assert there, as phase 1 says it did.

What matched: S2, handed to this round by `gaps.md`. Bare `seal mode` over a
root holding `config.md` and no `config.json` goes through `declared`, which
reads `config_pairs` and answers `none`. Then `write_mode` appends `Mode` to
an empty member list and writes a new `config.json`
(`skills/implement/scripts/seal.py:2106-2123`,
`skills/implement/scripts/seal.py:1486-1509`, `lib/config.py:196-237`,
read). No line of `#mode_report` names or opens `config.md` or `parity.md`,
so it prints no conversion and no note, and `config.md` is left as it was
(read). `Test_mode_report` passes (executed).

What matched: S3, handed to this round by `gaps.md`. `chain_check.py#originals_of`
reads `seal/parity.json` alone and returns `[]` where git does not carry it
(`skills/code-review/scripts/chain_check.py:1636-1639`, read). No other line
of `chain_check.py` names `parity.md` (executed: `git grep -n 'parity\.md'`
outside `seal/threads/`, whose one hit is the `docs/checks/the-pull-request-check.md:110`
sentence that a `## Rule changes` `remove` item takes out). `Test_originals_of`
passes (executed).

What matched: S4. `skills/update/SKILL.md` reads steps 1, 2, 2b, 3 and 4;
step 2 stops on an update that is already current; and step 3's "go on to
step 4" names the step that names the two moves (read, `:39-41`, `:125`,
`:135`). `git grep -n -E 'agentic:start|CLAUDE_PLUGIN_DATA|4b' skills/update`
and the same search for `CLAUDE.md` find nothing (executed, exit 1 each).
The *Procedure* clause phase 2 removed, and the plan row that folded it into
R22, agree with the diff (read).

What matched: S5, S6, S8 and S9. `test_every_template_is_named_by_a_document_that_ships`
passes with no exemption left (executed). The S6 search finds only
`templates/setup/config.md` in each README (executed). `git grep -n
2027-02-07` finds the date only in #1492's records other than its
`changelog.md` and in this work item's frame and phase records (executed).
`git show e7215e0e4:.claude-plugin/plugin.json` reads `0.38.1`, and that
commit adds `changelog.md` (executed).

What matched: both phases' census greps, as `frame/plan.md` *Phases* now
states them, print what the Status cells say (executed at the target).

What matched: the five `## Rule changes` operations. Each `from` stands in
its file at the target (read: `docs/layout/one-root-by-lifetime.md:268-272`,
`docs/layout/one-root-by-lifetime.ko.md:254-257`, `docs/checks/the-fold.md:117-119`,
`docs/checks/the-pull-request-check.md:110-111`, `docs/checks/the-stamp.md:94-97`).
No other `docs/` sentence states one of the three paths (executed: the
prose searches under *Not judged*). The chain check printed six notices at
`frame/design.md:187` and `:195`, for example: "a test pins text this
operation takes out of `docs/layout/one-root-by-lifetime.md`:
`tests/block_shapes.py:59` holds "| Item | Value |", and the `to` does not".
The three lines it names, `tests/block_shapes.py:59`,
`tests/lib/test_tables.py:816` and `:847`, are table headers in the walker's
fixtures (read). None of them pins the rule's wording or a fact the sentence
states, so no notice is a finding.

What matched: `pr.md`. Each of its seven quotes stands word for word at the
coordinate it names, with runs of whitespace collapsed (read:
`frame/plan.md:29-41`, `frame/plan.md:115`, `frame/design.md:20`,
`frame/questions.md:30-35`, `routing.md:20`).

What matched: #1492's fragment. Its *Updating* line keeps its first sentence,
and the two that followed are one sentence naming 0.38.1, as *Scope* item 11
asks (read: the diff of
`seal/threads/1794271937-the-readme-narrates-three-migrations/changelog.md`).

What matched: the removed units have no reader left. `seal.py` calls
nothing of `tables` or `blocks`, and no file reaches `seal.converted`,
`seal.tables` or the removed aliases (executed: `git grep` on each name).
`lib/tables.py#gfm_table` has two callers, `settle.py:1245` without
`beside` and `pact_check.py:365` with it, which matches the rewritten
docstring line for `BESIDE` (executed, read).

Two cases left with `tests/behaviour/test_the_old_block_leaves_through_update.py`
that were neither moved nor named in *Removes* by name:
`test_the_installer_the_uninstaller_and_preset_setup_are_gone` and
`test_this_repository_carries_no_copy_of_the_block`. The premise of each
stood on step 4 or on the template ("step 4 is the one remover"; "nothing
holds it to the template any more"), so R26's grounds cover them. Nothing in
the tree now holds that `install.sh`, `uninstall.sh` or `skills/preset-setup`
stays absent, or that `CLAUDE.md` carries no block markers (executed:
`git grep` on each). Under *Scope* item 8 that is the frame's choice, and
this round opens no finding for it.

`tests/text/test_the_rules_claude_md_names_have_one_home.py#test_an_import_line_is_told_from_a_code_span`
puts `@` at the first character of no input, so the `^` alternative of
`IMPORT` is held by nothing. `gaps.md` *Not done* says so. The case moved
word for word and states no fact the frame states, so it is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check: the `Broad gate` key of `seal/config.json` at the target. This round ran only the narrow set under *Probes*, so the suite stays `unverified` | the whole tree | the orchestrator, at its broad run once the rounds settle |
| Prose that restates one of the three paths in words no search reached. The searches were `git grep` over shipped prose (`docs`, `skills`, `templates`, `agents`, `hooks`, `lib`, both READMEs, `CONTRIBUTING.md`) and over `tests`, `evals` and `.github`, for `config.md`, `parity.md`, `convert`, `earlier release`, `older release`, `launcher`, `preset`, `4b`, `CLAUDE.md`, `seal mode`, `agentic:start`, `CLAUDE_PLUGIN_DATA`, `stamp.py`, `Item \| Value`, `0.24`, `0.33`, `0.34`, `0.36`, and the Korean words `이전 릴리스`, `옛` and `실행기`. This is a sample by contract rule 12, since the spellings are unbounded. Every hit outside `seal/threads/` is a sentence a `## Rule changes` item takes out, a *Scope* **Out** item, or text about another subject | the tree outside `seal/threads/` | the sealer, which reads the tree against the issue |
| Whether the published v0.37.1 note keeps its date, which `frame/questions.md` assumes | GitHub release v0.37.1 | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/lib/test_config.py::Test_config_pairs tests/text/test_the_rules_claude_md_names_have_one_home.py tests/behaviour/test_update_reads_the_config_directory_in_use.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py::test_every_template_is_named_by_a_document_that_ships tests/skills/test_chain_check.py::Test_originals_of tests/skills/test_seal.py::Test_mode_report tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py` | exit 0, 58 passed |
| `git grep -n -w -E 'OLD_CONFIG\|OLD_TABLE\|old_config_path\|PARITY_KEYS\|OLD_PARITY_CONFIG\|config_shapes' -- ':!seal/threads'`, and `git grep -n -E 'unconverted_' -- ':!seal/threads'` | exit 1 each, nothing printed |
| `git grep -n -E 'agentic:start\|claude-md-block\|CLAUDE_PLUGIN_DATA\|4b\. The launcher\|2027-02-07' -- ':!seal/threads'` | `docs/checks/the-stamp.md:95` and two lines of the dated experiment record, as the phase 2 Status cell states |
| `skills/code-review/scripts/chain_check.py --baseline 8f6acbb0e --root <clone> --worktree`, before this record existed | exit 0. It printed the six pin notices quoted under *Confirmations*, and named the absent round record, gate record and guarantee as not yet written |
