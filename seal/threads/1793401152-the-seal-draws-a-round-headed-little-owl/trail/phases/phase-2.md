# Phase 2: 1793401152-the-seal-draws-a-round-headed-little-owl

## What this phase found

**The frame held, and two of its claims needed a reading.** Every path row
2 names was where the frame put it at `c857202a`. `docs/branch-and-release.md:85-86`
still names `assets/seals/owl.svg` as the icon's source and "the command
`assets/seals/README.md` gives", and both stay true. No other file outside
`seal/threads/` names `owl.ans`, `owl.png`, `owl.svg` or `rsvg-convert`
(`git grep`, executed).

**`TRADEMARKS.md` is in a user's install and stays home. The two statements
measure different things.** `frame/plan.md` *Operational impact* says the
file reaches users in the installed plugin, and *Scope* item 7 puts it in
`STAYS_HOME`. The installed 0.25.0 plugin's directory in Claude Code's
plugin cache holds `LICENSE`, both READMEs, `docs/`, `tests/` and every other root entry (`ls`,
executed), so the install copies the repository's root. `STAYS_HOME` does
not mean absent from the install. The refusal in
`tests/behaviour/test_the_release_check_watches_what_ships.py#test_every_top_level_entry_is_classified`
asks whether the plugin loader reads the entry or a user runs it while the
plugin is enabled. The loader does neither with `TRADEMARKS.md`, as with
`LICENSE`, so a change to it alone moves no version. The comment beside
the new `STAYS_HOME` entry and the changelog fragment both say this. The
plan's own sentence is the framer's, and this phase did not rewrite it.
Its one loose phrase is "reaches users", which `STAYS_HOME`'s comment uses
for the loader.

**S7's command, run at the phase's commit `8d86d3eb`, wrote `owl.ans`
byte for byte** (`cmp` exit 0, executed). That is the new entry's command
with `v0.25.1` replaced by `8d86d3eb`. The file had been drawn from
`c857202a` before the commit. Both commits hold the same
`skills/verify/scripts/`, and the output is 5,931 bytes, as the entry
says. The horned owl's command, which now writes `> horned-owl.ans`, still
writes that file byte for byte from `v0.23.1` (`cmp` exit 0, executed).

**The preview rule was re-implemented and checked against the committed
previews before it drew `owl.png`.** The script is
`<scratchpad>/1793401152/phase-2/preview.py`, run with the scratchpad
venv's Python and Pillow 13.0.0. Its first form drew each glyph on a layer
the size of its cell. That differed from `horned-owl.png` in 60 pixels,
all on the rule line. The `─` glyph is wider than its 12-pixel cell, and
the committed previews let it overlap the next cell. Drawn on the whole
image instead, anchored at the cell's centre, the script redraws
`horned-owl.png` and `placeholder-s.png` with no differing pixel (Pillow
`ImageChops.difference(...).getbbox()` is `None`, executed). That form drew
`owl.png`, and a second run over `owl.ans` writes the same bytes (`cmp`
exit 0). The README's preview paragraph now names Pillow 13.0.0 and the
overlap, which the rule did not state.

**The icon is the SVG at 512 pixels** (executed). `resvg_py` 0.5.0's
`svg_to_bytes(svg_path="assets/seals/owl.svg", width=512, height=512)`
writes 192,647 bytes, probe P4's size. Rerun by the README's command after
the commit, it writes the same bytes as `.claude-plugin/icon.png` (`cmp`
exit 0). `tests/github/test_release_seal.py` passes, so `draw` still
answers 256.

**The moves are shown by the blobs, as in phase 1** (executed). The diff
pairs the moved `owl.svg` as a modification and `horned-owl.svg` as an
addition. `git rev-parse` gives the same blob for
`efb91989:assets/seals/candidates/little-owl-wax-seal.svg` and
`HEAD:assets/seals/owl.svg` (`a5ad92d8`), and for each of the horned owl's
`56c94b6f:assets/seals/owl.*` and `HEAD:assets/seals/horned-owl.*`
(`46876d1f`, `8455812b`, `fd60ecd2`).

**Four sentences outside row 2's list stood on the old names, and were
rewritten** (rule 19). In `assets/seals/README.md`, the placeholder S's
entry said "#857 replaced it with the owl". The *Candidates* format line
said "read as the owl's is". The bee's entry said "beside the owl" and
"chose the owl over it". Each now names the horned owl, or each owl. *A
sprite becomes the mark* also said "only a candidate's disc is a
candidate", and that stopped being true once the disc became the wax
seal. It now says the mark. `read_sprite` at HEAD still accepts
`candidates/bee-28-pixel.txt` (executed), so "`read_sprite` accepts it as
it stands" holds.

**The horned owl's entry moved its present-tense rules to the little
owl's.** "No cell is shaded by its neighbours" and *What nothing checks*
are rules about the shipped mark, so they now stand in the new entry. The
horned owl's entry keeps what was true from 0.23.1 to 0.25.0, in the past
tense, and its last image shows `horned-owl.svg`. Its `rsvg-convert`
command and "none of them one of the stamp's nine" left, as `## Removes`
names.

**Seen red** (executed, `bin/seal mutate` after the commit): with
`"TRADEMARKS.md",` removed from `STAYS_HOME`,
`test_every_top_level_entry_is_classified` failed, naming `TRADEMARKS.md`.
With one line of `TRADEMARKS.md` lengthened past 88 columns,
`test_prose_stays_within_the_wrap_limit[TRADEMARKS.md]` failed. The tree
was clean after both.

**S9** (executed). `git diff 56c94b6f -- LICENSE` is empty. `git grep -n
-i 'all rights reserved' -- ':!seal/threads'` matches `TRADEMARKS.md:8`
alone, after `b4e2f1c6`. The first wording, "all rights to them are
reserved", matched nothing, and that commit rewrote it. Unlimited, the
grep also matches `frame/design.md:56` and `frame/plan.md:35`, where the
frame quotes the command. `README.md` *License*, `README.ko.md` *라이선스*
and the opening of `assets/seals/README.md` each link to `TRADEMARKS.md`.

**S10** (executed). `assets/seals/candidates/little-owl-*` matches no file.
`git grep -n 'little-owl-16\|little-owl-wax-seal' -- ':!seal/threads'`
exits 1. `git grep -n` for the private brand repository's name, with
`-- ':!seal/threads'`, exits 1. The
fifth grep, `scratchpad\|wax3\|owl_final` over `assets/ TRADEMARKS.md
README.md README.ko.md .claude-plugin/ skills/verify/scripts/
tests/skills/test_seal_stamp.py`, exits 1. The `owl.svg` file has no
comment and no metadata naming a script. `git grep -n 부엉이` matches only
`frame/design.md:20` and `:57`, where the frame quotes the command, and
nothing outside `seal/threads/`. 올빼미 appears once, in `README.ko.md`'s
licence line.

**The phase-boundary set** (executed, one command, exit 0, 860 passed).
Row 2's five modules, plus the modules that read `README.md`,
`README.ko.md`, `assets/seals/` or `.claude-plugin/icon.png`, plus
`tests/github/test_publish_release_note.py` for the fragment and
`tests/skills/test_seal_stamp.py`. It left out `tests/test_censuses.py`,
which reads every tracked file, the work item's records among them. Round
1's finding 1 found the census lines that module refuses:

```
bin/test tests/github/test_release_seal.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_no_document_names_the_old_roots.py tests/behaviour/test_a_release_is_sized_by_a_criterion.py tests/behaviour/test_both_editions_carry_the_same_folds.py tests/behaviour/test_first_setup_asks_once.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_release_hygiene.py tests/behaviour/test_the_contributor_has_a_procedure.py tests/behaviour/test_the_old_block_leaves_through_update.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_the_root_migrates_itself.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_unverified_rows_close.py tests/text/test_a_document_has_room_for_the_next_fold.py tests/text/test_a_segment_feeds_the_flow_log.py tests/text/test_settle_reads_before_it_removes.py tests/text/test_the_mode_is_a_row_and_a_command.py tests/text/test_the_records_can_be_carried_out_and_in.py tests/text/test_the_rules_have_one_owner.py tests/text/test_the_settings_have_a_front_door.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/github/test_publish_release_note.py tests/skills/test_seal_stamp.py -q
```

`b4e2f1c6` came after it and changed one line of `TRADEMARKS.md`.
`test_docs_line_wrap.py -k TRADEMARKS` passed over it (executed). No other
module reads that file.
