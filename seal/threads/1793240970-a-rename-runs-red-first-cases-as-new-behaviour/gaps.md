# Closing memo: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

## Why this work exists

A rename or a move paid for a case written new and a `seal mutate` run its existing cases already made needless, and now one row of the verify skill says what proves it, which the crafter, the implement skill, the review and the sealer read.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The eval runs' case filter | `frame/plan.md` rows 1 and 2: `--case rule-crafter-rename` and `--case rule-crafter-slugify`. The runner matched no case and spent nothing: `No eval cases found matching --case "rule-crafter-rename"` | `--case '*rule-crafter-rename'` and `--case '*rule-crafter-slugify'` | `claude plugin eval --help`: "`--case <glob>` Filter cases by name glob", and `rule_cases.py#main` writes each case's name as `<agent> <directory>`, so a bare directory name matches nothing |
| Where the phase-boundary set is written | `frame/design.md` *Scope* item 5: contract rule 2's sentence and the *Scope* row "become step 7's set, in one command", and item 3 has step 7 state the set. Built: rule 2 states the set, and the *Scope* row and step 7 cite rule 2 | the build | `tests/text/test_a_moved_rule_leaves_its_definition.py` refused `agents/crafter.md` carrying "contract rule 2's own words", and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` refused the three files sharing runs of 15 words "where 0 were measured", with "Link to the home instead of copying it". `CLAUDE.md`: "A fact has one source, and every other place links to it" |
| Where the crafter is told to record a rename's proving cases | `frame/design.md` *Scope* item 3: "Step 8's record says, under `## What this phase found`, which existing cases proved a rename or a move." Built: step 5 says the cases and the census go into that section, and step 8 is unchanged | the build | `tests/text/test_a_language_section_of_writing_style_opens_alone.py` refused the heading inside step 8: "an agent's writing-style step names a heading skills/writing-style/SKILL.md does not have" |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide `ruff check` and `ruff format --check`, and the typecheck on this branch | executed by the orchestrator's broad gate at `36a89ab2` against `1e82fd0a`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |
| closed Whether `rule-crafter-count-words`, `rule-crafter-truncate` and `rule-crafter-is-palindrome` still pass against the branch's crafter. The plan ran `rule-crafter-slugify` alone as the arm that adds behaviour | re-homed to #1178 |

## Not done

nothing

## Fed back into the design

none
