# Review round 2: 1793251201-a-push-only-workflow-answers-a-deferral

target: bef03a87, fixes 6dbc8963..bef03a87

This round verifies the fix diff. It ran in a `git clone --no-local` of the
branch at `bef03a87`. Round 1 handed over three things, and this round carried
them without establishing them again. The first is its probe method: the base
script comes from `git show <rev>:skills/verify/scripts/deferral_check.py` and
runs over one temporary project per trigger shape. The second is its YAML
readings of the round 1 shapes. The third is its `seal layout --pairs` result,
which names no pair in `tests/skills/test_deferral_check.py`; the fix diff adds
no test file. Every verdict below was reached on the code at `bef03a87`.

## Findings

### 1. An event name on the line below `on:` followed by a deeper line answers again, though YAML reads the two lines as one name

severity: should
location: `skills/verify/scripts/deferral_check.py:138-139`, `skills/verify/scripts/deferral_check.py:144-147`, `skills/verify/scripts/deferral_check.py:113-114`, `tests/skills/test_deferral_check.py:179-203`
evidence: executed `python3 -I test_tmp_r2.py`, `uv run --no-project --with pyyaml python3 -c 'import yaml; yaml.safe_load(...)'`
verdict: fixed d8edc4a6
regression: round-1#1

The unit is the bare-name arm of `block_entries` (`:144-147`), which 816646c6
added. `frame/plan.md`'s phase 1 row asks for an empty set exactly where the
trigger is unread, and `frame/design.md` *Scope* item 2 never returns a partly
read trigger as a smaller set, but the fix reads the first line of a plain
scalar and skips the lines that continue it, because the `indent > width` arm
at `:138-139`, written for the lines under a key entry, also skips the
continuation of a bare name.

Take the trigger `on:`, then `  pull_request`, then `    push`. A YAML parser
loads it as `{True: 'pull_request push'}`: the deeper line continues the
scalar, and the result is one event name with a space in it. GitHub runs no
workflow on that name. The probe ran three scripts over it. The base
`8d8d6390` printed `answers ... (on pull_request)` at exit 0. Round 1's target
`6dbc8963` printed `unread ... (trigger unread, not counted)` at exit 1.
`bef03a87` prints `answers ... (on pull_request)` at exit 0 again. So
`on:` / `  pull_request` / `    closed` also resolves a deferral to CI on a
workflow that never runs. That is the fail-open #1123 closes, and
`SECURITY.md` *What is in scope* counts a check that fails open as a security
defect.

The fix pass held the arm to one name with `two-names-on-the-lines-below`,
where the second name sits at the block's indent. It did not cover a second
line deeper than the block, and no parameter of the S5 case holds one (read
`tests/skills/test_deferral_check.py:179-203`). The docstring at `:113-114`
says "a block of one line", and the code accepts one bare line with any number
of deeper lines below it. A comment line below the name is not a
continuation: YAML drops it, and the scan drops it before the indent is
measured, so `on:` / `  pull_request` / `    # note` still answers, rightly.

The fix makes a deeper line under a bare name end the read. A deeper line
under a key entry still belongs to that entry. A bare name that comes after a
key already makes the block unread at `:146-147`, so the order of the two
cannot matter.

```python
        if indent > width:
            if bare:
                # A deeper line under a bare name continues that plain scalar:
                # `on:` / `  pull_request` / `    push` is "pull_request push".
                return []
            continue
```

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
            "on:\n  pull_request\n    push\n",
        ...
            "a-name-continued-on-a-deeper-line",
```

The parameter is to be seen red at `bef03a87`, where the probe printed
`answers` at exit 0 for this shape, and red again under a mutant that drops
the `if bare` arm (contract rule 15).

answer: Fixed for the whole class rather than the bare name alone. Under contract rule 12, a `- name` item continues the same way, and `on:` / `  - pull_request` / `    closed` answered too. `block_entries` now remembers whether the last entry held a colon. A deeper line under an entry with no colon, a bare name or a `- name` item, makes the block unread. A deeper line under a key still belongs to that key. The docstring at `:113-114` now names the shape. S5 gains `a-name-continued-on-a-deeper-line` and `an-item-continued-on-a-deeper-line`. Both were red at b0fd17c3, whose script is bef03a87's, where each printed `answers` at exit 0 (executed). S4 gains `name-with-a-comment-below` (`on:` / `  pull_request` / `    # the run`), which answers. `seal mutate` over the new arm gave 7 mutants, 6 red and one equivalent (executed). The equivalent mutant exposed a dead `not is_item and` condition, removed in f23464df, because a `- ` item holding a colon is never an event name. After it, 6 of 6 went red (executed). No sentence of `changelog.md`, `KNOWN_LIMITS`, `skills/verify/SKILL.md` or the two READMEs names this shape; each names unread shapes as examples or the outcome in general (read).

### 2. An inline event name followed by a deeper line answers, though YAML reads the two lines as one name

severity: should
location: `skills/verify/scripts/deferral_check.py:179-180`, `tests/skills/test_deferral_check.py:179-203`
evidence: executed `python3 -I test_tmp_r2.py`, `uv run --no-project --with pyyaml python3 -c 'import yaml; yaml.safe_load(...)'`
verdict: fixed d8edc4a6

This finding is outside the fix diff. This round opened it while
enumerating the class of finding 1, under contract rule 12. The inline arm of
`read_events` is a unit the build rewrote, and the base read the same shape
the same way, so it carries neither a `regression:` nor a `reopens:` line.

`on: pull_request` followed by `  push` loads in YAML as
`{True: 'pull_request push'}`, the same continued scalar as finding 1. The
probe printed `answers ... (on pull_request)` at exit 0 for it at
`8d8d6390`, at `6dbc8963` and at `bef03a87` alike. The else arm at
`:179-180` takes the value on the `on` line as the whole name and never
looks at the next line. `frame/design.md` *Scope* item 2 asks for the
whole trigger to be unread where any part of it is not read, and the part
on the next line is not read.

A line below `on:` that is not indented is the next top-level key, such as
`jobs:`, and the check below leaves it alone. An indented line there can only
continue the value, so it makes the trigger unread.

```python
def continued(lines):
    """True where the first line below that is neither blank nor a comment is
    indented, so it continues the value on the line above."""
    for line in lines:
        code = COMMENT.sub("", line)
        if code.strip():
            return code[0].isspace()
    return False
```

```python
        else:
            names = [value]
            # A deeper line under an inline name continues that plain scalar:
            # `on: pull_request` / `  push` is "pull_request push".
            if continued(lines[i + 1 :]):
                return set()
```

```python
# tests/skills/test_deferral_check.py, test_an_unread_trigger_is_reported_and_not_counted
            "on: pull_request\n  push\n",
        ...
            "an-inline-name-continued-on-a-deeper-line",
```

The parameter is to be seen red at `bef03a87`, where the probe printed
`answers` at exit 0 for this shape. Neither fix changes a sentence of `changelog.md`. Its list of shapes that
read as unread opens with "such as", and it names neither shape.

answer: Fixed with the proposed `continued` helper. The check sits before both inline arms, not inside the scalar arm alone: under contract rule 12, a closed flow list continues the same way, and `on: [pull_request]` / `  push` answered too. S5 gains `an-inline-name-continued-on-a-deeper-line` and `an-inline-list-continued-on-a-deeper-line`. Both were red at b0fd17c3, whose script is bef03a87's, where each printed `answers` at exit 0 (executed). S4 gains `inline-name-with-a-comment-below` (`on: pull_request` / `  # the run`), which answers. It went red under the mutant that measures the comment line's indent without dropping the comment (executed). The mutants that skip the check, and that make `continued` always false or always true, went red as well (executed). `changelog.md` needs no change: its list of unread shapes opens with "such as".

## Confirmations

confirms: round-1#1
The two spellings round 1 named read again. The fix pass claimed that S4's
`flow-list-trailing-comma` and `name-on-the-line-below` were red at
`6dbc8963` and that S5's two new parameters passed there. The probe ran
`6dbc8963`'s script over each shape (executed). `on: [pull_request, ]` and
`on:` / `  pull_request` printed `unread` at exit 1 there, so S4's exit 0 was
red. `on: [pull_request,,]` and `on:` / `  pull_request` / `  push` printed
`unread` at exit 1 there, as S5 expects. At `bef03a87` the first two print
`answers ... (on pull_request)` at exit 0, and the last two still print
`unread`. The pop at `skills/verify/scripts/deferral_check.py:176-178`
removes one empty last element only (read). `on: []` and `on: [,]` read as
unread (executed). The fix pass did not restore the base's `if e.strip()`
filter, and that holds. A YAML parser raises `ParserError` on
`on: [pull_request,,]` and on `on: [,]` (executed). GitHub runs no workflow
from either. The base read the first as `{pull_request}` and answered at
exit 0 (executed), which failed open. The fix pass calls this a partial read
that *Scope* item 2 refuses. The probe adds that no parser loads the text at
all, so refusing it fails closed. Finding 1 above is a new defect in the arm
this fix added. It does not undo what round-1#1 named.

confirms: round-1#2
`KNOWN_LIMITS` carries the proposed clause at
`skills/verify/scripts/deferral_check.py:86-88`, and S8 asserts
`filters (types, branches, paths) are not read` at
`tests/skills/test_deferral_check.py:247` (read). The narrow run below passes
it (executed). The fix pass claimed that `git grep` finds no third place
stating the command's limits. `git grep -E 'YAML graph|filters \(types'`
outside `seal/threads` finds the script, the test and
`skills/verify/SKILL.md:367` only (executed). The sentence added at
`skills/verify/SKILL.md:369-370` agrees with the printed clause (read).
No test reads that sentence. `git grep` for `closed pull requests` and `not
its filters` under `tests` finds nothing (executed). Round-1#2 asked for the
printed limit, and S8 pins that, so this is no finding.

confirms: none
The fix pass's case count holds. It claimed 37 cases in the module, and
`bin/test tests/skills/test_deferral_check.py --collect-only` collected 37
(executed). Each new parameter covers something the group did not. The two in
S4 cover the two new arms, and the two in S5 bound them to one comma and one
name (read `tests/skills/test_deferral_check.py:153-203`).

confirms: none
The phase record's sentences stand as history. `trail/phases/phase-1.md` is
bound to `Commit | 61e2e6be`, and it describes the trigger reader and the
`KNOWN_LIMITS` wording as built at that commit (read). `skills/implement/SKILL.md`
*A fix pass rewrites the `verdict:` line* says a fix pass "writes no phase
record" and that "the build's phases keep theirs". So a sentence that no
longer matches the code after a fix pass is not corrected in place. What
changed, and why, is in round 1's `answer:` lines. The same holds for
`frame/design.md` *Scope* items 1 and 4. Item 4 says one clause is added, and
`KNOWN_LIMITS` now carries two. Item 1's block form names no bare name. The
fix pass may not write `gaps.md`, and the round record holds the change.

confirms: none
The version bump and the changelog fragment in `bef03a87` match their rules.
`origin/release/v0.24.2` sits at `8d8d6390` with `plugin.json` at `0.24.1`
(executed). `gh pr list --base release/v0.24.2 --state all` printed no pull
request (executed). The other two open branches into that release,
`fix/1132-seal-pact-passes-near-misses-of-an-anchor` and
`test/1127-the-citation-case-misses-files-and-wrapped-comments`, carry
`0.24.1` (executed). So this is the first pull request into the branch, and
`skills/implement/orchestration.md` *Which branch the pull request lands on
is decided with the routing question* moves the version there. The move is in
the same commit as the fragment, as that paragraph asks.
`.claude-plugin/marketplace.json` carries no version (read). Read against the
code, each sentence of the fragment holds. Push-only `"on":` and four-space
spellings printed `answers ... (trigger unread)` at exit 0 at the base, as
round 1's probe showed. The reader now takes the three key spellings, any
consistent block indent, a key carrying a value or a comment, and a flow list
closed on its line (`skills/verify/scripts/deferral_check.py:94`, `:110-185`).
A flow mapping, a list across lines and a missing `on` key print the `unread`
line and do not resolve the deferral on their own (S5 and S6). The limit line
prints the filters clause. The fragment's shape, a `### Fixed` heading over
one bolded bullet with the issue number, matches the merged fragments of
`1793240966-the-framer-has-no-read-only-probe` and
`1793240969-pre-rename-readings-outlived-their-release` (read).

confirms: none
The broad gate's label is honest. `gaps.md` *Not verified* still names the
full suite, the repository-wide `ruff check` and `ruff format --check`, and
the typecheck, with the orchestrator through `seal gate` as the answerer
(read). This round ran none of the three.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's claim that 6 of 6 mutants over the two new arms went red after 8ecc92bf. Not re-run this round. A mutation score licenses tested, never safe: finding 1 is a branch the arm lacks, and no mutant of the existing code can show it | `skills/verify/scripts/deferral_check.py:144-147`, `:176-178` | the sealer, in its sample of the crafter's claims |
| The fix pass's run of 4168 passed over 61 modules. Not re-run; this round's narrow run is the seven modules below | the branch at `bef03a87` | the orchestrator, through `seal gate` |
| The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | the branch at `bef03a87` | the orchestrator, through `seal gate` |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_r2.py`, in the clone at `bef03a87`: one temporary project per trigger shape with a `pytest` step, run through the scripts of `8d8d6390`, `6dbc8963` and `bef03a87` (`git show <rev>:skills/verify/scripts/deferral_check.py`) with `--kind tests` | Exit 0. `on:` / `  pull_request` / `    push`, and the same with `closed` on the deeper line: `answers` exit 0 at `8d8d6390`, `unread` exit 1 at `6dbc8963`, `answers (on pull_request)` exit 0 at `bef03a87`. `on: pull_request` / `  push`: `answers (on pull_request)` exit 0 at all three. `on: [pull_request, ]` and `on:` / `  pull_request`: `answers` at `8d8d6390`, `unread` exit 1 at `6dbc8963`, `answers (on pull_request)` exit 0 at `bef03a87`. `on: [pull_request,,]`: `answers (on pull_request)` exit 0 at `8d8d6390`, `unread` exit 1 at the other two. `on:` / `  pull_request` / `  push`: `answers (on pull_request, push)` at `8d8d6390`, `unread` exit 1 at the other two. `on: []` and `on: [,]`: `answers (trigger unread)` at `8d8d6390`, `unread` exit 1 at the other two. `on:` / `  pull_request` / `    # note`: `unread` at `6dbc8963`, `answers (on pull_request)` at `bef03a87`. The file was deleted after its one run |
| `uv run --no-project --with pyyaml python3 -c 'import yaml; yaml.safe_load(...)'` over seven of the shapes above | `on:` / `  pull_request` / `    push` and `on: pull_request` / `  push` load as `{True: 'pull_request push'}`. `on: [pull_request,,]` and `on: [,]` raise `ParserError`. `on: []` loads as `{True: []}`, `on: [pull_request, ]` as `{True: ['pull_request']}`, `on:` / `  pull_request` as `{True: 'pull_request'}` |
| `bin/test tests/skills/test_deferral_check.py tests/test_censuses.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/hooks/test_version_check.py -q -p no:xdist` | 364 passed, exit 0 |
| `bin/test tests/skills/test_deferral_check.py -q -p no:xdist --collect-only` | 37 tests collected, exit 0 |
| `git -C <worktree> show origin/release/v0.24.2:.claude-plugin/plugin.json`, the same for the two other open branches, and `gh pr list -R MichaelYcJo/AgenticSeal --base release/v0.24.2 --state all` | `0.24.1` on all three branches. The listing printed nothing, exit 0 |
| `git grep -n -E 'YAML graph\|filters \(types' -- ':!seal/threads'`, and `git grep -n -E 'closed pull requests\|not its filters' -- tests skills README.md README.ko.md` | The first finds `skills/verify/SKILL.md:367`, `skills/verify/scripts/deferral_check.py:84`, `:86` and `tests/skills/test_deferral_check.py:247`. The second finds `skills/verify/SKILL.md:369-370` and `skills/verify/scripts/deferral_check.py:87`, and nothing under `tests` |
