# Phase 9: 1793273065-the-core-reaches-no-users-repository

| Field | Value |
|---|---|
| Phase | 9 |
| Commit | dd6f930a |

## What this phase was asked

Phase 9 of `frame/plan.md`, with `frame/design.md` *Scope* item 6 and
scenario S8. `seal payload` was to gain a session table before the agents'
tables. That table holds the `CLAUDE.md` pair with its imports and one row,
`SessionStart hook: skills/core/SKILL.md`, share `hook`. The row's bytes
are those of `hooks/lib/core.py#output` for a session in the measured tree,
and its tokens are estimated at `ASSUMED_RATIO` and labelled so. The JSON
was to gain a `session` object. The module docstring was to say why
`BASELINE_AGENT` stays `general-purpose`. The `seal payload` row of
`README.md` and `README.ko.md` was to be rewritten. Two runs against a
scratch home were to give the before and after numbers: base `53f21b54`
with the 0.24.2 block, and HEAD with no block. New cases in
`tests/skills/test_payload_meter.py` were each to be seen red first.

The handoff added one item. `test_an_import_that_is_not_a_file_is_a_missing_row`
still named A1's import path, the preset block's `@` line into the
marketplace clone's core, as its dangling import. A1 was rejected, so the
case was to get a dangling import that names no retired design and keep
what it asserts.

## What this phase found

**The frame held.** `BASELINE_AGENT` stood at
`skills/verify/scripts/payload_meter.py:93`, `composition` listed the pair
with `imports_of`'s rows, and `README.md:267` was the `seal payload` row
(read). `README.ko.md:262` holds the same row in Korean.

**How the design's rules were read where they left a choice.**

- `pair_rows(root, home, sections)` now holds the pair and its imports.
  `composition` calls it for an agent's table, and `session_composition`
  calls it for the session's, so the two tables cannot list the pair
  differently. The move added no behaviour, and the existing pair and
  import cases proved it unchanged.
- A tree with no `skills/core/SKILL.md` gets a hook row of 0 bytes marked
  `missing`. The design gives the row the bytes of `output`, and for a
  missing core `output` returns its one-line refusal. Only a tree that has
  the hook prints that refusal, and the base tree has no hook, so its
  before-run would have counted a line no session receives. `gaps.md`
  records this as a divergence.
- The meter loads `hooks/lib/core.py` from the plugin around it, the way it
  loads its two siblings. A copy of the script taken without the plugin
  exits 2 with a sentence naming the path and what it is for. `measure`
  builds the session after the calibration, so a copy missing
  `session_cost.py` still names that file first.
- The session's figures are estimated at `ASSUMED_RATIO` in a calibrated
  run too, and their basis says that no transcript calibrates a session.
- The session table lists each file of the pair on its own line, each
  import indented under its importer. An agent's table keeps the one pair
  line it had.
- `delta_against` still diffs agents alone, and a `--baseline` run prints
  no session delta. The design names none, so nothing was added.
- The module's first docstring line, which `--help` prints, and `seal.py`'s
  help line for `payload` said "what each agent's startup payload is made
  of". Both now say "a session's and each agent's". The case that runs
  `seal payload --help` asserts the new words, and the test module's
  docstring says the same.

**What the earlier work left in the test module, found by reading it whole
for the retired design.** Three things stood on A1. The dangling-import
case planted `@plugins/marketplaces/agenticseal/skills/core/SKILL.md` and
`@plugins`. It now plants `@rules/gone.md` and `@rules`, and asserts the
same two missing rows and the same rendered line. The import case's planted
text said "The block's `@` line", and now says "A backticked `@` line"; the
backtick still keeps it from being an import. Three docstrings cited
`frame/design.md` probes b, c and e. The reframe at `85e61e11` removed those
rows from the design, so each docstring now cites them at `346cd01d`, the
last commit that holds them (`git show 346cd01d:<design>`, read).

**Two checks refused correct code, and each was fixed rather than the
code** (contract rule 18).
`test_without_calibration_every_token_figure_reads_estimated_and_names_its_origin`
scans every report row whose token cell is a number, and asserts that the
basis cell starts with `estimated` or `measured`. The session's hook row in
that fixture's tree, which holds no core, is a `missing` row of three
zeros. The agent tables had always used that shape, but no fixture had
ever produced one. The scan now skips a row whose basis cell starts with
`missing`. `test_a_script_copied_alone_exits_2_and_names_what_it_misses`
copied the script into a bare directory and asserted that the refusal
names a path under it. `hooks/lib/core.py` stands three directories above
the script. The copy now stands at its own path inside an otherwise empty
plugin, so every sibling it misses is named under the copy's plugin root.
The two earlier parameters pass in that layout.

**New cases, each seen red against the meter before the code.** Four
cases joined `Test_measure` under a new S8 heading, after the pair cases.
`test_the_session_table_carries_the_hook_row_at_the_bytes_the_hook_prints`
compares the row with `output` loaded from `hooks/lib/core.py`.
`test_the_json_carries_the_session_as_an_object_of_its_own` covers the
JSON's `session` object, and checks the assumed basis in a calibrated run.
`test_no_agent_table_carries_the_hook_row` covers the agent tables.
`test_a_tree_without_the_core_has_a_missing_hook_row` covers the missing
row. `Test_module`'s copied-alone case gained a `core.py` parameter. The
red run was `bin/test -q -p no:xdist tests/skills/test_payload_meter.py -k
"session or hook_row or missing_hook or copied_alone or
not_a_file_is_a_missing"` against the committed meter with the cases added.
It failed 5 (exit 1): the four `Test_measure` cases on `KeyError:
'session'`, and the `core.py` parameter on exit 1 where 2 was asserted. The
module then passed 41 (exit 0). After `9d861670`, the first case was
extended to read the session's own lines above `## probe`, because the
agent tables print the same import rows. That is `dd6f930a`.

**`seal mutate`, one batch of 13 mutants over `payload_meter.py`, every one
red.** The mutants were: characters counted as the hook row's bytes; the
missing branch removed; the session's ratio at 3.0; no `session` in the
JSON; no session table in the report; the refusal's purpose sentence
reworded; the session built before the calibration; `missing` spelled
`absent`; no indent on an import row; no `imported by` note; no note on the
hook row; `max` for the total's `sum`; and `core.py` looked for beside the
script. The command was `bin/seal mutate skills/verify/scripts/payload_meter.py
--replace … --tests "bin/test -q -p no:xdist -x
tests/skills/test_payload_meter.py"`. It printed "13 mutants, 13 red, 0
SURVIVED" (exit 0), and `git status` was clean afterwards.

**The before and after numbers.** Both runs use the meter at `dd6f930a`.
The scratch home holds no user skill, so no row is shadowed, and no
`claude` process ran.

Before. `<scratch>/base-tree` is `git archive 53f21b54`, and
`<scratch>/home-before/.claude/CLAUDE.md` is
`git show 53f21b54:templates/setup/claude-md-block.md`. That file is
byte-identical to the installed 0.24.2 template (`cmp`, exit 0), 1,786 B:

```
HOME=<scratch>/home-before bin/seal payload --root <scratch>/base-tree
```

After. The root is this tree at `dd6f930a`, and
`<scratch>/home-after/.claude/` holds no `CLAUDE.md`:

```
HOME=<scratch>/home-after bin/seal payload
```

Every token figure below is estimated at the meter's assumed 3.2 B/token,
because no transcript was calibrated.

| Prefix | Before, bytes | After, bytes | Change | Before, tokens | After, tokens |
|---|---|---|---|---|---|
| session | 7,618 | 7,369 | -249 | 2,380 | 2,303 |
| crafter | 29,711 | 30,005 | +294 | 9,284 | 9,376 |
| framer | 32,373 | 32,667 | +294 | 10,115 | 10,208 |
| proofer | 29,304 | 29,598 | +294 | 9,156 | 9,249 |
| sealer | 29,070 | 29,364 | +294 | 9,083 | 9,176 |
| tracer | 22,790 | 23,084 | +294 | 7,121 | 7,213 |

The session's 7,618 B before are this repository's `CLAUDE.md` (5,832 B)
and the block (1,786 B), with no hook row. The 7,369 B after are
`CLAUDE.md` (1,143 B), no `~/.claude/CLAUDE.md`, and the hook's output
(6,226 B, 6,180 characters). Each agent's +294 B is the core through
`skills:` (6,732 B), less the 4,689 B `CLAUDE.md` lost and the 1,786 B
block, plus the definitions' opening sentence. Every agent's table lists
`skills/core/SKILL.md` once and carries no hook row.

In a plugin user's repository, the share this work controls is the block
and the hook. It goes from 1,786 B to 6,226 B, which is +4,440 B, about
+1,390 tokens per session. Before this work, that session read no core.
The hook's first line names the file it printed, so its bytes depend on the
path: the 6,226 B were measured with this clone's path, and an installed
copy's header names a longer version-cache path. Phase 3's after-run
measured A1, where each agent read the core twice and its total was 36,507
B for the crafter. Against that, every agent is now 6,502 B smaller.

**The phase-boundary set passed.** It was one `bin/test -q` command over
107 modules at `dd6f930a`: `tests/skills/test_payload_meter.py` and every
test module that names `payload_meter`, a README, `seal.py`,
`skills/implement/scripts` or `skills/verify/scripts`, or walks `skills/`.
It passed 5,016 cases and skipped 11 (exit 0).
