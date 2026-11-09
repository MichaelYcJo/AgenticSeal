# Review round 2: 1794187229-the-body-carries-the-seal-mark

```seal
target: e15a6ea8, fixes 89de04fa..e15a6ea8
```

This is the verifying round after round 1's fix pass. The code under review is the diff from `89de04fa`, round 1's target, to `e15a6ea8`. It holds the round 1 record `9c6bb6be`, the `pr.md` repair `a61f0fb0`, the fix `1012b256`, the docstring rewrap `722f0727`, the close blocks `628d9606` and the frame fold `e15a6ea8`. It was read in a scratch clone at `e15a6ea8` (`<scratchpad>/1452-r2/clone`). `routing.md`, the three frame files, `gaps.md`, `changelog.md` and `pr.md` were read whole at `e15a6ea8`. The fix diff touches no phase record, so the four records under `trail/phases/` state their own commits and were not read again. `seal/parity.md` is not declared, so no parity comparison applies. The record language is English, since `seal/config.md` holds no `Record language` row.

Carried from round 1 and not searched again: the guarantee arm's call to `follows` with `args.baseline` (`skills/code-review/scripts/chain_check.py:1712`, at `:2140` of round 1's target), the probe shape of finding 1, the `Test_body` fixtures `bodied`, `payload` and `check`, and the `MARK_LINE` fixture at `tests/skills/test_pr_body.py:283`. Every verdict below was reached again on the target.

The fix pass's account was read as a claim and checked against the commits. It said `722f0727` rewraps the docstrings and changes no word. `git diff 1012b256 722f0727 --word-diff=porcelain` shows no changed word (executed). It said `628d9606` appends the close blocks. That commit adds 20 lines to `trail/rounds/round-1.md` and changes nothing else (executed, `git show --stat`). It said `e15a6ea8` folds the `base` parameter into the frame. That commit changes *Scope* item 2 and *Data & interfaces* in `frame/design.md` and adds two rows to `frame/plan.md` *Judgments of the run* (read).

## Findings

No finding this round.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `body` takes `base` and passes it to `compared` (`skills/code-review/scripts/chain_check.py:1780`, `:1803-1805`). `main` passes `args.baseline` (`:2153`), the base the guarantee arm reads at `:2146`. `compared`, `seal_mark` and `_seal_at_head` carry it through, and `_seal_at_head` reads `base or target["base"]` (`skills/code-review/scripts/pr_body.py:842`, `:852`, `:464`, `:486`, `:419`). `main --check` and the writing run pass no base (`pr_body.py:902`, `:915`), so `seal pr-body` at the branch head still reads the guarantee's own base. `test_accepts_the_body_at_a_merge_past_a_later_base_commit` (`tests/skills/test_chain_check.py:3215`) builds round 1's probe shape. That shape is a guarantee base written as a SHA, one base commit after the seal, and HEAD detached at the merge. The close claims the case goes red under the mutations. With `base=base` dropped from `body`'s call, the case failed on the line round 1 quoted, "reads ``, then `<img src=...raw/HEAD/...>`, which the records do not give" (executed). With `args.baseline` dropped from `main`'s call, the case failed alone among the 16 cases of `Test_body` (executed). The finding's claim holds on the target.

```seal
confirms: round-1#2
```
What holds: `pr.md` now carries the six quotes round 1 asked for, above `Closes #1452.` (`pr.md:9-14`). All 16 quotes of `pr.md` stand word for word at the file each names, with runs of whitespace collapsed. The four failure-direction quotes stand inside the paragraph at `frame/design.md:144-150`, and the two *Removes* quotes inside the paragraph under the table at `frame/design.md:308-314` (executed: a `python3 -I -c` comparison of each list line against its file and its paragraph, all `True`). The second quote says a refusal is cleared by one `seal pr-body` run. That is true at the merge commit since round-1#1's fix, as the confirmation above shows. The *Fixed* item positions, first, third and fourth, and the *Updating*, prefix-row and second *Not verified* coordinates matched on reading.

```seal
confirms: round-1#3
```
What holds: `BODY_NONE_HOLDS` stands beside `BODY_SPLIT` (`skills/code-review/scripts/chain_check.py:1754-1757`). `body` picks between the two sentences by whether any item holds `pr.md` (`:1801-1802`). The module docstring's `body` row and `body`'s docstring name both shapes (`:76-87`, `:1780-1795`), and so does `changelog.md`'s first *Fixed* item (read). The close claims `test_names_the_body_as_not_read_for_two_work_items_without_pr_md` (`tests/skills/test_chain_check.py:3415`) goes red with `BODY_SPLIT` used for both shapes. Under that mutation it failed on the two-holder sentence at index 0 (executed). `test_refuses_a_missing_pr_md_at_its_path` (`:3435`) went red when the record's cause was placed on the work item's directory. Its failing line read `seal/threads/1791999999-a-work-item:0  is not there; ...` where the case asks for `.../pr.md:0` (executed). Each new case covers a branch no other case of `Test_body` reaches, since each went red alone under its mutation.

```seal
confirms: round-1#4
```
What holds: the two-manifest case's second manifest lacks `version`, and the case compares the set of lines with `MARK_LINE` (`tests/skills/test_pr_body.py:628-647`). The close claims the case goes red with `"version"` put back into `MARK_FIELDS` (`skills/code-review/scripts/pr_body.py:239`). Under that mutation it failed alone in `test_pr_body.py`, the set holding None beside the line (executed). So it now holds a fact no other case of `Test_seal_mark` holds: a manifest with no `version` still gives the mark.

What matched: the frame fold at `e15a6ea8`. *Scope* item 2 and *Data & interfaces* now state `compared(item, body, root, manifest=None, base=None)`. They say `chain_check.py#body` gives the `--baseline` value and `main --check` leaves the base to the guarantee's own, which is what `chain_check.py:2153` and `pr_body.py:902` do (read). The two new rows of *Judgments of the run* name their grounds and the document judged against. The row on round 1's *Not judged* bot shape answers that row (read). No other sentence of the seven files read whole is contradicted by the target (read).

What matched: the three touched modules pass at the target (executed: `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/text/test_ci_gives_the_checks_what_they_need.py -q` in the clone, exit 0, 303 passed). The label is honest: `gaps.md` *Not verified* still names the full suite, the lint and the format check at the branch's last commit as unrun, with the orchestrator's broad run as the answerer (read).

Weighed and left without a finding:

- A branch that merges its base after the seal. In that shape, a local `seal pr-body` reads the guarantee's base and would find the merged base commits after the seal. The arm reads `--baseline` and would not. The flow does not reach this state. `skills/code-review/orchestration.md:322-338` has the orchestrator run the broad gate and the sealer again after such a merge, and the new guarantee's base then covers the merged commits.
- `BASE_UNSEEN` reads "the guarantee names the base" (`pr_body.py:251-254`), which would be false for a base the check gave. The arm never reaches it, because `chain_check.py:2014` exits 2 before any arm runs where `--baseline` does not resolve (read).
- `722f0727` left two docstring lines past 88 columns (`chain_check.py:1792`, `pr_body.py:848`). `ruff.toml` holds `line-length = 88`, and other lines of both files already run past it (`chain_check.py:91`, `pr_body.py:61`). Such a line only reads badly, so it is no finding.

`python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.36.0 --root <the branch worktree> --worktree` printed no notice of a test pin or a copy at a line of `frame/design.md` (executed). No finding here comes from such a notice.

Nothing is open after this round. The orchestrator's broad run comes next, and then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| how GitHub shows an annotation on a directory at line 0, which no case can run | `gaps.md` *Not verified*, the second row | the first `hygiene` run that refuses a body, read on the pull request's checks |
| the full suite, the repository-wide lint and the format check at `e15a6ea8`; this round ran three modules only | the branch | the orchestrator's broad run |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py tests/text/test_ci_gives_the_checks_what_they_need.py -q` in the clone at `e15a6ea8` | exit 0, 303 passed |
| `bin/test tests/skills/test_pr_body.py tests/skills/test_chain_check.py -q -p no:xdist` with three mutations made through the Edit tool: `base=base` dropped from `body`'s call to `compared`, `BODY_SPLIT` used for both shapes, and `"version"` added to `MARK_FIELDS` | exit 1, 3 failed and 273 passed. The three failures were the merge case, the no-holder case and the two-manifest case, each on the line its guard names |
| `bin/test tests/skills/test_chain_check.py::Test_body -q -p no:xdist` with `args.baseline` dropped from `main`'s call to `body` | exit 1, the merge case alone failed of 16 |
| `bin/test tests/skills/test_chain_check.py::Test_body -q -p no:xdist` with a record's cause placed on the work item's directory | exit 1, `test_refuses_a_missing_pr_md_at_its_path` alone failed, its output reading `seal/threads/1791999999-a-work-item:0  is not there; ...` |
