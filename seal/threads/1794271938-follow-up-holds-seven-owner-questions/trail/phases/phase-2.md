# Phase 2: 1794271938-follow-up-holds-seven-owner-questions

## What this phase found

**The frame holds for this phase's unit.** I opened each coordinate G7 and *Scope* item 2 give, at `7a2b420ee`. The case stood at `tests/behaviour/test_waiver_decided_at_start.py:177`, and `offered` stood at `:291`. `lib/routing.py:72-74` holds `IMPLEMENTATION_ANSWERS = (BY_CRAFTER, BY_SESSION)`. The template's row reads `| Implementation | <crafter, or: the session> |`, which `offered` reads as `('crafter', 'the session')`. No coordinate was wrong.

**The new comparison is red when the parser drifts from the template (executed, at `4d8031dc0`).** I ran `seal mutate` on `lib/routing.py` with `BY_CRAFTER = "crafter"` replaced by `BY_CRAFTER = "builder"`, the template left alone, over `-k THIRD_axis`. It read `red`, exit 0. The case failed at `tests/behaviour/test_waiver_decided_at_start.py:236`, the `stated == routing.IMPLEMENTATION_ANSWERS` line, with "the template offers ('crafter', 'the session') and the parser accepts ('builder', 'the session')". The substitution loop at `:222-227` runs before that line, so it passed against the same break. This is S4.

**The `assert stated` line is red when `offered` reads nothing (executed, at `4d8031dc0`).** The literal pin at `:211` reads the same template row. So any break of the template's row turns `:211` red before `:232` runs, and a template break cannot show `:232`'s own red. I broke `offered`'s pattern instead, replacing `, or: ` in its regular expression with `; or: `. The run read `red`, exit 0, and failed at `:232` with "the placeholder no longer states the third axis's two answers". Ground: contract rule 15, a guard is shown red with only that guard's input removed.

**The case's body changed beside its name, so it is the *Logic* row of `skills/verify/SKILL.md` *The narrow command still has to be able to fail*.** The two runs above are its mutation runs. The census of the old name, `git grep -n "three_answers_it_ships"` at `4d8031dc0`, lists four places:

- `.test_durations:1351`. A work item never commits that file (`frame/design.md` G16).
- `frame/design.md:32` and `:111`, and `frame/plan.md:52`. Each names the old name as the case this work renames.
- `seal/follow-up.md:44`, row 3 of the schedulable table. Phase 3 removes that row (*Scope* item 5).

**Departure from the frame: the rename turns a tree-wide case red until phase 3 lands (executed, at `4d8031dc0`).** `frame/plan.md` *Alternatives considered* row 10 says the rename costs nothing beyond the old key in `.test_durations`. The phase-boundary run, `bin/test tests/text tests/behaviour -q`, exited 1 with 1 failed and 1850 passed. The failure is `tests/behaviour/test_a_cited_section_stands_in_its_file.py::test_every_cited_name_stands_in_its_file`. It reads `seal/follow-up.md` as a tracked file, and row 3 cites the case by `path#name`. The old name stood at `7a2b420ee:tests/behaviour/test_waiver_decided_at_start.py:177` (read), so this phase's rename is what left the citation pointing at nothing. I did not edit the row. `seal/follow-up.md` is not among the files `agents/crafter.md` *Job* lets me write, and phase 3 removes row 3 whole. Once it does, the citation is gone.

**For the next phase.** Removing row 3 of `seal/follow-up.md` also clears the red above. Phase 3's boundary run is the first one that can show `test_every_cited_name_stands_in_its_file` green again.
