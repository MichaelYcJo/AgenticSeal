# Round 3 — the last round, over round 2's fix pass

Target: HEAD 400a54df of `chore/930-nothing-holds-the-repositorys-size-and-speed`.
The fix range is `f594450d..4ddf0edb`, two commits. The review used a
`git clone --no-local` at the round's scratch directory, and nothing was
written in the implementer's worktree except this file.

## In short

- Both of round 2's findings are closed.
- The two cases round 2 asked for are planted. They pass now, and they fail
  against the `section` they replaced.
- The fix created no new problem.
- Nothing in this round needs a fix, so the run can end here.

## Round 2's findings, each against its fix

**🟡 1 (`section` read headings off fenced and commented lines).** Fixed by
bb6cd81c. `section` now takes each heading's level from
`unverified_check.py#readable`, which blanks the lines a renderer does not
show. It slices the section's text from the raw lines, at the same indexes,
and refuses a title that stands twice. The new code matches the paste-ready
fix of round 2.

The two cases asked for are planted in `tests/test_a_budget_ratchets.py`.
The fence case is parametrised over a fenced line and a commented line, so
there are three cases in all. Executed:

- At 400a54df, all three pass.
- With `budget_check.py` checked out from f594450d, which holds the old
  `section`, all three fail.

So each case catches the defect it was written for.

**⬜ 2 (the per-file spread did not reproduce).** Corrected by 4ddf0edb. The
docstring, `spec.md` and `overview.md` now name the set the figure is
measured over: 0.76 to 1.14 over the 19 files of 100 s or more, and 0.46 to
1.54 over the 72 files of 10 s or more. These are the figures round 2
measured. No `1.16` is left in the code, `seal/budgets.md`, `docs/`,
`CONTRIBUTING.md` or this work item's records.

## Checked for anything the fix created

- **No reopening.** A section's heading is read off `readable`, so the heading
  always stands outside a fence or a comment. The raw slice that
  `gfm_table` is then handed therefore cannot begin inside one. A fence or
  comment opened inside the section is handled by `readable` for the
  section's end and by the walker's own `unfenced` for the table, and the
  two agree.
- **The tree at 400a54df.** Executed: `budget_check.py` over the tree exits 0,
  "every gate row holds".
- **Census modules the orchestrator's set did not include.** Executed: one
  format one reader, encoding, no real identifiers and one word one meaning.
  182 passed, exit 0.

## Left for after the run

Nothing needs a fix. One property recorded in round 2 stays as it was.
A mass rewrite of `.test_durations` together with a restated price level
moves every seconds reading, and asks for no `Budget raised:` line. The
weighted ratio had the same property, and no round treats it as a defect.
Closing it means checking a level change against the refresh's CI artifact,
which is work for #931's durations upload and not for this branch.

## Verdicts

| # | Finding | Location | Verdict | Grounds |
|---|---|---|---|---|
| 🟢 | round 2's finding 1 is closed — `section` reads headings as GitHub shows them and refuses a doubled title | `.github/scripts/budget_check.py:384` | confirmed | executed: the three planted cases pass at 400a54df and fail against f594450d's `section` |
| 🟢 | round 2's note 2 is closed — the spread is stated with its set, 0.76 to 1.14 and 0.46 to 1.54 | `.github/scripts/budget_check.py:75` | confirmed | read: the docstring, `spec.md` and `overview.md`; no `1.16` left |
| 🟢 | the fix created nothing new | `.github/scripts/budget_check.py:384` | confirmed | read: a section's start is outside every fence and comment; executed: the tree exits 0, four census modules 182 passed |

## Executed probes

| What was run | Result |
|---|---|
| the three new cases in `tests/test_a_budget_ratchets.py` at 400a54df, through `bin/test -k` | 3 passed, exit 0 |
| the same three with `budget_check.py` checked out from f594450d, then restored | 3 failed, exit 1; the clone was clean afterwards |
| `budget_check.py` over the tree at 400a54df | exit 0, every gate row holds |
| 4 census modules through `bin/test` at 400a54df | 182 passed, exit 0 |
| the broad gate (full suite, lint, typecheck) at this branch's tip | not yet: the sealer's, and it is due now |

Needs a fix: no
Loses a record or crashes: no

The broad gate is due. This round leaves nothing open, so what comes next
is the sealer's spawn on 400a54df.

## Proof block

All files were opened at 400a54df in the clone, unless named otherwise:

- the fix diff `f594450d..4ddf0edb` of `.github/scripts/budget_check.py`,
  `tests/test_a_budget_ratchets.py`, and the work item's `spec.md` and
  `overview.md`;
- `.github/scripts/budget_check.py` around `section`;
- `.github/scripts/budget_check.py` at f594450d, checked out for the red
  run.
