# AgenticSeal

[![tests](https://github.com/MichaelYcJo/AgenticSeal/actions/workflows/test.yml/badge.svg)](https://github.com/MichaelYcJo/AgenticSeal/actions/workflows/test.yml)

**English** · [한국어](./README.ko.md)

A workflow of agents that frames, builds, inspects and seals a change without
asking anyone, and ends in a seal bound to a commit.

Coding agents make claims. AgenticSeal makes each claim leave something you can
open: a **hand-back** in which each agent labels every claim `executed`,
`read` or `unverified` and names who answers what it did not run, a
**routing declaration** (`seal/threads/<work-item-id>/routing.md`) that an edit
hook looks for before the first edit, and a **`check:` line** under each rule
a policy document states, naming the test that holds it.

Edit a file on a branch no declaration names and the hook refuses the edit
and names the ways on. Point a rule's `check:` line at a test that does not
exist and `seal rules --check` exits non-zero. Neither is a wall — both
are a record you have to walk past knowingly.

Distributed as a Claude Code **plugin**; the handoff protocol and
`seal rules --check` work anywhere git does.

## Why the always-on context is small

A seal is small; that is the point. Based on
[arxiv 2602.11988](https://arxiv.org/abs/2602.11988), context files generally
do *not* improve task success while adding over 20% inference cost — the model
already knows SOLID, DRY, and "read before edit". AgenticSeal ships only what
changes default behavior; everything else loads when summoned (skills) or
works outside the context entirely (hooks).

## What ships

| Who / what | Follows | What it concretely is |
|---|---|---|
| **framer** (subagent) | `core`, `agent-contract` | Writes the work item's `frame/design.md`, `frame/plan.md` and `frame/questions.md` before anybody builds, and is spawned where the SDD ladder already calls for a design. It reads the repository widely, opens `implement` at the step that decides the ladder and the file set and `writing-style` before it writes, answers from the tree what the tree can answer, and leaves only the rest to `questions.md`. The session asks the routing batch before the framer is spawned, so after that, approving `plan.md` is the run's one interruption. It writes no code — the party that draws the contract is not the party that executes it, which is what gives the proofer's *compliance first* a document somebody else wrote to check against |
| **crafter** (Claude Code subagent) | `core`, `agent-contract` | Builds one phase of a work item against the frame, or runs one fix pass over a round record. It opens `implement` at its first step and `writing-style` before it writes a record, and hands back each claim labelled `executed`, `read` or `unverified`, with the full suite labelled `unverified` and its answerer named |
| **proofer** (subagent) | `core`, `agent-contract` | Reviews compliance first, then quality. It opens `code-review` at its first step and `writing-style` before it writes its round record. The orchestrator verifies the record before acting on it, and the pull request's check reads it — the reviewer never verifies its own report |
| **tracer** (subagent) | `core`, `agent-contract` | Records what the original code does as `path#anchor` coordinates and returns facts, not verdicts. It opens `legacy-parity` at its first step. Appears only in repos that declare `seal/parity.md` |
| **sealer** (subagent, Opus) | `core`, `agent-contract` | The final, independent guarantor. After the rounds settle, the changelog is written, the orchestrator has run the one broad gate (`seal gate`, which writes `trail/gate.md`), and `seal pr-body` has copied the records into the first part of the pull request body, it reads that record and runs nothing broad itself, confirms through `seal pr-body --check` that the copied part still matches the records, re-runs a sample of the implementer's claims, and reads the design, the build, the last review, the changelog and the part of the pull request body the orchestrator wrote against the issue and the tree. Its verdict is the work item's `guarantee.md`: `sealed`, `withheld` naming what the tree contradicts, or `undecided` with a question for the owner. It does not re-judge the design or the code's quality |
| Skills | — | The skill the agents follow from their first tool call is in the column to the left. These a session loads on its own when the work calls for them, and an agent opens each at the step that names it — `code-review`, `commit-pr-convention`, `confidence-check`, `feature-planner`, `implement`, `legacy-parity`, `settle`, `verify`, `writing-style`. The rest you invoke by name; they are in the cheat sheet below |
| Hooks | — | The gates themselves — auto-registered by the plugin, no settings wiring |
| Core | — | `skills/core/SKILL.md`, the values every party shares. Every agent preloads it through its definition's `skills:` list, and the plugin's `core-start` hook prints it into every session, so a session holds what every agent holds from its first message and nothing is written into your `CLAUDE.md`. It carries no response-language rule — that stays yours. `! seal core` shows which core a session holds; disabling the plugin's hooks turns it off, and the plugin's other hooks with it |

## The chain

```
crafter builds → verify (scoped) → proofer reviews → report to the user
      ↑                                                   │
      └──── rebuild ↔ re-review, rounds 1..n ─────────────┘
                          │ rounds settle
                          ▼
     orchestrator → broad gate — full suite, lint, typecheck, ONCE
                          │
        new breakage → back to the loop (three returns, then stop)
        failing on base too → named as a follow-up, does not block
        new? → not measured at the base; run it there before either
                          ▼
     sealer reads trail/gate.md → guarantee.md
                          ▼
                        PR / commit
edit    → on a branch no routing.md names, the edit hook refuses and names
          the ways on: write the declaration, or run seal no-work-item
```

**The broad checks run once, after the review rounds settle.** Evidence binds
to a tree state, so a full suite taken before the rounds is spent by the first
fix they cause — measured on one work item: twenty broad runs, every one
followed by more edits, none surviving to the handoff, and together more than
half the session's tool time. The crafter hands over with the suite
`unverified` and says so; narrowing the scope is honest only because the label
is not omitted. At the gate, the run is read against the base commit: a
failure that predates the work is named as a follow-up rather than chased, and
nothing edits between that run and the PR.

`verify` is the crafter's own gate before it hands anything over: run the
checks, read the full output, and label each claim as executed, read, or
unverified. The proofer audits that record rather than re-running it — did the
command run, can the check fail, is the label honest — which is not the same as
taking its conclusions. The code is still read.

**The proofer starts cold.** It runs as a subagent, so the implementation
conversation does not reach it — what carries over is what was written down:
the diff, the frame, and the work item's round records. The one way in is the prompt
that spawns it, so the proofer treats implementation rationale found there as
the author's account rather than evidence, and says in its report that it set
it aside. For a review with no path in at all, open a fresh session and call
`@agent-agentic:proofer` there: the round history is files, so it is inherited
either way.
The review run is bounded: three finding rounds by default, counted from the
last design change (a reframe, or a new phase you approved), and one more at
a time only while each round finds fewer findings than the one before and
none of them is a regression, a defect a fix pass's own commit introduced.
A regression sent to a fix pass gets one verifying round for that fix, and
it is not an extension. At the cap every
finding still open is handed on and reads `deferred <home>`, whether or not
everything was resolved. What is left is handed over rather than
carried — an unanswered finding to `seal/follow-up.md`, a decision only
you can make to `questions.md`, an original whose behavior is plainly wrong
recorded both ways — each named in the PR body. **The chain ends at a PR,
never at a merge.**
Stopping at a report leaves finished work where nobody will look for it;
merging decides something that was never the chain's to decide. Whether that
PR merges, gets another round, or gets closed is yours.

## Where the records live

Cross-session memory lives in the repo, not the session:

| Root | Lifetime | Holds |
|---|---|---|
| `seal/` | permanent | everything this plugin maintains — the follow-up list, the repository's own config (the two language rows and the mode live there), the migration config — and, beneath it, the work items. Its existence, with its `README.md` opening with the marker line `templates/setup/seal-README.md` starts with, is also what opts the repository in, for each hook whose Where column under *The gates* below names `seal/` |
| `seal/threads/<id>/` | one work item | `frame/` (design, plan, questions), `trail/` (phases, review rounds, the broad run), and at its top `routing.md`, `changelog.md`, `guarantee.md` and `gaps.md`, the closing memo holding only what the diff cannot show. A human approves `frame/plan.md`, which is why this is a repository document and not tool state |
| `docs/` | permanent | whatever policy documents the repository already keeps; the documentation convention is the project's. A work item states its rule changes in its design instead of editing them, and the settle after the release writes each section as the latest decision those changes state (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*) |

```
seal/
├── README.md         what the root holds, and where the export rules are
├── config.md         what this repository says about itself — two languages
│                     and the mode. Optional, and an absent row is not an
│                     error
├── parity.md         migration config, only when declared
├── pact.md           the pact, only in the repository that holds one
├── follow-up.md      schedulable items in a repository with no tracker
└── threads/<work-item-id>/
    ├── routing.md    which way this work item goes, written before the first edit
    ├── frame/design.md · frame/plan.md · frame/questions.md
    ├── trail/phases/phase-N.md   what one build phase was asked and found
    ├── trail/rounds/round-N.md   review rounds — committed, drained, then closed and kept
    ├── trail/gate.md             the one broad run, at a SHA, against the base
    ├── changelog.md              this work item's entry in the next release's notes
    ├── gaps.md                   the closing memo: what the diff cannot show
    └── guarantee.md              the sealer's verdict on the work, at a SHA
```

Judgment runs policy > SDD > code where a repository has policy documents, and
SDD > code where it does not. Most repositories are the second kind, and the
plugin does not manufacture the first.

Missing files bootstrap from `templates/`. The round records, the check at the
pull request and the handoff to an agent are specified in
[docs/the-review-record.md](./docs/the-review-record.md).

**A rule names the test that holds it.** A rule a policy document states ends
with a `check:` line naming the test files that hold it, or a marker its
tests carry, and CI running the suite is the check that the rule still
holds. `seal rules --check` reads every such line and exits non-zero on a target
that does not exist. A rule no test can hold says
`check: none reader: <who reads it>`, which leaves the gap where a reviewer
reads it. What this proves is narrow and worth
stating: that a named test exists and passes, not that it asserts the whole
rule. That half is the review's.

## The gates

Hooks are scripts the plugin auto-registers; they run on your machine at
tool events. One process handles all the gates on an event rather than one per
gate — four interpreter startups per Bash call was most of the cost of having
them (measured: 220ms → 104ms before a Bash call, 323ms → 120ms after). A gate
that fails to load or crashes is skipped and the call goes ahead; at the end of
the turn you are told which gate it was, once per session. Full decision
tables:
[docs/the-routing-check.md](./docs/the-routing-check.md) ·
[docs/the-review-and-parity-arms.md](./docs/the-review-and-parity-arms.md) ·
[docs/the-review-record.md](./docs/the-review-record.md).

| Gate | Fires | Does | Where |
|---|---|---|---|
| routing-edit-gate | before a `Write`, `Edit` or `NotebookEdit` call | refuses an edit when no `routing.md` declares the edited file's branch, unless this session ran `seal no-work-item` on that branch. It judges the file's repository and branch, wherever the shell sits. Files under `seal/`, files git ignores and files in no opted-in repository pass, so the declaration itself is always writable. The model gets the refusal with its two ways on — write the declaration, or run `seal no-work-item` — and under the `automation` press it names no question to put to you. Nothing of this plugin runs inside git, so a person's own commit from a terminal runs none of its code; at the pull request, `chain-check` fails a commit whose `Seal-Routing` trailer names a work item no declaration names | `seal/` at the root, or under the common git dir in local mode — silent elsewhere |
| core-start | at session start, after `/clear` and after a compaction, never on resume | prints the core, `skills/core/SKILL.md`, into the session as plain text, under a first line that names the printed file, the running plugin's version and that file's SHA-256. In a clone of this plugin's own repository it prints the clone's copy. A resumed session keeps what its start printed, which is why resume is left out. It writes nothing | every session, in any directory |
| stub-remove | at session start | removes the `pre-commit`, `reference-transaction` and `post-commit` stubs an earlier release wrote into the clone's common `hooks/` directory: only a file whose second line is the marker `# specseal-git-hook`. A hook somebody else wrote is left byte for byte. Says once what it removed, and nothing where there was nothing | any git repo |
| root-migrate | at session start | moves a layout an earlier release wrote into the current one: it rewrites `seal/README.md` to open with the marker line and moves each 0.22.x work item to `seal/threads/<id>/`, as staged `git mv` steps for you to review and commit, or as plain renames under the common git dir in local mode. It refuses the whole move over uncommitted changes under what it would move, and says in one line what moved. It also gives the plugin's name to the state files an earlier release wrote under its old name, beside the root and under `~/.claude/` | any git repo whose tree or common git dir still holds an earlier layout; the state rename runs at every session start, silently |
| implementer-mark | before an Agent/Task call whose `subagent_type` is `framer` or `crafter` (`agentic:crafter`, or a project-local `crafter`) | writes the checked-out branch name to `.git/agentic-planner` or `.git/agentic-implementer`, one file per axis. It prints nothing, so it can neither deny nor ask; it is the trace the notice below reads | `seal/` at the root, or under the common git dir in local mode — silent elsewhere, and writes nothing |
| implementer-notice | after a command that actually runs `git commit` | where this branch's `routing.md` answers `Planning` with `framer` or `Implementation` with `crafter` and no mark of that axis stands for this branch, prints one line naming the file — **one line for both axes**, never one each. Nothing is said for an axis whose mark stands, whose row is absent or unreadable, or which answers `the session`. **Once per session per repository**, and it never blocks — a declared agent nobody spawned is a session forgetting its own answer, and a reminder is what that costs | `seal/` at the root, or under the common git dir in local mode — silent elsewhere |
| review-skill-gate | before the model opens a skill named `code-review` | puts the choice to you rather than making it: that name is Claude Code's built-in, not this plugin's. The built-in sweeps the diff for bugs and cleanup; `agentic:code-review` judges compliance first and inherits earlier rounds' verdicts. Fires **once per session per working tree**, so picking the built-in and retrying goes straight through. A skill you invoke yourself never routes through here | `seal/` at the root, or under the common git dir in local mode — silent elsewhere |
| question-gate | before an `AskUserQuestion` call | on a branch whose `routing.md` answers `Automation` with `yes`, refuses the question to the model on every call, so a run you routed `automation` does not stop to ask you. The model builds on the default the question states, writes it as a row of the work item's `questions.md`, and names it in the pull request body for you to overturn. The routing question put alone goes through until the session has answered it, so a resumed run can put it again once. A question another gate tells the model to put states no default, so the model takes none of its ways on and hands that stop back at the end of the run. A session sitting in a checkout of another branch is not held, and neither is a question asked as plain text | `seal/` at the root, or under the common git dir in local mode — silent elsewhere, and on every branch whose declaration does not answer `yes` |
| mode-gate | before a Bash call, so in practice the session's first one | names a root nobody chose a mode for: `seal/` exists and `seal/config.md` carries no `Mode` row, so nothing records whether this repository's review records travel with it or stay on this machine — and a root somebody chose is byte-identical to one that appeared because a session followed the routing rule. Denies once with the three ways on as options — `seal mode` records where the folder already is and moves nothing, `seal mode shared` / `seal mode local` move it — then the plain confirmation, where approving proceeds and records nothing. **Once per session per repository**, and nothing at all once the row exists. The repository judged is the one the SESSION sits in, not one a `-C` names: this is a fact about the workspace, not a verdict about a change | `seal/` at the root, or under the common git dir in local mode — silent elsewhere, and silent wherever the row is written. There is no waiver token: the way on is one command |
| version-check | at session start | asks this repository for its newest release tag and, when the running plugin is behind, shows a short notice naming `/agentic:update` and the two moves that load a release. Once a day, and a lookup that fails retries about twenty minutes later. It never installs anything — telling you a release exists and installing it are different acts | `seal/` at the root, or under the common git dir in local mode — silent elsewhere |
| sealer-stamp | when the main session's turn ends (`Stop`) | draws, once and after the turn's text, each stamp waiting for this session under `<git-common-dir>/agentic-stamp/<session>/` — queued at the write of a work item's `guarantee.md` reading `sealed` (the next row), once per work item — and renames the file `.drawn.json`. Nothing at a subagent's end, for another session's file, or under a `python3` older than 3.12; `seal stamp --from <file>` draws one by hand | `seal/` at the root, or under the common git dir in local mode — silent elsewhere |
| sealer-stamp-queue | after a Write or Edit of a work item's `guarantee.md` | in either mode, queues the work item's stamp for the main session's `Stop` when the write leaves `guarantee.md` reading `sealed` over a commit on the branch its `routing.md` names, once per work item, and prints the line naming the queued file and `seal stamp --from`; where that branch does not hold the commit, it queues nothing, records the refusal and says so in one line. Any other edit is passed over on its path alone, before anything is loaded or any `git` runs | `seal/` at the root, or under the common git dir in local mode — silent elsewhere |
| lint-python | after Write/Edit/NotebookEdit on a `.py` file | runs `ruff check --fix` then `ruff format` on that file — autofixes included, so code changes, not just layout (uv → uvx → global ruff; skips silently if none) | **a project that configures ruff** — `ruff.toml`, `.ruff.toml`, or `[tool.ruff]` in `pyproject.toml`, searched up to the repo root. Silent everywhere else |

No hook of this plugin stops a session from switching the branch of a
working tree another session is using; give each concurrent session its own
worktree.

A work item writes `seal/threads/<id>/routing.md` before its first edit — which
way it goes, and whether it opens a pull request — and the routing edit gate
refuses an edit on a branch no declaration names, so the route is chosen
before the work rather than guessed after it. The review itself is checked at
the pull request: CI reads the same file out of the diff and, for anything
routed through the chain, requires a committed round record with no finding
left unanswered. A pull request that declared neither way is judged by its
commits' `Seal-Routing` trailers alone
([docs/the-routing-check.md](./docs/the-routing-check.md)), and a notice says
nothing else was checked.

A round's findings are closed after it ends, by whoever writes the
fixes, and the round that follows is what reads them — except after the last
round, where nobody did. So a run ends with a **verifying round**:
spawned after those fixes are committed, pointed at their diff rather than at
the branch, and asking of each finding marked closed whether its fix holds. A round
that opens nothing needing a fix does not spend one of the three.

A ready pull request fails while a commit outside the work item's records
follows the commit on the last record's `target:` line, or while a finding of
that record reads `fixed` or `rejected` — a review cannot have passed while
the fixes that closed its findings went unread. On a draft it prints and
names the verifying round.

No gate transmits your code, your paths, or your prompts anywhere. These side
effects are worth stating outright: version-check writes a timestamp file
under `~/.claude/agentic/`, the write of a `guarantee.md` reading `sealed`
writes the stamp's values under
`<git-common-dir>/agentic-stamp/`, which the stamp hook renames once drawn
and nothing prunes, and a `sealed` refused because its audited commit is not
on the work item's branch leaves an empty file under
`<git-common-dir>/agentic-stamp-refused/`, written by the edit hook in
either mode, which nothing prunes either,
and lint-python rewrites the `.py` file you just saved — in
ruff-configured projects only.

lint-python and version-check reach the network. lint-python falls back to
`uvx ruff`, and uv fetches ruff from PyPI on first use. version-check runs
one `git ls-remote --tags` against this repository, once a day where `seal/`
exists. A lookup that fails retries about twenty minutes later rather than
waiting out the day. What that tells GitHub is that a machine somewhere runs
AgenticSeal. Each stays silent when the network is unavailable.

## Honoring the original (migrations)

A repo that declares `seal/parity.md` (original repo, baseline commit) gets
three-way judgment — policy ↔ original ↔ new, with *preserve the original*
as the fallback — and the tracer fetches the original's facts. Repos without
the config never see any of it.

You do not write that file by hand. Your session asks once, the first time it
sets up a repo's layout: *does this project port behavior from an existing
codebase?* Answer no and it never asks again. Answer yes and it proposes
candidates for the original — sibling checkouts, an upstream in `git remote
-v`, repos whose paths overlap — reads the baseline from whichever you
confirm, and writes the file. Deciding later is `/agentic:parity-setup`.

Your checkout path stays out of the committed file, in
`~/.claude/agentic/parity-paths.md` keyed by the origin remote, since it is
wrong for every other machine.

## Cheat sheet

**Runs by itself (the gates above — nothing to invoke).**

**Run it yourself:**

| Command | Does |
|---|---|
| `seal deferrals . [--kind all]` | resolve the answerer an `unverified` row names — does anything here actually run the check you are deferring? Separates *answers on pull requests* from *answers too late*, *trigger unread, not counted*, *local hook only*, and *nothing* |
| `seal unverified . [--baseline <ref>]` | read the rows those `unverified` labels left behind — what is still open, in which work item, and who was named to answer it. Fails on a section it cannot read, because a tolerant reader reports zero and zero reads as *all closed*. With `--baseline`, it compares counts against `git merge-base <ref> HEAD`: the point where this branch forked from that ref on a branch checkout, and the base's tip in CI, which checks a pull request out already merged into the base. Either way a work item that landed on the base afterwards is not this branch's removal. A table with fewer rows than at that commit fails, as does a `gaps.md` that was there and is gone. Replacing one row with another keeps the count and passes |
| `seal cost --latest` | where a session's minutes went — command time, model time between calls, checks re-run for a result already produced, and how many tools went out per turn — numbers nothing inside a session can measure |
| `seal cost --segments <transcript>` | one row per agent the run spawned, read from that agent's own transcript: its span, calls, tools per turn, mean gap, tokens, and the context its largest turn read. That span is in no other column — where a harness writes a spawn's result on acceptance, the `--spawns` table reads seconds for an agent that ran twenty minutes. A resumed agent is one row per stretch of work, so no span covers the wait between two of them — whether the command is given the run's transcript or that agent's own — and a segment that spawned an agent of its own prints a line saying so. Under the table it names each row whose tools per turn sit under its kind's bar — a proofer's or a framer's; a crafter's edit-test loop is exempt — and counts the rows it could not grade |
| `seal settle [--apply]` | the dry run: the `## Rule changes` the released designs state, grouped by the section each names and in merge order, with whether each `from` and `to` is in that section now; the designs to read whole; every open row of every released record; and what `--apply` removes. It refuses nothing. The session running the settle then writes the sections and decides the open rows, asking nobody (`skills/settle/SKILL.md` *The settling session's procedure*). `--apply` writes no document: it removes each released directory whose record holds no open row, with a `frame/design.md` or without, and names any it keeps |
| `seal fold [--ceiling <n>]` | checks the top level of the policy root for one read and the index, as `skills/settle/scripts/fold_check.py` and its rows in `templates/setup/config.md` *The fold's values* state them. The flag replaces its row for one run |
| `seal rules <doc> [--root <dir>]` · `seal rules --check [--root <dir>]` | `seal rules <doc>` prints each heading of a document and, under it, the targets of its `check:` lines, each with the first sentence of its test's docstring, or why the target does not resolve. A rule's text lives once, in that docstring, so this is how a document and its tests read side by side, and it exits 0 whatever it finds. `seal rules --check` reads every check line in every rule file and exits 1 naming each one out of grammar or naming a target that is gone, by file, line and heading. Such a line inside a section an unsettled design's `remove` with no `from` takes out at the settle is printed as excused, naming that work item, and does not fail the check; a pending `change` excuses nothing, and where the `seal/` root is local no line is excused. One case of the suite runs it over the tree. The targets resolve in the repository the command is typed in, and neither form writes anything |
| `seal pact [ROOT]` | run at the repository holding a pact (`seal/pact.md`), the one copy of a contract several repositories keep together: reads every signer the pact lists, found through `~/.claude/agentic/pact-paths.md` or a sibling checkout, checks that each names the pact in its `Pact` row, and grades every pact anchor it cites. `SUPERSEDED` says the signer was built against an older clause, `NOT TAKEN` names the branch holding a change the pact has not taken, `UNMATCHED` and `BROKEN` say read both sides or re-coordinate. Local only: a signer's CI can read one repository, so it reads nothing of the pact |
| `seal core [--transcript <path>]` | whether this session's context holds the core, `skills/core/SKILL.md`, once and whole, read from the session's transcript: exit 0 where one `SessionStart` hook entry in context holds the file its first line names, 1 with the reason otherwise. The core arrives from the plugin's `SessionStart` hook and not from a `CLAUDE.md` file, so `/memory` does not list it; type `! seal core` in a session to see which core it holds. Run from an agent's Bash, it reads the session that spawned the agent |
| `seal payload [--calibrate <main transcript>] [--baseline <run.json>]` | what a session's and each agent's startup payload is made of, in bytes, chars and tokens. A session's table comes first: the two `CLAUDE.md` files with each file their `@` lines import, and the core the plugin's `SessionStart` hook prints, which reaches no agent. Then each agent's: its definition, every skill its `skills:` list injects, and the same `CLAUDE.md` pair. Every token figure carries a basis: `measured` where it came from a transcript's spawns, `estimated` from a per-agent ratio otherwise, and always `estimated` for the session, whose prefix no transcript calibrates. `--baseline` prints the delta against an earlier `--json` run, which is how a trimmed payload is shown to have shrunk |
| `/agentic:parity-setup` | declare that this repo ports from another codebase — finds the original, records the baseline |
| `/agentic:config` | show what this repository decided for itself — the two languages it writes in and where its records live — and change any of it. Routes a change to whatever owns that row rather than editing behind it |
| `/agentic:update` | take the newest release and see what is in it — runs both update commands in the right order, then names the changelog entries between your version and the new one. It also names both ways to load it and how far each one was actually measured |

**Inline switches:**

| Switch | Effect |
|---|---|
| `seal no-work-item` | marks this session, on the branch checked out where it runs, as doing work outside any work item, so the edit hook lets it edit on that branch and on no other; on a detached HEAD it marks nothing. Where the root is shared, each commit it then makes ends with the trailer `Seal-Routing: no work item`, and the pull request's check prints those commits (`skills/commit-pr-convention/SKILL.md`) |

## Install

**Requirements**: `git`, and **Python 3.12 or newer** resolving as `python3`
on PATH — the gates are Python scripts, and `python3` is the command the
plugin invokes them with. Worth checking rather than assuming: macOS ships
3.9 as `/usr/bin/python3`, and a version manager (pyenv, asdf) resolves
`python3` to whatever it was last told. `python3 -V` is the whole test. On
Windows that name is the one the official installer does not create, so each
hook falls back to `py -3` when `python3` cannot start. Optional: `uv`/`uvx` or `ruff`
for the Python auto-format hook — without them it silently skips.

```bash
# The plugin: agents, skills, gates and the core
claude
> /plugin marketplace add MichaelYcJo/AgenticSeal
> /plugin install agentic@agenticseal
```

That is the whole install. The core reaches every session from the
plugin's `SessionStart` hook and every agent through its `skills:` list, so
nothing is written into a `CLAUDE.md`. An earlier release wrote a
CLAUDE.md block between `<!-- agentic:start -->` and `<!-- agentic:end -->`;
`/agentic:update` takes it out (*Updating*). To uninstall, run
`/plugin uninstall agentic`, and delete such a block yourself, its markers
and the lines between them, where no update has taken it out.

### Coming from `specseal@specseal`

The plugin was installed as `specseal@specseal` before it was renamed.
Claude Code knows a marketplace by its name, and its reference does not say
what a registration does when the catalog it points at changes its own name,
so register the marketplace again under the new one:

```bash
claude plugin marketplace remove specseal
claude plugin marketplace add MichaelYcJo/AgenticSeal
claude plugin install agentic@agenticseal
```

The first line also uninstalls `specseal@specseal` and deletes its cache
(`code.claude.com/docs/en/plugins/cli-reference.md` *plugin marketplace
remove*). The CLAUDE.md block the old install wrote, between
`<!-- specseal:start -->` and `<!-- specseal:end -->`, carries nothing the
new install needs: `/agentic:update` takes it out at the next release, or
you delete its markers and the lines between them. The update
command of the old install runs the old names, so it cannot carry you
across. These three lines are read from the Claude Code reference and have
not been run on a machine that holds the old install.

In a repository where `seal pr-checks install` wrote
`.github/workflows/hygiene.yml` before the rename, run `seal pr-checks
install` again once the session start has moved the records, and commit the
rewritten workflow together with the move. The old workflow clones the
release it was pinned to, which looks for work items where that release
kept them and for the old trailer, so after the move it finds no declaration and
passes every pull request without examining any. The session start's line
says so where it finds that workflow.

### Updating

```
/agentic:update
```

It runs both commands below in the right order and then names the changelog
entries between your version and the new one, calling out anything that
changes behavior or needs you to do something. The session you are in keeps
the version it started with either way, so nothing is half-applied.

Then load it. `/reload-plugins` re-reads the preloaded skill bodies a spawned
agent is handed, out of the copy your session is already on — that is what
`docs/experiments/2026-09-03-skill-preload-and-the-copy-in-force.md` measured,
and it is the whole of it. Nobody has measured whether a reload reaches hooks,
agent definitions, or the newly installed version at all, so restart when you
want the update loaded for certain.

By hand:

```bash
claude plugin marketplace update agenticseal
claude plugin update agentic@agenticseal   # then load it — see above
```

Both lines, in that order. The first refreshes the marketplace clone; the
second installs from it. Running only the second reports *already at the
latest version* against whatever the clone last knew. Updates are keyed to the
version in `plugin.json`, not to commits — a change that ships without a
version bump reaches nobody.

`/agentic:update` also takes out the CLAUDE.md block an earlier release
wrote: it backs your `CLAUDE.md` up to `CLAUDE.md.bak`, removes the block's
markers and the lines between them, and never edits your own content. The
update that brings this step in runs the earlier release's procedure, which
copies the block from `templates/setup/claude-md-block.md`; that template
holds its two markers and nothing between them, so the update leaves an
empty marker pair, and the next update removes it.

### Coming up from 0.3.x

0.3.x kept the plugin's files in two directories (`.specseal/`, `specs/<id>/`);
every release since keeps them in one, `seal/`. The old pair opts nothing in,
so every gate is silent in a repository that still holds it. No code of the
plugin opens either directory, so you move them by hand with the commands
below, and this is the only path.

Move only the plugin's own work items out of `specs/`: a directory named
`<unix-seconds>-<slug>` where git tracks a `routing.md`, or a file in a
`rounds` directory directly under it. Every 0.3.x work item carried `routing.md`.
Anything else under `specs/` is the project's own, whatever its name, and
stays where it is.

The README the second command moves is then overwritten from
`templates/setup/seal-README.md`, because that file's first line is the marker every
gate reads before it treats `seal/` as the plugin's root. Where
`.specseal/scratch` marked the repository as throwaway, delete it instead of
moving it: its successor is the file `.git/agentic-scratch`, which cannot be
committed.

```bash
# exempt from old_names: the 0.22.x layout, which the plugin then moves into seal/threads/
mkdir -p seal/specs
git mv .specseal/README.md seal/README.md    # then overwrite it from templates/setup/seal-README.md
git mv .specseal/* seal/                     # follow-up.md, parity.md and anything else in there
# exempt from old_names: the 0.22.x layout, which the plugin then moves into seal/threads/
git mv specs/<id> seal/specs/<id>            # each work item
rmdir .specseal specs                        # git mv leaves them empty on disk; one holding something else stays
```

Then review `git diff --cached` and commit. That commit belongs to no work
item, so a session making it in shared mode ends it with the trailer
`Seal-Routing: no work item`. The plugin then moves each work item into
`seal/threads/<id>/` the way it moves a repository installed before the
rename, as staged `git mv` for you to review and commit the same way.

## First run

Each gate acts only where the Where column of the gate table above says.
A gate whose Where column names `seal/` acts in a repo that has a `seal/`
directory at its root or under its git directory, whose `README.md` opens
with the plugin's marker line, and stays silent everywhere else. You never
create it by hand — your session builds
it the first time it works in a repo, after asking one question (*Shared or
local*, below), and it is the only directory this plugin adds to your tree —
plus, where you choose the pull-request checks, one workflow file under
`.github/workflows/`; in local mode, nothing at all.

lint-python acts only where the project has configured ruff — configuring
ruff is a project saying it wants ruff, and nothing else is.
Read the Where column above before installing globally.

Agents run only when you name one:

```
> @agent-agentic:crafter implement <your ticket>
```

`@agent-` opens a picker that completes the name for you. Spelling it out in
prose works the same way, if you prefer it:

```
> use the agentic:crafter agent to implement <your ticket>
```

The crafter reads the policy, the design and the plan, implements, verifies,
and hands off to the proofer for review — you decide what happens to the
report. Anything the
layout needs and the repo lacks (`seal/README.md` among them)
your session creates from `templates/` as it goes.

Two things work with no agent at all: `seal fold` and every gate in the
table.

### Shared or local

The first time your session works in a repository it asks one question, once,
and never again: where `seal/` lives, and whether CI checks pull requests
against it. Whichever place holds the folder is the mode; there is no config
key, and a repository with `seal/` at either place is not asked.

| | Shared, records only (the default) | Shared, with pull-request checks | Local |
|---|---|---|---|
| Where `seal/` lives | `<repo>/seal/`, committed | `<repo>/seal/`, committed | `$(git rev-parse --git-common-dir)/seal/` — under the common git dir, which is `.git/` in a main tree |
| What setup installs | nothing under `.github/` | the pull-request checks, `.github/workflows/hygiene.yml` written from the plugin's `templates/setup/hygiene.yml` only if no file is there | nothing; the tree is untouched |
| Fits | your own repository, or one where a committed `seal/` bothers nobody | a repository where every pull request should be checked against the records | a repository whose tree must not carry this plugin's files: a company repository, a contribution to someone else's project |
| Gives up | CI's checks, until you add them later | nothing | CI — the checks read committed files — and every other machine or re-clone, which starts empty |

Local mode sits under the git directory rather than behind a `.gitignore`
line because a linked worktree checks out committed files only, so an ignored
folder is simply absent there. The common git dir is shared by every worktree
of the clone, and nothing under it is ever a commit candidate.

**Switching is one command.** It stages; you commit.

```bash
seal mode            # where the root is, what the config says, whether they agree
seal mode local      # move it out of the tree
seal mode shared     # move it into the tree
```

The move itself is two shell lines, printed further down. What the command
adds is everything around them: it refuses when the other mode's root is
already there, refuses over a submodule under the root, refuses when the
index carries a change under `seal/` — `git rm -r --cached` takes a staged
edit out of the index without a word about it — and writes the mode into
`seal/config.md` so the file and the folder agree afterwards. It moves the
root and nothing else: `.github/` is left as it was. The hooks need no
restart: the next command reads the folder where it is.

**The pull-request checks are a command of their own**, whichever answer
first setup was given:

```bash
seal pr-checks           # whether .github/workflows/hygiene.yml is this plugin's, and the release it pins
seal pr-checks install   # write it pinned to the release you run, and stage it
seal pr-checks remove    # take out the file this plugin wrote
```

`install` refuses where `seal/` is not in the tree, because the checks read
committed records, and it never overwrites a file it did not write. Every
step of the workflow passes a pull request that declares nothing, so a
teammate who never used the plugin is not stopped by it. The file keeps the
release it names until you edit its `--branch` line, or remove it and
install it again. No config row says whether the checks are installed; the
file is the record.

**The row says what you want; the folder says what you have.** Nothing at
runtime reads the row — every gate finds the root by looking for it, in the
two places above — so the two can disagree, and that is the input the command
consumes rather than an error:

```bash
# edit seal/config.md to say `| Mode | local |`, then
seal mode --apply    # move the folder to what the row says
seal mode --check    # writes nothing; exits non-zero if they disagree
```

`--check` is what the pull-request checks run, so a row that stops being true
is caught rather than left standing. A repository that has never declared one
is not lying about anything: the first `seal mode` writes the row from where
the folder actually is.

**The two directions do not cost the same.** Going to local takes the records
out of the tree, and every other clone loses them at the next pull — `seal
export` here and `seal import` there is how a teammate gets a copy. Going to
shared is the one to be sure about, because the commit puts the records into
the history for good. How to walk the switch back before that commit, and
why it works, is `skills/config/SKILL.md` *Before switching to shared, say
what cannot be undone*.

By hand it is a move and a commit, from the repository root — both paths are
asked of git, so a subdirectory as the working directory lands them in the
same place:

```bash
# local → shared, then commit
mv "$(git rev-parse --git-common-dir)/seal" "$(git rev-parse --show-toplevel)/seal" && git add "$(git rev-parse --show-toplevel)/seal"
# shared → local, then commit the removal
git rm -r --cached "$(git rev-parse --show-toplevel)/seal" && mv "$(git rev-parse --show-toplevel)/seal" "$(git rev-parse --git-common-dir)/seal"
```

Doing it that way leaves `.github/` alone, as `seal mode` does. A workflow
left behind after a move to local stays in the tree, and
`docs/one-root-by-lifetime.md` *Shared or local* says which pin passes there
and how to move one that fails.

Between two machines the move is not available, because the other machine has
no folder to move. That is what `seal export` and `seal import` below are for,
and they are the second way to switch modes as well.

### Carrying local records to another machine

Local mode's trade-off is that the records never leave the clone. `seal
export` and `seal import` make that *take a copy* rather than *lose it*.
Both ship on the Bash tool's PATH while the plugin is enabled.

```bash
seal export                 # writes seal-<repo>-<date>.zip beside the clone
seal import <the zip>       # takes one in, overwriting nothing
```

The zip holds the root and nothing else. The implementer marks and the
`seal no-work-item` records sit *beside* the root under the git directory,
so none of them travels — the export walks the root, which is why the root
has to be its own directory. A symbolic link inside it
is skipped and named rather than followed. Alongside the files goes a
manifest naming the remote URL and the HEAD SHA at export. A field git could
not answer is **left out** rather than written empty, so the machine taking
the zip in can tell *this repository has no remote* from *nobody could say*.
The export names each field it left out and why, because the machine that
ran it is the only one that can clear the failure by running it again.

**Import never overwrites and never asks.** A file that is not there is
added. One that is there with the same bytes is left alone, so re-importing
the same zip writes nothing. One that is there with different bytes gets the
incoming copy beside it — `follow-up.incoming.md` next to `follow-up.md` —
and the collision is listed. Which of a pair is
right is a reading, not a merge, and no answer the command could pick would
avoid sometimes throwing work away.

It refuses, writing nothing, when the zip came from another repository
(`--allow-other-repo` if the two are one repository under two spellings),
when the remote could not be read on either side and so that question cannot
be answered at all (`--allow-unreadable-remote` to import without the check —
a separate flag, because *there is no remote* and *nobody could say* are
different facts),
when the manifest declares a format this build does not read,
when a member would land outside the root, when a member or the whole zip
declares more bytes or more members than a root of records holds, when a
member cannot be read — a bad checksum, encryption, a compression method this
build has no decompressor for — when a name has to be a directory for the zip
and is a file, and when both roots already exist.

Which side went silent decides what the unreadable-remote refusal tells you
to do next. A git that failed *here* may answer on the next run, so running
the import again is the first thing to try. A zip that records no remote
reads the same every time, and no re-run there can change it — that one is
exported again on the machine that wrote it, which is also the machine whose
export said which field it had to leave out. When both went silent at once
the zip decides, because no re-run here clears that side whatever this
clone's git answers next.

Those all stop before the first byte. One failure cannot: if a directory in
the root cannot be written into, or the disk fills, the copy stops part-way
and says what the filesystem said. Fix that and run it again — nothing is
overwritten, so a second run finishes the copy and reports what was already
there byte for byte.

A symbolic link at a name a collision would fall back to is treated as taken:
the copy lands at the next free name rather than being written through it.
`seal export` does the same with the zip's own name. If anything is already
at the temporary name it writes through, it refuses and leaves that alone —
it removes a half-written archive of its own, never a file it found there.
`seal import --into shared` or `--into local` creates the named mode's root,
which is the other way to switch modes: export, import into the other place,
commit or remove.

In shared mode `seal export` writes no zip. The records are committed, so
every clone and CI already have them, and it prints the path and the `mv`
that switches to local mode instead. Once per release, `seal export --check`
prints one line — how many work items changed since the last export — and
uploads nothing anywhere. Where the copy goes is nobody's business but yours.

## Limits

What this does not do is as load-bearing as what it does.

- **The gates put the decision to you or to the model; they do not block.**
  The edit hook refuses an edit on an undeclared branch and names the ways
  on, and `seal no-work-item` is one command any session can run; what it
  leaves, where the root is shared, is the `no work item` trailer on each
  commit, which the pull request's check prints. It is a record for a
  session about to edit unrouted work, not a security control — an edit
  made through the shell never reaches it, and a person's own commit is
  never judged.
- **`seal rules --check` proves a named test exists, not that it asserts the rule.**
  A target that resolves while the test checks something else reads clean,
  and a rule written as `check: none reader: <who>` is held by its reader
  alone.
- **"Broad and once" is a rule the agents follow, not a gate.** Nothing stops
  a session from running the full suite mid-round; what exists is the
  instruction, the proofer's audit of the crafter's labels, and `trail/gate.md`, which
  makes a repeat visible. A hook could not tell the difference anyway —
  whether the rounds have settled is not a property of the command being run.
- **Unread last fixes fail in one place.** A commit after the last record's
  `target:` commit fails a ready pull request; on a draft it prints and names the
  verifying round, and *Ready for review* re-runs the check. The way out costs
  no round — one verifying round at the diff of those fixes.
- **An `original:` line says someone compared, not that they compared well.**
  The pull request's check reads that a comparison was recorded, in each
  round record or in the sealer's guarantee. The quality of that comparison
  is whoever wrote the line's, and a line written where nobody compared turns
  "nobody checked" into "someone checked and it was fine".
- **Windows was run on real hardware once, and one defect is still open
  there.** Until 2026-08-26 this section claimed the `windows-latest` suite
  passed; it did not — 72 cases failed, were filed as an issue, and were fixed since on
  a native Windows 11 tree. The entry point was measured on the same machine:
  the `hooks/hooks.json` command line, run through `cmd.exe` against an
  opted-in repository, returned a `deny` and then an `ask`. `python3`
  resolved, so the `py -3` fallback is still unrun on Windows — it was
  verified on POSIX by removing the first name from PATH. The console-encoding
  defect that stood beside it is closed: a plain `pytest tests/` on
  a Korean cp949 console passes whole, with no `PYTHONUTF8=1`.
- **The behaviour evals run on the owner's account, not in CI.**
  `evals/behaviour/` holds the cases each agent's rewrite is proved on with
  `claude plugin eval`; CI checks their shape, and a rewrite's record says
  what its runs found.

## Contributing

**Base your pull request on the open `release/vX.Y.Z` branch, not on `main`.**
Work collects on one release branch here and `main` moves once per release, so
GitHub's default base is the wrong one for everything except a release. A
contribution aimed at `main` that touches what the plugin ships is refused by
CI for leaving the version alone, and the base is the cause rather than the
version. One that touches nothing shipped is not refused at all, which is why
the rule is the branch rather than the check.

Changes to a gate carry a higher bar than the rest of the tree, because a gate
decides whether someone's commit proceeds: a test seen failing before the fix,
a stated failure direction, and honesty about platforms you could not test.

[CONTRIBUTING.md](./CONTRIBUTING.md) *Opening a pull request* holds the rest,
including the half nobody can infer — what a contribution is **not** asked
for. None of this repository's own workflow applies to one: no work item, no
review round record, no changelog fragment, no version bump.

## Language policy

Functional files (skills, agents, hooks, commands) are English-only — they
load into model context, and a translated mirror would drift. Korean exists
for human-facing docs only (this README). One deliberate exception: the
writing-style skill carries per-language prose rules (Korean and English
sections) — independent norms, not mirrors, so the drift argument does not
apply. Response language follows the user's own CLAUDE.md settings — the
distributed block does not impose one.

## License

MIT
