# Phase 3: 1794200905-a-foreign-seal-dir-keeps-the-records-shared

## What this phase found

**The frame holds for this phase, with one reader it did not list, one case
built in another shape, and five removals `## Removes` did not name.** The
coordinates *Technical context* gives for this phase stood at `948ff0da`
(executed: the census below, run over `948ff0da`'s tree, listed
`.github/scripts/rules.py:229` and `:379`, `settle.py:1297`,
`rule_changes.py:576` and `unverified_check.py:1248`, `:1276` and `:1301`
among its 20 lines). Four things in the frame did not hold:

- `frame/design.md` *Scope* item 3 lists eleven modules and misses
  `.github/scripts/finding_counts.py`. It read `settle.SPECS`, which this
  phase removes, so it read `seal/threads/` whatever the root's name. It
  now reads the name through `lib/optin.py` (`threads_at`). Judged against
  *Scope* item 3's rule and contract rule 12.
- *Scope* item 4 asks for a text case with an allowlist in the shape
  `KEEP` has in `tests/behaviour/test_no_document_names_the_old_roots.py`.
  It is built as a census, `root_name` in `tests/censuses.py`, with three
  `# exempt from root_name: <why>` lines in place of the allowlist:
  `lib/fields.py#INFO`, `seal.py`'s `prog="seal"`, and
  `rule_changes.py#EARLIER`. The census runs in each module's
  `census_case(TARGET)` and in
  `tests/behaviour/test_every_tracked_file_meets_every_census.py`. An
  exemption that excuses nothing is refused, as every census refuses one.
  Grounds: the `tests/censuses.py` docstring makes a census the home of a
  rule every tracked file of a kind keeps, and says no census keeps a list
  of exemptions. `skills/core/SKILL.md` *The rule a mechanism is kept
  against* says nothing is kept beside the tree to stay in step with it,
  and an allowlist is such a list. The crafter's rule *A new test starts
  from its group* puts the case in the census group. Its limits stand in
  the comment above it: a name built from other strings, a pattern such as
  `^seal/`, and `optin.HOME` joined under a root all pass.
- *Data & interfaces* gives `inside_the_root(rel, home)`. It is built as
  `inside_the_root(rel, name)`, NAME being the root's name in the tree,
  `lib/optin.py#home_name`'s answer, because the function compares
  repository-relative paths. NAME is `""` in local mode, and then no tree
  path is inside the root. `reference_roots` and `under_reference_root`
  take NAME too, and the frame says nothing of them.
- *Removes* names none of these five, each removed because the root's name
  no longer stands as a constant:
  - `settle.py#SPECS`, replaced by `threads(home)`.
  - `settle.py#REMOVED_PLAN_RE`, replaced by `removed_plan_re(specs)`.
  - `publish_release_note.py#FRAGMENT_RE`, replaced by `fragment_re()`.
  - The default `specs="seal/threads"` of `rule_changes.py#order`. The
    argument is now required.
  - The case
    `tests/skills/test_settle.py::Test_module::test_the_pinned_checks_read_under_the_root_alone`.
    It held `settle.SPECS == "seal/threads"`. `Test_threads` replaces it,
    and its two cases hold the place under either name and under a local
    root.

**Decisions made while building.**

- Each reader that classifies a tree path falls back to `optin.HOME` where
  no shared root carries the marker, as phase 2's `chain_check.py#root_name`
  does: `rules.py#records_root`, `release_report.py#documents`,
  `publish_release_note.py#fragment_re`, `finding_counts.py#threads_at`,
  `unverified_check.py#root_name` and `settle.py#survey`'s default. The
  existing fixtures commit a `seal/` with no marker. Judged against S7,
  which lets existing cases change only where a signature changes.
- `rules.py#records_root` reads `home_name`, not `home_at`. The code before
  read `<root>/seal` alone, and a root in local mode is not in the tree a
  CI checkout holds.
- `unverified_check.py`'s settled and unwritten states compare the
  directory's name with `root_name` of the repository holding it
  (`named_root`). The absent state compares it with the shared place
  `home_paths` gives, since no root stands to be named.
- `settle.py#records_of` reads a root directly under the repository's top,
  by either name, as shared mode. It used to compare the path with
  `<root>/seal`.
- A message that calls the root by name in text keeps `seal/`, as *Scope*
  item 3's last sentence says. Examples: settle's no-root refusal,
  `unverified_check.py`'s three state lines, and `pact_check.py`'s
  one-sided line. A path a person opens is printed under the real name:
  `pact_check.py`'s `pact.md` and the signer's `config.md`, settle's work
  item paths, `rules.py`'s excused line, and `broad_gate.py`'s two places.
- The reference-root cases put the package's `specs/` at
  `seal/vendor/specs/`. The `old_names` census refuses `seal/specs` in a
  test, and the case needs only a directory named `specs` under the
  package.
- The `optin.HOME` equality pin in `tests/lib/test_config.py` is removed,
  as *Removes* row 2 names.

**The S5 cases**, in
`tests/behaviour/test_a_foreign_seal_dir_keeps_the_records_shared.py`, one
per command:

- `seal gate --preflight`: with no root, the refusal names
  `<repo>/agentic-seal`. With the root, it reads `Broad gate` from
  `agentic-seal/config.md`.
- `seal rules --check`: a design under `agentic-seal/threads/` excuses a
  refused line, named by its path there.
- `seal unverified agentic-seal/threads`: the unwritten, settled and absent
  states. A second case walks `.`, reads the memo under `agentic-seal/` and
  passes over the package's `seal/vendor/specs/`.
- `seal settle --released-at main`: names `agentic-seal/threads/<id>/`.
- `seal pact`: names `agentic-seal/pact.md`.
- `seal fold`: reads `Policy root` and `Document token ceiling` from
  `agentic-seal/config.md`.

`tests/github/` gained one case each for `release_report.py#documents`,
`publish_release_note.py#fragments` and `finding_counts.py#main`.
`tests/skills/test_pact_check.py` gained a third side of
`test_refuses_a_relationship_recorded_on_one_side`: a signer whose root is
`agentic-seal/`.

**Seen red.** The code under test was a scratch tree from `git archive`,
with the branch's `tests/` copied in.

- At `948ff0da`'s code (executed: `-k s5`), 7 failed and 2 passed. The two
  that passed are phase 2's `seal pr-body` case and the fold case, since
  `fold_check.py` reads through `home_at` from phase 1 on. The failing lines
  were read:
  - The gate's refusal named the places as `` `<repo>/seal/` `` and
    `` `<git-common-dir>/seal/` ``.
  - `seal rules` read "all 0 check lines in 0 rule files hold".
  - The settle run read the root as "the seal/ root, in local mode".
  - The pact line named `seal/pact.md`.
- At `bc3cb015`'s code all 9 failed. The fold case printed "has no seal/
  root at either place".
- The three `tests/github/` cases failed at `948ff0da`'s code. The
  documents list had no `policy/` entry, the fragment read was the
  package's `1700000001-pkg`, and the counts table was empty.
- The pact case failed there too, naming `seal/config.md`.
- The walk case failed there with "2 closing memos ... 1 unreadable" at the
  package's memo, before and after the move to `seal/vendor/specs/`.
- S9 (executed): `PLANTED = "agentic-seal"` was planted under
  `pact_check.py#PACT_FILE`. `bin/test tests/skills/test_pact_check.py -k
  census` exited 1, naming `pact_check.py:138`, and the line was removed.
  The census over `948ff0da`'s tree gives 20 lines. Over HEAD's 196 tracked
  `.py` files it gives none.

**Every unit that adds behaviour went red under `seal mutate`** (executed,
after `332d2cef` and the commits that add cases). No selection reached a
census case, so each red came from the cases named.

| Unit | Mutants | Cases run | Result |
|---|---|---|---|
| `lib/config.py#inside_the_root` | 1 | `test_config.py -k plugins_own_root` | red |
| `unverified_check.py#root_name`, `#absent_root` | 2 | the behaviour module `-k unverified` | 2 red |
| `unverified_check.py#config_at`, the name | 1 | `-k walks_agentic` | red |
| `settle.py#threads`, `#records_of` | 2 | `-k settle_shows_a_work_item`, `Test_threads` | 2 red |
| `rule_changes.py#pending`, the label | 1 | `-k rules_check` | red |
| `rules.py#records_root` | 1 | `-k rules_check` | red |
| `release_report.py#documents`, the name | 1 | `test_release_report.py -k agentic_seal` | red |
| `publish_release_note.py#fragment_re` | 1 | `test_publish_release_note.py -k agentic_seal` | red |
| `finding_counts.py#threads_at` | 1 | `test_finding_counts.py -k agentic_seal` | red |
| `pact_check.py`, the pact's path | 1 | `-k pact` | red |
| `pact_check.py`, the signer's config path | 1 | `test_pact_check.py -k one_side` | red |
| `broad_gate.py#gate`, the no-root message | 1 | `-k gate_reads_its_row`, `-k not_opted_in` | red |
| `tests/censuses.py#_spells_a_root` | 1 | `test_censuses.py -k root_name` | red |

The signer's config path at first had nothing behind it. A mutant spelling
`seal/` went red only on the census case. A mutant reading the pact's own
root survived. The third side of the one-sided case was added for it
(`10ed66ed`), seen red at `948ff0da`'s code, and the mutant then went red.

**The phase boundary** (executed, one command): `bin/test tests/lib
tests/skills tests/github tests/test_censuses.py tests/text tests/behaviour
-q`. That covers the plan row's files, each test file the phase changed,
each test file that loads a changed module, and the tree-wide files
`CONTRIBUTING.md` names. At `f87c7d4b` it failed once: the `old_names`
census refused `seal/specs` in two test files. After `3b035379` moved
those paths: 5641 passed, 9 skipped, exit 0. `e1049ae6` then changed only
`tests/skills/test_settle.py`'s docstrings (executed: that file, 160
passed).

**For the next phase.** The census reads `.py` files alone, so phase 4's
text case of *Scope* item 5 is the one that reads documents.
`.test_durations` still lists phase 2's and this phase's removed pins by
name. The boundary passed with them there.
