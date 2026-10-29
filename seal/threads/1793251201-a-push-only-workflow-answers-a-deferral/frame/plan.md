# Implementation Plan: 1793251201-a-push-only-workflow-answers-a-deferral

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phase 1.

## Summary

`seal deferrals` counts a workflow whose trigger it could not read as one
that answers a deferral, so a push-only test run resolves a deferral to CI
in five spellings the probes found. The fix has two parts that need each
other. `read_events` reads the spellings in use: a quoted `on` key, an
event block at any consistent indent, and an event key that carries a value
or a comment. `inspect` then reports whatever `read_events` still cannot
read as `unread`, and never counts it. With the second part alone, a
pull-request workflow keyed `"on":` would read as unread and refuse. With
the first part alone, a workflow with no `on` key, or with a flow list
across lines, would still answer.

## Technical context

- `skills/verify/scripts/deferral_check.py#read_events` (`:89-121`) matches
  `^on\s*:` only, adds an inline value whole, and reads block keys only at
  an indent of two or less, through a key pattern that refuses a key with
  anything after its colon (`:117-119`).
- `#inspect` (`:185-232`) puts a workflow with an empty event set into
  `resolving` (`:196-198`), printed with `(trigger unread)` (`:197`).
- `KNOWN_LIMITS` (`:82-86`) is printed after `limit: ` by `#main`
  (`:264`).
- `tests/skills/test_deferral_check.py` holds 11 cases in `Test_main`, the
  launcher case in `Test_module`, and `test_census`; none asserts on an
  unread trigger (`git grep 'trigger unread' -- tests`, executed: no match).
- `tests/censuses.py#heading_rule` and `#splitlines` read every shipped
  script: a new code line holding `startswith("#")`, a `#{<digit>`
  pattern, or `.splitlines(` takes its `# exempt from ...:` comment on its
  own line above it, as `read_events` does today at `:97`, `:106` and `:111`.

The chosen approach's failure scenario: six months on, a workflow uses a
trigger spelling nobody here wrote a case for, such as a YAML anchor or an
`on` key written as `? on`. It reads as `unread`, the deferral does not
resolve, and the person sees `trigger unread, not counted` against a
workflow that does run on pull requests. The cost is a false refusal with
its cause printed, which the person answers by rewriting the trigger or by
writing the row as unanswered. It is not a pass.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the text scan. Widen `read_events` to the spellings in use, and report anything still unread as `unread`, not counted (the design's Scope items 1 to 3) | An unforeseen spelling reads as `unread` and refuses a workflow that does answer, with the cause printed (*Technical context* above) | Chosen. The direction of an unread trigger is the refusal #1123 asks for, and the widened reader keeps that refusal off the spellings the probes found in use |
| Flip the direction only: an empty event set is `unread`, and `read_events` is left as it stands | `"on":` with `pull_request:`, the spelling a YAML linter asks for, reads as unread and refuses every repository that writes it; so does any event block at four spaces. #1123 *Done when* asks for both spellings to be read | Rejected: a false refusal on a common spelling, and half of the *Done when* left undone |
| Widen `read_events` only, and keep counting an unread trigger as answering | A workflow with no `on` key, or `on: [` with the events on the next lines, still answers a deferral at exit 0 (probe 1). The next spelling nobody read fails open the same way | Rejected: the first *Done when* bullet is not met, and the class stays open |
| Replace the scan with a YAML parse | The gates here are stdlib-only, and the module's docstring decides against a dependency for this reader. A YAML 1.1 parser also reads the bare key `on` as the boolean `true`, so a parse needs its own handling of the one key this reader exists for. A parse failure would still need a direction, which is the unread outcome this design adds | Rejected: a dependency in a stdlib-only toolset, and the direction question stays |
| Replace the structure: remove `seal deferrals`, and leave a deferral's answerer to the reviewer reading the row | The case the module docstring records comes back: a session deferred the suite to CI in a repository where no workflow ran it, and the row read as handled. `skills/verify/SKILL.md` *The answerer has to exist* would cite a command that no longer exists | Rejected. The premise that keeps it, checked: the module's 12 cases cost 1.04 s in `.test_durations` (executed), the command is the step `skills/verify/SKILL.md` names before a deferral row is written (read), and #1123 was filed by #956's audit into the release where one work item carries it, not into #1038, where the larger reader questions are decided by the record (`seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-5.md`, read). The command's own catch history is not in the tree: it arrived with the repository's initial commit `716d8548` (executed), so whether it stays is #1038's kind of question and not this fix's |
| Also refuse a trigger it read in part: add every event-shaped name it found, and skip the rest | `on: [push, {weird}]` would read as `push` alone, and a skipped `pull_request` element would turn an answering workflow into `too late` without saying a part was skipped (probe 2: `workflow_dispatch: {}` dropped silently today) | Rejected: a partial set reads as a full one. One unreadable element makes the whole trigger unread (Scope item 2) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `read_events` reads the spellings of Scope item 1 and returns an empty set exactly where the trigger is unread; `inspect` prints unread workflows as `unread` and does not count them; `KNOWN_LIMITS` gains its clause; the module docstring, `skills/verify/SKILL.md` *The answerer has to exist*, `README.md` and `README.ko.md` list the fifth outcome | The new cases S1 to S8 of `frame/design.md`, each seen red at this branch's base before the code changes, and the existing cases (S9), in one command over `tests/skills/test_deferral_check.py` together with the modules that read a changed path, `tests/test_censuses.py`, `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_one_word_one_meaning.py` among them; `seal mutate` over `deferral_check.py#read_events` and `#inspect` | 61e2e6be |

## Operational impact

None for a deployer: no migration, no environment variable, no dependency.
The visible change is to `seal deferrals`' output and exit code. A
repository whose workflow trigger the scan cannot read now gets exit 1 with
an `unread` line where it got exit 0 with `answers ... (trigger unread)`.
A session that deferred a check to CI on that exit 0 now sees the deferral
refused, and answers it by running the check or by writing the row as
unanswered.
