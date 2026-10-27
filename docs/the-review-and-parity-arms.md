# The review and parity arms

Authority for what each routing answer owes at the pull request, and for
the parity arm: what a change in a migration owes, and where that is
checked. Where a session's routing is checked, at its edit tools and at the
pull request, is `docs/the-routing-check.md`. What the pull-request check
reads of a round record is `docs/the-review-record.md`. Update spec and code
together.

## The two arms

**No arm runs at the commit.** The review arm is the routing check, which
runs at a session's edit tools and at the pull request
(`docs/the-routing-check.md`), and the parity arm is checked at the pull
request alone, as *Parity arm* below states. The migration config lives at
`seal/parity.md`, so declaring it creates `seal/`, which opts the
repository into the routing check too.
check: tests/test_routing_edit_gate.py tests/test_chain_check.py

### Review arm

**The review arm is the routing check.** Where it runs is *The two arms*
above; what it refuses, what it reads and what lets an edit through without
a declaration are `docs/the-routing-check.md`. A change confined to `docs/`
meets it as any other change does, because `docs/` is the policy the code
conforms to and review finds defects there as it does in code. A
documentation pass that should reach nobody is routed that way before the
first edit, by declaring `straight to the PR`; it is never inferred from
the paths it touches.
check: tests/test_routing_edit_gate.py

#### The declaration, and where the check went

**The routing check reads `seal/threads/<work-item-id>/routing.md` before it
reads anything else.** Where a declaration names the branch, an edit goes
ahead for either answer, because the routing question was answered before
the first edit.

| The declaration says | At an edit | At the pull request |
|---|---|---|
| through the review chain | allowed | a committed `trail/rounds/round-N.md` with no finding left `open`, the last record's `target:` commit at HEAD or followed only by the work item's own records, and the broad run's `trail/gate.md` and the sealer's `guarantee.md` beside it |
| straight to the PR | allowed | `trail/gate.md` beside the work item's records, naming the one broad run the orchestrator took at a SHA the tree can see, and the sealer's `guarantee.md` reading `sealed` at HEAD. A draft pull request prints instead of failing, and the declaration is printed either way |
| nothing readable, or no file | refused, unless the session recorded, on that branch, that its change belongs to no work item | each commit's `Seal-Routing` trailer is judged as `docs/the-routing-check.md` *At the pull request* states; nothing else is checked, and a notice says so |

What the check reads of each round record under the first answer is
`docs/the-review-record.md` *What the check reads at the pull request*.
check: routing-read-first

**`straight to the PR` owes the broad run's `trail/gate.md` and the sealer's
`guarantee.md` and turns off the reviewer alone, and `Review` has two
answers, not three.** Two answers, and not three: a review's record is worth
something only because somebody other than the author wrote it, and the
contract names a review that certifies itself as what the routing check
exists to catch. What an author's own check leaves that CI can read is what
it ran, the broad gate at a SHA against a base, and that is the broad run's
record the direct answer already owes. A change no work item owns writes no
declaration: it takes the third answer of question 1, `no work item`, in
`skills/implement/orchestration.md` *Question 1*.
check: two-review-answers

**There is no standing waiver: a declaration moves the review arm's check to
the pull request, and a change no work item owns is recorded for one
session on one branch, and stands for no other session.** Both answers stay
enforced, the chain at the pull request against the round record and the
direct route against the broad run's record, and no value means no
enforcement anywhere. Which declaration applies is settled by the branch it
names, looked up from the checked-out branch. Every way that lookup can fail
(a renamed branch, a detached HEAD outside the two cases
`docs/the-routing-check.md` *The edit check* allows, two declarations naming
one branch, a file that will not parse) resolves to *no declaration*, and
therefore to **refusing the edit**: a fail-open here would be a gate a
corrupt file switches off.

What it costs:

- A commit on a declared branch is not stopped as it is typed; between the
  declaration and the pull request, nothing local blocks.
- A branch that declares the chain and never opens a pull request is checked
  by nothing, and the `Destination` axis is what makes that a declared state.
- A repository that adopts the declaration and not the workflow has traded
  the edit check's refusal for a convention, and the plugin cannot detect
  that state.
- Deleting the routing file brings the edit check's refusal back.
- In local mode nothing under the root is committed, so no pull-request
  check reads a declaration or a round record.

**A declaration the pull request retired is not one it made**, and neither is
one it only renamed. The rename is how a root move renames every declaration
at once, and the retirement is `seal settle --apply` removing a released work
item's directory whole. A settle is what tells a retirement from a deletion,
because both leave the file absent at `HEAD`: a declaration whose directory
is gone is asked `unverified_check.py#settled` at the merge base, the
predicate `docs/the-record-layout.md` *The fold, and what tells it from a
deletion* states. Where it holds, the check prints `retired: a settle`;
where it does not, the refusal stands, except where the tree the check reads
has no top-level `seal` entry (`docs/the-review-record.md` *What the check
reads at the pull request*).

Every record is read as git carries it at `HEAD`, never as the working tree
holds it, because CI never sees a working tree. `--worktree` reads the working
tree instead, for a local check before a commit, and CI keeps the default.
check: a-declaration-removed

### Parity arm

Opt-in: `seal/parity.md`. Ported behaviour follows the original where policy
is silent, so a change to code carries a record, in the tree, that the
original was consulted.

| The declaration says | Where the comparison is recorded |
|---|---|
| through the review chain | each round record's `original:` line |
| straight to the PR | one `original:` line in the sealer's `guarantee.md` |
| none | nowhere, and no comparison is checked: each commit's `Seal-Routing` trailer is judged as `docs/the-routing-check.md` *At the pull request* states, and a commit reading `no work item` is printed, visible in history |
| any, for a change confined to `docs/`, `seal/` | nothing is owed: nothing there can be compared against an original |

"The change" is every path the pull request changes against its base.

**A diff git could not take is not a change confined to the document roots.**
Where the pull request's diff cannot be listed, the check ends with exit 2
before any record is judged, and `hooks/gate.py#touches_code` answers True
for a list it was not given.
check: tests/test_gate.py tests/test_chain_check.py

An `original:` line says a comparison was recorded, not that it was a good
one. Writing it for work nobody compared turns "nobody checked" into
"someone checked and it was fine", the one claim the parity methodology
exists to keep honest.

**The parity arm is checked at the pull request, in the record the table
above names for each answer, because a comparison exists only after the
change it compares.** In a review chain the proofer compares the change with
the original after the crafter has committed it, so a check at the commit
would meet each build commit before any comparison of it exists. What the
check reads is `docs/the-review-record.md` *What the check reads at the pull
request*.
Under `straight to the PR` no review round records a comparison, so the
sealer compares the audited commit with the original through
`legacy-parity` and writes the line in `guarantee.md`, where the check
reads it as it reads a round record's. A branch that declares the chain and
never opens a pull request is checked by nothing, which is the cost the
review arm's declaration already states. Three more shapes leave code
nobody compared with nothing that reads it. In local mode no pull-request
check reads a round record, the cost the review arm's declaration already
states. A repository whose
`.github/workflows/hygiene.yml` pins a plugin release older than this rule
runs a `chain-check` that reads no `original:` line, until a person moves
the pin's `v<version>` to the installed release. And a declaration
rewritten from `through the review chain` to `straight to the PR` after
code was committed leaves those commits compared by nobody, because the
check reads the answer at HEAD.
check: parity-at-the-pull-request parity-in-the-guarantee
