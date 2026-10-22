# Phase 4: 1792627930-the-section-sign-is-still-syntax

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 152bcb40 |

## What this phase was asked

The record templates. Every comment and every guidance sentence leaves the
eight `templates/sdd-*.md`; each sentence is removed where its owner already
states it, or moved to the home `spec.md` names. Each case that pinned a
template sentence pins it at its home. `tests/test_a_record_carries_no_comment.py`
refuses a comment in a record template (S10). The record lists every
sentence and where it now stands (S11), and the five preloads, and
recomputes its coordinates at HEAD before the first edit.

Coordinates at HEAD 910072a2, before the first edit (executed):
`git grep -n '<!--' -- 'templates/sdd-*.md'` printed 24 lines in the eight
templates (the frame counted 23 at a16acb40), and
`git grep -l -E 'sdd-(spec|plan|questions|routing|overview|phase|round|guarantee)' -- tests`
printed 17 modules. The new case, run at that HEAD, failed listing the same
24 lines (executed).

## What this phase found

**Where every sentence now stands (S11, Q7).** "Stated" means the home
already said it and the sentence was deleted; "moved" means it was written
there in this phase; "placeholder" means a body line became an
angle-bracket placeholder carrying its words. Each home is a file and its
heading.

| Template | Sentence | Now |
|---|---|---|
| spec | holds WHAT the work delivers | stated: `skills/implement/SKILL.md` *3. The SDD file set*, the `spec.md` row |
| spec | the policy documents outrank this file | stated: `skills/implement/SKILL.md` *1. Read the spec before the code* |
| spec | the framer cites them and does not restate them | stated: `docs/the-record-layout.md`, its opening rule that a file links to a rule's home and does not restate it |
| spec | a pact clause is cited as `pact:<name>/...@<hash>` and `pact-check` reads it | stated: `docs/the-pact.md` *The pact anchor* |
| spec | what is in and what is out; schema deltas by coordinates | placeholder |
| spec | a scenario row becomes the review's stage-1 checklist and the tests' skeleton | stated: `skills/code-review/SKILL.md` *Two stages, in order*, and `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test* (the case named in the scenario table) |
| spec | the `## Rule changes` grammar and the no-change block | stated: `skills/settle/SKILL.md` *Rule changes*, which `agents/framer.md` points the framer at |
| spec | the `## Removes` rule, its no-change block, a phase's unnamed removal going to `overview.md` | stated: `docs/the-reader-registry.md` *A frame names what its work removes* |
| spec | why a removal is recorded ("lost between two phases") | stated in other words: `agents/framer.md`, the rule **A removal is named once, at the frame**; the pin moved there |
| spec | a question lives in `questions.md`, not in prose | moved: `skills/implement/SKILL.md` *3. The SDD file set* |
| spec | the frame's mark: why CI needs it, `framer` as `<who>` | stated: `agents/framer.md`, the rule **Your mark goes at the foot of `spec.md`** |
| spec | `<who>` takes the `Planning` row's two answers, a disagreeing mark is refused, one shape with the plan and routing lines | moved: `skills/implement/SKILL.md` *3. The SDD file set* |
| spec | a reframe adds its line under the mark | stated: `docs/the-review-record.md` *The run* and `agents/framer.md` |
| plan | holds HOW in phases, the Design Gate's artifact | stated: `skills/implement/SKILL.md` *3. The SDD file set*, the `plan.md` row |
| plan | the approval line, its writer, moment and shape | stated: `skills/implement/orchestration.md` *The plan is approved at the spawn*; the shared shape moved with the mark paragraph above |
| plan | technical context; operational impact | placeholder |
| plan | vertical slices; the table is the task list; Status is empty or a commit, a tick and `done` refused | stated: `skills/implement/SKILL.md` *3. The SDD file set* |
| plan | the builder fills the cell as the phase closes; a rebase orphans the commits and the rebaser re-reads the column | moved: `skills/implement/SKILL.md` *3. The SDD file set* |
| plan | a phase's discoveries go to `phases/phase-N.md` from `templates/sdd-phase.md` | stated: `skills/implement/SKILL.md` *3. The SDD file set*, the phase row, and `agents/smith.md` |
| questions | holds decisions only a human can make | stated: `skills/implement/SKILL.md` *3. The SDD file set*, the `questions.md` row |
| questions | the framer inherits what existing behaviour answers | stated: `skills/implement/SKILL.md` *1. Read the spec before the code* ("A question you can answer is not a question") |
| questions | the three `Who can answer` values; the framer does not own the answers; who writes `Status` | moved: `skills/implement/SKILL.md` *3. The SDD file set* |
| questions | the orchestrator carries a row into `## Rule changes` when it drains | stated: `skills/implement/SKILL.md` *6. Drain the rows before the broad run, and keep the records* |
| routing | what the file holds, who commits it, CI reads it, the vocabulary is fixed | stated: `skills/implement/orchestration.md` *What the answer writes* |
| routing | `Review`, `Destination`, the `no work item` answer, neither answer is no enforcement | stated: `skills/implement/orchestration.md` *What the answer writes* and *Question 1* |
| routing | `Planning` is recorded, not asked, and the ladder decides | stated: `skills/implement/orchestration.md` *What the answer writes* |
| routing | answers are written without backticks; why four rows ship as placeholders; `no` is never written where the question was not put | moved: `skills/implement/orchestration.md` *What the answer writes* |
| routing | the `Implementation` criterion (finding out or writing down, `scribe`, replaceability) | moved: `skills/implement/orchestration.md` *What the answer writes* |
| routing | `Automation` names no party, unchecked is a value, held by `hooks/question-gate.py`; `Answer pressed` | stated: `skills/implement/orchestration.md` *Question 2* and *What the answer writes* |
| routing | one declaration per branch | moved: `skills/implement/orchestration.md` *What the answer writes*, a `Branch` row in its table |
| routing | what `## Why this way` holds | moved: `skills/implement/orchestration.md` *What the answer writes* |
| overview | the memo's terms; a lasting rule goes to `docs/` with its test | stated: `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show* and *2. Implement test-first, and let each rule name its test* |
| overview | the `## Not verified` shape, closing by the word `closed`, the open item worded `closed` | stated: `skills/implement/SKILL.md` *4. The closing memo — only what the diff cannot show* |
| overview | the placeholder row fails the check | moved: same section |
| overview | `## Not done` is prose because it holds decisions | moved: same section |
| phase | what the record holds and who writes it | stated: `skills/implement/SKILL.md` *3. The SDD file set*, the phase row |
| phase | why `## What this phase was asked` exists; what `## What this phase found` holds and why it is the durable home | moved: `skills/implement/SKILL.md` *3. The SDD file set* |
| phase | a removal is not recorded in a phase record | stated: `skills/implement/SKILL.md` *3. The SDD file set*, `docs/the-reader-registry.md` and `agents/smith.md` |
| round | the file, its writer, the fix pass's two lines, words only, the grammar | stated: `docs/the-review-record.md` *The round record* |
| round | the `target:` line and the extension line | stated: `docs/the-review-record.md` *The round record* and *The run* |
| round | the `original:` line | stated: `agents/warden.md` step 5 and `skills/legacy-parity/SKILL.md` |
| round | each label's meaning; when a ready pull request fails | stated: `docs/the-review-record.md` *The round record*, *The run* and *What the check reads at the pull request* |
| round | the grounds open with the unit (`regression:`) or why the close does not hold (`reopens:`) | the first stated in *The run*; the second moved: `skills/code-review/SKILL.md` *The record* |
| round | `## Confirmations` and `## Not judged` | stated: `docs/the-review-record.md` *The round record* |
| guarantee | who writes and commits the file | stated: `agents/sealer.md` and `docs/the-review-record.md` *The guarantee* |
| guarantee | a row per act; `holds` or `does not hold: <what came back>` | stated: `docs/the-review-record.md` *The guarantee*, and the template's placeholder cell |
| guarantee | the three verdict shapes and the owner's answer line | stated: `agents/sealer.md` step 5, which the verdict placeholder now names |

No sentence went into an agent definition, so Q5's measured route was not
needed.

**Preload bytes after phase 4 (executed):** unchanged from phase 3: framer
25194, smith 24668, warden 25300, sealer 23302, scribe 18486.

**Pins moved (each seen red against the old homes before the homes changed,
executed: 9 failed).** `tests/test_a_question_says_who_can_answer_it.py`,
`tests/test_a_phase_hands_the_next_one_a_record.py`,
`tests/test_waiver_decided_at_start.py` (the criterion now read from the
orchestration; the vocabulary of each optional row now read out of its
placeholder `<first, or: second>`), `tests/test_chain_check.py` (the spec
template's empty `## Rule changes` is refused like the comment it replaced;
the round template carries no `reopens:` or `original:` line, and the review
skill names the `reopens:` grounds), `tests/test_the_sealer_guarantees.py`,
`tests/test_the_set_a_work_item_always_has.py`,
`tests/test_unverified_rows_close.py` (the skill's example row is now run
through `check_file` and read as closed),
`tests/test_the_pull_request_language_is_the_repositorys.py` and
`tests/test_the_rules_have_one_owner.py` (the template is no carrier of the
regression sentences). Two cases went with their subject:
`test_plan_names_the_phase_record_path` (the skill's phase row holds the
path, pinned by `test_skill_file_set_table_carries_the_phase_row`) and
`test_the_phase_templates_own_path_comment_matches_the_round_templates`
(neither template has a path comment); `overview.md` records both.

**A gap phase 3 left, found here.** Phase 3 added two modules to the
writing rule's `check:` line, and
`tests/test_a_language_section_of_writing_style_opens_alone.py` holds that
line as a constant. The module was not in phase 3's boundary run, which
took the modules phase 3 edited; it was red from 9b2ec5e4 until this phase
updated the constant at 1a263ac0 (executed: red in this phase's first
boundary run, green after).

**Mutation-check of the new case, each killed (exit 0, executed):** the
opener test, and the glob widened to every template.

**The boundary run.** Every module that names a template, every module that
names `skills/implement/SKILL.md`, `skills/implement/orchestration.md` or
`skills/code-review/SKILL.md`, the size and wrap modules and the meta
modules: 3232 passed, 10 skipped (executed). The modules that name any file
this branch touched are 135 of the suite's 145, which is the broad gate, so
no phase ran them all.
