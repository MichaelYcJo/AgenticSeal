# Review round 1: 1793538230-code-text-brought-to-the-tree

```seal
target: 1e457247 against release/v0.27.3
```

No earlier round exists, so this round carries no coordinate from one and re-derives every fact it states. The target is the branch `fix/1235-code-text-brought-to-the-tree` at `1e457247141d09e43d1c9df72eafcfaf77b8dfea`. The base is `release/v0.27.3` as the branch forked from it, at the merge base `5f0cf7a7` (executed: `git merge-base HEAD origin/release/v0.27.3`). `origin/release/v0.27.3` has since moved, and the branch has not merged it, so the diff read is `5f0cf7a7..1e457247`. The round worked in a `git clone --no-local` of the worktree under the session's scratch directory. No `seal/parity.md` is declared, so the record carries no `original:` line. `seal/config.md` has no `Record language` row and no `Pact` row, so the record is in English and no pact anchor is read.

The axes walked are the table's ten and four of this change's own: the stream answer each of the three scripts ends with; whether the loop still runs on every path that starts each script in production, now that it sits in `__main__` and not in `main`; whether each name a changed comment cites stands in its file; and whether each reason the rewritten console docstring gives holds for every place it names.

## Findings

### 1. The console docstring gives the scripts under `skills/*/scripts/` a reason for copying the loop that the tree contradicts

```seal
severity: should
location: `hooks/lib/console.py:46-48`
evidence: read `hooks/lib/console.py:46-59`, `skills/implement/scripts/seal.py:229-242`, `skills/verify/scripts/core_check.py:69-81`, `skills/verify/scripts/unverified_check.py:82-97`, `skills/code-review/scripts/chain_check.py:122`, `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:28`
```

Why it matters: design *Scope* item 4 asks the rewritten paragraph to name each place that copies the loop "with the reason that place keeps a copy". The paragraph is what #1255, which decides which entry points owe the answer and whether they import it, will read to learn why each copy exists. For `skills/*/scripts/` it keeps the old sentence: the scripts "are standalone by design and assume nothing about their import path" (`hooks/lib/console.py:47-48`). The tree says otherwise. `skills/implement/scripts/seal.py:238-242` inserts `hooks/lib/` into `sys.path` and imports `config`, `hooksession`, `optin` and `routing` at its top. Its own refusal at line 231 says that "a copy of one script taken on its own is not a plugin". `skills/verify/scripts/core_check.py:69-81`, `skills/verify/scripts/unverified_check.py:82-97` and `skills/code-review/scripts/chain_check.py:122` each load `hooks/lib/` modules by path, and `unverified_check.py` does so at import (line 97). A search over the 14 scripts the docstring's command lists under `skills/` found 9 that reach `hooks/lib/` this way (executed, `## Probes`). So most of these scripts are not standalone, and `seal.py` could import `console` by the same `sys.path` insert it already makes. A reader who takes the stated reason keeps 14 copies for a premise that is false for most of them. The phase-2 record's decision 2 claims "The scripts under `skills/*/scripts/` are standalone by design, which the old paragraph said". It took the reason from the old text and did not open the scripts. The phrase came in through the frame too: `frame/design.md:28`, *Scope* item 4, gives "(standalone by design)" in parentheses, and no *Grounding* row checks it. Contract rule 20 asks for that premise to be checked before it is rested on. The other two reasons hold, and the confirmations below say so.

The fix replaces lines 46-48, the first two sentences of the paragraph, and keeps the rest:

```text
Some entry points spell the loop inline instead of importing this. The
scripts under `skills/*/scripts/` reach `hooks/lib/` themselves: most load
its modules by path, and `skills/implement/scripts/seal.py` imports them
after checking they are there. None of them says why it copies the loop
rather than loading this module the same way, and which of them owes the
import is #1255's.
```

The changelog fragment's second bullet says the docstring "names each place's reason". After the fix, that is still true of the release scripts and `hooks/dispatch.py`, and the paragraph names the open question for the scripts under `skills/*/scripts/`. The fix pass decides whether the bullet needs to change.

```seal
verdict: fixed 18bbd105
answer: The finding holds: at 1ac8b651, 11 of the 14 scripts under `skills/*/scripts/` that the docstring's command lists reach `hooks/lib/` (`seal.py` by a `sys.path` insert, the others by path, `pr_body.py` and `seal_stamp.py` through `chain_check.py`), and `arm_check.py`, `deferral_check.py` and `session_cost.py` reach none of it (executed: a `grep -c` per file for `sys.path.insert`, `spec_from_file_location` or `_load_hook(`, and a `hooks/lib` path, then each loader's target read). The paste-ready text's first clause says every one of these scripts reaches `hooks/lib/`, which those three do not, so the fix is in my own words: "Most of the scripts under `skills/*/scripts/` already reach `hooks/lib/`", with `seal.py`'s import and the by-path loads, then the same sentence that none states why it copies the loop and that which of them owes the import is #1255's. The paragraph's closing "A copied loop is cheaper than the machinery that would avoid it" stood on the same standalone premise and was removed, keeping "what must not diverge is the ANSWER". "This command lists them" now says it lists every place that spells the loop. The changelog fragment's second bullet no longer says the docstring names each place's reason: it names the reason the release scripts and `hooks/dispatch.py` state, and says the skill scripts state none. The frame's "(standalone by design)" was folded by the orchestrator in 1ac8b651, and this pass did not edit the frame. `git grep -n -i "standalone by design"` outside `seal/threads/` prints nothing at 18bbd105 (executed). The phase-2 record's decision 2 still states the premise as phase 2 took it; it is that phase's record and this pass writes none.
```

## Confirmations

```seal
confirms: none
```
What matched: design *Scope* item 1 and S1. `.github/scripts/release_report.py:316-323`, `.github/scripts/release_seal.py:557-564` and `.github/scripts/rules.py:517-524` each give the three pairs `hooks/lib/console.py:67` (`STREAMS`) holds, in its order, as the first statement of `__main__`. The new case `tests/hooks/test_console.py::Test_module::test_a_release_script_run_on_its_own_gives_the_answer_streams_holds` passed at HEAD. With the three scripts restored to `5f0cf7a7` and the case left in place, all three parameters failed, each with `stdin` at `('cp949', 'strict')` and `stderr` at `('utf-8', 'replace')`, and with exit codes 2, 0 and 2. That matches phase 1's *Seen red* claim (executed, `## Probes`). The case reads `console.STREAMS` at run time and spells no literal triple, as S2 asks (read, `tests/hooks/test_console.py:117-128`). Phase 1's mutation table was read and not re-run.

```seal
confirms: none
```
What matched: S3 and *Operational impact*. In `release_seal.py`, the loop was the first lines of `main` before the `try` at the base. It now runs just before `main` in `__main__` (read, `.github/scripts/release_seal.py:532-565`). So a failure in it ends the process the same way it did, and `main()` called in process by `tests/github/test_release_seal.py` no longer changes the test's streams. Every path that starts the three scripts in production runs `__main__`. `.github/workflows/publish-release.yml:158` runs `python3 .github/scripts/release_seal.py`. `.github/workflows/hygiene.yml:174` runs `rules.py --check`. `.github/workflows/test.yml:291` runs `release_report.py`. `seal rules` hands `rules.py` to `os.execv` (`skills/implement/scripts/seal.py:177-180`, `skills/implement/scripts/seal.py:2801`). So the changelog's claim that `rules.py` is the script `seal rules` runs holds (read). The release run with no `TAG` ends in `no seal:` printed to the stand-in stdout, so the case writes no `::warning::` line to a CI log (read, `.github/scripts/release_seal.py:538-549`).

```seal
confirms: none
```
What matched: the class design *Scope* item 1 names, every entry point whose own loop differs from `STREAMS` in `stderr`. `git grep -n -A1 '"stderr"'` over the files the Scope 4 command lists shows `backslashreplace` for `stderr` in every loop at HEAD (executed). The five loops that leave `stdin` out are the frame's *Out* item for #1255.

```seal
confirms: none
```
What matched: design *Scope* item 2 and S4. The paragraph at `hooks/lib/cmdline.py:25-32` cites `hooks/dispatch.py#run_gate`, and `hooks/dispatch.py:114-154` does what it says. A raised gate is appended to `FAILED`, the call goes ahead as if the gate printed nothing, and the module docstring (`hooks/dispatch.py:25-30`) says that a record is written "once per gate per session" and said by the `stop` group. Phase 2's decision 1, "once per gate per session" in place of the design's "once per session", follows that docstring, and it holds. `run_gate` appends to `FAILED`, and the comment in its handler says that `main()` writes the record. The paragraph's "writes the failure down" folds those two steps into `run_gate`. A reader who opens `run_gate` meets the comment naming `main()`, so the sentence sends no one the wrong way (read). The class: a regex over every `path.ext:N` spelling, wider than the design's four extensions, run over `hooks/`, `skills/`, `.github/scripts/`, `bin/` and `evals/scripts/`, found only the eval fixture `evals/scripts/rule_cases.py:809` and a format string at `skills/verify/scripts/arm_check.py:373` (executed).

```seal
confirms: none
```
What matched: design *Scope* item 3 and S5. With `overwide_rows` gone, the comment at `skills/verify/scripts/unverified_check.py:98-117` cites names that each stand in their files: `fence_spans`, `blank_fences`, `closed_fence_lines`, `liveness`, `_paragraph_ends_at` and `live_lines` in that file; `coordinates.py#quoted_lines`; `payload_meter.py#heading_starts`; `hooks/lib/blocks.py#walk` at line 277; `close_issues_on_release.py#FENCE` at `.github/scripts/close_issues_on_release.py:122`; and `test_docs_line_wrap.py#fenced_numbers`. The two test files it names exist (executed: `grep -cE` per name, `ls`). The grammar around the removed item reads as one list ending "and the oracle walk".

```seal
confirms: none
```
What matched: design *Scope* items 4 and 5 and S6, apart from finding 1. The console paragraph states no count, and its command lists the 19 files phase 2 reports at HEAD (executed). The reasons given for the three release scripts and for `hooks/dispatch.py` hold. `release_report.py#meter` and `rules.py#sibling` raise `Unreadable`, which `main` turns into exit 2 (`.github/scripts/release_report.py:78-88`, `.github/scripts/release_report.py:301-303`, `.github/scripts/rules.py:130-137`, `.github/scripts/rules.py:506-508`). `hooks/dispatch.py:265` and `hooks/dispatch.py:283` say that a report must not depend on the module whose failure it reports (read). The `test_console.py` case docstring at lines 72-80 says "The gates' own `console.to_utf8()` calls" and "every one of them", with no figure (read). Phase 2's departure, "four lines duplicated" made "A copied loop", holds by its own count (read, not re-counted).

```seal
confirms: none
```
What matched: the new case read against its group. `Test_module` held one case before this one, which runs a gate, and no case in `tests/` runs any of the three scripts' `__main__` or reads their streams (executed: `git grep -l "reconfigure\|backslashreplace\|STREAMS" -- tests`). `bin/seal layout --check tests/hooks/test_console.py` exited 0. `bin/seal layout --pairs` names no pair holding the new case (executed). The case loads `publish_release_note.py` through `release_seal.py#publisher`, which changes `sys.path` in the test process. `tests/github/test_release_seal.py:245` already loads the same module in process, so the case adds no new kind of leak (read).

```seal
confirms: none
```
What matched: the changelog fragment. The spawn prompt relays phase 2's disclosure that it appended to `changelog.md` with a shell heredoc, against contract rule 9. The fragment at HEAD is one `### Fixed` heading and two bullets, in the shape the other fragments under `seal/threads/` use. Each claim in it was checked against the code. None of the three scripts reads `stdin` outside the loop (executed: `grep -n stdin`, three lines, each a loop pair). The breach left no defect in the tree, so it is no finding. That an edit went around the edit tools is the orchestrator's to weigh.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the new case passes on the Windows legs of `.github/workflows/test.yml` (`frame/questions.md` Q1). This round ran it on darwin alone | `tests/hooks/test_console.py:102-128` | the pull request's Windows legs, read by the orchestrator |
| The full suite, the repository-wide lint and the format check at HEAD. `gaps.md` labels them unverified and names the orchestrator, and that label is honest: nothing in the phase records claims them | the whole tree | the orchestrator, by `seal gate` after the rounds settle |
| Which 9 cases phase 2's boundary run skipped, and why | `trail/phases/phase-2.md` | the orchestrator's broad run |
| Phase 1's mutation table: 9 mutants and one `STREAMS` mutant reported red. Read, not re-run | `trail/phases/phase-1.md` | the sealer, at its sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/hooks/test_console.py tests/github/test_release_seal.py tests/github/test_rules.py tests/github/test_release_report.py -q -p no:xdist`, at 1e457247 in the clone | 144 passed, exit 0 |
| `git checkout 5f0cf7a7 -- .github/scripts/release_report.py .github/scripts/release_seal.py .github/scripts/rules.py && bin/test tests/hooks/test_console.py -q -p no:xdist -k release_script`, then `git checkout HEAD -- .github/scripts` | 3 failed, exit 1; each diff shows `stdin` `('cp949', 'strict')` and `stderr` `('utf-8', 'replace')`; `git status --short` empty after the restore |
| `git grep -l "[.]reconfigure(" -- '*.py' ':!tests' ':!evals/behaviour'`, then for each file under `skills/` a count of `sys.path.insert` and of `spec_from_file_location` or `_load_hook(`, and a `grep` for a `hooks/lib` path join | 19 files; under `skills/`, `seal.py` with one path insert, 8 others loading `hooks/lib/` modules by path, and `arm_check.py`, `deferral_check.py` and `session_cost.py` with neither |
| `git grep -nE '[A-Za-z_/.-]+\.[A-Za-z]+:[0-9]+' -- hooks skills .github/scripts bin evals/scripts` | 2 lines: `evals/scripts/rule_cases.py:809` and `skills/verify/scripts/arm_check.py:373` |
| `bin/seal layout --check tests/hooks/test_console.py`; `bin/seal layout --pairs` | exit 0, 0 refused; exit 0, no pair names the new case |
