# Review round 3: 1793833681-an-import-inside-a-fence-is-not-charged

```seal
target: 9696913a, fixes c9d22759..9696913a
```

This is a verifying round, and the orchestrator's row of `frame/plan.md` *Judgments of the run* (`:43`, committed at c97e4936) names it as the run's last. It read the diff of round 2's fixes, `git diff c9d22759 9696913a`, which holds four commits: c97e4936, 5c3491f3, 6344c4e0 and 9696913a (executed). The branch's base is `release/v0.32.2` at 2ecb8d4b. The repository tracks no `seal/parity.md`, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is English. Every run took place in a `git clone --no-local` of the branch at 9696913a under the session scratchpad, which was removed before the hand-back.

Carried from earlier rounds and not re-established: the reading of Claude Code 2.1.318 in `frame/design.md` G3, which says what the harness reads after an inline `<!--`; CommonMark's rule that an HTML comment block opens only at the start of a line; and round 2's finding that a copy without `hooks/lib/core.py` stops there first, whose coordinate `payload_meter.py:514-515` was opened again this round and still holds. Every verdict below was reached this round. Round 2's two probe shapes for its finding 1 were written again from its `## Probes` row and run, and both matched.

The accounts were read as claims. The fix pass, in its close of round 2's finding 1 (6344c4e0), claimed that each causal claim of its docstring was checked against `_scan` at `unverified_check.py:367-447`. It claimed that a second list-item fence brings the fences back in step and a tilde fence does not, that the short line of the last rewrap is gone, and that ruff and 90 cases passed. The orchestrator's c97e4936 claimed that S8, *Data & interfaces* and *Operational impact* name a copy that holds `hooks/lib/core.py` and not `unverified_check.py`, and that *Out* states the scan's difference by its cause. Its 9696913a claimed that *Out* states the reach of the fence misstep as the docstring does. Each claim is checked below. Under the judgment row at `frame/plan.md:43`, the round raises a finding only where a sentence of the docstring or of the frame is false, and takes no further shape of the scan as one.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the *What this does not model* part of `imports_of`'s docstring (`skills/verify/scripts/payload_meter.py:404-418`) now states the shared scan's two differences by their causes, and each causal sentence matches the code (read: `skills/verify/scripts/unverified_check.py:367-447`, `hooks/lib/blocks.py:94`, `:125-144`).

- "Its fence rule reads each line with no list item or block quote around it." The rule is `FENCE`, `^ {0,3}` and then a run of backticks or tildes (`blocks.py:94`). `_scan` asks it of each raw line (`unverified_check.py:387`, `:391`) and strips no `>` or list marker first.
- "So it opens no fence behind `>` or a list marker." A line that opens with `>` or `-` fails `^ {0,3}`, so `fence_opener` returns None for it.
- "It reads that fence's closing line as an opener where the line stands within three spaces of the margin." A closer such as two spaces and three backticks matches `FENCE`. A closer at four spaces does not, and a `>` closer does not either. The probe showed both: the block-quote fence gave `a.md` and `b.md`, so the fences stay in step after it.
- "From there the meter's fences stand out of step with the file's, until a later fence line happens to bring them back or the file ends." The fence is decided by `fence_closes` alone while one is open (`unverified_check.py:386-389`). The probe gave `a.md`, `c.md` for round 2's shape, `a.md`, `d.md` after a second list-item fence, and `a.md` alone after a tilde fence. The fix pass's two claims and round 2's shape each matched.
- "The scan also opens a comment at every `<!--` in live text and closes it at the next `-->`, however far below." `_scan` looks for `OPENER` only outside a fence, a comment and a span (`:390`, `:419-423`). It then looks for `CLOSER` on every later line and keeps no fence or paragraph state in between (`:399-404`).
- "There the meter hides the imports up to the next `-->`, or to the end of the file where none follows." The probe gave `c.md` alone for round 2's inline opener closed in a later paragraph.
- "The harness reads them" rests on G3 and is carried.

The short line of the rewrap is gone: no line of the docstring at `:396-422` ends before the block's width without ending a sentence (read). `uvx ruff check` and `uvx ruff format --check` on the file each exited 0, and the two modules ended 90 passed (executed). This matches the fix pass's figures.

*Out* (`frame/design.md:36`), as 9696913a leaves it, states the fence misstep's reach in the docstring's words: "until a later fence line happens to bring them back, or the file ends". It states the comment shape by the class round 2 named: a `<!--` that CommonMark reads as text hides the text up to the next `-->`, or to the end of the file. Neither sentence is false for the shapes where the meter and the file part.

Three places were weighed and opened no finding. Each is a shape the docstring's causes cover. Under the judgment row such a shape is no finding, and no agent at a step acts on it (`skills/code-review/SKILL.md` *The record*: "a sentence that only reads badly is no finding").

- *Out* says without a condition that "a fence's closing line behind a list marker opens a fence for the meter". The docstring adds "within three spaces of the margin". The probe ran `10. ` and three backticks, `@a.md` indented four, the closer indented four, then `@b.md`. It gave `b.md`. The four-space closer opens no fence, and the first line's run pairs with it as a code span across the item (`_partner_ahead`, `unverified_check.py:552-569`), so `a.md` is hidden as the file hides it. Here the meter and the file agree. *Out*'s clause overstates a limit of a meter that gates nothing, and it names the docstring as the statement of the limit. The same shape makes the docstring's "the meter reads an import inside such a fence" untrue for that one item, where again there is no difference to state.
- *Out* files "an import inside a fence behind `>` or a list marker" among the shapes where Claude Code's reader goes past its documentation. The docstring puts it under the scan's fence rule. Both readings stand: G2 shows the frame counting a shape as past the docs where the docs name no rule for it, and the meter's reading there comes from the scan. *Out*'s "Two shapes come from the shared scan itself" counts the two it lists in that sentence, and every shape the docstring states is listed somewhere in *Out*.
- The scan opens a comment at `\<!--` and at `<!-->`, where CommonMark reads an escaped `<` and an empty comment. The docstring's sentence on where CommonMark reads a `<!--` as text names neither. Its causal sentence, "opens a comment at every `<!--` in live text", covers both.

```seal
confirms: round-2#2
```
What holds: c97e4936 applies round 2's three paste-ready rows word for word (executed: `git diff c9d22759 9696913a`). S8 (`frame/design.md:52`) gives the no-flag copy as one holding `hooks/lib/core.py` and `hooks/lib/optin.py` and not `unverified_check.py`. *Data & interfaces* (`:58`) and *Operational impact* (`frame/plan.md:34`) name a copy that holds `hooks/lib/core.py` and not `unverified_check.py`. Each matches the tree. `session_composition` calls `_core()` before `pair_rows` (`skills/verify/scripts/payload_meter.py:514-515`, read), so only a copy that holds `core.py` reaches the scan. `Test_module.test_a_copy_without_the_scan_exits_2_on_a_run_that_reads_a_claude_md` copies the script, `hooks/lib/core.py` and `hooks/lib/optin.py` and nothing else (`tests/skills/test_payload_meter.py:1492`, read). It asserts exit 2 and the sentence's "no import of a `CLAUDE.md` can be read" (`:1515-1518`), which is the half of `_fence_rule`'s sentence that names the import use (`payload_meter.py:177-183`). The case passed this round (executed). The fix pass's account of this close says no code changed for it, and the diff touches no code but the docstring.

What matched, in the orchestrator's new judgment row (`frame/plan.md:43`). It cites `skills/code-review/orchestration.md` *Orchestrator: the run ends with a verifying round*, which stands at `:99`, and `skills/core/SKILL.md` *The rule a mechanism is kept against* (executed: `grep -n`). Its count of three findings for round 1 matched (executed: `grep -c` over `round-1.md`'s finding headings). The count of two for round 2 matched too (read). The row's statement that `regression: round-1#1` stood in the orchestrator's own fold matched round 2's finding 2.

What matched, in the fix pass's close blocks (6344c4e0). Each close sits under its finding's paste-ready block and names the commit the diff holds, 5c3491f3 for the docstring and c97e4936 for the records. The close of finding 1 names a probe it ran and deleted, and no `test_tmp_*` file stands in the tree at 9696913a (executed: `git status --short` in the clone after this round's probe was deleted).

No test was added or changed in this diff, so no new test is read against its group. `gaps.md` still labels the full suite, the repository-wide lint and the format check `unverified` with the orchestrator's broad run as their answerer, and that label is honest: no party has run them at 9696913a.

This round leaves nothing open. What comes due is the orchestrator's broad run at HEAD, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether G3's reading of the Claude Code 2.1.318 binary is right. The docstring's "the harness reads them" for the comment shapes rests on it, and it is carried from round 1 | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/frame/design.md:11` | the owner, where `frame/questions.md` Q1 is answered |
| The full suite, the repository-wide lint and the format check at 9696913a. The suite stays `unverified`, and this round ran two modules and one file's lint alone | `seal/threads/1793833681-an-import-inside-a-fence-is-not-charged/gaps.md` | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_payload_meter.py tests/behaviour/test_release_hygiene.py -q -p no:xdist` at 9696913a | exit 0, 90 passed |
| `uvx ruff check skills/verify/scripts/payload_meter.py` and `uvx ruff format --check skills/verify/scripts/payload_meter.py` | exit 0 each |
| `tests/skills/test_tmp_round3_shapes.py`, six shapes through `imports_of`, run once by `bin/test ... -q -s -p no:xdist`, then deleted | exit 0. Round 2's list-item fence then two fences: `a.md`, `c.md`. Round 2's inline opener closed in a later paragraph: `c.md`. List-item fence then a second list-item fence: `a.md`, `d.md`. List-item fence then a tilde fence: `a.md`. Block-quote fence then `@b.md`: `a.md`, `b.md`. Item `10. ` with its fence and closer indented four, then `@b.md`: `b.md` |
