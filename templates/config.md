# Repository config

What this repository says about itself, one row per item, read by the skills
that need it. It sits in the root the plugin maintains, beside `parity.md`,
in the same shape: a markdown table.

The root is at one of two places and whichever exists is the answer:
`<repo>/seal/`, which is committed, or `$(git rev-parse --git-common-dir)/seal/`,
which is not. This file goes wherever that root already is.

**This file is optional, and an absent row is not an error, with two
exceptions: `Mode` and `Broad gate`.** Every other item has a default, and
the defaults are what every repository got before the row existed. A
repository needs the file only where one of its answers is not the default;
a file that restates the defaults is a file nobody needs.

**`Mode` has no default.** An absent one is filled in from where the folder
is, by `seal mode` (*Mode* below). It is not silent while absent: a root with
no `Mode` row is a root nobody chose a mode for, so the first Bash call of a
session in that repository is denied and the second is asked, until
`seal mode` writes the row. Two prompts per session per repository, then
nothing once the row exists.

**An absent `Broad gate` is a refusal, not a prompt:** `seal gate` names the
row and exits 2 with nothing run, because a run over a command nobody chose
proves nothing (*Broad gate* below).

**A row written twice has no value, and a file that will not read is
refused rather than read as absent.** One reader answers every row of this
file, `hooks/config.py`. A row written more than once in the table is
neither its first nor its last: it is refused in the sentence
"`<item>` appears N times — one value". A file that is there and cannot be
read as UTF-8 text (a directory of that name, or bytes another encoding
wrote) is refused naming its path; a file that is absent still declares
nothing. A command a person runs (`seal fold`, `seal gate`, `seal mode`,
`seal pact`) prints the refusal and exits 2 with nothing judged, as it does
for a value it cannot parse. A hook says nothing: the mode gate is silent
rather than asking. Whoever writes the file repairs it by deleting the extra
row, or by writing the file as UTF-8.

**The table is read the way GitHub shows it, or refused.** The reader is the
walker the plugin holds to cmark-gfm, GitHub's renderer, so a row is a row
where GitHub shows it as one. A line it cannot read as GitHub shows it is
refused, in a sentence naming the line and the edit. The rows above that
line are read; every row written below it is that refusal, never an absent
row, because GitHub may show it and nobody read it. The commands and the
hooks act on it as on a row written twice. The shapes, each with its one
edit:

- a line directly above the header (a comment, a line of prose, a row of
  something else): leave a blank line above the header;
- a header with no delimiter row under it, or a delimiter row of another
  width: write `|---|---|` under the header;
- a bare pipe in a value, which GitHub shows cut off at the pipe: write it
  `\|` (*Broad gate* below says why);
- a third cell, a stray `|---|---|`, or a line of prose inside the table:
  write it as `| … | … |`, or take it out;
- a row under a comment, a fence or a blank line that ends the table: move
  it into the table; where it heads a table of something else, put a
  heading between the two tables;
- a row, the header or the delimiter row after a form feed or U+2028 on
  another line of the table, which GitHub shows as more of that line: put
  it on a line of its own.

A file `seal mode` wrote, and one copied from this template, has none of
these shapes.

| Item | Value |
|---|---|
| Commit and pull request language | English |
| Record language | English |
| Mode |  |
| Broad gate |  |
| Reference specs |  |
| Pact |  |

## Commit and pull request language

The language the **commit subject and body**, the **pull request title and
body**, and the **review report posted as a pull-request comment** are written
in. `commit-pr-convention` reads this row before writing any of them. The
value is a language's English name, such as `English`, `Korean` or
`Japanese`, because the reader is a model choosing prose, not a lookup table.

## Record language

The language the **prose** in the work-item records is written in:
`spec.md`, `plan.md`, `overview.md`, `questions.md`, `changelog.md`, and in
`rounds/round-N.md` each finding's heading, account and `answer:`, the prose
after each `confirms:` line, and the cells of its tables.

**Independent of the row above.** Setting one does not carry the other, for
the reason stated at the top of this file: an absent row's default is what
every repository got before the row existed, and a row that silently inherits
another's value is not that. Someone who set the commits to Korean and left
this one alone did not ask for Korean records.

The records have a human audience too, and its size differs by repository.
Where the whole team reads them, English is a tax on every reader; where the
repository is aimed outward, English is the point. That is a fact about the
people rather than about the file, which is why it is a row and not a rule.

**The review splits across the two rows on purpose.** The report posted to a
pull request is prose for whoever opens it, and follows the row above.
`rounds/round-N.md` is half structure (`chain_check.py` reads its headings,
its labelled lines and the four verdict values literally), and its prose
follows this one.

## What no row governs

Changing a language changes prose and nothing else. These stay English in
every repository, whatever either row says:

- **The prefix vocabulary is not translated.** `feat:`, `fix:`, `docs:` and
  the rest are scanned in a log and parsed by tooling, and a translated
  prefix teaches neither.
- **Branch names.** ASCII, in the shapes `skills/commit-pr-convention/SKILL.md`
  *Branch names* states: a branch name is typed into a shell and pasted into
  a URL.
- **The field names, section headings and vocabulary a checker or a pinned
  case reads literally**: every cell of a round record's grammar, the
  two tables in `docs/the-review-record.md` *The round record*, which
  `chain_check.py` reads; a round record's `## Not judged` and `## Probes`
  headings, which the parties and the eval graders read; a
  `guarantee.md`'s `Target SHA`, and its `Verdict:` line with the words
  `sealed`, `withheld`, `undecided`, `reason:` and `question:`; a
  `broad-gate.md`'s `Broad gate`; an
  `overview.md`'s `## Not verified` heading with its `Item` and
  `Who must answer` columns, or its no-change block `- nothing` with
  `why:`; a `spec.md`'s `## Removes` heading; its
  `## Rule changes` heading, the items `add`, `change`, `remove` and
  `nothing`, and the fields `file:`, `section:`, `from:`, `to:` and `why:`.
  A translated field name is not a translation, it is a broken gate.
- **The markers and anchors.** `<!-- specs/<work-item-id> -->`, a release
  section's `## X.Y.Z — <date>`, the word `closed` that opens a closed
  `## Not verified` row, and a pact
  anchor's `pact:<name>/"<heading path>"@<hash>`.
- **Code.** Identifiers, comments, docstrings, file names, and test function
  names.
- **The item column of this table**, which is a key rather than prose: the
  same rule `parity.md` already follows.
- **The response language**, what a session says to the person it works
  for. That is a person's setting, not a repository's, and it stays in the
  user's own configuration. Two people working in one repository can want different
  answers there and the same answer here.

Where a translated pull-request body is wanted, it goes in the repository as
a file, named for **its own** language rather than the body's: the work item's
own folder holds `pr.ko.md` when the commit row says English, and `pr.en.md`
when it says Korean. A record has no mirror: there is one file and a checker
reads it, so its prose is whatever `Record language` says and nothing else.

That folder sits under the root, which is resolved rather than spelled: the
same two places this file is looked for. Where the root resolves under the
git directory, the mirror does **not** go there, because nothing under it is
ever a commit candidate, so a reviewer cannot open the file and the merge
carries nothing. The mirror then goes beside the documents the pull request
already touches.

## Mode

Which of the two places this repository's root should live at: `local` or
`shared`. Empty in the table above on purpose (*There is no default* below).

**This row is what the repository wants. The folder's location is what it
has.** They are separate on purpose, and the second is the only one anything
at runtime reads: every gate resolves the root by looking for `<repo>/seal/`
and then `$(git rev-parse --git-common-dir)/seal/`, and a gate that trusted
this row instead would go looking in a place with no folder. The row can be
edited by anyone with a text editor; the folder is where the files are.

`seal mode` is the only thing that reads it:

```bash
seal mode            # the folder, the row, and whether they agree
seal mode local      # switch to local mode, and write the row
seal mode shared     # switch to shared mode, and write the row
seal mode --apply    # switch to whatever this row says
```

A disagreement is the input the command consumes: a person edits the row,
runs `seal mode --apply`, and the folder moves. `seal mode --check`, which
the pull-request checks run, exits non-zero for a disagreement left
standing, so the row cannot quietly go false.

**There is no default, and an absent row is filled in from the folder.**
Every other item here falls back to what repositories got before the row
existed; for the mode, what they got is *the folder decides*. So the first
`seal mode` in a repository with no such row writes one from where the
folder actually is, an observation rather than an assumption, and says
that it did. A fixed default of `shared` would write a lie into every
local-mode repository that had not declared one.

That is also why the row above is empty in this template. A copied file that
declared `shared` would hand every local-mode repository a row that is wrong
from the moment it lands.

## Broad gate

The repository's own broad command (the full suite, the repository-wide
lint, the typecheck) as **one shell command line**, run from the repository
root by `seal gate` once the review rounds settle. The plugin's own checks
follow it and are not part of the row; the module docstring of
`skills/verify/scripts/broad_gate.py` lists them, in the order they run.
`seal gate --preflight` runs those checks alone, reading the row and not
running it, and writes nothing; the orchestrator runs it before the sealer is
spawned.

```markdown
| Broad gate | uvx ruff check . && uvx ruff format --check . && bin/test -q |
```

**An absent row is a refusal, not a default.** `seal gate` names this row
and exits 2 with nothing run. It is a refusal rather than a prompt because
the orchestrator runs the command unattended, with nothing else running, and
asks nobody anything: a refusal that names whose the row is and where it is
answered reaches that person through whoever read it, where a question stops
a session that may have nobody at the keyboard. It does **not** name a
command to write, because the party reading it is the one party that may not
choose one.

**There is no default, and the reason is the Seal Test.** `verify` names the
counterfeit: a check that cannot fail. A default of `pytest` seals a
repository that runs `npm test`; a default of `true` seals everything. The
orchestrator that runs the gate does not pick a command either: a row is a
thing a person wrote, and what the broad run covers is exactly that. What the
row's command does is the repository's own claim: a command that exits 0
without running anything passes over nothing, and *the narrow command
still has to be able to fail* is the reader's rule, not the gate's.

**Which shell runs the row, and what it is handed.** `/bin/sh` on macOS and
Linux. On Windows it is whatever `%COMSPEC%` names, which is `cmd.exe` unless
somebody changed it, and `cmd.exe` reads a `/` inside a command name as the
start of a switch: handed `bin/test -q`, it runs a command called `bin` and
fails before any test does. So where the shell is `cmd.exe`, the gate
hands it the row with `/` written `\` inside a command name that starts in a
directory, and nowhere else. A command name is the word at the start of the
line, or the first word after `&&`, `||`, `&`, `|` or a `(` that opens a
block. It starts in a directory where the part before its first `/`, with its
quotes and carets removed and every leading `@` dropped, names a directory
that exists where the row runs; a name that begins with `/` starts at the
drive's root, which always exists. A plain `%VAR%` in that part is expanded
first, because `cmd.exe` expands it before it reads the name: from the gate's
own environment, and `%CD%` as the directory the row runs in unless the
environment defines `CD`, so `%CD%/bin/test` is still rewritten. A substring
or substitution (`%VAR:~0,2%`, `%VAR:a=b%`) is not expanded, so a name that
starts with one keeps its `/`. `bin/test` then runs as `bin\test`, which
`cmd.exe` resolves to `bin/test.cmd`. Arguments, quoted
paths, `%VAR%`, operators and `^`-escaped characters reach the shell as
written. Every other position is handed as written, and `cmd.exe` reads it
exactly as before: the definition above is the rule, and these are
examples of it rather than the whole list: a path after `call`, `start` or
`if`, or after `else`, `for … do` and `cmd /c`; a command name after a
redirection that opens its command (`>out.txt bin/test`); and a `/` written
straight after one of `cmd.exe`'s own commands, which is that command's
switch (`rd/s/q build`). A `/` written straight after any other program's
name reaches `cmd.exe` as written too, because no directory carries the
program's name: `xcopy/e/i` stays `xcopy/e/i`. A blank before the switch
(`xcopy /e`) works as well, and is never rewritten. The directory is judged
where the row starts, and that has two bounds. A directory an earlier command
in the row makes, or one a `cd` earlier in the row enters, is not seen, so
that name is handed over as written, which is what `cmd.exe` got before the
gate rewrote anything. And a directory at the root named like a program the
row calls with a glued switch (an `xcopy/` directory) makes `xcopy/e` read as
a path; `cmd.exe` itself cannot tell the two apart in that tree, so write the
blank there. Any other
`COMSPEC`, and every POSIX shell, is handed the row as written. Where the
two differ, the gate prints one line saying what `cmd.exe` was handed, and
that check's kept output carries it under the row as written.

### What is refused, and what stays allowed

**A value that would not run as the command it reads as is refused, not
repaired.** `seal gate` looks at the row before it hands it to a shell,
and three forms come back exit 2 with nothing run, the same shape an
absent row gets. The criterion is one sentence with two halves, and a form
is refused only for breaking one of them:

> **The value must run as the command it reads as, and the exit code the
> gate reads must be that command's.**

| Refused | Written as | What a shell does with it |
|---|---|---|
| the whole command wrapped in backticks | `` `bin/test -q && ruff check .` `` | runs the content, **discards its exit status**, then executes its OUTPUT as a command. The same content exits 1 bare and 0 wrapped, with the failure still on the screen |
| the whole command wrapped in `$(…)` | `$(bin/test -q && ruff check .)` | the same semantics in the spelling somebody who knows shell reaches for first |
| a trailing `&` that is not part of `&&` | `bin/test -q &` | `/bin/sh` backgrounds the whole line and answers 0 before any check has finished. `cmd.exe` separates two commands instead, so what the gate reads is the second one's status. Two different wrong answers, refused for the same half of the criterion |

**Nothing is stripped.** A value quietly repaired here would leave the file
still wrong and teach the next person that the way they wrote it was right,
so the refusal names the form, quotes the row as written, and shows it as
meant. Rewriting it is the person's act, and `/agentic:config` is the door
to the row.

**A table inside a code fence is an example of this format and never a
repository's own answer.** The live table is the first `| Item | Value |`
table that stands outside every fenced code block, and a line inside a fence
is not part of any table: not a header, not a separator, not a row, and not a
line somebody wrote as a row. One rule says so and the one walk of this
table reads through it (the gates, the mode gate, and `seal mode`'s writer
all read the rows it names), so the reader and the writer can never
disagree about which row is the row.

A fence opens at a line indented at most three spaces whose first run is three
or more backticks or three or more tildes, and closes at the next line of at
least as many of the same character with nothing after it but spaces. **A
fence that is never closed runs to the end of the file**, so everything under
it, the live table included, reads as undeclared: `seal gate` exits 2 with
a message and the mode question comes back. That is loud rather than quiet,
which is the trade this rule is written for.

What it prevents is quiet. The block `/agentic:config` copies out of this
file carries the fenced example row above; pasted above the live table, or
above a table with no parseable row yet, the example would otherwise be the
table every gate reads, a broad run over a plausible command nobody chose.
**`seal gate` says so by name**: where
this gate's row exists only inside a fence, the refusal quotes that line and
says where it has to move to, rather than reporting the row absent.

**A row inside an HTML comment that closes is not a row either.** A
comment block starts at a line that begins with `<!--` and runs to the first
line holding `-->`, and a row parked in one (an old command kept for
reference, a whole table put away) is not this repository's answer, so no
walk of the table reads it. A fence line inside such a comment opens no fence.
One reading decides both, and it is a CommonMark renderer's. Where a line's
context is one that reading cannot be sure of (inside a list item, after
inline HTML a line leaves open, such as a `<!--`, `<![CDATA[`, `<?`,
`<!DOCTYPE` or a tag started in the middle of a line, or below a block that
never closes), the line is read as outside any comment, so a `<!--` nobody
closed hides nothing. Where this
gate's row exists only inside a comment, the refusal quotes that line and says
it is commented out, rather than calling it absent or fenced.

**Everything else stays legal**, because the row is an arbitrary shell
command line by design. A gate that could tell a status-discarding `;` from
one inside a quoted argument would need a shell parser, whose own failure
modes would make legitimate rows unwritable. What each costs is stated here
rather than paid for by a refusal:

| Stays legal | What it costs |
|---|---|
| `$(…)` **inside** a longer line | nothing. `pytest -n $(nproc)` still runs as the command it reads as |
| `;`, `\|\|`, quotes, redirection, variables, globs | the row answers with whatever the composition the repository wrote answers with. That is the repository's own claim about itself, which is what this row already is |
| a pipe, **written `\|`** | the same, and one thing more. A piped row exits with the pipe's LAST status, so `bin/test -q \| tee out.txt` is green whenever `tee` is: the repository's own claim about itself. **This file is markdown and a cell of it ends at a bare pipe**, so `\|` is how the value carries one, the way every other cell of this table already writes it. The reader reduces exactly those two characters to a plain pipe before any shell sees it, so a value holding Windows path separators is untouched. **A BARE pipe is refused**: GitHub shows that row cut off at the pipe, so the command it shows is not the one written, and `seal gate` quotes the line, says to write it `\|`, and runs nothing. The walker reads no row below a line it refuses, so a `Mode` row written under it is that refusal rather than an absent row: `seal mode` writes nothing and names the line, and the mode gate says nothing. Written LAST in its table the line has nothing under it, and `seal gate`'s refusal says the rows below it go unread only where a row is written below it |
| an `&` anywhere but at the end | the command before it is backgrounded and its status discarded, exactly as a `;` discards one. Unlike a `;`, it may still be running when the gate reports, writing into the tree the report is about. That is `/bin/sh`; `cmd.exe` sequences the two commands instead, so nothing is left running and the status read is the second command's. Telling an operator `&` from a `2>&1` or a quoted `&` needs the shell parser this list exists to avoid, so it stays the row author's own composition. The **trailing** form is refused, because nothing composes after it and the whole line goes to the background |

### The criterion for choosing a value

Three rules, and this section is their one home: every other document that
mentions the row links here.

| # | Rule | Why |
|---|---|---|
| 1 | A check that is red repository-wide for reasons unrelated to any branch does not belong in the row | It would block every future work item for something none of them caused, and a gate that always fails is read as noise and then ignored |
| 2 | A command that **fixes** the tree (`--fix`, `--write`, a formatter in write mode) is not a gate command | A gate asks what is wrong. One that changes the answer while reading it can only come back green, which is the counterfeit `skills/verify/SKILL.md` names |
| 3 | Every pytest the row runs keeps the environment the gate hands it | On a failing test the gate compares each failing file with the base from a record, never from what pytest printed. It runs the row with a pytest recorder of its own loaded: the recorder's directory first on `PYTHONPATH`, `-p specseal_pytest_record` appended to `PYTEST_ADDOPTS`, and a key made fresh for the run. The first pytest session in each process that finds the key takes it out of that process's environment and writes down every test it ran with its outcome, and every file it could not collect, each by the path pytest collected it from, under `records/` in the kept output. A pytest a test starts, and an xdist worker, inherit no key and write nothing, so nothing a test prints or runs changes a word. The failing files are the ones that record holds failing, listed from the repository root with `/`. **Then the row runs once more, unchanged, at the base** (nothing appended, no part cut, every part run as written) in a scratch worktree the gate removes afterwards, kept as `suite-at-base.txt`, and each file reads one row of a table: where no pytest at the base left a record (the row ended before it started one, none loaded the recorder, or the one that did could not write its record and warned in `suite-at-base.txt`), `new?`; where the base's record holds a failing test or a failed collection of the file, `failing on base too`; where it holds the file and nothing of it failed, `new`; where it does not hold the file and the row exited 0, `new`, because the row ran to its end and never collected the file; and where it does not hold the file and the row exited otherwise, `new?` naming the exit, because the run may have ended before reaching it; so a file the branch added reads `new?` wherever the base's row already fails. Either `new` reads `new?` naming the count instead where a session of the base that ended non-zero left any test or collection out of every list, because one of them may be the file's failure: a test whose xdist worker died in its setup, before any report of it reached the controller, is one. A session that exited 0 failed nothing, so what it left out cannot be. One over-strictness is named rather than closed: a red session whose left-out reports all passed, such as a passing item a conftest parents to the session, still turns `new` into `new?`. Either `new` reads `new?` naming the count, too, where a session of the base stopped part-way, so the file's tests there may not have finished: it wrote no `end` line to its record, because its process died, as plain pytest does on a test that calls `os._exit` or segfaults, or its recorder stopped writing, a disk that filled among the causes; or its `end` line says pytest stopped it (an interrupt, `pytest.exit()` whatever code it chose, `-x` or `--maxfail`, a plugin's stop) or shows an exit other than 0, 1 and 5. Where a red session also left reports out, that count is the one named. Where no pytest the row ran at `HEAD` left a record, for any of those causes, the files come from its `FAILED` lines, each file reads `new?` with the reason, and the base is not run; where one runner loaded it and another did not, the other's failures stay in `suite.txt` and out of the list. **The cost is one more run of the whole row, and only when the suite fails**, whatever the number of failing files. Every part of the row runs in it as written, so a part after the runner that the branch's own run never reached, because `&&` stopped at its failing suite, runs at the base wherever the base's suite passes, its writes inside the scratch worktree removed with it and its writes outside it kept. So the runner may come first or last, and the order is the repository's trade: either way the row runs once, whole, at the base. **A row earns the measured word** by letting every pytest it runs load the recorder: it adds to the `PYTHONPATH` and `PYTEST_ADDOPTS` the gate hands it rather than replacing them, and runs pytest in that environment rather than in one it builds. A runner started by `tox`, `nox`, `env -i`, a container or a wrapper that rebuilds the environment without either variable writes no record, and so does a row that sets `PYTEST_ADDOPTS` to a value of its own; its files read `new?`. A row that keeps `PYTEST_ADDOPTS` and loses `PYTHONPATH` fares worse (one that replaces `PYTHONPATH`, an interpreter run with `-I` or `-E`, a wrapper that passes `PYTEST_ADDOPTS` or `PYTEST_*` on and not `PYTHONPATH`): pytest cannot import the module the `-p` names and exits 1 before any test runs, so the row fails at the gate. The person writing the row puts the row's directory in front of the variable instead (`PYTHONPATH=src:$PYTHONPATH` under `/bin/sh`), and passes `PYTHONPATH` on wherever `PYTEST_ADDOPTS` goes. The record names each file by the path pytest itself holds for the test or the collector, read in the process that holds it (an xdist worker too) and carried on the report, never by a name pytest made from that path, so a file outside the rootdir, a `--pyargs` module wherever Python imports it from and a collector a conftest builds are each named by their own path. It leaves three kinds of report out of every list, counts them on the record's `end` line, and the gate says how many under the failing files: a test with no file of its own, which a conftest or a plugin parents to the session or to a directory; a failed collection of the whole session, which is where pytest 7 lays a conftest's import error anywhere below the root; and a report that reached the recorder without its path, one a plugin built or rebuilt itself, unless the same xdist worker's last report was of the same test and not its teardown, as a test whose worker crashed in its body has; a report's node id alone never places it, because two tests can share one. The gate also says there how many sessions at `HEAD` stopped part-way, because the test such a session stopped in may be in no list. The path travels as a report attribute of the recorder's own, so a plugin that writes reports whole, pytest-reportlog's `--report-log` among them, writes it into the row's own log while the gate measures the row. One limit is named rather than closed: a test written to append to the record file the recorder is writing, or to write a record of its own with the gate's key, can put a line into a keyed record |

## Reference specs

The directories this repository keeps its own specifications in: history the
plugin reads and never takes. A person joining a project that had a
`specs/` before the plugin arrived keeps it where it is. The plugin writes
only to its own root, and it never moves, edits, absorbs or deletes a
reference root.

```markdown
| Reference specs | specs/, docs/adr/ |
```

| Value | Means |
|---|---|
| one or more repository-relative directories, separated by commas, each with or without a trailing `/` | those directories and everything under them |
| `none` | no reference root |
| absent or empty | every directory named `specs` outside the plugin's root, at any depth |
| no `seal/` root at either place | no reference root: the repository has not opted in, and the one layout the plugin read without a root is 0.3.x, whose top-level `specs/` was its own |

**What it governs.** The checks that would read a record leave a reference
root out: `seal unverified` prunes it from a directory walk while still
reading a file named to it explicitly. A prefix naming the plugin's own root
or anything under it is dropped, because the root's records are read whatever
this row says; `seal settle --apply` removes only under `seal/threads/`. One reader
answers the row, `hooks/config.py#reference_roots`, and one predicate the
path question, `hooks/config.py#under_reference_root`.

**What it asks of the party that frames or builds a change.** That party
reads a reference root when the change touches what it describes, and cites
what it read, in `spec.md` or in the statement `settle` folds into `docs/`,
so the next reader can open the same file.

## Pact

One row, written in a signer of a pact held in another repository
(`docs/the-pact.md`). A work item that commits in more than one repository,
where those repositories keep a contract together, keeps the one copy of that
contract in `seal/pact.md` in one of them. Every repository of the work item
is a signer, and every one except the pact's repository names the pact
here. The pact's repository needs no row: it is identified by holding
`seal/pact.md`.

- **`Pact`**: the origin remote URL of the pact's repository, such as
  `git@example.com:org/orders-api.git`; a signer of pacts held in more
  than one repository lists them separated by `;`. Absent: no pact is held
  elsewhere.

**The URL is compared normalised**, so `git@example.com:org/orders-api.git`
and `https://example.com/org/orders-api` name one repository. Its last path
segment is the name a pact anchor carries, `pact:orders-api/"## A"@1a2b3c4d`,
so two pacts whose URLs end in the same segment are refused as ambiguous.

**A row that will not parse is refused in a sentence**, never read as absent.
At this repository's pull request `chain-check` prints the sentence and its
exit status does not move: a signer's CI prints and does not verify.
`seal pact`, run at the pact's repository, reads the same row through the
same reader, `hooks/config.py#pact_declaration`, and exits 2 on it. A `Pact`
row the table does not hold is no row: `seal pact` then reads the signer as
naming no pact and exits 2 on a relationship recorded on one side only.

**A `Pact notify` row is read by nobody.** No command refuses it, prints it
or names it, like any item no reader asks for, and whoever next edits the
file deletes it. No reader names it, because naming it would keep a reader
for a row that changes nothing, and a refusal would stop `seal pact` at the
pact's repository over it.

## The fold's values

Two rows, read by `seal fold` and `settle` (`skills/settle/SKILL.md`). The
plugin sets no value; these rows are where a repository states its own.

```markdown
| Document token ceiling | 25000 |
| Policy root | docs |
```

| Row | Value | Absent |
|---|---|---|
| `Document token ceiling` | a positive whole number of estimated tokens. A top-level document of the policy root past it is reported as one to split | no length is checked |
| `Policy root` | the repository-relative directory of the ratified policy documents, which the settle writes and every reader of them reads | `docs` |

**The estimate is a document's UTF-8 bytes halved, rounded up.** Measured
English ran 2.85 bytes a token and mixed Korean 2.15, so halving
overestimates both. What a document past the ceiling owes is
`skills/settle/SKILL.md` *A document past its ceiling is split, never
trimmed*.

**An absent row means not declared, and the command says so rather than
refusing.** A `Policy root` value that is empty, absolute or climbs out with
`..` reads as `docs`. The cost is stated rather than hidden: a row deleted
while tidying this file turns its check off, and the only trace is the one
line `seal fold` prints about it.

**A value that will not parse is refused.** A ceiling that is not a positive
whole number exits 2 naming the row, and nothing is checked. The `--ceiling`
flag overrides its row for one run.
