# Closing memo: 1795389517-three-github-scripts-ship-in-dist

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check at the branch's HEAD after phase 1, which no agent runs (contract rule 2) | the orchestrator, at the broad gate |
| The full suite, the repository-wide lint and the format check at the branch's HEAD after phase 2, which no agent runs (contract rule 2) | the orchestrator, at the broad gate |
| The full suite, the repository-wide lint and the format check at the branch's HEAD after phase 3, which no agent runs (contract rule 2) | the orchestrator, at the broad gate |
| The `hygiene` step *a change to what ships must move the version* run with `docs` in its pattern. The suite reads the pattern out of the workflow and matches it with Python's `re`, and no run of the step's shell was made. The step runs only on a pull request whose base is `main` | the release pull request's CI run, read by the orchestrator |
| `bin/test.cmd` run under cmd.exe at its new runner path, `%here%..\tests\run_tests.py`. The suite holds only its text, and no workflow runs `bin/test` or its twin | the repository owner, on a Windows machine |

## Not done

Phase 1: no case was written for `lib/closing.py#CLOSING`'s trailing `\b`, which mutant 3 of `trail/phases/phase-1.md` showed no case watches. It was within reach: one assertion that `Closes #12abc` claims nothing. The old file misses it too, so it is an old gap. `CONTRIBUTING.md` *The test layout* asks a rebuilt module's record to name an old gap, and asks a new case only where the old files kill a mutant the new file lets survive. Writing one here would add behaviour coverage beyond a move, which the phase's Delivers cell does not ask for.

Phase 2: `tests/run_tests.py#main` keeps its refusal for a tree with no `tests/` directory, and its case `Test_main::test_refuses_a_tree_without_a_suite_in_a_sentence` stays. The check stood for `dist`, which held the runner and not the suite. The runner now stands inside `tests/`, so no copy the plugin ships reaches the check, and only the case's monkeypatched `repo_root` does. Removing it was within reach. It was not taken because the case is `Test_main`'s one `test_refuses_` case, which `CONTRIBUTING.md` *The test layout* requires of the class, and removing the case would make the move change the runner's behaviour, which the phase's Delivers cell does not ask for. Whoever next edits `main` decides whether the check goes.

Phase 3: the new A7 case of `tests/behaviour/test_a_cited_section_stands_in_its_file.py` reads a path under `.github/scripts/` only where one code string holds it whole. A shipped loader that builds the path from its parts, such as `os.path.join(".github", "scripts", "close_issues_on_release.py")`, is not read, and an installed copy, which is `main`'s whole tree, would still run it. Reading such a join was within reach: the case could join the constant arguments of a call before it searches them. It was not taken because `frame/plan.md` *Alternatives considered* chose code strings, which the Delivers cell of phase 3 builds, and its row does not name this limit. A reader that guesses a path from a call's arguments is the kind of reading `skills/core/SKILL.md` *The rule a mechanism is kept against* reports rather than blocks on. Executed at `2b33d5523`: `git grep -n -E '"\.github", "scripts"' -- ':!seal/threads' ':!tests' ':!.github'` printed nothing, so no shipped file builds such a path today. Review reads a new one.
