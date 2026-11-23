# Review round 1: 1795432997-cases-copy-facts-whose-source-is-code

```seal
target: f6989a83a against origin/release/v0.38.6
```

The round read the work item's own diff, `git diff
origin/release/v0.38.6...HEAD` with `origin/release/v0.38.6` at
`d7a6e3b31`, against the tree at `f6989a83a`. That tree includes the merge
`26ddbfd68`, which brought in #1597. Its case in
`tests/skills/test_chain_check.py` *Test_broad_gate* was read only for what
the frame's searches S1 and S2 find in it, and they find nothing. This is
the first round. No coordinate or verdict was carried from an earlier one,
and every fact below was established here. `seal/parity.json` is not
declared, so no parity comparison was owed. `seal/config.json` names
English for both language keys, so no `pr.<lang>.md` is owed and none
stands. The work item's records were each read whole at `f6989a83a`:
`routing.md`, the three frame files, `gaps.md`, `changelog.md`, `pr.md`
and the three phase records.

The round worked in a `git clone --no-local` of the branch under its
scratch directory, `<scratchpad>/1795432997-cases-copy-facts-whose-source-is-code/round-1/clone`.

**What the issue asks the round to judge.** The question was whether each
rewritten or removed case still holds its fact. Each removal *Removes*
names was read against the case the frame says holds it now:

| Removed | Claimed holder | What the round found |
|---|---|---|
| `test_the_contributor_has_a_procedure.py#test_the_check_can_fail` | `tests/test_conftest.py#Test_section` | holds: `test_refuses_a_longer_heading_that_begins_with_the_same_words` refuses a text without the heading (read `tests/test_conftest.py:284-287`) |
| the emptiness assertion of `test_chain_check.py#template_section` | `test_a_phase_hands_the_next_one_a_record.py#test_the_spec_template_carries_the_rule_changes_section_above_removes` | holds: `:122` asserts the same raw section empty, so the S3 parameter of `Test_rule_changes_read` still reads an empty section (read) |
| `test_review_axes.py#test_the_routing_section_holds_the_answers_and_the_shape` | the waiver module | holds for each fact G12 lists; the code-span spelling of `manual` is held by no case, which `trail/phases/phase-2.md` states (read) |
| the text read of `lib/routing.py` | the constants | holds: `AXES` is the reader's own tuples, so the parser accepts each answer by construction (read `tests/behaviour/test_waiver_decided_at_start.py:49-57`) |
| row 18 of `RULES` | no case, by design (A5a) | the number stands once, at `skills/code-review/orchestration.md:35` (executed: `git grep -n 806,241`) |
| `WRITING_RULE_CHECKS` | `seal rules --check` | holds: `tests/behaviour/test_this_repository_passes_its_own_checks.py:50` runs it over the tree (read) |
| the window cases | the paste test | holds: `skills/agent-contract/SKILL.md` and `agents/*.md` are in the paste test's corpus, no pair of them is exempt (`tests/text/test_no_passage_is_pasted_into_a_second_file.py:103`), and `words` reads at least every run the removed `copied` read; phase 2's probe, 90 caught of 90, is carried as the crafter's claim |
| the `Broad gate` refusal | none, by design (A14a) | holds as the frame states it |
| `Test_scalar`, `Test_grader_from` | `tests/workflows.py#front_matter` and its cases | holds for the reader. It does not hold for the writer the removed field-for-field case also read; finding 1 |

Each converted section reading was read against the old helper's stop
rule. The five changed readings `trail/phases/phase-1.md` lists are the
ones the stop rules predict, and the round found no other call whose old
helper stopped later than the next heading of its level or above. The
crafter's S9 probe is carried as a claim. The 42 changed test modules pass
in the clone (executed), and ruff's check and format check pass over the
46 changed Python files (executed). The frame's searches S1, S2 and S4 to
S8 print nothing at `f6989a83a` (executed).

**New failure paths.** Two are new and are read as acceptable. (1)
`tests/behaviour/test_evals_layout.py:134` reads `g["input_match"]` on
every `Bash` grader, so a sealer grader that bounds `Bash` without an
`input_match` raises `KeyError` rather than naming a gap. The generator
is the one writer of the sealer cases, and each Bash bound it writes
carries `input_match` (`evals/scripts/rule_cases.py:1012`, read). (2)
`tests/workflows.py#front_matter` refuses a file with no front matter
without naming the file, where `grader_from` named it. Both fail the case
rather than pass it, and both live in test code.

**Gaps that are not findings.** The three guards `gaps.md` *Not done*
names have no case that can fail them: the `max` comparison at
`tests/behaviour/test_evals_layout.py:361`, the `context` check at `:88`,
and the scaffold path at `:94`. Each read only committed cases before
this diff as well, and no *Scope* item asks for fixture cases, so the
round opens no finding for them.

## Findings

### 1. Nothing holds that the grader writer doubles a quote, since the case that read its output back went

```seal
severity: should
location: `tests/evals/test_behaviour.py:1-14`, `evals/scripts/behaviour.py:24-26`, `evals/scripts/behaviour.py:48-59`
evidence: executed `bin/test -q -p no:xdist tests/evals tests/behaviour/test_evals_layout.py tests/test_workflows.py` with `evals/scripts/behaviour.py#squote` edited to stop doubling a quote, 210 passed; executed `bin/test -q -p no:xdist tests/evals/test_tmp_writer_round_trip.py`, 2 passed; executed `git grep -l "''" -- 'evals/behaviour/**/graders/*.md'`, which printed nothing; read `git show origin/release/v0.38.6:tests/evals/test_behaviour.py`
```

Why it matters: the removed
`Test_grader_from::test_accepts_what_behaviour_writes_field_for_field`
read two units. It held the reader, `grader_from`, and it held the writer,
`report_regex` through `grader` and `squote`. It wrote a grader whose path
held a quote, a comma and braces, and compared every field read back. The
frame removes the reader because no code outside tests calls it
(`frame/design.md` G17, *Scope* item 10). The writer is another matter:
`evals/scripts/rule_cases.py` calls it, and so does every generator that
writes a case. `CONTRIBUTING.md` *The test layout* cuts a case only where
another case holds what it guarded.

`trail/phases/phase-3.md:16` claims that "`Test_parse` now holds that
spelling, and `test_every_sealer_case_grades_the_guarantee` parses the
`target` of every generated sealer grader". `tests/test_workflows.py:83`
holds the parser's reading of a hand-typed spelling, not the writer's
output. No committed grader holds a doubled quote (executed), so neither
the generated sealer cases nor their byte-for-byte comparison exercises
it. The round edited `squote` in the clone to write a quote undoubled, and
every eval module and both workflow modules stayed green (executed: 210
passed). So the writer can write a grader YAML cannot read, or reads with
another path, and no case notices. The new docstring of
`tests/evals/test_behaviour.py` says the writers "are held by the cases of
the scripts that call them", which this break shows is false for the
quoting.

The fix puts the round trip back through the suite's one reader. The
round's probe ran the first case below against the tree, and ran it again
with `squote` replaced by a writer that does not double a quote, which it
refused (executed). `seal layout --check` asks each class for a
`test_refuses_` case, so the class carries the kind refusal `grader`
raises. That refusal is shown red by the fix pass with the `kind not in
KINDS` guard removed (contract rule 15).

```python
"""`evals/scripts/behaviour.py`, the case writer the generators share.

`Test_report_regex` reads what the writer writes back through
`tests/workflows.py#front_matter`, the suite's one reader of a grader's
fields. The generators' output is held by the cases of the scripts that
call the writer: `tests/evals/test_rule_cases.py` and
`tests/evals/test_noninferiority.py`.
"""

import os

import pytest
from conftest import ROOT, census_case, load_module
from workflows import front_matter

TARGET = "evals/scripts/behaviour.py"

BEHAVIOUR = load_module(os.path.join(ROOT, *TARGET.split("/")), "behaviour_under_test")


class Test_report_regex:
    def test_accepts_a_path_and_a_pattern_holding_a_quote_field_for_field(self):
        """A quote doubled inside a single-quoted scalar, and a comma and
        braces inside a flow map's value, read back as written."""
        pattern = r"^location: .*it's(?:a|b)"
        _, text = BEHAVIOUR.report_regex(
            "truth", "q", "it's, {a}.md", pattern, "A defect.", "m", weight=2
        )
        assert front_matter(text) == {
            "type": "regex",
            "target": {"source": "file", "path": "it's, {a}.md"},
            "pattern": pattern,
            "flags": "m",
            "weight": "2",
        }

    def test_refuses_a_kind_outside_the_three(self):
        with pytest.raises(ValueError, match="is not one of"):
            BEHAVIOUR.report_regex("loose", "q", "a.md", "x", "A defect.")


test_census = census_case(TARGET)
```

The snippet changes the module's docstring with it. Two statements of the
old fact stand elsewhere, and the fix pass owes them too:
`changelog.md:15` says the file "loses their cases and keeps the census
over the script", and `frame/plan.md:50` (A15a) says it keeps its census
line "with no class". Each then names the new class.

### 2. Two sentences of the records say what the target does not hold

```seal
severity: should
location: `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/frame/design.md:39`, `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/frame/plan.md:39`, `tests/text/test_a_moved_rule_leaves_its_definition.py:5-8`, `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/frame/plan.md:80`, `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/pr.md:4`
evidence: read `tests/text/test_a_moved_rule_leaves_its_definition.py:1-25`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py:36-40`, `tests/skills/test_passages.py:6-9`, `evals/scripts/behaviour.py` in `git diff origin/release/v0.38.6...HEAD`, `seal/threads/1795432997-cases-copy-facts-whose-source-is-code/frame/plan.md:74`
```

Why it matters: the sealer reads these records against the tree, and
`pr.md` becomes the pull request's body. Each sentence below is
contradicted by the target.

First, *Scope* item 8 of `frame/design.md` says "The paste test's
docstring, `tests/skills/test_passages.py`'s docstring and the moved-rule
docstring cite that comment for it", the measurement over `WINDOW`.
`frame/plan.md` A10a says "three docstrings cite it". Two do
(`test_no_passage_is_pasted_into_a_second_file.py:38-40`,
`test_passages.py:7-8`). The moved-rule docstring names `WINDOW` and says
nothing of where its measurement stands (`:5-8`). No phase record names
this as a departure, and `changelog.md:6` already names only the two. The
fix that keeps the frame as written is one clause in the docstring:

```python
application. That no definition carries a contract rule's own sentences is
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`'s, which reads
every pair of the contract and a definition by runs of
`skills/settle/scripts/passages.py#WINDOW` words; the comment over `WINDOW`
holds the measurement that chose it.
```

Second, the judgment on the title's prefix (`frame/plan.md:80`) says the
diff "takes three functions out of `evals/scripts/behaviour.py`", and its
grounds cell says "the three functions had no caller outside tests". The
diff removes two functions, `scalar` and `grader_from`, and one constant,
`SCALAR`, as `frame/plan.md:74` says ("loses two functions"). `pr.md:4`
quotes the first cell, so it changes with it, word for word:

```markdown
| 2026-11-23 | The pull request's title takes `test:`, though the diff also takes two functions and a constant out of `evals/scripts/behaviour.py` and rewords a comment of `skills/settle/scripts/passages.py` | Every changed behaviour is a case's: the two functions and the constant had no caller outside tests, the comment changes no code, and no shipped gate reads or prints differently | `~/.claude/skills/commit-pr-convention/SKILL.md` *커밋 메시지*, the `test:` row; `frame/plan.md` *Technical context*; the titles of `gh pr list --state all --limit 10` |
```

```markdown
- "The pull request's title takes `test:`, though the diff also takes two functions and a constant out of `evals/scripts/behaviour.py` and rewords a comment of `skills/settle/scripts/passages.py`" (`frame/plan.md` *Judgments of the run*, the row on the title's prefix)
```

## Confirmations

What matched: `tests/conftest.py:876-901` builds `section` on
`lib/lines.py`'s `readable`, `sections`, `headings` and `heading_level`,
stops at the next heading of its level or above, leaves the heading line
out and fails on a heading held zero or two times, as `frame/design.md`
*Data & interfaces* states (read). The six cases of `Test_section` pass,
and `seal layout --pairs` names three pairs whose class docstring says
what each pair differs by (executed). Each member of a pair was shown red
on a different guard by `trail/phases/phase-1.md`'s mutation table, which
is carried as the crafter's claim.

What matched: the owner table and the wait case build every value S7
names from the code. `LINE_KEYWORDS` is `lib/fields.py`'s `CONFIRMS`,
`REGRESSION` and `REOPENS`, the verdicts are `chain_check.py`'s `FIXED`
and `REJECTED`, and row 27 is `broad_gate.py`'s `ON_BASE`, `NEW` and the
first word of `NOT_MEASURED`. The exit-code cells come from `pr_wait.py`'s
`range(7)` names, `STATES` and `MERGEABLE`
(`skills/code-review/scripts/pr_wait.py:138`, `:147-148`). Each built
value equals the literal it replaced (read).

What matched: `tests/workflows.py#parse` and `#front_matter` read as
*Data & interfaces* states, and `test_evals_layout.py` and
`tests/evals/test_rule_cases.py` read every `case.yaml` and grader through
them (read). `case_graders` takes `contains` where a grader names no
`match`, as `grader_from` did (`tests/evals/test_rule_cases.py:193`, read).

What matched: the prose that stood on the removed facts was rewritten in
the commits that removed them. Outside `seal/threads/`, `git grep` for the
moved-rule module's name, `806,241`, `LONGEST_KEPT`, `SMALLEST_REAL`,
`grader_from` and `a side records` finds only the two `check:` lines G2
names and a comment of `tests/evals/test_noninferiority.py:956`, which
describes that module's own record of a side (executed).

What matched: each quote of `pr.md` stands word for word at the
coordinate it names, in `frame/plan.md` A5a and A12a, `gaps.md` *Not
done* and the judgment row (read). Finding 2 changes the last one with its
source.

What matched: the three rows of `gaps.md` *Not verified* name the
orchestrator's broad run as their answerer, and the five files
`git grep -l passages -- 'tests/**/*.py'` lists at `f6989a83a` are the
ones its second row names (executed). The suite is labelled `unverified`
in each phase record, and the label is honest: no phase claims the broad
run.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `f6989a83a` | the whole tree | the orchestrator's broad run, after the review rounds settle |
| Whether the eval runner reads a `tool_used` grader with no `input_match` as every call of its tool; if it does, such a sealer grader bounds the broad run and the layout case raises on it | `tests/behaviour/test_evals_layout.py:134` | the orchestrator, from the runner's documentation |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/evals tests/behaviour/test_evals_layout.py tests/test_workflows.py`, in the clone | 210 passed |
| the same modules with `-p no:xdist`, after `evals/scripts/behaviour.py#squote` was edited to return `"'" + text + "'"` | 210 passed: no case holds the writer's quote doubling; the edit was reverted, and `git status` in the clone showed only the probe file |
| `bin/test -q -p no:xdist tests/evals/test_tmp_writer_round_trip.py`, a probe under the clone holding finding 1's accepting case and the same case with `squote` replaced by an undoubling writer | 2 passed: the round trip holds, and the undoubling writer fails it |
| `bin/test -q` over the 42 changed test modules, in the clone | 1146 passed, 1 skipped |
| `uvx ruff check` and `uvx ruff format --check` over the 46 changed Python files | exit 0 each |
| the searches S1, S2 and S4 to S8 of `frame/design.md`, at `f6989a83a` | each printed nothing |
| `bin/seal layout --pairs tests/test_conftest.py tests/test_workflows.py tests/behaviour/test_evals_layout.py` | 3 pairs, all in `Test_section` |
