# Review round 1: 1794178394-each-run-reaches-the-tree-wide-guards

```seal
target: 39de4f09 against release/v0.36.0
```

The base is `release/v0.36.0` at `94d04d30` (executed: `git log --oneline 94d04d30..39de4f09` lists the 15 commits of the branch). This is a finding round over the whole branch. No earlier round exists, so this round carried no fact and re-established every one it uses. `seal/parity.md` is absent, so no parity comparison applies. `seal/config.md` has no `Record language` row and no `Pact` row, so the record is English and no pact anchor is read.

The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` whole at `39de4f09`, and issue #1441 with its one comment (executed: `gh issue view 1441 --json body,comments`). The comment records that the body's #717 citation was corrected after the frame. The design's *Grounding* rows on the ticket's comments and on #717 are dated to the framer's read at `94d04d30`, so the comment does not contradict them.

## Findings

### 1. Phase 2's measured "new row's set" for #1421 leaves out four test files that read this repository's own `.claude-plugin/plugin.json`

```seal
severity: should
location: `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/trail/phases/phase-2.md:134-165`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/questions.md:16`
evidence: read `tests/github/test_plugin_directory_check.py:283`, `tests/github/test_plugin_directory_check.py:319`, `tests/github/test_plugin_directory_check.py:482`, `.github/scripts/plugin_directory_check.py:150-155`, `tests/github/test_release_seal.py:1007-1011`, `.github/scripts/release_seal.py:479`, `tests/lib/test_core.py:239-245`, `lib/core.py:68-76`, `lib/core.py:106-121`, `tests/hooks/test_core_start.py:40-55`, `tests/hooks/test_core_start.py:80-83`, `tests/hooks/test_core_start.py:171`; executed `git grep -n -E '"--root", (str\()?ROOT|\(ROOT\)|, ROOT\)|\[ROOT\]|cwd=(str\()?ROOT|root=ROOT' -- 'tests/*.py' ':!tests/text' ':!tests/behaviour'` in the clone at `39de4f09`
```

Why it matters: phase 2 claimed, for *Scope* item 7's second set, "Outside the two directories, no test file reads this repository's own `.claude-plugin/plugin.json`". It listed `tests/github/test_plugin_directory_check.py`, `tests/github/test_release_seal.py`, `tests/lib/test_core.py` and `tests/hooks/test_core_start.py` among the files that "write a manifest of that name into a fixture, or name it in a message" (`phase-2.md:134-148`). Each of the four opens the real manifest under `ROOT`, which is the row's own definition of reading a path:

- `tests/github/test_plugin_directory_check.py:283` and `:319` call `mod.main(["--root", ROOT])`, and `:482` calls `mod.plugin_name(ROOT)`. `plugin_name` opens `<root>/.claude-plugin/plugin.json` (`.github/scripts/plugin_directory_check.py:150-155`).
- `tests/github/test_release_seal.py:1007-1011` sets the module's `ROOT` back to the repository and calls `draw`, which opens `ROOT/.claude-plugin/plugin.json` for the icon (`.github/scripts/release_seal.py:479`).
- `tests/lib/test_core.py:239-245` calls `core.origin(ROOT, ROOT)` and `core.rendered(path, ROOT)`. `rendered` reads the version from `manifest(plugin_root)` into the header (`lib/core.py:106-121`, `lib/core.py:68-76`). The case asserts the output stays under `CAP`, so a version move can change its result.
- `tests/hooks/test_core_start.py:171` compares the hook's output with `printed(str(repo), ROOT)`, which is `core.rendered(..., ROOT)` (`:80-83`). The hook runs from `ROOT` by default (`:40-55`) and reads the same manifest.

#1421's changed paths include `.claude-plugin/plugin.json`. So the timed second set, 90 files, 2,119 passed, 17.73 s, is not the set the new `Phase boundary` row names for #1421's change. `frame/questions.md:16` Q2's Status quotes that set as "the new row's set, 90 files". This is also the first worked example of the row's third part, and its record hands the part back as a whole list after reading each match by eye. A crafter or a settle that reads this record takes the judgment as shown to work on the very path that missed. That is contract rule 12's finding on the method: a sample was handed back as a whole list.

The four were found by searching for `ROOT` passed whole. That search is itself a sample over spellings: a case that reaches the manifest through a helper's default root, as `start(..., where=ROOT)` in `tests/hooks/test_core_start.py` does, is found only where it also passes `ROOT` whole. The fix pass owes its own reading of each file the part-3 list left out, not just these four.

The fix rewrites the part-3 sentence and the set's command and counts in `phase-2.md`, and re-runs the second set once with the files added. The sentence at `phase-2.md:159-165` comparing the two sets, and `frame/questions.md:16` Q2's Status, take the new counts. `questions.md` is a frame file, so the orchestrator's fold rewrites it.

```markdown
3. The test files that read a changed path: `tests/evals/test_rule_cases.py`
   and `tests/evals/test_seed_defects.py`, by the reading above. Outside
   the two directories, four test files read this repository's own
   `.claude-plugin/plugin.json` under `ROOT`:
   `tests/github/test_plugin_directory_check.py` (`main` and `plugin_name`
   over `ROOT`), `tests/github/test_release_seal.py` (`draw` with `ROOT`
   restored), `tests/lib/test_core.py` (`core.rendered` reads the version
   into the header) and `tests/hooks/test_core_start.py` (`printed` over
   `ROOT`). `tests/github/test_tag_release.py`,
   `tests/github/test_roll_flow_measurement_issue.py`,
   `tests/github/test_release_completeness_check.py`,
   `tests/skills/test_broad_gate.py`, `tests/skills/test_pr_body.py`,
   `tests/skills/test_seal.py` and `tests/skills/test_payload_meter.py`
   write a manifest of that name into a fixture, or name it in a message,
   and were left out.

- Command: `bin/test tests/text tests/behaviour
  tests/evals/test_noninferiority.py tests/evals/test_rule_cases.py
  tests/evals/test_seed_defects.py tests/github/test_plugin_directory_check.py
  tests/github/test_release_seal.py tests/lib/test_core.py
  tests/hooks/test_core_start.py -q`.
- The file count, the passed and skipped counts, the exit code and the
  wall-clock seconds, as that one run prints them.
```

The fix pass writes the last bullet's figures from its own run.

```seal
verdict: fixed 4ad34865
answer: The finding holds, and the miss was wider than four. The fix pass re-read the eleven files phase 2's record set aside from part 3, a closed set, by an audit-hook probe on PYTHONPATH that logged each open of the real `.claude-plugin/plugin.json` with the running case (executed), and by reading the four it did not log at the calls that reach a manifest. Seven files read the manifest: the four the finding names, and `tests/skills/test_broad_gate.py` (nine cases, `plugin_version`), `tests/skills/test_pr_body.py` (`Test_seal_mark::test_accepts_the_plugins_own_manifest`) and `tests/skills/test_seal.py` (24 cases that read the version for the workflow's pin). `test_tag_release.py`, `test_roll_flow_measurement_issue.py`, `test_payload_meter.py` and `test_release_completeness_check.py` stay out. `trail/phases/phase-2.md` *Scope item 7* names the seven, the method and its limit, and the corrected set ran once at `69f00945`: 97 files, 2,995 passed, 10 skipped, exit 0, 24.84 s, with the #1421 set's 70.14 s reading kept and its conditions named. The paste-ready text was not applied as given, since it listed three readers as fixture writers. The same probe over the phase boundary's own set-aside list logged no read of the three documents phase 2 changed. `frame/questions.md:16` is the orchestrator's to fold.
```

### 2. "A case that reads this repository's own tree beyond its `TARGET`" has two readings, and under the wider one cases the build rightly left stand against it

```seal
severity: should
location: `CONTRIBUTING.md:272-274`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/changelog.md:4`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/pr.md:4`
evidence: read `CONTRIBUTING.md:268-277`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:7`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:34`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:49`, `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/trail/phases/phase-2.md:44-50`, `tests/skills/test_chain_check.py:4231-4272`, `tests/lib/test_core.py:232-245`, `tests/github/test_plugin_directory_check.py:283`
```

Why it matters: the sentence the build added to `CONTRIBUTING.md` *The test layout* reads "A case that reads this repository's own tree beyond its `TARGET` stands in a file that declares none." The frame defines the class it means as cases that hold "the whole tree, or a whole directory of it, to a rule" (`frame/design.md:7`). *Scope* item 1 says the same as a case that "walks a directory of the repository root, lists its tracked files, or runs a check over the root" (`frame/design.md:34`). The sentence says neither. Read plainly, a case that opens one named file of the tree beyond its `TARGET` reads the tree beyond its `TARGET`. Such cases stand in `TARGET` files at the target, and phase 2 judged that right: `tests/skills/test_chain_check.py:4231-4272` reads `agents/proofer.md` and `skills/code-review/SKILL.md` under `ROOT` (`phase-2.md:44-50`). So do `tests/lib/test_core.py:232-245`, which reads the tree's core and manifest, and `tests/github/test_plugin_directory_check.py:283`.

This paragraph is the one the frame names as the proofer's reference for where a new tree-wide case stands, with no check behind it (`frame/design.md:49`). A proofer that takes the wider reading asks every such case to move. A proofer that takes the narrower one passes them. The sentence an agent reads at that step has two readings, which `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* forbids. The changelog's second item repeats the phrase as "every case that reads the repository's own tree stands in one of them" (`changelog.md:4`). Under the wider reading that is false at the target, and `pr.md:4` quotes it. The release note and the pull request body carry whichever sentence the changelog ends with.

The snippet rewrites the `CONTRIBUTING.md` sentence in *Scope* item 1's terms. The changelog's bold sentence takes the same terms, and `pr.md:4`'s quote follows the changelog word for word. `pr.md` is the orchestrator's, so the fix pass names it in its hand-back.

```markdown
**A test file that declares no `TARGET` stands by what its cases run.** It
stands in `tests/behaviour/` where its cases load or run shipped code, and
in `tests/text/` where they only read text. A case that walks this
repository's tree or a whole directory of it, lists its tracked files, or
runs a check over its root stands in a file that declares none. The files
that declare no `TARGET`, `tests/text/` and `tests/behaviour/`, are this
repository's tree-wide files, which `skills/verify/SKILL.md` *Scope: cheap
and often, broad and once* runs at every phase boundary and every fix pass.
```

```markdown
- **This repository's tree-wide test files are `tests/text/` and `tests/behaviour/`, the files that declare no `TARGET`, and every case that walks the repository's own tree, lists its tracked files or runs a check over its root stands in one of them.**
```

```seal
verdict: fixed abde6b8c
answer: The finding holds. `abde6b8c` rewrites the `CONTRIBUTING.md` sentence to the paste-ready text, the frame's class of a case that walks the tree or a whole directory of it, lists its tracked files, or runs a check over its root, and `69f00945` rewraps the paragraph after `tests/behaviour/test_docs_line_wrap.py` refused a 117-column line. The changelog's bold sentence takes the same terms with "or a whole directory of it" kept, so it reads "every case that walks the repository's own tree or a whole directory of it, lists its tracked files or runs a check over its root stands in one of them". `pr.md:4` quotes the old sentence and is the orchestrator's to update, and so is `frame/design.md:35`, *Scope* item 2, which states the old phrase.
```

## Confirmations

What matched: *Scope* item 1. The fourteen cases moved with their bodies unchanged. Executed in the clone at `39de4f09`: `bin/seal layout --moved 94d04d30 --from <the ten old files> --to <the ten old files> <the five new files>` exited 0, and its last line was `seal layout: moved: 432 old cases, 877 items against 877 at 94d04d300622, 0 failed`. `bin/test` over the five new files passed 14 at exit 0, and `bin/seal layout --check` exited 0 with `139 files read, 0 refused, 87 declare no TARGET`. `tests/skills/test_fold_check.py`'s renamed accepting case keeps its body (read, `git diff 94d04d30 39de4f09 -- tests/skills/test_fold_check.py`). The branch adds no test case written new, so no case was read against a group for duplication. Each case in the five files is a moved one.

What matched: *Scope* items 3 and 4. `skills/verify/SKILL.md:144` gives the `Phase boundary` row's four parts, `:146` gives the `Review rounds 1..n` row as that set drawn over the fix's paths, `:152-159` define reading a path, and `:161-165` give the contribution guide's tree-wide files with the glob fallback (read). `git grep -n -i -E 'glob the directory|whether they name it|what the fix touches|test modules that read a path'` over the tree outside `seal/threads/` returns none of the old wording (executed).

What matched: *Scope* item 5. `agents/crafter.md:62-66` (step 9) runs the `Review rounds 1..n` set as one command through the runner once the fixes are committed, before the close blocks. That agrees with the order *A fix pass appends close blocks and writes no phase record* gives at `agents/crafter.md:210-216` (read).

What matched: *Scope* item 6 at `CONTRIBUTING.md:42-44`, and *Scope* item 2's clause at `CONTRIBUTING.md:275-277`, which phase 1 deferred and phase 2 added (read). The phrase defect in the paragraph's other sentence is finding 2.

What matched: the citations the move changed. `lib/launch.py:27`, `ruff.toml:38-40`, `.github/workflows/hygiene.yml:168-169`, `tests/censuses.py:7-9`, `tests/censuses.py:899`, `CONTRIBUTING.md:124-126`, `CONTRIBUTING.md:268` and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:64-70` name the new homes (read). The remaining `check:` lines that name an old file name rules its remaining unit cases still hold: `CONTRIBUTING.md:259`, `docs/running/the-broad-gate.md:172`, `docs/layout/the-record-layout.md:30`, `docs/running/the-agent-set.md:153`, `docs/releasing/release-checklist.md:187`, `skills/settle/rule-changes.md:131`, `skills/writing-style/SKILL.md:267`, `docs/running/what-a-script-gates.md:22`, `docs/checks/the-fold.md:102` and `docs/running/the-review-and-parity-arms.md:111` (read, each at its rule). The design's `## Rule changes` `from` stands word for word at `docs/running/what-a-script-gates.md:60` (read). `chain_check.py` printed no notice at `frame/design.md` (executed, the run below).

What matched: `gaps.md:8`, the question whether a test file outside `tests/text/` and `tests/behaviour/` reads `skills/verify/SKILL.md`, `agents/crafter.md` or `CONTRIBUTING.md`. A `git grep` for the three paths and their path parts outside the two directories found only names in docstrings, fixtures and parameters. `tests/skills/test_passages.py:33-45` passes two of them to `passages.in_corpus`, which opens no file (`skills/settle/scripts/passages.py:52-61`). A second `git grep` for `ROOT` passed whole found no case that reaches the three through a shipped script: of the scripts that open them, `.github/scripts/rules.py` and `.github/scripts/release_report.py` run over the tree only in the moved cases. Executed and read. The two searches are a sample over spellings, and a case that reaches one of the three by a route neither search names is the part they did not reach.

What matched: `gaps.md:9`, the question whether a case that takes a temporary directory still reads the tree through a command's default root. The four shipped commands whose `--root` defaults to the plugin's own tree are `finding_counts.py`, `plugin_directory_check.py`, `release_report.py` and `payload_meter.py`. Each call of them in a case that takes a temporary directory passes `--root`, or exits on argument parsing first (read). The probe below listed 264 calls with no `--root` and no `cwd=` in such cases. The hits in the files of commands whose root defaults to the working directory (`rules.py`, `test_layout.py`, `settle.py`, `deferral_check.py`, `unverified_check.py`, `mutation_check.py`) each `chdir` into the fixture, patch `_toplevel`, or pass the fixture as a positional root (read). The probe's filter is a sample. It drops any call whose text names `tmp`, `root` or `repo`, and it reads only calls named `run`, `main`, `check_output`, `call` or `Popen`.

What matched: `pr.md`'s six quotes, each found word for word at the coordinate it names (read).

What matched: the release context. The branch does not touch `.test_durations` or the `.test_durations` paragraph of `CONTRIBUTING.md`, and it does not move the version (executed, `git diff --stat 94d04d30 39de4f09`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `39de4f09`; `gaps.md:7` labels them `unverified`, and the label is honest, since neither phase claims a broad run | the branch at `39de4f09` | the orchestrator, at the broad gate |
| Whether the two timed runs of *Scope* item 7 compare like with like, since each is one run on a machine under the load of the release's other sessions (`phase-2.md:109-113`, `:191-199`) | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/trail/phases/phase-2.md` | the orchestrator, where it weighs the measurement for done-when 2 |
| Where the glob clause came from; the frame labels it `unverified` as history (`frame/design.md:28`) | `seal/threads/1794178394-each-run-reaches-the-tree-wide-guards/frame/design.md:28` | the owner |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the five new files under `tests/behaviour/`, in the clone at `39de4f09` | exit 0, 14 passed |
| `bin/seal layout --moved 94d04d30 --from <the ten old files> --to <the ten old files> <the five new files>` | exit 0; `seal layout: moved: 432 old cases, 877 items against 877 at 94d04d300622, 0 failed` |
| `bin/seal layout --check` | exit 0; `seal layout: 139 files read, 0 refused, 87 declare no TARGET` |
| `python3 test_tmp_default_root.py <clone>`, an `ast` walk of each case outside `tests/text/` and `tests/behaviour/` that takes `tmp_path`, `tmpdir` or `tmp_path_factory`, listing its calls named `run`, `main`, `check_output`, `call` or `Popen` with no `--root`, no `cwd=` and no `tmp`, `root` or `repo` in the call's text | exit 0, 264 calls listed; those in the test files of commands with a default root were read by hand, and none reaches this repository's tree; the file was deleted after its one run |
| `python3 skills/code-review/scripts/chain_check.py --baseline 94d04d30 --root <the branch worktree> --worktree`, before this record | exit 0; the refusals named no round record, no gate record and no guarantee, which the round, the broad run and the sealer each write |
