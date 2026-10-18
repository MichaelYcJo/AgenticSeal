# 1792311781-the-stamp-is-drawn-from-the-sealers-verdict — phase 1

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | fe201329 |


## What this phase was asked

The gate stops sealing. `broad_gate.py` gains `GATE_PASSED` and
`GATE_FAILED` (`BROAD GATE PASSED` / `BROAD GATE FAILED`) beside the
preflight's heads. The values-file write, the terminal drawing and the
terminal/pipe fork go, with `SESSION_VAR`, `SCALE_FOR_OLDER_HOOKS`,
`common_dir` and the four outcome strings. A passing run prints one form:
the head, `panel`'s rows as plain text with no title row, and the
uncommitted line. `not_sealed` moves into the gate as the failure form.
`PANEL_VALUE_WIDTH`, `ELISION`, `fit`, `wrapped`, `SEP`/`ARROW`/`TICK`/`DOT`
and `item_value` move to `seal_stamp.py` and are read back through
`stamp_module()`. The module docstring and `bin/broad-gate`'s header follow.
`tests/test_one_word_one_meaning.py::test_the_gate_never_says_sealed` is
written first and seen red. Phases 4 and 5 are not this spawn's.

## What this phase found

**The frame holds, with three corrections.**

- S3 says the report is "the same bytes on a terminal and a pipe, the
  letter twin's ASCII marks on a console that is not UTF-8", and `plan.md`'s
  row says "the twin's ASCII where `pick_shape` says so". The two disagree on
  a UTF-8 pipe: `pick_shape` answers True for every pipe. The spec's reading
  was built. The ASCII choice asks only the encoding, through a new
  `seal_stamp.is_utf8`, which `pick_shape` now calls too. `--shape` still
  forces ASCII, so the fixture runs that pass it read `+ 1 passed`.
- `bin/broad-gate`'s header names no stamp and no `SEALED`; it needed no
  change.
- `docs/the-broad-gate.md` is in S1's list of files that never say
  `SEALED`, and its rewrite is phase 3's. The case holds the gate's three
  files now; phase 3 adds the document to `GATE_SWEPT` when it removes
  §*Where the stamp is drawn*.

**Two things went wider than the frame named.** Both are the same class
the frame names (§12): the gate's own output calling its run a seal.

- The coverage line on stderr said `this seal answers`; it says
  `this run answers`, and `this seal` joined the case's phrases. The pins
  in `tests/test_the_gate_names_every_step_ci_runs.py` and the preflight
  case moved with it.
- `PREFLIGHT_TAIL` said `nothing is sealed`; it says `nothing is written`.

**Left as they stand, and named for whoever reads the next phase.** The
gate's refusal sentences still say `seal` in a few places: "no command to
seal over", "has no HEAD to seal", "a seal taken over a command nobody
chose". They refuse a run, they are not a pass line, and none matches S1's
phrases. Whether they should name the sealer's seal or say `run` is not
decided here.

**`main`'s encoding fallback had nothing behind it.** A mutation of
`if console_wants_ascii is None: … = not stamp.is_utf8(sys.stdout)`
survived, because `__main__` always names the value. The fallback was
removed (`fe201329`); `main` defaults to the owner's marks for a caller in
process, and `__main__` is the one place the stream is read.

**For phase 2.** `seal_stamp.py` now holds every rule the writer needs to
compose rows: `fit`, `wrapped`, `item_value`, the marks, and `TITLE_ROW`.
`SAMPLE_ROWS` still describes the old panel under the title; the case
`test_the_sample_carries_every_row_the_panel_can` compares the sample past
its title row with `panel`'s labels, and phase 2 has to decide what the
sample shows once the stamp's rows are the writer's (S9).

**How each rewritten case was seen red.** The new sweep was run against
`761722fa` and failed on `SEALED` in the module docstring. The rewritten
gate cases were copied over an archive of `761722fa` and run there: every
one failed, and the cases on the shared `a_recorded_run` fixture errored at
its setup, because the old gate prints no `BROAD GATE PASSED` line. The
case added after the build, `test_the_marks_go_out_in_ascii_where_utf8_cannot`
and its two parameters, was shown red by `mutation-check` on the ASCII
mapping and on `__main__`'s encoding read.
