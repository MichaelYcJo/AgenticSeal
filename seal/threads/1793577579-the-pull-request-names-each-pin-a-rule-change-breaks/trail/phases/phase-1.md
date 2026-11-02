# Phase 1: 1793577579-the-pull-request-names-each-pin-a-rule-change-breaks

## What this phase found

**The frame holds, judged before the build.** Each coordinate it hands the build was opened at the base `4ba077150` (read). `rule_changes.py` holds `Op.lines`, `section_lines` and `pattern`, and `chain_check.py` holds `rule_changes_read`, `check_lines_in`, `rule_changes_of`, `tracked_files`, `read_record` and `RULE_CHANGES_UNREAD` (G6, G7). The registry entry G9 names stands at `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:84`. Each `from` of `## Rule changes` stands where S8 says. `docs/the-review-record.md` *What the check reads at the pull request* holds the first, wrapped across a line. `docs/what-a-script-gates.md:42` holds the third. #1215's pending `to` values in `seal/threads/1793573444-a-check-line-inside-a-to-is-read-at-the-pull-request/frame/design.md` hold the other two. `docs/what-a-script-gates.md:53`, inside *The checks*, holds the wording-or-fact criterion the proofer's new sentence cites. Every test module and script the plan's *Verified by* names exists.

**Departure: `passages.py` tells a heading line through `skills/verify/scripts/unverified_check.py#heading_level`, and the paste test's `HEADING` pattern did not move.** The census `tests/censuses.py#heading_rule` refused the moved pattern in a shipped script as a second spelling of the heading rule. The census is right: `skills/core/SKILL.md` *The rule a mechanism is kept against* gives a fact one source, and contract rule 18 sends a correct check's refusal to the code. `passages.py` loads that reader by path, as `rule_changes.py` does. The paste test passes with `BASELINE` untouched after the change (executed, S6), so the two readings agree on this tree. The *Removes* table's row listed `HEADING` among what lands in `passages.py`; it lands nowhere, and `lines` lands as the private `_lines`, since the design's interface names four public names.

**Departure: a rule document that does not decode is named as not read, beside the test file *Scope* item 4 names.** The first build skipped such a document unnamed. Design E3 and `skills/core/SKILL.md` *The rule a mechanism is kept against* name a file the reader cannot read as not read. The notice is `chain_check.py#DOCUMENT_UNREAD`, added at `abe82825a` and pinned by `test_names_a_rule_document_that_does_not_decode_as_not_read`.

**Decisions settled in the code**, each against the design's *Scope* items 3 and 4:

- `in_corpus` checks the `.md` suffix itself, so the predicate is the whole selection rule of G8. The paste test still lists `*.md` with git and filters with it.
- `literals` reads every `str` constant `ast.walk` meets, the constant parts of an f-string among them, and leaves out bytes. A docstring is the first statement of a module, class or function body when that statement is a string.
- A pin's notice prints the literal whole, as `frame/questions.md` assumed. A copy's notice prints the first shared run in the `to`'s word order, normalised as `passages.py#words` leaves it.
- The tests and the rule documents are read from the working tree under `--worktree` and without it, once per run, on the first design with operations. The notices for the files not read are printed once, at each file's path and line 0.
- The function the marker class names is `chain_check.py#pins_and_copies_in`, so the class is `Test_pins_and_copies_in`, as `CONTRIBUTING.md` *The test layout* asks.

**A constraint found by trying.** A case of `tests/skills/test_chain_check.py` that plants a file outside the work item's records needs a round record at HEAD. Without one, the records arm refuses the ready pull request with "a verifying round is owed", and the case reads that refusal instead of the notice. The helper `planted_spec` puts the spec, then `reviewed_to_head`.

**Seen red (contract rule 15), each executed.**

- `tests/skills/test_passages.py`, and `Test_literals`, `Test_pins` and `Test_copies` of `tests/skills/test_rule_changes.py`, errored at collection against the base: the module and the three functions did not exist.
- Four cases of `Test_pins_and_copies_in` failed against the base, each because no notice was printed: the `from` pin, the `remove` pin, the copy, and the test file that does not parse.
- The two cases that expect nothing passed at the base. Each was seen red under the mutation its docstring names. `test_accepts_a_to_that_keeps_the_literal_naming_nothing` went red with `rule_changes.py#pins` reading no `to`. `test_refuses_to_name_a_copy_landing_in_a_korean_edition` went red with `passages.py#in_corpus` admitting every `.md`.
- `test_names_a_rule_document_that_does_not_decode_as_not_read` failed against `29ce13483`, which skipped the document unnamed.

**Mutations (`seal mutate`), every mutant red and none survived (executed).**

- `literals`: the docstring exclusion dropped, the floor at three words, no whitespace collapse. 3 of 3 red under `Test_literals`.
- `pins`: no `to` read, no guard on nothing taken, no collapse. 3 of 3 red under `Test_pins`.
- `copies`: no corpus guard on the `to`'s file, the `to`'s own file counted, a count of 1, no corpus guard on the other file. 4 of 4 red under `Test_copies`.
- `pins_and_copies_in`: the `from`'s line replaced by the operation's line, no section read for a `remove`, no unread notices, the `to`'s line replaced, the arm returning nothing. 5 of 5 red under `Test_pins_and_copies_in`.
- The document notice dropped: red under its case.

**The moved units owe no new case.** `words`, `windows`, `in_corpus` and `WINDOW` moved with their bodies. The two cases that tested `words` alone pass in `Test_words` of `tests/skills/test_passages.py`, and the paste test passes with `BASELINE` untouched (executed). The census of the old spellings is `git grep -n -e "from test_a_moved_rule_leaves_its_definition import" -e "^def words(" -e "^def windows(" -e "^def lines(" -e "^HEADING = re.compile" -e "^SECTION_TOKEN" -e "^TOP_DIRS" -- tests`. It lists three `HEADING` patterns, each another module's own, and none of the moved definitions (executed).

**S7, the record replayed (executed, a `test_tmp_replay.py` probe run once with `python3 -I` from the scratch directory over `git archive a92c358b^` and `git archive a92c358b`, removed after).** The built functions read 94 operations over the eleven designs and name 26 pins at 26 literal sites, G10's counts. The method G10 states, each literal's count in its module before and after the settle, lists 13 literals the settle took out of its eight test modules. Twelve are named pins. The thirteenth, `*The run*'s extension line does not say where the count started` in `tests/text/test_the_rules_have_one_owner.py`, is the failure message of an assert the settle removed, and that assert's own literal, `counting from round 1:`, is named. So every pin the settle removed or repointed is named, and the count of 13 holds only with the message among them. The copy half names 5 pairs from five `to` values of three designs, two of them the one copy of `skills/core/SKILL.md` two designs added, and each run is gone from its document at `a92c358b`, so the settle reworded or linked every one of them.

**S8 (executed).** `chain_check.py --baseline <release/v0.28.0> --root . --worktree` at `29ce13483` printed no pin and no copy for this design, and no refusal of its `add`'s check line, since `Test_pins_and_copies_in` carries the marker. The run took 2.88 s real for the whole check.

**Scope item 7, the census of sentences.** The method is the design's `git grep -n -e 'rule_changes' -e 'Rule changes' -e 'chain-check' -e 'chain_check' -- ':!seal/threads' ':!tests' ':!docs'`, run at the build with `.test_durations` left out, 158 lines, read line by line. `chain_check.py`'s module docstring was corrected in its *rule changes* arm and in its paragraph on notices. The rest are still true, since none claims to list everything the check reads of a design. `skills/settle/SKILL.md:99-102` says `chain-check` asks `rule_changes.py` at the pull request. `skills/settle/SKILL.md:136-139` and `.github/scripts/rules.py:24-27` and `:339` say what it asks `rules.py`. Each `docs/` sentence that lists the inputs is changed through the design's `## Rule changes` alone.

**The boundary run (executed).** At `abe82825a` with this record, `gaps.md` and the Status cell on disk, one `bin/test -q` over the 52 test modules the base's `git grep -l` lists and `tests/skills/test_passages.py` exited 0: 3158 passed, 10 skipped. The run before `gaps.md` existed failed one case, `tests/behaviour/test_chain_hooks_hardening.py::test_every_spec_directory_that_reached_the_ladder_has_an_overview`, for that file. `bin/seal layout --check tests`, `bin/seal rules --check`, and `uvx ruff check` and `uvx ruff format --check` over the changed Python files each exited 0.

**The plan's narrow list.** The base's `git grep -l` lists `tests/conftest.py` and `tests/censuses.py`, which hold no test case. The boundary run leaves them out and runs `tests/test_conftest.py` and `tests/test_censuses.py`, which read them.
