# Implementation Plan: the config table is read by the walker cmark-gfm holds (#871)

Approved 2026-10-13 by the orchestrating session, under the owner's `automation` answer, when `smith` was spawned.

## Summary

`hooks/config.py` holds two table readers: `config_rows`, an owned grammar
of three regexes and a stop rule argued over #82, #415, #429, #430 and #667
and held by hand cases; and `gfm_table`, held to cmark-gfm over an
enumerated corpus. The first reads `seal/config.md`, the file every gate's
answer depends on. Measured (`spec.md` §*Data & interfaces*), it hands a
gate rows GitHub does not render in five shapes and silently drops rows
GitHub renders in four. This work moves the config table onto the walker,
keeps every exported name a caller spells, and answers the issue's two open
decisions:

1. **The migration for installed configs the walker refuses is the
   refusal's own remedy, printed by the first command that reads the
   file.** No installed file is rewritten. Three shapes GitHub renders are
   refused — a non-blank line directly above the header (rows 1, 2, 11 of
   the measurement) — and the sentence the walker already prints for them
   is *leave a blank line above the header*. The plugin's own writer
   (`seal.py#NEW_CONFIG`) and `templates/config.md` both put that blank
   line there, so a config the plugin wrote is never refused; only a
   hand-written one can be, and it is refused once, naming the line.
2. **The prompt budget of a refusal that reaches a hook is zero.** The two
   hooks that read the file treat a refused table as #867 taught them to
   treat an unreadable one: the mode gate's `undeclared` already reads
   `"refused"` as *answered* and stays silent, and the evidence advisor
   keeps naming the frozen repair. No hook denies, asks or prints on a
   refusal. A person meets it at a command — `broad-gate`, `seal mode`,
   `evidence-check`, `correction-check`, `fold-check`, `pact-check` — which
   exits 2 with the sentence and nothing run, the shape those commands
   already take for a doubled row.

## Technical context

**The two readers, and what each caller reads.** `hooks/config.py#indexed_config_rows`
(line 349) is the walk; `config_rows` (310) is its projection; `refusal`
(~372) is the third walk, reading on past the stopping line for the sealer;
`seal.py#table_span` (1430) is the writer's fourth, over the same three
regexes re-exported at 1375–1377. `gfm_table` (1293) reads the three pact
tables through `read_table` (1452) and `pact_changes`/`pact_reviews`, with
`table_end`, `raw_html_open`, `a_list_above`, `table_cells` and the regexes
at 1180–1292. Both walks already read through `unfenced` (239), so the
fence and comment rule (#429, #667) is shared and does not move.

Callers of the config reader, from the inventory (`seal/specs/1791382684-…/inventory/`
rows 2-95, 4-E46, 4-C17, 4-F11, 4-X16, 4-X18, 5-11, 7-25):
`hooks/mode-gate.py#undeclared` (163) via `declared_mode`;
`hooks/evidence-advisor.py` (228) via the checker's `frozen_from`;
`broad_gate.py#broad_command` (822), `#refusal` (852), `#rows_read` (866),
`#missing_row` (1051) and the fenced/commented arms (937–1020);
`fold_check.py#config_rows` (525); `correction_check.py#cutoff_at` (1038);
`evidence_check.py#config_rule` (4370) and `vendored_config_rows` (4295);
`seal.py#table_span`, `with_row` (1492), `write_row` (1578);
`pact_declaration` (969) through `indexed_config_rows`;
`tests/test_the_pull_request_language_is_the_repositorys.py#items` (347).

**What the walker gives for free.** `gfm_table` returns `(line number,
cells)` per row, so the writer's and the pact reader's need for line
positions is met without a second walk; its refusals are sentences written
to read after a noun naming the file, which is how `broad-gate` and the
pact readers already print them. Its header match is `table_cells(line) ==
header`, so `("Item", "Value")` is the whole of what the config table has
to hand it.

**What the walker refuses that today's reader takes**, measured in
`spec.md` §*Data & interfaces*: a non-blank line directly above the header;
no delimiter row, or one of another width; a line between the delimiter
and the first row that is not a two-cell row; a line in the table that is
not a two-cell row (a bare pipe, a third cell, a stray delimiter, prose);
and every row written below a gap `unfenced` leaves, which is #667's
*row parked in a comment inside the table* with live rows under it
(`tests/block_shapes.py` C5/C7). Each of those is a shape GitHub renders
differently from how the gates read it today, and the last is a shape #667
pinned on purpose — the pin moves to *the rows below are refused*, because
GitHub does not render them (row 5 of the measurement).

**Failure scenario of the chosen approach, six months out.** A repository
whose hand-written config has `-->` directly above the header upgrades and
hears nothing until its next release run, where the sealer stops with
*leave a blank line above the header*. One run stops once, with the line
and the edit printed. The cheaper alternative — reading that shape because
the measurement says GitHub renders it — is a second grammar inside the
walker for one header, and #749's two rounds are where that reading was
measured wrong on shapes nobody had written. What this plan cannot see:
a config shape the corpus does not enumerate that GitHub renders and the
walker refuses; the oracle pass over the config header is what names it,
and the direction is a refusal with its line, never a silent default.

**Direction, stated once for every phase.** Refuse more, in commands only;
hooks say nothing. Prompt budget: zero in every phase. Platform: pure
Python, standard library in the hooks and the scripts; `cmarkgfm` stays
test-only.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| Keep two readers and hold `config_rows` to the oracle as well | It cannot be held: rows 3, 4, 5, 13 and 16 are rows it reads and cmark-gfm does not render, and rows 6, 8, 14 are rows cmark-gfm renders and it drops. The property S1 of #647 — cells equal the renderer's or the walk refuses — is false of it by construction, and a second oracle case written to the stop rule would be a check that passes the defect | rejected, measured |
| Move onto the walker and have `seal mode` rewrite an installed config into the walker's shape (insert the blank line, move the comment out) | A rewrite of a person's file on a guess about block state the walker itself declines to make; `with_row`'s history (#429 round 2, a row concatenated onto an unterminated last line) is of rewrites landing wrong, and the gate that would send a person to `seal mode` is silent on a refusal, so nobody is sent | rejected |
| Move onto the walker, but read a header with a non-blank line directly above it where the measurement shows cmark-gfm renders the table (rows 1, 2, 11) | A second grammar inside the walker for one header. The walker refuses the shape because whether GFM renders a table there depends on block state no reader here tracks — a lazy paragraph under a list item, a setext underline, an HTML block of kinds 6–7 — and PR #749 rounds 1 and 2 measured the first walker reading tables GFM does not render on exactly those shapes | rejected |
| Refuse the whole table on any refusal: every item `(None, sentence)` | More silence in the hooks than the file warrants: a `Mode` row the walk read above a bad line turns the mode gate off, and a `Fold shape from` row it read stops `fold-check`, for a line that is not theirs. Per-item is what #867 chose for a doubled row, and a row the walk read is a row GitHub shows | rejected; per item chosen (S2) |
| The mode gate prints a line on a refused table, at zero prompt budget, so a person hears before the sealer | A `PreToolUse` hook that prints is a change to what a person sees on every Bash call in that repository until the file is edited; #867 drew the line at silence for hooks, and a line printed from a hook is a decision for an owner, not a frame | rejected here; `questions.md` records it decided and names the owner as the one who can reopen it |
| The vendored twin carries the whole walker (`hooks/blocks.py`, `HTML_KINDS`, `raw_html_open`, `a_list_above`) | The vendored checker reads a CI checkout's config, where the table is the file's own (#867 round 1, ⬜ 7); carrying the block grammar there is a copy of 400 lines held equal by a case that already exists for the plugin's own walker. The twin follows the table grammar on lines it can judge alone and refuses where it lacks block state, which is the stated direction and the cheaper mistake in CI | rejected; S7 chosen |
| Keep `refusal`'s `(refused, below, stopper)` contract over the walker | The triple exists to answer which side of the stopping line a row is on, for a reader that steps past lines above the first row and reads on below the stopper. The walker does neither, so two of the three values are constant, and `missing_row`'s five arms collapse to one sentence plus #430's condition | rejected; `refusal` leaves (`## Removes`) |

## Phases

Vertical slices — each phase ends with something runnable and verified. A
case is planted only after it has been seen red (`agent-contract` §15), and
each phase that changes a gate's or a hook's answer states the direction and
the prompt budget in its phase record (`CONTRIBUTING.md` §*What a change to
a gate must carry*); the direction is *refuse more, in commands only* and
the budget is zero in every phase. Every unit a phase touches gains a
`Reads:` line and leaves `tests/undeclared_readers.txt` in that phase.

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The one walk: `hooks/config.py#config_table` over `gfm_table(text, CONFIG_TABLE)`; `indexed_config_rows` and `config_rows` as its projections; `config_value`, `declared_value`, `declared_mode` answering per item (S2); `pact_declaration` and `pact_lines_not_read` reading the walker's rows and appending its refusals; `refusal`, `CONFIG_ROW` and `CONFIG_HEADER` removed, `CONFIG_SEPARATOR` and `CELL` kept with a comment naming `path_map`; the oracle case's fourth header pass; `hooks/mode-gate.py` and `hooks/evidence-advisor.py` pinned silent over shapes 1, 5, 7 (S3). The docstrings of `config_rows` and `unfenced` rewritten for the walk they now describe. Direction: hooks say nothing; prompt budget zero | S1, S2, S3; red first in `tests/test_the_mode_question_is_asked_once.py` (shapes 3, 5, 6, 7, 13 against the stop rule), `tests/test_a_signer_declares_its_pact.py` (a signer config the walker refuses), `tests/test_one_table_walker_reads_what_gfm_renders.py` (the config pass); `tests/test_the_hooks_hide_what_a_renderer_hides.py` unchanged and green · NAME NOT IN TREE | bd27b1a6 |
| 2 | The writer: `seal.py#table_span` removed; `with_row` and `doubled_modes` over `config_table`'s row indices, the insertion point from the walk's own header and delimiter positions; a refused table is `(None, sentence)` and `write_row` prints *Nothing was written*; `seal mode --check` exits 2 on it; `NEW_CONFIG` unchanged. Direction: refuse more, command only; budget zero | S5; red first: `test_the_writer_and_the_reader_agree_about_which_row_is_the_row` extended with shape 7, `test_seal_mode_still_writes_a_second_mode_row_for_a_bare_pipe` removed and its inverse planted; `test_the_writer_reads_where_commonmark_breaks` and `test_the_writer_leaves_a_commented_row_alone` green | ecb4f8fd |
| 3 | The commands: `broad_gate.py#broad_command` through `config_value`; `missing_row` reduced to the walker's sentence with the `\|` remedy and #430's condition, `refusal`, `rows_read`, `hides_this_row` removed, the fenced and commented arms and the absent-row refusal unchanged; `fold_check.py#config_rows` raising `Unusable` on a refusal of a row it reads; `correction_check.py#cutoff_at` and `evidence_check.py#cutoff_row` through `config_value`; `config_rule` returning the pair with the twin — `vendored_config_rows` returning `(rows, refusals)` on the walker's table grammar, its docstring stating the direction — and `CONFIG_SHAPES` extended with shapes 1, 3, 4, 5, 6, 7, 8, 13, 14, 16; `pact_check.py` reading the refusals `declared_pacts` now carries. `templates/config.md` head and §*Broad gate*, `skills/config/SKILL.md`'s `\|` bullet rewritten to the refused shapes and their edits (S8). Direction: refuse more, commands only; budget zero | S4, S6, S7, S8; red first: one case per command on shape 7; the sealer's refusal cases re-pinned, the seven named in `## Removes` removed; `test_the_vendored_config_rule_agrees_with_the_shared_one` over the extended table; `tests/test_the_pull_request_language_is_the_repositorys.py`'s three table cases replaced; S8's document case | 8b4fbb10 |
| 4 | The record: `changelog.md` naming what an installed config sees change, shape by shape with its edit; `overview.md`; the ledger fragment with rows for the new units and `evidence-check --reverify --into seal/ledger/1791852616-….md --checked <date>` for every released row the stop rule's removal moves — the candidates are listed in `questions.md` Q4 — with a `Corrected ·` row where the claim no longer holds (0.5.0's 🟡 6 / 🟡 5, 0.12.0's three rows on the stop rule, 0.12.1's R2, 0.21.0's K8) and a `Re-read ·` row where it does; `tests/undeclared_readers.txt` with every touched unit gone; `tests/test_a_record_states_what_the_tree_has.py` green over this directory | S9: `evidence-check --strict .`, `correction-check --range`, the records case, exit codes read directly; the broad gate is the sealer's | 0db85117 |

This table is also where the work records how far it got. There is no separate
task list: a list of tasks is mutable progress, and a stale one asserts a state
that is not true, which is the failure the evidence ledger exists to prevent.

**Status is empty, or the commit that closed the phase.** A tick is refused,
and so is `done`: both can be typed without anything having happened, and both
assert a present state that nobody can check. A commit hash asserts a past one
— someone can open it — which is the same trick that lets a round record live
beside the contract rather than in tool state.

Fill it in as each phase closes, not at the end. A phase reconstructed
afterwards is reconstructed from the diff, which is where it already was.

What a phase discovers while it is being built, and needs the next phase to
know, does not fit in this table's cells. Write it to
`seal/specs/<work-item-id>/phases/phase-N.md`, from `templates/sdd-phase.md`,
when the phase closes.

One caveat, so nobody builds on it, and it has two halves. Where feature
branches squash, these commits stop resolving at the merge — and **a rebase
during the work does the same thing earlier and far more quietly**, because the
orphaned object still answers `git cat-file` in the worktree that wrote it.
The quiet half is the one that bites: this column was wrong on its own first
use, nine SHAs deep, and only a reviewer opening them found it. **Re-read the
column after any rebase**, or it names commits that resolve in one clone and
nowhere else. That is tolerable because nothing measures from this column.
The evidence ledger had the same problem and no such tolerance. It no longer
has it at all: a ledger row names a symbol and a content hash, so there is no
commit in it for a rebase to orphan.

## Operational impact

- **What an installed repository sees change.** A `seal/config.md` of any
  of the refused shapes in `spec.md` §*Data & interfaces* is refused by the
  first command that reads a row the walk did not read — `broad-gate` (the
  sealer stops with nothing run), `seal mode` (nothing written),
  `evidence-check --reverify`, `correction-check`, `fold-check`,
  `pact-check` — at exit 2, with the line quoted and the one-line edit
  named. Hooks say nothing, as they do for an unreadable file. A config
  `seal mode` wrote, or one copied from `templates/config.md`, has none of
  those shapes. The `Broad gate` row GitHub shows is now the one the gate
  runs: a bare-piped row is refused, never truncated.
- **The vendored checker.** `tools/evidence_check.py` picks up the twin at
  the next `/specseal:evidence-ci`, as every change to the checker does;
  until then a repository's CI reads the config with the stop rule and its
  local `--reverify` with the walker, which can differ only in the refuse
  direction.
- **No new dependency.** `cmarkgfm` stays test-only at its pin.
- **One issue to file** (the session's act, not the build's; into
  `release: 0.21.1`'s successor as the owner decides): *fix:
  `pact_check.py#path_map` reads `~/.claude/specseal/pact-paths.md` with the
  config table's retired grammar* — it is the last caller of
  `hooks/config.py#CONFIG_SEPARATOR` and `CELL` as a table grammar, reading
  a `| Remote | Path |` map by the stop rule this work removed from the
  config table; the first non-row line ends the map silently (inventory
  row 4-P4). What to decide: whether the map is read through `gfm_table`
  with its own header, which is one line, and what a refusal of a
  machine-local file should print. Grounds: this frame; #834 part 4 row P4.
