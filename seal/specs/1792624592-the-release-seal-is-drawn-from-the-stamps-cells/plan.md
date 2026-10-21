# Implementation Plan: the release seal is drawn from the stamp's cells (#1009)

<!-- seal/specs/<unix-epoch-seconds>-<slug>/plan.md holds HOW, in phases. It
is the Design Gate's artifact: where the work alters observable behaviour,
approval of this plan is the gate. -->

Approved <date> by <who>, when `smith` was spawned.

<!-- The line above is the record that the gate happened. The orchestrator
writes it when it spawns the build, in the shape and on the terms
`skills/implement/orchestration.md` *The plan is approved at the spawn*
states, including the shape where `routing.md` answers `Implementation`
with `the session`. A later session, a reviewer and CI all read the tree,
and a plan with nobody's name on it cannot be told from one nobody approved.
The line shares its shape with `templates/sdd-routing.md`'s `Answered <date>
by <who>, before the first edit.`: the verb, the date, who, and the moment.
The two are pinned against each other, so neither spelling can drift into a
second convention for one kind of fact. -->

## Summary

The release note's seal stops being the owner's SVG and becomes the terminal
stamp's disc, drawn by `.github/scripts/release_seal.py` from
`skills/verify/scripts/seal_stamp.py#build` with Pillow, one cell to one
square block of pixels (`spec.md` *Data & interfaces* sets its size). The SVG, its renderer and its install step
go, and every sentence and case that states them is rewritten or removed in
the same phase. The `docs/` sentences change through `spec.md`'s
`## Rule changes`.

## Technical context

**What this builds on** (read at eae7f0ad):

- `.github/scripts/release_seal.py`: `module()` and `_module()` (lines
  85 to 95) load a tree module by path, once; `SVG`, `SEAL_PX`, `DENSITY`
  (lines 108 to 114); `rasterise` (lines 425 to 444); `seal_release` calls
  `rasterise` at line 476 and passes `SEAL_PX` to `sealed_glance` at line
  494; `main` turns every exception into one `no seal:` line, one
  `::warning::` and exit 0 (lines 510 to 531).
- `skills/verify/scripts/seal_stamp.py#build` (lines 258 to 304) returns
  `(w, h, px)`: 28 by 28 cells, each one of the nine `DISC_COLOURS` or
  None. The comment above `DISC_CELLS` (lines 190 to 197) says a cell is one
  column by one half-row and so square. `CHART` is read at import (line
  255), and `build`'s inner `on` reads the module's `CHART` when it is
  called, so a case can replace `CHART` on the loaded module.
- `.github/workflows/publish-release.yml`, job `seal`: the pip step (line
  101) installs `pillow==12.3.0` before the suite and the draw; the
  `install rsvg-convert` step (lines 102 to 116) goes.
- `tests/test_the_release_seal_is_drawn.py`: `wired` (line 692) patches
  `subprocess.run` with the `rsvg_convert` stand-in; it will patch `draw`
  instead. `test_any_failure_leaves_the_note_as_it_was_published` (line
  799) is the failure parametrisation S4 and S5 extend.
- `.github/scripts/run_tests.py`: the Pillow paragraph of the docstring
  (lines 65 to 70), the comment above `PILLOW_VERSION` (lines 110 to 117),
  and the top-up's two messages (lines 327 to 342).

**The rule changes were checked in memory by the framer** (executed):
`skills/settle/scripts/rule_changes.py#parse` of `spec.md` returned three
`change` items and no error, and `#apply_op` of each on the document at
eae7f0ad applied, leaving no `rsvg` in either document. No other unsettled
spec rewrites those sentences: the two earlier seal work items and the
other four whose sections name these documents carry the no-change block.

**The window.** From the merge until the owner's settle applies this spec,
`docs/branch-and-release.md` and `docs/release-checklist.md` still say
`rsvg-convert`. A person who follows the checklist's hand-drawn route in
that window and has Pillow missing reads `no seal: Pillow is not
installed...` from the script itself, which names the fix. `questions.md`
Q1 offers the owner the other path.

**The release this lands in draws itself with it.** `publish-release.yml`
runs from the checkout at the tag, so v0.22.3's own seal is drawn by the
new code, unlike a hook, which runs from the installed plugin.

**The failure scenario of the chosen approach, six months on.** A change to
`seal_stamp.py#build`'s signature or meaning (#857 changing the chart is not
one: the image follows it) breaks the release draw. The tag push would
surface that only as a `::warning::` and a note without its image. The S1
case is what catches it first: it runs in every pull request's suite and in
the suite the `seal` job runs at the tag before the draw.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A1. Keep the owner's SVG drawn by `rsvg-convert` (the structure in the tree) | Two drawings of one seal: #857's mark would be charted for the stamp and redrawn as paths for the SVG, and the release page shows a seal no terminal shows. The premise that kept it, that the staircase edges are a defect (#832), is the premise the owner withdrew on 2026-10-22 (issue #1009) | rejected |
| A2. `release_seal.py` reads `seal_stamp.py#build` and paints each cell as one square block with Pillow | `build`'s interface changes and the release draw breaks; the S1 case runs in every suite and catches it before a tag | **chosen** |
| A3. As A2, with a PNG written by the standard library (`zlib` and `struct`) instead of Pillow | No dependency at all for the draw, but the repository then owns a PNG encoder (signature, chunk CRCs, filter bytes) that nothing else needs, and its one reader would be Pillow in the case anyway. The owner named Pillow, and the `seal` job installs it already | rejected |
| A4. Replace the release script's drawing with a PNG option in `seal_stamp.py` itself | `seal_stamp.py` ships to every plugin user and must load where Pillow is absent (`tests/test_the_seal_is_taken_once_by_the_sealer.py#test_the_stamp_module_imports_with_pillow_blocked`); a release-only concern would ship with it. Keeping the publishing path in `release_seal.py` rests on a premise checked here: issue #1009 changes only how the PNG is drawn, and the counts, the glance guard, the upload and the edit are untouched | rejected |
| A5. Paint from `compose`'s terminal cells (`▀` with a foreground and a background) instead of `build`'s grid | It needs rows for the text block, which the image does not carry, and adds a second decoding of what `build` already answers per cell | rejected |
| A6. The two `docs/` pins: keep their `rsvg-convert` assertions until the settle, or drop them now | Kept, they assert a sentence the settle rewrites, so the settle that applies this spec meets two red cases, and `settle --apply` writes no sentence by hand. Dropped now, the sentences are unpinned in the window; what the image is, is pinned by S1 and S2, and every other assertion of both cases stays | drop now, **chosen** |
| A7. Edit the `docs/` sentences in this diff, as work item 1792473741 did on its owner's answer | The standing rule says a pull request does not edit `docs/`; only the owner can grant the exception | `questions.md` Q1; the build proceeds on the rule |
| A8. Keep `SEAL_PX = 160` and fit 28 cells into 320 PNG pixels | 320 is not a whole multiple of 28, so cells would be of unequal widths or blended, and the block is no longer one cell | rejected; the width is derived |

## Phases

Vertical slices: each phase ends with something runnable and verified.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The draw from cells. `release_seal.py`: `draw(png)` with Pillow imported inside it, `CELL_PX`, the derived width, the stamp loaded through `module()`, `SVG`, `SEAL_PX` and `rasterise` gone, the docstring rewritten. `.github/scripts/release-seal.svg` deleted. `tests/test_the_release_seal_is_drawn.py`: S1, S2, S3, S4, S5 and S6's cases, `wired` standing in for `draw`, the SVG cases, fixtures and failure parameters gone, the module docstring and banner rewritten. `tests/test_no_real_identifiers.py`: the `www.w3.org` entry gone. `seal_stamp.py`: the docstring paragraph naming the release script rewritten | `bin/test tests/test_the_release_seal_is_drawn.py tests/test_no_real_identifiers.py tests/test_the_seal_is_taken_once_by_the_sealer.py -q`; each new case shown red as `spec.md` says, the showing written in the phase record | |
| 2 | The workflow and the prose outside `docs/`. `publish-release.yml`: the `install rsvg-convert` step and its comment gone, the opening comment rewritten. `tests/test_a_release_publishes_its_note.py`: the install case gone, the step count five. `run_tests.py`: the docstring paragraph, the `PILLOW_VERSION` comment and the top-up messages rewritten. `tests/test_the_suite_has_a_command_that_is_cheap_twice.py`: S9's pins. `CONTRIBUTING.md` *Running the checks*. The two `docs/` pins trimmed as `## Removes` says. S8's grep | `bin/test tests/test_a_release_publishes_its_note.py tests/test_the_suite_has_a_command_that_is_cheap_twice.py tests/test_the_release_seal_is_drawn.py -q`; S8's `git grep`, its output in the phase record | |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past
one, which someone can open.

The party that builds a phase fills its cell as the phase closes, not at the
end. A phase reconstructed afterwards is reconstructed from the diff, which is
where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. The party that builds the phase
writes it to `seal/specs/<work-item-id>/phases/phase-N.md`, from
`templates/sdd-phase.md`, when the phase closes.

Where feature branches squash, these commits stop resolving at the merge, and
**a rebase during the work does the same thing earlier and more quietly**,
because the orphaned object still answers `git cat-file` in the worktree that
wrote it. **The party that rebases the branch re-reads this column after the
rebase**, or the column names commits that resolve in one clone and nowhere
else. Nothing measures from this column, which is why that is tolerable.

## Operational impact

- **A release dependency goes.** The `seal` job no longer installs
  `librsvg2-bin` with `apt-get`. Pillow, already installed by the job's pip
  step at the version `.github/scripts/run_tests.py#PILLOW` pins, draws the
  PNG.
- **The image on the release page changes**: the stamp's disc with square
  cells, transparent outside the disc, at the width `spec.md` *Data &
  interfaces* derives. Releases already published keep their attached
  `seal.png`; nothing redraws them.
- **No gate changes, and nothing a plugin user installs changes.**
  `seal_stamp.py` keeps its imports; only its docstring changes.
- **A hand-drawn seal needs Pillow** in the `python3` that runs
  `release_seal.py`. `bin/test`'s `.venv` has it.
