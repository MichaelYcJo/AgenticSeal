# Review round 1: 1795759277-scripts-read-git-past-submodule-settings-and-a-floor

```seal
target: 851641519 against origin/release/v0.39.3
```

This is the work item's first round, so no earlier round carries a coordinate or a verdict. The round read `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md` and `trail/phases/phase-2.md` whole at `851641519`. The record language and the commit language are both English, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared, so no parity comparison is owed. The diff read is `origin/release/v0.39.3...851641519`, whose merge base is the base's tip `86f98018c`: `lib/gitcmd.py`, `skills/implement/scripts/range_read.py`, both README editions, `tests/conftest.py`, and the cases in `tests/lib/test_gitcmd.py`, `tests/skills/test_range_read.py`, `tests/skills/test_seal.py`, `tests/skills/test_settle.py` and `tests/behaviour/test_release_hygiene.py`. The issues were read with `gh issue view 1640 --json body,comments` and `gh issue view 1642 --json body,comments`. Neither has a comment, and #1642's body carries the note of its 2026-11-27 correction from 2.24 to 2.30. The probes ran in a `git clone --no-local` of the branch at `851641519` under the round's scratch directory, and nothing was changed in the branch's worktree but this record.

## Findings

### 1. The sealer's step 1 lists what followed the gate's run with a bare `git log --name-only`, which a `.gitmodules` `ignore` shortens, so it and `chain_check.py#follows` now read a pointer-only commit differently

```seal
severity: should
location: `agents/sealer.md:57`, `tests/behaviour/test_the_sealer_guarantees.py:164`
evidence: executed `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py -q` in the round's clone (104 passed, the `log-gitmodules` parameter of `test_refuses_a_submodule_left_out_by_a_setting_no_key_reaches` among them, whose bare assertion holds that `log --name-only` leaves `sub` out under the `.gitmodules` entry); executed `git grep -n -F 'log --no-merges --name-only' -- .` and `git grep -n -E '(log|diff|status|diff-tree) [^`]*--(name-only|name-status|porcelain|stat|raw)' -- agents skills docs CONTRIBUTING.md templates ':!*.py'`; read `agents/sealer.md:54-66`, `skills/code-review/scripts/chain_check.py:999-1004`, `skills/core/SKILL.md:114`, `frame/design.md:12`
```

Why it matters: `skills/core/SKILL.md:114` gives the invariant *No seal without the broad run* to `agents/sealer.md` step 1 and the chain check's broad gate arm. Before the pull request, and in local mode, step 1 holds it alone. Step 1 tells the sealer to run `git -C <root> log --no-merges --name-only <named>..HEAD ^<base>` (`agents/sealer.md:57`), and says "the rule it applies is the one `skills/code-review/scripts/chain_check.py#follows` reads". After this work the two reads differ in a repository whose `.gitmodules` entry reads `ignore = all`. `follows` reads through `chain_check.py#touched`, whose `diff-tree` now carries `--ignore-submodules=none` from `lib/gitcmd.py#FLAGS`. `records_only` (`chain_check.py:999-1004`) reads a commit that moved only the submodule's pointer as changing a path outside the records, and refuses it. The sealer's own command carries no flag, because an agent's command does not pass through `lib/gitcmd.py#argv`. Under the same entry it lists that commit with no path at all, as the `log-gitmodules` parameter's bare assertion shows. Step 1's branches are "followed only by paths under `seal/threads/<item>/`" and "followed by any other path". A commit that lists no path names no other path, so a sealer would go on and seal over a pointer that moved after the broad run.

#1640 asks for the reads of changed paths that a submodule setting can shorten, and `routing.md:19` scopes this work to "each git read that a gate decides on". The frame listed those reads by walking the `.py` files under `lib`, `skills`, `.github/scripts`, `evals/scripts` and `hooks` (`frame/design.md:12`), so a command that the plugin's text tells an agent to type is outside its list. The second `git grep` above lists every such command in `agents/`, `skills/`, `docs/`, `templates/` and `CONTRIBUTING.md` that names a listing flag, and it is a search by spelling, so it is a sample under contract rule 12. It printed `agents/sealer.md:57` and three other lines. `docs/releasing/release-checklist.md:211` lists the `routing.md` files a release adds, under a pathspec no submodule matches. `docs/running/what-a-script-gates.md:35` names the flags in prose. `skills/implement/SKILL.md:387` names `git diff --stat` in prose. `agents/sealer.md:116` diffs under `seal/threads/<item>/` alone, so no submodule reaches it. So `agents/sealer.md:57` is the one typed read that decides on any path. The first `git grep` prints the pin of that command at `tests/behaviour/test_the_sealer_guarantees.py:164`, and the guarantees of earlier work items, which state past runs and stay as written. The `-c` pairs of `lib/gitcmd.py#KEYS` change nothing in a range listing with no single path, so the flag alone is owed.

The fix is a line the frame did not plan: *Scope* names no agent definition. The orchestrator can fold a *Scope* item for it before the fix pass. If it judges the line outside this work, it can defer the line to a row of `seal/follow-up.md` and close this finding `deferred` there.

```markdown
1. **Read the gate's record.** Open `trail/gate.md` in the work item's
   directory, take its newest run's commit, the first word of the `run:`
   line in its last `seal` block, and run
   `git -C <root> log --ignore-submodules=none --no-merges --name-only <named>..HEAD ^<base>`,
   whose flag keeps a submodule's path in the listing whatever the
   repository's settings say, as `lib/gitcmd.py#FLAGS` does for the
   scripts; the rule it applies is the one
   `skills/code-review/scripts/chain_check.py#follows` reads.
```

```python
        # The `git` arguments the sealer runs to list what followed the run.
        assert (
            "log --ignore-submodules=none --no-merges --name-only <named>..HEAD ^<base>"
            in step
        ), step
```

### 2. The changelog says `chain_check.py` missed a pointer-only commit under either setting, and it missed it under the `.gitmodules` entry alone

```seal
severity: should
location: `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/changelog.md:3`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/plan.md:63`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/pr.md:2`
evidence: executed `bin/test tests/lib/test_tmp_round1_probe.py -q -s -p no:xdist` in the round's clone (see `## Probes`); executed `git grep -n -F -e 'touching no path' -e 'refuses more' -e 'ignored submodule' -e 'moves the pointer' -e 'moved only' -- seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor lib/gitcmd.py`; read `skills/code-review/scripts/chain_check.py:974-982`, `frame/design.md:11`, `frame/design.md:13`, `frame/plan.md:71`
```

Why it matters: the changelog entry is the release note a person reads to learn what was wrong in their repository. `changelog.md:3` says that "`diff.ignoreSubmodules` in a configuration, and `ignore = all` in a submodule's `.gitmodules` entry, take the submodule's path out of what those subcommands print", where "those subcommands" are `diff`, `diff-tree`, `log` and `status`. It then says "`chain_check.py` read a commit that moved only an ignored submodule's pointer as touching no path". `chain_check.py#touched` (`:974-982`) reads `diff-tree`, and `frame/design.md:11` (G3) measured that `diff-tree` "prints it under the configuration key". The round's probe ran the bare form of `touched`'s command on the fixture of `tests/lib/test_gitcmd.py#submoduled` under git 2.50.1. It printed `sub` under no setting and under `diff.ignoreSubmodules=all`, and nothing under the `.gitmodules` entry. So a repository that sets the configuration key had a records arm that already refused such a commit. A person who reads the note as written would conclude that the records arm let a pointer through in their repository, and it did not. `frame/design.md:13` (G5) and `frame/plan.md:71` state the fact precisely, "where `.gitmodules` ignores the submodule" and "Under a `.gitmodules` `ignore` setting".

The `git grep` above, a search by the fact's words and so a sample under contract rules 12 and 19, prints two more statements in the same reading. The second sentence of `frame/plan.md:63` follows "In a repository whose submodule is ignored by `diff.ignoreSubmodules` or by its `.gitmodules` entry" and says "For `chain_check.py` this refuses more: a commit that moves the pointer after the last round, the gate or the seal is read as a change outside the work item's records". `pr.md:2` quotes that sentence to the pull request's reader. Under the configuration key, what changes in `chain_check.py` is `changed`'s `diff --raw` (`frame/design.md` G6), not the records arm. `frame/plan.md:41` and the lines of `frame/design.md` the search prints state a mechanism, not which setting reaches it, and stand. The snippets cover the three lines. `frame/plan.md` is the framer's, so the orchestrator folds its line, and `pr.md:2` changes with it so that the quote stays word for word.

```markdown
- **A submodule's path now stays in every `diff`, `diff-tree`, `log` and `status` read a script makes, whatever the repository's settings say (#1640).** `diff.ignoreSubmodules` in a configuration takes the submodule's path out of what `diff`, `log` and `status` print, `ignore = all` in a submodule's `.gitmodules` entry takes it out of `diff-tree` as well, and no `-c` key reaches the `.gitmodules` entry. `seal range` alone passed `--ignore-submodules=none`. Under the `.gitmodules` entry, `chain_check.py` read a commit that moved only the submodule's pointer as touching no path, so such a commit could stand after the last round, the broad gate or the seal. Under either setting, its listing of a pull request's changed paths read such a pointer as no change to code. `lib/gitcmd.py#FLAGS` now holds `--ignore-submodules=none` for `diff`, `diff-tree`, `log` and `status`, and `argv` puts it directly after the subcommand on every command a script starts, past any option a caller writes before it, such as the `--literal-pathspecs` of `seal settle`'s reads. `seal range` passes the flag nowhere itself. `tests/lib/test_gitcmd.py` holds each subcommand under each setting that reshapes it, and a case fails where a subcommand is added to `FLAGS` with no case of its own.
```

```markdown
- In a repository whose submodule is ignored by `diff.ignoreSubmodules` or by its `.gitmodules` entry, `chain_check.py`, `seal mode`'s guard, `seal settle`'s listings and the release note's fragment listing now read the submodule's path as they do under no setting. For `chain_check.py` this refuses more: under the `.gitmodules` entry, a commit that moves the pointer after the last round, the gate or the seal is read as a change outside the work item's records.
```

```markdown
- "For `chain_check.py` this refuses more: under the `.gitmodules` entry, a commit that moves the pointer after the last round, the gate or the seal is read as a change outside the work item's records." (`frame/plan.md` *Operational impact*)
```

### 3. `frame/questions.md` says #1642 asks for 2.24, and the issue's body now says 2.30

```seal
severity: should
location: `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/questions.md:7`, `seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor/frame/design.md:17`
evidence: executed `gh issue view 1642 --json body,comments`; executed `git grep -n -F -e '2.24' -- seal/threads/1795759277-scripts-read-git-past-submodule-settings-and-a-floor lib/gitcmd.py README.md README.ko.md`
```

Why it matters: the sealer reads every party's account against the issue. `frame/questions.md:7` reads "Which version the floor is, and why: 2.30, where #1642 says 2.24". The body of #1642 now gives 2.30 and closes with "_Corrected on 2026-11-27: this body first gave 2.24 and `git diff`. ... The framer of this issue's work item found it._". A sealer that reads the sentence in the present tense finds a disagreement with the issue that no longer stands, and spends a check on it. The `git grep` above, a sample by the number's spelling, prints this line and `frame/design.md:17` (G9). G9's right column says "#1642 says 2.24 and names `git diff`". *Grounding* is dated to `f7d315f01`, where that was what the issue said, so G9 reads as a statement of that moment. Its present tense still invites the same misreading, so the snippet covers it as well. No other line of the records, the docstring or either README names 2.24. Both lines are the framer's, so the orchestrator folds them. The first snippet replaces `frame/questions.md:7`. The second replaces the right-hand cell of G9 at `frame/design.md:17`, and the left-hand cell stays as it is.

```markdown
- Which version the floor is, and why: 2.30. #1642 first gave 2.24, and its body was corrected to 2.30 on 2026-11-27 after this frame read it. The grounds are `frame/design.md` G9 and G10 and `frame/plan.md` row 7.
```

```markdown
#1642 gave 2.24 and named `git diff` when this frame read it, and its body was corrected to 2.30 on 2026-11-27. The tree passes the option to `rev-parse` alone, which reads it from 2.30. The floor `seal range` sets is 2.30.
```

## Confirmations

What matched: the runner. *Scope* item 1 and *Data & interfaces* say that `FLAGS` maps `diff`, `diff-tree`, `log` and `status` to `--ignore-submodules=none`, and that `argv` puts the options directly after the subcommand. `lib/gitcmd.py:121-145` does that. The subcommand is the first argument that does not open with `-`, after `-C` and `-c` with their values. `Failed.command` and `one_run`'s key stay the caller's arguments (`lib/gitcmd.py:299-300`). `older` (`:396-410`) reads the first line by `VERSION.fullmatch`, returns None on a non-zero exit or another shape, compares both numbers as one version against `OLDEST`, and lets `Unrun` through (read). The new code uses nothing past Python 3.9, as the module's docstring asks (`:93-95`, read). The S4 search, `git grep -n -F -e 'ignore-submodules' -e 'ignoreSubmodules' HEAD -- lib skills .github hooks evals/scripts`, prints `lib/gitcmd.py:57`, `:62`, `:63` and `:122-125` and no other file (executed). `older` is called at `skills/implement/scripts/range_read.py:426` alone (executed: `git grep -n 'older(' HEAD -- lib skills hooks .github evals bin`).

What matched: the crafter's three departures, each claimed in a phase record. First, the claim at `trail/phases/phase-1.md:5`: `settle.py#git_run` and `#git_fields` pass `--literal-pathspecs` before the subcommand. That stands at `skills/settle/scripts/settle.py:480` and `:1534` (read). An `argv` built to the frame's first wording would have put no flag on them, and the frame's bullet was folded to the build at `1360c8550`. Second, the claim at `trail/phases/phase-2.md:7`: `_work_item` starts `rev-parse --show-toplevel` through `lib/optin.py#repo_root` before `_commit`. `range_read.py:196` calls `optin.repo_root`, and the ask stands at `:426`, before `_work_item` (read). The place meets *Scope* item 5 and S7, and the *Data & interfaces* sentence "before `_commit`" still holds of it. Third, the claim at `trail/phases/phase-1.md:11`: the helpers that stall one git command matched the argv by its words. `tests/conftest.py#as_called` takes the `FLAGS` options out, and `tests/skills/test_settle.py#unanswered`, `#past_the_bound` and `tests/skills/test_seal.py#unanswered` read through it (read).

What matched: the new failure path. `seal range` now starts `git version` before anything else, so a missing `git` ends in `Unrun`'s line at exit 2 through `main`'s `except gitcmd.Failed` (`range_read.py:486-488`, read). Before, the first git command was `repo_root`'s, which reads `Unrun` as "not opted in", so the person got a line about the work item. The new path names the cause, and no other refusal moved (read).

What matched: the floor. G9's release-note line and the tree's one use of `--end-of-options` were carried from the frame, not re-fetched. `git grep -n -E 'path-format|%\(trailers|--end-of-options|--porcelain=v2|--pathspec-from-file|--deduplicate|--show-scope|--remerge|--object-only|--batch-command' -- 'lib/*.py' 'skills/*.py' 'hooks/*.py'` prints `range_read.py:219`, the `%(trailers:key=...,valueonly,separator=...)` format at `chain_check.py:2039`, which G10 dates to 2.22, and two `for-each-ref` formats (executed). It is a search by option names, so it is a sample. It found no option newer than 2.30. Whether git 2.30 reads each command the same is `frame/questions.md` Q1 and stays open below.

What matched: the four `## Rule changes`. The first `from` is the `to` of `seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md`'s operation on *Which gate a script holds*, word for word. The second is `docs/running/what-a-script-gates.md:44-45`. The fourth is a phrase of that design's `seal range` row of *The checks* (read). The chain check run at the end of this round printed no notice at a line of `frame/design.md` and refused no operation (executed, `## Probes`).

What matched: the new cases. Each was read against its group. The flag's cases sit beside `CASES` and `test_every_key_has_a_case` in `tests/lib/test_gitcmd.py`, and none repeats a key's case. `seal layout --pairs` names three pairs, all in `Test_older`, for calling `older` with equal arguments (executed). Each case of a pair supplies a different line through `starts`: a version below the floor, one at or above it, and a line in another shape. So each holds an answer of `older` that its pair does not, and none is a duplicate. The phase records show the S1, S3, S6, S7 and S8 cases seen red (read). They do not show the S2 case seen red: `trail/phases/phase-1.md:19` says it passed against the old runner "as an accepting case does". The round's probe turned it red. With `diff`'s entry in `FLAGS` set to `--ignore-submodules=all`, its `diff` parameter failed at its `argv` assertion (executed, `## Probes`). So it can fail on the guard it names. The probe also removed `or not found` from `older`. The `another-program`, `a-v-before-it` and `nothing` parameters then failed in `older` itself. So S6's "the other-shape case seen red with the shape check removed" holds, though no record had run that mutation (executed). With every `FLAGS` value set to `--ignore-submodules=dirty`, only `test_accepts_the_flags_after_the_subcommand_past_the_options_before_it` failed, on its literal (executed). No fixture holds a submodule whose checkout has changed files inside, which G3 measured `status` to leave out, so the value `none` against `dirty` is held by that literal alone. The value is still held, so this round opens no finding on it.

What matched: the frame's *Overlap with the release* (`frame/plan.md:52-57`). It is dated to the day both other frames were uncommitted. `origin/fix/1630-1639-the-orchestrators-records-after-the-last-round` at `f9d2756dd` now changes `skills/code-review/orchestration.md`, `skills/implement/orchestration.md` and one case of `tests/skills/test_chain_check.py`. Its `## Rule changes` operate on `docs/running/the-run.md` *The run* alone, so neither `range_read.py` nor `docs/running/what-a-script-gates.md` is shared. Its new case adds a row to `seal/follow-up.md` and stalls no git command, so it needs no `as_called` (executed: `git diff --stat origin/release/v0.39.3...` of the branch, the design's `file:` lines, and the case's diff). `fix/1641-the-cores-margin-depends-on-the-path` at `5590dddf0` changes `lib/core.py`, `payload_meter.py` and their cases, and none of this work's files (executed). The row's "merges first" stands, and the conflict it foresaw in `range_read.py` does not arise.

What matched: `gaps.md`. Its three `## Not verified` rows name an answerer each, and no row left the memo (read). `changelog.md:4`'s line, `seal range: git <version> answers here, and the plugin's scripts need git 2.30 or newer`, is what `older` and `main` print together (`lib/gitcmd.py:407-410`, `range_read.py:484`, read). The README sentences state `` `git` 2.30 `` in both editions (`README.md:51`, `README.ko.md:53`, read). `pr.md:1` and `pr.md:3` quote `frame/plan.md:61` and the `fix:` row at `:71` word for word (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `851641519` beyond the two modules this round ran; the phase boundary sets' counts (`3474 passed, 11 skipped` and `3050 passed, 11 skipped`) were not run again | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, once the round's findings are closed |
| Whether git 2.30 reads each command the scripts under `lib/`, `skills/` and `hooks/` start as 2.50.1 and 2.39.3 read it, and whether a git between 2.24 and 2.29 ends `seal range`'s `rev-parse --end-of-options` with the "does not resolve to a commit" refusal that `changelog.md:4` describes | `frame/questions.md` Q1, `gaps.md:8` | a measurement under a git whose `git --version` prints 2.30 or older, which the repository owner arranges |
| The `FLAGGED` cases and `Test_older::test_accepts_the_line_the_git_running_the_suite_prints` under the Linux and Windows runners' git | `gaps.md:9` | CI's Linux and Windows legs on the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py -q`, in the round's clone at `851641519` | `104 passed` |
| `bin/test tests/lib/test_gitcmd.py -q -p no:xdist -k "under_its_own_defaults_ or a_submodule_named or another_shape"`, with `FLAGS["diff"]` set to `("--ignore-submodules=all",)` and `if done.returncode or not found:` cut to `if done.returncode:` in `lib/gitcmd.py` | `4 failed, 4 passed`: `test_accepts_a_submodule_named_as_git_names_it_under_its_own_defaults[diff]` at `tests/lib/test_gitcmd.py:240`, `assert b'' == b'sub\n'`; `another-program`, `a-v-before-it` and `nothing` at `lib/gitcmd.py:405` on `AttributeError`; `a-non-zero-exit` passed. Both edits were reverted |
| `bin/test tests/lib/test_gitcmd.py tests/skills/test_range_read.py -q -p no:xdist`, with every `FLAGS` value set to `("--ignore-submodules=dirty",)` | `1 failed, 103 passed`: `test_accepts_the_flags_after_the_subcommand_past_the_options_before_it` alone. The edit was reverted |
| `bin/test tests/lib/test_tmp_round1_probe.py -q -s -p no:xdist`, which builds `submoduled(tmp_path, setting)` for each setting and prints `touched`'s `diff-tree --no-commit-id --name-only -r --root -z HEAD` bare and through `argv` | under no setting `sub` both ways; under `configuration` `sub` both ways; under `.gitmodules` nothing bare and `sub` through `argv` |
| `seal layout --pairs`, in the clone | three pairs, each within `tests/lib/test_gitcmd.py::Test_older`, for calling `older` with equal arguments |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.39.3 --root <the branch worktree> --worktree` | exit 0 before the record was written, naming no round record, no gate record and no guarantee. Exit 0 after it, naming findings 1, 2 and 3 as open for want of a close block, and the gate record and guarantee as absent. Neither run printed a notice at a line of `frame/design.md` |
