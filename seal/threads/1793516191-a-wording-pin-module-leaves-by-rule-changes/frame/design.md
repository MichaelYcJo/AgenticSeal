# Design: 1793516191-a-wording-pin-module-leaves-by-rule-changes

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| **G1** `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* (read) | A pull request does not edit the policy root, `docs/` here (`seal/config.md` holds no `Policy root` row, read). The three `check:` lines that name `tests/behaviour/test_one_word_one_meaning.py` change only through this design's `## Rule changes`, which the settle after the release writes into `docs/`. |
| **G2** `skills/settle/SKILL.md` *A rule has one shape*, and the module docstring of `.github/scripts/rules.py` (read) | `seal rules --check` refuses a `check:` line whose target is gone. It excuses only a line inside a section that a pending `remove` with no `from` takes out, and a pending `change` excuses nothing. So the module cannot leave in this pull request: until the settle writes the three `to` values, the lines still name it. A check line holds targets or `none reader:`, never both, and a rule ends with one check line. `RULE_FILES` reads `docs/*.md` and `skills/*/SKILL.md`, and no file under `seal/`, so the `to` values below meet the reader only once they stand in `docs/` (read: `.github/scripts/rules.py:68-76`). |
| **G3** Milestone `release: 0.27.1`, its description (executed: `gh api repos/:owner/:repo/milestones/77 --jq .description`) | The owner's order: this release writes the rule changes for the module's three policy `check:` lines, and the module's removal follows the settle that applies them. |
| **G4** #1197 body (executed: `gh issue view 1197 --json title,body,milestone,state`, 2026-11-01) and its one comment (executed: `gh issue view 1197 --comments`, 2026-11-01) | The body lists what the removal owes and gives two *Done when* bullets. The comment retitled the issue `refactor:` and changes nothing the issue asks. |
| **G5** `v0.27.0:seal/threads/1793411151-judgment-where-meaning-is-the-question/frame/design.md` Scope item 4 and its `trail/phases/phase-1.md` (executed: `git show`) | #1167 decided the module goes whole, because its cases pin a phrasing and the absence of a looser one, and a case that turns red when the wording changes and the meaning does not is what `skills/core/SKILL.md` *Judgment is spent where meaning is the question* calls the worst result. That decision is not argued again here. Its phase 1 listed the references outside `docs/` with `git grep -n test_one_word_one_meaning`. |
| **G6** The three lines (executed: `git grep -n one_word_one_meaning -- . ':!seal/threads'`) | `docs/the-broad-gate.md:33`, under *One act, one owner, and the owner is the orchestrator*; `docs/the-pact.md:18` and `docs/the-pact.md:31`, both under *The words*. Each line names another target beside the module, so the issue's first *Done when* bullet asks a `change` that drops the module from each and no line turns to `none reader:`. |
| **G7** `docs/the-pact.md` *The words*, the paragraph ending at line 18 (read) | Its last sentence says "a case holds other words for them out of the shipped text". That case is the module's `test_the_pacts_words_keep_one_meaning`. Once the module goes the sentence is false, so the `change` for line 18 rewrites the sentence as well as the line (`skills/core/SKILL.md` *The rule a mechanism is kept against*: a change removes what stood on the old fact in the same change). |
| **G8** `tests/skills/test_broad_gate.py:2445`, `:2460-2461`, `:2472`, `:2739`, `:2757` (read) | The gate's own cases assert that its stdout opens `BROAD GATE PASSED` or `BROAD GATE FAILED` exactly, and that a run queues no stamp. That is the behaviour `docs/the-broad-gate.md` *One act, one owner, and the owner is the orchestrator* states in the rule its line 33 ends, and the module's gate and stamp cases held the same fact as a sweep of the gate's text. The `change` for line 33 names this module in the module's place. |
| **G9** `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* (read, lines 250-290) | Its second rule, a word the repository defined keeps that meaning, ends `check: tests/behaviour/test_one_word_one_meaning.py` (line 276). Its third rule already ends `check: none reader: the proofer at review`. The skill is no policy document, so its line changes in the removal's own change, and `tests/text/test_a_language_section_of_writing_style_opens_alone.py#WRITING_RULE_CHECKS` pins that line beside it. |
| **G10** `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* item 3, and `docs/issues-and-milestones.md` *One thing reads a milestone, and it can stop a release* (read) | The pull request body carries `Closes #N`, and the release workflow closes the issue when the release reaches `main`. `.github/scripts/release_completeness_check.py` refuses the release while `release: 0.27.1` holds an open issue the release branch does not claim. The removal cannot be built before the settle, and `docs/release-checklist.md` *2b. Settle what earlier releases left behind* runs the settle only when the owner calls it (read). |
| **G11** `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* and `skills/settle/SKILL.md` *What `--apply` does* (read) | The settle's `--apply` removes this work item's directory, this frame with it, in the same change that writes the `to` values. A frame cannot carry work that only starts after that change. It stays readable at the release tag: `git show v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md`. |
| **G12** #1216 body (executed: `gh issue view 1216`) | At the last settle (#1214), eleven cases pinned a `from` that a released `change` replaced, and four `to` values shared a 15-word run with another shipped file, so `tests/text/test_no_passage_is_pasted_into_a_second_file.py` failed. This design's `from` and `to` values were probed against both (*Data & interfaces*, *The probes*). |
| **G13** `docs/the-record-layout.md` *A commit after the build brings its changelog fragment along* (read) | "A commit that changes nothing a release note states owes the fragment nothing." This pull request changes no file a release ships (*Scope*), so it owes no `changelog.md`. The precedent is `seal/threads/1793490088-each-kind-of-restatement-is-measured/`, which wrote none and was sealed (read: its `guarantee.md:53`). |
| **G14** `docs/` policy in force (executed: `grep -ln 'the-broad-gate.md\|the-pact.md\|one_word_one_meaning' seal/threads/*/frame/design.md`) | One unsettled design names the module, `1793490088-each-kind-of-restatement-is-measured`, and its `## Rule changes` is the no-change block; it cites #1197 for the module's removal. No unsettled design changes either section. `seal/follow-up.md` holds no row about the module (read). |

## Scope

In:

1. Three `change` items in `## Rule changes`, one for each `check:` line G6 names. Each drops the module from its line. The line-33 item names `tests/skills/test_broad_gate.py` in its place (G8). The line-18 item also rewrites the sentence G7 names, so it names the proofer as the reader of the pact's words.
2. The account the issue's second *Done when* bullet asks for: for each of the module's 24 cases, the fact a reader acts on and what holds it once the module goes (*Data & interfaces*, *What each case held*). The removal's change cites this table, at the release tag G11 gives.
3. The carrier of the removal. This pull request's body closes #1197. The orchestrator files one successor issue before `seal pr-body` runs, and the body names it. The successor holds what the removal owes and the precondition that it waits for (*Data & interfaces*, *The successor issue*).
4. A rehearsal of what the settle will meet. In a scratch clone, the crafter writes the three `to` values into `docs/` as the settle would, runs the checks that read either document, and then deletes the module there and runs `seal rules --check` again, to show that the list the successor carries is whole. The crafter records the result in `trail/phases/phase-1.md`.

Out, each with its reason:

- **Every place outside `docs/` that #1197 lists waits for the removal.** These are the two sections of `skills/writing-style/SKILL.md`, the two test pins, the comments at `skills/verify/scripts/session_cost.py:63` and `hooks/lib/config.py:1414`, the four test docstrings and the 24 rows in `.test_durations`. Each one states a fact that holds until the module goes: a check line naming a module that runs, a pin on that line, a classification of a case that exists, a comment saying the module holds a rule it holds, a docstring citing a file that is there, and a duration row for a case that runs. Changed now, each would state a false fact for the time between this merge and the removal (read: each coordinate, *Data & interfaces*).
- **The module's removal itself.** The module goes after the settle (G2, G3).
- **A wider excuse in `.github/scripts/rules.py`**, which would let the module go in this pull request (`plan.md` *Alternatives considered*, row A3).
- **A check line for the rules in `skills/verify/SKILL.md` *The hand-back's labels carry the claims, and the one seal is the sealer's* and `skills/verify/orchestration.md` *Measure the segment, and feed the flow log*.** Neither carries one now, and the module's removal leaves them as they are (*What each case held*, rows 8 and 17).
- **#1216's notice of pins and copies.** It is that issue's work. This design runs the same readings by hand on its own values.
- **No changelog fragment** (G13).

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The settle reads three operations | Given this design at HEAD, when `skills/settle/scripts/rule_changes.py#parse` reads it with policy root `docs`, then it returns three `change` operations and no error | executed by the framer from a clone (*The probes*, P3); `chain-check` reads the same reader at the pull request |
| S2 The rule reader passes the new lines | Given a scratch clone with the three `to` values written into `docs/`, when `seal rules --check` runs there, then it exits 0, and `tests/skills/test_broad_gate.py` resolves as a target | phase 1, in the clone |
| S3 No check that reads either document turns red | Given the same clone, when these modules run, then each passes: `tests/github/test_rules.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_the_gate_names_every_step_ci_runs.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/test_censuses.py`, `tests/hooks/test_config.py`, `tests/skills/test_pact_check.py`, `tests/skills/test_broad_gate.py` and `tests/behaviour/test_one_word_one_meaning.py` itself, which still reads `docs/the-pact.md` and `docs/the-broad-gate.md` | phase 1, in the clone, one command |
| S4 The line-33 target holds the rule | Given the same clone, when `skills/verify/scripts/broad_gate.py`'s passing verdict line is changed to open with `SEALED`, then `tests/skills/test_broad_gate.py` fails, and with the change reverted it passes | phase 1, seen red in the clone (contract rule 15's method, applied to a target this design names) |
| S5 The removal's list is whole | Given the same clone, when the module is deleted there and `seal rules --check` runs, then the one refusal is `skills/writing-style/SKILL.md:276`. When `git grep -n one_word_one_meaning -- . ':!seal/threads'` runs, it lists the places *The successor issue* names and no other | phase 1, in the clone |
| S6 The diff holds the work item's records alone | Given the branch at HEAD, when `git diff --stat ad4556f4...HEAD` runs, then every path is under `seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/` | the sealer, at its guarantee |
| S7 #1197's removal is carried | Given the pull request body, when it is read, then it carries `Closes #1197` and names the successor issue's number, and the successor's body holds what *The successor issue* lists | the sealer, reading the body and `gh issue view <successor>` |

## Data & interfaces

### What each case held

The method is rule 12's second one: the module taken apart into each of its 24 cases (executed: `grep -n '^def test_' tests/behaviour/test_one_word_one_meaning.py`, 24 lines). A fact's other holder was found with `git grep -l -F` on the phrase the case pins, over `tests` and `evals` with the module left out (executed), and then read at the coordinate. "The proofer" means the reader `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* names for its second rule once the removal turns that rule's line to `check: none reader: the proofer at review`. That line is the `check: none reader:` naming the issue's second *Done when* bullet asks for. It covers every case below whose fact is a word's one meaning.

| # | Case | The fact a reader acts on | Held once the module goes by |
|---|---|---|---|
| 1 | `test_the_start_is_the_moment_before_the_first_edit` | the first edit waits for the routing answer | `tests/hooks/test_routing_edit_gate.py`, the behaviour (read: `git grep` lists it with the phrase); the phrase, the proofer |
| 2 | `test_every_once_in_the_readme_states_its_grain` | the mode gate asks once per session per repository, the review-skill gate once per session per working tree | `tests/hooks/test_mode_gate.py:321`, whose case reads that README row against the marker's key, and `tests/hooks/test_review_skill_gate.py:137`, `:143` (read) |
| 3 | `test_the_korean_readme_states_the_same_grains` | the Korean edition says the same grains | the proofer |
| 4 | `test_the_refusal_is_named_by_who_it_addresses` | the routing check denies the model, which puts the question to the person | `tests/hooks/test_routing_edit_gate.py`, the target of the rule's own line `docs/the-routing-check.md:71` (read) |
| 5 | `test_the_bound_is_on_the_review_run_and_never_on_the_cycle` | the bound is on the review run | `docs/the-review-record.md` *The run*, whose rules end `check: run-ends-with-verifying-round` and `check: tests/text/test_the_rules_have_one_owner.py` (read, lines 421 and 424); the absent old heading is history |
| 6 | `test_the_crafter_calls_the_whole_thing_a_review_run` | `agents/crafter.md` cites *The run* for the bound | `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which holds that a cited section stands in its file (read: its module docstring); the absent phrase, the proofer |
| 7 | `test_the_row_that_could_not_be_true_is_corrected_not_reworded` | an old routing row is in neither implement file | history, which `tests/behaviour/test_waiver_decided_at_start.py:25` records in its docstring; the wording, the proofer |
| 8 | `test_the_owner_states_that_one_seal_is_final` | the one seal is the sealer's `guarantee.md` | `tests/text/test_the_rules_have_one_owner.py`, which pins that sentence (executed: `git grep -l -F 'the one seal over the'`); the section's other two sentences, the proofer |
| 9 | `test_the_two_definitions_name_what_they_actually_keep` | the proofer claims no seal; the sealer takes the last one | the proofer |
| 10 | `test_the_readme_says_what_the_proofer_audits` | the proofer audits the crafter's labels | the proofer |
| 11 | `test_no_instructing_document_leaves_an_instance_anonymous` | a bare "the seal" names whose | the proofer, by `skills/writing-style/SKILL.md` *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* |
| 12 | `test_the_gate_never_says_sealed` | the gate's verdict line is `BROAD GATE PASSED` or `BROAD GATE FAILED`, never `SEALED` | `tests/skills/test_broad_gate.py` (G8), the new target of `docs/the-broad-gate.md:33`; seen red as S4 |
| 13 | `test_the_gate_calls_its_run_no_seal_by_construction` | the gate's prose calls its run no seal | `tests/skills/test_broad_gate.py` for what the run prints; the prose, the proofer |
| 14 | `test_the_gate_sweep_reads_a_seal_that_ends_a_sentence` | none: it pins case 13's own pattern | leaves with case 13 |
| 15 | `test_no_instructing_document_gives_the_stamp_to_the_broad_gate` | the stamp is the sealer's, and the gate draws none | `tests/skills/test_broad_gate.py:2460-2461`, no stamp queued; `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:136`, the orchestrator is told the broad run draws nothing (read) |
| 16 | `test_the_stamp_sweep_reads_the_gates_run_and_the_passive` | none: it pins case 15's own pattern | leaves with case 15 |
| 17 | `test_the_owner_states_what_a_segment_is_and_what_it_is_not` | a segment is one agent's stretch of a chain, and a spawn cycle is not one | `tests/skills/test_session_cost.py:1854`, `:3518`, `:3543` for what `--segments` reports (read: case names); the sentence, the proofer |
| 18 | `test_no_shipped_document_calls_a_spawn_cycle_a_segment` | no file says the loose phrasing | the proofer |
| 19 | `test_the_sweep_reads_across_a_string_literal_seam` | none: it pins the module's own `LITERAL_SEAM` | leaves with the module |
| 20 | `test_folding_the_seam_cannot_hide_an_instance_it_would_have_found` | none: it pins the module's own sweep constants | leaves with the module |
| 21 | `test_flat_is_what_folds_the_seam_and_it_folds_python_only` | none: it pins the module's own `flat` | leaves with the module |
| 22 | `test_the_pacts_words_keep_one_meaning` | the pact and the signer are named one way | `tests/hooks/test_config.py`, the `Signer` table of `seal/pact.md` (read: `:1518`, `:1528`); the words, the proofer, as the line-18 `to` says |
| 23 | `test_no_pact_text_names_a_signer_the_way_0_18_did` | the pact's texts say `signer`, and a 0.18.x header still reads | `tests/hooks/test_config.py:1556`, `:1581` and `tests/skills/test_pact_check.py` for the old header's reading (read); the word, the proofer |
| 24 | `test_no_live_text_says_the_word_0_19_0_renamed` | no tracked file says the old word for a signer | the proofer, as for case 23 |

No case asks for a new case. Each fact is either held by a case that reads the behaviour, or is a word's one meaning, whose reader the writing-style line names. Cases 14, 16 and 19 to 21 hold a fact about the module itself and leave with it.

### The successor issue

The orchestrator files it before `seal pr-body` runs, in the milestone `frame/questions.md` Q1 gives. Its body holds:

- **The precondition.** It is built after the settle that writes this design's three `to` values into `docs/` has merged. Before that merge, `seal rules --check` refuses the removal (G2).
- **What the removal owes.** It is #1197's *What the removal owes* list less its first bullet, which this design answers. Each place outside `docs/` in that list: `skills/writing-style/SKILL.md` *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* line 276 turns to `check: none reader: the proofer at review`, and `tests/text/test_a_language_section_of_writing_style_opens_alone.py#WRITING_RULE_CHECKS` follows it. The sentence of *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* that names the module (lines 245-248) is rewritten so it no longer says a check holds the word. `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py#APPLIES_THE_SHARED_GUARD` loses the module's row. The comments at `skills/verify/scripts/session_cost.py:63` and `hooks/lib/config.py:1414` and the four docstrings no longer cite the module. The 24 rows leave `.test_durations`. The module goes.
- **How the list was made whole.** `git grep -n one_word_one_meaning -- . ':!seal/threads'` and `seal rules --check` after the deletion (S5).
- **The facts.** *What each case held* above, cited at `v0.27.1:seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes/frame/design.md`.
- **Done when.** #1197's two *Done when* bullets, with the first one's settle already applied.

### The probes

- **P1. A test that pins a `from`** (#1216's first half). Executed: `git grep -n -F -e 'holds other words' -e 'a case holds' -e '<each from line>' -- tests evals`. It listed one line, `tests/behaviour/test_release_hygiene.py:157`, whose text is "a case holds them to", which is another sentence and not this `from`. Executed: `git grep -l` on the two document names under `tests/`. It listed seven files, and S3 runs each, `tests/censuses.py` through `tests/test_censuses.py`. Of those, only `tests/behaviour/test_one_word_one_meaning.py` pins a sentence of *The words*, the definition sentence, which no item changes.
- **P2. A `to` that copies a passage** (#1216's second half). Executed: `python3 -I <scratch>/test_tmp_windows.py <worktree>`. The probe re-implements the normalisation of `tests/text/test_no_passage_is_pasted_into_a_second_file.py` (its `words`, `windows` and `shared_counts`, with `WINDOW = 15` from `tests/text/test_a_moved_rule_leaves_its_definition.py:85`) and imports nothing from the repository. It applies the three items to the 61 corpus files in memory. No pair's count rose. `docs/the-broad-gate.md` gains 15 new windows and `docs/the-pact.md` gains 44, and none of them is in another corpus file. Both documents share no window with any other file before or after.
- **P3. The block parses, and each `from` stands in its section.** Executed: `python3 -I <scratch>/test_tmp_parse.py <clone> <this file>`, where `<clone>` is a `git clone --no-local` of the worktree at `bf1a5e3f`. The probe loads the clone's `skills/settle/scripts/rule_changes.py` and calls `parse(<this file>, "docs")`, which returned three `change` operations, `errors=[]` and `unread=[]`. Then it calls `section_lines` on each document. *One act, one owner, and the owner is the orchestrator* spans `docs/the-broad-gate.md` lines 8 to 42, and *The words* spans `docs/the-pact.md` lines 8 to 31. Each `from`, with whitespace collapsed, is found in its section. The third `to` is found there too, before any settle, because dropping the last target leaves a prefix of the `from` line. The dry run will report that `to` as found, and the `from` beside it as found as well.

## Rule changes

- change
  file: docs/the-broad-gate.md
  section: One act, one owner, and the owner is the orchestrator
  from: check: tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py
  to: check: tests/skills/test_broad_gate.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py
- change
  file: docs/the-pact.md
  section: The words
  from: The three names are the owner's, and a case holds other words for them out of the shipped text.
    check: tests/behaviour/test_one_word_one_meaning.py tests/hooks/test_config.py
  to: The three names are the owner's, and a text that names one of them another way is the proofer's to find at review.
    check: tests/hooks/test_config.py
- change
  file: docs/the-pact.md
  section: The words
  from: check: tests/skills/test_pact_check.py tests/hooks/test_config.py tests/behaviour/test_one_word_one_meaning.py
  to: check: tests/skills/test_pact_check.py tests/hooks/test_config.py

## Removes

- nothing
  why: The pull request adds this work item's records and nothing else, and adds no mechanism. The three rule changes take the module out of three policy check lines at the settle, and the module and every reference to it leave in the successor issue's change, whose design names them in its own `## Removes`.

Framed 2026-11-01 by framer, before the build.
