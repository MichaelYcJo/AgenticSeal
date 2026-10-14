# 1791876665-each-budget-ratchets-and-every-pull-request-measures-it — phase 4

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | e6a31b4e |
| Ran by | smith on Opus 5.5, as `routing.md`'s models line gives it |

## What this phase was asked

First fix the two defects pull request #938's run 38485697284 found, each in a
commit of its own with a case seen red:

1. `tests/test_every_reader_ends_a_line_where_gfm_does.py::test_every_splitlines_call_left_is_named_with_its_reason`
   failed on ubuntu, macOS group 2 and Windows group 1, naming
   `budget_check.py`'s `classify`, `declarations` and `main`: a reader of
   document lines reads `unverified_check.py#gfm_lines`, and anything else
   is named with its reason in `OUT_OF_CLASS`. Run that module and the other
   census modules the checker touches, which phase 3's slice had missed.
2. Windows group 2 measured the fixture at 1,008 bytes against 1,000: a byte
   budget reading the working tree counted CRLF. Choose a measure that is
   the same on every platform, state it in the checker and in
   `seal/budgets.md`, add a case that fails if CRLF is counted, and check
   whether the fixtures write platform newlines.

Then phase 4 as `plan.md` states it: `rounds-bytes` per open work item,
`ledger-rereads` on base `main`, `--trend <tag>`, `docs/release-checklist.md`
§2's one-line-per-budget step, the changelog fragment and the ledger
fragment. Keep the checker open for the families #923 and #929 add, and build
none of them.

## What this phase found

**Fix 1 — the lines a document has are GitHub's** (c5605ab2). `classify` and
`declarations` read `gfm_lines`, and `main`'s docstring line is named in
`OUT_OF_CLASS`. `classify` hands those lines to `hooks/config.py#unfenced`
without the text, because the walk answers for `str.splitlines` pieces when it
is given the text, and for the lines as handed when it is not. Two cases pin
it: a U+2028 inside a line keeps a later history line at its GitHub number,
and a `Budget raised:` after a U+2028 opens no line GitHub shows. Seen red
under `mutation-check` with each reader put back on `splitlines`: the census
case and the new parameter, together, both times.

**Fix 2 — a byte is what git stores** (96e94481). Each file a
byte row reads is counted with every CRLF read as one LF, the bytes git keeps
under this repository's `* text=auto eol=lf`; the checker's docstring and
`seal/budgets.md`'s comment say so. The fixtures themselves wrote in text
mode, which is CRLF on Windows, and that is what produced 1,008: they now
write LF on every platform. The new case converts a checkout to CRLF and
measures 1,000 and 300; seen red with CRLF counted. The real tree's rows were
not wrong on Windows, because `eol=lf` checks the files out with LF; the
fixture was, and so would a clone whose attributes are overridden.

Commits: c5605ab2 (fix 1), 96e94481 (fix 2).

**Phase 4, against the frame.**

- `rounds-bytes` reads every `seal/specs/<id>/rounds/` the tree holds. The
  0.21.1 items' records are still there, so the reading is the frame's own
  example, 142,823 bytes for `1791852616`, and seven more are listed below
  it. The row is a `report`, so it fails nothing; a `report` row may be
  `one-sided` now, as a per-run row may.
- `ledger-rereads` reads `seal/releases/<version>.md` for
  `.claude-plugin/plugin.json`'s version, unread until that file exists. On
  this branch the manifest still names 0.21.1: 203 `Re-read ·` and 27
  `Corrected ·` of 280 rows, each row counted once by the marker it opens
  with. That answers `questions.md` Q4 as #908 did. The first build read
  rows through `hooks/config.py#table_cells`, which declines the one 0.21.1
  row whose cells carry an even run of backslashes before a pipe, and it
  counted 26; the row is a line opening with `| `, which is how the fold
  writes it, and the count is now by that opening.
- `--trend <tag>` sets each budget's ceiling at the tag beside its ceiling
  and reading today, from the tag's `seal/budgets.md` blob, with no checkout
  of the tag. Against v0.21.1 every row reads `new since then`. The hygiene
  step passes `git describe --tags --abbrev=0` of the base; locally that is
  v0.21.1 for `origin/release/v0.22.0`. An empty name is exit 2.
- `docs/release-checklist.md` §2 opens with the step: read the trend line,
  and lower a `one-sided` ceiling in the preparation commit to 1.3 times the
  largest of the release's runs. It sits before §2's first fold marker,
  because a paragraph after a folded statement is read by `fold-check` as
  part of it, and it carries no `Enforced by:` line, because it is no fold.
  It adds no history line: `docs-history:docs/release-checklist.md` still
  reads 11.
- The ledger fragment gains thirteen rows, B1 to B13, one per clause of the
  checker, each anchored to its units and its cases, stamped by
  `evidence-check --reverify --into`; four released rows the two fixes
  drifted are re-read there too. `evidence-check --strict` exits 0.
- The changelog fragment says what a contributor and a release meet.
- The checker's families are a dictionary, `MEASURERS`, and per-file
  families a second, `FILE_TABLES`; #923's and #929's rows are one entry
  each, and nothing of theirs is built here.

**Every case seen red** (`executed`, `bin/mutation-check`, all `red`): the
two fixes' three mutations above, and phase 4's thirteen — rounds summed
rather than maximised, listed by name, a work item with no `rounds/` listed,
a report failing the run, `Corrected ·` counted before `Re-read ·`, rows read
through the cell reader, an unfolded release read as 0, a trend with no `new`
and no `gone`, an empty tag read, a manifest with no version read, a report
row refused `one-sided`, and the hygiene step without `--trend`. The rounds
case first survived two of them, a list in name order and an empty
`rounds/` listed, because its fixture sorted the same either way and its
assertion did not look for the absent item; both are pinned now (60e49c5d).

**Owed at the push.** The two fixes on CI's legs, and `--trend` naming the
base's tag in the runner's checkout.
