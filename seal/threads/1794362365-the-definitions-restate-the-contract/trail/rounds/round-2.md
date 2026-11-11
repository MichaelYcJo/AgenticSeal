# Review round 2: 1794362365-the-definitions-restate-the-contract

```seal
target: 83d77b301, fixes b67e42ea5..83d77b301
```

This round verifies round 1's four findings and reads every commit after
the round's record, `b67e42ea5..83d77b301`, against `release/v0.37.3` at
`9c6907942`. It ran in a `git clone --no-local` at `83d77b301` under
`<scratchpad>/1794362365-the-definitions-restate-the-contract/round-2/clone`.
The work item's records were each read whole at `83d77b301`: `routing.md`,
the three frame files, `gaps.md`, `changelog.md`, `pr.md` and
`trail/phases/phase-1.md`. No `pr.<lang>.md` stands or is owed, since
`seal/config.json` names English for both language keys.

Carried from round 1 and not re-established: where each statement of the
scratch rule stands (round 1, *Confirmations*), and the census probe's
method, re-run below from round 1's `## Probes` row. Every verdict below
was reached on the tree at `83d77b301`.

The owner's decision of 2026-11-11 was read where the orchestrator's
prompt named it: issue #1503's comment by its owner says the orchestrator
removes the work item's scratch directory once, after the pull request
opens, in one `rm -rf` with no variable in its path, and that both
conditions of *Done when* still hold for agents (executed: `gh issue view
1503 --comments`). `frame/plan.md:74` records the same decision. So the
removal T22 adds is judged against the issue as amended, and
*Alternatives considered* row 1's "It meets both issues' *Done when*"
holds.

## Findings

### 1. No case holds the orchestrator's one removal to the work item's directory

```seal
severity: should
location: `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `skills/implement/orchestration.md:46-50`
evidence: executed `git show 9c6907942:tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py`, `git grep -n -F "removes nothing else of the scratchpad" -- tests`; read `skills/implement/orchestration.md:21-53`, `tests/text/test_a_parallel_agent_names_its_scratch_after_the_work_item.py:1-208`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/design.md:266`, `seal/threads/1794362365-the-definitions-restate-the-contract/frame/plan.md:21`
regression: round-1
```

Why it matters: the unit is step 2's new sentence in
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket* (`:46-50`). It tells the orchestrator to remove
`<scratchpad>/<work-item-id>/` in one `rm -rf` and to remove "nothing else
of the scratchpad". That last clause is the guard of #1445, where a removal
took the whole scratchpad with every other agent's files. At `9c6907942`
the same guard stood in rule 21, and
`test_rule_21_removes_the_agents_directory_and_never_the_scratchpad`
pinned it: the directory `<scratchpad>/<work-item-id>/` and "never names
the scratchpad itself". *Scope* item 11 removed that case because the
removal it pinned had gone. The fix pass brought a removal back, with the
same guard, and no case holds it (executed: `git grep -n -F "removes
nothing else of the scratchpad" -- tests` prints nothing). The frame's T22
says what the sentence holds and *Removes* (`frame/design.md:266`) still
gives the old case's reason as gone; the fix pass built T22 as written, and
the gap comes from the frame removing the case before T22 brought the
removal back. `frame/plan.md:21` names the wrong path as the failure that
breaks this in six months, and says no check reads the command. The
sentence the orchestrator copies the path from is the one thing a case can
read, and a later edit that drops "nothing else" or shortens the path
leaves every test green.

The case belongs in the scratch module beside the cases that hold each
agent's directory. It is shown red with the clause deleted, as contract
rule 15 asks, and `frame/design.md` *Removes*' last row then names the old
case's fact as moved here, which is the orchestrator's to fold.

```python
IMPLEMENT_ORCH = os.path.join(ROOT, "skills", "implement", "orchestration.md")
WORK_ITEM_HOME = "<scratchpad>/<work-item-id>/"


def test_the_orchestrators_one_removal_names_the_work_items_directory():
    """#1445 S6, #1503. The one removal left is the orchestrator's, once the
    pull request is open. A removal that named the scratchpad took every
    agent's files with it in the 0.37.0 run, so the sentence names the work
    item's directory, written out, and says nothing else of the scratchpad
    goes."""
    where = section(IMPLEMENT_ORCH, "Orchestrator: the order inside a ticket")
    assert f"`{WORK_ITEM_HOME}`, in one `rm -rf`" in where, (
        "the orchestrator's removal does not name the work item's directory "
        f"as `{WORK_ITEM_HOME}`, so the scratchpad reads as the directory "
        "it removes"
    )
    assert "removes nothing else of the scratchpad" in where, (
        "the orchestrator's removal does not say it removes nothing else of "
        "the scratchpad, which every agent of the session shares"
    )
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `agents/tracer.md:66-67` now reads "a probe you do run leaves
nothing outside your scratch directory (rule 7)", which states rule 7's
scope at HEAD (`skills/agent-contract/SKILL.md:90-99`). The case at
`tests/behaviour/test_a_probe_that_commits_says_so.py:76-80` pins
"outside your scratch directory (rule 7)", and the docstring at `:9-10`
follows. Claimed seen red with the old sentence put back; read: the
assertion's substring stands nowhere in the old sentence, so the case fails
on it. The module passes (executed). `frame/design.md` *Scope* item 17, S11
and a *Removes* row now name the tracer and its case (read).

```seal
confirms: round-1#2
```
What holds: rule 7's sixth sentence opens "Outside your scratch directory,
what the probe made for ITSELF is what goes"
(`skills/agent-contract/SKILL.md:95-96`), so a clone or a virtual
environment a probe made inside the scratch directory is kept by the third
sentence alone. Rule 17's heading reads "Name your scratch for the work
item, keep it, stop only what you started" (`:183`), 78 columns, and
`tests/behaviour/test_docs_line_wrap.py` passes (executed). Both match the
folded T1 and T2 (read).

```seal
confirms: round-1#3
```
What holds: `frame/plan.md:30` now names "a framer, a proofer, a sealer
and a tracer" and sends each figure to *Operational impact*, whose figures
match `wc -c` at `83d77b301` (executed: crafter 32,343 B, framer 36,952 B,
proofer 32,891 B, sealer 33,186 B, tracer 25,046 B from the core's 9,322 B,
the contract's 12,806 B and each definition). `pr.md:2` quotes the row
word for word with whitespace collapsed (executed).

```seal
confirms: round-1#4
```
What holds: `frame/design.md` *Rule changes* holds a `change` of
`docs/forms/the-round-record.md` *The round record*, and its `from` stands
word for word, with whitespace collapsed, in that file (executed). The
`to` keeps the sentence's action and gives a probe in a clone its
place.

What matched: the sizes and the census the fix pass's records carry. `wc
-c` at `83d77b301` gives the four definitions 46,860 B, the contract
12,806 B and the tracer 2,918 B, as `changelog.md:5` and `frame/design.md`
G17 state, inside S1's 47,310 B and S9's 12,864 B (executed). The census
probe of round 1, run again over the clone, reads crafter 254 of 1,592,
framer 140 of 2,369, proofer 141 of 1,695, sealer 81 of 1,727, tracer 26
of 445, the contract 90 of 2,138, the core 133 of 1,595, all 865 of
11,561, every cell as G18 and `changelog.md:5` give it (executed).

What matched: `pr.md`. Each of its seven quotes stands word for word, with
whitespace collapsed, in `frame/plan.md` at the coordinate it names,
quote 5 in the *Judgments of the run* row of the owner's decision
(executed).

What matched: the other new texts. The README sentences
(`README.md:377-379`, `README.ko.md:374-376`) state T24 and the owner's
decision, and rule 17's body says "No agent removes" as T2 now gives it
(read). The scratch module's docstrings cite
`skills/implement/orchestration.md` *Orchestrator: the order inside a
ticket*, which stands as a heading at `:21`, and that file is in no
agent's `skills:` list (read). `gaps.md:8` marks Q1's row `closed` with its
answer, and keeps the row (read).

What matched: the narrow modules. The scratch module,
`tests/behaviour/test_a_probe_that_commits_says_so.py`,
`tests/behaviour/test_docs_line_wrap.py`,
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` and
`tests/text/test_a_moved_rule_leaves_its_definition.py` give 273 passed in
the clone at `83d77b301` (executed). The fix pass's claim of a green
`tests/text tests/behaviour` run at `59d730708` was not re-run here.

One gap holds no finding. `skills/code-review/orchestration.md:347-357`
keeps a repair path after the pull request opens: a verifying round, the
broad run and the sealer again. Their directories are made after the one
removal and stay, which the owner's "once" accepts and which
`frame/plan.md` *Operational impact* does not mention. *Not judged* names
it for the owner.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, labelled `unverified` for the orchestrator, and the label is honest | `seal/threads/1794362365-the-definitions-restate-the-contract/gaps.md:7` | the orchestrator, by `seal gate --record` |
| Whether a repair after the pull request opens, which makes new scratch directories after the one removal, leaves them by design or owes a second removal | `skills/implement/orchestration.md:46-50`, `skills/code-review/orchestration.md:347-357` | the owner |
| Whether agents under the released text still write an `rm`, and take `-2` where their directory stands | `seal/threads/1794362365-the-definitions-restate-the-contract/frame/questions.md:20` | a measurement, as Q2 states |
| The crafter's eval cases, not run | `seal/threads/1794362365-the-definitions-restate-the-contract/gaps.md:10` | the owner, where the release runs them |

## Probes

| Command | Result |
|---|---|
| `python3 -I round-1/test_tmp_census.py round-2/clone 83d77b301`, from `<scratchpad>/1794362365-the-definitions-restate-the-contract/`, the census of round 1's `## Probes` row | crafter 254 of 1592, framer 140 of 2369, proofer 141 of 1695, sealer 81 of 1727, tracer 26 of 445, contract 90 of 2138, core 133 of 1595, all 865 of 11561 |
| `bin/test` over the five modules named under *Confirmations*, `-q`, one command in the clone | 273 passed, exit 0 |
