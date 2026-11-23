# Review round 3: 1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home

```seal
target: 881a96b4f, fixes 94c866bcb..881a96b4f
```

This is a verifying round after the sealer's guarantee at `94c866bcb`. CI
run 45138012071 of `.github/workflows/test.yml` on pull request #1595 failed
one Windows shard, and two commits answer it. `940d92b5d` changes one case,
`tests/skills/test_pact_check.py#Test_module.test_accepts_the_map_named_in_posix_form_under_windows_joins`.
`881a96b4f` rewrites two `## Not verified` rows of `gaps.md`. The code
reviewed is that diff. `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `guarantee.md`
were each read whole at `881a96b4f`. No `pr.<lang>.md` stands, and none is
owed, since `seal/config.json` names English for both language keys. No
`seal/parity.json` is declared.

Carried from earlier records, not established again: the coordinate of
mutant k1 (`trail/phases/phase-3.md:58`), which this round ran again below.
This round re-established the CI facts itself, from the run's jobs and its
failed log. Every verdict below is this round's.

The account checked against the tree:

- Claimed (the commit message of `940d92b5d`): on Windows `os.path` is
  `ntpath`, so the patch replaced `ntpath.join`, and `windows_join` called
  that name and reached itself. The failed log of run 45138012071 shows
  exactly that: the shard `--splits 4 --group 3` raised `RecursionError` at
  `tests\skills\test_pact_check.py:160`, `return ntpath.join(first, *rest)`,
  called from `pact_check.py:156`, `MAP = os.path.join(*MAP_PARTS)`
  (executed: `gh run view 45138012071 --log-failed`).
- Claimed (the spawn prompt): nothing shipped changed. The diff touches
  `tests/skills/test_pact_check.py` and `gaps.md` alone (executed:
  `git diff 94c866bcb..881a96b4f`). `.gitattributes` keeps `tests/` and
  `seal/threads/` out of `dist`, as `frame/design.md` G18 says (read).

## Findings

### 1. `gaps.md`'s install-line row names the `pytest-wide` jobs on this pull request as its answerer, and the run shows they never run on it

```seal
severity: should
location: `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/gaps.md:9`
evidence: executed `gh run view 45138012071 --json jobs`, `gh pr view 1595 --json baseRefName`; read `.github/workflows/test.yml:35-51`, `.github/workflows/test.yml:174-189`, `seal/threads/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/gaps.md:9`
```

Why it matters: a row of `## Not verified` tells the next party what is
still open and who closes it. The orchestrator and the sealer act on it. The
row at `gaps.md:9` hands its open part to "the `pytest` and `pytest-wide`
jobs of `.github/workflows/test.yml` on the pull request". Neither of the
two things it leaves open can be answered there. So the row waits on a run
that will not come.

The grounds:

- Pull request #1595 targets `release/v0.38.6` (executed:
  `gh pr view 1595`). `test.yml:175` gives the `pytest-wide` job
  `if: ${{ !startsWith(github.base_ref, 'release/') }}`, so it never runs
  on this pull request. Run 45138012071 shows it as skipped, with no steps
  (executed). `test.yml:47-48` says where those legs first read a release's
  code: the release pull request into `main`.
- The row now says the run "installed the file in every `pytest` leg of
  `test.yml`". That holds for the five legs of the `pytest` job: ubuntu at
  3.12 and the four Windows shards each passed their
  `pip install -r tests/requirements.txt pytest-split==0.11.0` step
  (executed). But `test.yml:176` names the `pytest-wide` legs
  `pytest (...)` too, so "every `pytest` leg" reads as covering the macOS
  and ubuntu 3.14 legs, which installed nothing.
- The row says the `pip install -r` fallback of `CONTRIBUTING.md` was not
  run. No job of `test.yml` runs it, so no CI run on the pull request
  answers it either.

This finding takes no `regression:` line. The answerer cell was written by
phase 4 and the rewrite at `881a96b4f` kept it. The rewrite adds the
ambiguous "every `pytest` leg", which this finding covers too.

The fix replaces the row at `gaps.md:9` whole. No other record states this
answerer: round 1's `## Not judged` row is a closed round's record, and
`frame/plan.md` names no install-line answerer.

```markdown
| Phase 4's install lines: `pip install -r tests/requirements.txt pytest-split==0.11.0` in every leg of `.github/workflows/test.yml`, and the `pip install -r` fallback of `CONTRIBUTING.md` *Running the checks*. Run 45138012071 at `94c866bcb` installed the file in the five legs of the `pytest` job, ubuntu at 3.12 and the four Windows shards. It skipped the `pytest-wide` job, which `test.yml` runs on no pull request into `release/*`, so its macOS and ubuntu 3.14 legs have not installed the file. No job runs the `pip install -r` fallback of `CONTRIBUTING.md`, and it was not run; the `uvx --with-requirements` fallback was run on macOS and installed the file's packages | the `pytest-wide` jobs of `.github/workflows/test.yml` on the release pull request into `main`; for the `pip install -r` fallback, the orchestrator, by running it once in a new virtual environment |
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: `changelog.md:11` says `chain_check.py` and `pr_body.py` keep
their loops, "which run before they load any module, as `lib/console.py`'s
docstring says". `lib/console.py:58-61` names both scripts as the kind that
runs its loop before it loads any module (read). `647d0d661` touched
`changelog.md` alone, and the sealer read it at `c2363ca01`. Nothing in this
round's diff touches either file.

What matched: the fixed case tests on POSIX what it tested before. At
`94c866bcb` it bound `posix_join = os.path.join` and called `ntpath.join`
by name. At `881a96b4f` it binds `native_join, nt_join = os.path.join,
ntpath.join` (`tests/skills/test_pact_check.py:158`) and calls those names.
On POSIX `os.path` is `posixpath`, so the patch never touches `ntpath.join`,
and the two bound names are the same functions the old names reached (read).
Mutant k1 of `trail/phases/phase-3.md:58`, `MAP_SHOWN` built from `MAP` in
`pact_check.py:157`, turns the case red on
`~/.claude\agentic\pact-paths.json`, and the module passes without it
(executed, *Probes*).

What matched: the fixed case cannot recurse where `os.path` is `ntpath`.
Both names are bound before `patched.setattr` at `:166`, so `windows_join`
reaches only the unpatched `ntpath.join`. `ntpath.join` and `ntpath.isabs`
call no `join` through the module attribute, so nothing inside them reaches
`windows_join` again (executed: a search of the bodies of `join`, `isabs`,
`splitroot` and `splitdrive` in CPython 3.12's `ntpath.py`, the run's
Python being 3.12.10, which found no call of `join`). A probe took the case's own statements before its
`with` from the committed text by `ast` and ran them with `os.path` standing
as `ntpath`. Under the patch, `ntpath.join` was `windows_join`, it joined
`MAP_PARTS` to `.claude\agentic\pact-paths.json` and an absolute
`C:\plugin` path natively, and the patch undid cleanly. The same statements
from `94c866bcb` raised `RecursionError` (executed, *Probes*). On Windows
both branches of `windows_join` are the native join, so the case loads the
script with Windows' join throughout, which is what its docstring's first
sentence says it does.

What matched: the docstring's new sentence at `:154-157` says what the code
does. The patch replaces `ntpath.join` on Windows, and a call through that
name would reach `windows_join` again (read, and the failed log).

What matched: `gaps.md:8` says what the run answered. Windows shards 1, 2
and 4 passed. Shard 3 printed `1 failed, 1390 passed, 17 skipped`, and its
one failure is the Windows-joins case with `RecursionError` (executed). So
every case of the fourteen entry points that ran on the Windows leg passed,
with stdout in the locale's encoding, cp1252 there (`tests/censuses.py:132`,
read). The row keeps the fixed case open for the `windows-latest` jobs, and
says it ran on macOS alone, which holds.

What matched: `gaps.md` keeps every row in place. The diff rewrites rows 8
and 9 in their Item cells, and no row leaves.

The fix diff adds no case, so no new case is read against its group. The
changed case keeps its name and its guard, and k1 shows it still watches
`MAP_SHOWN`. The crafter's label is honest: the broad suite at HEAD is not
claimed, and `gaps.md:7` hands it to the orchestrator's broad run.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fixed Windows-joins case on a real Windows runner. This round simulated `os.path` as `ntpath` on macOS and did not run Windows | `tests/skills/test_pact_check.py:146-171` | the `windows-latest` legs of `.github/workflows/test.yml` on pull request #1595 |
| The full suite, the repository-wide lint and the format check at `881a96b4f`. `trail/gate.md` records the run at `66d542f93`, and `940d92b5d` changes a test file after it | the tree | the orchestrator's broad run, then the sealer's spawn after it |

## Probes

| Command | Result |
|---|---|
| `gh run view 45138012071 --json headSha,conclusion,jobs`; the same with each job's steps | head `94c866bcb`. `lint`, `pytest (ubuntu-latest, 3.12, 5)` and Windows shards 1, 2 and 4 succeeded; shard 3 failed at its pytest step; every `pytest` leg's install step succeeded; the `pytest-wide` job was skipped with no steps |
| `gh run view 45138012071 --log-failed` | shard 3: `1 failed, 1390 passed, 17 skipped`; the one failure is the Windows-joins case, `RecursionError` at `test_pact_check.py:160` from `pact_check.py:156` |
| `gh pr view 1595 --json baseRefName,headRefOid` | base `release/v0.38.6`, head `94c866bcb` |
| `bin/test -q tests/skills/test_pact_check.py` in a `git clone --no-local` of the branch at `881a96b4f`, under `<scratchpad>/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/round-3/clone` | exit 0: 111 passed |
| mutant k1: `MAP_SHOWN = "~/" + MAP` at `pact_check.py:157` in the clone, then `bin/test -q` on the Windows-joins case alone; the file restored by `git checkout` | exit 1: the case failed on `~/.claude\agentic\pact-paths.json`; `git status` clean after the restore |
| `pytest -q -p no:xdist test_tmp_windows_joins_as_committed.py`, with the clone's `.venv`, under `<scratchpad>/1795412533-a-dozen-small-facts-are-spelt-again-beside-their-home/round-3/` | exit 0: 2 passed. The case's statements at `881a96b4f` joined without recursion with `os.path` standing as `ntpath`; those at `94c866bcb` raised `RecursionError` |
| `uvx ruff check` and `uvx ruff format --check` over `tests/skills/test_pact_check.py` | exit 0 each |
