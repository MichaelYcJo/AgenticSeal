# Review round 4: 1793251201-a-push-only-workflow-answers-a-deferral

target: 13b15928, fixes cd259e77..13b15928

Extended past round 3, counting from round 1: round 3 found 1, round 2 found 2, and none is a regression.

This round verifies the fix diff. It ran in a `git clone --no-local` of the
branch at `13b15928`. Earlier rounds handed over four things, and this round
carried them without establishing them again. The first is the probe method:
the script of a revision comes from
`git show <rev>:skills/verify/scripts/deferral_check.py` and runs over one
temporary project per trigger shape. The second is round 3's YAML readings,
among them `on:` / `  pull_request:foo` loading as `{True: 'pull_request:foo'}`
and `on:pull_request` raising `ScannerError`. The third is `seal layout
--pairs`, which names no pair in `tests/skills/test_deferral_check.py`. The
fourth is round 3's list of narrow modules, which this round ran again. Every
verdict below was reached on the code at `13b15928`.

## Findings

### 1. A colon followed by a Unicode space still reads as a key, so a trigger GitHub runs nothing on answers a deferral

severity: should
location: `skills/verify/scripts/deferral_check.py:95`, `skills/verify/scripts/deferral_check.py:98`, `skills/verify/scripts/deferral_check.py:101`, `skills/verify/scripts/deferral_check.py:108`, `skills/verify/scripts/deferral_check.py:195`, `tests/skills/test_deferral_check.py:183-221`
evidence: executed `python3 -I test_tmp_r4.py <clone> <work>`, `uv run --no-project --with pyyaml python3 -I -c 'import yaml; yaml.safe_load(...)'`
verdict: open
reopens: round-3#1

The close of round-3#1 holds for an ASCII letter glued to the colon and not
for the whole class it named. Round-3#1 asked that a colon count as a key's
only where YAML white space follows it, since text glued to the colon makes
one scalar. e8dc9313 wrote that test as `\s` in `KEY` (`:98`) and in `ON_KEY`
(`:95`). In a Python `str` pattern, `\s` also matches U+00A0 (no-break
space), U+2003, U+3000 and the other Unicode spaces. YAML 1.1 and 1.2 both
count only a space and a tab as white space inside a line, so to YAML each of
those characters is text glued to the colon. The defect is older than the fix
pass: `cd259e77` answered on each shape below as well (executed). No fix
pass's commit made it, so the line is `reopens:` and not `regression:`.

The probe ran three revisions over each shape. `on:` / `  pull_request:`
U+00A0 `foo` loads in YAML as `{True: 'pull_request:\xa0foo'}`, one scalar
(executed). At `13b15928` it prints `answers ... (on pull_request)` at exit 0.
The same holds with U+2003 or U+3000 in place of U+00A0. `on:` U+00A0
`pull_request` raises `ScannerError` in YAML, so GitHub runs nothing from the
file. At `13b15928` it also prints `answers` at exit 0, through `ON_KEY`'s
`(\s.*|)`. The ASCII shapes the fix was written for read as unread at
`13b15928`, as claimed: `pull_request:foo`, `pull_request:x: y`,
`on:pull_request` and the dropped `pull_request:foo` / `    push` each print
`unread` at exit 1 (executed). Each Unicode shape is the fail-open #1123
closes. `SECURITY.md` *What is in scope* counts a check that fails open as a
security defect, as round 2 and round 3 recorded for their shapes.

Under contract rule 12 the cause is wider than the two patterns. The cause is
that Python's `\s` and a bare `str.strip()` stand in for YAML's space and tab.
Three more sites outside the fix diff answer on a trigger GitHub runs nothing
on (executed):

- `on: pull_request` U+00A0 loads as `'pull_request\xa0'`. The `.strip()` at
  `:195` drops the space, and the shape prints `answers` at exit 0.
- `on:` / `  pull_request` U+00A0 `:` loads as the key `'pull_request\xa0'`.
  `unquoted` at `:108` strips it, and the shape prints `answers` at exit 0.
- `on: pull_request` U+00A0 `#x` loads as `'pull_request\xa0#x'`, since YAML
  opens a comment only after a space or a tab. `COMMENT` at `:101` takes the
  U+00A0 as white space and drops `#x`, and the shape prints `answers` at
  exit 0.

A mutant that writes `[ \t]` in `KEY` and `ON_KEY` alone turned the first two
shapes `unread` and left these three answering (executed), so the patterns
alone do not close the class. Three more sites read this way and were not
probed: the `\s*` before the colon in `ON_KEY`, and the `strip()`, `lstrip()`
and `isspace()` that measure an item and its indent in `block_entries`
(`:135`, `:138`) and in `continued` (`:169-170`). The fix pass enumerates
them under rule 12.

The fix gives the module one name for YAML's in-line white space and uses it
at each site. `SPACE` is a new name, defined here. Lines come from
`str.splitlines()`, so none holds a line break, and no OS boundary is
crossed.

```python
# YAML's white space inside a line is a space or a tab. Python's `\s` and a
# bare `str.strip()` also take U+00A0 and the other Unicode spaces, which YAML
# reads as text: `pull_request:` then U+00A0 then `foo` is one scalar.
SPACE = " \t"  # new name, defined here
ON_KEY = re.compile(r"""^(?:on|"on"|'on')[ \t]*:([ \t].*|)$""")
KEY = re.compile(r"(.*?):(?:[ \t]|$)")
COMMENT = re.compile(r"(?:^|[ \t])#.*$")
```

```python
def unquoted(value):
    """VALUE stripped of YAML white space, with one pair of matching quotes
    around it dropped."""
    value = value.strip(SPACE)
```

```python
        value = COMMENT.sub("", key.group(1)).strip(SPACE)
```

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
            "on:\n  pull_request:\xa0foo\n",
            "on:\xa0pull_request\n",
            "on: pull_request\xa0\n",
            "on:\n  pull_request\xa0:\n",
            "on: pull_request\xa0#x\n",
        ...
            "a-name-glued-to-a-colon-by-a-unicode-space",
            "an-on-key-glued-to-its-value-by-a-unicode-space",
            "an-inline-name-ending-in-a-unicode-space",
            "a-key-ending-in-a-unicode-space",
            "a-comment-sign-after-a-unicode-space",
```

Each parameter is to be seen red at `13b15928` before the fix lands (contract
rule 15). The probe printed `answers` at exit 0 there for all five
(executed).

answer:

## Confirmations

confirms: none
The fix pass claimed two new parameters red at `cd259e77`. The probe ran
`cd259e77`'s script, which is `f23464df`'s (`git diff --stat` printed
nothing, executed). `on:` / `  pull_request:foo` and `on:pull_request` each
printed `answers ... (on pull_request)` at exit 0 there, where S5 asks for
exit 1 (executed). So both were red. `on:` / `  pull_request:x: y`, which
d27c214e added, printed `answers` at exit 0 under the same script
(executed). YAML loads it as `{'pull_request:x': 'y'}` (executed).

confirms: none
The fix pass claimed three mutants red after d27c214e: the old `ON_KEY`, a
`KEY` with no lookahead, and the old `partition(":")` arm. The probe built
each from `13b15928`'s script and ran the S4 and S5 shapes through it
(executed). The old `ON_KEY` failed S5 on `on:pull_request` alone. The `KEY`
with no lookahead failed it on `pull_request:foo` and `pull_request:x: y`. The
old `partition` arm failed it on `pull_request:x: y` alone. The probe checks
the S4 and S5 outcomes only and not the whole module, which can only add red.

confirms: none
The dropped parameter was weighed against round 3's proposal. Round 3
proposed `a-glued-name-continued-on-a-deeper-line` because the fix pass's
`under_key = ":" in item` read the same colon as the key arm. After
e8dc9313, `KEY` decides both at `:150-151` (read). The mutant that restores
`under_key = ":" in item` failed no S4 or S5 shape, and the dropped shape
printed `unread` at exit 1 under it and under `13b15928` alike (executed).
By reading, a line that holds a colon `KEY` does not read is a bare name or a
`- ` item whose text keeps the colon. `EVENT_NAME` at `:208` refuses either,
so the block is unread either way, as the fix pass's answer says. The deeper
line in the dropped shape reaches the refusal at `:146-148`, which
`a-name-continued-on-a-deeper-line` already holds. The drop holds.

confirms: none
Each new parameter covers something its group does not. `an-on-key-glued-to-its-value`
is the one S5 shape the old `ON_KEY` fails, and `a-key-holding-a-glued-colon`
the one the old `partition` arm fails (executed, above).
`a-name-glued-to-a-colon` is the one parameter whose colon line reaches the
bare arm at `:156-157` (read `tests/skills/test_deferral_check.py:183-221`).
`bin/test tests/skills/test_deferral_check.py --collect-only` collected 46,
as claimed (executed).

confirms: none
The fix pass claimed `runners_in`'s colon test at `:225` decides nothing about
a trigger. The `re.sub` there trims a `run:`, `entry:` or `script:` label off
`cmd` after `re.search` at `:224` has already decided the line runs the kind,
and `cmd` is only printed (read `skills/verify/scripts/deferral_check.py:214-229`).
The claim holds.

confirms: none
The text the fix changed matches the code. The comment above `ON_KEY` and
`KEY` at `:92-98` and the `block_entries` docstring at `:120-130` describe a
colon that ends the line or that whitespace follows, which is what the two
patterns do (read). Finding 1 changes what "whitespace" has to mean there.
`changelog.md` names "an event key that carries a value or a comment", which
stays true (read).

confirms: none
The fix pass's record edit is two lines. `git diff cd259e77..13b15928 --
seal` changes the `verdict:` and `answer:` lines of round 3's finding and
nothing else (executed). e8dc9313 changes
`skills/verify/scripts/deferral_check.py` and
`tests/skills/test_deferral_check.py`, which the finding's `location:` line
names (executed).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* names the full
suite, the repository-wide `ruff check` and `ruff format --check`, and the
typecheck, with the orchestrator through `seal gate` as the answerer (read).
This round ran none of the three.

## Not judged

| What | Location | Who answers |
|---|---|---|
| A tab after a colon. PyYAML, a YAML 1.1 parser, raises `ScannerError` on `on:` / `  pull_request:` tab `foo` and on `on:` tab `pull_request`, and `13b15928` prints `answers` at exit 0 for both (executed). YAML 1.2 lets a tab separate there. Which reading GitHub's workflow parser takes was not established, so finding 1's fix keeps the tab in `SPACE` | `skills/verify/scripts/deferral_check.py:95`, `:98` | the fix pass, which settles the separator set, and the orchestrator, who names the choice in the pull request body |
| The fix pass's `seal mutate` run over the module. This round's mutants ran over the S4 and S5 shapes only | `skills/verify/scripts/deferral_check.py:92-160` | the sealer, in its sample of the crafter's claims |
| The fix pass's run of 3865 passed over 48 modules. Not re-run; this round's narrow run is the eight modules below | the branch at `13b15928` | the orchestrator, through `seal gate` |
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the branch at `13b15928` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_r4.py <clone> <work>`, in the round's scratch directory: one temporary project per trigger shape with a `pytest` step, run with `--kind tests` through the scripts of `8d8d6390`, `cd259e77` and `13b15928`, and through five mutants of `13b15928`'s script, each substitution asserted to match | Exit 0, 36 shapes per script. At `cd259e77`, S4 and S5 failed on `pull_request:foo`, `pull_request:x: y` and `on:pull_request` alone. At `13b15928`, no S4 or S5 shape failed, and the dropped `pull_request:foo` / `    push` printed `unread` exit 1. Mutants: old `ON_KEY` failed 1 shape, `KEY` with no lookahead 2, old `partition` arm 1, `under_key = ":" in item` 0, `[ \t]` in `KEY` and `ON_KEY` 0. At `13b15928`, `pull_request:` with U+00A0, U+2003 or U+3000 then `foo`, `on:` U+00A0 `pull_request`, `on: pull_request` U+00A0, `pull_request` U+00A0 `:`, `on: pull_request` U+00A0 `#x`, `pull_request:` tab `foo` and `on:` tab `pull_request` printed `answers (on pull_request)` exit 0; `- pull_request:` U+00A0 `foo` printed `unread` exit 1. Under the `[ \t]` mutant, the U+00A0, U+2003 and U+3000 colon shapes and `on:` U+00A0 printed `unread` exit 1, and the other three U+00A0 shapes and both tab shapes still answered. The file, its projects and its script copies were deleted after its one run |
| `uv run --no-project --with pyyaml python3 -I -c 'import yaml; yaml.safe_load(...)'` over ten of the shapes above | `pull_request:` U+00A0 `foo` loads as `'pull_request:\xa0foo'`, and with U+2003 or U+3000 the same way. `on:` U+00A0 `pull_request`, `pull_request:` tab `foo` and `on:` tab `pull_request` raise `ScannerError`. `on: pull_request` U+00A0 loads as `'pull_request\xa0'`, `pull_request` U+00A0 `:` as `{'pull_request\xa0': None}`, `on: pull_request` U+00A0 `#x` as `'pull_request\xa0#x'`, and `pull_request:x: y` as `{'pull_request:x': 'y'}` |
| `bin/test tests/skills/test_deferral_check.py -q -p no:xdist --collect-only` | 46 tests collected, exit 0 |
| `bin/test tests/skills/test_deferral_check.py tests/test_censuses.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/skills/test_coordinates.py tests/skills/test_test_layout.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py -q -p no:xdist` | 426 passed, 8 skipped, exit 0 |
| `git -C <clone> diff cd259e77..13b15928 -- seal`, `git -C <clone> show --stat e8dc9313`, `git -C <clone> diff --stat f23464df cd259e77 -- skills/verify/scripts/deferral_check.py` | The record diff changes one `verdict:` and one `answer:` line. e8dc9313 touches the script and the test module. The script is the same at `f23464df` and `cd259e77` |
