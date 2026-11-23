# Review round 2: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

```seal
target: e902ea9a3, fixes 2b75b0d79..e902ea9a3
```

This is the verifying round after round 1's fix pass. The code reviewed is
the diff of `a43ab8261`, the fix, and `e902ea9a3`, the frame's fold of it;
`73bb7bfbd` adds round 1's close blocks alone. `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md` and `pr.md` were each read whole at `e902ea9a3`. No
`pr.<lang>.md` stands, and none is owed, since `seal/config.json` names
English for both language keys. No `seal/parity.json` is declared.

Carried from round 1, not established again: that `panel` is the one caller
of `rounds_rows` outside the suite, which this round re-ran as round 1's
`git grep` and found unchanged, and the module-level loads of each file the
S10 search lists, which this round re-derived with its own `grep` because
the fix pass's grounds rest on them. Every verdict below is this round's.

## Findings

### 1. `changelog.md`'s *Removed* item says every entry point that loads `lib/` at import lost its stream loop, and `chain_check.py` and `pr_body.py` keep theirs

```seal
severity: should
location: `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/changelog.md:11`
evidence: executed `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'` and a `grep` of the module-level `import sibling` and `sibling.load` lines of each file it lists; read `skills/code-review/scripts/chain_check.py:149-159`, `skills/code-review/scripts/chain_check.py:256-285`, `skills/code-review/scripts/pr_body.py:136-160`, `lib/console.py:40-61`
```

Why it matters: the changelog fragment becomes the release note a person
reads. Its second *Removed* item says the work removed "The UTF-8 stream
loop of each entry point that loads `lib/` at import". A reader takes that
to mean no such entry point spells the loop any more. Two do, on purpose,
and the note gives no hint of them.

The grounds:

- `chain_check.py:149-159` spells the loop in an `if __name__ ==
  "__main__":` block at module level. `chain_check.py:260` then imports
  `lib/sibling.py`, and `:276-285` load `lib/` modules through
  `sibling.load`, also at module level. So the check loads `lib/` at import
  and keeps its loop.
- `pr_body.py:136-147` has the same shape: the loop first, then
  `import sibling` at `:157` and its loads below it.
- Both are deliberate. `lib/console.py:47-61` names them as the second kind
  of script that spells the loop, "which run their loops before they load
  any module". So the code is right and the changelog sentence is wrong.

The account: the fix pass declined round 1's proposed change to this
sentence, and claimed it "holds once the conversion is in: every other file
the S10 search lists loads nothing at import, loads inside a function, or
runs its loop first". The ground holds for `lib/console.py:47-61`, whose
"only these" names the two files as an exception. It does not hold for the
changelog, which names no exception: the files that "run their loop first"
are exactly the entry points that load `lib/` at import and keep the loop.
Round 1 made the same reading in its grounds ("With the fix, ...
`changelog.md:11` hold[s] as written"), so the sentence was never read
against these two files.

This finding takes no `reopens:` line. Round 1's finding 2 was the instance
in `session_cost.py`, and that instance is fixed (see the confirmation
below). The changelog was written by phase 4, so this is that phase's
defect, met here.

The fix, replacing the one sentence at `changelog.md:11` that begins "The
UTF-8 stream loop":

```markdown
The UTF-8 stream loop of each entry point that loads `lib/` at import, for `lib/console.py#to_utf8`. `chain_check.py` and `pr_body.py` keep theirs, which run before their loads so that a refusal at import does not meet a console's code page.
```

No other statement of this fact needs the change. `frame/design.md`
*Scope* item 9 and `lib/console.py:47-61` already name the two files, and
`pr.md` does not quote the changelog.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `skills/verify/scripts/broad_gate.py:1577-1579` loads
`CHAIN_CHECK` with no guard. The new comment says `main` loaded the check
before any arm ran and the chain arm read its `SEALING`. Both are true:
`main` loads it at `:2237`, and `gate` reads `SEALING` at `:2045`, before
`panel` at `:2103`. `panel` is the one caller of `rounds_rows` (`:1706`;
executed: `git grep -n rounds_rows -- ':!seal/threads'`). The two cases are
gone from `tests/skills/test_broad_gate.py`. The two that remain in
`Test_rounds_rows` pass (executed, below). No statement of the removed
sentence is left outside `seal/threads` (executed: `git grep -n "deferred
findings are not counted" -- ':!seal/threads'` printed nothing), and
`broad_gate.py` no longer names `going_on` or `Absent`. `lib/sibling.py`
keeps `going_on`, which `.github/scripts/release_seal.py:323` and `:607`
use (executed). The fold matches the code. The new `## Removes` row at
`frame/design.md:129` names the guard, its comment and both cases. The
`frame/plan.md:64` judgment row names the guard among what the change
removes. The paragraph removed from `gaps.md` *Not done* is prose recording
a decision, not a `## Not verified` row, so it owes no `closed` mark, and
round 1 asked for its removal.

```seal
confirms: round-1#2
```
What holds: `skills/verify/scripts/session_cost.py:124` binds `console =
sibling.load("lib/console.py")` at module level, and `:3675` opens the
`__main__` block with `console.to_utf8()`. The loop is gone. The S10 search
prints exactly the eleven files `frame/design.md:77` now lists (executed).
The comment at `:97-104` and the docstring of `lib_module` at `:3073-3075`
name `console.py` beside `sibling.py`. The new comment says `lib/console.py`
"reads nothing beside the standard library as it loads". That holds:
`lib/console.py` imports `os` and `sys` alone at its top and imports
`gitcmd` inside `annotate` only (read `lib/console.py:90-130`). The fix
pass declined to change the "only these" of `lib/console.py:47-61`, and
that holds. This round re-derived each file the S10 search lists.
`durations_union.py`, `release_report.py`, `hooks/core-start.py`,
`rules.py`, `deferral_check.py` and `mutation_check.py` load nothing from
`lib/` at module level. `release_seal.py` and `seal_stamp.py` load inside
functions. `chain_check.py` and `pr_body.py` run their loop first (executed:
`grep` of each file's module-level loads). The fix pass also declined to
change the changelog sentence, and that does not hold: finding 1 of this
round.

What matched: `gaps.md:8` counts fourteen entry points given the call,
thirteen by phase 3 and `session_cost.py` by the fix pass. The diff from
the base `8dea1ca7b` to `e902ea9a3` adds a `console.to_utf8()` line to
fourteen files (executed: `git diff 8dea1ca7b..e902ea9a3 -- '*.py'`,
keeping each file with an added `console.to_utf8()` line). The files are
the thirteen of `frame/design.md` G15 and `session_cost.py`. `frame/plan.md:64`
says "fourteen" too, and *Scope* item 9 names `session_cost.py` with the
merge that brought its import, `8b8b434b5`, which `git log` shows merging
#1572 (`459116a4e`).

What matched: `pr.md` quotes the judgment cell of each `frame/plan.md`
*Judgments of the run* row. The fold changed only the grounds cell of the
second row, so both quotes still match word for word (read `pr.md:1-2`,
`frame/plan.md:63-64`).

The crafter's label is honest: `gaps.md:7` hands the full suite, the lint
and the format check to the orchestrator's broad run, as `unverified`. The
fix diff adds no case, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| `session_cost.py`'s `console.to_utf8()` at a cp1252 console, with the other thirteen entry points | `gaps.md:8` | the `windows-latest` jobs of `.github/workflows/test.yml` on the pull request |
| The fix pass's two mutation runs, read in its close block and not run again | `trail/rounds/round-1.md:87`, `:185` | the sealer |
| The full suite, the repository-wide lint and the format check at HEAD | the tree | the orchestrator's broad run, which comes due once finding 1 is closed |

## Probes

| Command | Result |
|---|---|
| `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'` | the eleven files `frame/design.md:77` lists, and no other |
| `grep` of the module-level `import sibling` and `sibling.load` lines of each of those eleven files | only `chain_check.py` (`:260`) and `pr_body.py` (`:157`) import `sibling` at module level, each after its loop |
| `git grep -n "deferred findings are not counted" -- ':!seal/threads'`; `git grep -n -e going_on -e Absent -- skills/verify/scripts/broad_gate.py` | nothing; one comment line at `:2131` on a different subject |
| `git grep -n rounds_rows -- ':!seal/threads'` | `broad_gate.py:1706` in `panel`, the module docstring and the cases of `Test_rounds_rows` |
| `git diff 8dea1ca7b..e902ea9a3 -- '*.py'`, keeping each file with an added `console.to_utf8()` line | fourteen files: the thirteen of G15 and `session_cost.py` |
| `uvx ruff check` and `uvx ruff format --check` over `broad_gate.py`, `session_cost.py` and `tests/skills/test_broad_gate.py` | exit 0 each |
| `bin/test -q tests/skills/test_broad_gate.py tests/skills/test_session_cost.py tests/github/test_roll_flow_measurement_issue.py tests/behaviour/test_every_tracked_file_meets_every_census.py tests/behaviour/test_every_entry_point_runs_at_the_floor.py` | exit 0: 533 passed, 1 skipped |
