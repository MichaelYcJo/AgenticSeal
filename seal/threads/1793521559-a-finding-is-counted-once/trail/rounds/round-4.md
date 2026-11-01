# Review round 4: 1793521559-a-finding-is-counted-once

```seal
target: a7b91f6a, fixes a0b0a4c8..a7b91f6a
```

This is the verifying round for round 3's fix pass. The target is the diff `a0b0a4c8..a7b91f6a` on `fix/1223-a-finding-is-counted-once`, at `a7b91f6a65c41151dfe7d5bd591b1c9774b5769b`. It holds three commits and three files (executed: `git diff --stat a0b0a4c8..a7b91f6a`). `259f8695` answers round 3's finding 1 with a new class, `Test_why_not`, of two cases in `tests/github/test_finding_counts.py:367-382`. `a7b91f6a` appends the fix pass's close block to `round-3.md` and removes no line of it (executed: the diff of that file holds five `+` lines and no `-` line). `0bed123d` is the orchestrator's row in `frame/plan.md` *Judgments of the run* that sends the run past round 3. No `seal/parity.md` is declared, so the record carries no `original:` line. Everything ran in a `git clone --no-local` of the branch worktree at the target, under the round's scratch directory.

Carried from round 3 as coordinates, and opened again rather than searched for: `why_not` at `.github/scripts/finding_counts.py:108-116` and its two callers at lines 127 and 153; the two `Test_main` cases that reach its `strerror` arm, `test_a_record_that_cannot_be_opened_is_named_with_why` (lines 200-231) and `test_a_declaration_that_cannot_be_read_is_named_under_the_table` (lines 281-320); and round 3's two mutants, written again from its `## Probes` rows. Every verdict below is this round's own.

The crafter's account was read as a claim. It says two mutants turned the class red, `seal layout --check` exits 0 and reports the four functions `gaps.md:12` names, and 3776 cases passed over 55 modules. This round ran both mutants and the layout check itself. The 3776 count was not re-run (`## Not judged`).

The new units are test code alone, so the axes walked are the ones that apply to a case. Inputs: which errors the cases build, and whether each arm of `why_not` gets one. Boundaries: an `OSError` whose `strerror` is empty. Error paths and Security: whether any built error lets an absolute path through. Test quality: whether each case was seen red, whether it holds on every platform CI runs, and whether it covers something its group does not. Two axes of this change's own were also walked. The first is whether the case names follow `CONTRIBUTING.md` *The test layout*. The second is whether every other statement of a fact the fix changed was changed along (contract rule 19). Authorization, Query scope, Ordering, State transitions and Concurrency have nothing to act on in two cases that call a pure function.

## Findings

None. The close of round 3's finding 1 holds, and the new class opens nothing that needs a fix.

## Confirmations

```seal
confirms: round-3#1
```
What holds: both arms of `why_not` are now pinned by a case of its own class, and `gaps.md` *Not done* is true as written. The crafter claimed two mutants turned the class red. In the clone, an `Edit` deleted `and problem.strerror` from line 114. `test_refuses_to_say_none_for_an_os_error_with_no_strerror` then failed, and the other 17 cases of the module passed (executed, `## Probes`). That is the arm round 3 found reached by no case: under the same mutant, round 3's run passed all 16 cases. A second `Edit` made the first arm return `str(problem)`. Three cases then failed: `test_accepts_an_os_error_and_says_its_strerror_without_its_path`, and the two `Test_main` cases round 3 named (executed, `## Probes`). Both edits were reverted, and `git diff --quiet` exited 0 after (executed). The refuses case's docstring says it was seen red with `and problem.strerror` removed, which matches the first mutant. So contract rule 15 holds for both cases.

The crafter claimed `seal layout --check` reports `chained`, `item_counts`, `load` and `readers` with no class. At the target it reports exactly those four, exits 0 and refuses nothing (executed). They are the four `gaps.md:12` names, so that paragraph's list is complete, and its reason, a class per function would restate `Test_main`'s cases, is now claimed for those four alone (read). The class is listed by a command that names each function holding the property, so the list is whole and not a sample (contract rule 12).

The close says the paste-ready class was narrowed because its UnicodeDecodeError parameter and its ENOENT case opened through `open` restated `Test_main`'s cases. That holds. The not-UTF-8 parameter at line 200 pins a `UnicodeDecodeError`'s whole text through `why_not`'s fallback. The declaration case at line 313 pins `os.strerror(errno.ENOENT)` for a missing `routing.md` (read). The fix pass took the first of round 3's two options. Of the two cases round 3 offered for the fallback arm, it kept `OSError("no errno")` and added `OSError()`, which no earlier case built (read).

```seal
confirms: none
```
What matched: the new class reads against its group. `bin/seal layout --pairs tests/github/test_finding_counts.py` names no pair (executed). The refuses case covers an arm no other case reaches, which the first mutant shows. The accepts case reaches the `strerror` arm that two `Test_main` cases already pin, and the second mutant turns all three red. It still stands on two grounds. `CONTRIBUTING.md` *The test layout*, lines 244-245, asks each `Test_<name>` class for a `test_accepts_<what>` case as well as a `test_refuses_<what>` case. And its first assertion, at line 373, checks that the error's own text carries the absolute filename. No `Test_main` case checks that. Without it, their assertion that the root's path is absent from the output could pass because the platform's text held no path at all (read). The cases are named `test_accepts_` and `test_refuses_` as the layout asks, and the class is spelt `Test_why_not` as the code spells the function (read; `seal layout --check` refuses neither).

Both cases build their errors directly and open no file. `OSError(errno.ENOENT, os.strerror(errno.ENOENT), path)` puts the filename in the text on every platform. `os.strerror` gives the expected words the same way the code gets them. So, unlike round 3's directory parameter, neither case depends on the system (read). `OSError()` has `strerror` `None` and the text `''`, and `OSError("no errno")` has `strerror` `None` (executed, `## Probes`), so the refuses case's two assertions are what the fallback returns.

The boundary was weighed: an `OSError` built with an errno and an empty `strerror` would take the fallback and print its whole text, filename included. No platform's `open` raises one, since every errno has words, and `main` builds none. So the state is not reached and is no finding. The refuses case pins `OSError()` as the empty text, which would leave a line under the table with no reason after its colon. That state, too, is one `main` never reaches. The docstring at lines 112-113 says such an error is "said whole", and the case pins exactly that (read).

```seal
confirms: none
```
What matched: no other statement of the facts the fix changed is left standing. The fix changed two facts: `why_not` has no class, and no case reaches its no-`strerror` arm. A search for `why_not` and for "no `strerror`" outside the round records finds the function, its docstring, its two callers, the new class and the new `frame/plan.md` row (executed: `git grep -n "no .strerror\|why_not" -- ':!seal/threads/*/trail/rounds'`). None states either old fact as current. The plan row describes the defect in the past, as the finding it routes. `frame/design.md` *Data & interfaces*'s Stdout bullet and the changelog fragment describe what the script prints. The fix changed no line of that, so both stay true (read). The round records state the old facts as history and are not rewritten (contract rule 19 asks that of text that amends, and a record is the history `skills/core/SKILL.md` sends to the work record). `uvx ruff check` and `uvx ruff format --check` on the changed test file exit 0 (executed). The plan's two modules pass at the target: `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` gave 184 passed (executed). That is round 3's 182 plus the two new cases. These narrow runs are probes and never the broad gate.

```seal
confirms: none
```
What matched: the orchestrator's row in `frame/plan.md:49`. `docs/the-review-record.md` *The run* asks that a decision past or at the third round be a row naming the counts weighed. The row names them, 2, 2 and 1, all `should`, and they match the finding headings of `round-1.md`, `round-2.md` and `round-3.md` (executed: `grep -n "^### \|^severity:"` over the three). The same section says a second regression on one unit after a fix-pass route goes to the framer unless the row's grounds say why the frame holds and the fix alone was wrong. The row writes that sentence. The frame says nothing of `why_not`, which round 2's fix added. The defect was a case left out, which a case answers. That matches `frame/design.md`, whose scope and *Data & interfaces* name no test class, and the fix pass closed it with a case alone (read). The route is the orchestrator's judgment, and this round does not remake it. The row's *Judged against* cell names `skills/code-review/orchestration.md`'s two sections and not `docs/the-review-record.md` *The run*, which that section names as the section to cite. Both state the rule the row applies, so a settle reading the row reaches its source either way. The round-2 row of the same table cites the same way, and round 3 confirmed it. This round raises no finding on the citation.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass's claim that 3776 cases passed over 55 modules. This round re-ran the plan's two modules alone. | the crafter's hand-back, which the spawn prompt carries | the orchestrator, by `seal gate` after the rounds settle |
| The full suite, the repository-wide lint and the format check at the head. `gaps.md` *Not verified* labels them `unverified` and names their answerer. That label is still honest, because neither the fix pass nor this round ran them (contract rule 2). | `gaps.md` *Not verified*, first row | the orchestrator, by `seal gate` |
| S9: whether the design's `## Rule changes` parse with no refusal at the head. This round's `chain_check.py --worktree` reading covers the records arm alone. | `frame/design.md` `## Rule changes` | the sealer, at its guarantee |
| Carried from round 3, outside this diff: whether the directory parameter of `test_a_record_that_cannot_be_opened_is_named_with_why` passes on Windows. This round ran on macOS. | `tests/github/test_finding_counts.py:200-231` | CI's Windows leg, `.github/workflows/test.yml:105-108` |

This round leaves nothing open. What comes due is the orchestrator's broad run, `seal gate`, and the sealer's spawn after it.

## Probes

| Command | Result |
|---|---|
| `bin/seal layout --check` and `bin/seal layout --pairs` over `tests/github/test_finding_counts.py`, in the clone at the target | exit 0 each; four functions reported with no class, `chained`, `item_counts`, `load` and `readers`; no pair |
| `bin/test tests/github/test_finding_counts.py -q -p no:xdist` | 18 passed |
| `and problem.strerror` deleted from `finding_counts.py:114` by `Edit`, then the same `bin/test` command | 1 failed, `Test_why_not::test_refuses_to_say_none_for_an_os_error_with_no_strerror`; 17 passed |
| The first arm of `why_not` made to return `str(problem)` by `Edit`, then the same `bin/test` command | 3 failed: `Test_why_not`'s accepts case, the `a directory` parameter of `test_a_record_that_cannot_be_opened_is_named_with_why`, and `test_a_declaration_that_cannot_be_read_is_named_under_the_table`; 15 passed; reverted, `git diff --quiet` exit 0 |
| `python3 -c` printing `OSError().strerror`, `str(OSError())` and `OSError('no errno').strerror` | `None`, `''`, `None` |
| `bin/test tests/github/test_finding_counts.py tests/skills/test_chain_check.py -q -p no:xdist` | 184 passed |
| `uvx ruff check` and `uvx ruff format --check` over `tests/github/test_finding_counts.py` | exit 0 each |
