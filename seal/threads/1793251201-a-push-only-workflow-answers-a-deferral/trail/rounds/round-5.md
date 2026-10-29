# Review round 5: 1793251201-a-push-only-workflow-answers-a-deferral

target: 53f28d009, fixes 1943fe760..53f28d009

This round verifies the fix diff. It ran in a `git clone --no-local` of the
branch at `53f28d009`, under the round's scratch directory. Earlier rounds
handed over four things, and this round carried them without establishing
them again. The first is the probe method: the script of a revision comes
from `git show <rev>:skills/verify/scripts/deferral_check.py` and runs over
one temporary project per trigger shape. The second is round 3's and round
4's YAML readings of their shapes. The third is `seal layout --pairs`, which
names no pair in `tests/skills/test_deferral_check.py`. The fourth is round
4's list of narrow modules, which this round ran again. Every verdict below
was reached on the code at `53f28d009`.

The fix pass's account was read as claims: the five proposed parameters and
`a-block-line-opened-by-a-unicode-space` red at `1943fe760`; ten mutants,
seven red, two survivors pinned by `6f6650392`, one equivalent; 56 cases in
the module; 3875 passed over 48 modules. What each claim met is below.
Findings 1 to 3 stand in units the fix pass's commits added. Findings 4 and
5 are older than the fix pass and name no earlier finding.

## Findings

### 1. The fix narrowed the `on` key's test before its colon, and no case watches it, so putting the old test back passes the module

severity: should
location: `skills/verify/scripts/deferral_check.py:102`, `tests/skills/test_deferral_check.py:185-241`
evidence: executed `bin/seal mutate skills/verify/scripts/deferral_check.py --replace OLD NEW (13 pairs) --tests "bin/test tests/skills/test_deferral_check.py -q -p no:xdist -x"`, `python3 -I test_tmp_r5.py <clone> <work>`, `uv run --no-project --with pyyaml --with ruamel.yaml python3 -I yaml_r5.py`
verdict: open
regression: round-4#1

The unit is `ON_KEY` at `:102`, which 276585926 rewrote on both sides of the
colon. The phase row of `frame/plan.md` verifies the build by cases seen red
and by `seal mutate` over `read_events`; 276585926 narrowed the test before
the colon to `{SPACE_CHAR}*` and added no parameter that holds another space
there; the defect came from the fix pass's rule 12 enumeration, which
widened the code past the record's five parameters without widening the
cases.

The fix pass claimed seven of its ten mutants red, and named three
survivors: the `strip()` in `continued`, the trailing-comma test and the
indent's `lstrip()`. This round ran thirteen mutants over the module at
`53f28d009` (executed). Mutant 1 puts back `\s*` before the colon, and it
survived. Under it, `on` then U+00A0 then `: pull_request` reads as the key
again and answers. `1943fe760`, which held that `\s*`, printed
`answers ... (on pull_request)` at exit 0 for that shape (executed).
`53f28d009` prints `unread` at exit 1 for it (executed). PyYAML and
ruamel.yaml both load the shape as `{'on\xa0': 'pull_request'}`, a file with
no `on` key, so GitHub runs nothing from it (executed). The behaviour is
right today, and nothing keeps it right.

Mutant 2 puts back `\s` after the colon, and it also survived. That
mutant is inert on any one `on` line. A value it lets in opens with a space
that `strip(SPACE)` keeps, so `EVENT_NAME` refuses it at `:222`, and the
trigger is unread either way (read `:209-224`). The two differ only where a
later line also opens with `on:`, and the scan reads the first matching line
by design, at the base as now. It needs no case. Mutants 7 and 10, the two
survivors the fix pass named, are red at `53f28d009`. Mutant 9, the indent's
`lstrip()`, survived, and it is equivalent, as the second entry of
`## Confirmations` records. So the account's three survivors and this
round's three are not the same three.

The fix is one parameter, seen red at `1943fe760`, where the probe printed
`answers` at exit 0. Seen red at `53f28d009` means under mutant 1, which
`bin/seal mutate` writes and restores.

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
            "on\xa0: pull_request\n",
        ...
            "an-on-key-ending-in-a-unicode-space",
```

answer:

### 2. A new case covers nothing its group does not, and it was never seen red

severity: should
location: `tests/skills/test_deferral_check.py:210`, `tests/skills/test_deferral_check.py:237`
evidence: executed `bin/seal mutate skills/verify/scripts/deferral_check.py --replace OLD NEW (13 pairs) --tests "bin/test tests/skills/test_deferral_check.py -q -p no:xdist -x --deselect <the case>"`, `bin/seal mutate skills/verify/scripts/deferral_check.py --replace OLD NEW (13 pairs) --tests "bin/test <the case> -q -p no:xdist -x"`, `python3 -I test_tmp_r5.py <clone> <work>`
verdict: open
regression: round-4#1

The unit is the parameter `an-inline-name-above-a-line-opened-by-a-unicode-space`
(`on: pull_request` above U+00A0 then `push`), which 276585926 added. The
design's S5 and the plan's phase row ask for each parameter seen red;
276585926 added this one, green at `1943fe760`, to pin the `isspace()` that
`continued` keeps at `:184`; the defect came when 6f6650392 pinned a
survivor in the same function with
`an-inline-name-above-a-line-of-a-unicode-space`, which also kills the one
mutant this parameter kills.

The new parameter was green at `1943fe760`. That script printed `unread` at
exit 1 for it, as `53f28d009` does (executed). The fix pass's answer does
not claim it red. Over the thirteen mutants, the module with this parameter
deselected gives the same verdict for every mutant as the whole module
(executed). Run alone, the parameter kills one mutant, mutant 12, which
writes `code[0] in SPACE` at `:184`. The later parameter kills mutant 12 as
well: with both deselected, mutant 12 survives (executed). By reading, both
shapes take the same path through `continued`. The first line below is not
blank after `strip(SPACE)`, and `code[0]` is U+00A0 in both (read
`:181-185`). `agents/crafter.md` *A new test starts from its group* adds a
case only where it covers something its group does not.

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
# delete the trigger "on: pull_request\n\xa0push\n" and its id
# "an-inline-name-above-a-line-opened-by-a-unicode-space"
```

answer:

### 3. Two comments the fix wrote state a rule and a count the code does not keep

severity: should
location: `skills/verify/scripts/deferral_check.py:92-95`, `skills/verify/scripts/deferral_check.py:131-140`
evidence: read `skills/verify/scripts/deferral_check.py:92-98`, `skills/verify/scripts/deferral_check.py:122-185`
verdict: open
regression: round-4#1

The units are the comment above `SPACE` at `:92-95`, which 276585926 added,
and the `block_entries` docstring at `:131-140`, which it changed. The
design's S10 holds the module's text to its code; 276585926 appended a
sentence beside each rule it amended instead of rewriting the rule; the
defect came from that append.

The `SPACE` comment says "every reader below strips and matches this and
nothing wider". Two readers test wider on purpose: `item[0].isspace()` at
`:148` and `code[0].isspace()` at `:184`. The answer of round 4 names both
as deliberate, and finding 2's mutant 12 shows what narrowing `:184` to
`SPACE` does: the module goes red because the trigger then answers. A
reader who follows the comment makes that change. The docstring says "Three
shapes make the whole block unread" and then lists three. Its last sentence
adds a fourth with "too". A count that does not match its list is the
defect the design's *Removes* table fixed in the module docstring.

```python
# YAML's white space inside a line: a space or a tab, the tab as YAML 1.2
# reads it. Python's `\s` and a bare `str.strip()` also take U+00A0 and the
# other Unicode spaces, which YAML reads as text, so every reader below
# strips and matches this. Two tests are wider on purpose, and both only
# refuse: `block_entries` and `continued` read a line whose text opens with
# any other space as unread.
SPACE = " \t"
```

```python
    The block's indent is its first entry's: one space or more, or zero
    where that entry is a `- ` item. A deeper line under a key belongs to
    that key and is skipped. A line at indent zero that is not a `- ` item
    ends the block. Four shapes make the whole block unread, an empty
    list: a line whose text, after SPACE, opens with any other space,
    which YAML reads as text and no key or event name starts with; a line
    shallower than the block but not at zero, which no valid workflow
    holds; a line at the block's indent that is neither a key nor an item
    beside any other entry; and a deeper line under an entry that holds no
    key, a bare name or a `- name` item, which continues that name, so
    that `  pull_request` above `    push` is the one name
    "pull_request push". A key is what `KEY` reads: text before a colon
    that ends the line or that SPACE follows.
```

answer:

### 4. A tab in a block line's indentation is read as indentation, so a trigger no YAML parser loads answers a deferral

severity: should
location: `skills/verify/scripts/deferral_check.py:150`, `tests/skills/test_deferral_check.py:185-241`
evidence: executed `uv run --no-project --with pyyaml --with ruamel.yaml python3 -I test_tmp_r5_tabs.py <clone> <work>`
verdict: open

The fix pass's answer keeps the tab in `SPACE` "as YAML 1.2 reads it", and
276585926 measures the indent with `code.lstrip(SPACE)` at `:150`. YAML
indents with spaces alone. The YAML 1.2 specification, section 6.1, says
tab characters must not be used in indentation (quoted from memory, not
opened this round). `on:` above a tab then `pull_request:` raises
`ScannerError` in PyYAML and in ruamel.yaml (executed). So does the same
block with a bare name, and with one space then a tab (executed). GitHub
runs nothing from such a file. `53f28d009` prints `answers ... (on
pull_request)` at exit 0 for all three (executed). Each is the fail-open
#1123 closes, and `SECURITY.md` *What is in scope* counts a check that fails
open as a security defect.

The defect is older than the fix pass. `8d8d6390` and `1943fe760` printed
`answers` at exit 0 for the same three shapes (executed), measuring the
indent with a bare `lstrip()`. No fix pass's commit made it, so the finding
carries neither a `regression:` nor a `reopens:` line. It is not round-4#1
standing: round 4 read the tab as YAML white space, inside a line, and
its paste-ready fix kept it. Under contract rule 12, `:150` is the one
place the script measures an indent. `continued` at `:184` already takes a
line opened by a tab as a continuation, so the trigger is unread there
(read `:181-185`). The tab after a colon is another question, and it is a
row of `## Not judged`.

The fix refuses a tab among a line's leading white space. `lead` is a new
name, defined here. Lines come from `read_events`, so none holds a line
break, and no OS boundary is crossed.

```python
        if item[0].isspace():
            return []
        lead = code[: len(code) - len(code.lstrip(SPACE))]  # new name, defined here
        # YAML indents with spaces alone: a tab among a line's leading white
        # space is refused by every YAML parser, so the block is unread.
        if "\t" in lead:
            return []
        indent = len(lead)
```

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
            "on:\n\tpull_request:\n",
        ...
            "a-block-key-indented-by-a-tab",
```

The parameter is to be seen red at `53f28d009` before the fix lands
(contract rule 15). The probe printed `answers` at exit 0 there (executed).

answer:

### 5. `splitlines()` breaks a line where YAML does not, so a comment's text is read as the trigger and a push-only run answers a deferral

severity: should
location: `skills/verify/scripts/deferral_check.py:203-204`, `tests/skills/test_deferral_check.py:126-151`
evidence: executed `python3 -I test_tmp_r5.py <clone> <work>`, `uv run --no-project --with pyyaml --with ruamel.yaml python3 -I yaml_r5.py`, `git -C <worktree> log -S'exempt from splitlines: YAML keys' -- skills/verify/scripts/deferral_check.py`
verdict: open

This round opened it outside the fix diff, while enumerating the class of
round-4#1's cause: a Python character class standing in for YAML's. Round
4's paste-ready fix rested on "Lines come from `str.splitlines()`, so none
holds a line break". `str.splitlines()` also breaks at U+2028, U+2029,
U+0085, U+000B, U+000C and U+001C to U+001E. YAML 1.2 breaks a line only at
a line feed or a carriage return.

`# note` U+2028 `on: pull_request` above `on: push` is one comment line and
a push trigger in YAML 1.2. ruamel.yaml refuses the file with
`ParserError`, and PyYAML, a YAML 1.1 parser that does break at U+2028,
loads it as `{True: 'push'}` (executed). No reading runs it on a pull
request. `read_events` returns at the first line `ON_KEY` matches, and
`splitlines()` hands it `on: pull_request` from inside the comment (read
`:203-224`). `1943fe760` and `53f28d009` print `answers ... (on
pull_request)` at exit 0 (executed). This is the fail-open #1123 closes.

The defect is older than the work item. The exemption
`# exempt from splitlines: YAML keys` at `:203` came with cbf97bf55, before
this branch (executed `git log -S`). `tests/censuses.py#splitlines` asks
for that exemption because `.splitlines(` ends a line where another reader
does not (read `tests/censuses.py:667-691`). No fix pass's commit made it,
and it names no earlier finding. Under contract rule 12, `runners_in` at
`:232` also splits with `splitlines()`. It finds runner commands and
decides no trigger, so it stands.

The fix splits on the line feed alone. It assumes `read` opened the file
with universal newlines, which `open(path, encoding="utf-8",
errors="replace")` at `:283` does, so a carriage return is already a line
feed. `inspect` is the one caller of `read_events`, and it passes `read`'s
text (read `:294-299`). The exemption comment goes, since nothing is left
for it to excuse.

```python
    # `read` opened the file with universal newlines, so "\r\n" and "\r" are
    # "\n" already, and YAML 1.2 breaks a line nowhere else. `splitlines()`
    # also breaks at U+2028, U+2029, U+0085, U+000B, U+000C and U+001C to
    # U+001E, inside what YAML reads as one line.
    lines = text.split("\n")
```

```python
# tests/skills/test_deferral_check.py, test_a_push_only_trigger_in_each_spelling_is_too_late
            "# note" + chr(0x2028) + "on: pull_request\non: push\n",
        ...
            "a-comment-holding-a-line-separator-above-the-trigger",
```

The parameter is to be seen red at `53f28d009` before the fix lands
(contract rule 15). The probe printed `answers` at exit 0 there (executed).

answer:

## Confirmations

confirms: round-4#1
The fix pass claimed the five proposed parameters red at `1943fe760`, whose
script is `13b15928`'s. The probe ran `1943fe760`'s script over each
(executed). `pull_request:` U+00A0 `foo`, `on:` U+00A0 `pull_request`,
`on: pull_request` U+00A0, `pull_request` U+00A0 `:` and
`on: pull_request` U+00A0 `#x` each printed `answers ... (on pull_request)`
at exit 0 there. Each prints `unread ... (trigger unread, not counted)` at
exit 1 at `53f28d009` (executed). The three sites round 4 named unprobed
were narrowed as asked. The `\s*` before the `on` colon is `SPACE_CHAR` at
`:102`, and `on` U+00A0 `: pull_request` now reads as unread, though no case
watches it (finding 1). The item strip and the indent are `strip(SPACE)` and
`lstrip(SPACE)` at `:145` and `:150`, and the blank test in `continued` is
`strip(SPACE)` at `:183` (read). The two wider sites were weighed against
round 4's paste-ready fix, which changed neither function. The guard at
`:148` makes the block unread where a line opens with another space. Without
it, `on:` / `  pull_request:` / U+00A0 ` push:` measures indent 0 under
`lstrip(SPACE)`, ends the block and answers. Mutant 11 removes the guard and
goes red (executed). `1943fe760` printed `answers ... (on pull_request,
push)` for that shape (executed). The guard also reaches a deeper line under
a key: `pull_request:` above U+00A0 `branches: [main]` now reads as unread.
Both parsers load that key as `'\xa0branches'` (executed). So the cost is a
refusal of an event filter no workflow writes, and its cause is printed.
Keeping `isspace()` in `continued` at `:184` refuses a line opened by
U+00A0 below an inline name. YAML reads that line as text at column zero.
Mutant 12 narrows the site to `SPACE` and goes red, because the trigger then
answers (executed). Both wider sites refuse where the narrow reading would
answer. They hold. The tab the fix keeps after a colon is a row of
`## Not judged`, and the tab in indentation is finding 4.

confirms: none
The fix pass claimed two survivors, the old `strip()` in `continued` and in
the trailing-comma test, pinned by 6f6650392. `on: pull_request` above a
line of U+00A0, and `on: [pull_request,` U+00A0 `]`, printed `answers` at
exit 0 at `1943fe760` and print `unread` at exit 1 at `53f28d009`
(executed). Mutants 10 and 7 put the old `strip()` back, and both are red
over the module at `53f28d009` (executed). The fix pass claimed the indent's
`lstrip()` equivalent. Mutant 9 survives (executed). By reading,
`code.lstrip()` and `code.lstrip(SPACE)` differ only where the first
character after SPACE passes `isspace()`, and the guard at `:148` has
returned for every such line (read `:144-150`). The claim holds.

confirms: none
The fix pass claimed `a-block-line-opened-by-a-unicode-space` red at
`1943fe760`. That script printed `answers ... (on pull_request, push)` at
exit 0 for it (executed). The fix pass claimed `a-tab-after-the-on-colon`
answers. `53f28d009` prints `answers` at exit 0 for it, and mutant 13, which
drops the tab from `SPACE`, is red over the module (executed). The fix pass
claimed a `-` then a tab is not read as an item. `on:` / `  -` tab
`pull_request` prints `unread` at exit 1, and both parsers raise
`ScannerError` on it (executed).

confirms: none
The fix pass claimed 56 cases in the module. `bin/test
tests/skills/test_deferral_check.py --collect-only` collected 56 (executed).

confirms: none
The fix pass claimed that no sentence of `changelog.md`, `KNOWN_LIMITS`,
`skills/verify/SKILL.md` or the two READMEs speaks of white space. A
`grep -i` for `white space`, `whitespace` and `U+00A0` over the four files
other than `KNOWN_LIMITS` found none (executed). `KNOWN_LIMITS` at `:83-90` names none either (read).
The claim that `runners_in` decides no trigger is carried from round 4's
read, and its lines now stand at `:228-243` (read).

confirms: none
The fix pass's record edit is two lines. `git diff 1943fe760..53f28d009 --
seal` changes the `verdict:` and `answer:` lines of round 4's finding and
nothing else (executed). 276585926 changes
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
| A tab after a colon. `53f28d009` answers on `on:` tab `pull_request`, on `on:` space tab `pull_request`, and on `pull_request:` tab `foo` (executed), and `a-tab-after-the-on-colon` pins the first on the fix pass's ground, "as YAML 1.2 reads it". PyYAML and ruamel.yaml raise `ScannerError` on all three. They also refuse a trailing tab and a tab before a comment (executed), which the YAML 1.2 grammar allows, so neither parser settles how GitHub reads the tab. The design's direction, that a line which excuses a deferral is not taken on doubt, points to refusal. GitHub's parser was not established | `skills/verify/scripts/deferral_check.py:96`, `:102`, `:105`, `tests/skills/test_deferral_check.py:164` | the orchestrator, who names the choice in the pull request body, as round 4's row asked |
| The fix pass's run of 3875 passed over 48 modules. Not re-run; this round's narrow run is the eight modules below | the branch at `53f28d009` | the orchestrator, through `seal gate` |
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the branch at `53f28d009` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_deferral_check.py -q -p no:xdist --collect-only` | 56 tests collected, exit 0 |
| `bin/test tests/skills/test_deferral_check.py tests/test_censuses.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/skills/test_coordinates.py tests/skills/test_test_layout.py tests/behaviour/test_whether_a_line_is_live_is_asked_by_what_the_line_does.py -q -p no:xdist` | 436 passed, 8 skipped, exit 0 |
| `python3 -I test_tmp_r5.py <clone> <work>`: one temporary project per trigger shape with a `pytest` step, run with `--kind tests` through the scripts of `1943fe760` and `53f28d009` | Exit 0, 16 shapes. The five proposed shapes, `a-block-line-opened-by-a-unicode-space`, the line of U+00A0 below an inline name and the flow list ending in U+00A0: `answers` exit 0 at `1943fe760`, `unread` exit 1 at `53f28d009`. U+00A0 then `push` below an inline name, U+2003 then `push` below one, and `-` tab `pull_request`: `unread` exit 1 at both. `on` U+00A0 `: pull_request`, and `pull_request:` above U+00A0 `branches: [main]`: `answers` exit 0 at `1943fe760`, `unread` exit 1 at `53f28d009`. `on:` tab `pull_request` and `pull_request:` tab `foo`: `answers` exit 0 at both. `# note` U+2028 `on: pull_request` above `on: push`: `answers (on pull_request)` exit 0 at both. The file and its projects were deleted after its one run |
| `uv run --no-project --with pyyaml --with ruamel.yaml python3 -I yaml_r5.py`, in the round's scratch directory, over six of the shapes above | `on:` tab `pull_request`, `pull_request:` tab `foo` and `-` tab `pull_request`: `ScannerError` in both. `on` U+00A0 `: pull_request` loads as `{'on\xa0': 'pull_request'}` in both. `pull_request:` above U+00A0 `branches: [main]` loads the key `'\xa0branches'` in both. `# note` U+2028 `on: pull_request` above `on: push`: PyYAML `{True: 'push'}`, ruamel.yaml `ParserError`. The script was deleted after its run |
| `bin/seal mutate skills/verify/scripts/deferral_check.py` with 13 `--replace` pairs and `--tests "bin/test tests/skills/test_deferral_check.py -q -p no:xdist -x"`, run four times: the whole module; the module with `an-inline-name-above-a-line-opened-by-a-unicode-space` deselected; that parameter alone; the module with it and `an-inline-name-above-a-line-of-a-unicode-space` deselected. The pairs, at `53f28d009`: 1 `\s*` before the `on` colon; 2 `\s` after it; 3 `\s` in `KEY`; 4 `\s` in `COMMENT`; 5 `strip()` in `unquoted`; 6 `strip()` on the inline value; 7 `strip()` in the trailing-comma test; 8 `strip()` on the item; 9 `lstrip()` for the indent; 10 `strip()` in the blank test of `continued`; 11 the guard at `:148-149` removed; 12 `code[0] in SPACE` at `:184`; 13 `SPACE = " "` | Whole module: 10 red, mutants 1, 2 and 9 survived, exit 1. With the first parameter deselected: the same verdict for every mutant. That parameter alone: mutant 12 red, every other mutant survived. With both deselected: mutants 1, 2, 9, 10 and 12 survived. Each run restored the file, and `git status` in the clone showed nothing of the script |
| `uv run --no-project --with pyyaml --with ruamel.yaml python3 -I test_tmp_r5_tabs.py <clone> <work>`: 12 tab shapes through the scripts of `8d8d6390`, `1943fe760` and `53f28d009`, and each through both parsers | `on:` above a tab then `pull_request:`, a tab then `pull_request`, and one space then a tab then `pull_request:`: `answers` exit 0 at all three scripts, `ScannerError` in both parsers. Tab after the `on` colon, space then tab after it, tab after a block key's colon, space then tab after one, and tab then a comment after one: `answers` exit 0 at all three, `ScannerError` in both. A tab before a comment, a trailing tab, a tab before a key's colon and a tab before the `on` colon: `ScannerError` in both parsers. The file and its projects were deleted after its one run |
| `git -C <clone> diff 1943fe760..53f28d009 -- seal`, `git -C <clone> show --stat 276585926 6f6650392`, `git -C <worktree> log -S'exempt from splitlines: YAML keys' -- skills/verify/scripts/deferral_check.py` | The record diff changes one `verdict:` and one `answer:` line. 276585926 touches the script and the test module, 6f6650392 the test module. The exemption came with cbf97bf55 |
