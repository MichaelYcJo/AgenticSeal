# Review round 3: 1793411151-judgment-where-meaning-is-the-question

target: c9939cad against release/v0.26.0

This round reads phase 2 alone, the range `6dfffd4d..c9939cad`, as
`frame/plan.md` *Phases* and the spawn prompt narrow it. The range holds
`84af7a2d` (the build: `skills/code-review/scripts/chain_check.py` and
`tests/skills/test_chain_check.py`), `33872e18` (its records) and `c9939cad`
(the orchestrator's fold of the fourth scenario). It is the first finding
round over phase 2, since a new phase in the plan starts the count again.
It reads `frame/design.md` *Scope* item 5, the first five scenarios of
*User scenarios & acceptance*, the `## Rule changes` items and the
`## Removes` rows that state what item 5 builds, and Table A's
`chain_check.py` row. It reads nothing of phases 3 to 5.

Rounds 1 and 2 reviewed phase 1, so no fact of phase 2 is carried from
them. One coordinate is carried: round 2's `skills/core/SKILL.md:121-126`
for the core's script sentence, re-read this round at `:123`. Round 2's
finding 1 is answered below.

## Findings

### 1. The check does not name a guarantee's `Original:` line, which the core and the frame's policy text say it names

severity: should
location: `skills/code-review/scripts/chain_check.py:774-793`, `tests/skills/test_chain_check.py:2206-2227`, `seal/threads/1793411151-judgment-where-meaning-is-the-question/gaps.md:24-26`
evidence: executed `.venv/bin/python -m pytest -p no:xdist -q -s tests/skills/test_tmp_round3_probe.py::test_tmp_direct_guarantee_original_spelt_otherwise`
verdict: open

The crafter claimed this as departure d (`trail/phases/phase-2.md`, the
paragraph on a near `original:` line in a guarantee, and `gaps.md` *Not
done*):
the parity arm refuses such a guarantee at line 0, "so the reader is sent
to the file either way". The claim about the code holds. `unread` reads
the guarantee through `unread_verdicts` alone (`chain_check.py:789-792`).
The probe built a work item declared `straight to the PR` in a migration
repository and spelt its guarantee's line `Original: <sha>`. The check
exited 1 with the refusal "no `original:` line" at line 0, and printed no
`not read:` line.

The departure does not hold against the documents above the code. The
guarantee of a work item declared `straight to the PR` is a form this
check reads: `originals_of` hands it to `original_of`, which reads the
grammar table's `original:` row (`chain_check.py:1899-1905`). The
core says a script "names as not read a line or a file that looks like one
of its form's and is not one" (`skills/core/SKILL.md:123-126`). The frame's
`## Rule changes` item for *What the check reads at the pull request*,
which the settle writes as policy, says the check "names each line outside
a fence that opens like a label and is not one" (`frame/design.md:172`).
Table A's row says the same (`frame/design.md:291`). After the settle, the
policy root would state a naming this check does not do.

The cost is real, not only textual. The refusal says the guarantee holds
no `original:` line while the file visibly holds `Original: <sha>`. The
sealer, who writes the line, or the orchestrator reads a refusal that
contradicts the file, and nothing in the output says the spelling is why.
That is the case the naming exists for. The fix is one reading in the
function that already gathers the notices, restricted to the guarantees
`originals_of` reads, so a chained work item's guarantee, which the check
reads for no `original:` line, names nothing new.

In `unread`, at `chain_check.py:789-793`; the docstring at `:775-780`
gains "and, where the work item is not chained, each line of its
`guarantee.md` that opens like `original:` and is not it":

```python
    rel = f"{item}/{GUARANTEE_FILE}"
    text = read_record(root, rel)
    if text is not None:
        found += unread_verdicts(reader, text, rel)
        if not chained:
            # `originals_of` reads this guarantee's `original:` line, so a
            # line that opens like the label and is not it is named.
            label = f"`{ORIGINAL_ROW}`"
            found += [
                (rel, i + 1, UNREAD_LINE.format(said=ln.strip(), label=label))
                for i, ln in enumerate(reader.readable(text))
                if opens_like(ln) == ORIGINAL_ROW
            ]
    return found
```

In `Test_originals_of::test_refuses_a_direct_guarantee_whose_only_original_is_misspelt`,
after its last assertion, so the case is seen red against the code as it
stands:

```python
        number = path.read_text(encoding="utf-8").splitlines().index(
            f"Original: {BASELINE}"
        ) + 1
        said = chain.UNREAD_LINE.format(
            said=f"Original: {BASELINE}", label=f"`{chain.ORIGINAL_ROW}`"
        )
        assert f"{rel}:{number}  {said}" in out.splitlines(), out
```

The snippet assumes the fixture writes the line as `original: <sha>` at
the start of a line, which the case's own `replace` already relies on;
this round did not run it. The third paragraph of `gaps.md` *Not done*
stops being true with the fix, and goes in the same commit.

answer:

### 2. No case holds that a line inside a fence is not named, in a round record or in a guarantee

severity: should
location: `tests/skills/test_chain_check.py:3496-3550`, `tests/skills/test_chain_check.py:2454-2474`
evidence: executed `bin/test tests/skills/test_chain_check.py tests/skills/test_seal_stamp.py tests/behaviour/test_the_sealer_guarantees.py -q`
verdict: open

*Scope* item 5 defines the net as "a line outside every fence"
(`frame/design.md:48`). Both readers keep it by blanking fences:
`unread` hands `unread_lines` the record through `reader.readable`
(`chain_check.py:788`), and `unread_verdicts` reads the guarantee through
`reader.readable` (`:1957`). This round replaced both calls with
`reader.gfm_lines`, which splits the same lines and blanks no fence. With
both mutants in place the command above passed, 432 cases. A first try
with `.splitlines()` failed only `test_census`, a lint over how lines are
split, so no case of the behaviour caught either mutant.

It matters because a paste-ready fix in a round record is a fenced block
by the template, and a finding about the sealer or the grammar quotes
lines such as `Verdict: open` there. A reader that loses the blanking
prints a `not read:` notice for every such block. The exit code stays the
same, so nothing goes red. `frame/plan.md` *Operational impact* and the
crafter's own grounds for departure a name this noise as the failure that
stops anyone reading the notices. The crafter's mutation run, 8 red of 8,
licenses that those eight breaks are tested, not that the net is.

Beside `Test_main::test_names_a_line_it_did_not_read_as_a_notice_and_keeps_the_exit`:

```python
    def test_names_no_line_inside_a_fence(self, branch, ready, capsys):
        """#1167, *Scope* item 5: the net reads a line outside every fence.
        A paste-ready fix block holding `Verdict: open` prints no `not
        read:` line, and the exit code is the clean record's."""
        root, code_sha = branch
        rel = f"{ITEM}/trail/rounds/round-1.md"
        text = record(code_sha, [finding(1, f"fixed {code_sha[:8]}")]).replace(
            "x = 1", "Verdict: open"
        )
        write(root, rel, text)
        commit(root, "a fix block that quotes a verdict line")
        seal(root)
        code, out = check(root, capsys)
        assert code == 0, out
        assert [ln for ln in out.splitlines() if "not read" in ln] == [], out
```

In `Test_verdicts_of`, beside
`test_reads_the_label_exactly_and_names_a_line_that_opens_like_it`:

```python
    def test_names_no_verdict_line_inside_a_fence(self):
        """The guarantee's net reads outside fences too."""
        text = guarantee("abc1234", "sealed") + (
            "\n" + "`" * 3 + "markdown\n**Verdict:** withheld\n" + "`" * 3 + "\n"
        )
        assert chain.verdicts_of(reader, text)[-1][1] == "Verdict: sealed"
        assert chain.unread_verdicts(reader, text, "g.md") == []
```

Each case is to be seen red against its mutant above before it is
committed (contract rule 15). This round ran neither snippet; it ran the
same two assertions over `unread_lines` and `unread_verdicts` directly,
which passed against the code as it stands (`## Probes`).

answer:

## Confirmations

confirms: round-2#1
The close holds. `5db4f69f` touched `frame/design.md` alone (executed,
`git show --stat`). The *Grounding* row at `:8`, *Scope* item 1 at `:44`
and the bold rule of the `add` item at `:259-262` now say "names as not
read a line or a file that looks like one of its form's and is not one"
and give the judgment to the agent that reads the text. That is what the
core says at `skills/core/SKILL.md:123-126` (read).

confirms: none
The first five scenarios each have a case, and each case is red against
the checker before the phase. This round put `chain_check.py` from
`6dfffd4d` into its clone and ran the five cases: all five failed
(executed). The first failed on "a label in another spelling" at the
heading, the misspelt guarantee case exited 0, the round record case got
the near-miss refusal, the grammar case stopped on the missing
`Old spelling` table, and the fourth failed on the refusal at the line
holding the old spelling. That matches the crafter's *Seen red*
paragraph. At `c9939cad` the module passed, 258 cases (executed).

confirms: none
Departure a holds. The crafter claimed that a net derived from the labels
does not name `refixes:`, and that a net of any word before a colon named
20 prose lines over 19 records. This round ran `unread_lines` over the 19
round records under `seal/threads/` at `c9939cad`: it named 0 lines
(executed). So the label-derived net is quiet on real records. Naming
the old spelling would need the spelling list that *Scope* item 5 and
`## Removes` remove, and the core forbids that list (`skills/core/SKILL.md:123-126`).
The fold `c9939cad` states the departure in the fourth scenario
(`frame/design.md:80`) and in probe C (`:32`), and no other frame line
says the line is named (executed, `git grep -n -i` for "refixes", "old
spelling" and "fix of a fix" over the frame). The case at
`tests/skills/test_chain_check.py:1575` pins that the line is not named.

confirms: none
Departure b is the frame's own decision. `frame/plan.md` A2 rejects
removing the nets because a bold withheld verdict beside a plain sealed
one "is silent" without them, and keeps them as reports. The
guarantee's rule change says a guarantee "with no `Verdict:` line, or with
two, is refused naming the file" (`frame/design.md:216`), counting only
exact lines. `verdicts_of` returns the exact line only
(`chain_check.py:1935-1946`), and the case at
`tests/skills/test_chain_check.py:2454` pins both the one verdict and the
named line (read). The stamp reads through `verdicts_of` unchanged:
`tests/skills/test_seal_stamp.py` and
`tests/behaviour/test_the_sealer_guarantees.py` passed, 174 cases
(executed).

confirms: none
Departure c follows from *Scope* item 5, "`Verdict:` at the start of a
line exactly". `verdicts_of` skips a line whose raw text opens with
whitespace (`chain_check.py:1944`), and the guarantee holding only an
indented line is refused at line 0 as "0 `Verdict:` lines", with the line
named; the case is parametrised over the tab and the four-space indent
(`tests/skills/test_chain_check.py:2720-2742`, read). A line that opens
with `Verdict:` exactly and holds no shape is still refused at its line
(`NEAR_MISSES`, read).

confirms: none
The notice form holds what the plan asks. `main` prints every entry of
`unread` with the shared reader's `annotate("notice", ...)`, before the
refusals, and the exit code is computed from `problems` alone
(`chain_check.py:2381`, `:2403-2407`, read). The case at
`tests/skills/test_chain_check.py:3496` pins the plain line, the
`::notice` line under `GITHUB_ACTIONS` and the exit code beside each
(read). How GitHub renders it stays with the orchestrator, as `gaps.md`
says.

confirms: none
The second scenario holds: `rounds_listed` names every tracked name under
`trail/rounds/` that `routing.round_number` does not read, at line 0, and
the case at `tests/skills/test_chain_check.py:3552` pins the one line and
the unchanged exit (read). It lists regular files directly in the
directory, by `tracked_files` and `worktree_files`, so a subdirectory and
a symbolic link there are neither read nor named. That is how the readers
listed records before this phase, and this round counts it as a limit, not
a finding.

confirms: none
The fifth scenario and the `## Removes` rows for the loader hold.
`OLD_COLUMNS`, `old_spelling`, `OLD_SPELLINGS`, `misspelt`,
`spelt_otherwise` and `MEANT_VERDICT` are gone from the tree outside the
records, and no caller of `grammar` reads a second value (executed,
`git grep -n -E` over the names). `original_of` counts the exact label
only (`chain_check.py:1857`, read). The two changed files pass
`ruff check` and `ruff format --check` (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and `seal gate` over the branch, labelled `unverified` in `gaps.md` | the branch at `c9939cad` | the orchestrator, by `seal gate --base release/v0.26.0 --record` after the rounds settle |
| How GitHub renders the `::notice` `not read:` lines, including one at line 0 | `skills/code-review/scripts/chain_check.py:2403-2404` | the orchestrator, at the first CI run of the pull request |
| The crafter's `seal mutate` run (8 of 8 red) and its 31-module boundary run (2,546 passed), not re-run here | `tests/skills/test_chain_check.py` and the modules the crafter named | the orchestrator's broad run |
| Departure e: a near `## Rule Changes` heading has no path into `unread` yet, since `rule_changes_of` returns refusals only | `skills/code-review/scripts/chain_check.py:774` | the round that reads phase 3 |
| Phases 3 to 5 and their Scope items, outside this round by `frame/plan.md` *Phases* | `frame/design.md` *Scope* items 6 to 14 | the rounds that read those phases |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py -q`, in a `git clone --no-local` at `c9939cad` under the scratchpad | 258 passed, exit 0 |
| `bin/test tests/skills/test_seal_stamp.py tests/behaviour/test_the_sealer_guarantees.py -q`, same clone | 174 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over the two changed files, same clone | exit 0 and exit 0 |
| `python3 -I -c` running `chain_check.unread_lines` over every `seal/threads/*/trail/rounds/*.md`, same clone | 19 records, 0 lines named |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.26.0 --root .`, same clone | exit 0, unseen pull request; three notices: round 2's `target:` behind HEAD, no `trail/gate.md`, no `guarantee.md`; no `not read:` line |
| The five scenario cases run by node id with `chain_check.py` checked out from `6dfffd4d` in the clone, then restored | 5 failed, each on the old reading (Confirmations) |
| `bin/test` over the module, `test_seal_stamp.py` and `test_the_sealer_guarantees.py` with `reader.readable` replaced by `reader.gfm_lines` at `chain_check.py:788` and `:1957`, then restored | 432 passed: neither mutant caught (finding 2); the `.splitlines()` form failed `test_census` alone |
| `tests/skills/test_tmp_round3_probe.py`, two cases, run once by node id with `.venv/bin/python -m pytest -p no:xdist -q -s`, then deleted | a `straight to the PR` guarantee with `Original: <sha>` alone: exit 1, the refusal at line 0, no `not read:` line (finding 1); fenced `Verdict: open` and `**Verdict:** withheld` named by neither reader at `c9939cad`, passed |
| `bin/seal layout --pairs`, same clone | no pair names a case of `tests/skills/test_chain_check.py` |
