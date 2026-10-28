# Review round 1: 1793152332-the-stamps-mark-is-an-owl

target: 10a8444a against origin/release/v0.23.1

## Findings

### 1. Two of the four Pillow absence assertions pass a pin spelt `Pillow==12.3.0`

severity: should
location: `tests/behaviour/test_the_release_seal_is_drawn.py:36`, `tests/github/test_run_tests.py:444`
evidence: read `tests/behaviour/test_the_release_seal_is_drawn.py:25-36`, `tests/github/test_run_tests.py:429-444`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:163-167`, `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:197-198`
verdict: open

`gaps.md` row 4 claims that each of the four rewritten cases asserts that no
word of its line starts with `pillow`, so that a pin put back is refused.
Two of the four compare case-insensitively:
`tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:166`
lowers each word, and line 198 lowers the section. The other two compare
the word as written. `tests/behaviour/test_the_release_seal_is_drawn.py:36`
splits the `publish-release.yml` install line into words and tests
`word.startswith("pillow")`. `tests/github/test_run_tests.py:444` does the
same over the runner's install step. pip treats a distribution name without
regard to case, so `Pillow==12.3.0` is the same pin as `pillow==12.3.0`.
Put back on the `seal` job's install line in that spelling, it installs
Pillow again, and the case that reads that line passes. The case then says
something that is not true: it tells the next reader the job installs no
Pillow. The class is the four absence assertions this work added, and the
two that already lower the word need no change. The fix is the same lowering
on the other two lines.

```python
# tests/behaviour/test_the_release_seal_is_drawn.py:36
assert not any(word.lower().startswith("pillow") for word in installs[0]), installs

# tests/github/test_run_tests.py:444
assert not any(word.lower().startswith("pillow") for word in install), install
```

answer:

## Confirmations

confirms: none
The terminal owl is the owner's candidate, apart from the shadow's colour.
Phase 2 claimed that `seal-mark.txt` is the candidate's sprite byte for byte
and that 275 of the 300 field cells match the candidate. It also claimed the
other 25 are the shadow, painted (78, 8, 12) in the candidate and `DROP` in
`build`. Executed: the probe compared `skills/verify/scripts/seal-mark.txt`
with `c8bb9693:assets/seals/candidates/owl-28-pixel.txt`, and the two are
equal, 272 bytes each. It also decoded the candidate's `.ans` at `c8bb9693`
from its SGR stream without reading `seal_stamp.py`, and compared every cell
within 9.8 of the centre with `build()`. Of 300 field cells, 25 are the
candidate's (78, 8, 12), and `build` draws each of those as `DROP`. `build`
draws 25 `DROP` cells in the field in all, and no other cell differs.

confirms: none
The stamp still fits one hook message. The case at
`tests/skills/test_seal_stamp.py:780` reads its bound from
`MESSAGE_BUDGET` (`skills/verify/scripts/seal_stamp.py:184`) rather than a
stored number. It passed in this round's `bin/test` run (executed). The
5,959-unit figure in its docstring was not measured again here.

confirms: none
The letter twin still prints for a console that is not UTF-8. The case at
`tests/skills/test_seal_stamp.py:807` passed in this round's `bin/test` run.
The probe drew `stamp(SAMPLE_ROWS, shape=True)`, and every line was ASCII and
as wide as the block form's line with its codes removed (executed). The
twin printed the owl in `x`, `n`, `X`, `Y`, `M`, `.` and `y` inside the
frame's letters.

confirms: none
`read_sprite` refuses each malformed sprite the design lists, with a sentence
a person can act on (`skills/verify/scripts/seal_stamp.py:233-280`, read).
`Test_read_sprite` (`tests/skills/test_seal_stamp.py:413`) holds the
following faults with the exact sentence, and it passed (executed): 15
lines, a line of 17 characters, a stray character, a drawn cell on the rim,
and a shadow on the rim. The probe also tried five more inputs (executed).
An empty file is refused as `0 lines`. A trailing blank line is refused as
`17 lines`. A tab and a lowercase `k` are each refused as the character
they carry. A sprite saved with CRLF line endings is accepted, and so is
one with no final newline. A drawn cell in the last column, whose shadow
falls past the sprite but inside the field, is accepted, and `build` draws
that shadow (`seal_stamp.py:331-333`). `candidates/bee-28-pixel.txt` is
accepted, so `assets/seals/README.md:215` holds.

confirms: none
Nothing reads a `.M` chart, a `CHART` name or `read_chart` any more.
Executed: `git grep` for `read_chart`, `CHART`, `CHART_` and the `.M`
spelling outside `seal/`, the changelogs and `.test_durations` matched only
`assets/seals/README.md:92` and `assets/seals/README.md:187`. The first is
the placeholder S's history. The second says that a `.M` chart is not a
sprite.

confirms: none
`draw` refuses in each way the design lists, and the job's `::warning::`
path leaves the note as published. Read: `.github/scripts/release_seal.py:417-464`
refuses where the manifest cannot be read, where it names no `icon`, where
the file cannot be read, where the file lacks the PNG signature and `IHDR`,
and where the copy cannot be written. `seal_release` calls `draw` at line
496, before `gh release view`, the upload and the edit. `main`
(`release_seal.py:530-551`) turns any refusal into one `no seal:` line, one
`::warning::` line and exit 0. Executed: the five draw parameters of
`tests/github/test_release_seal.py:682` (`REASONS_OF_THE_DRAW`, line 319)
run the real `draw`, and they passed.

confirms: none
`publish-release.yml` still runs with Pillow gone. Read:
`release_seal.py` imports nothing outside the standard library, and the
`seal` job's install line (`.github/workflows/publish-release.yml:101`)
names pytest, pytest-xdist, the parser and the renderer. The suite at the
tag no longer has a case that imports Pillow. Executed:
`tests/behaviour/test_the_release_seal_is_drawn.py` and
`tests/behaviour/test_a_release_publishes_its_note.py` passed.

confirms: none
Every path takes one separator on Windows (read). `draw` splits the
manifest's `icon` on `/`, drops the empty and `.` segments, and joins the
parts under `ROOT` with `os.path.join` (`release_seal.py:444-446`). The
fixture helper `page_image` joins with `Path.joinpath` over the split. The
icon case `tests/behaviour/test_chain_hooks_hardening.py:83-103` joins the
split parts with `os.path.join`. It keeps a `.` segment, which every
platform resolves. `SPRITE_PATH` is joined with `os.path.join`.

confirms: none
No Pillow import, pin, install line or fallback command is left for a fresh
clone to trip on. Executed: `git grep -i` for `pillow`, `import PIL` and
`from PIL` outside `seal/`, the changelogs and `.test_durations` matched
four groups. The first is `assets/seals/README.md:29`, which says how the
previews were drawn. The second is the two policy sentences
(`docs/branch-and-release.md:63`, `docs/release-checklist.md:272`), which
the frame's `## Rule changes` gives to the settle. The third is the four
absence assertions of finding 1. The fourth is their comments.
`.github/scripts/run_tests.py` names no Pillow, and `PACKAGES` holds four
entries. `templates/setup/hygiene.yml` and `.github/workflows/hygiene.yml`
install nothing beyond `python3`'s standard library. A further `git grep`
for `12.3.0` matched only the README's line 29.

confirms: none
The icon is a square PNG the directory accepts, the manifest names it, and
it ships. Executed: the probe read the header of `.claude-plugin/icon.png`.
It holds the PNG signature and `IHDR`, it is 512 by 512, and it is 67,791
bytes. `rsvg-convert -w 512 -h 512 assets/seals/owl.svg` drew a file
byte-identical to it. `assets/seals/owl.svg` is byte-identical to
`c8bb9693:assets/seals/candidates/owl-web.svg`. `claude plugin validate .`
in the clone, under a scratch home, exited 0. It printed only the earlier
warning about `CLAUDE.md` at the plugin root and no `ICON_MISSING`. Read:
`.claude-plugin/plugin.json:12` names `./.claude-plugin/icon.png`.
`.claude-plugin` is in `SHIPS`
(`tests/behaviour/test_the_release_check_watches_what_ships.py:43`).
`.claude-plugin/marketplace.json` names the source as `./`, so
`${CLAUDE_PLUGIN_ROOT}` holds the icon.

confirms: none
The owl's entry can be drawn again. Phase 4 claimed this. Executed: the
README's command for the owl (`assets/seals/README.md:125`) was run with its
`v0.23.1:` replaced by `HEAD:`. Its output equals `assets/seals/owl.ans`,
6,199 bytes each.

confirms: none
`gaps.md`'s first two departures hold. In the first, `draw` reads the
manifest under `ROOT` rather than `CODE`, and `ROOT = CODE`
(`release_seal.py:67`), so the release job reads the same tree. In the
second, `read_sprite` checks the shape of every line before it checks the
field (`seal_stamp.py:257-280`), so the shadow check never reads a line that
has not been shape-checked. The faults are still reported in the order the
design lists. Both read.

confirms: none
The orchestrator's `ccf642bf` passes the layout and adds a refusal that its
group does not already hold. Executed: `bin/seal layout --check` exited 0
with 158 files read and 0 refused. `bin/seal layout --pairs` over the three
changed test modules printed 0 pairs. Read: the new case
`tests/github/test_release_seal.py:858` overlaps the `the icon is not a PNG`
parameter of `Test_main`. It also asserts that `draw` leaves no file at the
path it was handed, which none of `Test_main`'s draw refusals checks. The
rename at line 833 is a move, and under `frame/plan.md` *Verification this
work item owes* it owes nothing.

confirms: none
`10a8444a`'s `.test_durations` is CI run 40621949451's, and that run predates
`ccf642bf`. So the file keeps the old name
`Test_draw::test_copies_the_png_the_manifest_names_and_answers_its_width_over_density`
(`.test_durations:1983`) and does not price `ccf642bf`'s two cases (read).
That is 3 keys of about 6,790, far below the 0.05 `STALE_SHARE` of
`tests/behaviour/test_the_windows_leg_runs_in_shards_that_make_the_whole.py:90`.
No case fails on it.

confirms: none
`bin/seal rules --check` exited 0: all 265 check lines in 55 rule files
hold (executed). `uvx ruff check` and `uvx ruff format --check` over the 15
Python files the branch changes both passed (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over this branch, labelled `unverified` | the whole tree | the orchestrator, through `bin/seal gate` after the rounds settle |
| The stamp's modules this round did not run: `tests/hooks/test_sealer_stamp.py`, `tests/hooks/test_sealer_stamp_queue.py`, `tests/behaviour/test_the_stamp_reaches_the_person_it_is_drawn_for.py`, `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py`, `tests/behaviour/test_one_word_one_meaning.py`. The phase 2 and phase 4 records say they passed, which is the implementer's account | `tests/hooks/`, `tests/behaviour/` | the orchestrator's broad run |
| Whether `ccf642bf`'s new case `test_refuses_an_icon_that_is_not_a_png_and_writes_nothing` was seen red before it was committed. The refusal is behaviour this work item added, and no record says how the case was shown failing | `tests/github/test_release_seal.py:858` | the orchestrator, who wrote it |
| That the placeholder S's disc is the same at every tag from v0.20.0 to v0.23.0. Phase 4 claims it drew all five tags, and this round drew none of them | `assets/seals/README.md:86-87` | the sealer |
| `frame/questions.md` Q1: whether the page form keeps the SVG's seven reds or takes the stamp's nine. It is open, and the build shipped default (a) | `frame/questions.md` Q1, `assets/seals/README.md:131-132` | the owner |
| `frame/questions.md` Q3: whether `README.md`, `README.ko.md` and the GitHub social preview show the owl. It is open, and the build shipped default (a), which is neither | `frame/questions.md` Q3 | the owner |
| How the release page shows the 512-pixel icon at 256 CSS pixels, and whether the plugin directory's listing takes the icon. Neither is a file of the tree | the 0.23.1 release page, the directory's portal | the owner, at the release |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository into `<scratch>/1793152332-the-stamps-mark-is-an-owl/round-1/clone`, checked out at `10a8444a` | HEAD `10a8444a8092dc28c75425386f5514a533c5d05e` |
| `env HOME=<scratch>/home python3 test_tmp_owl_probe.py` in the clone, one file run once and deleted. It compared the sprite with the candidate's `.txt`, decoded the candidate's `.ans` at `c8bb9693` and compared its field with `build()`, fed `read_sprite` eight inputs, ran the README's owl command with `HEAD:`, read the icon's header, re-drew the icon with `rsvg-convert`, and drew the twin | exit 0. Sprite equal, 272 bytes. 300 field cells, 25 shadow cells read as `DROP`, 0 mismatches. `read_sprite`: empty `0 lines`, trailing blank `17 lines`, tab and `k` refused, CRLF, no final newline, the shadow past the sprite and the bee accepted. README command equal to `owl.ans`, 6,199 bytes. Icon PNG 512 x 512, 67,791 bytes, the fresh render equal. SVG equal to the candidate. Twin ASCII with the same footprint |
| `bin/seal layout --check` in the clone | exit 0, 158 files read, 0 refused |
| `bin/seal rules --check` in the clone | exit 0, all 265 check lines in 55 rule files hold |
| `bin/seal layout --pairs tests/github/test_release_seal.py tests/skills/test_seal_stamp.py tests/behaviour/test_chain_hooks_hardening.py` in the clone | exit 0, 0 pairs |
| `bin/test -q tests/skills/test_seal_stamp.py tests/github/test_release_seal.py tests/behaviour/test_chain_hooks_hardening.py tests/behaviour/test_the_release_seal_is_drawn.py tests/behaviour/test_a_release_publishes_its_note.py tests/github/test_run_tests.py tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py tests/behaviour/test_release_hygiene.py tests/skills/test_broad_gate.py tests/test_censuses.py` in the clone, under a scratch home and caches | exit 0, 837 passed and 1 skipped |
| `env HOME=<scratch>/home claude plugin validate .` in the clone | exit 0, one warning about `CLAUDE.md` at the plugin root, no `ICON_MISSING` |
| `uvx ruff check` and `uvx ruff format --check` over the 15 Python files `git diff --name-only origin/release/v0.23.1...HEAD` lists, in the clone | exit 0 and exit 0, 15 files already formatted |
