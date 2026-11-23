# Phase 3: 1795389517-three-github-scripts-ship-in-dist

## What this phase found

**The frame held, with one departure.** Each item was judged against `frame/design.md` and the tree at `2df6f33be`.

- **Four more files stated what the removed lists said, and the frame names none of them.** They were found by `git grep` on the removed names and on the test module's path, so the list is a sample. `tests/behaviour/test_chain_hooks_hardening.py:49` cited `test_the_release_check_watches_what_ships.py#SHIPS`, a name the module no longer binds. The citation went, and the sentence keeps `hooks` in the hygiene step's pattern. `tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py:44` said `docs/` "does not ship" under that module's classification. `.github/scripts/roll_flow_measurement_issue.py:128` said `.github/` "stays home" under the same classification. `tests/github/test_dist_branch.py:22` said the archive leaves out `.github/workflows/`. Each now states what HEAD holds. None is a rule's sentence under `docs/`, so no `## Rule changes` item was needed, as `frame/design.md` *Grounding* reads `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*. The census below reaches files that cite the module by its path or by the removed names. A sentence that restates the old classification in other words was not searched for.

**Decisions settled while writing the code.**

- The new case keeps the label A7, because it holds A7's claim and more. A8 has no successor, so the module's archive cases now run A3 to A7 and then A9.
- `UNREAD` is the name of *Scope* item 9's set, "the entries the archive holds that nothing installed reads". Its comment gives each entry's reason: `assets/` for the READMEs' images, and the top-level files for people on GitHub. The comment keeps the note on `TRADEMARKS.md` (#1174) that `STAYS_HOME` carried.
- `archive_top_level` counts a top-level entry as a directory where some archive path stands under it. `tarfile` names a directory without its trailing slash, so a member's own type was not used.
- `tracked_top_level_entries` keeps its name and body. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#OPENS_NOTHING` classifies it by that name, and its sentence there is still true.
- The new A7 case judges the `.py` files the archive holds that are on disk, through `tests/conftest.py#on_disk`. This is a positive sweep, as `corpus` in the same module is. A file the working tree deleted runs nothing.
- `code_strings` leaves out a docstring and keeps every other `str` constant, a piece of an f-string among them, as *Scope* item 10 and `frame/plan.md` *Alternatives considered* (the code-string row) state. At `2b33d5523` no code string of a shipped `.py` names `.github/scripts/`. The constants probe of `frame/design.md` *Grounding* named `seal.py:1393`, `:1859`, `:2638` and `deferral_check.py:120`. Those name `.github` and not `.github/scripts/`.
- The `.gitattributes` comment keeps the workflows' second reason for leaving, GitHub's refusal of a token push of a workflow file, beside the first: no file `dist` holds loads anything under `.github/`.
- `.claude-plugin/plugin.json` moved from 0.38.5 to 0.38.6 in `2b33d5523`, the commit that adds `changelog.md`. That is what `frame/plan.md` *Operational impact* and `docs/releasing/branch-and-release.md` *Cutting a release* state. No other tracked file outside `seal/threads/` names 0.38.5. Executed: `git grep -n "0\.38\.5" -- ':!seal/threads'`, which printed nothing.
- The fragment changes nothing that `docs/layout/the-record-layout.md` *A change writes fragments, never a shared file* lists for a `### Process changes` table: no `skills/core/SKILL.md`, `CLAUDE.md`, `agents/*.md`, `skills/*/orchestration.md` or `skills/implement/bootstrap.md` in the work item's diff. So the fragment has no such table.

**Seen red (contract rule 15).** Every run below was executed at `2b33d5523`. Each line names the mutant and the assertion its case failed on, which was read for the guard the case names.

| # | Case | Mutant | Verdict and failing line |
|---|---|---|---|
| 1 | A7, first half | none: the case run at `2df6f33be`'s `.gitattributes`, before the `/.github/` line | red: `the archive holds ['.github', '.github/ISSUE_TEMPLATE', ..., '.github/scripts/close_issues_on_release.py']` |
| 2 | A7, first half | `seal mutate .gitattributes`: `/.github/ export-ignore` to `/.github/workflows/ export-ignore` | red: the same assertion, naming every script under `.github/scripts/` and the templates |
| 3 | A7, second half | `seal mutate skills/code-review/scripts/pr_body.py`: `sibling.load("lib/closing.py")` to `sibling.load(".github/scripts/close_issues_on_release.py")`, the old load of `frame/design.md` *User scenarios* row 4 | red: `these files the archive holds name a script under .github/scripts/ in code: [('skills/code-review/scripts/pr_body.py', '.github/scripts/close_issues_on_release.py')]` |
| 4 | every directory is watched or unread | none: the case run before `docs` entered the pattern | red: `['docs'] is a top-level directory the archive holds, and the hygiene step's pattern ... do not decide it` |
| 5 | the same | `seal mutate hygiene.yml`: `docs` taken out of the pattern (*User scenarios* row 2) | red: the same line for `['docs']` |
| 6 | the same | `seal mutate` of the test module: `"assets"` taken out of `UNREAD` (row 3, by removing one name) | red: the same line for `['assets']` |
| 7 | the same, never both | `seal mutate` of the test module: `"docs"` added to `UNREAD` | red: the same line for `['docs']`, now both watched and named |
| 8 | every top-level file is unread | `seal mutate` of the test module: `"README.md"` taken out of `UNREAD` (row 3) | red: `['README.md'] is a top-level file the archive holds and UNREAD ... does not name it` |
| 9 | nothing left out is watched | `seal mutate hygiene.yml`: `tests` added to the pattern | red: `['tests'] leaves the archive, so no installed copy holds it, yet the pattern ... would demand a version bump` |
| 10 | the pattern names only roots the archive holds | `seal mutate hygiene.yml`: `commands` added to the pattern | red: `the pattern names ['commands'], which the archive does not hold` |

Mutants 5, 9 and 10 also ran in one call. Its last line: `seal mutate: 3 mutants, 3 red, 0 SURVIVED, 0 with no verdict (1.5s)`. Mutants 6 to 8 also ran in one call, with the same last line except `(1.3s)`. Each mutant was then run alone, so that its failing line could be read. Every `seal mutate` run used `bin/test <module> -q -x -p no:xdist`, and each restored its file by its own hash check.

**`tests/conftest.py#archived` is only moved.** Its body and docstring are those of `tests/behaviour/test_a_cited_section_stands_in_its_file.py#archived` at `2df6f33be`, word for word, so no case was written for it and no mutant was run. A3 to A6 and A9 prove it at the new place, and so do the new A7 and the four derived cases. Census, executed at `2b33d5523`: `git grep -n "def archived" -- tests` prints `tests/conftest.py` alone.

**The censuses of the removed names.** Each was executed at `2b33d5523`:

- `git grep -n -E 'RUN_BY_A_SHIPPED_COMMAND|STAYS_HOME|_SHIPS\b|watches_what_ships\.py#SHIPS|holds_no_workflow_file|holds_only_the_scripts' -- ':!seal/threads'` prints nothing, exit 1.
- `git grep -n -E '\.github[/\\]+scripts[/\\]+(rules|run_tests)\.py' -- ':!seal/threads'` prints `docs/releasing/branch-and-release.md:168` and `:169` alone. *Rule changes* item 2 rewrites them at the settle.
- `git grep -n -E '"\.github", "scripts", "(rules|run_tests)\.py"' -- ':!seal/threads'` prints nothing, exit 1.
- `git archive HEAD | tar -t | grep -c '^\.github'` prints `0`.
- `bin/seal rules --check`, exit 0: `seal rules: all 176 check lines in 68 rule files hold.`

**The phase boundary set.** Executed at `2b33d5523`, as one command: `bin/test tests/text tests/behaviour tests/github/test_dist_branch.py tests/github/test_issue_claims_check.py tests/github/test_plugin_directory_check.py tests/github/test_release_completeness_check.py tests/github/test_release_seal.py tests/github/test_roll_flow_measurement_issue.py tests/github/test_tag_release.py tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/skills/test_seal.py tests/skills/test_broad_gate.py tests/skills/test_payload_meter.py tests/skills/test_session_cost.py tests/hooks/test_core_start.py tests/lib/test_core.py tests/evals/test_noninferiority.py tests/e2e/teammate/test_teammate_flow.py tests/test_conftest.py -q`. It exited 0, with `2852 passed, 10 skipped, 5 warnings in 64.00s`. The set holds the plan row's three modules, each test file the phase changed, the tree-wide files under `tests/text/` and `tests/behaviour/`, and each test file outside them that names `.gitattributes`, `hygiene.yml`, `plugin.json` or `roll_flow_measurement_issue`. That list was made by `git grep -l` on those four names. The reasons of the ten skips were not read. `uvx ruff check` and `uvx ruff format --check` over the seven `.py` files the phase changed exited 0.

**What `docs/releasing/branch-and-release.md` still says.** The sentence at `:44-47` lists seven watched roots, and the pattern now watches eight. The sentence at `:166-173` names three scripts that `dist` keeps, and `dist` keeps none. *Rule changes* items 1 and 2 rewrite both at the settle. No case holds either sentence any more, because `test_the_release_document_names_the_same_roots` and A8 are gone.
