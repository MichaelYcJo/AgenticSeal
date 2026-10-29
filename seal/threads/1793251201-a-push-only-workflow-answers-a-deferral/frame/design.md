# Design: 1793251201-a-push-only-workflow-answers-a-deferral

## Grounding

Every coordinate below is the tree at `ea08c39c`, this branch's routing
commit on top of `8d8d6390`. `executed` marks a fact a command the framer
ran printed. `read` marks a fact the framer opened and read.

| Policy clause | What it fixes for this work |
|---|---|
| Issue #1123 *Done when* (read; a ticket, not policy; it has no comments) | Two outcomes. A workflow that runs the kind and whose trigger the scan cannot read is reported as unread and is not counted, so the kind does not resolve on it alone. `"on":` and an event key at any consistent indent are read, and a case shows both push-only spellings reported as `too late`, seen red against `c825fd2c` |
| `SECURITY.md` *What is in scope* (read) | "a check that fails open is a security defect here, not a correctness one, and each gate's test file holds its cases for that class". The cases of this work go into `tests/skills/test_deferral_check.py` |
| `CLAUDE.md` *The rule a mechanism is kept against* (read) | "A check gates only a fact it reads." A trigger the scan did not read is no fact it read, so it cannot resolve a deferral |
| `docs/the-record-layout.md` *Whether a line is live is asked by what the line does* (read) | The policy's direction for a line that excuses something: it "is not taken on doubt". An `answers` line excuses a deferral to CI, so an unread trigger takes the same direction. `seal deferrals` is none of the four readers that section names, so the section is cited as the direction and not changed |
| `docs/README.md` (read) | The policy index has no topic for `seal deferrals` or for deferring a check. The rule lives in `skills/verify/SKILL.md` *The answerer has to exist*, outside the policy root, so `## Rule changes` holds the no-change block |
| `skills/verify/SKILL.md` *The answerer has to exist* (read) | It lists four outcomes the command separates and says "Exit 1 means the row about to be written is not true". This work adds a fifth outcome to that list, and an unread trigger takes exit 1 |
| `seal/threads/1793171931-checks-that-read-text-pass-what-they-cannot-read/trail/phases/phase-1.md` row R14 and `trail/phases/phase-5.md` row R14 and its filing table (read) | The audit's finding, measured at `c825fd2c`, filed as #1123 |
| `git -C <worktree> diff --stat c825fd2c ea08c39c -- skills/verify/scripts/deferral_check.py tests/skills/test_deferral_check.py` (executed: empty output, exit 0) | Neither file changed since the audit's commit. A case seen red at this branch's base is seen red against `c825fd2c`'s `deferral_check.py` |
| Probe 1 at `ea08c39c` (executed; `python3 -I test_tmp_shapes.py <clone> <work>` in a `git clone --no-local` under the scratch directory; one workflow per spelling, running `pytest`, then `deferral_check.py --kind tests`) | Fails open, exit 0 on a push-only run, printed `answers ... (trigger unread)`: `"on":` with `push:` at two spaces; `on:` with `push:` at four spaces; `'on':` with `push:` at two spaces; `on:` followed by `- push` at indent 0; `on: [` with `push` on the next line; no `on:` key at all. Reads right, exit 1 `too late ... (on push ...)`: `on:` with `push:` at two spaces; `on: # triggers` with `push:` at two spaces; `push:` at two spaces with a nested `pull_request:` at four. Misreads to a refusal with a wrong event name, exit 1: `on: push # trigger` printed `(on push # trigger, ...)`; `on: pull_request # trigger` printed `too late` for a pull-request workflow; `on: [push] # trigger` printed `(on push] # trigger, ...)`; `on: {push: {branches: [main]}}` and `on: {pull_request: {}}` printed the whole mapping as one event, `too late`. Reads as unread and answers, exit 0: `on:` with `pull_request:` at four spaces, and `"on":` with `pull_request:` at two spaces |
| Probe 2 at `ea08c39c` (executed; `python3 -I test_tmp_shapes2.py <clone> <work2>`, same method) | An event key at the block's indent that carries a value or a comment on its own line is skipped. `push: {branches: [main]}` alone at two spaces: exit 0, `answers ... (trigger unread)`. `push: # on main` at two spaces: exit 0, `answers ... (trigger unread)`. `pull_request: {types: [opened]}` alone: exit 0, `(trigger unread)`. `push: {branches: [main]}` beside a bare `pull_request:`: exit 0, `(on pull_request)`, the push key dropped. `workflow_dispatch: {}` beside `push:` is dropped from the printed set |
| `grep test_deferral_check.py .test_durations`, summed (executed) | The module's 12 cases took 1.04 s in the recorded durations |
| `evals/behaviour/proofer/replay-1791382684-r2/graders/truth-inspect-reads.md` and its `scaffold.sh` (read) | The grader pins `deferral_check.py` line numbers 176 to 206, but `scaffold.sh` checks out `7ef6abbf`, so the pin reads that commit's file and not this branch's. Line moves here do not touch it |
| `tests/censuses.py#heading_rule` and `#splitlines` (read) | A code line holding `startswith("#")` or `.splitlines(` in a shipped script needs its exemption comment on its own line above it, as `read_events` and `runners_in` carry today. A new line of either kind in `read_events` carries the same comment |
| The parallel work items #1127, #1132 and #1158: their branches against `8d8d6390` (executed, `git diff --name-only`: each holds its `routing.md` alone) and their uncommitted frames in their worktrees (executed `grep`, and read) | None of them edits a file this work changes. #1127 reads `README.md` and `README.ko.md` as corpus and names `deferral_check.py` as a file it does not edit (`frame/questions.md`, *Settled from the tree*) |

## Scope

In:

1. **`skills/verify/scripts/deferral_check.py#read_events` reads the
   spellings in use.** The top-level key is `on`, `"on"` or `'on'`, at the
   start of a line. Its value is read in three forms:
   - an inline scalar, `on: pull_request`;
   - an inline flow list closed on the same line, `on: [push, pull_request]`;
   - a block below the key. The block's indent is the indent of its first
     line that is neither blank nor a comment. That indent is any width of
     one space or more, or zero where the line begins with `- ` (a block
     sequence YAML allows at the parent key's indent). Each line at that
     indent is one entry: a key, with or without a value or a comment after
     its colon, or a `- ` sequence item. A deeper line belongs to an entry
     and is skipped. A shallower line, or a line at indent zero that is not
     a `- ` item, ends the block.

   In every form, a trailing YAML comment (a `#` at the start of the value
   or after whitespace) is dropped before the value is read, and one pair of
   matching quotes around an event name is dropped.
2. **What `read_events` cannot read is unread as a whole.** The trigger is
   unread where the file has no top-level `on` key, where the value is a
   flow mapping (`on: {...}`) or a flow list not closed on its line, where
   a block holds no entry, and where any one entry or list element is not
   an event-shaped name, `[A-Za-z_][\w-]*`, after the comment and quotes
   are dropped. A partly read trigger is not returned as a smaller set:
   one element it could not read makes the whole trigger unread.
3. **`#inspect` reports an unread trigger and does not count it.** A
   workflow that runs the kind and whose trigger is unread goes to a fourth
   list beside `resolving`, `wrong_trigger` and `local_only`. It is printed
   as `  unread    <name> (trigger unread, not counted) — <commands>`, and
   the kind resolves only where the `resolving` list is not empty. Exit
   codes keep their meaning: 0 every requested kind resolves, 1 at least
   one does not.
4. **`KNOWN_LIMITS` names the new limit.** One clause is added to the
   printed limit: a trigger written as a flow mapping, or as a flow list
   across lines, reads as unread and is not counted.
5. **The text that lists the outcomes lists five.** The module docstring
   of `deferral_check.py`, which says "three outcomes" and lists four, is
   rewritten in place to list the five. `skills/verify/SKILL.md` *The
   answerer has to exist* adds the fifth to its list: something runs it,
   but its trigger could not be read, so it is not counted. `README.md`'s
   `seal deferrals` row and `README.ko.md`'s matching row add *trigger
   unread* to the outcomes they name.
6. **The cases**, in `tests/skills/test_deferral_check.py`, one per
   scenario row below, each seen red against this branch's base.

Out:

- **A YAML parser.** The module's docstring decides a text scan because
  the gates here are stdlib-only. `plan.md` *Alternatives considered*
  weighs it.
- **The triggers of other CI systems.** `#inspect` counts a runner in
  `.gitlab-ci.yml` and the other single-path configs as `pipeline`, and
  its comment states why: those systems run every pipeline on push by
  default, which includes the branch a merge request comes from. That is a
  stated reading of a default and not a trigger the scan failed to read.
  Whether their `rules:` or `only:` restrictions should be read is a
  different defect. #956's audit recorded no probe of it, and #1038
  decides larger reader fixes by the record.
- **`on: push` with no branch filter read as `too late`.** A push without
  a filter also runs on the head branch of a same-repository pull request,
  before the merge. The scan refuses it, so the error is a false refusal
  and not a pass. `test_runner_on_wrong_trigger_is_named_not_counted` pins
  `push` filtered to `main`, and #1123 does not ask for the case.
- **A runner word in text that does not run it.** Probe R14 at `c825fd2c`
  read `run: echo skip pytest` as a test run. `KNOWN_LIMITS` already says
  the scan reads command text. #1123's body and *Done when* do not name
  this case, so it stays out of this work.
- **`workflow_call`.** A reusable workflow called from a pull-request
  workflow reads as `too late`, and `KNOWN_LIMITS` already names a runner
  reached through a reusable workflow.
- **Removing `seal deferrals`.** `plan.md` *Alternatives considered* weighs
  it.

## User scenarios & acceptance *(mandatory)*

Every scenario is one workflow file under `.github/workflows/` in a
temporary project, run through `deferral_check.py --kind tests`, the way
the existing cases of `tests/skills/test_deferral_check.py` run it.

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The quoted key, push only | Given `"on":` with `push:` at two spaces and a `pytest` step. When the scan runs. Then it prints `too late` with `on push`, and exits 1 | A case in `tests/skills/test_deferral_check.py`, seen red at this branch's base (probe 1: exit 0, `answers ... (trigger unread)`) |
| S2 Four spaces, push only | Given `on:` with `push:` at four spaces and `branches:` at eight. Then `too late` with `on push`, exit 1 | A case, seen red at base (probe 1: exit 0) |
| S3 The rest of the push-only class | Given each of: `'on':` with `push:` at two spaces; `on:` followed by `- push` at indent zero; `on:` with `push: {branches: [main]}` at two spaces; `on:` with `push: # on main` at two spaces and `branches:` below. Then each prints `too late` with `on push`, exit 1 | One parametrised case, each parameter seen red at base (probes 1 and 2: exit 0) |
| S4 The new spellings are read, not only refused | Given `"on":` with `pull_request:` at two spaces, and separately `on:` with `pull_request:` at four spaces. Then each prints `answers` with `on pull_request`, exit 0 | A parametrised case asserting the `on pull_request` text, seen red at base, where both printed `(trigger unread)` |
| S5 An unread trigger is reported and not counted | Given each of: no `on` key; `on: {pull_request: {}}`; `on: [` with `push` on the next line and `]` after it. Then the scan prints an `unread` line holding `trigger unread, not counted`, prints no `answers` line, and exits 1 | A parametrised case, seen red at base (no `on` key and the multi-line list: exit 0 `answers`; the flow mapping: exit 1 but printed `too late` with the mapping as an event name) |
| S6 An unread workflow beside one that answers | Given one workflow with no `on` key and a `pytest` step, and a second with `on: pull_request` and a `pytest` step. Then the scan prints both an `answers` line and an `unread` line, and exits 0 | A case, seen red at base, where no `unread` line was printed |
| S7 Trailing comments on an inline value | Given `on: pull_request # trigger`. Then `answers` with `on pull_request`, exit 0. Given `on: [push] # trigger`. Then `too late` with `on push,` and no `]` or `#` in the event text, exit 1 | A parametrised case, seen red at base (probe 1: `too late` for the pull request, and `on push] # trigger`) |
| S8 The printed limit names the new limit | Given any project. Then the `limit:` line printed at the end names a flow mapping as read unread and not counted | A case asserting the clause, seen red at base |
| S9 What held before still holds | Given the eleven cases of `Test_main` and the case of `Test_module`. Then each passes unchanged | The existing cases, run in the same command as the new ones |
| S10 The documents list the fifth outcome | `skills/verify/SKILL.md` *The answerer has to exist*, the module docstring, `README.md` and `README.ko.md` name the unread outcome, and the docstring's count matches its list | check: none reader: the proofer at review |

## Data & interfaces

- `deferral_check.py#read_events(text)` keeps its signature and returns a
  set of event names. The set is empty exactly where the trigger is unread,
  as Scope item 2 defines it. A trigger that was read always names at least
  one event, so the empty set has one meaning.
- `deferral_check.py#inspect(root, kind)` keeps its signature and its
  `(verdict, lines)` return. The verdict is `True` only where `resolving`
  is not empty. A new list holds the unread workflows, and its lines print
  after the `too late` lines and before the `local` lines, in the shape
  `  unread    <name> (trigger unread, not counted) — <commands>`, with the
  label padded to the same ten-character column as `answers   `,
  `too late  ` and `local     `.
- `KNOWN_LIMITS` stays one string, printed once after `limit: `, and gains
  the clause of Scope item 4.
- No caller outside the module reads `read_events` or `inspect`. The
  `git grep` for `deferral_check`, `read_events` and `trigger unread`
  (executed) finds the script named in code only by the `seal` dispatcher
  in `skills/implement/scripts/seal.py`, which runs it as a command and
  hands it every argument (read, with
  `tests/skills/test_seal.py`'s `deferrals` case).

## Rule changes

- nothing
  why: no section of the policy root `docs/` states what `seal deferrals` reads or counts; `docs/README.md` indexes no such topic. The rule this work changes lives in `skills/verify/SKILL.md` *The answerer has to exist*, outside the policy root, and the cases in `tests/skills/test_deferral_check.py` hold it.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The `not events` arm that counts a workflow with an unread trigger as answering | `skills/verify/scripts/deferral_check.py#inspect` | The unread list of Scope item 3, printed and not counted |
| The `(trigger unread)` text on an `answers` line | `skills/verify/scripts/deferral_check.py#inspect` | The `unread` line, which carries `trigger unread, not counted` |
| The `indent <= 2` bound on an event key | `skills/verify/scripts/deferral_check.py#read_events` | The block's own indent, taken from its first entry, as Scope item 1 defines it |
| The docstring sentence "Anything else lands as an empty set, which is reported as unknown rather than as absent." | `skills/verify/scripts/deferral_check.py#read_events` | The rewritten docstring, which says an empty set is an unread trigger and is not counted |
| The count "three outcomes" | `skills/verify/scripts/deferral_check.py`, the module docstring | The same docstring, listing five outcomes |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-29 by framer, before the build.
