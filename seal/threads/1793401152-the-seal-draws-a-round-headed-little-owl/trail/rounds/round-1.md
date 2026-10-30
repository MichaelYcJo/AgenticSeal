# Review round 1: 1793401152-the-seal-draws-a-round-headed-little-owl

target: 2af276c8 against release/v0.25.1

## Findings

### 1. Three of the work item's records name a real user path, so the tree-wide census fails and the private copy's location is published

severity: must
location: `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/frame/design.md:49`, `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/frame/plan.md:11`, `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/trail/phases/phase-1.md:29`, `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/trail/phases/phase-1.md:31`
evidence: executed `bin/test "tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census" -q -p no:xdist`
verdict: open

`CONTRIBUTING.md` *House rules* says examples, fixtures and docs use
`example.com` and `/Users/x/` only. The `real_identifiers` census in
`tests/censuses.py` enforces this over every tracked file, and the
work item's records are tracked. The case above failed at `2af276c8` with
four lines and nothing else. `frame/design.md:49` (S2) gives the
durable copy as an absolute path under a real user's home directory.
`frame/plan.md:11` gives the same path, and also defines `<scratchpad>` as
the absolute scratchpad path, which spells the user's name in the
projects-directory slug that `SLUG_USER_RE` reads. `trail/phases/phase-1.md:29`
and `:31` repeat both paths. The broad gate runs this case, so the seal
cannot be taken while these lines stand.

The house rule's own grounds say why this is a must and not a lint.
A real machine path in a public repository is the leak that forces a
history rewrite. The frame's decision 7 says the same about the brand's
private material: no public text points at it. S10 exempts `seal/threads/`
from the brand-repository grep. That exemption covers the repository's
name, but not an absolute path to the owner's home directory, which no
frame row allows and the census refuses.

What was claimed and what was found. `trail/phases/phase-2.md:111-114`
says its boundary set included every module that reads the tracked file
list. `tests/test_censuses.py:964` reads `git ls-files` and judges every
tracked file. That module was not in the command at `phase-2.md:118`, and
phase 1's command at `phase-1.md:114` did not hold it either. Phase 1's
commit `c857202a` added two of the four lines, so phase 1's boundary set
owed the module by contract rule 2.

The branch is not on the remote yet (`git ls-remote --heads origin
'*1174*'` printed nothing). `e6365343`, `56c94b6f` and `c857202a` carry the
paths in their trees. A fix commit removes the paths from the tip only;
whether the history is rewritten before the push is a row of
`## Not judged`.

The fix rewrites each sentence in place, keeping a coordinate a person can
open without naming the home directory:

```markdown
<!-- frame/design.md:49, inside S2's second cell: replace the clause
     "and a durable copy is `<absolute path>` in the owner's private repository" with -->
and a durable copy is `candidates/little-owl-16-on-wax.ans` under the brand skill of the owner's private brand repository

<!-- frame/plan.md:11: replace the sentence "`<scratchpad>` is `<absolute path>`." with -->
`<scratchpad>` is the orchestrating session's scratchpad directory.
<!-- and in the same line, replace "at `<absolute path>` in the owner's private repository" with -->
as `candidates/little-owl-16-on-wax.ans` under the brand skill of the owner's private brand repository

<!-- trail/phases/phase-1.md:28-31 -->
**The reference was transcribed from the approved stream.** The file read
is `<scratchpad>/owl/f1/stamp.ans` (sha256 `62b56aeb…7130d`). `cmp` of it
with the durable copy in the owner's private brand repository,
`candidates/little-owl-16-on-wax.ans` under its brand skill,
```

The precondition: `<scratchpad>` is already the placeholder the plan and
the phase record use for the same directory, so no reader loses a
coordinate. After the edit, the case in `evidence:` passes.

answer:

### 2. TRADEMARKS.md reserves every file under assets/seals/, which includes the README's commands and drawings no release shipped

severity: should
location: `TRADEMARKS.md:10-11`, `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/frame/design.md:32`
evidence: read `TRADEMARKS.md:1-15`, `assets/seals/README.md:171`, `assets/seals/README.md:187`, `assets/seals/README.md:207-217`
verdict: open

The owner's decision 6, as `frame/design.md` *Grounding* quotes it, puts
the AgenticSeal name, the owl emblem and its seal drawings outside the MIT
License, and keeps the code under MIT. `TRADEMARKS.md:3-5` says the same.
Its list at `:10-11` then names "every file under `assets/seals/`, the
emblem as each release drew it". Two kinds of file under that directory
fit neither half of that description:

- `assets/seals/README.md` is prose and code. Its commands at `:171` and
  `:187` are Python that a reader is told to run. Under the list, they are
  "all rights reserved", while `:3` says the repository's code is MIT. A
  reader cannot tell which sentence governs the commands.
- `assets/seals/candidates/` holds the section signs and the bee, which no
  release drew (`assets/seals/README.md:207-217` says the owner shipped
  neither section sign and chose the horned owl over the bee). "The emblem
  as each release drew it" does not describe them.

The build follows the frame: Scope item 7 at `frame/design.md:32` names the
directory as `assets/seals/`. So the defect is in the frame's reading of
decision 6, and the build carried it over. `gaps.md` leaves the notice's
legal force to the owner, and this finding does not judge that. It judges
whether the list agrees with the notice's own first paragraph. The owner may
mean to reserve the README and the candidates too. If so, the fix pass
rejects this finding and says so, and the list's description changes to
match instead.

```markdown
- every drawing under [`assets/seals/`](assets/seals/), its `.ans`, `.png`,
  `.svg` and `.txt` files: the emblem as each release drew it, and the
  candidates kept beside it;
```

The same words go into Scope item 7's parenthesis at
`frame/design.md:32` ("the drawings under `assets/seals/`"), so the frame
and the notice state one list. `tests/behaviour/test_docs_line_wrap.py`
covers `TRADEMARKS.md`, and the lines above are under its limit.

answer:

## Confirmations

confirms: none
The terminal reference is the approved picture. The frame and phase 1
claimed that `REFERENCE_DISC` was transcribed from the approved stream by a
script that reads no line of `seal_stamp.py`. I parsed the durable copy of
the approved stream myself, with a parser of my own and the colour table
typed from `frame/design.md` *Data & interfaces*. All 28 half-rows were
28 cells wide and used exactly 15 colours, with no colour outside the
table. `tests/skills/test_seal_stamp.py`'s `REFERENCE_DISC` differs from
the stream in 0 of 784 half-cells. `seal_stamp.build()` at `2af276c8`
also differs from the stream in 0 of 784. The disc half of each
`REFERENCE_TWIN` line equals the stream's letters by `letter_row`'s rule
(the top half where drawn, else the bottom half). Executed; probe row 1.

confirms: none
`build` and the test's `owners_disc` give the same cells by different
orders, as `trail/phases/phase-1.md` says. I read
`skills/verify/scripts/seal_stamp.py:331-394` against
`tests/skills/test_seal_stamp.py:221-259`. `build` tests the outer edge
only inside `d > RADIUS - STEP_INSET`. That is the same cell set, because
`edge - EDGE_WIDTH` is at least 13.5 - 0.45 - 0.25 - 1 = 11.8, above both
9.8 and the lip's 10.6. The gloss test sits after the outer edge in both.
`GLOSS_INSETS` unpacks as `inner, outer` = 1.9, 0.7, which gives
11.6 < d < 12.8, the frame's band. `math.degrees(atan2(dy, dx)) % 360`
puts the upper left at 225, inside 200 to 250. Read.

confirms: none
`read_sprite`'s field bound is unchanged at 9.8 (`RADIUS - STEP_INSET`
against the old `DISC_CELLS / 2 - GROOVE_INSET`). The new
`on-the-step-ring` case draws line 2 column 1, at sqrt(7.5^2 + 6.5^2) =
9.925 cells from the centre. With half-integer offsets of at most 7.5 on
each axis, the smallest squared distance above 96.04 is (15^2 + 13^2) / 4
= 98.5. So the case is the nearest cell outside the bound, as its
docstring says. Read, at `tests/skills/test_seal_stamp.py:462-496`.

confirms: none
S7 holds for both owls. The new entry's command, with `v0.25.1` replaced by
`2af276c8`, writes `assets/seals/owl.ans` byte for byte (5,931 bytes). The
horned owl's command from `v0.23.1` writes `assets/seals/horned-owl.ans`
byte for byte (6,199 bytes). Executed; probe row 3.

confirms: none
S8: the icon is the SVG at 512 pixels. `.claude-plugin/icon.png` is a
512 x 512 RGBA PNG (`file`). Redrawn from `assets/seals/owl.svg` by
`resvg_py.svg_to_bytes(..., width=512, height=512)` in the session's
scratchpad environment, it is byte for byte the committed file. Executed;
probe row 4. Whether it looks like the approved drawing is the owner's.

confirms: none
The moves are moves. The blobs are equal for
`efb91989:assets/seals/candidates/little-owl-16.txt` and
`skills/verify/scripts/seal-mark.txt` (`993b924c`), for
`efb91989:assets/seals/candidates/little-owl-wax-seal.svg` and
`assets/seals/owl.svg` (`a5ad92d8`), and for each of the horned owl's
`56c94b6f:assets/seals/owl.*` and `horned-owl.*`. `assets/seals/candidates/`
lists the same eleven files at `2af276c8` as at the base. Executed;
probe row 5.

confirms: none
S9 and S10 hold outside `seal/threads/`. `git diff aa9221d3 2af276c8 --
LICENSE` is empty. `all rights reserved` matches `TRADEMARKS.md:8` alone.
No file is named `assets/seals/candidates/little-owl-*`. Of the other S10
greps, `little-owl-16|little-owl-wax-seal`, `부엉이` and the brand
repository's name each exit 1 outside `seal/threads/`. So does
`scratchpad|wax3|owl_final` over the files S10 lists. Executed; probe row 6.
Finding 1 is about `seal/threads/`, which S10 leaves out.

confirms: none
`TRADEMARKS.md` stays home and still reaches the install, as
`tests/behaviour/test_the_release_check_watches_what_ships.py:65-68`
says. The installed 0.25.0 plugin's root holds `LICENSE`, both READMEs,
`docs/` and `tests/` (`ls`, executed), so the install copies the root. No
reader of `KEY`, `DISC_COLOURS`, `SPRITE_COLOURS` or `letter_row` exists
outside the module and its test (`git grep`, executed), so the twin's new
letters reach no other parser.

confirms: none
The touched modules pass at `2af276c8`: 307 passed. Executed; probe
row 2. This is a narrow run, not the broad gate. `gaps.md` labels the suite
`unverified` and names the orchestrator, and that label is honest. Finding
1 shows the broad run would fail at this commit.

No earlier round exists, so this round carried no fact from one. Every
fact above was established this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the wax stamp, `owl.png` and `.claude-plugin/icon.png` look like the drawings the owner chose | `assets/seals/owl.png`, `.claude-plugin/icon.png` | the owner, at the pull request |
| Whether `TRADEMARKS.md` works as a notice in law; finding 2 reads only whether its list agrees with its own first paragraph | `TRADEMARKS.md` | the owner |
| Whether the branch's history is rewritten before the first push, since `e6365343`, `56c94b6f` and `c857202a` carry the paths of finding 1 and a pull request shows every commit even when the merge squashes | the branch `chore/1174-the-seal-draws-a-round-headed-little-owl` | the orchestrator, with the owner |
| The full suite, the repository-wide lint and format check | the branch at `2af276c8` | the orchestrator, through `seal gate` |
| Whether the relative links to `TRADEMARKS.md` resolve on GitHub's rendered pages | `README.md:701`, `README.ko.md:698`, `assets/seals/README.md:16` | the orchestrator, on the pull request |
| The record's path: the prompt asked for the record in the branch worktree, and the only worktree on the branch is the main checkout, so the record is written there | `seal/threads/1793401152-the-seal-draws-a-round-headed-little-owl/trail/rounds/round-1.md` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I test_tmp_reference.py <durable copy of the approved stream>` in the round's clone: a parser of the stream's SGR codes, the frame's colour table typed in, `ast` reading `REFERENCE_DISC` and `REFERENCE_TWIN`, and `seal_stamp.build()` | 28 half-rows of 28; 15 colours, none outside the table; `REFERENCE_DISC` against the stream 0 differences; `build()` against the stream 0 differences; the twin's disc half against the stream no differing line. The file was deleted after the one run |
| `bin/test tests/skills/test_seal_stamp.py tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py tests/behaviour/test_the_release_check_watches_what_ships.py tests/behaviour/test_docs_line_wrap.py tests/github/test_release_seal.py -q` | exit 0, 307 passed |
| `assets/seals/README.md`'s two draw commands, the new one with `v0.25.1` replaced by `2af276c8`, each written to a scratch file and `cmp`'d with `assets/seals/owl.ans` and `assets/seals/horned-owl.ans` | both `cmp` exit 0; 5,931 and 6,199 bytes |
| `<scratchpad>/venv/bin/python -c` writing `bytes(resvg_py.svg_to_bytes(svg_path="assets/seals/owl.svg", width=512, height=512))` to a scratch file, then `cmp` with `.claude-plugin/icon.png` | `cmp` exit 0 |
| `git rev-parse` of the six pairs of moved blobs, and `git ls-tree -r --name-only` of `assets/seals/candidates` at `2af276c8` and at `aa9221d3` | each pair one blob; the two listings equal, eleven files |
| S9's and S10's commands as `frame/design.md` gives them, run outside `seal/threads/` | each grep exit 1, except `all rights reserved`, which matched `TRADEMARKS.md:8` alone; `git diff` of `LICENSE` empty |
| `bin/test "tests/test_censuses.py::Test_module::test_every_file_no_module_file_declares_meets_every_census" -q -p no:xdist` | exit 1, 1 failed: four `real_identifiers` lines, at `frame/design.md:49`, `frame/plan.md:11`, `trail/phases/phase-1.md:29` and `:31` |
