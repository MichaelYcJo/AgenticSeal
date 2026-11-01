# Review round 2: 1793521559-a-finding-is-counted-once

```seal
target: 16465921, fixes afe345a8..16465921
```

This is the verifying round for round 1's fix pass. The target is the diff `afe345a8..16465921` on `fix/1223-a-finding-is-counted-once`, at `16465921a2118718cb6ad31d7d9392b1c747790e`. It holds four commits (executed: `git show --stat`). `2a695ac9` answers round 1's finding 1, and `41b938f6` answers finding 2. `ff06e5ed` appends the fix pass's two close blocks to `round-1.md` and removes no line of it (executed: `git diff afe345a8 16465921 -- .../round-1.md`, no `-` line). `16465921` is the orchestrator's fold into `frame/design.md` and two rows of `frame/plan.md` *Judgments of the run*. No `seal/parity.md` is declared, so the record carries no `original:` line. Everything ran in a `git clone --no-local` of the branch worktree at the target.

Carried from round 1 as coordinates, and opened again rather than searched for: `hooks/lib/routing.py:611-646`, the reader `rounds_unreadable`; `skills/settle/scripts/settle.py:1017`, where the settle takes its work items as the tree's directories that are also released; and the S8 command. Every verdict below is this round's own. The crafter's account was read as a claim. It says each new case was seen red before its fix, `seal mutate` went red on four mutants, the phase-boundary set passed 3525 cases over 51 modules, and S8's output is unchanged. This round checked the seen-red claim against two mutants equal to the old code, and S8 by `cmp`. The 3525 count was not re-run (`## Not judged`).

The axes walked over the new units are the table's ten, and three of this change's own. The first is what a line under the table says when a declaration cannot be read. The second is whether that text is fit to be pasted into a public issue comment, which design S6 makes the output's use. The third is whether every other statement of a fact the fixes reworded was changed along (contract rule 19).

## Findings

### 1. A `routing.md` that cannot be opened prints the machine's absolute path under the table, and the table is pasted into a public issue

```seal
severity: should
location: `.github/scripts/finding_counts.py:116`, `.github/scripts/finding_counts.py:142`, `tests/github/test_finding_counts.py:285-287`, `tests/github/test_finding_counts.py:199-208`
evidence: executed `python3 .github/scripts/finding_counts.py --root <scratch>/fixture --released-at HEAD`, `gh repo view --json visibility`
regression: round-1#2
```

Why it matters: the unit is `chained`'s `(None, why)` answer at `.github/scripts/finding_counts.py:116`, which `41b938f6` added. `frame/design.md` *Data & interfaces* gives the line as `<path>/routing.md: whether it went through the review chain is not read: <why>`, and S6 says the output is the comment's table. The fix sets `why` to `str(problem)`, which for an `OSError` carries the absolute filename. The defect came from round 1's own paste-ready snippet, which the fix followed, and from the convention the build phase set at line 142.

This round built a fixture repository under the round's scratch directory. It held one released work item with no `routing.md`, and the script printed this line (executed, exit 0):

`seal/threads/1700000001-no-routing/routing.md: whether it went through the review chain is not read: [Errno 2] No such file or directory: '<scratch>/fixture/seal/threads/1700000001-no-routing/routing.md'`, where `<scratch>` stands for the round's scratch directory, which the line spells from `/`

The line names the file twice: once from the root, and once as the machine's absolute path. The script's docstring says the settling session posts the table to the `flow-baseline` issue. That issue is #51, in a repository whose visibility is `PUBLIC` (executed: `gh repo view --json visibility`). So a missing declaration puts a path like `/Users/x/...` into a public comment. That path holds a user's home directory, and the repository refuses such paths in its own tracked files. A missing `routing.md` is the likeliest of the states this fix was written for.

The same class stands at line 142, `f"{shown}: {problem}"`, for a round record that cannot be opened. That line is the build phase's work. Round 1 confirmed its case. It is reported here because it was opened. The class was listed by its cause: every place in the script where an exception's text reaches stdout (executed: `git grep -n "{problem}\|str(problem)" -- .github/scripts/finding_counts.py`). There are two places, 116 and 142. The third, line 180, goes to stderr and is not posted. Line 142's case, `tests/github/test_finding_counts.py:199-208`, builds a record that is not UTF-8. A `UnicodeDecodeError`'s text names no path, so the case cannot show the leak. The new case at lines 285-287 asserts only a prefix of the line, so nothing pins `<why>` (contract rule 14).

```python
# .github/scripts/finding_counts.py, beside the constants
def why_not(problem):
    """Why a file was not read, without the absolute path an `OSError`'s text
    carries: the line already names the file from the root, and the table is
    pasted into a public issue's comment. Precondition: none; `strerror` is
    None only for an `OSError` built without an errno, which falls back."""
    if isinstance(problem, OSError) and problem.strerror:
        return problem.strerror
    return str(problem)


# chained, line 116
        return None, why_not(problem)

# item_counts, line 142
            unread.append(f"{shown}: {why_not(problem)}")
```

```python
# tests/github/test_finding_counts.py,
# test_a_declaration_that_cannot_be_read_is_named_under_the_table, in place of
# the startswith at lines 285-287
        assert lines[4] == (
            f"seal/threads/1700000004-no-routing/routing.md: {said}: "
            "No such file or directory"
        ), lines
        assert str(root) not in "\n".join(lines), lines
```

### 2. The docstring of `hooks/lib/routing.py#rounds_unreadable` states one of the three states its body answers for, the same narrowing round 1's finding 1 fixed in the script's message

```seal
severity: should
location: `hooks/lib/routing.py:612`
evidence: read `hooks/lib/routing.py:611-646`, `.github/scripts/finding_counts.py:67-73`, `skills/settle/scripts/settle.py:556`
```

Why it matters: `2a695ac9` reworded the fact of what `rounds_unreadable` answers for in `NOT_LISTED`. It also added a comment at `.github/scripts/finding_counts.py:67-69` that names all three states. Contract rule 19 asks that every other statement of that fact be corrected in the same pass. The reader's own docstring summary, at `hooks/lib/routing.py:612`, still reads "True when `rounds` exists beside the work item and is not a directory". Its body answers True for any link, including one to a directory that holds records (lines 627-636). It also answers True for a directory nothing can list (lines 639-645). The summary is wrong for both.

This summary line is the likeliest source of the build phase's "it is not a directory". An agent that reads the summary and not the body writes the narrow message again. `skills/settle/scripts/settle.py:556` states the three states correctly, so the tree now holds two readings of one fact. The line predates this work item and lies outside the fix diff. It is reported because the fix and round 1's finding both cite this function. The fix pass may close it `deferred <home>` if it judges the file out of the work item's scope. The class was listed by every statement of what `rounds_unreadable` answers for (executed: `git grep -n "rounds_unreadable" -- ':!seal/threads'`, outside `tests/`). That gave five places. `finding_counts.py:67`, `release_seal.py:340`, `routing.py:607` and `settle.py:603` do not restate the states, and `settle.py:556` states them rightly.

```python
def rounds_unreadable(item):
    """True when `rounds` beside the work item is a link, any link, a path
    that is not a directory, or a directory nothing can list.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `NOT_LISTED` at `.github/scripts/finding_counts.py:70-73` now reads "the round records cannot be listed: it is a link, a file, or a directory nothing can list". That is true of each arm of `hooks/lib/routing.py:627-645`: any link, a path that exists and is not a directory, and a directory `os.listdir` cannot list (read). The case at `tests/github/test_finding_counts.py:211-240` is parametrized over a file and over a link to a directory holding a record, and pins the whole line. In the clone, an `Edit` put the old text back, and both parameters failed (executed: `bin/test tests/github/test_finding_counts.py -q -p no:xdist -k "cannot_be_listed or declaration_that_cannot"`). The edit was reverted. The third state is not built, as the close says, because the case would have to remove its own read permission. That gap is stated and does not change the verdict: the text is true of that state too. The close's remark that `trail/phases/phase-1.md` decision 4 keeps the old text, as a record of what stood at `2665efb1`, holds. A phase record is history, and its text names the commit. The narrowing's other statement is finding 2.

```seal
confirms: round-1#2
```
What holds: the silent skip is gone. `chained` at `.github/scripts/finding_counts.py:108-119` returns `(True, None)`, `(False, None)` or `(None, why)`. `main` at lines 194-205 skips a released item the tree no longer holds, prints a line for the `None` answer, and skips a straight-to-the-PR item with no line (read). The comment at line 195 says `seal settle` lists such an item nowhere. That holds at `skills/settle/scripts/settle.py:1017`, which takes the tree's directories that are also released, and at `work_items`, which lists directories alone (read). `routing.parse` returns None or a dict that holds `review` (`hooks/lib/routing.py:243-262`), so `parsed["review"]` at line 119 cannot raise (read). In the clone, an `Edit` made the `None` arm unreachable, which is the old loop's behaviour. The new case `test_a_declaration_that_cannot_be_read_is_named_under_the_table` then failed (executed, the same command as above). The edit was reverted, and `git status --short` was empty. The text of `<why>` for a file that cannot be opened is finding 1, a regression of this fix. It does not reopen this close, because the defect the finding named, a row missing with nothing said, is fixed.

```seal
confirms: none
```
What matched: S8 is unchanged. `python3 .github/scripts/finding_counts.py --released-at 813665f0`, run in the clone at the target, exited 0. Its stdout was byte for byte the block `trail/phases/phase-1.md` pastes (executed: `cmp` against that block, exit 0). The crafter's claim that S8's output did not change holds. The plan's two modules pass at the target: `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` gave 181 passed, exit 0 (executed). That is round 1's 179 plus the new parameter and the new case. This narrow run is a probe and never the broad gate.

```seal
confirms: none
```
What matched: the new tests read against their group. `bin/seal layout --pairs tests/github/test_finding_counts.py` names no pair, and `bin/seal layout --check` on the module exits 0 (executed). The new case covers three states that its neighbour `test_the_rows_are_the_released_items_routed_through_the_chain` does not reach: a missing `routing.md`, one that is no declaration, and a work item removed after the release. It shares only the straight-to-the-PR item. The link parameter of the unlistable case covers the first arm of `rounds_unreadable`, which no case built before.

```seal
confirms: none
```
What matched: the orchestrator's fold and the texts that came along. `frame/design.md` *Data & interfaces*'s Stdout bullet now states both lines and the skip of a removed item, as `main` prints and skips them (read). The two new rows of `frame/plan.md` *Judgments of the run* cite headings that exist: *The frame is read against the issue at the spawn* at `skills/implement/orchestration.md:81`, and *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer* at `skills/code-review/orchestration.md:18`. That section holds the sentence on folding a statement into the frame (read). The module docstring at `.github/scripts/finding_counts.py:17-33` and the new sentence in `changelog.md` say what the code does (read). The words of the fact `2a695ac9` reworded were searched (executed: `git grep -n "cannot be listed\|it is not a directory\|NOT_LISTED\|NOT_ROUTED\|NO_DECLARATION"` outside `seal/threads`). The only hits that state it are the script and its case. The other place stating it is not those words but finding 2's.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's claim that its phase-boundary set passed 3525 cases over 51 modules. This round re-ran the plan's two modules alone. | the crafter's hand-back, which the spawn prompt carries | the orchestrator, by `seal gate` after the rounds settle |
| The full suite, the repository-wide lint and the format check at the head. `gaps.md` *Not verified* labels them `unverified` and names their answerer, and that label is still honest: neither the fix pass nor this round ran them (contract rule 2). | `gaps.md` *Not verified*, first row | the orchestrator, by `seal gate` |
| S9: whether the design's `## Rule changes` parse with no refusal at the head. This round's `chain_check.py --worktree` reading covers the records arm alone. | `frame/design.md` `## Rule changes` | the sealer, at its guarantee |

## Probes

| Command | Result |
|---|---|
| `python3 .github/scripts/finding_counts.py --root <scratch>/fixture --released-at HEAD`, over a fixture whose one released work item has no `routing.md` | exit 0; the header, the separator, a blank line, and one line whose `<why>` holds the fixture's absolute path; fixture removed |
| `python3 .github/scripts/finding_counts.py --released-at 813665f0` in the clone | exit 0; `cmp` against the phase record's S8 block exited 0 |
| `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` in the clone | 181 passed, exit 0 |
| `NOT_LISTED` edited back to "it is not a directory", and the `None` arm of `main` made unreachable, then `bin/test tests/github/test_finding_counts.py -q -p no:xdist -k "cannot_be_listed or declaration_that_cannot"` | 3 failed (both parameters, and the declaration case); reverted, `git status --short` empty |
| `bin/seal layout --pairs` and `bin/seal layout --check` over `tests/github/test_finding_counts.py` | exit 0 each; no pair |
| `gh repo view --json visibility,nameWithOwner` | `PUBLIC` |
