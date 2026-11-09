---
name: config
description: Show what this repository decided for itself and change any of it, such as the languages it writes in, where its records live, and the command its broad gate runs. Reads seal/config.json, and routes a change to whatever owns that key.
disable-model-invocation: true
---

# /agentic:config, what this repository decided and how to decide otherwise

`seal/config.json` holds what a repository says about itself, one JSON
object with one key per item. Four keys have no default, the two language
keys, `Mode` and `Broad gate`, and the table below says what each absent key
means. A person runs this command to see every key and to change one; the
session running it follows the procedure below. First setup asks its
questions once and never again, and this command is how a person answers
them again later.

## Where the file is

`<repo>/seal/config.json` where that directory exists with the marker
(contract rule 11), and
`$(git rev-parse --git-common-dir)/seal/config.json` otherwise: local mode,
where the root sits under the common git directory. Resolve it that way rather
than spelling the first place and stopping.

**No root at either place** means this repository has not been set up. Say so,
name the `implement` skill's bootstrap as what does it, and stop. Do not
create the file: the root at one of those two places, with the README first
setup copies from `templates/setup/seal-README.md`, is what opts a repository in, so
a root is the bootstrap's to create, and a `seal/` made here without that
README would read as the project's own directory.

**A `config.md` standing in the root without a `config.json`** is an
earlier release's table, which no command reads now. Say so, and run
`seal mode` once: it writes `config.json` from the table and removes
`config.md`, or prints why it wrote nothing. Then read the new file.

## Procedure

**1. Show every key, present or not.** Read the file, and print every key of
the table below with its current value, including the ones the file does not
carry, with the default and where it comes from. A key a repository never set
is the most likely one somebody wants to change, and showing only what is
present hides exactly those.

| Key | Default | What it governs |
|---|---|---|
| `Commit and pull request language` | *none: `seal pr-body` refuses without it, and a commit is written in English* | the commit subject and body, the pull request title and body, and a review report posted as a pull-request comment |
| `Record language` | *none: `seal pr-body` refuses without it, and a record is written in English* | the prose in `frame/design.md`, `frame/plan.md`, `gaps.md`, `frame/questions.md`, `changelog.md`, and a round record's cells |
| `Mode` | *the folder decides* | which of the two places the root should live at |
| `Broad gate` | *none: `seal gate` refuses without it* | the one shell command line `seal gate` runs once the review rounds settle: the full suite, the repository-wide lint, the typecheck |
| `Document token ceiling` | *not declared: no length is checked* | the estimated tokens past which `seal fold` reports a document of the policy root or of one of its groups as one to split |
| `Policy root` | `docs` | the directory of the ratified policy documents, which the settle writes |
| `Reference specs` | *every directory named `specs` outside the root* | the directories this repository kept its own specifications in, which the plugin reads as history and never takes |
| `Pact` | *none: no pact is held elsewhere* | the origin remote URL of the repository holding a pact this repository signs, several separated by `;` |
| `Pact signers` | *none: in a repository holding `seal/pact.md`, `seal pact` refuses the pact without it* | in the pact's repository, the origin remote URL of every other signer, separated by `;` |
| `Pull request seal mark` | *off: no mark* | whether `seal pr-body` writes the plugin's seal mark under the pull request body's `## From the records` heading once the work item is sealed at HEAD; `yes` turns it on |
| `Release note seal mark` | *off: no image* | whether the release's `seal` job attaches the seal image and shows it beside the results in the release note's header; `yes` turns it on. Read only by this plugin's own release workflow, so a key in any other repository changes nothing |

**The two language keys are required**: absent in any of the four ways (no
file, no such key, an empty value, a file that does not parse),
`seal pr-body` names the key and refuses with nothing written, and the
orchestrator asks for both before the next work item's first edit. A
commit or a record is never refused for them and is written in English.
Show each as absent and say what happens without it. **The `Broad gate` key
has no default at all**: absent, `seal gate` names the key and exits 2 with
nothing run, because what a command nobody chose reports proves nothing.
Show it as absent and say what happens without it.

**2. For the mode, show what is true as well as what is written.** That key is
what the repository *wants*; the folder's location is what it *has*, and the
two are separate on purpose. Run `seal mode` and report what it says: the
folder, the key, and whether they agree. Do not read the key directly for
this one: `seal mode` is what the pull-request checks run, and a second
reader is a second answer. Then run `seal pr-checks` and report its line:
whether `.github/workflows/hygiene.yml` is this plugin's, and the release it
pins. No key records that; the file is the record.

**3. Take a change, and route it.**

- **A language key, or the `Broad gate` key,** is only a key. Edit the value
  in place, leaving the rest of the file as it is. Where the file carries no
  such key at all (the file `seal mode` writes holds only `Mode`), add it to
  the object as a key alone, `"<key>": "<value>"`, because
  `templates/setup/config.md` is the documentation of every key and the
  root's `README.md` already names it. A JSON file carries no prose, so
  nothing from the template is copied beside a key.

  **The two lists and the criterion are pointed at, never copied down.** They
  are the plugin's, they change when the plugin changes, and a frozen copy
  anywhere in somebody's repository is a copy that says something false
  about the tool at the next release, which is what the criterion's one-home
  rule is for. Point at `$CLAUDE_PLUGIN_ROOT/templates/setup/config.md`
  *Broad gate* for both. The `Broad gate` value is one shell command line,
  run from the repository root.

  **How to choose that value is written down, and not here.**
  `templates/setup/config.md` *The criterion for choosing a value* owns the
  criterion: three rules, with the reason for each. Read it to the person
  before they answer, rather than summarising it back to them.

  **A `"` or a `\` in a value is written `\"` or `\\`.** The value is a JSON
  string, so `"Broad gate": "bin/test -q -k \"not slow\""` is the key that
  runs `bin/test -q -k "not slow"`, and a pipe is written as it stands.
  `templates/setup/config.md` *Broad gate* says what a single `\` before `t`
  or `n` does to a Windows path.

  **The file is read by a JSON parser, or refused.** A file that does not
  parse, such as one with a trailing comma, is refused for every key, and a
  key written twice or holding no string is refused for that key; each
  refusal names the file, and `templates/setup/config.md` says which
  commands print it and stop and which read their defaults. Read the refusal to the person in plain words, and correct the
  JSON rather than any key the refusal did not name.

  **The `Broad gate` key is looked at before it is run**, and a value that
  would not run as the command it reads as is refused with nothing run:
  the whole command wrapped in backticks or in `$(…)`, or a trailing `&`.
  Nothing is stripped or repaired: rewriting the key is the person's act,
  which is what brings them here. `templates/setup/config.md` *What is refused,
  and what stays allowed* lists the three forms and the ones that stay
  legal, each with its reason, and it is where this is decided.
- **A fold key**, `Document token ceiling` or `Policy root`, is only a key
  too. Edit or add it in place, and point at
  `$CLAUDE_PLUGIN_ROOT/templates/setup/config.md` *The fold's values* for what
  each accepts and what an absent one means, rather than restating it. A
  value `seal fold` will not parse makes it exit 2 naming the key, so run it
  once after the edit.
- **`Reference specs`, `Pact` or `Pact signers`** is only a key too. Edit
  or add it in place, and point at
  `$CLAUDE_PLUGIN_ROOT/templates/setup/config.md` *Reference specs* or *Pact*
  for what each accepts and what an absent one means. `Pact` and `Pact
  signers` are read strictly by `seal pact` at the pact's repository, so a
  value it will not parse is named there.
- **The `Mode` key moves files.** Run `seal mode local` or `seal mode shared`.
  It moves the root, stages the change and writes the key, so the file and
  the folder agree afterwards, and it leaves `.github/` alone. Do not do any
  of that by hand. A person who wants the pull-request checks added or taken
  out is sent to `seal pr-checks install` or `seal pr-checks remove`.

**4. Say what happened beyond the key.** A language key changes a key. The
`Mode` key moves a directory and stages a commit, and the line the switch
prints about the pull-request checks says what it left under `.github/`.
The person needs to see that list rather than *done*.

## Before switching to shared, say what cannot be undone

Going to shared puts the records in the tree. **The commit is the point of no
return, not the move**: once it lands, the records stay in the history
whatever later leaves the tree. `docs/layout/one-root-by-lifetime.md` *Shared or
local* holds that rule. Until that commit, `git reset -- :/seal` and then
`seal mode local` walk the whole thing back. The reset comes first because
the switch stages the move, and `seal mode` refuses a switch over a staged
change under the root. The pathspec is there because a bare `git reset`
unstages the whole index, and the guard has never looked outside the root.

Say it before running the command, not after. Local mode exists for the
repository whose tree must not carry this plugin's files, and shared is the
direction that cannot be walked back.

Going the other way costs something different and it is not a secret either:
every other clone loses the records at the next pull. `seal export` here and
`seal import` there is how a teammate gets a copy.

## What this does not do

- **It does not define a schema.** It reads the keys that are there and routes
  them. A generic setter would be a writer for a file people edit by hand,
  and would invite a short file to drift into settings nobody documents.
- **It does not start over.** Discarding the records means discarding the
  evidence chain every gate here reads. That stays a deliberate act done by
  hand, and `seal export` first is the order.
- **It does not replace the file.** A person can still open `config.json` and
  edit it. This is a door to the room, not a gate in front of it.
