# Contributing to AgenticSeal

## Opening a pull request

**A contributor bases the branch on the open release branch, not on
`main`.** GitHub offers `main` by default, and for everything except a
release that default is the wrong one here. Work collects on one release
branch and `main` moves once per release; `docs/branch-and-release.md` *Work
accumulates on a release branch* holds the reasoning, and this section is the
part a contributor needs.

**How to find it.** Exactly one branch named `release/vX.Y.Z` is open at a
time. On GitHub it is the only entry beginning `release/` in the branch
dropdown on the code page. In a clone:

```bash
git branch -r --list 'origin/release/*'   # the one to base on, and nothing else
```

The contributor sets it as the base when opening the pull request: the base
is the left-hand dropdown on the compare page. For a pull request already
open against `main`, the **Edit** button beside its title changes the base
without closing anything.

**Why a wrong base is refused with a message about a version.** A pull request
into `main` is a release here, so the checks that run there are a release's
checks, and one of them asks for `.claude-plugin/plugin.json` to move. A
contribution is not a release and must not touch that file. Changing the base
instead takes the refusal with it.

**The contributor opens the pull request when the work is done, and opens it
ready.** Every push to an open pull request runs the suite on Linux, macOS and
Windows, and a branch with no pull request runs nothing. So the branch is
pushed as often as the contributor likes, and the pull request opens once
nothing is left to push. `skills/code-review/orchestration.md` *Orchestrator:
the pull request opens once the sealer seals* owns the order a maintainer's
run follows.

### What a contribution is asked for

- A branch cut from the open release branch, and a pull request based on it.
- `bin/test tests/<file> -q` on each module the change touched. CI runs the
  rest, on three platforms.
- **A change to a gate carries a higher bar**: a test seen failing before the
  fix, a stated failure direction, a prompt budget, and honesty about the
  platforms the contributor could not test. *What a change to a gate must
  carry* below is the whole of it, and it covers anything under `hooks/` or
  `.github/workflows/`.
- The house rules below. Two of them catch most changes: both READMEs move
  together, and examples use `example.com` and `/Users/x/` rather than any
  real domain, path or handle.

### What a contribution is not asked for

This repository runs a spec-driven workflow on itself: work items under
`seal/threads/`, review rounds, a version that moves once per release. **A
contribution is asked for none of it.** The version and milestone steps
belong to a release and exit early on any base but `main`. The others run on
every pull request, and they pass for a different reason: they ask nothing
of a branch that declared nothing. Those are the review-chain check and the
issue-claim report. The suite reads one fact
about the rule files: a `check:` target the change renamed or removed fails
it, naming the file, the line and the heading, and `bin/seal rules --check`
gives the same answer before the push. Each row below gives its own reason,
and a maintainer adding a CI step reads the row rather than this sentence.

| A contribution does not write | Why no check asks for it |
|---|---|
| a `routing.md`, `frame/design.md` or `frame/plan.md` under `seal/threads/` | Nothing in CI reads them. They route a maintainer's own session |
| a review round record | *a declared review chain has the round record it claimed* passes with a notice when no declaration names the branch |
| a `changelog.md` fragment | No CI step reads it. The release note is built from a maintainer's fragments when the release is tagged |
| a `gaps.md`, or a row inside one | No CI step reads it. It is a maintainer's closing memo for their own work item |
| a new version in `.claude-plugin/plugin.json` | *a change to what ships must move the version* exits 0 unless the base is `main` |
| an issue number in the description | the issue-claim step reports what it finds and never fails; an empty description is a description |

A contributor's machine also has no routing edit gate. It is this plugin's
own hook, installed on a maintainer's machine, and nothing in CI stands in
for it.

## Running the checks

The suite needs `pytest`, one parser, `markdown-it-py`, pinned to one
version in `MARKDOWN_IT` in `.github/scripts/run_tests.py`, and one
renderer, `cmarkgfm`, pinned in `CMARKGFM` beside it.
The parser is the CommonMark oracle the hook readers are checked against.
The renderer is
GitHub's own, cmark-gfm, and the table walker in `hooks/lib/config.py` is checked
against what it renders. The parser and the renderer are test-only: the gates
themselves are stdlib-only Python and
import nothing the suite installs. `bin/test` acquires all three once: it
builds a virtualenv at `.venv` on the first call and reuses it afterwards, so
only the first call pays for an environment. It works from any directory in
the repository or a worktree of it, and it prints the interpreter it used.

```bash
bin/test tests/skills/test_session_cost.py -q   # one module: the form to type
bin/test                                 # everything, in parallel: the orchestrator's broad run
uvx ruff check . && uvx ruff format .    # the linter and formatter CI holds the tree to
```

Both forms run under `-n auto` unless the command line passes its own `-n`,
`-p no:xdist` or `--pdb`, and the runner installs `pytest-xdist` into a
`.venv` that lacks it, and the pinned `markdown-it-py` and `cmarkgfm`
into one that lacks that version. What the whole run costs is a figure with a
date and a machine, recorded in the work item that measured it, not here.

**A contributor names a module.** The full suite is the orchestrator's, run
once after the review rounds settle and before the sealer is spawned, and
contract rule 2 in `skills/agent-contract/SKILL.md` forbids it to every
agent. A cheap runner
does not widen that rule. What it makes cheap is `bin/test tests/<file> -q`,
and that is the form a segment types.

**Python 3.12 is the supported floor**, held as `FLOOR` in `hooks/lib/launch.py`
so this sentence and the code state one number. `bin/seal` runs its script
through that launcher, which refuses an older interpreter with one sentence
before the script is read, and hands each subcommand's script to the
interpreter it held. `bin/test` starts on
whatever `python3` it finds, because its runner is what gets past an old one:
it builds its virtualenv with an interpreter at that floor or newer, refuses a
`.venv` it finds below it, and where it finds neither `uv` nor such an
interpreter it says which to install. What runs before any floor is checked
(a hook, a git hook, the launcher, `bin/test`'s runner, and every module one
of them loads in its own process) runs on whatever `python3` starts it.
`ruff.toml` lints that code at the version its `per-file-target-version`
names, and `tests/hooks/test_launch.py` derives the set, holds every file of it to
that table, and refuses in it the syntax `ast` rejects at that version and the
two constructs ruff pushes toward above it, `zip(..., strict=)` and
`datetime.UTC`. Nothing runs that code at that version, so a standard-library
module or an annotation only a newer `python3` has, as `tomllib` or
`str | None` in a signature, passes both.

The fallback runs the suite without writing a `.venv` into the tree, and it
resolves and installs its environment on every call, close to sixty
seconds each. A contributor using it checks `python3 -V` first, since
nothing here holds the floor for it: macOS ships 3.9 under that name, and a
version manager points it wherever it was last told.

```bash
uvx --with pytest --with markdown-it-py==4.2.0 --with cmarkgfm==2025.10.22 python3 -m pytest tests/ -q
# or: pip install pytest markdown-it-py==4.2.0 cmarkgfm==2025.10.22 && python3 -m pytest tests/
```

CI runs these jobs: lint (`ruff check` and `ruff format --check`); the suite
on ubuntu, macOS and Windows at the floor stated above, macOS and Windows in
shards that `pytest-split` divides from the one committed `.test_durations`,
and ubuntu as one job; `durations`, which unions what the Windows shards
measured; `tests/skills/test_arm_check.py` at 3.13 and 3.14, because `seal arms`'s
node-type tables are only as true as the interpreter that reads them;
`release-report`, which on a pull request into `main` only prints the release
table against the last release tag and fails nothing; and the hygiene
workflow that guards releases. A change to any hook needs a test that fails
without it, as the counterfeit rule below says.

**A slow case is named, and each leg has a budget.** A case whose call runs
longer than `SLOW_CASE_S` in `tests/conftest.py` is named with its seconds in
the run's terminal summary, locally as in CI, and nothing fails for it: a
loaded machine moves a call by four times, so a time reading is a report.
The contributor who sees a case named makes it cheaper, splits it, or samples
what it walks. The report reads a case's call only: time spent building a
fixture in setup is the module's, and the release table's row for each test
file is where that shows. Each `pytest` leg in `test.yml` carries a
`timeout-minutes`, and the comment beside the values says which runs they
were set from.

`.test_durations` goes stale as cases are added, which unbalances the
Windows and macOS shards and drops no case. The file is the Windows leg's,
and it divides the macOS leg too, because every leg collects the same
cases under the same ids: a parametrized path takes `ids=posix_id` from
`tests/conftest.py`, and no id carries the interpreter's path, which
`test_no_collected_id_carries_the_interpreters_path` holds. It prices each
case as Windows ran it, so a case Windows skips is near zero there and its
macOS cost is unseen by the division; a macOS shard that grows past its
`timeout` fails, and the rule beside the values in `test.yml` sets it
again. Every `tests` run measures the file: each Windows shard runs with
`--store-durations --clean-durations` and uploads the part it wrote, and
the `durations` job unions the parts into the `test-durations` artifact,
kept for the days `test.yml` sets, and writes each shard's measured seconds
and their spread to its summary. When to commit it is
`test_the_durations_file_prices_the_suite`'s to say: it fails when more
than one collected case in twenty (`STALE_SHARE`) has no price in the
file, or when more than one second in twenty of the file's belongs to
entries the suite no longer collects.
`bin/test tests -q -k test_the_durations_file_prices_the_suite` runs that
case alone against the whole collection, and naming one module skips it.
The contributor refreshes the file from the artifact of the branch's latest
`tests` run: `gh run download <run id> -n test-durations -D <dir>`, then
moves `<dir>/.test_durations` over the committed file and commits it. Its
line ends are already LF. The download goes to a directory of its own
because `gh` will not write over a file that is already there. Where the
run's artifact has expired, the contributor re-runs it first, with
`gh run rerun <run id>`. A branch
with no pull request has no `tests` run until one is dispatched, and neither
has a branch whose run is too old to re-run:
`gh workflow run test.yml --ref <branch>` starts one.

**The suite runs with `gh` logged out, on a contributor's machine as on
CI.** CI's pytest job has no token, so `tests/conftest.py` makes the same
true locally when it is imported: it points `GH_CONFIG_DIR` at an empty
directory, removes `GITHUB_TOKEN` and `GITHUB_ENTERPRISE_TOKEN`, and sets
`GH_TOKEN` and `GH_ENTERPRISE_TOKEN` to a value no server accepts, because
without a token variable, `gh` reads the login it keeps in the OS keyring. A
case that falls through its stubs onto a live `gh` then fails where it runs,
instead of passing on a machine that happens to be logged in and failing
only on CI after the branch was sealed. A case that needs `gh` stubs it. The
conftest also removes every variable whose name starts with `GITHUB_`, so a
case sees under a pull request's CI run what it sees everywhere else, and a
case that needs one sets it with `monkeypatch.setenv`. One question is
stubbed for every case: `chain_check.py` asks `gh pr view --json isDraft`
where no event payload exists, so the conftest puts a `gh` first on PATH
that finds no pull request, which the check reads as *unknown*, not as
ready, and passes every other call to the `gh` behind it. A case that means
a draft or a ready pull request says so with `gh_answers`.

Two steps of the hygiene workflow ship to user repositories as well, as
`templates/setup/hygiene.yml`: the chain check and the mode check, run from a
clone of this repository at the release the user installed. `seal pr-checks
install` writes it, at first setup or later, so a change to either of them
here reaches a user at their next install, and the template has to keep
telling the same story as the workflow. Every step
passes a pull request that declares nothing, and
`tests/e2e/teammate/test_teammate_flow.py` runs each one to hold that.

The broad runs come once, at the end. The `verify` skill's scope rule applies
to work on this repository too: narrow runs while the work is still being
edited, everything after the review rounds settle, and nothing edited between
that run and the pull request.

## The test layout

**Each shipped module has one test file, and the file names its module
once.** The file is `tests/<area>/test_<stem>.py`. The area is the first
directory of the module's path with a leading dot dropped, so the file for
`hooks/lib/optin.py` is `tests/hooks/test_optin.py` and the file for a
script under `.github/` stands in `tests/github/`; a module under `tests/`
keeps its file at `tests/`. The stem is the module's file
name without `.py`, with each hyphen written as an underscore, and where two
shipped modules share a stem, the parent directory's name goes before it.
The first assignment after the file's imports is
`TARGET = "<tracked path>"`. A file whose cases run a `seal` subcommand names
the script that subcommand runs. The file holds one class per public top-level
function of the module, `Test_<name>`, with the name spelt as the code spells
it, and a class or a private function of the module may have a class too.
Each such class holds a case named `test_accepts_<what>` for good input and
one named `test_refuses_<what>` for bad input. What the module does as a
whole goes in `Test_module`. A flow across modules lives under
`tests/e2e/<flow>/`: its `TARGET` names the command or hook the flow starts
from, and each of its classes is a scenario that keeps the same two cases.
A case whose assertion reads a shipped document names that document as
`TARGET`, and its classes take any name. A helper two test files use is
defined once, in `tests/conftest.py`. Each module file ends with
`test_census = census_case(TARGET)`, which runs every census in
`tests/censuses.py` over its module, and a line a census flags on purpose
carries `# exempt from <census>: <why>` on its own line above it, where the
census reads it and refuses it once it excuses nothing.
`bin/seal layout --check` refuses a file that declares `TARGET` and breaks
this, and lists the files that do not declare one yet. A contributor writing
a case first reads its class and the pairs `bin/seal layout --pairs` names
in it.
check: tests/skills/test_test_layout.py tests/test_censuses.py

**A test file takes the repository root from `tests/conftest.py`.** A test
file imports `ROOT` from `tests/conftest.py` and joins every other path under
it. It does not take a directory from its own `__file__`, because that
directory is right only at the depth the file stands at. No two Python files
under `tests/` share a file name: `tests/conftest.py` puts every directory
under `tests/` that holds a test file on `sys.path`, so two files of one name
import as one module.
check: tests/test_conftest.py

**A test file that declares no `TARGET` stands by what its cases run.** It
stands in `tests/behaviour/` where its cases load or run shipped code, and
in `tests/text/` where they only read text.
check: none reader: the proofer at review

**A module's old cases get one verdict each when the module is rebuilt.**
The contributor rebuilding a module reads its functions first and lists the
classes its file must have. Then each old case that exercises the module is
placed in its class as it stands, merged into a case of the class that
already covers it, cut, or rewritten. A case whose assertion reads a
document's prose stays where it is, and so does a case whose rows pin how
another module reads a shape, until the module it pins is rebuilt. A case is
cut only where the mutation table shows that every mutation it kills is
killed by another case, or where the behaviour it guarded has left the tree.
check: none reader: the proofer at review

**A module's tests are written anew from the code when its old files cost
past the threshold.** The threshold is 60 seconds of the module's old files in
`.test_durations`, or a pair `bin/seal layout --pairs` names inside one of
the module's classes. Every other module's old cases are placed and merged.
A module written anew takes its accepting and refusing cases from reading
the code, one class per function, and its old cases are read for their
inputs.
check: none reader: the proofer at review

**A rewritten module builds its world once and reads a command without
git.** Its fixture repositories are built once, in a module-scoped fixture.
A case that writes into them takes a copy, and the copy is the reset; where
no case writes more than a marker keyed by a session id, each case makes its
own session id, and that is the reset. A case about how a command is read
runs neither real git nor a real shell; the real-git cases that stay are the
ones showing that the reading and git agree. A case samples one input of
each kind where the mutation table shows the sample kills what enumerating
the whole input space killed. These bind the rewrite and nothing in CI: the
seconds the record states are read by the release table, not by a gate.
check: none reader: the proofer at review

**A rebuilt module's record carries its move check or its mutation table,
and one line per removed case.** The contributor writes it into the phase
record of the work item that rebuilt the module, in four parts:

- the move check, `bin/seal layout --moved <base> --from <old file>...
  --to <new file>...`, with its command and its last line. One run covers
  a group, the modules of one shipped directory or a smaller group rebuilt
  together, and names every old file the group's cases came from after
  `--from` and every new file the group wrote after `--to`; an old file
  that keeps cases for a later group stands in both lists. It passes where
  every condition `skills/verify/scripts/test_layout.py`'s docstring
  states for `--moved` holds. Where it exits 0, the group's cases were
  only moved and the record has no mutation table. Where it exits 1, each
  module of the group carries the mutation table, and so does a module
  written anew. A failing case that stands in a file declaring no `TARGET`
  counts for the shipped module whose function it calls as its subject.
  Where it calls no shipped module as its subject, as a check across files
  or a case reading prose does, it counts for every definition of a name
  its line names that the working tree's reading reaches, in each file
  that holds one, less any definition the base's reading also reaches in
  the same file and as written. Those definitions' decision points carry
  the mutants: each branch of a function, each entry of a collection the
  case reads, and, for any other definition, the value it binds, an
  import's module among them; they run against the cases whose lines send
  them there and no others. A module's mutants sit at the decision points
  where a case accepts or refuses, one or two per class and one more for
  each further decision point a function holds, so their count follows
  the module's classes. They run against the new file in one
  `bin/seal mutate` call with `-x` in its tests command. The old files'
  column runs only for a mutant the new file lets survive: where the old
  files miss it too, the table names an old gap, and where they kill it,
  the new file gets a case seen red on that mutant;
- the module's cases and seconds before and after, from
  `bin/test <files> -q` on the machine that built it;
- the real-git cases kept, each named;
- one line per old case cut or rewritten: its name, what it guarded, and the
  case or tree fact that holds it now; and the names of the cases left
  where they stand because they read prose, or because they wait for the
  module they pin, with that module named.

check: none reader: the proofer at review

## What a change to a gate must carry

The gates decide whether someone's commit or branch switch proceeds, so a
change to one is judged by what it does when it is wrong, and a change that
adds any mechanism by what it takes away:

- **A test seen red.** The contributor writes the test against the unfixed
  code and watches it fail before fixing anything. A test that has never
  failed proves nothing (this repository's own `verify` skill calls that a
  counterfeit seal).
- **A stated failure direction.** The pull request says whether the change
  makes the gate block more or allow more, and why that direction is the
  cheaper mistake here. A wrong deny costs a prompt; a wrong allow can break
  another session's tree. A deny that fires on *every* invocation in some
  environment is an outage, not a cost.
- **A prompt budget.** The pull request says how many times the change puts
  a question in front of a person, per session, and what each one costs when
  nobody is at the keyboard. **Verification through an automated workflow is
  this project's first goal**, so an interruption is a price paid against it
  rather than a neutral design choice. A change that adds one says why
  nothing cheaper reaches the same guarantee: a value read from a file, a
  default assumed in writing, a refusal the agent makes on its own. Where a
  question really is the only answer, it belongs in the batch asked before
  the first edit, never at minute thirty.
- **Platform honesty.** Process inspection (`ps`, `lsof`, `/proc`) behaves
  differently across macOS, Linux, and Windows. The contributor names in the
  pull request each platform they could not test, rather than assuming it.
- **What it removes.** A pull request that adds a mechanism (a gate, a
  checker, a hook, a CI step, a rule) names the existing one it removes, or
  says why none can go, and with either answer what that one caught against
  what it costs. `CLAUDE.md` *The rule a mechanism is kept against* is why.
  What goes is listed under its `frame/design.md`'s `## Removes`, which the review
  reads against the diff; `docs/the-reader-registry.md` *A frame names what
  its work removes* is the rule.

The prompt budget and what a change removes are the two a passing suite
cannot report on: nothing counts interruptions, and nothing weighs a
mechanism's catches against its cost. Both are answered in the pull request
body or they are not answered. `skills/implement/SKILL.md` *1. Read the
documents that outrank the code first* holds the reasoning the budget is
drawn against: the cost of a question is not its difficulty, it is when it
arrives.

## House rules

- **A change writes a fragment, never a shared registry.** Which file a
  change writes its changelog entry into is `docs/the-record-layout.md`
  *A change writes fragments, never a shared file*. No branch writes the
  release notes: the tag's workflow builds them from the fragments, as
  `docs/branch-and-release.md` *Work accumulates on a release branch* says.

- **No real identifiers.** Examples, fixtures, and docs use `example.com`
  and `/Users/x/` only. The `real_identifiers` census in `tests/censuses.py`
  enforces it in CI, and a contributor extends its allowlist deliberately,
  never to make a test pass.
  The rule is held this hard because a real domain, path or organisation
  name inlined into an example is the leak that forces a rewrite of the
  repository's history.
- **Every file read or written names its encoding.** An `open`,
  `read_text`, `write_text` or text-mode `subprocess` call with no
  `encoding=` takes the locale's, which is cp1252 on the Windows leg and
  UTF-8 everywhere else, so that leg is the only one that sees it. The call
  names `encoding="utf-8"`. Every hook entry point also opens its `__main__`
  with `console.to_utf8()`. The `encoding` and `entry_point` censuses in
  `tests/censuses.py` enforce the first over every tracked `.py` and the
  second over `hooks/`, and a contributor exempts a line deliberately, never
  to make a test pass. A `python3 -c` line in a skill or a workflow is outside
  their reach, so its writer names the encoding there.
- **Functional files are English-only.** Skills, agents, hooks, and commands
  load into model context, where a translated mirror would drift. Korean
  belongs in human-facing docs (`README.ko.md`). The `writing-style` skill
  is the deliberate exception: its per-language sections are independent
  norms, not mirrors.
- **Both READMEs move together, and so does every document with a `.ko.md`
  edition.** They need not be literal translations, but they must tell the
  same story about what exists. The outline is checked:
  `tests/behaviour/test_both_editions_carry_the_same_folds.py` reads every
  tracked `X.ko.md` beside an `X.md`, wherever it stands, the READMEs among
  them, and requires the same sequence of heading levels.
- **Hooks stay local and quiet.** No writing outside the repo being worked
  on, and failure must never block a tool call. A gate that crashes should
  let the work through, not wedge the session.

  Every hook that reaches the network is named in the README's privacy
  section, because a rule with undisclosed exceptions is not a rule.
  `lint-python` fetches ruff through `uvx` when no local copy exists.
  `version-check` asks the plugin's own repository for its newest release tag.
  A new one needs the same limits `version-check` carries (an opt-in
  condition so unrelated repos are untouched, a throttle so it is not
  per-session, and silence on every failure), plus a line in the README
  saying what leaves the machine. Anything that would send repository
  contents, paths, or prompts is not on the table.
- **Hooks are Python invoked as `python3 <script>`, with `py -3 <script>`
  behind it.** Shebangs and exec bits do not exist on Windows, and `python3`
  is the one name its official installer does not create, so the registered
  command names both, in that order, and the packaging test enforces the
  form. The fallback is safe because `dispatch.py` exits 0 for every decision
  it makes, deny included: `||` is reached only when the first interpreter
  could not start, never as a second run of a gate that already decided.

## Cutting a release

`docs/branch-and-release.md` holds it: where a branch is cut from, **which
merge method each direction takes** (they are not interchangeable), the two
things that carry the version, how the release note is built from the
changelog fragments, and
which issues a release closes. A maintainer reads it before merging anything,
not after.

## Proposing a new gate or skill

A proposal opens an issue first, describing the failure it prevents and what
a false positive would cost. The plugin's value is that its always-on surface
stays small: a new always-loaded rule has to earn its place against
[the context-file study](https://arxiv.org/abs/2602.11988) the README cites.
Skills that load on demand are a much easier case to make than anything
added to the CLAUDE.md block.
