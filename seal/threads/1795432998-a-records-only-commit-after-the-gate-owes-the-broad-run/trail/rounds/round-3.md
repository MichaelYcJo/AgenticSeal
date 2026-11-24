# Review round 3: 1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run

```seal
target: 09df8993b, fixes b34bb9e6b..09df8993b
```

This is a verifying round. Its code bound is the diff from round 2's target
to HEAD, `b34bb9e6b..09df8993b`: the round-2 record (`73f6d4118`), the
framer's fold and the orchestrator's row in `frame/plan.md` *Judgments of
the run* (`5a3f3f263`), the fix (`9105342bb`, one line of
`skills/core/SKILL.md`) and the close block (`09df8993b`) (executed:
`git log --stat b34bb9e6b..09df8993b`). The round worked in the branch's
worktree, whose root is 124 characters long (executed: `wc -c` over the
root printed by `printf %s`), because round 2's finding depends on the
root's length. The
worktree's `git status` was clean before and after every run (executed).
`seal/parity.json` is not declared, so no parity comparison was owed.
`seal/config.json` names English for both language keys, so no
`pr.<lang>.md` is owed and none stands.

The work item's records were each read whole at `09df8993b`:
`routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`,
`gaps.md`, `changelog.md`, `pr.md`, `trail/phases/phase-1.md`,
`trail/rounds/round-1.md` and `trail/rounds/round-2.md`. Each quote of
`pr.md` still stands word for word at its coordinate: `frame/design.md:35`
(*Scope*, which the fold moved by no line), the G3 row at
`frame/design.md:11` and `frame/plan.md:47` (read). Findings 1 and 2 are
the two sentences the target contradicts.

Carried from round 2, not re-established: the arms of
`chain_check.py#broad_gate` and `#guarantee`, and `CLOSING_RECORDS`. The fix
diff leaves `skills/code-review/scripts/` and `agents/` untouched (executed:
`git diff --stat b34bb9e6b..09df8993b`). Round 1 answered the `gaps.md:8`
row on `README.ko.md` at `round-1.md:176`, and neither file changed since.

The class findings 1 and 2 belong to was listed by taking the fold
`5a3f3f263` apart into each line it adds or rewrites. Those are G23 at
`frame/design.md:31`, the *Scope* paragraph at `:37`, *Scope* item 1 at
`:41`, the acceptance row at `:68`, the *Removes* row at `:92`, and the
row at `frame/plan.md:49`. Each was read against the target. G23, item 1,
the acceptance row and the *Removes* row hold. The paragraph at `:37` and
the row at `plan.md:49` do not.

The case stays shorter than `CAP` only for a root of at most 140
characters. A `git clone --no-local` under this session's scratchpad has a
root of about 196 characters, and there the case gives about 10,166 and
fails. The base fails there too, at 9,462 + 3 x 196 = 10,050, which agrees
with round 2's limit of 179 at the base. So the gap predates this branch,
and it is no finding of this round. It does mean that an agent which runs
`tests/lib/test_core.py` in such a clone reads a failure the branch did not
cause.

## Findings

### 1. The fold's *Scope* paragraph says the core's rows 3 and 4 carry no sentence another document states, which the target and *Scope* item 1 contradict

```seal
severity: should
location: `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/frame/design.md:37`
evidence: read `frame/design.md:37`, `frame/design.md:41`, `skills/core/SKILL.md:114-115`, `skills/code-review/orchestration.md:268-278`, `docs/checks/the-pull-request-check.md:53`, `docs/forms/the-guarantee.md:28`
regression: round-2#1
```

Why it matters: the unit is the paragraph the fold `5a3f3f263` added at the
head of `frame/design.md` *Scope*. Its second sentence ends "so the two
rows carry no sentence another document already states". *Scope* item 1
says that the third row's *Held by* cell restates no rule, the fix
`9105342bb` cut that one cell, and the defect came from the fold's
paragraph, written before the fix, which claims the same of every cell of
both rows.

At the target, the third row's *What it protects* cell
(`skills/core/SKILL.md:114`) states the rule that
`skills/code-review/orchestration.md:268-278` states for the orchestrator.
`docs/checks/the-pull-request-check.md:53` states it too. The fourth row's
cell (`skills/core/SKILL.md:115`) states the guarantee arm's set, which
`docs/forms/the-guarantee.md:28` also states. *Scope* item 1
(`frame/design.md:41`) itself says that the rule "stands in *What it
protects*, and for the orchestrator in the paragraph of *Scope* item 3".
So the frame states two readings of the same rows. A sealer that reads
the *Scope* paragraph as a condition finds both rows breaking it. A fix
pass that later grows the core would have to remove sentences that the
table is meant to hold.

The paragraph's second sentence also opens "G23 gives the room that leaves
*Scope* items 1 and 2 over the base". A reader has to read it twice to
learn that this is the room the two items may add over the base. The fix
below rewrites the whole sentence. No other line of the fold states the
claim. The commit message of `5a3f3f263` says "holds its rule once", but a
commit message is history and needs no fix.

```markdown
The core's rendered output stays under `lib/core.py#CAP` when the core is rendered from this worktree, whose root is 124 characters long. G23 gives the room that *Scope* items 1 and 2 may add over the base, and item 1 says how the third row stays within it.
```

```seal
verdict: fixed 90be06ca8
answer: The framer folded the finding's rewrite into `frame/design.md` *Scope*'s opening paragraph, word for word: its second sentence now reads "G23 gives the room that *Scope* items 1 and 2 may add over the base, and item 1 says how the third row stays within it." The framer's search of the three frame files found no other statement of the claim. The fix touches the work item's records alone, as the finding's `location:` does, so no verifying round reads it and the sealer reads it at HEAD.
```

### 2. The orchestrator's row on round 2's finding says the core fails the cap "at HEAD", which at the target it passes

```seal
severity: should
location: `seal/threads/1795432998-a-records-only-commit-after-the-gate-owes-the-broad-run/frame/plan.md:49`
evidence: executed `bin/test tests/lib/test_core.py -q -p no:xdist` in the worktree, 16 passed; executed `python3 -I -c` rendering the tree's core through `lib/core.py#rendered`, which prints 9950 and 9578; read `frame/plan.md:49`
regression: round-2#1
```

Why it matters: the unit is the row `5a3f3f263` added to `frame/plan.md`
*Judgments of the run*. Its *Grounds* cell says "at HEAD it fails in a root
past 88 characters, this worktree's 124 among them". The row judges
that option (a) fixes round 2's finding, the fix `9105342bb` then made the
core pass, and the defect came from the row's grounds naming the commit
they measured as HEAD. "HEAD" in the row meant `b34bb9e6b` when it was
written, and the next commit made it false. The row names no commit, and
*Judgments of the run* is not a section dated to a commit. So the sealer
and every later round read "HEAD" as the commit they hold. At `09df8993b`
the rendered core is 9,950 characters in this worktree, and the case
passes for a root of up to 140 characters (executed). The other figures in
the row hold: 9,734 - 9,578 = 156 characters removed out of the 272 the
branch had added (executed, with round 2's 9,734 carried).

```markdown
| 2026-11-23 | Round 2's finding 1 is fixed by option (a) of its *Not judged* row, in the core's own text: the third row's *Held by* cell names its two mechanisms, "`agents/sealer.md` step 1 and the same check's broad gate arm", and no longer restates the rule *What it protects* states, which takes about 156 characters out of the 272 the branch added | The core's rendered output carries the checkout root three times and must stay under `lib/core.py#CAP`; at `b34bb9e6b` it failed in a root past 88 characters, this worktree's 124 among them, where the base passed to 179. Option (b), measuring the case under a fixed-length root, would hide the length a session's real root adds; the cell's rule already stands in *What it protects* and in `skills/code-review/orchestration.md`, so the cut removes a copy and no fact | `skills/core/SKILL.md` *The rule a mechanism is kept against* (a fact has one source); `tests/lib/test_core.py#Test_module`; `trail/rounds/round-2.md` finding 1 |
```

```seal
verdict: fixed 90be06ca8
answer: The orchestrator's row now says "at `b34bb9e6b` it failed in a root past 88 characters", naming the commit it measured, as the finding's rewrite does. The fix touches the work item's records alone, as the finding's `location:` does, so no verifying round reads it and the sealer reads it at HEAD.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: the third row's *Held by* cell at `skills/core/SKILL.md:114`
reads "`agents/sealer.md` step 1 and the same check's broad gate arm" (read).
In this worktree `bin/test tests/lib/test_core.py -q -p no:xdist` passes,
16 cases (executed). The rendered core is 9,950 characters, and 9,578 of
them do not depend on the root, so the case passes for a root of up to 140
characters (executed). The close block's three figures hold. With the old
cell put back through `bin/seal mutate`,
`test_the_trees_core_stays_under_the_harness_cap` fails with
`AssertionError: 10106` at `tests/lib/test_core.py:243`, which is
9,734 + 3 x 124 (executed). So the case holds the cell, and the cut is what
brought the core under the cap. The cell still names what holds the row.
Both mechanisms stand by name, and "the same check" reads back to
`chain_check.py` in the first row, as it does in rows 2 and 4. The rule the
mechanisms read stands in the row's *What it protects* cell. No file
outside `seal/threads/` quotes the removed wording (executed: `git grep -F`
for "holds no run", "follows its newest run", "reads the same rule",
"withholds where", "step 1 withholds" and "broad gate arm reads"). The
close block says no sentence of `changelog.md` describes the cell. That
holds: `changelog.md:3` and `:11` speak of the row's name and of what it
lets follow the run (read).

What matched: `frame/design.md` G23 (`:31`), *Scope* item 1 (`:41`), the
acceptance row *The core fits the hook's cap* (`:68`) and the first
*Removes* row (`:92`) agree with the target (read; the acceptance row
executed as above). G23's room of 165 characters at a 124-character root is
10,000 - 1 - 9,462 - 372 (arithmetic on round 2's figure).

What matched: the narrow modules that read `skills/core/SKILL.md` pass at
the target in the worktree. Those are `tests/lib/test_core.py`,
`tests/skills/test_passages.py`, `tests/text/test_the_rules_have_one_owner.py`,
`tests/text/test_a_moved_rule_leaves_its_definition.py`,
`tests/behaviour/test_first_setup_asks_once.py`,
`tests/skills/test_payload_meter.py`, `tests/behaviour/test_docs_line_wrap.py`,
`tests/text/test_no_passage_is_pasted_into_a_second_file.py`,
`tests/behaviour/test_no_document_names_the_old_roots.py`,
`tests/text/test_the_rules_claude_md_names_have_one_home.py`,
`tests/behaviour/test_one_heading_rule_holds_to_commonmark.py`,
`tests/text/test_broad_gate_rule.py` and
`tests/behaviour/test_the_sealer_guarantees.py`: 422 passed (executed).
`bin/seal rules --check` holds all 175 check lines in 68 rule files
(executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check over the target. The suite is `unverified` by this round, and contract rule 2 leaves it out of this round | `gaps.md:7` | the orchestrator, at the broad run after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/lib/test_core.py -q -p no:xdist`, in the worktree | exit 0: 16 passed |
| `python3 -I -c` importing `lib/core.py` and printing the length of `rendered(origin(root, root), root)`, that length less 3 x the root's length, and the longest root under `CAP` | `9950 9578 140` |
| `bin/seal mutate skills/core/SKILL.md --replace` with the cell's new text and its text at `b34bb9e6b`, `--tests "bin/test tests/lib/test_core.py -q -p no:xdist -k test_the_trees_core_stays_under_the_harness_cap"`, in the worktree | `red`: 1 failed, `AssertionError: 10106` at `tests/lib/test_core.py:243`; the file restored, `git status` clean |
| `bin/test` over the thirteen modules named under *Confirmations*, `-q`, in the worktree | exit 0: 422 passed |
| `bin/seal rules --check`, in the worktree | exit 0: all 175 check lines in 68 rule files hold |
