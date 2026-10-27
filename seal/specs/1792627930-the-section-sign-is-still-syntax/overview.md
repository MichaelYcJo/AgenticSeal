# Overview: 1792627930-the-section-sign-is-still-syntax

## Why this work exists

The section sign leaves every living file, so an agent reads a contract rule
as `contract rule <N>` and another file's section by its heading text, and a
record template stops carrying comments that every record then copies.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The contract's preamble lost its list of agent names | `spec.md` scope item 1: "The preamble says a spawn prompt cites a rule as `contract rule <N>`"; the build also removed "smith, warden, framer, sealer, scribe, and whichever arrives next" | the build | With the list kept, four of five preloads rose above the base (phase 1's record); the heading above the preamble already says the rules bind every agent this plugin spawns, and no case pinned the list |
| Four test cases and three test constants left that `## Removes` does not name | `## Removes` names the citation readers' arms and the two in-step cases; the build also removed `test_another_files_section_in_a_definition_is_not_the_contracts` (phase 1), the `*_LINK` constants of `tests/test_the_rules_have_one_owner.py` and `POINTER_LINK` of `tests/test_a_reference_root_is_read_and_never_taken.py` (phase 2), and `test_plan_names_the_phase_record_path` and `test_the_phase_templates_own_path_comment_matches_the_round_templates` (phase 4) | the build | Each pinned a form that left the tree: a section-sign citation after a file name, a second spelling of one citation, the plan template's pointer sentence, the template's path comment. What each guarded is held at its home by the case its phase record names |
| The spec template's short body lines became placeholders | `spec.md` scope item 10 names body guidance in the plan and questions templates only | the build | Item 10's end state holds only headings, table headers and placeholders, so the spec template's prose lines (scope, data, open questions) became placeholders carrying their words; no sentence was lost |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at the branch's head | answered by `broad-gate.md` and `guarantee.md`: BROAD GATE PASSED at 5992b4d3 against 0d62145a, 7481 passed and 13 skipped, chain exit 0; `seal/config.md`'s `Broad gate` row names no typecheck (read) |
| closed The paid non-inferiority run for the five rewritten preloads | moved 2026-10-27 to MichaelYcJo/SpecSeal#1081, a measurement nobody has taken: no record holds the paid run |

## Not done

`.test_durations` still names the test cases this work removed; CI's
measuring runs rewrite that file, and no case fails on a stale entry, so it
was not edited by hand.

## Fed back into the spec

none
