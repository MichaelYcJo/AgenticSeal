# 1792365855-the-placeholder-s-emblem-has-no-assets-entry — review round 1

target: abc49184 against release/v0.22.2

The diff read is `769f2aa4..abc49184`, the commit this branch was cut at to
its head. The base has since gained #966 at `8a100e13`, which touches no file
of this branch. This is round 1, so no fact was carried from an earlier
round: every fact below was established in this round. The work item is on
the second rung, so it has no `spec.md` or `plan.md`. The frame is issue
#978, the repository's `CLAUDE.md`, and `assets/seals/README.md`'s own
conventions. `overview.md` is the smith's account, and each of its claims was
checked as a claim.

## Findings

### 1. The new entry restates the frame, the chart and #857 that §*Candidates for #857* already states, so the page now holds three statements of one fact

severity: should
location: `assets/seals/README.md:84-87`, `assets/seals/README.md:99`, `assets/seals/README.md:105-111`
verdict: fixed eba4fa05

The repository's `CLAUDE.md` says a fact has one source, and every other
place links to it. `assets/seals/README.md` now says that the frame is
settled, the mark is Georgia Bold's S in `seal-mark.txt`, and #857 decides
what the mark becomes. Before this branch it said so once, in the opening
paragraph of §*Candidates for #857*. That paragraph was written while the S
had no entry and was the only place the page described the S. The new entry's
**Issue** bullet adds a second statement of the same facts. The rewritten
§*The next entry* adds a third statement about #857. The sentence "What the
mark becomes is #857." now appears word for word at line 86-87 and at line
109. When #857 lands, all three places must be rewritten together, and a
fix that reaches only one of them leaves the page contradicting itself.
Contract §19 asks a change to correct what stood on the old fact. Here the
old fact is that the S has no entry, and the §*Candidates* paragraph stood
on it.

Read: `assets/seals/README.md` at `abc49184`, lines 84-87, 97-101 and
105-111. `git diff 769f2aa4..abc49184 -- assets/seals/README.md` shows that
lines 105-111 are unchanged and lines 84-87 and 99 are new.

The entry is the natural home for these facts now, so the fix moves the
§*Candidates* paragraph to point at the entry and keeps only what the entry
does not state: the frame's parts and the chart's shape. Replace lines
105-111 with:

```markdown
The placeholder S above stands on the disc whose frame the owner settled
on 2026-10-07: 28 cells across, a wax edge, a rim lit from the upper left,
a groove and the field. Its chart is 28 lines of 28 characters over `.M`.
The owner looked at these three marks the same day and shipped none of
them; they wait here for #857.
```

answer: Holds. The entry's **Issue** line is now the one home for the mark, its chart file and #857. Lines 105-111 are the round's rewrite, used verbatim. §*The next entry* now reads "The mark that replaces the placeholder S gets its entry once a tag carries it", which names the mark without restating who chooses it. The same class also covered the parchment sheet: the entry said #832 "took the parchment sheet away", and §*Candidates for #857* already states that the owner retired it. The entry drops that clause. A `grep` for `#857`, `seal-mark.txt`, `Georgia` and `parchment` on the page now finds each fact once, plus links to it and alt text.

## Confirmations

confirms: none
The README's draw-again command for the placeholder S reproduces the
committed file byte for byte. Executed: in a `--no-local` clone at
`abc49184`, I ran the command from `assets/seals/README.md:91` exactly as
written, from `assets/seals/`, over the committed `placeholder-s.ans`. It
exited 0 and wrote 5,498 bytes. `git status --porcelain` printed nothing,
and `cmp` against the main checkout's file exited 0. The **Bytes** line at
`assets/seals/README.md:94-95` holds.

confirms: none
The smith claimed that `seal-mark.txt` is the same from v0.20.0 to v0.22.1.
Executed: `git rev-parse <tag>:skills/verify/scripts/seal-mark.txt` gives
`80593dfc` at v0.20.0, v0.21.0, v0.21.1, v0.22.0 and v0.22.1, and the path
is absent at v0.19.0. `git log --diff-filter=A` names `149ca9e`, whose
subject ends `(#832) (#859)`, so the **Issue** line's "#832, through pull
request #859" holds as well.

confirms: none
The claim "The disc is the same at every tag from v0.20.0 to v0.22.1"
(`assets/seals/README.md:80-81`, and the first row of `overview.md`'s
divergence table) holds. Executed: a probe loaded each tag's
`seal_stamp.py` with its own `seal-mark.txt`, drew `stamp(SAMPLE_ROWS)`, and
compared the first 28 cells of each of the 14 lines (character, foreground,
background and attributes) with v0.22.1's. Every cell both tags draw is
equal. The only difference is trailing blank padding on the lines where
v0.22.1's shorter panel has no text. v0.20.0's docstring says the disc is one
size at every scale (read), so calling it at its default scale does not hide
a difference.

confirms: none
The panel history at `assets/seals/README.md:81-82` holds. Executed: the
probe printed `SAMPLE_ROWS` for each tag. It has a `ledger` row through
v0.21.1, none at v0.22.0, and at v0.22.1 the shorter panel of `tree`,
`base`, `item`, `gate` and `rounds`. Read: `git show 5b1f6fa`, whose subject
ends `(#944) (#950)`, removes the `ledger` sample row. `git show f1c9932`,
whose subject ends `(#975) (#977)`, rewrites `SAMPLE_ROWS`. Both commits
fall in the tag ranges the line names.

confirms: none
The smith said the lilies' command shape does not draw the S. That claim and
the README paragraph at `assets/seals/README.md:28-34` hold. Executed: if
v0.20.0's or v0.22.1's `seal_stamp.py` is loaded with no `__file__`, it
raises `NameError: name '__file__' is not defined`. From v0.21.0, `stamp` has
the signature `(rows, shape=False, disc=True)` and the module has no
`DEFAULT_SCALE`. So the S's command must point the module at a chart and must
pass no scale, as the paragraph says.

confirms: none
The smith claimed that the preview rule now in `assets/seals/README.md:17-25`
reproduces the five earlier previews pixel for pixel. Executed: I ran the
smith's renderer, kept outside the tree in the session scratchpad as
`978/ans_png.py`, under `uv run --with pillow==12.3.0` at `--size 19
--dim-alpha 128`. All six committed `.ans` files were redrawn
(`gold-lily`, `red-lily`, `placeholder-s` and the three candidates), and
each matched its committed `.png` with 0 differing pixels. Read: the
renderer's code does what the paragraph says. It uses 12 × 24 cells, draws
half-blocks as two halves, uses Menlo for text with the anchor centred in
the cell, reads 256-colour codes through xterm's table, and draws the
default foreground as (128, 128, 128). Executed: an inventory of the codes
in each `.ans` found that bold (`1`), dim (`2`) and green (`32`) occur only
in `placeholder-s.ans`, so "adds three styles" holds. A 256-colour code
(`38;5`, `48;5`) occurs in `red-lily.ans` and in
`candidates/section-14-light-red.ans`, so the xterm-table sentence describes
earlier files. With half opacity drawn as alpha 127, the S's preview differs
in 1,473 pixels. The README claims pixel equality only for the five earlier
previews, so this ambiguity does not falsify any sentence.

confirms: none
`placeholder-s.png` is the S's stamp, and its alt text describes it. Read: I
opened the image. It shows the red 28-cell disc with the S, a bold red
`SEALED` and a grey rule, and the dim labels and grey values of the v0.22.1
sample panel. The `gate` row has a green check mark, U+2713. Executed: the
PNG's chunks are `IHDR`, `IDAT` and `IEND` only, so no text chunk carries a
path or a host. "Georgia Bold's S" is the frame's own wording: read,
`seal/specs/1791270164-the-release-seal-is-drawn-in-curves/spec.md:40`.

confirms: none
The smith claimed that the sentence it dropped from §*The next entry* was
false. That holds. Read: `tests/test_release_hygiene.py:45-55` is `LOADED`
(`skills`, `agents`, `docs`, `templates` and five root files), and
`test_no_loaded_file_names_a_version_at_or_above_the_running_one` at line
588 sweeps only `tracked(*LOADED)` (line 579). Nothing in that check reads
`assets/`, so an entry written before its tag would not be refused, which is
the opposite of what the dropped sentence said.

confirms: none
Nothing else in the tree still says the S has no entry. Executed: `git grep
-i` for `no entry`, `placeholder S`, `placeholder-s`, `assets/seals` and
`red lily` outside the README and this work item's directory finds only
released changelogs, records of other work items, and unrelated uses of "no
entry". Executed: `bin/test tests/test_one_word_one_meaning.py -q -p
no:xdist` in the clone passed 26 tests, exit 0. That module sweeps
`assets/seals/README.md` (`tests/test_one_word_one_meaning.py:244`) for a
sentence that gives the stamp to the broad gate, and the rewritten opening
paragraph passes it.

confirms: none
The smith's `## Not done` says this change owes no changelog fragment. That
holds. Read: `docs/the-record-layout.md` §*A change writes fragments, never
a shared file* says where an entry goes and does not require one for every
change. `tests/test_the_release_check_watches_what_ships.py:47-58` lists
`assets` in `STAYS_HOME`, as work that never reaches a plugin user. No code
reads `assets/seals/` (`git grep` over `tests` and `.github` finds two
mentions, a sweep list and that set).

## Not judged

| What | Location | Who answers |
|---|---|---|
| How `placeholder-s.ans` looks when printed with `cat` in a truecolour terminal. Its bytes were shown equal to v0.22.1's own `stamp` output, but no terminal drew it in this round | `assets/seals/placeholder-s.ans` | the owner, through the orchestrator |
| Whether the preview's three new styles (dim at half opacity, Menlo Bold, xterm's green) read like a real terminal's | `assets/seals/README.md:22-24` | the owner, through the orchestrator |
| The full suite, the repository-wide lint and the typecheck: unverified, not run in this round under contract §2 | the branch at `abc49184` | the orchestrator, through `broad-gate` |

## Probes

| Command | Result |
|---|---|
| The README's draw-again command at `assets/seals/README.md:91`, verbatim, from `assets/seals/` of the clone | exit 0; 5,498 bytes; `git status --porcelain` empty; `cmp` with the main checkout's file exit 0 |
| `git rev-parse <tag>:skills/verify/scripts/seal-mark.txt` for v0.19.0 through v0.22.1 | absent at v0.19.0; `80593dfc` at all five later tags |
| `python3 -I test_tmp_disc.py <clone>` (scratch, deleted): each tag's `stamp(SAMPLE_ROWS)`, first 28 cells compared with v0.22.1; `SAMPLE_ROWS` and `stamp`'s signature printed; the module loaded without `__file__` | discs equal except trailing blank padding; `ledger` row through v0.21.1, gone at v0.22.0, short panel at v0.22.1; no `scale` from v0.21.0; `NameError` on `__file__` at v0.20.0 and v0.22.1 |
| `uv run --with pillow==12.3.0 python -I 978/ans_png.py <ans> <out> --size 19 --dim-alpha 128 --compare <png>` over the six committed `.ans` | 0 differing pixels for all six; for the S at alpha 127, 1,473; at 255, 2,181 |
| A scan of the SGR codes in each `.ans` and of each `.png`'s chunks | `1`, `2`, `22`, `32` only in `placeholder-s.ans`; `38;5` and `48;5` in `red-lily.ans` and `section-14-light-red.ans`; every PNG holds `IHDR`, `IDAT` and `IEND` only |
| `bin/test tests/test_one_word_one_meaning.py -q -p no:xdist` in the clone | 26 passed, exit 0 |
