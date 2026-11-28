# Review round 2: 1795841829-skill-descriptions

```iadd
target: 2418460d, fixes c2388b71..2418460d
```

Round 2 is a verifying round over the fix diff `c2388b71..2418460d`. The
range holds the orchestrator's `af141ae2`, the framer's fold `c1837a66`,
the fix pass's `e53def2a`, `76ecf7a7` and `8ac6cafa`, and the close blocks
in `2418460d`. It holds no merge of the base (executed: `git log --merges
c2388b71..2418460d` printed nothing). The code under review is one
frontmatter hunk, `skills/commit-pr-convention/SKILL.md` in `e53def2a`. The
rest of the range is the work item's records. Beside that bound, the round
read whole at `2418460d` the records that state the present: `routing.md`,
`frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`,
`changelog.md`, `pr.md`, `trail/phases/phase-1.md` and
`trail/rounds/round-1.md`. No `pr.<lang>.md` stands, and none is owed,
because both language keys of `agentory/config.json` read `English`.
`agentory/parity.json` is not declared.

Carried from round 1 and not re-derived: the base's `skills/`, `agents/`
and `.claude-plugin/` equal the `v0.40.1` tag's, which is what lets the
changelog state its total before as "4,860 characters in 0.40.1". Round
1's checks of the measurement record and the new case were not run again,
because the fix diff touches neither. Re-derived here: M1, the searches of
S2 and S3, the finding searches of both round 1 findings, the pull request
body, and the frames of #1655 and #1659.

## Findings

### 1. The plan's phase 1 row says phase 1 delivers *Scope* item 3 and passes S2, which the fold made false

```iadd
severity: should
location: `agentory/threads/1795841829-skill-descriptions/frame/plan.md:48`
evidence: executed `git grep -n 'NOT for' ee1c63a3 -- 'skills/*/SKILL.md'`, `git grep -n -F 'print what those rows state' -- agentory/threads/1795841829-skill-descriptions`, `git grep -n -F 'Scope* items 2, 3, 4 and 5' -- agentory/threads/1795841829-skill-descriptions`; read `agentory/threads/1795841829-skill-descriptions/frame/design.md:32-36`, `agentory/threads/1795841829-skill-descriptions/frame/design.md:41`, `agentory/threads/1795841829-skill-descriptions/frame/design.md:55-56`
```

Why it matters: the *Phases* row for phase 1 is the plan's task list.
`skills/implement/SKILL.md` says its Delivers cell is what the phase was
asked, and the inspector reads it against the tree at the commit in its
Status cell. The row says phase 1, closed at `ee1c63a3`, delivers
"`frame/design.md` *Scope* items 2, 3, 4 and 5". It also says phase 1 is
verified because "The searches of S2 and S3 print what those rows state"
(`frame/plan.md:48`). The fold `c1837a66` rewrote *Scope* item 3, so it now
removes commit-pr-convention's `NOT for:` clause
(`frame/design.md:32-36`). It rewrote S2, which now expects one line each
in `skills/code-review/SKILL.md` and `skills/writing-style/SKILL.md` and no
other (`frame/design.md:56`). It rewrote *Scope* item 5, whose total after
now comes from the fix pass for round 1's first finding
(`frame/design.md:41`). At `ee1c63a3`, S2's search prints three lines, one
of them `skills/commit-pr-convention/SKILL.md:10` (executed). So phase 1 did
not deliver *Scope* item 3 as it now reads, and S2's search did not print
what S2 states. The fix pass delivered that part in `e53def2a`, and
*Scope* item 5 says so. The *Phases* row still states the scope before the
fold, so the frame gives two answers to who delivered the clause's
removal. `skills/implement/fold-and-reframe.md` asks the framer to rewrite
in place every sentence of its three files that a fold changes, reading
each file whole. This cell is one of those sentences, and the fold left it.

This finding carries no `regression:` or `reopens:` line. No commit of the
fix range changed this row, so the row is not a unit a fix pass's own
commits made, and finding 1's close holds (`## Confirmations`). The
defect's source is the fold `c1837a66`: it rewrote *Scope* item 3, S1, S2
and *Scope* item 5, and it left this row as it stood. The fix is a frame
sentence, so it is the framer's to fold. The Status cell stays as it is.

The searches above found the Delivers wording and the "print what those
rows state" wording only at `frame/plan.md:48`. A search on these words is
a sample, so a statement of the same claim in other words can escape it.
`trail/phases/phase-1.md:28-43` reports S1, S2 and S3 at `8fc3c2fe`, a
named commit, with the three lines that commit held. That report is true
as dated and needs no change.

```markdown
frame/plan.md:48, the Delivers cell:
`frame/design.md` *Scope* items 2, 3, 4 and 5, with `changelog.md` and the version move (*Operational impact*), except the removal of commit-pr-convention's `NOT for:` item and the total after, which the fix pass for round 1's first finding delivers (*Scope* item 5). Where the measurement step's run was made, also *Scope* item 1's record under `docs/experiments/`, written from the commands and the transcript paths the orchestrator's spawn names

frame/plan.md:48, the Verified by cell, its sentences "M1 prints a total below 4,860 (S1). The searches of S2 and S3 print what those rows state." replaced by:
M1 prints a total below 4,860. `git grep -n 'NOT for' -- 'skills/*/SKILL.md'` prints one line in each of `skills/code-review/SKILL.md`, `skills/commit-pr-convention/SKILL.md` and `skills/writing-style/SKILL.md`, each opening `NOT for:`, and S3's search prints nothing.
```

```iadd
verdict: fixed efc72d4c
answer: The finding holds. The framer folded `frame/plan.md` *Phases* row 1 in `efc72d4c`, the orchestrator's fix after the last round: the Delivers cell keeps *Scope* items 2 to 5 and adds that round 1's first finding's fix pass delivers `commit-pr-convention`'s `NOT for:` clause's removal and the total after the work, which that pass's close block records; the Verified by cell states phase 1's S2 result, three lines in `code-review`, `commit-pr-convention` and `writing-style`, and points at round 1's first finding's close block for the S1 and S2 results at the last commit that changes a description. The Status cell stays `ee1c63a3`. The finding's searches, run again at `efc72d4c`: `git grep -n -F 'print what those rows state' -- agentory/threads/1795841829-skill-descriptions` prints this record's own lines alone; `git grep -n -F 'Scope* items 2, 3, 4 and 5' -- agentory/threads/1795841829-skill-descriptions` prints `frame/plan.md:48`, the Delivers cell, whose list stands as phase 1 built it beside the new sentence, and this record's own lines. The change touches the work item's records alone, so the inspector reads it (`skills/core/SKILL.md` *Judgment is not licence to skip a party*, row *No fix that no round reads*).
```

## Confirmations

```iadd
confirms: round-1#1
```
What holds: the frame, the skill and the release note now agree that two
`NOT for:` items stay, each with a confusion G10 records. The framer
rejected the round's paste-ready fix as row A12 (`frame/plan.md:42`). The
fold rewrote G10 (`frame/design.md:18`), *Scope* item 3
(`frame/design.md:32-36`), *Scope* item 5 (`:41`), S1 and S2 (`:55-56`) and
*Data & interfaces* (`:68-69`) to remove the item. `e53def2a` removes the
two lines from `skills/commit-pr-convention/SKILL.md`'s description. The
description is left ending at its `Use when:` line, a valid literal block,
and no body line changed. No later commit touches `skills/` (executed:
`git log e53def2a..HEAD -- skills` printed nothing). At `2418460d`, M1
prints `commit-pr-convention 347` and `total 3305` among the nine figures
the close block quotes (executed). S2's search prints
`skills/code-review/SKILL.md:9` and `skills/writing-style/SKILL.md:12`
alone, and S3's prints nothing and exits 1 (executed). `changelog.md:3`
states 4,860 and 3,305, names commit-pr-convention among the skills with no
clause, and names the two kept items. The finding's search, run again at
the target over the same pathspec, prints the lines the close block lists
at the line numbers it gives, each standing for the reason it gives
(executed). The close claims that G10 records the item in `716d8548` with
no confusion. That claim stands on the framer's searches, which round 1 ran
too, and round 1 found the same. The A12 quote "Format rules for" stands at
`skills/commit-pr-convention/SKILL.md:4`, and the skill body still says at
`:19` that `writing-style` governs what a pull request body says (read).
The other statement of the removed item in the tree is G10's history
sentence. No test, README row or doc copies the item (executed: `git grep
-n -i -F 'prose and structure of a PR body'` and `git grep -n -F
'(writing-style)'` over the tree). `#test_the_writing_style_handoff_names_a_skill_that_ships`
reads writing-style's frontmatter alone (`tests/behaviour/test_chain_hooks_hardening.py:547-570`,
read), so the removal leaves it standing. `gaps.md:9` changes the row in
place to add the PR-body request and commit-pr-convention. No row left the
memo. The added case matches the third case the fold added to
`frame/plan.md:25`.

```iadd
confirms: round-1#2
```
What holds: the Grounds cell of the `perf:` row (`frame/plan.md:98`) no
longer says every skill keeps when a session reaches it. It now says that
whether a session picks a skill differently is unverified and that the
repository owner answers it in `gaps.md`. `gaps.md:8-9` name the repository
owner for both questions (read). `pr.md:6` quotes the cell word for word
(executed: the two strings compared equal), and `bin/agentic pr-body`
composed the body at the target and refused no quote (executed). The
cell's claim that no skill body changes holds: every hunk of `git diff
origin/release/v0.41.0..2418460d -- skills` falls under `description: |`
(executed). The finding's two searches, run again at the target, print
round 1's own lines and `frame/plan.md:86`. That line says a session may
choose a skill differently, which agrees with the new cell (executed).

What matched: the axis *Record against another work item's frame*. The
frames of #1655, at `31b480b5`, and of #1659, at `4c46218b`, name neither
commit-pr-convention nor a `NOT for:` clause. #1659 names
`agents/framer.md`'s description, which this work leaves alone (executed,
`grep` over each worktree's `frame/design.md`).

What matched: the narrow modules the fix diff reaches passed at the target,
152 cases (executed). They are `tests/behaviour/test_chain_hooks_hardening.py`,
`tests/text/test_the_rules_have_one_owner.py`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/behaviour/test_this_repository_passes_its_own_checks.py` and
`tests/lib/test_gaps.py`. This is no broad run. `gaps.md:7` labels the broad
gate unverified and names the orchestrator as its answerer, and that label
is honest. The row says the broad gate runs over phase 1's commits, while
the run that comes due reads the branch at HEAD, fix pass included. The
orchestrator runs it at HEAD whatever the row says, so this is no finding.

The fix diff adds no test, so no new test was read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether a plain review request still invokes `agentic:code-review`, and whether a request a removed `NOT for:` item named now loads `implement`, `verify` or `commit-pr-convention`. No case runs the model's choice of a skill | `agentory/threads/1795841829-skill-descriptions/gaps.md:8-9` | the repository owner |
| The broad gate over the branch | `agentory/threads/1795841829-skill-descriptions/gaps.md:7` | the orchestrator, at the broad run |

## Probes

| Command | Result |
|---|---|
| M1 from `frame/plan.md:11-19`, run in the round's clone at `2418460d` | nine figures, `commit-pr-convention 347`, `total 3305` |
| `git grep -n 'NOT for' -- 'skills/*/SKILL.md'`, then `git grep -n -E 'Use when\|NOT for\|disable-model-invocation' -- skills/core/SKILL.md skills/agent-contract/SKILL.md`, at `2418460d` | two lines, then nothing with exit 1 |
| `git grep -n 'NOT for' ee1c63a3 -- 'skills/*/SKILL.md'` | three lines, `skills/commit-pr-convention/SKILL.md:10` among them |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py tests/text/test_the_rules_have_one_owner.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_this_repository_passes_its_own_checks.py tests/lib/test_gaps.py -q` | exit 0, 152 passed |
| `bin/agentic pr-body --body <scratch>/out/body.md agentory/threads/1795841829-skill-descriptions` | exit 0, the body written with every quote accepted |
