# Phase 1: 1793843891-remove-the-seal-candidates

## What this phase found

**The frame holds against the tree.** `git diff --stat 858c5fb7 8761ce2a` lists only the three frame files, so the frame commit's tree outside this work item is the tree the frame dates its statements to (executed). At 8761ce2a, `git ls-files assets/seals/candidates` listed the eleven files `frame/design.md` G1 names. G1's two searches outside `seal/threads/` hit `TRADEMARKS.md:11` and `assets/seals/README.md` alone, at the lines G1 gives (executed). `git grep -n "assets/seals"` outside the README and `seal/threads/` hit `.github/scripts/publish_release_note.py:653`, both READMEs at the root, `TRADEMARKS.md` and `docs/releasing/branch-and-release.md:104`. Each names `owl.svg`, `owl.png` or the README, which stay, and none is a test, hook or workflow, so G2 holds (executed). Judged against `frame/design.md` *Grounding* and the crafter's rule *The frame is judged before it is built to*.

**Departures from the frame: none.** Each edit is the one `frame/design.md` *Scope* 1 to 7 states. These wording choices were left to the build:
- *Scope* 3: the preview rule now reads "Redrawn by this rule with Pillow 12.3.0 from a throwaway environment, the previews of the gold lily, the red lily and the placeholder S each matched its `.ans` pixel for pixel, and `horned-owl.png` was drawn the same way." The rest of the paragraph is reflowed with no word changed.
- *Scope* 4: "over the bee below, in two forms" becomes "over the bee, in two forms". The comma keeps "in two forms" attached to "chose the owl", as it was. The item is reflowed with no other word changed.
- *Scope* 5: the first list item of `TRADEMARKS.md` reads "every `.svg`, `.png` and `.ans` file under [`assets/seals/`](assets/seals/). These are the emblem each release carried;".
- *Scope* 2: the README ends with `## The next entry`'s paragraph and one newline.

**No case is written new, and no `seal mutate` run is owed.** The phase removes files and prose and adds no behaviour, so no unit has anything to break. `skills/verify/SKILL.md` *The narrow command still has to be able to fail* puts prose under "whatever actually parses those files", and `frame/plan.md` *Technical context* names the checks that read the two files as the proof. Judged against the crafter's steps 5 and 6.

**The census of the removed names** (executed, after the removal):
- S1: `git ls-files assets/seals/candidates` printed nothing, and `test -e assets/seals/candidates` exited 1.
- S2: `git grep -n "seals/candidates\|candidates/" -- ':!seal/threads'` exited 1, and with `bee-28\|bee-web\|section-28\|section-14` it exited 1.
- `git grep -n -i "candidate" -- assets TRADEMARKS.md README.md README.ko.md` exited 1.
- S3: every `](<target>)` of `assets/seals/README.md`, resolved from `assets/seals/`, and of `TRADEMARKS.md`, resolved from the root, was checked with `os.path.exists` in one `python3 -c` command. It read 11 targets and found 0 missing, exit 0. The 11 are the targets `frame/design.md` G3 says stay.
- S7: `.claude-plugin/plugin.json` parses as JSON, and its `version` reads `0.32.3`.

**S4 and S5 by reading** (read): the README has no `## Candidates` section. Its preview rule names the three measured previews with no `candidates/`, and the horned owl's entry points at no section below. `TRADEMARKS.md`'s first list item names the emblem each release carried under `assets/seals/`, with no candidates and no `.txt`.

**The phase boundary** (executed): one `bin/test` command over 37 modules ended 2498 passed, 10 skipped, exit 0. The run took place after the version move, the fragment and `gaps.md` were written, and before this record was. The modules were chosen this way:
- The three modules `frame/plan.md`'s Verified by cell names: `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py` and `tests/behaviour/test_the_release_check_watches_what_ships.py`.
- The modules that name `plugin.json`, found by `git grep -l plugin.json -- tests`. That search lists 20 modules, `test_release_hygiene.py` among them, whose `test_no_loaded_file_names_a_version_at_or_above_the_running_one` reads the moved version.
- Seventeen modules that glob the tree and read markdown, citations, folds, encodings, the test layout or the records: `test_a_document_that_names_a_script_says_how_to_reach_it.py`, `test_no_document_names_the_old_roots.py`, `test_one_heading_rule_holds_to_commonmark.py`, `test_both_editions_carry_the_same_folds.py`, `test_no_passage_is_pasted_into_a_second_file.py`, `test_a_moved_rule_leaves_its_definition.py`, `test_a_document_has_room_for_the_next_fold.py`, `test_every_file_the_plugin_reads_or_writes_names_its_encoding.py`, `tests/skills/test_test_layout.py`, `test_the_record_is_written_in_words.py`, `test_a_record_carries_no_comment.py`, `tests/skills/test_unverified_check.py`, `tests/skills/test_chain_check.py`, `test_a_cited_commit_outlives_the_squash.py` and `tests/test_censuses.py`, with the two above that the plan also names.

A first attempt of that command passed the module list as one argument, because zsh does not split an unquoted variable, and ran no tests, exit 5. It is not counted. The other modules that glob the tree were not run. The record-reading modules ran again after this record was written, as the last paragraph says.

**The changed paths** (executed): `git diff --cached --name-only origin/release/v0.32.3`, with the phase's last commit staged, listed the eleven removed files, `assets/seals/README.md`, `TRADEMARKS.md`, `.claude-plugin/plugin.json` and this work item's `routing.md`, frame files, `changelog.md`, `gaps.md` and this record, and nothing else.

**A removal the frame's `## Removes` did not name:** none.

**Other statements of the removed text across the tree** (executed: `git grep -n -i` on `candidate`, `section sign`, `\bbee\b` and the Korean words for candidate and bee, outside `seal/threads/` and `.test_durations`). This list is a sample by wording (contract rule 12). The one hit about the seal candidates is the horned owl's entry, which *Scope* 4 rewrote. Every other `candidate` hit means a commit candidate, a `Broad gate` candidate or a variable in code. The `section sign` hits are `tests/censuses.py` and two cases, which refuse the character `\N{SECTION SIGN}` in a living file and do not name the mark. `git grep -n "assets/seals/\*\|seals/.*\.txt"` outside `seal/threads/` exited 1, so no other file states a `.txt` under `assets/seals/`.

**The record-reading modules after this record** (executed): with this record written and the phase's last commit staged, one `bin/test` command over `test_the_record_is_written_in_words.py`, `test_a_record_carries_no_comment.py`, `tests/skills/test_unverified_check.py`, `tests/skills/test_chain_check.py`, `test_a_cited_commit_outlives_the_squash.py`, `tests/test_censuses.py`, `test_docs_line_wrap.py`, `test_a_cited_section_stands_in_its_file.py` and `test_every_file_the_plugin_reads_or_writes_names_its_encoding.py` ended 898 passed, exit 0.
