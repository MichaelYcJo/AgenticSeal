# Phase 7: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 7 |
| Commit | 56861925 |

## What this phase was asked

Phase 7 of `frame/plan.md`, with `frame/design.md` *Scope* item 4,
*Removes*, and scenarios S6 and S9: the preset block's machinery retires.
`install.sh`, `uninstall.sh` and `skills/preset-setup/` were to be deleted.
`templates/setup/claude-md-block.md` was to keep its two markers and nothing
between them. `skills/update/SKILL.md` step 4 was to take an installed block
out after a backup. The README text in both editions, `.gitignore:14` and
`tests/censuses.py:1014-1015` were to follow. The installer's test module was
to be replaced by `tests/behaviour/test_the_old_block_leaves_through_update.py`.
Phase 5's record left this phase the block sentences at `README.md:45` and
`:265`, `install.sh`, `skills/preset-setup/SKILL.md`, `skills/update/SKILL.md:129`
and five test docstrings. `payload_meter.py` was left to phase 9, and
`skills/core/SKILL.md` to phase 8. The handoff carried two facts. The framer
had read that the update to 0.25.0 runs 0.24.x's step 4, which diffs the
marketplace clone's template. The orchestrator had run `bin/test -q
tests/test_censuses.py` green after `22838410`.

## What this phase found

**The frame held at every coordinate the row names.** `install.sh`,
`uninstall.sh`, `skills/preset-setup/SKILL.md` and the template stood as
phase 2 left them. Update step 4 held the `diff` command, the four-row table
and the paragraph on a clone of the plugin's own repository. `.gitignore:14`
and `tests/censuses.py:1013-1015` held the sentences *Removes* names. Each
case and docstring *Removes* lists stood at its line. One case it does not
list stood on the old README row:
`tests/behaviour/test_chain_hooks_hardening.py#test_the_always_on_block_is_described_without_counts`
required the `CLAUDE.md block` row to name the template.

**Step 4 is one `python3 -c` command, in step 3's shape, and a case runs
it.** *Scope* item 4 states what the step does and not how. Written as
prose, it would be held only by phrases. As a command, the new module takes
the program out of the step's bash fence and runs it under the test's own
interpreter over scratch files, the way the replaced module ran
`install.sh`. A separate check holds the fence's shell argument,
`"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/CLAUDE.md"`. The command backs the
file up to `CLAUDE.md.bak` and takes every region under either marker pair
out with its markers. It exits 1 and changes nothing at a start marker with
no end marker after it. It prints nothing where no block stands. It reads
the marker in the `CLAUDE.md` at `git rev-parse --show-toplevel` and names
that file without editing it. Reading and writing use `newline=""`, so a
file with `\r\n` line endings keeps them.

**No shipped prose may write the version this release carries.**
`tests/behaviour/test_release_hygiene.py#test_no_loaded_file_names_a_version_at_or_above_the_running_one`
refused the first draft, which said "before 0.25.0" in the update step and
both READMEs. The text now says "an earlier release".

**The template still needs a shipped document that names it.**
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py#test_every_template_is_named_by_a_document_that_ships`
went red once `install.sh`, `preset-setup` and update step 4 stopped naming
`templates/setup/claude-md-block.md`. The README's *Updating* paragraph, in
both editions, now names it as the file the earlier release's update
copies, holding two markers. Update step 4 itself does not read the
template, and a case holds that.

**What *Removes* lists was taken out, and three cases keep a half.**
`test_the_installer_writes_the_block_from_its_template.py` went whole. Its
three cases that read this repository's `CLAUDE.md` moved unchanged into the
new module. `seal layout --moved HEAD` listed them as neither missing nor
changed, and it listed the other 14 old cases as retired and the 8 new ones
as standing for no old case. In `test_chain_hooks_hardening.py`, the
`install.sh` case went. The preset-setup case kept its `commands/`
assertion as `test_the_commands_directory_stays_gone`, because no other case
holds it; parity-setup's user-invoked flag is held at
`test_parity_declaration_is_bootstrappable_not_hand_written`. The README
row case became `test_the_always_on_core_is_described_without_counts`. It
reads the new `Core` row (`코어` in Korean) and requires
`skills/core/SKILL.md` there. In the paste module, the template paste case
went, and the template case kept its fence, heading and capitalisation
assertions as
`test_fences_and_headings_are_not_read_and_case_and_backticks_are_not_words`.
`test_release_hygiene.py#test_update_tells_the_user_when_the_preset_block_changed`
became `test_update_takes_out_only_what_the_markers_hold`. The list entries
for the two scripts left `test_release_hygiene.py`,
`test_the_release_check_watches_what_ships.py` and
`test_no_document_names_the_old_roots.py`. `gaps.md` records two
divergences: the kept halves, and `.gitignore`'s `backup/` line, which
nothing writes and which went with its comment.

**The test fixture in the payload meter case no longer plants the A1
block.** `tests/skills/test_payload_meter.py#Test_measure.test_an_import_in_either_file_of_the_pair_is_a_harness_row_under_it`
now plants a user's own `@rules/mine.md` import. The next case,
`test_an_import_that_is_not_a_file_is_a_missing_row`, still uses the A1
line's path as a dangling import. *Removes* does not name it, and it sits
with the meter, so it is left to phase 9.

**Each new case was seen red first.** Against the tree at `445b4dd4`, with
only the new module written, 8 of its 11 cases failed: every case of step 4,
the template case, and the S9 case. The 3 moved cases passed.

**`seal mutate` ran once per unit, and every mutant went red in the end.**
Step 4 had 14 mutants in one batch: the backup, the damaged-block return,
the end-marker match, the old marker pair, the project check, the block
check, the exit code, the shell argument, the kept line, the missing-file
guard, the heading, `SessionStart`, *Needs action*, and a fourteenth that
broke nothing. The `SessionStart` mutant survived, because the output
table's row repeated the opening's sentence. `56861925` points the row at
the opening's two facts, so each stands once. A second batch of 4 then went
red: `SessionStart`, "No question is asked", where the rules stand, and the
`.bak` name. The template's `@` line, the hygiene case's "does not delete",
`CLAUDE.md`'s import, and both README editions (the `Core` row, a returned
preset-setup row and a returned `bash install.sh`) each went red too.

**The plan's census.** `git grep -n` on "preset-setup", "install.sh",
"uninstall.sh" and "`@` line", outside `seal/`, at `56861925`:

- `.test_durations:1167` and `:1171` name the two retired list cases. The
  orchestrator refreshes the file from CI after the phases close.
- `README.md:267`, the `seal payload` row, says the meter follows the pair's
  `@` lines. That stays true. The row is phase 9's.
- `skills/verify/scripts/payload_meter.py:8`, `:306` and `:343` describe
  `imports_of`, which stays under plan D1.
- `tests/behaviour/test_the_old_block_leaves_through_update.py` names the
  three retired files to hold them absent, and `@` imports to hold that
  `CLAUDE.md` has none.
- `tests/skills/test_payload_meter.py:8`, `:318`, `:327` and `:997` describe
  the meter's import reading. Line 327 is a planted code span that the case
  holds is not an import.

**The phase-boundary set passed.** It was one `bin/test -q` command over 118
modules: row 7's *Verified by* modules, and every test module that names a
README, `.gitignore`, `templates`, the update skill, `skills` as a
directory, `CLAUDE.md`, the censuses or an installer. It passed 5,088 cases
and skipped 11.
