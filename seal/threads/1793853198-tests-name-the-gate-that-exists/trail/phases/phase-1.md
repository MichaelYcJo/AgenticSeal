# Phase 1: 1793853198-tests-name-the-gate-that-exists

## What this phase found

**The frame holds for this phase, with two corrections and two departures.** The phase was built on `e1e84f0ca`, whose `tests/` tree is the tree at `c54f0040` (executed: `git diff --stat c54f0040 e1e84f0c` lists the three frame files alone). Each of D1's 19 coordinates holds the text its row names (read). Row 16 stands at `tests/censuses.py:892`, where D1 says `:890`; the text is the one D1 names. Every grounding fact the rows stand on was opened before the build: `tests/conftest.py#fired` has no caller (executed: `git grep -n -w fired -- . ':!seal/threads'` prints only its own `def`), `hooks/routing-edit-gate.py:257` lets an edit through when `routing.for_branch` returns a declaration (read), `agents/crafter.md` holds no waiver (executed: `grep -n -i waive`), and `ruff.toml:45` gives `hooks/lib/` as its example of `*` crossing a `/` (read).

**Each of the 19 rows, at `e1e84f0ca`** (read: each rewrite at its line after the edit). Q2 of `frame/questions.md` is answered by the last column.

| # | Line | Disposition | What replaced it |
|---|---|---|---|
| 1 | `tests/conftest.py:577-585` | R | removed: `fired`, its docstring and its body, with the two blank lines after it |
| 2 | `tests/conftest.py:1716` | N | "An opted-in repository, at a path holding non-ASCII." |
| 3 | `tests/hooks/test_question_gate.py:203` | N | "S6, S7: the branch and the root resolve as the edit gate's do", padded to the section comments' width |
| 4 | `tests/hooks/test_routing.py:1-2` | N | "`hooks/lib/routing.py`: the routing answer is recorded where the hooks read it, so nothing re-derives it." |
| 5 | `tests/hooks/test_routing.py:4-5` | N | "A declaration at `seal/threads/<work-item-id>/routing.md` is what the edit check reads, through `routing.for_branch`." The failure-direction sentence after it stands |
| 6 | `tests/hooks/test_routing.py:7` | N | "What a hook does with an answer is that hook's own file's." |
| 7 | `tests/hooks/test_routing.py:62` | N, worded apart from D1 | "or every declaration like it carries an answer its author never gave". The predicate is unchanged. Why the wording departs from D1's row is below |
| 8 | `tests/hooks/test_routing.py:109-110` | N | "A third or a fourth axis that invalidated them would make each one no declaration, and the edit check would refuse the branch it names." |
| 9 | `tests/hooks/test_routing.py:263-264` | N, then D | "so the file is no declaration and the edit check refuses the next edit. This case asks the parser." The sentence on the gate's own case is removed |
| 10 | `tests/hooks/test_routing.py:414` | N | "a required row, or a row whose absence took the declaration down, would make every one of those no declaration, and the edit check would refuse the branch each names." |
| 11 | `tests/hooks/test_routing.py:536-537` | N | "The direction the module states is "no declaration", which means the edit check refuses the edit." The "Not silence" sentence stands, and so does the past narration at `:533` |
| 12 | `tests/hooks/test_routing.py:555-556` | D | "This case asks the reader." The sentence naming the commit gate's case is removed |
| 13 | `tests/behaviour/test_waiver_decided_at_start.py:196-197` | N | "a wrong answer in the first two makes the file no declaration, so the edit check refuses the next edit on the branch, and a wrong answer here is never contradicted by anything." |
| 14 | `tests/behaviour/test_waiver_decided_at_start.py:705-706` | N | "`for_branch` finds no declaration, and the edit check refuses the next edit on that branch." |
| 15 | `tests/behaviour/test_a_commit_names_its_repository.py:3-8` | R | removed: the gate-half sentence and the milestone-49 measurement. The paragraph is now "The rule came with work item `1790644505` (#662, #665)." The paragraph at `:19-21` stands |
| 16 | `tests/censuses.py:892` | D | "a git hook" removed: "(a hook, the launcher, `bin/test`'s runner, and every module one of them loads)" |
| 17 | `tests/censuses.py:952` | N | "`"hooks/*.py"` lints `hooks/lib/routing.py` too." `tests/test_censuses.py:788` keeps its input |
| 18 | `tests/hooks/test_launch.py:204` | D | "a git hook" removed: "nothing holds it for a hook, the launcher itself or `bin/test`'s runner" |
| 19 | `tests/text/test_a_moved_rule_leaves_its_definition.py:26-27` | D | the waiver item removed: "the crafter's 1.08-1.17 and its hand-back as the place both answers land." The closing sentence stands |

**Row 7 departs from D1's wording, because D1's wording names a failure the predicate does not guard.** D1 row 7 has the message say that every declaration like the file "stops being one and the edit check refuses the branch it names". The message is printed only when `parsed[key] is None` fails, and the line before it, `assert parsed is not None, path`, has already passed, so the file is a declaration when the message prints. The edit check reads whether `routing.for_branch` returns a declaration and nothing else (`hooks/routing-edit-gate.py:257`, read), so an optional row read wrongly does not move it. What a wrong read gives is an answer on an axis the file never answered, and the message says that. Judged against `frame/design.md` D1 *N, present* ("names the mechanism that does today what the sentence describes") and `hooks/routing-edit-gate.py`.

**One edit falls outside D1's lines: the comment above `CRAFTER` in `tests/text/test_a_moved_rule_leaves_its_definition.py`, at `:260-262` of the base.** It said the waiver example "is one of the kept applications this module's docstring names". Row 19 removes the example from that docstring, so the comment was false at the phase's first commit `b965a9a8`. It now reads "The waiver example, then a kept application, sat inside that range, so a removal keyed on lines would have taken it too." That is commit `cebd347f`. Judged against `skills/core/SKILL.md` *The rule a mechanism is kept against* ("in the same commit removes what stood on the old fact") and `frame/design.md` *Scope* item 1. No sibling work item edits this file. The comment at `:324-326`, which says in the past tense that the waiver example and the one waiver sentence left, stands.

**S3's command as the frame writes it cannot fail on this machine's git.** `git grep -n -E "\bfired\(" -- . ':!seal/threads'` printed nothing at `c54f0040`, where `def fired(stdout):` stands at `tests/conftest.py:577` (executed, exit 1). Git's extended regular expressions here do not read `\b`. The phase ran it with `-P`, which prints that line at `c54f0040` (executed, exit 0) and nothing at `cebd347f` (executed, exit 1).

**S4 was measured from git's blobs, not in a scratch clone.** A probe read each touched module with `git show <rev>:<path>` at `c54f0040` and at `b965a9a8`, removed every docstring from both parsed trees and compared `ast.dump`. Six modules are equal as they stand. `tests/conftest.py` is equal once `fired` is taken out of the base (193 top-level nodes to 192). The probe's first run reported `tests/hooks/test_routing.py` as different with no constant swapped: adjacent f-strings with no placeholder join into one constant, so the old message is a substring of it. A second probe swapped the old message for the new one as a substring: 1 constant swapped, and the trees are equal (executed). Both probes were files named `test_tmp_*` in the session's scratchpad, each run once and deleted. `cebd347f` changes one comment, which no parsed tree holds.

**S1, at `cebd347f`** (executed: `git grep -n -i "commit gate" -- tests`). Nine lines, each in `frame/design.md` *Left as they stand*:

```
tests/hooks/test_cmdline.py:5
tests/hooks/test_gate.py:6
tests/hooks/test_optin.py:82
tests/hooks/test_routing.py:535
tests/text/test_edits_go_through_the_edit_tool.py:16
tests/text/test_edits_go_through_the_edit_tool.py:17
tests/text/test_edits_go_through_the_edit_tool.py:51
tests/text/test_the_direct_answer_owes_the_sealers_record.py:9
tests/text/test_the_direct_answer_owes_the_sealers_record.py:20
```

`tests/hooks/test_routing.py:535` is the past narration D1 calls `:533`. The two lines the rewritten module docstring added moved it.

**S2, at `cebd347f`** (executed: `git grep -n -i -E "git hook|hooks/git/" -- tests`). Eight lines. `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py:287` and `tests/hooks/test_dispatch.py:1155`, `:1156`, `:1157` and `:1169` say the git hooks are gone. `tests/skills/test_test_layout.py:85` and `:86` and `tests/test_censuses.py:788` are a case's input.

**S3, at `cebd347f`**: `git grep -n -P "\bfired\(" -- . ':!seal/threads'` prints nothing (executed, exit 1).

**S5.** One run of the eight touched modules but `tests/conftest.py`, with `tests/test_censuses.py`, `tests/test_conftest.py` and the modules that glob `tests/` or read `tests/censuses.py` (`tests/skills/test_test_layout.py`, `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py`, `tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/behaviour/test_every_reader_ends_a_line_where_gfm_does.py`, `tests/github/test_plugin_directory_check.py`, `tests/github/test_release_report.py`), through `bin/test -q`: 763 passed, 2 skipped, exit 0 (executed, at `cebd347f`). Each module imports `tests/conftest.py`. The three touched modules that declare `TARGET`, `tests/hooks/test_question_gate.py`, `tests/hooks/test_routing.py` and `tests/hooks/test_launch.py`, ran their `test_census` in it. The two skips are in `test_the_windows_leg_runs_in_shards_that_make_the_whole.py`, which reads the whole suite's collection and skips where the run collected less. `uvx ruff check` and `uvx ruff format --check` over the nine touched files exit 0 (executed).

**S6** is the table above, one row for each of D1's 19 rows.

**The three methods, rerun at the phase's commits.**

- **M1.** S1 above, nine lines.
- **M2** (executed, at `b965a9a8`). Each file name #1027 deleted, searched under `tests/` with `git grep -F`, prints `tests/text/test_edits_go_through_the_edit_tool.py:53`, a case's asserted string, `tests/test_censuses.py:788`, a case's input, and `tests/hooks/test_dispatch.py:1166`, a loop over names that must stay gone. None describes the gate as present.
- **M3** (executed, at `cebd347f`). `git blame -s 61a8455a..HEAD` over the 157 tracked `.py` files under `tests/` marks 66,777 lines unchanged since #1027's squash or older. The framer counted 66,824 at `c54f0040`; this phase removed or rewrote the difference. Filtered on the frame's nine words, they give 6,016 hits, most of them `gate` inside a live gate's name. The 12 hits on the words other than `gate` and the 227 hits that speak of "the gate", "a gate" or a gate's act without naming the edit, question or mode gate were read. None describes the commit gate as present. The read found two more lines outside the class: `tests/text/test_a_moved_rule_leaves_its_definition.py:380-382` says #1027 retired a rule "with the gate it waived", and `tests/hooks/test_mode_gate.py:245-246` tells a round 1 measurement in the past tense.
- **The list is a sample**, as the frame says: the word filter is not whole over spellings. A line that describes the commit gate as present in none of the nine words is outside it, and the proofer reads the diff's files for it.

**No case was written and no `seal mutate` ran.** Each change is a docstring, a comment, one failure message or the removal of a function nothing calls. None adds behaviour, so `skills/verify/SKILL.md` *The narrow command still has to be able to fail* asks only that each module still imports, which S5's run shows, and `frame/design.md` D2 adds no case.
