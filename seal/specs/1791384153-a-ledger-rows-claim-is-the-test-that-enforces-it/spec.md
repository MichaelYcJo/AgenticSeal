# Feature Specification: a ledger row's claim is the test that enforces it

<!-- seal/specs/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it/spec.md — WHAT this work delivers and how we'll know.
The policy documents in docs/ outrank this file; cite them, don't restate.
Issue #836 and its reopen comment. Record language: English (seal/config.md
has no `Record language` row). Every coordinate below was opened by the
framer at 5623d728 (0.20.0 as shipped) unless it says otherwise; every count
is labelled with how it was taken. -->

## Reframed after round 2 — the collection half observes

The repository owner's decision of 2026-10-12
(`seal/specs/1791382684-every-reader-and-record-is-inventoried/handoff.md`
§*Review of the run* and §*What the owner decided*, read on branch
`chore/834-every-reader-and-record-is-inventoried`): 0.21.0's theme is that
a reader observes, forces a format, or is deleted, and the half of this item
that read a test file to predict whether pytest would collect a test and
whether it could fail was a guessing reader patched round by round.
`collected`, `unconditional` and `never_fails` in `evidence_check.py` each · NAME NOT IN TREE
learned a spelling per round — round 1: a non-test file, `conftest.py`, a
class with `__init__`, an unconditional `skip` or `xfail`, `pytestmark`;
round 2: `xfail(condition=…)`, `strict=True`, a mark under an `if`,
`pytestmark +=`, a module-level `pytest.skip` — and the owner judged the
list a cover-up. It is not a fix-of-a-fix count: round 2's `Fix of a fix`
reads `first`. That half is redesigned here. **The test-row half — D1,
D3–D6, S1–S3, S5–S14 — predicts nothing and stands as built in phases 1–5.**

What moves, and where the rest of this file says it:

- **D2 is rewritten.** The static checker keeps only what reading a file
  establishes for certain: the file is there and a `def` or `class` of that
  qualified name is defined in it once. Every name-reading and mark-reading
  unit leaves (D11).
- **D9 and D10 are new.** Whether a cited test ran, and how it ended, is
  read off the record #869's pytest recorder writes during the sealed run
  (`skills/verify/scripts/pytest_record/specseal_pytest_record.py`), and the
  broad gate's ledger arm hands that record to the checker. Nothing about a
  test is predicted from its file any more.
- **§*What the observation cannot see*** names where no record exists — CI's
  `ledger` job, a preflight, a vendored copy — and what the checker says
  there.
- Round 2's three findings are closed `deferred the frame` at ec48b584 and
  are answered by D9: each named spelling is now a line of the record, or no
  line, and no case names a spelling.

Every coordinate this section and D9–D11 add was opened by the framer at
ec48b584 (the branch's head at the reframe); the rest of the file keeps its
5623d728 readings, which phases 1–5 built against.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `docs/the-evidence-ledger.md` §*A row is a content anchor, and it names no commit* | A coordinate is `path#major[>minor]@hash`, it degrades to DRIFTED and never to BROKEN below the major level, and a row with no coordinate cites nothing. This work adds a second row form beside that one and changes nothing in it: a row held by a test carries no hash, so nothing in it can drift |
| `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment* | A `Corrected ·` row supersedes the family of the row it cites, whose coordinates are not checked again, and starts a family of its own; a released row is never removed. That is the whole migration mechanism (D5): a `Corrected ·` row whose grounds hold the citation and the test, and no code coordinate, is a family nothing can drift. No new verb and no new reader is needed to supersede |
| `docs/the-record-layout.md` §*A change writes fragments, never a shared file*; `templates/config.md` §*The ledger freeze* | A released file never changes, so no released row is rewritten into the new form. Every row this work writes goes to `seal/ledger/1791384153-a-ledger-rows-claim-is-the-test-that-enforces-it.md` |
| `skills/settle/SKILL.md` §*2. Write one standing statement per segment* (the `Enforced by:` line) and `skills/settle/scripts/fold_check.py#target_problem` | The grammar `path::name` and its resolution — the file exists, `::name` is a `def` or `class` in it — already exist for a folded statement. This work gives a ledger row the same grammar and gives the two readers one resolver (D6). The issue's sentence *`Enforced by:` already names that test* is this clause |
| `CONTRIBUTING.md` §*What a change to a gate must carry* | `evidence-check` is a gate: the broad gate runs it with `--strict`, CI's evidence job runs it, and the post-commit advisor prints it. Each verdict this work changes carries a case seen red (§*Scenarios*), a failure direction (§*What drifting means*: every new refusal blocks more), and a prompt budget of zero — nothing here asks a person anything |
| `CLAUDE.md` §*The goal a design is chosen against — verification that runs unattended* | A row held by a test is verified by the suite with nobody at the keyboard. A hashed row is verified by a person re-reading the claim, and #834 part 7 measured that reading at 84 % of the rows landed since 0.18.0. Between the two forms, this goal decides |
| `skills/agent-contract/SKILL.md` §12, §14, §15 | Each defect is fixed across its class; every changed sentence a person reads is pinned in the same commit; every new case is seen red before it is committed |
| #834's inventory, part 7 (`seal/specs/1791382684-every-reader-and-record-is-inventoried/inventory/7-records.md`, read on the `chore/834-…` branch) and the framer brief's three rules | The input is owned (pytest's own node-id spelling), the unknown is refused (a mixed row, a name no test runner collects, a method not spelled the way pytest spells it), and what goes is named (D6: `fold_check.py`'s own `ast.walk` resolver) |
| `skills/verify/scripts/pytest_record/specseal_pytest_record.py`, its module docstring §*What it writes*, and `#Recorder.pytest_runtest_logreport`, `#Recorder.category_of` (reframe) | The record's format is this plugin's own: one JSON Lines file per pytest process, a `session` line carrying the run's `key`, and a `test` line per report carrying `nodeid`, `when`, `path` — absolute, the node's own, never rebuilt from a node id — and `category`, the word pytest's own summary counts the report under: `passed`, `failed`, `skipped`, `xfailed`, `xpassed`, `error`, `""` for a report pytest counts nowhere (a passed setup or teardown). D9 reads those fields and no other, and derives no rule of pytest's: it matches the words pytest wrote |
| `skills/verify/scripts/broad_gate.py#recording_env`, `#read_record`, `#record_path`, and `#main` — `head = read_record(records_dir(keep), head_key, root)` followed by `checks[LEDGER] = run(LEDGER, [py, EVIDENCE, "--strict", root], …)` (reframe) | The gate holds the head run's record directory and key at the moment the ledger arm runs, and a preflight runs no suite (`head` is None). D10 hands both to the arm, and the gate's order does not change. `record_path` is how a recorded path is named against the worktree — `realpath` on both sides, relative, `/`-spelled — and D9 names a path the same way |
| `templates/config.md` §*Broad gate*, rule 3 (read, not edited: 57 coordinates cite the section) (reframe) | Which rows load the recorder and which do not (`tox`, `nox`, `env -i`, a replaced `PYTEST_ADDOPTS`), and what a row that does not earns: no record, `new?`. D10's *no keyed session* rule is that case for the ledger arm |
| `.github/workflows/test.yml`, the `ledger` job and its comment *This job is the LENIENT reader, and it is not the one that decides* (reframe) | CI's ledger job runs without a pytest run, leniently, by the owner's answer of 2026-09-26; the reader that decides is the gate. So the observation decides in the gate, and CI's job reads existence as it does today (§*What the observation cannot see*; `questions.md` Q7 is whether CI should observe too) |
| `seal/specs/1791382684-…/handoff.md` §*What the owner decided*, items 1 and 3 (reframe) | The reframe is the owner's, against the theme; Q1 stays at (a) until this item lands |

## What the inventory measured, re-read for this frame

Every number here is `read` from part 7 or re-derived by the framer with the
command beside it, at 5623d728. None was executed as a test.

- **84 % of the ledger rows landed since 0.18.0 are bookkeeping.** Of 993
  rows in `seal/releases/0.18.1.md` through `0.20.0.md`, 712 are `Re-read ·`
  and 123 `Corrected ·`; 158 are new claims (part 7, footnote [d]).
- **A re-read re-triggers itself.** A `Re-read ·` row is anchored on the
  unit it re-read, so the next edit to that unit drifts the family again.
  `evidence_check.py#reverify` is cited by 84 bookkeeping rows and 21 claim
  rows; `templates/config.md#"## Broad gate"` by 57 coordinates in all
  (part 7 §*Observations*; re-derived: `grep -c 'evidence_check.py#reverify@'`
  over the claim rows of every released file → 21).
- **The claims already name their tests.** Of 1,308 claim rows in
  `seal/ledger.md` and `seal/releases/*.md` (rows that are neither
  `Re-read ·` nor `Corrected ·`), 1,048 cite a `tests/*.py#<unit>@<hash>`
  coordinate, and 139 cite nothing but test units (framer's count, a
  `re.split` on unescaped pipes over the Code grounds cell). So for most rows
  the test that holds the claim is already in the row — as a hash that drifts
  whenever the test is edited.
- **The cheapest record drifts nothing by construction.** `# RIDER:` comments
  share the ledger's anchor and hash with no families and no freeze: 20 at
  0.18.0, 20 now, 0 drifted (part 7 row 11). What they show is not that a
  hash is cheap — a rider's drift is the rider firing, which is its purpose —
  but that a record whose purpose is served by one stamp costs one stamp. A
  ledger row's purpose is the claim holding, and the instrument for that is
  a test, not a reading.
- **`Enforced by:` is held by name only and has cost nothing.** 451 targets
  under `docs/` (framer's count: every comma-separated target on an
  `Enforced by:` line that is not `nothing`): 431 are a top-level `def` or
  `class` with a unique name, 20 name a file alone, 24 name a unit that is
  not a test (`fold_check.py::bound` and the like), 0 are nested, 0 are
  missing. Zero issues since 0.18.0 are about it (part 7, the by-mechanism
  table).
- **The `path::name` spelling already appears in 16 claim rows, and in no
  Code grounds cell.** 9 sit in Verified behavior and 7 in Notes (framer's
  count). D3's reading of the grounds cell alone therefore changes no
  existing row's verdict.

## Scope

**In.** Eleven decisions, each from the tree. D2 is as the reframe rewrote
it; D9–D11 are the reframe's.

**D1. A second row form: the claim is held by a test.** A ledger row's Code
grounds cell may hold, instead of coordinates, one or more test node ids in
pytest's own spelling — `tests/test_x.py::test_y` for a function,
`tests/test_x.py::TestA::test_b` for a method — each in backticks, comma
separated, and nothing else. The Clause is then a description that nothing
holds to the code, which is what the issue asks for and what `Enforced by:`
already is under `docs/`. The Verified behavior cell holds how the test was
seen red (`skills/agent-contract/SKILL.md` §15), and Checked holds the date
it was seen red then green. The row's claim is the test passing. A hashed
row is still written for a claim no test holds.

**D2. What the static checker reads of such a row, and what it says
(rewritten at the reframe).** Each node id is resolved through
`evidence_check.py#named_unit`: the path is a `.py` file in a checkout the
run reads, and the names after the path, joined with `.`, are the qualified
name `unit_kinds` keys on. It is **OK** when a `def` or `class` of that name
is defined in that file once; **BROKEN** when the file or the unit is not
there, naming which — a constant of that name is no `def` or `class` and is
told so — and for a method written bare (`path::test_b` where `test_b` lives
only inside a class) saying that a method is written `path::Class::method`,
and when the name is defined more than once; **MALFORMED** when the token
does not parse as a node id, with a remedy naming the two forms. It is never
DRIFTED: there is no hash. **That is all reading the file establishes for
certain, and it is all the static reader says.** Whether the unit is a test,
whether pytest collects it, whether a mark keeps it from running or from
failing — none of it is read off the file: each is a prediction of pytest,
and a predicting reader learns a new spelling every round (the reframe
section lists the ones this one learned). The sealed run's record answers
every one of them by observation (D9). So a `def helper` in
`tests/helpers.py`, a `conftest.py` function and a method of a class with an
`__init__` each resolve here, and are refused there, where the record shows
they did not run. A resolved node id counts among `ok` on the totals line;
nothing new is printed there.

**D3. Where it is read: the Code grounds cell, and nowhere else.** The node
ids are read per row through `grounds_cells`, the one table walk, never over
the whole body the way `ANCHOR_RE` is read, because `a::b` is a spelling
prose uses — a C++ scope, a Rust path, a quoted `Enforced by:` line — and a
coordinate is unambiguous by its `#…@hex` shape where a node id is not. The
16 tokens that already sit in Verified behavior and Notes stay prose.

**D4. A row is one form or the other.** A Code grounds cell holding both a
node id and a code coordinate — any `ANCHOR_RE` match other than a citing
row's citation — is MALFORMED, with a remedy naming the two forms. Allowing
the mix would let a row say *held by a test* while still owing a re-read on
every edit, which is the half-form that keeps the bookkeeping while looking
migrated. A grounds cell holding node ids and no coordinate is no longer the
*cites no coordinate* MALFORMED of `malformed_rows`. The citation a
`Corrected ·` or `Re-read ·` row opens with is a ledger line, not code, and
is not a coordinate for this rule — `family_view` already grades it apart.

**D5. A released row migrates by one `Corrected ·` row, on demand, and
never in bulk by a feature branch.** Under the freeze a released row is
never edited. Its claim moves onto its test by a `Corrected ·` row in the
branch's fragment whose grounds hold the citation and the node ids and no
code coordinate, and whose Notes carry `Corrected <date> by work item <id>:
held by its test from here on`. Nothing in the checker changes for this to
work: `family_view` supersedes the cited family (its coordinates are not
checked again), and the correcting row's own family carries no code
coordinate, so no later edit drifts it. It is written by the branch whose
edit drifted the row, at the moment `--reverify --into` would otherwise
write a `Re-read ·` row for it, and the smith chooses per row by reading: a
claim the cited test holds takes the `Corrected ·` test row; a claim no test
holds takes the `Re-read ·` row as today. `--reverify --into` names the
option once per run, in its summary line, unconditionally — it does not
guess which test holds a claim. A bulk pass over the 1,042 released rows
that cite a test is a person's decision (`questions.md` Q1), and its
vehicle, if taken, is a fold fragment at a release
(`docs/the-evidence-ledger.md` §*A fold is not a work item*), because two
feature branches correcting one released row in one release are each
DRIFTED at the fold by the existing rule.

**D6. One reader for `path::name`, and `fold_check.py`'s own goes.**
`fold_check.py#target_problem` loads `evidence_check.py` the way it already
loads `unverified_check.py` and `hooks/config.py` through `fold_check.py#load`,
and asks it to resolve the target. Its own `ast.walk` resolver is removed:
that is the copy this frame names as going. What each caller accepts stays
the caller's: `fold-check` accepts a file alone, any `def` or `class`, as
it does today (the 451 targets resolve exactly as before — 0 are nested,
so the move from `ast.walk` to `py_spans`'s top-level and qualified names
changes no answer); the ledger accepts a test. Grammar and resolution are
one function; acceptance is one line in each caller.

**D7. The documents.** A new section in `docs/the-evidence-ledger.md`, placed
after §*A released row is read again in the branch's fragment* and before
§*What the checker refuses*, so that no existing section's region changes
(`heading_path` ends a region at the next heading of its level or higher;
inserting a section between two leaves both regions byte-identical — 9 and
3 released rows cite the two neighbouring sections). It states D1–D5 as the
rule, with `Enforced by:` lines naming the cases. `templates/ledger.md` shows
both row forms. `skills/evidence-check/SKILL.md` §*Verdicts and what to do*
gains the test row's verdicts and §*Re-verifying is recomputing the hash*
says what the run leaves alone (4 and 2 released rows cite those sections;
the re-reads are this item's). `skills/evidence-ci/SKILL.md` §*Updating
later* says that an older vendored copy refuses a test row as MALFORMED, so
a repository updates the copy before writing one, and that the step reads
whether the test exists while the repository's own test job judges whether
it passes.

**D8. This item's own records are the first test rows.** Its fragment holds
a test row per scenario below. The released rows its edits drift
(`evidence_check.py#malformed_rows`, `#grounds_cells`, `#malformed_remedy`,
`#check_ledger`, `#reverify_into`, `fold_check.py#target_problem`, and the
two skill sections — 2, 3, 1, 0, 6, 2, 4 and 2 claim rows at 5623d728, the
bookkeeping rows citing them on top) get, per row, the `Corrected ·` test
row or the `Re-read ·` row of D5, chosen by reading (`questions.md` Q3).

**D9. Whether a cited test ran, and how it ended, is read off the sealed
run's record — never predicted from the file.** Given a record — a directory
of the recorder's `*.jsonl` files and the key of one run (D10) — the checker
reads, from every file whose first line is a `session` line carrying that
key, each `test` line's `path`, `nodeid`, `when` and `category`, and nothing
else of the record. A cited unit's lines are the lines whose `path` names the
cited file — `realpath` made relative to the root and spelled with `/`, as
`broad_gate.py#record_path` names a file — and whose node id's parts after
the first `::`, with a parametrise suffix `[…]` stripped from the last, begin
with the cited parts: `tests/test_x.py::test_y` owns `test_y` and
`test_y[case]`, `tests/test_x.py::TestA` owns `TestA::test_b`, and one prefix
rule covers a class and a parametrised function. Never a path rebuilt from a
node id and a rootdir: pytest makes the node id from the path by a rule
#825's five rounds could not enumerate, and the recorder writes the path for
exactly that reason. The cited test is **held** where at least one of its
lines carries the category `passed` and no line carries any other non-empty
category (`""` is a passed setup or teardown); the row is OK. Otherwise it is
**MALFORMED**, and the detail names the observation: *not run in the
recorded suite* where it owns no line — a unit pytest did not collect (a
`def helper`, a `conftest.py`, a class with `__init__`, a module skipped at
collection), or a `-k` or a shard that left it out; *skipped in the recorded
suite* where its lines say `skipped` (a `skip`, a true `skipif`, in any
spelling); *xfailed* or *xpassed in the recorded suite* where they say so (an
`xfail` mark, conditional or not, leaves the suite green whatever the code
does, and a non-strict `xpass` is that mark on a test that happened to
pass); *failed* or *error in the recorded suite* where they say so, which the
suite arm already fails. In every case the remedy is the one `NOT_A_TEST` · NAME NOT IN TREE
gives today: name a test that holds the claim, or write `path#anchor@hash`
where none does. The categories are pytest's own words, asked of
`pytest_report_teststatus` by the recorder the way pytest's terminal reporter
asks it; the checker matches them and derives none. A unit that is not a
test, or a mark in a spelling nobody has met, needs no new case: it is a line
that is not `passed`, or no line.

**D10. The broad gate's ledger arm hands the checker the head run's record;
everywhere else the checker reads existence and says so.** `evidence-check`
gains two options, a record directory and a run key — `--suite-record DIR
--suite-key KEY` in this file's spelling; the build may choose the words —
and `broad_gate.py#main` passes `records_dir(keep)` and `head_key` on
`checks[LEDGER]` wherever it ran the suite, which is every run but a
preflight. The checker then reads every test row of every ledger it reads
against that record (D9). Given no record — the CI `ledger` job, a preflight,
the post-commit advisor, a vendored copy whose repository hands it none, a
`--reverify` typed by hand — the test rows are read by D2 alone, and the run
prints one line, once, where it prints its totals, saying that its test rows
were read for existence and no suite record was given; a ledger with no test
row prints no such line. Given a directory and key under which no `session`
line is found — the row loaded no recorder (`templates/config.md` §*Broad
gate* rule 3 names the ways), or the directory cannot be listed — the
checker reads as given no record and the line names the key: the strict
reading of an absent record would refuse every test row of a repository
whose row never ran the recorder, which is a refusal about the row and not
about any claim; the gate prints the checker's line on its own output, so
the sealer is told the row is unmeasured (corrected in round 3's fix pass,
⬜ 7: the gate's `new?` says so only on a failing run). `--reverify` and `--reverify --into` take the same options and
name a row the record refuses on a `LEFT` line, as they name one whose test
is gone today; they write nothing on it and date nothing. The record is read
once per run and reaches `node_finding`'s three callers — `held_by_tests`,
`family_view`'s member loop, and `reverify_into` through `held_by_tests`;
how it is threaded is `questions.md` Q6, the work's.

**D11. What leaves the tree.** In `evidence_check.py`: `collected`,
`TEST_FILE_RE`, `never_fails`, `unconditional`, `NEVER_FAILS`, `NEVER_RUNS`, · NAME NOT IN TREE
the two calls in `node_finding` and its detail *a `def` that reads as a
test*. In `tests/test_a_ledger_row_is_held_by_its_test.py`:
`test_a_test_the_suite_does_not_collect_holds_nothing`, · NAME NOT IN TREE
`test_a_test_that_cannot_fail_holds_nothing`, · NAME NOT IN TREE
`test_a_conditional_mark_is_left_to_the_reader`, the `NEVER` constant, the · NAME NOT IN TREE
name-prefix cases of `test_a_unit_pytest_does_not_collect_is_no_test` (a · NAME NOT IN TREE
`def` not named `test…` and a class not named `Test…` now resolve; its
constant case stays, as BROKEN), and the pins of every sentence D7's rewrite
removes. Round 2's paste-ready `level`, `LEVEL_NODES` and the `unconditional` · NAME NOT IN TREE
rewrite are never written. In the documents: every sentence saying what
*reads as a test without running pytest* and every sentence about marks —
`docs/the-evidence-ledger.md` §*A claim held by a test*, statements 1 and 2;
`skills/evidence-check/SKILL.md` §*Verdicts and what to do*, the test-row
paragraph; `templates/ledger.md` §*A row held by a test*, its last two
sentences; the matching sentences of `changelog.md`. In this item's
fragment: T15 whole, and T4's clause about a unit pytest does not collect by
default. Nothing released cites any of these — all were added by this branch
in phases 1–5 and round 1's fix (read at ec48b584: `grep` over
`seal/releases/*.md`, `seal/ledger.md` and `seal/ledger/*.md` finds no
coordinate `#<name>@` naming any of the six) — so their removal owes
no `Corrected ·` row, and `survivor-check` over the range is what shows the
removed sentences stand nowhere else.

**Out, each with its grounds.**

| Cut | Grounds |
|---|---|
| A hash-less code pointer beside the test (`path#unit` with no `@hash`) | A grammar change: `ANCHOR_RE` requires the hash, `refused_coordinate` names a bare `path#unit` MALFORMED today, and the coordinate grammar's five copies are #867's. A pointer that only resolves would also be bookkeeping again: a rename breaks it and owes a `Corrected ·` row. The test names the code it reads, which is one hop |
| A third citing verb (`Held ·`) | `Corrected ·` already supersedes a family, and its readers — `correction_check.py#dropped_corrections`, `survivor_check.py#corrected`, `settle.py#anchored_rows`, `family_view` — stay unchanged. A new verb is a new copy of the supersede judgment in each of them, which #834's brief refuses |
| `evidence-check` running the named tests | The post-commit advisor runs the checker in about 1.7 s; a run that spawns pytest is a different tool. The suite judges a test; the broad gate here runs `bin/test -q` and `--strict` together, and a consuming repository's test job does the same |
| A bulk re-homing of the released rows | `questions.md` Q1; D5 says why a feature branch never does it |
| Reading pytest's naming configuration (`python_functions`, `python_classes`) | Reading a config to decide what is a test is a guess from text this checker does not own; the default names are pytest's own. A repository with other names writes a hashed row, and the new section says so as a known limit. This repository declares no override (read: `pyproject.toml`) · NAME NOT IN TREE |
| A parametrised node id (`::test_y[case]`) | Not a `def`; the row names the function |
| `CONTRIBUTING.md` §*House rules*, `seal/README.md`, `CLAUDE.md` | Each links to `docs/the-evidence-ledger.md` as the home and states no rule this changes; 6 and 2 released rows cite the first two, and an edit would drift them for nothing |
| `correction_check.py`, `settle.py`, `rider_check.py`, `survivor_check.py`, `fold_ledger.py` | None reads a node id; a `Corrected ·` row holding one is to each of them what one holding prose is. The coordinate grammar copies in the first three are #867's |
| The totals line gaining a word (`N held by tests`) | A new word on a line two wrappers and the CI job read is a change to what a gate prints with no reader asking for it; `grep -c '::'` over the ledgers is the count |
| `hooks/evidence-advisor.py` | It prints the checker's output. Whether it carries a repair sentence of its own that must learn the form is `questions.md` Q4, the work's |
| *(reframe)* CI's `ledger` job, or the ubuntu pytest leg, reading its own record | The job is the lenient reader by the owner's answer of 2026-09-26 (`test.yml`'s comment above it), so an observation there could warn and never decide; the deciding reader is the gate, which has the record. Handing the ubuntu leg's record to a step is one more shape in a job branch protection reads. `questions.md` Q7, a person's, default *no*; it does not block the build |
| *(reframe)* A new verdict word for a test the run did not hold, or a word on the totals line | `exit_code`, `classify`, the two wrappers and the CI job read the verdict words. MALFORMED already means *the grounds cell cites nothing that holds*, is graded 1 leniently and 2 under `--strict`, and is the word round 1's fix used for this meaning; the detail names the observation |
| *(reframe)* One shared reader of the recorder's format — the checker loading `broad_gate.py#read_record` | The checker ships alone (`evidence-ci` vendors it without the gate), and `read_record` reduces a run to files where D9 needs node ids. The second reader reads four fields of a format this plugin owns and its recorder's docstring defines, and S19 runs the real recorder so that both readers are read against one record |
| *(reframe)* `skipped` or `xfailed` read as OK, *left to the reader* | Round 1's 🟡 2 by another door: a test the sealing machine skips holds nothing on it, and an `xfail` leaves the suite green whatever the code does. A claim the sealed run did not verify is unverified; the row is hashed instead, or the seal is taken where the test runs |
| *(reframe)* Keeping the `test…` / `Test…` name prefix, or `test_*.py`, as a static default | The prefix was a prediction of `python_functions`' default, the same class as the marks, and the record makes it needless: a repository that names its tests otherwise has them in the record, and a `test_` function pytest deselected is not. The earlier row refusing to read pytest's configuration stands, now with no default to read either · NAME NOT IN TREE |
| *(reframe)* The gate writing a digest of the record for the checker | A third format for one observation; the record is already a format this plugin owns, and a digest is a second place its meaning is defined |
| *(reframe)* `evidence-ci` vendoring the recorder beside the checker | A consuming repository that wants the observation loads the recorder in its own test job and hands the record to the step; whether `evidence-ci` should copy the recorder for it widens that skill with no asker yet. `skills/evidence-ci/SKILL.md` §*Updating later* says what the vendored step reads without one |
| *(reframe)* `templates/config.md` §*Broad gate*, `.github/scripts/release_seal.py`, `publish-release.yml` | 57 coordinates cite the config section; the gate's own docstring (item 2 of its list) and `skills/evidence-check/SKILL.md` carry the sentence instead. The release job runs the suite with the recorder for the seal's counts, and running the checker against that record there is the CI question above |

## What drifting means after this work

The failure direction of every new verdict is *blocks more*: a MALFORMED or
BROKEN finding where today's checker finds nothing, at exit 1 leniently and
2 under `--strict` for MALFORMED, and 2 either way for BROKEN, as
`exit_code` already grades them. No new verdict reads a mixed, mis-spelled
or non-test row as OK.

| | A hashed row (today's form, unchanged) | A row held by a test (D1) |
|---|---|---|
| OK | every coordinate's hash matches its unit, or a newer reading in its family holds it | every node id resolves to one `def` or `class` (D2), and — given the sealed run's record — each was seen `passed` and nothing else (D9) |
| DRIFTED | a cited unit changed; a person re-reads the claim | never — there is no hash |
| BROKEN | a unit or file is gone; a `Corrected ·` row re-points or retires | a test or file is gone, a method is spelled bare, or the name is defined twice; a `Corrected ·` row re-points |
| MALFORMED | a coordinate nothing parses, or a grounds cell citing nothing | a token that is no node id, a row mixing the two forms, or — given the record — a test the run did not hold: not run, skipped, xfailed, xpassed, failed, each named as observed |
| The claim turning false | found by a person re-reading after a drift, or by a review round | found by the suite: the test is red, and the ledger arm names the row from the record in the same gate run. The prose may lag the test, as an `Enforced by:` sentence may; review reads it |
| No record — CI's `ledger` job, a preflight, the advisor, a vendored copy, a row that loaded no recorder | unchanged | read for existence (D2); one line says the test rows were read with no suite record (D10) |
| `--reverify` | re-stamps a drifted hash; `--checked` dates the row | writes nothing, dates nothing; leaves a BROKEN node id named |
| `--reverify --into` under the freeze | writes a `Re-read ·` row per drifted released row | writes none for a superseded family; its summary names the `Corrected ·` test row as the other repair |
| The fold | moves the row whole | moves the row whole |
| A consuming repository with no node id in its ledger | every finding identical before and after (S11) | — |
| A consuming repository whose vendored copy predates this | — | reads a test row as MALFORMED, *cites no coordinate*; `skills/evidence-ci/SKILL.md` says to update the copy first |

## What the observation cannot see

Each is named rather than closed, with what the checker says there.

- **Where no pytest ran, nothing is observed.** CI's `ledger` job, the
  post-commit advisor, a preflight, a vendored copy whose repository hands it
  no record, and a `--reverify` typed by hand read a test row for existence
  (D2) and print one line saying so. The reader that decides — the gate —
  always has the record of the run it seals, and that is where the
  observation decides. Whether CI should observe too is `questions.md` Q7.
- **A row that does not load the recorder observes nothing either.**
  `templates/config.md` §*Broad gate* rule 3 names the shapes (`tox`, `nox`,
  `env -i`, a replaced `PYTEST_ADDOPTS`). Such a row's run leaves no
  `session` line under the key, the checker reads as given no record, and
  its line names the key. The seal is then over existence only, and the
  gate repeats that line on its own output, so the sealer is told the row is
  unmeasured on a passing run too (corrected in round 3's fix pass, ⬜ 7).
- **Where one runner of the row loaded the recorder and another did not**, a
  test only the other ran owns no line and reads *not run*. The remedy is
  the row's, as rule 3 says; the finding is honest about this run.
- **A test the sealing machine skips holds nothing there.** A `skipif` true
  on the sealer's platform reads *skipped*; the row is hashed instead, or the
  seal is taken where the test runs. That is the strict reading, chosen on
  purpose (the Out table's fourth reframe row).
- **A run that stopped part-way** leaves tests unrun. The suite arm already
  fails such a run (`broad_gate.py#RAN_TO_ITS_END`, the `end` line's
  `stopped`), and the ledger arm's *not run* findings are a second reading of
  one stop, not a second stop.
- **A `passed` line for a test that asserts something weaker than the row's
  prose** is the limit the first frame named (`plan.md` §*Failure scenario*),
  and nothing here changes it: review reads the test.
- **The record is the head run's, and the ledger arm reads the same tree.**
  The gate runs both in `root`, and nothing between them edits a file; a
  record from another tree is another key, which the reader passes over.

## User scenarios & acceptance *(mandatory)*

Each scenario is a case seen red before it is committed. *Verifiable how*
names the module by its purpose; the build names the file.

| # | Scenario | Given / When / Then | Verifiable how |
|---|---|---|---|
| S1 | A test row resolves | Given a fragment row whose grounds hold one backticked node id naming a top-level `test_` function that exists, when `evidence-check` runs, then the row is OK, counted among `ok`, exit 0 | the new module, red against the unfixed checker, which names the row MALFORMED *cites no coordinate* |
| S2 | A renamed test breaks the row | Given S1 with the function renamed, then the finding is BROKEN naming the file and the missing name, exit 2 | the new module |
| S3 | A method is spelled pytest's way | Given a node id `path::TestA::test_b` for a method, then it resolves; given `path::test_b` for the same method, then BROKEN, and the detail says a method is written `path::Class::method` | the new module |
| S4 | *(rewritten at the reframe)* A unit that exists resolves; a kind that is no `def` or `class` does not | Given a node id naming a `def helper` in `tests/helpers.py`, a `conftest.py` function, or a method of a class with an `__init__`, with no record given, then OK; given one naming a module constant, then BROKEN, *no def or class named*; given a name defined twice, then BROKEN | the new module, the collection cases rewritten (D11), the OK cases red against the checker at ec48b584 |
| S5 | A mixed row is refused | Given a grounds cell holding a node id and a `path#unit@hash`, then MALFORMED naming both forms; given a `Corrected ·` row holding its citation and a node id, then not | the new module |
| S6 | A node id outside the grounds cell is prose | Given `path::name` in Verified behavior or Notes beside a hashed grounds cell, then no finding about it | the new module, over a fixture copying one of the 16 existing shapes |
| S7 | A migrated released row never drifts again | Given a released row citing a unit, a `Corrected ·` row in a fragment with the citation and a node id, and an edit to that unit, when `evidence-check --strict` and `--reverify --into` run, then no finding names the released row and no `Re-read ·` row is written; the correcting row is OK | `tests/test_a_released_row_is_read_again_in_a_fragment.py`, red when the superseding is removed from `family_view` |
| S8 | `--reverify` leaves a test row alone | Given a test row and `--reverify --checked <date>`, then the row's text and date are unchanged; given a BROKEN node id, then a `left` line names it | the new module |
| S9 | The summary names the other repair | Given `--reverify --into` writing at least one `Re-read ·` row, then its summary says once that a `Corrected ·` row naming the test that holds a claim retires its hashes | the new module, pinned on the sentence |
| S10 | One resolver for `Enforced by:` | Given `fold-check` over `docs/`, then every one of the 451 targets resolves as before; given a doc target `path::TestA::test_b`, then it resolves; given `fold_check.py` with its `ast.walk` branch, then the suite is red | `tests/test_a_folded_statement_names_what_enforces_it.py`, its pins updated in the same commit |
| S11 | A ledger with no node id is unchanged | Given a fixture ledger of hashed rows, citing rows and a fenced example, then the findings before and after this work are identical, line for line | the new module, over the fixture the existing cases already use |
| S12 | The vendored copy reads it alone | Given the checker copied alone into `tools/`, then S1–S5 hold there | `tests/test_evidence_check.py`'s `vendored_copy` fixture |
| S13 | The documents state it and are pinned | Given the new section, then its `Enforced by:` lines name S1–S9's cases and `fold-check` is green; given `templates/ledger.md`, then both forms are shown; given `skills/evidence-ci/SKILL.md`, then the update sentence is there | `fold-check`; a pin per changed sentence |
| S14 | This item's ledger is the first | Given the fragment, then every row of it is a test row or a citing row; `evidence-check --strict .` is 0 drifted at the head; every released row an edit drifted has a citing row | `evidence-check --strict .`, executed by the build and the sealer |
| S15 | *(reframe)* A test seen passing is held | Given a record the real recorder wrote for a planted suite in which `tests/test_x.py::test_y` passed, and a row naming it, when `evidence-check --strict` runs with the record directory and key, then the row is OK, exit 0, and no existence line is printed | the new module, running `pytest -p specseal_pytest_record` over the planted suite with the recorder's two variables set, as `tests/test_the_recorder_writes_what_its_process_ran.py` already drives it; red against ec48b584, whose checker knows no such options |
| S16 | *(reframe)* A test the run did not hold is refused by what was observed | Given the same with the test skipped, xfailed, xpassed (non-strict), failed, erroring in setup, or absent from the record (a `def helper`, a module-level `pytest.skip`, a class with `__init__`), then MALFORMED, exit 2 under `--strict`, the detail naming the observation — *not run* / *skipped* / *xfailed* / *xpassed* / *failed* / *error in the recorded suite* — and the remedy | the new module, one case per category, each red against the phase-6 checker, which reads OK for every one |
| S17 | *(reframe)* Round 2's spellings are the record's finding, and no case names a spelling | Given `xfail(condition=False)` on a passing test, `xfail(strict=True)` on a passing test, a skip mark under a module `if`, `pytestmark +=`, `skipif(True)`, each recorded, then the verdict is what pytest did: the conditional xfail that ran and passed is OK, the strict xfail that passed reads `failed`, the skipped ones `skipped`; the checker's source holds no mark name | the new module, parametrised over round 1's and round 2's spellings; `grep -c 'xfail\|skip' evidence_check.py` is 0 outside the detail words |
| S18 | *(reframe)* A class and a parametrised function own their lines | Given a row naming `tests/test_x.py::TestA` whose methods all passed, then OK; one method skipped, then MALFORMED *skipped*; given `::test_y` with `test_y[a]` passed and `test_y[b]` failed, then MALFORMED *failed*; given a record line of another file's `test_y`, then it is not this row's | the new module |
| S19 | *(reframe)* The path is the record's, never rebuilt | Given a pytest rootdir that is `tests/` (an ini file there), so the record's node id is `test_x.py::test_y`, and a row naming `tests/test_x.py::test_y`, then the match holds through the line's `path`; given `broad_gate.py#read_record` over the same record, then it names the same file | the new module, the real recorder, both readers over one record |
| S20 | *(reframe)* No record is existence, and says so once | Given test rows and no record options, then every D2 verdict as today and one line saying the test rows were read for existence; given a directory under which no `session` line carries the key, then the same line naming the key; given a ledger with no test row, then no line | the new module, pinned on the sentence; `tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py` green unchanged |
| S21 | *(reframe)* The gate hands the arm the record | Given `broad_gate.py#main` after the suite ran, then `checks[LEDGER]`'s argv carries the record directory and the head key; given `--preflight`, then it carries neither; given a planted repository whose test row names a test its row skips, then the ledger arm comes back failed and the run is NOT SEALED | the gate's module that reads `checks[LEDGER]`'s call site (`tests/test_the_lenient_run_says_what_the_broad_gate_will_say.py` names it), red with the two items missing; one gate run over the planted repository |
| S22 | *(reframe)* `--reverify` names what the record refuses and writes nothing | Given a test row and a record in which its test was skipped, when `--reverify` and `--reverify --into` run with the record options, then a `LEFT` line names the row with the observation, the row's text and date are unchanged, exit 1 | the new module |
| S23 | *(reframe)* The documents state the observation and are pinned | Given §*A claim held by a test*, then statements 1 and 2 say what the static reader establishes and what the record answers, and no sentence in the five documents says what *reads as a test* or names a mark; `templates/ledger.md`, the two skill sections and the gate's docstring item 2 say the same; `fold-check` is green; the removed sentences stand nowhere (`survivor-check`) | `fold-check`; a pin per changed sentence, red with the sentence removed; `survivor-check --range origin/release/v0.21.0...HEAD` exit 0 |

## Data & interfaces

- **The token.** `path::name(::name)*` inside backticks in a Code grounds
  cell, `path` ending `.py`. The parts after the path, joined with `.`, are
  the qualified name looked up in `py_spans`. This is `fold_check.py`'s
  grammar extended by pytest's own nesting; no new regular expression for a
  coordinate is added anywhere, and `ANCHOR_RE` is not touched.
- **The findings.** The same `(status, coordinate, detail)` triples
  `check_ledger` returns, with the node id in the coordinate slot. Statuses:
  OK, BROKEN, MALFORMED. `exit_code` is unchanged.
- **One sentence** in `--reverify --into`'s summary, printed once per run
  that writes a `Re-read ·` row, pinned.
- **`fold_check.py`** gains a loader constant for `evidence_check.py` beside
  its three existing ones and loses the body of its resolver.
- **The record (reframe).** Two options on `evidence-check`, a directory and
  a key. The reader opens every `*.jsonl` directly under the directory, keeps
  those whose first line parses as an object whose `key` equals the key, and
  reads of each later line with `"kind": "test"` the fields `path`, `nodeid`,
  `when` and `category`; a line that does not parse is passed over, as
  `read_record` passes it over. Its answer is `{(relative path, names):
  {category, …}}`, or None where no file carried the key. Four fields and no
  other, so a field the recorder adds changes nothing here.
- **The match (reframe).** A key is (`path` named as `record_path` names it,
  the node id's parts after the first `::` with `[…]` stripped from the
  last). A cited `(path, names)` owns every key whose path is equal and whose
  names begin with the cited names.
- **The held rule (reframe).** The union of the owned keys' categories, less
  `""`, is exactly `{"passed"}`.
- **The words (reframe).** `not run in the recorded suite`, `<category> in
  the recorded suite`, each followed by the `TEST_FORM` remedy; and one line,
  printed once beside the totals, where test rows were read with no record,
  naming the key where one was given and found empty. Each is pinned (§14).
- **`broad_gate.py#main` (reframe)**: two more argv items on `checks[LEDGER]`
  where `head is not None`; item 2 of the module docstring's list says so.

## The seam with the sibling frames

- **#867 (the coordinate grammar's five copies).** This work adds no
  coordinate grammar and edits no copy: `ANCHOR_RE`, `correction_check.py`'s
  `ANCHOR` and `CITATION`, `settle.py`'s `COORDINATE_RE` and
  `rider_check.py`'s stamp are untouched. The node id is a different token,
  read in one new function in `evidence_check.py` through the existing table
  walk. If #867 moves `grounds_cells` or `ledger_table_rows`, phase 1
  rebases one call site; if it lands second, it finds one more caller of the
  walk and no second reader of a coordinate.
- **#870 (`generic_units`).** D2 resolves through `resolve_unit`'s Python
  branch only, which calls `py_spans`; the non-Python branch is #870's and
  is never reached by a node id, because a token whose path is not `.py` is
  refused before resolution.
- **`evidence_check.py` units this work changes:** `malformed_rows`,
  `malformed_remedy`, `check_ledger`, `reverify_into` (one sentence), and
  one new function with its constants. **Units it reads and does not
  change:** `resolve_unit`, `py_spans`, `grounds_cells`, `family_view`,
  `judge`, `classify`, `exit_code`. `fold_check.py`: `target_problem` and a
  loader constant.
- **At the reframe (ec48b584), the units phases 6–9 change:** `node_finding`
  (two calls leave, the record arrives), `held_by_tests`, the call in
  `family_view`'s member loop, the call in `reverify_into`, `main` (two
  options), and one new reader with its constants; `check_ledger`,
  `ledger_families` and `reverify` carry the record through only if Q6's
  answer threads it as a parameter. **Units that leave:** D11.
  `broad_gate.py#main`: one call. #870's `generic_units` and the non-Python
  arms are still never reached by a node id.

## Judgments the tree answered

Listed so nobody reopens them; each is overturnable by opening what is named.

1. *Test alone, or test plus a code anchor?* Test alone — the Out table's
   first row.
2. *Which verb migrates a released row?* `Corrected ·` — the Out table's
   second row, and D5.
3. *May a row mix the forms?* No — D4.
4. *Does the checker run the test?* No — the Out table's third row.
5. *Any `def`, or a test?* A test, by pytest's default names — D2 and the
   Out table's fifth row. A row naming a unit that merely exists is a claim
   nothing holds, which is what *cites no coordinate* already refuses.
6. *Does a new section or an edit carry the rule?* A new section, inserted
   where it drifts no neighbour — D7, with the counts.
7. *Does the ledger's reader or `fold_check.py`'s become the one?*
   `evidence_check.py`'s, because `evidence-ci` ships it alone and
   `fold_check.py` already loads its readers — D6.

At the reframe, from the tree:

8. *Where is the observation read?* In the gate's ledger arm, which holds
   the head run's record at the moment it runs — D10. Not `evidence-check`
   reading *the newest* record: which run is newest is an inference, and the
   gate keys each run fresh so that a reader passes every other key over
   (`broad_gate.py#record_key`). Not the sealer: it judges nothing
   (`agents/sealer.md`).
9. *What does the static checker keep?* Existence of a `def` or `class`,
   once — D2. The name prefix was a prediction of the same class as the
   marks — the Out table.
10. *Which word for a test the run did not hold?* MALFORMED, the observation
    in the detail — the Out table.
11. *Is a skipped or xfailed test held?* No — the Out table and §*What the
    observation cannot see*.
12. *One reader of the record or two?* Two, because the checker ships alone;
    S19 reads one record with both — the Out table.
13. *What of a record with no session under the key?* No record, and the
    one line names the key — D10.
14. *Does CI observe?* Not in this item; `questions.md` Q7 puts it to the
    owner with the default *no*.

## Rule changes

- nothing
  why: overturned: the ledger left the tree at 5b1f6fae, where a rule's check line came to
    name its test instead.

## Open questions → questions.md

Seven rows. Q1–Q4 are answered. The reframe adds one measurement (Q5), one
the work's (Q6) and one a person's (Q7, which does not block the build).

Framed 2026-10-07 by framer, before the build.
