# Implementation Plan: a pull request body past GitHub's length limit folds its longest parts

## Technical context

The tree as read at `e685d989b`.

`skills/code-review/scripts/pr_body.py#_composed` (lines 776-845) builds the part below `HEADING` as one flat list of `(line, source)` pairs: the seal mark, the changelog's section laid out by `_laid`, `FOLD`, the summary, then the blocks of `_built`, `_rounds`, `_gate`, `_gaps` twice and `_questions`, all laid out together, and `FOLD_END`. It then refuses each copied line that equals `HEADING`, opens an unclosed comment, holds a `details` tag or a closing keyword. `compose` (852-857) puts `HEADING` in front. `main` (1014-1080) composes `below` first, reads `first_part` second, and writes `first part + HEADING + below`. `compared` (976-995) composes `below` the same way and hands it with the body and `first_part` to `_check` (945-973), which compares lines through `difflib`. `chain_check.py#body` (1815-1857) calls `compared` and composes nothing itself.

The fold needs two things the flat list does not give. The sections must stay separate units until the fold has chosen, and the first part's length must be known before the fold, while today `main` and `compared` read it after `_composed`. The build keeps the refusals over copied lines where they run now, over every section before any fold, and reads the first part only after them. So the order in which a record's refusal and a language key's refusal reach a caller does not move.

Failure scenario of the chosen approach, six months on: a record grows a new section, and its author adds a builder beside `_built` and the others without listing it among the foldable sections and their paths (`frame/design.md` *Data & interfaces* D2). The new section is then never folded, and a body long because of it is refused under D5 while a shorter body was within reach. The mitigation is that the foldable sections and their paths stand in one table in `pr_body.py`, next to the builders, and S1's case composes from every builder's records.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Fold whole sections, the longest first, keeping each heading and putting one fixed line per path `frame/design.md` D2 lists in place of its text, a directory named once as the directory | A section that is one long record and one short one loses both from the page. The issue's measured table (`frame/design.md` G1) shows one section, `## Not verified`, whose fold alone brings that body within the limit | Chosen. It is the owner's decision applied at the unit the issue measured, and the fold set is a function of six lengths |
| 2. Fold smaller parts, each round record and each `gaps.md` section on its own | The order mixes parts of different sections, so the page shows some of the rounds and not others, and each new round record can move which rounds are folded. Each part needs its own fold line, and `_round`'s output has to be split by record. The issue's numbers need one fold either way | Not taken. It keeps more on the page in some bodies and costs a second ordering rule and more fixed lines in all of them |
| 3. Name the commit in the fold line, as the issue's *Decision* says "at the commit" | CI checks out the pull request's merge commit, so the commit `compared` reads there is not the branch head the body was written at, and the body arm refuses every folded body (`frame/design.md` G5). Every later commit would also change the body | Not taken. The fold line names the record's path in the work item, as every other fixed line does, and the reader opens it in the branch the pull request shows |
| 4. Measure the body with the mark only where `seal_mark` writes it | A body within 114 characters of the limit fits at the sealer's check and passes the limit once the mark is added, so the run after the seal folds a section and changes copied lines, against `docs/forms/the-guarantee.md` *The guarantee* (`frame/design.md` G4) | Not taken. The fold always leaves the mark's room (D4); the cost is at most 114 characters of a body that fits |
| 5. Write a body past the limit when nothing more can fold, and let `gh pr create` refuse it | That is #1559's own failure: the refusal arrives after the seal, when `gh pr create` runs, and the orchestrator shortens the body by hand into one the check refuses | Not taken. `seal pr-body` refuses and writes nothing (D5), so the sealer's `--check` meets the same refusal before any verdict |
| 6. Let `compared` fold as the received body folded, reading the fold lines it finds there | The check would accept any fold set a person wrote, so the body would stop being a function of the records, which is what the body arm holds (`docs/checks/the-pull-request-check.md` *What the check reads at the pull request*) | Not taken. `compared` composes from the records and folds by its own composition's length |
| 7. Keep `_composed`'s flat list and fold afterwards, by finding the section headings among the laid lines | A copied record line equal to a section heading, such as a `## Not done` line inside a round record's prose, would be read as a section start, and the fold would cut the copy there. Keeping the structure is safe only where no copied line can equal a fixed heading, and `_composed` refuses only `HEADING` among such lines (read: lines 810-818) | Not taken. The structure changes: the sections stay separate units until the fold has chosen, and are laid out after |
| 8. Skip the refusals of copied lines inside a folded section, since those lines leave the page | Whether a section folds depends on the length of other records, so a bad line would pass at one commit and be refused at a later one when another record shrank | Not taken. Every copied line is refused or passed before any fold (D5, S8) |
| 9. Count the body in code points with Python's `len`, the unit the one source reports (`frame/design.md` G7) | Where GitHub counts UTF-16 code units, a body within `LIMIT` by `len` but holding characters outside the Basic Multilingual Plane passes GitHub's limit, and the fix fails at `gh pr create`, which is #1559's own failure, with nothing in the tree to see it | Not taken. The count is in UTF-16 code units (D1), which fits under either unit, at the cost of one extra unit for each such character |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 6, through *Data & interfaces* D1 to D7 | The new cases of *User scenarios & acceptance* S1, S2, S4 to S8 and S10, each seen red as its cell states; S3's case green unchanged; S9's search printing nothing; `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/evals/test_rule_cases.py -q` green | |

## Overlap with the release

The spawn names one other open work item of `release/v0.38.3`, #1557 (`docs/1557-the-process-has-no-name`, pull request #1558, sealed and open), read at `e6d1945a0` with its frame. It meets this work in no file and in no check either reads: the two lists of changed files share none, and no file this work changes cites the core heading #1557 renames (`frame/design.md` G16). The order is still fixed, by `routing.md` *Version* and `skills/implement/merge-order.md`: #1557 moves `.claude-plugin/plugin.json` to 0.38.3 and merges first, and this work item leaves the version alone and merges after it.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1557 | No common file. This work's files cite no core heading that `tests/behaviour/test_a_cited_section_stands_in_its_file.py` would read after #1557's rename | #1557 | It carries the release's version move and is sealed. Merging the base into this branch after it lands costs no conflict, since no file is shared |

## Operational impact

None for a deployer. The fold changes the body only where the body would pass GitHub's limit, so every body within it is composed as before (S3). A work item past the limit whose `pr.md` and `changelog.md` alone pass it now stops at `seal pr-body` with exit 1 instead of at `gh pr create`. This pull request moves no version (`routing.md` *Version*).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
