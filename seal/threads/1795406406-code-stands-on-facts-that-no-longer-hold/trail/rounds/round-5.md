# Review round 5: 1795406406-code-stands-on-facts-that-no-longer-hold

```seal
target: f3ec679b8, fixes 0de0f2f00..f3ec679b8
```

This is the verifying round after round 4's fix pass, and the run's last round: `frame/plan.md` *Judgments of the run* records that the run stops here. The range `0de0f2f00..f3ec679b8` holds four commits. `d1eb77535` commits round 4's record. `cb228b694` adds that judgment row to `frame/plan.md`. `8ecc3048e` is the fix of round 4's two findings: two hunks of `remove_workflow`'s docstring and one hunk of `#mode`'s `--check` comment, all in `skills/implement/scripts/seal.py`. `f3ec679b8` appends the two close blocks to `trail/rounds/round-4.md` (executed: `git diff --stat 0de0f2f00 f3ec679b8`, and `git show 8ecc3048e` read whole). The round worked in a `git clone --no-local` of the branch worktree, checked out at `f3ec679b8`, under `<scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-5/clone`.

The work item's records were read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-3.md`, and `trail/rounds/round-1.md` to `round-4.md` for their coordinates and verdicts. No `pr.<lang>.md` stands, and none is owed, because `Commit and pull request language` is English. No `seal/parity.json` is declared.

Carried from round 4 and not established again: eight of its nine runs, 1a, 1b and 1d to 3a. They stand for the target because the fix changed no code they ran. `chain_check.py` has the same blob at `0de0f2f00` and at `f3ec679b8`, and `seal.py` parses to the same tree at both once each docstring is dropped (executed, probe row 0). Run 1c was run again. Also carried: round 4's reading of `docs/checks/the-routing-check.md` *At the pull request* for the premise "a commit made before the switch whose trailer names a work item still fails a ready pull request there", a line this fix did not change.

The fix's new sentence names two ways out of a pull request the left workflow fails: correcting the trailer, and removing the workflow. Round 4's probe ran neither, so this round ran both (probe rows 4a and 4b).

## Findings

No finding. The fix diff breaks nothing and makes no statement false.

## Confirmations

```seal
confirms: round-4#1
```
What holds: the fix pass claimed it applied round 4's paste-ready text as given; `seal.py:1865-1869` (read) carries it word for word. The docstring no longer says the removal is "never a repair". It says the removal is the person's choice, except on a pull request a pre-switch work-item commit fails. There correcting the trailer is the repair the check names, and the removal is the other way out. Both halves were run against the target. In run 1c the left workflow exits 1 on that commit and prints `UNDECLARED_TRAILER`, which ends "commit its `routing.md`, naming this branch, or correct the trailer". In run 4a the same pull request with the trailer corrected to `no work item` exits 0 and prints the `no work item` notice. That is the repair the check names. In run 4b the checks were installed while the root was shared and the switch was merged. On that repository `seal pr-checks remove` exits 0 and stages the deletion ("removed .github/workflows/hygiene.yml and staged the removal"). The check itself, run after the removal is committed, still exits 1. So the removal is a way out because the workflow no longer runs on the pull request, not because the check passes. The template's trigger is `pull_request` (`templates/setup/hygiene.yml:31-45`, read), and that event runs the workflow file the pull request's merge commit carries. The sentence on the older pin, unchanged, already relied on that. `tests/skills/test_seal.py#Test_pr_checks.test_accepts_remove_where_the_root_left_the_tree` holds the removal with no root, and it passed in the narrow run. `git grep -n -i -e 'never a repair' -e "person's choice" -e 'other way out'` outside `seal/threads/` and `evals/` matches `seal.py:1865` alone (executed). So no other statement of the old conclusion stands. The new sentence agrees with `left_workflow_line` (`seal.py:1724-1758`) and with the template's header (`templates/setup/hygiene.yml:17-23`). Both name `seal pr-checks remove` as what takes the checks out, and neither calls it a repair or not one (read).

```seal
confirms: round-4#2
```
What holds: `remove_workflow`'s docstring (`seal.py:1859-1862`) and `#mode`'s `--check` comment (`seal.py:2430-2435`) now cite `docs/checks/the-pull-request-check.md` *What the check reads at the pull request*, where they cited `chain_check.py#ROOT_LEFT_SAYS` (read). That heading stands at `docs/checks/the-pull-request-check.md:6`. Its paragraph over `check: nothing-declared-nothing-owed` (`:136-144`, read) says that where the tree has no top-level `seal` entry the check reads nothing as declared and judges the trailers as for any pull request that declares nothing. Runs 1c, 4a and 4b printed that, "this pull request declared neither way, so the review-chain check judged the commit trailers and nothing else", and never `ROOT_LEFT_SAYS`. So the citation states what both texts say for every pull request after the switch. `git grep -n ROOT_LEFT_SAYS` outside `seal/threads/` lists the constant (`chain_check.py:1935`) and its one use (`:2186`) alone (executed), as the fix pass claimed. The heading's spelling matches the citation that `chain_check.py:94`, `docs/forms/the-guarantee.md:25`, `docs/running/what-a-script-gates.md:56` and `tests/text/test_ci_gives_the_checks_what_they_need.py:431` already make (executed: `git grep -n 'What the check reads at the pull request'`). `trail/phases/phase-3.md:11` and `:28` still name the old citation. They are phase 3's account of what it did at its commit, so this round leaves them, as round 4 did.

What matched: `frame/design.md` *Scope* item 2 says the two `seal.py` texts "name the steps of G7 that pass where no root stands and cite no unit of `unverified_check.py`". G7 names the paragraph over `check: nothing-declared-nothing-owed` in `docs/checks/the-pull-request-check.md` as the rule that applies there. After the fix both texts cite that rule's section, and neither cites a unit of `unverified_check.py` (read: `seal.py:1853-1873`, `seal.py:2415-2438`).

What matched: the fix pass claimed that no assertion changed, no case was added, and `uvx ruff check`, `uvx ruff format --check` and `bin/test -q tests/skills/test_seal.py` (394 passed) exited 0. The fix diff touches only docstring and comment lines (read), and the docstring-stripped trees are equal (executed, probe row 0). The narrow run and both lint commands exited 0 in this round's clone, with 394 passed (executed). The fix adds no test, so no new test is read against its group. Its commit message says what the diff does (read).

What matched: the records read whole state nothing the target contradicts. The new row of `frame/plan.md` *Judgments of the run* says rounds 1 to 4 found 3, 1, 1 and 2 findings, and that round 3's carried a `regression:` line. The records hold those counts and that line (executed: a count of `severity:` and `regression:` lines per round record). The two quotes of `pr.md` stand word for word at the Judgment cells of the title row and the gate row of `frame/plan.md` *Judgments of the run* (read). `changelog.md` describes printed lines and no docstring, so the fix leaves it true.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at the target: the full suite, the repository-wide lint and the format check (`Broad gate` of `seal/config.json`). The suite stays `unverified` (contract rule 2). This round leaves nothing open, so the orchestrator's broad run is next, and the sealer's spawn after it | `seal/config.json` | the orchestrator's broad run |
| That a pull request which deletes `.github/workflows/hygiene.yml` does not run that workflow. This is GitHub's behaviour for the `pull_request` event, read from the template's trigger and not run here. The older-pin sentence of `remove_workflow`'s docstring already relied on it before this fix | `skills/implement/scripts/seal.py:1867-1869`, `templates/setup/hygiene.yml:31-45` | the repository owner, on the first pull request that removes the workflow |
| The close-issues workflow without the label step, on a push to `main` | `.github/workflows/close-issues-on-release.yml` | the close-issues run when this release reaches `main`, read by the repository owner (`gaps.md`) |

## Probes

| Command | Result |
|---|---|
| `python3 -I <scratchpad>/1795406406-code-stands-on-facts-that-no-longer-hold/round-5/test_tmp_round5_ways_out.py <clone> <scratch>`, row 0 | `seal.py` at `0de0f2f00` and at `f3ec679b8` parse to equal trees with docstrings dropped: True; `chain_check.py`'s blob is the same at both: True |
| the same run, row 1c: left workflow in CI, ready, a commit with trailer `some-item` | exit 1; the "declared neither way" notice, then `UNDECLARED_TRAILER` |
| the same run, row 4a: 1c with the trailer amended to `no work item` | exit 0; the same notice, then the `no work item` notice |
| the same run, row 4b: checks installed with the shared root (`seal pr-checks install`, exit 0, pinned to v0.38.6), the switch merged, a commit with trailer `some-item` | the check exits 1 as in 1c; `seal pr-checks remove` exits 0 and stages `D  .github/workflows/hygiene.yml`; with the removal committed the check still exits 1 on the earlier commit |
| `bin/test -q tests/skills/test_seal.py` in the clone at `f3ec679b8` | 394 passed, exit 0 |
| `uvx ruff check` and `uvx ruff format --check` over `skills/implement/scripts/seal.py` | both exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline 459116a4e --root <the branch worktree> --worktree`, run on this record before hand-back | exit 0 on an unknown pull request state; it names the gate record and the guarantee as not yet written, refuses no line of this record, and prints no notice at a line of the design naming a pin or a copy |
