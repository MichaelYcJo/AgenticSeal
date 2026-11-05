# Review round 2: 1793833681-an-import-inside-a-fence-is-not-charged

```seal
target: 4d54b937, fixes 6137faf8..4d54b937
```

This is a verifying round. It read the diff of round 1's fixes, `git diff 6137faf8 4d54b937`, which holds four commits: 18806108, b4146073, 77d00cac and 4d54b937 (executed). The branch's base is `release/v0.32.2` at 2ecb8d4b. The repository tracks no `seal/parity.md`, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is English. Every run took place in a `git clone --no-local` of the branch at 4d54b937 under the session scratchpad, which was removed before the hand-back.

Carried from round 1 and not re-established: the reading of Claude Code 2.1.318 in `frame/design.md` G3, which no round reopens cheaply, and CommonMark's rule that an HTML comment block opens only at the start of a line. Every verdict below was reached this round. Round 1's two comment shapes and its mutant for finding 1 were run again from its `## Probes` rows, and both matched.

The fix pass's account was read as a claim. It claimed the no-flag case is red under a mutant that fails `imports_of` open, on `assert 1 == 2`. It claimed `Test_live_pieces` is red under three mutants of `_scan`, and 485 passed over three modules. It claimed the docstring names the four shapes its probe ran. The orchestrator's fold, 4d54b937, was read as a claim too: it says *Operational impact*, *Data & interfaces*, S8 and *Out* now state the no-flag exit 2 and the two shapes the shared scan does not model. Each claim is checked below.

## Findings

### 1. The docstring's two shapes of the shared scan stop short of where the meter and the harness part

```seal
severity: should
location: `skills/verify/scripts/payload_meter.py:402-411`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:36`
evidence: executed `bin/test tests/skills/test_tmp_round2_shapes.py -q -s -p no:xdist` in the round's clone (exit 0), which printed `[('a.md',), ('c.md',)]` for the list-item fence followed by two fences and `[('c.md',)]` for an inline opener closed in a later paragraph; read `skills/verify/scripts/unverified_check.py:398-423`, `skills/verify/scripts/payload_meter.py:402-411`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:36`
reopens: round-1#3
```

Why it matters: round 1's finding 3 asked the docstring's *What this does not model* to name where the shared scan reads a file differently from CommonMark. The close names two instances that a probe found. It does not name the cause, which is wider than the two instances. The meter reports and gates nothing, so the cost is a person reading the list as whole when it is not. Contract rule 12 asks for the class, built from what produces it. A list made from the instances a probe happened to try is a sample.

The fence half. The docstring says the list item's closing line opens a fence for the meter, and "a next fence line then closes that fence, so what the next fence quotes is read". The probe ran `- ` followed by three backticks, then `  @a.md`, the indented closing line, `@b.md`, a three-backtick fence holding `@c.md`, and `@d.md` after that fence. It returned `a.md` and `c.md`. The harness reads `b.md` and `d.md`. So the closing line of that next fence opens a fence again and hides `d.md`. The meter's fences stay out of step with the file's to the end of the file, and the docstring reads as if they fall back in step at the next fence.

The comment half. `_scan` opens a comment at every `<!--` in live text and closes it at the next `-->`, on any later line (`unverified_check.py:398-423`). The docstring names only an opener "with no `-->` after it". The probe ran `Use <!-- to open.`, a blank line, `@b.md`, a blank line, then `then --> and @c.md`. It returned `c.md` alone. CommonMark reads that inline `<!--` as text, because an inline comment cannot cross the paragraph's end, and the harness reads `@b.md` (G3, carried). So the defect is any `<!--` that CommonMark reads as text, and its `-->` may stand later or nowhere.

The orchestrator's fold copies the same two instances into `frame/design.md` *Out* (`:36`), so the frame states the narrower list too. The line `harness reads the imports below it. And the` (`payload_meter.py:411`) is left short by the rewrap. The snippet below rewraps it, and the wrap is no finding on its own.

The fix states each half by its cause, in place of `payload_meter.py:402-411`. Every name in it is in the tree. It changes a docstring alone, which no check reads, so it owes no pin.

```python
    not text, and the meter follows either. The meter reads an import inside
    a fence behind `>` or a list marker, where the shared fence rule opens
    no fence. Where that fence's closing line stands within three spaces of
    the margin, the rule reads it as an opener. From that line to the end
    of the file the meter's fences stand out of step with the file's, so
    live text below it can be hidden and what a later fence quotes can be
    read. The shared scan opens a comment at every `<!--` in live text and
    closes it at the next `-->`, however far below. CommonMark reads a
    `<!--` as text inside a paragraph that does not hold its `-->`, and
    after a comment that closed on its line. There the meter hides the
    imports up to the next `-->`, or to the end of the file where none
    follows, and the harness reads them. And the meter reads no import
    whose `@` follows a code span, a comment, emphasis or a link with no
    whitespace between them, where the harness can begin a text token with
    the `@`."""
```

The snippet does not reach `frame/design.md:36`, the orchestrator's to fold. Its second and third sentences become these:

```markdown
Two shapes come from the shared scan itself, which this work does not move (S7). A `<!--` that CommonMark reads as text, inside a paragraph that does not hold its `-->` or after a comment closed on its line, hides the text up to the next `-->`, or to the end of the file where none follows. A fence's closing line behind a list marker opens a fence for the meter, and from there to the end of the file the meter's fences stand out of step with the file's.
```

### 2. The fold describes the no-flag copy as one without its siblings, and that copy stops at `hooks/lib/core.py` first

```seal
severity: should
location: `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:52`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:58`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/plan.md:34`
evidence: read `skills/verify/scripts/payload_meter.py:498-507`, `skills/verify/scripts/payload_meter.py:763-781`, `tests/skills/test_payload_meter.py:1480-1518`, `tests/skills/test_payload_meter.py:1430-1438`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:52`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:58`, `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/plan.md:34`
regression: round-1#1
```

Why it matters: the unit is the S8 row, which 4d54b937 rewrote to answer finding 1, with the two sentences of the same fold that describe the same copy. The plan's phase 1 row verifies S8 through the copy-alone case. The fold extended S8's Given, "the script copied without its siblings", to the no-flag run. But the case it cites copies `hooks/lib/core.py` and `hooks/lib/optin.py` beside the script, so the defect came from the fold reusing the old Given for a copy that Given does not describe.

With no flag, `measure` reaches `session_composition`, which calls `_core()` before `pair_rows` (`payload_meter.py:506-507`). So a copy without its siblings, given no flag where a `CLAUDE.md` exists, exits 2 naming `hooks/lib/core.py`. The `core.py` row of the copy-alone case pins that sentence (`tests/skills/test_payload_meter.py:1430-1438`). It never reaches the sentence S8 says it prints. The sealer reads S8 against the tree, and as written its no-flag half is false.

The same omission stands in the fold's two other statements of this copy. Each one is true only of a copy that holds `hooks/lib/core.py`. `frame/design.md:58` says exit 2 "is newly reached by a copy taken without `unverified_check.py`", and a copy without `core.py` reached exit 2 before the diff too. `frame/plan.md:34` says such a copy reaches exit 2 "where before it measured", and the same copy did not measure before. The list was made by reading the fold's diff whole, which is a closed set: these three statements are every place it describes the copy.

The fix names what the copy holds in all three. The frame is the orchestrator's to fold.

```markdown
| S8 A copy taken alone names what it needs | Given the script copied without its siblings, when it runs under `--sections`, and given the script copied with `hooks/lib/core.py` and `hooks/lib/optin.py` and without `unverified_check.py`, when it runs with no flag where a `CLAUDE.md` exists, then each exits 2 with the rewritten sentence naming both uses | The copy-alone case with its purpose string moved, seen red against the old sentence; the no-flag case, added by round 1's fix pass, red under a mutant that fails `imports_of` open |

- No JSON field, row name or command line changes, and no exit code is added. Exit 2 is newly reached by a copy that holds `hooks/lib/core.py` and not `unverified_check.py`, given no flag, wherever a `CLAUDE.md` exists (S8).

No new dependency, environment variable or exit code. A copy of the script that holds `hooks/lib/core.py` and not `unverified_check.py`, given no flag, now reaches exit 2 wherever a `CLAUDE.md` exists, where before it measured; every other run with no `CLAUDE.md` that holds an `@` behaves as it does today. The JSON of `seal payload` keeps its shape, and a `--baseline` file from 0.32.1 still reads.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `Test_module.test_a_copy_without_the_scan_exits_2_on_a_run_that_reads_a_claude_md` (`tests/skills/test_payload_meter.py:1480-1518`) is round 1's snippet, wrapped by the formatter and with a longer docstring. It passed at 4d54b937 (executed: 452 passed over the two modules). Round 1's mutant was written again: `imports_of` returns `[]` where `unverified_check.py` is missing. Under it the meter module ended 1 failed and 56 passed (executed, exit 1). The one red was this case, on `assert done.returncode == 2` with `assert 1 == 2`, and the copy's stderr said it found no `agents/*.md` under the repository. That shows the copy measured past the scan. The crafter's claim of red on `assert 1 == 2` matched. The docstring's claim that the row above stops at `hooks/lib/core.py` first matched `payload_meter.py:506-507` (read).

```seal
confirms: round-1#2
```
What holds: `Test_live_pieces` stands at `tests/skills/test_unverified_check.py:501-524`, after `Test_liveness`, with round 1's two cases and offsets unchanged. Both pass (executed). `bin/seal layout --check` printed no report line for `unverified_check.py` (executed, exit 0). This round wrote three mutants of `_scan`, each run with `-k Test_live_pieces` and then restored. Making the piece before a comment opener end after the opener turned both cases red (exit 1). Splitting a piece at a lone backtick run turned the accepting case red (exit 1). Making a span opened across lines keep its line's piece to the line's end turned the refusing case red (exit 1). The crafter named three mutants. The first is the same as this round's, and the other two differ. So each half of the docstring's contract that round 1 named now has a case in its own module.

What matched, against the orchestrator's fold: the new row of *Judgments of the run* (`frame/plan.md:42`) cites `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, which stands at `:16` (executed: `grep -n`). Finding 2 covers the fold's statements of the no-flag copy, and finding 1 covers its *Out* bullet.

What matched: the crafter's count. 452 passed over `tests/skills/test_payload_meter.py` and `tests/skills/test_unverified_check.py`, and 33 over `tests/behaviour/test_release_hygiene.py`, together 485 (executed, exit 0 each). The hygiene row for `2.1.318` still matches, because the docstring keeps that build's name at `payload_meter.py:395` (read).

What matched: the crafter's reading that the fragment and `gaps.md` need no change. The fragment says a copy without `unverified_check.py` "now stops with exit 2 wherever it reads a `CLAUDE.md` that exists". A copy without `core.py` reads no `CLAUDE.md`, so the sentence holds for every copy, unlike the fold's three (read: `changelog.md:3`). `gaps.md` names the broad run as unverified, and that is still true.

What matched: round 1's two comment shapes, run again in this round's probe. `Use <!-- to open a comment.` with `@b.md` below returned `[]`. A second opener after a comment closed on its line returned only `b.md`. These are the shapes the docstring now names, and finding 1 widens them.

Each new test was read against its group. `bin/seal layout --pairs` names the same four pairs inside `Test_imports_of` that round 1 named, and no pair holds either new unit (executed, exit 0). The no-flag case is the only case of the meter module that went red under the fail-open mutant, so it holds a path no other case holds. `Test_live_pieces` holds the lone-backtick piece. The meter's lone-backtick case cannot see that piece, because its `@b.md` opens a line of a later paragraph, which a piece split at a backtick run does not reach (read: `tests/skills/test_payload_meter.py:1342-1351`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether G3's reading of the Claude Code 2.1.318 binary is right. Finding 1 rests on it for what the harness reads after an inline `<!--`, and it is carried from round 1 | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:11` | the owner, where `frame/questions.md` Q1 is answered |
| The full suite, the repository-wide lint and the format check at 4d54b937. The suite stays `unverified`, and this round ran three modules alone | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/gaps.md` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_payload_meter.py tests/skills/test_unverified_check.py -q -p no:xdist` at 4d54b937 | exit 0, 452 passed |
| `imports_of` made to return `[]` where `unverified_check.py` is missing, `bin/test tests/skills/test_payload_meter.py -q -p no:xdist`, then restored | exit 1, 1 failed and 56 passed; the failure was the no-flag case on `assert 1 == 2` |
| `_scan`'s piece before a comment opener made to end after the opener, `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -k Test_live_pieces`, then restored | exit 1, 2 failed |
| `_scan` made to split a piece at a lone backtick run, the same command, then restored | exit 1, 1 failed (the accepting case) and 1 passed |
| `_scan`'s piece before a span opened across lines made to run to the line's end, the same command, then restored | exit 1, 1 failed (the refusing case) and 1 passed |
| `tests/skills/test_tmp_round2_shapes.py`, four shapes through `imports_of`, run once by `bin/test ... -q -s -p no:xdist`, then deleted | exit 0. List-item fence then two fences: `a.md`, `c.md`. Inline opener closed in a later paragraph: `c.md`. Inline opener with no closer: nothing. Opener after a comment closed on its line: `b.md` |
| `bin/test tests/behaviour/test_release_hygiene.py -q -p no:xdist` | exit 0, 33 passed |
| `bin/seal layout --check` and `bin/seal layout --pairs` | exit 0 each; no report line for `unverified_check.py`, and the four pairs round 1 named, none new |
