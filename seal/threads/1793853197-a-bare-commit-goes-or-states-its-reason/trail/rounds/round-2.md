# Review round 2: 1793853197-a-bare-commit-goes-or-states-its-reason

```seal
target: 022242a0, fixes 7b03f3aa..022242a0
```

This is a verifying round. It reads the fix range after the sealer withheld
at 7b03f3aa: 853b3fbc and 022242a0 fold `frame/design.md` D1 row 36 and add
a judgment row to `frame/plan.md`, and 5e2718cf rewrites the module
docstring of `tests/text/test_a_moved_rule_leaves_its_definition.py` and
`trail/phases/phase-1.md` row 78 with its Q1 bullet. Round 1 closed no
finding, so no `confirms:`, `reopens:` or `regression:` line is owed. The
fix answers the sealer's withholding (`guarantee.md`, the `Verdict:` line),
and this round judges that answer.

Every probe ran in a scratch clone of the branch at 022242a0, under the
round's own scratch directory, and the clone was removed before this record
was written. The worktree was not changed except by this record.

Carried, not re-established: round 1's confirmations of the branch up to
8a6aa184, which this round does not re-review because the fix range touches
none of what they cover. The coordinate of the heading list,
`tests/text/test_every_agent_reads_the_contract.py:82-84` and the assertion
at `:138`, came from `guarantee.md` and was opened again here. Every claim
about the docstring below was run or read this round.

The implementer's account was read as claims. The fix pass claimed, in the
Q1 bullet for row 78 of `trail/phases/phase-1.md`, that with rule 9's body
appended to `agents/proofer.md` the four named modules fail with a new `##`
heading and give 52 passed under a `###` heading or as a paragraph, that
this module gives 3 failed in all three shapes and 189 passed with nothing
planted, and that the heading list entered at 2fc33333 under #957. The
crafter's probe logs in the session scratchpad were not taken as results.
Each claim is answered under `## Confirmations` by what this round ran.

## Findings

None. The round opens no finding, so nothing is open for a fix pass.
Commit 5e2718cf changed a file under `tests/` after the broad run at
a0b71874, so what comes due is the orchestrator's broad run at HEAD, then
the sealer's spawn after it. `chain_check.py` names both.

## Confirmations

What matched, the docstring states what holds at HEAD: the module
docstring at `tests/text/test_a_moved_rule_leaves_its_definition.py:8-14`
says that rule 9's body pasted into `agents/proofer.md` as a paragraph, or
under a `###` heading, leaves the four named modules green, and that a paste
under a new `##` heading is caught there by the heading list. In the clone
at 022242a0, rule 9's body, with its `check:` line as `sections` reads it,
was appended to `agents/proofer.md` through the `Edit` tool in three shapes.
For each shape the four modules ran in one `bin/test -q` call and this module
in another (executed). Under `### What rule 9 states`, the four gave 52
passed at exit 0. As a bare paragraph, they gave 52 passed at exit 0. Under
`## What rule 9 states`, the shape the module's own `paste_back` makes, they
gave exit 1 with 1 failed and 51 passed. The failure was
`test_every_definition_has_the_shape_and_preloads_the_core_and_the_contract[agents/proofer.md]`
on "the `## ` headings are (..., '## Rules', '## What rule 9 states'), not
(..., '## Rules')". This module gave exit 1 with 3 failed and 186 passed in
all three shapes, and 189 passed at exit 0 with nothing planted. Each
figure matches the fix pass's Q1 bullet. The paragraph shape was appended
at the end of the file. A paragraph planted before the opening sentence
would instead fail the opening-paragraph check at
`tests/text/test_every_agent_reads_the_contract.py:79-81` (read). The
docstring's natural reading, a paste into the body, holds.

What matched, "Only a paste under a new `##` heading": `shape_problems` reads
`^## .*$` and compares the tuple with `SECTIONS` for equality
(`tests/text/test_every_agent_reads_the_contract.py:82-84`, read). A `###`,
`####` or `#` heading does not match that pattern, so `##` is the only
heading level the list catches.

What matched, the attribution to #957: `git log --follow -S'headings are'`
on `tests/text/test_every_agent_reads_the_contract.py` names 2fc33333,
dated 2026-10-18, whose subject carries #957 and #972 (executed). The
docstring's "(#957)" names one of the two, and that is the work item the
fix pass and `frame/plan.md` name.

What matched, the past-tense sentence: "When phases 1 and 2 wrote their two
modules, every assertion in them was a presence check" moves the old
present-tense sentence to the time it was written. The three modules were
added together at 438cffe4, dated 2026-09-03 (`git log --follow
--diff-filter=A`, executed). The module's docstring there carries the same
sentence in the present, beside the 2026-09-03 measurement (`git show`,
executed). The sentence is therefore the original author's statement of
that day, and the fix changes its tense, not its content. The sentences
after it, "had nothing behind it" and "could drift", were already past.

What matched, the module keeps its reason for existing: the docstring still
names a paste the four modules miss, and the probe above shows this module
catches each such paste. The `## Where this draws the line` section below it
is unchanged. `paste_back`'s docstring at `:231`, "pasted back in under a
new heading", describes what that helper builds, which is a `##` heading,
and claims nothing about the four modules (read).

What matched, the records agree with the docstring: `trail/phases/phase-1.md`
row 78 quotes the docstring's first two sentences and the opening of the
third word for word (read, against the module at HEAD).
`frame/design.md` D1 row 36 states the same split, a paragraph or `###`
paste green and a `##` paste caught by #957's list, and moves the
presence-check sentence to the time phases 1 and 2 wrote (read). Its
*Removes* row for this module, "the defect stays as a sentence", still
holds. The `frame/plan.md` judgment row cites
`tests/text/test_every_agent_reads_the_contract.py:138`, which is the
assertion that failed in the `##` probe (read).

What matched, no other record went stale: `changelog.md` says "Four held
the grounds of a behaviour, which now stand in the sentence". The sealer
read row 78 as the one of the four that HEAD contradicted, and HEAD now
holds it. `gaps.md` says nothing of the module. Its third row hands the
meaning of each rewrite to the proofer, and row 78's rewrite still keeps
what its reader acts on: why the module exists. `git grep -n "new heading"`
and `git grep -n "presence check"` at HEAD find the old wording only in
`guarantee.md` and `trail/rounds/round-1.md`, and in `paste_back`'s
docstring (executed). Each record states the commit it names, and the
sealer replaces `guarantee.md` when it runs again. `git grep -n
test_a_moved_rule_leaves_its_definition HEAD -- tests` lists nine lines in
eight other test modules that name this module (executed), and each was
read with the lines around it:
`tests/text/test_broad_gate_rule.py:18`,
`tests/text/test_edits_go_through_the_edit_tool.py:12`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py:36`,
`tests/behaviour/test_a_section_marked_for_one_role_reaches_only_that_role.py:27`,
`tests/behaviour/test_the_pull_request_language_is_the_repositorys.py:1191`,
`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:771`, `:843`
and `:952`, and `tests/skills/test_passages.py:8`. None restates that the
four stay green on a paste. Each cites the module for its window, for its
refusal of a copy, or for the moment it began to exist. The list is the
closed set of lines that name the module, not a sample.

What matched, no commit added outside `seal/`: the `+` lines of `git diff
-U0 7b03f3aa 022242a0 -- . ':(exclude)seal/'` hold no hex token of seven to
forty digits (executed, grep exit 1). So the squash case has no new token
to read.

The fix range adds no test, so no new case is read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at 022242a0. The last broad run, at a0b71874, predates 5e2718cf, which changes a test module's docstring | `trail/gate.md` | the orchestrator, at the broad run at HEAD |
| The sealer's own re-run of its withheld claim at the new HEAD | `guarantee.md` | the sealer |

## Probes

| Command | Result |
|---|---|
| `bin/test` over `test_broad_gate_rule`, `test_edits_go_through_the_edit_tool`, `test_every_agent_reads_the_contract` and `test_the_agent_contract_holds_the_universal_rules`, `-q`, nothing planted | 52 passed, exit 0 |
| `bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q`, nothing planted | 189 passed, exit 0 |
| the four, rule 9's body under `### What rule 9 states` | 52 passed, exit 0 |
| this module, the same plant | 3 failed, 186 passed, exit 1 |
| the four, rule 9's body as a bare paragraph | 52 passed, exit 0 |
| this module, the same plant | 3 failed, 186 passed, exit 1 |
| the four, rule 9's body under `## What rule 9 states` | 1 failed, 51 passed, exit 1, on the `## ` heading list |
| this module, the same plant | 3 failed, 186 passed, exit 1 |
| `git log --follow --format='%h %ad %s' -S'headings are' -- tests/text/test_every_agent_reads_the_contract.py` | 2fc33333, 2026-10-18, #957 and #972 |
| `git log --follow --diff-filter=A` on the three contract modules | 438cffe4, 2026-09-03, for each |
| `git diff -U0 7b03f3aa 022242a0 -- . ':(exclude)seal/'`, `+` lines grepped for 7-to-40-hex tokens | none, exit 1 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 31558c76 --root <worktree> --worktree`, before this record | exit 0; it named the owed verifying round, the gate run behind HEAD and the guarantee behind HEAD, and no notice on `frame/design.md` |
