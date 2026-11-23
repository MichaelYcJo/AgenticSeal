# Review round 1: 1795389517-three-github-scripts-ship-in-dist

```seal
target: 8bdf766fa970030bfd1d578300737556f7102fc2 against release/v0.38.6
```

This is a finding round over `git diff 641b6bfb5..8bdf766fa`, the whole build: phases 1 to 3, the orchestrator's frame folds and the `pr.md` and `routing.md` commit. It was read in a `git clone --no-local` under the round's scratch directory, checked out at the target. No earlier round exists, so no fact was carried and every coordinate below was opened this round. No `seal/parity.json` is declared, so no parity comparison was owed. The two facts the orchestrator's prompt passed on from the crafters, labelled unchecked, were each opened: the archive at the target holds no `.github/` path, and `docs/releasing/branch-and-release.md:43-47` and `:166-174` still state the old classification, as *Rule changes* items 1 and 2 leave them to the settle. The floor case change of phase 2 was read at `tests/behaviour/test_every_entry_point_runs_at_the_floor.py:133-148`.

The axes walked were the table's ten and this change's own: what the archive holds against what an installed copy reads, a reader's equivalence after it moves between modules, a census or a test whose scope is a path prefix that a move leaves, and the statements across the tree of the old classification. Stage 1 read `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `routing.md` and the three phase records whole at the target. No `pr.<lang>.md` is owed: `Commit and pull request language` is English.

## Findings

### 1. The changelog says `bin/test` in `dist` still answers as it did, and its answer changed

```seal
severity: should
location: `seal/threads/1795389517-three-github-scripts-ship-in-dist/changelog.md:3`
evidence: executed `sh bin/test -q` in the extracted `git archive 641b6bfb5` and in the extracted `git archive 8bdf766fa` (the `## Probes` rows); read `641b6bfb5:.gitattributes:31-44`, `641b6bfb5:.github/scripts/run_tests.py` `main`, `bin/test:30-34`, `seal/threads/1795389517-three-github-scripts-ship-in-dist/gaps.md:17`, `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md:66`
```

Why it matters: the fragment becomes the release note, and a person reads it as what changed for them. Its first item ends with two sentences: "`seal rules`, `seal pr-body`, `chain-check` and `bin/test` keep their arguments, output and exit codes. `bin/test` in a copy with no `tests/` beside it, such as `dist`'s, still answers with its sentence that no runner stands there, and exits 2."

At the base, `.gitattributes` gave `.github/scripts/run_tests.py` no `export-ignore` line, so `dist` held the runner. `dist`'s `bin/test` found it and handed it to the interpreter, and the runner's `main` refused with "bin/test runs AgenticSeal's own test suite, and there is no tests directory at <root>". At the target the runner leaves with `tests/`, and `bin/test` refuses with its own sentence: "this copy of bin/ has no runner beside it". Both exit 2. So the output changed and the word "still" is false. The work item's own closing memo says the same about the base: the runner's check "stood for `dist`, which held the runner and not the suite" (`gaps.md:17`). `frame/plan.md:66` lists only `seal rules`, `seal pr-body` and `chain-check` as keeping their output, which is correct. The fragment adds `bin/test` to that list.

The fix rewrites the two sentences of `changelog.md:3`. No other statement carries the claim: `frame/design.md` *Scope* item 4 says `dist`'s `bin/` "answers with its existing sentence and exit 2", which holds.

```markdown
`seal rules`, `seal pr-body` and `chain-check` keep their arguments, output and exit codes, and `bin/test` keeps its arguments and exit codes. `bin/test` in a copy with no `tests/` beside it, such as `dist`'s, now answers with its own sentence that no runner stands beside it, where the runner `dist` used to hold answered that no `tests` directory stood there, and it still exits 2.
```

### 2. The plan says the release's other items run after this one and none is branched, and two run beside it

```seal
severity: should
location: `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md:48`
evidence: read `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md:46-60`, `seal/threads/1795389517-three-github-scripts-ship-in-dist/routing.md:24`; executed `git show 8bdf766fa -- seal/threads/1795389517-three-github-scripts-ship-in-dist/routing.md` and `git worktree list` in the main checkout
```

Why it matters: the sealer reads the plan's account of the release against `routing.md`, and the two now disagree. The commit `8bdf766fa` rewrote the routing sentence "The release's items run one after another in issue order, so no other item's plan orders against this one." It now reads: "The owner asked on 2026-11-23 for the release's items to run side by side where they can, so #1577 and #1578 run in worktrees beside this item. This item merges into `release/v0.38.6` first, and each of the others merges the base before its broad run". The same fact stands unchanged at `frame/plan.md:48`: "The spawn names eleven other items of the release, none branched yet, and says they run one after another after this one merges." At the target, `fix/1577-the-broad-gate-rewrites-cmd-exe-commands` and `fix/1578-the-root-places-omit-agentic-seal` are checked out in worktrees beside this branch. *Overlap with the release* is not one of the two sections whose statements are dated to the commit the framer read: by `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*, those are *Grounding* and *Technical context*. So the sentence is held against the target, and the target contradicts it. The conclusion drawn from it, that this item merges first, still holds.

The table's closing paragraph, `frame/plan.md:60`, says no file this work changes is named by #1577 or #1578, judged from their issue bodies, and that still holds. As facts for the orchestrator only: the two branches do touch files this one changes. `origin/fix/1577-the-broad-gate-rewrites-cmd-exe-commands` at `c37d615d` changes `templates/setup/config.md` and `tests/conftest.py`. `origin/fix/1578-the-root-places-omit-agentic-seal` at `7aa027aa` changes `templates/setup/config.md` and `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py`. No hunk of theirs overlaps a hunk of this branch.

```markdown
The spawn named eleven other items of the release. The owner asked on 2026-11-23 for them to run side by side where they can, so #1577 and #1578 run in worktrees beside this one (`routing.md` *Why this way*, the Version item). This item merges into `release/v0.38.6` first in every row, each of the others merges the base before its broad run, and each row names the new path the later framer reads.
```

### 3. The runner's `splitlines` exemption stands in a file that census no longer reads

```seal
severity: should
location: `tests/run_tests.py:372`, `tests/censuses.py:40`
evidence: read `tests/censuses.py:17-24`, `tests/censuses.py:40`, `tests/censuses.py:76-90`, `tests/censuses.py:116-121`, `tests/censuses.py:804-811`, `tests/censuses.py:868-873`, `tests/run_tests.py:372`, `641b6bfb5:.github/scripts/run_tests.py:372`, `tests/test_run_tests.py:813`, `.gitattributes:30`; executed `git grep -n "exempt from [a-z_]*:" -- tests`
```

Why it matters: an exemption comment tells the next editor that a census reads this line and lets it pass. Here no census reads it. The `splitlines` census reads a `.py` file only under `SHIPPED = ("lib/", "skills/", ".github/scripts/")` (`tests/censuses.py:40`, through `_python(rel, root, SHIPPED)` at `:810`), and so does `heading_rule` (`:872`). At the base the runner stood at `.github/scripts/run_tests.py`, inside that scope, so its `text.splitlines()` over `pyvenv.cfg` carried `# exempt from splitlines: pyvenv.cfg`. At `tests/run_tests.py` the file is outside the scope. So `test_census = census_case(TARGET)` in `tests/test_run_tests.py:813` runs neither census over it, and the comment excuses nothing.

The census module's own rule is that such an exemption is refused and leaves with its line (`tests/censuses.py:21-24`, and `_held` at `:86-90`). That rule cannot fire on a file the census never reads, so the move left the comment with nothing to refuse it. `skills/core/SKILL.md` *The rule a mechanism is kept against* asks a change to remove what stood on the old fact in the same commit, an exception among the examples. The same move left `SHIPPED` calling `.github/scripts/` shipped code, while `.gitattributes:30` now takes all of `.github/` out of `dist`. The frame and `trail/phases/phase-2.md` are silent on both. The phase's census of old spellings searched for paths, and this scope is a path prefix that names no moved file, so that search could not find it. The `git grep` above finds one other exemption under `tests/`: `tests/lib/test_routing.py:156`, an `old_names` exemption, which this change does not touch.

```python
# tests/run_tests.py:370-373, the exemption goes
    except OSError:
        return None
    for line in text.splitlines():
```

```python
# tests/censuses.py:40
# The code `splitlines` and `heading_rule` read: what the plugin ships,
# `lib/` and `skills/`, and the release automation under `.github/scripts/`,
# which the workflows run from the tree and `dist` does not hold. The suite
# and its runner under `tests/` are not read.
SHIPPED = ("lib/", "skills/", ".github/scripts/")
```

The snippet stops at the constant. The docstrings at `tests/censuses.py:805` ("No shipped reader") and `:869` ("No shipped script") and the comment above `HEADING_SPELLING` use "shipped" for the same set. With the comment in place they read against it. The fix pass weighs whether they or the constant's name owe a change too.

## Confirmations

What matched: the three loads the issue names left `.github/`: `skills/code-review/scripts/pr_body.py:181` loads `lib/closing.py`, `skills/implement/scripts/seal.py:161` names `skills/settle/scripts/rules.py`, and `bin/test:30` names `tests/run_tests.py`. Executed: `git grep -n -E '\.github[/\\]+scripts[/\\]+(rules|run_tests)\.py' -- ':!seal/threads'` prints only `docs/releasing/branch-and-release.md:168-169`. The join-form search `git grep -n -E '"\.github", "scripts", "(rules|run_tests)\.py"' -- ':!seal/threads'` prints nothing, and so does the closing memo's search over shipped roots, `git grep -n -E '"\.github", "scripts"' -- ':!seal/threads' ':!tests' ':!.github'`. Executed: `git grep` for an attribute of the closer outside `run`, `gitcmd`, `arrived`, `pull_request_body`, `issue_labels` and `main` prints nothing, so no caller still reaches a reader through the closer.

What matched: `lib/closing.py:20-127` holds the base closer's `KEYWORDS`, `CLOSING`, `FENCE`, `COMMENT`, `SPAN`, `HIDDEN` and `keywords_in` unchanged, with their comments. The one change is `MERGED_PR`'s leading `\s*` (`lib/closing.py:38`), read against each caller. `chain_check.py:472`, `close_issues_on_release.py:357` and `label_merged_on_release_branch.py:202` search a stripped subject, where the leading `\s*` changes no match and group 1 is the number. `publish_release_note.py:569` substitutes on a stripped title, as the removed `TRAILING_REF_RE` did with the same pattern minus the group.

What matched: `git archive HEAD | tar -t` holds no path under `.github/` and none under `tests/` (executed). Its top-level entries are the eight directories the pattern at `.github/workflows/hygiene.yml:92` watches, `assets`, and the seven files `UNREAD` names (`tests/behaviour/test_the_release_check_watches_what_ships.py:47-56`). This confirms the phase 3 hand-back.

What matched: *Rule changes* item 1's `from` stands at `docs/releasing/branch-and-release.md:43-47`, and item 2's at `:166-174`. Each was found word for word with runs of whitespace collapsed (read). Executed: the installed `chain_check.py --baseline release/v0.38.6 --worktree` over the branch worktree printed no notice of a test pin or a copy at a line of `frame/design.md`, and `bin/seal rules --check` exits 0 with "all 176 check lines in 68 rule files hold".

What matched: each quote of `pr.md` stands word for word at its coordinate: `frame/plan.md:74`'s Judgment and Grounds cells, `routing.md:16`, `frame/design.md:68` and `gaps.md:11` (read).

What matched: `.claude-plugin/plugin.json` reads 0.38.6. It moved in `2b33d5523`, the commit that adds `changelog.md` (executed `git show --stat 2b33d5523`), and `git grep -n "0\.38\.5" -- ':!seal/threads'` prints nothing (executed).

What matched: the narrow modules this change touches pass in the clone. Executed: `bin/test` over eight modules, 280 passed. `uvx ruff check` and `uvx ruff format --check` over the 47 `.py` files the range adds, changes or renames exit 0. `bin/seal layout --check` over the three moved test files exits 0. The suite stays `unverified` as the crafters labelled it, and that label is honest: no phase claims the full suite, and `gaps.md:7-9` names the orchestrator as the one who answers.

Two gaps of cases that hold no fact the frame states. `tests/behaviour/test_the_release_check_watches_what_ships.py:47` (`UNREAD`) is never checked against the archive, so an entry the archive stops holding stays in the set unremarked, as `STAYS_HOME` did. The new A7 case at `tests/behaviour/test_a_cited_section_stands_in_its_file.py:901-932` reads `.py` files alone. A `bin/` wrapper or `hooks/hooks.json` that handed a `.github/` script to an interpreter is held instead by `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:49` for `bin/test`, and by the floor case's derivation, not by A7. Its docstring's sentence "A load, a tool's path and a message naming one all stand in a code string" covers the `.py` files only.

Two coordinates for whoever acts next. At the settle, `tests/behaviour/test_chain_hooks_hardening.py:48-50` still lists "the roots sentence of `docs/releasing/branch-and-release.md` *Cutting a release*" among the places a removal of `hooks/` undoes. *Rule changes* item 1's `to` takes that list out, so the docstring then names a place that holds no `hooks`. In the frame, `frame/design.md:90` and `frame/plan.md:43` cite `tests/skills/test_chain_check.py:1971` and `:1980`. At the target the asserts they mean stand at `:1973-1976` and `:1985`. `:1815` and `tests/skills/test_seal.py:3465` hold.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `hygiene` step *a change to what ships must move the version* run by GitHub's bash on ubuntu at a pull request into `main`, with `docs` in its pattern. This round ran only the step's `grep -E` pattern, under a local bash, over sample paths | `.github/workflows/hygiene.yml:92` | the release pull request's CI run, read by the orchestrator |
| `bin/test.cmd` under cmd.exe at `%here%..\tests\run_tests.py` | `bin/test.cmd:7` | the repository owner, on a Windows machine |
| The full suite, the repository-wide lint and the format check at the target, which no agent runs (contract rule 2) | `seal/threads/1795389517-three-github-scripts-ship-in-dist/gaps.md:7-9` | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/lib/test_closing.py tests/behaviour/test_every_entry_point_runs_at_the_floor.py tests/github/test_label_merged_on_release_branch.py tests/github/test_issue_claims_check.py tests/github/test_publish_release_note.py tests/github/test_close_issues_on_release.py -q`, in the clone at the target | 280 passed, 5 warnings, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the 47 `.py` files `git diff --name-only --diff-filter=AMR 641b6bfb5..HEAD` lists | "All checks passed!", exit 0; "47 files already formatted", exit 0 |
| `bin/seal rules --check` | exit 0, "all 176 check lines in 68 rule files hold" |
| `bin/seal layout --check tests/test_run_tests.py tests/skills/test_rules.py tests/lib/test_closing.py` | exit 0, "3 files read, 0 refused, 0 declare no TARGET" |
| `bin/seal layout --pairs` over the same three files | one pair, in `tests/skills/test_rules.py::Test_main`, which the move carried unchanged from `tests/github/test_rules.py` |
| `git archive HEAD`, listed with `tar -tf` | 0 paths under `.github/`, 0 under `tests/` |
| `sh bin/test -q` in the extracted `git archive 641b6bfb5` | exit 2, the runner's "there is no tests directory at <root>" |
| `sh bin/test -q` in the extracted `git archive 8bdf766fa` | exit 2, `bin/test`'s "this copy of bin/ has no runner beside it" |
| The pattern of `hygiene.yml:92` through `grep -E` under bash, over `docs/a.md`, `assets/seals/owl.png`, `README.md`, `tests/x.py`, `.github/scripts/x.py`, `skills/settle/scripts/rules.py`, `.claude-plugin/plugin.json` and `docsx/a` | matched `docs/a.md`, `skills/settle/scripts/rules.py` and `.claude-plugin/plugin.json` and nothing else, exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 641b6bfb5 --root .`, the tree's own copy, in the clone | exit 0. It loads `lib/closing.py` at import and reads the records; it names no round record, gate or guarantee yet |
| `git diff --name-only 641b6bfb5...<branch>` for `origin/fix/1577-the-broad-gate-rewrites-cmd-exe-commands` and `origin/fix/1578-the-root-places-omit-agentic-seal`, intersected with this range, then `git diff -U0` of the shared files | two shared files each, no shared hunk |
