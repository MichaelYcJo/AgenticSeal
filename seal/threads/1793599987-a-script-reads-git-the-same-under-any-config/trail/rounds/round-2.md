# Review round 2: 1793599987-a-script-reads-git-the-same-under-any-config

```seal
target: 802f6a54, fixes c27e3db2..802f6a54
```

This is a verifying round. It read the diff of the fix pass and the
orchestrator's commits, `c27e3db2..802f6a54`: e6e2c438, baae20c1,
c16db375, e8e6dbd3 and 802f6a54. The review ran in a `git clone --no-local`
of the branch worktree at `802f6a54`. In the commands below, `$S` is the
round's scratch directory, and the clone is `$S/clone`. No `seal/parity.md`
is declared, so the record holds no `original:` line.

Carried from round 1, and not run again: the `ast` walk that listed every
git call in the shipped scripts, and the probe in which `rev-parse` and
`worktree list --porcelain` printed a path holding Hangul, a double quote
and a tab unquoted. Nothing in the fix diff touches a git call those two
read, so neither check has failed. Everything else below was established
this round.

The fix pass's account was read as a claim. It claimed that the new case
was seen red at c27e3db2 with exit 1, that `tests/skills/test_broad_gate.py`
gives 317 passed and 1 skipped, and that its 105-module narrow run failed
on the census refusal alone. The first two are checked below. The third was
not re-run: this round ran the census module alone, as the orchestrator
asked.

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-1#1
```
What holds: a copy of the gate with no `hooks/lib/gitcmd.py` beside it now
ends at exit 2 with the loader's sentence, and no traceback (executed and
read). `broad_gate.py#gitcmd_module` (`skills/verify/scripts/broad_gate.py:233-240`)
loads the helper through `load`, so a missing file and a file that raises
at import both become `Refused`. `functools.lru_cache` caches no
exception, so the docstring's "A refusal is not cached" is true. `main`
wraps its first git call, `repo_root`, in `except Refused` at
`broad_gate.py:3175-3180`. That call is the first one the module makes:
the `load(STAMP, ...)` before it runs no git. Any git call `main` makes
after `repo_root` comes after the helper has loaded and is cached, and
every call inside `gate` stands in the `try` at `:3198-3202`. So no path from `main` lets the helper's `Refused` escape.
No test patches `PLUGIN` or clears the cache, so caching the module across
the in-process cases changes no case (executed, a `git grep` over
`tests/skills/test_broad_gate.py` and `tests/github/test_release_seal.py`).

The new case `Test_main::test_refuses_a_copy_without_the_git_helper_in_a_sentence`
(`tests/skills/test_broad_gate.py:2700`) is round 1's probe made a case. It
passes, and the module gives 317 passed and 1 skipped, which matches the
fix pass's count (executed). Three mutants of the refusal in `main`, run by
#898's `seal mutate` in this clone, all went red against the new case alone
(`## Probes`, row 3). They were `except Refused` made `except ValueError`,
which is the code at c27e3db2 in effect; `return 2` made `return 1`; and the
sentence's `sys.stderr.write` made `pass`. So the case pins the exit code,
the sentence and the catch, each on its own. The fix pass placed the case in
`Test_main`, not in `Test_gate_copy` as round 1 asked. Its grounds hold:
round 1 named the wrong class. `Test_main` opens at
`tests/skills/test_broad_gate.py:2649`, and the case round 1 named as the
neighbour, `test_refuses_a_copy_whose_sibling_will_not_load`, stands inside
it at `:2675` (read). The changelog fragment now says `seal gate` exits 2
naming `hooks/lib/gitcmd.py`, and the sentence `load` writes names that
path (read). So the person-facing change is documented and pinned in the
same commit, e6e2c438, as contract rule 14 asks.

```seal
confirms: round-1#2
```
What holds: round 1 closed finding 2 `deferred the frame`, and 802f6a54
folds it into the frame (read and executed). The `to:` at
`seal/threads/1793599987-a-script-reads-git-the-same-under-any-config/frame/design.md:181-202`
now bounds the `-z` half of the rule by the property: "a script that takes
a path out of output git quotes under `core.quotePath` asks for it with
`-z`". The listings it names follow "such as", so the list is an example
and not the criterion. Git's own documentation of `core.quotePath` applies
the quoting to every command that outputs paths, so the property is the
right criterion (read). Each group of readers round 1 found correct but
outside the bare sentence now has a sentence of its own. The existence
checks and the readers that print git's line fall under "only asks whether
git printed anything, prints git's line as it came". `seal.py#indexed`
falls under "compares the line with an ASCII path the script names".
`rev-parse` and `worktree list --porcelain` fall under "print a path
unquoted", with the newline limit stated. So a later proofer reads the rule
one way, and the readers round 1 listed pass under it. The one
`check-ignore` caller in the shipped scripts, `hooks/routing-edit-gate.py:199`,
reads only the exit code of `check-ignore -q`, so the wider criterion
raises nothing new (executed, a `git grep` for `"check-ignore"` under
`hooks`, `skills` and `.github/scripts`).

The orchestrator's parse claim holds: `rule_changes.py#parse` over the
frame at `802f6a54`, with policy root `docs`, gives one `add` to
`docs/what-a-script-gates.md` *Which gate a script holds*, errors `[]` and
unread `[]` (executed). That section exists at
`docs/what-a-script-gates.md:10` (read). The docstring of
`hooks/lib/gitcmd.py` (`:26-28`) was the other place the bare rule stood,
and baae20c1 bounds it the same way (read). It gives the rule as the reason
`KEYS` leaves `core.quotePath` unset, which is that module's own fact.
`chain_check.py` printed no notice at a line of `frame/design.md` for a
test pin or a copy (executed). Scope item 4 (`frame/design.md:64`) still
opens "Every reader that takes paths out of git's output". The six readers
named after its colon bound it, and it goes with the frame at the settle,
so no reader acts on it after the settle. The fix pass left it to the
orchestrator, and the orchestrator left it as it stands (read). This round
raises no finding on it. The *Judgments of the run* row at
`frame/plan.md:115` cites `skills/implement/orchestration.md`
*Orchestrator: the order inside a ticket*, and that heading exists at
`skills/implement/orchestration.md:25` (read).

```seal
confirms: none
```
What matched: `tests/test_censuses.py` passes at `802f6a54`, 176 passed
with exit 0 (executed). At e8e6dbd3, `trail/phases/phase-2.md:83` held the
user's home directory in the path of #898's `seal mutate`. At `802f6a54`, a
`git grep` for a user path over the work item finds nothing (executed). The
rewritten line names the command as `bin/seal mutate` in #898's worktree.
It still says which copy ran at which commit, so the phase record keeps its
coordinate (read).

```seal
confirms: none
```
What matched: c16db375 closes the two proofer rows of `gaps.md`
(`seal/threads/1793599987-a-script-reads-git-the-same-under-any-config/gaps.md:9-10`)
in the form `unverified_check.py` reads: the Item cell opens with `closed`,
and the second cell says what closed it. `seal unverified` over the file
reads 2 open, 2 closed and 0 unreadable (executed). Each close cites round
1's confirmation that answered it, and round 1 holds both confirmations
(read). Both open rows name the orchestrator as their answerer.

```seal
confirms: none
```
What matched: the new case covers something its group did not. Its
neighbour `test_refuses_a_copy_whose_sibling_will_not_load` takes a
`seal_stamp.py` that raises at import. The new case takes a `seal_stamp.py`
that loads and a plugin with no git helper, the path this branch added
(read). `seal layout --pairs` over `tests/skills/test_broad_gate.py`
reports 0 pairs (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `802f6a54`, and the fix pass's 105-module narrow run; the suite stays `unverified` here, by contract rule 2, and this round ran three modules | the branch | the orchestrator, by `seal gate --base release/v0.29.0 --record 1793599987-a-script-reads-git-the-same-under-any-config`, then the sealer's spawn after it |
| Whether the new case and `tests/hooks/test_gitcmd.py` read the same on the Windows and Linux legs; this round ran on macOS | `.github/workflows/test.yml` | the orchestrator, reading the legs of the pull request's test run |

This round leaves nothing open. What comes due is the orchestrator's broad
run, and the sealer's spawn after it.

## Probes

`$S` is the round's scratch directory. The clone was deleted before the
hand-back, and the probes made no file of their own.

| Command | Result |
|---|---|
| `bin/test tests/test_censuses.py -q`, `bin/test tests/skills/test_broad_gate.py -q` and `bin/test tests/hooks/test_gitcmd.py -q`, in `$S/clone` | 176 passed; 317 passed and 1 skipped; 17 passed; each exit 0 |
| `git grep -n` for a user path over the work item at e8e6dbd3 and at `802f6a54` | one line at e8e6dbd3, `trail/phases/phase-2.md:83`; none at `802f6a54` |
| #898's worktree's `bin/seal mutate skills/verify/scripts/broad_gate.py` with three `--replace` pairs in `main`'s new `except` (`Refused` to `ValueError`, `return 2` to `return 1`, the `stderr` write to `pass`), `--tests "bin/test tests/skills/test_broad_gate.py -q -p no:xdist -k test_refuses_a_copy_without_the_git_helper_in_a_sentence"` | baseline passed; 3 mutants, 3 red, 0 survived; the clone was clean after the run |
| `rule_changes.parse` over `frame/design.md` at `802f6a54`, policy root `docs` | 1 op, `add` to `docs/what-a-script-gates.md` *Which gate a script holds*; errors `[]`; unread `[]` |
| `bin/seal unverified` over the work item's `gaps.md` | 2 open, 2 closed, 0 unreadable, exit 0 |
| `bin/seal layout --pairs tests/skills/test_broad_gate.py` | 1 file read, 0 pairs |
| `git grep -n '"check-ignore"' -- hooks skills .github/scripts` | one call, `hooks/routing-edit-gate.py:199`, `check-ignore -q`, read for its exit code alone |
