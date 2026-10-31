# Design: the seal draws a round-headed little owl (#1174)

## Grounding

| Policy clause | What it fixes for this work |
|---|---|
| The owner's decisions of 2026-10-31, made in conversation before the routing answer took effect. Carried to this frame by the orchestrator's spawn prompt and its message of the same day; the orchestrator's account, which nobody can open as a file. Its inputs are in the tree at `efb91989` | (1) The terminal sprite is `assets/seals/candidates/little-owl-16.txt`, and it replaces `skills/verify/scripts/seal-mark.txt`. (2) The terminal disc becomes a red wax seal, still on the 28-cell grid, as the prototype `wax3.py` drew it with a pressed field of (150, 16, 22). The text panel does not change. (3) The page's form is `assets/seals/candidates/little-owl-wax-seal.svg`. It replaces `assets/seals/owl.svg`, and `.claude-plugin/icon.png` is drawn again from it. (4) The runners-up are not kept in this public repository. (5) The English word stays `owl`, and Korean text that names the bird says 올빼미. (6) A notice states that the AgenticSeal name, the owl emblem and its seal drawings are not licensed under the MIT License, while the code stays MIT. (7) No public text points at the brand's private material: the owner moved the drawing scripts, the runners-up and a brand guide into a private repository on 2026-10-31, because this repository is public under MIT |
| `docs/the-review-record.md` *The stamp*, the paragraph on the budget | The hook holds its whole message under `MESSAGE_BUDGET` (9,000 UTF-16 units). The disc has one size and two rungs, with the disc and without it. A redraw must keep one stamp of the widest panel under the budget. The probe below measures it at 5,725 units |
| `docs/the-review-record.md` *The stamp*, "the owner's disc is drawn 28 cells across and has one size" | The grid stays `DISC_CELLS = 28` and `DISC_LINES = 14`, and `compose` places the disc as it does today. The painted wax disc fills 27 columns and 27 half-rows of that grid, because its edge wobbles (probe P2). The sentence still holds, since the disc's block is 28 columns wide and has one size. No rule change |
| `docs/branch-and-release.md` *Cutting a release*: "The PNG is drawn from `assets/seals/owl.svg` by the command `assets/seals/README.md` gives, and the job installs no imaging library to attach it" | The new page form keeps the path `assets/seals/owl.svg`, so this sentence stays true. The README's command must name the renderer that actually drew the committed icon |
| `assets/seals/README.md`, its opening and *The next entry* | The directory keeps each shipped version of the emblem as the terminal drew it. The work that ships a new mark writes its entry in the same pull request: an `.ans` drawn by the entry's command, a `.png` drawn from it by the preview rule, and the section. The command names the first tag that carries the mark (`v0.25.1`, since `.claude-plugin/plugin.json` is already 0.25.1), and the files are drawn from the commit that writes them |
| `skills/core/SKILL.md` *The rule a mechanism is kept against*: "A fact has one source", and "a change rewrites the text it amends in place, and in the same commit removes what stood on the old fact" | The two input files leave `candidates/` in the commit that installs them, by `git mv`. A copy would be a second source of a shipped file. Every sentence and test pin that states the nine-colour disc is rewritten in the same commit as the disc |
| `tests/behaviour/test_the_release_check_watches_what_ships.py#STAYS_HOME` | Every tracked top-level entry must be classified as shipping or staying home. A new notice file at the root joins `STAYS_HOME`, as `LICENSE` does |
| `CONTRIBUTING.md`, which the comment above `tests/behaviour/test_docs_line_wrap.py#README_PAIR` quotes: the two READMEs move together | The licence line in `README.md` *License* and in `README.ko.md` *라이선스* changes in the same commit |
| Ticket #1174, read with `gh issue view 1174 --json title,body,comments` (executed): no comments | The round-headed little owl (*Athene noctua*) replaces a drawing whose raised head corners read as ear tufts. The new drawing replaces `owl.svg`, `owl.png` and `owl.ans`, drawn by the README's commands, with the `alt` text and the README entry describing the new head. The first Done-when bullet asked for several candidates. The owner's choice in conversation answers it, and the orchestrator is rewriting that bullet on the issue |
| Probe P1 (executed): `python3 -I test_tmp_wax_budget.py` in a `git clone --no-local` under `<scratchpad>/1793401152/frame/`, replacing the clone's `seal_stamp.build` with the prototype's geometry and `SPRITE` with `little-owl-16.txt`, and measuring the widest reference panel of `tests/skills/test_seal_stamp.py#Test_stamp` with its label | Today: 5,959 UTF-16 units. The wax disc: 5,725 units, against `MESSAGE_BUDGET` 9,000. `stamp(SAMPLE_ROWS)` plus a newline: 6,199 bytes today (`owl.ans`'s size) and 5,931 bytes with the wax disc. The disc lines carry 2 to 27 SGR codes each with the lean writer, against one code per cell in the prototype's own encoder (10,598 bytes for its disc alone) |
| Probe P2 (executed): the same script, comparing its transcription of the prototype cell by cell with the owner-approved output `scratchpad/owl/f1/stamp.ans` | 784 half-cells, 0 differences. The disc uses exactly 15 colours (listed in *Data & interfaces*). Its painted cells span columns 1 to 27 and half-rows 0 to 26 of the 28-cell grid. `cmp scratchpad/owl/FINAL-seal-mark.txt assets/seals/candidates/little-owl-16.txt` exits 0, so the approved output was drawn from the committed sprite |
| Probe P3 (executed): `read_sprite` of the clone over `little-owl-16.txt` | Accepted. The field bound `read_sprite` uses today, `DISC_CELLS / 2 - GROOVE_INSET` = 9.8, equals the prototype's `R - 3.7` = 9.8, the step ring's inner edge |
| Probe P4 (executed): `resvg_py.svg_to_bytes(svg_path=<little-owl-wax-seal.svg>, width=512, height=512)` in the scratchpad venv (`resvg_py` 0.5.0, Pillow 13.0.0) | A 512 x 512 PNG, 192,647 bytes. `tests/github/test_release_seal.py#Test_draw` asserts the tree's icon answers 256, its width over `DENSITY` 2, so the icon stays 512 pixels wide. `which rsvg-convert resvg cairosvg inkscape magick` finds none of them on this machine |
| `git grep -n -E '부엉이|올빼미'` (executed) | No match in the tree. The work adds 올빼미 only where Korean text names the bird, and adds no 부엉이 |

## Scope

In:

1. **The wax disc.** `skills/verify/scripts/seal_stamp.py#build` draws the red wax seal the owner approved, with its colours, its geometry constants, its letter twin `KEY` and the module's prose about the disc. `DISC_CELLS`, `DISC_LINES`, `SPRITE_OFFSET`, `compose`, both row writers, the text panel, `admitted` and `fitted` keep their behaviour.
2. **The sprite.** `assets/seals/candidates/little-owl-16.txt` is moved by `git mv` over `skills/verify/scripts/seal-mark.txt`. `SPRITE_COLOURS` keeps its six letters and their six colour values.
3. **The tests that pin the disc**, rewritten against the approved drawing. In `tests/skills/test_seal_stamp.py`: the colour constants, `NINE`, `LETTERS`, `OWL_LETTERS`, `REFERENCE_TWIN`, `REFERENCE_DISC`, `owners_disc`, the frame's counts in `Test_build`, and the 5,959 figure in `Test_stamp`'s docstring. In `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_docstrings_describe_the_letter_and_the_rows_it_carries`: the asserts on "nine colours" and on the twin's letters.
4. **The page's form and the icon.** `assets/seals/candidates/little-owl-wax-seal.svg` is moved by `git mv` to `assets/seals/owl.svg`. `.claude-plugin/icon.png` is drawn again from it at 512 x 512 with `resvg_py` 0.5.0, the renderer the README then names.
5. **The emblem's history.** The horned owl's three files are renamed by `git mv`: `owl.ans` to `horned-owl.ans`, `owl.png` to `horned-owl.png`, `owl.svg` to `horned-owl.svg`. Its README entry becomes *The horned owl — 0.23.1 to 0.25.0*, and its command writes `> horned-owl.ans`. Its last image line, which shows `.claude-plugin/icon.png`, shows `horned-owl.svg` instead, because the icon now shows the little owl.
6. **The new entry.** `assets/seals/README.md` gets *The little owl — from 0.25.1*. It has `owl.ans` drawn by the entry's command from the commit that writes it, `owl.png` drawn from that file by the preview rule, alt text describing the round head without ear tufts, ringed eyes, beak, spotted breast and olive branch, the sprite and SVG paragraphs, and the command and renderer for the icon. The README's opening ("From 0.23.1 the stamp carries the owl"), the preview rule's sentence on which Pillow drew which file, and the *Candidates* section's opening sentence about the disc's frame are brought up to date. `candidates/` keeps only the files it held before `efb91989`.
7. **The brand notice.** A new root file, `TRADEMARKS.md`, is the notice's one home. It states that the AgenticSeal name, the owl emblem and its seal drawings (every `.svg`, `.png` and `.ans` file and each mark's `.txt` under `assets/seals/`, `candidates/` included, but not `assets/seals/README.md` or any code; `.claude-plugin/icon.png`; the drawing in `skills/verify/scripts/seal-mark.txt`, and the release seal image `seal.png` a release note attaches) are not licensed under the MIT License, and that all rights to them are reserved. It also states that the code stays under the MIT License in `LICENSE`. `README.md` *License* and `README.ko.md` *라이선스* each keep "MIT" and add one line linking to `TRADEMARKS.md`. `assets/seals/README.md`'s opening links to it. `LICENSE` is not edited. `TRADEMARKS.md` joins `STAYS_HOME` in `tests/behaviour/test_the_release_check_watches_what_ships.py`, and it joins `COVERED` in `tests/behaviour/test_docs_line_wrap.py` because it is written wrapped. The notice's wording is not legal advice, and the frame does not present it as such. No public text points at the brand's private material: the seals README's new entry describes `owl.svg` as the page form's source, which is self-contained. That entry, `TRADEMARKS.md`, the test module's comments and every other file outside `seal/threads/` name no generator script, no scratchpad path and no private repository.
8. **The changelog fragment**, `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/changelog.md`, written by the last phase. No `### Process changes` table, because the diff touches no `CLAUDE.md`, `agents/*.md`, `skills/*/orchestration.md` or `skills/implement/bootstrap.md`.

Out:

- **The runners-up.** The owner's decision of 2026-10-31 keeps them out of this public repository. No files, previews or *Candidates* entries.
- **A preview script or an imaging library in the tree.** The README's rule says no script in the tree draws a preview and the tree installs no imaging library. The `.png` previews and the icon are drawn from a throwaway environment, which the README names with its versions.
- **A check that the icon is the SVG.** *What nothing checks* in the README states this gap, and it stays stated. Rendering in the suite needs an SVG renderer the suite does not have on every operating system it runs on.
- **#1153**, which shows the image on the release note's first screen. It takes whatever this work draws.
- **`.claude-plugin/plugin.json`'s `"license": "MIT"`.** The code stays MIT, and the notice is the brand's.
- **The text panel, the hook's budget and `MESSAGE_LIMIT`.** The stamp gets smaller (5,959 to 5,725 units), so the budget needs nothing.

## User scenarios & acceptance *(mandatory)*

| Scenario | Given / When / Then | Verifiable how |
|---|---|---|
| S1 The disc by the owner's rule | Given the shipped sprite, when `build()` is called, then each cell of the 28 x 28 grid equals the rule in *Data & interfaces*, rebuilt in the test from constants written out there, and the set of colours drawn is the fifteen plus `None` | `tests/skills/test_seal_stamp.py#Test_build`, its counts and its cell-by-cell loop rewritten. Seen red against the relief disc, or with one constant moved |
| S2 The approved picture, cell for cell | Given `REFERENCE_ROWS`, when the stamp is composed, then every half-cell of the disc is the colour the owner-approved output `scratchpad/owl/f1/stamp.ans` shows, and the twin's lines equal `REFERENCE_TWIN` | `Test_compose.test_accepts_the_owners_reference_cell_for_cell` with `REFERENCE_DISC` and `REFERENCE_TWIN` transcribed from the approved stream by a script that reads no line of `seal_stamp.py`. The stream is `scratchpad/owl/f1/stamp.ans`, and a durable copy is in the owner's private brand repository, which the orchestrator names in the spawn prompt (`cmp` of the two exits 0, executed 2026-10-31). The copy is a build-time input only. The phase record names the file it read and keeps the transcription's command, and no file under test or shipped names either path |
| S3 The sprite is the little owl | Given the tree, when the module loads, then `SPRITE` is the content `git show efb91989:assets/seals/candidates/little-owl-16.txt` prints, and `read_sprite` accepts it and still refuses each malformed shape | `Test_read_sprite`, both cases. `git diff efb91989 -M --stat` shows the move |
| S4 The stamp fits one message | Given the widest reference panel with its label, when it is drawn, then its size in UTF-16 units is at most `MESSAGE_BUDGET` | `Test_stamp.test_accepts_the_widest_reference_panel_with_its_label_in_one_message`, its docstring stating the new figure (5,725 by probe P1) |
| S5 The twin is a lookup | Given any disc cell, when the letter twin writes it, then its letter is `KEY[colour]`, one letter per colour, fifteen letters, none repeated | `Test_letter_row.test_accepts_the_discs_letters_and_the_text_in_ascii` with `LETTERS` rewritten |
| S6 The module's prose says what it draws | Given `seal_stamp.py`, when its docstring is read, then it describes the wax seal and its fifteen colours, the twin's new letters, and no longer the rim, the groove or nine colours | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py#test_the_docstrings_describe_the_letter_and_the_rows_it_carries`, its asserts rewritten and the retired phrases added to its `gone` list |
| S7 The archive file is the command's output | Given the commit that writes the new entry, when the entry's command is run with the tag replaced by that commit, then its output is byte-for-byte `owl.ans` | `cmp` of the command's output and `assets/seals/owl.ans`, run by the phase and quoted in its record. A person reads `owl.png` against `owl.ans` |
| S8 The icon is the page's form | Given `assets/seals/owl.svg`, when the README's icon command runs, then it writes `.claude-plugin/icon.png` at 512 x 512, and `release_seal.draw` copies it and answers 256 | `tests/github/test_release_seal.py#Test_draw` (existing). Whether the PNG shows the SVG is read by a person, as *What nothing checks* says |
| S9 The brand notice has one home | Given the tree, when a reader opens `LICENSE`, `README.md` *License*, `README.ko.md` *라이선스* or `assets/seals/README.md`, then `LICENSE` is the MIT text unchanged, and each of the other three links to `TRADEMARKS.md`, which alone states the exclusion | `git diff <base> -- LICENSE` is empty. `git grep -n 'all rights reserved' -i` matches `TRADEMARKS.md` alone. `tests/behaviour/test_the_release_check_watches_what_ships.py` classifies the new root |
| S10 No copy, no stale name, no pointer to private material | Given the tree, when it is searched, then `assets/seals/candidates/little-owl-*` does not exist, `git grep -n 'little-owl-16\|little-owl-wax-seal'` matches nothing outside `seal/threads/`, `git grep -n 부엉이` matches nothing, a `git grep` for the private brand repository's name outside `seal/threads/` matches nothing, and `git grep -n -i 'scratchpad\|wax3\|owl_final' -- assets/ TRADEMARKS.md README.md README.ko.md .claude-plugin/ skills/verify/scripts/ tests/skills/test_seal_stamp.py` matches nothing. The `scratchpad` grep is held to the files this work writes, because agent definitions and docs name `<scratchpad>` for their own probes | The five commands, run by the phase and quoted in its record |

## Data & interfaces

**The colours** (`seal_stamp.py`, replacing the block at lines 92-139). They are the prototype's values, and P2 checked them against the approved output. The names are the frame's choice. The owner chose the colours and did not name them.

| Constant | RGB | Where it is drawn | Twin letter |
|---|---|---|---|
| `EDGE_DARK` | (128, 12, 18) | the outer edge where `lit > -0.2` | `e` |
| `WAX` | (204, 30, 34) | the outer edge elsewhere, and the lip where `-0.35 <= lit < 0.4` | `w` |
| `WAX_LIT` | (240, 92, 84) | the lip where `lit < -0.35` | `h` |
| `WAX_DARK` | (172, 18, 24) | the lip where `lit >= 0.4` | `d` |
| `GLOSS` | (255, 172, 162) | the lip's streak: angle strictly between 200 and 250 degrees, and distance strictly between `R - 1.9` and `R - 0.7` | `g` |
| `STEP_DARK` | (98, 8, 14) | the step ring where `lit < 0` | `s` |
| `STEP_LIT` | (226, 66, 60) | the step ring elsewhere | `t` |
| `FIELD` | (150, 16, 22) | the pressed field | `.` |
| `DROP` | (84, 8, 12) | a field cell whose up-left neighbour is drawn | `y` |
| `OUTLINE` | (90, 8, 12) | sprite `K` | `K` |
| `PUPIL` | (112, 16, 20) | sprite `P` | `P` |
| `BODY` | (160, 30, 34) | sprite `R` | `R` |
| `BREAST` | (186, 38, 42) | sprite `L` | `L` |
| `EYE` | (222, 86, 78) | sprite `W` | `W` |
| `BEAK` | (208, 68, 64) | sprite `Y` | `Y` |

`DISC_COLOURS` is these fifteen. Every disc cell is exactly one of them, and `TITLE_RED` (196, 40, 44) is the only other colour the stamp sets. The six sprite colours keep today's values. Only their names change, because the rim colours they borrowed are gone. The pupil is no longer the field's colour: today's `FIELD` (112, 16, 20) stays as `PUPIL`, and the field is (150, 16, 22). The twin writes a sprite colour as the sprite's own letter, so the twin's owl reads like `seal-mark.txt`. The frame colours use lower case, and the field stays `.`.

**The geometry** (replacing `EDGE_INSET`, `WAX_INSET`, `RIM_INSET`, `GROOVE_INSET` and `LIT_AT` at lines 187-201). With `c = (DISC_CELLS - 1) / 2`, `R = DISC_CELLS / 2 - 0.5` (13.5), a cell `dx, dy` from the centre at distance `d` and angle `a = atan2(dy, dx)` (y downward, so 225 degrees is the upper left), and `lit = (dx + dy) / (|dx| + |dy|)`:

1. `edge = R + 0.45 sin(3a + 0.7) + 0.25 sin(5a + 2.1)`. Past `edge` the cell is `None`.
2. Past `edge - 1` the cell is the outer edge: `EDGE_DARK` where `lit > -0.2`, else `WAX`.
3. Past `R - 2.9` it is the lip: `GLOSS` inside the streak, else `WAX_LIT`, `WAX` or `WAX_DARK` by `lit` at -0.35 and 0.4.
4. Past `R - 3.7` it is the step ring: `STEP_DARK` where `lit < 0`, else `STEP_LIT`.
5. Inside, the field: the sprite's letter's colour, `DROP` under an up-left drawn neighbour, else `FIELD`.

`lit` is read only past `R - 3.7` (9.8), where `d` is never 0. `read_sprite`'s field bound is the step ring's inner edge, `R - 3.7`, which is the same 9.8 as today. The prototype tests the edge before the lip, and since `edge - 1` is at least 11.8 the lip is never empty. Each number is a named constant, as today's insets are. `build`'s docstring states the rule in these terms.

**The twin and the module docstring.** The docstring's paragraphs on the disc (lines 4-36) and the comments above the colours, `KEY`, the geometry and `SPRITE_COLOURS` describe the wax seal: a wobbling edge, a lip lit at the upper left with a gloss streak, a step ring lit the other way, the pressed field, the owl, and its drop shadow. They state the owner's choice of 2026-10-31 (#1174) beside #832's grid and #857's sprite. The sentence "every cell exactly one of nine colours" becomes fifteen.

**Files.**

| Path | After |
|---|---|
| `skills/verify/scripts/seal-mark.txt` | the little owl, moved from `assets/seals/candidates/little-owl-16.txt` |
| `assets/seals/owl.svg` | the wax seal, moved from `assets/seals/candidates/little-owl-wax-seal.svg` |
| `assets/seals/owl.ans`, `owl.png` | drawn new, by the entry's command and the preview rule |
| `assets/seals/horned-owl.ans`, `horned-owl.png`, `horned-owl.svg` | the horned owl's files, renamed and unchanged |
| `.claude-plugin/icon.png` | 512 x 512, drawn from `assets/seals/owl.svg` by `resvg_py` 0.5.0 |
| `TRADEMARKS.md` | the brand notice, the only home of its statement |

The icon's command in the README is a `python3 -c` call through `resvg_py.svg_to_bytes(svg_path=..., width=512, height=512)`, run from the repository's top directory, with the package and its version named. P4 ran that call.

## Rule changes

- nothing
  why: The policy root says nothing about the disc's colours, its geometry, the twin's letters or the emblem's licence. The stamp's budget and its one 28-cell size in `docs/the-review-record.md` *The stamp*, and the icon's source path `assets/seals/owl.svg` in `docs/branch-and-release.md` *Cutting a release*, stay true after this work.

## Removes

| Removes | Coordinate | Where it lands, or why it can go |
|---|---|---|
| The horned owl's sprite | `skills/verify/scripts/seal-mark.txt` at `efb91989` | The little owl replaces it (owner's decision 1). The old drawing stays viewable as `assets/seals/horned-owl.ans` and at tag `v0.25.0` |
| The chosen sprite's input copy | `assets/seals/candidates/little-owl-16.txt` | Moved to `skills/verify/scripts/seal-mark.txt`. A copy would be a second source of a shipped file |
| The chosen page form's input copy | `assets/seals/candidates/little-owl-wax-seal.svg` | Moved to `assets/seals/owl.svg`, for the same reason |
| The relief disc's colours and geometry | `skills/verify/scripts/seal_stamp.py`: `WAX_EDGE`, `RIM_LIT`, `RIM_MID`, `RIM_DARK`, `FACE`, `LIGHT`, `INNER`, today's `FIELD` value, `EDGE_INSET`, `WAX_INSET`, `RIM_INSET`, `GROOVE_INSET`, `LIT_AT`, and `KEY`'s nine letters | The wax seal's fifteen colours and constants (*Data & interfaces*). Today's sprite colour values carry over under the sprite's role names |
| The nine-colour and rim-and-groove prose | `seal_stamp.py` module docstring lines 11-36, the comments at lines 92-103, 120-128, 187-194 and 213-216, `build`'s and `read_sprite`'s docstrings | Rewritten in place to describe the wax seal |
| The relief disc's test reference | `tests/skills/test_seal_stamp.py:46-238` (`WAX_EDGE` to `owners_cell`), `Test_build`'s counts `[176, 84, 98, 30, 96]`, `Test_disc_cell`'s and `Test_letter_row`'s cells in the relief colours, and `Test_stamp`'s "5,959 ... 5,258" | The same names rewritten from the approved drawing (S1, S2, S4, S5) |
| The docstring pins on the relief disc | `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:224-228`, "every cell exactly one of nine colours" and "`m` its wax edge, `M n N` its rim lit, mid and dark, `.` its field" | Asserts on the new docstring's sentences (S6), with the old phrases moved to the case's `gone` list |
| The horned owl's file names | `assets/seals/owl.ans`, `owl.png`, `owl.svg` | Renamed to `horned-owl.*`, because the README keeps every shipped version. `owl.*` now hold the little owl |
| The README's renderer and its claims | `assets/seals/README.md` *The owl*: the `rsvg-convert` command, "2.58.4 drew the committed file", "seven reds of its own, none of them one of the stamp's nine", and the icon image line | The new entry names `resvg_py` 0.5.0 and its command, and describes the wax seal's own colours. The horned owl's entry shows `horned-owl.svg` |
| The README's description of the current disc | `assets/seals/README.md` opening ("From 0.23.1 the stamp carries the owl") and *Candidates*' first paragraph ("a wax edge, a rim lit from the upper left, a groove and the field") | Rewritten to say the stamp carries the little owl from 0.25.1 on the wax seal. The candidates that remain stood on the 2026-10-07 frame, and the paragraph says so in the past tense |
| "MIT" as the whole licence line | `README.md` *License*, `README.ko.md` *라이선스* | Each keeps "MIT" and adds a line linking to `TRADEMARKS.md` |

Framed 2026-10-31 by framer, before the build.
