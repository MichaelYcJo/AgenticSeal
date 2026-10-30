# Phase 8: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 8 |
| Commit | 72c1a3ee |

## What this phase was asked

Phase 8 of `frame/plan.md`, with `frame/design.md` *Scope* items 9 to 12
and scenarios S11 and S12. The core's prose was to lose its repeated
sentences and its `#1167` pointer while keeping every directive, citation,
invariant and reason, its `##` headings and phase 5's `description:` (item
9). It was to say which work it governs, whose paths it cites, whose owner
and whose mechanisms it names, and the `CONTRIBUTING.md` sentence was to
move to `CLAUDE.md` (item 10). Each two-way sentence item 11 lists was to be
rewritten. `hooks/lib/core.py#output` was to print the body below the
frontmatter, and `core_check.py` was to compare against that body (item
12). The four agents' behaviour suites were to run on both sides (S11).

A crafter built the phase in `02a34267`, `ac5eae67`, `769a1413` and
`a5dbf0a2` and left no record. The owner stopped the behaviour suites after
two agents. The run then moved to a new session, whose crafter closes the
phase. It was asked three things. The first was to fix the Windows failure
that CI run 40989182473 found in `tests/skills/test_core_check.py` at
`df5ba5f1`, under the orchestrator's decision that the check moves and the
fixture does not. The second was to write this record and the Status cell.
The third was to add two `gaps.md` *Not verified* rows: S11 for the proofer
and the crafter, and a diagnosis of the framer's rule 5 result.

## What this phase found

**The frame held for items 9, 11 and 12, and item 10's paths sentence says
more than the design does.** Between `6ebfada5` and HEAD, the headings and
the frontmatter lines of `skills/core/SKILL.md` are unchanged (`diff` of
the two, executed). `#1167`, "mid-run", "closed form", "most expensive
judgment", "history shows" and "argued for" are gone, and "A few invariants
hold the chain" stays. `CLAUDE.md` holds the `CONTRIBUTING.md` sentence, and
`CONTRIBUTING.md:367` follows the core's new word, "step". Item 10's design
says every cited path is relative to the plugin's root "and never to the
session's repository". The core's sentence adds "except `seal/`, the records
root `skills/implement/SKILL.md` *Document layout — two roots, three
lifetimes* places". The exception is needed: the core cites
`seal/threads/` for the work item's records, and those stand in the
session's repository or its common git directory, never under the plugin's
root. `gaps.md` records it as a divergence.

**The core is 48 B smaller, and the hook prints 6,180 characters.** The
file is 6,780 B at `6ebfada5` and 6,732 B at HEAD (`git cat-file -s`). At
HEAD, `python3 -c` over `core.output('.', '.')` gives 6,180 characters,
6,226 B, of which the body below the header is 6,058 B. That is under
`CAP`, 10,000 characters, and S7's case in the boundary set holds it.

**The Windows failure is phase 6's, not phase 8's.** The handoff named it a
failure phase 8 opened. `tests/skills/test_core_check.py` arrived at
`6fc5941e`, phase 6, with a local `write` that passed `newline="\n"`.
`84cf2dd3`, also phase 6, replaced it with `tests/conftest.py#write`, which
does not. `f4aedb93`, the last commit whose tests workflow was green, holds
neither (`git merge-base --is-ancestor`, executed). The first Windows run
that held the module was at `df5ba5f1`, after phases 5 to 8 were pushed
together. All six failing cases were written in phase 6. The case phase 8
added passes on Windows, because its planted `stdout` has `\n` line
endings.

**The orchestrator's reading held, and a second instance stood beside it.**
`tests/conftest.py#write` calls `pathlib.Path.write_text` with no
`newline=`, so on Windows the scratch core is written with `\r\n`. The
hook's `stdout` then ends `\r\n` plus the dispatcher's `\n`. The fixture
`hook()` sets `content` to `stdout.rstrip("\n")`, which keeps a `\r`.
`_normal` removed only trailing `\n`. The counts in the log match this: 279
characters of `stdout` and 277 of `content`. The log's fourth failure,
`test_refuses_nothing_for_line_endings_or_trailing_newlines` (284 against
281), has a second cause. Its `out.replace("\n", "\r\n")` over a `\r\n`
core makes `\r\r\n`, and one `replace("\r\n", "\n")` leaves that as `\r\n`.
So a fix for the trailing `\r` alone would have left that case red on
Windows. The same `\r\r\n` is what a Windows `sys.stdout`, which writes
each `\n` as `\r\n`, makes of a core whose own lines end `\r\n`. That is
read from CPython's documented behaviour and was not run on Windows.

**The check moved, test-first, in `72c1a3ee`.** Two cases joined
`Test_judge` beside the line-endings case. Each writes the scratch core's
bytes as `b"# The core\r\n\r\nOne value.\r\n"`, so each is red on any
platform. `test_refuses_nothing_for_a_carriage_return_left_before_dropped_newlines`
holds the trailing `\r` in `content`.
`test_refuses_nothing_for_a_crlf_core_through_a_translating_stream` holds
`\r\r\n` against both `content` and the file. Before the fix, `bin/test -q
-p no:xdist tests/skills/test_core_check.py -k "carriage_return_left or
translating_stream"` failed both (exit 1). With `rstrip("\r\n")` alone, the
same command passed the first and failed the second (exit 1), at the body
against the file. With `_normal` reading every `\r` before a `\n` as part of
the line ending (`LINE_END = re.compile(r"\r*\n")`), it passed both (exit
0). `_normal`'s docstring and the module docstring now say so.

**A one-time probe reproduced the CI failure on macOS.** A probe module ran
the module's `Test_core_entries`, `Test_judge`, `Test_main` and
`Test_module` cases with `write` replaced by one that writes `\r\n`. Against
HEAD's `core_check.py` before the fix, 7 failed: the five `Test_judge` and
`Test_main` cases CI names, and the two new ones. CI's sixth,
`test_seal_core_runs_this_script`, runs the script on disk through a
subprocess, so the probe ran it against the fixed copy. Against the fix,
all 19 passed (exit 0). The probe's two files were deleted.

**`seal mutate` turned each half red.** `rstrip("\r\n")` mutated back to
`rstrip("\n")` made the first new case fail. `r"\r*\n"` mutated to
`r"\r?\n"` made the second fail. Each printed "red: the cases failed
against the mutation (exit 1)", and the tree was clean after each restore.

**The class, by construction: every place in `core_check.py` and
`hooks/lib/core.py` that compares, strips or measures text from a file or a
transcript.**

- `core_check.py#entries` reads the transcript in text mode, which turns
  `\r\n` into `\n`. JSON escapes `\r` inside a string, so a transcript with
  `\r\n` lines parses the same. Not broken.
- `#in_context` and `#core_entries` compare JSON values (`type`,
  `subtype`, `uuid`, `hookEvent`), never file text. Not broken.
- `#core_entries` calls `core.parse` on `stdout`. The header is printed with
  one `\n`, which a Windows stream makes `\r\n`, and `parse` drops one `\r`
  before the first `\n` (`tests/hooks/test_core.py:81` holds it). Not
  broken.
- `#judge`, `content` against `stdout`: broken by the trailing `\r` and by
  `\r\r\n`. Fixed.
- `#judge`, the two lengths in the failure message: they count the raw
  characters on each side, which is what the message reports. Not broken.
- `#judge`, the digest: both the hook and the check hash the file's bytes as
  read, so `\r\n` is in both. Not broken.
- `#judge`, the body against the file's text below its frontmatter: broken
  by `\r\r\n` where a translating stream carried a `\r\n` core. Fixed.
- `core.py#manifest` and `#origin` read JSON and compare its values and
  paths. Not broken.
- `core.py#without_frontmatter` matches `---\r?\n` and `---\r?`, and
  `tests/hooks/test_core.py:157` holds a `\r\n` frontmatter. Not broken.
- `core.py#output` prints the body as read, and `len(output)` is what S7
  holds under `CAP`. A `\r\n` core is one character longer per line, and
  the output holds 100 line endings at HEAD, against a margin of 3,820. `.gitattributes` (`* text=auto eol=lf`)
  checks the core out with `\n` on every platform. Not broken.
- `core.py#parse` splits at the first `\n` and keeps the body as given.
  Not broken.

**The design's comparison sentence is narrower than the code.**
`frame/design.md:110` says bodies are compared "with line endings as `\n`
and trailing newlines removed". The check now also reads each `\r` before a
`\n` as part of a line ending, and removes a `\r` left at the end.
`gaps.md` records it as a divergence; the design is the framer's file.

**S11 ran for two of the four agents.** Both sides' JSON and both compare
records are in `evals/`, old side at `6ebfada5` and new side at `769a1413`.
The sealer passed every rule. The framer failed rule 5 alone: tokens read
rose from 7,070,907 to 8,367,258, and per tool call from 21,623.6 to
26,147.7. Over the same runs the preload fell by 48 B and the spend fell
from 26.74 to 26.37 USD. Rules 1 to 3 passed: every grader passed 2 of 2
on both sides. The proofer's new side was stopped after 27 minutes and
left no output, and no crafter side ran. The owner stopped the runs on
2026-10-30, and `gaps.md` *Not verified* carries both the decision and the
framer's diagnosis, read from the two JSON files with no re-run.

**The build crafter's red runs and mutation runs are not on record.**
`02a34267` and `ac5eae67` hold item 12's cases in `tests/hooks/test_core.py`
and `tests/skills/test_core_check.py`. No record states that each was seen
red first, or which units `seal mutate` broke. The orchestrator holds that
crafter's hand-back.

**The phase-boundary set passed.** It was one `bin/test -q` command over 94
modules at `72c1a3ee`. Those were phase 8's *Verified by* modules, phase
5's and phase 6's sets, and every test module that names or globs a path
the phase changed: `skills/core`, `CLAUDE.md`, `CONTRIBUTING.md`,
`core_check`, `hooks/lib/core.py`, the `skills` directory, `seal/threads`,
`hooks.json`, a README or `seal.py`. It passed 4,552 cases and skipped 11
(exit 0).
