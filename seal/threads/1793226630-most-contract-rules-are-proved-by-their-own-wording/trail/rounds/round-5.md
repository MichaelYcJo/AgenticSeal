# Review round 5: 1793226630-most-contract-rules-are-proved-by-their-own-wording

target: c7daab03, fixes d857348d..c7daab03

## Findings

None. The sweep below found no count, file count, bound or reader that is
still wrong in the work item's records, frame, changelog or the comment on
#1111.

## Confirmations

confirms: round-4#1
The close is `deferred #1111`, and the grammar gives that close to this
repair. `docs/the-review-record.md:141-145` closes a repair made outside the
tree, "an issue or a pull request body edited", as `deferred <where it was
repaired>`, and such a close owes this round nothing. The caller asked for
the close to be weighed anyway, so it is weighed here. The fix range
touches only `round-2.md` and `round-4.md` (executed `git diff
d857348d..c7daab03 --stat`), and no path on the finding's `location:` line
changed, which fits a repair made on the tracker.

Claimed: the comment now carries all 39 rows and the total, and the 182
sentence says 174 lines are in the 39 modules and 8 in the contract module.
Found: `issuecomment-6483485058` was edited once, at
2026-10-28T23:41:06Z (executed, its `userContentEdits` through `gh api
graphql`). It holds 39 module rows (executed `grep -c`). Its 39 rows and
its total row, module name and number, equal `phase-2.md:32-71` cell for
cell (executed `diff` of the two lists, exit 0). The rows sum to 255
(executed `awk`). Its module names equal the `tests/text` modules at
`ee746f3b` without the contract module (executed `diff`, exit 0), and the
module list at HEAD equals the one at `ee746f3b` (exit 0).

The rewritten 182 sentence holds. The issue's grep, run per file with GNU
`grep` over `tests/text` at `0b75346f`, gives 182: 174 outside the
contract module and 8 in it. Over the 39 modules at `ee746f3b` it gives 168
(executed). One module of the 39,
`test_no_case_tells_the_agent_it_is_evaluated.py`, is not in the tree at
`0b75346f`. So the 174 lie in 38 of the 39 modules. That module gives 0
under the grep at `ee746f3b` (executed). The sentence names no module count
for the 174, so it is not wrong, and "the same grep over the 39 modules"
compares like with like.

Every other sentence of the comment equals the records, re-run this round:
the ten largest modules and their numbers, "16 modules have 0" and "9 or
fewer" (16 rows at 0, the largest of the rest 9), the left-out kinds summing
to 124 and 279 with the commands, the three Q2 lines, and 75 and 81 against
`phase-2.md:71`. The issue's second *Done when*, "each module with its
number", now holds on the issue.

One departure from round 4's paste-ready text is no defect. Round 4 asked
for the table "in place of" the sentence that points at `phase-2.md` on the
branch. The edit kept that sentence and added the table after it. The
sentence is true. The per-module numbers no longer depend on it, and only
the left-out line list sits behind it, which the *Done when* does not ask
for. Executed and read.

confirms: round-4#2
`7cb74da2` changes one line of `round-2.md`, line 128, and in it only "in 5
files" to "in 4 files" (executed `git diff d857348d..c7daab03`). That path
is the finding's `location:`, so the close meets
`docs/the-review-record.md:101-108`, and a correction to a record a commit
made closes `fixed <commit>` (`docs/the-review-record.md:140-141`). I re-ran
round 4's executed lines. `git grep -l -E '^\s*check:.*evals/' -- ':!seal/'`
lists 4 files at `7cb74da2` and at HEAD, and the same pattern with `-n`
prints the 10 lines round 1's answer lists:
`agents/proofer.md:74`, `agents/sealer.md:125`, `:130`, `:136` and `:148`,
`skills/agent-contract/SKILL.md:46`, `:78` and `:102`, and
`skills/code-review/SKILL.md:38` and `:140`. The unanchored pattern
`check:.*evals/behaviour` lists 5 files, the fifth
`tests/github/test_rules.py`, whose matches at `:266` and `:503` are the
two fixture strings that `round-2.md:111-112` names. No other record states
"5 files" except round 4's own heading, grounds and quoted fix, which are
that round's and stay. The orchestrator wrote the verdict and answer
because no fix pass ran, the form rounds 3 and 4 accepted. The edit made no
new defect in the line. Executed.

confirms: none
The sweep for a wrong count, file count, bound or reader found none
standing. Each claim below was re-run at HEAD or read at the commit it
names.

Counts. `frame/plan.md:7-8` "16 of the contract's 20 rules": `git grep -c`
of the module's name in `skills/agent-contract/SKILL.md` at `4134055a`
gives 16 (executed). The 13 rewritten lines and the rules 2, 3, 4, 5, 7, 12,
13, 14, 15, 17, 18, 19 and 20 in `frame/design.md:34-35`, `phase-1.md:22-24`
and the changelog's list add up to 13. `frame/design.md:28` puts `PINS` at
`:38-68`, and `git show` at `4134055a` and at `0b75346f` both put it there
(executed). `frame/design.md:89-98`: `git log --follow` on the module at
`4134055a` lists 11 commits, from `438cffe4` to `e391ea04`, and `git log
-S'test_each_section_holds_its_rule' 4134055a` lists 8 (executed). Five
modules import from the contract module (`frame/design.md:191`,
`frame/plan.md:29-34`), and `git grep` finds those five (executed). All five
sealer eval cases carry `shape-runs-no-broad-run.md`
(`frame/design.md:146`, executed `ls`). `phase-1.md:28` "all six eval
targets" is the count at `9ad992b6` and `ee746f3b`, where the contract
names 6 distinct eval directories. HEAD names 7, since round 1's fix
replaced rules 4 and 15's case with rule 5's two. The phase records its own
commit, so it stands, as rounds 1, 2 and 4 found. `round-2.md:192` "26
modules with a left-out number" equals the table (read).
`gaps.md:22-23` "six unpriced case ids", "four crafter eval cases and the
three sealer eval cases" hold against round 1's probe row and the
contract's `check:` lines.

Bounds. 182 is called a bound only where `gaps.md:16` and
`phase-2.md:146-148` quote `frame/design.md` at `d0b5cf4f`, and in round
records describing that. `frame/design.md:230-232`, `gaps.md:16`,
`phase-2.md:149-155` and the comment all call it no bound (executed `grep`
for `182`, `174` and `168` over the work item).

Readers. The 20 `check:` lines at `skills/agent-contract/SKILL.md`
(executed, `awk` over each `## <N>` section) equal the rows at
`frame/design.md:119-138`, the eval bullets at `:143-160`, judgments 4 and
5 at `frame/questions.md:30-42`, rows C and E at `frame/plan.md:72` and
`:74`, the eval targets at `frame/plan.md:45-48`, the changelog sentence,
and `gaps.md:23`. The changelog's reader list names 13 rules, the same 13.

`round-2.md:128` still says "Round 1's record stays as written", and
`126cdfa7` has since corrected `round-1.md:104`. Round 3's reopen of
round-2#3 is that line's correction, and round 4 weighed it the same way.
It states no count, bound or reader, so it is outside the class this round
was asked to sweep. Executed and read.

confirms: none
Carried, not re-established. The per-module decisions behind phase 2's
table were re-derived by rounds 1 and 2. This round re-ran only the table's
rows, sums and module names, and the issue's grep. The readings of the
graders behind `agents/proofer.md:74`, `agents/sealer.md:125` and `:148`,
and `skills/code-review/SKILL.md:38` and `:140`, are still the round-1 fix
pass's. No file outside `seal/` changed in this fix range or in round 4's.
Every verdict above was reached this round. Read.

confirms: none
The checks the caller named, run narrow, each exit 0. Through `bin/test
-q`: the contract module (29 passed),
`tests/text/test_the_record_is_written_in_words.py` (3) and
`tests/behaviour/test_docs_line_wrap.py` (39). `bin/seal layout --check`
exits 0. `bin/seal rules --check` exits 0 with "all 266 check lines in 55
rule files hold". The chain check over the worktree reads this record. Its
refusals are the absent `trail/gate.md` and `guarantee.md`, which the
orchestrator's broad run and the sealer write after the rounds settle. The
suite stays labelled `unverified`, and the orchestrator answers it.
Executed.

This round leaves nothing open. What comes due is the orchestrator's broad
run through `seal gate`, and the sealer's spawn after it.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, including `test_the_durations_file_prices_the_suite` | the branch at `c7daab03` | the orchestrator, through `seal gate` |
| Whether the eval cases that rules 2, 5 and 7 name pass on a run | `evals/behaviour/sealer/`, `evals/behaviour/crafter/` | the orchestrator, at the next preload rewrite that runs the behaviour evals |
| `gaps.md:16` says `208f7076` wrote the count's reading of 182 into the frame, and `gaps.md:34-36` *Fed back into the spec* reads `none`. Whether the folds at `208f7076` and `5a77bc37` belong under that heading | `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md` | the orchestrator |
| Rule 2's case reads one agent and one command spelling. Whether that partial reach is enough for rule 2 | `evals/behaviour/sealer/rule-sealer-no-gate/graders/shape-runs-no-broad-run.md` | the owner |
| `frame/questions.md` Q1 and Q2 stand on their defaults with Status `open` | `frame/questions.md` | the owner |
| The issue body, outside this round's target, puts `PINS` at `:38-65`. `git show 0b75346f` of the module puts it at `:38-68`, as `frame/design.md:28` does. The body is the owner's text, and no record repeats the `:65` | #1111, *Where it stands* | the owner |

## Probes

| Command | Result |
|---|---|
| `git diff d857348d..c7daab03`; `git show --stat 7cb74da2 c7daab03` | one line of `round-2.md`, "5 files" to "4 files"; the verdict and answer lines of `round-4.md` findings 1 and 2 |
| `gh api repos/MichaelYcJo/AgenticSeal/issues/comments/6483485058`; `gh api graphql` for its `userContentEdits` | one edit at 23:41:06Z; 39 module rows and a total; the pointer sentence kept; the 182 sentence reworded |
| `diff` of the comment's module and number cells against `phase-2.md:32-71` | exit 0 |
| `diff` of the `tests/text` modules at `ee746f3b` without the contract module against the table's names; the same lists at HEAD and `ee746f3b`; at `0b75346f` and `ee746f3b` | exit 0; exit 0; one module, `test_no_case_tells_the_agent_it_is_evaluated.py`, absent at `0b75346f` |
| the issue's grep with GNU `grep`, per file over `tests/text`, at `0b75346f` and `ee746f3b` | 182, 174 without the contract module, 8 in it; 168, of which 0 in the module absent at `0b75346f` |
| `git grep -l` and `-n` for `^\s*check:.*evals/` outside `seal/`, at `7cb74da2` and HEAD; `git grep -l` and `-n` for `check:.*evals/behaviour` | 4 files and 10 lines each; 5 files, `tests/github/test_rules.py:266` and `:503` the extra |
| `git log --follow` on the module at `4134055a`; `git log -S'test_each_section_holds_its_rule' 4134055a`; `git grep -c` of the module name in the contract at `4134055a` | 11; 8; 16 |
| distinct eval directories on the contract's `check:` lines at `9ad992b6` and HEAD | 6; 7 |
| `bin/test <module> -q` over the three modules in *Confirmations* | each exit 0: 29, 3 and 39 passed |
| `bin/seal layout --check`; `bin/seal rules --check` | exit 0; exit 0, "all 266 check lines in 55 rule files hold" |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --worktree` | see *Confirmations* |
