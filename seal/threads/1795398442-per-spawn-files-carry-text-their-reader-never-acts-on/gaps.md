# Closing memo: 1795398442-per-spawn-files-carry-text-their-reader-never-acts-on

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the format check, the broad gate, over phase 1's tree | the orchestrator, at the broad run after the review rounds settle |
| The same broad gate over phase 2's tree, whose runs covered only the plan row's modules and the phase boundary set | the orchestrator, at the broad run after the review rounds settle |
| The same broad gate over phase 3's tree, whose phase boundary set ran with one case failing, `tests/text/test_no_passage_is_pasted_into_a_second_file.py#test_no_pair_of_rule_documents_shares_a_run` (`trail/phases/phase-3.md`) | the orchestrator, at the broad run after the review rounds settle |

## Not done

Phase 1 adds no case that refuses a retired-number list written back into
the contract's preamble. `frame/design.md` S8 holds that absence with
`git grep -n -F 'retired numbers' -- skills`, run once at the build, and
*Scope* item 9 asks the case only to read the list from
`docs/running/the-agent-set.md`. A copy in the contract would sit beside
the one the case reads and leave it green, and catching that copy is
review's reading.

Phase 3 leaves the paste check red at `236d3c5e6`. The new file's
exit-1 paragraph and `skills/code-review/orchestration.md` *Orchestrator:
the run ends with a verifying round* each cite the core's row as "that the
row *No fix that no round reads* of `skills/core/SKILL.md` *Judgment is
not licence to skip a party* gives to a round,". That is 15 words once
`skills/settle/scripts/passages.py#words` folds the path and its section
into one token. The check counts any 15-word run two rule documents
share, and the cut made the two clauses a pair. The text is a link in the
form `tests/text/test_the_rules_have_one_owner.py#THE_CORES_ROW` requires,
so contract rule 18 forbids rewording it to pass. *Scope* item 4 moves
the paragraphs with their words. Teaching `passages.py#words` to fold the
row's name with its citation changes a reader `chain_check.py` uses too,
which phase 3's Delivers cell does not hold. Whether to reword one clause
or change the normaliser is the orchestrator's to decide.
