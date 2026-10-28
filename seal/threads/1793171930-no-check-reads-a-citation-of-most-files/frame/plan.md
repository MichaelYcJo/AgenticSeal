# Implementation Plan: 1793171930-no-check-reads-a-citation-of-most-files

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned for phases 1 and 2.

## Summary

One case reads every citation of another file's section across the tracked
text files outside the records and refuses one whose file has no such
heading or bold rule lead. It replaces the case that read citations of
`skills/implement/SKILL.md` alone. Run over the tree, it finds three
citations that point at nothing, and the work corrects all three. A citation
in `docs/` that a pending `## Rule changes` item corrects is reported as a
warning and passes until the settle. `skills/writing-style/SKILL.md`'s
citation sentence names the bold rule lead and the new case.

## Technical context

- The case it replaces is
  `tests/behaviour/test_the_set_a_work_item_always_has.py:438-516`: a regex
  over whitespace-collapsed text (`:443-446`), its own list of record
  prefixes (`:449`), `##` and `###` headings by regex (`:452-454`), a floor of 10
  (`:497`), and a refusing case built in memory (`:502-516`). It reads no
  bold lead, no possessive, no other file, and no citation wrapped across a
  `#` comment line.
- Headings are read through `skills/settle/scripts/rule_changes.py#headings`
  and `#heading_text` (`:61-76`), which ask `live_lines`, so a heading in a
  fence is not one. Pending corrections are read through `#parse` (`:85`)
  and, for a whole-section `remove`, `#section_lines` (`:200`). The module
  is loaded with `tests/conftest.py#load_module` (`:1058`), the way
  `tests/skills/test_rule_changes.py:21-25` loads it.
- The policy root is `hooks/lib/config.py#policy_root` (`:689`). This
  repository's `seal/config.md` has no `Policy root` row, so it is `docs`.
- The corpus exclusions are `tests/censuses.py#RECORDS` (`:871`), the list
  the `section_sign` census already reads for the same purpose.
- `tests/conftest.py` puts every directory under `tests/` holding a test file
  on `sys.path` (`CONTRIBUTING.md` *The test layout*), so `censuses` imports
  by name, as `tests/test_censuses.py` does.
- The three citations to correct are at
  `.github/scripts/gather_changelog.py:43-44`,
  `skills/verify/scripts/mutation_check.py:103-104` and
  `tests/behaviour/test_one_word_one_meaning.py:461-462`; `frame/design.md`
  *Scope* gives each one's target text and its grounds.

**Failure scenario of the chosen approach, six months on.** A writer cites a
section in a shape outside the case's grammar, such as `` *X* in
`docs/y.md` `` or a path and heading separated by a comma. The case does not
read it, the heading is later renamed, and the citation dangles with the
suite green. That is the reader failing open on input it cannot read, the
class #956 audits; the grammar is the one `skills/writing-style/SKILL.md`
prescribes, so the drift starts as a style miss a review can see. A second,
smaller one: the prefix rule lets a heading's tail be rewritten under a
citation of its opening words, which keeps naming the same section and is
intended.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep the `implement`-only case as the structure, and add one such case per cited file | The scan found 35 cited files (executed). A 36th file cited for the first time is read by no case, which is how `gather_changelog.py`'s citation of `docs/the-record-layout.md` went unseen. The premise that keeps the structure, that only `implement`'s headings move, is false: three files other than `implement` hold a citation that points at nothing now (executed). | rejected |
| Keep the `implement`-only case and add a tree-wide case beside it | Two readers of one citation shape drift apart, and each reports the same miss in its own words. `CLAUDE.md` *The rule a mechanism is kept against*: a fact has one source. | rejected |
| Replace it with one tree-wide case in `tests/behaviour/` | The failure scenario above. | chosen |
| A shipped checker, a `seal` subcommand run in CI and offered to plugin users | It adds a mechanism and a CI step, and it ships a gate into repositories that cite in their own conventions. Nothing asks for it, and the issue asks for a case. | rejected |
| A census in `tests/censuses.py`, run by `census_case` over each module file | `census_case` runs over the files test modules declare as `TARGET`. The citations in `docs/`, `skills/*/SKILL.md` and `agents/` are not module files, so most of the corpus goes unread. | rejected |
| Resolve a citation only by exact match with a heading | Four citations that name their section by its opening words would be refused (`docs/the-review-record.md:409`, `docs/the-record-layout.md:283`, `tests/behaviour/test_a_release_publishes_its_note.py:30`, `skills/verify/scripts/session_cost.py`'s *Measure the segment*), and every long heading would need its whole text at each citation. The defect it alone catches is a tail rewritten under a citation that still names the section. | rejected |
| Match the cited text case-insensitively | A near-miss spelling passes, which `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* says a check refuses at its line. It would also leave `mutation_check.py`'s lowercase citation standing. | rejected |
| Resolve against headings only, as the issue's first scan did | Three living citations name a bold rule lead (executed), among them `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`'s of `skills/verify/orchestration.md` *A run says what it did not answer*. Each would be refused, and the rules of this repository open with a bold sentence by design (`skills/settle/SKILL.md` *A rule has one shape*). | rejected |
| Fail a `docs/` citation that a pending rule change corrects | A pull request that renames a heading cited from `docs/` cannot edit `docs/`, so it could not pass until the settle. Every such rename would block. | rejected |
| Excuse such a citation through a list kept in the test | A stored list beside the tree that has to be kept in step with it, which `CLAUDE.md` rules out. The pending `## Rule changes` items already are that list, read through their one reader. | rejected |
| Excuse it by reading the pending `## Rule changes` items through `rule_changes.parse`, and report it as a warning | A correction item whose `from` does not quote the citation excuses nothing, so the case fails on a pull request whose framer quoted the sentence loosely. That failure is the cheaper direction: the framer re-quotes the sentence. | chosen |
| Rewrite the comment that cites the removed *Where the stamp is drawn* in words, without the path | It stops being a citation and stops naming where the section stood. The `<commit>:<path>` form `docs/the-record-layout.md` *seal/threads/<work-item-id>/* prescribes keeps both, and the case does not read it. | rejected for the `<commit>:<path>` form |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The new module with its reader and scenarios S1 to S8 of `frame/design.md`, each fixture case seen red before its code; S1 seen red naming the three coordinates, then the three citations corrected; the `implement`-only case, its reader, its record list, its timing entries and its now-unused imports removed | `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_one_word_one_meaning.py tests/github/test_gather_changelog.py tests/skills/test_mutation_check.py -q`, exit code read directly; the red runs recorded in `trail/phases/phase-1.md`; `uvx ruff check` and `uvx ruff format --check` over the changed `.py` files | 577daff6 |
| 2 | S9: the pending-correction excusal through `rule_changes.parse` and `config.policy_root`, with its warning, seen red first; S10: `skills/writing-style/SKILL.md`'s citation sentence names the bold rule lead, and its `check:` line names the new module | `bin/test tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/github/test_rules.py -q` and `bin/seal rules --check`, exit codes read directly; the red run recorded in `trail/phases/phase-2.md` | |

## Operational impact

None for a deployer: no migration, no environment variable, no dependency.
For a contributor, the suite now refuses a citation of any tracked file's
section that the file does not have, where it refused only citations of
`skills/implement/SKILL.md` before. The failure direction is stricter: a
pull request that renames a heading cited outside `docs/` must correct its
citations in the same pull request.
