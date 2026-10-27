# Phase 3: 1793057292-agent-lifetime-and-process-archive

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | bdfdb018 |

## What this phase was asked

Take the unverified record's gate arms out. Remove the step *the unverified
record is readable, and rows leave it closed* and its comments from
`.github/workflows/hygiene.yml` and `templates/hygiene.yml`. Remove the
`unverified` arm and its `PARTITION` row from
`skills/verify/scripts/broad_gate.py`, and the cases that pinned them.
Rewrite in place the count of shipped steps in `CONTRIBUTING.md` and the
`skills/implement/SKILL.md` sentence that a deleted row fails the next pull
request. Read every other hit of `git grep -i unverified` that states the
removed gate, and either rewrite it in place or name it here as staying. The
reader module, the command, `--baseline` and `settle`'s list of open rows
stay. Remove the `.test_durations` entry phase 2 left for its removed case 9
of `tests/test_the_rules_have_one_owner.py`, and any entry for a case this
phase removes. See every changed pin red against the old text first. Run the
touched modules, the modules that read the changed files, `bin/test-layout
--check` and `--pairs`, and `uvx ruff check` and `uvx ruff format --check`
over the changed Python files. State, for the pull request, the failure
direction, the prompt budget, the platforms and what the change removes.
Stop after phase 3.

## What this phase found

**The frame holds for phase 3, with four lists short of the tree and one
coordinate that names nothing** (`executed`, `git grep -n -i unverified`
outside `seal/specs`, `changelog` and `.test_durations`, 217 lines, each
read). Each site below was corrected in bdfdb018 under contract rule 19,
except the policy documents, which no commit of this branch edits:

- `tests/test_arm_check.py` names no `unverified` arm. `spec.md` `## Removes`
  and S10 name it, but the module tests `arm_check.py`, the mutation-arm
  counter, and its word "arm" means a branch of code, not a broad-gate arm.
  Nothing in it changed. It ran green (94 passed, 2 skipped).
- `tests/test_unverified_rows_close.py#test_the_documents_state_the_merge_base_footing`
  held both workflow files to the phrase *the base's tip*. That phrase stood
  only in the removed step's comments, so its two parameters for the
  workflow files left with the step, and their `.test_durations` entries
  left with them.
- `tests/test_first_setup_asks_once.py#test_the_template_runs_the_two_shipped_checks_from_the_plugin_at_its_tag`
  asserted that the template runs `unverified_check.py`. It now asserts the
  template runs `chain_check.py` and `seal.py`, and that it names
  `unverified_check.py` nowhere. The name stays true: the template still runs
  two shipped checks.
- `tests/test_the_gate_names_every_step_ci_runs.py` pins the coverage line
  verbatim. The `release` job now runs 7 steps, 4 of them on a base that is
  not `main`, and the gate mirrors 2. Both cases are rewritten to those
  numbers. The panel's `· 2 more steps` and `· 5 more steps` do not change,
  because the step and its arm left together.
- Sites outside the frame's lists that stated the step or the arm, each
  rewritten in place: the chain step's comment in
  `.github/workflows/hygiene.yml` justified itself by "the step above"; the
  template's header named the closing memo's rows and `unverified_check.py`,
  and its checkout comment said *both checks*; `skills/verify/orchestration.md`
  *The broad gate* said *the two baselines*; `unverified_check.py#settled_root`
  said every pull request hands the tool `seal/specs/`, the shipped template
  included; a comment in `unverified_check.py#main` said the workflow runs
  it; `unverified_check.py#annotate` said it is unreachable while
  `hygiene.yml` pins `ubuntu-latest`; `CONTRIBUTING.md` *What a contribution
  is not asked for* listed the tally and gave the overview row the step as
  its reason; and `tests/test_a_reference_root_is_read_and_never_taken.py`
  said `broad-gate` hands `seal/specs/` to the checks above.

**One policy document states the removed step, and no `## Rule changes` item
covers it** (`read`). `docs/one-root-by-lifetime.md` (line 123) and
`docs/one-root-by-lifetime.ko.md` (line 119) say a hygiene workflow left in
local mode is red forever because `unverified_check.py` runs second and
exits 2. With the step gone, that sentence is false. The plan says no phase
edits `docs/`, so it stands. The framer or the orchestrator answers it with
a `change` item on both editions before the settle.

**The settle that applies this spec turns one parameter red** (`read`).
The `## Rule changes` items on `docs/release-checklist.md` remove both
sentences there that name the merge base. The parameter
`docs/release-checklist.md-None-None` of
`test_the_documents_state_the_merge_base_footing` asserts the file says
*merge-base* or *merge base*, so it fails once those items are applied. The
settle session answers it by removing that parameter in the settle's own
commit.

**What stays, by kind** (`read`, each hit opened):

- The label `unverified` among `executed`, `read` and `unverified`: the
  READMEs, `agents/*.md`, `skills/agent-contract/SKILL.md`,
  `skills/verify/SKILL.md`, `skills/implement/SKILL.md` lines 160, 276 and
  343, `docs/the-broad-gate.md`, `docs/the-review-record.md`,
  `skills/verify/orchestration.md` line 18, `deferral_check.py`, and the
  cases pinning the label.
- The reader module loaded by path: the `.github/scripts` checks,
  `chain_check.py`, `fold_check.py`, `rule_changes.py`, `settle.py`,
  `coordinates.py`, `payload_meter.py`, `seal.py`, `hooks/blocks.py`,
  `ruff.toml`, `evals/`, and every test module that loads it.
- The command a person types, with `--baseline`: `bin/unverified-check` and
  its `.cmd` twin, the README rows, `skills/verify/SKILL.md` *And something
  has to read the row afterwards*, `SECURITY.md`, `templates/config.md`
  *Reference specs*, `hooks/config.py`, and `unverified_check.py`'s own
  docstring and `--baseline` help. These say what the merge base is when
  the command runs in CI. That is a fact about the command, and
  `test_the_documents_state_the_merge_base_footing` pins it.
- `tests/test_broad_gate_rule.py#BY_HAND` lists `unverified-check` among
  names the `Broad gate` prose must not list by hand. That is a negative pin,
  and it holds as it is.
- `skills/code-review/orchestration.md` and `broad_gate.py` say *record
  arm*. That still describes the chain arm and the mode arm.
- `docs/the-record-layout.md` *The unverified record, and the baseline it is
  read against* states the merge-base rule, with `check: one-merge-base`. It
  stays, as `plan.md` row U-C keeps `--baseline`.
- `docs/release-checklist.md`: its two sites are this spec's `## Rule
  changes` items.

**The failing-arm pad keeps its rule and loses its example** (the work).
`broad_gate.py#failed_form` pads to the widest failing name, not to 8,
because `unverified` was ten characters. No arm name is longer than 8 now.
The logic stays, its comment states the rule without the removed name, and
`Test_failed_form::test_refuses_to_set_a_long_name_a_column_out` uses
`longer-arm`, also ten characters.

**The gate change, for the pull request** (`CONTRIBUTING.md` *What a change
to a gate must carry*):

- **Failure direction**: the gate allows more. A pull request that deletes a
  `## Not verified` row, or a whole `overview.md`, instead of closing it now
  passes CI and the broad gate. That is the cheaper mistake here: the step
  failed in none of 142 failed hygiene runs (`spec.md` *Scope* item 5,
  `executed` by the framer). Its recorded issues are its own defects. A
  deleted row still meets the warden, who reads `overview.md` in the diff at
  stage 1 (`skills/code-review/SKILL.md`, `read`), and the sealer. A wrong
  allow here costs a lost row of a record. It cannot break another session's
  tree.
- **Prompt budget**: zero. The change removes a CI step and a gate arm, and
  it asks nobody anything.
- **Platforms**: the cases ran on macOS only (`executed`). The removed step
  ran on `ubuntu-latest`. Nothing here was run on Linux or Windows; CI on
  the pull request answers both.
- **What it removes**: the CI step in both workflows, the broad-gate arm with
  its constants (`UNVERIFIED`, `UNVERIFIED_NAME`, `SPECS`) and its
  `PARTITION` row, and the release-day ordering duty the step put on
  `docs/release-checklist.md`, through `## Rule changes`. It adds nothing.
- **A repository installed from an earlier release** keeps the step until
  `seal pr-checks install` writes the file again (`spec.md` *Limits*).

**Each changed pin was seen red against the old text** (`executed`, `bin/test
tests/test_broad_gate.py tests/test_first_setup_asks_once.py
tests/test_unverified_rows_close.py -p no:xdist -q -k ...` at 2fc25fbd with
the tests written and the tree unchanged, 3 failed; then
`tests/test_the_gate_names_every_step_ci_runs.py` with the workflow step
removed and `PARTITION` unchanged, 4 failed):

| S row | Case | Red against the old text |
|---|---|---|
| S10 | `tests/test_broad_gate.py::Test_gate::test_accepts_a_green_tree_and_runs_every_check_in_order` | the run kept `unverified.txt` |
| S10 | `tests/test_the_gate_names_every_step_ci_runs.py::test_every_entry_of_the_partition_names_a_step_the_workflow_has` | `PARTITION` named the removed step |
| S10 | `test_a_feature_seal_counts_the_steps_ci_runs_for_it` and `test_a_release_seal_counts_every_step_ci_runs_for_it`, rewritten | the old counts, 5 and 8 steps with 3 answered, against the pins of 4 and 7 with 2, under the mutant below |
| S12 | `tests/test_first_setup_asks_once.py::test_the_template_runs_the_two_shipped_checks_from_the_plugin_at_its_tag` | the template names `unverified_check.py` |
| S10 | `tests/test_unverified_rows_close.py::test_the_skill_states_the_closing_convention` | the skill does not say no check at the pull request refuses a deleted row |

The fixture changes in `tests/test_broad_gate.py` (`WORKFLOW`'s first step,
`Test_job_steps`, `Test_unanswered`, `Test_failed_form`) only follow the
removed name. Each passes against the old code too, so they are not new pins.

**Mutations** (`executed`, `bin/mutation-check` after bdfdb018, each bounded
at 300 s, the tree clean after each). The step written back into
`.github/workflows/hygiene.yml`, run over the two count cases: red. Run over
`test_every_step_the_workflow_runs_is_classified`: red. A step running
`unverified_check.py` written back into `templates/hygiene.yml`, run over the
template case: red. An `unverified` arm written back into
`broad_gate.py#gate`, run over the `Test_gate` case: red. Two mutants of the
`skills/implement/SKILL.md` sentence, run over the closing-convention case:
2 red, 0 survived. This phase added no unit of code, so no other mutant was
owed.

**`.test_durations` prices no removed case** (`executed`, the file parses as
JSON with 6,531 entries). Three entries left: phase 2's case
`test_the_owner_states_the_rule[9 a hand-back's verification claim is a
claim]` and the two workflow parameters above. No case was renamed.

**The narrow checks** (`executed`). The 76 test modules that read a changed
file, run one at a time with `bin/test <module> -q` and each exit code
recorded: 3,569 passed, 13 skipped and 2 failed. The two failures:
`tests/test_docs_line_wrap.py`, over a `CONTRIBUTING.md` line, which was
rewrapped, and the module then ran green with three other document modules;
and `tests/test_chain_hooks_hardening.py#test_every_spec_directory_that_reached_the_ladder_has_an_overview`,
which fails until phase 4 writes `overview.md`, as the spawn said. Among them
are the plan's six modules: `tests/test_broad_gate.py` 304 passed and 1
skipped, `tests/test_arm_check.py` 94 passed and 2 skipped,
`tests/test_the_gate_names_every_step_ci_runs.py` 9 passed,
`tests/test_seal.py` 380 passed, `tests/test_unverified_check.py` 333 passed,
and `tests/e2e/teammate/test_teammate_flow.py` 7 passed (S11, S12).
`bin/test tests/test_settle.py -q` returned 75 passed (S11).
`bin/test-layout --check` and `--pairs` over the five changed test files
refused nothing and named no pair. `uvx ruff check` and `uvx ruff format
--check` over the seven changed Python files report nothing.
