# Design: 1795397629-git-runs-through-thirty-hand-written-helpers

## Grounding

The tree as read at `d0b15b72f`.

| Policy clause | What it fixes for this work |
|---|---|
| G1. `docs/running/what-a-script-gates.md` *Which gate a script holds*, the rule opening **A script reads git the same under any configuration** (read) | The rule binds only the `git log` and `git status` a script under `lib/`, `skills/` or `.github/scripts/` starts, and leaves to review whether a call is one of them. It says nothing of a timeout, of a command that could not start, or of `gh`. This work widens it to every git and `gh` command and states what an unanswered command is, in `## Rule changes` |
| G2. `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | A fact has one source, and a change removes in the same commit what stood on the old fact. So the timeout constants, the handlers and the helper copies this work replaces leave in the commit that replaces them (`## Removes`) |
| G3. `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | The subject of this work item is the code, so the rule it changes is stated in `## Rule changes` for the settle, and no file under `docs/` is edited by the build |
| G4. `lib/sibling.py#Absent` (read) | The plugin already holds a `SystemExit` raised from a `lib/` reader, so that a caller which does not catch it ends at a stated exit code with no traceback. `Failed` in *Data & interfaces* follows that precedent |
| G5. `CONTRIBUTING.md` *House rules*, **Every file read or written names its encoding** (read) | A text-mode process call names `encoding="utf-8"`. The runner names it once, with `errors="replace"`, the spelling every text-mode git call at `d0b15b72f` already uses |
| G6. `tests/censuses.py` *floor_syntax* and the docstring of `lib/sibling.py` (read) | A module the `Stop` hook reaches runs on the `python3` it finds, 3.9 on a stock macOS. `skills/verify/scripts/seal_stamp.py#_gitcmd` loads `lib/gitcmd.py`, so the runner stays Python 3.9 syntax, as `lib/console.py` does |
| G7. `CONTRIBUTING.md` *The test layout*, as `skills/verify/scripts/test_layout.py` states it (read) | Each public top-level function of a module has one class `Test_<name>` in the module's test file, with a `test_accepts_` and a `test_refuses_` case. Each function this work adds to `lib/` gets one. A unit that leaves takes its class with it |
| G8. Issue #1573 and `routing.md` (executed: `gh issue view 1573 --json title,body,comments`; read: `routing.md`) | The body as filed, no comments. `routing.md`: Planning `framer`, Implementation `crafter`, Review through the review chain, Automation `yes`. The release is a patch, so the work builds no `feat:` |
| G9. Every process call under the four roots of the issue's *Done when* (executed: `git grep -nE "subprocess\.(run\|Popen\|call\|check_call\|check_output)\(" d0b15b72f -- skills lib .github/scripts evals/scripts ':!lib/gitcmd.py'`) | The search prints 71 lines. 62 are calls that start git or `gh`, each named by a *Scope* item. The other 9 lines are no git or `gh` call: `evals/scripts/noninferiority.py:395` (`claude`), `skills/implement/scripts/seal.py:2550` (a tool's script), `skills/verify/scripts/broad_gate.py:822` (the `Broad gate` command), `:844`, `:903` and `:923` (comments), `:2427` (a shipped script), `skills/verify/scripts/mutation_check.py:405` (the tests command) and `skills/verify/scripts/test_layout.py:1027` (pytest). One more `gh` call is reached through a parameter whose default is `subprocess.run`: `skills/code-review/scripts/chain_check.py:622`, with the parameter at `:569` and `:622` (executed: `git grep -n "=subprocess.run" d0b15b72f -- skills lib .github/scripts evals/scripts`). No file under `hooks/` or `bin/` imports `subprocess` (executed: `git grep -lE "import subprocess\|from subprocess" -- ':!tests/**'`) |
| G10. What each call does with a slow or absent git (read: the calls G9 names as starting git or `gh`, at `d0b15b72f`) | The handlers that catch a timed-out process are spelt four ways (executed: `git grep -n "TimeoutExpired\|SubprocessError" d0b15b72f -- skills lib .github/scripts evals/scripts`). Every line it prints catches a git or `gh` call except `mutation_check.py:422`, which bounds the tests command, and `## Removes` lists them. Seven calls have a timeout and no handler: `seal.py:1847`, `:1912`, `:1926`, `:1996`, `:2367`, `:2405` and `chain_check.py#git` (`:358`). Every other call has no timeout, every call of `skills/settle/scripts/settle.py` and `skills/settle/scripts/rule_changes.py` among them, so a slow git holds `seal settle` until it answers. The bounds that exist are 5 s (`lib/optin.py`, `lib/routing.py`), 15 s and 30 s (`seal.py`), 30 s (`chain_check.py#GH_TIMEOUT`) and 60 s (`chain_check.py#git`, `pact_check.py#git`, `settle.py#GH_TIMEOUT`, `pr_wait.py#GH_TIMEOUT`); no comment beside any of them records a measurement |
| G11. What a git timeout does to `seal` today (executed: the probe `<scratchpad>/1795397629-git-runs-through-thirty-hand-written-helpers/frame/test_tmp_timeout_probe.py`, run against a `git clone --no-local` of `d0b15b72f`, which makes one git subcommand raise `subprocess.TimeoutExpired` and calls `seal.py#main`) | `seal mode local` with `git rm` timing out: a `TimeoutExpired` traceback, after the root had moved to `.git/seal` and the `Mode` key was written. `seal mode shared` with `git add` timing out: the same traceback, after the root had moved to `<repo>/seal`. `seal pr-checks install` with `git add` timing out: the same traceback. `seal mode local` with `git status` timing out: exit 1, `git status could not be run (…timed out after 15 seconds)`, nothing moved. `seal export` with `git rev-parse` timing out: exit 1 and `not inside a git repository — seal works on a clone`, which is `lib/optin.py#repo_root` reading the timeout as no repository. `seal export` in local mode with `git config` timing out: exit 0, the zip written, and the line naming the remote as left out |
| G12. `seal export`'s reading of a manifest field git did not answer (read: `seal.py#manifest_of`, `#remote_url`, `#head_sha`, and the cases `tests/skills/test_seal.py:910`, `:1385` and `:1679`, which raise `TIMED_OUT` at `config --get`) | A field git did not answer is left out of the manifest, its line is printed, and the export exits 0, because the machine that ran it is the one that can run it again. That reading tells a failure from an empty answer already, and it stays |
| G13. How long the reads take (executed: `/usr/bin/time -p` over the six heaviest reads at the repository, each 0.01 s to 0.02 s over 675 commits; `seal settle` as a dry run in the clone, 1.42 s whole) | No read the scripts make here comes near any bound in G10. The bound is a guard against a git that hangs, and not a budget of a read |
| G14. How Python ends on an uncaught `SystemExit` subclass whose code is a message (executed: the probe `<scratchpad>/1795397629-git-runs-through-thirty-hand-written-helpers/frame/test_tmp_systemexit.py` under Python 3.15.0 and `/usr/bin/python3` 3.9.6) | Both print the message as one line on stderr and exit 1, and an `except Exception` around the raise does not catch it |
| G15. The two branch readers (executed: `git symbolic-ref --short -q HEAD` and `git rev-parse --abbrev-ref HEAD` on an unborn branch, a branch with a commit and a detached HEAD, git 2.50.1) | Unborn: `feat/x` against `HEAD`. With a commit: `feat/x` against `feat/x`. Detached: nothing against `HEAD`. So `lib/routing.py#current_branch` answers what `broad_gate.py#branch_name` answers on every HEAD that holds a commit, which is every HEAD the broad gate names a branch beside |
| G16. The copies of a path spelt the way git spells it (executed: `git grep -n "relpath(.*replace(os.sep" d0b15b72f -- skills lib .github/scripts evals/scripts`) | Each line the search prints is the open-coded form of `lib/gitcmd.py#git_path`, and *Scope* item 9 lists them. The issue counted seven at v0.38.5 without naming its search; this search, over the four roots of the issue's *Done when*, gives the list *Scope* item 9 holds |
| G17. What a missing `lib/` costs each script that loads nothing from it at import (read: the docstrings and imports of `.github/scripts/release_seal.py:24-27` and `:84-95`, `seal_stamp.py#_gitcmd`, `session_cost.py#lib_module`, `rule_changes.py#gitcmd`, `test_layout.py`, `noninferiority.py`, `roll_flow_measurement_issue.py`) | `release_seal.py` names why: every way it fails ends in the day's note at exit 0, and its `main` catches `(Exception, SystemExit)` (`:611`). `seal_stamp.py`, `session_cost.py` and `rule_changes.py` load `lib/` at first use already. `test_layout.py`, `noninferiority.py` and `roll_flow_measurement_issue.py` import nothing from `lib/`, and none of their docstrings gives a reason, so each loads the runner as the scripts beside it load `lib/` |
| G18. `seal mode` on a stage step git refused (read: `seal.py#switch`, `:2363-2436`; `tests/skills/test_seal.py:2881-2891`) | Where `git add` or `git rm -r --cached` exits non-zero, the switch prints that the records could not be staged and how to finish by hand, then prints `Now commit.` and returns 0. The case pins `code == 0` beside the text that says a commit now would record nothing |
| G19. The closer's `run` (read: `seal/threads/1795389517-three-github-scripts-ship-in-dist/frame/plan.md` *Overlap with the release*, the row for #1573) | #1571's frame kept `.github/scripts/close_issues_on_release.py#run` in the closer, because `label_merged_on_release_branch.py` and `release_completeness_check.py` load it there. That decision is not argued again: the closer keeps its `run`, and the runner moves under it |
| G20. Whether the tree already holds the runner (executed: G10's handler search, and `git grep -n "def git\|def gh\|def run_git\|def run_gh\|def git_run\|def git_bytes" -- skills lib .github/scripts evals/scripts`) | `lib/gitcmd.py` holds `argv`, `git_path` and `under_root` and starts no process. The nearest whole runner is `skills/code-review/scripts/pr_wait.py#gh`, which bounds its call, names the command and tells a timeout from an exit code, and it is pr_wait's own. Nothing in `lib/` starts git or `gh` except `lib/optin.py` and `lib/routing.py`, each for its one question |
| G21. The policy in force beside this work (read: `docs/README.md`; executed: `grep -ln "what-a-script-gates" seal/threads/*/frame/design.md`, and a read of each match's `## Rule changes`; `gh release view --json body` of v0.38.5, which holds no *Process changes* section; the *Process changes* tables of the fragments under `seal/threads/`; `seal/follow-up.md`, whose two tables are empty) | No unsettled design changes *Which gate a script holds*. No process change concerns how a script starts git. `seal/follow-up.md` holds no item this work is the prerequisite of |

## Scope

In:

1. **`lib/gitcmd.py` runs every git and `gh` command a script starts**, through the surface *Data & interfaces* gives: `TIMEOUT`, `Failed`, `Unrun`, `Exited`, `git`, `gh` and `is_ancestor`. Its docstring says it is the one place a script's git or `gh` command is started, and that `argv` builds every git command, where it now says every `git log` and `git status`.
2. **`lib/optin.py` and `lib/routing.py` ask through the runner.** `lib/optin.py` gains `toplevel(cwd)`, which raises `Failed` where git did not answer. `repo_root` becomes `toplevel` with `Failed` read as `""`, its documented direction toward *not opted in*, and `git_common_dir` reads `Failed` as `""` the same way. `lib/routing.py#current_branch` reads `Failed` as `""`, as it reads an unreadable branch now.
3. **`write_output` moves from `.github/scripts/publish_release_note.py` to `lib/console.py`.** `tag_release.py` loads it from there and no longer loads `publish_release_note.py`, and with it `settle.py` (`publish_release_note.py:133`). The comment at `.github/workflows/publish-release.yml:67` names `lib/console.py#write_output`.
4. **`skills/implement/scripts/seal.py`**, its 11 calls at `:255`, `:1527`, `:1597`, `:1627`, `:1847`, `:1912`, `:1926`, `:1996`, `:2172`, `:2367` and `:2405`:
   - `git_asked` runs through `gitcmd.git` and reads `Failed` as `(None, why)`, its documented answer. `gitlinks_under_root` asks through `git_asked` and no longer spells it again.
   - `resolve` and `pr_checks` ask `optin.toplevel`, so `seal export`, `seal pr-checks` and every other subcommand say that git did not answer, and not that there is no repository.
   - `tracked` no longer reads a git that did not answer as *nothing tracked*.
   - In `switch`, a stage step that did not happen, by a non-zero exit or by `Failed`, prints the step's existing line naming the command and what to run by hand, prints no `Now commit.` line, and makes `seal mode` exit 1. The same holds for `tracked` asked inside `switch`.
   - `pr-checks install` and `remove` read `Failed` at their `git add`, `git diff --cached --quiet` and `git rm` as each reads a non-zero exit now: `unstaged`, not HEAD's copy, and `failed`.
5. **`skills/settle/scripts/settle.py` and `skills/settle/scripts/rule_changes.py`.**
   - Each of settle's calls at `:265`, `:312`, `:332`, `:341`, `:426`, `:519`, `:1091`, `:1612` and `:1748` runs through the runner. `show`, `released`, `resolves`, `git_run` and `git_fields` keep their readings of a non-zero exit.
   - `reaches` goes, for `gitcmd.is_ancestor`. `tracked_names` and `tracked_text` read through `git_fields`. `ask_gh` runs through `gitcmd.gh` and reads `Unrun` as `Unasked`. `GH_TIMEOUT` goes.
   - `settle.py#main` catches `gitcmd.Failed` and writes one line, `settle: ` and the exception's line, and returns 2.
   - `rule_changes.py#order` and `#merge_order` read the exit code: a non-zero exit raises `gitcmd.Exited`, and the history is not read as empty. `_ancestor` becomes `a != b and gitcmd.is_ancestor(root, a, b)`.
6. **`skills/code-review/scripts/chain_check.py` and `skills/code-review/scripts/pr_wait.py`.**
   - `chain_check.py#git` runs through `gitcmd.git` and keeps its `None` for a non-zero exit. `commit_of`, `merge_base` and `tree_at` ask through it. `is_ancestor` goes, for `gitcmd.is_ancestor`. `follows` asks `touched` for a commit's paths.
   - `pull_request_from_gh` defaults its seam to `gitcmd.gh`, reads `Unrun` as `unknown`, and `GH_TIMEOUT` goes. `main` catches `gitcmd.Failed` and returns 2.
   - `pr_wait.py#gh` and `#head` run through the runner and read `Failed` as `Unanswered`. Its `GH_TIMEOUT` goes, and its docstring (`:55`) names `lib/gitcmd.py#TIMEOUT`.
7. **The scripts under `skills/verify/scripts/`.**
   - `broad_gate.py#git` runs through `gitcmd.git`. `repo_root` goes, for `optin.toplevel`. `branch_name` goes, for `routing.current_branch` (G15). The worktree removal at `:1662`, which runs in a `finally`, catches `Failed` and names the scratch worktree on stderr, so a cleanup that timed out does not replace the run's result. `main` catches `Failed` and returns 2, the gate's refusal.
   - `pact_check.py#git` runs through `gitcmd.git`, and `Failed` reaches `main`, which returns 2.
   - `seal_stamp.py#_git` reads `Failed` as `None`, as it reads a non-zero exit, because `--stop` exits 0 whatever happens (`seal_stamp.py:78`).
   - `session_cost.py#run_gh` reads `Unrun` as `(None, "", line)` and `#run_git` as `(None, b"")`, each its documented reading of a command that could not start.
   - `test_layout.py#_git` and `#_tracked` run through `gitcmd.git`, `_tracked` with `check=True`. `_toplevel` goes, for `optin.repo_root`. `main` catches `Failed` and returns 2.
   - `unverified_check.py#repo_root` goes, for `optin.repo_root` of the path's directory.
8. **The scripts under `.github/scripts/` and `evals/scripts/`.**
   - `close_issues_on_release.py`: `run` stays the closer's (G19). Its first argument names the program, `git` or `gh`, and the rest are that program's arguments, which it hands to `gitcmd.git` at the repository's top or to `gitcmd.gh`, with `check=True`. A caller that hands it `gitcmd.argv`'s output now hands it `git` and the git arguments alone, since `gitcmd.git` builds the argv: `close_issues_on_release.py:343` and `:345`, and `release_completeness_check.py:134`. `attempt` reads `Failed` as `(False, line)`. `_issue_api` and the label removal at `:182` run through `gitcmd.gh` and keep their readings.
   - `publish_release_note.py`: `run`, a byte-for-byte copy of the closer's, goes, and its callers use the runner. The milestones list, the release lookup and the pull request list read `Unrun` as each reads a failure now.
   - `roll_flow_measurement_issue.py`: `run`, another byte-for-byte copy of the closer's, goes, and its callers use `gitcmd.gh` with `check=True`. `try_run` reads `Failed` as `None`. The script loads `lib/gitcmd.py` through `lib/sibling.py` (G17).
   - `release_seal.py`: `gh` and `tagged` load the runner at first use and read `Failed` as `Refused`. Its docstring already names why it loads nothing at import.
   - `tag_release.py`: `git` and `create` run through the runner, and `create` reads `Unrun` as its error string.
   - `dist_branch.py#git` runs through `gitcmd.git` with `binary=True` and keeps `GitFailed` for a non-zero exit.
   - `plugin_directory_check.py#is_ancestor` keeps its third answer, `None`, for a commit the clone lacks or a git that did not answer, and asks `gitcmd.is_ancestor` for the last step.
   - `evals/scripts/noninferiority.py#git_bytes` runs through `gitcmd.git` with `binary=True` and `check=True`, and the script loads `lib/gitcmd.py` through `lib/sibling.py` (G17).
9. **The 14 open-coded `os.path.relpath(...).replace(os.sep, "/")` become `gitcmd.git_path(os.path.relpath(...))`**: `.github/scripts/finding_counts.py:141` and `:212`, `.github/scripts/release_report.py:253`, `skills/implement/scripts/seal.py:378`, `:687` and `:1352`, `skills/settle/scripts/rules.py:215` and `:283`, `skills/settle/scripts/settle.py:1161` and `:1606`, `skills/verify/scripts/pact_check.py:677`, `skills/verify/scripts/seal_stamp.py:1328`, and `skills/verify/scripts/test_layout.py:1086` and `:1199`.

Out:

- **The readers of `rev-parse --verify --quiet <ref>^{commit}`**, `chain_check.py#commit_of`, `settle.py#resolves`, the first two steps of `plugin_directory_check.py#is_ancestor`, `tag_release.py#tag_commit_of` and `release_seal.py#tagged`. After *Scope* items 5, 6 and 8 each one asks through the runner, so none is a runner copy, and the issue names none of them. Folding them into one reader is a second change.
- **`broad_gate.py#run` and its handling of `cmd.exe`** (`:822`, `:844` to `:1160`): #1577 rewrites them, and they run the `Broad gate` command, not git.
- **The calls G9 names as starting no git or `gh`.**
- **`tests/`**, `tests/run_tests.py` among them. The issue's *Done when* names `skills/`, `lib/`, `.github/scripts/` and `evals/scripts/`, `tests/run_tests.py` starts `pip` and pytest, and the cases' own git helpers build fixtures.
- **`seal export`'s exit 0 where git did not answer for a manifest field** (G12).
- **A census that refuses a git or `gh` call outside `lib/gitcmd.py`** (`plan.md` *Alternatives considered*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. A slow git in the middle of `seal mode local` | Given a shared root, when `seal mode local` runs and `git rm -r --cached` does not finish within `TIMEOUT`, then the root has moved and the key is written as now, the output holds the line `the records are still tracked:` followed by the runner's line naming `git rm` and the bound, and the line naming `git rm -r --cached :/seal` to run by hand, holds no `Now commit.` line, and the command exits 1 with no traceback | A case in `tests/skills/test_seal.py` that raises `subprocess.TimeoutExpired` at `rm`, through the file's `unanswered` helper or its successor, seen red against `d0b15b72f`, where it raises |
| S2. A slow git in the middle of `seal mode shared` | Given a local root, when `seal mode shared` runs and `git add` does not finish within `TIMEOUT`, then the output holds `seal/ could NOT be staged:` with the runner's line, and the `git add -f :/seal` line, no `Now commit.` line, and exit 1 | A case in `tests/skills/test_seal.py`, seen red against `d0b15b72f` |
| S3. `git add` refused by an ignore rule in `seal mode shared` | Given `.gitignore` holding `seal/`, when `seal mode shared` runs, then the output holds `seal/ could NOT be staged:` with git's line and the `git add -f :/seal` line as now, holds no `Now commit.` line, and the command exits 1 | `tests/skills/test_seal.py:2881-2891` with `code == 1` (*Removes*) |
| S4. A slow git in `seal pr-checks` | When `install`'s `git add`, or `remove`'s `git diff --cached --quiet` or `git rm`, does not finish within `TIMEOUT`, then `install` prints its `could NOT be staged` line and exits 1, `remove` keeps the index's copy at the first and prints its `could not be removed` line at the second, each exiting 1 | Cases in `tests/skills/test_seal.py` |
| S5. A slow git when `seal export` asks for the repository | When `git rev-parse --show-toplevel` does not finish within `TIMEOUT`, then `seal export` prints one line naming `git rev-parse` and the bound, does not print `not inside a git repository`, and exits 1 | A case in `tests/skills/test_seal.py`, seen red against `d0b15b72f`, where it prints `not inside a git repository` |
| S6. A slow git for a manifest field of `seal export` | When `git config --get remote.origin.url` does not finish within `TIMEOUT`, then the zip is written, the remote is left out with its line, and the export exits 0 | The cases at `tests/skills/test_seal.py:910`, `:1385` and `:1679`, unchanged in what they assert but for the line: `:910` pins the runner's own line after `the remote was left out — `, which a wrapper would state a second time |
| S7. A slow git in `seal settle` | When any git read of the dry run, `--apply` or `--draft` does not finish within `TIMEOUT`, then `settle` writes one line on stderr, `settle: ` and the runner's line naming the command and the bound, and exits 2 with no traceback | A case in `tests/skills/test_settle.py`, seen red against `d0b15b72f`, where the read has no bound |
| S8. A slow git in `chain-check` | When a git read does not finish within `TIMEOUT`, then `chain-check` writes one line naming the command and exits 2 | A case in `tests/skills/test_chain_check.py`, seen red against `d0b15b72f`, where it raises a traceback at exit 1 |
| S9. The runner tells a failure from an answer | Given `gitcmd.git` and `gitcmd.gh`: a command past `TIMEOUT` raises `Unrun` whose line names the program, the arguments the caller passed and the bound; a program not on `PATH` raises `Unrun` naming it; a non-zero exit is returned as a `CompletedProcess` with its code; `check=True` turns the non-zero exit into `Exited` naming the command, its code and git's first line on stderr; the argv `gitcmd.git` starts is `argv("-C", root, *args)`; an uncaught `Failed` ends a process with its one line on stderr and exit 1 | `Test_git`, `Test_gh` and `Test_is_ancestor` in `tests/lib/test_gitcmd.py`, and one case that runs a script raising `Unrun` uncaught under `sys.executable` and reads its exit code and stderr |
| S10. No script starts git or `gh` outside the runner | Given the tree after the build | `git grep -nE "subprocess\.(run\|Popen\|call\|check_call\|check_output)\(" -- skills lib .github/scripts evals/scripts ':!lib/gitcmd.py'` prints lines in `evals/scripts/noninferiority.py`, `skills/implement/scripts/seal.py`, `skills/verify/scripts/broad_gate.py`, `skills/verify/scripts/mutation_check.py` and `skills/verify/scripts/test_layout.py` only, each one of the calls G9 names as starting no git or `gh`, and `broad_gate.py`'s three comment lines until #1577 removes them. `git grep -n "=subprocess.run" -- skills lib .github/scripts evals/scripts` prints nothing. Both run at `d0b15b72f` and accounted in G9 |
| S11. One copy of each helper the issue names | Given the tree after the build | `git grep -n "relpath(.*replace(os.sep" -- skills lib .github/scripts evals/scripts`, `git grep -n "GH_TIMEOUT" -- skills lib .github/scripts evals/scripts` and `git grep -nE "def (is_ancestor\|reaches\|repo_root\|_toplevel\|branch_name)\(" -- skills lib .github/scripts evals/scripts ':!lib/gitcmd.py' ':!lib/optin.py'` print, in turn, nothing; nothing; and `.github/scripts/plugin_directory_check.py`'s `is_ancestor` alone, which *Scope* item 8 keeps. Run at `d0b15b72f` they print the lines of *Scope* item 9; the lines of `chain_check.py`, `pr_wait.py` and `settle.py` that *Scope* items 5 and 6 remove, the `pr_wait.py:55` docstring among them; and `chain_check.py#is_ancestor`, `settle.py#reaches` and the definitions of *Removes*' row of the repository's top and branch, beside `plugin_directory_check.py:191` |
| S12. `tag_release.py` loads no other script | Given the tree after the build | `git grep -n "publish_release_note" -- .github/scripts/tag_release.py` prints nothing. At `d0b15b72f` it prints `:61`, which *Scope* item 3 removes |

## Data & interfaces

**The runner's surface, in `lib/gitcmd.py`.** Standard library only and Python 3.9 syntax (G6).

| Name | What it is |
|---|---|
| `TIMEOUT` | 60, the seconds one git or `gh` command may take before it is no answer. The largest bound the tree held (G10), and far above every read measured here (G13) |
| `Failed` | A `SystemExit` whose code is its one line, so an uncaught one ends the process with that line on stderr at exit 1 (G4, G14). Its `command` names the program and the arguments the caller passed, without `argv`'s `-c` pairs or `-C <root>` |
| `Unrun(Failed)` | The command did not start, its program is not on `PATH`, or it did not finish within `TIMEOUT`. The line says which, with the bound in seconds |
| `Exited(Failed)` | A non-zero exit where the caller passed `check=True`. It carries `returncode` and `stderr`, and its line holds the code and the first line of `stderr` |
| `git(root, *args, given=None, binary=False, env=None, check=False)` | Starts `argv("-C", root, *args)` with `stdin` from `given`, text as UTF-8 with undecodable bytes replaced, or bytes where `binary` is true, and the variables of `env` added to the environment. Returns the `subprocess.CompletedProcess` and reads no exit code unless `check` is true, because for `merge-base --is-ancestor`, `diff --quiet`, `config --get` and `rev-parse --verify --quiet` exit 1 is an answer |
| `gh(*args, root=None, check=False)` | Starts the `gh` `shutil.which` finds, in `root`, under the same bound and the same text mode, and returns as `git` does |
| `is_ancestor(root, commit, ref)` | Whether `commit` is `ref` or reachable from it: `merge-base --is-ancestor`'s exit 0. Raises `Unrun` as `git` does |

**What each script reads of an unanswered command.** A reader with a documented default catches `Failed` at the call; a command whose error code is not 1 catches it in `main`; every other script lets it end the process with its line at exit 1.

| Where | Reading of `Failed` |
|---|---|
| `lib/optin.py#repo_root`, `#git_common_dir`; `lib/routing.py#current_branch`; `seal.py#git_asked`, `#staged_text`; `seal_stamp.py#_git`; `session_cost.py#run_gh`, `#run_git`; `chain_check.py#pull_request_from_gh`; `close_issues_on_release.py#attempt`; `roll_flow_measurement_issue.py#try_run`; `plugin_directory_check.py#is_ancestor`; `release_seal.py#gh`, `#tagged`; `tag_release.py#create`; `pr_wait.py#gh`, `#head`; `settle.py#ask_gh` | Each documented reading of a command that could not run, kept: `""`, `(None, why)`, `None`, `unknown`, `(False, line)`, `Refused`, an error string, `Unanswered`, `Unasked` |
| `seal.py#switch`, `#install_workflow`, `#remove_workflow` | The step's existing failure line, then exit 1 (*Scope* item 4) |
| `settle.py#main`, `chain_check.py#main`, `broad_gate.py#main`, `pact_check.py#main`, `test_layout.py#main` | One line, then exit 2 |
| Every other script that reaches the runner, `seal.py`'s other subcommands, `.github/scripts/` and `noninferiority.py` among them | The line at exit 1, which is what `sys.exit(f"... failed: ...")` gives these scripts now |

## Rule changes

- change
  file: docs/running/what-a-script-gates.md
  section: Which gate a script holds
  from: **A script reads git the same under any configuration: each git
    command a script under `lib/`, `skills/` or `.github/scripts/` starts
    whose subcommand `lib/gitcmd.py` names is built by its `argv`, and
    a script that takes a path out of output git quotes under
    `core.quotePath` asks for it with `-z`.**
  to: **A script reads git the same under any configuration: each git
    command a script under `lib/`, `skills/`, `.github/scripts/` or
    `evals/scripts/` starts is started by `lib/gitcmd.py#git`, which builds
    it with `argv`, and a script that takes a path out of output git quotes
    under `core.quotePath` asks for it with `-z`.**
- add
  file: docs/running/what-a-script-gates.md
  section: Which gate a script holds
  to: **A git or `gh` command that did not start, or did not finish within
    `lib/gitcmd.py#TIMEOUT`, is no answer, and no script reads it as one.**
    Each `gh` command a script starts is started by `lib/gitcmd.py#gh`
    under the same bound. Both runners raise `lib/gitcmd.py#Unrun`, whose
    one line names the command, and neither reads an exit code unless asked
    to, because for some commands, such as `merge-base --is-ancestor`,
    `diff --quiet` and `config --get`, exit 1 is an answer. `Unrun` is a
    `SystemExit`, as `lib/sibling.py#Absent` is, so a script that does not
    catch it ends with that line at exit 1 and never in a traceback. A
    reader whose unanswered question has a documented default, such as the
    *not opted in* of `lib/optin.py#repo_root`, catches it at the call, and
    a command whose error code is not 1 catches it in `main` and returns
    that code. A script that loads nothing from `lib/` at import names why
    in its docstring, as `.github/scripts/release_seal.py` does, and loads
    the runner at first use.
    check: tests/lib/test_gitcmd.py tests/skills/test_seal.py tests/skills/test_settle.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The process calls that start git or `gh` outside the runner | the calls G9 names as starting git or `gh`, and the call at `skills/code-review/scripts/chain_check.py:622`, by file in *Scope* items 2 and 4 to 8 | `lib/gitcmd.py#git` and `#gh` |
| The handlers of a timed-out process | the handlers of G10, at `lib/optin.py:104` and `:147`, `lib/routing.py:263`, `chain_check.py:636`, `pr_wait.py:191`, `seal.py:262`, `:1534`, `:1604`, `:1634` and `:2179`, `settle.py:434` and `pact_check.py:294` | `lib/gitcmd.py#Unrun`, read where each stood as *Data & interfaces* gives |
| Three bounds of a `gh` call and the bounds written at each git call | `chain_check.py#GH_TIMEOUT`, `pr_wait.py#GH_TIMEOUT`, `settle.py#GH_TIMEOUT`, and the `timeout=` arguments of G10 | `lib/gitcmd.py#TIMEOUT` |
| Four answers to whether one commit reaches another | `chain_check.py#is_ancestor`, `settle.py#reaches`, `rule_changes.py#_ancestor`'s process call, and the last step of `plugin_directory_check.py#is_ancestor` | `lib/gitcmd.py#is_ancestor` |
| Three readers of the repository's top and one of the branch | `broad_gate.py#repo_root`, `unverified_check.py#repo_root`, `test_layout.py#_toplevel`; `broad_gate.py#branch_name` | `lib/optin.py#toplevel` and `#repo_root`; `lib/routing.py#current_branch` (G15) |
| Two byte-for-byte copies of the closer's `run` | `.github/scripts/publish_release_note.py#run`, `.github/scripts/roll_flow_measurement_issue.py#run` | `lib/gitcmd.py#git` and `#gh` with `check=True`; the closer keeps its own (G19) |
| A second spelling of `git_asked` and of `touched` | the body of `seal.py#gitlinks_under_root`; the `diff-tree` call inside `chain_check.py#follows` | `seal.py#git_asked`; `chain_check.py#touched` |
| Two raw `ls-files -z` reads | `settle.py#tracked_names`, `#tracked_text` | `settle.py#git_fields` |
| `write_output` and the load of a script for it | `publish_release_note.py#write_output`; `tag_release.py:61` | `lib/console.py#write_output` |
| The open-coded path spelling | the lines *Scope* item 9 lists | `lib/gitcmd.py#git_path` |
| The pin of exit 0 for a stage git refused | `tests/skills/test_seal.py:2887`, `assert code == 0`, and `Test_mode::test_s6_a_switch_that_could_not_stage_names_agentic_seal_in_the_command` (`:3078` at d0b15b72f) | `code == 1` and no `Now commit.` (S3) |
| The case classes of the units that go | `Test_repo_root` in `tests/skills/test_unverified_check.py:412`; `Test_run` in `tests/github/test_roll_flow_measurement_issue.py:881` | What they hold that `Test_repo_root` and `Test_toplevel` in `tests/lib/test_optin.py` and `Test_git` and `Test_gh` in `tests/lib/test_gitcmd.py` do not hold already moves there |
| The sentence that names a timeout as one of `repo_root`'s empty answers | the comment in `seal.py#mode`'s `--check` branch, `:2444-2450` | A timeout reaches that branch no more (*Scope* item 4); the branch says what an empty `toplevel` is, a directory outside any repository |

Framed 2026-11-23 by framer, before the build.
