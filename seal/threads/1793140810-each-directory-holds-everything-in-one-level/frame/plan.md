# Implementation Plan: 1793140810-each-directory-holds-everything-in-one-level

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 1.

## Summary

Five phases, each a fresh crafter, each moving one area and leaving the
tree green under its own narrow run. Phase 1 lands the census first, so
every later phase is held by it at its own commit: the census derives what
it refuses from the files that stand in a subdirectory, so it refuses
nothing until a phase moves something, and then refuses each citation that
phase missed. The order after that is the order of dependence. `hooks/`
moves before `tests/`, because the module test files name their `TARGET`
under `hooks/lib/` before they move into `tests/hooks/`. The general skills
go last and alone, so an answer to Q2 other than the default replaces one
phase and nothing else.

## Technical context

**Where `hooks/` is read.** `hooks/hooks.json` runs one script,
`hooks/dispatch.py`, for every event, and `dispatch.py#run_gate` loads each
gate of `GROUPS` from `os.path.join(HOOKS, filename)`. Each gate puts its own
directory on `sys.path` and imports by bare name (`import optin`, `import
routing`, `import cmdline_base as cmdline`); `hooks/config.py:61` and
`hooks/routing.py:51` load `blocks.py` from beside themselves. Outside
`hooks/`, scripts join `"..", "..", "..", "hooks"` or `"hooks"` and load a
module by path: `skills/code-review/scripts/chain_check.py:101`,
`skills/implement/scripts/seal.py:120`, `skills/settle/scripts/settle.py:90`
and `:91`, `skills/settle/scripts/fold_check.py:59` and `:60`,
`skills/verify/scripts/broad_gate.py:151` and `:152`,
`skills/verify/scripts/pact_check.py:85`,
`skills/verify/scripts/unverified_check.py:80`,
`.github/scripts/gather_changelog.py:88`, `issue_claims_check.py:87`,
`plugin_directory_check.py:88`, `publish_release_note.py:98`,
`release_seal.py:299`, `rules.py:83` and `:87`, `run_tests.py:92`,
`tracker_labels.py:56`, `evals/scripts/rule_cases.py:42`. `bin/seal` and
`bin/seal.cmd` run `hooks/launch.py`. `tests/conftest.py:331` joins
`HOOKS`, and `load_hook_module` (line 526) and `run_hook` (line 551) take a
file name under it; 20 test files call `load_hook_module` with a module that
moves, 27 calls in all (executed: `git grep -c`).

**Readers that shrink instead of failing.** Three readers derive a set of
files from a directory and do not fail when a file is no longer where they
look. `tests/test_launch.py#loaded_by` (line 312) follows a hook's imports
to files "beside it or in `hooks/`" (line 330); without `hooks/lib` the set
`test_what_runs_before_any_floor_is_linted_at_the_floor` holds to `ruff.toml`
loses every module and the case passes over less. `hooks/dispatch.py#opted_in`
(line 322) loads `optin.py` from `HOOKS` and answers True where it cannot
load it, so a missed path turns the failure report on for every repository
and no case reads it. `evals/scripts/replay_targets.py#CHECK_FILES` (line
184) copies `hooks/blocks.py` from a commit only where the commit holds it,
so a commit after this release copies no `blocks.py` and the check it
replays fails to load its reader. Contract rule 12 applies to the class:
the crafter of phase 2 enumerates it with
`git grep -n -E '"(blocks|cmdline_base|cmdline|config|console|gate|hooksession|implementer|launch|one_heredoc|optin|routing|tokens)\.py"' -- hooks skills .github evals tests bin`
and with every `glob`, `rglob`, `listdir` and `scandir` over `hooks`,
`templates` and `tests`, and names each hit in its phase record.

**Where `templates/` is read.** Three joins in shipped code
(`hooks/root-migrate.py:80`, `skills/implement/scripts/seal.py:1922` and
`:2043`), `install.sh:44`, the `$CLAUDE_PLUGIN_ROOT/templates/` paths in
`skills/config/SKILL.md`, `skills/preset-setup/SKILL.md` and
`skills/implement/orchestration.md`, the messages of
`hooks/routing-edit-gate.py` (lines 80 to 105), and 284 prose lines in 81
files (executed: `git grep -c 'templates/'`, records excluded). Tests join
`"templates", "<file>"` in 40 files, 92 lines.

**Where `tests/` is read.** 858 lines in 197 living files name a
`tests/test_*.py` path, 261 of them on `check:` lines (executed). 134 test
files compute the repository root from `__file__` with one `..`, which is
wrong by one level in every file that moves into a subdirectory.
`.test_durations` keys every case by its node id, 6,778 lines, and
`tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py#test_the_durations_file_prices_the_suite`
fails a full collection whose unpriced share passes `STALE_SHARE`. CI
divides the shards from that file (`.github/workflows/test.yml:105` to
`:108`) and writes a fresh one as the `test-durations` artifact on every
run, `workflow_dispatch` included (`.github/workflows/test.yml:12`).
`.github/workflows/test.yml:238` runs `pytest tests/test_arm_check.py -q`.

**What runs this work's gates.** The hooks and `seal` on PATH are the
installed 0.23.0 plugin's, not the tree's: `hooks/hooks.json` runs
`${CLAUDE_PLUGIN_ROOT}/hooks/dispatch.py`, which is the plugin cache, and
Claude Code puts the cached plugin's `bin/` on PATH. The installed edit gate reads
`seal/threads/<id>/routing.md`, which this work does not move, so it keeps
reading this work item's declaration. The installed `seal layout` does not
know the area rule, so a crafter runs the tree's command by path,
`/Users/michael/Documents/GitHub/SpecSeal/bin/seal layout --check`, and
the same for `seal rules --check`.

**The failure scenario of the chosen approach.** In six months a
contributor adds a module to `hooks/` beside the gates, or a test file at
the top of `tests/`, and nothing refuses the module: the census reads only
spellings, and `seal layout --check` reads only test files. The layout
then decays one file at a time. The test file is refused by the layout
reader this work extends; the module is not, and `CONTRIBUTING.md`
*The test layout* is where a reader learns where it goes. The second risk
is a reader of a moved path that none of the classes above finds: a path
assembled from a variable. The new fresh-interpreter case and the suite's
own runs at the new paths are what catch it, and the Windows shards are the
only run that catches a `/` written where `os.path.join` returns `\`, as
#1051's round 5 found (`4420ebd5:seal/threads/1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by/trail/rounds/round-5.md`).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| `docs/` into subject directories, as #1060 proposes | `skills/settle/scripts/rule_changes.py` refuses a `file` below the top of the policy root, so no spec could change a moved document's rules; `seal fold` reads the top level alone and stops checking it; `docs/README.md` already says a subdirectory is not policy. Keeping it working means widening the grammar and the fold, which changes what the settle accepts in every repository that installs the plugin | Rejected on Q1's default. The premise that keeps `docs/` flat was checked at its three readers |
| `docs/` flat, `docs/README.md` grouped into one table per subject (chosen) | The listing still holds 17 documents side by side, and a reader who lists the directory instead of opening the index meets them unordered | Chosen: the index is the file the fold already holds every document to, and a reader finds a document by subject there |
| `hooks/lib/` reached by a `sys.path` insert in each gate (chosen) | A gate whose insert is missed still loads under `dispatch.py` when an earlier gate in the same process inserted `lib`, and fails alone | Chosen, with the fresh-interpreter case that loads each gate with nothing else on `sys.path` |
| `hooks/lib/` as a package, `from lib import optin` | A module loaded as `lib.optin` by a gate and as `optin` by a script that loads it by path is two copies of one module with two states; every import line changes, not one line per file | Rejected |
| Keep `hooks/` flat | 30 files where 17 register or run the hooks and 13 are read by them, and nothing in the listing says which | Rejected: #1060's decision, and the premise for keeping it (that a reader can tell a gate from a module by name) does not hold: `worktree_consent.py` and `cmdline_base.py` are spelt alike and one is a gate |
| Keep `hooks/cmdline_base.py` at the top as the frozen exception | One module among the gates, kept there by a reason a reader has to find in the freeze case | Rejected: the premise that a move breaks the freeze was checked and is false. The hash covers the bytes from `START` on (`tests/test_the_frozen_reading_never_grows.py#below_the_rider`) |
| `tests/` kept flat | 156 test files side by side; the 65 module test files are found by name, `test_<stem>.py`, and the 91 that declare no `TARGET` are found only by reading the listing | Rejected: #1060's decision, and the cost it names, the 91 files, is real |
| `--import-mode=importlib` | It puts nothing on `sys.path`, so `from conftest import` in 134 files and the helper imports fail at collection | Rejected |
| An `__init__.py` in each test directory | pytest then inserts the first directory above the packages, the repository root, so `from conftest import` fails unless every import becomes `from tests.conftest import` | Rejected |
| Each moved test file edits its `..` to `"..", ".."` | The next move repeats 134 edits, and a depth wrong by one makes a `glob` under the root empty, so a case that loops over it passes over nothing | Rejected: one source, `tests/conftest.py#ROOT`, and a case that refuses a second |
| A stored list of the old paths in the census | A list kept beside the tree, which `CLAUDE.md` *The rule a mechanism is kept against* refuses | Rejected: the census derives the vacated spellings from the files in the subdirectories |
| A census of every backticked path in living text | Placeholders (`<work-item-id>`), globs, past-tense mentions of removed files and paths in other repositories all read as dangling; a reading that noisy is a report, not a gate | Rejected: the census reads exactly the spellings a move vacated, and `seal rules --check` already holds every `check:` target |
| `.test_durations` rewritten key by key with the Edit tool | 156 moved files, one edit each, over a 6,778-line file, and a miss prices a case at the mean without failing | Rejected: CI measures the file on every run and uploads it; the orchestrator commits that artifact, as #1051 committed 3adbe536 |
| `.test_durations` from a local `--store-durations` run | The shards divide by Windows seconds, and a local run on macOS prices every case at the wrong platform's cost | Rejected |
| `templates/records/` holding `design.md` and the rest without `sdd-` | A rename on top of a move: every work item record in every installed repository says it began from `templates/sdd-<name>.md`, and the name in 284 prose lines changes as well as the directory | Rejected: the move keeps each file name |
| The eight general skills moved out to a plugin of their own | A second plugin to version, release and register, for skills no record shows used | Rejected on Q2's default |
| The eight general skills kept | They stay paid for in every session's skill listing with no history of a use | Rejected on Q2's default; the instrument's blind side is stated in Q2 |
| `skills/` split by kind into `skills/workflow/` and `skills/general/` | Claude Code loads `skills/<name>/SKILL.md` one level deep; the split needs the manifest's `skills` key and rewrites every `skills/<name>/` citation | Rejected: after the removal `skills/` holds one kind |

## Verification this work item owes

The owner decided this on 2026-10-27 for #1051 and carried it to this work
item on 2026-10-28. It binds every crafter, proofer and sealer of this work
item, and it overrides any wording in the phase rows below.

- A name or path that moves is proved by the existing cases passing at the
  new path. It owes no new case, no red run and no `seal mutate`.
- A case is written new, and seen red once, only for behaviour that did not
  exist before. The cases this work writes new are listed in the phase rows:
  the census, the fresh-interpreter load, the replay copy at either path,
  the layout's area refusal, the root from `conftest`, and the unique test
  file name. No phase runs `seal mutate`, and no phase owes the move check
  `seal layout --moved`.
- A phase runs, in one `bin/test` command, the cases its row names plus the
  modules `git grep -l` finds reading what it changed. The orchestrator's
  broad run after the review rounds is the only sweep of the suite.
- A proofer does not raise a finding that a moved path lacks red-first
  evidence or a mutation run. A sealer does not withhold over it.
- A phase that moves test files collects them before and after the move,
  with `bin/test <files> --collect-only -q`, and records that the node ids
  are the same set when compared as file name and the rest of the id.
- Each phase record names the cases it wrote new and the existing cases it
  relied on.

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The census `tests/censuses.py#vacated_paths` joined to `CENSUSES`, with cases in `tests/test_censuses.py`; `templates/` moved into `templates/records/` and `templates/setup/` by `git mv`, every reader of a template path at its new path (the three code joins, `install.sh`, the `$CLAUDE_PLUGIN_ROOT` paths, the gate messages and the tests that pin them, and every prose citation); `docs/README.md`'s table grouped into one table per subject, each row unchanged | The census seen red against the template citations after the move and before their sweep, then green; `bin/test tests/test_censuses.py tests/test_root_migrate.py tests/test_seal.py tests/test_first_setup_asks_once.py tests/test_the_installer_writes_the_block_from_its_template.py tests/test_routing_edit_gate.py tests/test_fold_check.py` plus the modules `git grep -l templates` finds; `ls templates` lists `records` and `setup` only | 8fcc543b |
| 2 | `hooks/lib/` holding the 13 modules by `git mv`; each gate's `sys.path` insert, `dispatch.py#opted_in`, the scripts outside `hooks/`, `bin/seal`, `bin/seal.cmd`, `run_tests.py`, `tests/conftest.py#load_hook_module` and its callers, `tests/test_launch.py#loaded_by`, `replay_targets.py#CHECK_FILES` reading both spellings, the freeze case's `FROZEN` and the rider's paths, the `KEPT_FILES` of both censuses, `ruff.toml`'s comment, and every prose citation; each test file's `TARGET` at `hooks/lib/` | New cases, each seen red once: every gate of `dispatch.GROUPS` loads in a fresh interpreter (`tests/test_dispatch.py`); a commit holding `hooks/lib/blocks.py` has it copied (`tests/test_replay_targets.py`); `loaded_by` reaches a module under `hooks/lib/` (`tests/test_launch.py`). Then `bin/test` over the 28 hook module test files, `tests/test_the_frozen_reading_never_grows.py`, `tests/test_chain_hooks_hardening.py`, `tests/test_censuses.py`, `tests/test_replay_targets.py` and the modules `git grep -l` finds loading a moved module; `ls hooks` lists the 17 files *Scope* keeps and `lib` | |
| 3 | The 63 module test files moved into `tests/hooks/`, `tests/skills/`, `tests/github/` and `tests/evals/`, each importing `ROOT` from `tests/conftest.py`; `test_layout.py --check` refusing a module test file outside its area, with `CONTRIBUTING.md` *The test layout* rewritten in place; `.github/workflows/test.yml:238`; every `check:` line and citation of a moved file | New case, seen red once: the area refusal, in the moved `tests/skills/test_test_layout.py`. Then `bin/test tests/hooks tests/skills tests/github tests/evals`; the collection before and after compared; the tree's `bin/seal layout --check` and `bin/seal rules --check` exit 0 | |
| 4 | The 91 files that declare no `TARGET` moved into `tests/behaviour/` and `tests/text/` by the criterion of `frame/design.md` *Data & interfaces*, each importing `ROOT`; the rider of `hooks/lib/cmdline_base.py`, the census constants and every `check:` line and citation of a moved file | New cases in `tests/test_conftest.py`, each seen red once: no file under `tests/` but `conftest.py` computes the root from `__file__` (red at phase 3's commit), and no two test files share a name (red with a planted duplicate in a fixture tree). Then `bin/test tests/behaviour tests/text tests/test_conftest.py tests/test_censuses.py`; the collection before and after compared; the tree's `bin/seal rules --check` exits 0; `ls tests` lists the files *Scope* keeps and the six directories | |
| 5 | The eight general skills removed with `git rm -r`; `README.md` and `README.ko.md` counting fourteen skills, their group lists and the cheat sheet without the two removed commands; `tests/test_chain_hooks_hardening.py`'s count words carrying fourteen; the changelog fragment `changelog.md` of this work item, with a *Removed* entry naming each skill | `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/skills/test_payload_meter.py tests/text/test_every_agent_reads_the_contract.py tests/hooks/test_review_skill_gate.py`; `git grep -n -E 'agentic:(debug|build-fix|checkpoint|gap-analysis|security-audit|testing|learn|audit)\b|skills/(debug|build-fix|checkpoint|gap-analysis|security-audit|testing|learn|audit)/'` matching only records; `claude plugin validate .` exits 0 | |

## Operational impact

- **No installed repository migrates.** What a user's repository holds
  that names a path inside the plugin was read (read 2026-10-28):
  `templates/hygiene.yml`, written as `.github/workflows/hygiene.yml`,
  clones the plugin at the tag it was written against
  (`git clone --depth 1 --branch v<version>`) and runs
  `skills/code-review/scripts/chain_check.py` and
  `skills/implement/scripts/seal.py` from that clone, which this work does
  not move, so a workflow pinned to 0.23.0 runs 0.23.0's tree whole and one
  written by `seal pr-checks install` at 0.23.1 runs 0.23.1's whole. The
  CLAUDE.md block names `skills/implement/orchestration.md`, which does not
  move. `seal/config.md`'s `Broad gate` row is the repository's own
  command. No hook reads a path out of a user's repository that names the
  plugin's layout.
- **Two files in an installed repository cite a plugin path in prose.**
  `seal/README.md`, written from `templates/seal-README.md`, cites
  `hooks/optin.py#MARKER`, and the comment `seal mode` writes at the top of
  `seal/config.md` (`skills/implement/scripts/seal.py#NEW_CONFIG`) cites
  `templates/config.md`. A repository set up before 0.23.1 keeps those
  spellings. Nothing reads either sentence, the marker line is the README's
  first line and does not change, and a reader who opens the cited path in
  the plugin finds the file one directory down. This is a limit, stated
  here and in the changelog fragment, and no migration rewrites them.
- **Two commands a person types stop existing.** `/agentic:security-audit`
  and `/agentic:testing` are removed with their skills, and a repository's
  `.claude/audit-rules/*.md` has no skill reading it. The changelog
  fragment's *Removed* entry says so, under Q2's default.
- **`.test_durations` is refreshed by the orchestrator after phase 4 and
  before the review rounds.** The orchestrator pushes the branch, runs
  `gh workflow run tests --ref chore/1060-each-directory-holds-everything-in-one-level`,
  downloads that run's `test-durations` artifact over `.test_durations`,
  checks that `durations_union.py` wrote it from four parts, and commits it.
  Until then a full collection fails
  `test_the_durations_file_prices_the_suite`, which skips in every narrow
  run. The same run's Windows shards are the answerer of every path
  separator this work spells, and the orchestrator compares that run's
  collection with the base's, by file name and the rest of the id, for the
  whole suite.
- **The 0.23.1 release report lists each moved test file twice**: under its
  old path with cases at the tag and none now, and under its new path with
  none at the tag. `.github/scripts/release_report.py` reads
  `.test_durations` in both trees and fails nothing. This is a limit of the
  one release that moves the files.
- **This run's gates are the installed 0.23.0 plugin's.** Nothing this work
  moves is read by them from the tree. A crafter runs the tree's
  `bin/seal` by its absolute path for `layout` and `rules`, because `seal`
  on PATH is the installed one.
- No new dependency, no new environment variable, and no gate decides
  anything differently.
