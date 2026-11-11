# Review round 3: 1794376287-check-lines-ride-in-every-preload

```seal
target: a7c86e202, fixes ab8bddb3a..a7c86e202
```

This is the verifying round over round 2's one finding. The range `ab8bddb3a..a7c86e202` holds five commits: round 2's record (`3d4f46af5`), the framer's fold of the finding (`e8830bd8d`), fix pass 2 (`d322c0cb7`), its `gaps.md` row (`71bfe52fb`) and the close block (`a7c86e202`) (executed, `git log --oneline`). Outside `seal/`, the range changes `README.md`, `README.ko.md` and `skills/settle/rule-changes.md`, one hunk each (executed, `git diff --stat`). Every command ran in a `git clone --no-local` checked out at `a7c86e202`, under the round's scratch directory `<scratchpad>/1794376287-check-lines-ride-in-every-preload/round-3/clone`. The branch worktree received this record and nothing else.

The records read whole at the target are `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`, `trail/rounds/round-1.md` and `trail/rounds/round-2.md`. Both language keys of `seal/config.json` are English, so no `pr.<lang>.md` stands. No `seal/parity.json` stands, so no original is compared. The issue still has no comment (executed, `gh issue view 1475 --json comments`, from the main checkout, since the clone has no GitHub remote).

Carried from rounds 1 and 2 and not re-established: S1's zero lines in the six files, S2's 32 targets, S4's preload figures, the four re-sliced units reading their base text, D2 read against its group, and round 1's probe of the 47 pairs. The fix range touches none of the files those rest on. Re-derived here: the fix of round 2's finding in each of its four places, the frame's fold, the new `gaps.md` row, the close block's claims, `seal rules --check`, and every verdict.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: no statement in the tree now says every rule of the agent definitions and the contract is held by a case. Each of round 2's four snippets stands word for word in its file: the English bullet in `README.md`, the Korean bullet in `README.ko.md`, the last sentence of `changelog.md:4`, and D1 in `skills/settle/rule-changes.md` (executed, a `python3` substring test of each fenced snippet of `trail/rounds/round-2.md` against its file, raw and with whitespace collapsed). The bullet stands at `README.md:441-446` and `README.ko.md:436-441`, and D1 at `skills/settle/rule-changes.md:118-128`, as the close block gives them (read). D1's block at `frame/design.md:79-93` stands in `skills/settle/rule-changes.md` word for word once whitespace is collapsed (executed, the same test). Both editions now say a rule there is held by the cases that read it where any do, and by review alone where none does. The cited section, *A rule has one shape* (`skills/settle/rule-changes.md:88`), states both halves: D1's "A rule there that a case holds is still held by it." at `:121-122`, and "A rule no case holds carries no check line, and review reads it." at `:94` (read). The two rules the finding named still have no case. `git grep -l -i -F` of their words over `tests`, `evals`, `lib`, `bin` and `.github` finds no file at `896f50cab` or at HEAD, except "A check that refuses", which matches the comment at `tests/behaviour/test_chain_hooks_hardening.py:945` about a check that refuses a phrase by spelling (executed). That comment does not pin contract rule 18, so the claim holds. Round 2's probe row reports "no file" for the same search, so this round corrected the carried fact and did not take it over. G10 now names that comment as the one hit (read). `git grep -n -i -E` over the tree for "still held by its cases", "cases still hold", "their cases still" and "held by their cases" finds the old reading only in round records and in the dated row `frame/plan.md:52`. Each of those states the commit it was written at (executed).

What matched: the framer's fold at `e8830bd8d`. *Scope* item 13 (`frame/design.md:50`) now cites round 2's finding 1 and gives the bullet as the fix wrote it. G10 (`:18`) now says the old bullet, after the work, calls every rule of the six files held by review alone, though many are held by cases, and that some are held by none. It names the framer's count rule and contract rule 18. Its coordinates `README.md:441-442` and `README.ko.md:436-438` are those of `f47b1d5ae`, the commit its section is dated to, which round 2 checked (carried). `frame/plan.md:11` adds the case of a rule no case holds to the failure scenario. Its "the search finds nothing" follows "finds nothing in the file to name them", and reads as finding no case of that rule. That matches the probe above. The new row at `frame/plan.md:53` records the judgment, its grounds and the docstring it rests on. That docstring stands at `tests/text/test_the_agent_contract_holds_the_universal_rules.py:16-20`, where it leaves a rule's sentences to review (read).

What matched: S3. `bin/seal rules --check` exits 0 and prints `seal rules: all 179 check lines in 69 rule files hold.` at `a7c86e202`, the count the close block gives (executed).

What matched: the two README cases and the modules around D1 and D2. One `bin/test` command over `tests/behaviour/test_both_editions_carry_the_same_folds.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/skills/test_rule_changes.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/behaviour/test_this_repository_passes_its_own_checks.py`, `tests/github/test_rules.py` and `tests/behaviour/test_the_set_a_work_item_always_has.py` gave 284 passed, exit 0 (executed). The fix range adds no test, so no case is read against its group.

What matched: S7. `git diff --name-only 896f50cab...HEAD -- ':!seal/'` lists the same 17 files as at round 2: the 15 of *Scope* items 1 to 12 and the two READMEs of item 13 (executed).

What matched: `gaps.md` row 4. It was added by `71bfe52fb` with no row taken out (read, the diff). It says fix pass 2 changed `changelog.md` as well as fix pass 1's three files, ran the same command, and calls the list the same sample, with the orchestrator as its answerer. That search did not look for readers of `changelog.md`. So this round listed every test file outside `tests/text` and `tests/behaviour` that names `changelog`: `tests/github/test_publish_release_note.py`, `tests/skills/test_chain_check.py`, `tests/skills/test_pr_body.py` and `tests/skills/test_settle.py` (executed, `git grep -l -F`). The first and third build their work items in fixtures and read no work item of the tree (read, `tests/github/test_publish_release_note.py:407-428`, `tests/skills/test_pr_body.py:274`). The other two are in the README search's list. So the row's label is honest. The count of 4,669 passed and 9 skipped was not re-run.

What matched: `pr.md` and the body. Its four quotes still stand word for word at `frame/plan.md:17`, `:18`, `:49` and `:50`, because the fold appended its row after `:52` (executed, `grep -n -F` on each quote). The tree's `bin/seal pr-body` composed the body into the round's scratch directory with exit 0 (executed).

What matched: the rest of the records that state the present. `routing.md`, `frame/questions.md`, `trail/phases/phase-1.md`, the changelog's *Removed* items 1 and 3, its *Changed* item and its *Process changes* row are unchanged in the range, and nothing in the fix diff contradicts them (read).

What matched: the chain check over this record. `python3 skills/code-review/scripts/chain_check.py --baseline 896f50cab --root <the branch worktree> --worktree` exited 0. It printed no notice at a line of `frame/design.md` naming a test pin or a copy. Its other lines say git carries no `trail/gate.md` and no `guarantee.md` yet, which the orchestrator's broad run and the sealer write after the rounds (executed).

This round leaves nothing open. What comes due is the orchestrator's broad run, `seal gate --record`, and then the sealer's spawn.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at HEAD, and fix pass 2's run of 4,669 passed and 9 skipped, which this round did not re-run | the work item's HEAD | the orchestrator, by `seal gate --record` |
| Whether the sealer withholds on a missing or a stale `trail/gate.md` now that the rule naming the two evals is gone | `evals/behaviour/sealer/rule-sealer-no-gate/`, `evals/behaviour/sealer/rule-sealer-stale-gate/` | the owner, by the release's eval run, as `gaps.md` row 5 names |
| D2's `seen red` at the base and with one line restored, claimed in `trail/phases/phase-1.md:21` and `:29` | `tests/text/test_every_agent_reads_the_contract.py` | the sealer, by its sample |

## Probes

| Command | Result |
|---|---|
| `python3` substring test of each fenced snippet of `trail/rounds/round-2.md` against `README.md`, `README.ko.md`, `changelog.md` and `skills/settle/rule-changes.md`, and of D1's block in `frame/design.md` against `skills/settle/rule-changes.md`, raw and whitespace collapsed | every snippet found, both ways |
| `git grep -l -i -F` of the words of the framer's count rule and of contract rule 18 over `tests`, `evals`, `lib`, `bin` and `.github`, at `896f50cab` and at HEAD | no file, except "A check that refuses" in `tests/behaviour/test_chain_hooks_hardening.py` at `:945`, a comment on another check |
| `bin/seal rules --check` at `a7c86e202` | `all 179 check lines in 69 rule files hold.`, exit 0 |
| `bin/test` over the seven modules named under *Confirmations*, `-q` | 284 passed, exit 0 |
| `git grep -l -F changelog -- tests`, outside `tests/text` and `tests/behaviour` | four files, none reading a work item of the tree outside the README search's list |
| `bin/seal pr-body --body <scratch>/pr-body.md` over the work item | exit 0 |
