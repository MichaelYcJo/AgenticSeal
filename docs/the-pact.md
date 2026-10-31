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
naming where it is held. `seal pact` is the command that reads every signer
from there. The three names are the owner's, and a case holds other words for
them out of the shipped text.
check: tests/behaviour/test_one_word_one_meaning.py tests/hooks/test_config.py

**A pact headed with the word 0.18.x used still reads, and `seal pact`
names the rename on it in no exit class.** Through 0.18.x a signer was
called a signatory, and a pact's `| Signatory |` table carried that word
into a file nobody regenerates. A file holding no table under the new header
is read under the old one exactly as it would be under the new; a file
holding one is read from it alone, and an old header beside it is refused,
because its rows would otherwise go unread. `seal pact` prints one line
naming the file, both headers and the release that renamed them before that
file's other lines, and its exit is what the new header gives. No command
rewrites a pact: the line says to rename the header when the file is next
edited, and every text this plugin ships says `signer`.
check: tests/skills/test_pact_check.py tests/hooks/test_config.py tests/behaviour/test_one_word_one_meaning.py

## When there is a pact at all

**A sentence is contract when another repository's code would be wrong if it
changed, and a pact exists only where a work item commits in more than one
repository and those repositories share contract.** The rule is the owner's,
and it decides two things: whether the structure exists, and which sentences
go in `seal/pact.md`. A work item that only commits in several repositories
gets a routing declaration in each and nothing else. A sentence only one
repository's code depends on stays in that repository's own documents,
because a pact that collects those sends every signer to re-read changes
that were never theirs. `templates/setup/pact.md` states the rule where the file is
begun.
check: tests/behaviour/test_a_signer_declares_its_pact.py

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
`skills/implement/multi-repository.md` *Orchestrator: a work item that commits in more than one repository* is the procedure.
check: tests/behaviour/test_a_signer_declares_its_pact.py tests/behaviour/test_every_orchestrator_act_names_its_delivery.py

## How a signer names the pact

**Every signer but the pact's repository names the pact in a `Pact` row
of its `seal/config.md`, and one reader answers that row for every
caller.** `Pact` is the origin remote URL of the pact's repository, several
separated by `;`, compared normalised, and a pact anchor names the pact by
that same URL.
`hooks/lib/config.py#pact_declaration` refuses what will not parse in a sentence
and stops nothing, so every reader of the row reads the same row. A `Pact`
row written twice has no value at all: its first row is not the answer. A
`Pact` row the config table does not hold is no row, so `seal pact` reads
that signer as naming no pact, a relationship recorded on one side only.
check: tests/behaviour/test_a_signer_declares_its_pact.py tests/skills/test_pact_check.py tests/hooks/test_config.py

## The pact anchor

**A signer cites a clause as one row of a `| Pact | Clause | Hash |` table in
a work item's `frame/design.md`, and `seal pact` reads the table with
`hooks/lib/config.py#gfm_table`.** The row is the pact anchor, and it records
what the work was built against. `Pact` is the origin remote URL of the
pact's repository, as the signer's `Pact` row writes it, compared
normalised. `Clause` is the clause's heading path, such as
`## Order response shape / ### Fields`: every `##` heading of `seal/pact.md`
below its `| Signer |` table is a clause, and a `###` narrows inside one.
`Hash` is the eight lowercase hex digits `coordinates.py#content_hash` gives
the clause's region, `00000000` until the first report names the real one.
The walker reads the table as GitHub renders it, as it reads every other
table here, so nothing in a row is quoted or escaped except a pipe, written
`\|`. A row naming another pact the signer's `Pact` row declares is passed
over, for that pact's `seal pact` to grade.
check: tests/skills/test_pact_check.py tests/skills/test_coordinates.py tests/hooks/test_config.py

**The anchor table is the table whose header is `| Pact | Clause | Hash |`, cell for cell, and a table whose header is near it is named and not read.** A header whose cells, case folded and with one emphasis run removed, are those words is the near one: `seal pact` names it at its line, with the exact header to write, grades no row of it and refuses nothing for it. Whether `| pact | clause | hash |` meant the anchor table is the judgment of the person reading the report and of the proofer reading the frame, never the tool's, so the tool carries no normalisation of the header (`skills/core/SKILL.md` *Judgment is spent where meaning is the question, and a script answers the rest*). The template writes the exact header. A code span is a mention of the word rather than a use, strikethrough marks it deleted, and a plural, another word, another order or another width is another table. A second exact header is refused as a second anchor table.
check: tests/skills/test_pact_check.py

**`seal pact` refuses, at exit 2, a row of the anchor table it cannot grade
and every `pact:` token in a signer's frame.** A row whose `Pact` cell is not
one remote URL names no pact anybody can tell, and a row naming this pact
whose `Clause` cell does not open with a heading, or whose `Hash` cell is not
eight lowercase hex digits, grades nothing; each is refused at its line. A
row whose `Pact` cell names a pact the signer's `Pact` row does not declare,
such as a remote one letter off the pact's, is refused at its line, because
no `seal pact` grades it: another pact's reports the signer `ONE-SIDED` and
reads none of its frames. A `pact:` token outside a fenced code block, in any
case, is the inline anchor `seal pact` read through 0.23.x, and it is refused
at its line with the row to write in its place. A token with a space beside
its colon is not read: prose writes the word before a colon and a space, and
no release read that spelling as an anchor. A frame leaves the tree at the
settle after its release, so the rewrite is one row in a file that is leaving
anyway, and a token passed over would read as a signer citing nothing. A text
that shows the retired shape rather than citing a clause puts it in a fenced
code block, which nothing reads.
check: tests/skills/test_pact_check.py

## A signer's CI reads nothing of the pact

**At a pull request nothing reads the pact, and no exit status moves on
anything about it.** There is no token for a pull request to read another
repository with, so a signer's CI could see one side only; `seal pact` at the
pact's repository is where the reconciliation runs.
`skills/code-review/scripts/chain_check.py` holds no pact arm.
check: none reader: review

## `seal pact` reconciles, locally

**`seal pact`, run at the pact's repository, reads every signer the pact
lists and says which way each mismatch points.** It finds each checkout
through the `| Remote | Path |` table of `~/.claude/agentic/pact-paths.md`
or the one sibling directory with that origin, guessing nothing; refuses a
signer whose config does not name the pact; and grades every anchor naming
the pact. The map is read by `gfm_table`, as every other table is, and a map
that is there and will not read, holds no such table, holds it twice, or has
a row the walk does not read is refused at exit 2, because a row nobody reads
reports its signer as not found. A remote written on two rows of the map is
refused, and neither row is read. `SUPERSEDED` means HEAD's own history gave
the clause that hash, so the signer was built against a replaced clause;
`NOT TAKEN` means only another ref did, and names it, so the pact has not
taken the signer's recorded change; `UNMATCHED` means no commit did; `BROKEN`
means the heading path names no single clause. Git decides the direction and
never decides `OK`. Exit 1 is a mismatch or a checkout not found, and exit 2
is unusable input.
check: tests/skills/test_pact_check.py tests/hooks/test_config.py

## What this does not see

**A pact whose history was squashed, or that lives under the git directory,
reads every old version as `UNMATCHED`, and a renamed heading breaks every
anchor to it.** A repository that squashes its pact edits loses the
intermediate clauses, so a signer built against one reads `UNMATCHED`
where `SUPERSEDED` was true; both are exit 1 and both say to read the two
sides, so the reading degrades without going quiet. A pact under local mode
has no history at all, and `seal pact` says so in its summary. A clause's
heading is its address, so rewording the prose is a change every citing
signer re-reads, and renaming the heading is one each of them has to
re-coordinate. And `seal pact` runs where a person runs it: nothing on a
pull request reconciles anything.
check: tests/skills/test_pact_check.py

**`seal pact` reads the anchor table and nothing else in a frame.** A table
under a header outside the normalisation, such as `| Pact | Clause | Hashes |`,
and a row no anchor table holds are neither graded nor refused, and the
signer's `READ` line does not count them. Whether such a line was meant as an
anchor is a judgment of meaning, and a grammar written to make it finds a new
shape at every reading. So the proofer makes it, at stage 1 of the signer's
own review. It reads the work item's `frame/design.md` against the shape
`seal pact` reads and the signer's `Pact` row, and a line meant as an anchor
that `seal pact` does not read is a finding. A signer whose work item goes
straight to the pull request has no proofer, and there the `READ` line's
count is the only sign.
check: tests/skills/test_pact_check.py skills/code-review/SKILL.md
