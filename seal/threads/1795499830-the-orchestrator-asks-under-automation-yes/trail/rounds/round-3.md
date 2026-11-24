# Review round 3: 1795499830-the-orchestrator-asks-under-automation-yes

```seal
target: 7a56bbc2d, fixes 61513fa00..7a56bbc2d
```

This is the verifying round over round 2's fixes. The code read is the diff `61513fa00..7a56bbc2d`, which holds three commits and three files (executed: `git diff --stat 61513fa00 7a56bbc2d`). `1554da36a` adds round 2's record. `cb6e41818` changes `tests/hooks/test_ask_under_automation.py`, the one file outside the records. `07a5e180c` changes the work item's `gaps.md`, and `7a56bbc2d` appends the two close blocks to `trail/rounds/round-2.md`, ten lines and nothing else (executed: `git diff 1554da36a 7a56bbc2d`). Outside that bound, each of the work item's present-state records was read whole at `7a56bbc2d`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`. Both phase records and both earlier round records were read for their coordinates. `seal/config.json` names English for both language keys, so no `pr.<lang>.md` is owed. `seal/parity.json` is not declared, so no parity comparison was owed.

Carried from rounds 1 and 2 as coordinates and not re-established here, since the fix diff does not touch them: the hook's fail-toward-allow paths, the `STATED` and `NEAR` patterns, the dedupe case and its mutation, the normalisation in `lib/routing.py:394-401` and its case, the four `## Rule changes` items and their parse, *Scope* item 7's three passages, the S10 and S11 searches, `frame/questions.md` Q1, and the Windows group 2 durations that round 2 downloaded from run 45343775784. Re-established here: both closes, with round 2's `evidence: executed` line run again and the close's second mutation run as well; the conclusion of run 45343775784; the `gaps.md` diff; and every quote in `pr.md`.

## Findings

None. Both closes hold, and the fix diff introduces no defect this round found.

## Confirmations

```seal
confirms: round-2#1
```
What holds: S1's case, `test_refuses_a_question_under_automation_yes_with_the_rule`, now pins both sentences of the open-items part whole, at `tests/hooks/test_ask_under_automation.py:121-131`. The `opened` string matches the hook's text from "A work item counts as open" to "in a worktree of this repository." at `hooks/ask-under-automation.py:137-138`. The `ends` string matches from "Where its run has ended," to "take nothing from this call." at lines 138 to 141. Each string matches the hook's text character for character, the closing full stop included (read). Round 2's `evidence: executed` line was run again in this round's clone: "Where its run has ended, checking out " read as "Now, checking out " now fails S1 at line 131, `assert ends in reason`, with the other ten cases passing. Round 2 recorded SURVIVED for the same mutation. The close's second mutation was run too: "worktree of this repository. Where" read as "worktree here. Where" fails S1 at line 130, `assert opened in reason`, with ten passing. The close claimed two mutations red, each with the other ten cases passing, and both hold. The close also says that round 1's close of finding 2 was wrong to call the earlier pin "the second whole", and that the round 1 record is not edited. That matches round 2's finding, and earlier records are history, so leaving round 1's text in place is correct. The S1 docstring at lines 112 to 115 says the reason names "what makes it open and what ends the refusal", and it stays true. The change edits an existing case and adds none, so no new case has a group to be read against.

```seal
confirms: round-2#2
```
What holds: `gaps.md` line 10 is a new open row of `## Not verified`. It names `skills/implement/orchestration.md` *Orchestrator: how the work is routed*, the paragraph opening **While the `Automation` row reads `yes`**. That section heading stands at line 266, and the paragraph opens at line 304 (read). The row says that after the settle both the paragraph and the hook's row of `docs/running/what-a-script-gates.md` *The checks* would state when the hook refuses a call. It also says that before the settle the paragraph keeps its statement. Its answerer is the session that runs the settle after the 0.38.8 release. The settle reads such a row: its step 6 decides each open row against the tree, and it keeps a directory whose record still holds an open row (read: the installed plugin's `skills/settle/SKILL.md`, lines 95, 237 and 342). The deferral now has a home the settle reads, which is what round 2 finding 2 asked for. The close says that a tracker issue was not the fix pass's to open, since contract rule 6 withholds posting from every agent. That is correct. The close describes the row as the round's text with two changes. A third change, the wording of the answerer cell, is named in the close's next sentence, so the close states what was written. `skills/implement/orchestration.md` is not changed in the range, as the close says (executed: `git diff --stat`).

What matched: `07a5e180c` also closes the `gaps.md` row on the Windows legs at line 9. It closes the row in place, with the Item cell opening with the word `closed`, as the installed plugin's `skills/implement/SKILL.md` lines 310 and 311 give the form. No row leaves the memo: the diff removes one line and adds two, and the removed line's item stands again on the closed line (read). The closed row cites run 45343775784 at `61513fa00`. This round ran `gh run view 45343775784`: it read `success` and `completed` at `61513fa00dfd2c45eac1a4883178854b89c2f89d`, with nine jobs `success` and one `skipped` (executed). The durations half of the row's answer is round 2's executed download, carried here and not re-run.

What matched: the three quotes of `pr.md` still stand at their sources. `frame/plan.md` and `frame/questions.md` are unchanged in the range. The `gaps.md` row that quote 3 names, at line 8, is unchanged, and it is still the one row whose answerer is the repository owner on Windows hardware (read). `changelog.md`, `routing.md` and the frame files are unchanged in the range. No sentence in them is contradicted at `7a56bbc2d` by the test change or the memo change (read).

What matched: the chain check, run before this record, printed no notice at a line of `frame/design.md` naming a test pin or a copy (executed, `## Probes`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate: the suite is `unverified` at `7a56bbc2d` beyond the hook's module, which this round ran. CI run 45343775784 ran at `61513fa00`, not at the target, and it does not run the broad gate's command | the `Broad gate` key of `seal/config.json` | the orchestrator's broad run, which comes due now, since this round leaves no finding open; the sealer's spawn follows it |
| Whether the main session honours the deny and shows no question: carried from `frame/questions.md` Q1, measured by the orchestrator, not re-established here | `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/frame/questions.md:13` | the orchestrator |
| The hook's `py -3` half and a real session on Windows | `hooks/hooks.json:30` | the repository owner, on Windows hardware |
| Whether `skills/implement/orchestration.md:304-317` should cite the row of *The checks* in place of its own statement once the settle writes that row | `seal/threads/1795499830-the-orchestrator-asks-under-automation-yes/gaps.md:10` | the session that runs the settle after the 0.38.8 release |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist` in a `git clone --no-local` at `7a56bbc2d`, in the round's scratch directory | 11 passed, on macOS |
| `bin/seal mutate hooks/ask-under-automation.py --replace 'Where its run has ended, checking out ' 'Now, checking out ' --tests "bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist"` in the same clone | S1 red at `tests/hooks/test_ask_under_automation.py:131`, `assert ends in reason`; 10 passed |
| `bin/seal mutate hooks/ask-under-automation.py --replace 'worktree of this repository. Where' 'worktree here. Where' --tests "bin/test tests/hooks/test_ask_under_automation.py -q -p no:xdist"` in the same clone | S1 red at line 130, `assert opened in reason`; 10 passed |
| `gh run view 45343775784 --json conclusion,status,headSha,jobs` | `success`, `completed`, at `61513fa00`; nine jobs `success`, one `skipped` |
| `python3 skills/code-review/scripts/chain_check.py --baseline 7c8f67103 --root` the checkout `--worktree`, from the installed plugin, before the record | exit 0. It printed the two owed-verifying-round notices for round 2's closes, the target-behind-HEAD notice for `cb6e41818`, and the missing gate record and guarantee. It printed no notice at `frame/design.md` |
