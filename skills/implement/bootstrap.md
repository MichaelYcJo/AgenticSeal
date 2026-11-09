# implement, the bootstrap

This file is the orchestrator's, read before the first edit only where no
`seal/` root carrying the marker stands yet, neither at `<repo>/seal/` nor at
`$(git rev-parse --git-common-dir)/seal/`. It creates the root, asks where it
lands and whether the project ports an original, and then the orchestrator
goes back to `skills/implement/orchestration.md` for the routing question.

## Orchestrator: Bootstrap

When a root or file this skill needs does not exist, the orchestrator creates
it from `templates/` in this plugin and continues. In particular:

- `seal/README.md`, which says what the root holds and names the section of
  `skills/implement/SKILL.md` that states the export rules. Its first line
  is the marker the gates read, so the file is copied from
  `templates/setup/seal-README.md` as it stands.
- **Not** policy documents. A repository that has none has none; judge from
  the SDD set and the code. Creating `docs/policies/<domain>/` imposes one
  project's documentation habit, and one field's vocabulary, on every
  repository this plugin touches.

**When no `seal/` whose `README.md` opens with the marker exists at either
place, the orchestrator asks once, in the one call step 1 states, before
creating anything, then does two more things before continuing.**
Creating the root is what opts the repository in: from the next command on,
the `seal` commands and the pull request's check read it. Where the root
lands, committed with the repository or under the git directory on this
machine only, is the person's decision and not the orchestrator's. Nobody
reads a README to discover a question they did not know to ask, so this is
the only place the mode, and whether the project ports an original
codebase, are asked at all. Before it asks, the orchestrator runs
`seal mode`: with no root at either place, the command exits 1 and prints
the shared place and the local place, both from `lib/optin.py#home_paths`.
A shared answer creates the root at the shared place it printed.

**A `<repo>/seal/` whose `README.md` does not open with the marker is the
project's own.** The marker is the first line of
`templates/setup/seal-README.md`, and a package or a tool can keep a directory
named `seal` for itself. The orchestrator writes nothing into it. Beside it,
the shared place `seal mode` prints is the second name `skills/core/SKILL.md`
gives the root, and the three options are offered with that place. Where a
directory whose `README.md` does not open with the marker stands at that
printed place too, it is the project's own as well. The orchestrator writes
nothing into it either and offers neither shared option. The root goes under
the git directory, at `$(git rev-parse --git-common-dir)/seal/`, as the
local option below creates it, and the orchestrator says so in one line:
*"`<the shared place>` is this project's own, so the plugin keeps its root
under the git directory, in local mode"*. The one call of step 1 then
carries the `Broad gate` question and the two language questions.

1. The orchestrator asks once, with one `AskUserQuestion` carrying **four
   questions**: the mode, the `Broad gate` key, `Commit and pull request
   language` and `Record language`. The mode's three options come first, in
   this order:

   - **shared, records only** (the default, listed first) creates
     `<repo>/seal/` in the tree, at the shared place `seal mode` prints; the
     routing commit made before the first edit carries it. It writes
     nothing under `.github/`, so nothing it installs can stop a teammate's
     pull request.
   - **shared, with pull-request checks** does the same, and then the
     orchestrator installs the checks with `seal pr-checks install`, run
     after `seal mode` below. That command writes
     `.github/workflows/hygiene.yml` from `templates/setup/hygiene.yml` only when
     that path is absent, pinned to the release of the installed plugin, and
     stages it, so the routing commit carries it too. An existing file is
     never overwritten, and the orchestrator relays the line the command
     prints when it leaves one alone.
   - **local** creates `$(git rev-parse --git-common-dir)/seal/`, installs
     nothing, and touches nothing in the tree. The path is spelled through
     the common git directory rather than through `.git`, which is a file in
     a linked worktree; the root lands beside the stamp's queue, shared by
     every worktree of the clone, never a commit candidate, with no
     `.gitignore` line. The orchestrator says what it gives up: the pull-request checks
     read committed files, so CI cannot run them, and a new machine or a
     re-clone starts empty.

   Whichever the answer, the mode is the place: the commands read
   `<repo>/seal/` and then the common git directory, and a repository with
   both is shared.

   **The answer is not a door that shuts.** `seal mode` reports where the
   root is, and `seal mode local` or `seal mode shared` moves it, writing the
   mode into `seal/config.json` on the way and leaving `.github/` alone.
   `seal pr-checks` reports whether the checks are installed, and
   `seal pr-checks install` and `seal pr-checks remove` put them in and take
   them out. The orchestrator says so in one line when it creates the root,
   because the question is asked once and the person answering it does not
   yet know what they will want.

   **The second question is the `Broad gate` key, and it is a proposal
   rather than a blank.** That key is the one value in this flow only a
   person can write (`templates/setup/config.md` *Broad gate* says why it has no
   default). Unasked, it reaches the person as the gate's refusal after the
   review rounds have settled. A repository being opted in may not yet know
   its broad command, so **what the machine can derive is offered, the
   person picks, and nothing is guessed.**

   Read candidates off the repository, in this order, and offer each with
   the file it came from:

   | Where to look | What to take |
   |---|---|
   | `.github/workflows/*.yml` | the `run:` steps of whatever job gates a pull request. What CI already refuses a merge for is the repository's own answer, written down before anybody asked |
   | a runner under `bin/` | `bin/test`, `bin/check`, or whatever the contribution guide names first |
   | a package manifest | `package.json`'s `scripts.test`, a `pyproject.toml` tool section, `Cargo.toml` |
   | a `Makefile` | a `test`, `check` or `lint` target |

   Offer each candidate as **one shell command line** composed the way
   `templates/setup/config.md` *The criterion for choosing a value* says to compose
   one, and name the file it came from: a candidate whose source is named is
   one the person can correct. Where nothing is findable, say so rather than
   inventing one: a guessed command is what `templates/setup/config.md`
   *Broad gate* argues against by name.

   **A candidate carrying a `"` or a `\` is written with it escaped, `\"`
   or `\\`**, because the key's value is a JSON string, and a CI `run:`
   step is where one is likeliest to come from. Offer it that way rather
   than dropping the character or moving to the next candidate. Say why: a
   bare `"` ends the string, so the file no longer parses and `seal gate`,
   `seal pr-body` and every other command that refuses an unreadable config
   refuses it, and a bare `\` before `t` or `n` reads as
   a tab or a new line, so the gate runs a command nobody wrote. A `|`
   stays as written. `templates/setup/config.md` *Broad gate* carries the
   rule.

   **Name the criterion; do not restate it.** `templates/setup/config.md`
   *The criterion for choosing a value* owns the criterion, three rules with
   the reason for each, and the person answering reads it there.

   **Offer a decline, and say what it costs.** *Not yet* is a real answer:
   one written to get past a question is worse than none. The cost is one
   sentence: the first `seal gate` run refuses with nothing run, and that
   refusal lands after the review rounds have settled. `/agentic:config`
   fills the key in at any point before then.

   **The third and fourth questions are the two language keys, with the
   recent titles beside them.** `seal pr-body` refuses to compose a pull
   request body where either key is absent, so first setup asks for both
   while the session is already stopped. Beside the two questions the
   orchestrator shows the titles `gh pr list --state all --limit 10`
   returned and names the language it reads them in; where the list is
   empty or `gh` cannot read it, it says so. The option listed first in
   each question is the titles' language where one was read, and `English`
   otherwise. Each question says in one line what its key governs, taken
   from that key's section of `templates/setup/config.md`.

   **Then record the answer: run `seal mode`, with no argument.** It writes
   the `Mode` key from where the folder is and moves nothing. The key is the
   only trace that anybody was asked: left unwritten, a root somebody chose
   and a root that appeared because a session followed the routing rule are
   the same bytes. Nothing asks the question again later: `seal mode --check`
   reports a key that is absent or disagrees with the folder, and writes
   nothing. Under **shared, with pull-request checks**, the orchestrator then
   runs `seal pr-checks install` and relays the line it prints; an exit 1 is
   that line's refusal, and the setup goes on without the checks.

   **Then the two language keys.** `seal mode` has just written
   `config.json` holding `Mode` and nothing else, and the root's
   `README.md` already names `templates/setup/config.md` as the
   documentation of every key. So the orchestrator adds the two keys to
   that file's object, each as `"<key>": "<answer>"`, with nothing beside
   them.

   **Then the `Broad gate` key, where a command was chosen.** The file
   holds `Mode` and the two language keys, so the orchestrator adds the
   `Broad gate` key the way `/agentic:config` step 3 adds one: the key
   alone, `"Broad gate": "<command>"`. A JSON file carries no prose, so the
   two lists and the criterion are read in
   `$CLAUDE_PLUGIN_ROOT/templates/setup/config.md` *Broad gate* and never
   copied into the config, where a frozen copy would say something false
   at the plugin's next release. No command does this and none is being
   added: `skills/implement/scripts/seal.py`'s writer is the `Mode` key's,
   and `skills/config/SKILL.md` *What this does not do* refuses a generic
   setter for a file people edit by hand.

   **A decline writes nothing at all.** No key, no sentinel, no note. A
   repository that declined and one that was never asked meet the same
   refusal at the same moment and are told the same correct thing, so a trace
   would separate two states nothing treats differently. The `Mode` key is
   the opposite: its absence makes a root somebody chose and a root nobody
   chose the same bytes.
2. The orchestrator says in three lines what it created, that its presence
   at that place with the marker as its README's first line is the opt-in,
   and what each part of the root is for. The
   layout is invisible otherwise: it appears in a diff the user did not
   request, or, in local mode, in no diff at all.
3. The orchestrator asks once:
   *"Does this project port behavior from an existing codebase? If so, tell
   me which one and I will set up parity mode."*
   - **Yes**: the orchestrator reads `skills/parity-setup/SKILL.md`
     *Procedure* and follows it, then continues the work.
   - **No**: the orchestrator continues and never raises it again. Bootstrap
     does not re-run, so the question does not either.

Nothing else is asked. **`/agentic:config` is how any of it is changed
later**: it shows every key with its value and routes a change to whatever
owns that key. The orchestrator says so once, here, because a person who
answers a question in a batch has no reason to expect a way back to it.

Ask only here. A repository that has a `seal/` carrying the marker at either
place, `<repo>/seal/` or `$(git rev-parse --git-common-dir)/seal/`, has been
through this: the mode is read from where the folder is, and asking again is the
nagging this plugin exists to avoid. The two language keys are the one
exception, and only where either is missing: the batch of
`skills/implement/orchestration.md` *Orchestrator: what needs a person is
asked in one batch, before the first edit* asks for them before a work
item's first edit.
