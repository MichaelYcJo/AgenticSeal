# Review round 2: 1795339519-the-thread-layout-has-one-spelling

```seal
target: a66fe67f, fixes 6af655c2..a66fe67f
```

This is a verifying round over `git diff 6af655c2..a66fe67f`. The range holds the code fix `8fa01124`, the records fix `f8c60526` and the close blocks of `a66fe67f`. The code review stays inside that diff. Beside it, this round read `routing.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/rounds/round-1.md` whole at `a66fe67f`. The work item has no `frame/` and no `trail/phases/`, and `Commit and pull request language` is English, so no `pr.<lang>.md` is owed. No `seal/parity.json` is declared.

Facts carried from round 1 and not established again: the issue's table and its coordinates, the reading of the first *Done when* item, that `seal.py:193-196` loads `lib/config.py`, `lib/gitcmd.py`, `lib/optin.py` and `lib/core.py` at import, that `sibling_module` lets the loader's exit through (`broad_gate.py:214-215`), and the count reconciliation of the twelve test files behind the 1983 of `gaps.md:10`. Round 1's three `## Not judged` rows stay with the orchestrator and are not written again.

## Findings

### 1. The comment in `broad_gate.py#rounds_rows` still says a label never stops a run that passed, and the line above it now stops one where `lib/routing.py` is absent

```seal
severity: should
location: `skills/verify/scripts/broad_gate.py:1773-1774`, `tests/skills/test_broad_gate.py:1612-1614`
evidence: executed `python3 -I test_tmp_lib_absent.py <clone> <scratch>` at a66fe67f (the `## Probes` row) and `git grep -n -i "label never stops"` at a66fe67f; read `skills/verify/scripts/broad_gate.py:1762-1790`, `:1900-1913`, `tests/skills/test_broad_gate.py:1600-1645`, `lib/lines.py:478-490`
reopens: round-1#3
```

Why the close of round 1's finding 3 does not hold: that finding said what the changelog and a docstring tell a reader about an absent `lib/` module. Its grounds quoted "a run never stops on a label" and said the sentence "now reads as covering this case too, and it does not". The fix bounded that one docstring, at `broad_gate.py:312-317`, and wrote both loads into `changelog.md:3`. Both of those parts hold. The same fact stands in a second sentence, in `rounds_rows`, and the close left it. The round 1 snippet was scoped to `plugin_version` alone. It did not name this sentence, so the fix pass did not reach it either.

Why it matters: `broad_gate.py:1771` now reads `sibling_module(ROUTING).rounds(item)`, where the base listed the records itself through `round_records`. The comment two lines below says "A label never stops a run that passed, so an absent check is said here and the run goes on." The panel calls `rounds_rows` after the suite's counts are read (`broad_gate.py:1903-1912`), so it is the label of a run that has finished. The probe points the loader at a `lib/` without `routing.py` and calls `rounds_rows` on an empty work item. It ends with the loader's `cannot read .../lib/routing.py` sentence and `SystemExit 2`. `changelog.md:3` states that exit. The comment states the opposite, at the line a person editing this function reads first. The test docstring at `tests/skills/test_broad_gate.py:1612` opens with the same unbounded sentence. The case below it, at `:1637-1638`, already says that `lib/routing.py` is the tree's and only the check is absent. The other statement, at `lib/lines.py:485`, is about a table hidden by a fence nobody closed, in a whole plugin. It stays true, so the fix leaves it.

```python
# skills/verify/scripts/broad_gate.py:1771-1774, in rounds_rows
    records = sibling_module(ROUTING).rounds(item)
    rows = [("rounds", str(len(records)))]
    # The deferred row beneath never stops a run that passed, so an absent
    # check is said here and the run goes on. `lib/routing.py`, which lists
    # the records above, loads as every other `lib/` module does: absent, it
    # is the loader's sentence and exit 2.

# tests/skills/test_broad_gate.py:1612-1614, the docstring of
# test_refuses_to_stop_a_run_where_the_check_will_not_load
        """The deferred row never stops a run that passed: a check that raises
        or exits while it loads leaves the count alone beneath it. An absent
        check is `lib/sibling.py#Absent`, which the case below holds."""
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the six lines read their module at `a66fe67f`. `settle.py:1732` builds `CITATION_RE` from `re.escape(WORK_ITEMS)`, and `settle.py:1778` tests `f"{WORK_ITEMS}/"`. `WORK_ITEMS` is bound at module scope at `settle.py:229`, and `re.escape("threads")` is `threads`, so the pattern is the base's. `session_cost.py:3078` uses the `routing` that `:3066` binds. `session_cost.py:3140-3141` binds `lib_module("routing").FILENAME` as `declaration`. The loop above it does bind `name` (`:3135`), as the answer says. Both `chain_check.py:1104-1105` and `:1111-1112` read `routing.FILENAME` from `frame`'s parameter, which `:2162` loads as `lib/routing.py`. Each split f-string joins to the old text, "`'s mark ` + `says`" and "`'s ` + `foot says`" (read). `tests/skills/test_chain_check.py:1429` still spells the old message and passes, so the output is unchanged (executed, the narrow run below). The fix pass's walk prints 46 constants at `a66fe67f`, and none of them is a path join or a read (executed, `## Probes`). `uvx ruff check` and `uvx ruff format --check` over the four changed scripts exit 0 (executed).

```seal
confirms: round-1#2
```
What holds: `gaps.md:14` now states the walk the fix pass ran, and the walk does what the paragraph says. I ran `session/literals.py` at `a66fe67f`, and it printed 46 constants. I also ran a wider walk of my own. It keeps every non-docstring string constant in which a name stands bounded by characters that are not letters, digits, `_` or `-`, so a name followed by `.` or `#` is kept too. It kept the same 46 constants and none that the token split misses (executed, `## Probes`). I sorted all 46 into the memo's four kinds by reading each one at its line. There are 36 message or help sentences, among them the `round-{n}.md` of `chain_check.py:936` and the `round-N.md` of `:310` and `:1497`. Three of them, at `chain_check.py:332`, `:936` and `:954`, also hold a finding's coordinate. There are 5 panel or table labels, at `broad_gate.py:1772`, `seal_stamp.py:1069`, `seal_stamp.py:1488` (`SAMPLE_ROWS`), `pr_body.py:279` and `.github/scripts/finding_counts.py:71`. There are 4 `found["threads"]` keys, at `settle.py:1561`, `:1802`, `:1943` and `:2020`. One constant is a coordinate part alone, the `f"round-{n}"` of `chain_check.py:923`. At `settle.py:1943` the path is joined from the key's value, `specs`, and never from the key, so the memo's "No script reads or joins a path through any of them" holds (read). No tracked non-Python file under `bin/`, `hooks/` or `.github/` spells a thread's file name outside a comment or a template (executed, `git grep`).

```seal
confirms: round-1#4
```
What holds: `routing.md:19` now says "the diff came to nine scripts, no `lib/` module and those cases". `git diff --name-only 0eca6e77..a66fe67f` lists nine scripts under `skills/` and nothing under `lib/` (executed). "The issue named seven scripts" is the issue's own count, in its title and its table (executed, `gh issue view 1567`). `routing.md:17` stays true.

What matched: `gaps.md:10` claims a narrow run after the fix pass with 2041 passed and 10 skipped. I ran `bin/test -q tests/text tests/behaviour tests/skills/test_settle.py tests/skills/test_session_cost.py tests/skills/test_chain_check.py tests/skills/test_broad_gate.py` at `a66fe67f`. It exited 0 with 2041 passed and 10 skipped (executed). The twelve files the memo now names for the build's 1983 are the files of round 1's reconciliation, `test_optin.py` left out and `test_pr_body.py` added (read). The broad gate has not run. It stays the orchestrator's, so the memo's "the broad gate runs before the seal" is an honest label.

What matched: `changelog.md:3`'s added clause, that a copy without `lib/core.py` ends every `seal` command at exit 2, stands on `seal.py:196` (carried) and on the probe, where `plugin_version` ends at `SystemExit 2` (executed). "as each already did for the other modules under `lib/`" holds: `seal.py:193-195` loads three other modules the same way (read). The changelog's three list items have no `pr.<lang>.md` to render them in. Both `pr.md` quotes stand word for word at `routing.md:15` and `gaps.md:16`, which the fix diff did not touch (read).

A gap in a docstring, which is no finding: the fix pass glosses SPECS as `WORK_ITEMS` at `settle.py:1767`, while twelve other docstrings in the same file still gloss it as `threads`, for example `:293` and `:1747`. SPECS is `threads(home)`, `<root name>/threads` (`settle.py:283-289`), so neither gloss is wrong. A reader now meets two spellings of one gloss.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at a66fe67f, which no agent runs (contract rule 2) | `seal/config.json` `Broad gate` | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `python3 -I session/literals.py <clone>`, the fix pass's walk, at a66fe67f | 46 constants, sorted into the four kinds above |
| `python3 -I test_tmp_walk.py <clone>` at a66fe67f. The probe walks every non-docstring `ast.Constant` string in each tracked `.py` outside `lib/`, `tests/` and `evals/`. It keeps a constant in which one of the walk's seventeen names stands bounded by characters that are not letters, digits, `_` or `-`, or that holds `round-`, and it marks each kept constant that the token split would miss | 46 constants, none marked as missed by the token split |
| `python3 -I test_tmp_lib_absent.py <clone> <scratch>` at a66fe67f. The probe copies `lib/` without `core.py`, points `sibling.ROOT` at it and calls `broad_gate.plugin_version`. It then copies `lib/` without `routing.py`, points `sibling.ROOT` at that copy and calls `broad_gate.rounds_rows` on an empty directory | `plugin_version`: the loader's `cannot read .../lib/core.py` sentence and `SystemExit 2`. `rounds_rows`: the loader's `cannot read .../lib/routing.py` sentence and `SystemExit 2` |
| `bin/test -q tests/text tests/behaviour tests/skills/test_settle.py tests/skills/test_session_cost.py tests/skills/test_chain_check.py tests/skills/test_broad_gate.py` at a66fe67f | exit 0, 2041 passed, 10 skipped |
| `uvx ruff check` and `uvx ruff format --check` over `settle.py`, `session_cost.py`, `broad_gate.py` and `chain_check.py` | exit 0 and exit 0 |
