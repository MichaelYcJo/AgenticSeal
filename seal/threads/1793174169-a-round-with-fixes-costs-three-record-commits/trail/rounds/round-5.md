# Review round 5: 1793174169-a-round-with-fixes-costs-three-record-commits

target: 3a0b6c09 against aa8b54cb

## Findings

### 1. Two shipped sentences say the round record's history holds who wrote a finding's two lines, and under the new rule no commit holds it

severity: should
location: `skills/implement/orchestration.md:666`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/changelog.md:5`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:79-82`
evidence: read `skills/implement/orchestration.md:666`, `skills/code-review/orchestration.md:78-84`, `agents/crafter.md:156-159`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/changelog.md:5`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:79-82`
verdict: open

The phase rewrote the last sentence of the `Grounds` cell at
`skills/implement/orchestration.md:666`. It now reads: "Who wrote a
finding's `verdict:` and `answer:` lines, whether the orchestrator's commit
after the fix pass carried them, and whether that commit changed them are
in the round record's history and no check reads it". The cell is the
reason the orchestrator's rule stays a sentence and has no check. Under the
rule this phase built, two of its three claims are false.
`skills/code-review/orchestration.md:78-84` and `agents/crafter.md:156-159`
say the fix pass writes the two lines and does not commit them, and the
orchestrator commits the record as the fix pass left it. So the fix pass's
version of the lines reaches no commit. The record's history holds the
proofer's commit, with `open` and an empty `answer:`, and then the
orchestrator's commit with the closes. Nothing in it shows who wrote the
closes. Nothing in it shows what the fix pass left before the orchestrator
committed, so whether that commit changed the lines cannot be read either.
The author field does not help: `749cb56c`, the crafter's commit, and
`9c162a3c`, the orchestrator's, carry the same author (executed, see
`## Probes`). Only the first claim holds: whether the orchestrator's one
commit after the fix pass carried the lines is in the history.

The phase built what the frame says. `frame/design.md:79-82`, *Scope* item
4, gives the same three claims. The crafter's account named the sentence as
unread by any case (`gaps.md`, *Not verified*, last row); this round read it
against the rule beside it, and it does not hold.

The changelog's third bullet carries the same fact in another form:
"No check refuses a split: who wrote the two lines, and in which commit, is
in the round record's history". That was true of #955, where the split
took two commits. Under the rule this release ships, a split like #955's is
an orchestrator writing the verdicts before its one commit, and it leaves
nothing in the history. The release note gives the old reason for having
no check (contract rule 12: same cause, every instance).

Why it matters: the cell and the release note tell a reader that the
history can be audited for a second hand on the lines, so the rule needs
no check. A maintainer weighing `frame/questions.md` Q1, the check the
owner has not decided on, reads the cell as saying the history can show
the split. It cannot. That is a stronger reason against the check, and it
also means no later reader can find a split from the history.

The paste-ready fix, the last sentence of the `Grounds` cell at
`skills/implement/orchestration.md:666`:

```markdown
Whether the orchestrator's one commit after the fix pass carried a finding's `verdict:` and `answer:` lines is in the round record's history and no check reads it, and a refusal at the pull request could be cured only by rewriting the branch's history; who wrote the two lines, and whether that commit changed what the fix pass left, is in no commit, because the fix pass commits neither line
```

The last two sentences of the changelog's third bullet (`changelog.md:5`):

```markdown
The tree already named the fix pass as the writer of both lines. No check refuses a split: the fix pass commits neither line, so who wrote them is in no commit, and a refusal of what the history does hold could be cured only by rewriting the branch's history.
```

`frame/design.md:79-82`, the end of *Scope* item 4:

```markdown
   sentence names what nothing reads: whether the orchestrator's commit
   carried a finding's two lines is in the round record's history and no
   check reads it, and a refusal at the pull request could be cured only by
   rewriting the branch's history; who wrote the lines, and whether that
   commit changed what the fix pass left, is in no commit, because the fix
   pass commits neither line.
```

The cell has no case, so the fix closes when one pins it
(`skills/code-review/SKILL.md` *The record*). The case belongs in
`tests/text/test_the_rules_have_one_owner.py`, beside the other readers of
`ORCH_IMPL`. It has not been run:

```python
def test_the_acts_table_says_no_commit_holds_who_wrote_the_two_lines():
    """#1041, the owner's answer of 2026-10-28: the fix pass commits neither
    line, so the row's `Grounds` cell cannot send a reader to the history
    for who wrote them."""
    text = flat(*ORCH_IMPL)
    start = text.index(
        "| Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer |"
    )
    row = text[start : text.index("| Orchestrator: the run ends with a verifying round |", start)]
    assert "is in no commit, because the fix pass commits neither line" in row
    assert "whether that commit changed them are in the round record's history" not in row
```

answer:

### 2. The policy sentence for the settle says a second hand on either line costs a record commit, and under the chosen design it costs none

severity: should
location: `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:251`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/plan.md:87-91`
evidence: read `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/design.md:251`, `seal/threads/1793174169-a-round-with-fixes-costs-three-record-commits/frame/plan.md:87-91`, `skills/code-review/orchestration.md:78-84`
verdict: open

The `## Rule changes` item that the settle writes into
`docs/the-review-record.md` *The round record* ends: "A second hand on
either line costs the round a record commit and gives a reader nothing."
That held for row A, where the fix pass committed its own lines, so a
second hand needed a commit of its own. Under row F, the design this phase
built (`skills/code-review/orchestration.md:78-84`), the orchestrator
receives the record uncommitted. An orchestrator that rewrites a verdict
before its one commit pays no extra commit, and the history looks just as
the rule asks. #955's split, redone under the new rule, costs nothing that
can be counted and leaves nothing that can be seen.

`frame/plan.md:87-91`, the first failure scenario of the chosen approach,
makes the same assumption: an orchestrator that "moves the verdicts to
itself again" makes each round cost "one more record commit until a
proofer reads the fix range's commits or the owner reads the history". In
the likely form of that failure, neither the commits nor the history show
it.

Why it matters: the policy sentence is the reason docs will give for the
rule, and an agent reads it. An orchestrator that knows the rule only by
its stated cost can conclude that a verdict corrected inside its own commit
costs the round nothing, and so is harmless. The bold sentence before it
still forbids that ("It edits no line in that commit"), so the rule itself
has one reading; the stated cost is wrong. The `to:` text reaches `docs/`
only at the settle, so the fix belongs in the frame now. The shipped files
need no change for this finding.

The paste-ready fix, the last sentence of the `to:` text at
`frame/design.md:251`:

```markdown
A second hand on either line gives a reader nothing: made before the orchestrator's commit it leaves no trace in the history, and made after it the round pays one more record commit.
```

`frame/plan.md:87-91`, from "Six months on":

```markdown
  First, the rule stays a sentence, and nothing refuses a split. Six months
  on, an orchestrator writes a fix-pass prompt from memory and moves the
  verdicts to itself again. Where it writes them before its one commit, the
  history shows the commit the rule asks for and nothing shows the split;
  only a transcript does. Where it commits them apart, each round costs one
  more record commit, which the fix range's commits show. No wrong verdict
  reaches a merge, because the verdict is still
```

After the edit, S7 has to be measured again: the `to:` text must share no
15-word run with `skills/code-review/orchestration.md` or
`agents/crafter.md`. The sentence above was written apart from both, and
this round has not measured it.

answer:

## Confirmations

confirms: none
Issue #1041 *Done when* bullet 1 holds at `3a0b6c09`.
`skills/code-review/orchestration.md:81-83` says in bold that the
orchestrator commits the round record as the fix pass left it, in one
commit for the whole pass, before it spawns the verifying round, and
changes none of its lines. `:58-60` still says the orchestrator writes
neither line of a finding the fix pass answers (read). Bullet 2 holds: the
orchestrator's step comes right after the fix pass's last step, at
`:78-81`, in the same paragraph. `agents/crafter.md:20` and `:148-151`,
`skills/implement/SKILL.md:484-489`, the `## Rule changes` item and the
orchestration file all name the fix pass as the writer (read). Bullet 3 is
the changelog's third bullet, confirmed below.

confirms: none
The two sentences give one reading of who commits and when. The crafter's
sentence at `agents/crafter.md:156-159`: write the lines last, after the
last fix commit and its corrections, and do not commit them, because the
orchestrator commits the round record as you left it. The orchestrator's at
`skills/code-review/orchestration.md:78-84`: the fix pass leaves the record
uncommitted, and on the hand-back the orchestrator commits it before the
verifying round. They name the same act, the same party and the same
moment (read). Step 6 of the crafter's *Order of work*, "Commit", is the
build's step. Step 9 replaces steps 5 to 8's record with the two lines in
a fix pass, so it does not reach the round record (`agents/crafter.md:42`,
`:49-50`, read). The paragraph at `skills/code-review/orchestration.md:64-69`
says two commits after the build are the orchestrator's. It lists only
commits that can change what the work item ships. It already left out the
orchestrator's commit of each proofer's record (`agents/proofer.md:6`,
"for the orchestrator to verify and commit"), so the answer commit's
absence from it leaves the count read the same way. That is the frame's
premise in *Out of scope*, checked (read).

confirms: none
Nothing outside the changed files still says the fix pass commits its own
lines. `git grep` over the tree outside `seal/` and the changelogs, for
statements of a fix pass, an answer commit or a round record next to
"commit", matched `docs/the-review-record.md:90` and `:135-146`,
`docs/the-record-layout.md:55`, `skills/implement/SKILL.md:484`,
`agents/proofer.md:6` and `:114`, `skills/code-review/SKILL.md:98` and
README.md:95. Each names the writer, the fix's own commits or the
regression line, and none names who commits the two lines (executed). No
crafter eval and no hook reads a clean tree at a subagent's hand-back
(executed, `git grep` over `evals/behaviour/crafter` and `hooks`).

confirms: none
S1 and S3 hold, and so does the group read. `RULES` entry 20 pins the bold
sentence with `ORCH` as owner. The section case pins the fix pass's write,
"and leaves the round record uncommitted" and "That commit holds
`trail/rounds/round-N.md` alone.", and refuses the old "the fix pass
commits the two lines". The crafter's case pins the new sentence and
refuses "Then commit the `verdict:` and `answer:` lines"
(`tests/text/test_the_rules_have_one_owner.py:149-158`, `:199-214`,
`tests/text/test_a_moved_rule_leaves_its_definition.py:510-521`, read). No
new test function was added, and entry 20 shares no clause with the section
case, so neither duplicates a case of its group. The 40 modules that read a
changed file, the three named in S4 among them, passed (executed, see
`## Probes`). The phase's red runs against `aa8b54cb` and its nine mutants
are the crafter's account. This round did not re-run them.

confirms: none
S5 holds: `rule_changes.parse` over `frame/design.md` at `3a0b6c09` gives
one `add` op for `docs/the-review-record.md` *The round record* and no
errors (executed). S7 holds: `longest_run` of the `to:` text is 0 against
`skills/code-review/orchestration.md`, `agents/crafter.md`,
`docs/the-review-record.md` and `skills/implement/orchestration.md`
(executed).

confirms: none
S6 holds. `grep -n -F` over session
`50face2d-96d3-4774-92e7-faa0805279a3`'s `.jsonl` finds the sentence
"Leave every `verdict:` line as it stands" at 7832 and "Leave `verdict:` as
it stands" at 8016 and 8972. Each of those lines is a `tool_use` whose description
reads "Fix pass #955 round 1", "Fix pass #955 round 2" and "Fix pass #1016
round 1" (executed). `2b68252c` and `517a1139` add 0 `+verdict:` lines
and 6 and 1 `+answer:` lines. `137d0a9c` and `f294b3bd` add 6 and 1
`+verdict:` lines and no `+answer:` line (executed). At `137d0a9c`,
`agents/smith.md:20` and `:153-156` name the fix pass as the writer of
both lines (executed, `git show`). The changelog's third bullet states each
of these as found. Its last sentence is finding 1's.

confirms: none
The `Reframed 2026-10-28 by framer, after round 4.` line is the right
mark, and the only one the tree reads. `docs/the-review-record.md:552-556`
counts a reframe as a design change, and the count of finding rounds
starts again at the first round after it. So this round is the first of a
new count, and it carries no extension line. `chain_check.py#frame_foot`
reads a line under the `Framed` mark only in this shape, and refuses one
whose author is not the declared framer (read). The rule that defines the
line, `docs/the-review-record.md:586-588`, names only the regression route.
`skills/code-review/orchestration.md:306-308` gives an `undecided` answer
no route back to the framer: it says to write the answer, commit, and spawn
the sealer again. Here the owner's answer sent the frame back
(`guarantee.md:40`), and the line says when that happened. `frame/design.md:3-10`
says why (read). What the tree should say for that route is a row of
`## Not judged`.

Facts carried from earlier rounds rather than re-established: round 4's
coordinates for the two paragraphs of the fix-pass section, which this
round opened at their new lines `:54-62` and `:71-84`. Re-established this
round: every verdict above, the four commit counts and the transcript
lines.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `3a0b6c09`. Not run, under contract rule 2 | the branch | the orchestrator, through `seal gate` after the rounds settle |
| The spawn prompt asked for every module that `git grep -l` finds under `tests/` for each changed path and its basename. That is 98 of 160 modules, because the basenames `design.md`, `plan.md`, `questions.md`, `gaps.md` and `changelog.md` name fixtures across the suite. The round ran 40: those naming a changed file by path, by `crafter.md`, `phase-2.md`, the two changed test modules or this work item's id, and the tree-wide text and record readers. The rest is taken as the broad gate's under contract rule 3 | the 58 modules matched by a generic basename only | the orchestrator, through `seal gate` |
| Whether the tree should name the route an owner's answer to an `undecided` verdict takes back to the framer, and the foot line for it. `skills/code-review/orchestration.md:306-308` names only a fresh sealer run, and `docs/the-review-record.md:586-588` names the `Reframed` line only for a regression. This lies outside this work item's diff | `skills/code-review/orchestration.md:306-308`, `docs/the-review-record.md:586-588` | the owner, whether to file it |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the 40 modules chosen as `## Not judged` row 2 describes | exit 0, 1037 passed |
| `bin/seal layout --check` | exit 0, 160 files read, 0 refused |
| `bin/seal rules --check` | exit 0, all 266 check lines in 55 rule files hold |
| `.venv/bin/python -B -c` calling `rule_changes.parse(<frame/design.md>, "docs")` and `longest_run(ops[0].new, <file>)` for the four files | 1 `add` op, `errors=[]`; 0, 0, 0, 0 |
| `grep -n -F` for the two quoted sentences over session `50face2d-96d3-4774-92e7-faa0805279a3`'s `.jsonl` in the user's Claude Code project directory, then each line's `description` field | 7832, 8016, 8972 (and 10016, 10024, not cited), as "Fix pass #955 round 1", "Fix pass #955 round 2", "Fix pass #1016 round 1" |
| `git show <c> \| grep -c '^+verdict:'` and the same for `^+answer:`, over `2b68252c`, `517a1139`, `137d0a9c` and `f294b3bd` | 0 and 6, 0 and 1, 6 and 0, 1 and 0 |
| `git log --format='%h %an' -1` for `749cb56c` and for `9c162a3c` | the same author on both |
| `git show 137d0a9c:agents/smith.md`, lines 20 and 153 to 156 | the fix pass named as the writer of both lines |
| `python3 skills/code-review/scripts/chain_check.py --baseline origin/release/v0.24.0 --root <worktree> --worktree`, after this record was written | see the hand-back |
