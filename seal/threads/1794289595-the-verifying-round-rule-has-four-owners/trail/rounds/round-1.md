# Review round 1: 1794289595-the-verifying-round-rule-has-four-owners

```seal
target: e889a539b against release/v0.37.2
```

This round reviews the branch against `df775c52c`, the tip of
`release/v0.37.2`. It reads the tree's text of `skills/core/SKILL.md`,
`agents/proofer.md` and `skills/code-review/SKILL.md` from the diff, not the
installed 0.37.1 copies the proofer was spawned with. Round 1 has no
earlier record, so no fact is carried from one; every verdict below is this
round's own.

## Findings

### 1. *Earlier rounds* says "exactly one of three lines", and a fix whose close holds but which introduced a regression in its unit meets two of them

```seal
severity: should
location: `skills/code-review/SKILL.md:140-148`, `tests/text/test_the_rules_have_one_owner.py:175-181`, `seal/threads/1794289595-the-verifying-round-rule-has-four-owners/frame/design.md:29`
evidence: read `skills/code-review/SKILL.md:140-157`, `skills/code-review/scripts/chain_check.py:888-946`, `docs/forms/the-round-record.md:64-80`, and at `df775c52c` `skills/code-review/SKILL.md:135-139` and `docs/running/the-run.md:18-22`
```

Why it matters: the section is now the one definition every proofer acts
on, and it gives no answer for a case a fix pass produces often. Take a
round-1 finding #2 whose fix adds the missing guard and, in the same
function, breaks something else. The close of #2 holds, so the sentence at
`skills/code-review/SKILL.md:142` gives it a `confirms:` line. The new
defect is in a unit that fix changed and that fix introduced it, so the
sentence at `:143-145` puts a `regression:` line naming `round-1#2` on the
new finding. The sentence at `:140-141` then forbids naming #2 twice. The
proofer has to drop one line, and the text does not say which. Dropping
the `regression:` line loses the route that
`skills/code-review/orchestration.md` *A regression is routed by comparing
the fix with the frame* takes. Dropping the `confirms:` line tells the
orchestrator that #2's own close did not hold.

The word "exactly" is new in this diff, and nothing else in the tree asks
for it. The check collects every `confirms:`, `regression:` and
`reopens:` reference into one list and refuses only a finding none of them
names (`chain_check.py:905-946`). It does not refuse two lines naming one
finding. `docs/forms/the-round-record.md:68-72` gives the three relations
side by side ("`confirms:` where its close holds; ... `regression:` on a
new finding where a fix pass's own commit introduced it"), and in this case
both hold. Before the diff, the texts disagreed here. The old *Earlier
rounds* (`SKILL.md:135-139` at `df775c52c`) let a `regression:` line stand
only "where it does not" hold. The old *The run* (`the-run.md:19-22` at
`df775c52c`) wrote it wherever the fix's own commits introduced the
defect. The new definition takes *The run*'s unconditional reading and
adds "exactly one", so the conflict is now inside the one owner. The
frame asks for "exactly one line" (`frame/design.md:29`, *Scope* item 1).
The crafter built what the frame says, so the fix reaches the frame too.

The changelog's "No line's meaning changes" (`changelog.md:3`), which
`pr.md:2` quotes, stays true under the fix below. The fix makes the
definition agree with the check and with the form, and it gives no line a
meaning those two do not already give it.

The fix covers three statements: the section's sentence, the `RULES` row
that pins it word for word, and *Scope* item 1. In
`skills/code-review/SKILL.md` *Earlier rounds*:

```markdown
Every finding the round before closed `fixed <commit>` or `rejected` is
named this round by one of three lines: `confirms:`, `regression:` or
`reopens:`. A `confirms:` line names the finding where its close holds.
A `regression:` line stands on a new finding where the defect is in a unit
that a fix pass's own commits added or changed, and those commits
introduced the defect. Where that fix's own finding holds as well, a
`confirms:` line names it beside the regression. A `reopens:` line stands
on a new finding in every other case where the close does not hold: a
rejection that was wrong, or a `fixed` commit that left the defect
standing, in the unit that commit changed or in another.
```

In `tests/text/test_the_rules_have_one_owner.py`, row 21:

```python
        "Every finding the round before closed `fixed <commit>` or `rejected` "
        "is named this round by one of three lines: `confirms:`, "
        "`regression:` or `reopens:`.",
```

In `frame/design.md` *Scope* item 1, the second sentence becomes: "The
section says that every finding the round before closed `fixed <commit>`
or `rejected` is named this round by one line, and by a `confirms:` line
beside a `regression:` line where its close holds and its fix introduced a
defect in the unit." Run the changed row red with the new sentence taken
out of the section, as contract rule 15 asks.

```seal
verdict: fixed b2590e477
answer: `skills/code-review/SKILL.md` *Earlier rounds* drops "exactly", and `RULES` row 21 pins the sentence without it; the row was red against the unfixed section (executed, `bin/test tests/text/test_the_rules_have_one_owner.py -q -p no:xdist -k 21`, exit 1), and `seal mutate` that put "exactly" back ended `red`. The pass wrote the second sentence in its own words: "Where that fix's own finding holds as well" reads two ways in this tree, where a finding that holds is one whose claim stands (`docs/forms/the-round-record.md` *The round record*: "`rejected` means only that the finding does not hold"), so the section says "Where the close of the finding whose fix made the unit holds as well, a `confirms:` line names that finding too, so two lines name it." Like the paste-ready text, it does not name `regression:` in backticks, so `test_a_close_that_does_not_hold_reopens_it` asks no `reopens:` of it. No case holds that sentence: a `seal mutate` run that took it out survived, and `gaps.md` *Not done* gives why the pass left it unpinned. The frame's half was folded by the framer at `ff6d0e908`, and `frame/design.md` *Scope* item 1 states what the section now says.
```

### 2. The changelog says `agents/proofer.md` keeps the sentence on new units, which it did not hold before this diff

```seal
severity: should
location: `seal/threads/1794289595-the-verifying-round-rule-has-four-owners/changelog.md:4`
evidence: executed `git show df775c52c:agents/proofer.md | grep -n -i 'new unit'` (no line), `git show df775c52c:skills/code-review/orchestration.md | grep -n -i -A1 'new units'` (lines 118 to 119), `grep -n 'new unit' agents/proofer.md` (line 139)
```

Why it matters: the fragment becomes the release note a person reads, and
this sentence tells them where the rule came from. The claim is
"`agents/proofer.md` keeps the bound of a verifying round and the sentence
on a new unit in the fix diff". At `df775c52c`, `agents/proofer.md` holds
no sentence on new units. The sentence was
`skills/code-review/orchestration.md:118-119`, and this diff moved it to
`agents/proofer.md:139`. The frame says the same: "`agents/proofer.md`
... gains one citation and one sentence on new units" (`frame/design.md`
*Data & interfaces*), and *Removes* names the move. `pr.md` quotes only the
item's bold lead, so no quote changes with the fix.

```markdown
- **Each part of the verifying-round rule has one owner (#1476).** `agents/proofer.md` keeps the bound of a verifying round, and now holds the sentence on a new unit in the fix diff, which `skills/code-review/orchestration.md` held. `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round* keeps the orchestrator's judgment: when a round counts, the weighing at the third round, the signals, the stop row and the routes of a regression. `docs/running/the-run.md` *The run* keeps the policy and cites the orchestrator's half in one sentence.
```

```seal
verdict: fixed 972908a57
answer: The second *Changed* item now reads as the paste-ready text: `agents/proofer.md` keeps the bound and now holds the sentence on a new unit, which `skills/code-review/orchestration.md` held. Checked first: `git show df775c52c:agents/proofer.md | grep -n -i 'new unit'` finds nothing, and the base's `skills/code-review/orchestration.md:118-119` holds the sentence (executed). `pr.md` quotes only the item's bold lead, which did not change.
```

### 3. `frame/plan.md` says the work edits six rule files, and the diff edits seven

```seal
severity: should
location: `seal/threads/1794289595-the-verifying-round-rule-has-four-owners/frame/plan.md:7`
evidence: executed `git diff --stat df775c52c..e889a539b`, and read `seal/threads/1794289595-the-verifying-round-rule-has-four-owners/gaps.md:6` and `frame/design.md:29-52`
```

Why it matters: *Technical context* is dated to `0d73b6ed3`, but this
sentence is a claim about the work, not about the tree at that commit. The
sealer reads it against the tree. The diff edits seven rule files:
`skills/core/SKILL.md`, `skills/code-review/SKILL.md`,
`skills/code-review/orchestration.md`, `skills/implement/orchestration.md`,
`agents/proofer.md`, `docs/running/the-run.md` and
`docs/checks/the-pull-request-check.md`. *Scope* items 1 to 6 already named
all seven when the frame was written, so the count was off from the start.
`gaps.md:6` says "seven files", so two records of the work item disagree
on the count.

```markdown
The work edits text in seven rule files, one test file and
`.claude-plugin/plugin.json`. No line of a script changes.
```

```seal
verdict: fixed ff6d0e908
answer: The framer's fold at `ff6d0e908` rewrote `frame/plan.md` *Technical context* to count seven rule files and list them, the seven this finding names (read, `frame/plan.md:7-12` at HEAD); `git show --stat ff6d0e908` lists `frame/plan.md` among its two paths (executed). The fix pass made no commit for it.
```

## Confirmations

What matched: *Scope* items 2 to 6, read against the text at HEAD. The
proofer's rule keeps its bold lead, the target, one citation of *Earlier
rounds*, the sentence on new units, and the bound word for word with its
`check:` line (`agents/proofer.md:136-147`). The *Target* row cites the
proofer's two rules by their leads, and the *Job* row cites *Earlier
rounds* and defines no line (`skills/code-review/orchestration.md:112-114`).
*The run* keeps the four paragraphs *Scope* item 4 lists, and its one
citation of `orchestration.md` is at `docs/running/the-run.md:11`. The
core's cell reads as *Scope* item 5 words it (`skills/core/SKILL.md:107`).
Every site item 5 lists names that row, and so do the two sites phase 2
added (`orchestration.md:174-175`, `:202-217`) and the repair sentence
(`orchestration.md:477-481`). The notice sentence names the core's rule
(`agents/proofer.md:63-66`). Read.

What matched: the scenario greps S1 to S7 print what `frame/design.md`
*User scenarios & acceptance* says. S1 gives one line, 11, for
`code-review/orchestration.md` in `the-run.md`, and the three greps that
must find nothing find nothing. S2 gives 0 for all four files. S3 lists
`skills/core/SKILL.md:107` alone. S4 gives 0. S5 finds nothing and counts
one `signals` line. S6 finds nothing. S7 gives `0.37.2` on line 4, and
`54ebe2e74` is both the version commit and the commit that adds
`changelog.md`. Executed.

What matched: the phases claim that the narrow modules are green. This
round ran seven of them in one command, and it exited 0 with 178 passed
(see `## Probes`). Phase 2 claims the core is 9,276 characters, below the
cap of `frame/design.md` *Grounding* G15. `wc -m skills/core/SKILL.md`
prints 9276. Executed.

What matched: phase 2 claims that a `fixed <commit>` the core's row gives
to the sealer is the case the check passes. The core's cell, read with
`chain_check.py#channel`'s docstring at `:897-903`, gives the same two
conditions: a commit that touched the records alone, and a finding located
in the records alone. Read.

What matched: every quote of `pr.md` stands at the source its coordinate
names, with runs of whitespace collapsed. Quote 8 (`pr.md:8`) writes the
inner quotation marks as `\"`, and the source at `frame/design.md:14`
writes them bare. A backslash before a quotation mark is Markdown's escape,
so the rendered body reads word for word. This round judges that a match,
and a reader comparing bytes would see two extra backslashes. No
`pr.<lang>.md` stands, because the two language keys of `seal/config.json`
both read English. Read.

What matched: the three sentences that `gaps.md` *Not done* names stand at
`skills/code-review/orchestration.md:326` and `:350` and at
`docs/running/the-review-and-parity-arms.md:37`. None of them states the
condition on which the sealer reads a change. Read. Searches of the `*.md`
files outside `seal/threads` for other wordings of the exception found no
statement beyond the changed sites. The wordings were "records-only",
"only the work item's", "outside the work item's records", "owes no ...
round", "no verifying round", "work item's (own) records" next to a round
or the sealer, and "verifying round" outside the two owner files.
Executed. This is a sample of an open class, as rule 12 calls it.

The changed case's first assertion, `assert both(SKILL)`
(`tests/text/test_the_rules_have_one_owner.py:596`), holds nothing that row
21's owner check does not already hold, because that row pins a sentence
naming all three lines. The frame asks for the assertion (*Scope* item 7),
so this is no finding.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the full suite, the repository-wide lint and the format check. This round ran seven narrow modules, and the suite stays `unverified` | `seal/config.json` `Broad gate` | the orchestrator, by its broad run after the rounds |
| The `seal mutate` runs and the seen-red runs both phase records report. This round read each case's guard and ran none of them again | `trail/phases/phase-1.md:76-101`, `trail/phases/phase-2.md:94-119` | the sealer, which re-runs a sample of the crafter's claims |
| Statements of the exception or of the three lines in docstrings and comments under `skills/*/scripts/`, `lib/` and `tests/`. The searches read `*.md` files alone, and the frame puts the checker's docstrings out of scope | `frame/design.md` *Scope*, out of scope | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_the_rules_have_one_owner.py tests/text/test_the_verifying_round_is_bounded_not_cheapest.py tests/text/test_review_axes.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_docs_line_wrap.py tests/lib/test_core.py -q` | exit 0, 178 passed |
| the scenario greps S1 to S7 of `frame/design.md`, in one command | the output *Confirmations* gives |
| `git grep -n -i -E` over `*.md` outside `seal/threads` for other wordings of the exception, in two commands | only the changed sites and the three `gaps.md` names |
