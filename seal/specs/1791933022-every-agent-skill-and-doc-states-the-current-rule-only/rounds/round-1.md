# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — review round 1

| Field | Value |
|---|---|
| Target SHA | c79670b6 against ce448bbef731a5e05a48c3e403ada5bc1c094f19 |

Part A, phases 1–5, reviewed against `spec.md`, `plan.md` rows 1–5 and
`questions.md` Q7. Part B (phases 6–9) is out of this round's scope and
nothing below asks for it. Findings from reading and from execution are
labelled in each Grounds cell; every command named there is in
`## Executed probes`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | **A ready pull request passes with an open finding whose severity is not in the `#` cell.** `open_findings` counts a row only where `severity_of` finds 🔴 or 🟡 at the head of the first cell. A row reading `open` with its severity at the head of the Finding cell, with an empty `#` cell, with a word such as `carried` there, or in a table whose `#` column is not first, is no finding and passes. And `CLOSED_WORDS` now holds `confirmed` (and still `out of verified scope`), so a 🔴 or 🟡 row the warden wrote `confirmed` — "confirmed, still holds" — closes. The base's `open_blocking` refused any row with a 🔴 anywhere in it and a non-closing word, and its docstring named this exact narrowing as the repair that "would let a row whose verdict the vocabulary does not hold stop being refused at all". The deleted `tests/test_a_finding_id_is_a_bare_integer.py` held the generator's refusal of an empty or worded `#` cell; `phases/phase-3.md` says `TestOpenFindings` "reads the id", and it reads only the marker. The severity-in-the-Finding-cell shape is the one the 0.21.1 warden definition measured in two of three reviewers of one release | `skills/code-review/scripts/chain_check.py:573-599` | fixed 18315ee2 | executed: `test_tmp_probe.py` fed eight rows to `open_findings`; it named only the control row `🔴 8 open`, and the reordered table named nothing. read: `templates/sdd-round.md` tells every reader "a ready pull request fails while any 🔴 or 🟡 row reads anything else", and `spec.md` S3 says a row at `open` exits 1. read: the base's `open_blocking` at ce448bbe · fix pass: `open_findings` finds the `#` column by its header; a 🔴 or 🟡 there closes only by `FINDING_CLOSES` (`CLOSED_WORDS` less `confirmed` and `out of verified scope`); a 🟢, ❓ or ⬜ there is no finding; any other `#` cell (empty, a number, a word) is a finding that closes only by a closing word. Narrower than the paste on one point: a ⬜ row naming a 🟡 in its text stays no finding, because an old record carries exactly that (`⬜ 3 … same claim as 🟡 2 … open`). The refusal now reads `which closes no finding`, pinned in `TestMain::test_an_open_verdict_fails_a_ready_pull_request`; `docs/the-review-record.md` and the changelog fragment state the rule. Three new `TestOpenFindings` cases, each seen red on the shipped code (executed: 3 failed, 2 passed); five `mutation-check` breaks of the new units, each `red`. executed: `bin/test tests/test_chain_check.py` exit 1 before this record's cells were filled, its one failure `test_a_record_written_by_the_old_generator_reads` naming only this record's seven open rows, so the 35 earlier records read clean |
| 🟡 2 | **After a `not sound` verdict, the orchestrator is sent into a loop the sealer cannot leave.** The orchestration file says "`not sound` names the claim and the coordinate: fix that, commit, and spawn the sealer again at the new HEAD". A fix to code is a commit outside the work item after the last round's `Target SHA`, so the records arm refuses it, and the sealer's own broad run asks that arm first under `--sealing`, which excuses only `broad-gate.md` and `guarantee.md`. The sealer comes back NOT SEALED, writes `not sound` again, and nothing tells anyone that a verifying round is owed in between | `skills/code-review/orchestration.md:163-168` | fixed fabc1eba | executed: `test_tmp_not_sound_loop.py` built a branch with a record at the code commit and one fix commit after it, then ran `chain_check.main(["--baseline", "main", "--root", …, "--sealing"])` as a ready pull request: exit 1, naming `rounds/round-1.md` *a verifying round is owed*. read: `broad_gate.py:3076-3082` runs the chain check with `--sealing` as one of its arms · fix pass: the paragraph rewritten in place: a repair to the work item's own records or the pull request body goes straight back to the sealer; a repair to any other file is committed, a verifying round runs on its diff, and the sealer is spawned once that round's record is committed, with the reason. No other file states the `not sound` path (`grep` of `agents/`, `docs/`, `templates/`, `skills/`). executed: the six modules reading `orchestration.md`, exit 0 |
| 🟡 3 | **The `fix of a fix` stop names a test that does not hold it.** `docs/the-review-record.md` §*The run* ends the rule with `Enforced by: tests/test_chain_check.py::TestFrame`. `TestFrame`'s two cases check that `spec.md` carries the mark and that a `Reframed` line names the framer; nothing reads the `fix of a fix` mark or refuses a fix pass after it. `spec.md` §*What leaves* says of this rule "Checked by nothing; the sealer reads the records", and S9 says `chain_check.py` reads nothing of the mark. `rules --check` passes, so a reader takes the stop for a mechanical one | `docs/the-review-record.md:168` | fixed fb519b50 | read: `tests/test_chain_check.py:450-485`, `chain_check.py#frame`. executed: `bin/rules --check` exit 0, which is why nothing flags it · fix pass: `Enforced by: nothing — the orchestrator applies it, and the sealer reads the mark in the records`, the form the cap and the ladder rules use and what `spec.md` S9 and §*What leaves* say. executed: `bin/rules --check` exit 0, 400 targets in 60 files |
| 🟡 4 | **`spec.md` §*Removes* names three broad-gate units that still stand, and no divergence says so.** The row *the broad gate's record arms* lists `broad_gate.py#seal_home`, `#round_count` and `#rounds_rows`; all three are in the tree, `rounds_rows` still reading every record through `chain_check.verdict_table` for the panel's `rounds` row. `seal_home` is the root resolver the gate needs, and §*Data & interfaces* also says the panel is unchanged, so the spec contradicts itself and the build kept the working half. The sealer's step 3 confirms "nothing of it stands" for every `## Removes` row, so this item's own guarantee will read `not sound` on its own paperwork unless the row or `overview.md` says what stayed and why | `seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:420` | fixed 1a985894 | read: `skills/verify/scripts/broad_gate.py:705`, `:2567`, `:2619`; `overview.md` and `phases/*.md` name none of the three (`grep` returned nothing) · fix pass: `round_count` had no caller in the tree and is removed. `seal_home` and `rounds_rows` stay, because something live needs each: `seal_home` is the gate's root resolver, through which it reads the `Broad gate` command from `config.md`, and the record arm the frame meant was the generator's `round_record.seal_home` call (the base's `broad_gate.py:2643`), gone in phase 3; `rounds_rows` draws the panel's `rounds` row, which §*Data & interfaces* keeps unchanged. The §*Removes* row and the §*Data & interfaces* sentence are rewritten in place to say so, and `overview.md` gains a divergence row quoting both sides. executed: `tests/test_broad_gate.py`, `tests/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/test_a_reader_declares_its_input_class.py` exit 0 |
| 🟡 5 | **The release table will print the suite at 6,827 s where it now runs about 3,717 s.** `release_report.py#suite_seconds` sums every entry of `.test_durations`, and the branch left 3,110 s of entries for the 29 test modules it deleted (`phases/phase-3.md`: "the file was not refreshed by this phase"). The table on 0.22.0's release pull request is what the person preparing the release reads to see the suite fall, and S12's whole point is that fall | `.github/scripts/release_report.py:113-131` | fixed 1b875efc | executed: summed `.test_durations` in Python: 6,827 s over 8,981 entries, 3,110 s of them under 29 module paths that no longer exist · fix pass: the 1,332 entries of the 29 deleted modules dropped by a script that refused unless the file round-tripped byte for byte, so every kept entry is unchanged; nothing re-measured, and the file now sums to 3,717 s over 7,649 entries. `suite_seconds` is left as it is: the paste's filter on existing modules would be new mechanism in a fix pass, and the stale entries it guards against are gone. `overview.md`'s row that left the stale entries as history is rewritten in place. executed: the three modules reading `.test_durations`, 79 passed, 2 skipped, exit 0 |
| 🟡 6 | **Four shipped files still tell a user or an orchestrator about the `Pass` box and `Fixes checked by`.** `README.md:180-187`: CI "requires a committed round record whose `Pass` does not contradict its own verdict table", and "Each round record also has to say who opened the fixes"; `README.ko.md:171-179` the same in Korean. `templates/hygiene.yml:33-37`, which a plugin user copies: "`chain_check.py` … requires a checked `Pass` on the last round". `skills/code-review/orchestration.md:79-83`: "the box saying the review passed is ticked by the session that wrote them"; `:14`: "Nothing here changed when it moved", false since this branch rewrote three of its sections; `:245`: "Record both SHAs in `round-N.md`", an instruction to edit the warden's file, which the record now has one field for and nobody else writes | `README.md:180` | fixed 0b435be9 | read: each line above at c79670b6; the `git grep` over the shipped tree in `## Executed probes` · fix pass: each sentence rewritten in place: both READMEs state the open-row rule and drop the `Fixes checked by` paragraph's lead; `templates/hygiene.yml` names the four refusals a draft defers; `orchestration.md` says the last round's fixes have no reader unless a round is spawned, drops "Nothing here changed when it moved", and says the next round's `Target SHA` names the new HEAD. A `git grep` for `Pass` box, `Fixes checked by` and `who opened the fixes` outside the records finds only the test docstrings of 🟡 7. executed: the 37 modules naming `hygiene.yml`, a README, `code-review/orchestration` or `verifying round`, 2,058 passed, the one failure this record's open rows |
| 🟡 7 | **Test modules still name the three deleted documents and the removed mechanisms, and two leftovers stood only on them.** Docstrings and comments cite `docs/review-handoff-protocol.md`, `docs/round-record-spec.md` or `docs/review-chain-spec.md` as the source of what they pin: `tests/test_ci_gives_the_checks_what_they_need.py:15`, `:35-36`, `:414` (and its `Pass` requirement), `tests/test_a_phase_hands_the_next_one_a_record.py:13`, `tests/test_session_cost.py:541`, `:3243`, `tests/test_one_word_one_meaning.py:360`, `tests/test_docs_line_wrap.py:182-185`, `tests/test_the_agent_contract_holds_the_universal_rules.py:232`. `tests/test_no_passage_is_pasted_into_a_second_file.py:231` keeps an exemption for a pair whose second file is gone. `tests/conftest.py:296-340` keeps `committed_round_records_on_disk` and `ROUND_RECORD_NAME`, whose every caller was a deleted module. A smith extending one of these groups reads the deleted file as where the rule lives | `tests/test_ci_gives_the_checks_what_they_need.py:35` | fixed d31a8fc0 | read: each coordinate; executed: `git grep -n committed_round_records_on_disk` finds the definition and no caller outside `seal/specs/` · fix pass: every coordinate listed rewritten in place to `docs/the-review-record.md` or the current rule, the `("agents/smith.md", "docs/review-chain-spec.md")` exemption deleted, and `ROUND_RECORD_NAME` and `committed_round_records_on_disk` deleted. The class was enumerated by `git grep` over `tests/` for the three documents, `round_record`, `Pass` and the helper: also rewritten are the present-tense claims in `test_the_seal_is_taken_once_by_the_sealer.py` (its docstring's `seal` subcommand and `Pass` box, the scripts a fixture starts), `conftest.py#gathered_entry`'s `BLOCK_START` comment, `test_docs_line_wrap.py`'s `fenced_after` sentence, two in `test_a_document_that_names_a_script_says_how_to_reach_it.py`, one each in `test_one_word_one_meaning.py` and `test_unverified_rows_close.py`, and a second in `test_a_phase_hands_the_next_one_a_record.py`. History true as written stays (#226, #318, #526, #590 and the fixtures' fake `round_record.py` paths). `gathered_entry`'s comment edit moved its census hash, so it declares `Reads:` and its `undeclared_readers.txt` line leaves. executed: ruff check and format on the 11 files, exit 0; the 10 touched test modules with the census, shrunken-corpus and settle modules, 1,071 passed and the census red until the declaration, then `test_a_reader_declares_its_input_class.py` 76 passed |
| ❓ | The three guarantor cases (S6, S7) have never run against a model, and what one guarantor run costs (`questions.md` Q2) is unmeasured; the sealer that will audit this branch is its first run | `evals/behaviour/sealer/` | ❓ out of verified scope | read: `phases/phase-4.md` "No session ran", recorded with its answerer in `overview.md`. Answerer: the orchestrator, at this branch's sealer spawn |
| ❓ | Q7's default on GitHub itself: whether 0.22.0's release pull request reads the real squash commits as carried | `skills/code-review/scripts/chain_check.py:237-275` | ❓ out of verified scope | read: the probe in `phases/phase-5.md` made its squash locally under GitHub's identity; `overview.md` names the release pull request's first hygiene run and the owner as answerers |
| 🟢 | Q7 is built as the orchestrator's default answered it: a declaration every commit after the base touched as a GitHub squash ending `(#N)` is named and not judged; one naming the branch, or touched by any other commit, an uncommitted change or no commit, is judged | `skills/code-review/scripts/chain_check.py:237-275`, `:1027-1037` | confirmed | read: `carried_by` and `main`; `docs/the-review-record.md` §*What the check reads at the pull request* and `skills/settle/SKILL.md:110-113` say the same. executed: `TestCarriedBy` and the two `TestMain` release cases pass |
| 🟢 | The check reads every record in the tree: `Target SHA` and the verdict table of all 35 `round-N.md` under `seal/specs/` read with no error, no open row and a SHA each (S11) | `seal/specs/*/rounds/` | confirmed | executed: `test_tmp_old_records.py` |
| 🟢 | The five arms, the template, the guarantee template, `broad-gate --record` on both routes, `rules --check` and the release table match `spec.md` §*Data & interfaces* and `plan.md` rows 1–5, apart from findings 1, 4 and 5; every chain-check arm §*Removes* names is gone | `skills/code-review/scripts/chain_check.py`, `templates/sdd-round.md`, `templates/sdd-guarantee.md`, `.github/scripts/rules.py`, `.github/scripts/release_report.py` | confirmed | read: the files against the spec; the base's function list against the new one (`comm`). executed: the narrow modules, 160 passed; `bin/rules --check` exit 0, 401 targets in 60 files; `chain_check.py --baseline origin/release/v0.22.0` exit 0, naming the three files this branch does not carry yet |
| 🟢 | Of the deleted check and test modules, only the open-row reading of finding 1 lost a guard the spec did not decide to drop; `gate_before_review`'s premature-run refusal is held by `follows`, and `rounds_unreadable`'s state now reads as *holds no `round-N.md`*, loudly | `skills/code-review/scripts/chain_check.py:634-667`, `:744-789` | confirmed | read: the base's `gate_before_review`, `rounds_unreadable` and `open_blocking`, and `phases/phase-3.md`'s table of 28 modules |
| 🟢 | The rewritten repository rules hold in this diff: `CLAUDE.md` and `CONTRIBUTING.md` are rewritten in place rather than appended to, and no example or fixture carries a real identifier | `CLAUDE.md`, `CONTRIBUTING.md` | confirmed | read: their diff hunks. executed: `tests/test_no_real_identifiers.py` among the 160 passed |

## Paste-ready fixes

### 🔴 1

`skills/code-review/scripts/chain_check.py`, replacing `open_findings`:

```python
# The words that close a 🔴 or 🟡 finding. `confirmed` is a 🟢 row's word and
# `out of verified scope` a ❓ row's: neither answers a finding.
FINDING_CLOSES = CLOSED_WORDS - {"confirmed", OUT_OF_SCOPE}


def open_findings(reader, lines, rel):
    """([(line, the `#` cell, the verdict word)], errors) for every row that
    carries a 🔴 or 🟡 and whose verdict does not close it.

    A row whose `#` cell opens with 🔴 or 🟡 closes only by a fix pass's word.
    A row whose `#` cell carries neither is still a finding where a 🔴 or 🟡
    stands anywhere in it and its verdict closes nothing, so a severity at
    the head of the Finding cell, an empty `#` cell or a reordered table
    fails a ready pull request rather than passing it.

    Reads: guess — the warden's record, through `verdict_table`; unknown refused"""
    rows, col, _header, errors = verdict_table(reader, lines, rel)
    if col < 0:
        return [], errors
    found = []
    for line, seen in rows:
        word = verdict_of(seen, col)
        if severity_of(seen) in FINDINGS:
            still_open = word not in FINDING_CLOSES
        else:
            still_open = word not in CLOSED_WORDS and any(
                mark in "".join(seen) for mark in FINDINGS
            )
        if still_open:
            found.append((line, seen[0].strip() or f"row at line {line}", word))
    return found, errors
```

Run over the probe rows it names `1 open`, `row at line 8 open` and
`🔴 4 confirmed`, and over the 35 records in the tree it names nothing
(`test_tmp_fix_check.py`). `tests/test_chain_check.py`, in
`TestOpenFindings`:

```python
    def test_a_finding_the_id_cell_does_not_mark_is_still_open(self):
        lines = reader.readable(
            "# r\n\n## Verdicts\n\n"
            "| # | Finding | Location | Verdict | Grounds |\n"
            "|---|---|---|---|---|\n"
            "| 1 | 🔴 severity in the finding cell | `a:1` | open | g |\n"
            "|  | 🟡 empty id cell | `a:2` | open | g |\n"
            "| 🔴 3 | closed by a 🟢 row's word | `a:3` | confirmed | g |\n"
            "| 🟢 | round 1's 🔴 2 is closed | `a:4` | confirmed | g |\n"
        )
        found, errors = chain.open_findings(reader, lines, "r.md")
        assert errors == []
        assert [(mark, word) for _line, mark, word in found] == [
            ("1", "open"),
            ("row at line 8", "open"),
            ("🔴 3", "confirmed"),
        ]
```

### 🟡 2

`skills/code-review/orchestration.md:163-168`:

```markdown
**Commit the sealer's two files together; a verdict other than `sound` keeps
the pull request a draft.** `not sound` names the claim and the coordinate.
Where the repair touches only the work item's own records — a phase record,
the changelog fragment — or the pull request body, make it, commit, and spawn
the sealer again at the new HEAD. Where it touches anything else it is a fix
nobody reviewed: commit it, spawn a verifying round on its diff, and spawn
the sealer once that round's record is committed, because the sealer's broad
run asks the records arm first and the arm refuses a commit after the last
round's `Target SHA`. `undecidable` is a question for the owner, put after
the run rather than during it; write the answer under the verdict as
`Answered <date> by <who>: <answer>`, commit, and spawn the sealer again.
```

### 🟡 3

`docs/the-review-record.md:168`:

```markdown
Enforced by: nothing — the orchestrator applies it, and the sealer reads the mark in the records
```

### 🟡 4

`seal/specs/1791933022-every-agent-skill-and-doc-states-the-current-rule-only/spec.md:420`,
the row rewritten in place to what the build did:

```markdown
| the broad gate's record arms | `broad_gate.py#sealed_record`, `#kept_broad_gate`-through-`round_record`, the `round_record` import, the `Broad gate` cell write | `broad-gate.md`, one home; `#seal_home` (the root resolver), `#round_count` and `#rounds_rows` (the panel's `rounds` row, which §*Data & interfaces* keeps unchanged) stay |
```

### 🟡 5

`.github/scripts/release_report.py`, the sum in `suite_seconds`, so a
duration file left stale by a deletion prices only the cases that exist:

```python
    return sum(
        seconds
        for case, seconds in data.items()
        if os.path.isfile(os.path.join(root, *case.split("::")[0].split("/")))
    )
```

and in the same commit drop the 29 deleted modules' entries from
`.test_durations` (a refresh from the next green run, as `CONTRIBUTING.md`
describes, does both halves of the file). A case in
`tests/test_the_release_table_reads_two_trees_and_fails_nothing.py`:

```python
def test_the_suite_prices_only_the_cases_whose_module_exists(tmp_path):
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_kept.py").write_text("", encoding="utf-8")
    (tmp_path / ".test_durations").write_text(
        json.dumps({"tests/test_kept.py::t": 2.0, "tests/test_gone.py::t": 40.0}),
        encoding="utf-8",
    )
    assert report.suite_seconds(str(tmp_path)) == 2.0
```

(`report` and `json` are that module's own names, `tests/…:14` and `:32`.)

### 🟡 6

`README.md:179-187`:

```markdown
guessing from the absence of a mark. The check moved to the pull request: CI
reads the same file out of the diff and, for anything routed through the
chain, requires a committed round record with no 🔴 or 🟡 row left open. A
pull request that declared neither way is not failed; it gets a notice
saying nothing was checked.

A round's findings are closed after it ends, by whoever writes the fixes,
and the round that follows is what reads them — except after the last round,
where nobody did. So a run ends with a **verifying round**:
```

`README.ko.md:171-179`:

```markdown
요구합니다. 그 기록의 판정표에 열린 🔴·🟡 행이 남아 있으면 막습니다. 어느 쪽도
선언하지 않은 PR 은 실패시키지 않고, **아무것도 검사하지 못했다**는 알림만
남깁니다.

한 회차의 지적은 그 회차가 끝난 뒤에 수정으로 닫히고, 그 수정을 읽는 것은
다음 회차입니다. 마지막 회차만 예외였습니다 — 아무도 읽지 않았습니다.
```

`templates/hygiene.yml:33-37`:

```yaml
    # so nothing re-runs. `chain_check.py` reads the draft state, and fails
    # an open finding, a record behind HEAD, or a missing `broad-gate.md` or
    # `guarantee.md` only once the draft is over.
```

`skills/code-review/orchestration.md:79-83`, `:14` and `:244-245`:

```markdown
A round's findings are closed after it ends, by whoever writes the fixes. Every
round but the last has a reader for those fixes — the round that follows, since
each of its verdicts needs an answer there. The last round's fixes have none
unless a round is spawned for them.
```

```markdown
The headings keep the `Orchestrator:` prefix they were written with, so a
reference to one of these sections names the section it always named and
only the file it names changed (#265).
```

```markdown
Also check whether HEAD moved during the review; if source changed, those
verdicts need a re-pass, and the next round's `Target SHA` names the new HEAD.
```

### 🟡 7

`tests/test_no_passage_is_pasted_into_a_second_file.py:231`, the line
deleted:

```python
    ("agents/smith.md", "docs/review-chain-spec.md"): 3,
```

`tests/conftest.py:296-340`: delete `ROUND_RECORD_NAME` and
`committed_round_records_on_disk` whole.

`tests/test_ci_gives_the_checks_what_they_need.py:34-36`:

```python
# Events GitHub does NOT include by default and that this repository needs,
# because a draft is the documented way past `chain_check.py`'s refusals
# (`docs/the-review-record.md` §*What the check reads at the pull request*).
```

and the same re-pointing in each other docstring the finding names: the
deleted document replaced by the section of `docs/the-review-record.md`
that now states the rule (§*The handoff* for the per-segment bars and the
handoff, §*The round record* for the record's shape), and the `Pass` and
`Fixes checked by` sentences rewritten to the open-row and last-record
rules.

## Executed probes

| What was run | Result |
|---|---|
| `bin/test tests/test_chain_check.py tests/test_broad_gate.py tests/test_the_sealer_guarantees.py tests/test_evals_layout.py tests/test_every_orchestrator_act_names_its_delivery.py tests/test_the_rules_command_reads_each_rule_off_its_test.py tests/test_the_release_table_reads_two_trees_and_fails_nothing.py tests/test_no_real_identifiers.py tests/test_a_rewritten_definition_proved_non_inferior.py -q` | exit 0, 160 passed in 4.99 s |
| `bin/rules --check` | exit 0: all 401 `Enforced by:` targets in 60 rule files resolve |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.22.0 --root .` | exit 0, judged as unknown (no pull request yet); names three refusals as notices: no `round-N.md`, no `broad-gate.md`, no `guarantee.md` |
| `test_tmp_probe.py`: `open_findings` over eight verdict rows and a reordered table; `verdict_word` over five spellings | only `🔴 8 open` named; rows with the severity in the Finding cell, an empty or worded `#` cell, `confirmed` and `❓ out of verified scope` on 🔴/🟡 rows, bare `fixed` and `withdrawn` all pass; the reordered table names nothing; `Sound.` and `sound — see note` are not `sound` |
| `test_tmp_old_records.py`: `open_findings` and `target_of` over every `seal/specs/*/rounds/round-N.md` at c79670b6 | 35 records, no error, no open row, a SHA in each |
| `test_tmp_not_sound_loop.py`: a branch whose record names the code commit, then one fix commit, judged by `chain_check.main([... "--sealing"])` as a ready pull request | exit 1: `rounds/round-1.md` *the last round's `Target SHA` is behind HEAD … a verifying round is owed* |
| `test_tmp_fix_check.py`: the 🔴 1 fix's `open_findings` over the probe rows and the 35 records | names `1 open`, `row at line 8 open`, `🔴 4 confirmed`; no record refused |
| `test_tmp_record_reads.py`: the 🔴 1 case's four rows through the shipped `open_findings` and through the fix; this record through `target_of` and `open_findings` | shipped: names nothing (the case is red on it); fix: `1 open`, `row at line 8 open`, `🔴 3 confirmed`. This record: `c79670b6`, seven open rows, no error |
| Python: sum of `.test_durations`, and of the entries whose module file is gone | 6,827 s over 8,981 entries; 3,110 s under 29 missing module paths |
| `git grep` over the shipped tree (excluding `seal/specs`, `seal/releases`, changelogs, `.test_durations`, replay prompts) for the removed generator, guard, documents, fields and sections | the hits listed in 🟡 6 and 🟡 7, plus history in comments (`round 1's ⬜ 4`) and `evals/scripts/replay_targets.py`'s asked-paragraph reader, which `overview.md` already hands to part B |
| `comm` of the base's and the new `chain_check.py` function names | every removed function is in §*Removes* or only they called it, except `gate_before_review`, `rounds_unreadable` and `config_at_head`, each read and covered or dead with the pact notices |

Every probe file sat under the round's scratch directory and was deleted
with it.
