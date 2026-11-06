# Review round 2: 1793922920-the-windows-leg-finds-path-defects-last

```seal
target: ba335ef8, fixes 4e8b9418..ba335ef8
```

This is a verifying round. The range is the crafter's fix pass (`ae441282`,
`a52c1bce`, `2677ddde`), the close blocks at `679fe407`, and the
orchestrator's fold of the frame at `ba335ef8`. The round read the diff of
`4e8b9418..ba335ef8` whole and opened code outside it only where a fix
calls into it: the callers of `routing.rounds` and
`routing.rounds_unreadable`, and the definitions of the constants the probe
matched.

Carried from round 1, as coordinates, and opened again here: the four joins
of `routing.ROUNDS_DIR`, `hooks/lib/optin.py:53` (`ROUNDS = f"{TRAIL}/rounds"`),
`hooks/lib/routing.py:508` (`ROUNDS_DIR = optin.ROUNDS`), and the git paths
`skills/code-review/scripts/chain_check.py:495` and `:1426` build from the
constant. Round 1's Probes rows 2 and 3 were written again from their rows
and run again. No verdict is carried.

## Findings

None. Each of round 1's four closes holds, and the fix diff opens no defect.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the four joins are split. `hooks/lib/routing.py:578` and `:605`,
`.github/scripts/release_seal.py:357` and `.github/scripts/finding_counts.py:143`
each now join `*ROUNDS_DIR.split("/")` or `*routing.ROUNDS_DIR.split("/")`
(read, the diff of `2677ddde`). `ROUNDS_DIR` itself keeps its `/`, so the git
paths at `chain_check.py:495` and `:1426` are unchanged (read). The callers
of the two functions are `finding_counts.py:142-145`, `release_seal.py:353-359`
and `skills/settle/scripts/settle.py:1025`. Each opens or counts the returned
paths, or prints them through `os.path.relpath`, and none compares one with a
`/` spelling (executed, `git grep -n -E '\.rounds\(|\brounds\('` over the
shipped roots; read at each line).

The fix pass claimed it listed the class again with a method that resolves
what the frame's method missed, and that only these four joins came out.
This round checked the claim by its own probe, Probes row 1. It collected
every module-level and class-level constant over the 222 tracked `.py` files
whose value holds `/` through a literal, an f-string, a `+` or `%`, or a chain
of aliases to such a constant. It then matched each name and attribute
argument of the 1063 `os.path.join` calls by name. No match is the defect. Each
match was opened at its definition. Each is a same-name constant with no `/`:
`CONFIG` (`"config.md"`), `INDEX`, `optin.WORK_ITEMS` (`"threads"`),
`OPTIN.GUARANTEE` (`"guarantee.md"`), the `ITEM` and `GATE` of the test
files. Or it is a join built natively: `broad_gate.py`'s `ROUNDS_DIR`
(`:172`) and `WORKFLOW`, and `TESTS` in `tests/test_conftest.py`. Neither
`pr_body.py`'s `GATE = OPTIN.GATE` nor `routing.WORK_ITEMS` reaches a join.
No module constant is built by `"/".join` or `posixpath.join` (executed,
`git grep`, exit 1). The method matches by name, so the list is whole for
module-level and class-level string constants. A value a function builds
stays outside it, as the fix pass's answer says.

The other statements of the fact were reached. `changelog.md:4` names six
shipped scripts, the two added among them. `gaps.md` closes phase 1's
Windows row and opens one for these joins. `trail/phases/phase-1.md:17` calls
its earlier list the sample it was. The frame's fold at `ba335ef8` counts six
cross-module sites, six shipped files and 17 rewrites. Those are 11 census
sites and 6 hand-split joins, and `frame/design.md:14`, `:15`, `:19`, `:35`,
`:46`, `:60`, `:68` and `:78` and `frame/plan.md:37`, `:55`, `:56`, `:58` and
`:74` state that count (read; a search for the old counts over the work
item's files listed only `design.md:15`'s "the four shipped sites", which
is the four that row read, and phase 1's record of `225448dc`, executed).

```seal
confirms: round-1#2
```
What holds: `changelog.md:4` now ends "Seven test sites the census flagged
are joined the same way, and the two `"/c"` fixture roots in
`tests/skills/test_seal_stamp.py` take the case's temporary directory
instead", the paste-ready sentence (read). Its first sentence counts six
scripts. The six it names match the six shipped files the fold lists at
`frame/design.md:68` (read).

```seal
confirms: round-1#3
```
What holds: `_constants` reads every target of an `ast.Assign`
(`tests/censuses.py:1353-1375`), and the case
`test_refuses_a_constant_each_assignment_form_binds[chained]`
(`tests/test_censuses.py:1147-1158`) holds it. The `len(node.targets) == 1`
guard was put back through the Edit tool, and `chained` alone failed among
the 215 cases (executed, Probes row 2). The census comment at
`tests/censuses.py:1329` and `:1331-1336` now names the chained form among
those read. It lists a tuple target, `:=`, and a constant whose value is an
f-string or another name among those not read. Each of the three is true of
the code: `_constants` reads only a `Name` target of a top-level `Assign` or
`AnnAssign`, and only an `ast.Constant` value (read).

```seal
confirms: round-1#4
```
What holds: each of the three binding kinds now has a case that fails with
only its own branch removed (executed, Probes rows 2 and 3). The `ast.alias`
branch of `_bound_names` off: `a-constant-an-import-rebinds` failed.
The `name` attribute branch off: `a-constant-a-definition-rebinds` failed.
The `AnnAssign` branch of `_constants` off: `annotated` failed. Each run
changed two branches, and the reading says which case fails for which. Row 2
put back the chained guard and turned off the alias branch. The definition
branch stayed on, so `a-constant-a-definition-rebinds` stayed green. Row 3
turned off the definition and `AnnAssign` branches. The alias branch stayed
on, so `a-constant-an-import-rebinds` stayed green. The fix pass's account of
`a52c1bce` holds. With `from m import GATE`, an `ast.alias` whose `name` is
`GATE` is counted by the definition branch too. With `from m import OTHER as
GATE`, only the alias branch yields `GATE` (read, `tests/censuses.py:1339-1350`).

What matched: `bin/test tests/test_censuses.py -q -p no:randomly` at
`ba335ef8` gave 215 passed, exit 0. The 211 of round 1 plus `chained`,
`annotated` and the two rebinding cases make 215, and
`Test_module::test_every_file_no_module_file_declares_meets_every_census` is
among them (executed, Probes row 4). The new parametrized case and the two
new `NO_SLASH_JOINED` entries each hold a binding form or kind no earlier case
of `Test_slash_in_join` holds. `bin/seal layout --pairs` names no pair in
`tests/test_censuses.py` (executed, exit 0).

What matched: the dispatched run 42140399533 at `ba335ef8` completed with
conclusion `success`. Its four `windows-latest` pytest jobs passed, with
3075, 511, 1505 and 1115 passed and 38 skipped in all. That is 6244
collected, the same as the `ubuntu-latest` 3.12 leg's 6235 passed and 9
skipped. The three `macos-latest` jobs, both `ubuntu-latest` jobs, `lint`
and `durations` passed, and `release-report` was skipped (executed, Probes
row 5). That run answers the open `gaps.md` row "The joins of
`routing.ROUNDS_DIR` on Windows". `bin/seal unverified` still reads that row
as open, 1 open and 1 closed (executed). Closing it is the crafter's or the
orchestrator's act, not this round's. The two Windows cases that reach the
unlistable branch are `tests/github/test_finding_counts.py:233-262`, whose
printed path goes through `rel()`, and `tests/github/test_release_seal.py:636-650`,
which asserts `"rounds"` and `"not read"`. So the run shows that the split
breaks nothing on Windows. It does not pin the `\` spelling, which the frame
does not ask a case to pin (`frame/plan.md` *Alternatives considered* row 9).

What matched: the `CONTRIBUTING.md:435-440` bullet now says a constant
"imported from another module, or one built from other constants" is outside
the census's reach. That agrees with the census comment and with
`changelog.md:2` (read).

Two gaps hold no finding. First, the dict comment at
`tests/test_censuses.py:1099` reads "Each source has `/` near a join and none
inside one of its arguments", and the case that reads the dict is named
`test_accepts_each_shape_with_no_slash_inside_a_join` (`:1173`). Two of its
sources join a `/` at run time, which the census passes by design:
`a-constant-bound-twice` (`:1107`, from phase 1) and the fix pass's
`a-constant-an-import-rebinds` (`:1113`), where `GATE = "a/b"` follows the
import. Second, S6's `git grep -n 'BROAD_GATE_FILE)\|settle.SPECS,\|ROUNDS_DIR)'`
at `frame/design.md:60` also lists `skills/verify/scripts/broad_gate.py:2505`.
That line joins a same-name `ROUNDS_DIR` that `broad_gate.py:172` builds
natively, so no `/` reaches the join. The other hits are the work item's own
records (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| `frame/questions.md` Q2, whether every work item routed to a pull request runs the other platforms before the broad run. It is a person's row, still open, with its default kept under `Automation` `yes` | `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/frame/questions.md` | the repository owner |
| The broad gate at HEAD: the full suite, the lint and the typecheck. This round ran `tests/test_censuses.py` narrowly and probes, and labels the suite `unverified` | `seal/config.md` | the orchestrator, by its broad run, and the sealer after it |
| What issue #103 says of run 33715420379 and of the earlier repository's #81 and #96, which neither the frame nor either round opened | `seal/threads/1793922920-the-windows-leg-finds-path-defects-last/frame/design.md:12` | the repository owner |

This round leaves nothing open. What comes due is the orchestrator's broad
run at HEAD, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test test_tmp_slash_probe2.py -q -s -p no:xdist -p no:cacheprovider`, a probe in the clone. It collected module-level and class-level constants holding `/` by a literal, an f-string, a `+` or `%`, or an alias chain, and matched each name and attribute argument of every `os.path.join` call by name | exit 0, 1 passed. 222 files, 1063 calls, 256 constants. 24 matches by name. Each opened to a same-name constant with no `/` or a native join, as *Confirmations* lists. None reached the four split sites |
| `bin/test tests/test_censuses.py -q -p no:randomly`, with `len(node.targets) == 1` put back at `tests/censuses.py:1360` and `tests/censuses.py:1347` prefixed `False and`, through the Edit tool | exit 1, 2 failed and 213 passed: `test_refuses_a_constant_each_assignment_form_binds[chained]` and `test_accepts_each_shape_with_no_slash_inside_a_join[a-constant-an-import-rebinds]`. Both edits were reverted through the Edit tool |
| `bin/test tests/test_censuses.py -q -p no:randomly`, with `tests/censuses.py:1349` and `:1362` each prefixed `False and`, through the Edit tool | exit 1, 2 failed and 213 passed: `[annotated]` and `[a-constant-a-definition-rebinds]`. Both edits were reverted through the Edit tool, and `git diff --quiet` in the clone gave exit 0 afterwards |
| `bin/test tests/test_censuses.py -q -p no:randomly` at `ba335ef8` | exit 0, 215 passed |
| `gh run view 42140399533 --json status,conclusion,headSha,jobs` and `gh run view 42140399533 --log` | `status` `completed`, `conclusion` `success`, head `ba335ef8`. The four Windows jobs passed 6206 cases and skipped 38. The `ubuntu-latest` 3.12 job passed 6235 cases and skipped 9 |

The probe file was removed before hand-back. The clone and the round's
scratch logs are removed with it.
