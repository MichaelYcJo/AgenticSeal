# Review round 1: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

```seal
target: b9dc650deb987e01af94e1b800db460aadc39d7d against release/v0.38.6
```

The base `release/v0.38.6` resolves to `origin/release/v0.38.6` at `c22d58982`, and the range is `c22d58982...b9dc650de` (executed: `git rev-parse HEAD origin/release/v0.38.6`, `git log --oneline c22d58982..HEAD`). This is the first round, so no earlier round's coordinates were carried. Three facts were carried from the phase records and not re-established: the list of cases that run the gate over a key (`trail/phases/phase-1.md` *The cases the Windows leg may now refuse, listed whole*), the 23 `seal mutate` mutants of phase 1 and the four of phase 2, and phase 3's macOS run of the new key over one module. Each is a claim this round read and did not re-run.

## Findings

### 1. The rule change's `to` repeats the template's paragraph, so after the settle two files state the cmd.exe refusal and its reasons

```seal
severity: must
location: `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/design.md:83`, `templates/setup/config.md:256-268`
evidence: executed `python3 skills/code-review/scripts/chain_check.py --baseline c22d58982 --root . --worktree`; read `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/design.md:83`, `templates/setup/config.md:256-268`
```

Why it matters: the chain check printed this notice at the `to` line: "this `to` repeats a passage of `templates/setup/config.md`: 33 of its runs of 15 words stand there, one of them "one value cannot carry both spellings, because /bin/sh reads bin\test as another name. so a"". Read side by side, the `to` restates the template's paragraph *Which shell runs the command, and what the gate refuses there* sentence by sentence. Both say that `cmd.exe` reads a `/` in a command name as a switch, that `bin/test -q` runs `bin` and the report reads as the suite failing, that the gate hands the value as written, that one value cannot carry both spellings, and that a key run under both shells names its commands with no directory in front. The template stays after the settle, and the settle writes the `to` into `docs/running/the-broad-gate.md` *What the gate runs*. Two files would then state one fact, against `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has one source, and every other place links to it." The `to` already names the template as the owner of the reading, so the fix keeps the policy decision in the `to` and sends the rest to that owner. The policy decision is the refusal itself and why the gate does not repair the value. The fix touches only this `to`. The template's paragraph stays as it is, because it is the door a person writing the key opens.

```markdown
- add
  file: docs/running/the-broad-gate.md
  section: What the gate runs
  to: **Where the shell is `cmd.exe`, a command name that starts in a directory with `/` is refused, and the refusal names its `\` spelling.** The gate rewrites no part of the command. A value repaired on its way to the shell leaves the file still wrong, and a model of `cmd.exe`'s reading good enough to repair it is a second shell inside the gate. Why `cmd.exe` fails on such a name, which words the gate reads as command names, what it names as not read, and how a key that runs under both shells is spelt have one owner, `templates/setup/config.md` *Broad gate*.
    check: tests/skills/test_broad_gate.py
```

### 2. A wrapped or backgrounded key's `as meant` line on cmd.exe is a value the gate then refuses

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:878-904`, `tests/skills/test_broad_gate.py:662-683`
evidence: executed `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-1/test_tmp_round1.py <worktree>`; read `skills/verify/scripts/broad_gate.py:878-928`
```

Why it matters: the three older forms are tested first (`broad_gate.py:878-904`), and their `as meant` value is the content with the wrapper or the `&` taken off. On `cmd.exe` in a root that holds `bin/`, the probe asked `not_as_written` about `` `bin/test -q` ``, `$(bin/test -q)` and `bin/test -q &`. Each refusal's `as meant` line read `"Broad gate": "bin/test -q"`. Asked again with that value, the gate refused it a second time, naming `bin/test` and `bin\test`. So a Windows person who writes the key as the first refusal shows it gets a second refusal on the next run. Before this diff the rewriter ran that `as meant` value under `cmd.exe`, so the first `as meant` line was a value the gate ran. This diff made the `as meant` line of the older forms one the gate refuses. The frame's *Scope* item 1 asks that the new form's `as meant` line turn each refused name, and it says nothing of the older forms. No case in `Test_not_as_written` drives a wrapped value on `cmd.exe`, so nothing holds either answer.

```python
def as_cmd_exe_runs(value, root, windows=None, comspec=None):
    """VALUE with `/` written `\\` in each command name the `cmd.exe`
    reading refuses, so that an `as meant` line is a value this gate runs;
    VALUE itself under any other shell."""
    if not cmd_exe_reads(windows, comspec):
        return value
    refused, _ = names_in_a_directory(
        value, lambda part: os.path.isdir(os.path.join(root, part))
    )
    return backslashed(value, list(dict.fromkeys(refused)))


# in not_as_written, each of the three older branches:
        meant = as_cmd_exe_runs(value[1:-1].strip(), root, windows, comspec)
        ...
        meant = as_cmd_exe_runs(value[2:-1].strip(), root, windows, comspec)
        ...
        meant = as_cmd_exe_runs(value[:-1].strip(), root, windows, comspec)
```

The snippet assumes no precondition at an OS boundary beyond the one `not_as_written` already makes: `root` is the directory the command runs in. The fix pass also owes a case in `Test_not_as_written`: `` `bin/test -q` `` on `cmd.exe` in a root that holds `bin/`, whose `as meant` line reads `bin\\test -q`, seen red against the tree as it stands. The other reading, that an `as meant` line strips the wrapper and nothing else, is a choice the fix pass may make instead. Then the template's refused table owes the sentence that on `cmd.exe` the `as meant` value of a wrapped key can be refused again.

### 3. The template's list of places where the reading and cmd.exe differ omits a `(` that opens a block, a leading `@` and a redirection that opens the command

```seal
severity: should
location: `templates/setup/config.md:291-308`
evidence: executed `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-1/test_tmp_round1.py <worktree>`; read `templates/setup/config.md:270-308`, `skills/verify/scripts/broad_gate.py:766-776`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/design.md:21`, `git show c22d58982:templates/setup/config.md` lines 278-279
```

Why it matters: the section *Where the reading and `cmd.exe` differ* reads as the whole list. A Windows person who checks a key against it learns that outside its four bullets the reading and `cmd.exe` agree. Three more cases make `cmd.exe` read a command name that the gate neither refuses nor names. The probe ran `@bin/test -q` and `>out.txt bin/test` on `cmd.exe` in a root holding `bin/`, and `not_as_written` returned `None` for both and wrote nothing to stderr. `command_names` (`broad_gate.py:766-776`) takes `@bin/test` and `(bin/a` as first words, whose parts before the `/` are `@bin` and `(bin`, and those name no directory. It takes the word after `>out.txt` for an argument. The frame's own probe found the block case: design.md G13 says "`(bin/a` is not read". The paragraph this diff replaced named the redirection case as handed over as written (`c22d58982`, `templates/setup/config.md` lines 278-279), and the rewrite dropped it. Each of the three fails under `cmd.exe` as #448 did, with no line saying why. A list over `cmd.exe`'s syntax stays a sample (contract rule 12), so the fix names these three and says the list gives examples. It does not claim the list is whole.

```markdown
**Where the reading and `cmd.exe` differ.** The bullets below are examples,
not the whole list: the reading models nothing of `cmd.exe`'s syntax beyond
the cut and the four separator words.

- A name `cmd.exe` reads after a character the reading does not strip is
  neither refused nor named: after a `(` that opens a block, as in
  `(bin/a && b)`, or a leading `@`, as in `@bin/test`, the reading asks
  about `(bin` or `@bin`, which names no directory. A name after a
  redirection that opens its command, as in `>out.txt bin/test`, is read as
  an argument. `cmd.exe` reads each as a command name and fails on it.
  Writing the name first, with a blank before the redirection, puts it back
  in the reading.
```

The existing four bullets stay below this one. The snippet replaces the heading line at `templates/setup/config.md:291`. No other sentence states the list: `broad_gate.py:861-864` names the glued separator and points at the template for the rest.

### 4. On Windows a name that opens with a drive is refused, and the template, the docstring and the changelog say a name is refused only where its part names a directory under the root

```seal
severity: should
location: `templates/setup/config.md:276-278`, `skills/verify/scripts/broad_gate.py:857-859`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/changelog.md:3`
evidence: executed `python3 -c` over `ntpath.join` for `('C:\\a\\repo', 'C:')` and `('D:\\a\\repo', 'C:')`; read `skills/verify/scripts/broad_gate.py:908-910`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/gaps.md:8`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/trail/phases/phase-1.md:21`
```

Why it matters: `not_as_written` asks `os.path.isdir(os.path.join(root, part))` (`broad_gate.py:908-910`). On Windows `os.path` is `ntpath`, and `ntpath.join` gave `C:\a\repo\` for a root on `C:` and `C:` for a root on `D:`. Both are directories, so `C:/Python/python.exe -m pytest` is refused naming `C:\Python\python.exe`, as `trail/phases/phase-1.md` and `gaps.md` *Not verified* state. Three texts a reader acts on state the rule as a directory under the root. The template says "names a directory under the repository root, where the command runs. An empty part (a name that opens with `/`), `.` and `..` each name one" (`templates/setup/config.md:276-278`). The docstring says "a directory under ROOT, the root the command runs in" (`broad_gate.py:857-859`). The changelog says "A name is refused where the part before its first `/` is a directory under the repository root" (`changelog.md:3`). The template's list names three parts that are not under the root, and it leaves the drive out. `gaps.md` names the case, but `gaps.md` does not ship. So a Windows user with an absolute interpreter path in the key meets a refusal that no shipped text names. Whether `cmd.exe` runs the `/` spelling of a drive path is a measurement `gaps.md` already asks for, and this finding does not depend on it. Where `cmd.exe` runs it, the template's bullet list is the place for the refusal of a correct value. Where it does not, the rule sentence is where the drive belongs. The snippet takes the second reading, because the code refuses either way.

```markdown
under the repository root, where the command runs. An empty part (a name
that opens with `/`), `.` and `..` each name one, and on Windows so does a
drive, so `C:/Python/python.exe` is refused naming `C:\Python\python.exe`.
```

The same clause goes into the docstring at `broad_gate.py:858-859`, as "a directory under ROOT, the root the command runs in, or on Windows a drive". It goes into `changelog.md:3` as "is a directory under the repository root, or on Windows a drive such as `C:`".

### 5. A name that straddles the cut is refused by its truncated part, and the refusal says cmd.exe runs that part

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:779-817`
evidence: executed `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-1/test_tmp_round1.py <worktree>`; read `skills/verify/scripts/broad_gate.py:779-817`, `skills/verify/scripts/broad_gate.py:916-928`
```

Why it matters: `names_in_a_directory` reads `command[:cut]`, so a word that holds the cut character after its `/` is read up to the cut. The probe ran `bin/%TOOL% -q` on `cmd.exe` in a root holding `bin/`. The refusal read "starts a command name in a directory with `/`: `bin/`" and "cmd.exe runs `bin\`". The `as meant` line was right (`bin\\%TOOL% -q`), but the sentence names a word the key does not hold and says `cmd.exe` runs `bin\`, which it does not. The refusal itself holds, because the `/` before the cut is read exactly. Only the named word is wrong. Keys with a `%` inside a command name are rare, which bounds the cost. The fix names the whole word and still turns only the part before the cut:

```python
    cut = cmd_cut(command)
    whole = dict(command_names(command))  # offset -> the word as it stands
    refused = [
        whole[at]
        for at, w in command_names(command[:cut])
        if starts_in_a_directory(w)
    ]
    ...

def backslashed(value, refused):
    out = list(value)
    whole = dict(command_names(value))
    for at, word in command_names(value[: cmd_cut(value)]):
        if whole[at] in refused:
            out[at : at + len(word)] = word.replace("/", "\\")
    return "".join(out)
```

A word that starts before the cut starts at the same offset in both readings, because the two splits agree up to the cut. The fix pass also owes a row in `Test_not_as_written` for `bin/%TOOL% -q` naming `bin/%TOOL%`, seen red as it stands. The docstring of `names_in_a_directory` owes one sentence saying a name the cut splits is named whole.

### 6. `pr.md` does not quote `frame/questions.md` M1, the default taken under automation on whether this repository's own key runs on Windows

```seal
severity: should
location: `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/pr.md:1-5`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/questions.md:14`
evidence: read `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/pr.md:1-9`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/questions.md:14`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/routing.md:9`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/gaps.md:10`, `skills/code-review/orchestration.md:385-393`
```

Why it matters: `routing.md` reads `Automation` `yes`, and `frame/questions.md` M1 is open with the default "The spelling of `design.md` *Scope* item 9 stands". `skills/code-review/orchestration.md` *The pull request body's first part* names exactly this as what the owner must see before the fold: "a default taken where `routing.md` reads `Automation` `yes`, from its `frame/questions.md` row". `pr.md` quotes the two other measurements of `gaps.md` *Not verified*, the drive row and the template row. It leaves out M1, which `gaps.md:10` also carries. M1 decides whether the key this diff writes into `seal/config.json` runs the suite on the owner's Windows machine. The owner is the person #448 was measured on, and no CI leg runs the key. The repair is the orchestrator's (`orchestration.md` *Where a fix pass or a fold changes a sentence that `pr.md` quotes*). Each added line quotes a cell of M1 word for word:

```markdown
- "Does `uvx ruff check . && uvx ruff format --check . && uv run --no-project tests/run_tests.py -q` run the suite under `cmd.exe` on Windows, with `PYTHONPATH` and `PYTEST_ADDOPTS` kept as the gate sets them?" (`frame/questions.md`, row M1, the question)
- "The spelling of `design.md` *Scope* item 9 stands" (`frame/questions.md`, row M1, the default until answered)
```

The two lines go after `pr.md:5` and before `Closes #1577.`.

## Confirmations

What matched: *Scope* item 3 and the *User scenarios* row *The gate rewrites nothing*. `git grep -n -E 'handed_to_shell|command_names_backslashed|as_cmd_expands|CMD_BUILTINS|CMD_VARIABLE|handed_line|cmd\.exe was handed' -- . ':!seal/threads'` printed nothing and exited 1 (executed). `run` (`broad_gate.py:960-985`) hands `command` to `subprocess.run` unchanged, and keeps `$ <command>`, `exit <code>`, a blank line and the output (read). `compare_at_base` calls `run` with no platform arguments (`broad_gate.py:1484-1491`, read).

What matched: *Scope* items 1 and 2 against `broad_gate.py:716-937` (read). The cut at `"`, `^` and `%` is `CMD_CUT`. The split at blanks and tabs is `CMD_WORD`. The separator words are `CMD_SEPARATORS`. The directory question is asked of `root` in `not_as_written`, and `gate` passes its own `root` (`broad_gate.py:2011`, read). The refusal's sentence, `as written` and `as meant` lines and the not-read line match the frame's wording. `test_refuses_a_command_name_cmd_exe_reads_as_a_switch` pins the message whole (`tests/skills/test_broad_gate.py:685-709`, read). `not_as_written` has no caller but `gate` and the two calls in `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:66-67` (executed: `git grep -n not_as_written`).

What matched: *Scope* items 4 and 5 and the *Removes* rows on cases. `Test_not_as_written` holds one case per edge *Scope* item 4 lists, and `Test_run`'s two real-platform cases match *Scope* item 5 (`tests/skills/test_broad_gate.py:662-905`, read). None of the helpers *Removes* names stands in the file (executed: `grep -n -E 'CMD_ROW|HANDED|DIRECTORIES|only_slashes_turned|_Ran\b|runs_under_cmd_exe|def tree\b'`). Nothing in the tree names the removed text case (executed: `git grep` on its file name, exit 1). The narrow run of the four modules this diff touches passed (executed, *Probes*).

What matched: phase 3's claim that it strengthened `test_this_repositorys_own_config_is_answered_exactly_as_before` to ask `cmd.exe` on every leg. The case now asks `not_as_written(home, command, ROOT, windows=True, comspec="cmd.exe")` and asserts `None` (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:66-68`, read). `ROOT` holds `bin/`, so a key naming `bin/test` would be refused on a POSIX leg too. That is the red the phase reports from `seal mutate seal/config.json`, which this round read and did not re-run. The frame's *User scenarios* row *This repository's key* states the same at the target (`frame/design.md:67`, read).

What matched: *Scope* items 6 to 8. The template's paragraph states the reading, the not-read line and the bounds. Its refused table gains the row, and the sentence above it stops counting (`templates/setup/config.md:256-327`, read). The config skill names the form (`skills/config/SKILL.md:110-118`, read). `REFUSED` names the form, and `refusal_bullet` is checked against `REFUSED` (read). The `tests/conftest.py` sentence is rewritten as *Scope* item 8 asks (read). `git grep -n -i -E 'three (refused )?forms|the three forms|refused three'` found only `broad_gate.py:16`, which counts the kinds of refusal, and `seal.py:1719`, which names another command (executed).

What matched: `seal/config.json:5` holds the key of *Scope* item 9. Its command names are `uvx`, `uvx` and `uv`, none holding a `/` (read). The routing estimate of "about 340 lines" removed from `broad_gate.py` and "about 170" added holds at 344 and 177 (executed: `git diff --numstat`).

What matched: every quote of `pr.md` stands word for word at its coordinate. Line 1 is `frame/plan.md:59`, line 2 is `routing.md:16`, line 3 is `frame/plan.md:60`, line 4 is `gaps.md:8` and line 5 is `gaps.md:9` (read). Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` is owed. `gaps.md` is new in this range, so no row of it left.

One parametrized row repeats another case: `test_refuses_a_name_after_each_separator_word[&&]` (`tests/skills/test_broad_gate.py:730-736`) reads a value that differs from the pinned case's `OLD_KEY` only by its `-q`. The test's other three rows cover what its group does not, so this is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The `cmd.exe` half of `Test_run`'s two real-platform cases. The shell here is `/bin/sh`, so the second case skipped and the first ran its POSIX half | `tests/skills/test_broad_gate.py:849-905`, `gaps.md:7` | CI's `windows-latest` leg, read by the orchestrator at the pull request |
| Whether `cmd.exe` runs `rem a && bin/test`, a glued separator, a drive path with `/`, and this repository's key as written. Finding 4 does not rest on the drive answer | `gaps.md:8-10`, `frame/questions.md:14` | a measurement on a Windows machine, as `gaps.md` names |
| The broad gate: the full suite, the lint and the format check. The phase records name narrow and boundary runs only, and no hand-back reached this round to check its `unverified` label | `seal/config.json:5` | the orchestrator's broad run |
| How the merge with #1573, which also edits `broad_gate.py`, lands. This round did not open #1573's checkout, as its spawn asked | `frame/plan.md:47` | the orchestrator, at whichever merge comes second |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/text/test_broad_gate_rule.py -q`, from the worktree | exit 0, 221 passed and 1 skipped. The skip is `Test_run#test_a_switch_against_a_program_runs_on_the_real_platform` on a shell that is not `cmd.exe` |
| `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-1/test_tmp_round1.py <worktree>`, run once, which loads `broad_gate.py` from the worktree and asks `not_as_written` with `windows=True` and `comspec="cmd.exe"` in a temporary root holding `bin/` | the three wrapped or backgrounded values each refused with `as meant` `bin/test -q`, and that value refused again naming `bin/test` (finding 2). `bin/%TOOL% -q` refused naming `` `bin/` `` and `` `bin\` `` (finding 5). `@bin/test -q` and `>out.txt bin/test` returned `None` (finding 3) |
| `python3 -c` printing `ntpath.join` for a root on `C:` and on `D:` with the part `C:` | `C:\a\repo\` and `C:`, both directories on a Windows machine (finding 4) |
| `python3 skills/code-review/scripts/chain_check.py --baseline c22d58982 --root . --worktree`, before this record stood | exit 0. One notice at `frame/design.md:83`, quoted in finding 1, and the arms for the missing round, gate and guarantee records |
