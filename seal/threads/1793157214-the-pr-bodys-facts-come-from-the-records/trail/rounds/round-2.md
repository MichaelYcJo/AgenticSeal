# Review round 2: 1793157214-the-pr-bodys-facts-come-from-the-records

target: 242e7658, fixes 143fc233..619ac510

## Findings

None. The fix range closes the three findings of round 1, and this round
found no new defect in it.

## Confirmations

confirms: round-1#1
The answer claims that `_composed` now refuses a copied line holding a
closing keyword, using `close_issues_on_release.py#keywords_in` and no
second pattern. The code does this. `pr_body.py:90` loads the closer inside
the same `try` as `chain_check.py`. `_claims` (`pr_body.py:404`) calls
`CLOSER.keywords_in` on the record's line as `readable` gives it
(`pr_body.py:439`), so a line inside a fence claims nothing. `keywords_in`
masks code spans on that line. The closer module has stdlib imports only and
keeps its run under `if __name__ == "__main__":` (`:468`), so loading it
does nothing else. The archived changelog of `3d78c220` was used again. This
round's write over it exited 1 with one `refused:` line at `changelog.md:42`
naming `#732`, and it wrote no body file. The owl thread at `74a680c1` still
writes, exit 0, and its body is byte for byte the body phase 1 generated
(`cmp` exit 0). This thread's own records write with exit 0. The new
parametrize row of
`Test_compose::test_refuses_a_record_it_cannot_copy_faithfully` holds a
bare claim, a claim in a code span and a claim in a fence, and expects one
cause. It passed in this round's run. The crafter's claim that it was seen
red at `143fc233` was read, not re-run. `frame/design.md` S6, `gaps.md` and
`changelog.md` state the same refusal. Executed.

confirms: round-1#2
The answer claims that `_place` names the body file by its name and a
record by its path under the `seal/` root. `pr_body.py:528` does this. A
`--check` over the owl thread given an absolute body path, with a line
added above the copy, exited 1. Its line read
`refused: owl-t.md:1: reads ...`. The write over the `3d78c220` changelog,
given a work item path relative to the scratch directory, named
`seal/threads/1791270162-.../changelog.md:42`. Neither line held a machine
path. The pin at `tests/skills/test_pr_body.py:424` and the new case
`Test_main::test_refuses_naming_no_machine_path` (`:428`) passed in this
round's run. The new case covers what no earlier case did: a record's
refusal printed with absolute paths given. The docstring states, as a
limit, that exit 2 still prints `<item>` as it was given. That is stderr on
an argument the normal flow does not produce, so it is not the line step 2
copies from a refusal. Executed.

confirms: round-1#3
The answer claims the sentence was reworked. It was.
`skills/writing-style/outside-the-review.md:63` now says that the first part
holds the plan's `## Phases` section and the phase records' paths. It also
names each round's target line, each finding's heading with its severity,
verdict and answer lines, the gate's table and `gaps.md`'s
`## Not verified`. It adds that a phase record's text is not copied, so a
fact from one is named by its path. Each part matches `_built` and `_round`
(`pr_body.py:276-333`, unchanged by the fix). The sentence does not mention
the `regression:` and `reopens:` lines, but it does not say that only the
listed lines are copied, so it states nothing untrue. Read.

confirms: none
`frame/design.md` S6, as `242e7658` rewrites it, matches the code's three
refusals at `pr_body.py:436-452`. Read.

No fact was carried from round 1 without re-running it. The probes above
were run again on this round's clone at `242e7658`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Suppose an `answer:` paragraph opens a fence, holds a blank line inside it, and has a closing keyword after the blank. `_claims` reads the record's `readable` lines, which blank that line. The copy stops at the blank line (`pr_body.py:326-332`), so the fence stays open in the body. The closer's `FENCE` pattern needs a closing delimiter, so it would read the keyword. No record in the tree has this shape. This round did not probe it, and it is not a finding. Whether it needs a limit sentence is a question | `skills/code-review/scripts/pr_body.py:326-332`, `skills/code-review/scripts/pr_body.py:404` | the orchestrator |
| The full suite, the repository-wide lint and the typecheck over this branch | `trail/gate.md` | the orchestrator, through `seal gate` after the rounds settle |

## Probes

| Command | Result |
|---|---|
| `bin/seal pr-body h732/seal/specs/1791270162-the-worktree-guard-allows-a-listed-shape-and-asks-the-rest --body <scratch>/h732-body.md`, the directory archived from `3d78c220` | exit 1, one `refused:` line at `changelog.md:42` naming `#732`, no body file written |
| `bin/seal pr-body <scratch>/owl/seal/threads/1793152332-the-stamps-mark-is-an-owl --body <scratch>/owl-body.md`, archived from `74a680c1` | exit 0. `cmp` against phase 1's body exited 0 |
| `bin/seal pr-body seal/threads/1793157214-the-pr-bodys-facts-come-from-the-records --body <scratch>/self-body.md` at `242e7658` | exit 0 |
| `bin/seal pr-body <owl item> --body <scratch>/owl-t.md --check`, the owl body with one line added above the copy | exit 1. The line names `owl-t.md:1` and holds no machine path |
| `bin/test tests/skills/test_pr_body.py -q` | exit 0, 21 passed |
| `bin/seal layout --check` | exit 0, 0 refused |
| `bin/seal rules --check` | exit 0, 265 check lines hold |
