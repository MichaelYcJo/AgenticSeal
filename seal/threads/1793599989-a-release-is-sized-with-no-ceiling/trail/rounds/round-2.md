# Review round 2: 1793599989-a-release-is-sized-with-no-ceiling

```seal
target: f59167a7, fixes 2ee19260..f59167a7
```

This is a verifying round. Its target is the diff of round 1's fixes, `2ee19260..f59167a7`, on the branch whose base is `release/v0.28.1`. It was reviewed in a `git clone --no-local` of the branch worktree at `f59167a7`, under `<scratchpad>/1289-round-2/clone`. `release/v0.28.1` does not resolve in the worktree, so every command that names the base names `origin/release/v0.28.1`, which `git rev-parse` gives as `40e6c23e` (executed). No `seal/parity.md` is declared, so the round block holds no `original:` line. The target line takes the verifying form `fields.py` gives, `<sha>, fixes <a>..<b>`, which names no base.

The diff holds four commits: `51bfa4ed` (finding 3, the test module and `gaps.md`), `c72cff98` (findings 1 and 2, `changelog.md`), `75b19965` (round 1's close blocks) and `f59167a7` (the orchestrator's fold into `frame/design.md` and one `frame/plan.md` row). This round stayed inside that diff, and every place it opened outside it is named below.

Facts carried from round 1, not re-established: at the base, `read` had one caller passing `root`, `restatements` at `:153` (round 1's `## Probes`, `git grep -n 'read(' 40e6c23e`); and the release-branch rule stands at `docs/branch-and-release.md:329`, under the heading at `:120`. The second was re-opened and still reads as round 1 quoted it (read). Every verdict below was reached at this target.

The implementer's account, claim by claim:

- Claimed in finding 3's close block: `read` is `def read(rel):` and opens `os.path.join(ROOT, rel)`, Ruff check and format exit 0, and the module passes. `tests/behaviour/test_a_release_is_sized_by_a_criterion.py:24-26` reads so (read). `uvx ruff check` and `uvx ruff format --check` on the module exited 0, and the module passed under `bin/test` (executed).
- Claimed in finding 1's close block: no pending design changes the paragraph the `to` now cites. One pending design, `seal/threads/1793582903-each-entry-links-its-pull-request/frame/design.md:188-200`, names the section *Work accumulates on a release branch*. Its `from` is "and writes each under an HTML comment naming its work item", a sentence about fragments, not the paragraph at `:329` on where a `feat:` ships, and it keeps the heading. The cited section therefore still stands after the settle (read).
- Claimed by the orchestrator's spawn prompt: the crafter re-parsed the folded `to` with one op, no errors, nothing unread, placed. This round parsed the committed design and got the same result (executed, `## Probes`).
- Claimed by the orchestrator's spawn prompt: `chain_check.py` exited 0 after the fold, printed no pin notice, and named the verifying round owed for `51bfa4ed`. This round ran it over the worktree before writing this record and got the same (executed, `## Probes`).

## Findings

No finding. The diff adds one changed unit of code, `read` (`tests/behaviour/test_a_release_is_sized_by_a_criterion.py:24-26`), and no new test, so no test is read against a group.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the folded `to` at `frame/design.md:91-95` is the five lines finding 1's close block gives, character for character (read, `git diff 2ee19260..f59167a7`). An overflowing issue now "moves to a later `release:` milestone, and a `feat:` moves only where `docs/branch-and-release.md` *Work accumulates on a release branch* sends it." The paragraph at `docs/branch-and-release.md:329` sends a `feat:` in a patch-numbered milestone to the planned minor whose goal it shares, or renames the milestones forward. The `to` defers to it and states no destination of its own for a `feat:`, so the two documents give one answer (read). *Scope* item 1 at `frame/design.md:39` now states the same rule as the close block wrote it (read). `changelog.md:3` reads "moves to a later release, and a `feat:` only where `docs/branch-and-release.md` *Work accumulates on a release branch* sends it" (read). `rule_changes.parse` with root `docs` returns one op, `errors=[]` and `unread=[]`, and `apply_op` places it with no refusal. In the applied document the section holds no "next release." and no "ceiling", and the `to`'s check line stands as its paragraph's last line, before **What the criterion does not change.** (executed). `tests/behaviour/test_a_cited_section_stands_in_its_file.py` passed (executed).

```seal
confirms: round-1#2
```
What holds: the `to` at `frame/design.md:95` reads "The judgment weighs work items rather than ticket numbers.", `changelog.md:3` reads the same, and *Scope* item 1 at `frame/design.md:39` reads "the judgment weighs work items, not ticket numbers" (read). The applied document's section holds no "judgment counts" (executed). `git grep -n -i -E 'next release|counts work items|judgment counts'` over the work item finds the old wording only in round 1's record, which quotes it (executed).

```seal
confirms: round-1#3
```
What holds: `read` takes `rel` alone and joins it to `ROOT` (`tests/behaviour/test_a_release_is_sized_by_a_criterion.py:24-26`, read). Its one caller, `flat` at `:35`, passes no root, and `os` is still used, so no import is left unused (read; Ruff check exit 0, executed). The module and `tests/text/test_the_release_tail_does_not_end_at_the_tag.py`, which cites the module's reader, passed (executed). `gaps.md` *Not done* now reads `nothing` (`gaps.md:13`, read). `trail/phases/phase-1.md:10` still records the build's decision to keep the parameter. That line is a record of what phase 1 did at `ea581e55`, and finding 3's close block says where the decision was reversed, so a reader of the work item finds both. The tree states no copy of the old signature: `git grep -n -E 'root=ROOT|read\(rel, ?root'` over `tests/` names other modules' own helpers only (executed).

```seal
confirms: none
```
What matched: S2 holds at the target. `chain_check.py --baseline origin/release/v0.28.1 --root <branch worktree> --worktree`, run before this record was written, exited 0. It printed no pin notice and no line at `frame/design.md`. Its lines named the verifying round owed for finding 3 and for `51bfa4ed`, and the not-yet-written `trail/gate.md` and `guarantee.md` (executed). No notice was printed at a design line, so this round takes no finding from a notice.

```seal
confirms: none
```
What matched: the `frame/plan.md` *Judgments of the run* row added in `f59167a7` records the fold, its grounds and the documents judged against. `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* (`:25`) asks the orchestrator to fold a decision made after the frame into `frame/design.md` in place and write it as one row of that table in the folding commit, and `f59167a7` does both (read). `tests/text/test_no_passage_is_pasted_into_a_second_file.py` passed over the changed records (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck. The suite is `unverified`, as `gaps.md:7` labels it, and that label is honest: no party has run it on this branch | the tree at `f59167a7` | the orchestrator's `seal gate --base release/v0.28.1 --record 1793599989-a-release-is-sized-with-no-ceiling`, then the sealer's spawn |
| S3's mutation results, carried from round 1 as read and not re-run | `trail/phases/phase-1.md:15-23` | the sealer, which samples the crafter's claims |

This round leaves nothing open. What comes due is the orchestrator's broad run, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/test -q -s -p no:xdist -p no:cacheprovider test_tmp_round2.py tests/behaviour/test_a_release_is_sized_by_a_criterion.py tests/text/test_the_release_tail_does_not_end_at_the_tag.py`, the probe parsing `frame/design.md` with `rule_changes.parse` (root `docs`) and placing the op with `apply_op` | exit 0, 9 passed; one op, `errors=[]`, `unread=[]`, `apply_op` gave no refusal; the three folded phrases stand once each in the applied section, and "next release.", "judgment counts" and "ceiling" stand in it not at all; the probe file was deleted after the run |
| `uvx ruff check` and `uvx ruff format --check` on `tests/behaviour/test_a_release_is_sized_by_a_criterion.py` | both exit 0 |
| `bin/test -q -p no:cacheprovider tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/text/test_no_passage_is_pasted_into_a_second_file.py` | exit 0, 50 passed |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.28.1 --root <branch worktree> --worktree`, before the record | exit 0; no pin notice; lines for finding 3's owed verifying round, the record behind HEAD at `51bfa4ed`, `trail/gate.md` and `guarantee.md` |
| `git grep -n -i -E 'next release\|counts work items\|judgment counts\|root=ROOT\|read\(rel, root'` over the work item and the module; `git grep -n -E 'root=ROOT\|read\(rel, ?root' -- tests` | the old wording only in round 1's record and `trail/phases/phase-1.md:10`; no copy of the old signature in `tests/` |
