# Review round 4: 1793411151-judgment-where-meaning-is-the-question

target: c7384abf, fixes 476ff249..c7384abf

This is the verifying round over round 3's fix pass. The range holds
`b2f0bc30` (finding 1: `chain_check.py`, its case, `gaps.md`), `a143e583`
(finding 2: two cases) and `c7384abf` (the round 3 record's closing
lines). It reads that diff and what the diff calls. It reads nothing of
phases 3 to 5, which are not built.

Carried from round 3, not re-derived: where `unread`, `unread_verdicts`,
`originals_of` and the `item` fixture live, and its finding that no pair of
`seal layout --pairs` names a case of the module; the pairs were re-run and
still name none. Re-derived this round: each close, by re-running the case
the fix added against the mutant that case pins, and the fix's own unit, by
a probe. The repository declares no `seal/parity.md`, so this record holds
no `original:` line.

## Findings

### 1. A guarantee whose `original:` line no check reads has its `Original:` line named, and the notice says the check reads it

severity: should
location: `skills/code-review/scripts/chain_check.py:796-802`, `skills/code-review/scripts/chain_check.py:1879-1916`, `tests/skills/test_chain_check.py:2206-2235`
evidence: executed `bin/test tests/skills/test_tmp_round4_probe.py -p no:xdist -q -s`
verdict: fixed 321c8e58
regression: round-3#1

The unit is the block `b2f0bc30` added to `unread` at
`chain_check.py:796-802`. The frame (`frame/design.md:172`, Table A's row
at `:291`, built by `frame/plan.md`'s phase 2 row as *Scope* item 5) has
the check name a line that opens like a label of a form it reads, while
the fix names a guarantee's near `original:` line wherever the work item
is not chained, and the gap came from round 3's paste-ready fix, whose
grounds said "restricted to the guarantees `originals_of` reads" and whose
code tested `not chained` alone.

A guarantee's `original:` line is a line of its form only where step 5 of
`agents/sealer.md` owes it: git carries `seal/parity.md`, the work item
answers `straight to the PR`, and the diff changes a path outside `docs/`
and `seal/` (`agents/sealer.md:105-111`). `originals_of` reads the
line under exactly those conditions: it returns nothing where the config is
absent (`chain_check.py:1891`) and nothing where the paths stay inside the
document roots (`:1900`). `unread` checks none of them. The new docstring
says the naming applies "where the work item is not chained, so that
`originals_of` reads the guarantee's `original:` line"
(`chain_check.py:780-782`), and that is not what `not chained` means.

The probe built the `item` fixture, a work item declared `straight to the
PR` in a repository with no migration config, and gave its guarantee the
line `Original: abc1234`. The check exited 0 and printed
`guarantee.md:8  not read: ...`, which says the check "reads `original:` at
the start of a line, lowercase". No check reads that line there, in either
spelling. The notice tells the sealer or the orchestrator to respell a line
nothing reads, and a notice that sends its reader to fix nothing is the
noise `frame/plan.md` *Operational impact* fears. The core's sentence names
"a line ... that looks like one of its form's" (`skills/core/SKILL.md:123-124`),
and outside a migration the guarantee's form has no such line.

The class is every guarantee of a work item not chained that `originals_of`
does not read. It has two members: no migration config at HEAD, and a diff
that stays inside the document roots. The fix below covers both by
construction, since the naming happens only where `original_of` reads the
guarantee.

Move the naming out of `unread` into the loop of `originals_of` that reads
the guarantee. In `chain_check.py`, beside `original_of`:

```python
def unread_originals(reader, text, rel):
    """[(rel, line, why)] for each line outside fences of a guarantee
    `originals_of` reads that opens like `original:` and is not it, at its
    line (`UNREAD_LINE`). Such a line is prose: it decides nothing, and the
    guarantee holding only it holds no `original:` line."""
    label = f"`{ORIGINAL_ROW}`"
    return [
        (rel, i + 1, UNREAD_LINE.format(said=line.strip(), label=label))
        for i, line in enumerate(reader.readable(text))
        if opens_like(line) == ORIGINAL_ROW
    ]
```

`originals_of` takes `notices=None` after `direct=()`, its docstring gains
"Each line of a guarantee it reads that opens like `original:` and is not
it goes to NOTICES (`unread_originals`).", and its guarantee loop becomes:

```python
    for item in direct:
        rel = f"{item}/{GUARANTEE_FILE}"
        said = read_record(root, rel)
        if said is not None:
            found.extend(
                original_of(reader, said, rel, sha, config, NO_GUARANTEE_ORIGINAL)
            )
            if notices is not None:
                notices.extend(unread_originals(reader, said, rel))
```

In `main`, `notices` is printed after this call, so the call passes it:

```python
    found = originals_of(reader, routing, root, paths, chained, direct, notices)
```

In `unread`, the `if not chained:` block at `:796-802` goes, and the
docstring returns to the text before `b2f0bc30`: "...and each line of its
`guarantee.md` that opens like `Verdict:` and is not it
(`unread_verdicts`). `main` prints them as notices."

In `Test_originals_of`, after
`test_refuses_a_direct_guarantee_whose_only_original_is_misspelt`. The probe
above is this case with its last assertion inverted, so the case is red
against the code at `c7384abf`:

```python
    @pytest.mark.rule("parity-in-the-guarantee")
    def test_names_no_original_line_where_none_is_owed(self, item, capsys):
        """Round 4 of #1167: with no migration config no check reads a
        guarantee's `original:` line, so `Original: <sha>` there is no line
        of its form and is not named. Seen red against the `unread` that
        named it in every guarantee of a work item not chained."""
        root, _audited = item
        reseal(root, BASELINE)
        path = root / f"{ITEM}/guarantee.md"
        text = path.read_text(encoding="utf-8").replace("original:", "Original:")
        path.write_text(text, encoding="utf-8")
        commit(root, "a guarantee holding Original: with no migration declared")
        code, out = check(root, capsys)
        assert code == 0, out
        assert [ln for ln in out.splitlines() if "not read" in ln] == [], out
```

The existing misspelt case keeps its one `not read:` line, since there the
config is carried and the diff changes `f.txt`. This round ran neither
snippet. A diff inside the document roots has no case here; the fix covers
it by where the call stands, and the fix pass may add one if it is cheap
with the `item` fixture.

answer: The finding holds. Before applying the paste-ready fix, I checked its code against its grounds sentence, which says the line is named "only where `original_of` reads the guarantee". The call stands in `originals_of`'s guarantee loop, after the config, the parity readers, the document-roots test and the baseline SHA have all let the read through, so it holds. `321c8e58` applies the fix as written: `unread_originals`, the `notices` argument of `originals_of`, the call in `main`, and the `unread` block and docstring sentence that `b2f0bc30` added, both removed. The module docstring's naming paragraph, which named `unread` alone, now names `unread_originals` too. The case is `test_names_no_original_line_where_none_is_owed`. It runs the paste's half, with no migration config, and adds the second member of the class, a config with a diff inside the document roots, through the setup of the case beside it. It failed at `a143e583`'s code on the first half (executed). After the fix, three `seal mutate` runs were red, each against the case it targets (executed): the naming put back into `unread` turned the new case red; the call in the loop removed turned `test_refuses_a_direct_guarantee_whose_only_original_is_misspelt` red; a naming placed before the document-roots return turned the new case's second half red. `bin/test` over `test_chain_check.py`, `test_seal_stamp.py` and `test_the_sealer_guarantees.py` passed, 435 cases (executed). `trail/phases/phase-2.md`'s departure d still says the line is not named; it stays as the phase's account, since a fix pass writes no phase record.

## Confirmations

confirms: round-3#1
The close holds for the case round 3 found, and finding 1 above is about
the guarantees beyond it. `b2f0bc30` touches the three paths named on
finding 1's location line (executed, `git show --stat`). In a migration
repository with a code change, a `straight to the PR` guarantee holding the
line `Original: <sha>` alone is refused as holding no `original:` line, and
that line is named once, at its line (`chain_check.py:796-802`, read). With the
block switched off in the clone, the case
`Test_originals_of::test_refuses_a_direct_guarantee_whose_only_original_is_misspelt`
failed on its new assertion, `[] == [...]` at
`tests/skills/test_chain_check.py:2232`, and the block was restored
(executed). That is the crafter's seen-red claim, reproduced. The
`gaps.md` *Not done* paragraph that stood on the old reading is gone
(executed, `git grep` over the branch for the old sentence).

confirms: round-3#2
The close holds. Each new case is red against its own mutant and only
against it. With `unread`'s call reading the round record through
`reader.gfm_lines` (`chain_check.py:791`),
`Test_main::test_names_no_line_inside_a_fence` failed on a `not read:`
line for the fenced `Verdict: open` at the record's line 17, and the
guarantee case passed. With `unread_verdicts` reading through `reader.gfm_lines`
(`:1967`), `Test_verdicts_of::test_names_no_verdict_line_inside_a_fence`
failed on `('g.md', 21, ...)`, and the record case passed. Each mutant was
restored (executed). The fix pass claimed the guarantee case's first
assertion is stricter than the paste's: it compares the whole list of
verdicts read, not the last one's text (`tests/skills/test_chain_check.py:2492-2494`,
read). That holds. That assertion does not test the fence, since
`verdicts_of` never reads a `**Verdict:**` line, fenced or not; the second
assertion is the one the mutant fails, which is all finding 2 asked.

confirms: none
The fix range passes. `bin/test` over `tests/skills/test_chain_check.py`,
`tests/skills/test_seal_stamp.py` and
`tests/behaviour/test_the_sealer_guarantees.py` at `c7384abf` passed, 434
cases, as the crafter reported, and `ruff check` and
`ruff format --check` over the two changed code files exited 0 (executed).
Each new case covers what no case of its group covered before, since round
3's mutants survived the module without them, and `seal layout --pairs`
names no pair in the module (executed).

confirms: none
The two accounts of departure d are linked, not contradictory for a reader
of the rounds. At HEAD `trail/phases/phase-2.md:58-63` still says that a
guarantee's near `original:` line is not named, while the code names it. A
fix pass writes no phase record (`agents/crafter.md:164`,
`skills/implement/SKILL.md:485-490`, read), so leaving the paragraph is the
documented flow. Round 3's finding 1 cites that paragraph by name and
closes `fixed b2f0bc30`, so a reader who reads the phases and the rounds,
as the sealer does, meets the later account with its commit. The
`gaps.md` paragraph, which is read as a live claim at the seal, is
removed. The one reader not sent from one account to the other is phase
3's crafter, whose order of work reads earlier phase records and not round
records (`agents/crafter.md:35-38`); that is a row of `## Not judged`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `c7384abf` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| How GitHub renders the `::notice` `not read:` lines, carried from round 3 | `skills/code-review/scripts/chain_check.py:2403-2404` | the orchestrator, at the first CI run of the pull request |
| Whether phase 3's crafter, which will add a path into `unread` for departure e and reads `trail/phases/phase-2.md` but not round records, is handed round 3's finding 1 and this round's finding 1 beside departure d | `seal/threads/1793411151-judgment-where-meaning-is-the-question/trail/phases/phase-2.md:58-63` | the orchestrator, in the phase 3 spawn prompt |
| Departure e: a near `## Rule Changes` heading has no path into `unread` yet | `skills/code-review/scripts/chain_check.py:774` | the round that reads phase 3 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py tests/skills/test_seal_stamp.py tests/behaviour/test_the_sealer_guarantees.py -q`, in a `git clone --no-local` at `c7384abf` under the scratchpad | 434 passed, exit 0 |
| `bin/test tests/skills/test_tmp_round4_probe.py -p no:xdist -q -s`, one case on the `item` fixture with no migration config and `Original: abc1234` in the guarantee, then deleted | exit 0 from the check, one `guarantee.md:8  not read:` line naming the `original:` label (finding 1) |
| The misspelt-original case by node id with `unread`'s `if not chained:` made `if False:`, then restored | 1 failed, at `test_chain_check.py:2232`, `[] == [...]` (round-3#1) |
| Both new fence cases by node id with `unread`'s round-record call on `reader.gfm_lines`, then restored | 1 failed, `test_names_no_line_inside_a_fence`; 1 passed (round-3#2) |
| Both new fence cases by node id with `unread_verdicts` on `reader.gfm_lines`, then restored | 1 failed, `test_names_no_verdict_line_inside_a_fence`; 1 passed (round-3#2) |
| `uvx ruff check` and `uvx ruff format --check` over `chain_check.py` and `test_chain_check.py`, same clone | exit 0 and exit 0 |
| `bin/seal layout --pairs`, same clone | no pair names a case of `tests/skills/test_chain_check.py` |
