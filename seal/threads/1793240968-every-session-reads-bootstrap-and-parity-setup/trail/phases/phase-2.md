# Phase 2: 1793240968-every-session-reads-bootstrap-and-parity-setup

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 0f7d7a49 |

## What this phase was asked

Build phase 2 of `frame/plan.md` against the frame at `77fe5438`, after
phase 1 closed at `3890b230`. `skills/implement/bootstrap.md` is created
with a title, an opening paragraph, and *Orchestrator: Bootstrap* moved byte
for byte from `skills/implement/orchestration.md`. The move is a `Write` of
the new file and an `Edit` removing the section, and a `diff` of the two
ranges shows the bytes match. `orchestration.md`'s opening paragraph drops
its clause about the root and parity mode and gains the pointer sentence of
`frame/design.md` *Scope* item 3. The acts table's opening prose, the
Bootstrap row's `File` cell and the table's own row name three files.
`templates/setup/claude-md-block.md:16` and `hooks/mode-gate.py:15-16` and
`:50-51` name the new file. The cases of `frame/design.md` *Data &
interfaces* read the new file, and one new case pins the pointer sentence
(S3), seen red before the sentence is written. The record holds `wc -w` of
`orchestration.md` before and after, and the S5 `diff` with its exit code.
`frame/questions.md` Q1 is answered by this phase's run of
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`.

## What this phase found

**The S5 comparison (executed).** The command was

```
diff <(git show 3890b230:skills/implement/orchestration.md | sed -n '89,279p') \
     <(sed -n '/^## Orchestrator: Bootstrap$/,$p' skills/implement/bootstrap.md)
```

and it exited 0; `cmp` over the same two ranges exited 0 too. Lines 89 to
279 run from the heading to the section's last line. Line 280, the blank
line that separated the section from *Orchestrator: how the work is
routed*, has no counterpart at the end of the new file. A first comparison
that ran up to the next heading differed by that one line alone.

**The word counts (executed, `wc -w`).** `skills/implement/orchestration.md`
held 7,835 words at `1e82fd0a`, 7,680 after phase 1 at `3890b230`, and 5,839
after phase 2 at `0f7d7a49`, which is 1,996 fewer than at the base. The moved
section is 1,848 words. The phases added words to `orchestration.md` in four
places. Phase 1 rewrote step 3's yes, which then moved. It also extended the
Bootstrap row's grounds with the removed Parity row's grounds. Phase 2
rewrote the opening paragraph, which went from 70 to 71 words with the
pointer sentence. It also made the acts table's prose and its own row name
three files, adding 6 words. `skills/implement/bootstrap.md` is 1,907 words.

**How the S3 case was seen red (executed).**
`test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap` in
`tests/behaviour/test_first_setup_asks_once.py` was written before the
pointer sentence, and `bin/test tests/behaviour/test_first_setup_asks_once.py
-k test_the_orchestrators_half_sends_a_fresh_repository_to_the_bootstrap -p
no:xdist -q` exited 1 on `the orchestrator's half does not send a fresh
repository to the bootstrap`. After the commit, `bin/seal mutate` removed the
pointer sentence from `orchestration.md`, printed `red: the cases failed
against the mutation (exit 1)` and exited 0. `bin/seal mutate` over the moved
step 3 sentence in `bootstrap.md`, against the re-pointed parity case, gave
the same verdict and exit. The tree was clean after both restores.

**`frame/questions.md` Q1 (executed).** With `skills/implement/bootstrap.md`
tracked, `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py
-q` exited 0, 8 passed. The default, green, holds, and `BASELINE` needs no
key. The module reads tracked files, so a run made while the new file was
still untracked would not have measured it. The same holds for
`tests/behaviour/test_a_cited_section_stands_in_its_file.py`, which reported
the new file's three citations as dangling until the file was staged.

**The narrow runs (executed, one module per command, exit codes read
directly).** The nine modules of the *Verified by* cell each exited 0:
`test_chain_hooks_hardening.py` 30 passed,
`test_every_orchestrator_act_names_its_delivery.py` 15 passed,
`test_first_setup_asks_once.py` 51 passed,
`test_a_cited_section_stands_in_its_file.py` 23 passed,
`test_no_passage_is_pasted_into_a_second_file.py` 8 passed,
`test_docs_line_wrap.py` 40 passed,
`test_the_settings_have_a_front_door.py` 18 passed,
`test_the_rules_have_one_owner.py` 35 passed and
`test_a_section_marked_for_one_role_reaches_only_that_role.py` 11 passed.
Twenty-one more modules read `orchestration.md`, the preset block, the hook
or the parity-setup skill without being in the frame's list. Each was run
the same way and each exited 0. They include `test_mode_gate.py`,
`test_the_installer_writes_the_block_from_its_template.py`,
`test_waiver_decided_at_start.py`, `test_one_word_one_meaning.py`,
`test_a_moved_rule_leaves_its_definition.py` and
`test_a_document_that_names_a_script_says_how_to_reach_it.py`. None needed a
change, so the frame's list of readers that change was complete.

**Two docstrings the frame listed stand unchanged.**
`tests/behaviour/test_first_setup_asks_once.py:175` names "the whole
Bootstrap section" as the slice a round finding once read, and says nothing
of the file the section is in.
`tests/behaviour/test_every_orchestrator_act_names_its_delivery.py#_tree`
says its planted root holds "both orchestration files", and it still does:
the planted tree carries no bootstrap file, and `acts` skips a path that does
not resolve. `gaps.md` records both.

**A test id changes, and `.test_durations` keeps the old one.**
`test_prose_stays_within_the_wrap_limit` gains the id
`[skills/implement/bootstrap.md]`, and
`test_a_document_naming_a_script_with_a_command_says_how_to_reach_it` reads
`seal.py` in the new file under `[skills/implement/bootstrap.md::seal.py]`,
where `.test_durations` holds `[skills/implement/orchestration.md::seal.py]`
(executed, `--collect-only`). `.test_durations` is written by CI
(`.github/scripts/durations_union.py`), and a missing key only prices a
case at the default.
