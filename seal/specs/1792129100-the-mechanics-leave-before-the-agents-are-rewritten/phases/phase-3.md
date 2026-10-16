# 1792129100-the-mechanics-leave-before-the-agents-are-rewritten — phase 3

<!-- seal/specs/<unix-epoch-seconds>-<slug>/phases/phase-<N>.md — what this phase
of the build did, written by the implementer when the phase closes. It is the
build side's counterpart of `rounds/round-N.md`. -->

| Field | Value |
|---|---|
| Phase | 3 |
| Commit | 3a5351cf |


## What this phase was asked

The round record's grammar as one table in `docs/the-review-record.md`
§*The round record*, which `chain_check.py` loads and against which it
accepts a labelled line or heading only where it matches a row whole; a
table it cannot read exits 2 naming the file. The constants that restate it
in the script go; `templates/sdd-round.md`'s comment and `templates/config.md`
point at the table and restate nothing; the shapes that leaked in #923 stay
as fixed example cases; no generated-variant test (#929). The plan's row,
Verified-by column and test rows T2 and T3, with the tree winning where it
disagrees.

Handed over: the constants at `SEVERITY` (`:98`) through `DEFERRED_VALUE`
(`:184`) of a 1,597-line file; `evals/scripts/replay_targets.py` reading the
record through `round_of`, `finding_spans`, `TARGET_LABEL`, `LOCATION_LABEL`
and `FIXED`, to be re-pointed in the same commit without restating the
grammar a fifth time. The grammar is the 0.22.0 record as the owner designed
it; this phase changes where it is stated, not what it accepts, except that
a shape outside the table is refused by construction, and a refusal of a
record a 0.22.0 round wrote stops the phase. The section heading is what the
loader finds, and #941 (0.22.2) must move the table with it.

## What this phase found

**The table is fourteen rows, and the loader reads every column.**
`docs/the-review-record.md` §*The round record* now holds
`| Line | Shape | Where | How many | Refused as |`: the eight labels, the
finding heading, the two sections and the three old spellings. A shape is a
regular expression that must match the whole line, label included, with the
parts the check reads named as groups (`(?P<commit>…)`, `(?P<round>…)`,
`(?P<finding>…)`, `(?P<home>…)`, `(?P<number>…)`). `Where` and `How many`
are each one of a few words the script names, and the readers enforce them
generically: every row placed in a finding is counted and matched in
`finding_of`, every row outside every finding in `record_lines`, every row
in `## Confirmations` in `confirmations`. `misspelt` builds its loose match
from the table's `Line` cells, and an old spelling's row names the label it
means in its `Refused as`. So the sections and the old spellings, which
were constants (`OLD_LABELS`, the `MISSPELT_LABEL` alternation, the section
counts in `NO_FINDINGS` and `TWO_CONFIRMATIONS`), are rows too
(`overview.md`'s divergence row).

**What the script still names, and why.** The nine rows it reads a meaning
from, by their `Line` cell, with the named parts of each (`READ_ROWS`), and
the four verdict words it decides on (`OPEN`, `FIXED`, `REJECTED`,
`DEFERRED`), which `release_seal.py`, `broad_gate.py` and
`replay_targets.py` also read. `grammar` refuses a table that lacks one of
the nine rows or one of its named parts. Every shape, place, count, refusal
sentence, the label list and the old spellings left the script
(`git grep` for the removed names finds nothing outside `seal/specs/` and
`changelog/`, executed).

**The loader loads the shared reader at import.** The table's cells are
split by `unverified_check.py#split_row`, the one reader of a GFM row, so
importing `chain_check.py` now loads that file as well. Run as a command, a
reader or a table that will not load prints its sentence and exits 2;
imported, the error is raised as `GrammarError`, a `ValueError`, so an
importer decides what it means. `broad_gate.py#load` turns it into
`Refused` and its panel's label goes on without the round counts, which
keeps its rule that a label never stops a sealed run (read). The copied-alone
case of `tests/test_a_script_copied_alone_exits_2.py` still meets the reader
first and still passes unchanged (executed).

**What the check now refuses that it accepted before, all by construction
of the table, and none in a 0.22.0 record.**

- A `severity:` value other than `must` or `should`. Before, nothing of
  the value was read.
- A finding with no `severity:` or no `answer:` line, or with two of
  either. Before, neither was counted. The template, the document and
  every 0.22.0 record hold one of each.
- A section heading that only begins with `## Findings` or
  `## Confirmations` is still no section, as before; that is now a case.

T2's first case shows each (`verdict: fixed abc1234 and more`,
`target: abc1234 against main and more`, `severity: anything at all`, a
finding with its `answer:` line deleted). A scratch script read every round
record in the tree through `round_of` and `channel` before and after the
change and diffed the two (executed): the ten 0.22.0 records of
`1791933022-every-agent-skill-and-doc-states-the-current-rule-only` read
identically with no refusal; the 35 pre-0.22.0 table records were refused
before and after, and only the wording of their `no target:` refusal moved.

**The test rows, against the tree.** T3 (T32, T33, T35, T36 of #923) is
unchanged in what it refuses; each docstring now names the row it reads
through. Three fixtures elsewhere in `tests/test_chain_check.py` had written
a finding with its `answer:` line removed or a severity of
`anything at all`, as a control or a convenience, and now keep a valid one.
The open-finding message names the verdict row's refusal instead of a
restated list of three values, and its pin moved with it.

**The document's other restatement went too.** `docs/the-review-record.md`
§*What the check reads at the pull request*'s paragraph listed the grammar's
refusals a second time; it now names the table for them and keeps the
refusals the table does not hold (an open finding, a `fixed` commit off the
branch or touching nothing located, the references between rounds).

**Left standing, and whose.** `agents/warden.md`, `agents/smith.md` and
`skills/code-review/SKILL.md` name labels and values in their own
instructions (`agents/warden.md:284`, `:295`, for two). They are #957's
rewrite, and it should point them at the table. `evals/scripts/behaviour.py`'s
`FINDINGS_SHAPE` is an eval grader's loose regular expression for "a finding
in the record's shape", not the grammar, and the evaluation is #957's too.

**For #941.** The loader finds the table by `GRAMMAR_SECTION`
(`## The round record`) and `GRAMMAR_COLUMNS`, in `GRAMMAR_DOC`. A rewrite
of `docs/` that moves the heading, renames a column or splits the file
moves those three constants in the same commit, or every import of the
check raises and CI goes red naming the file. The document's loader
paragraph says so.

**The file grew.** `chain_check.py` went from 1,597 lines to 1,850: about
110 lines of constants left, and the loader with its refusals and the
generic readers came in (`wc -l`, executed).

**The cases this phase added or changed, and how each was seen red.**
`tests/test_chain_check.py::TestGrammar` (T2):
`test_the_table_loads_and_every_line_matches_its_row_whole` and
`test_a_document_the_check_cannot_read_is_exit_2_naming_it`, the second over
sixteen broken documents. All seventeen ids were red against the reader at
`bccd906c`, run from a scratch copy of the module pointed at that script
(`AttributeError`, no `GRAMMAR` and no `GrammarError`, executed).
`tests/test_the_pull_request_language_is_the_repositorys.py::test_the_exclusion_list_points_at_the_grammar_table_and_restates_none_of_it`
is new, and `ROUND_RECORD_FIELDS` is now derived from the table. Then
`mutation-check`, one break at a time, all executed and all `red`:

| Unit | Break | Cases |
|---|---|---|
| `finding_of` | a row's shape read by `match` instead of `fullmatch` | T2 first case |
| the load at import | `raise SystemExit(2)` dropped | T2 second case |
| `as_row` | `fullmatch` as `search` | `TestLocationOf` (T33) |
| `label_of` | the label read case-insensitively | T32 |
| `code_span` | the same-length run check dropped | T2 second case |
| `meant_by` | more than one label accepted | T2 second case |
| `value_of` | the space after the label kept | `test_each_finding_is_read_by_its_labelled_lines` |
| `reference` | a round alone read as finding 0 | `TestReferenceOf` (T35) |
| `sections_of` | `fullmatch` as `match` | T2 first case, after the case was added (it SURVIVED first) |
| `finding_of` | the missing-line count dropped | T2 first case (`test_what_the_check_cannot_read_is_refused_by_name` alone let it survive, because the verdict guard below says the same) |
| `finding_of` | the too-many count dropped | `test_what_the_check_cannot_read_is_refused_by_name` |
| `counted` | a record with no `target:` line accepted | `TestRecordTarget` |
| `grammar_row` | a label's shape not held to open with the label | T2 second case |
| `finding_of` | the `regression:` and `reopens:` rule dropped | T42's case |
| `record_findings` | the rows outside every finding not read | T2 first case |
| `misspelt` | an old spelling named as itself | T32 |
| `findings` | a `confirms:` line outside its section accepted | `test_a_target_or_confirms_line_out_of_its_place_is_refused` |
| `finding_of` | the guard for a finding with no verdict dropped | T2 first case, after the case was added (it SURVIVED first) |
| `replay_targets.py#labelled_round` | the location read from the `target:` row | the two labelled cases |
| `replay_targets.py#labelled` | a record read as labelled by its `location:` row | the two labelled cases |
| `templates/config.md` | the pointer to the table replaced by a label | the new language case |
| `templates/sdd-round.md` | `## Probes` misspelt | `test_the_round_template_carries_the_fields_it_is_expected_to` |

The two survivors were answered with cases in 3a5351cf.

**Verification.** On the tree committed as 3a5351cf, all executed:
`bin/test` over the 52 modules that read `docs/the-review-record.md`,
`templates/sdd-round.md`, `templates/config.md` or `chain_check.py`, with
`tests/test_evals_layout.py` and `tests/test_a_phase_hands_the_next_one_a_record.py`,
exit 0, 2,994 passed and 7 skipped, with this record in the tree;
`bin/rules --check` exit 0, *all 415 `Enforced by:` targets in 60 rule files
resolve*; `chain_check.py --baseline
origin/release/v0.22.1 --root <this checkout>` exit 0, judged as no pull
request, naming this item's rounds, broad-gate file and guarantee as owed;
the two collection-wide durations cases exit 0; `uvx ruff check` and
`uvx ruff format --check` over the four changed Python files exit 0.
