# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 2

| Field | Value |
|---|---|
| Target SHA | 2f0b4460, fixes 61dcd638..2f0b4460 |

A verifying round over round 1's fix pass, part A only. Its target is the
diff of the nine commits after round 1's record; each of round 1's seven
findings is answered below, and round 1's two ❓ rows stand as written. Two
of the seven are not closed: 🔴 1 and 🟡 2 here take their place, and both
sit in a unit the fix pass changed. 🟡 3 is an instance of round 1's 🟡 7
class that the fix pass's sweep did not reach. Findings from reading and
from execution are labelled in each Grounds cell, and every command named
there is in `## Executed probes`. The full suite was not run: it is
`unverified`, and the sealer answers it.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | **fix of a fix — a ready pull request still passes an open finding, now behind a 🟢, ❓ or ⬜ `#` cell, or behind a lost severity read `confirmed`.** Round 1's 🔴 1 is not closed. The new `open_findings` skips every row whose `#` cell opens with 🟢, ❓ or ⬜, whatever its verdict, so `\| ⬜ 3 \| 🔴 a defect graded as a note \| … \| open \|`, `\| ❓ \| 🔴 … \| open \|` and `\| 🟢 \| 🟡 … \| open \|` all pass. A row whose `#` cell carries no severity closes by any of `CLOSED_WORDS`, so `\| 1 \| 🔴 … \| confirmed \|` passes. That is round 1's two shapes combined, the severity at the head of the Finding cell and `confirmed`. A table with no `#` header falls back to column 0 and passes the same row. The base's `open_blocking` refused all of these, because it read a 🔴 anywhere in the row and did not count `confirmed` as closing. The ⬜ exclusion is where the fix departed from round 1's paste, and its stated ground is false: the old record it cites, `seal/specs/1791876666-the-test-suite-is-held-to-a-budget/rounds/round-2.md:31` (`⬜ 3 … same claim as 🟡 2`), reads `answered`, not `open`. No record in the tree needs the exclusion. `tests/test_chain_check.py:430` now pins the hole as passing (`⬜ 7 … open`), and `docs/the-review-record.md:70-76` states it as the rule. The unit is the one 18315ee2 rewrote | `skills/code-review/scripts/chain_check.py:608-618` | deferred the frame | executed: `test_tmp_open_findings.py` fed 21 rows to the shipped `open_findings`. The four rows above, `\| 2 \| 🟡 … \| ❓ out of verified scope \|`, `\| carried \| 🔴 … \| confirmed \|` and the row under a `No.` header all passed. executed: the same script ran a stricter reading over all 36 `round-N.md` in the tree: a 🟢, ❓ or ⬜ row reading a word outside `CLOSED_WORDS`, and a lost-severity row carrying 🔴 or 🟡 and reading a word outside `FINDING_CLOSES`. It found no such row in any of them. executed: `test_tmp_candidate.py` ran the paste-ready function below. It names all five holes and the `No.` header row. It passes `🟢 \| round 1's 🔴 2 is closed \| confirmed`, `❓ \| … \| ❓ out of verified scope` and `⬜ \| … \| answered`. It refuses none of the 35 earlier records. read: the base's `open_blocking` at ce448bbe, `chain_check.py:1968-2004` there · orchestrator: round 2 marked fix of a fix, so no fix pass runs and the work item goes back to its framer |
| 🟢 | round 1's 🟡 2 is closed: after a `not sound` repair outside the work item, the orchestrator spawns a verifying round before the sealer | `skills/code-review/orchestration.md:162-173` | confirmed | read: the rewritten paragraph against `chain_check.py#follows`, which excuses only commits inside `seal/specs/<id>/`, and against `broad_gate.py:3069`, which runs the chain check with `--sealing`. A repair to a phase record, the changelog fragment (`seal/specs/<id>/changelog.md`) or the pull request body adds no commit outside the work item, so the sealer can re-run straight away, as the paragraph says. No other file states the `not sound` path (round 1's grep, carried) |
| 🟢 | round 1's 🟡 3 is closed: the `fix of a fix` stop names no test | `docs/the-review-record.md:173` | confirmed | read: the line now says `Enforced by: nothing — …`, the form its two neighbouring rules use. `agents/sealer.md:61-67` has the sealer read every round-record row and the warden's last record, and `spec.md` S9 and the `Fix of a fix` row say the same. executed: `bin/rules --check` exit 0 |
| 🟢 | round 1's 🟡 4 is closed: `seal_home` and `rounds_rows` are live, so keeping them is the right repair, and `spec.md` now says so | `skills/verify/scripts/broad_gate.py:705`, `:2612`, `:2798`, `:2968` | confirmed | read: `seal_home` is called once, at `:2968` in the gate's run, and `broad_command(home)` reads the `Broad gate` row through it; removing it stops the gate. `rounds_rows` is called at `:2798` and draws the panel's `rounds` row. It reads the records only through `chain_check.verdict_table`, `verdict_of` and `deferred_home`, so it adds no second reader of the table, and §*Data & interfaces* keeps the panel unchanged. The one-home decision (`spec.md:218`) is about the broad run's record, `broad-gate.md` against the `Broad gate` cell; the `seal_home` its cost cell names is the generator's. `round_count` has no caller left (`grep`). `spec.md:385-389` and `:422` and the `overview.md:52` divergence row agree with the code |
| 🟡 2 | **fix of a fix — `.test_durations` still prices 301 cases the suite no longer collects, so the durations case fails and the release table is still inflated.** Round 1's 🟡 5 is not closed. 1b875efc dropped the 1,332 entries of the 29 deleted modules. It left 301 entries, 345.3 s, for cases this branch removed from modules that still exist: 81 in `tests/test_the_seal_is_taken_once_by_the_sealer.py`, 52 in `tests/test_the_rules_have_one_owner.py`, 38 in `tests/test_the_pull_request_language_is_the_repositorys.py`, 34 in `tests/test_settle_retires_the_process_record.py`, and others. That is 9.3 % of the file's 3,717.2 s, over the 5 % `STALE_SHARE`. So `tests/test_the_windows_leg_runs_in_shards_that_make_the_whole.py::test_the_durations_file_prices_the_suite` fails in every run that collects the whole suite, CI's included. `release_report.py#suite_seconds` also still prices 3,717 s where the collected cases sum to 3,372 s. The fix pass's grounds say "the stale entries it guards against are gone" and "nothing re-measured"; the first is false. Round 1's Location was `release_report.py`, which 1b875efc does not touch; this row's is the file the fix changes | `.test_durations` | deferred the frame | executed: `bin/test tests -q -k test_the_durations_file_prices_the_suite` exit 1, with the assertion "345.3 s of the file's 3,717.2 s (9.3%) belong to 301 entries the suite no longer collects". The case had skipped in the narrow run, because one module named on its own is not the suite. executed: `pytest --collect-only` collected 7,577 cases; 301 entries of the file are not among them, and 229 collected cases have no entry (3 %, under the share). executed: `test_tmp_durations.py` shows that 1b875efc removed only ids of the 29 deleted modules and changed, added and reordered nothing. That part of the fix holds · orchestrator: round 2 marked fix of a fix, so no fix pass runs and the work item goes back to its framer |
| 🟢 | round 1's 🟡 6 is closed: both READMEs, `templates/hygiene.yml` and `skills/code-review/orchestration.md` state the open-row rule and the one `Target SHA` field | `README.md:182`, `README.ko.md:173`, `templates/hygiene.yml:36-38`, `skills/code-review/orchestration.md:14`, `:81-82`, `:250` | confirmed | read: each rewritten sentence against `chain_check.py#main` and `#records` and against `templates/sdd-round.md`. A draft prints every refusal and exits 0, so the hygiene comment's list of what fails once the draft is over is true. Every `##` heading of `orchestration.md` carries the `Orchestrator:` prefix. A `git grep` over `tests/` for the removed names finds only history (#226, #318, #590) and the fixtures' made-up paths |
| 🟡 3 | **A test docstring still counts five `.py` members in the seal and segment sweeps, and there are four.** `tests/test_one_word_one_meaning.py:472` says "across both sweeps five members are `.py`". The fifth was `round_record.py`, which left the sweep's member list and the pinned set at `:495-500` in e84e76f2. The case's own assertion message at `:501-505` says the docstring's count has to be brought to the new list when the set moves. The docstring is the case's argument that the phrase set is closed, so a smith extending a sweep reads a member count that is wrong. This is round 1's 🟡 7 class, a test module stating a removed mechanism as current, and the fix pass's `git grep` for the names did not reach a count | `tests/test_one_word_one_meaning.py:472` | deferred the frame | read: `:472`, the pinned set at `:495-500`, and the base's `:483` and `:508`, where `round_record.py` was the fifth. Every other coordinate round 1's 🟡 7 named is rewritten: read each, and `git grep` over `tests/` as in the 🟢 row above · orchestrator: round 2 marked fix of a fix, so no fix pass runs and the work item goes back to its framer |
| 🟢 | round 1's 🟡 7's leftovers are gone and the census holds: the dead exemption, `ROUND_RECORD_NAME` and `committed_round_records_on_disk` are deleted, and `conftest.py#gathered_entry` declares `Reads:` in place of its `undeclared_readers.txt` line | `tests/conftest.py:335-346`, `tests/undeclared_readers.txt:969` | confirmed | read: `gathered_entry` reads the `changelog/X.Y.Z.md` files that `gather_changelog.py` writes, so `owned` is its class, and `unknown passed` matches its `None` for a missing marker. `git grep` finds no caller of the deleted helper. executed: `tests/test_a_reader_declares_its_input_class.py` and `tests/test_no_passage_is_pasted_into_a_second_file.py` among the 439 passed |
| 🟢 | The past-tense `round_record.py` line in `test_the_sweep_reads_across_a_string_literal_seam` is true history the case needs | `tests/test_one_word_one_meaning.py:433-434` | confirmed | read: the case pins `LITERAL_SEAM`'s join, which still guards the four `.py` members. The line says why a seam shape was an ordinary edit and where round 1 measured it; with `built` in place of `builds` it no longer claims the generator exists |
| 🟢 | The fix pass's new cases were seen red, and the changelog fragment's counts are the tree's | `tests/test_chain_check.py:417-475`, `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:85-97` | confirmed | executed: `test_tmp_candidate.py` ran the three new `TestOpenFindings` inputs through c79670b6's `open_findings`, and it named nothing for any of them, so each case was red there. executed: `wc -l` at 2f0b4460 gives 1,135, 3,400 and 228 lines; `git diff --numstat ce448bbe 2f0b4460 -- tests` gives 31,995 deleted and 3,117 added; there are 143 test modules against 167 at the base. Each matches the fragment. 🔴 1's and 🟡 2's fixes move these counts again |

## Paste-ready fixes

### 🔴 1

`skills/code-review/scripts/chain_check.py`, `open_findings`, the loop
(`:608-618`) and the docstring above it:

```python
def open_findings(reader, lines, rel):
    """([(line, the `#` cell, the verdict word)], errors) for every row whose
    verdict does not close it.

    The `#` column is found by its header, the first column where there is
    none. A row whose `#` cell opens with 🔴 or 🟡 closes only by a fix
    pass's word, never by `confirmed` or `out of verified scope`. One opening
    with 🟢, ❓ or an old record's ⬜ commissions no fix, and still closes
    only by a closing word, so such a row left at `open` fails. Any other row
    lost its severity: where a 🔴 or 🟡 stands anywhere in it, it closes as a
    🔴 or 🟡 row does, and otherwise by any closing word.

    Reads: guess — the warden's record, through `verdict_table`; unknown refused"""
    rows, col, header, errors = verdict_table(reader, lines, rel)
    if col < 0:
        return [], errors
    id_col = header.index(ID_COLUMN) if ID_COLUMN in header else 0
    found = []
    for line, seen in rows:
        word = verdict_of(seen, col)
        severity = severity_of(seen, id_col)
        if severity in FINDINGS:
            closes = FINDING_CLOSES
        elif severity in NOT_FINDINGS:
            closes = CLOSED_WORDS
        elif any(mark in "".join(seen) for mark in FINDINGS):
            closes = FINDING_CLOSES
        else:
            closes = CLOSED_WORDS
        if word not in closes:
            cell = seen[id_col].strip() if len(seen) > id_col else ""
            found.append((line, cell or "the row", word))
    return found, errors
```

The comment above `NOT_FINDINGS` (`:78-79`):

```python
# The marks that open a row which commissions no fix: 🟢 and ❓, and an old
# record's ⬜ note. Such a row still closes only by a closing word.
```

`tests/test_chain_check.py:430`, the old note closed as the tree's one
such row is:

```python
                    "| ⬜ 7 | an old note naming 🟡 2 | `a:7` | answered | g |",
```

and a new case in `TestOpenFindings`:

```python
    def test_a_row_that_commissions_no_fix_still_closes(self):
        lines = reader.readable(
            record(
                "abc1234",
                [
                    "| ⬜ 1 | 🔴 a defect graded as a note | `a:1` | open | g |",
                    "| ❓ | 🔴 a blocking question | `a:2` | open | g |",
                    "| 🟢 | 🟡 marked green and left open | `a:3` | open | g |",
                    "| 4 | 🔴 the severity in the Finding cell | `a:4` | confirmed | g |",
                    "| 🟢 | round 1's 🔴 2 is closed | `a:5` | confirmed | g |",
                    "| ❓ | x | `a:6` | ❓ out of verified scope | g |",
                    "| ⬜ 7 | an old note | `a:7` | answered | g |",
                ],
            )
        )
        found, errors = chain.open_findings(reader, lines, "r.md")
        assert errors == []
        assert [(mark, word) for _line, mark, word in found] == [
            ("⬜ 1", "open"),
            ("❓", "open"),
            ("🟢", "open"),
            ("4", "confirmed"),
        ]

    def test_a_table_with_no_id_header_still_reads_a_severity_in_the_row(self):
        lines = reader.readable(
            "# r\n\n## Verdicts\n\n"
            "| Finding | No. | Location | Verdict | Grounds |\n"
            "|---|---|---|---|---|\n"
            "| x | 🔴 1 | `a:1` | confirmed | g |\n"
        )
        found, errors = chain.open_findings(reader, lines, "r.md")
        assert errors == []
        assert [(mark, word) for _line, mark, word in found] == [("x", "confirmed")]
```

`docs/the-review-record.md:70-76`:

```markdown
**A ready pull request fails while any row of any record reads a word that
does not close it.** A row's severity is its `#` cell, the column headed `#`. One
opening with 🔴 or 🟡 closes only by `fixed`, `answered` or
`deferred <home>`, never by `confirmed` or `out of verified scope`. One
opening with 🟢, ❓ or an old record's ⬜ commissions no fix and closes by
any closing word, so left at `open` it fails. Any other `#` cell — empty, a
bare number, a word — lost its severity: where a 🔴 or 🟡 stands anywhere in
the row it closes as a 🔴 or 🟡 row does, and otherwise by any closing word.
```

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/changelog.md:30-33`,
and the line counts at `:85-97` recounted after the fix:

```markdown
  every 🔴 or 🟡 row reads `fixed`, `answered` or `deferred <home>`, no row
  reads `open`, and the last round's commit is HEAD or only the work item's
  own records follow it. A row whose `#` cell lost its severity, empty or a
  bare number, counts as a finding where a 🔴 or 🟡 stands in it.
  `broad-gate.md` names HEAD.
```

Round 1's 🔴 1 Grounds cell keeps its text; the old-record ground it cites
is answered here.

### 🟡 2

Refresh the file the way `CONTRIBUTING.md:184-190` and the failing case's
own message name: from this branch's latest `tests` run,

```sh
gh run download <run id> -n test-durations -D <dir>
mv <dir>/.test_durations .test_durations
bin/test tests -q -k test_the_durations_file_prices_the_suite
```

or, where no run of this branch has the artifact, drop the entries the suite
no longer collects with the same round-trip guard 1b875efc used. Run it from
the repository root as a script file, not a heredoc:

```python
import json
import subprocess

out = subprocess.run(
    [".venv/bin/python", "-m", "pytest", "tests", "--collect-only", "-q"],
    capture_output=True, text=True, check=True,
).stdout
collected = {line.strip() for line in out.splitlines() if "::" in line}
with open(".test_durations", encoding="utf-8") as handle:
    text = handle.read()
data = json.loads(text)
assert json.dumps(data, indent=4) == text, "the file does not round-trip"
kept = {case: seconds for case, seconds in data.items() if case in collected}
with open(".test_durations", "w", encoding="utf-8", newline="\n") as handle:
    handle.write(json.dumps(kept, indent=4))
print(len(data) - len(kept), "dropped;", round(sum(kept.values()), 1), "s kept")
```

Either way, `bin/test tests -q -k test_the_durations_file_prices_the_suite`
exits 0 afterwards. The prune is expected to report 301 dropped and 3,371.9 s
kept, the figure the changelog fragment's suite-fall sentence and
`overview.md`'s 🟡 5 row then use.

### 🟡 3

`tests/test_one_word_one_meaning.py:470-472`:

```python
    WHY SEVEN PHRASES ARE THE WHOLE OF WHAT IS AT RISK, which is a fact about
    the MEMBER lists rather than about the phrases: `flat` folds the seam for
    `.py` members only, and across both sweeps four members are `.py`. Every
```

## Executed probes

| What was run | Result |
|---|---|
| `test_tmp_open_findings.py`: the shipped `open_findings` over 21 crafted rows and four header shapes; a stricter reading over every `round-N.md` in the tree | passed: `⬜ 3 … open`, `❓ … open`, `🟢 … open` with a 🔴 or 🟡 in the row, `1 \| 🔴 … \| confirmed`, `2 \| 🟡 … \| ❓ out of verified scope`, `carried \| 🔴 … \| confirmed`, `1 🔴 … confirmed`, an unknown mark `🟠 … confirmed`, bare `fixed`, `withdrawn`; named: emphasised, glued and doubled marks, `deferred` with no home, an empty verdict, `\#`, `✅`. A `No.` header passes `🔴 1 confirmed`. 36 records; the stricter reading finds no row in them |
| `test_tmp_candidate.py`: the three new `TestOpenFindings` inputs and the holes through c79670b6's, 2f0b4460's and the paste-ready `open_findings`; the paste over the 35 earlier records | c79670b6 names nothing for any of the three inputs; 2f0b4460 names what the cases assert and none of the holes; the paste names the holes and the `No.` header row, and the 35 records name nothing |
| `test_tmp_durations.py`: `.test_durations` at 61dcd638 and 2f0b4460 | 8,981 entries and 6,827 s before, 7,649 and 3,717 s after; 1,332 removed, 3,110 s, from 29 modules, none of which exists at 2f0b4460; nothing added, changed or reordered |
| `.venv/bin/python -m pytest tests --collect-only -q`, compared with `.test_durations` | 7,577 collected; 301 entries, 345.3 s, not collected, 81 of them in `test_the_seal_is_taken_once_by_the_sealer.py`; 229 collected cases unpriced |
| `bin/test tests -q -k test_the_durations_file_prices_the_suite` | exit 1: "345.3 s of the file's 3,717.2 s (9.3%) belong to 301 entries the suite no longer collects … over the 5% STALE_SHARE allows" |
| `bin/test` over `test_chain_check.py`, `test_broad_gate.py`, `test_a_reader_declares_its_input_class.py`, `test_one_word_one_meaning.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_ci_gives_the_checks_what_they_need.py`, `test_docs_line_wrap.py`, `test_a_phase_hands_the_next_one_a_record.py`, `test_a_document_that_names_a_script_says_how_to_reach_it.py`, `test_the_agent_contract_holds_the_universal_rules.py`, `test_the_changelog_is_gathered_at_release.py`, `test_the_release_table_reads_two_trees_and_fails_nothing.py`, `test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `test_the_release_check_watches_what_ships.py`, `test_no_real_identifiers.py` (`-q -rs`) | exit 0, 439 passed, 8 skipped: 6 "no shipped document names it", 2 "the suite was not collected" (the durations cases, run above) |
| `bin/rules --check --root <worktree>` | exit 0: all 400 `Enforced by:` targets in 60 rule files resolve |
| `wc -l` and `git diff --numstat ce448bbe 2f0b4460 -- tests` at 2f0b4460 | 1,135 · 3,400 · 228 · 45 · 143 lines; tests 31,995 deleted, 3,117 added; 143 test modules against 167 |
| `git show --name-only` for each `fixed <commit>` of round 1 | each touches its row's Location except 1b875efc, which touches `.test_durations` and `overview.md` and not `release_report.py` |
| the full suite | not run: `unverified`, the sealer's |

Every probe file sat under `<scratchpad>/923-r2/` and was deleted with it.
