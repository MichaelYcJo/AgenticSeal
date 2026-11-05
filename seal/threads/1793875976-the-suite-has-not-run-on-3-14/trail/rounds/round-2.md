# Review round 2: 1793875976-the-suite-has-not-run-on-3-14

```seal
target: f8ab23f4, fixes 9fcc8d39..f8ab23f4
```

This is a verifying round. It read `git diff 9fcc8d39..f8ab23f4` in a clone at `f8ab23f4`, made with `git clone --no-local` into the round's scratch directory. The range holds three commits. `2fba6eb5` changes `frame/questions.md` and `frame/plan.md`. `e5eea9b4` changes `tests/github/test_release_report.py` alone. `f8ab23f4` appends the two close blocks to `trail/rounds/round-1.md`. Executed: `git show --stat` on each.

The round carried round 1's coordinates and did not search for them again: the four places that state the leg's version (`.github/workflows/test.yml:40`, `:54`, `:70` and `CONTRIBUTING.md:147`), the guard at `.github/scripts/release_report.py:270`, and round 1's `bin/seal layout --pairs` result, which names no pair for `tests/github/test_release_report.py`. The range adds no test function. It extends one, so no new pair is owed a reading. Every verdict below was reached this round, and round 1's `git grep` and its mutant were run again at `f8ab23f4`.

Axes walked inside the fix range: the statements of the present about what a version change costs (the frame's two cells and its judgment row), the order of `other_legs` at its boundary (a system outside `LEGS`), and the extended case's name and docstring against what it holds. The range changes no workflow line, no script and no document outside the work item, so the CI, error-path, concurrency and security axes have no surface in it.

## Findings

None.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the frame no longer says a change of the leg's version is one matrix line. `frame/questions.md:17`'s options cell now ends "and with it the two `test.yml` comments and `CONTRIBUTING.md`'s sentence that name the version". Its default cell reads "Changing it later is the matrix entry, the two `test.yml` comments and `CONTRIBUTING.md`'s sentence that name the version". `frame/plan.md:53`'s Grounds cell says the same. At `f8ab23f4`, `git grep -n -i -E "3\.14"` outside `seal/threads/` and the census files lists the version where the leg depends on it at exactly those places: `.github/workflows/test.yml:40`, `.github/workflows/test.yml:54`, `.github/workflows/test.yml:70` and `CONTRIBUTING.md:147`. The other matches are a historical clause at `test.yml:41`, test data in `tests/github/test_release_report.py`, and docstrings and comments about which interpreters a module was measured on. None of those changes when the leg moves. The fold's "two comments" names the two lines of one comment block, `test.yml:40` and `test.yml:54`, and a reader who opens the block finds both. Executed: the two `git grep` commands under *Probes*; read `frame/questions.md:17`, `frame/plan.md:53` and `frame/plan.md:56`, `.github/workflows/test.yml:35-72`, `CONTRIBUTING.md:144-152`.

The close's account was read as a claim. It says the finding's search, `git grep -n -E "one matrix|matrix line|one line|by itself"` over the work item's directory, "now matches only `frame/design.md:13`", the judgment row at `frame/plan.md:56`, and round 1's record. Run at `f8ab23f4`, the search also matches `frame/questions.md:17`, through the default cell's "the release report's row follows by itself". That phrase is true: `leg_minutes` keys a job at another Python by the Python in its name (`release_report.py:258-259`). So the close's conclusion, that no file of the directory still says a version change is one line, holds. Only its list of matches is short by one. This is no finding, because no party acts on the list.

```seal
confirms: round-1#2
```
What holds: `Test_other_legs::test_accepts_the_legs_past_the_three_by_system_then_version` at `tests/github/test_release_report.py:201-214` now holds the row of a system outside `LEGS`. Its `at` map gains `"freebsd": 2.0`, and the expected list ends with `"freebsd"`, after `"macos 3.13"`. The crafter claimed that the mutant `rank = LEGS.index(system)` fails this case with `ValueError: tuple.index(x): x not in tuple`. This round reduced `release_report.py:270` to that line in the clone and ran the two modules of plan row 2. The result was 1 failed, 28 passed, exit 1. The one failure is this case, and its failing line is `.github/scripts/release_report.py:270: ValueError` with that message, so the case is red on the guard it names. The guard was restored, and the two modules gave 29 passed, exit 0, at `f8ab23f4`. Two more mutants of the same guard, `else 0` and `else len(LEGS) - 1`, were also red (`bin/seal mutate`, 3 mutants, 3 red, 0 survived). They show that the case also holds where the row stands, after `macos`, and not only that `other_legs` does not raise. The docstring's added clause, "a system outside `LEGS`, at the floor, comes after every system of it", says what the new assertion holds. The case name, "by system then version", still covers it. Ruff's check and format check on the test file exit 0. Executed: the commands under *Probes*.

What matched: the module docstring at `release_report.py:24-28` and the changelog fragment's second bullet each state "A system other than the three gets a row at the floor". A case now holds the order half of that statement. The label half, `` `<leg>` leg (minutes) ``, is the same code that prints `` `ubuntu 3.14` leg (minutes) ``, which `Test_main` pins at `tests/github/test_release_report.py:260`. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the leg runs 3.14 or 3.15 (`frame/questions.md` Q1, still open, built on its default under Automation yes) | `.github/workflows/test.yml:70` | the owner |
| The 3.14 job at `f8ab23f4`: run 42019408766 measured `b1669859`, and the commits after it change a comment, records and one case | `.github/workflows/test.yml` | the orchestrator, through the pull request's own `tests` run or a dispatch at the head |
| The broad gate (`seal/config.md` `Broad gate`) at `f8ab23f4`: unverified, because by contract rule 2 this round ran two narrow modules and a one-file lint only. The round leaves nothing open, so what comes due is the orchestrator's broad run and then the sealer's spawn | the whole tree | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git grep -n -E "one matrix\|matrix line\|one line\|by itself" f8ab23f4 -- seal/threads/1793875976-the-suite-has-not-run-on-3-14` | matches at `frame/design.md:13`, `frame/plan.md:56`, `frame/questions.md:17` and seven lines of `trail/rounds/round-1.md` (13, 18, 21, 23, 30, 36, 47) |
| `git grep -n -i -E "3\.14" f8ab23f4 -- ':!seal/threads' ':!tests/censuses.py' ':!tests/test_censuses.py'` | the version at `test.yml:40`, `:41`, `:54`, `:70`, `CONTRIBUTING.md:147`, and test data and docstrings elsewhere, as under *Confirmations* |
| `bin/test tests/github/test_release_report.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py -q`, in the round's clone at `f8ab23f4` | 29 passed, exit 0 |
| `bin/seal mutate .github/scripts/release_report.py` with three `--replace` pairs on `release_report.py:270` (`rank = LEGS.index(system)`, `else 0`, `else len(LEGS) - 1`) and `--tests` the same two modules | baseline passed; 3 mutants, 3 red, 0 survived; the file restored by the tool |
| The same two modules with `release_report.py:270` edited to `rank = LEGS.index(system)` through the edit tool, then restored | 1 failed, 28 passed, exit 1; the failure is `Test_other_legs::test_accepts_the_legs_past_the_three_by_system_then_version`, raising `ValueError: tuple.index(x): x not in tuple` at `release_report.py:270`; `git status --short` empty after the restore |
| `uvx ruff check tests/github/test_release_report.py` and `uvx ruff format --check tests/github/test_release_report.py` | exit 0 and exit 0 |
