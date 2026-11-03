# Review round 2: 1793688270-a-check-line-names-a-case-or-the-rule-carries-none

```seal
target: e3594e43c, fixes bb5ad7a80..e3594e43c
```

The target is `git diff bb5ad7a80 e3594e43c`, read in a `git clone --no-local` of the repository at `e3594e43c` under the session's scratchpad. The diff holds five commits: `76989974c` (round 1's record and one orchestrator row in `frame/plan.md` *Judgments of the run*), `c87f09304` and `82e9afa58` (the fix pass), `d6b279865` (`gaps.md`) and `e3594e43c` (the close blocks) (executed: `git log --oneline bb5ad7a80..HEAD`, `git diff --stat bb5ad7a80 HEAD`). The request is issue #1277 whole, its body and three comments (executed: `gh issue view 1277 --json title,body,comments`). `seal/parity.md` is not declared, so the round block holds no `original:` line. `seal/config.md` has no `Record language` row, so the record is English.

Carried from round 1 and not established again: where the section `skills/implement/acts.md:69` tables stands (`skills/implement/orchestration.md` *What the answer writes*), and that `hooks/question-gate.py` refuses on the `Automation` row. Re-read this round: `hooks/lib/routing.py#parse` at HEAD, the section at `skills/implement/orchestration.md:267-312`, and which rows `hooks/implementer-notice.py` reads.

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-1#1
```
What holds: a declaration built with the `Answer pressed` row is now pinned to read as the same declaration without it. `tests/hooks/test_routing.py:119-126` adds `test_a_row_the_reader_does_not_read_changes_no_answer` to `Test_parse`. It builds the row with `with_row("Answer pressed", "automation")`, which is the label and one of the two values the base template wrote (`templates/records/sdd-routing.md:10` at `147285fda`, executed: `git grep -n 'Answer pressed' 147285fda -- templates`). It asserts that the whole parsed dictionary equals that of `two_axis_text()`. So a reader that refused the row, or that carried its value into any key, fails it (read). The case passes at HEAD in a run of the module (executed, `## Probes`). Claimed in the close: the case was seen red under `seal mutate` with a guard making `parse` return `None` on any label outside the six it reads. Found: the same mutation over that one case reads `red: the cases failed against the mutation (exit 1)`, and the failure is the equality assertion at `:126`, where `parse` of the declaration with the row returned `None` (executed). The clone's tree was clean after the run (executed: `git status --short`, empty). Read against its group: `seal layout --pairs` (exit 0) pairs the case with `test_accepts_a_two_axis_declaration_with_no_optional_row_answered` and `test_an_absent_automation_row_is_not_the_same_fact_as_a_chosen_no`, because each calls `parse(two_axis_text())` (executed). That call is the baseline the new case compares against. No other case parses a row whose label the reader does not read: the other `with_row` calls in `tests/` (`tests/hooks/test_routing.py:338`, `:379`) take their labels from the optional-row constants, and the cases that write a row by hand (`:136-149`, `:272-284`) write an `Implementation` row (executed: `git grep -n 'with_row(' -- tests`, read). So the case covers what its group does not, and it stays. The close also claimed that `gaps.md` names the case's id as unpriced. The `gaps.md` row on phase 4's case ids now names it, and `.test_durations` holds no line for it (executed: `grep -c` on the id, exit 1). The statements round 1 named, `changelog.md:6` and `frame/plan.md:40`, are unchanged and now stand on this case (read).

```seal
confirms: round-1#2
```
What holds: `skills/implement/acts.md:69` now names the `Implementation` and `Planning` rows as the ones nothing that refuses reads. The rest of the row is unchanged (executed: `git diff bb5ad7a80 e3594e43c -- skills/implement/acts.md`). The sentence is true at HEAD. `hooks/implementer-notice.py:56-61` reads only the `planning` and `implementation` keys, and the hook is PostToolUse, so it blocks nothing (`:20`, `:34`, `:98`, read). `Automation`, which the section marks OPTIONAL (`skills/implement/orchestration.md:274`), is no longer among the rows the sentence names, so the sentence has one reading. The close claimed no other sentence on this act says "optional rows". Found: `git grep -n -i 'optional rows\|two optional\|three optional' -- ':!seal/'` lists `docs/running/the-review-and-parity-arms.md:105`, `hooks/implementer-notice.py:13`, `hooks/lib/routing.py:195`, `skills/implement/orchestration.md:282` and four test lines (executed). None of them is about who refuses on the rows. `routing.py:195` stays for the reason round 1 gave. The four modules that read `acts.md` pass at HEAD (executed, `## Probes`).

```seal
confirms: none
```
What matched: the orchestrator's row at `frame/plan.md:49` answers round 1's *Not judged* row on `docs/checks/the-routing-check.md`. It cites issue #1277 *The `check: none reader:` form goes*, and that heading stands in the issue body. The body removes "every `check: none reader:` line in the plugin's files" (executed: `gh issue view 1277`). The removed line is `docs/checks/the-routing-check.md:80` at the base. The paragraph above it, at `:73-79`, still reads whole, and the diff changes nothing else in the file (executed: `git diff 147285fda e3594e43c -- docs/checks/the-routing-check.md`). The row records the decision, its grounds and the document it was judged against, which `skills/core/SKILL.md` *The first value: efficient development through the workflow* asks of a judgment.

```seal
confirms: none
```
What matched: `d6b279865` changes `gaps.md` in two places, and both are true. The phase 4 case-id row now names the case round 1's fix pass added and the commit it came in (`c87f09304`, executed: `git show c87f09304 --stat`). The first row gains the fix pass's run, and the blank line above `## Not done` returns (read). The run is labelled under *Not verified* with the orchestrator at the broad gate as its answerer. That label is honest: it reports a narrow set and claims nothing about the full suite (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD. This round re-ran one routing module and four modules that read `acts.md`, not the fix pass's 89 modules | `gaps.md` *Not verified* | the orchestrator, at the broad gate |
| Whether the unpriced `test_a_row_the_reader_does_not_read_changes_no_answer`, with the ids phases 1 to 4 removed, pushes `test_the_durations_file_prices_the_suite` past its share | `gaps.md` *Not verified*, `frame/questions.md` Q1 | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_routing.py -q` | exit 0, 52 passed |
| `bin/seal mutate hooks/lib/routing.py --replace '    if not branch:' '    if not branch or set(found) - {"Axis", REVIEW, DESTINATION, BRANCH, IMPLEMENTATION, PLANNING, AUTOMATION}:' --tests "bin/test tests/hooks/test_routing.py -q -k test_a_row_the_reader_does_not_read_changes_no_answer"` | exit 0, `red`: 1 failed, at `tests/hooks/test_routing.py:126`; tree clean afterwards |
| `bin/seal layout --pairs` | exit 0; the new case is paired twice in `Test_parse` for calling `parse(two_axis_text())` |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_every_orchestrator_act_names_its_delivery.py tests/text/test_broad_gate_rule.py tests/text/test_no_passage_is_pasted_into_a_second_file.py -q` | exit 0, 83 passed |
| `grep -c test_a_row_the_reader_does_not_read_changes_no_answer .test_durations` | exit 1, 0 lines |
