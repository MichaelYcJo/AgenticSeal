# Phase 4: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

## What this phase found

**The frame holds for this phase, with one statement the tree contradicted,
one case built in another place, and one process row more than the frame
names.** The phase started at `71a77691`, which holds #1445 and #1459. Both
READMEs were read as they stand there: #1459 rewrote the routing question's
list, and *Shared or local* (`README.md`) and *shared 인가 local 인가*
(`README.ko.md`) still open with the table of the three answers (read). Four
things in the frame did not hold as written:

- `frame/plan.md` *Phases* row 4 says `git grep -n "agentic-seal" -- skills
  agents templates docs README.md README.ko.md CONTRIBUTING.md CLAUDE.md`
  lists one line of the core and one of each README. At `71a77691`, before
  any text was written, it listed two lines of
  `skills/implement/scripts/seal.py` (`:1260` and `:2407`), comments phase 1
  wrote (executed). The census of *Scope* item 4 reads string constants,
  so neither comment was refused. Both now cite `optin.SECOND_HOME`. At
  `09fb3049` the grep lists `README.ko.md:191`, `README.md:188` and
  `skills/core/SKILL.md:25`, and nothing else (executed).
- `frame/design.md` G14 says the check of where the second name is stated
  reads `SCANNED` imported, and *Scope* item 5 and S8 call it a text case.
  The three cases are in `tests/behaviour/test_no_document_names_the_old_roots.py`,
  the module that defines `SCANNED`:
  `test_the_core_states_the_second_name_once`,
  `test_each_readme_states_the_second_name_on_one_line_of_shared_or_local`
  (one parameter per README) and
  `test_no_other_scanned_file_states_the_second_name`. Grounds: the
  crafter's rule *A new test starts from its group* puts a case beside the
  cases of what it covers, and that module is the group that holds which
  root names the shipped documents may state. `SCANNED` keeps one source
  with no import. The name is read from `lib/optin.py#SECOND_HOME`, loaded
  through `conftest.load_lib_module`.
- `frame/design.md` *Scope* item 7 gives the fragment's `### Process changes`
  table one row. It has two: the bootstrap's change, and the core's
  definition with the two sentences that point at it. Grounds:
  `docs/layout/the-record-layout.md` *A change writes fragments, never a
  shared file* asks for one row per change to the way of working, and it
  names `skills/core/SKILL.md` as such a file.
- `frame/design.md` S7 says existing cases change only for a changed
  signature. `tests/behaviour/test_first_setup_asks_once.py::test_a_projects_own_seal_names_the_marker_template_and_the_git_dir_root`
  pins the bootstrap paragraph *Scope* item 5 changes, and it gained one
  assertion: the paragraph names `` `seal mode` ``. Judged against *Scope*
  item 5, which states the change S7 describes the old cases around.

**Departures from the frame in the text, each judged against the document
named.**

- The core's sentence says the *shared* root is `agentic-seal/`, and each
  README says that `seal/` means that folder *in shared mode*. The local
  root keeps the name `seal` (`frame/design.md` *Out*, the local root's
  name), so a sentence saying the root is `agentic-seal/` beside a
  project's own `seal/` would be false in local mode.
- `templates/setup/seal-README.md` and `seal/README.md` gained a paragraph
  after the by-hand moves: where the root has the second name, each
  `--show-toplevel` path in those commands ends in that name in place of
  `seal`. The frame names only the marker paragraph of these files. The
  commands are paths a person runs, so this is the class *Scope* item 3
  states for messages ("a path a person reads in a message is the real
  path") and contract rule 12. The paragraph stands apart from the moves,
  because `test_first_setup_asks_once.py#switch_block` reads exactly two
  code spans after each lead and runs them.
- Each README's sentence stands after the paragraph on what local mode fits,
  not right under the table. `test_first_setup_asks_once.py::test_the_readme_states_what_local_mode_leaves_unchecked_under_the_table`
  pins the paragraph under the table as local mode's limit, and it failed
  with the sentence there (executed). *Scope* item 8 asks for "below the
  table of answers", which holds.
- `skills/implement/bootstrap.md` says in its opening paragraph on asking
  that the orchestrator runs `seal mode` before it asks, and that a shared
  answer creates the root at the shared place it printed. The option
  **shared, records only** names that place for every repository, so the
  instruction cannot stand only in the paragraph on a project's own `seal/`.
  That paragraph keeps its opening words, says the shared place `seal mode`
  prints beside it is the core's second name, and offers only local where a
  directory without the marker stands at that place too.

**Seen red** (executed):

- Before any text, at `71a77691`'s text with the cases added:
  `bin/test tests/behaviour/test_no_document_names_the_old_roots.py -q -p
  no:xdist -k second_name` gave 3 failed, 1 passed. The core case failed on
  the count, and each README parameter on "names agentic-seal on 0 lines".
  The case that passed is the one that asserts no other file states the
  name, green against a tree that states it nowhere.
- The bootstrap case failed against the old paragraph on its new line,
  `` assert '`seal mode`' in own ``.
- `seal mutate`, one command per mutant, each run with the `-k second_name`
  cases, every one red, each failing line read:

| Mutant | Commit | Failing line |
|---|---|---|
| the name removed from the core's sentence | `037d2fa2`, again at `09fb3049` | "does not name `agentic-seal/` exactly once" |
| the name removed from `README.md`'s line | `037d2fa2`, again at `09fb3049` | "README.md names agentic-seal on 0 lines" |
| the name removed from `README.ko.md`'s line | `037d2fa2`, again at `09fb3049` | "README.ko.md names agentic-seal on 0 lines" |
| `README.md`'s line moved under a new `## Moved` heading | `037d2fa2` | "is not under ### Shared or local" |
| a second `README.md` line naming it | `037d2fa2` | "README.md names agentic-seal on 2 lines" |
| `` `agentic-seal/` `` planted in `skills/implement/bootstrap.md` | `037d2fa2` | "stated outside skills/core/SKILL.md and the READMEs", naming `skills/implement/bootstrap.md:42` |

The plan row asks for S8 red with the core's sentence deleted. Each
mutant takes the name out of the sentence and leaves the rest of it,
because `seal mutate` replaces one literal string and the name is what the
case reads. No unit of code adds behaviour in this phase: the change to
`seal.py` is two comments, and `tests/skills/test_seal.py` imports the
module in the boundary run below.

**`seal rules --check`** (executed, at `09fb3049`): exit 0, "all 221 check
lines in 68 rule files hold".

**The other statements of the reworded rule** (a sample, by `git grep` on
"keeps the root under the git", "one place", "offers neither" and "only
local", and by the `check:` lines naming the two changed test modules).
`docs/layout/one-root-by-lifetime.md:73` and its Korean edition still say
first setup keeps the root under the git directory. The design's
`## Rule changes` rewrites both at the settle, because this work item's
subject is the code. `templates/setup/hygiene.yml:16` says local mode keeps
the root under the git directory, which holds. The policy sections whose
`check:` lines name `test_first_setup_asks_once.py` and
`test_no_document_names_the_old_roots.py` state the places with `seal/` as
the core's name, which `frame/design.md` *Out* judges true. The search
reads only the wordings listed, so a statement worded otherwise was not
reached.

**The phase boundary** (executed, one command): `bin/test tests/text
tests/behaviour tests/test_censuses.py` and every test file outside those
two directories that names a changed path, a README, the core, the
contract, `skills/implement/SKILL.md`, `bootstrap.md`, `seal.py` or a
changelog: `tests/e2e/teammate/test_teammate_flow.py`,
`tests/evals/test_noninferiority.py`, `tests/evals/test_rule_cases.py`,
`tests/github/test_publish_release_note.py`,
`tests/github/test_release_report.py`,
`tests/github/test_roll_flow_measurement_issue.py`,
`tests/github/test_rules.py`, `tests/hooks/test_core_start.py`,
`tests/lib/test_config.py`, `tests/lib/test_core.py`,
`tests/lib/test_optin.py`, and `tests/skills/` for `broad_gate`,
`chain_check`, `fold_check`, `pact_check`, `passages`, `payload_meter`,
`pr_body`, `seal_stamp`, `seal`, `session_cost`, `settle` and
`unverified_check`. At `037d2fa2` with the fragment it failed twice, in
`tests/behaviour/test_docs_line_wrap.py`: `skills/agent-contract/SKILL.md`
and `skills/implement/bootstrap.md` each had a line past 88 columns, which
`482e0616` rewrapped. At `482e0616`: 5036 passed, 9 skipped, exit 0. The
same command at `09fb3049`, with this record and the Status cell written
in the working tree: 5036 passed, 9 skipped, exit 0.
