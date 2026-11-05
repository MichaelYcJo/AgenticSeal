# Review round 1: 1793875976-the-suite-has-not-run-on-3-14

```seal
target: 9fcc8d39 against release/v0.32.5
```

The round read `git diff a73e0b8c..9fcc8d39` in a clone at `9fcc8d39`. It read the code against `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and the three phase records. This is round 1, so no earlier round's coordinates were carried, and every fact below was established this round.

Axes walked: inputs (the job name's two values, the floor's spelling), exclusions and boundaries (a job at the floor, at another Python, on a fourth system, with no Python), ordering (the rows past the three), error paths (the floor's loader inside `main`'s `try`), the matrix shape the existing cases hold, the CI cost and wall clock, and the records' statements of the present. Concurrency, authorization, query scope and security have no surface in this diff: a CI matrix entry, a report script that reads a file `gh` wrote, and their cases.

## Findings

### 1. Q1's default and the plan's judgment say a change of the leg's version is one matrix line, and the build made it four places, one of which no case holds

```seal
severity: should
location: `seal/threads/1793875976-the-suite-has-not-run-on-3-14/frame/questions.md:17`, `seal/threads/1793875976-the-suite-has-not-run-on-3-14/frame/plan.md:53`, `CONTRIBUTING.md:147`, `.github/workflows/test.yml:39-41`, `.github/workflows/test.yml:54-56`
evidence: executed `git grep -n -i -E "newer python|no newer|python 3\.1[3-9]|3\.14" -- ':!seal/threads' ':!tests/censuses.py'` and `git grep -n -E "one matrix|matrix line|one line|by itself" 9fcc8d39 -- seal/threads/1793875976-the-suite-has-not-run-on-3-14`; read `frame/questions.md:17`, `frame/plan.md:53`, `CONTRIBUTING.md:144-152`, `.github/workflows/test.yml:39-70`
```

Why it matters: Q1 is open, and the owner may still answer 3.15. Whoever acts on that answer reads Q1's default cell, "Changing it later is one matrix line and the release report's row follows by itself", and its options cell, "Each option changes one matrix entry's `python` value or adds one entry". The plan's second judgment row says the same: "changing the version later is one matrix line" (`frame/plan.md:53`). At `9fcc8d39` the leg's version is stated in four places. The entry is at `.github/workflows/test.yml:70`. The comment above `include:` names it at `.github/workflows/test.yml:40` and in the timeout row at `.github/workflows/test.yml:54`, beside a run that measured 3.14. Phase 1's `315358a8` added the sentence at `CONTRIBUTING.md:147`, "the suite once more on ubuntu at Python 3.14, as one job". No case holds that sentence to the entry. `test_the_section_states_the_floor_once` reads the floor's number, and plan alternative M rejected a case that reads the 3.14 entry. So a change made as the records describe it leaves `CONTRIBUTING.md` telling contributors that CI runs 3.14, and nothing fails.

The class is the work item's statements of the present about what a change of version costs. The second `git grep` above lists them over the work item's directory. Two statements were found: Q1's row, which makes the claim in two cells, and the plan's judgment row. `frame/design.md:13` matched the search for its "one matrix" words, and it describes the matrix's shape, not the cost of a change. Contract rule 12 puts each file of the work item's directory that states the present in the crafter's closed set, and phase 1's record does not name Q1. So this is also a finding on that method: the phase that made the statement false did not list it.

The fix corrects the two records and keeps Scope 3's sentence, which the frame orders. The alternative is a frame fold that takes the number out of `CONTRIBUTING.md` and points it at the matrix. That alternative follows `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source, and every other place links to it", more closely, and it is the orchestrator's to choose. If the fold is chosen, it also rewrites the changelog fragment's last sentence of its first bullet.

In `frame/questions.md:17`, the options cell's last sentence:

```text
Each option changes one matrix entry's `python` value or adds one entry, and with it the comment above `include:` in `test.yml`, which names the version twice, and `CONTRIBUTING.md` *Running the checks*, whose sentence on the leg names it and which no case holds to the entry
```

and the default cell:

```text
3.14, as the owner named it. Changing it later is the matrix entry's `python` value, the two places the comment above `include:` names it, and `CONTRIBUTING.md` *Running the checks*, which no case holds to the entry; the release report's row follows by itself
```

In `frame/plan.md:53`, the Grounds cell's last clause:

```text
changing the version later is the matrix entry, the comment above it and `CONTRIBUTING.md` *Running the checks*, which `frame/questions.md` Q1 names
```

```seal
verdict: fixed 2fba6eb5
answer: The orchestrator folded this into the frame at 2fba6eb5, and the fix pass read that commit against the finding. Q1's options cell now ends "and with it the two `test.yml` comments and `CONTRIBUTING.md`'s sentence that name the version". Its default cell says changing the version "is the matrix entry, the two `test.yml` comments and `CONTRIBUTING.md`'s sentence that name the version". The plan's judgment row says the same in its Grounds cell. Both now name the four places HEAD holds: `.github/workflows/test.yml:70`, the comment lines at `test.yml:40` and `test.yml:54`, and `CONTRIBUTING.md:147`. The fold calls the two comment lines "two comments" where the paste-ready text said "the comment above `include:`, which names the version twice". Both point at the same two lines. The fold also leaves out the clause that no case holds the `CONTRIBUTING.md` sentence to the entry. The statement is true without it, because it lists the sentence among the places to change. The finding's search, `git grep -n -E "one matrix|matrix line|one line|by itself"` over the work item's directory at HEAD, now matches only `frame/design.md:13`, which describes the matrix's shape, the fold's own judgment row at `frame/plan.md:56`, and this record. No file of the directory still says a version change is one line.
```

### 2. A pytest job on a system outside the three now prints as a row of its own, and no case holds it

```seal
severity: should
location: `tests/github/test_release_report.py:200-212`, `.github/scripts/release_report.py:270`, `.github/scripts/release_report.py:24-28`
evidence: executed probe `bin/test tests/github/test_release_report.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py -q` with `release_report.py:270` reduced to `rank = LEGS.index(system)`: 29 passed, exit 0; read `tests/github/test_release_report.py:183-259`, `.github/scripts/release_report.py:228-276`
```

Why it matters: before this diff, `leg_minutes` summed a job on a fourth system, such as `pytest (freebsd-latest, 3.12)`, under its own key, and `table` never printed it. Since `59b0991b`, `other_legs` lists every key outside `LEGS`, so that job prints as a `` `freebsd` leg (minutes) `` row after the three. The `else len(LEGS)` at `release_report.py:270` is what keeps the sort from raising `ValueError` on such a system. The module docstring states the row at `release_report.py:27-28`: "A system other than the three gets a row at the floor too, as `<leg>` leg". The changelog fragment's second bullet states it to users: "A system other than the three gets a row at the floor as well." Phase 2 records this as its own departure (`trail/phases/phase-2.md:11`). Its seven mutations reach the guards of `LEGS` systems only, and every job list and leg map in the module names ubuntu, windows or macOS. The probe shows the guard can be taken out and both modules stay green. This is the *Regression test* row of `skills/code-review/SKILL.md` *Probes and regression tests*: a behaviour the diff changed, which no case holds. No entry of `test.yml` runs on a fourth system today, so the release ships nothing wrong. A case is still owed, because the docstring and the release note each state the behaviour as a fact.

The fix extends the order case, which already reads the rows past the three by system. The case's name and docstring change with it, so they claim what the case now holds:

```python
    def test_accepts_the_legs_past_the_three_by_system_then_version(self):
        """#1065: the legs at another Python follow `LEGS`' order, 3.9 before
        3.14 and a version with a letter after its number, and a system
        outside `LEGS`, at the floor, comes after every system of it."""
        at = {"macos 3.13": 1.0, "windows 3.13": 4.0, "freebsd": 2.0}
        now = {"ubuntu 3.14": 3.0, "ubuntu 3.14t": 1.0, "ubuntu 3.9": 3.0}
        assert report.other_legs(at, now) == [
            "ubuntu 3.9",
            "ubuntu 3.14",
            "ubuntu 3.14t",
            "windows 3.13",
            "macos 3.13",
            "freebsd",
        ]
```

```seal
verdict: fixed e5eea9b4
answer: e5eea9b4 applies the paste-ready edit to `Test_other_legs::test_accepts_the_legs_past_the_three_by_system_then_version`, with its name kept and its docstring extended. The edit was read against `other_legs` first. `"freebsd".partition(" ")` gives the system `freebsd` and an empty Python, so `order` ranks it `len(LEGS)` and it sorts after `macos 3.13`, as the list expects. `release_report.py:24-28` and `frame/design.md` *Data & interfaces*, "one row for each other key either job list holds", both state this row. Seen red: `bin/seal mutate .github/scripts/release_report.py --replace 'rank = LEGS.index(system) if system in LEGS else len(LEGS)' 'rank = LEGS.index(system)'`, run over `tests/github/test_release_report.py` and `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py` at e5eea9b4, gave 1 failed and 28 passed. The failure was this case, with `ValueError: tuple.index(x): x not in tuple` raised from `order`. At e5eea9b4 the same two modules gave 29 passed. Ruff's check and format check on the test file exit 0.
```

The fix pass shows it red with `release_report.py:270` reduced to `rank = LEGS.index(system)`. Its failing line should be the `ValueError` raised from `order`.

## Confirmations

What matched: Scope 1. `.github/workflows/test.yml:70` holds `{ os: ubuntu-latest, python: "3.14", timeout: 15 }` right after the ubuntu 3.12 entry, with no `split` and no `store`. The comment's first paragraph no longer says "at no newer Python" or "has not been measured" (`test.yml:39-41`), and the timeout row gives the leg ubuntu's base (`test.yml:54-56`). The `on:` block runs it on `push` to `main`, on `pull_request` and on `workflow_dispatch` (`test.yml:3-12`). The upload step runs only where `matrix.store` is set (`test.yml:176`), so the new entry writes no durations part, and `durations --count 4` is unchanged (`test.yml:209`). Read.

What matched: GitHub names the job as `frame/design.md` *Data & interfaces* says. Run 42019408766's job list holds `pytest (ubuntu-latest, 3.14, 15)`, with the Python as the second value in every pytest job's name. That includes the Windows shards, whose names put `timeout` last: `pytest (windows-latest, 3.12, --splits 4 --group 1, --store-durations --clean-durations, 20)`. So `PYTEST_JOB` at `release_report.py:70` reads the Python of every job the workflow writes. Executed: `gh api repos/<owner>/<repo>/actions/runs/42019408766/jobs --paginate`.

What matched: Scope 2. `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:278-293` asserts that every system the matrix names holds an entry at `rt.FLOOR_TEXT`. Its docstring cites the `CONTRIBUTING.md` sentence it holds and names the per-shard limit that `gaps.md` *Not done* records. Phase 1 claimed it saw the case red with all four Windows entries moved to 3.14. Reading the case shows `missing` would be `['windows-latest']` there, so the assertion at line 290 fails. Read. `tests/behaviour/test_release_hygiene.py:1015-1017` takes the lowest version by integer parts, so 3.14 leaves the floor check at 3.12. Read.

What matched: Scope 3. `CONTRIBUTING.md:147-148` names the leg, and the section still states the floor's number once. The plan rows' modules passed in this round's run. Executed.

What matched: Scope 4 and S4. `leg_minutes` keys a floor job as its system and any other job as `<os> <python>` (`release_report.py:258-260`). `floor()` is read inside `main`'s `try` (`release_report.py:357-364`), so a missing `hooks/lib/launch.py` ends as the exit-2 sentence. The existing cases are unchanged in the diff. The phase 2 record says the S4 case failed against the old `leg_minutes` with the `ubuntu` row reading `('2.0', '5.0', ...)`. The old code summed both ubuntu jobs under `ubuntu`, so that result follows from the code. Read. The round did not re-run phase 2's seven `seal mutate` runs. Finding 2 is the guard those runs did not reach.

What matched: Scope 5 and S1, S5. The crafter claimed run 42019408766 at `b1669859` concluded `success`, with the 3.14 job at 1 m 44 s on CPython 3.14.10, 6208 passed and 10 skipped. `gh run view 42019408766 --json headSha,conclusion,event,headBranch` gives `workflow_dispatch` at `b1669859...`, conclusion `success`. The job list gives job 127218122565 from 11:29:51 to 11:31:35. The saved job log reads `Successfully set up CPython (3.14.10)` and `6208 passed, 10 skipped in 87.05s`, and its checkout names `b1669859`. The 3.12 ubuntu job's log, fetched this round, reads CPython 3.12.16 and `6209 passed, 9 skipped`, and its nine skips are the nine the phase names. The run holds 12 jobs, as G6 predicted. Executed.

What matched: the 3.14-only skip is the case's design. `tests/skills/test_mutation_check.py:236-255` skips where `OTHER: (y := 1) = 2` compiles the same with and without the annotations flag. Compiling that line locally gave `True False` on 3.12 and `False False` on 3.14, so on 3.14 the case cannot tell the guard from its absence. Executed.

What matched: `af153874` changes `test.yml` only in the timeout row's comment, and after `b1669859` no commit changes a line the job runs other than records under `seal/threads/`. Executed: `git diff b1669859 af153874 -- .github`, `git diff b1669859..9fcc8d39 --stat`.

What matched: the row closed in `seal/threads/1793862998-seal-arms-is-run-by-nothing/gaps.md:8` opens with `closed`, as `skills/implement/SKILL.md` asks. Its claim also holds: the 3.14 job's skip lines name no case of `Test_module` in `tests/skills/test_mutation_check.py`, its summary names no failure, and both ubuntu jobs ran 6218 cases. Executed: the job log read above.

The comment's first paragraph at `.github/workflows/test.yml:40-41` describes `arms-grammar`, a job no longer in the tree, as one "which ran one module on 3.13 and 3.14". Scope 1 asked for the reference to `arms-grammar`, and the added clause is true, but it is history that `skills/core/SKILL.md` sends to git and the work record. It tells no reader to do anything wrong, so it is no finding. The fix pass may drop the clause if it is in the file anyway.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the leg runs 3.14 or 3.15 (`frame/questions.md` Q1, open, built on its default under Automation yes) | `.github/workflows/test.yml:70` | the owner |
| The 3.14 job at `9fcc8d39`: run 42019408766 measured `b1669859`, and the commits after it change a comment and records | `.github/workflows/test.yml` | the orchestrator, through the pull request's own `tests` run or a dispatch at the head |
| The `` `ubuntu 3.14` leg (minutes) `` row over a real job list: every case reads a job list written by hand | `.github/scripts/release_report.py` | whoever prepares the 0.32.5 release, from the release pull request's `release-report` summary |
| The broad gate (`seal/config.md` `Broad gate`) at `9fcc8d39`: unverified, because by contract rule 2 this round ran narrow modules only | the whole tree | the orchestrator, at the broad run once the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/text/test_ci_gives_the_checks_what_they_need.py tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py tests/behaviour/test_release_hygiene.py tests/github/test_release_report.py tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py -q`, in the round's clone at `9fcc8d39` | 127 passed, 2 skipped, exit 0 |
| The same runner over `tests/github/test_release_report.py` and `tests/text/test_the_release_table_reads_two_trees_and_fails_nothing.py`, with `release_report.py:270` edited to `rank = LEGS.index(system)` and restored afterwards | 29 passed, exit 0: the mutant survives (finding 2) |
| `bin/seal layout --pairs` | exit 0; no pair names `test_release_report.py` or `test_the_suite_has_a_command_that_is_cheap_twice.py` |
| `gh run view 42019408766 --json ...`, the run's job list, and `gh run view 42019408766 --job 127218122715 --log` | as under *Confirmations* |
| `python3.12 -I -c ...` and `python3.14 -I -c ...` compiling `OTHER: (y := 1) = 2` with `dont_inherit=True`, without and with the annotations flag | 3.12: `True False`; 3.14: `False False` |
