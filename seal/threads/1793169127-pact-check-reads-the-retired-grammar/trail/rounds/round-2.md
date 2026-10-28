# Review round 2: 1793169127-pact-check-reads-the-retired-grammar

target: e9acea12, fixes 8729d434..e9acea12

## Findings

### 1. A table GitHub renders under a line of prose or a thematic break is still refused below the anchor table, at exit 2, as a lost row

severity: must
location: `hooks/lib/config.py:1052-1066`, `tests/skills/test_pact_check.py:771-777`
evidence: executed `bin/test tests/skills/test_tmp_round2_probe.py -q -s -p no:xdist`
verdict: open
reopens: round-1#1

Why the close does not hold. Round 1's finding 1 was that a correct frame
is refused when another table stands below the anchor table in its
section. `aaaeb8eb` stops the walk without a refusal only where the line
above that table's header is blank (`opens_table`, `config.py:1052-1066`).
A frame often opens a table with a sentence directly above it, such as
`The clauses:`, or after a `***` rule. In both shapes `cmark-gfm` renders
two tables, and `seal pact` still refuses the frame at exit 2. It still
calls the other table's header "a row the walk never reaches — it and
every row below it would go unread". The probe (`## Probes`) wrote both
shapes under `## Grounding`. For each, `cmark-gfm` counted 2 `<table>`
elements, and `check` printed that `REFUSED` line and exited 2. The anchor
row was graded `OK` both times.

The crafter's answer gives the reason for the blank-line condition: it
is "the rule `gfm_table` holds a first table's header to". That rule
guards the table `gfm_table` reads, where reading lines GitHub does not
render as a table would be the wrong pass. The table under the anchor
table is one `seal pact` never reads. Accepting it too readily costs
nothing the anchor reader needs. A second anchor header there is named by
`first_table`'s scan whatever stands above it. Any other header is not an
anchor row. So the blank-line condition refuses correct frames and
catches nothing.

`tests/skills/test_pact_check.py:771-777` (the id
`a row with no blank line above it`) pins one such refusal: a `***` line,
then a table with its delimiter row. That case was added in `c597ee93` to
kill the blank-line mutant. It turns into an accept case. Add one more
case for the sentence-above shape.

```python
# hooks/lib/config.py
def opens_table(index, line, under):
    """True where LINE, at INDEX, is the header of a table of its own: written
    `| … |`, with UNDER, `[(index, line)]` for the next shown line or `[]`,
    a delimiter row of the header's width directly below it. What stands
    above it is not asked: the caller does not read that table, and a second
    header of the caller's own table is named by the caller's header scan."""
    cells = table_cells(line)
    if cells is None or not under:
        return False
    below, row = under[0]
    return (
        below == index + 1
        and "|" in row
        and DELIMITER_ROW.match(row) is not None
        and row.strip().strip("|").count("|") + 1 == len(cells)
    )

# in gfm_table
                if beside and opens_table(index, line, body[k + 1 : k + 2]):

# tests/skills/test_pact_check.py, Test_check: the `***` shape leaves
# test_refuses_an_anchor_row_nobody_reads and joins an accept case
@pytest.mark.parametrize(
    "between",
    ["\n", "\nThe clauses:\n", "***\n"],
    ids=["a blank line", "a sentence", "a thematic break"],
)
def test_accepts_an_anchor_table_above_another_table_in_its_section(self, world, between):
    write(
        world.web,
        SPEC,
        "# Feature\n\n## Grounding\n\n"
        + anchor_table((PACT_URL, CLAUSE_PATH, clause(V2)))
        + between
        + "| Policy clause | What it fixes for this work |\n|---|---|\n"
        + "| a | b |\n\n## Scope\n\nx\n",
    )
    code, out = world.run()
    assert code == 0, out
    assert "REFUSED" not in out and " 1 ok " in out, out
```

answer:

### 2. A row written below the other table, before the next heading, is now dropped with nothing printed

severity: should
location: `hooks/lib/config.py:1189-1209`
evidence: executed `bin/test tests/skills/test_tmp_round2_probe.py -q -s -p no:xdist`
verdict: open
regression: round-1#1

The unit is the `beside` arm of `gfm_table`'s ended branch
(`config.py:1189-1209`), added by `aaaeb8eb`. The frame states no rule
for lines after the anchor table. The rule `gaps.md` infers is that a row
the walk does not reach would read as a signer citing nothing. The fix was
meant to narrow that rule, but it ends the walk at the other table. So a
`| … |` line past that table and before the next heading is never looked
at. The defect comes from choosing `break` over stepping past the other
table's rows.

The probe wrote the anchor table, a blank line, the policy table, a blank
line, and then a lone row naming the pact,
`| git@example.com:org/orders-api.git | ## Order response shape / ### Fields | 00000000 |`.
The writer meant it as a second anchor. GitHub renders it as a paragraph.
`seal pact` printed `1 pact anchor naming this pact` and `1 ok`, and
exited 0. The row was read by nobody, and nothing said so. The `beside`
arm exists only for the anchor reader, and the stray-row refusal exists
for exactly this row. Both shapes of the fix should hold together: step
over the other table, and keep refusing what follows it.

```python
# hooks/lib/config.py, gfm_table's walk after the table's end
    rows, stray, ended, previous = [], None, False, delimiter[0]
    body = shown[at + 2 :]
    # BESIDE: the index of the last line read as part of a table of its own.
    other = None
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
            if other is not None and index == other + 1 and not table_end(line):
                # The other table's delimiter row or one of its rows.
                other = index
                continue
            other = None
            if line.lstrip().startswith("|"):
                if beside and opens_table(index, line, body[k + 1 : k + 2]):
                    # A table of its own, which GFM renders apart from this
                    # one: the walk steps over it and goes on to the heading.
                    other = index
                    continue
                stray = (
                    f"has a `{name}` table that ends above `{line.strip()}`, "
                    "a row the walk never reaches — it and every row below it "
                    "would go unread"
                )
                break
            continue
```

Add a refusal case to `test_refuses_an_anchor_row_nobody_reads`: the
anchor table, a blank line, a two-column table, a blank line, and a lone
anchor-width row. Expect the `ends above` sentence naming that row.

answer:

## Confirmations

confirms: round-1#2
The close holds. `grade` prints the hash bare in both sentences, `its hash is {current} now` (`skills/verify/scripts/pact_check.py:503` and `:516-517`). *Test_grade* pins the `SUPERSEDED` detail and now the whole `UNMATCHED` detail (`tests/skills/test_pact_check.py:495` and `:511-515`). Executed: the class search the answer names, run again in the clone, prints only `docs/the-pact.md:79`. That line is the inline shape, which `design.md` *Rule changes* already rewrites at the settle.

confirms: round-1#3
The close holds. `test_refuses_each_map_line_it_does_not_read_at_exit_2` keeps one id, `a second header the walk names` (`tests/skills/test_pact_check.py:878-893`). The four removed shapes still stand in *Test_path_map* (`:287-290`). Read, and the module passed (executed, `## Probes`).

confirms: none
`seal/config.md`'s readers accept what they did before. `beside` defaults to false. A search over every `gfm_table` and `first_table` call outside the tests shows only the anchor reader passing it (`skills/verify/scripts/pact_check.py:656`). `config_table` (`hooks/lib/config.py:345`), `read_table` (`:1269-1271`) and the map's `first_table` (`pact_check.py:311`) pass nothing (executed, `## Probes`). The loop's change from `for index, line in shown[at + 2 :]` to `enumerate(body)` changes no line it visits (read, `config.py:1189-1190`).

confirms: none
The crafter's runs reproduce. The cases of `-k "anchor_row_nobody or above_another_table"` were run against `config.py` and `pact_check.py` as at `8729d434`: 2 failed, the two the answer names. The five modules at `e9acea12` gave 972 passed (executed, `## Probes`). The changelog fragment and `gaps.md` *Fed back into the spec* state the narrowed rule as built. Findings 1 and 2 above change that rule, so the fix pass rewrites both sentences with it.

Carried rather than re-established: round 1's coordinates for the anchor reader (`pact_check.py#first_table`, `check`'s frame loop) and for `gfm_table`'s ended branch. I opened them at the new lines and did not search again. Every verdict here was reached this round.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether `cmark-gfm` renders a table under every other non-blank line a frame can hold above one, such as a list item or an HTML block. The probe tried a sentence and a `***` rule only | `hooks/lib/config.py#opens_table` | the fix pass, where it keeps any condition on the line above |
| The full suite, the repository-wide lint and the typecheck | the branch | the orchestrator, through `seal gate` after the rounds settle |
| The rebase onto #1058's `tests/conftest.py` change near `:418-433` | `tests/conftest.py` | the orchestrator, after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_round2_probe.py -q -s -p no:xdist`, in a clone at `e9acea12` | Three frames under `## Grounding`, each rendered by `cmark-gfm` and run through `check`. First, the anchor table, a blank line, `The clauses:` and the policy table directly under it: 2 tables, exit 2, refused as a row the walk never reaches. Second, the same with a `***` line in place of the sentence: 2 tables, exit 2, the same refusal. Third, the anchor table, a blank line, the policy table, a blank line, and a lone anchor-width row naming the pact: exit 0, `1 ok`, nothing about the row. The file was deleted after the run |
| `bin/test tests/skills/test_pact_check.py tests/skills/test_coordinates.py tests/hooks/test_config.py tests/test_censuses.py tests/behaviour/test_one_table_walker_reads_what_gfm_renders.py -q`, in the clone | 972 passed, exit 0 |
| `git checkout 8729d434 -- hooks/lib/config.py skills/verify/scripts/pact_check.py`, then `bin/test tests/skills/test_pact_check.py -q -k "anchor_row_nobody or above_another_table"`, then both files restored to `e9acea12`, in the clone | 2 failed, 5 passed, exit 1. The two failures are `test_accepts_an_anchor_table_above_another_table_in_its_section` and the id `a second table under a blank line` |
| `git grep -n -E 'gfm_table\(\|first_table\(' -- '*.py' ':!tests'`, in the clone | callers at `config.py:345`, `:1269`, `:1271`, `pact_check.py:273`, `:311` and `:656`. Only `:656` passes `beside` |
| `git grep -n -E 'reads @\|@\{current\|@\{clause\|@<hash>\|@0000'` outside `seal/` and the changelogs, in the clone | one hit, `docs/the-pact.md:79` |
