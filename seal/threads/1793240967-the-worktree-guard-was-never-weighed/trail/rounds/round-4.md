# Review round 4: 1793240967-the-worktree-guard-was-never-weighed

target: 61d387ad, fixes 6afccf70..61d387ad

This is a verifying round. The diff read is `6afccf70..61d387ad`. It holds
two commits. 6eb32d52 is the orchestrator's fold of round 3's finding 1 into
`frame/design.md`. 61d387ad is the round-3 record with the lines the fix
pass wrote, its `verdict:` and `answer:`. The fix pass's answer, the commit
messages and the spawn prompt were read as claims. Each claim below says what
was claimed and what was found. The commands ran in a `git clone --no-local`
of the branch at 61d387ad.

Carried from round 3, and not re-established: `seal/parity.md` is not
declared, so this round writes no `original:` line. Also carried:
`skills/settle/scripts/rule_changes.py:259` skips every item that is not a
`remove` with no `from`, and `pending` at `:233-250` reads only a shared
root. Re-established this round: `seal/config.md` holds no
`Record language` row (executed, `grep -i language`), so the record is in
English. The rules check was run again at 61d387ad.

## Findings

None. The one finding round 3 closed holds, and the fix diff introduces no
defect.

## Confirmations

confirms: round-3#1
The *Grounding* layout row now states the one shape the check excuses. The
answer claimed that 6eb32d52 changes one line, `frame/design.md:17`, and
that the row now reads "`seal rules --check` excuses each such line, because
this design's pending `remove` with no `from` takes its section out, and
names this work item (Scope In 7)". `git diff 6afccf70 6eb32d52` shows that
one line changed in that one file, with that text (executed). The row now
matches Scope In 7 at `frame/design.md:104-109`, which names a pending
`remove` with no `from` as the one excused shape (read). It also matches the
design's own `## Rule changes` at `frame/design.md:171-173`: the `remove` of
`docs/worktree-guard-spec.md` names the section "The worktree guard" and
carries no `from` (read). The clause is true of the tree. `bin/seal rules
--check` exits 0 with "17 excused in 268 check lines of 55 rule files, and
every other line holds". All 17 excused lines stand in
`docs/worktree-guard-spec.md`, under subsections of its one top-level
section "The worktree guard". Every one names this work item (executed). The
answer cited this count from round 2's fix pass at f720935f, and this round
re-ran it at 61d387ad rather than carrying it. The fold leaves out the words
"at the settle" from round 3's paste-ready text. The same row already says
the two documents "leave at the settle through the two `remove` items
below", so the row still gives that timing (read).

confirms: none
The rest of the class holds. `git grep -n -i "reads the policy in force"`
over the work item's frame prints nothing (exit 1). `git grep -n -i "policy
in force"` over the frame prints only the first sentence of
`frame/design.md:17`. That sentence restates the layout rule's definition at
`skills/implement/SKILL.md:75`, and round 3 already accounted for it
(executed). A search for `rules --check` and `excuse` over the frame,
`gaps.md` and `changelog.md` prints the lines that state what the check
excuses. They are `frame/design.md:16`, `:104-116`, `:145`, `:147` and
`:237`, `frame/plan.md:16`, `:59-64` and `:107`, `frame/questions.md:22-24`
and `:35`, `gaps.md:39` and `changelog.md:12` (executed). None of them says
the check reads the policy in force. Where a line says no more than that a
pending `remove` takes a section out, it is the S8 title's short form or a
pointer to Scope In 7, and the text it points to names the shape with no
`from` (read). Round 3 confirmed `frame/plan.md:59-61` and
`frame/questions.md:22-24`, and 6eb32d52 does not touch them.

confirms: none
61d387ad changes only the finding's `verdict:` line, to `fixed 6eb32d52`,
and its `answer:` line in `trail/rounds/round-3.md`. Nothing else in the
record changed (executed, `git diff 6eb32d52 61d387ad`). The `fixed` commit
touches the path the finding's `location:` names, `frame/design.md` (executed,
`git diff --stat 6afccf70 61d387ad`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck over 61d387ad: unverified. The fix diff changes no code and no case, so this round ran no test module. | the whole tree | the orchestrator, at the broad gate |

## Probes

| Command | Result |
|---|---|
| `git diff 6afccf70 6eb32d52` | one line changed, `frame/design.md:17` |
| `git diff 6eb32d52 61d387ad` | two changed lines in `trail/rounds/round-3.md`, the finding's `verdict:` and `answer:` |
| `git grep -n -i "reads the policy in force"` over the work item's frame | exit 1, no line |
| `git grep -n -i "policy in force"` over the work item's frame | exit 0, only the first sentence of `frame/design.md:17` |
| `git grep -n -i -e "rules --check" -e "excuse"` over the frame, `gaps.md` and `changelog.md` | exit 0, the lines listed under `## Confirmations`, none saying the check reads the policy in force |
| `bin/seal rules --check` | exit 0, 17 excused in 268 check lines of 55 rule files, all in `docs/worktree-guard-spec.md` and each naming this work item |
