# 1791384155-a-round-record-cell-has-one-reader — review round 2 report

Verifying round over round 1's fixes, `b10835ff..092808fe` (d2eed6d1,
092808fe), plus the table and close commits, at target
03779b65f1549fe7ce75553080655366cd460b05. Draft pull request #890 into
`release/v0.21.0`. The review ran in a scratch clone of the worktree at the
target. Base-side copies were taken at b10835ff (round 1's target) and
ad447367 (the release branch the work item merged).

## The short answer

The four fixes do what round 1 asked. The unknown state behaves like a draft
in every reader that reads it, and a payload that cannot answer still behaves
like a ready pull request. But the fix pass broke one thing CI reads, and left
three sentences that still describe a draft:

```
round 1's fix pass
  ├─ the unseen state reads as unknown, which every arm treats as a draft  (holds)
  ├─ docs: one sentence written into two documents ───► CI red on 3 legs  (🔴 1)
  └─ notices written for a draft now print for a run nobody observed     (🟡 2)
```

## 🔴 1 — The fix pass pasted one sentence into two documents, and CI fails on it

`docs/review-chain-spec.md:656` and the `nobody — <why>` row at
`docs/round-record-spec.md:65` now both carry *and where a payload cannot
answer. In a draft, or where no pull request was seen,*. That is two new
15-word runs shared between the pair. The two documents were measured at 31
shared runs, and they now share 33.

`gh pr checks 890` at 03779b65 shows `pytest (ubuntu-latest)`, `pytest
(macos-latest … --group 2)` and `pytest (windows-latest … --group 2)` failing.
Each fails the same two cases, `test_no_pair_shares_more_than_it_was_measured_at`
and `test_a_removed_copy_passes_without_a_baseline_edit` in
`tests/test_no_passage_is_pasted_into_a_second_file.py`. Round 1 read every leg
green at db5595c8, so the red comes from this fix range.

- **Executed:** that module in the scratch clone at the target gives 2 failed
  and 6 passed. A probe counted the shared runs with the module's own
  counter: 31 at b10835ff and 33 at 092808fe and at HEAD. Exactly two windows
  are new, and both are the phrase above. No window disappeared.
- **Why it matters:** the pull request cannot go ready while three required
  legs are red. The sealer's broad run would hit the same failure. The smith's
  fifteen modules did not include this one, so the handover's account of a
  passing state did not reach it.
- **The fix:** reword the copy in `docs/review-chain-spec.md` so it no longer
  repeats the table row. Leave the row alone, because it is the refusal
  table's home. The probe measured the rewording below at 31 runs again. It
  keeps the paragraph at three lines, which matters because that document
  sits at 999 lines. Its widest line is 79 columns.

## 🟡 2 — A run nobody observed prints notices that say it is a draft

Round 1's 🟡 1 included a false sentence: the `Broad gate` arm told the reader
the rounds had settled. The fix corrected that sentence. But the fix also made
`strict` false for the unseen state (`chain_check.py:5737-5738`). So every
notice written for the draft branch of `strict` now prints for a run with no
pull request at all. Three of those notices state that a draft exists:

| Where | What it prints under the unseen state |
|---|---|
| `skills/code-review/scripts/chain_check.py:5956` | holds no `round-N.md` *— which is the state a draft pull request opens in* |
| `skills/code-review/scripts/chain_check.py:2721` | the pair is *the state a draft is in*, and *it prints because a draft is not a request to merge* |
| `skills/code-review/scripts/chain_check.py:5095` | an open note *prints because a draft is not a request to merge* |

The line above them reads *the pull request's state is unknown*, so the same
output tells two stories. Each notice then sends the reader to *Ready for
review*. On a `stop before the pull request` route, or before the draft
opens, there is no such button. This is the same kind of false sentence round
1 named. The agent contract's §12 says to fix every instance of a defect's
class, and §14 says a changed message is pinned in the same commit. No case
pins any of the three texts. A grep of `tests/`, `docs/` and `skills/` found
no other reader of them.

- **Executed:** the branch's check over every record in the tree, run with
  `gh` answering unknown, printed the first notice for eight declarations. The
  sample lines the probe printed show it, and they are byte-identical to the
  draft run.
- **Read:** the other two notices come from code in `checked_by` and
  `carried_notes` that reads `strict` alone. No record in this tree reaches
  them under that probe.

## ⬜ 3 — The unseen state's line promises a CI run that local mode never makes

`UNSEEN_SAYS` (`chain_check.py:1335`) ends *CI judges it from GitHub's
payload*. In local mode no hygiene copy is installed. `templates/hygiene.yml`
lines 12-22 explain why, and say `chain_check.py` never runs there. On a
`stop before the pull request` route there is no CI run either (`questions.md`
Q1). Where CI does run, the sentence is true, and the behaviour matches the
base in both cases. Something like *only a run with GitHub's payload judges it
as ready* would be true everywhere. The pin at
`tests/test_chain_check_at_the_pull_request.py:308` would change with it.

## ⬜ 4 — `event_payload_present` is a second reader of a fact `pull_request_state` already decided

`chain_check.py:1341` repeats the first test in `pull_request_state`
(`chain_check.py:1302-1303`) byte for byte. The two agree today. The probe ran
a directory, an empty file, a file that does not parse and a payload with no
pull request, each with `gh` answering draft. All four read as ready, with
output identical to a ready payload's. The two tests still split two ways:

- If a payload is deleted between the two calls, an unreadable payload reads
  as unseen when it should read as ready.
- A later change to the payload rule in one function would not reach the
  other.

This work item exists to give each fact one reader. Having
`pull_request_state` return whether it read a payload, beside the state, would
remove the second reader. Nothing is wrong at this SHA.

To the question asked: it cannot tell a real GitHub event from a stray file,
and it does not need to. A stray file that is not a pull-request payload is
judged as ready, which is stricter than unknown. A stray file that says
`"draft": true` is read as a draft. The base does the same, and this diff
does not change it.

## ⬜ 5 — A note keeps a closing mark the home opened

`deferred_parts` (`chain_check.py:1947`) now cuts the note from the cell as
written. Every note the probe produced is a byte-for-byte substring of its
cell, so no byte is rewritten. But a span opened before `HOME_END` leaves its
closing half in the note. `**deferred #854 — the note**` gives the note
`the note**`, and a home in a code span that contains an em dash gives
`` b` ``. In the Grounds cell `close` writes, that renders as stray marks. No
cell in the tree has this shape. It is a note, not a fix.

## What held

- **Unknown is never read as ready, and ready is never read as unknown**
  (executed). The base's and the branch's `chain_check.py` ran over the
  branch's tree, with a grafted empty root so that every declaration counts as
  changed. The results by state:
  - Branch, `gh` answering unknown, and branch with no `gh`: byte-identical
    bodies (139 lines) to the branch with `gh` answering draft.
  - Branch with `gh` answering ready: byte-identical to a ready payload (145
    lines).
  - Branch with each of four payloads that cannot answer, and `gh` answering
    draft: byte-identical to a ready payload. The payload wins, and `gh` is
    not asked.
  - Base against branch with a draft payload: identical.
  - Base against branch with a ready payload: one line differs, the sealer
    advice, as intended.
  - Base with no payload (judged ready) against branch with `gh` answering
    unknown: the ready-only refusals become draft notices. That is the
    intended change.
- **Only one place computes `strict`** (read). It is `main` at
  `chain_check.py:5738`. `round_record.py` reaches the check only through
  `run_check`, and the broad gate only through a subprocess with `--sealing`.
  No reader parses the state line.
- **Each new case was seen red** (executed). The probe restored
  `chain_check.py` and `broad_gate.py` from b10835ff in the scratch clone:
  - both new `test_the_panels_capped_is_the_gates_reopening` cells failed
  - both new `test_a_deferrals_home_is_what_stands_after_the_word` cells
    failed
  - `test_a_pull_request_nobody_observed_is_unknown_not_ready` failed

  Restoring the files turned them green again.
- **The `deferred_parts` rewrite changes no home a real record holds**
  (executed). Across 90 deferral cells from every table row and string literal
  in the tree, plus 14 written to break it, the home moved in three. One is a
  docs vocabulary cell that is no verdict. One is `_🟢_ deferred #1`, a marker
  inside underscores that nobody writes. One is `deferred #854. — note`, whose
  home is now `#854` where it was `#854.`, which matches the no-note reading.
  No note differs beyond its marks.
- **The helpers say what they mean** (read). Ten helpers pass `gh_answers(…,
  "ready")`. `tests/test_the_fixes_close_the_record.py` imports one of them.
  The helpers that keep the default now run unknown, which the probe above
  shows is identical to draft.

## Round 1's verdicts

| Round 1 | This round |
|---|---|
| 🟡 1 the generator's exit 1 outside a draft | closed (executed above). The sealer sentence it named is fixed. Three siblings are 🟡 2 |
| 🟡 2 the draft stub | closed (read and executed) |
| 🟡 3 the panel's input | closed (executed, red without the fix) |
| 🟡 4 the note's marks | closed (executed, red without the fix). ⬜ 5 is a remainder |
| ⬜ 5 `gh pr view` by branch name | the smith's note stands. CI reads the payload, and the probe shows a payload always wins |
| ⬜ 6 `--sealing`'s scope | the smith's note stands. `sealing_excuses` excuses only the `Broad gate` arm's errors |

## Regression tests to plant

- `tests/test_chain_check_at_the_pull_request.py`: under `gh="unknown"`, the
  empty-`rounds/` notice names the unobserved state (part of 🟡 2's fence).

## Facts for the evidence ledger

- The `docs/review-chain-spec.md` and `docs/round-record-spec.md` pair holds
  31 shared 15-word runs at b10835ff. Any edit to one of them that touches the
  `nobody — <why>` wording has to be measured against
  `tests/test_no_passage_is_pasted_into_a_second_file.py`.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🔴 1 | The fix pass wrote one phrase into both docs, so the pair shares 33 runs where 31 were measured, and three CI pytest legs fail at the target | `docs/review-chain-spec.md:656` | open | executed: the module fails 2 of 8 in the scratch clone; the shared-run count is 31 at b10835ff and 33 at 092808fe; read: `gh pr checks 890` shows three legs failing the same two cases |
| 🟡 2 | With the state unknown, three notices still say a draft exists and send the reader to *Ready for review* | `skills/code-review/scripts/chain_check.py:5956` | open | executed: the unknown run prints the first notice for eight declarations, byte-identical to draft; read: the same wording at `chain_check.py:2721` and `chain_check.py:5095`; no case pins any of them |
| ⬜ 3 | The unseen state's line says CI judges it, and in local mode and on a route that stops before the pull request nothing does | `skills/code-review/scripts/chain_check.py:1335` | open | read: `templates/hygiene.yml` lines 12-22; `questions.md` Q1 |
| ⬜ 4 | `event_payload_present` re-decides what `pull_request_state` already decided, which makes a second reader of one fact | `skills/code-review/scripts/chain_check.py:1341` | open | read; executed: the two agree on a directory, an empty file, a file that does not parse and a payload with no pull request |
| ⬜ 5 | A note keeps a closing mark that the home opened (`**deferred #854 — the note**` gives `the note**`) | `skills/code-review/scripts/chain_check.py:1947` | open | executed on written cells; no cell in the tree has this shape |
| 🟢 | round 1's finding 1 is closed — an unseen pull request reads as unknown, and the generator does not fail the record it wrote | `skills/code-review/scripts/chain_check.py:5737` | confirmed | executed: unknown and no-`gh` output identical to draft over every record; payloads that cannot answer identical to ready; the new case fails without the fix |
| 🟢 | round 1's finding 2 is closed — the suite's stub defaults to unknown, and the helpers that mean ready say so | `tests/conftest.py:559` | confirmed | read: ten helpers on `gh_answers(…, "ready")`; executed: unknown is identical to draft |
| 🟢 | round 1's finding 3 is closed — the panel hands `says_reopened` the gate's string | `skills/verify/scripts/broad_gate.py:2942` | confirmed | executed: both invisible-led cells fail without the fix and pass with it |
| 🟢 | round 1's finding 4 is closed — the note keeps its marks | `skills/code-review/scripts/chain_check.py:1943` | confirmed | executed: both new cells fail without the fix; 90 cells, every note verbatim, no real home moved |
| 🟢 | round 1's notes 5 and 6 stand as the smith answered them | `skills/code-review/scripts/chain_check.py:1302` | confirmed | executed: a payload always wins over `gh`; read: `sealing_excuses` excuses one arm |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the eight guard modules, in the scratch clone at 03779b65 | 437 passed, exit 0 |
| the branch's `chain_check.py` over the branch's tree, every declaration counted as changed (grafted empty root), under `gh` unknown, no `gh`, `gh` draft, `gh` ready, a draft payload, a ready payload, and four payloads that cannot answer with `gh` draft | unknown and no `gh` identical to `gh` draft (139 lines); `gh` ready identical to a ready payload (145 lines); all four payloads that cannot answer identical to a ready payload; all exit 1, on squash-removed `Target SHA` commits |
| the base's (ad447367) `chain_check.py` over the same tree with no payload, a draft payload and a ready payload | draft identical to the branch's; ready differs by the sealer advice line alone; no payload (ready at the base) against the branch's unknown: ready-only refusals become draft notices |
| `tests/test_no_passage_is_pasted_into_a_second_file.py` in the scratch clone at 03779b65 | 2 failed, 6 passed, exit 1, the same two cases as CI |
| the module's own shared-run counter over the two docs at b10835ff, 092808fe and HEAD | 31, 33, 33; two new windows, both the phrase in 🔴 1 |
| the same counter with 🔴 1's rewording applied in memory | 31 |
| `chain_check.py` and `broad_gate.py` restored from b10835ff, then the new panel, deferral and unknown-state cases | 2 failed (panel); then 3 failed (2 deferral, 1 unknown state); green once the files were restored |
| `deferred_parts` at b10835ff and at the target over 90 deferral cells from the tree plus 14 written to break it | home moved in 3, none a real record's; no note differs beyond its marks; every note is a substring of its cell |
| `gh pr checks 890` | read: three pytest legs fail on `tests/test_no_passage_is_pasted_into_a_second_file.py`, every other leg passes, at head 03779b65 (CI's run, read here) |
| the full suite, the repository-wide lint and the typecheck (the broad gate) | not yet — the sealer's, after the rounds settle |

## Paste-ready fixes

### 🔴 1

`docs/review-chain-spec.md`, in the paragraph beginning *`nobody` with its
reason is refused nothing*, replace these three lines:

```markdown
ready pull request, and where a payload cannot answer. In a draft, or where no
pull request was seen, it prints: the pair stands there between `close` and
the verifying round's record, and *Ready for review* re-runs the check.
```

with:

```markdown
ready pull request, and where a payload cannot answer. It prints in a draft and
where no pull request was seen: the pair stands there between `close` and the
verifying round's record, and *Ready for review* re-runs the check.
```

### 🟡 2

`skills/code-review/scripts/chain_check.py`, the empty-`rounds/` notice in
`main`:

```python
                        f"declares `{routing.CHAIN}` and "
                        f"{item}/{routing.ROUNDS_DIR}/ holds no `round-N.md` "
                        "— which is the state a draft pull request opens in, "
                        "and the state of a run no pull request was observed "
                        "for: the rounds run against it, so the record cannot "
                        "exist yet. It is still owed, and pressing *Ready "
                        "for review* fires `ready_for_review`, re-runs this "
                        "check, and fails the pull request if it is still "
                        "missing",
```

The pair notice in `checked_by`:

```python
                    f"`Pass` is checked beside `{CHECKED_BY}: {cell.strip()}` "
                    "on the last record — the state a draft, or a run no pull "
                    "request was observed for, is in between `close` ticking "
                    "`Pass` and the verifying round's record committing. It "
                    "prints because neither is a request to merge. It is "
                    "still owed: spawn one verifying round at "
                    "the diff of these fixes, and this cell names it. "
                    "Pressing *Ready for review* fires `ready_for_review`, "
                    "re-runs this check, and fails the pull request if the "
                    f"cell still says `{NOBODY}`",
```

The open-note notice in `carried_notes`:

```python
                        f"{said}. It prints because a draft, or a pull request "
                        "nobody observed, is not a request to merge; pressing "
                        "*Ready for review* re-runs this check and fails the "
                        "pull request if it is still open",
```

The pin, in `tests/test_chain_check_at_the_pull_request.py`, inside
`test_a_pull_request_nobody_observed_is_unknown_not_ready`, after the `holds no`
assertion:

```python
    assert (
        "the state a draft pull request opens in, and the state of a run no "
        "pull request was observed for"
    ) in out, out
```

Needs a fix: yes — 🔴 1 the pasted phrase that fails three CI legs; 🟡 2 the three draft-worded notices printed for a run nobody observed
Loses a record or crashes: no

## Proof block

Files opened this round: `rounds/round-1.md`, `rounds/round-1-fixes.md`,
`rounds/round-1-report.md` (excerpts), `overview.md` (two rows),
`skills/code-review/scripts/chain_check.py` (`pull_request_state`,
`event_payload_present`, `pull_request_from_gh`, `verdict_of`,
`deferred_parts`, `checked_by`, `broad_gate`, `carried_notes`, `check_round`,
`main`), `skills/verify/scripts/broad_gate.py` (module docstring, chain arm,
`rounds_rows`), `skills/code-review/scripts/round_record.py#run_check`,
`tests/conftest.py`, `tests/test_chain_check_at_the_pull_request.py`,
`tests/test_the_record_is_generated.py`,
`tests/test_the_seal_is_taken_once_by_the_sealer.py`,
`tests/test_the_fixes_close_the_record.py`,
`tests/test_local_mode_reaches_the_review_chain.py`,
`tests/test_no_passage_is_pasted_into_a_second_file.py`,
`.github/workflows/hygiene.yml`, `templates/hygiene.yml`,
`docs/review-chain-spec.md`, `docs/round-record-spec.md`, and the fix range's
diff of `CONTRIBUTING.md`, `questions.md`, `survivors.md` and this item's
ledger fragment.
