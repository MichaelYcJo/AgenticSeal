# Contributing to SpecSeal

## Opening a pull request

**Base your branch on the open release branch, not on `main`.** GitHub offers
`main` by default, and for everything except a release that default is the
wrong one here. Work collects on one release branch and `main` moves once per
release; `docs/branch-and-release.md` §*Work accumulates on a release branch*
holds the reasoning, and this section is the part a contributor needs.

**How to find it.** Exactly one branch named `release/vX.Y.Z` is open at a
time. On GitHub it is the only entry beginning `release/` in the branch
dropdown on the code page. In a clone:

```bash
git branch -r --list 'origin/release/*'   # the one to base on, and nothing else
```

Set it as the base when you open the pull request — the base is the left-hand
dropdown on the compare page. If one is already open against `main`, the
**Edit** button beside its title changes the base without closing anything.

**Why a wrong base is refused with a message about a version.** A pull request
into `main` is a release here, so the checks that run there are a release's
checks, and one of them asks for `.claude-plugin/plugin.json` to move. A
contribution is not a release and must not touch that file. Change the base
instead, and the refusal goes with it.

**Open the pull request when the work is done, and open it ready.** Every
push to an open pull request runs the suite on Linux, macOS and Windows, and
a branch with no pull request runs nothing. So push your branch as often as
you like, and open the pull request once nothing is left to push.
`skills/code-review/orchestration.md` §*Orchestrator: the pull request opens
once the sealer seals, and a phase is re-run* owns the order a
maintainer's run follows.

### What a contribution is asked for

- A branch cut from the open release branch, and a pull request based on it.
- `bin/test tests/<file> -q` on the module you touched. CI runs the rest, on
  three platforms.
- **A change to a gate carries a higher bar**: a test seen failing before the
  fix, a stated failure direction, a prompt budget, and honesty about the
  platforms you could not test. §*What a change to a gate must carry* below is
  the whole of it, and it covers anything under `hooks/` or
  `.github/workflows/`.
- The house rules below. Two of them catch most changes: both READMEs move
  together, and examples use `example.com` and `/Users/x/` rather than any
  real domain, path or handle.

### What a contribution is not asked for

This repository runs a spec-driven workflow on itself — work items under
`seal/specs/`, review rounds, a version that moves once per release. **A
contribution is asked for none of it.** The version and changelog steps
belong to a release and exit early on any base but `main`. The others run on
every pull request, and they pass for a different reason — they ask nothing
of a branch that declared nothing: the review-chain check, the
unverified-record tally and the issue-claim report. The suite reads one fact
about the rule files: an `Enforced by:` target your change renamed or removed
fails it, naming the file, the line and the heading, and `bin/rules --check`
gives the same answer before you push. Each row below gives its own reason,
and a maintainer adding a CI step should read the row rather than this
sentence.

Established by reading every step of `.github/workflows/hygiene.yml` and
`.github/workflows/test.yml` against a live contribution that carried none of
the following and came back green.

| You do not write | Why no check asks for it |
|---|---|
| a `routing.md`, `spec.md` or `plan.md` under `seal/specs/` | Nothing in CI reads them. They route a maintainer's own session |
| a review round record | *a declared review chain has the round record it claimed* passes with a notice when no declaration names your branch |
| a `changelog.md` fragment | *every changelog fragment reached the released file* exits 0 unless the base is `main` |
| an `overview.md`, or a row inside one | *the unverified record is readable* counts the rows already in the tree, so adding none passes |
| a new version in `.claude-plugin/plugin.json` | *a change to what ships must move the version* exits 0 unless the base is `main` |
| an issue number in the description | the issue-claim step reports what it finds and never fails; an empty description is a description |

You also have no commit gate and no worktree guard. Those are this plugin's
own hooks, installed on a maintainer's machine. Nothing runs them on yours,
and nothing in CI stands in for them.

## Running the checks

The suite needs `pytest`, one parser, `markdown-it-py`, pinned to one
version in `MARKDOWN_IT` in `.github/scripts/run_tests.py`, Pillow, pinned
in `PILLOW` beside it, and one renderer, `cmarkgfm`, pinned in `CMARKGFM`.
The parser is the CommonMark oracle the hook readers are checked against
(#667). Pillow decodes the release seal the tag push draws with
`rsvg-convert` and attaches to the GitHub Release, in the suite's pixel
case (#718, #832). The
renderer is GitHub's own, cmark-gfm, and the table walker in
`hooks/config.py` is checked against what it renders (#647). The parser and
the renderer are test-only and Pillow is test-and-release-only: the gates
themselves are stdlib-only Python and import nothing the suite installs.
`bin/test` acquires all four once: it builds a virtualenv at
`.venv` on the first call and reuses it afterwards, so only the first call
pays for an environment.
It works from any directory in the repository or a worktree of it, and it
prints the interpreter it used.

```bash
bin/test tests/test_session_cost.py -q   # one module — the form to type
bin/test                                 # everything, in parallel — the orchestrator's broad run
uvx ruff check . && uvx ruff format .    # the linter this plugin runs on your code
```

Both forms run under `-n auto` unless you pass your own `-n`, `-p no:xdist`
or `--pdb`, and the runner installs `pytest-xdist` into a `.venv` that lacks
it (#337), and the pinned `markdown-it-py`, Pillow and `cmarkgfm` into one
that lacks that version (#667, #718, #647). What the whole run costs is a
figure with a date and a machine, recorded in the work item that measured
it, not here.

**Name a module.** The full suite is the orchestrator's, run once after the
review rounds settle and before the sealer is spawned —
`skills/agent-contract/SKILL.md` §2 forbids it to every agent. A cheap runner
does not widen that rule. What it makes cheap is `bin/test tests/<file> -q`,
and that is the form a segment types.

**Python 3.12 is the supported floor**, held as `FLOOR` in `hooks/launch.py`
so this sentence and the code state one number. Every `bin/` wrapper but
`bin/test` runs its script through that launcher, which refuses an older
interpreter with one sentence before the script is read. `bin/test` starts on
whatever `python3` it finds, because its runner is what gets past an old one:
it builds its virtualenv with an interpreter at that floor or newer, refuses a
`.venv` it finds below it, and where it finds neither `uv` nor such an
interpreter it says which to install. What runs before any floor is checked
— a hook, a git hook, the launcher, `bin/test`'s runner, and every module one
of them loads in its own process — runs on whatever `python3` starts it.
`ruff.toml` lints that code at the version its `per-file-target-version`
names, and `tests/test_a_script_says_which_interpreter_it_needs.py` derives
the set, holds every file of it to that table, and refuses in it the syntax
`ast` rejects at that version and the two constructs ruff pushes toward above
it, `zip(..., strict=)` and `datetime.UTC`. Nothing runs that code at that
version, so a standard-library module or an annotation only a newer
`python3` has, as `tomllib` or `str | None` in a signature, passes both.

The fallback runs the suite without writing a `.venv` into the tree. It is the
form this section used to name first, and it resolves and installs its
environment on every call — 55–58 seconds each, paid on all seventeen test
calls of one measured segment (#133, #156). Check `python3 -V` before using
it, since nothing here holds the floor for you: macOS ships 3.9 under that
name, and a version manager points it wherever it was last told.

```bash
uvx --with pytest --with markdown-it-py==4.2.0 --with pillow==12.3.0 --with cmarkgfm==2025.10.22 python3 -m pytest tests/ -q
# or: pip install pytest markdown-it-py==4.2.0 pillow==12.3.0 cmarkgfm==2025.10.22 && python3 -m pytest tests/
```

CI runs six jobs: lint (`ruff check` + `ruff format --check`), the suite on
ubuntu, macOS and Windows at the floor stated above (macOS in three shards
and Windows in four, each leg divided by `pytest-split` from the one
committed `.test_durations`, #841, #864; ubuntu as one job), `durations`,
which unions what the Windows shards measured (#931),
`tests/test_arm_check.py` at 3.13 and 3.14 (`arm-check`'s node-type tables
are only as true as the interpreter that reads them, #684), `release-report`,
which on a pull request into `main` only prints the release table against
the last release tag and fails nothing, and the hygiene workflow that guards
releases. A
change to any hook needs a test that fails without it — see the counterfeit
rule below.

**A case has a budget, and so does each leg.** A case whose call runs longer
than `CASE_CEILING_S` in `tests/conftest.py` (90 s) fails with one line
naming it and its seconds, locally as in CI. Make it cheaper, split it, or
sample what it walks. On a machine running other suites at the same time, a
case can pass that ceiling on load alone; `SPECSEAL_CASE_CEILING_S=<seconds>`
raises it for one run, and CI never sets it. The ceiling reads a case's call
only: time spent building a fixture in setup is not held to it. Each
`pytest` leg in `test.yml` carries a `timeout-minutes`, and the comment
beside the values says which runs they were set from.

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
the `durations` job unions the four parts into the `test-durations`
artifact, kept seven days, and writes each shard's measured seconds and
their spread to its summary. When to commit it is
`test_the_durations_file_prices_the_suite`'s to say: it fails when more
than one collected case in twenty (`STALE_SHARE`) has no price in the
file, or when more than one second in twenty of the file's belongs to
entries the suite no longer collects.
`bin/test tests -q -k test_the_durations_file_prices_the_suite` runs that
case alone against the whole collection, and naming one module skips it.
To refresh the file, take the artifact from your branch's latest `tests`
run: `gh run download <run id> -n test-durations -D <dir>`, then move
`<dir>/.test_durations` over the committed file and commit it. Its line ends
are already LF. The download goes to a directory of its own because `gh`
will not write over a file that is already there. A run older than
seven days is re-run first, with `gh run rerun <run id>`. A branch with no
pull request has no `tests` run until one is dispatched, and neither has a
branch whose run is too old to re-run:
`gh workflow run test.yml --ref <branch>` starts one.

**The suite runs with `gh` logged out, on your machine as on CI.** CI's
pytest job has no token, so `tests/conftest.py` makes the same true locally
when it is imported: it points `GH_CONFIG_DIR` at an empty directory,
removes `GITHUB_TOKEN` and `GITHUB_ENTERPRISE_TOKEN`, and sets `GH_TOKEN` and
`GH_ENTERPRISE_TOKEN` to a value no server accepts — because without a token
variable, `gh` reads the login it keeps in your OS keyring. A case that falls
through its stubs onto a live `gh` then fails where you run it, instead of
passing because you happen to be logged in and failing only on CI after the
branch was sealed (#510). A case that needs `gh` stubs it. One question is
stubbed for every case: `chain_check.py` asks `gh pr view --json isDraft`
where no event payload exists (#866), so the conftest puts a `gh` first on
PATH that finds no pull request — which the check reads as *unknown*, not as
ready — and passes every other call to the `gh` behind it. A case that means
a draft or a ready pull request says so with `gh_answers`.

Two steps of the hygiene workflow ship to user repositories as well, as
`templates/hygiene.yml`: the unverified-rows tally and the chain check, run
from a clone of this repository at the release the user installed. The
`implement` skill writes it at a shared-mode first setup, so a change to
either step here reaches a user at their next first setup, and the template
has to keep telling the same story as the workflow.

Run the broad ones once, at the end. The `verify` skill's Scope rule applies
to work on this repo too: narrow runs while you are still editing, everything
after the review rounds settle, and nothing edited between that run and the PR.

## What a change to a gate must carry

The gates decide whether someone's commit or branch switch proceeds, so a
change to one is judged by what it does when it is wrong, and a change that
adds any mechanism by what it takes away:

- **A test seen red.** Write the test against the unfixed code and watch it
  fail before you fix anything. A test that has never failed proves nothing
  (this repo's own `verify` skill calls that a counterfeit seal).
- **A stated failure direction.** Say whether the change makes the gate
  block more or allow more, and why that direction is the cheaper mistake
  here. A wrong deny costs a prompt; a wrong allow can break another
  session's tree — but a deny that fires on *every* invocation in some
  environment is an outage, not a cost.
- **A prompt budget.** Say how many times the change puts a question in
  front of a person, per session, and what each one costs when nobody is at
  the keyboard. **Verification through an automated workflow is this
  project's first goal**, so an interruption is a price paid against it
  rather than a neutral design choice. A change that adds one says why
  nothing cheaper reaches the same guarantee — a value read from a file, a
  default assumed in writing, a refusal the agent makes on its own. Where a
  question really is the only answer, it belongs in the batch asked before
  the first edit, never at minute thirty.
- **Platform honesty.** Process inspection (`ps`, `lsof`, `/proc`) behaves
  differently across macOS, Linux, and Windows. If you cannot test a
  platform, say so in the PR rather than assuming.
- **What it removes.** A pull request that adds a mechanism — a gate, a
  checker, a hook, a CI step, a rule — names the existing one it removes, or
  says why none can go, and with either answer what that one caught against
  what it costs. `CLAUDE.md` §*The rule a mechanism is kept against* is why.
  What goes is listed under its `spec.md`'s `## Removes`, which the review
  reads against the diff; `docs/the-reader-registry.md` §*A frame names what
  its work removes* is the rule.

The prompt budget and what a change removes are the two a passing suite
cannot report on: nothing counts interruptions, and nothing weighs a
mechanism's catches against its cost. Both are answered in the pull request
body or they are not answered. `skills/implement/SKILL.md` §1 holds the reasoning the
budget is drawn against: the cost of a question is not its difficulty, it is
when it arrives.

## House rules

- **A change writes a fragment, never a shared registry.** Which file a
  change writes its changelog entry into is `docs/the-record-layout.md`
  §*A change writes fragments, never a shared file*. Three branches
  running in parallel once shared exactly one file between them, and it was
  the changelog: the conflict was three lines, and it arrived after the broad
  gate had run, where nothing may be edited.

  **One branch does write the changelog, and it is the one based on `main`.**
  A pull request into `main` is a release, so the entries are due there and
  the hygiene workflow fails it while a fragment is still ungathered. The
  gather writes the release's own file, `changelog/X.Y.Z.md`, and its heading
  in the index `CHANGELOG.md`, and no other branch writes either. The gather
  is the command in `docs/release-checklist.md` §*2. Gather, bump*. This is
  the rule above being satisfied rather than broken: the branch is not adding
  an entry to a shared region, it is collecting the fragments that already
  exist. A hotfix taken straight to `main` is the case that meets this without
  expecting to.

- **No real identifiers.** Examples, fixtures, and docs use `example.com`
  and `/Users/x/` only. `tests/test_no_real_identifiers.py` enforces it in
  CI — extend its allowlist deliberately, never to make a test pass. The rule
  is held this hard because both incidents that forced a rewrite of this
  repository's history entered exactly this way, as a real domain, path or
  organisation name inlined into an example.
- **Every file read or written names its encoding.** An `open`,
  `read_text`, `write_text` or text-mode `subprocess` call with no
  `encoding=` takes the locale's, which is cp1252 on the Windows leg and
  UTF-8 everywhere else, so that leg is the only one that sees it. Name
  `encoding="utf-8"`. Every hook entry point also opens its `__main__` with
  `console.to_utf8()`.
  `tests/test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`
  enforces the first over every tracked `.py` and the second over `hooks/`
  — classify a unit in its `ALLOWED` deliberately, never to make a test
  pass. A `python3 -c` line in a skill or a workflow is outside its reach,
  so name the encoding there yourself.
- **Functional files are English-only.** Skills, agents, hooks, and commands
  load into model context, where a translated mirror would drift. Korean
  belongs in human-facing docs (`README.ko.md`). The `writing-style` skill
  is the deliberate exception: its per-language sections are independent
  norms, not mirrors.
- **Both READMEs move together, and so does every document with a `.ko.md`
  edition.** They need not be literal translations, but they must tell the
  same story about what exists. Under `docs/` the outline is checked:
  `tests/test_both_editions_carry_the_same_folds.py` reads every top-level
  `docs/X.ko.md` beside a `docs/X.md` and requires the same sequence of
  heading levels and, under each heading position, the same fold markers. A
  fold into one edition is a fold into both.
- **Hooks stay local and quiet.** No writing outside the repo being worked
  on, and failure must never block a tool call. A gate that crashes should
  let the work through, not wedge the session.

  Two hooks reach the network, and both are named in the README's privacy
  section because a rule with undisclosed exceptions is not a rule.
  `lint-python` fetches ruff through `uvx` when no local copy exists.
  `version-check` asks the plugin's own repository for its newest release tag.
  A third needs the same three limits the second carries — an opt-in condition
  so unrelated repos are untouched, a throttle so it is not per-session, and
  silence on every failure — plus a line in the README saying what leaves the
  machine. Anything that would send repository contents, paths, or prompts is
  not on the table.
- **Hooks are Python invoked as `python3 <script>`, with `py -3 <script>`
  behind it.** Shebangs and exec bits do not exist on Windows, and `python3`
  is the one name its official installer does not create — so the registered
  command names both, in that order, and the packaging test enforces the
  form. The fallback is safe because `dispatch.py` exits 0 for every decision
  it makes, deny included: `||` is reached only when the first interpreter
  could not start, never as a second run of a gate that already decided.

## Cutting a release

`docs/branch-and-release.md` holds it: where a branch is cut from, **which
merge method each direction takes** — they are not interchangeable — the two
things that carry the version, how the changelog fragments are gathered, and
which issues a release closes. Read it before merging anything, not after.

## Proposing a new gate or skill

Open an issue first describing the failure it prevents and what a false
positive would cost. The plugin's value is that its always-on surface stays
small — a new always-loaded rule has to earn its place against
[the context-file study](https://arxiv.org/abs/2602.11988) the README cites.
Skills that load on demand are a much easier case to make than anything
added to the CLAUDE.md block.
