# The review and parity arms

Authority for the two opt-in arms of the commit gate, the review arm and the
parity arm: what each wants before a commit, its mark, its waiver and where it
stays silent, and the routing declaration that moves the review arm's check
to the pull request. Where the arms are asked from is
`docs/the-commit-gate-inside-git.md`, inside the commit where this plugin's
git hooks run, and `docs/commit-review-gate-spec.md`, the PreToolUse reading
where they do not. What the pull-request check reads of a round record is
`docs/the-review-record.md`. Update spec and code together.

## The two arms of the commit gate

The two arms are evaluated independently: each has its own mark, waiver token
and silence, and one satisfied never quiets the other. They are not declared
independently: the migration config lives at `seal/parity.md`, so declaring it
creates `seal/`, which opts into the review arm too. A repository that wants
the parity arm alone waives the review arm per command.

### Review arm

Opt-in: `seal/` at the repository root, or under the common git directory in
local mode.

| Condition | Decision |
|---|---|
| the waiver in the command | silent, and visible in history |
| a `routing.md` declaration names this branch, for either answer | silent: the routing question was answered before the first edit, and CI checks the answer at the pull request |
| `specseal-reviewed` equals current HEAD | satisfied |
| the change confined to `docs/`, `seal/` | no different from any other change — this arm reads no paths. The paragraph below says why |
| otherwise | contributes a stop |

**The review arm reads no paths: a change confined to `docs/` and `seal/`
meets it as any other change does, and a lighter tier is declared, never
inferred.**

**Why this arm has no document-root line.** The parity arm asks whether the
original was consulted, and a `docs/` file has no original, so its silence
there is right. This arm asks whether anybody reads the change before it
lands, and `docs/` is the policy the code conforms to; review finds defects
there as it does in code. A documentation pass that should reach nobody is
routed that way before the first edit, by declaring `straight to the PR`; it
is never inferred from the paths it touches.
check: review-arm-asks

**The waiver goes in front of the command.** After `git commit` a bare word is
a pathspec and git rejects the command, and a `#` comment is no comment in
interactive zsh, so `: '[no-review]'; git commit …` puts the token inside a
no-op `:`, where the shell discards it and the history keeps it.
`git -c specseal.waive=review commit …` is the same waiver in git's own
spelling, and the one a refusal names first.
check: tests/test_the_waiver_can_be_typed.py

#### The declaration, and where the check went

**The gate reads `seal/specs/<work-item-id>/routing.md` before it reads
anything else.** Where a declaration is in force the review arm stays silent
for either answer, because asking for the waiver as well would ask for the
same answer twice.

| The declaration says | At the commit | At the pull request |
|---|---|---|
| through the review chain | silent | a committed `rounds/round-N.md` with no finding left `open`, the last record's `target:` commit at HEAD or followed only by the work item's own records, and the broad run's `broad-gate.md` and the sealer's `guarantee.md` beside it |
| straight to the PR | silent | `broad-gate.md` beside the work item's records, naming the one broad run the orchestrator took at a SHA the tree can see, and the sealer's `guarantee.md` reading `sealed` at HEAD. A draft pull request prints instead of failing, and the declaration is printed either way |
| nothing readable, or no file | the review arm's table above | pass, with a notice saying nothing was checked |

What the check reads of each round record under the first answer is
`docs/the-review-record.md` *What the check reads at the pull request*.
check: routing-read-first

**`straight to the PR` owes the broad run's `broad-gate.md` and the sealer's
`guarantee.md` and turns off the reviewer alone, and `Review` has two
answers, not three.** Two answers, and not three: a review's record is worth
something only because somebody other than the author wrote it, and the
contract names a review that certifies itself as what the commit gate exists
to catch. What an author's own check leaves that CI can read is what it ran,
the broad gate at a SHA against a base, and that is the broad run's record
the direct answer already owes. A change no work item owns writes no
declaration: it takes the third answer of `templates/sdd-routing.md`.
check: two-review-answers

**There is no standing waiver: a declaration moves the review arm's check to
the pull request, and the waiver stays per command.** Both answers stay
enforced, the chain at the pull request against the round record and the
direct route against the broad run's record, and no value means no
enforcement anywhere. Which declaration applies is settled by the branch it
names, looked up from the checked-out branch. Every way that lookup can fail
(a renamed branch, a detached HEAD, two declarations naming one branch, a
file that will not parse) resolves to *no declaration*, and therefore to
**asking**: a fail-open here would be a gate a corrupt file switches off.

What it costs:

- A commit on a declared branch is not stopped as it is typed; between the
  declaration and the pull request, nothing local blocks.
- A branch that declares the chain and never opens a pull request is checked
  by nothing, and the `Destination` axis is what makes that a declared state.
- A repository that adopts the declaration and not the workflow has traded a
  prompt for a convention, and the plugin cannot detect that state.
- Deleting the routing file restores the review arm's table exactly.

**A declaration the pull request retired is not one it made**, and neither is
one it only renamed. The rename is how a root move renames every declaration
at once, and the retirement is `settle --apply` removing a released work
item's directory once `docs/` holds its rule changes. A settle is what tells a
retirement from a deletion, because both leave the file absent at `HEAD`: a
declaration whose directory is gone is asked `unverified_check.py#settled` at
the merge base, the predicate `docs/the-record-layout.md` *The fold, and what
tells it from a deletion* states. Where it holds, the check prints
`retired: a settle`; where it does not, the refusal stands.

Every record is read as git carries it at `HEAD`, never as the working tree
holds it, because CI never sees a working tree. `--worktree` reads the working
tree instead, for a local check before a commit, and CI keeps the default.
check: a-declaration-removed

### Parity arm

Opt-in: `seal/parity.md`. Ported behaviour follows the original where policy
is silent, so a commit that changes code carries a record that the original
was consulted. Mark: `<git-dir>/specseal-parity`, written by the
`legacy-parity` skill after an actual comparison.

| Condition | Decision |
|---|---|
| `[no-parity]` in the command, placed as the review arm's waiver is | silent, and visible in history |
| the change confined to `docs/`, `seal/` | silent: nothing there can be compared against an original |
| `specseal-parity` equals current HEAD | satisfied |
| otherwise | contributes a stop |

"The change" is every path the commit would carry: `changed_paths()` reads
the staged diff and what `-a` and a trailing pathspec pick up.

**A diff git could not take is not a change confined to the document roots.**
Where a `git diff` that lists the paths exits non-zero, cannot start or times
out, the paths are unknown and the arm stops. The PreToolUse reading,
`pre-commit` and the `reference-transaction` backstop read the paths through
one runner, `hooks/gate.py#git`, which answers None for a failure, and
`hooks/gate.py#touches_code` answers True for None, a branch with no commit
yet included.
check: tests/test_chain_hooks_hardening.py

The mark says a comparison was recorded, not that it was a good one. Writing
it for work nobody compared turns "nobody checked" into "someone checked and
it was fine", the one claim the parity methodology exists to keep honest.
