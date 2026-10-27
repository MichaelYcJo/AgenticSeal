# Feature Specification: 1793081611-the-plugin-is-named-for-a-spec-it-no-longer-seals-by

Builds #1051: the plugin is renamed to AgenticSeal, its agents and records
take names that say what each does, the command line becomes
`seal <subcommand>`, and a `seal/` directory is read as the plugin's root
only where its marker stands. Milestone `release: 0.23.0` fixes the
release's purpose: names and places only, behaviour unchanged.

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| `CLAUDE.md` *The goal a design is chosen against* | Every choice below prefers the design that stops to ask nobody: the migration of an installed repository runs at session start and asks nothing, and the step an installed user runs is printed, not asked |
| `CLAUDE.md` *The rule a mechanism is kept against* | `hooks/root-migrate.py`'s arm for a top-level `specs/` and `.specseal/` is removed, not kept beside the new arm: it is the one reader of a directory another tool may own, and README.md *Coming up from 0.3.x* already holds the by-hand path |
| `docs/one-root-by-lifetime.md` *The opt-in signal is the root itself* | The rule this work changes: the root is the signal, and after this work the root is the signal only with its marker. The fail direction stays: no marker reads as not opted in |
| `docs/one-root-by-lifetime.md` *The plugin writes only to its own root* and `templates/config.md` *Reference specs* | A top-level `specs/` is a reference root the plugin reads as history and never takes. After this work no code opens it at all, which is the stronger form of the same rule |
| `docs/the-record-layout.md` *seal/specs/<work-item-id>/* | The files of a work item keep their paths until the settle. This work changes the paths once, for every work item at once, through the migration, so the rule holds under the new names |
| `docs/the-routing-check.md` *At the pull request* | The trailer is read by git's trailer parser and tells a session's commit from a person's. The rename keeps that reading and adds a grace for the old spelling, bounded to 0.23.x |
| `docs/the-agent-set.md` *One contract every agent receives, and one definition each* | An agent's rules live in its definition, so renaming an agent is a `git mv` of its definition plus every text that names it; nothing in the contract names an agent |
| `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The policy root is the baseline a pull request does not edit. This work edits it for spellings only, as *Scope* below states, and states every rule whose content changes in *Rule changes* |
| `https://code.claude.com/docs/en/plugins/host-marketplace.md` *Rename or remove a plugin* (read 2026-10-27) | The `renames` map carries a plugin's rename inside one marketplace, is append-only, and `claude plugin validate .` checks its chain. The page says Claude Code identifies a marketplace by its `name` and does not say what a changed `name` does to an existing registration |
| `https://code.claude.com/docs/en/plugins/cli-reference.md` *plugin marketplace remove* (read 2026-10-27) | Removing a marketplace from the last scope that declares it also deletes its cache and uninstalls every plugin installed from it. That is what makes the three-line step below complete |

## Scope

**In.** Every row of #1051's mapping, applied whole in one release:

| What | Now | After |
|---|---|---|
| The brand, where a person reads it | SpecSeal | AgenticSeal |
| The plugin's `name` and the prefix of every agent and skill | `specseal` | `agentic` |
| The plugin's `displayName` | SpecSeal | AgenticSeal |
| The marketplace's `name` | `specseal` | `agenticseal`; the install id is `agentic@agenticseal`; `renames` maps `specseal` to `agentic` |
| The repository slug in living text | `MichaelYcJo/SpecSeal` | `MichaelYcJo/AgenticSeal` |
| The command line | one command per tool under `bin/` | `seal <subcommand>`, one subcommand per tool, in `skills/implement/scripts/seal.py` |
| A work item's directory | `seal/specs/<id>/` | `seal/threads/<id>/` |
| The frame | `spec.md`, `plan.md`, `questions.md` | `frame/design.md`, `frame/plan.md`, `frame/questions.md` |
| What the parties hand each other | `phases/`, `rounds/`, `broad-gate.md` | `trail/phases/`, `trail/rounds/`, `trail/gate.md` |
| The sealer's conclusion | `guarantee.md` | `guarantee.md`, at the top of the thread |
| The closing memo | `overview.md` | `gaps.md`, at the top of the thread |
| What else stays at the top of a thread | `routing.md`, `changelog.md` | unchanged |
| The agents | framer, smith, warden, sealer, scribe | framer, crafter, proofer, sealer, tracer |
| The commit trailer | `SpecSeal-Routing:` | `Seal-Routing:` |
| The tagline | "Specs, sealed" | gone; one sentence describes the plugin |
| The opt-in | a `seal/` directory exists | a `seal/` directory exists and its `README.md` opens with the marker |
| A top-level `specs/` or `.specseal/` | read once by `hooks/root-migrate.py` and moved | read by nothing |

A thread holds two folders and four files at its top, and a record is
placed by what it is, never by which agent wrote it: `frame/` is the design
before the build, `trail/` is what passed between the parties, and
`routing.md`, `changelog.md`, `guarantee.md` and `gaps.md` speak for the
whole thread. The owner chose `trail` over `work`, `gaps` over `overview`,
and crafter and proofer over coder and inspector on 2026-10-27, and #1051's
body under *The mapping* states each name's origin; this frame names only
the chosen spellings. The names a person does not read but a file holds, which the mapping does
not list, follow the plugin's `name`: the state files under the git common
directory (`specseal-scratch`, `specseal-no-work-item`, `specseal-leases`,
`specseal-planner`, `specseal-implementer`, `specseal-implementer-notice`,
`specseal-gate-failure`, `specseal-mode-choice`, `specseal-mode-retry`,
`specseal-review-choice`, `specseal-worktree-choice`,
`specseal-worktree-consent`, `specseal-stamp`, `specseal-stamp-refused`,
`specseal-last-export.json`) take `agentic-` for `specseal-`, and
`~/.claude/specseal/` becomes `~/.claude/agentic/`. The session-start
migration renames each one it meets. Q2 of `questions.md` holds the choice,
and the build runs on this default.

**The step an installed user runs.** A user installed as
`specseal@specseal` registered a marketplace named `specseal`. Claude Code
identifies a marketplace by its `name`, and the reference does not say what
happens when the catalog a registration points at changes its own `name`,
so the step that is documented to work is to re-register:

```
claude plugin marketplace remove specseal
claude plugin marketplace add MichaelYcJo/AgenticSeal
claude plugin install agentic@agenticseal
```

The first line uninstalls `specseal@specseal` and deletes its cache with the
marketplace (`cli-reference.md` *plugin marketplace remove*). Then the user
runs `bash install.sh` again, or `/agentic:preset-setup`, so the CLAUDE.md
block takes the new markers and the new prefix. README.md *Install* carries
the three lines under a heading for users coming from `specseal@specseal`,
and `skills/update/SKILL.md` runs the new names. The `renames` map is still
written: it costs one line, it is the documented way a plugin's rename
reaches a registration, and it covers the registration Claude Code may keep
by the old name after the catalog changes.

**The policy root is rewritten in place for names and paths.** `docs/`
holds 12 files naming SpecSeal and 9 naming smith, warden or scribe
(`git grep`, executed 2026-10-27 at `bac5dcdd`). `skills/implement/SKILL.md`
*Document layout — two roots, three lifetimes* says a pull request does not edit the policy root, and the
reason is that a rule's decision is made at the settle, from the released
specs. A spelling carries no decision: a sentence naming `smith` says the
same thing of `crafter`. So the build rewrites every old name and path in
`docs/` where it stands, in the same commit as the code that reads the new
one, and *Rule changes* below states each rule whose content changes, with
`from` quoting the text as read on 2026-10-27. The proofer reads a `docs/`
edit against this paragraph, not as a divergence.

**What keeps the old name, and why.** The released changelog
(`changelog/*.md`, `CHANGELOG.md`) keeps the name each release shipped
under, as #1051 states. The changelog fragment marker
`<!-- specs/<work-item-id> -->` keeps its spelling: `gather_changelog.py`
decides what is gathered by reading that marker across every released file,
the marker is vocabulary a reader matches and not a path, and the 0.4.0
root move kept it for the same reason (`tests/test_no_document_names_the_old_roots.py`,
KEEP). The recorded eval scaffolds (`evals/behaviour/*/*/scaffold.sh`) keep
their clone line: each is generated, never edited by hand (`evals/README.md`),
records a run at a SHA, and the old URL redirects. The eval directories and
prompts rename with the agents (`evals/behaviour/warden/` becomes
`evals/behaviour/proofer/`), because `noninferiority.py --agent` is typed
by a person. Three readers keep reading an old spelling for one minor
release, each labelled at its constant and exempted from the census with a
reason: `chain_check.py` accepts `SpecSeal-Routing:` beside `Seal-Routing:`
on commits for 0.23.x; `hooks/stub-remove.py` keeps `# specseal-git-hook`,
which is the text a stub an earlier release wrote carries; `install.sh` and
`uninstall.sh` recognise the block between `<!-- specseal:start -->` and
`<!-- specseal:end -->` in a user's CLAUDE.md and replace it with the block
under the new markers. `.test_durations` is a cache the test runner writes
and is not living text.

**Out.**

- #1060, the reorganisation of `docs/`, `templates/`, `hooks/`, `skills/`
  and `tests/` by area and kind. This work moves no file between those
  directories. `bin/test` and `bin/test.cmd`, the repository's own suite
  runner, stay where they are: they are not a tool of the workflow, and
  #1060 decides where the repository's developer scripts live. `bin/seal`
  and `bin/seal.cmd` stay, because `bin/` is what Claude Code puts on PATH.
- #857, the stamp's placeholder S, in 0.23.1. `skills/verify/scripts/seal_stamp.py`
  changes its state file names only.
- Behaviour. No gate, check or agent's job changes. A test that pins a
  message changes the name in the message and nothing else.
- The repository's About text and topics, which live in GitHub's settings:
  the orchestrator sets them with `gh repo edit` when the release pull
  request merges into `main` (`plan.md` *Operational impact*).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| The plugin installs under its new id | Given the tree at the release tag, when a user runs the three lines above, then `claude plugin list` shows `agentic@agenticseal`, and every agent and skill answers to `agentic:` | `claude plugin validate .` exits 0 (a measurement the crafter runs); the install on a machine is a person's, Q4 of `questions.md` |
| A user installed as `specseal@specseal` reaches the new id | Given a machine with `specseal@specseal`, when the user runs the three lines and `bash install.sh`, then the old plugin and marketplace are gone and the CLAUDE.md block carries `agentic:` and the new markers | `tests/test_first_setup_asks_once.py`: `install.sh` over a CLAUDE.md holding the old block leaves one block, under the new markers; the live install is Q4 |
| The tagline is gone | When `git grep -F "Specs, sealed"` runs over the tree, then it matches nothing, and README.md, `plugin.json` `description` and both `description` fields of `marketplace.json` hold the one sentence | a case reads the three files and the grep |
| One spelling is left | When the census runs over every tracked file, then no living file names `specseal`, `SpecSeal`, `smith`, `warden`, `scribe`, `seal/specs/`, `SpecSeal-Routing`, `broad-gate.md`, `overview.md`, a bare `phases/` or `rounds/`, or `agent-specseal`, outside `changelog/`, `CHANGELOG.md`, the recorded scaffolds, and a line exempted with a reason | `tests/censuses.py#old_names`, run by `tests/test_censuses.py` over every tracked file; the case is seen red against the tree before the sweep |
| An installed repository migrates at its first session | Given a repository holding `seal/specs/<id>/` with `rounds/`, `phases/`, `broad-gate.md` and `guarantee.md` and a `seal/README.md` without the marker, when a session starts, then `seal/threads/<id>/frame/` and `trail/` hold the files as staged `git mv`, with `guarantee.md` and `gaps.md` at the thread's top, `README.md` opens with the marker, one line says what moved, and the gates decide as they did | `tests/test_root_migrate.py`: a fixture at the 0.22.x layout in shared mode and in local mode, migrated end to end; the gates' decisions pinned by their own modules |
| A `seal/` without the marker is not a root | Given a repository whose `seal/README.md` lacks the marker or is absent, when any gate runs, then `optin.home_at` answers "" and the gate says nothing | `tests/test_optin.py` |
| First setup meets a foreign `seal/` | Given a repository with a `seal/` of its own and no marker, when first setup runs, then nothing is written into it and the orchestrator is told local mode keeps the root under the git directory | `tests/test_first_setup_asks_once.py` reads the bootstrap's sentence |
| No code reads a top-level `specs/` | Given a repository holding another tool's `specs/<unix-seconds>-<slug>/` with a tracked `routing.md`, when a session runs, then nothing moves and nothing is printed | `tests/test_root_migrate.py`; `git grep` for `OLD_ITEMS` and `.specseal` in `hooks/` matches only the README section's quotation |
| The old trailer is read for one release | Given a pull request whose commits carry `SpecSeal-Routing: <id>` and `Seal-Routing: <id>`, when `chain_check.py` judges it, then both are read as the work item's trailer, and the reader's comment names 0.24.0 as the release that removes the old spelling | `tests/test_chain_check.py` |
| The command line is one command | When `seal gate --base <base> --record <item>` and each other subcommand run, then each runs the script its `bin/` wrapper ran, with the same arguments | `tests/test_seal.py`: each subcommand resolves to its script; `bin/` holds `seal`, `seal.cmd`, `test`, `test.cmd` and nothing else |
| This repository runs on the new layout | Given this branch, when the pull request opens, then this work item stands at `seal/threads/<id>/` and CI's `chain_check.py` from the tree judges it | the hygiene workflow's run on the pull request, read by the orchestrator |

## Data & interfaces

**Readers of the work item path.** `hooks/optin.py#WORK_ITEMS` (`"specs"`
at line 41) becomes `"threads"`, and `hooks/routing.py#WORK_ITEMS`
(`"seal/specs"`, line 121) follows it; `tests/test_routing.py:645` pins the
new value. The readers that join a file name under the work item change
with the layout: `chain_check.py` (the depth at line 1624 counts
`<WORK_ITEMS>/<id>/frame/design.md`; the rounds under `trail/rounds/`,
`trail/gate.md`, and `guarantee.md` at the top), `unverified_check.py`
(`gaps.md`, which was `overview.md`), `settle.py` and `rule_changes.py`
(`frame/design.md`), `broad_gate.py --record` (`trail/gate.md`),
`hooks/sealer-stamp-queue.py` and `seal_stamp.py` (`guarantee.md`,
unchanged path), `hooks/routing.py#rounds` (`trail/rounds/`),
`gather_changelog.py` (`changelog.md`, unchanged path),
`seal.py#work_item_of` (line 389), `hooks/mode-gate.py`,
`hooks/cmdline_base.py`, `.github/workflows/hygiene.yml` and `test.yml`
globs, `.github/PULL_REQUEST_TEMPLATE.md`, and the 28 files
`git grep -l seal/specs -- hooks skills .github templates` lists (executed
2026-10-27). The templates rename with the files: `templates/sdd-spec.md`
becomes `templates/sdd-design.md` and `templates/sdd-overview.md` becomes
`templates/sdd-gaps.md`; `sdd-plan.md`, `sdd-questions.md`, `sdd-phase.md`,
`sdd-round.md`, `sdd-guarantee.md` and `sdd-routing.md` keep their names,
because a template is named for the file it starts and those file names do
not change.

**The marker.** `hooks/optin.py` gains `MARKER`, the first line of
`templates/seal-README.md`, which is the heading
`# What AgenticSeal maintains in seal/`. `home_at` answers a path only
where `<path>/README.md` exists and its first line, with the line end
stripped, equals `MARKER`; every other state answers "". The template's
first line is pinned to the constant by a case, so the two cannot drift.
The one reader of the question stays `home_at`.

**The migration.** `hooks/root-migrate.py` keeps its name, its place in
`hooks/dispatch.py#GROUPS["session-start"]` and its boundaries (never over
uncommitted work, only what git tracks, once per repository, a stopped move
resumes, silent when there is nothing to do, a symbolic link refused). Its
units become: each `seal/specs/<id>/` to `seal/threads/<id>/`, with
`spec.md` to `frame/design.md`, `plan.md` and `questions.md` into `frame/`,
`phases/` and `rounds/` into `trail/`, `broad-gate.md` to `trail/gate.md`,
`overview.md` to `gaps.md`, and `routing.md`, `changelog.md`,
`guarantee.md` and any `pr.*.md` left at the top; the units list through
`entries`, the symbolic-link refusal points at `seal/specs/`, and the
rewrite of `seal/README.md` to the marker is a unit of this move, as phase
1's record states; `seal/README.md`
rewritten from the template so it opens with the marker; the same under the
git common directory in local mode, where the moves are renames and not
`git mv`; and each state file beside the root renamed from `specseal-` to
`agentic-`. The once-per-repository stamp moves to
`~/.claude/agentic/threads-migrated`, and `~/.claude/specseal/` is renamed
to `~/.claude/agentic/` where the old exists and the new does not. The
constants `OLD_HOME`, `OLD_ITEMS`, `OLD_SCRATCH`, `ITEM_RE`, `MARKS` and
the functions `marked`, `tracked_marks`, `unmarked`, `old_items` leave with
the arm they served.

**The command line.** `skills/implement/scripts/seal.py#main` (line 2704
and after) adds one subparser per tool, each handing its arguments to the
script its wrapper ran: `gate` to `skills/verify/scripts/broad_gate.py`,
`settle` to `skills/settle/scripts/settle.py`, `cost` to `session_cost.py`,
`mutate` to `mutation_check.py`, `unverified` to `unverified_check.py`,
`arms` to `arm_check.py`, `deferrals` to `deferral_check.py`, `fold` to
`fold_check.py`, `pact` to `pact_check.py`, `payload` to
`payload_meter.py`, `stamp` to `seal_stamp.py`, `layout` to
`test_layout.py`, `rules` to `.github/scripts/rules.py`. Each script keeps
its own `main(argv)`, so a subcommand is a dispatch and not a copy. Q1 of
`questions.md` holds the names the issue did not fix. Every document that
printed a bare command prints the subcommand; `seal/config.md`'s `Broad
gate` row keeps `bin/test -q`.

**The trailer.** `chain_check.py#TRAILER` (line 2054) becomes
`Seal-Routing`, and `trailers()` (line 2074) reads both keys from git's
trailer parser, with a comment at the old key naming 0.24.0 as the release
that removes it. `templates/claude-md-block.md`,
`skills/commit-pr-convention/SKILL.md`, `templates/hygiene.yml`, the
hygiene workflow and every document that spells the trailer spell the new
one.

**The names.** `.claude-plugin/plugin.json`: `name` `agentic`,
`displayName` `AgenticSeal`, `description` the one sentence, `homepage` and
`repository` at the new slug. `.claude-plugin/marketplace.json`: `name`
`agenticseal`, both `description` fields the one sentence, the plugin entry
`agentic`, `renames` `{"specseal": "agentic"}`. `agents/smith.md`,
`agents/warden.md`, `agents/scribe.md` move by `git mv` to `crafter.md`,
`proofer.md`, `tracer.md`, with `name:` changed; `hooks/implementer.py#AGENT_MARKS`
(line 57) and `mark_for` (line 122) spell `crafter` and the `agentic:`
prefix; `hooks/review-skill-gate.py#OURS` (line 42) spells
`agentic:code-review` and the reason names `@agent-agentic:proofer`;
`seal.py#PLUGIN_CLONE` (line 1381) and `templates/hygiene.yml` lines 54 and
55 take the new slug, and `workflow_at` (line 1841) recognises a workflow
carrying either clone line as this plugin's so that `seal pr-checks install`
rewrites one it wrote under the old slug. The 225 `specseal:` sites in 47
files (executed 2026-10-27) take `agentic:`.

**The one sentence.** README.md, `plugin.json` `description` and both
`marketplace.json` `description` fields hold exactly: *A workflow of agents
that frames, builds, inspects and seals a change without asking anyone, and
ends in a seal bound to a commit.* README.ko.md states it in Korean.

## Rule changes

- change
  file: docs/one-root-by-lifetime.md
  section: The opt-in signal is the root itself
  from: **A repository is opted in when `seal/` exists at its mode's location**: `<repo>/seal/` in shared mode, `$(git rev-parse --git-common-dir)/seal/` in local mode. The hooks look at the two places in that order; whichever exists says both "on" and which mode.
  to: **A repository is opted in when `seal/` exists at its mode's location and its `README.md` opens with the plugin's marker**: `<repo>/seal/` in shared mode, `$(git rev-parse --git-common-dir)/seal/` in local mode. The marker is the first line of `templates/seal-README.md`, written at first setup and by the migration of a repository installed before 0.23.0. The hooks look at the two places in that order; whichever exists with the marker says both "on" and which mode. A `seal/` without the marker is a project's own directory, as a package named `seal` has one, and reads as not opted in; first setup that meets one writes nothing into it and keeps the root under the git directory.
- change
  file: docs/one-root-by-lifetime.md
  section: The opt-in signal is the root itself
  from: A throwaway repository turns the gates off with an empty file, `.git/specseal-scratch`, under the common git directory, which no commit can carry to another clone.
  to: A throwaway repository turns the gates off with an empty file, `.git/agentic-scratch`, under the common git directory, which no commit can carry to another clone.
- change
  file: docs/one-root-by-lifetime.md
  section: The plugin writes only to its own root
  from: A `specs/` directory anywhere else is the project's own, read as history and never taken (`templates/config.md` *Reference specs*).
  to: A `specs/` directory anywhere else is the project's own, read as history and never taken (`templates/config.md` *Reference specs*), and no code of the plugin opens a top-level `specs/` or `.specseal/`: the 0.3.x layout moves by hand, with the commands README.md *Coming up from 0.3.x* gives, and that section says it is the only path.
- change
  file: docs/one-root-by-lifetime.md
  section: Naming
  from: **The product is SpecSeal, and bare `seal` is the vocabulary inside it**: the root `seal/`, the `seal export` / `seal import` commands, "the seal" for the record.
  to: **The product is AgenticSeal, and bare `seal` names the result inside it**: the root `seal/`, the `seal` command line, the sealer, "the seal" for the record. The plugin's `name` and the prefix of every agent and skill is `agentic`; the marketplace is `agenticseal`; the commit trailer is `Seal-Routing:`. Every identifier is lowercase with no separator, and `AgenticSeal` is written only where a person reads the brand.
- change
  file: docs/one-root-by-lifetime.md
  section: Naming
  from: | SpecSeal | seals a spec to the code that implements it | | `seal/` | the root, visible beside `docs/`, because the work items in flight are what people read while a pull request is open | | `seal/specs/<id>/` | a work item's directory, named for the primary artifact it holds |
  to: | AgenticSeal | a workflow of agents that frames, builds, inspects and seals a change without asking anyone, and ends in a seal bound to a commit | | `seal/` | the root, visible beside `docs/`, because the work items in flight are what people read while a pull request is open | | `seal/threads/<id>/` | a work item's directory: one thread, one issue, one branch, one pull request, with `frame/` for the design before the build, `trail/` for what passed between the parties, and `routing.md`, `changelog.md`, `guarantee.md` and `gaps.md` at its top, each record placed by what it is and never by which agent wrote it | | framer, crafter, proofer, sealer, tracer | the agents, each named for its part of one order: the framer designs the work, the crafter builds it, the proofer finds its defects, the sealer gives the final guarantee and seals it, and the tracer, outside that order, traces what an original codebase does |
- change
  file: docs/one-root-by-lifetime.md
  section: Naming
  from: A directory says what is in it to whoever opens it first, so no directory is named for a metaphor; smith and warden stay agent personas.
  to: A directory and an agent say what each is to whoever meets it first, so neither is named for a metaphor.
- change
  file: docs/the-record-layout.md
  section: seal/
  from: | `seal/specs/<work-item-id>/` | one work item's records, the table below |
  to: | `seal/threads/<work-item-id>/` | one work item's records, the table below |
- change
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  from: | `spec.md` | what is built, its scenarios, and the decisions with their grounds | | `plan.md` | in which phases it is built, how each is shown, and the approval line | | `questions.md` | which decisions only a person could make, and how each was answered | | `overview.md` | what the diff cannot show: purpose, divergences, what was not verified | | `phases/phase-N.md` | what one build phase was asked, found and removed | | `rounds/round-N.md` | what one review round read, found and closed | | `changelog.md` | this work item's entry in the next release's notes | | `broad-gate.md` | the orchestrator's one broad run, on either routing answer | | `guarantee.md` | whether the sealer sealed the work, against the issue and the tree |
  to: | `frame/design.md` | what is built, its scenarios, and the decisions with their grounds | | `frame/plan.md` | in which phases it is built, how each is shown, and the approval line | | `frame/questions.md` | which decisions only a person could make, and how each was answered | | `gaps.md` | where the build departed from the frame, what was not verified and who answers it, and what was not done | | `trail/phases/phase-N.md` | what one build phase was asked, found and removed | | `trail/rounds/round-N.md` | what one review round read, found and closed | | `changelog.md` | this work item's entry in the next release's notes | | `trail/gate.md` | the orchestrator's one broad run, on either routing answer | | `guarantee.md` | whether the sealer sealed the work, against the issue and the tree |
- change
  file: docs/the-record-layout.md
  section: seal/specs/<work-item-id>/
  from: **The files keep these paths until the settle after their release, and leave together.** `routing.md`, the SDD set (`spec.md`, `plan.md`, `questions.md`, `overview.md`, `changelog.md`) and the process record (`rounds/`, `phases/`, `broad-gate.md`, `guarantee.md`, and a `pr.*.md` where one was written) go with the directory, whole, when the settle removes it
  to: **The files keep these paths until the settle after their release, and leave together.** `routing.md`, the frame (`frame/design.md`, `frame/plan.md`, `frame/questions.md`), the trail (`trail/rounds/`, `trail/phases/`, `trail/gate.md`) and the files at the thread's top (`gaps.md`, `changelog.md`, `guarantee.md`, and a `pr.*.md` where one was written) go with the directory, whole, when the settle removes it. A repository installed before 0.23.0 holds the files under `seal/specs/<id>/` at their old names, and `hooks/root-migrate.py` moves them into this layout at the session start of each branch whose tree still holds them, as staged `git mv` in shared mode and as renames under the git directory in local mode
- change
  file: docs/the-routing-check.md
  section: At the pull request
  from: **A session's commit in a repository whose root is shared ends with one trailer, `SpecSeal-Routing:`, naming its work item or reading `no work item`; at a local root a commit carries none.**
  to: **A session's commit in a repository whose root is shared ends with one trailer, `Seal-Routing:`, naming its work item or reading `no work item`; at a local root a commit carries none.** A commit made before 0.23.0 carries `SpecSeal-Routing:`, which `chain-check` reads as the same trailer through 0.23.x; 0.24.0 removes that reading.
- change
  file: docs/the-routing-check.md
  section: At the pull request
  from: **At a shared root, `chain-check` fails a ready pull request where one of its own commits, committed by its author, carries a `SpecSeal-Routing` trailer naming a work item that no declaration it judges names, and prints each commit whose trailer reads `no work item`.**
  to: **At a shared root, `chain-check` fails a ready pull request where one of its own commits, committed by its author, carries a `Seal-Routing` trailer naming a work item that no declaration it judges names, and prints each commit whose trailer reads `no work item`.**
- change
  file: docs/the-routing-check.md
  section: The edit check
  from: It is `<git-common-dir>/specseal-no-work-item/<session-id>`, one line per branch
  to: It is `<git-common-dir>/agentic-no-work-item/<session-id>`, one line per branch
- change
  file: docs/the-routing-check.md
  section: Where the routing is checked
  from: A stub is a file in the common git directory's `hooks/` whose second line starts with the marker `# specseal-git-hook`, and a hook file without it is never touched.
  to: A stub is a file in the common git directory's `hooks/` whose second line starts with the marker `# specseal-git-hook`, the text every stub an earlier release wrote carries, and a hook file without it is never touched. The marker keeps the old name because the files it names were written under it.
- change
  file: docs/the-session-hooks.md
  section: Registration
  from: The dispatcher writes a record under `<git-common-dir>/specseal-gate-failure/`, keyed by session and gate
  to: The dispatcher writes a record under `<git-common-dir>/agentic-gate-failure/`, keyed by session and gate
- change
  file: docs/the-session-hooks.md
  section: The implementer mark and notice
  from: **A `framer` or `smith` spawn leaves a mark, and a commit on a branch whose declaration names that agent, with no mark standing, gets one line saying so.**
  to: **A `framer` or `crafter` spawn leaves a mark, and a commit on a branch whose declaration names that agent, with no mark standing, gets one line saying so.**
- change
  file: docs/the-session-hooks.md
  section: The implementer mark and notice
  from: | `implementer-mark` (`pre-agent`) | an Agent or Task spawn whose `subagent_type` is `framer` or `smith` | writes the name of the branch checked out, else of the branch a paused rebase names, to `<git-dir>/specseal-planner` or `<git-dir>/specseal-implementer`, and prints nothing |
  to: | `implementer-mark` (`pre-agent`) | an Agent or Task spawn whose `subagent_type` is `framer` or `crafter` | writes the name of the branch checked out, else of the branch a paused rebase names, to `<git-dir>/agentic-planner` or `<git-dir>/agentic-implementer`, and prints nothing |
- change
  file: docs/the-agent-set.md
  section: What each party writes, and when
  from: **A review round is one file the warden writes, the fix pass writes two lines of each finding it answers, the orchestrator's broad run writes `broad-gate.md`, and the sealer's verdict is `guarantee.md`.**
  to: **A review round is one file the proofer writes, the fix pass writes two lines of each finding it answers, the orchestrator's broad run writes `trail/gate.md`, and the sealer's verdict is `guarantee.md` at the thread's top.**
- change
  file: docs/the-agent-set.md
  section: What each party writes, and when
  from: No case runs the scribe. That a spawn opens `legacy-parity` first, returns facts and no verdict, and returns `original not found` where the original does not resolve is read from `agents/scribe.md`, not observed.
  to: No case runs the tracer. That a spawn opens `legacy-parity` first, returns facts and no verdict, and returns `original not found` where the original does not resolve is read from `agents/tracer.md`, not observed.
- add
  file: docs/the-agent-set.md
  section: One contract every agent receives, and one definition each
  to: **The agents are the framer, the crafter, the proofer, the sealer and the tracer, and each name says its part of one order.** The framer designs the work, the crafter builds it, the proofer finds its defects, the sealer gives the final guarantee and seals it, and the tracer, outside that order, traces what an original codebase does for a migration. The crafter is named for the Software Craftsmanship movement, and the proofer for the proof impression a seal maker strikes to find a defect before the seal is used. An agent's name is its definition's file name under `agents/` and the word every spawn, mark and record uses for it, so a rename is a `git mv` of the definition and of every text that names it, in one release. check: tests/censuses.py

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The wrappers `bin/arm-check`, `bin/broad-gate`, `bin/deferral-check`, `bin/fold-check`, `bin/mutation-check`, `bin/pact-check`, `bin/payload-meter`, `bin/rules`, `bin/seal-stamp`, `bin/session-cost`, `bin/settle`, `bin/test-layout`, `bin/unverified-check` and each one's `.cmd` twin | `bin/` | `skills/implement/scripts/seal.py#main`, one subparser each; `bin/seal`, `bin/seal.cmd`, `bin/test`, `bin/test.cmd` stay |
| The arm that reads `.specseal/` and a top-level `specs/` | `hooks/root-migrate.py#OLD_HOME`, `#OLD_ITEMS`, `#OLD_SCRATCH`, `#ITEM_RE`, `#MARKS`, `#marked`, `#tracked_marks`, `#unmarked`, `#old_items`, the `.specseal` and `specs` branches of `#moves` and `#main`, and `tests/test_root_migrate.py`'s cases over them | Nothing reads a top-level `specs/` after this; README.md *Coming up from 0.3.x* holds the by-hand commands and says it is the only path |
| The stamp `~/.claude/specseal/root-migrated` | `hooks/root-migrate.py#MARKER` | `~/.claude/agentic/threads-migrated`, a new once-per-repository stamp for the new move |
| The tagline "Specs, sealed" | `README.md:7`, `README.ko.md:7`, `.claude-plugin/marketplace.json:11` | The one sentence, at the same three places and `plugin.json` `description` |
| The sentence "smith and warden stay agent personas" | `docs/one-root-by-lifetime.md` *Naming* | *Rule changes* above: no agent is named for a metaphor |
| The paragraph beginning "Nothing writes `.specseal/` or a top-level `specs/` any more" | `templates/seal-README.md`, `seal/README.md` | A paragraph saying the first line is the marker and what a `seal/` without it is |
| The paragraphs describing the automatic move at session start | `README.md` *Coming up from 0.3.x*, `README.ko.md` the same section | The section keeps the by-hand commands and says they are the only path |
| The bootstrap's sentence telling the session to wait for the 0.3.x move | `skills/implement/orchestration.md` *Orchestrator: Bootstrap*, the paragraph beginning "First, look for the 0.3.x layout" | The bootstrap names README.md *Coming up from 0.3.x* as the by-hand path and continues |
| `agents/smith.md`, `agents/warden.md`, `agents/scribe.md` | `agents/` | `agents/crafter.md`, `agents/proofer.md`, `agents/tracer.md`, by `git mv` |
| `templates/sdd-spec.md`, `templates/sdd-overview.md` | `templates/` | `templates/sdd-design.md`, `templates/sdd-gaps.md`, by `git mv` |
| `evals/behaviour/warden/`, `evals/behaviour/smith/` | `evals/behaviour/` | `evals/behaviour/proofer/`, `evals/behaviour/crafter/`, by `git mv`; the recorded `scaffold.sh` files keep their bytes |
| The KEEP entries whose lines leave with the moved arm | `tests/test_no_document_names_the_old_roots.py#KEEP`: the bootstrap's entry and the seal README's entry | Each KEEP entry must still occur somewhere, so an entry whose line leaves goes with it |
| The assertion `routing.WORK_ITEMS == "seal/specs"` | `tests/test_routing.py:645` | The same case pins `"seal/threads"` |
| `/specseal:update`'s repair lines naming `specseal@specseal` and `marketplaces/specseal` | `skills/update/SKILL.md` lines 23, 24, 45, 60 | The same lines under the new names |

## Open questions

<none here: each is a row of `questions.md`>

Framed 2026-10-27 by framer, before the build.
