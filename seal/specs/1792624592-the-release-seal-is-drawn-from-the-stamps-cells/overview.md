# 1792624592-the-release-seal-is-drawn-from-the-stamps-cells — overview

## Why this work exists

The release note's seal was a second drawing of the stamp, an SVG that `rsvg-convert` drew, and now `.github/scripts/release_seal.py` draws the terminal stamp's own cells with Pillow, so the stamp and the release image are one drawing and the release job installs no SVG renderer.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How many cases fail where Pillow is absent | `spec.md` S9: "the line after a failed install still names the release seal's pixel case as the one case that fails". S1 and S2 are two cases, and each reads the PNG with Pillow | the line and its pins name the release seal's pixel cases | `spec.md` S1 and S2 each say "a new case", and S2 has to read the PNG drawn from a chart the case builds, so the two cannot share one case without dropping one scenario. A sentence naming one case would be false the day it shipped |
| What the `seal` job's case refuses | `spec.md` S7: "none installs `librsvg2-bin`". S8: the `git grep` for `librsvg` "finds only the `docs/` sentences `## Rule changes` rewrites". A case naming the package fails S8 | the case asserts that no step of the job runs `apt-get` | It refuses every step S7 refuses and keeps S8 true. With no `apt-get` step the job installs no system package, which is what the removed step was |

## Not verified

| Item | Who must answer |
|---|---|
| closed `tests/test_no_real_identifiers.py::test_only_neutral_domains` was red from 46a773ea through ed9ec343 on three frame lines writing out the W3C's namespace host | the framer's 5e2b93de reworded them; `bin/test tests/test_no_real_identifiers.py -q` exit 0, 6 passed (executed by the framer) |
| the full suite and the repository-wide lint at this branch's head | the orchestrator's broad run |
| the `seal` job at a real tag push draws the new PNG, attaches it and shows it 168 CSS pixels wide | the release run at the v0.22.3 tag, read by the owner |

## Not done

Nothing.

## Fed back into the spec

- S7 says no step of the `seal` job runs `apt-get`, and S9 names the release seal's pixel cases, S1's and S2's; both follow this overview's divergences (framer, 5e2b93de).
