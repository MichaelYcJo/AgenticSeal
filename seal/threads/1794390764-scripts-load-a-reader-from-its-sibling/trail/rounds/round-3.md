# Review round 3: 1794390764-scripts-load-a-reader-from-its-sibling

```seal
target: 6476e1ba5, fixes afc05486a..6476e1ba5
```

This is a verifying round. The range `afc05486a..6476e1ba5` holds the
round 2 record `e9fe95459`, fix pass 2 (`5532345fb`, `d984a81ee`,
`31c26a583`), the orchestrator's fold `0e8801ab7` and the close blocks
`6476e1ba5`. The code read is that range's diff:
`.github/scripts/release_seal.py#main`, one new case in
`tests/github/test_release_seal.py#Test_main`, and one row and docstring of
`tests/skills/test_broad_gate.py#Test_rounds_rows`. The work item's
present-state records (`routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`) were read whole
at `6476e1ba5`. `Commit and pull request language` is English, so no
`pr.<lang>.md` is owed. The probes and narrow runs ran in a
`git clone --no-local` of the branch at `6476e1ba5`, under this round's
scratch directory.

Carried from earlier rounds and not established again: that the four lazy
readers of `chain_check.py` (`:1177`, `:1420`, `:1648`, `:1815`) end the
check at exit 2 in their own result; that the other handlers outside
`tests/` that can catch `SystemExit` catch no load or re-raise (round 2's
search, which this round ran again and which lists the same sites plus the
`except sibling.Absent` arm at `broad_gate.py:1841`); G10 and phase 2's S6
rows; S1's count and S8's comparison; and the phase records, which no
commit in the range changed.

The fix widens `going_on` from one call in `chain_counts` to the whole of
`seal_release`. So every load the job reaches is now silent, and any
handler between such a load and `main` that catches the exit would now
swallow it with no word at all. The round listed those handlers by joining
the handler search above with the calls `seal_release` makes. It loads
`publisher()` (`:518`) and, at that module's import, the seven modules at
`publish_release_note.py:124-136`. It loads `gate()` through
`suite_counts` (`:247`), the readers in `chain_counts` (`:323`), and
`lib/optin.py` and `lib/config.py` in `mark_on` (`:423-424`). The only
handler on those paths that catches `SystemExit` is `chain_counts`' own,
and that handler names the path. `seal_release` catches only
`(OSError, ValueError)` around `suite_counts` (`:530`), and
`broad_gate.read_record` loads nothing. Every absent module the job meets
therefore reaches `main`'s line or `chain_counts`' line. A handler that
names a tuple held in a variable would escape the search, as round 2 said.

## Findings

None. Both of round 2's findings hold as closed, and the fix diff holds no
new defect at any severity this round would raise.

## Confirmations

```seal
confirms: round-2#1
```
What holds: `release_seal.py:602-610` imports `sibling` inside the `try`
and runs `seal_release` inside `sibling.going_on()`. The `elif` at `:615`
turns an exit that carries a `path` into `<path> is absent`. An
`ImportError`, which also has a `path` attribute, falls to the `else` arm
because the test asks for `SystemExit` first. `main` returns 0 on every
arm (read). The close answer claims the case failed before the fix. This
round saw that. `Test_main::test_names_an_absent_module_in_its_own_line_and_exits_0`
fails at `assert said.err == ""` against `afc05486a`'s `release_seal.py`,
where stderr holds the loader's sentence ending "Nothing was read."
(executed). The close also claims a mutant that dropped the path from the
warning went red. This round kept the block and removed only the `elif`
arm, and the case failed on its last assert, the stdout reading
`no seal: Absent: 2 -- ...` (executed). The case asserts both stdout lines
exactly and unsets `DRY_RUN`, so no line beyond the two can pass it.
`changelog.md:3` now says that the release seal, meeting an absent module,
names the file in a line of its own and prints no "Nothing was read." This
holds for every module the job loads through `sibling.load`, by the
handler list above. The module docstring at `release_seal.py:39-44` ("one
log line and one `::warning::` with an exit of 0") holds again, unchanged.
The fold `0e8801ab7` states `main` as the third caller in *Scope* item 4,
in S7 (whose *Verifiable how* names the new case, which stands under that
name) and in the *Removes* row. No other statement of "two callers" stands
in the tree (executed: `git grep -nE 'two callers|callers that go
on|There are two|going_on'`).

```seal
confirms: round-2#2
```
What holds: the row at `test_broad_gate.py:1572-1590` stubs
`SystemExit(3)` under the id `exits`. Its docstring sends an absent check
to `test_names_the_absent_check_in_its_own_line_and_goes_on`, the case
that follows it (read). `rounds_rows` at `broad_gate.py:1838-1848` takes a
plain `SystemExit` through its last arm. The close claims that a mutant
dropping `SystemExit` from that arm turns the row red. This round
confirmed it: the `[exits]` row then fails with `SystemExit: 3`, and the
`[raises]` row and the absent case stay green (executed).

What matched: the new case belongs to `Test_main`, and no other case of
that class covers an absent module. The other absent case,
`Test_chain_counts::test_refuses_to_end_the_seal_where_a_reader_is_absent`,
covers another function. The case holds the fact S7's new clause states.
`seal layout --check` refuses neither changed test module, and `--pairs`
names no pair (executed).

What matched: every quote in `pr.md` stands word for word at
`frame/plan.md:90`, `:91`, `:94` and `:149` once runs of whitespace are
collapsed (executed: a comparison of each quote with the plan). `gaps.md`
gains one row and takes none out. `frame/plan.md`'s new row at `:153`,
`routing.md`, `frame/questions.md` and the rest of `frame/design.md` hold
no sentence the target contradicts (read).

The comment at `release_seal.py:81-82` says `lib/sibling.py` "is imported
from at the first module `module` is asked for". Since `5532345fb`, `main`
imports it before any module is asked for. This round opens no finding for
it. The comment's subject, `lib/` going first on `sys.path`, still holds,
only whoever next edits the file reads it, and the import is lazy at both
places.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD; this round ran the changed test modules alone | the whole tree | the orchestrator, by the broad gate |
| `frame/questions.md` Q1, with `lib/sibling.py#_going_on` now held across the whole of `seal_release` in the job's process, carried from round 2 | `lib/sibling.py:61-77`, `frame/questions.md` Q1 | the orchestrator, by the broad gate |
| `lib/sibling.py#_same` on Windows, carried from round 1 | `lib/sibling.py:79` | CI's `windows-latest` job |
| The five workflows that run the scripts under `.github/scripts/`, `publish-release.yml`'s `seal` job among them, carried from round 1 | `.github/workflows/` | CI, on the release pull request, the merge to `main` and the next tag |
| Whether the orchestrator's own fold `0e8801ab7` meets `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*. That section names a round finding located in a frame file as a decision whose fold the framer writes, and round 2 finding 1's `location:` names `frame/design.md:94-115`. The plan row at `:153` reads the three statements as restatements of what the build changed. This round finds the fold's text true of the code. Who should have written it is a process question, not a defect in the diff | `frame/plan.md:153`, `frame/design.md:107-116`, `:218`, `:320` | the sealer |
| Round 1's fix pass mutants for findings 1 and 4, which the close blocks report as red; carried from round 2 | `tests/lib/test_sibling.py`, the four copied-alone cases | the sealer, against the fix pass's hand-back |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/github/test_release_seal.py tests/skills/test_broad_gate.py::Test_rounds_rows tests/lib/test_sibling.py -q -p no:xdist` | 71 passed |
| `git checkout afc05486a -- .github/scripts/release_seal.py`, then the new `Test_main` case, then `git checkout HEAD --` the file | 1 failed, at `assert said.err == ""`, stderr holding the loader's sentence ending "Nothing was read." |
| the new `Test_main` case with `main`'s `elif` arm removed, and `Test_rounds_rows` with `SystemExit` dropped from `rounds_rows`' last catch, both by `Edit` in the clone, then both files restored with `git checkout HEAD --` | 2 failed and 4 passed: the `Test_main` case on its stdout assert (`no seal: Absent: 2 -- ...`), and the `[exits]` row with `SystemExit: 3` |
| `git grep -nE 'except[^:]*(SystemExit\|BaseException\|Absent)\|except *:' -- '*.py' ':!tests' ':!evals/behaviour'` | 14 lines: round 2's thirteen sites and the `except sibling.Absent` arm at `broad_gate.py:1841` |
| `bin/seal layout --check` and `--pairs` over `tests/github/test_release_seal.py` and `tests/skills/test_broad_gate.py` | 0 refused; 0 pairs |
| `uvx ruff check` and `uvx ruff format --check` over the three changed `.py` files | exit 0 each |
