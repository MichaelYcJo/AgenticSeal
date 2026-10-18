# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 2

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 0dd09a37 |


## What this phase was asked

The stamp is queued at the guarantee's commit. `chain_check.py` gains
`earlier_verdicts(cell)`. `seal_stamp.queue_for_guarantee(top, common,
session)` writes one values file named `<ns>-<id>-<target sha>.json`, checks
for a twin under every session's directory, composes S9's rows, and returns
S4's line. `commitgate.post_commit` calls it after the notice, through a
loader shaped like `_notice_module`, silent on every failure and exit 0.
`hooks/git/post-commit.py` stays byte for byte; no `scale` key is written.
Q2's latency is measured and written here. The orchestrator answered Q1
with (a): the stamp's rows are what the records at HEAD say, and no suite
counts.

## What this phase found

**The frame holds, with one gap it did not name: local mode draws no
stamp.** A local-mode `seal/` root sits under the git directory and no
commit carries `guarantee.md`, so `post-commit` never sees one. The writer
matches `seal/specs/<id>/guarantee.md` in the commit's paths, which is the
shared-mode layout alone. The failure direction is the frame's own: a
missing stamp, never a false one. Phase 3's §*The stamp* names it beside
the foreign hooks slot.

**Q2, measured (`executed`).** A probe built one fixture clone per plugin
copy with the stubs installed and a declaration in force, then timed 12
`git commit` calls of each kind and dropped the first. Medians of the other
11, in milliseconds:

| Commit | Without the duty (`ddb5cf1a`) | With it (this tree) |
|---|---|---|
| An ordinary change | 333 | 343 |
| One adding a `sealed` guarantee | 336 | 375 |

An ordinary judged commit pays about 10 ms, which is loading
`seal_stamp.py` and one `git diff-tree`. A guarantee's commit pays about 39
ms more, which is `chain_check.py`'s import, three `git show`/`ls-tree`
calls and the write. Both are under the 50 ms the question set as the bar
for reading less before deciding, so the writer was left as it is. The
probe file and its copies were deleted.

**Where a case went beyond the plan's row.**

- `earlier_verdicts`' cases went to `tests/test_the_sealer_guarantees.py`
  as `TestEarlierVerdicts`, beside `TestVerdictsOf`, rather than to
  `tests/test_chain_check.py`. That module holds the readers of
  `guarantee.md`, which is the group the rule *a new test starts from its
  group* sends a case to.
- The end-to-end case through the real stub is in
  `tests/test_the_commit_gate_decides_at_the_commit.py`, beside the
  notice's: `test_a_sealed_guarantees_commit_names_its_stamp_in_the_commits_output`.
- S9's rows carry a blank between the identity rows and `gate`, the shape
  the owner's 2026-10-07 layout gives every panel. S9 lists the rows
  without it.
- `SAMPLE_ROWS`, which `seal-stamp` draws with no arguments, is now the
  guarantee's rows in neutral values. The case that held it against
  `panel` holds it against `guarantee_rows` and is renamed
  `test_the_sample_carries_every_row_the_stamp_can`. The twin's character
  case reads the sample as it stood at `5623d728`, which still carries all
  four of the owner's characters.
- `seal_stamp.quote` is a second spelling of `broad_gate.quote`'s two
  lines. Its docstring points at the gate's for the reasoning; the gate
  quotes a row for `cmd.exe` and the stamp a path for a person's shell, so
  neither was folded into the other.

**How each case was seen red.** S4, S6, S8 and S9 failed at `ddb5cf1a`
before the writer existed; S5 and S7 assert an absence and passed there,
so they were shown red by `mutation-check`: dropping the verdict test turns
S5 red, and dropping the earlier-run test turns S7 red. Every unit the
writer added went red under one mutation each — the verdict, the earlier
run, the twin check, its `.drawn.json` half, the round count, the gate
row, the base, the file's key, the quoting and `post_commit`'s call. The
quoting survived its first mutation, because no case ran under a path with
a space; the S4 case now does (`0dd09a37`).

**For phase 3.** The line `post-commit` prints is `seal_stamp.QUEUED`, and
the four silences S10 names are the hook's. `hooks/sealer-stamp.py`'s
docstring and `seal_stamp.py`'s module docstring still describe the gate's
values file; they are phase 3's rewrite.
