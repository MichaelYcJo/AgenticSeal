# 1791384159-a-unit-the-extractor-cannot-bound-is-refused — phase 6

| Field | Value |
|---|---|
| Phase | 6 |
| Commit | a1695208 |
| Ran by | smith on Opus 5.5 |

## What this phase was asked

`plan.md` phase 6: `Resolution` takes Q6's shape and every unpacking site
reads it in one commit; `judge`'s resurrection branch, `--reverify`'s and
`--migrate`'s unsure branches, `file_units`' third field and
`rider_check.py#region_lines`' refusal go; the cases of
`tests/test_a_released_row_is_read_again_in_a_fragment.py`,
`tests/test_a_signer_records_a_pact_change.py` and
`tests/test_a_row_points_by_content.py` that reached their property through
an unsure `.go`/`.cs` place are judged per Q7, re-fixtured or deleted, each
named here. Case S7 widened to the word `resurrected`. `bin/mutation-check`
over `judge`'s and `migrate`'s changed units.

## What this phase found

**Q6 is (a).** `Resolution` is a class with `places` and `refused` and no
tuple behind it, so `places, _ = resolve_unit(...)` fails with a `TypeError`
rather than reading a second field. Every unpacking site moved in one
commit: `judge`, `read_citation` (already on the attributes), the rider
check, the survivor sweep's `resolves` (`[0]` to `.places`), `resolve`, and
every test call site that unpacked the pair, in six modules. `file_units` yields
`(spelling, (start, end))`.

**`judge` keeps the tie-break and loses only the flag.** The branch read
`resurrected or len(places) > 1`; it now reads `len(places) > 1`, and the
"declaration rule is unsure of the only place" detail is gone with the
`unsure` list. `--reverify` had no branch of its own: its words were
`judge`'s. `--migrate` keeps its stamp proof, which still decides the
`unproven` count; only the unsure-place refusal left.

**The rider check's docstring paragraph went in this phase, not phase 8.**
"Resurrection is refused here where the ledger tolerates it" described the
branch this phase removed, and S7 forbids the word in the three scripts; it
now says the checker's refusal is the rider's.

**Q7, per case, for the two modules this phase owns.**

| Case | Verdict | Grounds |
|---|---|---|
| `test_a_held_coordinate_with_an_unsure_place_on_a_dated_row_heals_to_its_destination` (three parameters) · NAME NOT IN TREE | deleted | its only instance was B holding `handler` through the call a move left behind, a place only the declaration rule could resolve to; `ast` resolves a moved function to nothing |
| `test_into_re_reads_a_claim_on_an_unsure_place_at_its_statement` · NAME NOT IN TREE | deleted | `--into` re-reading a claim at its statement on a unit `ast` bounds is `test_into_re_reads_a_claimed_coordinate_at_its_minor_region` |
| `test_reverify_restamps_a_claim_on_an_unsure_place_at_its_statement` · NAME NOT IN TREE | deleted | the in-place re-stamp of a claim is the ordinary path, pinned on `.py` elsewhere in the module |
| `test_reverify_names_a_tie_among_unsure_places_as_the_check_does` · NAME NOT IN TREE | re-fixtured as `test_reverify_names_a_claims_tie_as_the_check_does` | three Python definitions of one name are three places `ast` gives; the claim's tie and the check's sentence are the property |
| `test_reverify_leaves_a_claim_whose_statement_is_gone_in_the_checks_words` | re-fixtured on `.py` | the gone statement is a claim's, whatever bounds the unit |
| `test_under_the_freeze_a_claim_on_an_unsure_place_is_recorded_as_a_move` · NAME NOT IN TREE | re-fixtured as `test_under_the_freeze_a_claim_is_recorded_as_a_move` | the pact record of a claim's re-read holds for a claim on any unit |
| `test_a_claim_on_an_unsure_place_restamped_in_place_is_recorded_as_a_move` · NAME NOT IN TREE | re-fixtured as `test_a_claim_restamped_in_place_is_recorded_as_a_move` | as above, in place |
| `test_a_claim_whose_statement_is_gone_from_an_unsure_place_is_recorded_broken` · NAME NOT IN TREE | re-fixtured as `test_a_claim_whose_statement_is_gone_is_recorded_broken` | as above, BROKEN |

`tests/test_a_row_points_by_content.py`'s unsure-place cases went in phase 5
(`phases/phase-5.md`), because they failed the moment the rule left; this
phase rewrote `test_the_two_commands_that_must_know_ask_for_the_flag`'s
docstring to the refusal it now guards. The comment in
`tests/test_the_fixes_name_their_surface.py` names `generic_units` as history
of rounds 4–6 of 1788229400 and stays.

**Mutation.** `judge`'s tie-break with `or not claim` taken out survived the
three modules' cases, because no case had two identical places for a row
with no claim; `test_two_identical_places_are_one_place_for_a_row_with_no_claim`
was added and turns it red. Dropping the `len(hit) == 1` guard was red
already. `--migrate`'s changed lines are a destructuring; the mutation tried
there (`a = s`) is equivalent on every fixture whose cited range is its whole
unit and was not kept as evidence.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| `Resolution.resurrected`, its tuple base and `__new__` | `Resolution(places, refused)`; S7's widened case |
| `judge`'s `resurrected` branch and its "declaration rule is unsure of the only place" detail | none: no rule can produce such a place |
| `--migrate`'s unsure-place refusal | none, for the same reason |
| `file_units`' third field | none |
| `rider_check.py#region_lines`' resurrection refusal and its docstring paragraph | the checker's refusal, read from `resolve_unit` |
| Three cases of `tests/test_a_released_row_is_read_again_in_a_fragment.py` | the ordinary claim cases named above |
