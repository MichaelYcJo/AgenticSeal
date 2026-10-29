# Review round 3: 1793251201-a-push-only-workflow-answers-a-deferral

target: 274317f3, fixes b0fd17c3..274317f3

This round verifies the fix diff. It ran in a `git clone --no-local` of the
branch at `274317f3`. Earlier rounds handed over three things, and this round
carried them without establishing them again. The first is the probe method:
the script of a revision comes from
`git show <rev>:skills/verify/scripts/deferral_check.py` and runs over one
temporary project per trigger shape. The second is round 2's YAML readings of
its shapes, among them `on: pull_request` / `  push` loading as
`{True: 'pull_request push'}`. The third is `seal layout --pairs`, which names
no pair in `tests/skills/test_deferral_check.py`; the fix diff adds no test
file. The round 2 shapes were run again through all three scripts, as the
executed evidence lines of round 2 ask. Every verdict below was reached on the
code at `274317f3`.

## Findings

### 1. A colon with text glued to it is read as a key, so one event name GitHub runs nothing on answers a deferral

severity: should
location: `skills/verify/scripts/deferral_check.py:145-149`, `skills/verify/scripts/deferral_check.py:94`, `tests/skills/test_deferral_check.py:183-215`
evidence: executed `python3 -I test_tmp_r3.py`, `uv run --no-project --with pyyaml python3 -I -c 'import yaml; yaml.safe_load(...)'`
verdict: open

This round opened it while enumerating the class of the fix pass's new
`under_key = ":" in item` at `:145`, which takes its colon test from the
build's key arm at `:148-149`. That arm came with 87ec5583, a build commit
and an ancestor of round 1's target. The probe shows `274317f3` and
`b0fd17c3` print the same thing for every shape below, so no fix pass made
the defect. The finding carries neither a `regression:` nor a `reopens:`
line. It is not round-2#1 standing either. Round-2#1 named a deeper line
that continues a name. These shapes answer with no deeper line at all,
because the cause is the colon test and not the continuation.

In block YAML a colon starts a mapping value only where a space or the end
of the line follows it. So `on:` / `  pull_request:foo` loads as
`{True: 'pull_request:foo'}`, one plain scalar (executed). GitHub runs no
workflow on that name. `block_entries` takes any line at the block's indent
that holds a colon as a key, and keeps the text before the first colon
(`:148-149`). The probe printed `answers ... (on pull_request)` at exit 0 for
it at `b0fd17c3` and at `274317f3`. The base `8d8d6390` printed
`answers ... (trigger unread)` at exit 0, which is the arm this work item
removes. The fix pass's `under_key` reads the same colon, so
`on:` / `  pull_request:foo` / `    push`, which YAML loads as
`'pull_request:foo push'`, also prints `answers ... (on pull_request)` at
exit 0 at both revisions.

`ON_KEY` at `:94` has the same test, `\s*:(.*)$`. `on:pull_request` matches
it with the value `pull_request`, and `continued` sees `jobs:` at indent zero
below it, so the inline arm returns `{pull_request}` (read `:94`,
`:186-203`). A YAML parser refuses that file with a `ScannerError`
(executed), so GitHub runs nothing from it. The base's
`^on\s*:\s*(.*)$` read it the same way (read base `:100`). The inline arm and
the flow list do not need the change: a value such as `pull_request:foo`
there already fails `EVENT_NAME` and reads as unread (read `:202`).

`frame/design.md` *Scope* item 1 reads a line at the block's indent as "a
key, with or without a value or a comment after its colon". Text glued to
the colon is no key in YAML, and *Scope* item 2 makes an entry that is not
an event name unread. This is the fail-open #1123 closes: a deferral to CI
is answered by a workflow that never runs. `SECURITY.md` *What is in scope*
counts a check that fails open as a security defect. Each shape is an
invalid trigger, which is also true of round 2's two findings.

The fix makes a colon a key's only where whitespace or the end of the line
follows it, in both readers. `KEY` is a new name, defined here.
`ON_KEY.group(1)` stays a string, empty or starting with whitespace, so the
`COMMENT.sub` at `:189` is unchanged. No OS boundary is crossed.

```python
# A workflow's trigger key at the start of a line, bare or in either quote,
# and the text after its colon. The colon ends the line or a space follows it:
# `on:pull_request` is one plain scalar in YAML, not the key.
ON_KEY = re.compile(r"""^(?:on|"on"|'on')\s*:(\s.*|)$""")
# A mapping key in a block line: the text before the first colon that ends the
# line or that whitespace follows. `pull_request:foo` is one scalar, not a key.
KEY = re.compile(r"(.*?):(?:\s|$)")
```

```python
        key = KEY.match(item)
        under_key = key is not None
        if is_item:
            entries.append(item[1:])
        elif key:
            entries.append(key.group(1))
        else:
            bare.append(item)
```

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
            "on:\n  pull_request:foo\n",
            "on:\n  pull_request:foo\n    push\n",
            "on:pull_request\n",
        ...
            "a-name-glued-to-a-colon",
            "a-glued-name-continued-on-a-deeper-line",
            "an-on-key-glued-to-its-value",
```

Each parameter is to be seen red at `274317f3` before the fix lands
(contract rule 15). The probe printed `answers` at exit 0 there for the
first two. The third rests on the reading above and has not been run.

answer:

## Confirmations

confirms: round-2#1
The fix pass claimed that a deeper line under an entry with no colon, a bare
name or a `- name` item, now makes the block unread, and that a deeper line
under a key still belongs to the key. `block_entries` refuses at `:141-143`
when the entry above held no colon (read). The probe ran round 2's shapes
again (executed). `on:` / `  pull_request` / `    push`, the same with
`closed`, and `on:` / `  - pull_request` / `    closed` printed `answers` at
exit 0 at `b0fd17c3` and print `unread ... (trigger unread, not counted)` at
exit 1 at `274317f3`. The class enumerated wider also reads as unread at
`274317f3`. That covers a `- ` item at indent zero continued below,
a blank line between the name and the deeper line, a comment line between
them, a quoted name, a tab-indented deeper line and CRLF line endings
(executed). YAML loads the item shapes as `['pull_request closed']` and the
blank-line shape as `'pull_request\npush'`, and refuses the comment-between
shape (executed). The readings that should stand, stand.
`on:` / `  pull_request` / `    # note` answers. So do `pull_request:` with
`types:` below it, and `pull_request: x` / `    y`, which YAML loads as
`{'pull_request': 'x y'}` (executed). f23464df removed `not is_item and` from
`under_key`, claiming a `- ` item holding a colon is never an event name.
`on:` / `  - pull_request:` / `      types: [opened]` prints `unread` at
`b0fd17c3` and at `274317f3` alike, because the entry ` pull_request:` fails
`EVENT_NAME` at `:202` (executed, read). The condition was dead, as
claimed. Finding 1 above is a separate cause, as its grounds say.

confirms: round-2#2
`continued` at `:157-165` runs before both inline arms, at `:192-193`
(read). `on: pull_request` / `  push` and `on: [pull_request]` / `  push`
printed `answers` at exit 0 at `b0fd17c3`. At `274317f3` they print `unread`
at exit 1. So do a blank line before the indented line, a quoted value and a
tab-indented line (executed). YAML refuses `on: [pull_request]` / `  push`
(executed). `on: pull_request` / `  # the run` and a whitespace-only line
below the value still answer at exit 0 (executed). The check reads only the
first line below that is neither blank nor a comment, and an indented line
there continues the value or is refused by YAML; no shape the probe tried
was a valid trigger that the check refused.

confirms: none
The fix pass claimed four new S5 parameters red at `b0fd17c3`, two S4
parameters, and 43 cases in the module. `bin/test
tests/skills/test_deferral_check.py --collect-only` collected 43 (executed).
The four S5 strings at `tests/skills/test_deferral_check.py:195-198` are the
probe's shapes, and each printed `answers` at exit 0 at `b0fd17c3`, where S5
asks for exit 1 (executed). So each was red there. The two S4 parameters at
`:162-163` are the only ones in their group with a comment on its own line
below the name. One holds the comment skip ahead of the new refusal in
`block_entries`, and the other holds the comment drop in `continued` (read
`tests/skills/test_deferral_check.py:153-215`). Neither repeats a case its
group already holds.

confirms: none
The fix pass named `changelog.md` as still true. Each of its sentences was
read against the code at `274317f3`. The three key spellings are `ON_KEY` at
`:94`. A block at any consistent indent is `:137-144`, and an event key with
a value or a comment is `:129` and `:148-149`. A flow list closed on its line
is `:194-198`. The unread shapes it names after "such as" print the `unread`
line at `:310` and do not resolve the deferral (S5 and S6, executed in the
narrow run below). The limit line carries the filters clause at `:86-88`.
The sentence on the base's `answers ... (trigger unread)` output for
push-only `"on":` and four-space spellings rests on round 1's probe, carried.
Finding 1 changes no sentence of it: `pull_request:foo` is not an event key,
so "an event key that carries a value" stays true after its fix.

confirms: none
The docstrings match the code. `block_entries` names three shapes that make
the block unread at `:119-125`. They are the shallower line at `:139-140`,
the bare name beside another entry at `:152-153`, and the deeper line under
an entry with no colon at `:141-143` (read). `read_events` adds the continued
inline value at `:178-179`, which is `:192-193` (read). The module
docstring's five outcomes at `:14-21` did not change (read).

confirms: none
The fix pass's record edit is two lines per finding. `git diff
b0fd17c3..274317f3 -- seal` changes the `verdict:` and `answer:` lines of
round 2's two findings and nothing else (executed). d8edc4a6 changes
`skills/verify/scripts/deferral_check.py` and
`tests/skills/test_deferral_check.py`, which both findings' `location:`
lines name (executed).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* names the full
suite, the repository-wide `ruff check` and `ruff format --check`, and the
typecheck, with the orchestrator through `seal gate` as the answerer (read).
This round ran none of the three.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's `seal mutate` result: 7 mutants over the new arm, 6 red and one equivalent, removed in f23464df, then 6 of 6 red. Not re-run this round. A mutation score licenses tested, never safe: finding 1 is a branch the colon test lacks, and no mutant of the existing code shows it | `skills/verify/scripts/deferral_check.py:141-145`, `:157-165` | the sealer, in its sample of the crafter's claims |
| The fix pass's run of 3862 passed over 48 modules. Not re-run; this round's narrow run is the eight modules below | the branch at `274317f3` | the orchestrator, through `seal gate` |
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the branch at `274317f3` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_r3.py`, in the clone at `274317f3`: one temporary project per trigger shape with a `pytest` step, run through the scripts of `8d8d6390`, `b0fd17c3` and `274317f3` (`git show <rev>:skills/verify/scripts/deferral_check.py`) with `--kind tests` | Exit 0, 25 shapes. Round 2's continued bare name, with `push` or `closed` below, its continued inline name, the continued `- ` item and the continued inline list: `answers` exit 0 at `8d8d6390` and `b0fd17c3`, `unread` exit 1 at `274317f3`. The same at `274317f3` for a `- ` item at indent zero continued, a blank line or a comment line between a name and its deeper line, a quoted name continued, a tab-indented continuation of a name or an inline value, a blank line between an inline value and its continuation, a quoted inline value continued, and CRLF endings. A comment line below a block name or an inline name, a whitespace-only line below an inline name, `pull_request:` with `types:` below, `pull_request: x` / `    y`, `on: pull_request` and a two-key block: `answers` exit 0 at all three. `- pull_request:` with `types:` below and `-` / `    pull_request`: `unread` exit 1 at `b0fd17c3` and `274317f3`. `on:` / `  pull_request:foo`, alone or with `    push` below: `answers (trigger unread)` exit 0 at `8d8d6390`, `answers (on pull_request)` exit 0 at `b0fd17c3` and `274317f3`. The file and its projects were deleted after its one run |
| `uv run --no-project --with pyyaml python3 -I -c 'import yaml; yaml.safe_load(...)'` over 12 of the shapes above | `on:` / `  pull_request:foo` loads as `{True: 'pull_request:foo'}`, and with `    push` below as `'pull_request:foo push'`; `on:` / `  pull_request:{}` as `'pull_request:{}'`. `on:pull_request` raises `ScannerError`, `"on":pull_request` raises `ParserError`. `on:` / `  - pull_request` / `    closed` and the same at indent zero load as `['pull_request closed']`. `on:` / `  pull_request` / blank / `    push` loads as `'pull_request\npush'`. `pull_request: x` / `    y` loads as `{'pull_request': 'x y'}`. `-` / `    pull_request` loads as `['pull_request']`. `on: [pull_request]` / `  push` and a comment line between a name and its deeper line raise `ParserError` |
| `bin/test tests/skills/test_deferral_check.py tests/test_censuses.py -q -p no:xdist` | 218 passed, exit 0 |
| `bin/test tests/skills/test_deferral_check.py tests/test_censuses.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/skills/test_coordinates.py tests/skills/test_test_layout.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py -q -p no:xdist` | 423 passed, 8 skipped, exit 0 |
| `bin/test tests/skills/test_deferral_check.py -q -p no:xdist --collect-only` | 43 tests collected, exit 0 |
| `git -C <clone> diff b0fd17c3..274317f3 -- seal`, `git -C <clone> show --stat d8edc4a6 f23464df`, `git -C <clone> blame -L 145,150 274317f3 -- skills/verify/scripts/deferral_check.py` | The record diff changes two `verdict:` and two `answer:` lines. d8edc4a6 touches the script and the test module, f23464df the script. Lines 146 to 150 come from 87ec5583, an ancestor of `b0fd17c3`; line 145 from f23464df |
