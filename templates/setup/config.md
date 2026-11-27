# Repository config

What this repository says about itself: `config.json`, one JSON object with
one key per item, read by the skills and commands that need it. Each value
is a JSON string in the grammar this file gives its key.

The root is the first of the places the opening paragraph of the plugin's
`skills/core/SKILL.md` names that holds the marker: committed in shared
mode, and under the common git directory, never committed, in local mode.
The file goes wherever that root already is, and `seal mode` creates it.

**An absent key is not an error, with four exceptions: the two language
keys, `Mode` and `Broad gate`.** Every other item has a default, and the
defaults are what every repository got before the key existed. Beyond those
four keys, a repository writes a key only where its answer is not the
default; a key that restates a default is a key nobody needs. An item is
named by its key spelt as this file spells it, case included. A key spelt
otherwise, such as `Policy Root`, names no item, so the item reads as
absent.

**`Mode` has no default.** An absent one is filled in from where the folder
is, by `seal mode` (*Mode* below). Nothing else reads the key, so an absent
one stops nothing: every script finds the root by where the folder is,
`seal mode --check` reports the key as not declared and exits 0, and the
next bare `seal mode` writes it.

**An absent `Broad gate` is a refusal, not a prompt:** `seal gate` names the
key and exits 2 with nothing run, because a run over a command nobody chose
proves nothing (*Broad gate* below).

**An absent language key is a refusal at the pull request body, and never
at a commit.** A language key is absent in four ways: no file, no such key,
an empty value, and a file that cannot be read or does not parse as one
JSON object, a key written twice or holding no string among them. The
fourth way is the refusal the next paragraph gives, and for these two keys
it counts as absent wherever this file or a skill speaks of an absent key.
In each, `seal pr-body` refuses with nothing written, naming the key, or printing
the refusal the next paragraph gives where the file or the key will not
read. A commit or a record is written in English, because a config nobody
can read must not stop the work. Who asks for the two keys is *Commit and
pull request language* below.

**A key written twice has no value, and a file that will not read is
refused rather than read as absent.** One reader answers every key of this
file, `lib/config.py`, through the standard library's JSON parser. A key
written more than once is neither its first nor its last: it is refused in
the sentence "`<item>` appears N times — one value". A value that is not a
string is refused for its key alone, naming its JSON type, and every other
key is read. A file that is there and cannot be read as UTF-8 text, does
not parse as JSON (a trailing comma, a quote left open), or whose top level
is not one object is refused for every key, naming its path and the
parser's message; a file that is absent still declares nothing, and a byte
order mark an editor wrote reads. `seal fold`, `seal gate`, `seal mode` and
`seal pact` print the refusal and exit 2 with nothing judged, as they do
for a value they cannot parse; `seal pr-body` prints it and exits 1 with
nothing written. `seal rules`,
`seal settle` and `seal unverified` read the `Policy root` and
`Reference specs` defaults instead, as they do for a key written twice.
Whoever writes the file repairs it by deleting the extra key or by
correcting the JSON.

```json
{
  "Commit and pull request language": "English",
  "Record language": "English",
  "Mode": "",
  "Broad gate": "",
  "Reference specs": "",
  "Pact": ""
}
```

An empty value declares nothing, as an absent key does. `Mode` is empty in
this example on purpose (*Mode* below).

## Commit and pull request language

The language the **commit subject and body**, the **pull request title and
body**, and the **review report posted as a pull-request comment** are written
in. `commit-pr-convention` reads this key before writing any of them. The
value is a language's English name, such as `English`, `Korean` or
`Japanese`, because the reader is a model choosing prose, not a lookup table.

In the body of a pull request routed through the review chain, the key
governs the lines of the work item's `pr.md` that quote no record: its
`Closes`, `Part of` and attribution lines. `pr.md` stands in the body's
first part, above the line `skills/code-review/scripts/pr_body.py#HEADING`
holds. A quote in
`pr.md` is its record's sentence as it stands, and the part below that line
is the records' own text, copied by `seal pr-body`, so both are in
`Record language`. Where this key and `Record language` name different
languages, the key also governs the mirror that opens the body (*What no
key governs* below).

**This key is required, and so is `Record language`.** First setup asks
for both, and the orchestrator asks for both before a work item's first
edit wherever either is missing. What an absent one does is the paragraph
opening *An absent language key* at the head of this file.

## Record language

The language the **prose** in the work-item records is written in:
`frame/design.md`, `frame/plan.md`, `gaps.md`, `frame/questions.md`,
`changelog.md`, `trail/phases/phase-N.md`, and in
`trail/rounds/round-N.md` each finding's heading and
account, the value of its close block's `answer:` line, the prose after each
confirmation block, and the cells of its tables.

**Independent of the key above, and required like it.** Setting one does
not carry the other: a key that silently inherited another's value would
declare a language nobody chose. Someone who set the commits to Korean and
left this one alone did not ask for Korean records, so both are asked.

The records have a human audience too, and its size differs by repository.
Where the whole team reads them, English is a tax on every reader; where the
repository is aimed outward, English is the point. That is a fact about the
people rather than about the file, which is why it is a key and not a rule.

**The review splits across the two keys on purpose.** The report posted to a
pull request is prose for whoever opens it, and follows the key above.
`trail/rounds/round-N.md` is half structure (`chain_check.py` reads its
headings and its `seal` blocks literally), and its prose follows this one.

## What no key governs

Changing a language changes prose and nothing else. These stay English in
every repository, whatever either key says:

- **The prefix vocabulary is not translated.** `feat:`, `fix:`, `docs:` and
  the rest are scanned in a log and parsed by tooling, and a translated
  prefix teaches neither.
- **Branch names.** ASCII, in the shapes `skills/commit-pr-convention/SKILL.md`
  *Branch names* states: a branch name is typed into a shell and pasted into
  a URL.
- **The field names, section headings and vocabulary a checker reads
  literally**: the info string `seal` that opens each block of a round
  record, an `inspection.md` and a `trail/gate.md`, and every key of those
  blocks and every fixed word of their values, whose one spelling is
  `lib/fields.py`, which `chain_check.py` and the stamp read them
  through; a round record's `## Findings` heading, which `chain_check.py`
  reads; a `gaps.md`'s `## Not verified` heading with its `Item` and
  `Who must answer` columns, or its no-change block `- nothing` with
  `why:`, and its `## Not done` heading; a `frame/plan.md`'s `## Phases`
  heading, which `seal pr-body` copies a section under, as it does those
  two of `gaps.md`; a `frame/design.md`'s `## Rule changes` heading, the
  items `add`, `change`, `remove` and `nothing` and the fields `file:`,
  `section:`, `from:`, `to:` and `why:`, which
  `skills/settle/scripts/rule_changes.py` reads, and the label `check:` of
  a check line inside a `to`, which `skills/settle/scripts/rules.py` reads; a
  `frame/plan.md`'s `## Judgments of the run` heading with its `Date`,
  `Judgment`, `Grounds` and `Judged against` columns, which `seal settle`
  groups the run's judgments by; and a `changelog.md`'s
  `### Process changes` heading, under which the release note lifts each
  fragment's rows into one table.
  A translated field name is not a translation, it is a broken gate.
- **The markers and anchors.** The word `closed` that opens a closed
  `## Not verified` row, the line `## From the records` that opens the
  part of a pull request body `seal pr-body` copies from the records, and
  the anchor table's header cells `Pact`, `Clause` and `Hash`.
- **Code.** Identifiers, comments, docstrings, file names, and test function
  names.
- **The keys of this file**, which a reader matches by their spelling
  rather than reads as prose, as it matches the keys of `parity.json`.
- **The response language**, what a session says to the person it works
  for. That is a person's setting, not a repository's, and it stays in the
  user's own configuration. Two people working in one repository can want different
  answers there and the same answer here.

Where the two language keys name different languages, the pull request body
opens with a mirror: the work item's own folder holds `pr.<lang>.md` beside
`pr.md`, written in `Commit and pull request language`, and `seal pr-body`
writes it above `pr.md`. It is named for **its own** language, the commit
key's: a repository whose records are English and whose commits are Korean
keeps `pr.ko.md`. What `pr.md` and `pr.<lang>.md` hold is stated in
`skills/code-review/orchestration.md` *Orchestrator: the pull request opens
once the work item is cleared*. A record has no
mirror: there is one file and a checker reads it, so its prose is whatever
`Record language` says and nothing else.

## Mode

Which of the two places this repository's root should live at: `local` or
`shared`. Empty in the example above on purpose (*There is no default*
below).

**This key is what the repository wants. The folder's location is what it
has.** They are separate on purpose, and the second is the only one anything
at runtime reads: every gate resolves the root by looking at the places the
opening paragraph of the plugin's `skills/core/SKILL.md` names, in its
order, and a gate that trusted this key instead would go looking in a place
with no folder. The key can be
edited by anyone with a text editor; the folder is where the files are.

`seal mode` is the only thing that reads it:

```bash
seal mode            # the folder, the key, and whether they agree
seal mode local      # switch to local mode, and write the key
seal mode shared     # switch to shared mode, and write the key
seal mode --apply    # switch to whatever this key says
```

A disagreement is the input the command consumes: a person edits the key,
runs `seal mode --apply`, and the folder moves. `seal mode --check`, which
the pull-request checks run, exits non-zero for a disagreement left
standing, so the key cannot quietly go false.

**There is no default, and an absent key is filled in from the folder.**
An item with a default falls back to what repositories got before the key
existed; for the mode, what they got is *the folder decides*. So the first
`seal mode` in a repository with no such key writes one from where the
folder actually is, an observation rather than an assumption, and says
that it did. Where there is no file at all, it writes `{"Mode": "<the
folder's mode>"}` and nothing else. A fixed default of `shared` would write
a lie into every local-mode repository that had not declared one.

That is also why the key is empty in the example above. A file written from
that example with `shared` in it would hand every local-mode repository a
key that is wrong from the moment it lands.

## Broad gate

The repository's own broad command (the full suite, the repository-wide
lint, the typecheck) as **one shell command line**, run from the repository
root by `seal gate` once the review rounds settle. The plugin's own checks
follow it and are not part of the key; the module docstring of
`skills/verify/scripts/broad_gate.py` lists them, in the order they run.
`seal gate --preflight` runs those checks alone, reading the key and not
running its command, and writes nothing; the orchestrator runs it before
the inspector is spawned.

```json
"Broad gate": "uvx ruff check . && uvx ruff format --check . && bin/test -q"
```

**An absent key is a refusal, not a default.** `seal gate` names this key
and exits 2 with nothing run. It is a refusal rather than a prompt because
the orchestrator runs the command unattended, with nothing else running, and
asks nobody anything: a refusal that names whose the key is and where it is
answered reaches that person through whoever read it, where a question stops
a session that may have nobody at the keyboard. It does **not** name a
command to write, because the party reading it is the one party that may not
choose one.

**There is no default, and the reason is the Inspection Test.** `verify` names the
counterfeit: a check that cannot fail. A default of `pytest` passes a
repository that runs `npm test`; a default of `true` passes everything. The
orchestrator that runs the gate does not pick a command either: a key is a
thing a person wrote, and what the broad run covers is exactly that. What the
command does is the repository's own claim: a command that exits 0
without running anything passes over nothing, and *the narrow command
still has to be able to fail* is the reader's rule, not the gate's.

**The value is a JSON string, so a `"` and a `\` in the command are
escaped.** A `"` is written `\"` and a `\` is written `\\`; a pipe, a `$`
and every other character are written as they stand. A single `\` before
`t` or `n`, as in a Windows path such as `C:\tools\new\pytest.exe`, reads as
a tab or a new line, and the gate runs a command nobody wrote. No reader
refuses it, because a value is a string the person wrote and the command it
then runs fails loudly.

**Which shell runs the command, and what the gate refuses there.**
`/bin/sh` on macOS and Linux. On Windows it is whatever `%COMSPEC%` names,
which is `cmd.exe` unless somebody changed it. `cmd.exe` reads a `/` inside
a command name as the start of a switch: handed `bin/test -q`, it runs a
command called `bin` and fails before any test does, and the report reads
as the suite failing. So where the shell is `cmd.exe`, the gate refuses a
command name that starts in a directory with `/`, and the refusal names
the name's `\` spelling. The example key above is refused there in a
repository that holds `bin/`. Every shell is handed the key's value as
written. One value cannot carry both spellings, because `/bin/sh` reads
`bin\test` as another name. So a key that runs under both shells names its
commands with no directory in front, and hands a script's path to an
interpreter as an argument.

**Which words the gate reads as command names.** The gate reads the value
up to its first `"`, `^` or `%`, because each of the three can move where
`cmd.exe` ends a command: a `"` hides a separator, a `^` escapes one, and a
`%VAR%` can expand to one. It splits that part at blanks and tabs. A word
is read as a command name where it is the first word, or where the word
before it is exactly `&&`, `||`, `&` or `|`. A command name is refused
where it holds a `/` and the part before its first `/` names a directory
under the repository root, where the command runs. An empty part (a name
that opens with `/`), `.` and `..` each name one, and on Windows so does a
drive, so `C:/Python/python.exe` is refused naming `C:\Python\python.exe`.
So `pytest tests/x.py` and `uvx ruff check src/` are not refused, because
`tests/x.py` and `src/` are arguments, and `bin -q` is not, because it
holds no `/`. A name that holds the `"`, `^` or `%` the reading stops at,
such as `bin/%TOOL%`, is never refused, and nor is any name after it.

**What the gate does not read is named, and decides nothing.** Where the
value holds a `"`, `^` or `%`, the gate names each word that holds the
first of them or stands after it, and that the same reading of the whole
value would refuse, with the character the reading stopped at. It names
the word as far as the blanks on either side of it, which is not always
the name `cmd.exe` reads. Where nothing is refused, that is one
line before the run, and the command then runs as written. Where a name is
refused, the refusal carries the same line. Under `/bin/sh`, or a
`COMSPEC` naming another shell, the gate reads nothing of the command for
this form and names nothing.

**Where the reading and `cmd.exe` differ.** The reading above is the
whole of what the gate decides by. It models nothing else of how `cmd.exe`
splits a line, and the root is read before anything runs. So wherever a
key uses more of `cmd.exe`'s syntax than the reading reads, the two can
disagree, in either direction.

- **A name `cmd.exe` runs where the reading takes none is neither refused
  nor named**, and `cmd.exe` fails on it as it does on `bin/test -q`. That
  is any command name that does not stand as the first word, or as the
  word after a separator word with a blank on each side, or whose part
  before the `/` is a directory only once the line has run. Examples are a
  name behind a leading `@`, as in `@bin/test`, a name after a redirection
  that opens its command, as in `>out.txt bin/test`, a name after a
  separator glued to a word, as in `a&& bin/x`, and a name in a directory
  an earlier command makes or a `cd` enters. A key stays inside the
  reading where each command name, with nothing glued in front of it, is
  the first word of its command and stands before the first `"`, `^` or
  `%`, and every separator has a blank on each side.
- **A word the reading takes for a command name that `cmd.exe` would not
  run is refused**, where its part before the `/` names a directory of the
  root. Examples are the text after `rem`, as in `rem a && bin/test`, and a
  switch glued to a program named like a directory of the root, as in
  `xcopy/e/i` in a repository with an `xcopy/` directory. The `\` spelling
  answers the first, and a blank before the switch (`xcopy /e/i`) answers
  the second.

The gate grows no reading for any such shape, because each one read is
one more piece of a model of `cmd.exe`, and the gate carries none.

**A commit after the run that changes only the work item's records does not
run the command again** (`skills/code-review/orchestration.md`
*Orchestrator: the pull request opens once the work item is cleared*). So a part of
the command that reads those records, such as a Markdown lint over every
`.md` file or a suite case over `seal/threads/`, reads them as they stood at
the run. Where the repository runs the same command in its pull request's
CI, that run reads the later records. Where it runs the command nowhere
else, the repository answers for what the command would have found in
them.

### What is refused, and what stays allowed

**A value that would not run as the command it reads as is refused, not
repaired.** `seal gate` looks at the key's command before it hands it to a
shell, and each form in the table below comes back exit 2 with nothing run,
the same shape an absent key gets. The criterion is one sentence with two
halves, and a form is refused only for breaking one of them:

> **The value must run as the command it reads as, and the exit code the
> gate reads must be that command's.**

| Refused | Written as | What a shell does with it |
|---|---|---|
| the whole command wrapped in backticks | `` `bin/test -q && ruff check .` `` | runs the content, **discards its exit status**, then executes its OUTPUT as a command. The same content exits 1 bare and 0 wrapped, with the failure still on the screen |
| the whole command wrapped in `$(…)` | `$(bin/test -q && ruff check .)` | the same semantics in the spelling somebody who knows shell reaches for first |
| a trailing `&` that is not part of `&&` | `bin/test -q &` | `/bin/sh` backgrounds the whole line and answers 0 before any check has finished. `cmd.exe` separates two commands instead, so what the gate reads is the second one's status. Two different wrong answers, refused for the same half of the criterion |
| a command name that starts in a directory with `/`, where the shell is `cmd.exe` | `uvx ruff check . && bin/test -q`, in a repository that holds `bin/` | `cmd.exe` reads the `/` as the start of a switch, runs a command called `bin`, and fails before any check has run, so the report reads as the suite failing. `/bin/sh` runs the same value as written, so the form is refused only where the shell is `cmd.exe`. *Broad gate* above says which words the gate reads as command names |

**Nothing is stripped.** A value quietly repaired here would leave the file
still wrong and teach the next person that the way they wrote it was right,
so the refusal names the form, quotes the key's value as written, and shows
it as meant. The value as meant removes the form the refusal names and
nothing else, so a key that holds a second refused form, such as
`` `bin/test -q` `` on `cmd.exe` in a repository that holds `bin/`, is
refused for that one by name on the next run. Rewriting it is the person's
act, and `/agentic:config` is the door to the key.

**Everything else stays legal**, because the value is an arbitrary shell
command line by design. A gate that could tell a status-discarding `;` from
one inside a quoted argument would need a shell parser, whose own failure
modes would make legitimate values unwritable. What each costs is stated
here rather than paid for by a refusal:

| Stays legal | What it costs |
|---|---|
| `$(…)` **inside** a longer line | nothing. `pytest -n $(nproc)` still runs as the command it reads as |
| `;`, `\|\|`, quotes, redirection, variables, globs | the command answers with whatever the composition the repository wrote answers with. That is the repository's own claim about itself, which is what this key already is. A pytest session the command runs that did not pass by its own record still fails the suite, whatever the composition exits (rule 3 of *The criterion for choosing a value* below) |
| a pipe | the same, and one thing more. A piped command exits with the pipe's LAST status, so `bin/test -q \| tee out.txt` exits 0 whenever `tee` does. That exit is the repository's own claim about itself, and the gate still fails the suite where a pytest session under the pipe did not pass by its own record (rule 3 of *The criterion for choosing a value* below). A JSON string carries a pipe as written, so the value holds it with nothing escaped |
| an `&` anywhere but at the end | the command before it is backgrounded and its status discarded, exactly as a `;` discards one. Unlike a `;`, it may still be running when the gate reports, writing into the tree the report is about. That is `/bin/sh`; `cmd.exe` sequences the two commands instead, so nothing is left running and the status read is the second command's. Telling an operator `&` from a `2>&1` or a quoted `&` needs the shell parser this list exists to avoid, so it stays the repository's own composition. The **trailing** form is refused, because nothing composes after it and the whole line goes to the background |

### The criterion for choosing a value

Three rules, and this section is their one home: every other document that
mentions the key links here.

| # | Rule | Why |
|---|---|---|
| 1 | A check that is red repository-wide for reasons unrelated to any branch does not belong in the command | It would block every future work item for something none of them caused, and a gate that always fails is read as noise and then ignored |
| 2 | A command that **fixes** the tree (`--fix`, `--write`, a formatter in write mode) is not a gate command | A gate asks what is wrong. One that changes the answer while reading it can only come back green, which is the counterfeit `skills/verify/SKILL.md` names |
| 3 | Every pytest the command runs keeps the environment the gate hands it | On a failing test the gate compares each failing file with the base from a record, never from what pytest printed. It runs the command with a pytest recorder of its own loaded: the recorder's directory first on `PYTHONPATH`, `-p agentic_pytest_record` appended to `PYTEST_ADDOPTS`, and a key made fresh for the run. The first pytest session in each process that finds the key takes it out of that process's environment and writes down every test it ran with its outcome, and every file it could not collect, each by the path pytest collected it from, under `records/` in the kept output. A pytest a test starts, and an xdist worker, inherit no key and write nothing, so nothing a test prints or runs changes a word. The failing files are the ones that record holds failing, listed from the repository root with `/`. **Then the command runs once more, unchanged, at the base** (nothing appended, no part cut, every part run as written) in a scratch worktree the gate removes afterwards, kept as `suite-at-base.txt`, and each file reads one row of a table: where no pytest at the base left a record (the command ended before it started one, none loaded the recorder, or the one that did could not write its record and warned in `suite-at-base.txt`), `new?`; where the base's record holds a failing test or a failed collection of the file, `failing on base too`; where it holds the file and nothing of it failed, `new`; where it does not hold the file and the command exited 0, `new`, because the command ran to its end and never collected the file; and where it does not hold the file and the command exited otherwise, `new?` naming the exit, because the run may have ended before reaching it; so a file the branch added reads `new?` wherever the base's command already fails. Either `new` reads `new?` naming the count instead where a session of the base that ended non-zero left any test or collection out of every list, because one of them may be the file's failure: a test whose xdist worker died in its setup, before any report of it reached the controller, is one. A session that exited 0 failed nothing, so what it left out cannot be. One over-strictness is named rather than closed: a red session whose left-out reports all passed, such as a passing item a conftest parents to the session, still turns `new` into `new?`. Either `new` reads `new?` naming the count, too, where a session of the base stopped part-way, so the file's tests there may not have finished: it wrote no `end` line to its record, because its process died, as plain pytest does on a test that calls `os._exit` or segfaults, or its recorder stopped writing, a disk that filled among the causes; or its `end` line says pytest stopped it (an interrupt, `pytest.exit()` whatever code it chose, `-x` or `--maxfail`, a plugin's stop) or shows an exit other than 0, 1 and 5. Where a red session also left reports out, that count is the one named. Where no pytest the command ran at `HEAD` left a record, for any of those causes, the files come from its `FAILED` lines, each file reads `new?` with the reason, and the base is not run; where one runner loaded it and another did not, the other's failures stay in `suite.txt` and out of the list. **The cost is one more run of the whole command, and only when the suite fails**, whatever the number of failing files. Every part of the command runs in it as written, so a part after the runner that the branch's own run never reached, because `&&` stopped at its failing suite, runs at the base wherever the base's suite passes, its writes inside the scratch worktree removed with it and its writes outside it kept. So the runner may come first or last, and the order is the repository's trade: either way the command runs once, whole, at the base. **A command earns the measured word** by letting every pytest it runs load the recorder: it adds to the `PYTHONPATH` and `PYTEST_ADDOPTS` the gate hands it rather than replacing them, and runs pytest in that environment rather than in one it builds. A runner started by `tox`, `nox`, `env -i`, a container or a wrapper that rebuilds the environment without either variable writes no record, and so does a command that sets `PYTEST_ADDOPTS` to a value of its own; its files read `new?`. A command that keeps `PYTEST_ADDOPTS` and loses `PYTHONPATH` fares worse (one that replaces `PYTHONPATH`, an interpreter run with `-I` or `-E`, a wrapper that passes `PYTEST_ADDOPTS` or `PYTEST_*` on and not `PYTHONPATH`): pytest cannot import the module the `-p` names and exits 1 before any test runs, so the command fails at the gate. The person writing the command puts its directory in front of the variable instead (`PYTHONPATH=src:$PYTHONPATH` under `/bin/sh`), and passes `PYTHONPATH` on wherever `PYTEST_ADDOPTS` goes. The record names each file by the path pytest itself holds for the test or the collector, read in the process that holds it (an xdist worker too) and carried on the report, never by a name pytest made from that path, so a file outside the rootdir, a `--pyargs` module wherever Python imports it from and a collector a conftest builds are each named by their own path. It leaves three kinds of report out of every list, counts them on the record's `end` line, and the gate says how many under the failing files: a test with no file of its own, which a conftest or a plugin parents to the session or to a directory; a failed collection of the whole session, which is where pytest 7 lays a conftest's import error anywhere below the root; and a report that reached the recorder without its path, one a plugin built or rebuilt itself, unless the same xdist worker's last report was of the same test and not its teardown, as a test whose worker crashed in its body has; a report's node id alone never places it, because two tests can share one. The gate also says there how many sessions at `HEAD` stopped part-way, because the test such a session stopped in may be in no list. Where one did, the suite fails even where the command exited 0, as it does when a test calls `pytest.exit()` with a return code of 0 or `os._exit(0)`, because a stop that chooses the exit code says neither that the session ran every test it collected nor that nothing it ran failed. So does a session whose `end` line shows exit 1 with nothing stopping it, whatever the command exited: that exit is the one pytest's run loop gave, which pytest hands every `pytest_sessionfinish` hook alike, so an act after the loop that turns the command's exit into 0 does not change it. Such an act is a hook that sets the session's exit status, a later `pytest_sessionfinish` hook that raises `pytest.exit()`, a `pytest_unconfigure` hook that ends the process, or a part of the command after pytest, such as `; true` or a pipe. In either case the failure form says so, and no `trail/gate.md` is written. One stop is out of the record's reach. A stop raised before the recorder writes a session's first line, such as a `pytest.exit()` in a conftest's `pytest_configure`, leaves no record of that session, so the gate reads the run as though that session never started: it judges the run on the command's exit and on the records the command's other sessions left, where there are any. The path travels as a report attribute of the recorder's own, so a plugin that writes reports whole, pytest-reportlog's `--report-log` among them, writes it into the command's own log while the gate measures the command. One limit is named rather than closed: a test written to append to the record file the recorder is writing, or to write a record of its own with the gate's key, can put a line into a keyed record |

## Reference specs

The directories this repository keeps its own specifications in: history the
plugin reads and never takes. A person joining a project that had a
`specs/` before the plugin arrived keeps it where it is. The plugin writes
only to its own root, and it never moves, edits, absorbs or deletes a
reference root.

```json
"Reference specs": "specs/, docs/adr/"
```

| Value | Means |
|---|---|
| one or more repository-relative directories, separated by commas, each with or without a trailing `/` | those directories and everything under them |
| `none` | no reference root |
| absent or empty, or no `seal/` root at either place | every directory named `specs` outside the plugin's root, at any depth |

**What it governs.** The checks that would read a record leave a reference
root out: `seal unverified` prunes it from a directory walk while still
reading a file named to it explicitly. A prefix naming the plugin's own root
or anything under it is dropped, because the root's records are read whatever
this key says; `seal settle --apply` removes only under `seal/threads/`.
`seal settle --from` reads a reference root only where a person names it at
the settle, whatever this key says, and writes nothing there. One reader
answers the key, `lib/config.py#reference_roots`, and one predicate the
path question, `lib/config.py#under_reference_root`.

**What it asks of the party that frames or builds a change.** That party
reads a reference root when the change touches what it describes, and cites
what it read, in `frame/design.md` or in the statement `settle` folds into `docs/`,
so the next reader can open the same file.

## Pact

Two keys, each written in one repository of a pact
(`docs/layout/the-pact.md`). A work item that commits in more than one
repository, where those repositories keep a contract together, keeps the one
copy of that contract in `seal/pact.md` in one of them, the pact's
repository. Every repository of the work item is a signer. Every one except
the pact's repository names the pact in a `Pact` key. The pact's repository
needs no `Pact` key, because it is identified by holding `seal/pact.md`, and
lists every other signer in a `Pact signers` key.

- **`Pact`**: the origin remote URL of the pact's repository, such as
  `git@example.com:org/orders-api.git`; a signer of pacts held in more
  than one repository lists them separated by `;`. Absent: no pact is held
  elsewhere.
- **`Pact signers`**: in the pact's repository, the origin remote URL of
  every other signer, separated by `;`, such as
  `https://example.com/org/orders-web; git@example.com:org/orders-mobile.git`.
  The pact's repository does not list itself: it cites its own clauses as
  it cites any other heading of its own. Absent or empty: `seal pact`
  refuses the pact at exit 2, because a pact nobody signs is not a pact.

**The URL is compared normalised**, so `git@example.com:org/orders-api.git`
and `https://example.com/org/orders-api` name one repository. A pact anchor
names the pact by the same URL, in the `Pact` cell of a
`| Pact | Clause | Hash |` row of a work item's `frame/design.md`.

**A key that will not parse is refused in a sentence**, never read as
absent. `seal pact`, run at the pact's repository, reads its `Pact signers`
through `lib/config.py#signer_declaration` and each signer's `Pact` through
`lib/config.py#pact_declaration`, and exits 2 on either; a signer's CI reads
nothing of the pact. A signer whose config holds no `Pact` key naming the
pact is read as naming no pact, and `seal pact` exits 2 on a relationship
recorded on one side only.

## The inspection mark

A key per surface the inspection mark is shown on beside the terminal stamp. Each
is off unless its key turns it on, and no key stops anything by itself. The
pull request's check reads the body against what `seal pr-body` composes, so
there a body whose mark line differs from the composition fails a ready pull
request, as any other differing line does.

```json
"Pull request inspection mark": "yes",
"Release note inspection mark": "yes"
```

| Value | Means |
|---|---|
| `yes`, written exactly so | the surface carries the mark |
| absent or empty | no mark, and nothing is said |
| any other value, such as `Yes`, `on` or `true` | no mark, and the command that writes the surface names the key and its value as not read |

**`Pull request inspection mark`** is read by `seal pr-body`
(`skills/code-review/scripts/pr_body.py#inspection_mark`). Under `yes` it writes
one line, the plugin's icon at the default branch of the plugin's
repository, between the line
`skills/code-review/scripts/pr_body.py#HEADING` holds and the fold,
where the newest verdict block of the work item's `inspection.md` reads
`cleared` at a commit that only the closing records, `trail/gate.md` and
`inspection.md`, follow. A work item not cleared at HEAD gets no mark, and the
inspector and the pull request's check name why. The mark's address is the
plugin's repository and names no version, so the installed plugin and the
copy the pull request's check runs compose one line whatever release each
is. A body carrying it shows the image while that repository stays public
and the icon stays at its path on the default branch.

**`Release note inspection mark`** is read by the `mark` job of this plugin's own
release workflow, at the release's tag. Under `yes` the job attaches the
plugin's icon to the release as `mark.png` and the note's header shows it
beside the results the stamp states; under any other value it attaches
nothing and the header holds the results alone. The plugin ships no release
workflow, so in any other repository nothing reads this key.

**A key that will not read writes no mark and is named**, a key written
twice or holding no string among them; the command's exit code is what it
would be without the key.

## The fold's values

Two keys, read by `seal fold` and `settle` (`skills/settle/SKILL.md`). The
plugin sets no value; these keys are where a repository states its own.

```json
"Document token ceiling": "25000",
"Policy root": "docs"
```

| Key | Value | Absent |
|---|---|---|
| `Document token ceiling` | a positive whole number of estimated tokens, written as a string. A document of the policy root or of one of its groups past it is reported as one to split | no length is checked |
| `Policy root` | the repository-relative directory of the ratified policy documents, which the settle writes and every reader of them reads | `docs` |

**The estimate is a document's UTF-8 bytes halved, rounded up.** Measured
English ran 2.85 bytes a token and mixed Korean 2.15, so halving
overestimates both. What a document past the ceiling owes is
`skills/settle/SKILL.md` *A document past its ceiling is split, never
trimmed*.

**An absent key means not declared, and the command says so rather than
refusing.** A `Policy root` value that is empty, absolute or climbs out with
`..` reads as `docs`. The cost is stated rather than hidden: a key deleted
while tidying this file turns its check off, and the only trace is the one
line `seal fold` prints about it.

**A value that will not parse is refused.** A ceiling that is not a positive
whole number exits 2 naming the key, and nothing is checked. The `--ceiling`
flag overrides its key for one run.
