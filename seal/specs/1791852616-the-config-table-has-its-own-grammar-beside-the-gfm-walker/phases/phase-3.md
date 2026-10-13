# 1791852616-the-config-table-has-its-own-grammar-beside-the-gfm-walker — phase 3

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 8b4fbb10 |
| Ran by | unknown — the spawn prompt named neither the agent's model nor asked this row to be filled; the orchestrator fills it |

## What this phase was asked

The commands: `broad_gate.py#broad_command` through `config_value`;
`missing_row` reduced to the walker's sentence with the `\|` remedy and
#430's condition, `refusal`, `rows_read`, `hides_this_row` removed, the
fenced and commented arms and the absent-row refusal unchanged;
`fold_check.py#config_rows` raising `Unusable` on a refusal of a row it
reads; `correction_check.py#cutoff_at` and `evidence_check.py#cutoff_row`
through `config_value`; `config_rule` returning the pair with the twin —
`vendored_config_rows` returning `(rows, refusals)` on the walker's table
grammar, its docstring stating the direction — and `CONFIG_SHAPES` extended
with shapes 1, 3, 4, 5, 6, 7, 8, 13, 14, 16; `pact_check.py` reading the
refusals `declared_pacts` now carries. `templates/config.md` head and
§*Broad gate*, `skills/config/SKILL.md`'s `\|` bullet rewritten to the
refused shapes and their edits (S8). Red first: one case per command on
shape 7; the sealer's refusal cases re-pinned, the seven `## Removes` names
removed; the vendored agreement case over the extended table; the
pull-request-language module's three table cases replaced; S8's document
case. The spawn added the seam with #872: keep any edit to
`evidence_check.py`'s `quoted_lines`, `claim_lines`, `anchored_rows`,
`live_lines`, `hidden_lines` or `readable` minimal and say so.

**Direction:** refuse more, in commands only. **Prompt budget:** zero.

## What this phase found

**`missing_row`'s first arm reads the walker's own sentence rather than a
second walk.** The stopping line is the backticked line in the sentence,
found again as the first line under the delimiter row that reads as it
(`stopping_line`); what is below it is any `| … |` line before the next
heading (`rows_written_below`). The walker's sentence is printed unchanged
except for one cut — its closing clause about rows below, where none is
written below (#430) — so the sentence stays the walker's for all four
tables, as `spec.md` §*Data & interfaces* asks. `broad_command` returns None
for a walker refusal so that `missing_row`, which owns the escape and the
condition, speaks; a doubled row still raises there.

**`refused_broad_row` keeps its name and changes its question**: the
`Broad gate` line the walker did not read, in a table it refused. Neither
`## Removes` nor the plan named it, and the sealer's cases call it.

**The twin refuses where it lacks block state, by line.** It has no fence
or comment state, so a fence or HTML opener above the header is refused (a
fenced example table there is not the table to the plugin), and inside the
table every line other than a two-cell row, a blank line or a heading is
refused in the walker's sentence for its shape. Shape 5 holds a comment, so
it sits in the direction case with three others, not in the equality table
(`overview.md`).

**Documents beyond the plan's two.** `skills/implement/orchestration.md`'s
bootstrap warning carried the stop rule's cost too; it was found in phase 4
and is recorded there. Three pins on the documents' wording were re-pinned
here: `test_the_allowed_list_says_how_a_pipe_is_written`,
`test_the_module_header_names_every_refusal_and_none_names_a_command`, and
`test_the_skill_says_how_a_value_carrying_a_pipe_is_written`.
`test_no_passage_is_pasted_into_a_second_file` refused the first wording of
the skill's list as a copy of the template's, so the skill says it in its
own words and points at the template. `test_a_format_has_one_reader` gained
one heading exemption, for the twin's `VENDORED_ATX_HEADING`, held equal to
the walker's.

**Seen red**, every new and re-pinned case, from archives (HEAD never
moved): against 62e2b443 (phase 2's code) 49 of 54 red; the other five —
the pact-check case and the three pull-request-language cases, already
answered by phase 1's reader, and this repository's own-config pin — red
against 3bb2ea42.

Verified by `bin/test` over the eighteen modules phase 3 touched or whose
pins it moved (the sealer, `test_evidence_check.py`, `test_pact_check.py`,
the correction, re-read and fold modules, the document pins, the format and
passage guards, the line-ending census, the reader registry, and phase 1–2's
modules) at d427badd: exit 0, 5,512 passed.

**Mutations:** twenty-four through `mutation-check`. Of nine in
`broad_gate.py`, five survived the first case selection; one was caught once
the gate-level case was in the selection, and four took
`test_the_refusal_reads_each_of_its_conditions_off_the_file` (a heading
below the stopping line, no escape without a bare pipe, the stopping line
under the delimiter, an empty row read as absent). Of fifteen in
`fold_check.py`, `correction_check.py` and the twin, the twin's list-item
check survived until its shape was planted; every one is now red (8b4fbb10).

**Direction:** refuse more, commands only. **Prompt budget:** zero.
