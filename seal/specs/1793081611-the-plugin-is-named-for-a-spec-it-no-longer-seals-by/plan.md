# Implementation Plan: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

Approved 2026-10-27 by the orchestrator under the owner's automation answer, when `smith` was spawned for phase 1.

## Summary

Five phases, each a fresh crafter, each leaving the tree green under the
installed 0.22.4 gates and its own narrow tests. The order is the order of
dependence: the marker and the removed arm change what a root is; the
thread layout changes where every record is; the names change what every
text says; the command line changes what every document tells a person to
type; the census proves the sweep and is seen red before it. This work
item's own directory moves to `seal/threads/` in phase 2, and from that
commit on the installed edit gate meets no declaration, which *Operational
impact* below answers.

## Technical context

`hooks/optin.py#home_at` (line 179) is the one reader of whether a `seal/`
is the root: it reads two places in order and answers the first directory
that exists. `WORK_ITEMS = "specs"` (line 41) is joined under it by every
hook that opens a file, and `hooks/routing.py#WORK_ITEMS` (line 121) spells
`seal/specs` for the readers that classify repository-relative paths:
`chain_check.py` (lines 1622 to 1628, 1985, 2031, 2180), `seal.py#work_item_of`
(line 389), `hooks/routing-edit-gate.py` (line 218). The 28 files
`git grep -l seal/specs -- hooks skills .github templates` lists spell the
path in prose, globs or constants (executed 2026-10-27 at `bac5dcdd`).

`hooks/root-migrate.py` (581 lines) moves an old layout at session start
and keeps six boundaries, each pinned in `tests/test_root_migrate.py`. Its
`moves` (line 300) lists units, `run_moves` (line 425) performs staged
`git mv`, `rewrite_readme` (line 408) overwrites `seal/README.md` from the
template, `stamp` (line 125) writes the once-per-repository marker, and
`main` (line 464) refuses a dirty tree, a symbolic link and a throwaway
marker. Every one of those mechanisms serves the new move unchanged; only
the units and the two constants naming the old roots change.

`skills/implement/scripts/seal.py#main` (line 2704 and after) is an
`argparse` dispatcher with five subparsers (`export`, `import`, `mode`,
`pr-checks`, `no-work-item`). Each `bin/` wrapper is two lines running one
script through `hooks/launch.py` (the interpreter floor); `bin/test` is the
exception that runs `.github/scripts/run_tests.py` directly, because that
script builds the interpreter the floor wants.

`chain_check.py#TRAILER` (line 2054) and `trailers()` (line 2074) read the
trailer through `git log --format=%(trailers:key=...)`, one key.
`hooks/implementer.py#AGENT_MARKS` (line 57) and `mark_for` (line 122)
recognise `framer` and `smith` with or without the `specseal:` prefix.
`hooks/review-skill-gate.py#OURS` (line 42) spells `specseal:code-review`.
`hooks/stub-remove.py#MARKER` (line 38) reads `# specseal-git-hook` in
stubs earlier releases wrote. `install.sh` lines 45 and 46 and
`uninstall.sh` lines 15 and 16 hold the CLAUDE.md block markers.

`tests/censuses.py` holds one census per rule every tracked file keeps,
`<name>(rel, root)` returning one line per problem, with exemptions as a
comment line `# exempt from <name>: <why>` directly above the line; the
markdown censuses (`section_sign`, `real_identifiers`) read `.md` files
through the same `_held`. `tests/test_censuses.py` runs every census over
every tracked file no module declares as its `TARGET`.

The hooks this run executes are the installed 0.22.4 plugin under
`~/.claude/plugins/cache/specseal/`, not the tree: the edit gate reads
`seal/specs/<id>/routing.md`, the implementer mark recognises `smith`, and
`bin/` on PATH is the installed plugin's. CI's hygiene workflow for this
repository runs `skills/code-review/scripts/chain_check.py` from the tree
(`.github/workflows/hygiene.yml:162`), so the pull request is judged by the
new reader.

**The failure scenario of the chosen approach.** In six months a reader
meets three spellings kept on purpose (the old trailer key, the stub
marker, the old CLAUDE.md block markers) and cannot tell them from a miss,
unless each is labelled at its constant with the release that removes it.
The census carries that label as the exemption's reason, and 0.24.0's
frame removes the trailer reading. The other risk is a path reader the
sweep did not find: `seal/specs` spelt through a variable or a glob the
grep does not match. The end-to-end migration case and this repository's
own run on the new layout are what catch that, because every reader runs
over `seal/threads/` here before the release.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep `hooks/root-migrate.py` and change its units (chosen) | Its boundaries were built for a move between repository roots; a boundary that reads `.specseal/` by name, such as the symbolic-link refusal, has to be re-pointed at `seal/specs/`, and one missed keeps refusing on a path nothing holds | Keep: the premise that keeps it, that every boundary is a property of a staged `git mv` and not of the old names, was checked in `main` (line 464): `dirty`, `git_mv`, `taken`, `move`, `run_moves`, `stamp` take paths as arguments and name no old root |
| Replace `root-migrate.py` with a new `layout-migrate.py` and delete the old file | Two session-start hooks, one of which reads a top-level `specs/` that #1051 says nothing may read, until the old one is deleted; deleting it loses the six pinned boundaries and their cases, which the new file re-earns one by one | Rejected: the structure is the boundaries, not the names, and the file's own rider says it leaves when nothing is left to migrate, which is not yet |
| A marker file beside `README.md`, such as `seal/.agentic` | A second file to create, export, import and explain; `seal export` walks the root and a dotfile is what a person deletes; the README already exists in every root and is plugin-owned | Rejected: the README's first line is one file the plugin already writes at first setup and overwrites at migration |
| The marker as an HTML comment on the README's first line | A comment is syntax a reader can trip on, and `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading* refuses a symbol as syntax where a word does; a person reading the file sees a line that says nothing | Rejected: the heading line names the plugin and the directory, and a heading is what a person reads first anyway |
| Keep one `bin/` wrapper per tool and add `seal <subcommand>` beside them | Two spellings of one command in every document, and the census has to allow the old one | Rejected by #1051: one command, one subcommand per tool |
| Read both layouts (`seal/specs/` and `seal/threads/`) for 0.23.x, like the trailer | A second reading of where a record is, in every reader, for one release; this repository's own run would not exercise the new layout, and a repository half-migrated would be read as whole | Rejected: the migration runs at session start before any gate, so no session meets the old layout after it; the trailer differs because a commit cannot be migrated |
| Edit `docs/` only through `## Rule changes` and leave the old names in the policy root until the 0.23.0 settle | The release ships with policy documents naming agents that do not exist and paths no reader opens, and the census has to exempt the whole policy root | Rejected: a spelling carries no decision; `spec.md` *Scope* states the in-place rewrite and the rows that are rule changes |
| Rename this work item's own directory last, after the sealer | CI's `chain_check.py` from the tree reads `seal/threads/` and finds no declaration for the branch while the directory stays at `seal/specs/`, so every push before the last commit fails the trailer arm | Rejected: the move lands in phase 2 with the readers, and *Operational impact* states what the installed gate then needs |
| State files keep `specseal-` under the git directory and `~/.claude/specseal/` | The census refuses the old prefix, or exempts fifteen constants; a user who reads `.git/specseal-scratch` beside `.git/seal/` meets a name the plugin no longer has | Rejected on the default of Q2; the migration renames each one it meets so no user loses a throwaway marker or a parity path |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The marker: `optin.MARKER`, `home_at` answering only a root whose `README.md` opens with it, `templates/seal-README.md` and `seal/README.md` opening with it, the bootstrap's sentence for a foreign `seal/`; the arm reading `.specseal/` and a top-level `specs/` removed from `hooks/root-migrate.py` with its cases; README.md and README.ko.md *Coming up from 0.3.x* reduced to the by-hand path | `tests/test_optin.py` (a root with the marker, without it, with no README), `tests/test_root_migrate.py` (a foreign `specs/<id>/` untouched, the removed cases gone), `tests/test_first_setup_asks_once.py`, `tests/test_no_document_names_the_old_roots.py`; each new case seen red first | dfae7be9 |
| 2 | First, this work item's `overview.md` opened from `templates/sdd-overview.md` with phase 1's departure from the frame (the marker reached 18 more modules and four readers outside `optin`, `trail/phases/phase-1.md` after the move), which clears `tests/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`. Then the thread layout: `WORK_ITEMS` `threads`, every reader of a work item file at its new path, `templates/sdd-spec.md` moved to `sdd-design.md` and `templates/sdd-overview.md` to `sdd-gaps.md`, the migration's new units for shared and local mode listing through `entries`, with the symbolic-link refusal pointed at `seal/specs/`, the rewrite of `seal/README.md` to the marker as a unit, the state-file renames and the new stamp, the paths in skills, templates, workflows and `docs/`, and this work item's own directory moved to `seal/threads/<id>/` with `frame/` and `trail/`, `overview.md` renamed to `gaps.md`, and `guarantee.md`, `routing.md` and `changelog.md` at the top. A fixture this phase adds that builds a root calls `tests/conftest.py#mark_root` | `tests/test_chain_hooks_hardening.py`, `tests/test_root_migrate.py` (a 0.22.x fixture migrated end to end, shared and local, through `entries`), `tests/test_routing.py`, `tests/test_chain_check.py`, `tests/test_settle.py`, `tests/test_unverified_check.py`, `tests/test_broad_gate.py`, `tests/test_seal.py`, `tests/test_gather_changelog.py`; `git ls-files seal/threads/<id>` lists the moved files | |
| 3 | The names: `plugin.json`, `marketplace.json` with `renames`, the agents moved to `crafter.md`, `proofer.md`, `tracer.md`, the `agentic:` prefix everywhere, the slug, `PLUGIN_CLONE` and `workflow_at` recognising both clone lines, the trailer with its 0.23.x grace, `implementer.py`, `review-skill-gate.py`, `install.sh` and `uninstall.sh` replacing the old block, `skills/update/SKILL.md`, the eval directories and prompts, `docs/` in place with the rule-change rows applied, LICENSE | `tests/test_chain_check.py` (both trailer keys), `tests/test_implementer_mark.py`, `tests/test_implementer_notice.py`, `tests/test_first_setup_asks_once.py` (the old block replaced once), `tests/test_seal.py` (`pr-checks install` rewrites a workflow under the old slug), `tests/test_every_agent_reads_the_contract.py`, `tests/test_payload_meter.py`; `claude plugin validate .` exits 0 | |
| 4 | The command line: one subparser per tool in `seal.py#main`, the thirteen wrappers and their `.cmd` twins removed, every document and skill printing the subcommand, `templates/hygiene.yml` and the hygiene workflow running `seal` where they ran a wrapper | `tests/test_seal.py` (each subcommand resolves to its script and passes its arguments), `tests/test_a_document_that_names_a_script_says_how_to_reach_it.py`, `tests/test_the_gate_names_every_step_ci_runs.py`; `ls bin/` lists four files | |
| 5 | The proof and the sentence: `tests/censuses.py#old_names` with its exemptions, seen red against the tree at phase 4's commit, then the sweep that makes it green; the tagline replaced by the one sentence at its four places and in Korean; README.md *Install* with the three lines for a user coming from `specseal@specseal`; the changelog fragment | `tests/test_censuses.py` over every tracked file, `git grep -F "Specs, sealed"` matching nothing, `git grep -i specseal` matching only the exempted lines, `changelog/` and `CHANGELOG.md` | |

## Operational impact

- **A user upgrades by three lines**, printed in README.md *Install*:
  `claude plugin marketplace remove specseal`, `claude plugin marketplace
  add MichaelYcJo/AgenticSeal`, `claude plugin install agentic@agenticseal`,
  then `bash install.sh` or `/agentic:preset-setup` for the CLAUDE.md
  block. `/specseal:update` in the installed copy runs the old names and
  cannot carry a user across; the README says so.
- **A repository installed from 0.22.x migrates at its first session
  start**: `seal/specs/<id>/` into `seal/threads/<id>/` as staged `git mv`
  in shared mode, as renames under the git directory in local mode; the
  marker written into `seal/README.md`; each `specseal-` state file beside
  the root renamed. The person reviews the diff and commits it with
  `Seal-Routing: no work item`. A workflow this plugin wrote under the old
  slug is rewritten by `seal pr-checks install`.
- **The commit trailer changes.** A commit made before the rename keeps
  `SpecSeal-Routing:`; `chain-check` reads both through 0.23.x, and 0.24.0
  removes the old key. The CLAUDE.md block says `Seal-Routing:`.
- **This run's own gates are the installed 0.22.4 plugin's.** From phase
  2's commit the installed edit gate finds no `seal/specs/<id>/routing.md`
  for this branch and refuses edits. The orchestrator runs
  `seal no-work-item` once per session on this branch, which is the
  installed plugin's one way to say the declaration lives where it cannot
  read, and every commit still carries `Seal-Routing: <this work item>`,
  which CI's reader from the tree judges. Q3 of `questions.md` holds the
  choice. The installed implementer mark does not recognise `crafter`, so the
  installed notice prints one line per commit after a `crafter` spawn; the
  spawn itself uses the installed `specseal:smith` definition, as every
  spawn of this run does. The orchestrator runs the tree's commands by
  path (`python3 skills/verify/scripts/broad_gate.py`), because `broad-gate`
  on PATH is the installed plugin's.
- **At the merge into `main`** the orchestrator sets the repository's About
  text to the one sentence and removes the topic `evidence-ledger`, with
  `gh repo edit`, as #1051 states.
- No new dependency, no new environment variable, no change to what any
  gate decides.
