# Review round 7: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 3434a855, fixes a01d3037..3434a855

## Findings

### 1. The plan's row C still says row F keeps the record-commit count at two, the count the fix qualified everywhere else

severity: should
location: `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/plan.md:114`
evidence: read `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/plan.md:114`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:164-170`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/changelog.md:3`
verdict: fixed 5d1e4181

Round 6's finding 1 was the count of two record commits stated for every
round with fixes, which round 5 broke. The fix qualified that count in the
two places the finding named. `changelog.md:3` now limits it to "A round
whose findings the fix pass answers", and `frame/design.md:167-170` adds
"A finding the orchestrator closes itself in a round that also has a fix
pass adds one more". One sentence in the same frame still states the count
without the qualification. Row C's verdict cell at `frame/plan.md:114`
ends: "F pays the record commit C saves, and keeps the count at two."

The cell can be read in two ways. Read against row C, the clause is a
comparison: C saves a commit and F does not. Read on its own, it says F's
count is two. Only the first half of the sentence holds in every round.
Under C the closes ride in the next round's record commit, so F pays
exactly one record commit more than C in any round with fixes. That
includes round 5's shape, where C would pay two and F paid three. The
clause "keeps the count at two" holds only for a round whose findings the
fix pass answers. That is the unqualified number the fix removed from the
changelog and from `frame/design.md`. Both readings are open, and the
frame is text an agent reads (`CLAUDE.md`, *text an agent or a check reads
has one reading*).

Why it matters: the sealer reads the frame against the branch's history,
and this branch's round 5 holds three record commits (round 6, executed).
A sealer that takes the second reading meets a frame sentence the history
contradicts. The withheld verdicts of 0.23.0 and 0.23.1 came from that
pattern, a restated sentence that was wrong. Contract rule 19 asks the
change that amends a fact to remove, in the same commit, what stood on the
old fact. `80325423` rewrote the cost paragraph and left this cell. The
count now has one home in the frame, `frame/design.md:164-170`, so the cell
does not need to state it.

This finding does not reopen round 6's finding 1. That finding named
`changelog.md:3` and `frame/design.md:164-179`, and both closes hold (see
`## Confirmations`). This cell is another instance of the same class. The
fix pass's own sweep found it and left it for the orchestrator, because the
frame is not the crafter's to write.

The last sentence of row C's verdict cell (`frame/plan.md:114`):

```markdown
Rejected. Row F differs from it in when the orchestrator commits. F commits at the hand-back, before the verifying round is spawned, so that round's `target:` holds every close and the uncommitted span is one orchestrator turn rather than a proofer run. F pays the record commit C saves.
```

The frame is the orchestrator's to write. The edit changes no rule and no
test reads the cell. `tests/text/test_no_passage_is_pasted_into_a_second_file.py`
leaves out `seal/`, so it does not read this edit.

answer: The orchestrator applied the block above to row C's verdict cell as given at `5d1e4181`, removing the clause "and keeps the count at two", since the frame is not the crafter's to write; no fix pass ran for this finding, so the orchestrator writes both its lines.

## Confirmations

confirms: round-6#1
The close holds. `ef34bd42` rewrites the last sentence of the changelog's
first bullet to round 6's changelog block word for word, and `80325423`,
the orchestrator's, applies the frame block at `frame/design.md:166-170`
word for word (executed, a substring test of each block against the file
at `3434a855`, both true). The verdict's commit `ef34bd42` touches
`changelog.md`, one of the two `location:` paths. The answer names the
other path's commit, `80325423` (executed, `git show --stat`). Each new
sentence holds against the history. Round 5 is a round with one finding
the fix pass answered and one the orchestrator closed, and it took three
record commits. Round 6 is a round whose one finding the fix pass
answered, and it took two, `a01d3037` and `3434a855` (executed, `git log`
over `round-6.md`). Round 6 also ran the way round 2 did: the orchestrator
repaired the frame half at `80325423` and left the finding open, so the
fix pass closed it and the count stayed at two. The changelog's example,
"such as one it repaired in the frame", fits a finding that sits in the
frame alone, like round 5's finding 2. A finding with a frame half and a
fix-pass half, like round 6's, is closed by the fix pass. The sentence
allows that case, since it names an example, not a rule. Both new
sentences agree with the `## Rule changes` `to:` text at
`frame/design.md:255-256`, which states no count and says that a second hand
"after it" makes the round pay one more record commit (read).

The crafter's account claimed that the new changelog sentences share no
15-word run with five shipped files, `frame/design.md` and `gaps.md`. This
round re-ran the measurement with `longest_run` on the new sentence. It
gives 0 against `skills/code-review/orchestration.md`,
`docs/the-review-record.md`, `agents/crafter.md`,
`skills/implement/orchestration.md`, `frame/design.md`, `frame/plan.md` and
`gaps.md` (executed, see `## Probes`).

The `git grep` sweep for the old fact found these sentences, and this round
read each one. `frame/plan.md:9`, `gaps.md:5` and
`tests/text/test_the_rules_have_one_owner.py:142` describe the three-commit
rounds of #955 and #1016. `frame/design.md:173` reports what this release's
other work items ran, with six commits as evidence. `frame/plan.md:92` says
a split costs one more record commit, and `frame/design.md:181-182` says the
third commit in #955 and #1016 was the defect. None states the count for
every round. `frame/plan.md:114` does, and that is finding 1.
`frame/design.md:181`, "The defect was the third commit", now follows a
sentence about a third commit that was no defect. Its subject is the #955
and #1016 runs named two lines above it, so it reads one way. No finding.

confirms: none
The 17-word run the crafter measured between `changelog.md` and
`frame/design.md` stands at `a01d3037` as well as at `3434a855`, so it
comes from before the fix range. It reads "and leaves them uncommitted, and
the orchestrator commits them as they stand, in one commit for the"
(executed, `longest_run` at both commits). It does not matter. The paste
check reads the rule documents under `docs/`, `skills/`, `agents/` and
`templates/` and the three top files. By its own docstring it leaves out
everything under `seal/` and `CHANGELOG.md`. The frame is removed at the
settle, and the fragment moves to `changelog/<X.Y.Z>.md`, which is outside
the corpus too (`docs/the-record-layout.md:17`, read). So the pair never
reaches a file the rule of one source governs. The same measurement over
the whole changelog finds a longer run, 21 words, against
`skills/code-review/orchestration.md`. It reads "its fix-pass prompt leaves
both lines to the crafter. a close the orchestrator doubts goes into the
verifying round's spawn prompt". It stands at `44f37009`, so it also comes
from before the fix range. It is the release note saying what the shipped
file says, beside the file's name, and the same exclusion covers it. The
crafter's "0 against `skills/code-review/orchestration.md`" was measured on
the new sentence alone, and that is what it claimed. No finding.

confirms: none
The four modules this run names pass, and so do the layout and rules
checks, at `3434a855` with this record not yet written (executed, see
`## Probes`). None of the four reads a file under `seal/`. They show that the
fix range broke nothing they read, and say nothing about the frame or the
changelog.

Facts carried from earlier rounds rather than re-established: round 6's
reading of the `to:` text, its S5 and S7 results, and round 5's record
commits. Re-established this round: both blocks' application, the commit
shapes of the fix range, round 6's record commits, the run measurements and
the sweep.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `3434a855`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |
| Whether finding 1 is fixed by dropping the clause, as given, or by a qualifying clause the orchestrator prefers | `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/plan.md:114` | the orchestrator, who writes the frame |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_no_passage_is_pasted_into_a_second_file.py` | exit 0, 8 passed |
| `bin/test -q tests/behaviour/test_docs_line_wrap.py` | exit 0, 39 passed |
| `bin/test -q tests/text/test_the_rules_have_one_owner.py` | exit 0, 35 passed |
| `bin/test -q tests/text/test_a_moved_rule_leaves_its_definition.py` | exit 0, 221 passed |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `.venv/bin/python -B -c` calling `longest_run` on `changelog.md` against `frame/design.md` at `a01d3037` and `3434a855`, and against `skills/code-review/orchestration.md` at `44f37009` and `a01d3037` | 17 words at both commits for the frame; 21 words at both commits for `skills/code-review/orchestration.md` |
| `.venv/bin/python -B -c` testing round 6's two blocks as substrings of `changelog.md` and `frame/design.md`, and calling `longest_run` on the new changelog sentence against seven files | both blocks found; 0 against each of the seven |
| `git show --stat` for `80325423`, `ef34bd42` and `3434a855`, and `git log --format='%h %s'` over `round-6.md` | each commit touches one file: `frame/design.md`, `changelog.md`, `round-6.md`; round 6's record took two commits, `a01d3037` and `3434a855` |
| `git grep -n -i -E` for "record commits?", "count at two", "the count", "two commits", "answer commit" and "per round" over `agents`, `skills`, `docs`, `templates`, `tests`, `changelog` and this work item outside its round records | the sentences named under `confirms: round-6#1`; only `frame/plan.md:114` states the count for every round |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --root <worktree> --worktree`, after this record was written | see the hand-back |
