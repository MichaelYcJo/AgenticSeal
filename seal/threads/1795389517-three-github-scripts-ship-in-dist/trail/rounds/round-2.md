# Review round 2: 1795389517-three-github-scripts-ship-in-dist

```seal
target: 73e7f9bbc1d37b4751c7461a692a440a3bb485e3, fixes d3794015b..73e7f9bbc
```

This is a verifying round over `git diff d3794015b..73e7f9bbc`. That range holds the orchestrator's fold for finding 2 (`867e1c39c`), the fix pass's two commits (`43062a75e`, `9a9bf18ae`), round 1's close blocks (`2b5ec35e1`) and the orchestrator's fold of the reader-message coordinates (`73e7f9bbc`). It was read in a `git clone --no-local` under the round's scratch directory, checked out at the target. No `seal/parity.json` is declared, so no parity comparison was owed. No `pr.<lang>.md` is owed, because `Commit and pull request language` is English.

Carried from round 1 and not established again: the archive at `8bdf766fa` holds no path under `.github/` or `tests/`; the pattern at `.github/workflows/hygiene.yml:92` matches the paths round 1's probe listed; the two other branches of the release share no hunk with this one; and `bin/seal rules --check` exits 0. The fix range changes none of the files those facts rest on. Re-derived this round: every verdict below, and the read of `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, each whole at the target, with the three phase records read for their coordinates.

## Findings

### 1. The comment on `SHIPPED` says the plugin ships `lib/` and `skills/`, and the census leaves out a shipped hook script

```seal
severity: should
location: `tests/censuses.py:40-43`
evidence: executed `git archive 73e7f9bbc | tar -t`, filtered to `.py` paths and counted by top-level directory; executed the probe `test_tmp_census_scope.py` (the `## Probes` row); read `tests/censuses.py:40-44`, `tests/censuses.py:120-124`, `tests/censuses.py:808-815`, `tests/censuses.py:873-877`, `hooks/core-start.py`
regression: round-1#3
```

Why it matters: the unit is the comment `9a9bf18ae` added above `tests/censuses.py#SHIPPED`. Its first line reads: "The code `splitlines` and `heading_rule` read: what the plugin ships, `lib/` and `skills/`, and the release automation under `.github/scripts/`". The frame says nothing about the census scope. Round 1's finding 3 asked for a comment that says what the scope holds, and the fix pass took that finding's own snippet word for word. The defect came from that snippet's wording, "what the plugin ships, `lib/` and `skills/`". It reads as if the shipped Python were exactly `lib/` and `skills/`.

The archive at the target holds 37 `.py` files: 16 under `lib/`, 20 under `skills/` and one under `hooks/`, `hooks/core-start.py`. `_python` (`tests/censuses.py:120-124`) returns nothing for a path outside `SHIPPED`. So the census never reads the hook script, although the plugin ships it. The probe confirms this. A copy of `hooks/core-start.py` with a bare `t.splitlines()` added gets no refusal from `censuses.splitlines`. A copy of `skills/settle/scripts/rules.py` without its `:502` exemption is refused. The hook script calls no `splitlines` at the target, so today no reader slips through. The comment is the next editor's account of the scope, though. An agent adding a `.py` reader under `hooks/` reads that the census covers what the plugin ships, and then trusts a census that never reads the new file. The comment's last sentence names `tests/` as the one root left out, which strengthens that reading. The same misreading made round 1 open finding 3: a scope described by what ships, which did not match what ships.

The fix rewrites the comment so it lists the roots the census reads and claims nothing about what ships. The docstrings at `:809` and `:874` and the comment above `HEADING_SPELLING` (`:849`) now say "under `SHIPPED`", which holds with either wording, so they owe nothing. The constant keeps its name, as the fix pass decided in its close of round 1's finding 3. With the comment below, the name is the one remaining claim, and the comment corrects it. Adding `hooks/` to the tuple would also make the name true. That widens a census's reach, which no part of this work's frame asks for, so the snippet does not take it.

```python
# The code `splitlines` and `heading_rule` read: `lib/` and `skills/`, and
# the release automation under `.github/scripts/`, which the workflows run
# from the tree and `dist` does not hold. A `.py` file under any other root
# is not read: `hooks/`, which the plugin ships, and `tests/`, which holds
# the suite and its runner.
SHIPPED = ("lib/", "skills/", ".github/scripts/")
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `changelog.md:3` now says `seal rules`, `seal pr-body` and `chain-check` keep their arguments, output and exit codes, and `bin/test` keeps its arguments and exit codes. It also says `dist`'s `bin/test` "now prints its own sentence, that this copy of `bin/` has no runner beside it", and that before, the runner `dist` held answered "that no `tests` directory stood at the root", with exit 2 both times. Read against `bin/test:30-33`, which refuses with "this copy of bin/ has no runner beside it" and exits 2, and against `641b6bfb5:.github/scripts/run_tests.py:545-555`, which refused with "there is no tests directory at {root}" and returned 2. Each sentence of the rewritten item holds at the target (read).

```seal
confirms: round-1#2
```
What holds: `frame/plan.md:48` now names #1577 and #1578 running in worktrees beside this item and this item merging into `release/v0.38.6` first. That matches `routing.md:24`, the Version item, and each row of the table still puts #1571 first (read). The fold is the round's paste-ready text, word for word, as the close says.

```seal
confirms: round-1#3
```
What holds: `tests/run_tests.py` carries no `# exempt from splitlines:` line, and `9a9bf18ae` removed the line at the old `:372` (read in the diff). The `splitlines` and `heading_rule` docstrings and the comment above `HEADING_SPELLING` say "under `SHIPPED`" where they said "shipped", which matches `_python`'s prefix test (read). Executed: `git grep -n "exempt from [a-z_]*:" -- tests` prints, outside `tests/censuses.py`, only four `old_names` exemptions in `tests/lib/test_routing.py` and `tests/skills/`. This change touches none of them. The comment the same commit added is finding 1, through its `regression:` line.

The fix pass's close of round 1's finding 3 says that `skills/settle/scripts/rules.py` "entered" the census's scope. At the base the file stood at `.github/scripts/rules.py`, which `SHIPPED` already covered, so it was inside the scope at both ends of the range. The conclusion the close draws holds anyway. `git diff --name-status -M 641b6bfb5..HEAD -- '*.py'` lists two shipped files moved, `rules.py` and `run_tests.py`, and only the runner leaves the scope. The added `lib/closing.py` stands inside it and carries no exemption (executed). The probe confirmed that the census reads `rules.py:502` and still needs it: the census refuses the file once that line is gone. So the class round 1's finding names, an exemption left in a file the move took out of a census's scope, has one instance, and the fix removed it. The census kinds that skip a prefix in `tests/censuses.py` are `RECORDS`, `OLD_NAME_RECORDS` and `ROOT_NAME_SKIPPED` (`:988`, `:1179`, `:1430`). Only `ROOT_NAME_SKIPPED` names `tests/`, and the moved runner carries no `root_name` exemption (executed: `grep -n 'exempt from'` over the six moved or added `.py` files prints only `rules.py:502`).

What matched: the fold at `73e7f9bbc` puts the reader messages at `tests/skills/test_chain_check.py:1816`, `:1974` and `:1985`, in `frame/design.md:90` and `frame/plan.md:43` and `:58`. At the target, `:1816` is the `CHECK_LINE_SAYS` string that names `skills/settle/scripts/rules.py`, `:1974` is the assert on "the check-line reader `skills/settle/scripts/rules.py`", and `:1985` is the assert on "`skills/settle/scripts/rules.py` could not read the check lines". `skills/code-review/scripts/chain_check.py:173` holds `CHECK_LINES_READER = "skills/settle/scripts/rules.py"` (read).

What matched: each quote of `pr.md` stands at the source its coordinate names, word for word with runs of whitespace collapsed. A script compared all five against `frame/plan.md`, `routing.md`, `frame/design.md` and `gaps.md` at the target (executed). The records read whole state nothing the fix range contradicts. The one coordinate the range moved under them, `tests/run_tests.py`, is cited in `frame/plan.md:55` at `.github/scripts/run_tests.py` lines that `frame/plan.md` dates to `036e7d424`, so that citation still holds (read).

What matched: the narrow modules of the two code files the range changes pass in the clone, and ruff passes them. Executed: `bin/test tests/test_censuses.py tests/test_run_tests.py tests/skills/test_rules.py -q`, 357 passed, exit 0. `uvx ruff check` and `uvx ruff format --check` over `tests/censuses.py` and `tests/run_tests.py` both exit 0. The fix pass's own run of seven modules, 1462 passed, was not repeated. The suite stays `unverified` as the fix pass labelled it, and that label is honest: `gaps.md:7-9` names the orchestrator as its answerer.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `hygiene` step *a change to what ships must move the version* run by GitHub's bash on ubuntu at a pull request into `main`, with `docs` in its pattern | `.github/workflows/hygiene.yml:92` | the release pull request's CI run, read by the orchestrator |
| `bin/test.cmd` under cmd.exe at `%here%..\tests\run_tests.py` | `bin/test.cmd:7` | the repository owner, on a Windows machine |
| The full suite, the repository-wide lint and the format check at the target, which no agent runs (contract rule 2) | `seal/threads/1795389517-three-github-scripts-ship-in-dist/gaps.md:7-9` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_censuses.py tests/test_run_tests.py tests/skills/test_rules.py -q`, in the clone at the target | 357 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `tests/censuses.py` and `tests/run_tests.py` | exit 0, exit 0 |
| `git grep -n "exempt from [a-z_]*:" -- tests` | outside `tests/censuses.py`: `tests/lib/test_routing.py:156`, `tests/skills/test_settle.py:916`, `:927`, `tests/skills/test_unverified_check.py:230`, all `old_names` |
| `git archive 73e7f9bbc \| tar -t`, its `.py` paths counted by top-level directory | 16 under `lib`, 20 under `skills`, 1 under `hooks` |
| `test_tmp_census_scope.py`, run once with the clone's `.venv` pytest: `censuses.splitlines` over `skills/settle/scripts/rules.py` at the target, over a fixture copy without `:502`, over a fixture `tests/run_tests.py` with the old exemption put back, and over a fixture `hooks/core-start.py` with a bare `t.splitlines()` added | `[]`; one refusal at `skills/settle/scripts/rules.py:502`; `[]`; `[]` |
| A script comparing each quote of `pr.md` with its source, whitespace runs collapsed | all five found |
