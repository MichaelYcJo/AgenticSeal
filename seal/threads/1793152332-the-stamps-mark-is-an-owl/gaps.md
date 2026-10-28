# Overview: 1793152332-the-stamps-mark-is-an-owl

## Why this work exists

The stamp carried a placeholder S that no longer stood for the name; the owl the owner chose becomes the mark, drawn for the terminal's grid and as a vector for a page, and the plugin gains its icon.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| Where `draw` reads the manifest | `frame/design.md` *Data & interfaces*: `draw` reads the manifest under `CODE` | under `ROOT` | `ROOT` is the module's name for the tree it reads data from, and a case can point it at a fixture; `CODE` also loads `publisher()`, `gate()` and `readers()` in the same run. In the release job the two are one path |
| The order `read_sprite` checks a sprite in | `frame/design.md`: the faults the reader reports, in a listed order | every line's shape first, then the field and the shadow | the shadow check on line N reads line N + 1, which a single pass had not yet shape-checked; the faults are still reported in the listed order |
| The shadow's colour against the owner's candidate | `assets/seals/candidates/owl-28-pixel.ans` drew the 25 shadow cells in (78, 8, 12) | `DROP`, (84, 8, 12), the stamp's own shadow | `frame/design.md` and `frame/questions.md`: every colour is one of the stamp's; the other 275 field cells match the candidate |
| Four cases that pinned a Pillow pin | `frame/design.md` S10: the rewritten cases show that no install line or fallback command names Pillow | each now asserts that no word of its line starts with `pillow` | the case keeps reading the line it read, and a pin put back is refused |
| Row 3's closing grep | `frame/plan.md` row 3 expects the grep for Pillow outside the records to match `assets/seals/README.md` alone | it also matches the two policy documents the frame's Rule changes give the settle, `.test_durations` keys of removed cases, and the four absence assertions above | the policy documents are the settle's to write, and the durations are refreshed from a CI run before the broad run |
| A test comment that cites a removed candidate | `frame/plan.md` row 4's closing grep for `owl-web` and `owl-28-pixel` outside the records expects no match | `tests/skills/test_seal_stamp.py:128` cites `assets/seals/candidates/owl-28-pixel.ans` at `c8bb9693` and stays | the reference case was transcribed from that file at that commit, and the citation names the commit |
| README sentences beyond the row's list | `frame/plan.md` row 4 names four kinds of untrue sentence | the parchment-sheet sentence, the `read_chart` clauses of both section signs, and the disc's tag range, which now reads to v0.23.0, were rewritten too | each stated a fact the change made untrue; the disc was drawn identical at v0.20.0, v0.21.0, v0.22.0, v0.22.1 and v0.23.0 |

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, the repository-wide lint and the typecheck over this branch | the broad gate's run at `081f9086` (`trail/gate.md`), and #1101 merged with lint and the suite green on the ubuntu, macOS and Windows legs |

## Not done

nothing

## Fed back into the spec

none
