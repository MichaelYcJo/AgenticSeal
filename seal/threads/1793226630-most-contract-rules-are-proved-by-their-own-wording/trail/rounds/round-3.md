# Review round 3: 1793226630-most-contract-rules-are-proved-by-their-own-wording

target: 0f77a2d0, fixes 6d003f3d..0f77a2d0

## Findings

### 1. Round 2's finding 3 closes `deferred` for a correction a commit made in the tree, and `round-1.md:104` still says 11

severity: should
location: `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/rounds/round-1.md:104`, `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/rounds/round-2.md:97`
evidence: executed `git grep -n -o 'finds 11 .check:. lines' -- seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording`, `git grep -n -E '^\s*check:.*evals/' -- ':!seal/'`, `git diff --name-only 6d003f3d HEAD -- seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/trail/rounds/round-1.md`, `git grep -n -i -E "fix-pass-two-lines|correction to a record|earlier record.{0,40}(edit|change|rewrit)|record stays|deferred <where" -- docs skills agents templates`
verdict: open
reopens: round-2#3

The close does not hold, for two reasons.

First, the grammar gives this repair `fixed`, not `deferred`.
`docs/the-review-record.md:140-145` says "A repair a commit made, a
correction to a record among them, closes `fixed <commit>`". It keeps
`deferred <where it was repaired>` for "A repair made outside the tree",
which "makes no commit on the branch".
`tests/text/test_the_record_is_written_in_words.py:111-136` pins both
sentences. The fix pass's answer says the correction is the answer line
of round 2's finding 3. That line is in the tree, and `0f77a2d0` committed
it on the branch. `skills/implement/SKILL.md:508-514` gives the other homes a
`deferred` close may name: `seal/follow-up.md`, or a rule change in
`frame/design.md`. A finding "Doable within this pull request" is "done
now". A one-word edit to `round-1.md:104` is doable now. The close also
matters to the chain. A `deferred` finding owes the next round nothing
(`docs/the-review-record.md:161-162`), so this close would have taken the
finding out of verification. The caller asked for this round's judgment,
which is the only reason the close is read here.

Second, the sentence the finding names still stands. Claimed: "Round 1's
record stays as written, so the correction is this answer line". Found:
`round-1.md:104` reads "`git grep` finds 11 `check:` lines" at HEAD, and
no commit in the fix range touched `round-1.md` (executed). The grep the
answer ran for "11 `check`" covered `trail/phases/`, `gaps.md` and
`changelog.md`, and left out `trail/rounds/`, where the sentence stands.
No rule freezes an earlier record's `answer:` line. The search over
`docs`, `skills`, `agents` and `templates` finds only the `fixed` sentence
above. "Every round file stays" (`docs/the-review-record.md:166`) keeps
the file, not its wrong number. Contract rule 19
(`skills/agent-contract/SKILL.md:216-222`) says "A correction written
beside the sentence it corrects leaves both for the next reader to choose
between". A sealer that re-runs round 1's sweep finds ten lines and reads
11 at `round-1.md:104`. Only by also reading round 2's answer does it
learn which number is right.

This is a reopen and not a second regression. `16e0d911`, round 1's fix
pass, wrote the 11. Round 2's finding 3 already counts that as a
regression of round-1#2. Round 2's fix pass made no commit to the unit.
It left the defect standing and did not introduce it.

In `round-1.md:104`, replace:

```markdown
`git grep` finds 11 `check:` lines in the tree that name an eval case.
```

with:

```markdown
`git grep` finds 10 `check:` lines in the tree that name an eval case.
```

Commit that edit. This finding then closes `fixed <that commit>`. Leave
`round-2.md:97` as round 2's fix pass wrote it. This finding's reopen of
round-2#3 and its close are the trail from that verdict to the repair.

answer:

## Confirmations

confirms: round-2#1
`5a77bc37` rewrote `frame/plan.md:72` and `:74` with the text round 2
gave, word for word (read, `git diff 6d003f3d 0f77a2d0`). Row C now lists
rules 3, 12, 13, 14, 17, 18, 19 and 20 as judgments, and row E names
rules 2 and 5 for the sealer cases. Both rows match the `check:` lines at
`skills/agent-contract/SKILL.md:46`, `:67`, `:78`, `:102` and `:182`
(executed `grep -n '^check:'`). Row C's citation resolves:
`frame/design.md:150-156` says no grader of the cases "reads the sealer's
own labels or its own red runs". Round 2's executed grep, re-run at HEAD,
finds no other sentence under the work item that gives rules 4 and 15 an
eval reader or calls rule 5 a judgment. The verdict names the
orchestrator's commit, not one the fix pass made. That is a close the
grammar allows: `fixed <commit>` names the commit that made the repair
(`docs/the-review-record.md:140-141`), and `5a77bc37` touches the path
the finding's location names. Executed and read.

confirms: round-2#2
`ec52e4f4` applied round 2's text to the bullet at `phase-2.md:146-155`
and the cell at `gaps.md:16` (read, the range's diff). The quote holds.
`git show d0b5cf4f:.../frame/design.md` gives the sentence at `:228-229`.
The cell stops the quote at "above." where the frame goes on ", and the
method sizes it", and the cut changes no meaning. "The frame this phase
counted against" holds. `git diff --stat d0b5cf4f ee746f3b -- frame/` is
empty, and `d0b5cf4f..f9c33d98` touches only `frame/plan.md`'s Status
cells, so both phases counted against that frame (executed). The claim
"`208f7076` wrote the count's reading of 182 into the frame" holds:
`208f7076:frame/design.md:230-232` reads "it is no bound on this count"
(executed). The fix pass swept for the class. Round 2's executed grep for
`182`, re-run at HEAD, finds no sentence outside the round records that
says the current frame calls 182 a bound. `frame/design.md:172` holds 182
as a line coordinate only. The rewrite made no new defect in the unit.
Executed and read.

confirms: none
Phase 2's count is fit to post on #1111 as `trail/phases/phase-2.md`
stands. Finding 1 does not touch it: the 11 is in a round record, not in
the phase. The table re-sums to 39 rows, 255 counted, 124 left out by
kind, 3 in Q2, 75 `not in` and 81 with a name on the left, and 255, 124
and 3 make 382 (executed, `awk` over the table). No file under `tests/`
changed between `ee746f3b` and HEAD (executed `git diff --stat`). The
range changed `phase-2.md` only in the 182 bullet, which round 2's
finding 2 covers. The bullet gives the issue's command with `-r
tests/text`, where the issue writes `-r tests/<dir>` above its table.
That table's `tests/text` row holds the 182, so the bullet quotes the
command for that row, and it is not a misquote (executed `gh issue view
1111 --json body`). Executed and read.

confirms: none
Carried, not re-established. The per-module decisions behind the table
were re-derived by rounds 1 and 2 and are not repeated. This round re-ran
only the sums, the `tests/` diff and the issue's text. The readings of the
graders behind `agents/proofer.md:74`, `agents/sealer.md:125` and `:148`,
and `skills/code-review/SKILL.md:38` and `:140`, are still the round-1 fix
pass's. Those files lie outside every fix range so far. Every verdict
above was reached this round. Read.

confirms: none
The checks the caller named, run narrow, each exit 0. Through `bin/test
-q`: the contract module,
`tests/text/test_the_record_is_written_in_words.py`,
`tests/behaviour/test_unverified_rows_close.py`,
`tests/skills/test_unverified_check.py` and
`tests/behaviour/test_docs_line_wrap.py`. `bin/seal layout --check` and
`bin/seal rules --check` also exit 0. The chain check over the worktree
exits 0 with no pull request open, and lists three refusals: this
record's finding 1, which reads `open`, and the absent `trail/gate.md`
and `guarantee.md`, which the orchestrator's broad run and the sealer
write after the rounds settle. The suite stays
labelled `unverified`, and the orchestrator answers it. Executed.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck, including `test_the_durations_file_prices_the_suite` | the branch at `0f77a2d0` | the orchestrator, through `seal gate` |
| Whether the eval cases that rules 2, 5 and 7 name pass on a run | `evals/behaviour/sealer/`, `evals/behaviour/crafter/` | the orchestrator, at the next preload rewrite that runs the behaviour evals |
| `gaps.md:16` now says `208f7076` wrote the count's reading of 182 into the frame, and `gaps.md:34-36` *Fed back into the spec* reads `none`. Whether the folds at `208f7076` and `5a77bc37` belong under that heading, whose template line asks for "clauses this work added" | `seal/threads/1793226630-most-contract-rules-are-proved-by-their-own-wording/gaps.md` | the orchestrator |
| Rule 2's case reads one agent and one command spelling. Whether that partial reach is enough for rule 2 | `evals/behaviour/sealer/rule-sealer-no-gate/graders/shape-runs-no-broad-run.md` | the owner |
| `frame/questions.md` Q1 and Q2 stand on their defaults with Status `open` | `frame/questions.md` | the owner |

## Probes

| Command | Result |
|---|---|
| `git grep -n -o 'finds 11 .check:. lines' -- <work item>` | `round-1.md:104`, plus round 2's heading and quote at `round-2.md:92` and `:119` |
| `git grep -n -E '^\s*check:.*evals/' -- ':!seal/'` | 10 lines in 4 files: `agents/proofer.md` 1, `agents/sealer.md` 4, `skills/agent-contract/SKILL.md` 3, `skills/code-review/SKILL.md` 2 |
| `git diff --name-only 6d003f3d HEAD -- <work item>/trail/rounds/round-1.md` | empty, exit 0 |
| round 2's grep for the readers of rules 4, 5 and 15, re-run at HEAD over the work item | `frame/plan.md:72` and `:74` hold the new rows; no other frame or record sentence states the old readers |
| `git grep -n "182" -- <work item>`; `git show d0b5cf4f:<work item>/frame/design.md`; `git show 208f7076:<work item>/frame/design.md` | 182 as a bound only at `d0b5cf4f:228-229`; as no bound at `208f7076:230-232` |
| `git diff --stat d0b5cf4f ee746f3b -- <work item>/frame/`; `git diff --stat ee746f3b HEAD -- tests/` | both empty |
| `awk` over the table of `phase-2.md` | 39 rows; 255, 124, 3, 75, 81 |
| `gh issue view 1111 --json body` | the command written `-r tests/<dir>`; `tests/text` row 182 |
| `bin/test <module> -q` over the five modules in *Confirmations* | each exit 0 |
| `bin/seal layout --check`; `bin/seal rules --check` | exit 0; exit 0 |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --worktree` | exit 0; lists round 3's finding 1 as `open`, and no `trail/gate.md` or `guarantee.md` yet |
