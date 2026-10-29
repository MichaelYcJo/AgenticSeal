# Phase 1: 1793251202-the-citation-case-misses-files-and-wrapped-comments

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 97052b16 |

## What this phase was asked

Build `plan.md` row 1 as a move. The seven contract-rule citation cases,
their readers, their constants and the six-tree walk leave
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` for
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`. Their names,
parameters and behaviour stay the same. The contract module loses its
`# --- citations (#957)` banner. The 15 `.test_durations` keys of the moved
cases are rewritten to the new path with their seconds kept. No case is
written new, because a move is proved by the cases it already has. Then run
the row's one command.

## What this phase found

The frame held at every coordinate it gave, with one line off. The registry
row `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#citations`
stands at line 91, not at `:85-87` as `frame/design.md` says (read). Nothing
depends on the line number.

Two names were changed in the move, and nothing else was. The helper
`dangling` is now `contract_dangling`, because the module's `citations()`
binds a local list called `dangling`. The contract module's `read` is
imported as `read_at_root`, because `citations()` also binds a local called
`read`. The two imports come from the contract module, as five modules
already import `HEADING` from it. The banner now reads
`# --- contract rule citations (#957)`, because a bare `citations` in this
module already means section citations. The moved code differs from the
old in those two names, the banner, and one list comprehension wrapped
because the longer name took it past the line length. A `diff -w` of the
old lines against the new block, with the two renames undone, showed
nothing else (executed).

A write hook in this session ran a formatter after each edit. After the
first edit it removed the two new imports, which were unused at that moment.
They were added again after the moved code landed, and `uvx ruff check` then
passed (executed).

The proof is the existing cases at the new path (executed):

- `bin/test` with the eight modules of the plan's row and `-q`: 332 passed,
  exit 0. A run of the same modules with `-rA` listed every moved node id
  as `PASSED` under the new path.
- `git grep -n -e tree_files -e CITED_TREES -e near_citations -- tests/text`
  found nothing, exit 1.
- A `git grep` over `tests/` for each of the seven case names found each
  only in the new module.
- A script compared `.test_durations` with `git show HEAD:.test_durations`.
  The 15 keys removed under the old path and the 15 added under the new
  path carry the same case ids and the same seconds, and the keys are still
  sorted.
- `uvx ruff check` and `uvx ruff format --check` over the two modules:
  exit 0.

Each old node id and its new one:

| Old node id under `tests/text/test_the_agent_contract_holds_the_universal_rules.py::` | New node id under `tests/behaviour/test_a_cited_section_stands_in_its_file.py::` |
|---|---|
| `test_every_cited_section_exists` | `test_every_cited_section_exists` |
| `test_a_citation_above_the_last_section_is_caught[...]`, 7 ids | the same 7 ids |
| `test_a_wrapped_citation_is_named_at_the_line_it_starts_on` | `test_a_wrapped_citation_is_named_at_the_line_it_starts_on` |
| `test_a_bare_rule_outside_the_contracts_homes_is_not_a_citation` | `test_a_bare_rule_outside_the_contracts_homes_is_not_a_citation` |
| `test_no_file_cites_the_contract_in_a_near_miss` | `test_no_file_cites_the_contract_in_a_near_miss` |
| `test_a_near_miss_citation_is_refused_at_its_line[...]`, 3 ids | the same 3 ids |
| `test_the_one_spelling_is_no_near_miss` | `test_the_one_spelling_is_no_near_miss` |

No `seal mutate` run was made, because a move adds no behaviour
(`skills/verify/SKILL.md` *The narrow command still has to be able to
fail*).
