# Review round 3: 1793521559-a-finding-is-counted-once

```seal
target: dc5050a1, fixes 1bf95206..dc5050a1
```

This is the verifying round for round 2's fix pass. The target is the diff `1bf95206..dc5050a1` on `fix/1223-a-finding-is-counted-once`, at `dc5050a1899478af1f024cac9227b5da428b02b4`. It holds five commits (executed: `git diff --stat 1bf95206..HEAD`). `527cba5a` answers round 2's finding 1, and `9eacfa51` answers finding 2. `f36673e7` appends the fix pass's two close blocks to `round-2.md` and removes no line of it (executed: `git diff 1bf95206..HEAD -- .../round-2.md`, no `-` line). `6b175886` is the orchestrator's routing row in `frame/plan.md` *Judgments of the run*, and `dc5050a1` is its fold into `frame/design.md` *Data & interfaces*. No `seal/parity.md` is declared, so the record carries no `original:` line. Everything ran in a `git clone --no-local` of the branch worktree at the target.

Carried from round 2 as coordinates, and opened again rather than searched for: `hooks/lib/routing.py:611-646`, the body of `rounds_unreadable`; the S8 command and the block `trail/phases/phase-1.md` pastes at lines 43-52; and round 2's fixture shape, one released work item with no `routing.md`, written again from its `## Probes` row. Every verdict below is this round's own.

The crafter's account was read as a claim. It says each new case was seen red before its fix, a mutant went red, 3774 cases passed over 55 modules, and S8 is unchanged. It also says the directory parameter on Windows is unverified, with CI's Windows leg as its answerer. This round checked the seen-red claim with a mutant equal to the old code, and S8 by `cmp`. The 3774 count was not re-run (`## Not judged`).

The axes walked over the new units are the table's ten, and three of this change's own. The first is whether every reason the script prints to stdout is free of the machine's absolute path, for each kind of file that cannot be opened. The second is whether each new arm of `why_not` is pinned by a case. The third is whether every other statement of a fact the fixes changed was changed along (contract rule 19).

## Findings

### 1. `why_not` is a fifth function with no test class, and `gaps.md` *Not done* still names four and says a class per function would catch nothing more

```seal
severity: should
location: `seal/threads/1793521559-a-finding-is-counted-once/gaps.md:12`, `.github/scripts/finding_counts.py:108-116`, `tests/github/test_finding_counts.py`
evidence: executed `bin/seal layout --check tests/github/test_finding_counts.py`, `bin/test tests/github/test_finding_counts.py -q -p no:xdist`
regression: round-2#1
```

Why it matters: the unit is `why_not` at `.github/scripts/finding_counts.py:108-116`, which `527cba5a` added. The phase's `frame/plan.md` row asks that each new case be seen red, and `frame/design.md` says nothing of test classes. The fix added a function with two arms and left the build phase's account of untested functions as it was. The defect came from the fix pass, which changed the fact `gaps.md` *Not done* states and did not change that statement (contract rule 19).

`gaps.md:12` says that `chained`, `item_counts`, `load` and `readers` have no test class of their own, which `seal layout --check` reports. It says a case of `Test_main` goes red under a mutation of each arm, and that a class per function "would catch nothing more". At the target, `seal layout --check` reports five functions, and the fifth is `function why_not has no class Test_why_not` (executed, exit 0). The fix pass's close does not mention it.

The last claim of that paragraph is false for `why_not`. It has two arms. The first, `strerror` for an `OSError`, is pinned: a mutant that returns the whole text turned both cases red (executed, `## Probes`). The second is the fallback for an `OSError` with no `strerror`, which the docstring says is "said whole". A mutant that drops `and problem.strerror` returns `None` for `OSError()` and for `OSError('x')`, and all 16 cases of the module still pass (executed: the `bin/test` command of the evidence line, run with that mutant in place, `## Probes`). A line under the table would then read `<path>: None`. No `open` call raises an `OSError` without an errno, so the state is not reached from `main`. That is why only a direct case can pin it. It is also why the sealer, reading `gaps.md` against `seal layout --check`, finds a list one short and a reason that does not hold for the fifth function.

Either fix closes it. The first adds the case, and then the paragraph's list is complete as written:

```python
# tests/github/test_finding_counts.py, a class beside Test_main
class Test_why_not:
    def test_an_os_error_is_said_in_its_own_words_without_its_path(self, tmp_path):
        """The error's `strerror`, with no filename, so the line pasted into a
        public issue carries no absolute path (round 2, finding 1)."""
        missing = tmp_path / "routing.md"
        try:
            open(missing, encoding="utf-8").close()
        except OSError as problem:
            said = counts().why_not(problem)
        assert said == os.strerror(errno.ENOENT)
        assert str(tmp_path) not in said

    @pytest.mark.parametrize(
        "problem, said",
        [
            (OSError("no errno"), "no errno"),
            (UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte"),
             "'utf-8' codec can't decode byte 0xff in position 0: invalid start byte"),
        ],
    )
    def test_an_error_with_no_strerror_is_said_whole(self, problem, said):
        assert counts().why_not(problem) == said
```

The second names `why_not` in the paragraph and states the arm no case reaches:

```markdown
`.github/scripts/finding_counts.py`'s `chained`, `item_counts`, `load`, `readers` and `why_not` have no test class of their own, which `seal layout --check` reports and does not refuse. Each is reached through `main`. The mutation table in `trail/phases/phase-1.md` shows a case of `Test_main` going red under a mutation of each arm of `chained` and `item_counts`, and round 2's fix pass shows the same for `why_not`'s `strerror` arm. `why_not`'s other arm, an `OSError` with no `strerror`, is not reached from `main`, because no `open` call raises one, and no case builds it. `load` and `readers` hold no arm, and a reader that will not load is `Test_main`'s readers case.
```

## Confirmations

```seal
confirms: round-2#1
```
What holds: no line the script prints to stdout carries the machine's absolute path for a file that cannot be opened. `why_not` at `.github/scripts/finding_counts.py:108-116` returns an `OSError`'s `strerror`, which holds no filename, and returns the text of anything else. Both callers use it, `chained` at line 127 and `item_counts` at line 153 (read). The class was listed by its cause, every place an exception's text reaches an output (executed: `git grep -n "str(problem)\|{problem}\|strerror\|why_not"` over the script). That gives lines 127 and 153, and line 191, the reader-load message, which goes to stderr. The other stdout text under the table is line 157, the refusals `record_findings` returns. That reader takes the record's text and the root-relative name `shown` (line 155), so it has no absolute path to print (read).

Round 2's fixture was built again under the round's scratch directory. One released work item has no `routing.md`, and the script printed `seal/threads/1700000001-no-routing/routing.md: whether it went through the review chain is not read: No such file or directory`, exit 0 (executed). A second run added two more released items. One has a `routing.md` with mode 000, and its line reads `... is not read: Permission denied`. The other has a `routing.md` that is a directory, and its line reads `... is not read: Is a directory`. Neither output held the scratch path (executed: `grep -c` gave 0). In the clone, an `Edit` made `why_not` return `str(problem)`, which is the old text. The directory parameter of `test_a_record_that_cannot_be_opened_is_named_with_why` and `test_a_declaration_that_cannot_be_read_is_named_under_the_table` then failed, and the not-UTF-8 parameter passed, as the close says it would (executed, `## Probes`). The edit was reverted. Both cases now pin the whole line, so they pin `<why>` as contract rule 14 asks. The close's account of the Windows reason, `Permission denied`, matches what the case reads: it takes `strerror` from its own `open` of the directory, so the expected words are the system's on each platform (read). Whether that parameter passes on Windows was not run here (`## Not judged`). The fallback arm of `why_not` is finding 1. It is a new defect in the fix's unit, and it does not reopen this close, because the leak the finding named is gone.

```seal
confirms: round-2#2
```
What holds: the summary of `rounds_unreadable` at `hooks/lib/routing.py:612-613` now reads "True when `rounds` beside the work item is a link of any kind, a path that is not a directory, or a directory nothing can list". That is true of each arm of the body: any link at lines 628-637, a path that exists and is not a directory at lines 638-639, and a directory `os.listdir` cannot list at lines 640-646 (read). The old words appear nowhere else (executed: `git grep -n "exists beside the work item\|and is not a directory" -- ':!seal/threads'`). The one hit, `skills/implement/scripts/seal.py:932`, describes a `FileExistsError` of another function. The five sites of `rounds_unreadable` round 2 listed were opened again, and none restates the states wrongly (executed: `git grep -n rounds_unreadable` outside `seal/threads` and `tests`).

```seal
confirms: none
```
What matched: S8 is unchanged. `python3 .github/scripts/finding_counts.py --released-at 813665f0`, run in the clone at the target, exited 0 with nothing on stderr. Its stdout was byte for byte the block at `trail/phases/phase-1.md:43-52` (executed: `cmp`, exit 0). The plan's two modules pass at the target: `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` gave 182 passed, exit 0 (executed). That is round 2's 181 plus the new directory parameter. `uvx ruff check` and `uvx ruff format --check` on the three changed Python files exit 0 (executed). These narrow runs are probes and never the broad gate.

```seal
confirms: none
```
What matched: the new test reads against its group. `bin/seal layout --pairs tests/github/test_finding_counts.py` names no pair (executed). The directory parameter covers a state none of its neighbours builds: an `OSError` from opening a round record. The case before it built only a `UnicodeDecodeError`, whose text names no path, so it could not show the leak (round 2). The declaration case's whole-line pin replaces a prefix assertion and adds no case.

```seal
confirms: none
```
What matched: the orchestrator's two commits. The new row of `frame/plan.md` *Judgments of the run* routes round 2's finding 1 to an ordinary fix pass. That matches the second row of the table under `skills/code-review/orchestration.md:177` *A regression is routed by comparing the fix with the frame*, "a review record's paste-ready fix applied as given", and round 2's grounds name that source (read). Finding 1 of this round stands in `why_not`, the function that now spells the reason round 2's finding 1 named. Whether that makes it a second regression on one unit, which that table's third row weighs, is the orchestrator's judgment. The fold into *Data & interfaces*'s Stdout bullet states what `why_not` does: `<path>` is relative to the root, and `<why>` is the error's own words with no absolute path (read). The changelog fragment says "a line under the table names that `routing.md` and why", which stays true (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's claim that 3774 cases passed over 55 modules. This round re-ran the plan's two modules alone. | the crafter's hand-back, which the spawn prompt carries | the orchestrator, by `seal gate` after the rounds settle |
| Whether the directory parameter of `test_a_record_that_cannot_be_opened_is_named_with_why` passes on Windows, where opening a directory raises `PermissionError`. This round ran on macOS. | `tests/github/test_finding_counts.py:200-231` | CI's Windows leg, `.github/workflows/test.yml:105-108`, which runs `pytest tests/` |
| The full suite, the repository-wide lint and the format check at the head. `gaps.md` *Not verified* labels them `unverified` and names their answerer, and that label is still honest: neither the fix pass nor this round ran them (contract rule 2). | `gaps.md` *Not verified*, first row | the orchestrator, by `seal gate` |
| S9: whether the design's `## Rule changes` parse with no refusal at the head. This round's `chain_check.py --worktree` reading covers the records arm alone. | `frame/design.md` `## Rule changes` | the sealer, at its guarantee |

## Probes

| Command | Result |
|---|---|
| `python3 .github/scripts/finding_counts.py --root <scratch>/fixture --released-at HEAD`, over a fixture whose one released work item has no `routing.md` | exit 0; the header, the separator, a blank line, and one line ending `No such file or directory`; no scratch path in the output |
| The same, with two more released items, one whose `routing.md` has mode 000 and one whose `routing.md` is a directory | exit 0; three lines ending `No such file or directory`, `Permission denied` and `Is a directory`; no scratch path; mode restored, fixture removed |
| `why_not` edited to return `str(problem)`, then `bin/test tests/github/test_finding_counts.py -q -p no:xdist -k "cannot_be_opened or declaration_that_cannot"` | 2 failed (the directory parameter and the declaration case), 1 passed (the not-UTF-8 parameter); reverted |
| `and problem.strerror` removed from `why_not`, then `bin/test tests/github/test_finding_counts.py -q -p no:xdist`, and `why_not(OSError())` and `why_not(OSError('x'))` called | 16 passed; both calls returned `None`; reverted |
| `python3 .github/scripts/finding_counts.py --released-at 813665f0` in the clone, and `cmp` against `trail/phases/phase-1.md:43-52` | exit 0; `cmp` exit 0 |
| `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` in the clone | 182 passed, exit 0 |
| `bin/seal layout --pairs` and `bin/seal layout --check` over `tests/github/test_finding_counts.py` | exit 0 each; no pair; five functions reported with no test class, `why_not` among them |
| `uvx ruff check` and `uvx ruff format --check` over the three changed Python files | exit 0 each |
