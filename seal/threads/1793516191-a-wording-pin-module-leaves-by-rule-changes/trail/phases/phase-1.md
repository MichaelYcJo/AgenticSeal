# Phase 1: 1793516191-a-wording-pin-module-leaves-by-rule-changes

## What this phase found

**The frame holds, with one wording the successor issue should not copy.** The coordinates were opened before the rehearsal (executed: `git grep -n one_word_one_meaning -- . ':!seal/threads'` in the worktree at `ad642d3f`). The three policy lines stand where G6 says: `docs/the-broad-gate.md:33`, `docs/the-pact.md:18` and `docs/the-pact.md:31`. `skills/writing-style/SKILL.md` names the module at lines 247 and 276. The two pins stand at `tests/text/test_a_language_section_of_writing_style_opens_alone.py:50` and `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77`. `seal/follow-up.md` holds no row about the module (read). The wording is in design *The successor issue*, which says "the four docstrings" and names no path. The tree holds six lines in four test files, and two of the six are `#` comments, not docstrings:

| File | Line | Kind |
|---|---|---|
| `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | 57 | comment in `SCANNED` |
| `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | 107 | docstring of `flat` |
| `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | 333 | docstring of `test_the_scanned_set_reaches_the_file_a_rule_gets_restated_in` |
| `tests/behaviour/test_chain_hooks_hardening.py` | 637 | comment above `EMPHASIS` |
| `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` | 19 | module docstring |
| `tests/text/test_edits_go_through_the_edit_tool.py` | 19 | module docstring |

#1197's body names the same four files (executed: `gh issue view 1197 --json body`). The rehearsal built to the frame as it stands, and the table is for the successor's text. Judged against design S5, which asks that the grep list equal the list *The successor issue* names.

**The rehearsal ran in one scratch clone, which is removed.** Executed: `git clone --no-local -q <the worktree> <scratchpad>/1793516191-a-wording-pin-module-leaves-by-rule-changes/clone`. The clone stood at `ad642d3f` on `refactor/1197-a-wording-pin-module-leaves-by-rule-changes`. Before any change, `bin/seal rules --check` there exited 0 and printed `seal rules: all 281 check lines in 55 rule files hold.` The directory, with the `.venv` that `bin/test` built in it, was removed with `rm -rf` after S5 (executed).

**The three `to` values were written with the `Edit` tool, as the design spells them.** The line-18 sentence was wrapped at the paragraph's width, after "names one of". That choice is the settle's at the real settle (`skills/settle/SKILL.md` *The settling session's procedure* step 2), and `tests/behaviour/test_docs_line_wrap.py` passed over it in S3. `git diff --stat` in the clone listed `docs/the-broad-gate.md` with 1 line changed and `docs/the-pact.md` with 4 (executed).

**S2 holds.** Executed in the clone: `bin/seal rules --check >/dev/null 2>&1; echo "exit=$?"` printed `exit=0`, and the run printed `seal rules: all 281 check lines in 55 rule files hold.` The count is unchanged because each item rewrites a line and adds none. Executed: `bin/seal rules docs/the-broad-gate.md`, which lists under `check, line 33:` the target `tests/skills/test_broad_gate.py` with that module's docstring line, so the new target resolves. `bin/seal rules docs/the-pact.md` lists line 18 with `tests/hooks/test_config.py` alone and line 31 with `tests/skills/test_pact_check.py` and `tests/hooks/test_config.py`.

**S3 holds.** Executed in the clone, one command: `bin/test tests/github/test_rules.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_the_gate_names_every_step_ci_runs.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/test_censuses.py tests/hooks/test_config.py tests/skills/test_pact_check.py tests/skills/test_broad_gate.py tests/behaviour/test_one_word_one_meaning.py -q`. It exited 0 with `1110 passed, 1 skipped in 9.03s`. The skipped case is `tests/skills/test_broad_gate.py:1126`, whose reason reads `the shell here is not cmd.exe`.

**S4 holds: `tests/skills/test_broad_gate.py` was seen red against the mutated verdict line, and green after the restore.** The three `to` values were first committed in the clone as `c103c834`, which existed only there, so the mutation ran over a committed tree (`agents/crafter.md` *Commit before you mutate, and restore from `seal mutate`'s copy*). Executed in the clone:

```
bin/seal mutate skills/verify/scripts/broad_gate.py --replace 'GATE_PASSED = "BROAD GATE PASSED   {names}"' 'GATE_PASSED = "SEALED   {names}"' --tests "bin/test tests/skills/test_broad_gate.py -q" --cwd <clone>
```

It exited 0 and printed `red: the cases failed against the mutation (exit 1)`. The cases run printed `3 failed, 313 passed, 1 skipped`. The three are `Test_gate::test_accepts_a_green_tree_and_runs_every_check_in_order`, `Test_main::test_the_fixture_branch_passes` and `Test_main::test_a_workflow_that_is_not_utf8_leaves_the_run_as_it_was`. After the restore, `shasum` of the file and of `git show HEAD:skills/verify/scripts/broad_gate.py` both read `cc93c8e17885a7edba446e227448030b5d54554d`. Then `bin/test tests/skills/test_broad_gate.py -q` exited 0 with `316 passed, 1 skipped`. The `GATE_PASSED` constant at `skills/verify/scripts/broad_gate.py:2825` was the unit mutated, because it is the line every passing run's stdout opens with (design G8).

**S5 holds: the one refusal is `skills/writing-style/SKILL.md:276`, and the grep lists the successor's places and no other.** Executed in the clone: `git rm -q tests/behaviour/test_one_word_one_meaning.py`, then `bin/seal rules --check`, which exited 1 and printed:

```
seal rules: skills/writing-style/SKILL.md:276: 에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다: tests/behaviour/test_one_word_one_meaning.py does not exist
seal rules: 1 refused in 281 check lines of 55 rule files.
```

Executed: `git grep -n one_word_one_meaning -- . ':!seal/threads'`. It listed the 24 rows of `.test_durations` and 12 lines in 10 files. Each line maps to an item of design *The successor issue*:

| Line | Item it answers |
|---|---|
| `skills/writing-style/SKILL.md:276` | the check line turns to `check: none reader: the proofer at review` |
| `tests/text/test_a_language_section_of_writing_style_opens_alone.py:50` | `WRITING_RULE_CHECKS` follows it |
| `skills/writing-style/SKILL.md:247` | the sentence of *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* at lines 245 to 248 |
| `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77` | `APPLIES_THE_SHARED_GUARD` loses the module's row |
| `skills/verify/scripts/session_cost.py:63` and `hooks/lib/config.py:1414` | the two comments |
| the six lines in the first table above | "the four docstrings" |
| `.test_durations`, 24 rows | the 24 rows |

The module's own line 950 left with the module. No line falls outside the list.

**How the list was made, and where it is a sample.** The grep reads one spelling, `one_word_one_meaning`, so on its own it is a search for one wording (contract rule 12). Phase 1 widened it with two searches, and the first of them was a sample too. Executed: `git grep -n -w` on the module's 24 case names and on two of its constants, `SWEEP_MODULE` and `LITERAL_SEAM`, outside the module, `.test_durations` and `seal/threads`. The module defines 55 top-level names, so this search took 26 of them and left out 26 constants and the helpers `flat`, `pact_texts` and `without_the_policy_span` (review round 1, finding 5). It listed one line, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77`, which is already on the list. The search over all 55 names is the one that makes the identifier list whole, and it stands in `frame/design.md` *The successor issue*, its *How the list was made* bullet. The fix pass after round 1 ran it again at `c66f09cf`, with the names taken from the module by `grep -oE '^(def [A-Za-z0-9_]+|[A-Z0-9_]+ =)'` (executed). It found 55 names, 24 of them cases. Leaving out the lines that hold `flat`, which name other units, it listed the same one line. Executed: `git grep -n -i` on `one_word`, `one word, one meaning`, `one word one meaning` and `one-word-one`, with every line holding `one_word_one_meaning` taken out. It listed nothing. A sentence that describes the module in prose without naming it by path or identifier is a spelling no search lists. That open part is the successor's reviewer's to read.

**The phase adds no behaviour to the worktree, so it wrote no case and ran no `seal mutate` there.** Its diff is this record, `gaps.md` and the Status cell of `frame/plan.md`. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* gives prose under `seal/threads/` the first row, where what can fail is whatever parses the files. The phase-boundary set is the modules that read this work item's records. `tests/behaviour/test_chain_hooks_hardening.py` asks every directory with a frame for a closing memo, `tests/skills/test_unverified_check.py` reads every closing memo under `seal/threads/`, `tests/github/test_rules.py` copies every `frame/*.md`, and `tests/test_censuses.py` reads every tracked text file. Executed in the worktree with `gaps.md` and this record written: `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/skills/test_unverified_check.py tests/github/test_rules.py -q`, which exited 0 with `486 passed`. Phase 1 left `tests/test_censuses.py` out of that command, and the module fails on a home path this record's line 18 held until the fix pass after round 1 (review round 1, finding 1). Executed: `bin/seal unverified seal/threads/1793516191-a-wording-pin-module-leaves-by-rule-changes`, which exited 0 and read `1 closing memos · 3 open · 0 closed · 0 unreadable`.
