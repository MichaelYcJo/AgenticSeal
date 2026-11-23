# Review round 2: 1795390621-the-broad-gate-rewrites-cmd-exe-commands

```seal
target: 2ab54198a74253599f841f5f1aa9a3cca7066b8c, fixes f65b9297d..2ab54198a
```

This is a verifying round. `f65b9297d` is the commit of round 1's record, so the fix diff is `f65b9297d..2ab54198a`. It holds the records fix `3f7fa4113`, the code fix `3372bc792`, its case `3248aaaf2`, the template fix `b85f55619`, the `gaps.md` row `2fbde64a9`, the close blocks `94e27b1d6` and the orchestrator's fold `2ab54198a` (executed: `git log --oneline origin/release/v0.38.6..HEAD`, `git diff --stat f65b9297d..HEAD`). The base `release/v0.38.6` now resolves to `3c89a70d5`, which this branch has not merged. That merge is the orchestrator's, before the broad run, and this round read nothing that #1578 brings.

Carried from round 1 and not established again: the list of cases that run the gate over a key (`trail/phases/phase-1.md` *The cases the Windows leg may now refuse, listed whole*), and the phase records' mutation counts. The fix pass's own `seal mutate` counts in round 1's close blocks of findings 2 and 5 were read and not re-run, except the one mutant in *Probes*. The coordinates of round 1's findings were opened where they stand at the target.

The records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, the three phase records and round 1. `seal/config.json` names English for both language keys, so no `pr.<lang>.md` is owed.

## Findings

### 1. A name the cut splits is still not named whole after a `"`, and the refusal says cmd.exe runs a spelling past the cut that the gate never read

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:941-961`, `skills/verify/scripts/broad_gate.py:779-799`, `templates/setup/config.md:275-283`, `templates/setup/config.md:308-311`, `tests/skills/test_broad_gate.py:840-848`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/design.md:32`
evidence: executed `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-2/test_tmp_round2.py <clone>`; read `skills/verify/scripts/broad_gate.py:760-803`, `skills/verify/scripts/broad_gate.py:941-961`, `templates/setup/config.md:270-311`
reopens: round-1#5
```

Why it matters: the close of round 1's finding 5 does not hold for every cut character. That finding's grounds were that the refusal "names a word the key does not hold and says `cmd.exe` runs `bin\`, which it does not". The fix names the name as the blank split of the whole value gives it (`broad_gate.py:796-799`). It then takes the `cmd.exe runs` spelling from the key as meant, which turns only the part before the cut (`broad_gate.py:943-951`). Past the cut the gate reads nothing exactly, so both choices still speak about text the gate did not read.

- After a `"`, the blank split is not the name. The probe asked `bin/"a b"/x -q` on `cmd.exe` in a root holding `bin/`. The refusal named `` `bin/"a` `` and said "cmd.exe runs `` `bin\"a` ``". `cmd.exe` reads the quoted blank as part of the name, so the name is not `bin/"a`, and `cmd.exe` does not run `bin\"a`. That is round 1's symptom: a word cut short, and a claim about what `cmd.exe` runs.
- After a `%`, the spelling keeps a `/` that the refusal's own sentence calls a switch. For `bin/%TOOL%/x -q` the refusal says "cmd.exe runs `bin\%TOOL%/x`" (pinned at `tests/skills/test_broad_gate.py:846`). The same sentence says `cmd.exe` "reads a `/` in a command name as the start of a switch". So after `%TOOL%` expands, by the gate's own rule, `/x` is still a switch. The probe then asked the gate about the key as meant, `bin\%TOOL%/x -q`. The gate returned `None` and wrote nothing to stderr, so a person who takes the offer gets #448's failure with no line saying why.

The template states the bound wrongly in two places. `templates/setup/config.md:280-281` says a name that holds a `"`, `^` or `%` after its `/` is "named whole", and the `"` case shows it is not. `templates/setup/config.md:308-311` gives the condition under which "a key stays inside the reading". A key such as `%PY%/python.exe -m pytest` meets every part of that condition, yet the reading cannot answer it. The cut is at offset 0, and the part before the `/` is the literal `%PY%`, which names no directory, so the gate neither refuses nor names it (read: `broad_gate.py:794-802`). `frame/design.md:32` says "A name the cut splits is named whole", which the target contradicts for `"`. The frame is the orchestrator's to fold.

The fix keeps the frame's choice that only the part before the cut is turned, and stops the refusal claiming what `cmd.exe` runs past it. Every name is wholly before the cut or is the one word the cut splits, because a word that holds a cut character holds the first one. So `name not in split` is exact, and the offset filter that `3248aaaf2` pins is no longer needed for the names wholly before the cut.

```python
        names = list(dict.fromkeys(refused))
        meant = backslashed(value, names)
        cut = cmd_cut(value)
        # A name the cut splits is read only up to the cut: the gate turns no
        # `/` past it and says nothing of what cmd.exe runs there.
        split = [
            word
            for at, word in command_names(value)
            if at < cut < at + len(word) and word in names
        ]
        turned = [name.replace("/", "\\") for name in names if name not in split]
        form = f"starts a command name in a directory with `/`: {listed(names)}"
        does = (
            "and the shell here is cmd.exe, which reads a `/` in a command "
            "name as the start of a switch, so it runs the part before the `/` "
            "as the command, which fails before any check has run, and the "
            "report reads as the suite failing. "
            + (f"cmd.exe runs {listed(turned)}, and " if turned else "")
            + (
                f"the gate read {listed(split)} only as far as its first "
                f"`{value[cut]}` and turned no `/` past it, so what cmd.exe "
                "runs there is not read, and "
                if split
                else ""
            )
            + "`/bin/sh` reads the `\\` spelling as another name, so a key run "
            "under both shells names its commands with no directory in front, "
            "and hands a script's path to an interpreter as an argument"
        )
```

The template's sentence at :280-281 moves after the `So pytest tests/x.py` sentence, so that the `So` follows the rule it draws on again:

```markdown
are arguments, and `bin -q` is not, because it holds no `/`. A name that
holds a `"`, `^` or `%` after its `/` is refused on its part before that
character and named as far as the next blank. The gate turns no `/` past
the character, and says nothing of what `cmd.exe` runs there.
```

The sentence at :308-311 gains the condition it leaves out:

```markdown
an earlier command makes or a `cd` enters. A key stays inside the
reading where each command name, with nothing glued in front of it, is
the first word of its command and holds no `"`, `^` or `%`, and every
separator has a blank on each side.
```

The snippets leave statements that the fix pass also owes. `names_in_a_directory`'s docstring (`broad_gate.py:783-784`) says "named whole", and it becomes "named as far as the next blank". The pinned message in `test_refuses_a_command_name_cmd_exe_reads_as_a_switch` changes from "reads that spelling" to "reads the `\` spelling" (contract rule 14). In `test_refuses_a_name_the_cut_splits_by_naming_it_whole`, the assertion on "cmd.exe runs `bin\\%TOOL%/x`" becomes an assertion that the sentence holds "the gate read `bin/%TOOL%/x` only as far as its first `%`" and does not hold "cmd.exe runs". The case gains a row for `bin/"a b"/x -q`, named as `bin/"a`, and its docstring stops saying the refusal "never names a word cut short". `frame/design.md:32` is the orchestrator's to fold. The snippet assumes no precondition at an OS boundary.

### 2. No case holds that the key as meant of a wrapped value turns nothing under `/bin/sh`

```seal
severity: should
location: `tests/skills/test_broad_gate.py:677-698`, `skills/verify/scripts/broad_gate.py:837-838`
evidence: executed `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py -q -p no:xdist` in the clone with `as_cmd_exe_runs`'s first two lines removed; read `tests/skills/test_broad_gate.py:662-698`, `git grep -n "not_as_written\|as_cmd_exe_runs" -- tests`
regression: round-1#2
```

Why it matters: the unit is `as_cmd_exe_runs` (`broad_gate.py:833-840`), which `3372bc792` added for round 1's finding 2. Its guard returns the value unchanged where the shell is not `cmd.exe`. `frame/design.md:32` says the key as meant of the three older forms turns names "on `cmd.exe`", and the fix built that half with a case. The defect is that only that half has a case. `test_refuses_a_wrapped_value_on_cmd_exe_with_a_key_as_meant_it_runs` drives `cmd.exe` alone. `test_refuses_a_wrapped_or_backgrounded_value` asks this machine's shell in `tmp_path`, which holds no `bin/`, so with the guard removed the scan finds nothing to turn there either. With the guard removed, the three modules that call `not_as_written` passed: 218 passed and 1 skipped, exit 0. Without the guard, a POSIX user with a wrapped key in a repository that holds `bin/` would be offered `bin\test -q`, which `/bin/sh` reads as another name. The probe showed that the target gives `bin/test -q` there, so the code is right and nothing pins it.

```python
    @pytest.mark.parametrize(
        "value", ["`bin/test -q`", "$(bin/test -q)", "bin/test -q &"]
    )
    @pytest.mark.parametrize(
        ("windows", "comspec"),
        [(False, None), (True, r"C:\Program Files\Git\bin\bash.exe")],
    )
    def test_refuses_a_wrapped_value_under_another_shell_with_its_slash_as_meant(
        self, tmp_path, value, windows, comspec
    ):
        """Under `/bin/sh`, or a `COMSPEC` naming another shell, the key as
        meant of a wrapped or backgrounded value turns nothing, even in a root
        that holds `bin/`: `/bin/sh` reads `bin\\test` as another name."""
        root = a_root(tmp_path, "bin")
        said = gate.not_as_written(HOME, value, root, windows=windows, comspec=comspec)
        meant = json.dumps("bin/test -q")
        assert f'    as meant:   "{ROW}": {meant}' in said, said
```

The case is seen red by removing the two lines at `broad_gate.py:837-838`. With them removed, each row's `as meant` line reads `bin\\test -q`.

### 3. The claim that every refusal offers a key the gate runs is false for a key that nests two refused forms

```seal
severity: should
location: `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/changelog.md:3`, `skills/verify/scripts/broad_gate.py:834-836`, `skills/verify/scripts/broad_gate.py:889-891`, `tests/skills/test_broad_gate.py:691-693`, `seal/threads/1795390621-the-broad-gate-rewrites-cmd-exe-commands/frame/design.md:32`
evidence: executed `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-2/test_tmp_round2.py <clone>`; read `skills/verify/scripts/broad_gate.py:901-931`
regression: round-1#2
```

Why it matters: the unit is the set of sentences that `3372bc792` and the fold `2ab54198a` wrote for round 1's finding 2. `frame/design.md:32` says the turning makes "the value a refusal offers ... one the gate runs". The fix states that as true of every refusal, and the code takes off one wrapper only. The changelog says "the value any refusal offers is one the gate runs". `not_as_written`'s docstring says "so the value a refusal offers is one it runs". `as_cmd_exe_runs`'s docstring says "a refusal's key as meant is one this gate runs", and the new case's docstring repeats it. The probe asked `` `bin/test -q &` `` on `cmd.exe` in a root holding `bin/`. The key as meant was `bin\test -q &`, and the gate refused it again, this time for the trailing `&`. The key `` $(`bin/test -q`) `` was offered `` `bin/test -q` `` and refused again. What the fix does guarantee is narrower: the key as meant names no command the gate refuses for its `/`. A reader who edits `not_as_written` and trusts the docstring's invariant would add a form without checking it. The changelog sentence promises a user something the gate does not do.

```markdown
changelog.md:3      ... turns those names too, so the key as meant names no command the gate refuses for its `/`.
broad_gate.py:835   `backslashed`, so that a refusal's key as meant names no command this
                    gate refuses for its `/`; VALUE itself under any other shell."""
broad_gate.py:890   meant of every form turns the names this reading refuses
                    (`as_cmd_exe_runs`), so the key a refusal offers names no command
                    refused for its `/`.
test_broad_gate.py:691-693
                    """On `cmd.exe`, the key as meant of a wrapped or backgrounded value
                    also turns each command name the `cmd.exe` reading refuses, so the
                    value the refusal offers is not refused for a name's `/`."""
```

The case's name, `..._with_a_key_as_meant_it_runs`, is true for its three rows and may stay. `frame/design.md:32` is the orchestrator's to fold: "so the value a refusal offers names no command the gate refuses for its `/`".

## Confirmations

```seal
confirms: round-1#1
```
What holds: the `to` at `frame/design.md:83` keeps the refusal and the reason the gate repairs nothing. It hands the rest to `templates/setup/config.md` *Broad gate*, whose three paragraphs it relies on stand at `:256`, `:270` and `:285` (read). The chain check printed no notice at `frame/design.md:83` this round (executed, *Probes*).

```seal
confirms: round-1#2
```
What holds: on `cmd.exe` in a root holding `bin/`, each of the three older forms is refused with the key as meant `bin\\test -q`, and that value is then not refused. Under `/bin/sh` the key as meant stays `bin/test -q` (executed, the probe). The three call sites stand at `broad_gate.py:913`, `:921` and `:931` (read). Findings 2 and 3 of this round are in units this fix added, and neither undoes the close.

```seal
confirms: round-1#3
```
What holds: `templates/setup/config.md:294-321` opens with the rule, that the reading is the whole of what the gate decides by. It gives one bullet for each direction, with each bullet's rule, gives shapes only as examples, and counts none (read). `not_as_written`'s docstring at `broad_gate.py:885-889` states the same rule and points at the template (read). `frame/design.md` *Scope* item 6, as folded at `2ab54198a`, says the same (read). `frame/plan.md:11`'s "names each of these bounds" still holds for its three cases, at `:285-288`, `:314-318` and `:306-307` (read). Finding 1 of this round is about the sentence at `:308-311`, which the rule's statement made, and it leaves the close standing.

```seal
confirms: round-1#4
```
What holds: the template's rule sentence names the drive at `templates/setup/config.md:278-279`. The docstring says "or on Windows a drive (`in_root`)" at `broad_gate.py:883`, and `in_root` at `:825-830` says why. The changelog reads "or on Windows a drive such as `C:`" (read). The code's answer is the same `os.path.isdir(os.path.join(root, part))` as before (read: `git diff f65b9297d..HEAD -- skills`).

```seal
confirms: round-1#6
```
What holds: `pr.md:6` and `pr.md:7` stand word for word in `frame/questions.md:14`, as the question cell and the default cell of M1 (read).

What matched: the other five quotes of `pr.md` still stand at their coordinates. Line 1 is at `frame/plan.md:59`, line 2 at `routing.md:16`, line 3 at `frame/plan.md:60`, line 4 at `gaps.md:8` and line 5 at `gaps.md:9` (read). The fix diff's change to `gaps.md` adds one row and removes none (executed: `git diff f65b9297d..HEAD -- seal/threads`).

What matched: the narrow run of the four modules over `broad_gate.py` and its documents passed at the target (executed, *Probes*). The two new cases in `3372bc792` and `3248aaaf2`, read against `Test_not_as_written`, each cover something no earlier case covers: the whole-naming of a split name, and one spelling for a name that stands again past the cut. Finding 1 changes what the first one pins.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `pr.md` quotes the `gaps.md` *Not verified* row that `2fbde64a9` added, on the template's `@bin/test` and `>out.txt bin/test` examples. Rows 8 and 9, of the same kind, are quoted | `gaps.md:11`, `pr.md:1-7` | the orchestrator, who writes `pr.md` |
| What `cmd.exe` does with the template's examples, with a drive path written with `/`, with a name holding `%VAR%` or a quoted blank after its `/`, and with this repository's key | `gaps.md:8-11`, `frame/questions.md:14` | a measurement on a Windows machine, as `gaps.md` names. Finding 1 rests on the gate's own stated rule, not on such a run |
| The broad gate: the full suite, the lint and the format check, after the merge of `3c89a70d5`. No crafter hand-back reached this round, so no `unverified` label was there to check | `seal/config.json:5` | the orchestrator's broad run |
| The `cmd.exe` half of `Test_run`'s two real-platform cases | `gaps.md:7` | CI's `windows-latest` leg, read by the orchestrator at the pull request |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_broad_gate_row_is_asked_for_and_runs_as_written.py tests/text/test_broad_gate_rule.py -q -p no:xdist`, in a `git clone --no-local` of the branch at the target | exit 0, 226 passed and 1 skipped |
| `python3 -I <scratchpad>/1795390621-the-broad-gate-rewrites-cmd-exe-commands/round-2/test_tmp_round2.py <clone>`, run once. It loads `broad_gate.py` from the clone and asks `not_as_written` with `windows=True` and `comspec` naming `cmd.exe`, in a temporary root holding `bin/`, and then asks again with each key as meant | `bin/%TOOL%/x -q` is refused, "cmd.exe runs `bin\%TOOL%/x`", and its key as meant gives `None` with nothing on stderr. `bin/"a b"/x -q` is refused naming `bin/"a` and saying `cmd.exe` runs `bin\"a` (finding 1). `` `bin/test -q &` `` is offered `bin\test -q &`, which is refused again for its `&`. `` $(`bin/test -q`) `` is offered `` `bin/test -q` ``, which is refused again (finding 3). With `windows=False`, the three older forms are offered `bin/test -q` (finding 2, confirmation of round-1#2) |
| The same three-module run, in the clone, with `if not cmd_exe_reads(windows, comspec): return value` removed from `as_cmd_exe_runs` through `Edit`, and then restored through `Edit`. `git status --short` printed nothing afterwards | exit 0, 218 passed and 1 skipped: no case holds the guard (finding 2) |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.38.6 --root <worktree> --worktree`, before this record stood | exit 0. No notice at `frame/design.md`. It names round 1's five closed findings as owing a verifying round, and names the gate and guarantee records as absent |
