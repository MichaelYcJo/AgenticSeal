# Implementation Plan: 1793251202-the-citation-case-misses-files-and-wrapped-comments

Approved 2026-10-29 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

The case that checks `contract rule <N>` citations reads only six trees
and `CONTRIBUTING.md`, and only five file extensions. It also reads no
citation that wraps across a `#` comment marker. The repository already
has a citation reader that reads every tracked text file outside the
records and drops `#` markers:
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`. This work
moves the contract-rule citation cases into that module unchanged, then
points them at that module's corpus and its `flowing`. The second walk
goes. At the base, the change is green on the tree: 232 citations read
over 325 files, none dangling, no near miss (`frame/design.md` *What the
probes answered*).

## Technical context

- The contract-rule reader is
  `tests/text/test_the_agent_contract_holds_the_universal_rules.py:64-75`
  (constants) and `:238-352` (readers and cases). `tree_files` (`:249-256`)
  walks `CITED_FILES` and `CITED_TREES` with `os.walk`. It keeps `.md`,
  `.py`, `.yaml`, `.json` and `.txt`, so a `.yml` file is skipped even
  inside `templates/`. `cited_sections` (`:238-246`) and `near_citations`
  (`:322-329`) read the raw text, so `CITATION`'s `\s+` cannot cross a
  `#` marker.
- The sibling module's corpus is `citations(root)` (`:166-199`):
  `git -C <root> ls-files -z`, `RECORDS` dropped, `conftest.on_disk` for a
  positive sweep, `text_of` returning `None` for a file that is not UTF-8.
  `flowing` (`:75-83`) joins adjacent `.py` literals with
  `ADJACENT` and drops `COMMENT_MARK` in every file that is not `.md`. It
  keeps each line break, so a citation's line number is still right.
- The sibling module loads `rule_changes.py` and `hooks/lib/config.py` at
  import (`:36-40`). That is why it stands in `tests/behaviour/`, and why
  the contract module cannot import `flowing` from it and stay in
  `tests/text/` (`CONTRIBUTING.md` *The test layout*).
- `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD`
  registers each test scope that lists paths from git by
  `path#scope`. The sibling module's row is
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py#citations`
  (`:85-87`). If the `ls-files` call moves into a new shared function,
  that row moves with it. The words `ls-files` stay at the call site
  (`tests/conftest.py#git_listing`'s docstring).
- Five modules import `HEADING` from the contract module (`git grep`
  executed). None imports a name this work moves.
- Two names collide in the sibling module. `citations(root)` binds the
  locals `read` and `dangling` (`:186`), and the moved code has a
  module-level `dangling` function and calls the contract module's
  `read(rel=CONTRACT)`. Phase 1 may rename the moved helpers, for example
  to `contract_dangling`, and import the contract's text by name from the
  contract module. A helper renamed in a move is still proved by the
  existing cases. The seven case names do not change.
- Failure scenario of the chosen approach, six months out: someone changes
  `flowing` for section citations, for example to join a new comment
  style, and contract-rule reading changes with it. That is intended,
  because both are citations a reader must see. The moved fixture cases
  are the guard on each grammar. A second risk: a reader looking for the
  contract's citation check opens the contract module and does not find
  it. The `check:` line in `skills/writing-style/SKILL.md:268` names both
  modules, and the sibling module's docstring names the contract-rule
  shape.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the contract module's own walk. Widen it to `git ls-files` minus `RECORDS`, and move `flowing` into `tests/conftest.py` so that both modules import it. | Two modules each list the same corpus with their own listing and their own exclusions. That drift is what #1127 is: the contract walk stopped at six trees while the sibling's read every file. The next change to either corpus repeats it. Editing `tests/conftest.py` also makes every test module a reader of a changed path at the phase boundary (contract rule 2). | Rejected. It keeps a structure whose only premise is that the contract module was there first. That premise was checked, and no case outside the module uses its walk (`git grep` executed). |
| Import `flowing` from the sibling module into the contract module and keep two walks. | Importing runs the sibling's module-level loads of `rule_changes.py` and `hooks/lib/config.py`. A `tests/text/` module would then load shipped code against `CONTRIBUTING.md` *The test layout*, and the two walks still drift. | Rejected |
| Copy `COMMENT_MARK` and `ADJACENT` into the contract module. | Two statements of how a citation is read across a comment. A fix to one, such as a new marker, leaves the other blind. | Rejected (`CLAUDE.md` *The rule a mechanism is kept against*: a fact has one source) |
| Leave the reach as it is and state in the module which files it leaves out. This is the issue's second option for its first *Done when*. | `CLAUDE.md`, `.github/workflows/*.yml` and `templates/setup/hygiene.yml` stay unread under a sentence saying so. A citation added there dangles while the suite stays green. Reading them costs nothing measurable: 0.066 s for all 325 files. | Rejected |
| Move the contract-rule citation cases into the sibling module. Read the one corpus through one listing and `flowing`, and remove the second walk. | See *Technical context*, last bullet. | Chosen. It replaces the structure where the defect lives. The contract module's remaining cases read the contract file alone, which is the premise for keeping them where they are (read). |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The seven contract-rule citation cases and their readers move to `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, unchanged in names, parameters and behaviour. They take with them `tree_files` and its two lists, which phase 2 removes. The contract module loses them and its `# --- citations (#957)` banner. The 15 `.test_durations` keys are rewritten to the new path with their seconds kept. No new case. This is a move, proved by the existing cases at the new path. | One command: `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/behaviour/test_a_commit_names_its_repository.py tests/behaviour/test_a_probe_that_commits_says_so.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/text/test_broad_gate_rule.py -q` passes. Each moved node id passes at the new path (S1). `git grep -n -e tree_files -e CITED_TREES -e near_citations -- tests/text` finds nothing. | 97052b16 |
| 2 | One corpus function in the module holds the `ls-files` call. `citations(root)` and the contract-rule reader both read through it. `cited_sections` and `near_citations` read `flowing(rel, text)`. `tree_files`, `CITED_TREES` and `CITED_FILES` go. The contract-rule reader takes a root, so fixture trees can be read. New cases cover S3 to S7. The module docstring states S8. The registry row in `test_a_shrunken_corpus_declines_to_judge.py` names the scope that holds the listing. | The phase 1 command passes, with the S2 tree case green and its two floors met. Each new case of S3, S5, S6 and S7 is shown red first: run it against phase 1's commit, with the corpus function replaced by the old walk (six trees, five extensions, over the fixture root) and `flowing` left out of the two readers. Then run it green against phase 2's code. Both runs and their outputs go in phase 2's record (contract rule 15). S4 passes on both sides, because the old walk read no record either. | |

## Operational impact

None. No shipped script, hook, `seal` subcommand, workflow or dependency
changes. Only the repository's own suite and `.test_durations` change.
