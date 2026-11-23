# Review round 2: 1795432997-cases-copy-facts-whose-source-is-code

```seal
target: be1be2f2e, fixes f6989a83a..be1be2f2e
```

This is a verifying round. Its code bound is `git diff
f6989a83a..be1be2f2e`, which holds the round-1 record (`614d95982`), the
framer's fold and the orchestrator's corrections (`3a8e2d209`), the fix
(`a9a431f84`), a changelog correction (`7f4158348`) and the close blocks
(`be1be2f2e`). The code the range changes is two test modules,
`tests/evals/test_behaviour.py` and the docstring of
`tests/text/test_a_moved_rule_leaves_its_definition.py`. The round read the
work item's records whole at `be1be2f2e`: `routing.md`, the three frame
files, `gaps.md`, `changelog.md`, `pr.md`, the three phase records and
`trail/rounds/round-1.md`. `seal/parity.json` is not declared, and
`seal/config.json` names English for both language keys, so no parity
comparison and no `pr.<lang>.md` is owed. The round worked in a `git clone
--no-local` of the branch at
`<scratchpad>/1795432997-cases-copy-facts-whose-source-is-code/round-2/clone`.

**What was carried from round 1, not re-established.** Three facts were
carried as coordinates. The generator writes its one Bash bound with an
`input_match` (`evals/scripts/rule_cases.py:1012`). No committed grader
holds a doubled quote, by round 1's `git grep`. The removed
`Test_grader_from::test_accepts_what_behaviour_writes_field_for_field` read
the writer as well as the reader, by round 1's read of the base. Every
verdict below was reached here.

**The orchestrator's answer to round 1's *Not judged* row stands on its
substance.** Round 1 asked whether the eval runner reads a `tool_used`
grader with no `input_match` as every call of its tool. The third row of
`frame/plan.md` *Judgments of the run* keeps
`tests/behaviour/test_evals_layout.py#sealer_grade_gaps` as phase 3 wrote
it, so the runner's reading is not needed. Its facts hold. No tracked file
outside `evals/behaviour/` and `seal/threads/` states what the runner does
with an absent `input_match`: `git grep -n input_match` there prints only
the generator's and the layout module's code lines (executed). Each of the
16 committed graders whose `tool` is `Bash` carries an `input_match`, out
of 172 graders parsed (executed). Phase 3 took out the guard on the key's
presence after it survived its break (`trail/phases/phase-3.md:13`, read). A
grader that bounds every Bash call is a form no writer produces, and the
case fails on it rather than passing. One cell of the row cites round 1 for
a read round 1 did not make; finding 1.

**What else the range states, read against the target.** The fold of
finding 1 holds in every record that states it: `frame/design.md` *Scope*
item 10, S11 and the *Removes* row; `frame/plan.md` A15a to A15c and the
second judgment row; `frame/questions.md:16`; `changelog.md:15`; and
`trail/phases/phase-3.md:16` (read). Each of the four quotes of `pr.md`
stands word for word at its coordinate, the corrected title row at
`frame/plan.md:81` among them (read). The *Phases* row of phase 3 still
names `730d99f79` as its last commit, while *Scope* item 10 as it now stands
was finished by `a9a431f84`. That row records the phase's own commits, and
`trail/phases/phase-3.md:16` and A15a name the fix, so the round reads it as
true of the phase and opens no finding. `git grep` outside `seal/threads/`
for the old fact's spellings, `census over the script`, `no class`, `held by
the cases of the scripts` and `writers are held`, finds no statement of it
(executed); that is a sample by contract rule 12, since it searches
spellings.

**Gaps that are not findings.** The module docstring of
`tests/evals/test_behaviour.py:3-6` says "a writer that quotes a value the
parser reads otherwise fails here", while the case exercises a quote, a
comma, braces and an integer; A15a's failure scenario states that limit
(`frame/plan.md:50`). The close of round 1's finding 1 says each red was
shown "through `seal mutate` after the commit", where contract rule 15 asks
for the red before the case is committed. The case is the one a pre-commit
red would have shown, and this round showed both reds again (executed), so
no shipped fact rests on the order.

## Findings

### 1. The answer to round 1's *Not judged* row cites round 1 for a read of every grader that round 1 did not make

```seal
severity: should
location: `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/frame/plan.md:83`
evidence: read `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/trail/rounds/round-1.md:49-57`, `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/trail/rounds/round-1.md:268`, `tests/behaviour/test_evals_layout.py:121-137`; executed `git grep -n "read every grader"` over the work item's tracked records, which printed `frame/plan.md:83` alone; executed a parse of every `evals/behaviour/**/graders/*.md` through `tests/workflows.py#front_matter` in the clone, which printed `graders 172 bash 16 bash without input_match 0`
regression: round-1
```

Why it matters: the unit is the third row of `frame/plan.md` *Judgments of
the run*, added at `3a8e2d209` to answer round 1's *Not judged* row. The
frame chose at A13a that a sealer grader's `input_match` is read as a
regular expression that must find `seal gate --base` (`frame/design.md`
*Scope* item 9). The row keeps that reading and grounds it on "No committed
sealer grader lacks `input_match` (round 1 read every grader)". The defect
came from the parenthetical. Round 1 read the generator's one Bash bound,
`evals/scripts/rule_cases.py:1012`, and said so (`round-1.md:53-54`). It
read no grader for the key. The sealer and the settle read this row as
grounds, and the parenthetical tells them a read was made that was not.
The fact itself holds: this round parsed all 172 committed graders, and the
16 whose `tool` is `Bash` each carry an `input_match` (executed).

The next clause of the same cell, "where one is added the case stops on a
`KeyError` that names the key", is also wider than the code. The case reads
its graders in `glob` order inside `any(...)`
(`tests/behaviour/test_evals_layout.py:121-137`), and `any` stops at the
first grader that satisfies it. So a grader with no `input_match` that is
read after a grader that bounds the run raises nothing. The `KeyError` is
certain only in a case whose other graders bound nothing, which is the
case the answer is about. The snippet below rewrites both clauses and
leaves the rest of the row as it stands. No other record states either
clause: `git grep -n "read every grader"` in the work item prints only this
row (executed).

```markdown
| 2026-11-23 | Round 1's *Not judged* row on a `tool_used` grader with no `input_match` is answered by leaving `tests/behaviour/test_evals_layout.py#sealer_grade_gaps` as phase 3 wrote it | No committed sealer grader lacks `input_match`: round 1 read the generator's one Bash bound (`evals/scripts/rule_cases.py:1012`), and round 2 parsed the 172 committed graders through `tests/workflows.py#front_matter`, of which each of the 16 whose `tool` is `Bash` carries one (executed). Where one is added to a case whose other graders bound nothing, the case stops on a `KeyError` that names the key, a loud failure rather than a silent pass; a default such as `g.get("input_match", "")` would encode a reading of the runner this repository's documents do not state, and phase 3 removed the guard that read the key's presence because no fixture could make it red | `trail/rounds/round-1.md` *Not judged*; `trail/rounds/round-2.md`; `trail/phases/phase-3.md`; `skills/core/SKILL.md` *The rule a mechanism is kept against* |
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `tests/evals/test_behaviour.py:22-42` holds `Test_report_regex`
as round 1's snippet gave it, with a docstring on the refusal case. The
round trip writes a path of a quote, a comma and braces through
`report_regex` and compares every field `front_matter` reads back. The
module passes (executed: 3 passed). With `evals/scripts/behaviour.py#squote`
edited to stop doubling a quote, the round trip fails on
`yaml.parser.ParserError: while parsing a flow mapping` (executed). With the
`kind not in KINDS` guard of `grader` taken out, the refusal case fails on
`DID NOT RAISE ValueError`, and it is the one case of `tests/evals` and the
layout module that fails, so no other case already held the guard
(executed: 1 failed, 199 passed). The base's `tests/evals/test_behaviour.py`
held no refusal of a kind either (read), so the case adds what its group
lacked, and `bin/seal layout --pairs` names no pair in the file (executed).
The docstring's claim that `noninferiority.py` reads the kind from the
prefix holds at `evals/scripts/noninferiority.py:470-472` (read). The
changelog entry at `changelog.md:15` and `trail/phases/phase-3.md:16` state
the class and the false premise as the code shows them (read).

```seal
confirms: round-1#2
```
What holds: the moved-rule docstring now ends its first paragraph with "the
comment over `WINDOW` holds the measurement that chose it"
(`tests/text/test_a_moved_rule_leaves_its_definition.py:8-9`, read). The
paste test's docstring and `tests/skills/test_passages.py:6-8` still cite
the comment, so the three docstrings that *Scope* item 8, A10a and
`changelog.md:6` name each cite it (read). The title row at
`frame/plan.md:81` counts two functions and a constant, and `pr.md:4` quotes
it word for word (read). The diff of `evals/scripts/behaviour.py` against
the base removes `scalar`, `grader_from` and `SCALAR` and nothing else that
row would have to count (read in round 1's range, unchanged since).

What matched: the two changed Python files pass `uvx ruff check` and `uvx
ruff format --check`, and the modules the fixes reach pass in the clone
(executed). `git status --short` in the clone printed nothing after the
probes were reverted (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `be1be2f2e`; the fix pass and this round ran narrow modules only, and the suite stays labelled `unverified` | the whole tree | the orchestrator's broad run, after the review rounds settle, and the sealer's spawn after it |

## Probes

| Command | Result |
|---|---|
| `bin/test -q -p no:xdist tests/evals/test_behaviour.py`, in the clone | 3 passed |
| the same, with `evals/scripts/behaviour.py#squote` edited to return `"'" + text + "'"` | 1 failed, 2 passed: the round trip fails on a `ParserError` in the flow map; the edit was reverted |
| the same, with the `kind not in KINDS` guard of `grader` taken out | 1 failed, 2 passed: `DID NOT RAISE ValueError` |
| `bin/test -q -p no:xdist tests/evals tests/behaviour/test_evals_layout.py`, with the guard still taken out | 1 failed, 199 passed: the refusal case alone; the guard was put back |
| `bin/test -q -p no:xdist tests/text/test_a_moved_rule_leaves_its_definition.py tests/evals tests/behaviour/test_evals_layout.py tests/test_workflows.py`, after both reverts | 221 passed |
| `bin/seal layout --pairs tests/evals/test_behaviour.py`; `bin/seal layout --check tests/evals/test_behaviour.py` | 0 pairs; 0 refused, with reports that `squote` and `write_case` have no class |
| `uvx ruff check` and `uvx ruff format --check` over `tests/evals/test_behaviour.py` and `tests/text/test_a_moved_rule_leaves_its_definition.py` | exit 0 each |
| a Python run in the clone that parses every `evals/behaviour/**/graders/*.md` through `tests/workflows.py#front_matter` and counts the graders whose `tool` is `Bash` without `input_match` | `graders 172 bash 16 bash without input_match 0` |
| `git grep -n input_match -- . ':!evals/behaviour' ':!seal/threads'` | six lines of `evals/scripts/`, four of `tests/behaviour/test_evals_layout.py`, no document |
