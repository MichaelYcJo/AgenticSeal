# Design: 1793853198-tests-name-the-gate-that-exists

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| #1352 (executed: `gh issue view 1352 --repo MichaelYcJo/AgenticSeal --json title,body,comments`, 2026-11-05) | The issue has no comments. Its *Scope* covers each sentence under `tests/` that describes the commit gate as present. Each such sentence names the mechanism that now does what it describes, names the moment it describes, or drops the clause. Its *Scope* puts the cases' assertions out. *Done when* asks for no such sentence at the commit that changes them, found by a method the pull request names |
| Milestone `release: 0.32.4` (executed: `gh api repos/MichaelYcJo/AgenticSeal/milestones/88`) | The milestone states its purpose: "docstrings and comments under tests/ and .github/scripts/ state only what the tree holds now, and text that costs lines with nothing to catch its drift is removed before it is corrected". It is a patch, and it builds no feat. It names `tests/conftest.py` and the hook tests as the one ground #1352 may share with #238 |
| `skills/core/SKILL.md` *The rule a mechanism is kept against* (read) | "A change rewrites the text it amends in place … History goes to git, the release notes and the work record." A mechanism stays only while what it caught outweighs what it costs. This decides D2 (no new case) and the removal of the dead helper (D1 row 1) |
| #1355's frame, `seal/threads/1793799285-a-pinned-path-is-removed-or-cut-to-its-grounds/frame/design.md` *D1* and *D2* (read) | This is the precedent for per-line dispositions and for adding no case that refuses a spelling. Its principle is the milestone's: text whose drift nothing catches is removed before it is corrected. D1 below uses three of its dispositions in this work's terms |
| #1346's records, `seal/threads/1793787547-each-statement-is-corrected-to-the-tree/gaps.md` *Not done* and `trail/phases/phase-3.md` (read) | Phase 3 found the 18 lines and classified three as saying the gate is gone. It judged the class out of its scope because these sentences describe a removed hook and do not cite a removed test module or case. This work classifies the other fifteen (D1, and *Left as they stand* below) |
| #1027's squash, `61a8455a` (executed: `git log --grep='#1027'`; `git show --diff-filter=D --name-only 61a8455a`) | It removed `hooks/commit-review-gate.py`, `hooks/commitgate.py`, `hooks/githooks.py`, `hooks/hook-install.py`, `hooks/git/pre-commit.py`, `hooks/git/post-commit.py`, `hooks/git/reference-transaction.py` and `hooks/answers.py`, `hooks/answer-write.py`, `hooks/answer-clear.py`. It added `hooks/routing-edit-gate.py`. So the class includes the git hooks the gate ran through, as well as the gate itself (method M2 below) |
| `docs/checks/the-routing-check.md`, its lead, *The edit check* and *At the pull request* (read) | "A session's routing is checked where the session acts, at its edit tools before the first edit, and again at the pull request; this plugin writes nothing into a clone's git hooks." So no git hook runs before the floor, and a declaration nobody can read is answered at the next edit, not at the next commit. No pending `## Rule changes` operation names this file or `docs/running/the-review-and-parity-arms.md` (executed: `grep` over `seal/threads/*/frame/design.md`) |
| `hooks/routing-edit-gate.py`, module docstring (read, lines 1-40 and 249-257) | "The declaration is read through `routing.for_branch`, so every way it cannot be read is no declaration, and the edit is refused." This is the present mechanism that a sentence saying "the commit gate asks" or "is caught at the next commit" now names |
| `hooks/question-gate.py:9` and `hooks/routing-edit-gate.py:22,256` (read) | Both resolve the branch through `routing.worktree_branch` and the root through `optin.repo_root`. `tests/hooks/test_question_gate.py:215` already says "the branch resolves as the edit gate resolves it" |
| `tests/hooks/test_routing_edit_gate.py`, its case list (executed: `grep -n "def test_\|malformed\|vocabulary\|no declaration"`) | No case runs a malformed declaration or a `Review` answer outside the vocabulary through the hook. So the two sentences in `tests/hooks/test_routing.py` that point at "the gate's own case" for these point at no case (D1 rows 9 and 12) |
| `tests/conftest.py#fired` (executed: `git grep -n -P "\bfired\("` over the tree outside `seal/threads`; `git log -S'fired(' -- tests evals hooks skills`) | Nothing calls it. Its last caller left with #1160, which removed the worktree guard. Its docstring describes the commit gate's shape: "a gate with two ways on denies the FIRST time … Detection tests care that the gate saw the command" |
| `agents/crafter.md` (executed: `grep -n -i 'waiver\|waive'`) | It carries no waiver example. So the item "its own waiver example as the patch contract rule 9's gate reads a commit out of" in `tests/text/test_a_moved_rule_leaves_its_definition.py` names something no definition keeps (D1 row 19) |
| `ruff.toml:45` (read) | `"hooks/*.py" = "py39"  # its `*` crosses a `/`, so hooks/lib/ too`. The tree's own example of the glob crossing a `/` is a path under `hooks/lib/` (D1 row 17) |
| Bare commits on the lines D1 rewrites (executed: a 7-to-40-hex word pattern over each D1 range, then `git cat-file -e <token>^{commit}`) | The one token found is `1790644505`, a work item id, and it is no commit. So no line on D1's list is #1359's, and #1359 holds no commit-gate sentence that is this work's |
| `seal/follow-up.md` (read) | No row waits on this work |
| Process changes (executed: `gh release view --json body` for `v0.32.3`, and a `grep` of `### Process changes` rows over `seal/threads/*/changelog.md`) | The `v0.32.3` notes hold no `### Process changes` table. Ten fragments hold one, and no row changes how a test docstring or comment is written. The nearest are #1317's rows, which say rule text carries no history |
| `routing.md` (read, committed at `c54f0040`) | Planning is framer, Implementation is crafter, Review is through the review chain, Destination is to open the pull request, and Automation is yes. Nobody is asked anything for this run, so `frame/questions.md`'s person row is built on its default |

**The class, and the three methods that listed it (contract rule 12).**

- **M1, the issue's wording.** `git grep -n -i "commit gate" -- tests` printed 18 lines in 8 modules (executed, 2026-11-05, at `c54f0040`). These are the issue's lines.
- **M2, from what produced the defect.** The removal produced the drift, so the names of what it removed were searched. Each file #1027 deleted was searched by its name under `tests/` (executed). This added `tests/censuses.py`'s `matches` docstring. The other hits say the file is gone, or are a case's input data. The 104 functions, classes and constants defined in the deleted modules were also searched as words under `tests/` (executed, from `git show 61a8455a^:<file>`). This found no prose about the gate, only calls into live modules that happen to share a name (`hooks/mode-gate.py`, `hooks/routing-edit-gate.py`, `hooks/lib/gate.py`, `skills/implement/scripts/seal.py`).
- **M3, every line written while the gate stood.** `git blame 61a8455a..HEAD` was run on each of the 157 tracked `.py` files under `tests/`. It marked 66,824 lines unchanged since #1027's squash or older (executed). Those lines were filtered on `gate`, `git hook`, `pre-commit`, `post-commit`, `at the commit`, `commit hook`, `inside git`, `asks again` and `un-silenc`, and each hit was read. This added `tests/conftest.py#fired`, `tests/hooks/test_routing.py:1`, `:263-264` and `:536`, `tests/behaviour/test_waiver_decided_at_start.py:196-197` and `:705-706`, `tests/behaviour/test_a_commit_names_its_repository.py:3-8`, `tests/censuses.py:892`, `tests/hooks/test_launch.py:204` and `tests/text/test_a_moved_rule_leaves_its_definition.py:26-27`.
- **This is a sample.** The blame step lists every line written before #1027, so that part is whole. The word filter is not whole, because the class is open over spellings. The part no method reached is a line, written before or after #1027, that describes the commit gate without any of those words. That part is the proofer's to read in the diff's files, and no list claims it.

**D1. Each sentence in the class takes one of three dispositions.**

- **N, present.** The sentence names the mechanism that does today what the sentence describes. Where that is the routing check, it is the edit check, `hooks/routing-edit-gate.py`, which refuses the next edit on the branch. The docstring does not list every reader of `hooks/lib/routing.py`, because a list of readers drifts with nothing to catch it.
- **D, drop.** The clause or item names something the tree no longer holds, and nothing does its job. It goes, and the rest of the sentence stays.
- **R, remove.** The text is removed whole. Here that is a dead unit of code, or a paragraph whose only subject is the removed gate.

| # | Coordinate at `c54f0040` | Disposition | What the rewrite leaves |
|---|---|---|---|
| 1 | `tests/conftest.py#fired`, lines 577-585 | R | The function goes, docstring and body. Nothing calls it (*Grounding*). `decision_of` above it stays |
| 2 | `tests/conftest.py:1716`, `opted_in_repo`'s docstring | N | The fixture is an opted-in repository at a path holding non-ASCII. No gate is named by a name the tree lacks |
| 3 | `tests/hooks/test_question_gate.py:203`, the section comment | N | "the branch and the root resolve as the edit gate's do", in the words line 215 already uses |
| 4 | `tests/hooks/test_routing.py:1-2`, the module docstring's first line | N | `hooks/lib/routing.py` records the routing answer where the hooks read it. Nothing re-derives it |
| 5 | `tests/hooks/test_routing.py:4-5` | N | A declaration at `seal/threads/<work-item-id>/routing.md` is what the edit check reads, through `routing.for_branch`. The failure direction in the sentences after it stays |
| 6 | `tests/hooks/test_routing.py:7` | N | What a hook does with an answer is that hook's own file's |
| 7 | `tests/hooks/test_routing.py:62`, the assertion's failure message | N | An absent optional row must read as nothing, or every declaration like the file carries an answer its author never gave; the message is printed only after the declaration parsed, so it names no refusal. The asserted predicate does not change |
| 8 | `tests/hooks/test_routing.py:109-110` | N | A third or fourth axis that invalidated the committed declarations would make each one no declaration, and the edit check would refuse the branch it names |
| 9 | `tests/hooks/test_routing.py:263-264` | N, then D | `maybe later` makes the file no declaration, so the edit check refuses the next edit. The sentence "The gate's own case runs the same answer through the hook" goes, because no such case exists. "this one asks the parser" stays as the case's own statement |
| 10 | `tests/hooks/test_routing.py:414` | N | As row 8, for the declarations that omit each row |
| 11 | `tests/hooks/test_routing.py:536-537` | N | "no declaration" means the edit check refuses the edit. "Not silence: silence would make a corrupt file into a standing waiver" stays. The past narration at `:533` stays as it is (*Left as they stand*) |
| 12 | `tests/hooks/test_routing.py:555-556` | D | The sentence naming the commit gate's case goes, because no such case exists. The case's own statement, that it asks the reader, stays |
| 13 | `tests/behaviour/test_waiver_decided_at_start.py:196-197`, the comment | N | A wrong answer in the first two rows makes the file no declaration, and the edit check refuses the next edit on the branch. The rest of the comment, which says a wrong third answer is contradicted by nothing, stays |
| 14 | `tests/behaviour/test_waiver_decided_at_start.py:705-706` | N | `for_branch` finds no declaration, and the edit check refuses the next edit on that branch |
| 15 | `tests/behaviour/test_a_commit_names_its_repository.py:3-8` | R | The sentence on "the gate half" goes, and so does the milestone-49 measurement of the stops that half made. The opening still names the rule's work item and issues. The paragraph at `:19-21` already says #1027 removed every gate that read a commit, and it states the reason that remains |
| 16 | `tests/censuses.py:892`, the `floor_syntax` comment | D | "a git hook" leaves the list of what runs before any floor is checked |
| 17 | `tests/censuses.py:952`, `matches`'s docstring | N | The example of `*` crossing a `/` names a file under `hooks/lib/` that the tree holds, as `ruff.toml:45`'s comment does |
| 18 | `tests/hooks/test_launch.py:204` | D | "a git hook" leaves the list, as in row 16 |
| 19 | `tests/text/test_a_moved_rule_leaves_its_definition.py:26-27` | D | The item "its own waiver example as the patch contract rule 9's gate reads a commit out of" leaves the crafter's list. The list's other items and its closing sentence stay |
| 20 | `tests/behaviour/test_waiver_decided_at_start.py:44-46`, the comment above `ORCH` | D | The sentence "The per-command waiver stays in `SKILL.md`, because the implementer is who types the command." leaves: #1027 removed that waiver, and the module's own case at `:749-756` holds that it is gone. Round 1 found it (`trail/rounds/round-1.md` finding 1); M3's words did not include `waiver` |
| 21 | `tests/text/test_a_moved_rule_leaves_its_definition.py:435-436`, the docstring of `test_the_crafters_four_rules_stand_with_their_enforcers` | N | "S4's four rules each keep their paragraph, their clauses and a `check:` line, and the waiver stays one sentence" becomes a statement that #1027 retired the fourth rule, the waiver, and that the case holds it gone, and "These four" becomes "These three". The case asserts the waiver is absent. Round 1's fix pass found it reading finding 1's class (`git grep -n -i "waiv" -- tests`). The case's name keeps "four", outside *Scope* |

**Left as they stand.** These lines were read and are outside the class:

- They say the gate is gone, or they date what it did: `tests/hooks/test_gate.py:6`, `tests/hooks/test_cmdline.py:5-8`, `tests/text/test_edits_go_through_the_edit_tool.py:16-17`, `tests/text/test_the_direct_answer_owes_the_sealers_record.py:9` and `:20`, `tests/behaviour/test_chain_hooks_hardening.py:4-5`, `tests/behaviour/test_a_probe_that_commits_says_so.py:1` and `:7`, and `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:177` and `:287`.
- They tell in the past tense a defect that passed through the gate, and they are the case's grounds: `tests/hooks/test_optin.py:82` and `tests/hooks/test_routing.py:533`. Neither describes the gate as present (plan A5).
- They are a case's asserted data or its input, which the issue puts out: `tests/text/test_edits_go_through_the_edit_tool.py:51-53`, `tests/test_censuses.py:788`, `tests/skills/test_test_layout.py:85-86`, `tests/behaviour/test_no_document_names_the_old_roots.py:173`, and the strings at `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:288` and `:304`.
- Their "the gate" is true of the edit check that reads the declaration today: `tests/behaviour/test_waiver_decided_at_start.py:4`, `:182` and `:760-761`, and `tests/hooks/test_routing.py:275`. Line 19 of the first file and `:751` tell the past.
- It is `pre-commit` the framework, not this plugin's hook: `tests/skills/test_deferral_check.py:211-222`.
- It is #1381's file, and it says the git hooks are gone: `tests/hooks/test_dispatch.py:1155-1169`.

**D2. No case is added to keep the class from returning.** `plan.md` *Alternatives considered* A2 holds the grounds. The weighing follows `skills/core/SKILL.md` *The rule a mechanism is kept against*:

- A spelling check cannot tell "the commit gate reads" from "the commit gate's arms went with #1027". Nine correct lines use the words.
- On the day it lands it has caught nothing, because this work removes the class by hand.

## Scope

In scope:

1. **The 21 rows of D1.** Each row is rewritten, dropped or removed as its row says. Any other sentence in the same docstring paragraph or comment block that leans on the rewritten clause changes with it.
2. **The record of each row.** The phase record lists each of the 21 rows with its path, its line at the base the phase was built on, its disposition, and the text that replaced it or `removed`. The record also names the three methods and the commands they ran at the phase's commit, as *Done when* asks.

Out of scope:

- **Shipped files outside `tests/`.** `hooks/lib/routing.py`'s module docstring still speaks of "the gate" in the present ("Imported by the gate and by the hygiene check", "so the gate goes back to asking"), and it names the commit gate in the past at line 4 (executed: `git grep -n -i "commit gate" -- . ':!seal/threads' ':!tests'`). #1352 and the milestone scope `tests/` and `.github/scripts/`. Whether it joins is `frame/questions.md` Q1.
- **`.github/scripts/`.** No line there names the commit gate (executed, the same `git grep`). #146 holds `roll_flow_measurement_issue.py`.
- **The cases' assertions and their data.** The issue's *Scope* puts them out. The one failure message D1 rewrites (row 7) changes no predicate (plan A6).
- **A hook-level case for a declaration that does not parse.** Rows 9 and 12 drop the pointers to such a case because it does not exist. Adding one is a new mechanism with no recorded catch. `tests/hooks/test_routing.py` holds the reader that the edit check calls.
- **Siblings' sentences.** `tests/hooks/test_dispatch.py` and `hooks/dispatch.py` belong to #1381, and the clause at `tests/hooks/test_routing.py:533` that cites `dispatch.py`'s `except` stays untouched. #238 holds a sentence in the version-check tests, and the rows here in `tests/conftest.py` (1 and 2) are not it. #1359 holds bare commits, and no line on D1's list carries one (*Grounding*). #1382 holds the READMEs.
- **Past narration of the gate.** See *Left as they stand* and plan A5.
- **`.claude-plugin/plugin.json`'s version.** It is the release's to set.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1. The issue's wording names no present gate | Given the phase's commit, when `git grep -n -i "commit gate" -- tests` runs, then it prints 9 lines, each in *Left as they stand*: `test_cmdline.py`, `test_gate.py`, three in `test_edits_go_through_the_edit_tool.py`, two in `test_the_direct_answer_owes_the_sealers_record.py`, `test_optin.py`, and `test_routing.py`'s past narration | the command at the phase's commit, its output in the phase record, each line read against *Left as they stand* |
| S2. No git hook is listed as running | Given the phase's commit, when `git grep -n -i -E "git hook|hooks/git/" -- tests` runs, then every line it prints says the git hooks are gone, or is a case's data | the command at the phase's commit, its output in the phase record |
| S3. The dead helper is gone | Given the phase's commit, when `git grep -n -P "\bfired\(" -- .` runs outside `seal/threads/`, then it prints nothing | the command at the phase's commit |
| S4. No assertion changed | Given each touched module at the base and at the phase's commit, when each is parsed with `ast` and every docstring is removed, then the two dumps are equal. The two exceptions are `tests/conftest.py`, which loses `fired`, and `tests/hooks/test_routing.py`, whose one assertion message (D1 row 7) differs | a probe that compares `ast.dump` of each file's blob at both commits, read with `git show`; its output in the phase record |
| S5. The touched modules still pass | Given the phase's commit, when each touched test module runs narrow, then it passes. Its `test_census` and `tests/test_censuses.py` pass for the touched files too | the crafter's narrow runs, labelled in the phase record. The broad gate is the orchestrator's |
| S6. Each row is accounted for | Given the phase record, when it is read against D1, then each of the 21 rows appears with its disposition and its replacement text or `removed` | the phase record against D1 |

## Data & interfaces

There are no interface changes. The only code removed is `tests/conftest.py#fired`, which has no caller. Every other change is a docstring, a comment, or the failure message of one assertion.

## Rule changes

- nothing
  why: This work corrects test docstrings and comments to the routing check that `docs/checks/the-routing-check.md` already states, and it applies `skills/core/SKILL.md` *The rule a mechanism is kept against* as written. No policy sentence changes, and none is missing for a writer of a test docstring to read.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| a helper with no caller, and its docstring describing the commit gate's two prompts | `tests/conftest.py#fired` | nothing. Its last caller left with #1160, and `decision_of` serves every case that reads a decision |
| the "gate half" sentence and the milestone-49 measurement of the stops it made | `tests/behaviour/test_a_commit_names_its_repository.py`, the module docstring's first paragraph | git and #662's records. The docstring's last paragraph states the reason that remains |
| two pointers to a hook-level case that does not exist | `tests/hooks/test_routing.py#Test_parse.test_refuses_a_review_answer_outside_the_vocabulary` and `#Test_module.test_a_routing_md_that_does_not_parse_is_left_out`, their docstrings | nothing. The cases name what they ask, which is the parser and the reader |
| "a git hook" in two lists of what runs before any floor | `tests/censuses.py`, the `floor_syntax` comment; `tests/hooks/test_launch.py#Test_module.test_what_runs_before_any_floor_is_linted_at_the_floor`'s docstring | nothing. `docs/checks/the-routing-check.md` says the plugin writes nothing into a clone's git hooks |
| the crafter's waiver example in the list of what a definition may keep | `tests/text/test_a_moved_rule_leaves_its_definition.py`, the module docstring *Where this draws the line* | nothing. `agents/crafter.md` carries no waiver, and the waiver left with #1027 |
| the sentence that the per-command waiver stays in the implement skill, because the implementer types the command | `tests/behaviour/test_waiver_decided_at_start.py`, the comment above `ORCH` | nothing. #1027 removed that waiver, and the module's case holds it gone |
| "the waiver stays one sentence" | `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafters_four_rules_stand_with_their_enforcers`, its docstring | the same docstring's sentence that #1027 retired the waiver and the case holds it gone |
| (the mechanism check) | this design | It adds no mechanism: no case, census, mark or rule (D2). So nothing has to be taken out in return |

Framed 2026-11-05 by framer, before the build.
