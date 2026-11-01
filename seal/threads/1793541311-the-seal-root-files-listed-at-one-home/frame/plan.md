# Implementation Plan: 1793541311-the-seal-root-files-listed-at-one-home (#1232)

## Technical context

The work touches three files; the policy changes are `frame/design.md` *Rule changes*, which the settle writes. Every coordinate is at the base, `cd694aa3`.

- `skills/implement/SKILL.md:87-99`, the paragraph of *Document layout — two roots, three lifetimes* that ends "what sits under `seal/threads/` lives as long as its work item:", leads into the fenced tree at lines 100-117. The paragraph after it, "The review round records live beside the work item they are about", stays. `skills/implement/SKILL.md:76` is the lifetimes table's row for the root above `threads/`; the row above it, line 75, holds K3.1's sentence, "A human approves `frame/plan.md`", which is #1102's and is not touched.
- `skills/verify/orchestration.md:433`, row `Findings by Location` of the table under *Measure the segment, and feed the flow log*.
- `skills/implement/scripts/seal.py:92-100`, the module docstring's paragraph opening "**What the reminder counts, and what it does not.**".
- `tests/behaviour/test_first_setup_asks_once.py#test_the_session_rule_sits_in_the_layout_section_of_the_skill` finds the section by `## Document layout` and `## Procedure`; both headings stay. `tests/behaviour/test_the_set_a_work_item_always_has.py#test_the_two_layout_trees_no_longer_show_it` pins the trees of `seal/README.md` and `templates/setup/seal-README.md`, which this work does not touch. `tests/text/test_no_passage_is_pasted_into_a_second_file.py#BASELINE` stores 2 for `README.md` with `skills/implement/SKILL.md`, and a lower count passes (design G12).
- Test modules that name a changed path at the base (executed, `git grep -l` over `tests/`): 22 for `skills/implement/SKILL.md`, 10 for `skills/verify/orchestration.md`, 13 for `skills/implement/scripts/seal.py`. 42 modules under `tests/` call a glob, a walk or `git ls-files`, so the set that reads a changed path through a directory is the crafter's to list at the phase boundary.

**The failure scenario of the chosen approach, six months on.** A file is added to the root, and its home row goes into `docs/the-record-layout.md` *seal/* through a design's `## Rule changes`, while `templates/setup/seal-README.md` keeps its own tree and is not updated. The template is then the one copy left to drift, read in every user's repository. That copy stays because it describes the directory it is written into, where the plugin's `docs/` is not beside it (design G4); the proofer reads it at review of the work item that adds the file, as it reads every list P1 finds.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| **A1** Replace the skill's tree with a link to `docs/the-record-layout.md` *seal/* and *seal/threads/<work-item-id>/*, drop the three prose lists for the same link, and give the home its two missing rows through `## Rule changes` | The scenario in *Technical context*: the setup template's tree drifts from the home | Chosen. One home for the list, and every copy that is not a fact about its own file leaves |
| **A2** Keep the skill's tree and add `config.md` to it, so it lists what the home lists | The next root or work-item file is added in one holder and not the other, as `config.md` was in the skill and `parity.md` and `pact.md` were in the table (design G5). A builder gains nothing from the tree: *3. The SDD file set* of the same skill already tables each work-item file with its writer and template, and every note the tree carries has a home elsewhere (design G11) | Rejected on `skills/core/SKILL.md` *The rule a mechanism is kept against*, "A fact has one source, and every other place links to it". The premise that would keep the structure, that a reader of the skill needs the picture in it, was checked against G11 and does not hold |
| **A3** Make the skill's tree the home, and have `docs/the-record-layout.md` *seal/* link it | Policy outranks the skill (`skills/implement/SKILL.md` *1. Read the documents that outrank the code first*), and `docs/README.md` *The records* names the record layout for where each kind of record lives. The settle writes `docs/` and not a skill, so a correction to the list would have no route through `## Rule changes` | Rejected |
| **A4** Keep the copies and add a test that compares each drawn tree with the *seal/* table | A check kept to hold two copies in step: the copy stays, and the check reads a drawing by a box-character grammar, which a drawing in another shape escapes. It adds a mechanism whose record of catches is nil on the day it is added | Rejected on `skills/core/SKILL.md` *The rule a mechanism is kept against*, "Nothing is kept beside the tree to stay in step with it" |
| **A5** Replace only the root half of the skill's tree, and keep the `threads/` half | The `threads/` half restates *seal/threads/<work-item-id>/* the same way, and the two already word the round record differently. A half tree under a sentence about both lifetimes reads as the whole | Rejected. The home holds both halves (design G2) |
| **A6** Leave the three prose lists (design Scope items 2 to 4), as the issue names only the tree | Each already omits files the root holds: `pact.md` and `README.md` in the skill's row and the docstring, `parity.md` and `pact.md` in the location row. A reader classifying a finding in `seal/pact.md` by the location row meets a list without it | Rejected on contract rule 12: the issue's *Done when* is every place that lists the root's files, and P2 lists these |
| **A7** Add the two rows by an `add` to *seal/* with no `from` | `add` places `to` at the end of the section's own text, after the table, so the settling session has to move two rows into a table the operation does not name | Rejected. A `change` whose `from` is the `seal/config.md` row puts the rows in the order the drawn trees list them |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Scope items 1 to 4 | P1 and P2 of `frame/design.md` re-run on the built tree, giving S1 and S2: no tree under `skills/`, and no window in the three files naming a subset of the root's files. `tests/behaviour/test_a_cited_section_stands_in_its_file.py` green for the new citations. The phase-boundary set of contract rule 2 over the three changed paths, from *Technical context* | |

One phase: the three edits are each a few lines, none depends on another, and a second phase would cost a spawn and a record. No case is added. The work adds no behaviour a case can pin: it removes copies and adds links, and the new links are held by the existing cited-section check.

## Operational impact

None for a deployer: no migration, environment variable, dependency or compatibility break. A user's builder reading `skills/implement/SKILL.md` follows one link to `docs/the-record-layout.md` for the file layout, where it read a tree. Until the settle after 0.27.3, `docs/the-record-layout.md` *seal/* lacks the `parity.md` and `pact.md` rows; the policy in force includes them through this design's `## Rule changes` (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
