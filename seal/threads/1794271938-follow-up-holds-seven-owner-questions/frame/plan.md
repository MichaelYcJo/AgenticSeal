# Implementation Plan: 1794271938-follow-up-holds-seven-owner-questions

## Technical context

The tree as read at `eccf1bcb7`.

`seal/follow-up.md:38-48` holds the schedulable table, each row answered by "the repository owner". `tests/text/test_a_rider_reaches_its_file.py#rows` (`:29-42`) reads a table by its `## ` heading and splits on it, so the heading has to stay for `test_no_schedulable_row_carries_a_coordinate` to run; it skips the header row by its first cell, `Item`.

`tests/github/test_close_issues_on_release.py:1160-1178` parses its script with `ast` inside one case. `tests/github/test_label_merged_on_release_branch.py:30` and `tests/github/test_tracker_labels.py:26` already import helpers from that module, so a module-level `argv_words` there is reached the way `load` is. The folded readers stand at `tests/github/test_release_completeness_check.py:571-574` and `tests/github/test_label_merged_on_release_branch.py:397-408`.

`tests/behaviour/test_waiver_decided_at_start.py#offered` (`:291-298`) reads the two answers of a row's placeholder `<first, or: second>`. `lib/routing.py:72-74` holds the `Implementation` constants.

`skills/implement/SKILL.md:323-328` states the Status cell. `tests/behaviour/test_the_set_a_work_item_always_has.py#KNOWN_PROSE` holds line 114 of that file verbatim and refuses any line that counts files, so the paragraph is rewrapped without touching line 114 and without writing a count of files.

What breaks in six months. First, a script that writes through a name, such as `GH = "gh"` used as an argv's first word, passes every case that reads through `argv_words`; that escape is kept open by the issue and is written in `argv_words`' docstring so the next reader meets it there. Second, `deferred #N` can be typed for an issue that does not exist, as the removed row 2 argued; nothing checks it, and the proofer and the sealer read the plan against the tracker. Third, the empty table can refill with a row whose answerer carries a condition, and only the party that writes or reviews the row reads it, which is the trade *Alternatives considered* row 6 takes.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Row 7: one module-level `argv_words` in `tests/github/test_close_issues_on_release.py`, imported by the two other modules | A rename or split of that module breaks two imports, loudly, at collection. | Chosen. One reader, one docstring on what it closes, and the import has precedent (*Technical context*). |
| 2. Row 7: a copy of the reader in each module | The day one copy learns to resolve module-level names, the other two keep the escape, and nothing says they differ. `skills/core/SKILL.md` *The rule a mechanism is kept against* asks for one source. | Rejected. |
| 3. Row 7: the reader in `tests/conftest.py` | Every test module imports a helper only the `.github/scripts` cases use, and its docstring on `gh` argvs sits among fixtures that have nothing to do with it. | Rejected. The modules that use it already import from `test_close_issues_on_release`. |
| 4. Row 7: keep the folded readers, the structure that stands | A forbidden argv split by one comment passes, as measured on 2026-09-22 against the sibling case (the issue, row 7). The premise that would keep them, that nobody comments inside an argv, is the premise the measurement broke. | Rejected. The owner's decision converts them. |
| 5. Row 7: also resolve module-level names before comparing | A different checker, with false positives of its own to argue, for an escape nobody has used. | Rejected. The issue keeps the escape open. |
| 6. Row 6: remove lines 83 and 84 and keep the header pins at 81 and 82 | A row whose answerer carries a condition passes every case, and only the party that writes or reviews the row catches it. | Chosen. The guard caught nothing real on record and refused one honest row (`frame/design.md` G8). The core forbids a script a list of spellings, and the pins keep the rule's sentences in the file a row's writer reads. |
| 7. Row 6: remove the whole case | The header's sentence *no condition attached* can be deleted with nothing red, and it is the sentence a writer of a row reads. | Rejected. The pins cost one line each. |
| 8. Row 6: widen the guard to read the shape of a condition | Any comma or future-tense clause refuses honest rows; the removed row 6 already argued this. | Rejected. A reading guessed from words is reported and never blocks (`frame/design.md` G1). |
| 9. Row 6: also remove `test_no_schedulable_row_carries_a_coordinate`, whose table is now empty too | A row tied to a coordinate lands in the table and nothing says it belongs in a `# RIDER:` comment. | Rejected. It reads one exact shape, `path.ext:N`, not a list of spellings, and the issue does not name it. |
| 10. Row 3: add the `offered` comparison to the third-axis case and rename it | The old name's key stays in `.test_durations` until CI prices the suite again (`frame/design.md` G16), and `seal/follow-up.md` row 3 cites the old name as `path#name`, so `tests/behaviour/test_a_cited_section_stands_in_its_file.py` is red from phase 2 until phase 3 removes that row (folded after phase 2). | Chosen, as the issue's table says. |
| 11. Row 3: merge the placeholder-axis cases into one case parametrized over `Implementation`, `Planning` and `Automation`, replacing the structure | Each case's docstring records a different finding (round 1's M4, #84's phase 4, #151's shape). A merged case keeps one docstring, and a reader of a red can no longer tell which finding it reopens. The premise that keeps them apart, that their docstrings carry distinct records, was checked by reading `:177-229`, `:230-289` and `:301-345`. | Rejected. |
| 12. Row 3: keep the name `three_answers` | The name says three where the parser and the placeholder hold two, and a reader looks for a third answer. | Rejected. |
| 13. Row 2: state the third value in `frame/design.md` `## Rule changes` | `skills/settle/rule-changes.md` *Rule changes* refuses a `file:` outside the policy root, and `skills/implement/SKILL.md` is outside it. | Rejected. The sentence is an edit in this pull request (`frame/design.md` G6). |
| 14. Row 2: pin `deferred #N` in `skills/implement/SKILL.md` with a text case | The pin holds one spelling of prose that agents read and the proofer reviews, and the paragraph carries no `check:` line today. | Rejected. The proofer reads the sentence. |
| 15. Row 2: add a new sentence after the paragraph and leave *empty or holds the commit* standing | Two sentences, one saying two values and one saying three, and the reader chooses (contract rule 19). | Rejected. The sentences are rewritten in place. |
| 16. The empty table keeps its heading and header row | The file reads as a list with nothing on it, which is what its header prose says it should normally hold. | Chosen. *Riders waiting on a file another branch holds* already stands so, and `rows` needs the heading. |
| 17. The citations of a row: rewrite only the one the issue names, in `test_close_issues_on_release.py` | Four sentences go on citing rows that left, two of them since `a53699ec5` (`frame/design.md` G12). | Rejected. Emptying the table makes every citation of a row false, and contract rule 19 asks the same commit to correct what stood on it. |
| 18. File an issue for a `gh api` write in `release_completeness_check.py` (`frame/design.md` *Scope*, *Out*) | A gate whose case says it writes nothing could write through `gh api --method PATCH`, and no case reads it. | Not this work's. The orchestrator decides whether it earns an issue. |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* item 1 | The three modules `tests/github/test_close_issues_on_release.py`, `tests/github/test_release_completeness_check.py` and `tests/github/test_label_merged_on_release_branch.py` green. Each converted case shown red, against the converted reader, with a forbidden argv split by a comment planted in its script, then the plant reverted (`frame/design.md` S1); the label case also shown red with its `--add-label` argv removed (`frame/design.md` S2). The same plant run against the folded case before conversion, green, goes in the phase record. | `2705f8d4f` |
| 2 | `frame/design.md` *Scope* item 2 | `tests/behaviour/test_waiver_decided_at_start.py` green. The new comparison shown red with `lib/routing.py#BY_CRAFTER`'s value changed and the template untouched, while the substitution loop above it stays green, then reverted (`frame/design.md` S4). | `4d8031dc0` |
| 3 | `frame/design.md` *Scope* items 3, 4, 5, 6 and 7 | `tests/text/test_a_rider_reaches_its_file.py`, `tests/behaviour/test_the_set_a_work_item_always_has.py`, `tests/test_conftest.py`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py` and `tests/behaviour/test_docs_line_wrap.py` green. `grep -c "the repository owner" seal/follow-up.md` prints 0 (`frame/design.md` S5). `git grep -n "follow-up"` outside `seal/threads/` read hit by hit for a sentence citing a row (`frame/design.md` S7). | `38ae1b728` |

What each changed or removed test caught on record, and what holds its rule after the change:

- `tests/github/test_release_completeness_check.py#Test_module::test_the_gate_writes_nothing` and `tests/github/test_label_merged_on_release_branch.py#Test_module::test_the_script_only_ever_creates_a_label_and_adds_one`. Caught: nothing on record (`frame/design.md` G11). After: the same cases, reading through `argv_words`, hold the same claims over argvs written as plain string literals, and a comment inside an argv no longer escapes them; an f-string or bytes first word, which the fold caught, now passes, and the docstring names it (folded after round 2).
- `tests/github/test_close_issues_on_release.py#Test_module::test_the_script_closes_and_takes_off_one_named_label_and_nothing_else`. Caught: in its `ast` form, the plain and the comment-split `gh issue reopen` that round 3 of #450 planted; its earlier folded form passed a comment-split argv in round 2, which is why it reads `ast` (its docstring, `:1099-1124`). After: unchanged claims through `argv_words`.
- `tests/behaviour/test_waiver_decided_at_start.py#test_the_template_PARSES_into_the_three_answers_it_ships`, renamed. Caught: written for round 1's M4, a template row that parsed as unanswered and shipped green; `git log -S` on its name finds only `716d8548d`, the initial commit, and no later red on record. After: the renamed case holds what it held, and the `offered` comparison adds the drift the removed row 3 named.
- `tests/text/test_a_rider_reaches_its_file.py#test_the_header_stops_the_answerer_that_is_really_a_condition`, lines 83 and 84. Caught: one false red on a row that described it, and it passed the defect measured on 2026-09-22 (`frame/design.md` G8). After: the header pins at lines 81 and 82 hold the rule's sentences, and the party that writes or reviews a row reads its answerer.

## Overlap with the release

The spawn named three other work items, none with a frame yet, so each is read from its issue. #1491 changes `docs/layout/one-root-by-lifetime.ko.md` and `skills/settle/rule-changes.md`, and #1492 changes `README.md`, `README.ko.md` and `docs/checks/the-stamp.md`; neither shares a file with this work, and neither changes a rule or a check that this work's change reads. #1490 shares directories with this work:

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1490 | Possibly `.github/scripts/run_tests.py`, whose comment at `:56-58` this work rewrites (*Scope* item 6), if #1490's census fix of section names reaches it; and the docstrings of `tests/github/test_close_issues_on_release.py`, `tests/github/test_label_merged_on_release_branch.py` and `tests/github/test_release_completeness_check.py`, which cite `docs/releasing/` documents (for example `test_close_issues_on_release.py:1128`, inside the case *Scope* item 1 changes) that #1490 restructures. No hunk is known to be shared until #1490 has a frame. | #1493 | This diff is the smaller and is likelier to be sealed first. Its hunks in those files sit in `Test_module` cases and one comment, away from the `docs/releasing/` citations, so #1490 merging second meets at most a neighbouring hunk inside rounds it spends anyway. Neither item adds a check that reads the whole tree. |

## Operational impact

None for a deployer: no migration, no environment variable, no dependency, no compatibility break. The version stays 0.37.1, where #1495 moved `.claude-plugin/plugin.json`; this pull request does not move it. Phase 3 writes the work item's `changelog.md` with one `### Process changes` row for *Scope* item 4 (`frame/design.md` G17). A work item never commits `.test_durations` (`frame/design.md` G16).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-10 | The title takes `refactor:` | The diff answers seven held questions: it empties a table, removes a guard, moves three cases onto one reader adds one assertion and one case, and changes one sentence of the implement skill that names a third value a record already used (#84's `deferred #350`); no command, script or hook behaves differently, so the patch carries no `feat:` | `~/.claude/skills/commit-pr-convention/SKILL.md` |
