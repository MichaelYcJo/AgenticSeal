# Review round 1: 1793521559-a-finding-is-counted-once

```seal
target: 2665efb1 against release/v0.27.2
```

No earlier round exists, so this round carries no coordinate from one and re-derives every fact it states. The target is the branch `fix/1223-a-finding-is-counted-once` at `2665efb164a1712de448f81ad9ba9e9e16ea2505`, against `release/v0.27.2` at `813665f0`, which is also the merge base (executed: `git merge-base release/v0.27.2 HEAD`). No `seal/parity.md` is declared, so the record carries no `original:` line. The axes walked are the table's ten, and this change's own: which work items make the rows, what the count does with a record or a declaration it cannot read, and whether each message printed under the table says what happened.

## Findings

### 1. The line printed under the table for an unlistable `trail/rounds` says "it is not a directory" where it is a link to a directory or a directory nothing can list

```seal
severity: should
location: `.github/scripts/finding_counts.py:64`, `.github/scripts/finding_counts.py:114-116`, `tests/github/test_finding_counts.py:210-223`
evidence: read `.github/scripts/finding_counts.py:64`, `.github/scripts/finding_counts.py:114-116`, `hooks/lib/routing.py:611-646`, `tests/github/test_finding_counts.py:210-223`
```

Why it matters: the settling session reads this line to learn why a work item's four cells read `not read`, and acts on it. The phase record's decision 4 claims the line tells the session which cause it was. `.github/scripts/finding_counts.py:114-116` prints `NOT_LISTED` whenever `routing.rounds_unreadable(where)` is true, and `NOT_LISTED` (line 64) states one cause: "it is not a directory". `hooks/lib/routing.py:611-646` returns true for three states: any symbolic link, including one that resolves to a directory holding records (lines 627-636); a path that exists and is not a directory (lines 637-638); and a directory that `os.listdir` cannot list (lines 639-645). For the first and third, the line tells the session something false. Someone who then runs `ls` sees a directory, and the line has sent them the wrong way. `.github/scripts/release_seal.py#chain_counts` names only the path and states no cause. The one case, `tests/github/test_finding_counts.py:210-223`, builds the file shape alone, and it asserts only that the line starts with the path. So the message's text is pinned by nothing, and contract rule 14 asks for a pin on a line a person reads.

```python
# .github/scripts/finding_counts.py, line 64
NOT_LISTED = (
    "the round records cannot be listed: it is a link, a file, or a "
    "directory nothing can list"
)
```

```python
# tests/github/test_finding_counts.py, the last two lines of
# test_rounds_that_cannot_be_listed_read_not_read_in_every_cell
path = f"seal/threads/{ITEM}/trail/rounds"
assert under == [
    f"{path}: the round records cannot be listed: it is a link, a file, "
    "or a directory nothing can list"
], under
```

```seal
verdict: fixed 2a695ac9
answer: The finding holds: `hooks/lib/routing.py:611-646` answers True for any link, a path that is not a directory, and a directory nothing can list, and the line named only the second. `NOT_LISTED` now reads the paste-ready text, which is true of each of the three, and a comment above it names them. The case is parametrized over a file and a link to a directory holding a record, and pins the whole line; both were seen red against the old text before the fix, and `seal mutate` back to "it is not a directory" turned the case red after it. A directory nothing can list is not built, because the case would need to drop its own read permission. The phase record's decision 4 still quotes the old text, as the record of what stood at 2665efb1.
```

### 2. A released work item whose `routing.md` is missing or does not parse leaves the table with no row and no line saying so

```seal
severity: should
location: `.github/scripts/finding_counts.py:94-102`, `.github/scripts/finding_counts.py:175-178`, `.github/scripts/finding_counts.py:24-30`, `tests/github/test_finding_counts.py`
evidence: read `.github/scripts/finding_counts.py:94-102`, `.github/scripts/finding_counts.py:175-178`, `.github/scripts/finding_counts.py:24-30`, `hooks/lib/routing.py:255-260`, `skills/settle/scripts/settle.py:1018`
```

Why it matters: the script's docstring (lines 24-30) takes the stance that "an incomplete count is a wrong number" and promises one line under the table for each record or directory not read. `frame/design.md` takes that stance from `.github/scripts/release_seal.py#chain_counts`, where a tree with no declaration reads `not read` rather than 0. `chained` (lines 94-102) returns `False` for three different states: the declaration answers `Review` `straight to the PR`; `routing.md` is missing or not UTF-8, caught at line 100; and `routing.parse` returns `None`, which `hooks/lib/routing.py:255-260` does for any table outside its strict vocabulary or with a doubled label. `main` (lines 175-178) skips all three with the same silent `continue`. The second and third are a work item that `seal settle` lists as released, since `skills/settle/scripts/settle.py:1018` takes every directory present in the tree and at the ref with no reading of its routing. For those, the script can say neither that the item went through the review chain nor that it did not. The table then reads as if the item were routed straight to the pull request, and the comment on the `flow-baseline` issue reports a total for fewer work items, with nothing saying which one is missing. No released work item at `813665f0` is in that state: all eight parse with `through the review chain`. So the defect is latent, and the first broken declaration makes it show. The design's *Scope* item 2 defines the rows as the work items "whose `routing.md` parses with `Review` `through the review chain`". The fix keeps those rows and adds a line under the table, which adds output as the phase record's decision 4 did, so the frame does not have to change. It owes a case in `tests/github/test_finding_counts.py`.

```python
def chained(routing, where):
    """`(True, None)` where `where/routing.md` parses with `Review` `through
    the review chain`, `(False, None)` where it parses with another answer,
    and `(None, why)` where it cannot be read or is no declaration."""
    try:
        with open(os.path.join(where, routing.FILENAME), encoding="utf-8") as f:
            parsed = routing.parse(f.read())
    except (OSError, UnicodeDecodeError) as problem:
        return None, str(problem)
    if not parsed:
        return None, "it is no declaration `hooks/lib/routing.py#parse` reads"
    return parsed["review"] == routing.CHAIN, None


# in main, replacing the loop's first three lines
    for name in sorted(released):
        where = os.path.join(root, settle.SPECS, name)
        if not os.path.isdir(where):
            # Absent from the tree: `seal settle` lists it nowhere either.
            continue
        through, why = chained(routing, where)
        if through is None:
            shown = os.path.relpath(
                os.path.join(where, routing.FILENAME), root
            ).replace(os.sep, "/")
            unread.append(f"{shown}: whether it went through the review chain is not read: {why}")
            continue
        if not through:
            continue
```

```seal
verdict: fixed 41b938f6
answer: The finding holds: `chained` returned False alike for `straight to the PR`, for a `routing.md` that could not be opened and for one `routing.parse` reads as no declaration, and `main` skipped all three in silence. The fix follows the paste-ready shape. `chained` returns `(True, None)`, `(False, None)` or `(None, why)`. `main` skips a released item the tree no longer holds, which `skills/settle/scripts/settle.py:1017` also leaves out, and prints `<path>/routing.md: whether it went through the review chain is not read: <why>` under the table for the `None` case; the sentence and the no-declaration reason are the constants `NOT_ROUTED` and `NO_DECLARATION`. One new case builds a chained item, a straight-to-the-PR item, an item with no `routing.md`, one whose `routing.md` is no declaration, and one removed after the release, and pins the table and both lines. It was seen red against the silent loop, and each of three `seal mutate` mutants (no line, no declaration read as another answer, no removed-item skip) turned it red. The module docstring now says the same, and `changelog.md` gains one sentence. `frame/design.md` *Scope* item 2 keeps its rows, and its *Data & interfaces* Stdout bullet does not name this line; the fix pass does not edit the frame.
```

## Confirmations

```seal
confirms: none
```
What matched: S8. `python3 .github/scripts/finding_counts.py --released-at 813665f0`, run in the clone at the target, exited 0 and printed the eight rows that `trail/phases/phase-1.md` pastes, cell for cell. `1793521559-a-finding-is-counted-once` is no row (executed). The claim in `frame/design.md` that all eight released work items parse with `Review` `through the review chain` holds: a read-only `python3 -I -c` over `settle.released('.', '813665f0')` and `routing.parse` found eight released items, each with that answer (executed).

```seal
confirms: none
```
What matched: the core of the fix. `skills/code-review/scripts/chain_check.py:758-759` builds `located` from the finding block's `location:` alone, and `paths` as a copy that the close block's paths then extend. So `located` never takes the close block's paths. That is phase decision 1, and the claim holds (read). `Finding` is built at one place, `chain_check.py:772`, and no code outside tests reads it by position. The new field is last in the tuple (executed: `git grep -n "Finding\b\|_make("` and `git grep -n "\.paths"` over the non-test Python). `.github/scripts/finding_counts.py:137` reads `located` with `all(...)` and `chain.under(..., settle.SPECS)`, which is the records-alone rule in *Data & interfaces* (read). The pull-request check's readers, `chain_check.py:908` and `:1118-1120`, still read `paths`, the union that *Out* keeps (read).

```seal
confirms: none
```
What matched: the class of the defect, listed by every reader of a finding's location rather than by a wording. Code that names the field reads it in one of two ways. Either it reads `Finding.paths` (`git grep -n "\.paths"`), which are the pull-request check's two readers above and read the union by design. Or it reads `round_read(...).inside` and keeps `FIELDS.FINDING_BLOCK` alone: `evals/scripts/noninferiority.py:324-332` and `evals/scripts/replay_targets.py:448-455` (executed: `git grep -n "LOCATION\b\|location:"` over the non-test Python, then read). `replay_targets.py` reads the raw value at an older checker (`checks_at`), so `located` cannot stand in for it, and it does not restate the new field. The `^location:` patterns in `evals/scripts/rule_cases.py` grade a proofer's own record, which holds no close block. Only the step's grep, which `frame/design.md` *Removes* names, counted both blocks.

```seal
confirms: none
```
What matched: the seen-red claim for S7 and S2, checked against one mutant. In the clone, an `Edit` passed `paths` in place of `located` to `Finding` at `chain_check.py:783`. Then `bin/test tests/skills/test_chain_check.py tests/github/test_finding_counts.py -p no:xdist -q -k "located_holds or where_the_defect_shows or close_blocks_location"` failed S7 and S2's first parameter, and passed S1 and S2's second (executed). That matches the phase record's mutation table. There, S1 goes red under a different mutant, one count per path, because both of S1's paths lie under `seal/threads/`. The edit was reverted, and `git status --short` was then empty.

```seal
confirms: none
```
What matched: the plan's two modules pass at the target. `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` in the clone gave 179 passed, exit 0 (executed). This is a narrow run, a probe, and never the broad gate. The new tests were read against their group. `seal layout --pairs` names no pair for either module, exit 0 (executed). `seal layout --check` exits 0 and reports, without refusing, the four functions with no class of their own that `gaps.md` *Not done* names (executed). In `Test_record_findings`, the cases at `tests/skills/test_chain_check.py:665` and `:3753` assert `paths` and never `located`, so S7 covers something its group does not. In `tests/github/test_finding_counts.py`, each case covers a distinct behaviour: S1 the count per path, S2 the block that decides, S3 prose and fences, then reopens, a refused record, an unopenable record, an unlistable directory, the rows, the ref, the readers, and the order.

```seal
confirms: none
```
What matched: the departures that `trail/phases/phase-1.md` names, read against the frame. Decision 3, the blank line under the table: `.github/scripts/finding_counts.py:183` prints it, and the `table` helper at `tests/github/test_finding_counts.py:94-106` asserts it wherever lines stand under the table (read). Decision 8, `load` with no `spec is None` arm: `spec_from_file_location` is called only on the three fixed `.py` paths at lines 80-90, and `main` catches a missing file at `exec_module` as a reader that will not load, at lines 160-164 (read). Decision 4 is additive, but its message is wrong in two of its three cases (finding 1). The policy root is untouched: `git diff --stat 813665f0...HEAD -- docs/` printed nothing (executed). The changelog fragment's `### Fixed` heading matches the other seven fragments under `seal/threads/` (executed: `head -1` over each `changelog.md`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the head. `gaps.md` labels them `unverified` and names their answerer, and that label is honest: this round ran none of the three (contract rule 2). | `gaps.md` *Not verified*, first row | the orchestrator, by `seal gate` after the rounds settle |
| Which two edits the crafter made through shell substitution, which its hand-back reports against contract rule 9. Nothing in the tree or in `trail/phases/phase-1.md` names them. This round read every changed file's text in the diff, so the result was judged and the act was not. | the crafter's hand-back, which the spawn prompt carries | the orchestrator, which holds the hand-back |
| The phase-boundary set's "3523 passed and 9 skipped" at `0d28fe61`. It was not re-run. Only `trail/phases/phase-1.md` changed after that commit (executed: `git diff --stat 0d28fe61 2665efb1`). | `trail/phases/phase-1.md`, *The phase-boundary set* | the orchestrator's broad gate |
| S9, whether the design's `## Rule changes` parse with no refusal at the head. This round's `chain_check.py --worktree` reading covers the records arm, and S9 is the sealer's. | `frame/design.md` `## Rule changes` | the sealer, at its guarantee |

## Probes

| Command | Result |
|---|---|
| `python3 .github/scripts/finding_counts.py --released-at 813665f0` in `<clone>` | exit 0; the eight rows of the phase record, no ninth |
| `python3 -I -c` over `settle.released` and `routing.parse` at `813665f0` in `<clone>` | eight released items, each `through the review chain` |
| `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` in `<clone>` | 179 passed, exit 0 |
| `chain_check.py:783` edited to pass `paths` for `located`, then `bin/test ... -k "located_holds or where_the_defect_shows or close_blocks_location"` | 2 failed (S7, S2 first parameter), 2 passed (S1, S2 second); reverted, `git status --short` empty |
| `bin/seal layout --pairs` and `bin/seal layout --check` over the two test modules | exit 0 each; no pair; four functions reported with no class |
