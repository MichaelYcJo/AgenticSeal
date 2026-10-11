# Implementation Plan: a ledger row's claim is the test that enforces it

<!-- seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/plan.md — HOW, in phases. This is the Design Gate's
artifact: where the work alters observable behaviour, approval of this plan is
the gate. -->

Approved 2026-10-08 by the repository owner, when `smith` was spawned.
Approved 2026-10-12 by the orchestrating session under the owner's `automation` answer and the owner's reframe decision, for the redesign after round 2, when `smith` was spawned; `questions.md` Q7 is built on its default (a).

## Summary

A ledger row may name the test that holds its claim, in pytest's own
spelling, instead of a hash over the code. Such a row never drifts: the
checker reads that the test exists, the suite reads that it passes, and
`--reverify` leaves it alone. A released row moves onto its test by one
`Corrected ·` row in the branch's fragment, written on demand where a
`Re-read ·` row would otherwise be owed, and never by a bulk pass from a
feature branch. `fold_check.py`'s own resolver of `Enforced by:` targets is
removed in favour of the ledger's. `spec.md` holds the decisions D1–D8 and
the fourteen scenarios; this file holds the order they are built in.

**Reframed 2026-10-12, after round 2, by the repository owner's decision**
(`spec.md` §*Reframed after round 2*). Phases 1–5 stand with their commits.
The half of phase 1 and round 1's fix that read a test file to predict what
pytest would collect and whether it could fail — `collected`, `never_fails`, · NAME NOT IN TREE
`unconditional` — is redesigned in phases 6–9: the static checker keeps only
that the file and the `def` or `class` exist (D2), the sealed run's pytest
record says whether each cited test ran and passed (D9), and the broad
gate's ledger arm hands that record to the checker (D10). A test row the
run did not hold is MALFORMED with the observation in its detail, and no
case anywhere names a `skip` or `xfail` spelling. Where no record exists the
checker reads existence and says so once. `spec.md` D9–D11 and S15–S23 hold
the decisions and the cases; this file holds the order.

## Technical context

Coordinates at 5623d728, all `read` by the framer.

- `skills/evidence-check/scripts/evidence_check.py#malformed_rows` (:2049)
  refuses a grounds cell that *cites no coordinate*: its second branch fires
  when `ANCHOR_RE` and `OLD_COORD_RE` both miss and another cell is not
  empty. A node-id-only cell is exactly that today. `#refused_coordinate`
  (:1930) does not refuse `path::name` — it partitions on `#` and `@`, and a
  node id has neither — so the token is prose to the present reader.
- `#grounds_cells` (:2019) is the one table walk over Code grounds cells,
  with the fragment's column index from `LEDGER_COLUMNS` (:1896). D3's
  reader goes through it.
- `#resolve_unit` (:614): for a `.py` path, `py_spans(text).get(locator, [])`;
  `#parsed_spans` (:479) keys a method as `Class.method`, which is why a
  node id's parts after the path join with `.`.
- `#check_ledger` (:1568) assembles the findings of one file: the body walk,
  the family findings, `old_format_rows`, `malformed_rows`, `overflow_rows`.
  The node-id findings join that list.
- `#family_view` (:2451): `superseded` is every root a `Corrected ·` row
  cites; a superseded family's coordinates are not graded; the correcting
  row's own line is graded as its own family, citation excluded
  (`if cite is not None and m.span() == cite.span(): continue`). A
  `Corrected ·` row with no code coordinate therefore has nothing to grade.
  `#left_alone` (:3064) keeps `--reverify` off a superseded family. Phase 2
  verifies both by a case rather than trusting this reading.
- `#reverify_into` (:4196) writes the `Re-read ·` rows and the summary.
- `#exit_code` (:5653): BROKEN → 2; MALFORMED → 1 leniently, 2 under
  `--strict`. Unchanged.
- `skills/settle/scripts/fold_check.py#target_problem` (:262) resolves an
  `Enforced by:` target with its own `ast.walk`; `#load` (:145) is how the
  module already loads `unverified_check.py`, `hooks/config.py` and
  `hooks/optin.py`. `tests/test_a_folded_statement_names_what_enforces_it.py`
  pins the detail text *no def or class named test_gone* (:161).
- `tests/test_evidence_check.py#vendored_copy` (:345) copies the checker
  alone into `tools/`; S12 runs there.
- `docs/the-evidence-ledger.md` is 547 lines against a 1,000-line ceiling;
  `#heading_path` (:567) ends a section at the next heading of its level or
  higher, so a section inserted between two changes neither region.

Coordinates at ec48b584, `read` by the framer at the reframe.

- `skills/verify/scripts/pytest_record/specseal_pytest_record.py`: the module
  docstring §*What it writes* defines the record; `#Recorder.pytest_runtest_logreport`
  (:296) writes one `test` line per report with `nodeid`, `when`, `outcome`,
  `path` and `category`; `#Recorder.category_of` (:312) asks
  `pytest_report_teststatus` as the terminal reporter does and writes `""`
  for a report pytest counts nowhere; `#pytest_configure` (:398) claims the
  key for the first session of the process.
- `skills/verify/scripts/broad_gate.py#recording_env` (:1878) hands a run
  the recorder; `#read_record` (:2014) keeps only files whose first line
  carries the key, and reduces a run to files; `#record_path` (:1949) is how
  a recorded path is named against the worktree; `#main` makes `head_key`
  (:3546), runs the suite under it and reads `head` (:3549–3552), then runs
  `checks[LEDGER]` (:3553) with `[py, EVIDENCE, "--strict", root]`. A
  preflight leaves `head` None. `#RAN_TO_ITS_END` (:2006) is where a stopped
  session is already judged.
- `skills/evidence-check/scripts/evidence_check.py#node_finding` (:2424)
  calls `collected` (:2332) and `never_fails` (:2390) after `named_unit` · NAME NOT IN TREE
  (:2308); `#held_by_tests` (:2479) is one caller, `#family_view`'s member
  loop (:3062) the second, `#reverify_into` through `held_by_tests` (:3894)
  the third. `#main` (:6177) is the argparse. `#unit_kinds` (:2300) records a
  kind per qualified name — `def`, `class`, `constant` — which is what D2's
  existence rule reads.
- `tests/test_a_ledger_row_is_held_by_its_test.py` :550–666 are the three
  collection cases D11 removes; :706–786 the document pins, five of which
  pin sentences D7's rewrite removes.
- `tests/test_the_recorder_writes_what_its_process_ran.py` drives the real
  recorder over planted suites; phase 7's cases do the same, so the
  checker's reader is read against a record the recorder wrote and never
  only against a hand-written fixture.
- `tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py` :17
  names `broad_gate.py`'s ledger call site as the place `--strict` is pinned;
  phase 8's pin of the two new argv items goes beside it or in the gate's
  own module.
- `.github/workflows/test.yml` :163–181: the `ledger` job runs
  `evidence_check.py .` leniently, with no pytest run before it, and its
  comment (:147–162) holds the owner's rule that it is not the reader that
  decides.

**Failure scenario of the reframed approach, in six months.** A test row
cites a test whose module the repository's broad row skips on the sealing
machine — a Windows-only module sealed on macOS. Every lenient run reads the
row OK for existence; the gate reads *skipped in the recorded suite* and
refuses the seal, and the sealer reports a refusal that is about a platform
rather than about a claim. That is the strict reading chosen on purpose
(`spec.md`'s Out table), and its cost is one hashed row or one seal taken
where the test runs. The quiet failure stays the first frame's: a `passed`
line for a test that asserts less than the row's prose says.

**Failure scenario of the chosen approach, in six months.** A test is
reworded to assert something weaker and its row's prose still describes the
stronger claim; nothing in the tree notices, because nothing holds the prose
to the test. That is the trade the issue asks for and the one `Enforced by:`
has run under since #565 with no issue filed. What catches it is review, and
what bounds it is that the test is named in the row, so a reader opens one
file. The other direction — a test deleted — is BROKEN at the next run.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A test node id alone in the grounds cell (chosen) | The reader of a row has to open the test to find the code; a test that names nothing is a bad test rather than a bad row | taken |
| A test plus a hash-less code anchor for the reader | `path#unit` with no `@hash` is MALFORMED under `refused_coordinate` today, so it is a grammar change in #867's five copies; a pointer that resolves but never drifts still breaks on a rename and owes a `Corrected ·` row, which is the bookkeeping coming back by another door | refused |
| A test plus a hashed code anchor, drift of the anchor reported as information | The row owes a re-read on every edit exactly as now; nothing is saved | refused |
| A third citing verb (`Held ·`) for the migration | A new copy of the supersede judgment in `family_view`, `correction_check.py`, `survivor_check.py` and `settle.py`, each of which reads `Corrected` today; the brief refuses a new copy where a reader exists | refused |
| `--reverify --into` writing the `Corrected ·` test row itself where the released row cites exactly one test unit | The tool guesses which of a row's grounds is the enforcer; a row may cite a test as one ground among several. The brief prefers a reader that refuses to one that guesses. The option is printed, not written | refused |
| A bulk pass over the 1,042 released rows citing a test, in this work item | Eleven branches in 0.21.0 edit the units those rows cite; two `Corrected ·` rows on one released row are each DRIFTED at the fold, so a bulk pass from a feature branch collides with every sibling | refused; `questions.md` Q1 |
| `evidence-check` running the named test | A 1.7 s per-commit advisor becomes a test run; a consuming repository's suite is its own job | refused |
| Any `def` or `class` accepted as the enforcer, as `fold-check` accepts | A row naming a unit that exists is a claim nothing checks, the state *cites no coordinate* already refuses | refused; the ledger accepts a test, `fold-check` keeps its wider acceptance |
| A mixed row allowed, its hashes graded as today | A row reads as migrated while still owing re-reads | refused |
| Editing §*A released row is read again…* to carry the rule | 9 released rows cite that section and would drift for prose | refused; a new section is inserted after it |
| *(reframe)* The static checker reads the sealed run's record for whether a cited test ran and passed (chosen) | A test the sealing machine skips refuses the seal there, and a row that loads no recorder is read for existence only; both are named in `spec.md` §*What the observation cannot see* | taken |
| *(reframe)* Keeping the test file's marks and names as a static prediction, with round 2's `level`/`LEVEL_NODES` fix | Each round found another spelling (two rounds, nine spellings); a module-level `pytest.skip`, a `skipif` whose condition is true, a conftest's `pytest.skip`, a `-k` and a `--deselect` are each unreadable from the file. The owner judged the list a cover-up · NAME NOT IN TREE | refused |
| *(reframe)* `evidence-check` reading the newest record under the kept output when one is present | Which run's record is newest is an inference from a file's `mtime`: the gate keys each run fresh so a reader passes every other key over (`record_key`), and *newest* reads by position where #825 ended reading by position | refused |
| *(reframe)* The sealer reading the record and judging the test rows itself | `agents/sealer.md`: the sealer runs the gate and judges nothing; a judgment there is a second reader of the ledger with no record of its own | refused |
| *(reframe)* The gate reading the ledger's node ids itself against `RunRecord` | The gate parses no ledger, and `RunRecord` holds files; the checker is the one reader of a ledger row, and a second one is #834's refused copy | refused |
| *(reframe)* Keeping the `test…` / `Test…` prefix and the `test_*.py` name as a static default, dropping only the marks | The prefix is a prediction of `python_functions`' default: it refuses a row the record would hold in a repository with other names, and holds one the record would refuse — a `test_` function pytest deselected or never collected · NAME NOT IN TREE | refused |
| *(reframe)* A new verdict word (`UNHELD`) for a test the run did not hold, or a word on the totals line | `exit_code`, `classify`, two wrappers and the CI job read the verdict words; MALFORMED already means *cites nothing that holds* and is what round 1's fix used for this meaning. The observation goes in the detail | refused |
| *(reframe)* `skipped` and `xfailed` as OK, *left to the reader* | Round 1's 🟡 2 by another door: a test the sealing machine skips holds nothing there, and an `xfail` leaves the suite green whatever the code does | refused |
| *(reframe)* The gate writing a digest of the record for the checker | A third format for one observation, with its meaning defined in a second place; the record is already a format this plugin owns | refused |
| *(reframe)* One shared reader of the record, the checker loading `broad_gate.py#read_record` | The checker ships alone through `evidence-ci`, and `read_record` reduces a run to files where the ledger needs node ids. The second reader reads four fields, and S19 reads one record with both | refused |
| *(reframe)* A lenient ledger step in CI's ubuntu pytest leg, reading that leg's record | CI's `ledger` job is the lenient reader by the owner's rule, so the step could warn and never decide; whether a warning at the pull request is worth one more step in a job branch protection reads is the owner's. The build runs either way | deferred to `questions.md` Q7, default *no* |

## Phases

Vertical slices — each phase ends with something runnable and verified. The
new test module's file name is the build's to choose; `spec.md`'s
scenarios call it *the new module*.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The reader: one new function in `evidence_check.py` that reads node ids from the Code grounds cell through `grounds_cells`, resolves each through `resolve_unit`'s Python branch with the parts joined by `.`, and grades OK / BROKEN / MALFORMED as D2 says; `malformed_rows` no longer refuses a node-id-only cell and refuses a mixed one (D4); `malformed_remedy` names the two forms; `check_ledger` adds the findings. S1–S6, S8 (the `--reverify` half), S11, S12 | the new module, each case seen red against the unfixed checker and the way it was shown recorded in `phases/phase-1.md`; `tests/test_evidence_check.py` and `tests/test_a_released_row_is_read_again_in_a_fragment.py` green unchanged | 48d201ad |
| 2 | The migration path: S7 as a case (a `Corrected ·` row with citation and node id supersedes, an edit to the root's unit produces no finding, `--reverify --into` writes no `Re-read ·` row for it), and S9's one summary sentence in `reverify_into`, pinned. If S7 needs a change in `family_view` or `left_alone`, the change is one branch and `phases/phase-2.md` says which | the cases, red with the superseding removed and with the sentence deleted | 5c24f534 |
| 3 | One resolver: `fold_check.py#target_problem` loads `evidence_check.py` through `load` and asks it; the `ast.walk` branch is removed; S10's method spelling; the pins in `tests/test_a_folded_statement_names_what_enforces_it.py` updated in the same commit; the 451 targets under `docs/` measured green by `fold-check` | that module red with the old resolver restored; `fold-check` over the tree green | 4b5eef0c |
| 4 | The documents (D7): the new section in `docs/the-evidence-ledger.md` with `Enforced by:` lines naming phases 1–3's cases, `templates/ledger.md`'s two forms, the two sections of `skills/evidence-check/SKILL.md`, and `skills/evidence-ci/SKILL.md` §*Updating later*; a pin per changed sentence; the text hygiene modules green | `fold-check`; the pins red with the sentence removed; `tests/test_docs_line_wrap.py` and the five text hygiene modules green | aae8f2bd |
| 5 | This item's records (D8): the fragment's test rows for S1–S13, the citing rows for every released row phases 1–4 drifted — per row the `Corrected ·` test row or the `Re-read ·` row, chosen by reading (Q3) — `changelog.md`, and `overview.md` | `evidence-check --strict .` 0 drifted, exit 0, executed and its output in `phases/phase-5.md` | 124cd1a6 |
| 6 | *(reframe)* The static reader keeps existence (D2, D11): `collected`, `TEST_FILE_RE`, `never_fails`, `unconditional`, `NEVER_FAILS`, `NEVER_RUNS` and `node_finding`'s two calls leave `evidence_check.py`; a `def` or `class` defined once is OK, a constant and a name defined twice BROKEN; the three collection cases and `NEVER` leave the new module, the name-prefix cases of `test_a_unit_pytest_does_not_collect_is_no_test` become S4's OK cases, the constant case stays; `fold-check` stays green, since `named_unit` is untouched. S4 | the new module, S4's OK cases red against ec48b584 and every remaining case green; `bin/mutation-check` over `node_finding` with the module as its cases · NAME NOT IN TREE | 2b501fd8 |
| 7 | *(reframe)* The record reader (D9, and D10's checker half): the two options on `main`; a reader of the recorder's `test` lines keyed by the `session` line; the match by `record_path` and names prefix with `[…]` stripped; the held rule; the MALFORMED details naming the observation; the one existence line; `--reverify` and `--into` `LEFT` lines; the record threaded to `node_finding`'s three callers the way Q6 answers. S15–S20, S22, each over a record the real recorder wrote (`pytest -p specseal_pytest_record` with the recorder's two variables set, over a planted suite, as `tests/test_the_recorder_writes_what_its_process_ran.py` drives it) | the new module, red against the phase-6 checker (the options unknown; then each verdict OK where the record says otherwise); `tests/test_the_recorder_writes_what_its_process_ran.py` and `tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py` green unchanged; S17's `grep` over the checker's source for a mark name | 1a6aa945 |
| 8 | *(reframe)* The gate hands over the record (D10's gate half): `broad_gate.py#main` adds the record directory and `head_key` to `checks[LEDGER]` where the suite ran, and neither on a preflight; item 2 of the module docstring's list says what the arm now reads. S21 | the module that pins `checks[LEDGER]`'s argv, red with the two items missing; one `broad-gate` run over a planted repository whose test row names a test its row skips, NOT SEALED with the ledger arm named | 4136d3ba |
| 9 | *(reframe)* The documents and this item's records (D7, D8, D11, S23): statements 1 and 2 of `docs/the-evidence-ledger.md` §*A claim held by a test* rewritten, their `Enforced by:` lines naming phases 6–8's cases; the test-row paragraph of `skills/evidence-check/SKILL.md` §*Verdicts and what to do*; `templates/ledger.md` §*A row held by a test*; `skills/evidence-ci/SKILL.md` §*Updating later* (the vendored step reads existence; the observation needs the recorder in the repository's own test job); the pins, five removed and the new sentences' added; `changelog.md` rewritten for what ships now; the fragment's T4 and T15 rewritten and rows for S15–S22 added; `--reverify --into` for every released row phases 6–8 drift (`node_finding`'s and `main`'s families at least); `overview.md`'s divergence rows for the reframe and its Not done | `fold-check` exit 0; each pin red with its sentence removed; `evidence-check --strict .` exit 0 at the head, executed and its output in `phases/phase-9.md`; `survivor-check --range origin/release/v0.21.0...HEAD --exempt …` exit 0 over the removed sentences; the eight guard modules green | |

**Order, and why.** Phase 1 before 2 because S7's `Corrected ·` row holds a
node id the reader must accept first. Phase 3 after 1 because it imports
what 1 writes. Phase 4 after 3 because its `Enforced by:` lines name cases
that must exist. Phase 5 last because it reads the hashes phases 1–4 leave.

**The reframe's order.** Phase 6 before 7 because 7's OK rule is 6's
existence rule plus the record, and 6's removals are what make 7's cases
red for the right reason (OK where the record says otherwise, not MALFORMED
by a mark). Phase 8 after 7 because the gate passes options the checker must
already accept, and a gate run over a planted repository is 8's own case.
Phase 9 last because its `Enforced by:` lines name 6–8's cases and its
`--strict` run reads the hashes they leave. The documents are not touched
before 9, so that `survivor-check` reads one range.

**Sequencing with the siblings.** #867 and #870 edit `evidence_check.py`;
`spec.md` §*The seam* names the units this item changes and the ones it
only reads. Whichever of the three lands second in `release/v0.21.0` merges
the release branch in and re-runs phase 5's `--strict`; the conflict
surface is `malformed_rows` and `check_ledger`, which #867 may touch for the
grammar and #870 should not.

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.
The evidence ledger had the same problem and no such tolerance. It no longer
has it at all: a ledger row names a symbol and a content hash, so there is no
commit in it for a rebase to orphan.

## Operational impact

- **No migration of any released file.** The freeze stands; released rows
  move onto their tests one `Corrected ·` row at a time, on demand.
- **A consuming repository changes nothing** until it writes a test row,
  and then it updates its vendored `tools/evidence_check.py` first, or the
  older copy refuses the row as MALFORMED (`skills/evidence-ci/SKILL.md`
  §*Updating later*). No new environment variable, no new dependency.
- **What a gate prints changes in two places**, each pinned: the new
  MALFORMED and BROKEN details for a node id, and one summary sentence of
  `--reverify --into`.
- **Prompt budget: zero.** Nothing here asks a person anything; every new
  verdict is a refusal a person reads at exit 1 or 2.
- **Failure direction: blocks more**, on rows that do not exist in any
  ledger today (measured: no Code grounds cell holds a `path::name` token).

At the reframe:

- **`evidence-check` gains two options**; a caller that passes neither sees
  the D2 verdicts and one more line where a ledger holds test rows. The
  post-commit advisor and CI's `ledger` job print that line on every run
  over this repository, whose fragment holds test rows; it is one line, and
  it is what keeps an existence-only OK from reading as an observed one.
- **The gate's ledger arm refuses a seal where a cited test did not pass in
  the sealed run** — not run, skipped, xfailed, xpassed, failed — including a
  `skipif` true on the sealer's machine. Failure direction: blocks more.
  Prompt budget: zero.
- **What a gate prints changes in three places**, each pinned: the MALFORMED
  detail for a test the record refuses, the existence line, and the
  `LEFT` line of `--reverify` for such a row. The `MALFORMED` detail for a
  unit *pytest does not collect by default* and for a mark leave.
- **A consuming repository's vendored copy reads existence**; the observation
  needs the recorder in its own test job and the record handed to the step,
  which `skills/evidence-ci/SKILL.md` §*Updating later* says and
  `evidence-ci` does not set up (the Out table).
- **No new dependency, no new environment variable**: the recorder's two
  variables and its `-p` are the gate's already.
