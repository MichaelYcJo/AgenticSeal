# Feature Specification: where the records live and whether CI checks pull requests are two answers (#952)

Issue #952, milestone `release: 0.22.4`. Today the bootstrap's mode question
makes one answer of two decisions: **shared** commits `<repo>/seal/` and also
installs `.github/workflows/hygiene.yml`, so a person who wants the records in
the repository gets a workflow that judges every teammate's pull request, and
`seal mode` carries that workflow in and out on every switch. Under it, a step
of that workflow fails a pull request that declares nothing. This work splits
the answer in two, moves the workflow to a command of its own, and makes every
step of `templates/hygiene.yml` pass a pull request that declares nothing.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | The default answer, shared with the records only, installs nothing that can stop a teammate who does not use the plugin. A check that gates a person who declared nothing is the expensive design this goal argues against |
| `CLAUDE.md` *The rule a mechanism is kept against* | A fact has one source, and nothing is kept beside the tree to stay in step with it. Whether the checks are installed is a fact the tree already holds: the file `.github/workflows/hygiene.yml` carrying the plugin's clone line. So no config row and no new `Mode` value records it (`questions.md` Q1) |
| `CLAUDE.md` *Repo rule: text an agent or a check reads has one reading*, and `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* | The three option labels and the command's two action words are spelled once, here, and argparse's `choices` refuse any other spelling of the action. The command's name is `pr-checks`, not a word one letter from `seal mode --check` |
| `skills/implement/SKILL.md` *1. Read the spec before the code* | A ticket ranks below policy. The issue's sentence *The answer is recorded where the mode row is* asks for a second record of a fact the tree holds, so it is a row of `questions.md` with the policy's answer as its default, not an instruction built as written |
| `docs/one-root-by-lifetime.md` *What first setup asks* and *Shared or local*, with the Korean edition's *처음 설정에서 무엇을 묻는가* and *shared 인가 local 인가* | The rules this work changes: two options become three, the shared option stops installing the workflow, `seal mode` stops carrying it, and the paragraph saying a workflow left in local mode is red forever stops being true. Changed through `## Rule changes` below |
| `docs/branch-and-release.md` *Work accumulates on a release branch* | Its bullet on a deleted feature branch says the `implement` skill writes the shipped workflow at a shared-mode first setup. `seal pr-checks install` writes it now |
| `docs/the-record-layout.md` *The fold, and what tells it from a deletion* | A `seal/` root with no work item under it already reads as settled, and only the root's own `specs` path is settled, which keeps a misspelt path from passing. This work keeps that and adds two states beside it |
| `docs/the-record-layout.md` *The unverified record, and the baseline it is read against* | The home of the new rule for `unverified-check` |
| `skills/settle/SKILL.md` *Rule changes*, *A rule has one shape* and *The index* | The grammar of `## Rule changes`. Each `file:` comes from `docs/README.md`, the policy root being `docs` (`seal/config.md` has no `Policy root` row). A rule whose test drives a script that fails a pull-request job names a marker on its `check:` line, so the `unverified-check` rule names `nothing-declared-nothing-owed` |
| `CONTRIBUTING.md` *The test layout* | A flow across modules lives under `tests/e2e/<flow>/`, and a case whose assertion reads a shipped document names that document as `TARGET`. The case of item 4 reads `templates/hygiene.yml` and drives three modules, so it is a flow whose `TARGET` is that template |
| `docs/the-record-layout.md` *A commit after the build brings its changelog fragment along* | The build's last phase writes `changelog.md`. This work changes what a consuming repository receives, so a fragment is owed (*Data & interfaces*, last table) |

## Scope

### What the tree says today, against the issue

The issue was written on 2026-10-16 against 0.22.2. Read at `02ee12de`:

1. **The empty root already passes.** `unverified_check.py#settled_root`
   (added by `edd022ad` for #525) reads `seal/specs/` as settled where the
   `seal/` root exists and `specs/` is empty or absent, and `main` exits 0
   saying so. Executed on a scratch repository: a teammate's pull request
   against a base holding only `seal/config.md` passes all three steps. The
   issue's *fresh install, or one settle emptied* case is fixed.
2. **Two shapes still fail** (executed, same scratch run, every step of
   `templates/hygiene.yml` but the clone, with `--baseline main` and
   `GITHUB_HEAD_REF` set):
   - a base whose `seal/specs/` holds a work item with no `overview.md`,
     which is every work item that never opened a closing memo:
     `unverified_check.py` exits 2, `no overview.md found under seal/specs/
     - nothing was checked`;
   - a base with no `seal/` root at all, which after this work is a
     local-mode repository that kept its workflow: `unverified_check.py`
     exits 2, `no such path: seal/specs/ - and nothing under it at main
     either`.

   `chain_check.py` exits 0 in all three shapes (*declared neither way*), and
   `seal mode --check` exits 0 in all three.
3. **The routing check moved out of git (#1027, `61a8455a`).** Nothing in the
   bootstrap or in `seal mode` installs git hooks, and the pull request's
   trailer arm lives in `chain_check.py`, which `templates/hygiene.yml` runs.
   Under the records-only answer no workflow runs, so the trailer arm does not
   run either. That is the answer's meaning, not a gap: it is the person's
   choice not to check pull requests.

### In

1. **The bootstrap's mode question takes three options, in this order, the
   first the default.** It stays one question inside the one
   `AskUserQuestion` the bootstrap already makes, beside the `Broad gate`
   question. The labels, exactly:
   - `shared, records only` creates `<repo>/seal/`, which the routing commit
     carries, and writes nothing under `.github/`.
   - `shared, with pull-request checks` does the same, then runs
     `seal pr-checks install`.
   - `local` creates `$(git rev-parse --git-common-dir)/seal/` and touches
     nothing in the tree, as today.

   The orchestrator records the answer as it does today, by running
   `seal mode` with no argument, which writes the `Mode` row from where the
   folder is. Under the second answer it then runs `seal pr-checks install`.
   The orchestrator no longer writes the workflow by hand, and the version
   one-liner leaves the bootstrap: `seal.py#plugin_version` already reads the
   version from beside the script.
2. **Where the answer is recorded.** The mode is the folder, and the `Mode`
   row says it, as today; its values stay `local` and `shared`. Whether the
   checks are installed is the file `.github/workflows/hygiene.yml` carrying
   the plugin's clone line, `seal.py#PLUGIN_CLONE`, which is how
   `remove_workflow` already tells this plugin's file from somebody else's.
   No row is added (`questions.md` Q1). `seal pr-checks` with no argument is
   the one reader that reports it.
3. **`seal pr-checks`, a subcommand of `skills/implement/scripts/seal.py`
   beside `seal mode`.** Three forms:
   - `seal pr-checks` reports one of three states: installed, naming the
     release the file pins; not installed; or a file at that path this plugin
     did not write. It writes nothing and exits 0.
   - `seal pr-checks install` writes the file from `templates/hygiene.yml`
     with `v<version>` replaced by the installed release, and stages it. It
     refuses, exit 1 and nothing written, where `<repo>/seal/` is not a
     directory, saying that the checks read committed records and that
     `seal mode shared` puts them in the tree; where a file this plugin did
     not write is at the path; where the version cannot be read; and where
     the template carries no placeholder. Where the plugin's own file is
     already there it reports the pin and exits 0. A file written that git
     would not stage is exit 1 with the existing `git add -f` sentence.
   - `seal pr-checks remove` takes out a file this plugin wrote: `git rm`
     where git tracks it, a plain delete where it is untracked and byte for
     byte what `install` would write now. A file staged and not yet
     committed, as `install` leaves it, is the untracked case for git, which
     keeps no committed copy of it: where the index and the working file are
     both byte for byte what `install` would write now, the removal is forced
     past git's staged-changes refusal and staged, so `install` then `remove`
     before a commit leaves nothing under `.github/` (the sealer, at
     `55aea15d`). It refuses, exit 1 and nothing removed, for a symbolic
     link, a file it cannot read, a file without the clone line, an untracked
     file that differs, and a staged file whose index or working copy
     differs. Where nothing is there
     it says so and exits 0. It needs no root, because a workflow that
     outlived its root is the case it exists for.

   Any other action word is argparse's usage error, exit 2. The README and
   its Korean edition each name the command once, in their *Shared or local*
   section.
4. **`seal mode local` and `seal mode shared` stop carrying the workflow.**
   `switch` no longer calls `install_workflow` or `remove_workflow`, and
   `refusals` no longer guards the workflow's path, because the switch no
   longer stages it. Every printed and documented
   `git reset -- :/seal :/.github/workflows/hygiene.yml` becomes
   `git reset -- :/seal`. After a switch to local, where the plugin's file
   is in the tree, the switch prints one line, chosen by the file's pin
   against the installed release (round 1, finding 2). Pinned to the
   installed release, the line says the checks stay, they examine nothing in
   local mode, and `seal pr-checks remove` takes them out. Pinned to another
   release, or where either version cannot be read, the line names the pin,
   says a release before this one fails every pull request with no `seal/`
   in the tree, and names the two ways out: move its `--branch` line to the
   installed release, or run `seal pr-checks remove`. The mode gate's
   *Local* option and the changelog fragment say the same of a workflow
   left after a switch to local. The two READMEs do not restate it: each
   says in one sentence that a workflow left after a move to local stays,
   and links to `docs/one-root-by-lifetime.md` *Shared or local* (the
   Korean README to its Korean edition), which holds the rule once the
   settle applies this spec (round 2, finding 1). After a
   switch to shared, where no such file is there, it prints one line naming
   `seal pr-checks install`.
5. **The mode gate's three options stop promising the workflow.**
   `hooks/mode-gate.py#question_reason` keeps *Keep it where it is*,
   *Shared* and *Local*. *Shared* no longer says the checks are installed and
   names `seal pr-checks install` instead; *Local* no longer says the
   workflow file is removed and says that one already in the tree stays.
6. **A pull request that declares nothing owes nothing, in every step of
   `templates/hygiene.yml`.** `unverified_check.py`, handed a path whose last
   two parts are `seal` and `specs`, exits 0 and prints why in two more
   states:
   - the `seal/` directory is not there: no root is in the tree, so nothing
     is declared and nothing is compared against the base. This comes before
     the base is resolved, so the pull request that moves a root to local
     mode is not read as deleting its records;
   - `specs/` holds work-item directories and none carries an `overview.md`,
     and the base comparison found nothing deleted and nothing settled: no
     row exists to read.

   Every other path holding no `overview.md` stays exit 2, as does every
   path that is missing and not spelled `seal/specs`. `seal mode --check`
   already exits 0 for such a pull request and is not changed.

   Before round 1's fix pass, `chain_check.py` exited 0 for a teammate's
   pull request and refused the pull request that moves a root to local
   mode with the checks kept: that pull request deletes every `routing.md`,
   and the check judged each deleted declaration, accepting one a settle
   retired and refusing the rest (round 1, finding 1). Where the
   tree the check reads has no top-level `seal` entry, `chain_check.py#main`
   reads nothing as declared and judges the trailers as for any pull request
   that declares nothing. The tree the check reads is HEAD, and the working
   tree under `--worktree`, the same tree it reads the declarations from
   (round 2, finding 2). Where git cannot answer whether HEAD has the entry,
   the declarations stay judged. An entry that is not a directory is still
   an entry, so the declarations are judged there; `unverified_check.py`'s
   no-root state asks for a directory, and the two are not described as one
   reading (round 2, finding 3). The test has five answers: under each of the
   two readings, the entry gone and the entry there, and under CI's reading
   git not answering. Each answer has a case of its own, which a mutant
   dropping that answer turns red (scenario S9; round 3, finding 2).
7. **One case runs every step of `templates/hygiene.yml` against a pull
   request that touches nothing under `seal/`.** It lives at
   `tests/e2e/teammate/test_teammate_flow.py`, `TARGET =
   "templates/hygiene.yml"`. It reads the template's steps with
   `tests/conftest.py#workflow_steps`, runs each `run:` block under `bash`
   with its text unchanged apart from GitHub's expression
   `${{ github.base_ref }}`, and requires exit 0 from each. The one step not
   run is the plugin's clone, found as the one step whose block holds
   `git clone`; the case asserts exactly one such step, so a second step
   that cannot run offline fails the case rather than being skipped.
   `$RUNNER_TEMP/specseal` resolves to the tree under test, the base is
   reachable as `origin/<base>`, `GITHUB_HEAD_REF` names the teammate's
   branch, and `GITHUB_EVENT_PATH` names a payload whose pull request is not
   a draft, so `chain_check.py` judges it as ready. It is one case
   parametrized over four bases: no `seal/` root; a root holding only
   `config.md`; a root whose `specs/` holds a work item with `routing.md`
   and `spec.md` and no `overview.md`; and a root whose work item carries an
   `overview.md` with an open `## Not verified` row and a round record.
   A second case runs the same steps on the pull request that moves the
   root to local mode: the fourth base with the plugin's workflow committed,
   and a head commit that ran `seal mode local` (round 1, finding 1). It is
   seen red at the phase 2 commit on the chain step before it passes.
8. **Every place that says what shared mode installs, or that `seal mode`
   carries the workflow, says the new rule.** The table under *Places*
   below lists each, found by search, with what this work does to it.

### Places

Found by `git grep -n -i` for `hygiene`, `pull-request checks`, `seal mode`
and `workflows/hygiene` over the tree at `02ee12de`, `CHANGELOG.md` and
`changelog/` left out as released history (executed). Coordinates are lines at
`02ee12de`.

| Coordinate | What it says now | What this work does |
|---|---|---|
| `skills/implement/orchestration.md` *Orchestrator: Bootstrap*, step 1 (lines 102 to 141) | two options; shared installs the workflow, written by the orchestrator with a version one-liner; `seal mode` carries the workflow | phase 2: three options as *In* item 1; the orchestrator runs `seal pr-checks install` under the second; the one-liner and the hand write leave; the *not a door that shuts* paragraph names `seal mode` for the root and `seal pr-checks` for the checks |
| `skills/implement/scripts/seal.py` docstring (lines 4 to 33), the `WORKFLOW` comment (1350 to 1357), `remove_workflow` docstring (1869 to 1881), `refusals` (2094 to 2163), `switch` (2181 to 2333), `mode`'s no-root comment (2354 to 2359), the parser (2514 to 2564) | `seal mode` carries the workflow; a workflow left in local mode is red forever | phase 2: *In* items 3 and 4; the two comments that say red forever are rewritten to what phase 1 makes true |
| `bin/seal` (lines 11 and 12) | lists `seal mode` forms | phase 2: adds `seal pr-checks` forms |
| `hooks/mode-gate.py#question_reason` (lines 224 to 251) | *Shared* installs the checks, *Local* removes the workflow | phase 2: *In* item 5 |
| `templates/hygiene.yml` header (lines 5 to 29) | the `implement` skill writes the file at first setup in shared mode; a copy in local mode is red forever; `seal mode shared` writes it | phase 2: `seal pr-checks install` writes it; it refuses in local mode; a copy left after a switch to local examines nothing and passes; `seal pr-checks remove` takes it out |
| `templates/seal-README.md` and this repository's `seal/README.md` (lines 20 to 30 of each) | `seal mode` moves the workflow in and out; local mode gives up CI | phase 2: the switch moves the root only; the checks are `seal pr-checks` |
| `skills/config/SKILL.md` steps 2 to 4 (lines 54 to 59, 142 to 149) and *Before switching to shared* (lines 155 to 157) | `seal mode` carries the workflow; the `git reset` names the workflow path | phase 2: step 2 also runs `seal pr-checks` and reports it; the mode bullet and step 4 drop the workflow; the reset loses the workflow path |
| `README.md` *Shared or local* (lines 422 to 505) and `README.ko.md` *shared 인가 local 인가* (lines 416 to 495) | one question about where `seal/` lives; shared installs the checks; the command carries the workflow; the by-hand paragraph about the workflow file | phase 2: the three answers; `seal pr-checks` named once in each; the reset loses the workflow path; the by-hand paragraph says the move leaves `.github/` alone, as `seal mode` now does |
| `CONTRIBUTING.md` (lines 213 to 218) | two steps ship as `templates/hygiene.yml`, written by the `implement` skill at a shared-mode first setup | phase 2: three steps ship (the unverified tally, the chain check, the mode check), written by `seal pr-checks install` |
| `skills/verify/scripts/unverified_check.py` docstring (lines 55 to 60), `main` (lines 1518 to 1527 and 1709 to 1718) | exit 2 for a scan with no overview except a settled root | phase 1: *In* item 6 |
| `docs/one-root-by-lifetime.md` and `.ko.md`, `docs/branch-and-release.md`, `docs/the-record-layout.md` | the rules above | `## Rule changes` below; the build does not edit `docs/` |
| `templates/claude-md-block.md` | sends a session with no root to the Bootstrap; *where the root lands is the user's decision* | kept: it names no option and nothing installed |
| `templates/config.md` *Mode* (lines 172 to 190) | `seal mode --check` is what the pull-request checks run | kept: still true wherever the checks are installed |
| `hooks/config.py` (lines 11, 225, 299, 573, 580) and `hooks/routing.py` (lines 19, 102) | the `Mode` row and `seal mode` | kept: nothing about the workflow |
| `skills/code-review/scripts/chain_check.py` (lines 2015 to 2021) | in local mode, *`seal mode shared` moves the root into the tree and gets the check running* | kept: printed by a workflow already installed, where moving the root in is what the check lacks |
| `skills/commit-pr-convention/SKILL.md` (lines 78 to 82) | the `Mode` row and `seal mode --apply` | kept |
| `skills/settle/SKILL.md` line 34 and `skills/settle/scripts/settle.py` lines 36 and 679 | `seal mode shared` moves the root into the tree | kept: about the root only; #955 rewrites settle in local mode |
| `skills/code-review/orchestration.md:168`, `skills/verify/orchestration.md:62`, `docs/release-checklist.md`, `docs/issues-and-milestones.md`, `docs/the-review-record.md:66`, `.github/` | this repository's own `hygiene` workflow | kept: the issue leaves this repository's workflow alone |
| the unsettled specs under `seal/specs/` | none states in its `## Rule changes` that shared mode installs the workflow or that `seal mode` carries it (executed: an `awk` over each `spec.md`'s *Rule changes* for `hygiene`, `seal mode`, `pull-request checks`, `shared mode` and `first setup`). `1792619408-an-automation-run-stops-at-the-parity-arm` names a `hygiene.yml` pinned to an older release, still true | kept; a released work item's records are history and are not rewritten |
| `tests/test_first_setup_asks_once.py#test_the_record_no_longer_says_the_checks_would_refuse` (lines 659 to 666) | asserts that `docs/one-root-by-lifetime.md` and its Korean edition carry `examined nothing` and `red forever`, the sentences this spec's `## Rule changes` retire | the fix pass of round 1 removes those two asserts and the comment above them, and keeps the first assert (round 1, finding 3; contract rule 19) |
| `skills/code-review/scripts/chain_check.py#main` (lines 2162 to 2170 and 2220 to 2231 at `3f2f5a5d`) | every deleted `routing.md` is a declaration, and one HEAD does not carry is refused unless a settle retired it | the fix passes of rounds 1 and 2: where the tree the check reads has no top-level `seal` entry, nothing is declared (*In* item 6) |
| `tests/test_chain_check.py` `Test_retired` (lines 3359 to 3450 at `2f41bbf9`) | cases for four of the no-root test's five answers; none for the working tree without the entry under `--worktree`, so a mutant that never gives that answer passes every case (round 3, finding 2, executed by the round) | phase 3: the case for that answer, seen red against the mutant first (S9) |
| `tests/test_first_setup_asks_once.py` (lines 71 to 91, 409 to 480, 495 to 510), `tests/test_seal.py` (`Test_install_workflow`, `Test_remove_workflow`, `Test_refusals`, `Test_switch`, `Test_mode`, `Test_main`), `tests/test_mode_gate.py`, `tests/test_unverified_check.py` | pin the two options, the workflow carry, the header's red-forever wording and the exit 2 | phases 1 and 2 rewrite the pins to the new text, each seen red first (contract rule 15) |

### Out

- SpecSeal's own `.github/workflows/hygiene.yml`. The issue leaves it
  untouched; it is this repository's.
- Any change to `seal mode --check`, and any change to `chain_check.py` but
  the one of *In* item 6. Both already exit 0 for a teammate's pull request
  (executed). The mode check
  judges the state of the repository rather than the pull request, and a
  disagreement reaches a base only through a pull request merged red, so it
  does not gate a teammate whose base is sound.
- Moving the pin of a workflow already installed. A consuming repository
  keeps the release its file names until a person edits the `--branch`
  line, or runs `seal pr-checks remove`, then `seal pr-checks install`, and
  commits. The changelog fragment says so.
- A `seal/` that is a symbolic link to a directory outside the tree. Git
  commits the link and not the records behind it, so the checks
  `seal pr-checks install` writes there read nothing. The first setup never
  makes that layout, so it is a limit and not a refusal: the build adds no
  guard for it.
- A check or a case at the pull request that applies a spec's
  `## Rule changes` and runs the documents' own cases over the result. Three
  rounds of this run found that class by hand, and a check would find it in
  every later work item. It is a new gate over every unsettled spec, so it
  would go red today on the three specs the merge-order replay already
  refuses for reasons outside this branch (round 2, `## Not judged`), and it
  owes the argument `CONTRIBUTING.md` *What a change to a gate must carry*
  asks for. This work carries the class as S8's applied half, run as a
  probe; whether the class earns a gate is `questions.md` Q4.
- A workflow pinned to a release newer than the installed one. The line
  `seal mode local` prints names the pin and advises moving the `--branch`
  line to the installed release (`seal.py#left_workflow_line`). Followed,
  that advice leaves a workflow that passes, because the installed release
  runs this line and so has the no-root state. The shape needs a person
  whose plugin is older than the one that wrote the workflow, which the
  one-issue flow does not produce, so it is a limit and the build adds no
  version comparison (rounds 2 and 3, `## Not judged`).
- Under `--worktree`, a top level the check cannot search. `os.path.lexists`
  answers False on any `OSError`, so the no-root test then reads nothing as
  declared, where CI's `git()` answering None keeps the declarations judged.
  Where the top level cannot be searched, the check can read nothing else
  there either (round 3, confirmations, read by the round).
- A `seal/` directory left empty, or holding only an ignored file, after a
  committed switch to local mode. Under `--worktree` it is an entry and the
  declarations are judged, while CI reads nothing declared, so the local run
  is the stricter of the two. `seal mode local` moves the root with one
  rename and leaves no such directory (round 3, confirmations, executed by
  the round).
- #955, settle in local mode, and #1030, settle applying every released
  spec. Shared coordinates, which whoever lands second rebases onto:
  `docs/one-root-by-lifetime.md` *Shared or local* (#955 may change its
  local-mode rows), `docs/the-record-layout.md` (#1030 rewrites *The fold,
  and what tells it from a deletion*; this work adds to the next section),
  and `skills/verify/scripts/unverified_check.py`, whose `settled` predicate
  #1030 may change while this work changes `main` and the paths beside
  `settled_root`.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 A teammate's pull request passes every step | Given a consuming repository whose `templates/hygiene.yml` copy is installed, on each of the four bases of *In* item 7, when a pull request changing only `README.md` runs every step but the clone, then each step exits 0 | `tests/e2e/teammate/test_teammate_flow.py`, marker `nothing-declared-nothing-owed`; seen red at `02ee12de` on the base with a work item and no overview and on the base with no root |
| S2 Records only installs nothing | Given a repository with no root, when the bootstrap's first answer is chosen, then `<repo>/seal/` exists with a `Mode` row reading `shared` and nothing under `.github/` was written | read by the warden in `skills/implement/orchestration.md`; the sentence pinned in `tests/test_first_setup_asks_once.py` |
| S3 The checks are their own command | Given `<repo>/seal/`, when `seal pr-checks install` runs, then the workflow is written pinned to the installed release and staged; run again, it reports the pin and exits 0; with only a local root, it exits 1 and writes nothing; `seal pr-checks remove` then removes the file it wrote and leaves somebody else's | `tests/test_seal.py`, a `Test_pr_checks` class with its accepting and refusing cases |
| S4 Switching leaves `.github/` alone | Given a shared root and the plugin's workflow committed, when `seal mode local` runs, then the workflow is still in the tree, `git status` shows no change under `.github/`, and the output names `seal pr-checks remove`; going back with `seal mode shared` leaves `.github/` as it was | `tests/test_seal.py` `Test_switch` |
| S5 An upgraded shared repository keeps its workflow and is not asked | Given a shared repository bootstrapped before this change, with a `Mode` row and the plugin's workflow pinned to an older release, when a session of this release starts there, then nothing under `.github/` changes, the mode gate stays silent, and `seal pr-checks` reports the old pin | the mode gate's silence on a declared row is `tests/test_mode_gate.py`; the report is `Test_pr_checks`; that no shipped code writes the workflow outside `seal pr-checks install` is read by the warden (`git grep install_workflow`) |
| S6 The unverified check reads two more states as nothing owed | Given `seal/specs/` with work items and no `overview.md`, or no `seal/` at all, when `unverified-check --baseline <ref> seal/specs/` runs, then it exits 0 naming the state; given another path holding no overview, or a misspelt path, it still exits 2 | `tests/test_unverified_check.py`, marker `nothing-declared-nothing-owed` |
| S7 The mode gate stops promising the workflow | Given a root with no `Mode` row, when the gate denies its first command, then its *Shared* option names `seal pr-checks install` and says nothing is installed, and its *Local* option says a workflow in the tree stays | `tests/test_mode_gate.py` |
| S8 The rule changes parse, apply, and leave the documents' own cases green | Given this spec, when the reader in `skills/settle/scripts/rule_changes.py` reads `## Rule changes`, then every item parses and each `from` appears once in its section of the policy in force. When every item is applied in order to `docs/` at `02ee12de`, as `settle --apply` would apply it, then every test module whose code names a changed document, `README.md`, `README.ko.md` or `docs/` passes, except a case that fails with `docs/` as committed too. Rounds 1, 2 and 3 each found a case green on the branch and red at that settle, and `settle --apply` writes no sentence by hand | the parse half: `chain_check.py --baseline release/v0.22.4` on the branch, which asks that reader for this judged work item. The applied half: a replay in a scratch clone, `parse` then `apply_op` for each item in order, then `bin/test` over those modules, and the same modules with `docs/` restored; run by the smith at phase 3's close as a probe, and by the verifying round |
| S9 Each answer of the chain step's no-root test has a case | Given `chain_check.py#main`'s test for a top-level `seal` entry, when each of its five answers is dropped by a mutant in turn (HEAD without the entry, HEAD with it, git not answering, and under `--worktree` the working tree without the entry and with it), then at least one case in `tests/test_chain_check.py` fails against each mutant | `tests/test_chain_check.py` `Test_retired`, marker `nothing-declared-nothing-owed`; each mutant run once by the smith at phase 3, and named in its phase record |

## Data & interfaces

**`seal pr-checks`**, in `skills/implement/scripts/seal.py`, beside `mode`:

| Form | Writes | Exit |
|---|---|---|
| `seal pr-checks` | nothing | 0, with one of three states |
| `seal pr-checks install` | `.github/workflows/hygiene.yml`, staged | 0 written or already the plugin's; 1 refused, nothing written, or written and not staged; 2 a `hooks/` module missing or a usage error |
| `seal pr-checks remove` | the removal, staged where tracked | 0 removed or nothing there; 1 refused, nothing removed; 2 as above |

The existing `install_workflow`, `remove_workflow` and `plugin_workflow` are
its body. `install_workflow` gains the root precondition and the
already-installed answer.

**`unverified-check`**: the two states of *In* item 6 join the settled root
as exit 0, each with a sentence of its own that names the path and the state
and never reads `open: 0`.

**The bootstrap's mode question**: the three labels of *In* item 1, exactly.

**What a consuming repository receives, which decides the changelog
fragment.** Something the plugin installs does change, so the build's last
phase writes `changelog.md` under `### Changed`:

| What | Before | After |
|---|---|---|
| first setup, default answer | `<repo>/seal/` and `.github/workflows/hygiene.yml` | `<repo>/seal/` only |
| the checks | written by the orchestrator at a shared first setup, carried by `seal mode` | written and removed by `seal pr-checks install` and `seal pr-checks remove` |
| `seal mode local` and `seal mode shared` | stage the workflow file in or out | leave `.github/` alone |
| `unverified-check` at the next pin | exit 2 for a root whose work items carry no `overview.md`, and for no root | exit 0, naming the state |
| an existing installed workflow | unchanged | unchanged, pinned to its release until a person moves the pin |

## Rule changes

- change
  file: docs/one-root-by-lifetime.md
  section: What first setup asks
  from: One `AskUserQuestion` with two options, shared first as the default, each saying what it does:
  to: One `AskUserQuestion` with three options, in this order, the first the default, each saying what it does:
- change
  file: docs/one-root-by-lifetime.md
  section: What first setup asks
  from: **shared** creates `<repo>/seal/`, which the routing commit carries, and installs `.github/workflows/hygiene.yml` from `templates/hygiene.yml` where that path is absent: a clone of the plugin at the release installed at setup, and the two pull-request checks.
  to: **shared, records only** creates `<repo>/seal/`, which the routing
      commit carries, and writes nothing under `.github/`.
    - **shared, with pull-request checks** does the same, then runs
      `seal pr-checks install`, which writes `.github/workflows/hygiene.yml`
      from `templates/hygiene.yml` where that path is absent: a clone of the
      plugin at the release installed at setup, and the pull-request checks.
- change
  file: docs/one-root-by-lifetime.md
  section: Shared or local
  from: "do CI and collaborators see this workflow"
  to: "do collaborators and every other clone see the records"
- change
  file: docs/one-root-by-lifetime.md
  section: Shared or local
  from: | CI (the chain checks) | cannot run; the hygiene workflow is not installed | runs |
  to: | CI (the pull-request checks) | cannot run; `seal pr-checks install` refuses here | runs where first setup's answer or `seal pr-checks install` put the workflow in the tree |
- change
  file: docs/one-root-by-lifetime.md
  section: Shared or local
  from: | Switching later | `seal mode shared` moves `.git/seal/` to `<repo>/seal/`, stages it, and installs the workflow; you commit | `seal mode local` moves `<repo>/seal/` back, stages the removal, and takes the workflow out; you commit |
  to: | Switching later | `seal mode shared` moves `.git/seal/` to `<repo>/seal/` and stages it; you commit | `seal mode local` moves `<repo>/seal/` back and stages the removal; you commit |
- change
  file: docs/one-root-by-lifetime.md
  section: Shared or local
  from: A hygiene workflow left behind in local mode is red forever: `unverified_check.py` runs second and exits 2 for a path that is nowhere, and with no `continue-on-error` the job stops, so `chain_check.py` never runs. Had it run, it would have exited 0 having examined nothing.
  to: **Where the records live and whether CI checks pull requests are two
    answers, and the workflow file is the record of the second.**
    `seal mode` moves the root and writes the `Mode` row, and leaves
    `.github/` alone. `seal pr-checks install` writes
    `.github/workflows/hygiene.yml` from `templates/hygiene.yml` where that
    path is absent, pinned to the installed release, and stages it. It
    refuses where `<repo>/seal/` is not a directory, because the checks read
    committed records. `seal pr-checks remove` takes out a workflow this
    plugin wrote and leaves any other file alone. No config row says whether
    the checks are installed: the file says it, and a second record would be
    a second answer. A workflow pinned to a release that has the no-root
    state, left in a local-mode repository, examines nothing and passes, as
    `docs/the-record-layout.md` *The unverified record, and the baseline it
    is read against* states. One pinned to an older release fails every
    pull request there until its `--branch` line moves or
    `seal pr-checks remove` takes it out, and `seal mode local` names the
    pin when it leaves such a file.
    check: tests/test_seal.py
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 처음 설정에서 무엇을 묻는가
  from: `AskUserQuestion` 한 번에 선택지 둘이고, shared 를 기본값으로 먼저 두며, 각 선택지가 무엇을 하는지 말합니다.
  to: `AskUserQuestion` 한 번에 선택지 셋을 이 순서로 두고, 첫째를 기본값으로
    하며, 각 선택지가 무엇을 하는지 말합니다.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: 처음 설정에서 무엇을 묻는가
  from: **shared** 는 `<repo>/seal/` 을 만들고, 라우팅 커밋이 그것을 싣습니다. `.github/workflows/hygiene.yml` 이 없으면 `templates/hygiene.yml` 에서 설치합니다. 설정할 때 깔린 릴리스의 플러그인 클론과, PR 검사 둘입니다.
  to: **shared, records only** 는 `<repo>/seal/` 을 만들고, 라우팅 커밋이
      그것을 싣습니다. `.github/` 아래에는 아무것도 쓰지 않습니다.
    - **shared, with pull-request checks** 는 같은 일을 한 뒤
      `seal pr-checks install` 을 실행합니다. 이 명령은
      `.github/workflows/hygiene.yml` 이 없으면 `templates/hygiene.yml` 에서
      씁니다. 설정할 때 깔린 릴리스의 플러그인 클론과 PR 검사입니다.
- change
  file: docs/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: "CI 와 협업자가 이 워크플로를 보느냐"
  to: "협업자와 다른 클론이 이 기록을 보느냐"
- change
  file: docs/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: | CI (체인 검사) | 돌 수 없다. hygiene 워크플로가 설치되지 않는다 | 돈다 |
  to: | CI (PR 검사) | 돌 수 없다. `seal pr-checks install` 이 여기서는 거절한다 | 처음 설정의 답이나 `seal pr-checks install` 이 워크플로를 트리에 넣은 곳에서 돈다 |
- change
  file: docs/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: | 나중에 바꾸기 | `seal mode shared` 가 `.git/seal/` 을 `<repo>/seal/` 로 옮기고 스테이지하고 워크플로를 설치한다. 커밋은 사람이 한다 | `seal mode local` 이 `<repo>/seal/` 을 되돌리고 삭제를 스테이지하고 워크플로를 뺀다. 커밋은 사람이 한다 |
  to: | 나중에 바꾸기 | `seal mode shared` 가 `.git/seal/` 을 `<repo>/seal/` 로 옮기고 스테이지한다. 커밋은 사람이 한다 | `seal mode local` 이 `<repo>/seal/` 을 되돌리고 삭제를 스테이지한다. 커밋은 사람이 한다 |
- change
  file: docs/one-root-by-lifetime.ko.md
  section: shared 인가 local 인가
  from: local 모드에 남은 hygiene 워크플로는 영원히 빨간불입니다. `unverified_check.py` 가 두 번째로 돌면서 어디에도 없는 경로에 대해 2 로 끝나고, `continue-on-error` 가 없으니 잡이 멈춰 `chain_check.py` 는 돌지 않습니다. 돌았다면 아무것도 안 본 채 0 으로 끝났을 것입니다.
  to: **기록이 어디 사는가와 CI 가 PR 을 검사하는가는 두 개의 답이고, 둘째의
    기록은 워크플로 파일 자체입니다.** `seal mode` 는 루트를 옮기고 `Mode`
    행을 쓰며, `.github/` 에는 손대지 않습니다. `seal pr-checks install` 은
    `.github/workflows/hygiene.yml` 이 없으면 `templates/hygiene.yml` 에서
    설치된 릴리스로 고정해 쓰고 스테이지합니다. `<repo>/seal/` 이 디렉터리가
    아니면 거절합니다. 검사는 커밋된 기록을 읽기 때문입니다.
    `seal pr-checks remove` 는 이 플러그인이 쓴 워크플로를 빼고, 다른 파일은
    그대로 둡니다. 검사가 설치되었는지를 말하는 설정 행은 없습니다. 파일이
    그것을 말하고, 두 번째 기록은 두 번째 답이 되기 때문입니다. 루트가 없는
    상태를 아는 릴리스로 고정된 워크플로는 local 모드 저장소에 남아도
    아무것도 보지 않고 통과합니다. `docs/the-record-layout.md` *The
    unverified record, and the baseline it is read against* 가 그것을
    말합니다. 그보다 오래된 릴리스로 고정된 워크플로는 `--branch` 줄을
    옮기거나 `seal pr-checks remove` 로 빼기 전까지 그곳의 모든 PR 을
    실패시키고, `seal mode local` 은 그런 파일을 남길 때 고정된 릴리스를
    알려 줍니다.
    check: tests/test_seal.py
- change
  file: docs/branch-and-release.md
  section: Work accumulates on a release branch
  from: run from a clone of this repository at the release installed when the `implement` skill wrote the file at a shared-mode first setup; local mode installs none, because the checks read committed files and local mode commits none.
  to: run from a clone of this repository at the release installed when
    `seal pr-checks install` wrote the file, at first setup or later; it
    refuses in local mode, because the checks read committed files and local
    mode commits none.
- add
  file: docs/the-record-layout.md
  section: The unverified record, and the baseline it is read against
  to: **A pull request that declares nothing owes the unverified check
    nothing.** Handed a `seal/` root's own `specs` path, `unverified-check`
    exits 0 and names the state in two more cases beside the settled root:
    where no `seal/` directory is in the tree, and where `specs/` holds work
    items none of which carries an `overview.md`. There is no row to read,
    and none could have left. Where the root is not in the tree it compares
    nothing against the base either, so the pull request that moves a root
    to local mode is not read as deleting its records. Every other path
    holding no `overview.md` is still exit 2, which keeps a misspelt path
    from passing in silence.
    check: nothing-declared-nothing-owed
- add
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  to: **Where the tree the check reads has no top-level `seal` entry, the
    check reads nothing as declared.** The tree is HEAD, and the working
    tree under `--worktree`. The pull request that moves a root to local
    mode deletes every `routing.md` with the root, and a deleted declaration
    is otherwise judged. With no `seal` entry there is nothing to declare,
    so the check judges the trailers as for any pull request that declares
    nothing. Where git cannot say whether HEAD has the entry, the
    declarations stay judged.
    check: nothing-declared-nothing-owed
- change
  file: docs/the-review-record.md
  section: What the check reads at the pull request
  from: is two declarations and the deletion is judged.
  to: is two declarations and the deletion is judged, except where the tree
    the check reads has no top-level `seal` entry.
- change
  file: docs/the-review-and-parity-arms.md
  section: The declaration, and where the check went
  from: where it does not, the refusal stands.
  to: where it does not, the refusal stands, except where the tree
    the check reads has no top-level `seal` entry (`docs/the-review-record.md`
    *What the check reads at the pull request*).

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| the orchestrator's hand write of the workflow, and the version one-liner | `skills/implement/orchestration.md` *Orchestrator: Bootstrap*, step 1, the **shared** bullet | `seal pr-checks install`, whose `seal.py#plugin_version` reads the version from beside the script |
| the switch's carry of the workflow | `skills/implement/scripts/seal.py#switch`, its calls to `install_workflow` and `remove_workflow` | `seal pr-checks install` and `seal pr-checks remove` |
| the workflow path in the switch's dirty-tree guard | `skills/implement/scripts/seal.py#refusals`, `WORKFLOW` in its `porcelain` call | nothing: the switch no longer stages that path, so nothing there can be lost by it |
| the workflow path in every `git reset` line the switch hands a person | `skills/implement/scripts/seal.py#switch`; `README.md` and `README.ko.md` *Shared or local*; `skills/config/SKILL.md` *Before switching to shared, say what cannot be undone* | `git reset -- :/seal`, because the switch stages nothing else |
| the sentences saying a workflow left in local mode is red forever | `templates/hygiene.yml` header; `seal.py#remove_workflow` docstring; `seal.py#mode` no-root comment; `docs/one-root-by-lifetime.md` and `.ko.md` *Shared or local* | phase 1 makes every step exit 0 there; the header and the rule change say so |
| the mode gate's promise that *Shared* installs the checks and *Local* removes the workflow | `hooks/mode-gate.py#question_reason` | the options name `seal pr-checks install`, and say a workflow in the tree stays |
| exit 2 for `seal/specs/` holding work items and no overview, and for no `seal/` root | `skills/verify/scripts/unverified_check.py#main` | exit 0 naming the state; the new rule in `docs/the-record-layout.md` |
| the case that pins the bootstrap's version one-liner | `tests/test_first_setup_asks_once.py#test_the_version_is_read_from_the_plugin_root_and_not_from_the_tree` | `tests/test_seal.py` `Test_plugin_version`, which already pins the read |
| the pins of two options, the shared option naming `hygiene`, the hand write and the red-forever header | `tests/test_first_setup_asks_once.py`, the cases at lines 71 to 91 and 437 to 471 | rewritten in phase 2 to pin three options, `seal pr-checks install` and the new header |
| the switch cases that assert the workflow is carried and its path guarded | `tests/test_seal.py` `Test_switch` and `Test_refusals` | rewritten to assert `.github/` is left alone; `Test_pr_checks` holds the install and remove cases |

## Open questions

None here: each is a row of `questions.md`.

Framed 2026-10-26 by framer, before the build.
Reframed 2026-10-26 by framer, after round 3.
