# The pact

Some work items commit in more than one repository, and some of those
repositories keep a contract together: a response shape one serves and
another reads, a field list two of them write. This document says where that
contract lives, how each repository knows about it, and what checks it.

## The words

**The pact is the one copy of what two or more repositories keep together,
and every repository of such a work item is a signer, the one holding the
pact included.** The pact is `seal/pact.md` in one of them. That repository
has no noun of its own: it is the pact's repository, identified by holding
the file, and where more than one pact can be meant, a text says which by
naming where it is held. `pact-check` is the command that reads every signer
from there. The three names are the owner's, and a case holds other words for
them out of the shipped text.
check: tests/test_one_word_one_meaning.py tests/test_config.py

**A pact headed with the word 0.18.x used still reads, and `pact-check`
names the rename on it in no exit class.** Through 0.18.x a signer was
called a signatory, and a pact's `| Signatory |` table carried that word
into a file nobody regenerates. A file holding no table under the new header
is read under the old one exactly as it would be under the new; a file
holding one is read from it alone, and an old header beside it is refused,
because its rows would otherwise go unread. `pact-check` prints one line
naming the file, both headers and the release that renamed them before that
file's other lines, and its exit is what the new header gives. No command
rewrites a pact: the line says to rename the header when the file is next
edited, and every text this plugin ships says `signer`.
check: tests/test_pact_check.py tests/test_config.py tests/test_one_word_one_meaning.py

## When there is a pact at all

**A sentence is contract when another repository's code would be wrong if it
changed, and a pact exists only where a work item commits in more than one
repository and those repositories share contract.** The rule is the owner's,
and it decides two things: whether the structure exists, and which sentences
go in `seal/pact.md`. A work item that only commits in several repositories
gets a routing declaration in each and nothing else. A sentence only one
repository's code depends on stays in that repository's own documents,
because a pact that collects those sends every signer to re-read changes
that were never theirs. `templates/pact.md` states the rule where the file is
begun.
check: tests/test_a_signer_declares_its_pact.py

## One routing answer, one id, every gated repository

**The routing question is asked once, the work-item id is minted once, and
a declaration goes into every repository the work item commits in that
already has a `seal/` root, and into no other.** The id names the directory
in every repository, so each share's changelog fragment and changelog marker
are keyed alike, and a directory named differently in each would have to be
renamed later, moving both. A repository with no root is named in the
handback and left alone, because writing into it would create its root,
which is the bootstrap's decision and the person's. Nothing checks that every
share carries one id: an id minted twice cannot be told from a signer's own
work item that cites the pact without changing it.
`skills/implement/orchestration.md` *A work item that commits in more than
one repository* is the procedure.
check: tests/test_a_signer_declares_its_pact.py tests/test_every_orchestrator_act_names_its_delivery.py

## How a signer names the pact

**Every signer but the pact's repository names the pact in a `Pact` row
of its `seal/config.md`, and one reader answers that row for every
caller.** `Pact` is the origin remote URL of the pact's repository, several
separated by `;`, compared normalised; its last path segment is the name an
anchor carries, so two pacts ending in one segment are refused.
`hooks/config.py#pact_declaration` refuses what will not parse in a sentence
and stops nothing, so every reader of the row reads the same row. A `Pact`
row written twice has no value at all: its first row is not the answer. A
`Pact` row the config table does not hold is no row, so `pact-check` reads
that signer as naming no pact, a relationship recorded on one side only.
check: tests/test_a_signer_declares_its_pact.py tests/test_pact_check.py tests/test_config.py

## The pact anchor

**A signer cites a clause as `pact:<name>/"<heading path>"@<hash>`.** Every
`##` heading of `seal/pact.md` below its `| Signer |` table is a clause, and
a `###` narrows inside one. The hash is the content hash
`coordinates.py#content_hash` gives the clause's region, the value a
local coordinate to that heading carries. A signer writes the anchor in a
spec's Grounding, recording what the work was built against.
check: tests/test_pact_check.py tests/test_coordinates.py

**A token begins a pact anchor where `pact:<name>` is followed at once by
`/` or `#`, or by the rest of an anchor with its `/` missing, and
`pact-check` refuses a token that begins one and does not go on to parse.**
The rest of an anchor is a quoted heading path closed by `@`, or `@` and a
hash, at once or after one mark or one space. The marks are `.`, `-` and `_`,
which the name itself could otherwise hold, and one of them standing just
before the `/` counts too, so the commonest typos are named rather than read
by nobody. Anything else naming the pact is a mention and is left alone:
`pact:<name>` followed by punctuation, a space or the end of a code span. The
one form that begins an anchor and is not an attempt is the one this plugin
prints to show the shape, its heading path a placeholder, `/"<heading path>"`.
So `pact:<name>/` written in prose is refused, and the refusal names both
ways out: quote the heading path and give it a hash, or, where the text shows
the shape rather than citing a clause, put it in a fenced code block, which
nothing reads.
check: tests/test_pact_check.py

## A signer's CI reads nothing of the pact

**At a pull request nothing reads the pact, and no exit status moves on
anything about it.** There is no token for a pull request to read another
repository with, so a signer's CI could see one side only; `pact-check` at the
pact's repository is where the reconciliation runs.
`skills/code-review/scripts/chain_check.py` holds no pact arm.
check: none reader: review

## `pact-check` reconciles, locally

**`pact-check`, run at the pact's repository, reads every signer the pact
lists and says which way each mismatch points.** It finds each checkout
through `~/.claude/specseal/pact-paths.md` or the one sibling directory with
that origin, guessing nothing; refuses a signer whose config does not
name the pact; and grades every anchor naming the pact. `SUPERSEDED` means
HEAD's own history gave the clause that hash, so the signer was built
against a replaced clause; `NOT TAKEN` means only another ref did, and names
it, so the pact has not taken the signer's recorded change; `UNMATCHED`
means no commit did; `BROKEN` means the heading path names no single clause.
Git decides the direction and never decides `OK`. Exit 1 is a mismatch or a
checkout not found, and exit 2 is unusable input.
check: tests/test_pact_check.py tests/test_config.py

## What this does not see

**A pact whose history was squashed, or that lives under the git directory,
reads every old version as `UNMATCHED`, and a renamed heading breaks every
anchor to it.** A repository that squashes its pact edits loses the
intermediate clauses, so a signer built against one reads `UNMATCHED`
where `SUPERSEDED` was true; both are exit 1 and both say to read the two
sides, so the reading degrades without going quiet. A pact under local mode
has no history at all, and `pact-check` says so in its summary. A clause's
heading is its address, so rewording the prose is a change every citing
signer re-reads, and renaming the heading is one each of them has to
re-coordinate. And `pact-check` runs where a person runs it: nothing on a
pull request reconciles anything.
check: tests/test_pact_check.py
