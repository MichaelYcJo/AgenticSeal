# Review round 3: 1793163944-the-issues-were-filed-against-the-old-tree

target: 4e635bd4, fixes e9006f9a..4e635bd4

This round verifies the fix for round 2. The range holds two commits:
`a28fbc24`, the crafter's fix pass, and `4e635bd4`, its answer. Carried from
round 2 without searching again: the two verdict lines of `round-1.md` and
the deleted `trail/phases/phase-5.md`. Re-derived here: whether each verdict
now names the commit that made the repair, and whether the evidence moved
into the answers is the evidence the deleted record held. No GitHub object
changed in this range, so nothing was read there again.

## Findings

None.

## Confirmations

confirms: round-2#1
The close holds. The commands and reads behind it:

- At `4e635bd4`, both verdicts in `trail/rounds/round-1.md` read
  `fixed bb9130fc` (`:23`, `:96`). `bb9130fc` changes
  `frame/design.md` alone (executed, `git show --stat`), and that file is
  on each finding's `location:` line. So each verdict names the commit that
  made the in-tree repair.
- Both `answer:` lines say that the GitHub edits made no commit.
- `trail/phases/phase-5.md` is gone from both `location:` lines, and from
  the tree at `4e635bd4`. `trail/phases/` holds phases 1 to 4 (executed,
  `git ls-tree`).
- The evidence moved into the answers equals what the deleted record held,
  checked against `git diff e9006f9a..4e635bd4`, which shows the record's
  removed text (executed):
  - finding 1: the three body edits, each with exit 0, and `updatedAt`
    06:01:52Z to 06:06:36Z for #1109, 05:29:42Z to 06:06:37Z for #1110,
    and 05:29:49Z to 06:06:39Z for #1111, with the note on #1109's earlier
    `updatedAt`;
  - finding 2: the eight old and new titles, each with exit 0, and the
    6,544-line reading behind #1049's "about 6,500 lines".
- The fix pass changed only the verdict, `location:` and `answer:` lines of
  `round-1.md`, deleted the phase record, and wrote round 2's verdict and
  answer.
- A `git grep` for `phase-5` and `81b9a229` in the work item's directory at
  `4e635bd4` finds both only in `trail/rounds/round-2.md`, where they
  describe the range round 2 reviewed (executed). Round 2's own `location:`
  still names `trail/phases/phase-5.md`. That is the coordinate of the unit
  the finding was about, and the fix removed that unit. A fix pass does not
  edit a round record beyond its verdict and answer, so the line stands.
- `fixed a28fbc24` names the commit that changed `round-1.md`, which is on
  round 2's `location:` (executed, `git show --stat a28fbc24`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the eight retitles stand: the owner has not answered, and they build on round 1's default | `frame/design.md:47-50` | the owner, through the orchestrator |
| The broad gate over this branch; this round ran no suite, lint or typecheck | `trail/gate.md`, not yet written | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `git diff e9006f9a..4e635bd4` | `phase-5.md` deleted; two verdict, two `location:` and two `answer:` lines of `round-1.md` changed; round 2's verdict and answer written |
| `git show --stat bb9130fc` and `git show --stat a28fbc24` | `bb9130fc` touches `frame/design.md` only; `a28fbc24` touches `round-1.md` and deletes `phase-5.md` |
| `git grep -n -E "phase-5\|81b9a229" 4e635bd4` over the work item's directory | hits in `trail/rounds/round-2.md` only |
| `git ls-tree --name-only 4e635bd4` over `trail/phases/` | `phase-1.md` to `phase-4.md` |
