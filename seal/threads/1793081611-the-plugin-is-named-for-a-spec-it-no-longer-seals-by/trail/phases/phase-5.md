# Phase 5: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

| Field | Value |
|---|---|
| Phase | 5 |
| Commit | 5822a705 |

## What this phase was asked

Build `frame/plan.md`'s row 5, the last phase: the census
`tests/censuses.py#old_names` with its exemptions, seen red against the tree
at phase 4's tip and then made green by the sweep; the tagline "Specs,
sealed" replaced by #1051's one sentence in README.md, README.ko.md (in
Korean), `.claude-plugin/plugin.json` `description` and both `description`
fields of `.claude-plugin/marketplace.json`; README.md *Install* with the
steps for a user coming from `specseal@specseal`, labelled as read from the
reference and not run (Q4's default); and the changelog fragment.

The sweep covers what phases 3 and 4 left to it: prose naming smith, warden
or scribe outside `docs/`; the brand in prose; `specseal_` identifiers and
`SPECSEAL_RECORD_*`; the eval case directory names and the saved side's
`specseal` key; the record name `broad-gate.md` and its compounds; the
scratch prefixes `broad-gate-` and `test-layout-moved-`; the CI job id
`arm-check-grammar`; `mutation-check` in docstrings; prose naming `spec.md`,
`overview.md`, `rounds/` or `phases/` as concepts; the sentence in
`docs/one-root-by-lifetime.md` *What first setup asks* and its Korean edition
that still said the session-start hook moves the layout from before the root;
and comments citing settled work items at `seal/specs/<id>/`. Each exemption
carries its reason: the old trailer key, the old CLAUDE.md block markers, the
old clone line, released `changelog/` entries, recorded eval scaffolds and
replay files, and `.test_durations`.

The owner's decision in `frame/plan.md` *Verification this work item owes*
bound the phase: the census is the one new case, seen red once; every other
change is a spelling proved by the existing cases; no `seal mutate`; one
`bin/test` command over `tests/test_censuses.py` and the modules that read
what changed.

## What this phase found

**The case written new, and how it was seen red.** `old_names` joined
`CENSUSES`, so `tests/test_censuses.py::Test_module` judges every tracked
file no module declares, and every module's `census_case` judges its target.
Before any sweep, with only the census in the tree at `79bc679f`, the module
ran 1 failed and 172 passed; the failure was the sweep case, and the census
over every tracked file found 1,974 lines in 273 files. Three unit cases sit
in `Test_old_names`: the new names, the kept spellings, the records and the
whole files pass; each family of old names is refused at its line with the
message; an old name beside a kept spelling is still refused. They were
written with the census and were not seen red on their own; the red the
owner's decision asks for is the sweep case's. Every other change is a
spelling, held by the cases that already pinned it, with the pins moved to
the new text.

**How the exemptions are spelt.** A markdown line cannot carry the census's
`# exempt from old_names:` line without making it a heading, so the census
takes an old spelling out of a line only where it is a spelling a reader
still meets, listed in `KEPT_OLD_NAMES` with its reason: the trailer key
`SpecSeal-Routing`, the two CLAUDE.md block markers, the stub marker
`# specseal-git-hook`, the old clone URL, the old install id and the
`marketplace remove` step, the `renames` entry, the 0.3.x directory
`.specseal`, and the two variables `SPECSEAL_LINT` and `SPECSEAL_LANG`. Whole
paths pass in `OLD_NAME_RECORDS` (`changelog/`, `CHANGELOG.md`,
`seal/process/`, `seal/threads/`, `evals/scripts/recurred_truths.json`,
`.test_durations`), in `RECORDED_CASE` (the replay and seeded eval cases),
and in `KEPT_FILES` (the migration and its two test modules, the frozen
`hooks/cmdline_base.py`, and the two test modules of the replay and seeded
generators). Every other kept line carries a line exemption: the generators'
reads of the 0.22.x round-record layout, the two by-hand commands in each
README's *Coming up from 0.3.x* block, where the exemption is a shell comment
inside the fence, another tool's `spec.md` in two settle and unverified
fixtures, the bytes of an old git hook stub, and the pattern in
`tests/test_one_word_one_meaning.py` that names the old brand.

**The frame does not hold in seven places.**

- The spawn's exemption list named no thread and no process archive.
  `seal/threads/` passes whole, because a thread is the record of its work
  item and this one quotes every name it renames; `seal/process/0.22.4.md`
  passes as a released archive. `SPECSEAL_LINT` and `SPECSEAL_LANG` keep
  their names, because a person sets them in their own shell, no migration
  reaches them, and a rename would turn a hook back on for whoever set the
  old one; renaming them with a grace reading is a behaviour change this
  release excludes.
- `hooks/cmdline_base.py` is frozen below its rider, byte for byte
  `86256492`'s `hooks/cmdline.py`, which
  `tests/test_the_frozen_reading_never_grows.py` holds. Two comment edits
  below the rider were taken back, and the file passes whole.
- `docs/one-root-by-lifetime.md` *Naming* stated the one sentence word for
  word, and `tests/test_no_passage_is_pasted_into_a_second_file.py` refused
  the pair with README.md, 9 shared runs where 0 were measured. The row now
  points at README.md's first line and `plugin.json` `description`, in both
  editions. This departs from the frame's `to:` for that row, which the 0.23.0
  settle reports rather than refuses.
- README.ko.md's Korean sentence takes the wording phase 3 wrote into
  `docs/one-root-by-lifetime.ko.md`, so the Korean has one spelling.
- Q4's default cell contradicts its own option (b): (b) says the README
  prints the lines labelled as read from the reference and not run, and the
  default cell says the README carries no label. The spawn prompt asked for
  the label, so README.md and README.ko.md carry it.
- The rule cases opted nothing in since phase 1 and graded files at paths no
  agent writes since phase 2: `evals/scripts/rule_cases.py` wrote
  `seal/specs/<item>/` and no `seal/README.md`, and
  `tests/test_evals_layout.py` held the 14 committed cases to that output.
  The generator now writes `seal/README.md` with `optin.MARKER` and the thread
  layout; the case directories are `rule-crafter-*` and
  `rule-proofer-one-finding`; the sealer grader `shape-runs-no-broad-gate` is
  `shape-runs-no-broad-run`; the heredoc delimiter is `AGENTIC_EOF`; and
  `recurred_truths.json` names the renamed case. Each committed file was
  edited with the Edit tool until it equalled the generator's output, which
  the layout case confirms; the generator wrote only into the scratchpad.
- `tests/e2e/teammate/test_teammate_flow.py` linked the tree at
  `$RUNNER_TEMP/specseal`, where the hygiene template clones it to
  `$RUNNER_TEMP/agentic` since phase 3, so its five cases failed at
  `79bc679f`. The link and the fixture's work item take the new names, and
  the module passes.

**What the sweep renamed beyond prose.** The pytest recorder is
`skills/verify/scripts/pytest_record/agentic_pytest_record.py` and its
module `tests/test_agentic_pytest_record.py`, by `git mv`, with
`AGENTIC_RECORD_DIR` and `AGENTIC_RECORD_KEY`; the gate's hand-over variable
is `AGENTIC_GATE_INVOKED_AS`; the gate's scratch prefixes are `seal-gate-`
and `seal-gate-base-`, the layout check's is `seal-layout-moved-`, and the
orchestrator's capture file is `<scratchpad>/<work-item-id>/gate.log`; a saved
side's key is `agentic`; the CI job is `arms-grammar`, and neither ruleset
requires the old id (`gh api .../rulesets`: `lint` and `release` only).
Every message a person reads that named the brand names AgenticSeal, and
each case that pins one pins the new text. `hooks/dispatch.py#LABEL` grew by
three units, so the longest failure reports are 567, 975 and 1,381 UTF-16
units, and `seal_stamp.py`'s reserve comment states the figures
`tests/test_dispatch.py` measured.

**What is left, and whose it is.** `evals/scripts/replay_targets.py` and
`seed_defects.py` read round records only at the 0.22.x layout every
committed case was cut from; the first case cut from a tag after the rename
needs the thread layout read there too, and that is the next session that
generates such a case. The replay and seeded cases rebuild 0.22.x trees,
which this release's session start would migrate during an eval run; nobody
has measured what a side run on this release reads in them. The departures
above are for the orchestrator to carry into `gaps.md`, as phase 4's were.

**The run.** The last run was 158 modules in one command: 6761 passed, 16
skipped, exit 0. `uvx ruff check` and `uvx ruff format --check` over the 160
changed Python files exited 0, and `claude plugin validate .` exited 0 with
its two warnings from before this phase. `git grep -F "Specs, sealed"`
matches only files of this thread, which the census passes as a record.

**The suite writes into the real home directory.** Each run left
`~/.claude/agentic/version-check`, as phases 2 to 4 recorded. Each was
removed after its run, and `~/.claude/specseal/` was never touched.
