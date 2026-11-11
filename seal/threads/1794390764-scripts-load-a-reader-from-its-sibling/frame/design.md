# Design: 1794390764-scripts-load-a-reader-from-its-sibling (#1482)

## Grounding

The tree as read at `333fb9def`, which is `origin/release/v0.37.4`
(`1a01c761a`) plus this work item's `routing.md`.

Each row is labelled `executed` where this framer ran the command that gave
it, and `read` where it opened the coordinate. The probes that run the
repository's code ran in a `git clone --no-local` of this branch under
`<scratchpad>/1794390764-scripts-load-a-reader-from-its-sibling/frame/`.
"A script" below is a tracked `.py` file under `skills/*/scripts/`,
`.github/scripts/`, `evals/scripts/` or `hooks/`. "A loader form" is a call
of `importlib.util.spec_from_file_location`, or a `sys.path.insert` followed
by a plain `import`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A fact has one source, and every other place links to it." How a script reaches another module, and what it says when the module is absent, are each one fact written in many files. The same rule says "before a fix adapts to an existing structure, ask whether the structure should change", so the frame weighs replacing the by-path loaders, not only adding a cache to each. |
| G2. `skills/core/SKILL.md` *The first value*, the paragraph *A document is cut by who opens it and at which step* (read) | A module is cut the same way. The scripts of G8 load the 1,459 lines of `unverified_check.py`. Most want a markdown reader that is about a third of the file, and two want predicates only they call (G9). |
| G3. Issue #1482 (executed: `gh issue view 1482 --json title,body,comments`) | No comments. *Change* asks for three things: the markdown readers move to `lib/blocks.py` or a new module under `lib/`, one loading mechanism executes each module once per process, and the exit-2 message for a missing sibling is written in one place. *Done when* asks that no script loads `unverified_check.py` except its own tests, that one `seal settle` executes each module once, and that `def load` or `_load` is defined in one place. It names one loss: the per-file wording of the message a script copied alone prints. |
| G4. `routing.md` of this work item (read) | Planning is `framer`, the review goes through the chain, and the destination is a pull request. The spawn prompt carried no line on the issue's comments; `gh` reads the issue here, and it has none. |
| G5. The loader forms at this base (executed: `git grep -c spec_from_file_location -- '*.py' ':!tests'`, the same for `sys.path.insert`, and `git grep -nE '^\s*def _?load\(' -- '*.py' ':!tests'`) | `spec_from_file_location` stands 34 times in 23 files outside `tests/`, and `sys.path.insert` 21 times in 16. Their union is the 34 files of *Scope* item 3 and *Out of scope*. Twelve functions are named `load` or `_load`; eleven load a module and `session_cost.py#load` reads a transcript. The issue counted 36 in 22 and thirteen before #1481 merged. |
| G6. What one `seal settle` executes at this base (executed: `test_tmp_count.py`, which counts `SourceFileLoader.exec_module` by file while `settle.py` runs as `__main__` in the clone) | The default run executes 165 modules from 9 files: `lib/blocks.py` 32 times, `unverified_check.py` 31, `lib/fields.py` 31, `rule_changes.py` 30, `lib/tables.py` 29, `lib/gitcmd.py` 7, `lib/optin.py` 3, `lib/config.py` 1 and `lib/routing.py` 1. With `--all-earlier` it executes 760 from the same files, 151 at most for one. The issue's 1,075 was taken before #1481 bounded the default run. |
| G7. One table of loaded modules, tried (executed: `test_tmp_once.py`, which answers every by-path load from one table keyed by the file and registered in `sys.modules` under the file's stem, then runs the same two commands) | Each file of G6 executes once. The output is byte-identical to G6's run, for the default run (108,756 B) and for `--all-earlier` (308,213 B), by `cmp`. So the modules a settle loads hold no state that one shared instance changes. |
| G8. What each script reads from `unverified_check.py` (executed: `test_tmp_uses.py` and a `grep -oE` of each script's reader variable; read: each call site's loader) | Ten scripts load it by path: `fold_check.py`, `rule_changes.py`, `passages.py`, `settle.py`, `chain_check.py`, `coordinates.py`, `payload_meter.py`, `issue_claims_check.py`, `rules.py`, and `publish_release_note.py` through a `sys.path` import. `pr_body.py` reads it through `chain_check.py#SHARED_READER`. Seven read line readers alone (`gfm_lines`, `heading_level`, `live_lines`, `live_pieces`, `split_row`, `is_separator`, `fence_opener`, `fence_closes`). `rule_changes.py` also reads the item grammar (`items`, `field_values`, `nothing_block`, `unread_block`, `NOTHING`) and `COMMENT_LINE`. `settle.py` reads `check_text`, `open_record_rows`, `OVERVIEW`, `NOTHING`, `policy_root` and `show`. `chain_check.py` reads `settled`, `merge_base`, `resolves`, `repo_root`, `policy_root`, `rule_changes`, `annotate`, `headings`, `readable` and `split_row`. `pr_body.py` reads `HEADING`, `sections`, `readable` and `gfm_lines`. |
| G9. Units `unverified_check.py` defines and never calls (executed: `grep -cE "\b<name>\("` over the file, a count of 1 being the definition alone) | `settled`, `merge_base`, `resolves`, `rule_changes`, `show` and `open_record_rows`. `commit_of` is called by `resolves` alone and `tree_at` by `settled` alone. The first four have one reader, `chain_check.py`; `show` and `open_record_rows` have one, `settle.py`. `fence_opener`, `fence_closes` and `gfm_lines` are `lib/blocks.py`'s, and `COMMENT_LINE` is `lib/fields.py`'s; the file re-exports them (`:101-107`, `:161`). |
| G10. What each script does when copied alone (executed: `test_tmp_alone.py`, which copies each of the 38 scripts into an empty directory and runs it with no argument; its output is `<scratchpad>/1794390764-scripts-load-a-reader-from-its-sibling/frame/alone.tsv`) | Eight exit 2 with no traceback because a sibling is absent: `seal.py`, `settle.py`, `fold_check.py`, `pact_check.py` and `payload_meter.py` in a sentence that holds "is not a plugin", and `chain_check.py`, `pr_body.py` and `broad_gate.py` in wording of their own. Sixteen die in a traceback at exit 1. Fourteen of those lack a module: eleven under `.github/scripts/`, `evals/scripts/rule_cases.py`, `seal_stamp.py` and `unverified_check.py`. Two have another cause: `roll_flow_measurement_issue.py` an unset `REPO`, and `agentic_pytest_record.py` an absent `pytest`. The remaining fourteen reach no load with no argument: `rules.py`, `release_report.py` and `session_cost.py` among those that exit 2 on their usage, `release_seal.py`, `core-start.py`, `passages.py`, `rule_changes.py` and `coordinates.py` among those that exit 0, and `deferral_check.py` at exit 1 with no traceback. |
| G11. The two hooks (read: `hooks/hooks.json`, `hooks/core-start.py:49-66`; executed: `seal_stamp.py --stop` copied alone) | Each hook command ends `\|\| exit 0`, so a non-zero exit of the script does not reach the session. `core-start.py` catches `BaseException` and exits 0. `seal_stamp.py --stop` copied alone exits 1 in a traceback today. |
| G12. The walk that derives what runs before any floor is checked (read: `tests/behaviour/test_every_entry_point_runs_at_the_floor.py#loaded_by`, `:203-235`; `ruff.toml:43-57`) | It follows a plain `import` beside the script or into `lib/`, a bare `"<name>.py"` constant, and an `os.path.join` whose last string ends in `.py`. It does not read a `/`-joined path handed to a function, so a load spelt a new way shrinks the set without failing unless the walk gains that spelling. `ruff.toml` lints `lib/*.py` at the floor as a whole. |
| G13. The test layout (read: `skills/verify/scripts/test_layout.py:1-60`, `CONTRIBUTING.md` *The test layout*) | A test file declares one `TARGET` and holds one class `Test_<name>` per public top-level function of it; a class naming no definition of its `TARGET` is refused. So a unit that moves takes its class to the test file of its new module, and `seal layout --moved` is the check that the cases were only moved. `tests/skills/test_unverified_check.py` is 2,247 lines. |
| G14. How `lib/` and `seal.py` load today (read: `lib/fields.py:54-60`, `lib/routing.py:40-46`, `lib/tables.py:26-35`, `lib/core.py:31`, `skills/implement/scripts/seal.py:180-225`) | A `lib/` module puts its own directory on `sys.path` and imports its neighbour by a plain name, so `sys.modules` already holds `blocks`, `optin`, `config`, `tables` and `gitcmd` under their stems in most processes. A by-path load of the same file under another name executes it again; G6's 32 runs of `blocks.py` are that. `seal.py#refuse_without_lib` exists because a plain import of an absent `lib/` module is a traceback (#610). |
| G15. Callers whose contract says what a failed load means (read: `skills/verify/scripts/broad_gate.py:198-216`, `.github/scripts/release_seal.py:85-99` and `:609`, `skills/code-review/scripts/chain_check.py:279-292`, `.github/scripts/rules.py:135-154`, `.github/scripts/release_report.py:87-101`) | `broad_gate.py#load` turns any exception a sibling raises while it executes into `Refused` (#869) and lets a `SystemExit` keep its exit. `release_seal.py` exits 0 always and catches `(Exception, SystemExit)` in `main`. `chain_check.py` exits 2 as a command where a reader will not load and re-raises when imported. `rules.py` and `release_report.py` raise their own `Unreadable`. These differ on a module that raises; on a file that is absent each prints a sentence of its own. |
| G16. The stems of the tracked modules (executed: `git ls-files '*.py' ':!tests' ':!evals/behaviour' \| xargs -n1 basename \| sort \| uniq -d`, and the same stems looked for under `tests/`) | No two tracked modules outside `tests/` share a file name, and no file under `tests/` carries one of their names. A file's stem can name it in `sys.modules`. |
| G17. Whether the tree already holds a shared loader (read: every site of G5) | It does not. Four files cache their own loads: `rules.py#sibling` in `_loaded`, `release_seal.py#_module` and `coordinates.py#shared_reader` under `functools.cache`, and `fold_check.py` in `_loaded`. `session_cost.py#lib_module` is the nearest to the mechanism chosen: it puts `lib/` on `sys.path` once and calls `importlib.import_module`. None is reached by another script. |
| G18. The policy root (read: `docs/checks/the-fold.md` *The fold, and what tells it from a deletion* `:20`, `:115`, `:135`; `docs/running/the-review-and-parity-arms.md` *The declaration, and where the check went* `:87`; `docs/layout/the-record-layout.md` *seal/threads/<work-item-id>/* `:147`; executed: `git grep -n unverified_check -- docs`, and `grep` for the three `file:` values over every `seal/threads/*/frame/design.md`) | Five sentences name a unit this work moves by `unverified_check.py`. `docs/README.md:59` and `docs/checks/the-unverified-record.md:3` name the script as the command, which stays true. `1794289596` and `1794289597` change other sentences of two of these sections, and no unsettled operation quotes the five. No policy sentence states how a script loads a module. The subject of this work is the code, so the five are stated in *Rule changes* and `docs/` is not edited. |
| G19. `docs/README.md`, the index (read) | Each `file:` below is picked from it. None of the documents named there has a `.ko.md` edition. |
| G20. `lib/console.py:1-68` (read) | Its docstring states how each entry point reaches `lib/` and names the scripts that "load them by path, directly or through a sibling script". That paragraph stands on the fact this work changes. `tests/censuses.py#entry_point` holds each entry point's first `__main__` block to it. |
| G21. `seal/follow-up.md`, the `### Process changes` table of v0.37.3 and of the fragments under `seal/threads/` (read; executed: `gh release view --json body`) | No follow-up row waits on this work, and no process change concerns how a script loads a module. |
| G22. #1481's frame (read: `seal/threads/1794383423-settle-reprints-every-earlier-judgment/frame/design.md:110-112`) | It left "`load` keeping no module between calls" to #1482 and did not change `settle.py#load`. |
| G23. The rule changes below (executed: `rule_changes.py#parse` on this file and `#apply_op` of each operation against the clone's `docs/`) | The section parses with no error. Each `change` operation is placed, so each `from` stands in its section at `333fb9def`. |

## Scope

In:

1. **`lib/sibling.py` is the one loader.** Its `load(rel)` takes a module's
   `/`-joined path under the plugin root and returns the module, executed
   once per process. *Data & interfaces* fixes what it does with an absent
   file, a module that raises and a stem another file holds.
2. **A script reaches `lib/sibling.py` by one stanza**, and reaches every
   other module, a `lib/` one included, through `load`. The stanza puts
   `lib/` first on `sys.path` and imports `sibling`. It stands where the
   script's first load stands at this base: at import where the script
   loads at import, and inside the function where it loads on first use, so
   a script that reaches no load with no argument still reaches none
   (G10). In the commands G10 names as exiting 2 for an absent sibling,
   the stanza is guarded: where `lib/sibling.py` is absent it prints the loader's
   sentence about that file and exits 2.
3. **The loader forms of 29 scripts go.** They are every file of G5's
   union but those of *Out of scope* item 2: under `skills/`,
   `chain_check.py`, `pr_body.py`, `seal.py`, `fold_check.py`,
   `passages.py`, `rule_changes.py`, `settle.py`, `broad_gate.py`,
   `coordinates.py`, `pact_check.py`, `payload_meter.py`, `seal_stamp.py`,
   `session_cost.py` and `unverified_check.py`; under `.github/scripts/`,
   `close_issues_on_release.py`, `dist_branch.py`, `finding_counts.py`,
   `issue_claims_check.py`, `label_merged_on_release_branch.py`,
   `plugin_directory_check.py`, `publish_release_note.py`,
   `release_completeness_check.py`, `release_report.py`, `release_seal.py`,
   `rules.py`, `run_tests.py`, `tag_release.py` and `tracker_labels.py`;
   and `evals/scripts/rule_cases.py`. A load that is lazy at this base
   stays lazy. The per-file tables and sentences that say what a missing
   file is for go with the loaders (*Removes*).
4. **A caller keeps its own contract for a module that raises** (G15).
   `broad_gate.py` still refuses with the sibling's own sentence (#869),
   `release_seal.py` still exits 0, `chain_check.py` and `pr_body.py` still
   exit 2 as commands and raise when imported, and `rules.py` and
   `release_report.py` still end in their `Unreadable`. Each catches at its
   call what it caught in its loader. None words an absent file itself.
5. **`lib/lines.py` holds the markdown line readers**, moved from
   `unverified_check.py`: `split_row`, `is_separator`, `visible`,
   `fence_spans`, `closed_fence_lines`, `blank_fences`, `comment_lines`,
   `liveness`, `live_pieces`, `_scan`, `heading_level`,
   `_paragraph_ends_at`, `_partner_ahead`, `live_lines`, `readable`,
   `headings` and `sections`, with the constants they alone read
   (`INVISIBLE`, `SEPARATOR`, `OPENER`, `CLOSER`, `BACKTICKS`). It imports
   `lib/blocks.py` as its neighbours do.
6. **`lib/items.py` holds the item grammar** of
   `skills/settle/rule-changes.md` *Rule changes*: `items`, `field_values`,
   `opens_the_block`, `unread_block`, `nothing_block` and their constants
   (`ITEM_RE`, `FIELD_RE`, `CONTINUED`, `NOTHING`, `WHY`,
   `NOTHING_WRITTEN`, `NEAR_NOTHING`, `UNREAD_BLOCK`).
7. **`lib/gaps.py` holds the reader of a closing memo's
   `## Not verified`**: `check_text`, `check_file`, `parse_section`,
   `closing_word`, `is_header`, `open_record_rows`, `_LooseHeading`, and
   the constants `OVERVIEW`, `HEADING`, `HEADER`, `CLOSED`, `OLD_MARK`,
   `FOUND_PROSE`, `PLACEHOLDER` and `LOOSE_HEADING`. It imports
   `lib/lines.py`, `lib/items.py` and `lib/fields.py`.
8. **A unit with one reader moves to that reader, and the rest to the
   `lib/` module that owns its kind** (G9). `settled`, `tree_at`,
   `merge_base`, `resolves` and `commit_of` move to `chain_check.py`.
   `show` moves to `settle.py`. `unverified_check.py#rule_changes` goes,
   and `chain_check.py` loads `rule_changes.py` through the loader.
   `annotate` moves to `lib/console.py` and `git_path` to `lib/gitcmd.py`.
   `chain_check.py` asks `lib/optin.py#repo_root` for the repository, and
   it and `settle.py` ask `lib/config.py#policy_root` of the root
   `lib/optin.py#home_at` gives.
9. **Every reader asks the home of what it reads.** The scripts of G8 load
   `lib/lines.py`, `lib/items.py` or `lib/gaps.py`, ask `lib/blocks.py` for
   `gfm_lines`, `fence_opener` and `fence_closes`, and ask `lib/fields.py`
   for `COMMENT_LINE`. `unverified_check.py` keeps the command: `main`, the
   walk (`overviews`, `reference_rule`, `references_at`, `config_at`), the
   path helpers it prints with, and the three root states. It keeps no
   name it does not use itself.
10. **The tests follow the units.** Each `Test_<name>` class of a moved
    unit moves to the test file of its new module, new files among them
    (`tests/lib/test_sibling.py`, `test_lines.py`, `test_items.py`,
    `test_gaps.py`), with its cases unchanged but for the module they
    call. A test file that loads `unverified_check.py` for a moved name
    loads the name's home. The cases that pin a per-file purpose or a
    removed loader go or are rewritten against `lib/sibling.py`
    (*Removes*). `loaded_by` (G12) reads a `sibling.load("<rel>")` call,
    and `ruff.toml`'s table follows what the walk then derives.
11. **Every sentence that stands on a moved fact is rewritten in place**,
    in the commit that moves it: the docstrings and comments that cite a
    moved unit as `unverified_check.py#<name>` or say a module is loaded
    by path, `lib/console.py`'s paragraph (G20), and any such sentence of
    `CONTRIBUTING.md`, the READMEs and `skills/`. The list is built with
    `git grep` on each moved name and on `by path`, and the hand-back
    calls it a sample where it is one.
12. **`changelog.md`** states what a user sees change: the one sentence a
    command copied alone prints.

Out of scope:

1. **The duplicate helpers the issue lists** (`git` in seven files,
   `plural` in six, `under` in four, `plugin_version` and `round_records`
   in two). The issue's *Change* and *Done when* name none of them, and
   merging them changes call sites this work does not otherwise open.
2. **The five files that keep the base form**: `lib/core.py`,
   `lib/fields.py`, `lib/routing.py`, `lib/tables.py` and
   `hooks/core-start.py`. A `lib/` module finds its neighbour by its own
   directory, which is the form the stanza itself is, and `load` finds the
   module they imported (*Data & interfaces*). The hook loads one `lib/`
   module and must pass in silence where it is absent (G11).
3. **The tests' own loaders** (`tests/conftest.py#load`, `#load_module`,
   `#load_lib_module`, and each test file's by-path load of its `TARGET`).
   A test loads the unit under test under a name of its own on purpose,
   and #1488 and #1489 own the shape of the test files.
4. **`session_cost.py#load`**, which reads a transcript and loads no
   module. It keeps its name.
5. **Removing `closed_fence_lines`**, which only tests call. #1484 owns
   it and finds it in `lib/lines.py`.
6. **The history sentences in the docstrings this work moves.** #1485
   owns them; a moved docstring moves as it reads.
7. **`lib/optin.py`'s rider on resolving the root again** (`:85`). This
   work does not open that file.
8. **The policy root.** The sentences of G18 are stated in *Rule
   changes* for the settle.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. One settle executes each module once | Given this repository's clone. When `settle.py` runs as `__main__`, with no argument and with `--all-earlier`. Then no file is executed more than once, and stdout is byte-identical to the run at `333fb9def`. | A count of `SourceFileLoader.exec_module` by file over the run, as G6 took it, and `cmp` of the two outputs. |
| S2. No script loads `unverified_check.py` | Given the tree at HEAD. When each hit of `git grep -n unverified_check -- '*.py'` outside the script and `tests/skills/test_unverified_check.py` is read. Then each is the `unverified` row of `seal.py#TOOLS`, an argv that runs the command, or a sentence naming a unit the script keeps. | The `git grep`, read line by line by the proofer; and S1's count holds no run of `unverified_check.py`. |
| S3. One function loads a module | Given the tree at HEAD. When `git grep -n spec_from_file_location -- '*.py' ':!tests'` runs. Then every hit is in `lib/sibling.py`. And `git grep -nE '^\s*def _?load\('` over the same files prints `lib/sibling.py#load` and `session_cost.py#load` alone. | The two commands. |
| S4. A command copied alone says one sentence | Given a guarded command of *Scope* item 2 copied into an empty directory. When it runs with no argument. Then it exits 2, stderr holds no traceback, and stderr holds the sentence of *Data & interfaces* naming the absent `lib/sibling.py` by its path. | A case per command that copies it and runs it, as `test_a_script_copied_alone_exits_2_and_names_what_it_misses` does today. |
| S5. An absent sibling of a whole command says the same sentence | Given a script that has `lib/sibling.py` and lacks a module it loads. When it reaches the load. Then the process exits 2 and stderr holds the same sentence naming that module's path, whichever script asked. | `tests/lib/test_sibling.py`, a `test_refuses_` case on `load`. |
| S6. Every other script does alone what it did | Given each script of G10 that *Scope* item 2 does not guard. When it is copied alone and run with no argument. Then its exit code is G10's, and it ends in a traceback only where G10's row does. | The copy-and-run of G10 repeated at HEAD, row against row. |
| S7. A caller's contract for a module that raises holds | Given a sibling that raises while it executes. When `broad_gate.py`, `release_seal.py`, `rules.py` or `release_report.py` loads it. Then each ends as *Scope* item 4 says. | The cases that hold each today, in `tests/skills/test_broad_gate.py`, `tests/github/test_release_seal.py`, `tests/github/test_rules.py` and `tests/github/test_release_report.py`, passing with only the loader's name changed. |
| S8. The moved cases were only moved | Given the test classes of *Scope* item 10. When `seal layout --moved` compares the old file with the new ones. Then it passes, and `seal layout --check` refuses none of the files this work writes. | The two commands, by the crafter in the phase that moves them. |
| S9. The floor walk still sees every load | Given a script whose only load is `sibling.load("<rel>")`. When `loaded_by` reads it. Then it returns that tracked path, and the set `ruff.toml` lints at the floor is no smaller than at `333fb9def` but for files this work removes from it by name. | A case beside `test_a_script_reaches_the_modules_under_lib`, and that file's cases passing. |

## Data & interfaces

**`lib/sibling.py#load(rel)`.** `rel` is a module's path under the plugin
root, joined with `/`, such as `"lib/optin.py"` or
`"skills/settle/scripts/rule_changes.py"`. The plugin root is the directory
that holds `lib/`. The module's name in `sys.modules` is its file's stem
(G16).

- Where `sys.modules` holds that stem and the module there is this file,
  `load` returns it. That is how a module `lib/` imported by a plain name
  and a module a script loaded are one instance (G14).
- Otherwise it executes the file under its stem, registers it, and returns
  it. A module that raises while it executes is not left in `sys.modules`,
  and its exception reaches the caller unchanged.
- Where the file is absent, it writes one sentence to stderr and raises
  `SystemExit(2)`. A string argument to `SystemExit` exits 1, so the code
  is the integer (#590).
- Where another file holds the stem, it raises `ImportError` naming both
  files. It replaces nothing.

**The sentence**, the one spelling of what an absent module is called:

```
cannot read <path>, which this command loads. It ships in the plugin beside this script; a copy of one script taken on its own is not a plugin. Nothing was read.
```

`<path>` is the absent file's absolute path. The sentence names no command
and no purpose. It is a constant of `lib/sibling.py`. The guard of *Scope*
item 2 spells the same words about `lib/sibling.py`, because it runs where
that constant cannot be read; S4 holds each guarded command to it.

**The stanza**, in a script three directories below the root:

```python
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "lib"))
import sibling
```

**No schema, endpoint or record form changes.** No command gains or loses
an argument. The exit codes of every command are unchanged; what changes
for a person is the wording of the sentence a copied command prints, and
that `chain_check.py`, `pr_body.py` and `broad_gate.py` print it where they
printed their own.

## Rule changes

- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `chain-check` asks one predicate, `unverified_check.py#settled`.
  to: `chain-check` asks one predicate, `chain_check.py#settled`.
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `unverified_check.py#live_lines` parks a line inside any fence or comment,
  to: `lib/lines.py#live_lines` parks a line inside any fence or comment,
- change
  file: docs/checks/the-fold.md
  section: The fold, and what tells it from a deletion
  from: `unverified_check.py#readable` blanks fenced lines with the indices
  to: `lib/lines.py#readable` blanks fenced lines with the indices
- change
  file: docs/running/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: is gone is asked `unverified_check.py#settled` at the merge base, the
  to: is gone is asked `chain_check.py#settled` at the merge base, the
- change
  file: docs/layout/the-record-layout.md
  section: seal/threads/<work-item-id>/
  from: `unverified_check.py` in a `gaps.md`, and `rule_changes.py` in a
  to: `lib/gaps.py` in a `gaps.md`, and `rule_changes.py` in a

## Removes

This work adds one module that scripts load and no gate, check, hook or
mark. What it takes out:

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The module loaders named `load` or `_load` (G5) | `settle.py#load`, `fold_check.py#load`, `chain_check.py#load`, `pr_body.py#_load`, `broad_gate.py#load`, `pact_check.py#load`, `finding_counts.py#load`, `label_merged_on_release_branch.py#_load`, `release_completeness_check.py#_load`, `tracker_labels.py#_load`, `rule_cases.py#load` | `lib/sibling.py#load`. `broad_gate.py` keeps its conversion to `Refused` at its calls (*Scope* item 4). |
| The other by-path loading code | `release_report.py#script`, `release_seal.py#_module`, `rules.py#sibling`'s loading half and `_loaded`, `issue_claims_check.py#load_reader`, `unverified_check.py#_load_lib` and the loop in `#config_at`, the four getters' bodies in `rule_changes.py:87-125`, `passages.py:44-48`, `coordinates.py#shared_reader`, the three loaders in `payload_meter.py:138-219`, `seal_stamp.py#_gitcmd`, `#_chain_check` and `#_optin`, `session_cost.py#lib_module`'s `sys.path` half, `run_tests.py:82-90`, `publish_release_note.py:120-136` | `lib/sibling.py#load`, called where each stood. A getter that only names its module may stay as one line. |
| The per-file sentences and tables saying what a missing file is for | `settle.py#PURPOSES`, `seal.py#LIB_PURPOSES` and `#refuse_without_lib`, the `purpose` argument of `fold_check.py#load` and its three call sites, the purposes in `rules.py#SIBLINGS`, the `purpose` argument of `release_report.py#script`, the three sentences in `payload_meter.py:151-214`, the sentence in `pact_check.py:270-275`, `chain_check.py:290-292`'s line for an absent reader, and the like line in `pr_body.py` | The one sentence of `lib/sibling.py`. The purposes go, which is the loss the issue names. |
| The markdown line readers, the item grammar and the `## Not verified` reader | `unverified_check.py:194-648`, `:650-730`, and `:732-918` with `#open_record_rows` | `lib/lines.py`, `lib/items.py` and `lib/gaps.py` (*Scope* items 5 to 7). |
| The units of G9 with one reader elsewhere | `unverified_check.py#settled`, `#tree_at`, `#merge_base`, `#resolves`, `#commit_of`, `#show` | `chain_check.py`, and `settle.py` for `show` (*Scope* item 8). |
| A loader that exists for one caller | `unverified_check.py#rule_changes` | Nothing owns it. `chain_check.py` loads `rule_changes.py` itself. |
| Two helpers both commands print with | `unverified_check.py#annotate`, `#git_path` | `lib/console.py#annotate` and `lib/gitcmd.py#git_path`. |
| The re-exports of names another module owns | `unverified_check.py:101-107` (`fence_opener`, `fence_closes`, `GFM_LINE_RE`, `gfm_lines`) and `:161` (`COMMENT_LINE`), where the script no longer reads them itself | `lib/blocks.py` and `lib/fields.py`, asked directly (*Scope* item 9). |
| The cases that pin a per-file purpose or a script's own loader | `tests/skills/test_settle.py::test_each_sibling_is_refused_with_its_own_purpose` and `::test_a_missing_sibling_reader_is_a_sentence_and_not_a_traceback`; the purpose phrase in each `test_a_script_copied_alone_exits_2_and_names_what_it_misses`; `tests/github/test_rules.py#Test_sibling`; the `load` cases of `tests/skills/test_broad_gate.py` and `tests/skills/test_pact_check.py` that test loading and not the caller's contract; the case in `tests/skills/test_chain_check.py#Test_module` that refuses a second `settled` | `tests/lib/test_sibling.py` holds the refusal and the one execution. The copied-alone cases stay, pinning S4's sentence. The `settled` case goes because the predicate now stands in its one reader. |

Framed 2026-11-11 by framer, before the build.
