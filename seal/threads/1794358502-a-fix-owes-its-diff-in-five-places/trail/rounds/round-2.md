# Review round 2: 1794358502-a-fix-owes-its-diff-in-five-places

```seal
target: 1a2e12c29, fixes ad1035e0a..1a2e12c29
```

This is the verifying round for round 1. The fix diff is `ad1035e0a..1a2e12c29`
and holds three commits. `112f5faf4` is the orchestrator's row and the
framer's fold of finding 1. `a085980ed` is the fix pass. `1a2e12c29` holds
the close blocks. The code this round reviewed is that diff alone.

Carried from round 1, not re-established: the coordinates of the crafter's
rule (`agents/crafter.md:178-201`), the proofer's step 3
(`agents/proofer.md:30-35`) and rule on the records, the base sizes at
`0b55462b2`, and the empty search for `pr.md` in the crafter's files. None
of their checks failed in this range. The fix diff touches none of those
crafter files.

The work item's records were read at `1a2e12c29`. `frame/design.md`,
`frame/plan.md` and `changelog.md` changed in the range. This round read
each hunk with its file, and read the rows the hunks sit in to their ends.
`routing.md`, `frame/questions.md`, `gaps.md` and `pr.md` are unchanged
since `1ea4a8eb0` (executed: `git diff --stat ad1035e0a..1a2e12c29`).
Round 1 read each of them whole at that commit, and nothing this range
changed contradicts them. `pr.md` quotes two rows of *Judgments of the run*
and three rows of *Alternatives considered*. The range leaves all five rows
unchanged, so each quote still stands word for word. No `pr.<lang>.md`
stands or is owed.

The spawn prompt reports that the fix pass ran on the installed 0.37.2
crafter definition, and also read the tree's `skills/implement/fix-pass.md`.
That is the implementer's account. This round judged the fix by its diff
and its close blocks, not by that account.

## Findings

None.

## Confirmations

```seal
confirms: round-1#1
```
What holds: `agents/proofer.md:138-143` now reads "account of what its own
reading of its diff and of these records listed, `pr.md` and `pr.<lang>.md`
aside, is a claim you verify on your own", word for word the round's
paste-ready text (read). The other statements of the sentence carry the
same words: `frame/design.md` T5 (`:101`) and the quote in `changelog.md:5`
(read). The byte figure moved with the sentence. `wc -c agents/proofer.md`
prints 10,999, which is 253 B more than 10,746 at `0b55462b2` and 35 B more
than 10,964 at `ad1035e0a` (executed). G11, *Overlap with the release*,
*Operational impact* and `changelog.md:5` all state 253 B, and G11 splits
it as 218 B plus 35 B (read). A search of the work item's directory for
`218` and `253` finds the old figure only in `trail/phases/phase-1.md:14`
and `trail/rounds/round-1.md:130`, which state the commits they name
(executed: `git grep -n -E "218|253" 1a2e12c29 -- <the work item's directory>`).
The clause after the colon is unchanged, so the case
`test_the_proofer_finds_a_missed_statement_on_the_method_of_a_fix` still
pins it. The case passes, and the reflowed lines pass
`tests/behaviour/test_docs_line_wrap.py` (executed, under *Probes*). The
new *Judgments of the run* row in `frame/plan.md:63` gives the same grounds
the finding gave, and its coordinates resolve (read).

```seal
confirms: round-1#2
```
What holds: `changelog.md:3` now says "A tracer, a sealer and a framer
writing a first frame act on none of those sentences. The framer's and the
orchestrator's folds cited the first of them, and now cite rule 12's second
method." The *Process changes* row's *Why* reads "about 0.8 KB that a
tracer, a sealer and a first-frame framer act on none of". Both are the
round's paste-ready text word for word (read). Both agree with
`frame/plan.md` *Alternatives considered* row 2 and with G8 (read). No other
record of the work item claimed that only the crafter and the proofer act
on the moved sentences (executed: `git grep -n -F "only the crafter and the proofer" 1a2e12c29`
over the work item's directory prints lines of `trail/rounds/round-1.md`
alone, the finding's own quotes).

What matched: both close blocks follow the finding's paste-ready fix and
read `fixed a085980ed`. `a085980ed` touches `agents/proofer.md` and
`changelog.md`, which the two `location:` lines name (read). The chain
check reads them as closed (executed, below).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The broad gate at `1a2e12c29`: the full suite, the repository-wide lint and the typecheck. It is still `unverified`, and this round ran S7's modules alone. With no finding open, the orchestrator's broad run falls due next, and the sealer's spawn follows it | `seal/threads/1794358502-a-fix-owes-its-diff-in-five-places/gaps.md:7` | the orchestrator, by `seal gate --record` |
| Whether the fix pass's steps under the installed 0.37.2 definition agreed with the tree's `skills/implement/fix-pass.md`. That is the fix pass's account of its own conduct, which no read of the diff shows | `skills/implement/fix-pass.md` | the orchestrator, which spawned the fix pass on that definition |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven modules `frame/design.md` S7 names | exit 0 |
| `wc -c agents/proofer.md` at `1a2e12c29` | 10,999 |
| `git grep -n -F "only the crafter and the proofer" 1a2e12c29 --` over the work item's directory | `trail/rounds/round-1.md:74`, `:85` and `:86` alone |
| `git grep -n -E "218\|253" 1a2e12c29 --` over the work item's directory | `changelog.md:5`, G11, `frame/plan.md:50` and `:55` state 253; only `trail/phases/phase-1.md:14` and `trail/rounds/round-1.md:130` state 218 |
