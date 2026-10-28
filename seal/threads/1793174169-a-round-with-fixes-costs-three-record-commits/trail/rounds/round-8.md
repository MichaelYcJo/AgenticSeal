# Review round 8: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 77a75dfd, fixes a88784dc..77a75dfd

## Findings

None. The fix range holds two commits. `5d1e4181` changes one cell of
`frame/plan.md` and `77a75dfd` changes two lines of `round-7.md`. No new
unit stands in the range, and the sweep below found no sentence that states
the record-commit count for every round or stands on the old design.

## Confirmations

confirms: round-7#1
The close holds. Round 7's answer claimed that the orchestrator applied the
block to row C's verdict cell as given at `5d1e4181`, removing the clause
"and keeps the count at two". `5d1e4181` changes one line, row C at
`frame/plan.md:114`, and the diff removes exactly that clause (executed,
`git show --stat` and `git diff a88784dc..77a75dfd`). The block in
`round-7.md` stands whole in `frame/plan.md` at `77a75dfd`, and the old
clause stands nowhere in the file (executed, a substring test, see
`## Probes`). The verdict `fixed 5d1e4181` names a commit that is an
ancestor of HEAD and touches the `location:` path `frame/plan.md`. The cell
now reads "F pays the record commit C saves." That sentence holds in every
round with a fix pass: under C the closes ride in the next round's record
commit, and under F the orchestrator's answer commit carries them, so F
pays exactly one record commit more. The cell no longer states a count, and
the count's one home in the frame stays `frame/design.md:164-170`.

The close itself followed the rule the work adds. No fix pass ran for the
finding, and the orchestrator wrote both lines in one commit, `77a75dfd`,
which touches `round-7.md` alone (executed, `git show --stat`). The
`## Rule changes` `to:` text at `frame/design.md:256` gives a finding
closed with no fix pass to the orchestrator as its writer. The `fixed`
close follows the precedent of round 5's finding 2 (`30e31aac`, confirmed
by round 6). Round 7 then cost two record commits, `a88784dc` and
`77a75dfd`, beside the frame commit `5d1e4181` (executed, `git log` over
`round-7.md`). That agrees with `changelog.md:3`, which gives a finding the
orchestrator closes itself a commit of its own and states no count for a
round without a fix pass.

confirms: none
The sweep for the record-commit count. A `grep -n -i -E` over
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `changelog.md`
and `gaps.md` for "record commits", "answer commit", "the count", "per
round", "three" and the shapes of "commits both lines" found these
sentences, and this round read each one in place.

- `changelog.md:3` and `frame/design.md:164-170` state the count with its
  qualification, as round 7 confirmed.
- `frame/plan.md:9` and `gaps.md:5` describe the three-commit rounds of
  #955 and #1016, in the past tense.
- `frame/design.md:181-182` says the third commit there was the defect, and
  that who makes the one answer commit does not change the count.
- `frame/plan.md:91-92`, row A's failure cell at `frame/plan.md:112` and Q1
  option (a) at `frame/questions.md:54` give "one record commit per round"
  as the cost of a split. A split needs a fix pass, so each ranges over the
  rounds that have one.
- Row C's first cell at `frame/plan.md:114` says C "saves one record commit
  per round". Its subject is a fix pass leaving its lines uncommitted, so it
  has the same range, and the verdict cell beside it now agrees.
- `frame/plan.md:96` says a crafter that commits its own lines leaves the
  count unchanged, which holds for one commit made by either party.

`frame/design.md:172-173` says this release's other work items "already
ran with two record commits per round". Round 7 carried this sentence
without re-reading it. This round walked the round-record history of the
four work items behind its six cited commits. #712 round 1, #1058 round 1
and #913 rounds 1 and 2 each took one record commit and one answer commit.
In #1052, round 1 took `a895ce30` and `8e5261cf`, and round 2 took
`e9006f9a` and `4e635bd4`. The fourth commit, `a28fbc24`, is round 2's fix:
it rewrites round 1's two lines because round 2's finding was about how the
fix pass recorded them (executed, `git log <commit> -- <work item>/trail/rounds`
and `git show a28fbc24`). So the sentence holds for each round it cites.
No finding.

confirms: none
The sweep for sentences standing on the old design, where the fix pass
committed its own lines. Every such sentence in the frame and `gaps.md`
describes phase 1 or row A, and each is pinned to that phase. These are
`frame/design.md:16` and `:116-158`, `frame/plan.md:14-15`, `:34-56`
(headed "read, at `aa8b54cb`"), row A at `:112` and phase 1's row at
`:123`, Q2 option (a) at `frame/questions.md:55`, and the divergence row at
`gaps.md:13`. Each is history in the past tense or a coordinate at a named
commit, so each has one reading.

The shipped files say the new design throughout. These are
`agents/crafter.md:148-160`, `skills/code-review/orchestration.md:54-62` and
`:71-84`, row *The record* at `:165`, and the `Grounds` cell at
`skills/implement/orchestration.md:666` (read). A `git grep` over `agents`,
`skills`, `docs`, `templates`, `tests` and the top files for the same
phrases found no other sentence on who commits a fix pass's lines (executed,
see `## Probes`). `agents/crafter.md:49-50`, *Order of work* step 9, says a
fix pass writes "its two lines instead of steps 5 to 8's record". That puts
the lines where the phase record would stand, after the commit of step 6,
so it agrees with the rule's "Last". It says nothing about a commit, and
the frame keeps step 6 on purpose (`frame/design.md:71-74`, and the second
failure scenario at `frame/plan.md:93-96`). `skills/implement/SKILL.md:484-489`
names the fix pass as the writer and says nothing about a commit, as
`frame/design.md:193-201` leaves it.

`guarantee.md:33` still says the changelog "states the fix pass as the
committer". That is the sealer's verdict on an earlier HEAD, answered by
the owner at `guarantee.md:40`, and the sealer writes the file again at its
next run. It is no sentence this work states. No finding.

confirms: none
The four modules this run names pass, and so do the layout and rules
checks, at `77a75dfd` with this record not yet written (executed, see
`## Probes`). None of the four reads a file under `seal/`. They show that
the fix range broke nothing they read. This round leaves nothing open. What
comes due is the orchestrator's broad run through `seal gate`, since
`trail/gate.md` names `a087c436`, and then the sealer's spawn.

Facts carried from earlier rounds rather than re-established: round 6's
reading of "the number the tree describes" at `frame/design.md:167`, round
7's paste measurements of `changelog.md`, and round 5's record commits.
Re-established this round: the block's application and the clause's
removal, the commit shapes of the fix range, round 7's record commits, the
round-record history behind `frame/design.md:172-176`, and both sweeps.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `77a75dfd`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `git show --stat` for `5d1e4181`, `77a75dfd` and `a88784dc`, and `git diff a88784dc..77a75dfd` | `5d1e4181` touches `frame/plan.md` alone and removes "and keeps the count at two"; `77a75dfd` touches `round-7.md` alone, its `verdict:` and `answer:` lines; `a88784dc` adds `round-7.md` |
| `git log --format='%h %s'` over `round-7.md` | two commits, `a88784dc` and `77a75dfd` |
| `python3 -` testing round 7's fenced block as a substring of `frame/plan.md`, and the old clause's absence | block found; clause absent |
| `git log --format='%h %s' <commit> -- <work item>/trail/rounds` for `ab628278`, `98a3b114`, `6e59b1ea` and `4e635bd4`, and `git show a28fbc24` | #712, #1058 and #913: one record commit and one answer commit per round; #1052: two per round, with `a28fbc24` as round 2's fix rewriting round 1's lines |
| `grep -n -i -E` for "record commits", "answer commit", "the count", "per round", "three" and the shapes of "commits both lines" over the frame, `changelog.md` and `gaps.md`; `git grep -n -i -E` for the same over `agents`, `skills`, `docs`, `templates`, `tests` and the top files | the sentences named under the two sweep entries; none states the count for every round, and none stands on the old design |
| `bin/test -q tests/text/test_no_passage_is_pasted_into_a_second_file.py` | exit 0, 8 passed |
| `bin/test -q tests/behaviour/test_docs_line_wrap.py` | exit 0, 39 passed |
| `bin/test -q tests/text/test_the_rules_have_one_owner.py` | exit 0, 35 passed |
| `bin/test -q tests/text/test_a_moved_rule_leaves_its_definition.py` | exit 0, 221 passed |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --root <worktree> --worktree`, after this record was written, from the plugin's copy and from the tree's | exit 0 from both; nothing refused in this record; it reports `trail/gate.md` and `guarantee.md` behind HEAD and the sealer's `undecided question` at `guarantee.md:38`, each a step still ahead of the orchestrator and the sealer |
