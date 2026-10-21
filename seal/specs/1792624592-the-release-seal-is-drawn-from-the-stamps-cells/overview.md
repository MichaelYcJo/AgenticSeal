# 1792624592-the-release-seal-is-drawn-from-the-stamps-cells — overview

## Why this work exists

The release note's seal was a second drawing of the stamp, an SVG that `rsvg-convert` drew, and now `.github/scripts/release_seal.py` draws the terminal stamp's own cells with Pillow, so the stamp and the release image are one drawing and the release job installs no SVG renderer.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| How many cases fail where Pillow is absent | `spec.md` S9: "the line after a failed install still names the release seal's pixel case as the one case that fails". S1 and S2 are two cases, and each reads the PNG with Pillow | the line and its pins name the release seal's pixel cases | `spec.md` S1 and S2 each say "a new case", and S2 has to read the PNG drawn from a chart the case builds, so the two cannot share one case without dropping one scenario. A sentence naming one case would be false the day it shipped |

## Not verified

| Item | Who must answer |
|---|---|
| `tests/test_no_real_identifiers.py::test_only_neutral_domains` is red at 46a773ea on three lines of the frame that write out the W3C namespace host (`spec.md` lines 18 and 149, `plan.md` line 101), and on nothing else | the orchestrator, by rewording those three lines so they name the host without writing it, then running the case |
| the full suite and the repository-wide lint at this branch's head | the orchestrator's broad run |
| the `seal` job at a real tag push draws the new PNG, attaches it and shows it 168 CSS pixels wide | the release run at the v0.22.3 tag, read by the owner |

## Not done

Nothing.

## Fed back into the spec

None.
