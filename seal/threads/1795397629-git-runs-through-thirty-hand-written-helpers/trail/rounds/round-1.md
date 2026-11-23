# Review round 1: 1795397629-git-runs-through-thirty-hand-written-helpers

```seal
target: 236289e3e6bf828c25d683745cb7aaa598c08a6c against origin/release/v0.38.6
```

This round reads the branch against its merge base `c3f568c6a`, which `origin/release/v0.38.6` names. No round ran before it, so nothing is carried from an earlier record and every fact below was established here. The installed plugin's `skills/code-review/SKILL.md` governed the two stages, and `seal/parity.json` is not declared, so no parity comparison applies.

The four findings share one cause and its effects. The build made `lib/gitcmd.py#Failed` a `SystemExit`, by design A4, and moved each script's exit-on-failure into a per-call `check=True`. Finding 1 is a handler written for `SystemExit` that now catches a git that did not answer and names it as something else. Finding 2 is three `check=True` flags that no case holds. Finding 3 is the frame left stating readings the build changed. Finding 4 is the pull request body, which does not say what a change to six gates must say.

## Findings

### 1. chain-check says the rule-changes reader would not load where a git read did not answer

```seal
severity: should
location: `skills/code-review/scripts/chain_check.py:1385-1402`, `tests/skills/test_chain_check.py:4039-4063`
evidence: executed `bin/test <scratchpad>/1795397629-git-runs-through-thirty-hand-written-helpers/round-1/test_tmp_round1.py -p no:xdist -q -s -W ignore`, and `git grep -nE "except[^:]*(SystemExit|BaseException|sibling\.Absent|\.Absent)|except:" -- lib skills .github/scripts evals/scripts hooks bin`
```

Why it matters: design S8 and *Data & interfaces* say that `chain-check` reads a git command past `lib/gitcmd.py#TIMEOUT` in `main`, writing `chain-check: ` and the runner's line at exit 2. The changelog repeats it: each of the five commands "now writes its name and the runner's line". One path does not. `rule_changes_of` (`chain_check.py:1394`) catches `(OSError, SyntaxError, ImportError, SystemExit)` around `rule_changes_read`, whose `read_record` asks `git show HEAD:<item>/frame/design.md` through `chain_check.py#git`. `Unrun` is a `SystemExit`, so the handler takes it and prints that a reader would not load. The probe made only that read time out over the S8 fixture branch. It printed `chain-check: the rule-changes reader would not load (`git show HEAD:seal/threads/1791999999-a-work-item/frame/design.md` did not finish within 60 seconds)` at exit 2, where S8's line is `chain-check: `git show HEAD:seal/threads/1791999999-a-work-item/frame/design.md` did not finish within 60 seconds`. A person who reads that line looks for a missing `skills/settle/scripts/rules.py` or `rule_changes.py`, and neither is missing. Before #1573 the same read raised `subprocess.TimeoutExpired`, which no clause of that handler caught, so the mislabel is new with `Failed`.

The S8 case does not see it. Its `read_record` row is `("show",)`, and `test_settle.py#unanswered` times out the first `git show` the run starts, so the row never reaches the read inside `rule_changes_of` unless that read is the first. Phase 4 records `tests/skills/test_chain_check.py` passing, and the probe shows that read giving another line, so the first `git show` is another read. This round read that and did not run the module. The class is every handler that catches `SystemExit` around a path that reaches the runner, and the `git grep` above lists every `SystemExit`, `BaseException` and bare handler under the four roots, `hooks/` and `bin/`: 14 handlers. Only `chain_check.py:1394` wraps a git read and names it otherwise. `chain_check.py:1151`, `:1618` and `:1782` wrap a module load alone. `broad_gate.py:1593`, `broad_gate.py:1599` and `release_seal.py:324` wrap a module load alone too. `release_seal.py:621` and `roll_flow_measurement_issue.py:561` read `Failed` as their documented failure on purpose. `hooks/core-start.py:64`, `seal.py:562`, `mutation_check.py:628`, `agentic_pytest_record.py:170` and `lib/sibling.py:126` re-raise or start no git. The fix pass owes the docstring of `rule_changes_of` as well, which the snippet rewrites.

```python
def rule_changes_of(reader, root, items, notices=None, sources=None):
    """[(path, line, problem)] from `rule_changes_read` over every work item
    directory of ITEMS, its notices going to NOTICES and what it reads of the
    tree to SOURCES, or None where a reader would not load or could not
    read, which is said on stderr. A git that did not answer
    (`lib/gitcmd.py#Failed`) is no reader that would not load: it reaches
    `main`, which names the command."""
    found = []
    try:
        for item in items:
            found.extend(rule_changes_read(reader, root, item, notices, sources))
    except GITCMD.Failed:
        raise
    except (OSError, SyntaxError, ImportError, SystemExit) as exc:
        print(
            f"chain-check: the rule-changes reader would not load ({exc})",
            file=sys.stderr,
        )
        return None
    except Unreadable as exc:
        print(f"chain-check: {exc}", file=sys.stderr)
        return None
    return found
```

The S8 case takes one more row, in `tests/skills/test_chain_check.py`, red against `chain_check.py` at the target:

```python
            ("diff-tree",),
            (f"HEAD:{ITEM}/frame/design.md",),
        ],
        ids=[
            # ... the nine ids as they stand ...
            "touched",
            "rule_changes_read",
        ],
```

### 2. Three check=True flags the build writes are held by no case

```seal
severity: should
location: `.github/scripts/roll_flow_measurement_issue.py:370`, `.github/scripts/roll_flow_measurement_issue.py:506`, `skills/verify/scripts/test_layout.py:1166`, `tests/github/test_roll_flow_measurement_issue.py:1138`, `tests/skills/test_test_layout.py:1203`, `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/gaps.md:23`
evidence: read `tests/github/test_roll_flow_measurement_issue.py:54-70`, `tests/github/test_roll_flow_measurement_issue.py:73-110`, `tests/github/test_roll_flow_measurement_issue.py:1138-1154`; executed `grep -n "gitcmd\.subprocess\|_run(monkeypatch\|close_issue\|open_issue" tests/github/test_roll_flow_measurement_issue.py`, and `python3 skills/verify/scripts/test_layout.py --check <scratchpad>/.../round-1/corrupt-index/tests` over a repository whose `.git/index` holds four junk bytes
```

Why it matters: before #1573 a failed `gh` or git call ended these runs because the helper that ran it always exited. After it, each call site carries its own `check=True`, and a flag dropped by a later edit reads a refusal as done. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* puts a call whose body and printed line change in the *Logic* row, so a case owes it. Phase 6 found two such flags unheld, `list_open_issues` and `publish_release_note.py#create`, and gave each a case after its mutant survived. Its mutation table broke the two writes the exactly-one-open invariant rests on only by swapping `gitcmd.gh` for `try_run` (`trail/phases/phase-6.md:73-74`), which a case catches because the swapped call reads another answer; no row takes `check=True` out of either. Phase 5 left the third in `gaps.md`.

- `roll_flow_measurement_issue.py#close_issue` (`:370`). Every case that reaches it goes through the test file's `_run`, whose `gh` returns exit 0 whatever `check` is (`:61-64`), and the one case that reaches the real runner is the list's (`:1138`). Without the flag, a close `gh` refused reads as done, and `main` opens a second log while the first stays open.
- The last create rung of `open_issue` (`:506`). The same `_run` answers it, and the `fatal` case at `:544` raises from the double, not from the flag. Without the flag, a refused create returns the title, and the run prints `rolled:` with no log open.
- `test_layout.py#_tracked` (`:1166`). `gaps.md:23` says no case needs it because "no reading this work changes depends on it". The reading did change: at `d0b15b72f` a non-zero `ls-files` ended `seal layout` in a `CalledProcessError` traceback at exit 1. At the target it ends at exit 2 with `seal layout: `git ls-files -z` exited 128: fatal: .git/index: index file smaller than expected`, which the run above printed, and the module docstring (`test_layout.py:134-137`) now promises it. Without the flag, `_tracked` reads the refusal as a repository holding no tracked file. `gaps.md:23` also says the fixture is hard to build. Four junk bytes written to `.git/index` build it.

The list of `check=True` sites came from `git grep -n "check=True"` over the four roots: the closer's `run`, `publish_release_note.py#git` and `#create`, `list_open_issues`, `close_issue`, the last create rung, `noninferiority.py#git_bytes`, `rule_changes.py#order` and `#merge_order`, and `_tracked`. The phase records show each of the others red on a mutant. The fix pass closes the `gaps.md:23` paragraph with the case.

```python
# tests/github/test_roll_flow_measurement_issue.py, beside
# test_a_list_gh_refuses_stops_the_release_in_the_runners_line
    @pytest.mark.parametrize("write", ["close", "the last create rung"])
    def test_a_close_or_the_last_create_gh_refuses_stops_the_release(
        self, monkeypatch, write
    ):
        """A refused close read as done opens a second log beside the one
        still open, and a refused last create read as done ends the roll with
        none open. Each passes `check=True`, so the refusal ends the run in
        `lib/gitcmd.py#Exited`'s line (#1573)."""
        m = _roller()
        if write == "the last create rung":
            _ladder_harness(m, monkeypatch, [None, None], [])
        monkeypatch.setattr(
            m.gitcmd.subprocess,
            "run",
            lambda argv, **_: subprocess.CompletedProcess(argv, 1, "", "HTTP 502\n"),
        )
        with pytest.raises(SystemExit) as stopped:
            if write == "close":
                m.close_issue("example/repo", 89, "0.8.2")
            else:
                m.open_issue("example/repo", "0.8.2", 89)
        assert str(stopped.value.code).endswith(" exited 1: HTTP 502")


# tests/skills/test_test_layout.py, in Test_main
    def test_refuses_a_listing_git_refused_in_one_line(
        self, tmp_path, monkeypatch, capsys
    ):
        """#1573: `_tracked` passes `check=True`, so a `git ls-files` that
        exits non-zero, here over an index git cannot read, is exit 2 in
        `lib/gitcmd.py#Exited`'s line, and not a repository read as holding
        no tracked file."""
        git_out(tmp_path, "init", "-q")
        write(tmp_path, "tests/test_x.py", PLACED)
        (tmp_path / ".git" / "index").write_bytes(b"junk")
        monkeypatch.chdir(tmp_path)
        assert layout.main(["--check"]) == 2
        out = capsys.readouterr().out
        assert out.startswith("seal layout: `git ls-files -z` exited "), out
```

### 3. The frame still states readings the build replaced

```seal
severity: should
location: `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md:115`, `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md:117`, `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md:58`, `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/questions.md:18`
evidence: read `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md:56`, `:115`, `:117`, `skills/verify/scripts/seal_stamp.py:1005-1016`, `skills/verify/scripts/seal_stamp.py:1546-1551`; executed `git show 87c10c522 -- seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/design.md` and `grep -n "^def _git\|_git(" skills/verify/scripts/test_layout.py`, which prints nothing
```

Why it matters: the sealer reads `frame/design.md` *Data & interfaces* as the statement of what each script does with a git that did not answer, and the pull request body carries `frame/questions.md` as written. Three sentences there say what the target does not do.

- `design.md:115` lists `seal_stamp.py#_git` among the readers that catch `Failed` and keep a documented reading. At the target `_git` lets it propagate (`seal_stamp.py:1005-1016`) and `main` returns 2 (`:1549-1551`). Phase 5 named both coordinates as its departure: "Design *Scope* item 7 and *Data & interfaces*' first row read `Failed` as `None` there". The fold at `87c10c522` rewrote *Scope* item 7 (`design.md:56`) and left the row, so the design now states the reading twice and two ways. `design.md:117`, the exit-2 row, does not name `seal_stamp.py#main` either.
- `design.md:58` says `test_layout.py#_git` runs through `gitcmd.git`. The target has no `_git`: its calls ask `gitcmd.git` directly.
- `questions.md:18` holds Q2 at `open`. Each of the six phase records answers it for its scripts under the heading *`frame/questions.md` Q2, answered by the work for phase N*, and the pull request body prints the row as open.

```markdown
<!-- frame/design.md:115, the first row of *Data & interfaces* -->
| `lib/optin.py#repo_root`, `#git_common_dir`; `lib/routing.py#current_branch`; `seal.py#git_asked`, `#staged_text`; `session_cost.py#run_gh`, `#run_git`; `chain_check.py#pull_request_from_gh`; `close_issues_on_release.py#attempt`; `roll_flow_measurement_issue.py#try_run`; `plugin_directory_check.py#is_ancestor`; `release_seal.py#gh`, `#tagged`; `tag_release.py#create`; `pr_wait.py#gh`, `#head`; `settle.py#ask_gh` | Each documented reading of a command that could not run, kept: `""`, `(None, why)`, `None`, `unknown`, `(False, line)`, `Refused`, an error string, `Unanswered`, `Unasked` |

<!-- frame/design.md:117 -->
| `settle.py#main`, `chain_check.py#main`, `broad_gate.py#main`, `pact_check.py#main`, `test_layout.py#main`, `seal_stamp.py#main` under `--guarantee` | One line, then exit 2 |

<!-- frame/design.md:58 -->
   - `test_layout.py`'s git reads run through `gitcmd.git`, and `_git` goes; `_tracked` asks with `check=True`. `_toplevel` goes, for `optin.toplevel`. `main` catches `Failed` and returns 2.

<!-- frame/questions.md:18, the Status cell of Q2 -->
answered 2026-11-23 by the work: each phase's ruling, in `trail/phases/phase-1.md` to `phase-6.md`
```

### 4. The pull request body does not say what a change to six gates must carry

```seal
severity: must
location: `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/pr.md:1`, `seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers/frame/plan.md:71`
evidence: read `CONTRIBUTING.md:373-405`, `CLAUDE.md`; executed `bin/seal pr-body seal/threads/1795397629-git-runs-through-thirty-hand-written-helpers --body <scratchpad>/.../round-1/body.md` and a search of the 101 lines it wrote for `direction` and `prompt`, which found neither
```

Why it matters: this repository's `CLAUDE.md` names `CONTRIBUTING.md` *What a change to a gate must carry* as the place a pull request here answers `skills/core/SKILL.md` *The rule a mechanism is kept against*. That section asks the pull request to say whether the change makes a gate block more or allow more and why that direction is the cheaper mistake, and to give a prompt budget. This work changes what `seal settle`, `chain-check`, `seal gate`, `seal pact`, `seal layout` and `seal stamp --guarantee` refuse, and the exit code of `seal mode`. The body `seal pr-body` composes at the target carries the changelog, the phases, `gaps.md` and the questions, and states neither the failure direction nor the prompt budget. Platform honesty is carried by the Windows rows of `gaps.md` *Not verified*, and what the change removes by the changelog's *Removed*. `seal/threads/1794383425-a-committed-durations-file-turns-ci-red/pr.md` quotes such a row from its plan, and this work item has none to quote. The direction below is this round's reading of the target, and the orchestrator owns the row.

```markdown
<!-- frame/plan.md, a row of *Judgments of the run* -->
| 2026-11-23 | What this change to the gates carries: its failure direction is block more, and its prompt budget is zero | `seal settle`, `chain-check`, `seal gate`, `seal pact`, `seal layout` and `seal stamp --guarantee` now refuse at exit 2, and `seal mode` at exit 1, where a git or `gh` command that did not answer was read as an answer or held the run without end. A wrong deny fires only on a command past `lib/gitcmd.py#TIMEOUT` and costs one run again once git answers; a wrong allow passes a gate on a reading git never gave. No step asks a person anything. The platforms not run are the Windows rows of `gaps.md` *Not verified*, and the runner replaces the helpers the changelog's *Removed* names, adding no mechanism | `CONTRIBUTING.md` *What a change to a gate must carry* |

<!-- pr.md, a line after the first -->
- "What this change to the gates carries: its failure direction is block more, and its prompt budget is zero" (`frame/plan.md` *Judgments of the run*, the row on what a gate change carries)
```

## Confirmations

What matched, executed at the target: design S10's two searches print `noninferiority.py:401`, `seal.py:2508`, `broad_gate.py:681`, `:699`, `:943`, `:2243`, `mutation_check.py:405` and `test_layout.py:1042`, and nothing; S11's three print nothing, nothing and `plugin_directory_check.py:191`; S12 prints nothing. The phase 5 and phase 6 records claimed these lines, and they hold. A wider search for every way a script starts a process (`import subprocess`, `os.system`, `os.popen`, `os.exec`, `os.spawn`, `create_subprocess`, `getoutput`) over the four roots, `hooks/` and `bin/` adds only `seal.py:2511`, `hand_over`'s `os.execv`, which starts no git. The release scripts that start `gh` without importing the runner, `label_merged_on_release_branch.py`, `release_completeness_check.py` and `tracker_labels.py`, each go through the closer's `run`.

What matched, read at the target: `lib/gitcmd.py:106-213` is the surface design *Data & interfaces* gives, with `Failed` a `SystemExit` whose code is its line, and `lib/sibling.py#load` registers a module by its stem, so `lib/optin.py`'s bare `import gitcmd` and every script's `sibling.load("lib/gitcmd.py")` are one module and one `Failed` class. `seal.py#switch` returns 1 before `Now commit.` on every stage step that did not happen (`seal.py:2334-2385`). `settle.py#apply` classifies every directory before its first `shutil.rmtree` (`settle.py:1962-2030`), and nothing after the removals starts git, since `fold_check.py` starts no process; so `main`'s exit 2 on `Failed` never follows a removal. `seal_stamp.py --stop` reaches only `lib/optin.py#git_common_dir`, which reads `Failed` as `""`, so the `Stop` hook still exits 0.

What matched, executed: `bin/test -q tests/lib/test_gitcmd.py tests/lib/test_optin.py tests/lib/test_routing.py tests/lib/test_console.py tests/skills/test_test_layout.py` gave 259 passed. `bin/seal layout --check` over the four `tests/lib/` files refused nothing. `bin/seal layout --pairs` over the 24 changed test files printed 121 pairs. The pairs this branch adds, `Test_try_run`, `Test_write_output` and `pr_wait.py`'s `Test_gh`, are each one call in two worlds, an accepting and a refusing case, so none covers only what its group covers. The installed chain check over the working tree (`--worktree`) printed no notice at `frame/design.md` naming a test pin or a copy, so no finding comes from one.

`gaps.md` *Not done* holds four items, where the spawn named three. Three of them stand as the round reads them, since none is a behaviour the build changed. `write_mode`'s exit 0 is a file write, not a git command, and the orchestrator kept it out with grounds in `frame/plan.md:70`. The `--literal-pathspecs` of `settle.py#git_run` (`gaps.md:19`) and the URL of `close_issues_on_release.py#_issue_api` (`gaps.md:21`) were carried over literally from the old argv, and no case held either at `d0b15b72f`, so each is a gap of code the diff did not change and owes no case here. The fourth, `_tracked`'s flag, is finding 2. The suite label is honest: phase 6 hands over the suite, the lint and the typecheck as `unverified`, and phases 1 to 5 claim only their boundary sets.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite, the lint and the typecheck over the whole tree, which this round did not run (contract rule 2) | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run after the rounds settle |
| Whether the hooks' git reads may now wait 60 s, where they waited 5 s. The `SessionStart` hook asks `lib/optin.py#repo_root` and the `Stop` hook may ask `#git_common_dir`. `frame/plan.md` *Operational impact* names the move, and no frame line weighs a hook that holds a session's start | `lib/optin.py:98`, `lib/optin.py:141`, `hooks/core-start.py:38-44` | the orchestrator, against `frame/plan.md` A6 |
| Whether the network commands now under `TIMEOUT` finish within it on the release workflow: `dist_branch.py`'s `ls-remote`, `fetch` and `push`, `publish_release_note.py#create`'s `gh release create`, and `release_seal.py`'s `gh` upload. Design G13 measured local reads, and `frame/questions.md` Q1 asks about the suite's cases alone | `.github/scripts/dist_branch.py:126-164`, `.github/scripts/publish_release_note.py:836-848` | the orchestrator, from the first release run after the merge |
| Whether the bound holds on Windows. CPython's `subprocess.run` calls `communicate()` after it kills a process that timed out on Windows, and a launcher `git.exe` whose child keeps the pipes open can hold that call past `TIMEOUT`. Every case raises `TimeoutExpired` from a double, so no run has shown the bound on a real hang there (contract rule 13) | `lib/gitcmd.py:155-167` | a measurement on a Windows machine, named by the orchestrator |
| Whether `chain_check.py#declared_for_this_branch` should ask the branch through a reader that raises. `lib/routing.py#current_branch` reads `Failed` as `""` by design *Scope* item 2, and outside a workflow the check then says the branch "could not be read — a detached HEAD", which is false for a git that did not answer. The declaration the branch adds is still judged through `changed_routing` | `skills/code-review/scripts/chain_check.py:1897-1902` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test <scratchpad>/1795397629-git-runs-through-thirty-hand-written-helpers/round-1/test_tmp_round1.py -p no:xdist -q -s -W ignore` | One case over `tests/skills/test_chain_check.py`'s `branch` fixture, with only `git show HEAD:<ITEM>/frame/design.md` raising `TimeoutExpired`: one call matched, exit 2, stderr `chain-check: the rule-changes reader would not load (`git show HEAD:seal/threads/1791999999-a-work-item/frame/design.md` did not finish within 60 seconds)`. It ran three times: the first two runs piped the output through `tail -30`, which cut the printed lines under the warnings, and the third saved them whole to `probe-out.txt` |
| `git init`, `git add`, four junk bytes to `.git/index`, then `git -C <repo> rev-parse --show-toplevel`, `git -C <repo> ls-files -z` and `python3 skills/verify/scripts/test_layout.py --check <repo>/tests`, in `<scratchpad>/.../round-1/corrupt-index` | `rev-parse` exit 0, `ls-files` exit 128 with `fatal: .git/index: index file smaller than expected`, and `seal layout` exit 2 printing `seal layout: `git ls-files -z` exited 128: fatal: .git/index: index file smaller than expected` |
