# Review round 2: 1793401152-the-seal-draws-a-round-headed-little-owl

target: 87fd511d, fixes 08d8d1dc..87fd511d

## Findings

None. The fix range holds five commits: `72083ad6` and `87fd511d` fold the
frame, `b5f01c6f` and `a1d60719` are the fix pass, and `042b9573` records
its verdicts. None of them made a defect this round found. The round read
those five commits and nothing outside them.

## Confirmations

confirms: round-1#1
The close holds. The fix pass's answer claimed that the census passes
after the fix. At `87fd511d`, `tests/test_censuses.py`, including
`Test_module::test_every_file_no_module_file_declares_meets_every_census`,
passes in the run of probe row 1. `72083ad6` rewrote `frame/design.md:49`
and `frame/plan.md:11`. `b5f01c6f` rewrote `trail/phases/phase-1.md:29-33`,
and it touches `phase-1.md`, which `location:` names. The answer also
claimed the class was enumerated wider than the four lines: the S10
paragraphs of both phase records, and the plugin cache's home-relative path
in `phase-2.md`. I read the diff at `phase-1.md:117-127` and
`phase-2.md:15-17`, `:100-102` and `:111-117`. Each now names the
repository and the cache in words. A search for a user path other than the
fixture's, in slashed or slug form, over `seal/threads/` and
`TRADEMARKS.md`, exits 1. A search for the private repository's name over
the whole tree also exits 1, `frame/design.md` S10 included after
`87fd511d` (probe row 2). Both phase records now say that their boundary
sets left out `tests/test_censuses.py`. That replaces the claim round 1
found untrue, rewritten in place (contract rule 19). The history rows of
round 1's `## Not judged` are still the orchestrator's: `e6365343`,
`56c94b6f` and `c857202a` still carry the paths in their trees.

confirms: round-1#2
The close holds. I read `TRADEMARKS.md:10-21` at `87fd511d`. The list now
names the reserved files by kind: every `.svg`, `.png` and `.ans` file
under `assets/seals/`, `candidates/` included, and each `.txt` file, the
sprite or chart of a mark. A closing sentence says `assets/seals/README.md`
and its commands are not reserved, nor is any other code. A listing of
`assets/seals/` at `87fd511d` holds 8 `.ans`, 9 `.png`, 3 `.svg`, 3 `.txt`
and one `.md`, the README. So the kinds cover every file but the README,
and the three `.txt` files are the candidates' charts and sprite (probe
row 3). The description "the emblem each release carried and the
candidates kept beside it, which no release carried" is now true of the
section signs and the bee. `87fd511d` gives `frame/design.md:32`'s
parenthesis the same list, so the frame and the notice state one list.
`all rights reserved` still matches `TRADEMARKS.md:8` alone outside
`seal/threads/`. `tests/behaviour/test_docs_line_wrap.py` and
`tests/behaviour/test_the_release_check_watches_what_ships.py` pass
(probe row 1).

Carried from round 1 and not re-established: the transcription, `build`,
S7, S8, the blob moves and the narrow run of `2af276c8`. The fix range
touches none of `skills/`, `tests/`, `assets/` or `.claude-plugin/`.
`git diff --stat 08d8d1dc..87fd511d` lists `TRADEMARKS.md` and five files
under the work item's directory, and nothing else.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the branch's history is rewritten before the first push, since `e6365343`, `56c94b6f` and `c857202a` still carry the paths of round 1's finding 1 in their trees | the branch `chore/1174-the-seal-draws-a-round-headed-little-owl` | the orchestrator, with the owner |
| The full suite, the repository-wide lint and format check | the branch at `87fd511d` | the orchestrator, through `seal gate` |
| Whether `TRADEMARKS.md` works as a notice in law | `TRADEMARKS.md` | the owner |
| The record's path: the only worktree on the branch is the main checkout, so the record is written there | `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/trail/rounds/round-2.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/test_censuses.py tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_the_release_check_watches_what_ships.py -q -p no:xdist` in a clone at `87fd511d` | exit 0, 255 passed |
| `git grep -q -E` for a user path other than the fixture's, slashed or as a slug, over `seal/threads` and `TRADEMARKS.md`; `git grep -q -i` for the private repository's name over the tree | both exit 1 |
| `git ls-tree -r --name-only HEAD assets/seals`, counted by extension, and the files that are not `.ans`, `.png`, `.svg` or `.txt` | 8 `.ans`, 9 `.png`, 3 `.svg`, 3 `.txt`, 1 `.md`; the one other file is `assets/seals/README.md` |
| `git grep -n -i 'all rights reserved' -- ':!seal/threads'` | `TRADEMARKS.md:8` alone |
