# The record layout

Where each kind of record lives. Every kind of record this repository keeps
has one home, and this document is the index: one table per place, each row naming a file
or a file shape and the one question it answers. A reader looking for a rule
or a record opens this index and then one file.

It is a policy document. A file that states a rule this index gives another
home links to that home and does not restate it, because two copies of one
rule are one rule today and two after the first edit to either. Where a copy
is found, the copy is the defect.

## Every kind of record, at a glance

| Kind | Home | Size target | Index |
|---|---|---|---|
| The changelog | `seal/threads/<work-item-id>/changelog.md` while a work item is open; the GitHub Release at the `vX.Y.Z` tag once its release is published | each fragment is under target | the repository's releases on GitHub, by tag |
| A work item's files | `seal/threads/<work-item-id>/` | each file under target | the table under *seal/threads/<work-item-id>/* below |
| The repository's rules | `skills/core/SKILL.md` for the core every party reads, `CLAUDE.md` for how a session in this repository reaches it, `CONTRIBUTING.md` for a contributor's procedure, and the `docs/` document each one links to | each file under target | this document, and `docs/README.md` |
| The configuration | `seal/config.md`, one row per item; `templates/setup/config.md` documents every row | under target | the `Item` column |
| The follow-up list | `seal/follow-up.md`, one row per item that waits on a named party | under target | its rows, each naming who answers it |
| The process rows | a `### Process changes` table at the end of a work item's `changelog.md` while its work item is open; the release note's table of the same name once its release is published | each fragment is under target | the repository's releases on GitHub, by tag |

## The size a reader takes whole

**A file a reader is meant to take whole fits one read.** The row and the
estimate are `templates/setup/config.md` *The fold's values*, and what a document
past it owes is `skills/settle/SKILL.md` *A document past its ceiling is
split, never trimmed*.
check: tests/skills/test_fold_check.py

## A change writes fragments, never a shared file

A file every branch appends to costs a conflict at the worst moment — after
the broad gate has run, which forces it to run again. So a change writes its
changelog entry into a file of its own, `seal/threads/<work-item-id>/changelog.md`,
never under a heading of a file every branch shares. No two work items
share an id, so no two branches share a file.

**The release note is built from the fragments at the tag, and no copy of
the notes is kept in the tree.** On the `vX.Y.Z` tag push,
`.github/scripts/publish_release_note.py` reads every fragment the commits
after the previous `vX.Y.Z` tag added and that tag does not already hold,
from the history, so a fragment a settle removed before the tag is still
read. The GitHub Release at the tag is the release's notes. A copy in the
tree is the one nobody works from, and so the one that drifts from its
fragment. A fragment lives from the work item's first entry to the settle
after the release that ships it, and the history keeps it after that.
check: tests/github/test_publish_release_note.py

**A change to the way of working writes its process row in its own
fragment.** A work item whose diff changes `skills/core/SKILL.md`, `CLAUDE.md`, an `agents/*.md` file, a `skills/*/orchestration.md` file or `skills/implement/bootstrap.md` ends its `changelog.md` with the line `### Process changes` and a table in
the shape `templates/records/process.md` gives: one row per change, holding
the date, the change, one line of why, and a link to the issue comment or
commit it came from. The orchestrator writes it with the fragment. A row
written with its change leaves no write for the end of the release, and the
next framer reads what the way of working became and why.

**The release note lifts every process row into one table.** Under the
heading `### Process changes`, above the fragments, the note carries every
row of every fragment's process section, in work item id order, and each
fragment follows without its section, so a row is shown once.
check: tests/github/test_publish_release_note.py

## A commit after the build brings its changelog fragment along

**A commit after the build that changes what the work item ships updates the
work item's `changelog.md` in the same range.** The build's last phase writes
the fragment and the release note is built from it as it stands at the tag,
so a later commit that changes behaviour can leave it describing something
that no longer ships. The rule binds whoever writes the commit: the crafter's
fix pass, a fix written after the last round, and an integration commit after a sibling's squash, which the
orchestrator writes. A commit that changes nothing a release note states owes
the fragment nothing.

## docs/

The standing policy. Its index is `docs/README.md`.

## seal/

What the plugin maintains, read and written by machines. Every `seal/…` path
means `<repo>/seal/` where that directory exists, and the root under the git
common directory otherwise.

| File | The question it answers |
|---|---|
| `seal/README.md` | what the root holds, where it lives in each mode, and which file states the export rules |
| `seal/config.md` | what this repository says about itself, one row per item |
| `seal/parity.md` | which codebase this repository ports behaviour from, and at which baseline commit; present only where a migration is declared |
| `seal/pact.md` | what two or more repositories keep together; present only in the repository that holds the pact |
| `seal/follow-up.md` | which items wait on a named party, and who |
| `seal/threads/<work-item-id>/` | one work item's records, the table below |

## seal/threads/<work-item-id>/

One work item's records, from its first commit to the `settle` fold that
retires the directory. Which file each agent writes is
`skills/implement/SKILL.md` *3. The SDD file set*; this table says what each
file answers.

| File | The question it answers |
|---|---|
| `routing.md` | who frames, builds and reviews this work, and where it ends — answered before the first edit |
| `frame/design.md` | what is built, its scenarios, and the decisions with their grounds |
| `frame/plan.md` | in which phases it is built, how each is shown, which approach was chosen over which, and the judgments the orchestrator made in the run, each with its grounds and the document it stands on |
| `frame/questions.md` | which decisions only a person could make, and how each was answered |
| `gaps.md` | what was not verified and who answers it, and what was within reach and deliberately not taken |
| `trail/phases/phase-N.md` | what building one phase found, each departure from the frame among it |
| `trail/rounds/round-N.md` | what one review round read, found and closed |
| `changelog.md` | this work item's entry in the next release's notes |
| `trail/gate.md` | the orchestrator's one broad run, on either routing answer |
| `guarantee.md` | whether the sealer sealed the work, against the issue and the tree |

**The files keep these paths until the settle after their release, and
leave together.** `routing.md`, the frame (`frame/design.md`,
`frame/plan.md`, `frame/questions.md`), the trail (`trail/rounds/`,
`trail/phases/`, `trail/gate.md`) and the files at the thread's top
(`gaps.md`, `changelog.md`, `guarantee.md`, and a `pr.*.md` where one was
written) go with the directory, whole, when the settle removes it
(`docs/checks/the-fold.md` *The fold, and what tells it from a deletion*,
and `docs/releasing/release-checklist.md` *2b*). A document that still cites a record of
it writes the path a commit holds, as `<commit>:<path>`, which `git show`
opens as written; in this repository `tests/censuses.py#HISTORY_PATH` is
the one form `old_names` passes.
check: tests/skills/test_settle.py

**A record a template starts carries no HTML comment.** Its template holds headings, table headers, placeholders, the `seal` blocks the record's grammar asks for and the foot line, and nothing else. The guidance for
writing the record is in the skill or agent definition its writer reads,
stated there once. A comment copied into every record is a second copy of
that guidance, and every reader of the record has to model it.
check: tests/text/test_a_record_carries_no_comment.py

**A record holds a fence around a finding's paste-ready fix and around each of its `seal` blocks, and a field a check reads stands inside a `seal` block and nowhere else.** The readers keep one fence state, by the fence rule of `hooks/lib/blocks.py`, so a `seal` block quoted inside a fix belongs to the fix and is not read, and `hooks/lib/fields.py` is the one reader of the blocks.
check: tests/skills/test_chain_check.py

**A reader of a record keeps no comment state: it reads `<!--` as text, and
refuses at its line a line outside every fence that begins with `<!--`.** A
record carries no comment, so a comment state in its reader models nothing
the record holds. The refusal stands where the reader reads:
`chain_check.py` in a round record, a `guarantee.md` and a `trail/gate.md`,
`unverified_check.py` in a `gaps.md`, and `rule_changes.py` in a
`frame/design.md`'s `## Rule changes`. A base revision that holds such a line is not compared,
because nobody can edit a commit that already happened. A `routing.md` is
the exception: its reader, `hooks/lib/routing.py`, runs in the edit check
(`docs/checks/the-routing-check.md` *The edit check*) before every edit in an
opted-in repository, where a refusal would stop the edits of a work item
framed before its template lost its comments, so that reader keeps the
comment walk of `hooks/lib/blocks.py`.
check: record-comment-line-refused

**A fact of a work item has one record, and every other record cites it by path and heading.** What changed, for a user, is `changelog.md`'s. What is built, its grounds, its rule changes and its removals are `frame/design.md`'s. In which phases, by which approach and with which commit each closed is `frame/plan.md`'s. What only a person could decide, and what was assumed in its place, is `frame/questions.md`'s. What building one phase found, each departure from the frame among it, is that phase's `trail/phases/phase-N.md`. What one round found is its `trail/rounds/round-N.md`. The one broad run is `trail/gate.md`. What went out unproved and what was within reach and not taken is `gaps.md`. The sealer's audit is `guarantee.md`. A record cites another's fact by its path and heading and does not restate it, so a template holds no section or cell that could hold only a copy.
check: tests/behaviour/test_a_phase_hands_the_next_one_a_record.py tests/behaviour/test_unverified_rows_close.py

**A `<commit>:<path>` citation names a commit that `main` or a release
branch reaches, except in a work item's `trail/` and its
`guarantee.md`.** A feature branch squashes into its release branch, and
the squash discards every commit the branch wrote, so a citation of one
opens in no clone after the merge, and a reader sent to it finds no
source. The commit to cite is the squash that holds the same file, or
the path at HEAD where the file is the branch's own. A round record, a
phase record and a guarantee cite what a party ran at the branch's own
commits, which the squash orphans as it orphans the round's `target:`
line, and they leave with the work item; a file under
`evals/behaviour/` is not read either. A bare commit is not read: a
plan's Status cell and a round's `fixed` line name the branch's own
commits by rule, and whether a sentence cites a bare commit as where a
file was read is the reviewer's reading. Where the checkout holds no
`main` or release branch ref, nothing is judged.
check: tests/text/test_a_cited_commit_outlives_the_squash.py

## The root records

| File | The question it answers |
|---|---|
| `CLAUDE.md` | how a session in this repository reaches the core, `skills/core/SKILL.md`, which the plugin's hook prints from the tree here; any rule this repository alone asks of a session, each linking to its home |
| `CONTRIBUTING.md` | how a contribution is made and checked, and what a change to a gate must carry |
| `README.md` and `README.ko.md` | what the plugin is and how to install it |

**A `CLAUDE.md` row that points at a home carries three things: the home's
path and section, the moment a session needs the rule, and the act in one
sentence of the row's own, with the value the act needs.** It carries no
table, reasoning or history. Only the home's sentences are pinned, so a stale
value in a row is a reviewer's finding. No two rule documents may share more
15-word runs than their pair was measured at, except two agent definitions,
since a passage two definitions share states a fact about each file that
holds it; the count does not see a rule restated in fresh words.
check: tests/text/test_the_rules_claude_md_names_have_one_home.py tests/text/test_no_passage_is_pasted_into_a_second_file.py

**Shipped text an agent or a user reads points only at documents the plugin ships: no agent definition, template, skill document or message a script prints names this repository's `CONTRIBUTING.md` or `CLAUDE.md`.** An agent reads a `skills/`, `templates/` or `docs/` path as the plugin's and a bare file name as the repository it works in, so a shipped sentence naming `CONTRIBUTING.md` names, in a user's repository, a file that is not this one. A rule an agent applies lives in its definition or in the skill it opens at that step, and this repository's contributor's guide cites it where a person needs it. A comment or docstring in a shipped script is read by whoever maintains the plugin, a contributor, so it may cite `CONTRIBUTING.md`. The direction is read from the links as written, by `git grep -l 'CONTRIBUTING\|CLAUDE\.md' -- agents templates 'skills/**/*.md'`, whose only hits name a user's own `CLAUDE.md`, and by reading the printed messages of a script the review changes; the proofer does both at stage 1 of a review that changes a shipped document.
