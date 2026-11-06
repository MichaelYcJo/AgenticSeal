# Closing memo: 1793922920-the-windows-leg-finds-path-defects-last

## Not verified

| Item | Who must answer |
|---|---|
| closed the rewritten joins of phase 1 on Windows. `skills/settle/scripts/rule_changes.py#pending`, `evals/scripts/noninferiority.py`, `skills/verify/scripts/seal_stamp.py#queue_for_written_guarantee`, `.github/scripts/finding_counts.py`'s directory of each released work item, the seven test sites joined part by part and the two `tests/skills/test_seal_stamp.py` cases that take a temporary directory now spell their paths with `\` throughout there. Phase 1 ran them on macOS only, under `posixpath` | run 42137403140 at `4e8b9418`: conclusion `success`, each of its four `windows-latest` pytest jobs `success`, read by round 1 (`trail/rounds/round-1.md` *Probes*) and by round 1's fix pass with `gh run view` |
| The joins of `routing.ROUNDS_DIR` on Windows. Round 1's fix pass splits it at `hooks/lib/routing.py#rounds` and `#rounds_unreadable`, `.github/scripts/release_seal.py`'s path of a rounds directory it cannot read, and `.github/scripts/finding_counts.py`'s, so every path `routing.rounds` returns is spelt with `\` throughout there. The pass ran them on macOS only, under `posixpath` | the `tests` run with the Windows legs, which the orchestrator dispatches after round 1's fix pass |

## Not done

The census reads constants a file binds at module level, and not a string bound once inside a function and joined there. Reading function bodies is within reach, and a probe over the tree found no such join at HEAD (`trail/phases/phase-1.md`). It was not built, because `frame/design.md` *Scope* item 1 asks for module-level constants and a census with nothing to catch adds only upkeep. The census's comment names the limit.

The census does not read a constant whose value is an f-string or another name, the shape of `hooks/lib/optin.py#ROUNDS` (`f"{TRAIL}/rounds"`) and of `hooks/lib/routing.py#ROUNDS_DIR` (`optin.ROUNDS`). Inside one file it is within reach: a constant whose value is an f-string with a `/` in its literal part could be read the way an f-string argument is. Round 1's fix pass did not build it. A probe over every tracked `.py` found no join of such a constant inside the file that assigns it, and the four joins of that shape reached the constant from another module, which no reading of one file sees. The four are split by hand, and the census's comment names the limit.
