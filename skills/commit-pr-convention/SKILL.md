---
name: commit-pr-convention
description: |
  Format rules for commit messages, PR titles, PR bodies and branch names:
  the prefix vocabulary, the language the repository states in `seal/config.md`,
  where a translated body lives, and how to check a title against the
  repository's own history.
  Use when: writing a commit message, opening a pull request, naming a
  branch, or titling either.
  NOT for: the prose and structure of a PR body or review comment
  (writing-style), code comments and docstrings, a project's response
  language.
---

# commit-pr-convention, the format of commits, pull requests and branches

This skill is read by whoever writes a commit, a pull request or a branch
name: the crafter, and the orchestrator, which also writes the code where
`routing.md` answers `Implementation` with `the session`. Below, that party
is **the writer**.

`writing-style` governs what a pull request body **says** and how it is
built. This skill governs the **envelope**: the prefix, the title's shape, the
branch name, and where a translation lives. A body can satisfy one and
violate the other.

## First, check the title against the history

```
gh pr list --state all --limit 10
```

**The history is the rule even where no document states it.** Everything below
was read off a repository's log, and repositories differ. A title that does
not look like the ones in that list is the one that is wrong. The comparison
is of a title's shape and language, and its prefix is the one the table in
*Commit messages* gives the change.

This step is first because the failure happens here: a list on screen is not
a comparison made. Having run the command is not the same act as comparing
the title to what it returned, so the writer makes the comparison in one line
before opening anything.

**An empty list is an answer, not a blocker.** A repository with no pull
requests yet has no history to outrank anything, so the table in the next
section is what the writer uses, unchanged, and the first title written
becomes the history the next one is compared against.

## The language is the repository's, and it says so in a file

**The writer reads `config.md` in the root before writing any of the five
things below.** The root is `<repo>/seal/` where that directory exists with
the marker (contract rule 11) and `$(git rev-parse --git-common-dir)/seal/`
otherwise, which is where local
mode keeps it; resolve it that way rather than spelling the first place and
stopping.

```markdown
| Item | Value |
|---|---|
| Commit and pull request language | Korean |
```

That row governs the **commit subject and body**, the **pull request title and
body** (all four, because a squash makes them one text) and the **review
report posted as a pull-request comment**, which is prose for whoever opens
that pull request. In the body of a work item routed through the review
chain it governs the orchestrator's part, as *Pull request bodies* below
says.

**It does not govern the work-item records.** `frame/design.md`, `frame/plan.md`,
`gaps.md`, `frame/questions.md`, `changelog.md` and `trail/rounds/round-N.md`'s cells
follow a second row, `Record language`, read by the
`implement` and `code-review` skills. The two are independent: setting one
does not carry the other.

**Every way of not naming a language lands on English.** There are four of
them and they are one rule: no file, no such row, an empty value, and a file
that cannot be read or does not parse as that table. A config nobody can read
must not stop a commit, so the writer meeting any of these writes English and
carries on rather than asking.

**To create it, copy `templates/setup/config.md` from this plugin into the root and
edit the row meant.** It ships more than one. The mode's row is written
by `seal mode` from where the folder is, and edited by hand only to ask for
a move: `seal mode --apply` then moves the folder to what the row says. That
file repeats the exclusions below, because the person who writes a
repository's config reads it and never reads this one.

It governs prose and nothing else, and the exclusions are what make it safe
to change:

- **The prefix vocabulary is not translated.** `feat:`, `fix:`, `docs:` stay
  as they are in every repository. They are scanned in a log and parsed by
  tooling, and `기능:` teaches neither.
- **Branch names stay ASCII**, because a branch name is typed into a shell
  and pasted into a URL. *Branch names* below states their shape.
- **The field names, section headings and vocabulary a checker reads
  literally**, which belong to the other row's surface and are excluded from
  both. The whole list is in `templates/setup/config.md` under *What no row
  governs*, and it is derived from the checkers' own constants rather than
  copied: a hand-copied list is a second source that drifts.
- **Code**: identifiers, comments, docstrings, file names, test function
  names.
- **The response language is not in that file.** What a session says to the
  person it works for is a person's setting and lives in that person's own
  configuration. Two people in one repository can want different answers
  there and the same one here.

A repository whose team writes another language says so in one row; one that
says nothing writes English.

## Commit messages

`<prefix>: <one line, starting lower-case>`, in the repository's language.
The prefix is not part of that: it stays as the table below spells it.

**A prefix is the writer's judgment of what the change does for whoever
meets it after the merge, a user or a party working on a later change, and
the writer states its grounds.**

| Kind | What whoever meets the change meets | Examples |
|---|---|---|
| `feat:` | something new to use or to meet | a command; a record format; a refusal on a rule the change itself states; a thing removed that its users must now work around |
| `fix:` | behaviour that was wrong against a rule the tree stated before the change, now matching it | a check that let through what its rule refused; a skill sentence that contradicted the policy it cites |
| `perf:` | the same behaviour, sooner or at less cost | a file parsed once instead of once per row |
| `refactor:` | the same kinds of outcome, reached another way | a judgment moved from a script to an agent; a gate retired because what it caught did not outweigh its cost; a skill nobody used, removed; a section moved to another file |
| `test:` | nothing outside the repository's own tests | a case added or corrected, even one that refuses where the suite gates the merge |
| `docs:` | text nobody acts on | a README's explanation; a comment |
| `chore:` | upkeep that changes nothing anyone meets | the version move; the changelog fold; a dependency pin that changes nothing met; a work item's records committed alone; a settle that writes the rule changes released work items stated |

**Where a change does more than one of these, its prefix is the one highest
in the table**, because whoever meets it meets the largest change.

**A change's own tests and its work item's records never decide its
prefix**, so a speed-up with the case that pins it is `perf:`, and a README
edit with the case that pins its words is `docs:`.

**Text a party reads and acts on is behaviour**, so a change to a skill, an
agent definition, a template a party fills or a hook's message is never
`docs:` and never `chore:`, while a work item's own records, which describe
their change and leave with it, fall under the paragraph before this one.

**"Before the change" is the branch the change merges into**, and a rule
stated only in the change's own work item, such as its frame, belongs to the
change, so a commit that builds it takes the kind its pull request takes.

**An effect is counted once, by the change that decided it**, so a settle
that writes a rule change a released work item stated is `chore:`, and a
section it rewrites that no released work item decided is that rewrite's
kind.

**The writer states the grounds** in the orchestrator's part of the pull
request body, as *Pull request bodies* says, and `agents/sealer.md` step 4
reads that part against the design and the diff, so a prefix the change does
not bear out is a disagreement the sealer names.

**An issue's title takes the prefix the pull request that closes it will
take**, chosen by this table, so no issue is filed `chore:` by default, and
the issue is retitled where the pull request takes a prefix other than the
issue's.

**The prefix states what the change is, and is never chosen to fit a release
number.**

**A repository's own log decides how a prefix is spelt, and never which row
a change takes.** Where the log spells a prefix of the table differently, the
writer follows it. Where the log uses a prefix of its own for its workflow,
one the table lacks, the writer uses that one too. The writer invents none: a
prefix nobody has used before teaches a reader nothing, and the log is how
they learn what it means. Which row a change takes is the table's, because a
log written by default teaches the default. A repository with no history
uses the table as it stands, because a first commit has nothing to compare
against.

**One language, in the subject and in the body: the one the row names.**
Where feature branches squash, the commit body becomes the pull request body,
so the two cannot be in different languages without one of them being wrong
at the merge. That is why one row answers for all four surfaces rather than
one row each.

**A session's commit in a repository whose root is shared (`<repo>/seal/`)
ends with one `Seal-Routing:` trailer, naming its work item or reading
`no work item`.** In local mode a commit carries none. The work item is its
directory's name under `seal/threads/`, the one the branch's `routing.md` sits
in; `no work item` is the value where the session ran `seal no-work-item` on
the branch. The trailer stands in the message's last paragraph, beside any
other trailer, so git's trailer parser reads it:

```
feat: the edit check refuses an undeclared branch

Seal-Routing: 1792935671-the-routing-check-moves-to-the-sessions-tools
Co-Authored-By: <the harness's co-author line>
```

The value is a field, not prose, so it stays as spelt in every language.
Why a session's commit carries it, why a local-mode commit does not, and
what `chain-check` does with it are `docs/the-routing-check.md` *At the pull
request*.

## Pull request titles

**The same prefix vocabulary as the commits, and the same language.**

```
good  fix: the commit gate has three ways out and its prompt named two
bad   The commit gate has three ways out and its prompt named two   (no prefix)
bad   fix: improve gate messaging                                    (a category)
```

**A title states the symptom, not the technique or the category.** Someone
reading only the list of titles should learn what happened. `writing-style`
carries this at length; this file carries the prefix in front of it.

## Pull request bodies

**The language the row names.** The prose and structure rules are
`writing-style`'s, and the writer reads it **before** writing, not after:
structure that came out wrong is not recovered by fixing sentences.

**A work item routed through the review chain has a body in two parts, and
the orchestrator's comes first.** The orchestrator writes the first part,
above the line `skills/code-review/scripts/pr_body.py#HEADING` holds, and
`seal pr-body` writes the second part under that line from the work item's
records, inside one `<details>` fold
(`skills/code-review/orchestration.md` *Orchestrator: the pull request
opens once the sealer seals*). The first part is in the language
`Commit and pull request language` names. The second part is the records'
own text, so it is in `Record language`, and nobody rewrites or translates
it.

**Its chain section has one shape: what the rounds found is the copy's
*Review rounds* section, and the comparison table opens the orchestrator's
part.** The table is what makes this run readable beside the last one, so
it stands above the orchestrator's prose rather than under it, where a
reader who stops after the body's first screen still has the numbers. What
the rounds found is copied from the round records, so the orchestrator's
part does not restate it.

**The rows have one owner: `skills/verify/orchestration.md` *Measure the
segment, and feed the flow log*.** That section states each row and where it
is taken from. The writer links it rather than copying the rows into this
file or into the body: two copies are two things to keep in step, and the one
that drifts is the copy nobody owns.

**The orchestrator's part says in one sentence why the title takes its
prefix, and names the kind that came closest, where one did.**

Where a translated body is wanted, **the writer puts it in the repository as a
file and links it from the body.**

- **Where**: the work item's own folder under the root, as `pr.<lang>.md`,
  and `<lang>` is the mirror's **own** language rather than the body's. An
  English repository keeps a Korean mirror at
  `<root>/threads/<work-item-id>/pr.ko.md`; a Korean one keeps an English
  mirror at `pr.en.md`. `<root>` resolves the way the language section above
  resolves it, and the next bullet says where it must not land.
- **Why there**: its permissions are the repository's, so anyone who can
  read the pull request can open it; it is versioned with the code; and it
  survives the merge.
- **So not under the git directory.** Where the root resolves to
  `$(git rev-parse --git-common-dir)/seal/`, nothing under it is ever a
  commit candidate, which takes away all three reasons above at once: a
  reviewer cannot open it, no version of it exists, and the merge carries
  nothing. The mirror goes beside the documents the pull request already
  touches instead, the same place a repository with no work-item structure
  puts it.
- **Not a hosted document or artifact.** A hosted document is private by
  default, so its link in a public pull request opens for nobody but its
  author; it stays readable only through a share somebody makes by hand; and
  it lives outside the repository, so the merge leaves it behind.

**A translation keeps the terms the repository invented.** It renders the
prose, not the vocabulary: a coined term stays in its original spelling and
is unpacked once, at first use. `writing-style` has the reasoning.

## Branch names

A branch name takes the same prefix vocabulary as the commits, and is
**ASCII whatever the repository's language is**. The row does not reach
here: a branch name is typed into a shell and pasted into a URL.

- A branch cut from an issue is `<prefix>/<issue number>-<slug>`.
- A branch for two issues joins their numbers with a hyphen:
  `feat/110-117-<slug>`.
- A change with no issue has the slug alone: `<prefix>/<slug>`.
- A release branch is `release/vX.Y.Z`.

```
fix/940-on-demand-files-state-the-current-rule
docs/the-readme-says-how-to-install
```

**The slug states the symptom.** A name carrying only the issue number
(`fix/88`) tells a reader nothing in a list of branches, which is the one
place branch names are ever read.

## Before the pull request opens

The writer answers these rather than assuming them.

1. Was `gh pr list` run, **and the title compared to what it returned**?
2. Does the title carry the prefix the table in *Commit messages* gives the
   change?
3. Was **`config.md` in the root opened**, and are the title and body in
   the language its `Commit and pull request language` row names? No file and
   no such row both mean English.
4. If there is a translation, is it a file in the repository, not a hosted
   document, and is it named for its own language?
5. Does the title alone say what happened?
