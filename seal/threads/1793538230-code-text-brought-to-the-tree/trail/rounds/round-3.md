# Review round 3: 1793538230-code-text-brought-to-the-tree

```seal
target: bee67bfe, fixes 40e5a3d6..bee67bfe
```

This is a verifying round. Its target is the diff of round 2's fixes, `40e5a3d6..bee67bfe`. That diff holds three commits. In 3e81b425 the orchestrator re-folded the parenthetical of `frame/design.md` *Scope* 4 and added a row to `frame/plan.md` *Judgments of the run*. In bbf80a99 the fix pass rewrote `hooks/lib/console.py:50-54` and the second bullet of `changelog.md`. bee67bfe holds the two close blocks of round 2. The round worked in a `git clone --no-local` of the worktree under the session's scratch directory, checked out at `bee67bfe`. No `seal/parity.md` is declared, so the record carries no `original:` line. `seal/config.md` has no `Record language` row, so the record is in English.

Carried from earlier rounds and not re-derived: the reasons the docstring gives for `.github/scripts/release_report.py`, `.github/scripts/release_seal.py`, `.github/scripts/rules.py` and `hooks/dispatch.py` (round 1's sixth confirmation), and the count of scripts under `skills/*/scripts/` that reach `hooks/lib/`, 11 of 14 (round 2's first confirmation). The fix diff leaves the lines stating both unchanged. Re-derived this round: what `skills/code-review/scripts/chain_check.py` does before its loop and what it loads after it; the comment above each of the other 13 loops under `skills/`; the body of #1255; and the listing command's output at `bee67bfe`.

The axes walked are the two closes, one sentence of the rewritten docstring at a time against the code it names; the changelog fragment's restatement of those sentences; the orchestrator's fold and its route row against the sections they cite; and the claims the fix pass makes in its close blocks.

Convergence: round 1 raised one finding on this paragraph. Round 2 raised two, both on the sentence that replaced it, and both traced to round 1's paste-ready text. This round finds no defect in the sentence that replaced those, and opens nothing. The fixes have converged. The paragraph's claims about the skill scripts now each rest on a coordinate this round opened.

## Findings

None. Both closes of round 2 hold, and the fix diff introduced no defect this round found.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the docstring now names the one script under `skills/*/scripts/` that states a reason, and the reason holds at the code. `hooks/lib/console.py:50-53` says that `chain_check.py` runs its loop before it loads any of the `hooks/lib/` modules, so that its refusal does not meet a console's code page. In `skills/code-review/scripts/chain_check.py`, lines 98-106 import the standard library alone. The loop stands at lines 108-118 under the comment "Before the readers load below: a refusal printed at import must not meet a console's code page". The loads come after it, in the `try` at lines 234-242, which prints "chain-check: the shared reader would not load" and exits 2 when one fails. Its later loads, of the rule-changes reader at line 1073 and the parity readers at line 1292, sit inside functions that run after the loop (read). The docstring's own inference, that loading this module would be one more load that can fail before the streams are set, follows from that order. The claim "None of the others says why it copies the loop rather than loading this module the same way" was re-derived by reading the comment above each of the other 13 loops (executed, `## Probes`). `seal.py`, `settle.py`, `deferral_check.py`, `session_cost.py`, `unverified_check.py`, `arm_check.py` and `seal_stamp.py` say that `hooks/lib/console.py` owns the reasoning. `fold_check.py` and `pr_body.py` say why the streams need setting. `core_check.py`, `pact_check.py` and `payload_meter.py` carry no comment. `broad_gate.py:3189-3191` and `seal_stamp.py:1511-1513` say why their loop must come after a question asked of stdout. That is a reason for where the loop stands, and a call to this module made at the same place would keep it, so neither is a reason to copy. So the sentence holds for all 13. The changelog fragment's second bullet says "only `skills/code-review/scripts/chain_check.py` states a reason, that its loop must run before anything it loads" (`changelog.md:4`), which matches the comment's own words. The fix pass claimed its set of six test modules gave 341 passed and 8 skipped. The same command at `bee67bfe` in the clone gave the same (executed, `## Probes`).

```seal
confirms: round-2#2
```
What holds: the docstring's hand-off now names a question #1255 holds. `hooks/lib/console.py:54` reads "Which entry points owe the answer is #1255's." The fix pass did not open #1255 and relied on round 2's read, and its close says so. This round opened it again. #1255 is open, and its body says "The first half, which entry points owe the answer, is this issue's frame to decide". Its *Done when* asks that "every entry point gives `STREAMS`' answer or carries its reason" (executed, `## Probes`). The changelog fragment's last clause, "leaves which entry points owe the answer to #1255" (`changelog.md:4`), matches. `git grep` for "owes the import", "import is #1255", "should import the module", "none states a reason", "no stated reason" and "None of them says why" finds nothing outside `seal/threads/`. Inside this work item it finds them only in round 1's and round 2's records and in the 1ac8b651 row of `frame/plan.md` *Judgments of the run*, each a record of what was decided then (executed). The import question has no owner in the tree after this fix. The docstring no longer names a false one, and round 2 left the choice to give it one with the orchestrator (`## Not judged`).

```seal
confirms: none
```
What matched: the orchestrator's re-fold in 3e81b425. `frame/design.md:28`, *Scope* 4, was rewritten in place, and its parenthetical now says that `chain_check.py` states its loop runs before its loads, that the others state no reason, and that which entry points owe the answer is #1255's. Each clause matches the code and #1255's body as this round read them. The new row of `frame/plan.md` *Judgments of the run* cites `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*, which stands at line 177 of the tree's copy (read). The row routes round 2's two regressions to an ordinary fix pass. The section's table gives that route where "the defect is in how it was written, a review record's paste-ready fix applied as given among them". Round 2's grounds say both sentences came from round 1's paste-ready text, and round 1's record at lines 25-32 holds them word for word (read). So the route is the one the table gives. The row's grounds argue the route differently: "The fix built the frame as the orchestrator's fold at 1ac8b651 wrote it", which is the wording of the table's first row, and a lower cost than sending the work item back to the framer. They do not name the paste-ready row, which licenses the route on its own. This is a question of how the grounds are worded, not a wrong route, so it is no finding. Its third claim holds: round 1's finding 1 carries no `regression:` line, so round 2's were this unit's first regressions. This round raises none, so the table's third row, a unit's second regression, does not come into play.

```seal
confirms: none
```
What matched: the rewritten lines of `hooks/lib/console.py` are each 79 characters or fewer (executed: `awk 'length > 79'` lists lines 25, 35, 42, 43 and 72, none of which the fix diff changed). `uvx ruff check` and `uvx ruff format --check` exit 0 on the file, and it imports under `python3 -W error` (executed). The listing command at `hooks/lib/console.py:62` prints the same 19 files at `bee67bfe` as at the build's HEAD: the three `.github/scripts/` files, `hooks/dispatch.py`, this file, and 14 under `skills/*/scripts/` (executed). So *Scope* 4's "holds against that command's listing at the build's HEAD" still holds.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `bee67bfe`. `gaps.md` labels them unverified and names the orchestrator, and no fix pass changed that label, so the label is honest. This round leaves nothing open, so what comes due is the orchestrator's broad run by `seal gate`, then the sealer's spawn | the whole tree | the orchestrator, then the sealer |
| Whether the import question, which the docstring no longer hands to anyone, should be added to #1255. Carried from round 2 | #1255 | the orchestrator |
| Whether the new case passes on the Windows legs (`frame/questions.md` Q1). Carried open from round 1, and outside this fix diff | `tests/hooks/test_console.py:102-128` | the pull request's Windows legs, read by the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'` | 19 files, 14 under `skills/` |
| for each of the 14 `skills/` files, the 12 lines above its first `.reconfigure(`, then `sed` over `broad_gate.py:3180-3206`, `seal_stamp.py:1505-1526` and `payload_meter.py:1128-1141` | `chain_check.py:109-110` alone ties its loop's place to the loads after it; `broad_gate.py` and `seal_stamp.py` tie theirs to a question asked of stdout; no other comment gives a reason to copy rather than load |
| `gh issue view 1255 --json title,state,body` | `OPEN`; the body gives the frame of #1255 "which entry points owe the answer" and asks nothing about importing the module |
| `git grep -n -i -E "owes? the import\|import is #1255\|should import the module\|none states a reason\|no stated reason\|None of them says why"`, outside and then inside `seal/threads/` | outside: no line, exit 1; inside: round 1, round 2 and the 1ac8b651 row of `frame/plan.md` alone |
| `bin/test tests/hooks/test_console.py tests/test_censuses.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_one_word_one_meaning.py tests/behaviour/test_a_document_that_names_a_script_says_how_to_reach_it.py tests/behaviour/test_docs_line_wrap.py -q -p no:xdist` | 341 passed, 8 skipped, exit 0 |
| `python3 -W error -c "import sys; sys.path.insert(0,'hooks/lib'); import console"`; `uvx ruff check hooks/lib/console.py`; `uvx ruff format --check hooks/lib/console.py` | exit 0, exit 0, exit 0 |
| `awk 'length > 79' hooks/lib/console.py` | lines 25, 35, 42, 43 and 72, none in the fix diff |
