# Round 1 report — 1791384155, a round-record cell has one reader (#866)

Target SHA db5595c8787ed563dd63a67f777ff1cb9db5f868, the diff
`origin/release/v0.21.0...db5595c8`, reviewed in a `git clone --no-local` at
that commit. This is the first round, so nothing is inherited and every claim
in the handoff, `overview.md` and the spawn prompt was checked against the
code or run.

## How the findings relate

```
the pull request's state now has two observed sources (J4)
  ├─ 🟡 1  where neither can see a draft, `new` and `close` exit 1 on a
  │        correct mid-run record, and the check's text tells the
  │        orchestrator the rounds have settled
  ├─ 🟡 2  the suite's `gh` stub answers draft everywhere, which hides 🟡 1
  │        and silently moved six modules' "local run, judged ready" to draft
  ├─ ⬜ 5  `gh` answers for a closed or merged pull request on the branch
  └─ ⬜ 6  `--sealing` is a typed excuse that CI would honour
one reader per cell (J1, J2)
  ├─ 🟡 3  the panel feeds `says_reopened` a different string than the gate
  └─ 🟡 4  the home reader strips marks from the note, not only from the home
```

Everything else the work claims held where I measured it: no record in the
tree reads differently under the base's `chain_check.py` and this branch's
(details under *What held*).

## 🟡 1 — Outside a visible draft, the generator exits 1 on a correct record and says the rounds have settled

`run_check` (`skills/code-review/scripts/round_record.py:2735`) no longer
writes a draft payload, so the check reads the state itself
(`pull_request_state`, `skills/code-review/scripts/chain_check.py:5707`).
Where there is no payload and `gh pr view --json isDraft` cannot answer, the
state is `unknown` and is judged ready, as the policy table says.

Claimed (spec J4, failure direction): the population that now blocks more is
"a machine with no pull-request payload and no `gh` that can answer". The code
puts more in that population than the sentence does. `gh` also cannot answer:

- before the draft pull request opens, which is every round of a run that
  reviews before pushing;
- for every work item whose `Destination` reads `stop before the pull
  request`, a declared answer in `skills/implement/orchestration.md` (:304)
  where no pull request ever exists;
- on a code host `gh` does not reach, which is every plugin user not on
  GitHub, and on a clone whose HEAD is detached (measured below: `gh` exits 1
  with *could not determine current branch*).

Executed in a scratch fixture (`tests/test_the_record_is_generated.py`'s
`repo` and `report()`, round 1, `Needs a fix: yes`): with `gh` answering as a
branch with no pull request, `new` wrote the record and exited **1**; with the
suite's draft answer it exited 0. The two errors it printed are the
ready-only arms, and one of them is false advice at round 1:

```
chain-check: judged as a ready pull request (no pull-request event payload, and `gh pr view` exited 1: no pull requests found for branch "x")
…  the last round's `Pass` is not checked. … Open it as a draft while the rounds run
…  `Broad gate` is `not yet` on the last round record, and this is a ready pull request. … The rounds have settled, so spawn the `sealer` …
```

Why it matters. The generator documents its exit as the check's verdict
(`round_record.py` module docstring, *Exit codes*), and an orchestrator under
`automation` reads exit codes directly. Nothing tells it that this exit 1 is
not a broken record: `skills/code-review/orchestration.md` §*The pull request
opens before round 1* names no such case. The orchestrator is then holding a
non-zero exit beside a sentence that says to spawn the sealer, on round 1. The
same document's own reason for #296 applies: a check that is red for following
the document beside it is a check people learn to skip.

No case pins this at the generator (§14). The new S7 cases run
`chain_check.py`, and every generator case runs under the suite's draft stub
(🟡 2), so the line a person meets after `new` is unpinned.

Whether the `stop before the pull request` route should be read as a state at
all is a design question, not this fix; it is the ❓ row below. The fix that
needs no decision is to make the exit say what it is and pin it.

## 🟡 2 — The suite's `gh` stub answers draft for every case, which hides 🟡 1 and moved six modules from ready to draft

`tests/conftest.py:560` puts a `gh` first on PATH that answers `isDraft:
true` for every case. `overview.md` records why: 176 cases failed once the
generator stopped writing its payload. The stub restores the old default
instead of the cases saying which state they are about.

Two consequences, both executed:

- **It hides 🟡 1.** Re-running `tests/test_new_says_when_head_is_not_the_target.py`
  with `gh` answering *unknown*, two cases fail
  (`test_nothing_is_refused_and_the_line_says_so` and its neighbour): each
  asserts `new` exits 0, which is true only because the stub says draft.
- **It silently changed what six modules test.** Their `run()` helpers pop
  `GITHUB_EVENT_PATH` to mean the local run, which was judged **ready** before
  this branch. Under the stub each is now a draft. The branch moved four
  helpers to `gh_answers(…, "unknown")` and left these six:
  `tests/test_the_reopening_is_one.py:215`,
  `tests/test_the_record_is_held_to_the_floor_and_the_depth.py:189`,
  `tests/test_a_record_says_what_ran_it.py:175`,
  `tests/test_a_record_precedes_the_fixes_it_commissions.py:215`,
  `tests/test_the_chain_goes_back_to_its_framer.py:170`,
  `tests/test_the_fixes_name_their_surface.py:174`. That is about 130 calls.
  Two cases are named for the state they no longer run in:
  `test_a_ready_pull_request_passes_a_blocking_finding_deferred_to_an_issue`
  and `test_a_ready_pull_request_refuses_a_blocking_finding_deferred_nowhere`.

Re-run with `gh` answering *unknown*, all six modules pass (the 343 passed in
the probe table includes them), so moving their helpers back to ready costs no
red today. What it buys back is coverage of the ready arms (`Pass`,
`nobody` beside `Pass`, open notes, `Broad gate`) that a draft excuses. Left
as is, a regression in any of those arms on a correct settled record passes
these cases silently. This is §12's class: the helpers that meant "ready" are
one class, and four of ten were moved.

## 🟡 3 — The panel reads `Needs a fix` through the gate's reader, but not from the gate's string

`rounds_rows` calls `chain.says_reopened(needs)` on the raw cell
(`skills/verify/scripts/broad_gate.py:2938`). The gate and the generator's
bound call it on `reader.visible(cell).strip()` (`record_facts`). The panel
before this branch also called `visible` first. So the work moved the panel
onto the one reader and dropped the normalisation that made it read the same
string.

Executed: a cell beginning with a zero-width space, U+FEFF, or `yes` followed
by U+FE0F reads True at the gate and None on the panel. The base's panel read
all three as capped. The record then prints `<R>` alone on the stamp while the
gate counted a reopening, which is J1's two-readers-of-one-cell shape again.
`docs/round-record-spec.md`'s new opening sentence ("the check is the one
reader of every cell") is not true for this cell until the input is the same.

The S1 case enshrines it: `test_the_panels_capped_is_the_gates_reopening`
compares the panel with `says_reopened(needs)` on the raw cell, not with the
gate's reading.

## 🟡 4 — The home reader strips marks from the fix pass's note, so `__init__.py` is written as `init.py`

`deferred_parts` (`skills/code-review/scripts/chain_check.py:1891`) runs
`HOME_MARKS` over the whole cell before it cuts the home from the note. The
marks therefore come off the note too: backticks, asterisks, and an
underscore at a word's edge. `fix_table` writes that note into the record's
Grounds cell. Executed:

| Cell | Home | Note returned |
|---|---|---|
| `deferred #854 — see __init__.py` | `#854` | `see init.py` |
| the same home, with a note naming a private helper in a code span and a word in asterisks | `#854` | the helper's leading underscore, the backticks and the asterisks all gone |

The verdict-cell path was worse on the base (it ran `EMPHASIS` over the whole
cell), so that path improved. The third-cell path regressed: on the base a
bare `deferred` beside `#854 — see __init__.py` kept the text as written,
and now the Grounds cell names a file and a helper that do not exist. #391
part 1 is the reason the note is kept at all, because it is "the whole of"
a deferral's value.

The marks belong to the home, which a panel prints, and not to the note,
which is the fix pass's prose. The fix applies `HOME_MARKS` after the cut and
to the home alone. Executed against S2's sixteen cells plus the two above:
all eighteen read as the case expects.

## ⬜ 5 — `gh pr view` answers for a closed or merged pull request on the branch

Measured with the installed `gh` (2.92.0), read-only, in a scratch repository
whose remote is this project's: a branch named after one with a draft pull
request answers #890's `isDraft: true`, and the tracking config
(`branch.<name>.merge` pointing elsewhere) changes nothing. A branch named
`release/v0.20.0` answers pull request #863 with `state: MERGED` and
`isDraft: false`.

So a branch whose only pull request was closed while a draft reads as a draft
and excuses the ready arms. For the generator and the broad gate's chain arm
this equals what the base did (the same call, or a forced draft), so it is
not a regression there. It is a new fail-open only for `chain_check.py` run
by hand outside a workflow, which the base judged ready. Asking for
`isDraft,state` and treating anything but `OPEN` as `unknown` closes it; the
conftest stub's answers would need a `state` too. Recorded rather than
commissioned: the local run gates nothing.

## ⬜ 6 — `--sealing` is a typed excuse that a workflow could pass

`pull_request_state`'s docstring rejects a `--draft` flag because "an
override anyone can type is the same hole with a name". `--sealing` is that
for one arm: CI's `hygiene.yml` and `templates/hygiene.yml` do not pass it,
and the help text says CI never does, but nothing refuses it where a
pull-request payload exists. Its scope is right (read and executed below), and
the state line names it, so it cannot pass in silence. A refusal under a
payload would also stop the suite's broad-gate cases on a runner that leaks
`GITHUB_EVENT_PATH` (W2), so this is a note, not a fix.

## What held

- **Every record in the tree reads the same under both checks** (executed). A
  grafted empty root made all 92 declarations "changed", and the base's and
  this branch's `chain_check.py` were run over the branch's tree with a draft
  and a ready payload. The outputs are byte-identical (182 and 198 lines).
  Both exit 1, on `Target SHA` commits a squash removed, which is the same
  state before and after. The tree holds 38 records now, not the 22 the
  frame measured.
- **Each merged reader agrees with the copy it replaced over those 38
  records** (executed): 38 `Needs a fix` cells (28 `yes — …`, 10 `no`), 26
  `deferred` cells, 100 `fixed` rows, every Grounds cell, every field label
  and box. The one difference is the release seal's count for
  `deferred #854 — … as #825's round 6`, which now counts 854 alone, the
  change S3 names. No `fixed` row's `Location` carries a backticked or bare
  name, so the depth walk's narrowing (J3) moves no record.
- **The walks, the run cut and the premature test are the same function
  both callers had** (read). `floor_walks` reproduces both loops index for
  index; `stopping_floor` feeds it a met record at index 0 and maps `fixers`
  back through `later`; `cut_runs` keeps the `count == 2 and landed` rule;
  `gate_before_review` gives `seal` the same first-premature answer it gave.
- **`--sealing` excuses one cell** (read, and executed by the branch's own S9
  cases at the PR). `sealing_excuses` wraps only the `broad_gate` arm of the
  last record and `direct_seal`, whose errors are all about the `Broad gate`
  cell or its missing `broad-gate.md`. An unchecked `Pass`, `nobody` beside
  `Pass`, open notes and an empty `rounds/` are not touched by it.
- **The `gh` fallback fails closed on a hang, a logout, a non-JSON answer and
  a missing `gh`** (read; the S7 cases pin it). A timeout raises
  `SubprocessError`, every non-zero exit and every non-boolean `isDraft` is
  `unknown`, and `unknown` is ready. `gh` inherits stdin, but its prompts need
  a terminal on stdout and the call captures it.
- **No reader predicts a format nothing owns** (read, against the owner's
  review). The home's grammar is `close`'s join, the close prefixes are
  `close`'s `; ` join, the fields and boxes are `new`'s, and the state is
  `gh`'s own answer. `HOME_MARKS` is the one reader of marks a person types;
  🟡 4 is where it reaches too far.

## Regression tests to plant

- `tests/test_the_record_is_generated.py`: the generator under *unknown*
  exits 1, writes the record and prints the trailer (🟡 1's last fence).
- `tests/test_the_seal_is_taken_once_by_the_sealer.py`: a zero-width-space
  `Needs a fix` reads capped on the panel, with the case comparing against the
  gate's reading (🟡 3's fence).
- `tests/test_chain_check_at_the_pull_request.py`: two rows in S2's table
  whose note keeps its code span and its edge underscores (🟡 4's fence).
- The six modules in 🟡 2: no new case; their `run()` helpers move to
  `gh_answers(…, "unknown")`, which the probe ran green.

## Facts for the evidence ledger

- The tree's 38 round records read identically under the base's and this
  branch's `chain_check.py` with a draft and a ready payload (executed, at
  db5595c8).
- `gh pr view --json isDraft` (2.92.0) selects the pull request by the
  current branch's own name, ignores `branch.<name>.merge`, answers a merged
  pull request with its state, and exits 1 on a detached HEAD (executed,
  2026-10-12).
- CI at db5595c8 is green on every leg, Windows' four shards included (read
  from `gh pr checks 890`; CI's run, not mine). That is the only evidence
  here for the `gh.cmd` stub and the found-path call on Windows.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟡 1 | Where no draft is visible (no PR yet, `stop before the pull request`, a host `gh` cannot reach, a detached clone) `new` and `close` exit 1 on a correct mid-run record, and the check's text tells the orchestrator the rounds have settled; nothing documents or pins that exit at the generator | `skills/code-review/scripts/round_record.py:2735` | open | executed: round 1 `new` exits 1 under *unknown* and 0 under the draft stub, printing the `Broad gate` arm's "The rounds have settled, so spawn the sealer"; no case runs the generator under *unknown*; orchestration.md names no such exit |
| 🟡 2 | The conftest `gh` stub answers draft for every case, hiding 🟡 1 and moving six modules whose `run()` means the ready local run to draft, two cases named for a ready pull request among them | `tests/conftest.py:560` | open | executed: under *unknown* the six modules pass and `tests/test_new_says_when_head_is_not_the_target.py` fails two cases on the generator's exit; four of ten such helpers were moved to `gh_answers` |
| 🟡 3 | The panel calls `says_reopened` on the raw `Needs a fix` cell while the gate calls it on `reader.visible(cell).strip()`, so an invisible-led cell is capped at the gate and not on the stamp | `skills/verify/scripts/broad_gate.py:2938` | open | executed: U+200B, U+FEFF and U+FE0F cells read True at the gate, None on the panel, capped on the base's panel |
| 🟡 4 | `deferred_parts` strips `HOME_MARKS` from the note as well as the home, so the Grounds cell `close` writes loses code spans and edge underscores (`__init__.py` becomes `init.py`) | `skills/code-review/scripts/chain_check.py:1891` | open | executed on two cells; the third-cell path kept the text on the base; a version applying the marks to the home alone reads all of S2's cells as the case expects |
| ⬜ 5 | `gh pr view` answers for a closed or merged pull request, so a branch whose only pull request closed as a draft reads as draft; new only for a hand run of the check | `skills/code-review/scripts/chain_check.py:1325` | open | executed with gh 2.92.0: a merged PR answered `state: MERGED`; the generator and the chain arm behaved this way before |
| ⬜ 6 | `--sealing` is honoured where a pull-request payload exists, the typed-override shape the `--draft` paragraph rejects, narrowed to one cell and printed | `skills/code-review/scripts/chain_check.py:4441` | open | read; a refusal under a payload would also stop the suite's leak case (W2) |
| 🟢 | Every declaration and record in the tree judges byte-identically under the base's and this branch's check, with a draft and a ready payload | `skills/code-review/scripts/chain_check.py:5707` | confirmed | executed over 92 declarations and 38 records through a grafted empty root |
| 🟢 | `--sealing` excuses the `Broad gate` arm of the last record and the direct home and nothing else | `skills/code-review/scripts/chain_check.py:4448` | confirmed | read: `sealing_excuses` wraps `broad_gate` and `direct_seal` only; S9's second case keeps an unchecked `Pass` failing |
| 🟢 | The `gh` source fails closed on a hang, a logout, a non-JSON answer and a missing `gh` | `skills/code-review/scripts/chain_check.py:1330` | confirmed | read; the S7 cases pin each shape |
| ❓ | Whether a declared `Destination` of `stop before the pull request` should be read by the check as a state, so a run that will never have a pull request does not exit 1 on every round | `skills/code-review/scripts/chain_check.py:1255` | ❓ out of verified scope | a design choice against the policy table's ready default; the owner answers it, since #866's frame did not weigh that route |

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

## Paste-ready fixes

### 🟡 1

`skills/code-review/scripts/chain_check.py`, beside `WORKTREE = False` (:931):

```python
# The state `main` judged in and where it read it, for an in-process caller
# that has to say what its exit means (`round_record.py#run_check`, #866).
JUDGED = None
```

In `main`, widen the `global` line (:5654) and record the state after
`pull_request_state(root)` (:5707):

```python
    global WORKTREE, JUDGED
```

```python
    state, where = pull_request_state(root)
    JUDGED = (state, where)
```

`skills/code-review/scripts/round_record.py#run_check`, replacing the return
(:2749):

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

`skills/code-review/orchestration.md`, after the paragraph on the `close` to
verifying-round window (#598):

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

`tests/test_the_record_is_generated.py`, beside
`test_the_exit_code_is_chain_checks_and_the_record_stays`:

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

### 🟡 2

In each of `tests/test_the_reopening_is_one.py:216`,
`tests/test_the_record_is_held_to_the_floor_and_the_depth.py:190`,
`tests/test_a_record_says_what_ran_it.py:176`,
`tests/test_a_record_precedes_the_fixes_it_commissions.py:216`,
`tests/test_the_chain_goes_back_to_its_framer.py:171` and
`tests/test_the_fixes_name_their_surface.py:175`, add `gh_answers` to the
module's `from conftest import …` line (or add the line where the module has
none) and replace the first line of `run()`:

```python
    # No payload is the local run, judged READY: the `gh` the check then asks
    # (#866) finds no pull request for the branch.
    env = gh_answers(dict(os.environ), "unknown")
```

### 🟡 3

`skills/verify/scripts/broad_gate.py#rounds_rows` (:2938):

```python
    reopened = (
        chain.says_reopened(reader.visible(needs).strip())
        if needs is not None
        else None
    )
```

`tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_panels_capped_is_the_gates_reopening`:
a row in its parameters, and the case compared with the gate's reading:

```python
        # Invisible characters come off before the word is read, as the gate
        # reads the cell (`chain_check.record_facts`).
        ("​yes — 🟡 1, the wording", "3 · capped"),
```

```python
    chain, reader = check_module(), reader_module()
    reopened = chain.says_reopened(reader.visible(needs).strip())
```

### 🟡 4

`skills/code-review/scripts/chain_check.py`, the word's head pattern above
`deferred_parts`, and the function's body after its docstring:

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

`tests/test_chain_check_at_the_pull_request.py#test_a_deferrals_home_is_what_stands_after_the_word`,
two rows in its table:

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

## The answer

Needs a fix: yes — 🟡 1 the generator's exit 1 outside a draft, unpinned and undocumented; 🟡 2 six ready helpers left on the draft stub; 🟡 3 the panel's input to `says_reopened`; 🟡 4 the note loses its marks
Loses a record or crashes: no


## Proof

- Opened: `seal/specs/1791384155-a-round-record-cell-has-one-reader/`
  `spec.md`, `overview.md`, `questions.md`, `handoff.md`; the diff of
  `skills/code-review/scripts/chain_check.py`,
  `skills/code-review/scripts/round_record.py`,
  `skills/verify/scripts/broad_gate.py`, `.github/scripts/release_seal.py`,
  `skills/evidence-check/scripts/evidence_check.py`, `tests/conftest.py`,
  `tests/test_chain_check_at_the_pull_request.py`,
  `tests/test_the_record_is_generated.py`, and of `docs/round-record-spec.md`,
  `docs/review-chain-spec.md`, `agents/sealer.md`, `CONTRIBUTING.md`;
  `skills/code-review/orchestration.md` (:598–660);
  `skills/verify/scripts/unverified_check.py` (`readable`, `visible`);
  the `run()` helpers of the six modules in 🟡 2 and the S1 case in
  `tests/test_the_seal_is_taken_once_by_the_sealer.py`.
- Executed: the probes in the table above, in scratch clones of the target
  and of `origin/release/v0.21.0` (ad447367), and one scratch repository for
  `gh`. Every probe file, clone and scratch repository was removed after.
- Not opened: `plan.md`, `survivors.md`, the phase files and the changelog
  fragment; the `Re-read ·` rows of the ledger fragment.
- Unverified: the full suite, lint and typecheck (the sealer's); the Windows
  `gh.cmd` path, read only, and green on CI's Windows shards, which CI ran.
