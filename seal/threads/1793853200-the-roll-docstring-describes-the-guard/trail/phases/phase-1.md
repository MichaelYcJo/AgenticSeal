# Phase 1: 1793853200-the-roll-docstring-describes-the-guard

## What this phase found

**The frame holds against the tree.** `git diff --stat 31558c76 669d5958` lists this work item's `routing.md` and its three frame files alone, so the tree outside the work item is v0.32.3, the tree the frame dates its coordinates to (executed). `.github/scripts/roll_flow_measurement_issue.py` was read whole at 669d5958. Each passage `frame/design.md` D1 items 1 to 5 names stands at the lines D1 gives: the lag paragraph at `:68-80`, the guard paragraph at `:111-117`, the transaction clause at `:136-138`, `open_flow_measurement_issues`'s docstring at `:316-322` and `landed_create`'s at `:447-455`. D1 item 6's sentence stands in `tests/github/test_roll_flow_measurement_issue.py` at `:256-258` (read). Judged against `frame/design.md` *Grounding* and the crafter's rule *The frame is judged before it is built to*.

**Departures from the frame: none in what was built.** Each edit is the one D1 states. The words were left to the build, and these choices were made:
- D1 item 1: the paragraph names the kind of write before it names the direction, and says what the extra issue is ("the closed issue still listed as open"). The retry is stated as `RETRY_DELAY_SECONDS` in place of "a short sleep", so the paragraph names the constant both lookups use. The grounds for not retrying two or more are the invariant paragraph above and the undercount #109 measured, in that order.
- D1 item 4: `open_flow_measurement_issues`'s docstring cites the module docstring for which way a lag moves a reading, then states its own decision: one retry on an empty reading, none on two or more, so `main` fails loudly.
- D1 item 5: `landed_create`'s docstring keeps its condition and cites "the module docstring's rule for a lag behind a close" for why `closed_number` can still be in the reading. Its last sentence, on the retry and a lag behind the create, stays as it read, reflowed.
- D1 item 6: the test docstring reads "A reading of two or more fails loudly without the retry: the one retry is for an empty reading alone."
- The guard and transaction paragraphs are reflowed to the module docstring's wrap, with no word changed beyond D1 items 2 and 3.

S3's comparison read each file at the two commits through `git show` in the worktree rather than from a scratch clone, so it made nothing to remove. The input is the same blob either way, so the result does not depend on that choice. Judged against `frame/design.md` *User scenarios & acceptance* S3.

**No case is written new, and no `seal mutate` run is owed.** The phase changes docstring text alone and adds no behaviour, so no unit has anything to break. For a docstring inside source, `skills/verify/SKILL.md` *The narrow command still has to be able to fail* names "that the module still imports" as what can fail, and S4's run imports both modules. `frame/plan.md` *Alternatives considered* A4 and A5 put a pinning case and the two mutation cases out. Judged against the crafter's steps 5 and 6.

**S1** (executed at 93063507): `git grep -n -i -E "only ever undercount|can only undercount|never one with an extra|never what a .*lag produces|never a lag artifact|no longer empty"` over the script and `tests/github/test_roll_flow_measurement_issue.py` printed nothing, exit 1. This is a sample over spellings, and S2 is the proofer's reading.

**S3** (executed): a Python script removed every module, class and function docstring with `ast` and compared `ast.dump` of each file at 31558c76 and at 93063507. It removed 14 docstrings from the script and 40 from the test module at each commit, and both dumps were equal, exit 0. Run against `6310a6e8`, where the script's `__main__` block did not yet exist, the same comparison printed `DIFFER`, exit 1, so it can fail on a code change. The script was in the scratchpad and was removed after these two runs.

**S4** (executed at 93063507): `bin/test tests/github/test_roll_flow_measurement_issue.py tests/behaviour/test_a_release_rolls_the_flow_measurement_issue.py -q` ended 40 passed, exit 0; `--co` collected 37 cases from the first module and 3 from the second. `uvx ruff check` and `uvx ruff format --check` on the script and the test module both exited 0, before that commit.

**The phase boundary is narrower than the verify table's row, by the spawn's instruction.** `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* puts the modules that read a changed path at the phase boundary. Twenty-one modules under `tests/` name `plugin.json` (`git grep -l plugin.json -- tests`), and several read the records under `seal/threads/`. The spawn said to run the two roll modules and ruff on the touched files alone, and contract rule 3 follows a prompt that narrows. Those modules were not run, and `gaps.md` *Not verified* names the orchestrator's broad run as their answerer.

**The version move** (executed): `.claude-plugin/plugin.json`'s `version` reads `0.32.4`, and `git grep -n "0\.32\.3"` outside `seal/threads/` printed only that line before the move. *Scope* item 5 and `frame/plan.md` *Judgments of the run* place the move here. The fragment does not mention it, as the 0.32.3 release's fragment for #1375 did not.

**A removal the frame's `## Removes` did not name:** none.

**Other statements of the reworded rule across the tree** (executed: `git grep -n -i -E "undercount|short a result|extra issue|lag artifact|no longer empty|search.index|index lag|lag(s|ging)? (behind|the write)"` outside `seal/threads/` and `.test_durations`). This list is a sample by wording (contract rule 12). Beyond this phase's own lines it hit two. `tests/github/test_roll_flow_measurement_issue.py:174-178` says the retry exists for a lag on an empty reading, which stays true; *Scope*'s out-of-scope list keeps it. `skills/verify/seal-arms.md:63` is about a walk that skips files, not this lag. No document under `docs/` states the lag's direction (`frame/design.md` *Rule changes*).
