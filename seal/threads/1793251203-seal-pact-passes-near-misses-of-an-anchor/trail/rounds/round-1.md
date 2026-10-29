# Review round 1: 1793251203-seal-pact-passes-near-misses-of-an-anchor

target: 9c8252d3 against origin/release/v0.24.2

## Findings

### 1. A row in a tab-indented code block is refused as a row no anchor table holds

severity: should
location: `skills/verify/scripts/pact_check.py:501-519`, `tests/skills/test_pact_check.py:578-585`
evidence: executed `bin/test tests/skills/test_tmp_r1_probe.py -p no:xdist -q -s`

`seal pact` exits 2 on a signer's frame that GitHub renders correctly. A
frame holding no anchor table, with a blank line and then
`\t| git@example.com:org/orders-api.git | ## Order response shape / ### Fields | deadbeef |`,
printed `REFUSED ... design.md:5` with the `OUTSIDE_TABLE` sentence. The
same line indented by two spaces and a tab was refused the same way. In
CommonMark a tab before the run counts to the next multiple of four, so both
lines are an indented code block, not a table row. The signer is told to
rewrite text that cites nothing.

The crafter claimed, in `row_cells`' docstring and in `trail/phases/phase-1.md`,
that the kept indentation makes "a line four columns in, an indented code
block" read as no row. `pact_check.py:512` strips spaces alone
(`written.lstrip(" ")`), so a leading tab stays in `content`, which then
does not start with `|`. Line 514 prepends `| `, and `config.table_cells`
reads `| \t| <remote> | <heading> | deadbeef |` as a four-cell row whose
cells include the declared remote and the heading. The claim holds for four
spaces (probe P3, exit 0) and fails for a tab (P1, P2, exit 2). The passes
case pins only the four-space shape (`tests/skills/test_pact_check.py:578-585`).
`hooks/lib/config.py#gfm_table` already counts columns this way for a
heading (`blocks.columns(line) < 4`), so the walker and the new scan
disagree on what an indented line is.

```python
def row_cells(config, line):
    """The cells of LINE read as a table row by `config.table_cells`, with
    an outer pipe given where LINE leaves one out, so a row of a table
    written without them reads too; None where LINE holds no pipe, does
    not read as a row even so, or stands four columns in, a tab counting to
    the next multiple of four (`blocks.columns`), which is an indented code
    block."""
    if "|" not in line:
        return None
    # No precondition beyond `hooks/lib/config.py` having imported `blocks`,
    # which it does at import. Any tab in the leading run reaches four
    # columns, so past this guard the run is spaces alone.
    if config.blocks.columns(line) >= 4:
        return None
    cells = config.table_cells(line)
    if cells is not None:
        return cells
    written = line.rstrip()
    content = written.lstrip(" ")
    indent = written[: len(written) - len(content)]
    if not content.startswith("|"):
        content = "| " + content
    if not content.endswith("|") or content.endswith("\\|"):
        content += " |"
    return config.table_cells(indent + content)
```

The passes case's frame z gains the tab shape beside the four-space one,
seen red against `9c8252d3` before the guard lands:

```python
        write(
            world.web,
            "seal/threads/1790000002-z/frame/design.md",
            f"# Z\n\nx\n\n    | {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n"
            f"\n\t| {PACT_URL} | {CLAUSE_PATH} | deadbeef |\n",
        )
```

verdict: fixed 1783b55a
answer: The finding holds. `row_cells` now returns None where `config.blocks.columns(line) >= 4`. Past that guard the leading run is at most three spaces, which `table_cells` reads past, so the kept-indentation step is gone and the line is read without it. Frame z of the passes case gained a tab line and a two-spaces-and-a-tab line beside the four-space one. Against the code before the fix, the case failed with `OUTSIDE_TABLE` at line 7 of frame z and exit 2 where 0 was expected. `seal mutate` replaced the guard with `if False:` and then with `>= 5`, and both were red. `trail/phases/phase-1.md`'s sentence on the four-column line was corrected in place at `bbfbe93e`.

### 2. No case pins that the row scan reads every declared pact, not this pact alone

severity: should
location: `tests/skills/test_pact_check.py:953-963`
evidence: executed `bin/test tests/skills/test_pact_check.py -q`, `bin/test tests/skills/test_tmp_r1_probe.py -q -k declared`

`frame/design.md` *Scope* item 2 refuses a stray row where "one cell is one
remote URL matching a declared remote", and `stray_rows` receives
`declared_remotes`, every pact the signer's `Pact` row declares
(`pact_check.py:735`, `:776`). A stray row naming another declared pact is
refused at `9c8252d3`: probe P4 wrote a signer declaring the pact and
`git@example.com:org/billing.git`, and a near-miss header over a row naming
billing and a heading, and the run exited 2.

No test holds that shape. With the argument at `pact_check.py:776` replaced
by `frozenset({ours})`, `tests/skills/test_pact_check.py` passed whole (107
passed), and only P4 went red. `trail/phases/phase-1.md` claims ten mutants,
all red, among them "the declared-remote test"; this mutant was not among
them and survives. Every case of
`test_refuses_an_anchor_row_no_anchor_table_holds` runs under the default
signer config, which declares `PACT_URL` alone, and the only case declaring
other remotes, the passes case, puts them in walked rows. A later edit that
narrows the scan to this pact would ship silently, and a signer's stray row
naming a second pact would again be graded by nobody. The mutation result
above licenses *tested* for what the suite pins, never *safe*.

The group gains one id and declares billing for every id, which changes no
other id's outcome, since none names billing:

```python
BILLING = "git@example.com:org/billing.git"  # NAME NOT IN TREE: the passes case spells it inline

            (
                "| pact | clause | hash |\n|---|---|---|\n"
                f"| {BILLING} | {CLAUSE_PATH} | 1a2b3c4d |\n",
                3,
            ),

            "a row naming another pact the signer declares",

    def test_refuses_an_anchor_row_no_anchor_table_holds(self, world, text, line):
        write(
            world.web,
            "seal/config.md",
            signer_config(("Pact", f"{PACT_URL}; {BILLING}")),
        )
        write(world.web, SPEC, text)
        code, out = world.run()
        assert code == 2, out
        assert f"REFUSED {SIGNER_URL} {SPEC}:{line} — {OUTSIDE_TABLE}" in out, out
```

The new id is seen red with the scan narrowed to `frozenset({ours})`.

verdict: fixed 1783b55a
answer: The finding holds. `test_refuses_an_anchor_row_no_anchor_table_holds` declares `BILLING` beside the pact for every id. It gained the id `a row naming another pact the signer declares`, a near-miss header over a row naming billing and a heading. `BILLING` is now a module constant, and the passes case reads it instead of its own inline spelling. Before the fix commit, `seal mutate` passed `frozenset({ours})` in place of `declared_remotes` at the `stray_rows` call, and the run was red on that id alone. `trail/phases/phase-1.md`'s mutation paragraph now says that none of its ten mutants narrowed the scan (`bbfbe93e`).

## Confirmations

confirms: none
The crafter's named walker limit is not exposed through `stray_rows`. An
anchor table, a blank line and a four-space `| … |` line print one `REFUSED`
line for the frame, the walk's "a row the walk never reaches" (probe P5),
because the scan runs only where the walk refused nothing
(`pact_check.py:771`). The walk's own refusal stands at the base and is a
row of `## Not judged`. Executed.

confirms: none
*Scope* item 1 is built as framed: a walked row whose `Pact` cell names a
remote outside `declared_remotes` is refused with `UNDECLARED`, and a row
naming another declared pact is passed over (`pact_check.py:756-759`).
`one_remote` refuses a backtick before the sentence formats the cell, so the
backticks around `{cell}` cannot be broken. S1's two ids and S2's rewritten
passes case pass. Executed, by the narrow run below.

confirms: none
*Scope* item 3 matches *Data & interfaces* character for character:
`INLINE_TOKEN` at `pact_check.py:213` is the framed pattern with
`re.IGNORECASE`, and the comment above it states the case fold and the
space limit (*Scope* item 4). Read.

confirms: none
S5 is an assertion on its group rather than a new case: every id of
`test_refuses_an_anchor_row_nobody_reads` now counts one `REFUSED` line for
the frame (`tests/skills/test_pact_check.py:887`), and the new id
`a row under a blank line` covers d06. The ten ids of
`test_refuses_an_anchor_row_no_anchor_table_holds` cover shapes no existing
case held, so neither addition duplicates its group. Read.

confirms: none
The two `## Rule changes` entries whose `from:` text is quoted from #913's
unsettled design match that design's `to:` text
(`seal/threads/1793169127-pact-check-reads-the-retired-grammar/frame/design.md:242`,
`:262-273`). The module docstring sections *What each frame is read for*
and *Exit codes* are rewritten in place, and `git grep` outside
`seal/threads/` finds no other statement that a row naming another pact is
passed over. Executed.

confirms: none
The orchestrator's fold at `9c8252d3` holds: `frame/design.md:49` writes
`git@other.example.com:o/pact.git`, and `tests/test_censuses.py` passed in
the narrow run below. Executed.

confirms: none
The handoff's label is honest: the full suite, the repository-wide lint and
the typecheck are labelled `unverified` with the orchestrator as their
answerer, and this round ran none of them (contract rule 2).

Carried from the frame, not re-established: the d01 to d26 reprobe at
`28edee12`, the four-revision measurements of the case-folded token and of
a bare remote beside a heading cell, and the claim that the pact files are
unchanged between `5287dd42` and `28edee12`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck | the branch at `9c8252d3` | the orchestrator, by the broad gate |
| The walk refuses a row line indented four spaces, below a blank line under the anchor table, as a row nobody reads, though GitHub renders it as code. It stands at the base, outside this diff and outside the plan, which does not edit the walker (probe P5) | `hooks/lib/config.py#gfm_table` | the orchestrator: whether it is a later work item |
| The phase records' red-first runs against `28edee12` and their eleven mutation runs were not re-run; finding 2 names one mutant the list did not hold | `trail/phases/phase-1.md`, `trail/phases/phase-2.md` | the sealer, by its sample |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_tmp_r1_probe.py -p no:xdist -q -s` in a `git clone --no-local` at `9c8252d3`, five cases | P1 (a tab-indented row, no anchor table) and P2 (two spaces and a tab) exited 2 with `OUTSIDE_TABLE` at line 5: 2 failed. P3 (four spaces) exited 0. P4 (a stray row naming a second declared pact) exited 2. P5 (a four-space row below the anchor table) printed one `REFUSED` line for the frame. The probe file was deleted |
| `bin/test tests/skills/test_pact_check.py -q` with `pact_check.py:776` passing `frozenset({ours})` for `declared_remotes`, edited in the clone | 107 passed, exit 0: the mutant survives. `bin/test tests/skills/test_tmp_r1_probe.py -q -k declared` under the same mutant: 1 failed. The edit was reverted with `git checkout` |
| `bin/test tests/skills/test_pact_check.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_a_signer_declares_its_pact.py tests/test_censuses.py -q` at `9c8252d3`, unmodified | 309 passed, exit 0 |
