# Review round 1: 1793862999-unverified-baseline-is-run-by-a-person-only

```seal
target: c2702707 against release/v0.32.5
```

The range is `a0303ee9..c2702707`, where `a0303ee9` is both the tip of
`release/v0.32.5` and the merge base (executed: `git rev-parse` and
`git merge-base`). This is round 1, so no earlier round carries a coordinate
or a verdict here, and every fact below was established in this round. No
`seal/parity.md` is declared, so the parity comparison does not apply. The
review ran in a `git clone --no-local` of the branch at `c2702707`, kept in
the round's scratch directory.

Stage 1 read the code against issue #1240's decision as the design quotes
it, the design's *Scope* items 1 to 12, A1 to A6, `## Rule changes` and
`## Removes`, and the three phase records. Stage 2 walked the axes of
`skills/code-review/SKILL.md`. The axes this change adds are the reading of
an argument through a symbolic link, the docstrings and prose that name the
removed mode, and the rule markers the removed cases carried.

The run of `skills/code-review/scripts/chain_check.py` printed two notices at
`frame/design.md:75`, the `remove` of *The unverified record, and the
baseline it is read against*. One names "not in the tree" at
`tests/skills/test_settle.py:1738`, and the other names "is not in the tree"
at `tests/text/test_the_release_tail_does_not_end_at_the_tag.py:193`. The
first is an assertion about a settle run's output. The second is the message
of a check that a checklist box names an existing script. Neither pins the
wording of that docs section, and neither pins a fact read from it. Both are
matches on a common phrase, so neither is a finding.

## Findings

### 1. The implement skill says no script reads a closed row's second cell, and two scripts read it

```seal
severity: should
location: `skills/implement/SKILL.md:382-385`
evidence: read `skills/implement/SKILL.md:382`, `skills/verify/scripts/unverified_check.py:807-813`, `skills/settle/scripts/settle.py:1763-1771`, `skills/settle/scripts/settle.py:1831-1833`, `tests/skills/test_settle.py:877`, `seal/threads/1793862999-unverified-baseline-is-run-by-a-person-only/frame/design.md:37`; executed `git grep -n -i 'second cell\|what closed it' -- tests skills/implement skills/verify/SKILL.md`
```

Why it matters: `e8e53f01` replaced the paragraph that said the command
reads the **number** of rows with "No script reads what the second cell of a
closed row says" (`skills/implement/SKILL.md:382`). That is false at HEAD in
two places. `parse_section` reads the second cell of every row and refuses
it where it is empty (`skills/verify/scripts/unverified_check.py:807`) or
still the template's placeholder (`:812`). `settle.py#closed_rows` returns
the second cell of each closed row (`skills/settle/scripts/settle.py:1771`),
and `apply` prints it as "what closed it: ..." (`:1833`), which
`tests/skills/test_settle.py:877` pins. The crafter, who writes and closes
rows, reads this skill and acts on it. The claim that matters, that no check
judges whether the cell says what closed the item, is true. The sentence
around it states more than that. Design *Scope* item 9
(`frame/design.md:37`) asked for this wording, so the frame states the same
false fact. The snippet below does not reach the design, and the
orchestrator owes the fold there.

```markdown
No check reads whether the second cell of a closed row says what closed the
item: `seal unverified` refuses that cell only where it is empty or still the
template's placeholder, and `seal settle` prints it as it stands. So the
second cell saying what closed the item is a convention no check enforces.
Leaving the original answerer in place beside the word is how a closing goes
out unproven, and only a reader catches it.
```

### 2. The proofer is made the one reader of a deleted row, and the proofer's own procedure never asks it to read one

```seal
severity: should
location: `skills/code-review/SKILL.md:29-33`, `skills/implement/SKILL.md:376-379`, `skills/verify/SKILL.md:239-241`
evidence: executed `grep -n -i 'gaps.md\|closing memo\|delet' agents/proofer.md skills/code-review/SKILL.md skills/code-review/orchestration.md agents/sealer.md`; executed a whitespace-collapsed search of every tracked file outside `seal/threads` and `.test_durations` for `deleted rather than closed`, `a deleted row` and `rows? (that )?left (the record )?without`; read `skills/code-review/SKILL.md:29-33`
```

Why it matters: after this change, nothing but the proofer reads a
`## Not verified` row deleted instead of closed, or a `gaps.md` deleted from
a work item that stays. `skills/implement/SKILL.md:376-379`,
`skills/verify/SKILL.md:239-241`, the module docstring at
`skills/verify/scripts/unverified_check.py:25-27`, and the changelog
fragment's first item all say so. The changelog calls the proofer "now the
one reader". The proofer opens `agents/proofer.md` and
`skills/code-review/SKILL.md`. The crafter reads the implement skill, and a
session reads the verify skill. Neither of the proofer's two files tells it
to look for a row that left or a memo that was deleted. Stage 1 of
`skills/code-review/SKILL.md:29-33` treats `gaps.md` rows only as the
implementer's claims to check, which is a reading of the rows that remain.
The search found these sentences only in the two edited skills and the
module docstring. Before this change, a person running
`seal unverified --baseline` was a second reader, so this gap went unseen.
The change removes that reader, so the reading it now relies on has to be
in the proofer's own procedure. Without it, the release tells users that a
reader exists when no reader is instructed to do that reading.

Add this to `skills/code-review/SKILL.md` after the paragraph that ends at
line 33. The two sentences in the implement and verify skills then describe
a step the proofer's own skill states:

```markdown
A `## Not verified` row is closed by marking it, never by deleting it
(`skills/implement/SKILL.md` *4. The closing memo — only what the diff
cannot show*), and no script reads a row or a `gaps.md` that the diff
removes. So at stage 1 the proofer reads the closing memo's diff. A row
that left without opening with the word `closed`, or a `gaps.md` deleted
from a work item directory that stays, is a `must` finding. A work item
directory that the diff removes whole is a settle and not a deletion
(`docs/checks/the-fold.md` *The fold, and what tells it from a deletion*).
```

## Confirmations

What matched: design *Scope* item 1 and A1. `main` holds no `--baseline`
(`skills/verify/scripts/unverified_check.py:1342-1348`). Run through the
launcher, `bin/seal unverified --baseline HEAD .` printed
`unrecognized arguments: --baseline` and exited 2, and the usage line names
only `[-h] [path ...]` (executed). The plain run over `seal/threads` exited 0
(executed). `Test_main::test_refuses_the_baseline_option_it_no_longer_has`
pins both the exit and the help text.

What matched: design *Scope* item 2. None of the eleven removed names stands
in the tree outside `seal/threads` (executed: `git grep -n -w` for each name).
The module imports nothing it does not use, and neither do the two changed
test modules (executed: an `ast` walk over imports and names). `errno` and
`pathlib` are gone.

What matched: design *Scope* item 3 and phase 1's mutant claim. `overviews`
reads `os.path.realpath` at `skills/verify/scripts/unverified_check.py:934`.
With that line changed to `os.path.abspath`, the selection
`-k 'Test_main or Test_overviews or Test_module'` failed on
`Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link`
alone, and 24 cases passed (executed, then reverted). The claim that only a
`Reference specs` prefix row lets that case tell the two readings apart was
not probed. It stays the crafter's account.

What matched: design *Scope* items 4 and 12. A search of the module for
`base`, `compar`, `delet`, `ref`, `relax`, `legacy` and `both sides`
(executed) leaves only sentences that hold at HEAD: `readable`'s "on disk
and at a ref alike", which `chain_check.py` reads at HEAD
(`skills/code-review/scripts/chain_check.py:687`); the docstrings of
`resolves`, `merge_base` and `settled`, which name `chain_check.py`'s calls
at `:1892`, `:1964` and `:1864`; and `tree_at`. `check_text(text)` and
`open_record_rows(root, directory)` have the signatures *Data & interfaces*
states. `settle.py:944` and `:1795` pass no `None`. `sections` has its string
arm only, and its two shipped callers, `check_text` and
`skills/code-review/scripts/pr_body.py:448`, pass a string.
`git grep -n -w -e strict_header -e _text_at -- ':!seal/threads'` exited 1
(executed), as phase 3 claims.

What matched: phase 1's departure on `SETTLED`. Phase 1 claims the clause
"and nothing left the record without being closed" claims what only the
base comparison measured. The clause stood at `a0303ee9`
(`unverified_check.py:1535-1539` there), and no run measures it at HEAD.
`Test_main::test_the_roots_own_specs_path_is_settled_when_nothing_is_under_it`
pins the new sentence and asserts that "left the record" is absent from it.
The departure stands on `skills/core/SKILL.md` *The rule a mechanism is kept
against*. The changelog fragment states it.

What matched: design *Scope* item 5 and phase 1's claim that each removed
case ran only under a baseline. Of the cases removed from
`tests/skills/test_unverified_check.py`, two had a run without `--baseline`
(executed: a split of the base module's cases, with each `run(` and `main(`
line read). These are the help case, which A1 replaces, and the no-root
case, whose plain run is `test_accepts_no_root_in_the_tree`. The parametrized
plain runs at `a0303ee9` lines 2855 to 2935 and the cases at 2950, 2962,
2973 and 2430 keep their plain runs at HEAD lines 1884 to 1980. The walk
skipping `build/`, which the removed
`test_accepts_an_overview_tracked_under_a_skipped_directory` reached only
under a baseline, stays pinned by
`Test_overviews::test_accepts_every_overview_under_a_path_once_skipping_build_output`.

What matched: design *Scope* item 6 and A3. `git grep -n
'a-settle-is-no-deletion\|one-merge-base' -- tests docs` names the marker
only at `tests/skills/test_chain_check.py:4026`, on the case that asserts
"retired: a settle" (executed). `bin/seal rules --check` exited 0 with one
line excused, `one-merge-base` at `docs/checks/the-unverified-record.md:14`,
which the design's `remove` takes out (executed).

What matched: design *Scope* items 9 to 11, A5 and A6. A5's command names
only `docs/checks/the-fold.md:21` (executed). A whitespace-collapsed search
for the mode's statements across every tracked file outside `seal/threads`
and `.test_durations` (executed) also finds `docs/checks/the-fold.md:158-159`,
where the line grep cannot see `seal unverified` and `--baseline` across a
line break. The design's second `change` on that file quotes the passage as
its `from`. The other `--baseline` hits outside `seal/threads` belong to
`chain_check.py`, `payload_meter.py` or the workflow reader's shape fixtures.
The implement skill names no command that lists a deleted row. The verify
skill's citation names the heading at `skills/implement/SKILL.md:329` as it
is spelt.

What matched: the new tests read against their groups. `seal layout --pairs`
names no pair in `tests/skills/test_unverified_check.py` (executed). In
`Test_sections`,
`test_accepts_the_heading_spelt_exactly_and_no_heading_near_it` holds the
exact match that the refusal case beside it does not hold. In
`Test_overviews`, the link case holds the reading through a link, and the
walk case beside it does not hold that reading. A1 is the only case in
`Test_main` that passes an option. Each new case covers something its group
does not already cover.

What matched: `gaps.md` labels the full suite, lint and typecheck at HEAD
`unverified`, with the orchestrator's broad gate named as the answerer. That
label is honest. This round ran no broad command.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `c2702707` | the `Broad gate` row of `seal/config.md` | the orchestrator, at the broad gate |
| `ruff check` and `ruff format --check` on the changed Python files, which phases 1 and 3 claim exit 0. No `ruff` was on this machine's path or in the clone's virtual environment | `skills/verify/scripts/unverified_check.py`, `skills/settle/scripts/settle.py`, `tests/skills/test_unverified_check.py`, `tests/behaviour/test_unverified_rows_close.py`, `tests/skills/test_chain_check.py`, `tests/behaviour/test_a_reference_root_is_read_and_never_taken.py` | the orchestrator, at the broad gate |
| Whether `Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link` runs or skips on Windows | `tests/skills/test_unverified_check.py:1414` | the orchestrator, reading the pull request's Windows CI leg |
| Phase 3's six `seal mutate` mutants, which this round did not re-run | `skills/verify/scripts/unverified_check.py` | the sealer, where it samples the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_unverified_check.py tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_a_reference_root_is_read_and_never_taken.py tests/skills/test_settle.py tests/github/test_rules.py tests/skills/test_pr_body.py -q -p no:randomly` | exit 0, 607 passed |
| `bin/test tests/skills/test_chain_check.py -q -k 'Test_retired or Test_module'` | exit 0, 11 passed |
| `os.path.realpath` changed to `os.path.abspath` at `skills/verify/scripts/unverified_check.py:934`, then `bin/test tests/skills/test_unverified_check.py -q -p no:xdist -k 'Test_main or Test_overviews or Test_module'` | exit 1: only `Test_overviews::test_refuses_a_reference_root_on_a_walk_reached_through_a_link` failed, and 24 passed. The line was restored, and `git status --short` printed nothing |
| `bin/seal unverified --baseline HEAD .` | exit 2, `unrecognized arguments: --baseline` |
| `bin/seal unverified seal/threads` | exit 0, `33 closing memos · 112 open · 11 closed · 0 unreadable` |
| `bin/seal rules --check` | exit 0, 1 excused in 226 check lines |
| `bin/seal layout --check`; `bin/seal layout --pairs` | both exit 0; no report and no pair for the unverified module |
| `git grep -n -e "seal unverified --baseline" -e "\[--baseline <ref>\]" -- ':!seal/threads'` | `docs/checks/the-fold.md:21` alone |
| `git grep -n -w -e strict_header -e _text_at -- ':!seal/threads'` | exit 1, no output |
| `python3 skills/code-review/scripts/chain_check.py --baseline a0303ee9 --root <the clone> --worktree`, run before this record existed | exit 0; two test-pin notices at `frame/design.md:75`, weighed above, and the round, gate and guarantee records named as absent |
