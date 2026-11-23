# Review round 1: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

```seal
target: 2b75b0d79 against origin/release/v0.38.6
```

This is the first round, so no earlier record carries a coordinate and every
fact below was established here. The diff was read from the merge base
`8dea1ca7b` to `2b75b0d79`, all 65 files. `routing.md`, `frame/design.md`,
`frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`
were each read whole at `2b75b0d79`, and so were the four phase records. No
`pr.<lang>.md` stands, and none is owed: `seal/config.json` names English
for both language keys. No `seal/parity.json` is declared.

The two findings share one cause. Each is a fact the build moved whose old
statement was left standing, once by the build's own step (finding 1) and
once by a base merge that added a member to a class the build had already
enumerated (finding 2).

## Findings

### 1. `broad_gate.py#rounds_rows` keeps a guard and two cases for a chain check that `main` has already loaded

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:1577-1592`, `tests/skills/test_broad_gate.py:1259-1305`, `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/gaps.md:16`
evidence: read `skills/verify/scripts/broad_gate.py:2250`, `skills/verify/scripts/broad_gate.py:2058`, `skills/verify/scripts/broad_gate.py:2116-2124`, `skills/verify/scripts/broad_gate.py:1719`, `skills/verify/scripts/broad_gate.py:1577-1592`, `lib/sibling.py:93-130`; executed `git grep -n "rounds_rows" -- '*.py'`, which names `gate`'s `panel` as the one caller outside the suite
```

Why it matters: the comment over the guard tells the next reader that "an
absent check is said here and the run goes on". Since phase 2 no run of
`seal gate` can reach that line, so the comment describes a behaviour the
command does not have. An agent asked what the gate does with an absent
`chain_check.py` reads it and answers wrong. `skills/core/SKILL.md` *The
rule a mechanism is kept against* asks a change to remove, in the same
commit, what stood on the old fact: "a check, an exception, a comment, a
copy". Here the exception branches, their comment and the two cases that
hold them stand on the fact that the check may be unloaded when the panel
is built.

The grounds:

- `broad_gate.py:2250` loads `CHAIN_CHECK` in `main` before `gate` runs, and
  an absent file ends the process there at exit 2 (`lib/sibling.py:114-117`).
  A module that raises while it executes is not registered
  (`lib/sibling.py:124-129`), and its exception ends `main`.
- Inside `gate`, `broad_gate.py:2058` loads the check again for `SEALING`
  before the chain arm runs. That line is the only path to `panel`
  (`broad_gate.py:2116`), and `panel` is the only caller of `rounds_rows`
  (`broad_gate.py:1719`). So a direct call of `gate`, which the suite makes,
  meets an absent check at the arm and never at `rounds_rows`.
- By the time `rounds_rows` runs, `sibling.load` returns the module the
  process holds (`lib/sibling.py:112-113`). Neither `except` branch at
  `broad_gate.py:1585-1592` can be taken.
- The two cases at `tests/skills/test_broad_gate.py:1259-1305` reach the
  branches only by monkeypatching `sibling.load` and calling `rounds_rows`
  directly. They hold a branch no command reaches.

The account: `gaps.md:16` claimed that "`seal gate` never reaches that
block without the check" and left the call to this round. The claim
holds, as the grounds above show, and the block goes.
`lib/sibling.py#going_on` stays, because
`.github/scripts/release_seal.py:323` and `:607` still use it.

The fix, at `broad_gate.py:1577-1592`:

```python
    records = sibling.load(ROUTING).rounds(item)
    rows = [("rounds", str(len(records)))]
    # `main` loaded the check before any arm ran and the chain arm read its
    # `SEALING`, so this is the module the process already holds.
    chain = sibling.load(CHAIN_CHECK)
    stamp = stamp_module()
```

The fix pass owes three more changes. It deletes
`Test_rounds_rows::test_refuses_to_stop_a_run_where_the_check_will_not_load`
and `Test_rounds_rows::test_names_the_absent_check_in_its_own_line_and_goes_on`.
It removes the second paragraph of `gaps.md` *Not done*, whose question
this round answers. It also adds a row to `frame/design.md` *Removes* for
the guard and its two cases, as phase 2 did for `misplaced`'s `reader`.
Nothing a person reads changes. The sentence the guard printed is printed
by no command, so contract rule 14 asks for no new pin.

### 2. `session_cost.py` reaches `lib/` at import since #1572 and still spells the stream loop, which `lib/console.py` says only two other kinds of script do

```seal
severity: should
location: `skills/verify/scripts/session_cost.py:3669-3682`, `skills/verify/scripts/session_cost.py:97-119`, `skills/verify/scripts/session_cost.py:3068-3070`, `lib/console.py:47-61`, `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/changelog.md:11`, `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/frame/design.md:77`
evidence: executed `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'` and a `grep` of the module-level loads of each file it listed; read `skills/verify/scripts/session_cost.py:97-119`, `skills/verify/scripts/session_cost.py:3669-3682`, `lib/console.py:47-61`, `git show 15636c7f0:skills/verify/scripts/session_cost.py` at the same lines
```

Why it matters: the work's rule for the stream loop is the docstring of
`lib/console.py`. An entry point that imports `lib/sibling.py` at import
and loads its modules through `sibling.load` calls `console.to_utf8()`. Two
kinds of script spell the loop inline, "and only these". At the target,
`session_cost.py` is neither kind and still spells the loop. So the
docstring's "only these" is false, and the next author who reads it to
decide whether a script may copy the loop is told something the tree does
not do. The changelog's `### Removed` item says the same false thing to a
person: "The UTF-8 stream loop of each entry point that loads `lib/` at
import". The loop it claims removed still stands in one such entry point.

The grounds:

- At `2b75b0d79`, `session_cost.py:104-115` imports `lib/sibling.py` at
  module level. `:119` loads `skills/verify/scripts/deferral_check.py`
  through `sibling.load`, also at module level. `:3669-3682` spells the
  loop.
- At `15636c7f0`, where `frame/design.md` G15's probe ran, the same file
  imported nothing from `lib/` at import. #1572 (`459116a4e`) added the
  import and the load, and this branch took them in at `8b8b434b5`. Phase 3
  had closed at `604c995ab` before that merge. Phase 4's census re-ran S14
  and S15 alone. So the class phase 3 enumerated was never listed again
  after a merge that added a member to it. Contract rule 12 asks for that
  list to be rebuilt from what produces the defect, and a merge that
  changes what a file loads at import is such a producer.
- Of the other files S10's search lists, none loads a module at import
  before its loop. `durations_union.py`, `deferral_check.py` and
  `mutation_check.py` load nothing. `release_report.py`, `release_seal.py`,
  `rules.py`, `hooks/core-start.py` and `seal_stamp.py` load inside a
  function. `chain_check.py` and `pr_body.py` run the loop first (executed,
  as the evidence line says). `session_cost.py` is the one instance.
- `frame/plan.md` A7's argument holds for this file as it did for the
  thirteen. `session_cost.py` already fails at import, with the loader's
  sentence, where `deferral_check.py` is absent. Phase 3 made a load of
  `lib/console.py` read nothing beside the standard library
  (`lib/console.py:91-93`, `:124`). So the load adds no way to fail that
  the file does not already have.
- `frame/design.md:77`, S10, describes the twelve files its search prints
  as "the scripts that load nothing from `lib/` at import, the two whose
  loop runs before their loads, and `lib/console.py`", and lists
  `session_cost.py` among them. At the target that description is false
  for `session_cost.py`.

The fix, in `skills/verify/scripts/session_cost.py`, after `RUNNERS` at
line 119:

```python
# The runner words of each kind of check, the one list `seal deferrals`
# reads too.
RUNNERS = sibling.load("skills/verify/scripts/deferral_check.py").RUNNERS
# `lib/console.py`, whose `to_utf8` the `__main__` block opens with. It
# reads nothing beside the standard library as it loads, so it adds no way
# to fail before the answer that the load above does not already have.
console = sibling.load("lib/console.py")
```

and at line 3669:

```python
if __name__ == "__main__":
    console.to_utf8()
    sys.exit(main())
```

The snippet does not reach three other statements of the same fact, and the
fix pass owes them too. First, the comment at `session_cost.py:97-103` says
`deferral_check.py` loads at import and "each module of `lib/` at its first
use". It then names `lib/console.py` at import beside `deferral_check.py`.
Second, the docstring of `lib_module` at `:3068-3070` says a light reading
"loads no module of `lib/` but `sibling.py`". It then names `console.py`
beside `sibling.py`. Third, S10 of `frame/design.md:77` drops
`skills/verify/scripts/session_cost.py` from its list of twelve, which
becomes eleven. That row is the orchestrator's to fold, as it folded each
phase's statements. With the fix, `lib/console.py:47-61` and
`changelog.md:11` hold as written. The census reads the new call on the
module-level name `console` (`tests/censuses.py:634-646`), and
`tests/skills/test_session_cost.py::test_census` with
`tests/behaviour/test_every_tracked_file_meets_every_census.py` is the
narrow run that proves it. The fix pass may instead keep the loop, but only
by adding a third kind to the list in `lib/console.py:47-61` that names
`session_cost.py` and why, and by narrowing `changelog.md:11` to the
thirteen. A copy the work's own rule says goes would then stay, so the
round's reading is the conversion above.

## Confirmations

What matched: every acceptance search of `frame/design.md` S1 to S5, S7 to
S11 and S13 to S15 prints at `2b75b0d79` exactly the lines the row names,
after both base merges (executed: each `git grep` as the row writes it). S8
prints `skills/verify/scripts/session_cost.py:2764`, three lines lower than
the phase record's run, because #1572 added lines above it.

What matched: the printed sentences the build moved read as they did.
`lib/config.py:248-252` builds `SWITCH_NOT_YES` and `SWITCH_NOT_READ`, which
with the key and the closing words are the old `KEY_NOT_YES` and
`KEY_REFUSED` of `pr_body.py` and `release_seal.py` word for word. A value
holding braces is passed as a `format` argument and not as the template,
and `tests/lib/test_config.py` holds that with its `braces` row. Every
`plural` call in `settle.py`, `seal.py`, `fold_check.py`, `release_seal.py`
and `publish_release_note.py` prints what the old helper printed. Among
them are `removed N directory` and `directories`, `N older commit` and
`commits`, and `1 work items` at `seal.py:2463-2467`, which still uses no
helper (read).

What matched: each replaced helper answers as before. `gitcmd.inside` takes
both paths absolute. Every caller passes `(path, top)` in that order:
`seal.py:605` and `:673`, `settle.py:1543` and `:1545`, and
`broad_gate.py:302` and `:337`. The two `broad_gate.py` callers keep the
`root is None` answer (read). `_prefix` followed by `lstrip("/")` equals
the old `strip("/")` for every input, since only the order of the two
strips changed (read `lib/config.py:299-307`, `:342-346`).
`declared_policy_root` with `policy_root` keeps the old answer for no home,
a refusal and a value that leaves the repository (read
`lib/config.py:381-406`). `fold_check.py#declared` raises `Unusable` on the
same sentence `stated` raised, since both come from
`config_value`'s refusal (read `skills/settle/scripts/fold_check.py:286-304`,
`lib/config.py:196-206`).

What matched: `gaps.md` *Not done*, first paragraph. The claim is that
`Policy root` is read once and the file opened twice. `fold_check.py:301`
reads the key once, and the second open is `declared_policy_root`'s own
read of the file, as the paragraph says (read).

What matched: `gaps.md` *Not done*, third paragraph. The claim is that the
exclusion of `tests/` in
`tests/behaviour/test_every_entry_point_runs_at_the_floor.py#loaded_by`
does not rest on `PINS`. The claim holds, and the exclusion stays. A
script that names a tracked module under `tests/` in a whole string still
exists: an `ast` walk of every tracked `.py` outside `tests/` found
`skills/verify/scripts/test_layout.py:1292` and `:1294` naming
`tests/conftest.py` (executed). So the guard still has an input it would
turn away, and its cost is one condition.

What matched: the new cases each belong to a new unit's group, and none
duplicates another. `bin/seal layout --pairs tests` read 140 files and
printed 129 pairs, none in `Test_opted_out`, `Test_marked_home`,
`Test_declared_policy_root`, `Test_policy_group`, `Test_switch`,
`Test_plural`, `Test_inside`, `Test_read_declaration`, `Test_requirements`,
`Test_pin_of` or `Test_preload_files` (executed).

What matched: `pr.md` quotes the two rows of `frame/plan.md` *Judgments of
the run* word for word, and the changelog's `### Changed` items state what
`tests/run_tests.py:94-98`, `:288-301`, `broad_gate.py:2246-2251` and
`evals/scripts/noninferiority.py:91-104` do (read). `pytest-xdist` in the
fallback commands parallelises nothing on its own, since `-n auto` is the
runner's argument (`tests/run_tests.py:306-340`) and no pytest
configuration file passes it, so the changelog's "still run the suite
serially" holds. The evidence was executed: `git ls-files` lists no
`pytest.ini`, `pyproject.toml`, `setup.cfg` or `tox.ini`, and
`git grep -n addopts`, `seal/threads` left out, prints only lines of the
runner and of `PYTEST_ADDOPTS`. The `### Removed` item
on the stream loop does not hold at the target, as finding 2 says.

What matched: a claim of the spawn prompt. It said #1576 removed
`lib/config.py#reference_roots`' empty-home answer, and the merge
`2b75b0d79` had no textual conflict. `reference_roots` still answers None
for an empty home at `lib/config.py:333-334`, and so does the base
`8dea1ca7b`. The merge kept the base's version, and this work's change to
that function is the normaliser loop alone (read). No unit #1576 removed is
named by this work at the target: a search for `OLD_MARK` and for the
removed names of this work's own *Removes* over the tree, `seal/threads`
left out, prints only test fixtures (executed).

The crafter's label is honest: `gaps.md:7` hands the full suite, the lint
and the format check to the orchestrator's broad run, as `unverified`. The
orchestrator's set of 4213 passed cases is the spawn's claim and was not
re-run here.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The thirteen `console.to_utf8()` entry points at a cp1252 console, and the Windows-joins case of `pact_check`, whose join now depends on whether a path is absolute | `tests/skills/test_pact_check.py:146-170` | the `windows-latest` jobs of `.github/workflows/test.yml` on the pull request |
| The two workflow install lines, `pip install -r tests/requirements.txt` with and without `pytest-split==0.11.0` | `.github/workflows/test.yml:122`, `.github/workflows/publish-release.yml:136` | the `pytest` and `pytest-wide` jobs on the pull request; the `publish-release` run of the release that ships this |
| The seen-red runs and the mutation runs of phases 1 to 4, which were read and not run again | `trail/phases/phase-1.md` to `phase-4.md` | the sealer |
| The full suite, the repository-wide lint and the format check at HEAD | the tree | the orchestrator's broad run |
| Outside this diff: `docs/releasing/branch-and-release.md:166-169` says `bin/test` runs `.github/scripts/run_tests.py` and `seal.py` loads `.github/scripts/rules.py`, and neither file exists at the target | `docs/releasing/branch-and-release.md:166-169` | the orchestrator, as a follow-up outside this work item |

## Probes

| Command | Result |
|---|---|
| each acceptance search of `frame/design.md` S1 to S15, as written, at `2b75b0d79` | each printed the lines its row names; S10 printed the twelve files it lists |
| `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'`, then a `grep` of each listed file's module-level `import sibling` and `sibling.load` lines | `skills/verify/scripts/session_cost.py` imports `sibling` at line 106 and loads `deferral_check.py` at line 119, at module level; every other listed file loads nothing at import, or loads after its loop |
| `bin/seal layout --pairs tests` | exit 0; 140 files read, 129 pairs, none among the classes the diff adds |
| an `ast` walk of every tracked `.py` outside `tests/`, printing each string constant that is a tracked path under `tests/` | `skills/verify/scripts/test_layout.py:1292` and `:1294`, `tests/conftest.py` |
| `git grep -n "rounds_rows" -- '*.py'` | `broad_gate.py:1719` in `panel`, and the cases of `Test_rounds_rows` |
| `git ls-files` for a pytest configuration file, and `git grep -n addopts` with `seal/threads` left out | no `pytest.ini`, `pyproject.toml`, `setup.cfg` or `tox.ini`; `addopts` only in the runner and in `PYTEST_ADDOPTS` lines |
