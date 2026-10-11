# 1791384155-a-round-record-cell-has-one-reader — review round 1

| Field | Value |
|---|---|
| Target SHA | db5595c8787ed563dd63a67f777ff1cb9db5f868 |
| Written late | no |
| Ran by | specseal:warden on Opus 5.5 |
| PR | 890 |
| Broad gate | not yet |
| Fixes checked by | nobody — the fixes are written and no round has opened them |
| Fix range | `b10835ff3b06f2b0418fba4e38dfb4c7d6940347..092808fe7017db9f0fac8f3f0c3633e3aeafbaed`, 2 commits |
| Contract changes | none |
| New units | UNSEEN_SAYS (depth 1); event_payload_present (depth 1); DEFERRED_HEAD_RE (depth 1); test_a_pull_request_nobody_observed_is_unknown_not_ready (depth 1); test_a_run_that_cannot_see_a_pull_request_is_not_judged_as_a_ready_one (depth 1); generate_under (depth 1); test_with_no_pull_request_to_see_new_does_not_fail_the_record_it_wrote (depth 1) |
| Fix of a fix | no |
| Needs a fix | yes — 🟡 1 the generator's exit 1 outside a draft, unpinned and undocumented; 🟡 2 six ready helpers left on the draft stub; 🟡 3 the panel's input to `says_reopened`; 🟡 4 the note loses its marks |
| Loses a record or crashes | no |

- [x] Pass

## What this round was asked

Round 1 of the build at db5595c8, against origin/release/v0.21.0 at ad447367, which the branch merged before the build. Because the branch changes the readers of round records, the spawn asked the reviewer to judge every record in the tree under both the base's chain_check.py and this branch's. The spawn named the things to attack. First, the gh fallback: fail-open or fail-closed when gh hangs, is logged out or answers for another PR. Second, whether 'else ready' fails a legitimate local run. Third, the exit 1 after writing a record, and --sealing's scope. Fourth, every merged reader against its old callers over every record. Fifth, the gh stub in conftest, and whether any reader predicts a format nothing owns. It also ran the eight guard modules once. Facts arrived labelled. Read from the smith: the one reader per cell, the gh fallback, --sealing, the stub, 437 passed and the module results.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Where no draft is visible (no PR yet, `stop before the pull request`, a host `gh` cannot reach, a detached clone) `new` and `close` exit 1 on a correct mid-run record, and the check's text tells the orchestrator the rounds have settled; nothing documents or pins that exit at the generator | `skills/code-review/scripts/round_record.py:2735` | **fixed** `d2eed6d1` | fixed at d2eed6d1 — with no payload and no `gh` answer the check reads the state as unknown, does not judge it as a ready pull request, and names every source tried; a payload that cannot answer stays ready; a record `new`, `close` or `seal` writes mid-run is not failed for it; the sealer advice says *once the rounds have settled*; `docs/round-record-spec.md` §*`Pass` has to be checked* and `docs/review-chain-spec.md` say so, and the `stop before the pull request` reading is `questions.md` Q1 with the default unknown; executed: round 1 `new` exits 1 under *unknown* and 0 under the draft stub, printing the `Broad gate` arm's "The rounds have settled, so spawn the sealer"; no case runs the generator under *unknown*; orchestration.md names no such exit |
| 🟡 2 | The conftest `gh` stub answers draft for every case, hiding 🟡 1 and moving six modules whose `run()` means the ready local run to draft, two cases named for a ready pull request among them | `tests/conftest.py:560` | **fixed** `d2eed6d1` | fixed at d2eed6d1 — the suite's `gh` stub defaults to the unknown answer; the ten helpers that mean a ready pull request say ready through `gh_answers`, the two ready-named cases among them now run ready, and the generator is pinned under the unknown state; executed: under *unknown* the six modules pass and `tests/test_new_says_when_head_is_not_the_target.py` fails two cases on the generator's exit; four of ten such helpers were moved to `gh_answers` |
| 🟡 3 | The panel calls `says_reopened` on the raw `Needs a fix` cell while the gate calls it on `reader.visible(cell).strip()`, so an invisible-led cell is capped at the gate and not on the stamp | `skills/verify/scripts/broad_gate.py:2938` | **fixed** `d2eed6d1` | fixed at d2eed6d1 — `rounds_rows` hands `says_reopened` `reader.visible(needs).strip()`, the gate's string; U+200B and U+FEFF cells pinned; executed: U+200B, U+FEFF and U+FE0F cells read True at the gate, None on the panel, capped on the base's panel |
| 🟡 4 | `deferred_parts` strips `HOME_MARKS` from the note as well as the home, so the Grounds cell `close` writes loses code spans and edge underscores (`__init__.py` becomes `init.py`) | `skills/code-review/scripts/chain_check.py:1891` | **fixed** `d2eed6d1` | fixed at d2eed6d1 — `deferred_parts` cuts the note from the cell as written (`DEFERRED_HEAD_RE`) and takes `HOME_MARKS` off the home alone; the reviewer's two cells added to S2; executed on two cells; the third-cell path kept the text on the base; a version applying the marks to the home alone reads all of S2's cells as the case expects |
| ⬜ 5 | `gh pr view` answers for a closed or merged pull request, so a branch whose only pull request closed as a draft reads as draft; new only for a hand run of the check | `skills/code-review/scripts/chain_check.py:1325` | answered | a note, left as it stands: `gh pr view` picks the PR by branch name and answers a merged PR as not draft; only a hand-run `chain_check` meets it, and CI always reads the payload; executed with gh 2.92.0: a merged PR answered `state: MERGED`; the generator and the chain arm behaved this way before |
| ⬜ 6 | `--sealing` is honoured where a pull-request payload exists, the typed-override shape the `--draft` paragraph rejects, narrowed to one cell and printed | `skills/code-review/scripts/chain_check.py:4441` | answered | a note, left as it stands: `--sealing` excuses only the last record's `Broad gate` cell and prints that it did; CI never passes it; read; a refusal under a payload would also stop the suite's leak case (W2) |
| 🟢 | Every declaration and record in the tree judges byte-identically under the base's and this branch's check, with a draft and a ready payload | `skills/code-review/scripts/chain_check.py:5707` | confirmed | executed over 92 declarations and 38 records through a grafted empty root |
| 🟢 | `--sealing` excuses the `Broad gate` arm of the last record and the direct home and nothing else | `skills/code-review/scripts/chain_check.py:4448` | confirmed | read: `sealing_excuses` wraps `broad_gate` and `direct_seal` only; S9's second case keeps an unchecked `Pass` failing |
| 🟢 | The `gh` source fails closed on a hang, a logout, a non-JSON answer and a missing `gh` | `skills/code-review/scripts/chain_check.py:1330` | confirmed | read; the S7 cases pin each shape |
| ❓ | Whether a declared `Destination` of `stop before the pull request` should be read by the check as a state, so a run that will never have a pull request does not exit 1 on every round | `skills/code-review/scripts/chain_check.py:1255` | ❓ out of verified scope | a design choice against the policy table's ready default; the owner answers it, since #866's frame did not weigh that route |

## Paste-ready fixes

```python
# The state `main` judged in and where it read it, for an in-process caller
# that has to say what its exit means (`round_record.py#run_check`, #866).
JUDGED = None
```
```python
    global WORKTREE, JUDGED
```
```python
    state, where = pull_request_state(root)
    JUDGED = (state, where)
```
```python
    code = chain.main(["--worktree", "--baseline", baseline, "--root", root])
    state = (chain.JUDGED or (None, ""))[0]
    if code == 1 and state == "unknown":
        print(
            "round-record: the record is written, and the exit above is the "
            "check's verdict on a READY pull request. It could see none (no "
            "payload, and `gh` could not say) and judges that state as ready "
            "on purpose; a round still running stands in a draft. Where the "
            "draft is not open yet, open it and run the check again. Where "
            "this work item's routing stops before the pull request, the "
            "lines above that fail only a ready pull request (`Pass` "
            "unchecked, `Broad gate` not yet, `nobody` beside `Pass`, an open "
            "note) are the run's mid-review state, and the rounds have not "
            "settled because one of them says so"
        )
    return code
```
```markdown
**Outside a draft, `round_record.py` exits 1 on a record it wrote correctly
(#866).** The check reads the pull request's state from the event payload,
else from `gh pr view --json isDraft`, and judges a state it cannot see as
ready. Before the draft opens, on a host `gh` cannot reach, and on a work
item whose `Destination` stops before the pull request, `new` and `close`
exit 1 on every round still running, and the generator's last line says so.
That exit is the ready state's verdict on an unfinished review, not a broken
record, and the sealer is spawned when the rounds settle, never on it.
```
```python
def test_with_no_pull_request_to_see_new_exits_1_and_says_why(repo):
    """#866 J4 at the generator. No payload and a `gh` that finds no pull
    request is a READY pull request, so round 1's record -- `Pass` unchecked,
    `Broad gate` not yet -- is written and `new` exits 1, and the last line
    says the record stands and that the rounds have not settled. Under the
    suite's draft stub the same call exits 0."""
    declared(repo)
    scratch = repo.parent
    (scratch / "report-1.md").write_text(report(), encoding="utf-8")
    (scratch / "asked-1.md").write_text(ASKED, encoding="utf-8")
    command = [
        sys.executable,
        GENERATOR,
        "new",
        "--item",
        str(repo / ITEM),
        "--round",
        "1",
        "--target",
        git(repo, "rev-parse", "HEAD").stdout.strip(),
        "--report",
        str(scratch / "report-1.md"),
        "--asked",
        str(scratch / "asked-1.md"),
        "--ran-by",
        RAN_BY,
        "--baseline",
        "base",
    ]
    r = subprocess.run(
        command,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        timeout=120,
        env=gh_answers(env_without_a_pull_request(), "unknown"),
    )
    out = r.stdout + r.stderr
    assert (repo / ROUNDS / "round-1.md").exists(), out
    assert r.returncode == 1, out
    assert "judged as a ready pull request (no pull-request event payload" in out
    assert "the record is written, and the exit above is the check's" in out
    assert "the rounds have not settled" in out, out
```
```python
    # No payload is the local run, judged READY: the `gh` the check then asks
    # (#866) finds no pull request for the branch.
    env = gh_answers(dict(os.environ), "unknown")
```
```python
    reopened = (
        chain.says_reopened(reader.visible(needs).strip())
        if needs is not None
        else None
    )
```
```python
        # Invisible characters come off before the word is read, as the gate
        # reads the cell (`chain_check.record_facts`).
        ("​yes — 🟡 1, the wording", "3 · capped"),
```
```python
    chain, reader = check_module(), reader_module()
    reopened = chain.says_reopened(reader.visible(needs).strip())
```
```python
# The verdict word at the head of a deferral cell as written: any marker or
# emphasis before it and emphasis after it, so the note behind the home can
# be cut from the cell as written and keep its marks (round 1's 🟡 4).
DEFERRED_HEAD_RE = re.compile(r"^\W*?[*_`]*" + DEFERRED + r"[*_`]*", re.IGNORECASE)
```
```python
    if verdict_of([cell], 0) != DEFERRED:
        return None, ""
    cell = cell.strip()
    head = DEFERRED_HEAD_RE.match(cell)
    if head is None:
        return None, ""
    rest = cell[head.end() :].strip(SEPARATORS)
    home, _cut, note = rest.partition(HOME_END)
    # The marks are the home's to lose, never the note's: the note is the fix
    # pass's prose, and `close` writes it into the Grounds cell as given.
    home = HOME_MARKS.sub("", home).strip().rstrip(".").strip()
    return (home or None), (note.strip() if home else "")
```
```python
        # The note keeps its marks: `close` writes it into a Grounds cell.
        (
            "deferred #854 — the `_helper` in **x**.",
            "#854",
            "the `_helper` in **x**.",
            854,
        ),
        ("deferred #854 — see __init__.py", "#854", "see __init__.py", 854),
```

## Executed probes

| What was run | Result |
|---|---|
| `bin/test` on the eight guard modules, in the scratch clone at db5595c8 | 437 passed, exit 0 |
| the base's and this branch's `chain_check.py --baseline <empty root>` over the branch's tree, draft and ready payloads | byte-identical output both ways; exit 1 both, on squash-removed `Target SHA` commits |
| every merged reader, base copy against branch copy, over the 38 records | no difference except the release seal's one cell S3 changes |
| `round_record.py new` at round 1 with `gh` answering *unknown*, then *draft* | exit 1 with the ready-only errors quoted in 🟡 1; exit 0 |
| six stub-reached modules plus two generator modules re-run with `gh` answering *unknown* | 343 passed, 1 skipped, 2 failed (both `new` exit 0 assertions in `tests/test_new_says_when_head_is_not_the_target.py`) |
| `says_reopened` on three invisible-led cells, raw and through `visible` | None raw, True through `visible`; the base's panel read all three as capped |
| `deferred_parts` on two cells with marked notes | notes returned without their marks |
| the proposed `deferred_parts` against S2's sixteen cells plus two | eighteen of eighteen as expected |
| `gh pr view --json isDraft,number,headRefName,state` in a scratch repository, four branch shapes | own name with a draft PR: #890 draft; tracking another branch: unchanged; merged PR: #863 `MERGED`, not draft; detached: exit 1 |
| `uvx ruff check` on the ten files this diff touches | all checks passed |
| `gh pr checks 890` | every leg passes at db5595c8 (CI's run, read here) |
| the full suite, the repository-wide lint and the typecheck (the broad gate) | not yet — the sealer's, after the rounds settle |

## Inherited coordinates

| From | Coordinate | Why it is still worth opening |
|---|---|---|

## Deferred

| Finding | Where it went | Who answers it |
|---|---|---|

nothing to drain
