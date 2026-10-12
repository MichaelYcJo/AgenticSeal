# 1791384155-a-round-record-cell-has-one-reader — review round 3 report

Verifying round over round 2's fixes, `ff88f31d..07449c19` (6b9f311e,
3f08be56, 07449c19), plus the table and close commits, at target
ec02e1562543d8dcd2f10a84ea7873af204617fd. Draft pull request #890 into
`release/v0.21.0`. The review ran in a `git clone --no-local` of the worktree
at the target, under the session scratchpad. This round ends the run.

## The short answer

Both fixes hold. Nothing this round found needs a fix, and nothing loses a
record or crashes. Two notes remain, and both are about wording that is
incomplete rather than wrong:

```
round 2's fix pass
  ├─ 🔴 1  the docs pair is back at 31 shared runs, the module passes        (closed)
  ├─ 🟡 2  three notices read true for a draft and for an unseen run        (closed)
  │          └─ docs and docstrings around them still name the draft alone  (⬜ 1)
  │          └─ one notice's new wording is asserted in the unseen run only (⬜ 2)
  └─ ⬜ 3–5 answers                                                          (hold)
```

## 🔴 1 — The pasted sentence is gone, and the ratchet is back at its baseline

The fix rewords the `docs/review-chain-spec.md` sentence so it no longer
repeats the `nobody — <why>` row at `docs/round-record-spec.md:65`. The new
wording is *It prints in a draft and where no pull request was seen*, the
second of the two forms round 2's report offered.

- **Executed:** a probe imported `shared_counts` from
  `tests/test_no_passage_is_pasted_into_a_second_file.py` and counted the pair
  at five revisions: 31 at b10835ff, 33 at ff88f31d, and 31 at 6b9f311e,
  07449c19 and ec02e156. `over_baseline` over the whole tree at the target
  returns nothing.
- **Executed:** `docs/review-chain-spec.md` is 999 lines at every one of those
  revisions, so the 1,000-line bound holds.
- **Executed:** `bin/test` on that module and the three other modules the
  fix range touched gives 301 passed, exit 0.
- **Read:** `gh pr checks 890` shows head ec02e156 with every pytest leg
  still pending, so CI's own answer at the target is not in yet. The three
  legs that failed were failing at 03779b65.

## 🟡 2 — The three notices now say what prints for a draft and for an unseen run

Each notice used to give *a draft* as the reason it prints. Each now names
*a pull request not marked ready, or none seen*:

| Notice | Where | Pinned in a draft | Pinned in an unseen run |
|---|---|---|---|
| empty `rounds/` | `chain_check.py:5955` | prints (`test_a_draft_pull_request_has_not_had_its_rounds_yet`); wording not asserted | wording asserted (`test_a_pull_request_nobody_observed_is_unknown_not_ready`) |
| `Pass` beside `nobody` | `chain_check.py:2715` | wording asserted | wording asserted (same loop) |
| open note | `chain_check.py:5096` | wording asserted (`[draft]`) | wording asserted (`[none seen]`) |

- **Executed:** with `chain_check.py` restored from ff88f31d, the new pins
  give 4 failed and 1 passed. The failures are the open-note case's `[draft]`
  and `[none seen]`, the unseen-run case and the `Pass`-beside-`nobody` loop.
  The one that passed is `[ready]`, which asserts no notice wording. With the
  file restored to the target, all four modules pass.
- **Read:** `chain_check.py` branches on `strict` at six places. Only three
  of them print anything when `strict` is false, and they are the three
  above. `broad_gate`, `direct_seal` and the unchecked-`Pass` arm of
  `check_round` return nothing when not strict. The state line in `main`
  says *draft* only when `state == "draft"`, and prints `UNSEEN_SAYS` for an
  unseen run.
- **Read:** `skills/verify/scripts/broad_gate.py` holds no sentence with the
  word *draft* at all. In `round_record.py` the word appears only in the
  `run_check` docstring, which describes the old behaviour as old.

So there is no fourth printed sentence that names a draft where the state is
unknown. Two smaller things sit beside the fix, and both are notes.

## ⬜ 1 — The docs and docstrings around the notices still name the draft alone

Since round 1's fix, an unseen run excuses the same three arms a draft does.
Several sentences that describe those arms still give only the draft:

- `chain_check.py:5033` is the `carried_notes` docstring, whose table says
  *an error at a ready pull request and a notice on a draft*. Round 2's fix
  changed this function's notice and left the table.
- `skills/code-review/orchestration.md:238` says the same of an open note.
- `docs/review-chain-spec.md` §*What a draft is excused, and what it is not*
  says the record-count arm prints in a draft and does not mention the unseen
  state.
- `chain_check.py:5455` (`direct_seal`) and `chain_check.py:166` say the
  same of their arms.

None of these is false: a draft does get a notice. What is missing is the
second state, so a reader of the docs alone would expect an unseen run to
fail. `docs/review-chain-spec.md` is at 999 lines, so a sentence added there
has to replace one. This is a note and not a 🟡, because the behaviour and
every printed line are right.

## ⬜ 2 — The empty-`rounds/` wording is asserted in the unseen run only

Round 2's fix table says each notice is *pinned in a draft and in an unseen
run*. For the empty-`rounds/` notice that is true of the notice printing, not
of its wording. `test_a_draft_pull_request_has_not_had_its_rounds_yet` checks
that the notice prints and names `ready_for_review`. Only
`test_a_pull_request_nobody_observed_is_unknown_not_ready` asserts the new
words.

Nothing escapes because of it. Both states print the same string literal, so
a revert of the wording fails the unseen case, and the executed revert above
showed that. The claim in the record is one step stronger than the case.

## ⬜ 3–5 — Round 2's answers hold

- **⬜ 3** (`UNSEEN_SAYS` says CI judges it, and on some routes nothing does).
  `questions.md` Q1 exists and puts the no-pull-request route to the owner,
  with the default the check already follows. `templates/hygiene.yml` lines
  12-22 say local mode installs no workflow. The answer holds. The same Q1
  also covers the second half of the three notices above: *pressing Ready
  for review … re-runs this check* has no button to press on a route that
  never opens a pull request.
- **⬜ 4** (`event_payload_present` beside `pull_request_state`). Both read
  `GITHUB_EVENT_PATH` and test it the same way (`bool(path)` and
  `os.path.exists`). They cannot disagree on one environment, and the round 2
  reviewer ran four shapes to show it. The answer holds.
- **⬜ 5** (a note keeps a closing mark its home opened). Round 2 executed
  that no cell in the tree has the shape. The answer holds.

## The fix range as a finding surface

Round 2's fixes changed three string literals, three test helpers and their
assertions, ledger anchors, and one `survivors.md` row. None of them changes
how the state is read.

- **Read:** `run(repo, draft=None, gh="ready")` and `run_main` keep `ready`
  as the default, and `gh="unknown"` and `draft=None` are new opt-ins. No
  existing case moved from ready to unknown or back.
- **Executed:** `bin/evidence-check --strict` on this work item's ledger
  fragment gives 194 ok, 0 drifted, exit 0. On the 1791384154 and 1791384160
  fragments it exits 2 on 1 and 3 drifted rows. Those rows anchor
  `agents/warden.md`, `tests/test_every_reader_ends_a_line_where_gfm_does.py`
  and `skills/verify/scripts/payload_meter.py`, and this branch touches none
  of them (`git diff origin/release/v0.21.0...ec02e156` over the three paths
  is empty). That is release-branch drift, which #836 clears, and not this
  branch's finding.
- **Executed:** `bin/survivor-check` over the fix range exits 1 without
  `--exempt` and names one place, `seal/releases/0.9.5.md:31`. With this work
  item's `survivors.md` it exits 0. The exemption's grounds hold:
  `Corrected · G1` stands in this item's fragment, and
  `bin/evidence-check --strict` on `seal/releases/0.9.5.md` reads 66 ok, 0
  broken.
- **Read:** the check prints a notice that this item's `changelog.md` last
  changed before 6b9f311e and 3f08be56. The fragment still says what ships:
  round 2's fixes reword three notices and one doc sentence, and the fragment
  quotes none of them.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's blocking finding 1 is closed — the review-chain-spec sentence no longer repeats the round-record-spec row | `docs/review-chain-spec.md:655` | confirmed | executed: the module's own `shared_counts` gives 31 at 6b9f311e, 07449c19 and ec02e156 (33 at ff88f31d); `over_baseline` over the tree is empty; the file is 999 lines; `bin/test` on the module and the three other touched modules gives 301 passed, exit 0. read: CI at ec02e156 still pending |
| 🟢 | round 2's finding 2 is closed — the three notices read true for a draft and for an unseen run | `skills/code-review/scripts/chain_check.py:5955` | confirmed | executed: with `chain_check.py` from ff88f31d the new pins give 4 failed, 1 passed (the `[ready]` case, which asserts no notice). read: only three of the six places that branch on `strict` print when not strict, and `broad_gate.py` holds no draft sentence |
| 🟢 | round 2's note 3 stands as answered — the unseen line's CI clause is Q1's | `skills/code-review/scripts/chain_check.py:1335` | confirmed | read: `questions.md` Q1 and `templates/hygiene.yml` lines 12-22; the same Q1 covers the re-arm half of the three notices on a route with no pull request |
| 🟢 | round 2's note 4 stands as answered — the payload test is one reading | `skills/code-review/scripts/chain_check.py:1341` | confirmed | read: `event_payload_present` and `pull_request_state` test `GITHUB_EVENT_PATH` the same way |
| 🟢 | round 2's note 5 stands as answered — no cell has the shape | `skills/code-review/scripts/chain_check.py:1947` | confirmed | read: round 2 executed it over every cell in the tree; nothing in the fix range writes a deferral cell |
| ⬜ 1 | The docs and docstrings describing the three non-strict arms still name the draft alone, though an unseen run is excused the same way | `skills/code-review/scripts/chain_check.py:5033` | open | read: also `skills/code-review/orchestration.md:238`, `docs/review-chain-spec.md` §*What a draft is excused, and what it is not*, `chain_check.py:5455` and `chain_check.py:166`; none is false, each omits the unseen state; `docs/review-chain-spec.md` is at 999 lines |
| ⬜ 2 | Round 2's fix table says each notice is pinned in both states, and the empty-`rounds/` wording is asserted in the unseen run only | `tests/test_chain_check_at_the_pull_request.py:246` | open | read: the draft case asserts the notice prints and names `ready_for_review`; executed: one shared literal, so the wording revert fails the unseen case |

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on `tests/test_no_passage_is_pasted_into_a_second_file.py`, `tests/test_a_note_closes_once_at_the_runs_end.py`, `tests/test_chain_check_at_the_pull_request.py` and `tests/test_the_last_rounds_fixes_are_checked.py`, in the scratch clone at ec02e156 | 301 passed, exit 0 |
| a probe calling the module's `shared_counts` on the docs pair at b10835ff, ff88f31d, 6b9f311e, 07449c19 and ec02e156, and `over_baseline` on the tree | 31, 33, 31, 31, 31; 999 lines each; `over_baseline` empty |
| `chain_check.py` restored from ff88f31d, then the open-note, unseen-run and `Pass`-beside-`nobody` cases | 4 failed, 1 passed (`[ready]`); restored to the target afterwards |
| `bin/evidence-check --strict --ledger` on this item's fragment, the 1791384154 and 1791384160 fragments, and `seal/releases/0.9.5.md` | 194 ok exit 0; 1 drifted exit 2; 3 drifted exit 2, all on paths this branch does not touch; 66 ok exit 0 |
| `bin/survivor-check --range ff88f31d..07449c19`, with and without this item's `survivors.md` | exit 0 with it (one exempt place); exit 1 without it, naming `seal/releases/0.9.5.md:31` |
| `gh pr checks 890` | read: every pytest leg pending at ec02e156 (CI's run, not this round's) |
| the full suite, the repository-wide lint and the typecheck (the broad gate) | not yet — the sealer's, after the rounds settle |

## Regression tests to plant

None owed. For ⬜ 2, if the smith chooses to close it, the destination is
`tests/test_chain_check_at_the_pull_request.py`, in
`test_a_draft_pull_request_has_not_had_its_rounds_yet`: assert the same
*which is the state a pull request not marked ready, or none seen, opens in*
phrase the unseen case asserts.

## Facts for the evidence ledger

- The docs pair `docs/review-chain-spec.md` and `docs/round-record-spec.md`
  shares 31 runs at ec02e156, its `BASELINE` value (executed).
- The three notices the check prints when not strict are the only printed
  sentences in `chain_check.py` that run while `strict` is false (read).

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

## What is due next

This round leaves nothing open that needs a fix, so the broad gate has come
due. The next step is the sealer's spawn, against base
`origin/release/v0.21.0`.

Needs a fix: no
Loses a record or crashes: no

## Proof block

Files opened this round: `seal/specs/1791384155-a-round-record-cell-has-one-reader/rounds/round-2.md`,
`seal/specs/1791384155-a-round-record-cell-has-one-reader/rounds/round-2-fixes.md`,
`seal/specs/1791384155-a-round-record-cell-has-one-reader/rounds/round-2-report.md` (head),
`seal/specs/1791384155-a-round-record-cell-has-one-reader/questions.md` (Q1),
`seal/specs/1791384155-a-round-record-cell-has-one-reader/survivors.md` (diff),
`skills/code-review/scripts/chain_check.py` (1250-1400, 2590-2740, 4570-4625,
5025-5105, 5265-5300, 5450-5475, 5540-5650, 5725-5770, 5915-6000),
`skills/code-review/scripts/round_record.py` (2725-2790),
`skills/verify/scripts/broad_gate.py` (searched),
`skills/code-review/orchestration.md` (230-242),
`docs/review-chain-spec.md` (905-960 and the fix hunk),
`docs/round-record-spec.md:65`, `templates/hygiene.yml` (12-22),
`tests/test_chain_check_at_the_pull_request.py` (205-320),
`tests/test_a_note_closes_once_at_the_runs_end.py` (238-293),
`tests/test_the_last_rounds_fixes_are_checked.py` (165-190, and 820-840 through the fix diff),
`tests/test_no_passage_is_pasted_into_a_second_file.py` (searched),
`tests/conftest.py` (548-560), and the ledger fragments' fix-range diff.
