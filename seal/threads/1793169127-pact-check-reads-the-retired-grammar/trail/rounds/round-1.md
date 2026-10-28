# Review round 1: 1793169127-pact-check-reads-the-retired-grammar

target: 29e1b040 against 977b6613

## Findings

### 1. `seal pact` refuses a correct frame at exit 2 when the anchor table comes before another table in its section

severity: must
location: `skills/verify/scripts/pact_check.py:263-286`, `skills/verify/scripts/pact_check.py:653-658`, `hooks/lib/config.py:1166-1184`
evidence: executed `bin/test tests/skills/test_tmp_round1_probe.py -q -s -p no:xdist`
verdict: open

Why it matters. `design.md` *Data & interfaces* puts the anchor table in a
signer's `frame/design.md` under `## Grounding`. In
`templates/records/sdd-design.md`, that section already holds the
`| Policy clause | What it fixes for this work |` table. A framer who writes
the anchor table first and leaves the policy table under it writes a frame
GitHub renders as two tables. `seal pact` refuses that frame at exit 2 and
says something false: the policy table's header is "a row the walk never
reaches — it and every row below it would go unread". The anchor row above
it is still graded `OK`. The signer is told to repair a frame that has
nothing wrong with it. The run's exit is 2, the class `BROKEN` uses.

The grounds. `gfm_table` was written for `config.md`. That file holds one
table, so any `| … |` line after the table's end and before the next
heading is refused as a lost row (`hooks/lib/config.py:1166-1184`). The
frame reader passes every walk refusal through except `holds no`
(`pact_check.py:653-658`). That is the rule `gaps.md` *Fed back into the
spec* calls inferred during implementation. `design.md` S8 does not state
it, and neither does the `to:` text of *The pact anchor*. The inference is
sound for the map, a file that holds one table. It is wrong for a frame,
which holds a table in nearly every section. A second anchor table is a
different shape, and `first_table` already names it on its own. What
`gaps.md` claimed: a row the walk does not reach would read as a signer
citing nothing. What the probe found: the line refused is another table's
header, not an anchor row.

The probe (`## Probes`) wrote a frame of the shape
`# Feature`, `## Grounding`, the anchor table with one current row, a blank
line, the policy table, `## Scope`. It got exit 2 and a `REFUSED` line
for the frame. The line says the anchor table ends above
`| Policy clause | What it fixes for this work |`, which it calls a row
the walk never reaches. The summary read `1 ok`. With the two tables
swapped, the same probe got exit 0 and no refusal.

The fix. Stop the walk without a refusal where the line after the table's
end, together with the line under it, opens a GFM table of its own. Do
this only for a caller that asks for it, so `config.md` keeps its rule. A
second anchor table is then still named by `first_table`'s header scan.
That scan runs because the walk now refused nothing. Add a case per shape
to *Test_check*: the anchor table above a policy table is graded with no
refusal; a second anchor table directly below the first, after a blank
line, is still refused. No OS boundary is involved.

```python
# hooks/lib/config.py, gfm_table: a keyword the anchor table's reader passes
def gfm_table(text, header, beside=False):
    ...
    rows, stray, ended, previous = [], None, False, delimiter[0]
    body = shown[at + 2 :]
    for k, (index, line) in enumerate(body):
        if not ended and (index != previous + 1 or table_end(line)):
            ended = True
        if ended:
            if (
                begins[index]
                and ATX_HEADING.match(line.lstrip(" "))
                and blocks.columns(line) < 4
            ):
                break
            if line.lstrip().startswith("|"):
                under = body[k + 1] if k + 1 < len(body) else None
                if (
                    beside
                    and table_cells(line) is not None
                    and under is not None
                    and under[0] == index + 1
                    and DELIMITER_ROW.match(under[1])
                ):
                    # BESIDE: a table of its own, which GFM renders apart from
                    # this one; this table ended above it, and no row is lost.
                    break
                stray = (
                    f"has a `{name}` table that ends above `{line.strip()}`, "
                    "a row the walk never reaches — it and every row below it "
                    "would go unread"
                )
                break
            continue
        ...

# skills/verify/scripts/pact_check.py
def first_table(config, text, header, beside=False):
    rows, walked = config.gfm_table(text, header, beside=beside)
    ...

# in check():
            rows, table_refusals = first_table(config, body, ANCHOR_TABLE, beside=True)
```

answer:

### 2. A `SUPERSEDED` or `UNMATCHED` line prints the new hash as `@<hash>`, which the `Hash` cell refuses

severity: should
location: `skills/verify/scripts/pact_check.py:497-516`, `tests/skills/test_pact_check.py:495`
evidence: read `skills/verify/scripts/pact_check.py:497-516`, `skills/verify/scripts/pact_check.py:670-672`, `tests/skills/test_pact_check.py:495`, `templates/setup/pact.md:27-30`
verdict: open

Why it matters. `templates/setup/pact.md:27-30` tells a signer to start a
row with `00000000` and correct it from the first report. The report it
means is `grade`'s detail, `it reads @{current} now`
(`pact_check.py:500` and `:514`). That line prints the hash with the
inline anchor's `@` in front. A person who copies `@1a2b3c4d` into the
`Hash` cell is refused with `NOT_A_HASH` (`pact_check.py:670-672`). The
tool's own report leads the person into the near miss the new grammar
refuses. `design.md` *Scope* item 2 names the `@` as syntax a reader trips
on and removes it from the anchor. These two sentences still carry it.
`tests/skills/test_pact_check.py:495` pins the `@` (contract rule 14), so
the test changes with the code.

```python
# skills/verify/scripts/pact_check.py, grade
            return SUPERSEDED, (
                f"the signer was built against a superseded clause, the one "
                f"at {sha[:8]}; its hash is {current} now. Re-read it in the "
                "signer and re-anchor"
            )
...
    return UNMATCHED, (
        f"no commit in this repository gave the clause this hash, and its hash "
        f"is {current} now: the version was squashed away or never existed. "
        "Read both sides"
    )

# tests/skills/test_pact_check.py, Test_grade
            f"bbbbbbbb; its hash is {clause(V2)} now. Re-read it in the signer and "
```

answer:

### 3. Four of the five new map cases in *Test_check* repeat *Test_path_map*'s and cover nothing more

severity: should
location: `tests/skills/test_pact_check.py:814-852`
evidence: read `tests/skills/test_pact_check.py:245-300`, `tests/skills/test_pact_check.py:781-852`, `skills/verify/scripts/pact_check.py:586-588`
verdict: open

Why it matters. *Test_path_map*'s
`test_refuses_each_line_it_does_not_read_and_reads_the_rest` (`:245-300`)
already pins, for `path_map` itself, the shapes `no table`,
`one remote twice`, `an empty cell` and `a second header`. It pins each
sentence whole and asserts exactly one refusal. Between `path_map` and the
printed line, `check` adds one loop (`pact_check.py:586-588`). That loop
prefixes `the map` and maps the refusal to exit 2, and it is the same for
every shape. `test_refuses_a_map_that_will_not_read` (`:781`) and
`test_refuses_a_map_row_past_the_tables_end_and_reads_the_row_above`
(`:791`) already hold the loop. So the four matching ids of
`test_refuses_each_map_line_it_does_not_read_at_exit_2` (`:814-852`) catch
no mutant the group does not catch. Each of them builds a copied git world
and runs `check`. The fifth id, `a second header the walk names`, covers
something new: the `if walked` guard in `first_table` that keeps a second
header from being named twice. `plan.md` phase 1 asks for "a new case per
refusal" in both classes. That is a reading of the plan, not a policy, so
the group rule decides.

```python
    @pytest.mark.parametrize(
        "text, said",
        [
            (
                f"{MAP_TOP}\n{MAP_TOP}",
                "has a `Remote | Path` table that ends above `| Remote | Path |`",
            ),
        ],
        ids=["a second header the walk names"],
    )
    def test_refuses_each_map_line_it_does_not_read_at_exit_2(self, world, text, said):
```

Or move that one shape into *Test_path_map*'s parametrize and delete the
*Test_check* case.

answer:

## Confirmations

confirms: none
*Scope* item 1 holds as built. `path_map` (`pact_check.py:289-330`) reads the map through `first_table` and `gfm_table` with `("Remote", "Path")`. It answers `(found, refusals)`. It refuses an unreadable map once, a map with no table, an empty cell, a remote on two rows (no row read) and a second header. `check` prints each refusal after `the map` (`:586-588`). `CONFIG_SEPARATOR` and `MAP_HEADER` are gone. Executed: the search for the removed names (`## Probes`) printed no live reader of any of them. Its only hits were the word "unescape" in prose at `hooks/lib/config.py:123`, `tests/hooks/test_config.py:580` and `tests/hooks/test_worktree_guard.py:1224`.

confirms: none
*Scope* item 2 and *Data & interfaces* hold as built, except where findings 1 and 2 say otherwise. Rows are graded by the normalised `Pact` cell (`pact_check.py:659-677`). A row naming another pact is passed over. S8's three shapes are refused at the row's line. `INLINE_TOKEN` (`:190`) is one pattern over `unquoted`, so a token in a closed fence is not read. The `READ`, summary and no-origin lines name the pact by URL (`:553-559`, `:682-697`). `pact_name`, `PACT_NAME_RE` and the `named` parameter are gone from `hooks/lib/config.py`, and `pact_declaration` answers pairs. Read, and pinned by `tests/skills/test_pact_check.py` and `tests/hooks/test_config.py` *Test_pact_declaration*, which passed (executed, `## Probes`).

confirms: none
*Scope* item 3 holds. `coordinates.py` keeps exactly the units `design.md` lists. The census `coordinate_grammar`, `HASH_AFTER_AT`, its list entry and *Test_coordinate_grammar* are gone. Executed: a search for them prints only `.test_durations`, which `design.md` leaves to the orchestrator's broad run. Executed: no `check:` line names the deleted behaviour module.

confirms: none
`gaps.md`'s three divergences check out against the code. `unescape` is gone at HEAD, so the end state is the frame's. The six moved cases stand in *Test_heading_path* (`tests/skills/test_coordinates.py:32`) and ask `heading_path` directly. The second-header rule is `first_table` (`pact_check.py:263-286`): a second header is named only where the walk refused nothing. Read. The *Fed back into the spec* inference is the subject of finding 1.

confirms: none
*Scope* items 4 and 5 hold in the files listed. The sentences that said a signer's CI prints the relationship now name `seal pact` alone. The template and skill texts state the table. Read in `hooks/lib/config.py`, `README.md:269`, `README.ko.md:261`, `templates/setup/config.md:147` and `:414-424`, `templates/setup/pact.md:19-30` and `skills/implement/orchestration.md:598-601`. The crafter's claim of four more sentences fixed in test files holds: `tests/behaviour/test_a_signer_declares_its_pact.py:11` and `tests/behaviour/test_one_word_one_meaning.py:761` and `:771` read in the diff. `docs/` is untouched: the diff's stat names no `docs/` path (executed).

confirms: none
`questions.md` Q2 holds. The `tests/conftest.py` hunks sit at `:1420-1430`, `:1447-1468` and `:1513-1520`, all in the pact world, and none is near `:514-536` (read in the diff).

Carried rather than re-established: nothing. This is round 1, and no earlier record exists.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Each phase's red runs against `977b6613` and the `seal mutate` survivors the phase records report. This round re-ran none of them | `trail/phases/phase-1.md`, `phase-2.md`, `phase-3.md` | the sealer, which re-runs a sample of the crafter's claims |
| The full suite, the repository-wide lint and the typecheck. `gaps.md` labels them `unverified`, and that label is honest: no phase record claims a broad run | the branch | the orchestrator, through `seal gate` after the rounds settle |
| What the pull request body says for `CONTRIBUTING.md` *What a change to a gate must carry*: `seal pact` now refuses more (the map shapes, anchor rows, every `pact:` token), it asks nobody anything, and `## Removes` lists what goes. The body is not in the tree | the pull request body | the orchestrator, which writes it, and the sealer, which reads it |
| Whether `docs/the-pact.md` takes `gaps.md`'s inferred rule as written, or as finding 1 narrows it | `design.md` *Rule changes*, `gaps.md` *Fed back into the spec* | the settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round1_probe.py -q -s -p no:xdist`, in a clone at `29e1b040` | Two cases over `check`. The anchor table above the policy table under `## Grounding`: exit 2, the stray-row refusal naming `| Policy clause | What it fixes for this work |`, and `1 ok`. The same tables swapped: exit 0, no refusal. The file was deleted after the run |
| `bin/test tests/skills/test_pact_check.py tests/skills/test_coordinates.py tests/hooks/test_config.py tests/test_censuses.py -q`, in the clone | 515 passed, exit 0 |
| `git grep -n -w -E 'OPEN_QUOTE\|CLOSE_QUOTE\|PACT_MENTION_RE\|MAP_HEADER\|unescape'` and the same over `pact_declaration\|remote_entries\|pact_name\|PACT_NAME\|CONFIG_SEPARATOR\|resolve_unit\|PACT_ANCHOR_RE\|near_miss\|coordinate_grammar\|HASH_AFTER_AT\|py_spans\|text_regions`, outside `seal/`, `changelog/` and `CHANGELOG.md` | no live reader of a removed name. `unescape` appears only as prose, and the others only where the unit stays (`pact_declaration`, `remote_entries`) |
| `git grep -n -E 'test_a_unit_is_bounded_where_a_parser_decides\|Test_coordinate_grammar\|coordinate_grammar'` outside `seal/` and the changelogs | hits only in `.test_durations` |
| `bin/seal layout --pairs`, in the clone | no pair names `test_pact_check.py` or `test_coordinates.py` |
