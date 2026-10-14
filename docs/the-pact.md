# The pact — one contract kept by several repositories

Some work items commit in more than one repository, and some of those
repositories keep a contract together: a response shape one serves and
another reads, a field list two of them write. This document is the standing
account of where that contract lives, how each repository knows about it,
and what checks it.

It is a policy document: it outranks the SDD set, and a work item that finds
it wrong corrects it rather than working around it.

## The words

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
**The pact is the one copy of what two or more repositories keep together,
and every repository of such a work item is a signer, the one holding the
pact included.** The pact is `seal/pact.md` in one of them. That repository
has no noun of its own: it is the pact's repository, identified by holding
the file, and where more than one pact can be meant, a text says which by
naming where it is held. `pact-check` is the command that reads every signer
from there. The three names are the owner's, given twice: in #647 on
2026-10-03, and in #822 on 2026-10-06, which renamed the second. The working
words of the first issue's thread name nothing here, and a case holds them
out of the shipped text.
Enforced by: tests/test_one_word_one_meaning.py::test_the_pacts_words_keep_one_meaning, tests/test_a_signer_declares_its_pact.py::test_the_routing_step_mints_one_id_and_declares_only_in_gated_repositories

<!-- specs/1791239490-a-repository-that-keeps-a-pact-is-a-signer -->
**A pact or a pact review record headed with the word 0.18.x used still
reads, and `pact-check` names the rename on it in no exit class.** Through
0.18.x a signer was called a signatory, and two headers carried that word
into files nobody regenerates: a pact's `| Signatory |` table, and a pact
review record's `| Signatory | Change | Verdict |`, which is permanent. A
file holding no table under the new header is read under the old one
exactly as it would be under the new; a file holding one is read from it
alone, and an old header beside it is refused, because its rows would
otherwise go unread. `pact-check` prints one line naming the file, both
headers and the release that renamed them before that file's other lines,
and its exit is what the new header gives; at the pact's repository
`chain-check`'s notice carries the same sentence and its exit does not
move. No command rewrites a pact: the line says to rename the header when
the file is next edited, and every text this plugin ships says `signer`.
Enforced by: tests/test_pact_check.py::test_s2_a_pact_headed_as_0_18_wrote_it_reads_the_same_and_names_it, tests/test_a_pact_review_takes_a_pact_change.py::test_s5_a_review_record_written_in_0_18_still_takes_its_change, tests/test_a_signers_ci_prints_its_pact.py::test_a_pact_headed_as_0_18_wrote_it_is_counted_and_the_rename_named, tests/test_a_signer_declares_its_pact.py::test_s4_a_pact_holding_both_tables_reads_signer_and_refuses_the_old_one, tests/test_pact_check.py::test_s4_a_pact_holding_both_tables_is_exit_2_naming_the_old_one, tests/test_one_word_one_meaning.py::test_no_pact_text_names_a_signer_the_way_0_18_did, tests/test_a_pact_review_takes_a_pact_change.py::test_s5_a_review_record_holding_both_headers_is_refused, tests/test_one_word_one_meaning.py::test_no_live_text_says_the_word_0_19_0_renamed

## When there is a pact at all

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
**A sentence is contract when another repository's code would be wrong if it
changed, and a pact exists only where a work item commits in more than one
repository and those repositories share contract.** The rule is the owner's
(#647, decision 5) and it decides two things: whether the structure exists,
and which sentences go in `seal/pact.md`. A work item that only commits in
several repositories gets a routing declaration in each and nothing else. A
sentence only one repository's code depends on stays in that repository's
own documents, because a pact that collects those sends every signer to
re-read changes that were never theirs. `templates/pact.md` states the rule
where the file is begun.
Enforced by: tests/test_a_signer_declares_its_pact.py::test_the_routing_step_mints_one_id_and_declares_only_in_gated_repositories

## One routing answer, one id, every gated repository

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
**The routing question is asked once, the work-item id is minted once, and
a declaration goes into every repository the work item commits in that
already has a `seal/` root, and into no other.** The id names the directory
in every repository, so each share's changelog fragment and fold marker are
keyed alike, and a directory named differently in each would have to be
renamed later, moving both. A repository with no root is
named in the handback and left alone, because writing into it would create
its root, which is the bootstrap's decision and the person's. Nothing checks
that every share carries one id: an id minted twice cannot be told from a
signer's own work item that cites the pact without changing it.
`skills/implement/orchestration.md` §*A work item that commits in more than
one repository* is the procedure.
Enforced by: tests/test_a_signer_declares_its_pact.py::test_the_routing_step_mints_one_id_and_declares_only_in_gated_repositories, tests/test_every_orchestrator_act_names_its_delivery.py::test_every_orchestrator_act_names_its_delivery

## How a signer names the pact

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
**Every signer but the pact's repository names the pact in a `Pact` row
of its `seal/config.md`, and says in `Pact notify` what it asks to be told,
and one reader answers both rows for every caller.** `Pact` is the origin
remote URL of the pact's repository, several separated by `;`, compared
normalised; its last path segment is the name an anchor carries, so two
pacts ending in one segment are refused. `Pact notify` is `always`,
`when the pact is touched` or `never`, `when the pact is touched` where it
is absent. The value decides which rows of the signer's records of pact
changes `pact-check` reads. `hooks/config.py#pact_declaration` refuses
what will not parse in a sentence and stops nothing, so the print at a
signer's pull request and the refusal at the pact's repository are about
the same rows. A `Pact notify` value outside the vocabulary, or a row
written twice, has no value at all: its first row is not the answer.
Enforced by: tests/test_a_signer_declares_its_pact.py::test_one_pact_reads_normalised_with_the_default_notify, tests/test_a_signer_declares_its_pact.py::test_a_notify_value_outside_the_vocabulary_is_refused_naming_all_three, tests/test_a_signer_declares_its_pact.py::test_a_notify_row_written_twice_has_no_value, tests/test_a_signer_declares_its_pact.py::test_a_row_that_will_not_parse_is_refused_and_never_read_as_absent

<!-- specs/1791128260-a-pact-row-is-read-in-one-plain-spelling -->
**A pact row is read in one spelling, and every other line of `seal/config.md`
that names a pact is refused.** The one spelling is a row of the
`| Item | Value |` table whose item is exactly `Pact` or `Pact notify`: that
case, one space between the words, and nothing in its cell but the item and the
spaces around it. A line names a pact where the letters `p`, `a`, `c` and `t`
stand in that order with only non-letters between them and no letter before the
`p`, as written or with its character references decoded and its compatibility
letters folded (NFKC), so a fullwidth or mathematical `Pact` names one and
`impact` names none. On a row of the table only the item is read, so a value
that mentions a pact is never refused. Any other line is refused where it also
holds a `|`: a row written below the table's end, in a second table, in a block
quote, inside a code fence or an HTML comment, or cut by a character only
Python ends a line at. An example kept in a fence or a comment is refused too,
because telling it from a live row would mean modelling GFM; delete it. A line
with no `|` has no value cell, so the pact can be named in prose. A line
standing directly over a table's delimiter row is that table's header, and a
one-column table needs no pipe anywhere, so such a line naming a pact is
refused with or without a `|`, inside a block quote or a list item too. In a
file that holds an HTML table cell's tag, `<td>` or `<th>`, anywhere, a code
span, a fence or a comment included, a line naming a pact is refused with or
without a `|`, because such a cell carries a value with no pipe beside it; take
the tag out to name the pact in prose again. A refusal leaves `Pact notify`
with no value, so `pact-check` exits 2 and a signer's CI prints a notice.
Enforced by: tests/test_a_signer_declares_its_pact.py::test_s2_every_way_the_walk_passes_a_pact_row_by_is_refused, tests/test_a_signer_declares_its_pact.py::test_s2_a_pact_item_spelled_another_way_is_refused, tests/test_a_signer_declares_its_pact.py::test_s4_a_line_that_is_not_a_pact_row_in_another_spelling_is_silent, tests/test_a_signer_declares_its_pact.py::test_s5_a_plain_row_in_a_fence_or_a_comment_is_refused_and_not_read

## The pact anchor

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
**A signer cites a clause as `pact:<name>/"<heading path>"@<hash>`.** Every
`##` heading of `seal/pact.md` below its `| Signer |` table is a clause, and
a `###` narrows inside one. The hash is the content hash
`evidence_check.py#content_hash` gives the clause's region, the value a
local coordinate to that heading carries. A signer writes the anchor in a
spec's Grounding, recording what the work was built against.
Enforced by: tests/test_pact_check.py::test_s12_a_signer_citing_the_current_clause_is_clean, tests/test_a_unit_is_bounded_where_a_parser_decides.py::test_a_word_ending_in_pact_is_not_a_pact_anchor

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**A token begins a pact anchor where `pact:<name>` is followed at once by
`/` or `#`, or by the rest of an anchor with its `/` missing, and
`pact-check` refuses a token that begins one and does not go on to parse.**
The rest of an anchor is a quoted heading path closed by `@`, or `@` and a
hash, at once or after one mark or one space — a `.`, `-` or `_` included,
which the name itself could otherwise hold, and so is one of those marks
standing just before the `/` — so the commonest typos are named rather than
read by nobody. Anything else naming the pact is a
mention and is left alone: `pact:<name>` followed by punctuation, a space or
the end of a code span. The one form that begins an anchor and is not an
attempt is the one this plugin prints to show the shape, its heading path a
placeholder, `/"<heading path>"`. So `pact:<name>/` written in prose is
refused, and the refusal names both ways out: quote the heading path and
give it a hash, or, where the text shows the shape rather than citing a
clause, put it in a fenced code block, which nothing reads.
Enforced by: tests/test_pact_check.py::test_an_anchor_missing_its_slash_is_refused, tests/test_pact_check.py::test_a_mark_the_name_holds_is_not_a_second_name, tests/test_pact_check.py::test_the_refusal_names_both_remedies, tests/test_pact_check.py::test_prose_naming_the_pact_is_not_a_citation, tests/test_pact_check.py::test_a_pact_anchor_that_does_not_parse_is_refused

## A signer's CI prints and verifies nothing

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
**At a pull request, `chain-check` prints the pact a signer names and how
many pact anchors its declared work item cites, and no exit status moves on
anything about the pact.** There is no token for a pull request to read
another repository with (#647, decision 2), so a signer's CI can see one
side only. It prints the pact's repository, the notify value and the anchor
count, a notice for a row that will not parse or an anchor naming an
undeclared pact, and in the pact's repository how many signers the pact
lists, and every one of them says that `pact-check` at the pact's repository
is where the reconciliation runs.
Enforced by: tests/test_a_signers_ci_prints_its_pact.py::test_a_signer_prints_its_pact_and_its_exit_status_does_not_move, tests/test_a_signers_ci_prints_its_pact.py::test_a_row_that_will_not_parse_is_a_notice_and_never_a_failure, tests/test_a_signers_ci_prints_its_pact.py::test_the_pacts_repository_prints_how_many_signers_it_lists

## `pact-check` reconciles, locally

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
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
Enforced by: tests/test_pact_check.py::test_s8_a_hash_from_heads_own_history_is_superseded, tests/test_pact_check.py::test_s9_a_hash_only_another_ref_holds_is_not_taken_and_names_it, tests/test_pact_check.py::test_s10_a_heading_path_that_resolves_to_nothing_is_broken, tests/test_pact_check.py::test_s11_a_relationship_recorded_on_one_side_is_refused, tests/test_pact_check.py::test_s12_a_signer_citing_the_current_clause_is_clean

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**`pact-check` reads every signer's records of pact changes, following
that signer's `Pact notify` as read now, and reports a row citing a
clause of this pact as `NOT TAKEN`, exit 1, until a pact review here takes
it.** This is the second source of `NOT TAKEN` that #735's frame named, and
the report keeps its name. The line names the signer, the record and its
line, the clause, the work item, and the record's content hash, which is the
value a pact review writes. A `—` row from a signer whose notify is
`always` is `NOTED`, printed until a pact review takes it and in no exit
class, because a pact review is owed only where a clause is cited (#647's
decision 4). Under `when the pact is touched` a `—` row is not read, and
under `never` no row is. A record that will not read is `UNREADABLE` and one
that will not parse `REFUSED`, both exit 2. The `READ` line and the summary
count the pact changes read and taken.
Enforced by: tests/test_a_pact_review_takes_a_pact_change.py::test_s12_an_untaken_pact_change_is_not_taken, tests/test_a_pact_review_takes_a_pact_change.py::test_s13_a_row_citing_no_clause_is_noted_under_always, tests/test_a_pact_review_takes_a_pact_change.py::test_s13_a_row_citing_no_clause_is_not_read_when_the_pact_is_touched, tests/test_a_pact_review_takes_a_pact_change.py::test_s13_under_never_no_row_is_read, tests/test_a_pact_review_takes_a_pact_change.py::test_s17_a_record_that_will_not_read_or_parse_is_exit_2

## A pact review takes a pact change

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**A pact review is an ordinary work item at the pact's repository, opened
when `pact-check` reports a `NOT TAKEN` from a pact change, and it takes a
record by a row of `seal/pact-reviews/<work-item-id>.md` naming the
signer and the record at its current content hash.** The row's `Change`
is the signer's work-item id, `@`, and the content hash `pact-check`
printed; its verdict is `holds`, the clause stands and the change keeps it,
or `amended`, this work item amends the clause to take the change. The
builder judges each change against its clause in the signer's checkout,
and the review chain's warden verifies those judgments there; where the
routing answer skips the review chain, the builder's judgment is the whole
pact review. The record is begun from `templates/pact-review.md`.
`skills/implement/orchestration.md` §*A pact review at the pact's
repository* is the procedure.
Enforced by: tests/test_a_pact_review_takes_a_pact_change.py::test_s14_a_pact_review_at_the_current_hash_takes_it, tests/test_a_pact_review_takes_a_pact_change.py::test_s16_amended_is_taken_where_the_clause_moved

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**A record is taken at the content hash a pact review row names and no
other, and a row that cannot be true is refused at exit 2.** A commit SHA is
never the key, because a signer's feature branch squashes and the SHA
stops resolving. So a record that gains rows after its pact review reads
`NOT TAKEN` again, naming the hash the review took and the hash it holds now,
and a change that keeps its clause can still be taken, which a key on the
clause's own hash would forbid. `pact-check` refuses a row naming a
signer the pact does not list, a record that signer does not hold, a
verdict other than the two, a change not written `<work-item-id>@<hash>`,
and `amended`, at the record's current hash, where a clause it cites still
has the hash the record recorded. A review at an older hash is not judged
again against rows the record gained since: what it said was about the
record it took. A pact review takes a whole record, one verdict for every
row in it. A record citing a clause the pact amended beside one it kept is
taken as `holds`, the amendment written in the pact itself; and a row that is
not this pact's — a `—` row, or one citing another pact — still changes the
record's hash, so a record this pact took reads `NOT TAKEN` again when one is
added.
Enforced by: tests/test_a_pact_review_takes_a_pact_change.py::test_s15_a_record_grown_after_its_review_is_not_taken_again, tests/test_a_pact_review_takes_a_pact_change.py::test_s16_a_pact_review_row_that_cannot_be_true_is_refused, tests/test_a_pact_review_takes_a_pact_change.py::test_s17_a_review_that_will_not_read_or_parse_is_exit_2, tests/test_a_pact_review_takes_a_pact_change.py::test_an_amended_review_at_an_older_hash_is_not_judged_again

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**A clause the pact's repository changes owes no pact review.** `SUPERSEDED`
already sends every signer citing the clause to re-read it against its
own code and re-anchor, which is checked where that code is, and nothing on
a pull request can see which signers cite a clause (#647's decision 2).
A pact review answers the other direction alone: a signer's code moved
under a clause it cites.
Enforced by: tests/test_pact_check.py::test_s8_a_hash_from_heads_own_history_is_superseded

## What this does not see

<!-- specs/1790993137-a-signatory-declares-its-pact-and-pact-check-reads-it -->
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
Enforced by: tests/test_pact_check.py::test_a_pact_under_local_mode_has_no_history_and_says_so, tests/test_pact_check.py::test_s10_a_hash_no_commit_gave_is_unmatched

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**A pact under local mode keeps its pact reviews on one machine.** It keeps
`seal/pact-reviews/` under the git directory, so another clone of the pact's
repository reads the same changes as `NOT TAKEN`, which is loud in the right
direction.
Enforced by: nothing — no pact case builds two clones of one repository

<!-- specs/1791128260-a-pact-row-is-read-in-one-plain-spelling -->
**A pact line with a letter written between the word's letters, or with a
look-alike letter, from another script or its own, is read as no line at all.**
The reader names a pact by its four letters with only non-letters between them,
so the letters of markup break the word: a tag name in `P<b></b>act`, a link
destination in `[P](x)act`, and an entity name the decode does not know. So
does `Pаct` spelled with a Cyrillic `а`, U+0430, and `ᴘᴀᴄᴛ` in Latin small
capitals, which NFKC does not fold. Each such line is read as it was before
#759, and a notify value written in one is the default. YAML front matter is
not read either: github.com shows it as a table, cmark-gfm does not, and a line
of it naming a pact is refused only where it holds a `|`. Catching these would
need a grammar of GFM's markup or a table of look-alike letters, and leaving
both out is what keeps the rule one that refuses rather than one that models.
Every spelling the review of the earlier design found is caught:
`` `Pact notify` ``, `**Pact notify**`, `Pact` with a U+200B inside it,
`[Pact notify](x)` and a character reference such as `P&#97;ct`.
Enforced by: tests/test_a_signer_declares_its_pact.py::test_the_blind_side_is_read_as_no_line, tests/test_a_signer_declares_its_pact.py::test_s2_a_pact_item_spelled_another_way_is_refused

<!-- specs/1791076833-the-reverify-writer-records-before-it-restamps -->
**A pact review row naming a signer the pact has since taken out of its
`Signer` table is refused at exit 2, and stays refused.** A pact review
record is permanent, and a departed signer and a mistyped URL are the
same text, so the refusal cannot tell them apart and does not try. Take the
pact review rows naming a signer out with the signer, in the same
change.
Enforced by: tests/test_a_pact_review_takes_a_pact_change.py::test_a_review_row_naming_a_signer_since_dropped_stays_refused
