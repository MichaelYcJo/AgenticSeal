# Implementation Plan: 1793538230-code-text-brought-to-the-tree

## Technical context

The code this builds on, each item opened at `1cdde66f`:

- `hooks/lib/console.py#STREAMS` and `#to_utf8`. Six scripts under `.github/scripts/` import the module after a `sys.path.insert` of `hooks/lib`, and call `console.to_utf8()`. `.github/scripts/tag_release.py` and `finding_counts.py` are two of them.
- `.github/scripts/release_report.py`, `release_seal.py` and `rules.py` spell a two-stream loop with `errors="replace"`. In `release_report.py` and `rules.py` the loop opens the `__main__` block. In `release_seal.py` it opens `#main`. None of the three imports a module of the tree at its top. `release_seal.py#module`, `rules.py#sibling` and `release_report.py#meter` load such modules by path when first asked, so a module that will not load ends in the script's own named result (design *Grounding*).
- `tests/hooks/test_console.py` holds `Test_to_utf8`, which drives `to_utf8` against cp949 stand-ins, and a `Test_module` case. `tests/github/test_release_seal.py` calls `main()` in process with `capsys`.
- `hooks/dispatch.py#run_gate` and the module docstring's #28 paragraph. `skills/verify/scripts/unverified_check.py`, the comment above `fence_opener`.

The failure scenario of the chosen approach, in six months: `STREAMS` changes, for example to a new handler for `stdout`, and the three inline loops still spell the old pairs. The Scope 1 case reads `STREAMS` at run time, so it goes red in the commit that changes `STREAMS` and names each script. What it does not reach are the 14 inline loops under `skills/*/scripts/` and the one in `hooks/dispatch.py`. Those stay with `tests/hooks/test_dispatch.py` and with #1255's census.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Replace each script's inline loop with `import console` at the top and `console.to_utf8()` as the first statement of `__main__`, as the six siblings under `.github/scripts/` do | A `hooks/lib/console.py` that will not load ends each script before `main` runs: a `ModuleNotFoundError` traceback at exit 1. That breaks `release_seal.py`'s stated rule that every failure ends in today's note and an exit of 0, and it breaks the named `Unreadable` exit 2 the other two give a missing module. The premise that keeps the inline loop is that sentence, checked: read in the comment above `.github/scripts/release_seal.py#module`, and in `rules.py#sibling` and `release_report.py#meter`, which raise `Unreadable` naming the missing file | rejected |
| 2. Load `console` through each script's own lazy loader (`module(...)`, `sibling(...)`, a loader like `meter`) as the first statement of `__main__` | The load runs before `main`'s guard, so each script needs a handler for its first line. If that handler skips the call when the load fails, the streams are left unfixed with no trace, which is the silent degradation `hooks/lib/console.py` exists to end. Three new failure paths would replace one four-line answer | rejected |
| 3. Keep each inline loop, give it `STREAMS`' three pairs, and put it first in `__main__`. One case holds the three scripts to `STREAMS` read at run time | A later `STREAMS` change leaves the loops behind until the case goes red, in the same commit. The copies stay, and the case is what keeps them from drifting silently | chosen |
| 4. Change `stderr` alone, leaving each loop's two streams | The three join the five entry points that leave `stdin` out, which #1255's census would refuse as not `STREAMS`' answer. The case could not compare the loop with `STREAMS` whole. Adding `stdin` costs nothing, since none of the three reads it (executed: `grep -n stdin`, 0 lines) | rejected |
| 5. One case per script, in each script's own test module's `Test_module`, sharing a helper | `seal layout --check` refuses a helper defined byte-identically in two test files, so the helper would go to `tests/conftest.py` for one use. When #1255 builds the census, three cases would be weighed instead of one. The fact pinned is `STREAMS`', and `tests/hooks/test_console.py` is that module's file | rejected |
| 6. A static case reading each script's `__main__` with `ast`, as `tests/censuses.py#opens_with_to_utf8` reads the hooks | It pins the loop's spelling and not the answer the streams end with. Reading an inline loop's pairs by `ast` is the census #1255 builds | rejected |
| 7. `hooks/lib/console.py`'s docstring keeps a count and adds the commit it was taken at | The count is true only at its commit, so a reader has to recount anyway. `skills/core/SKILL.md` *The rule a mechanism is kept against* rules out a stored count kept beside the tree. The issue allows either form, and the core decides between them | rejected |
| 8. `unverified_check.py`'s comment names a successor to `overwide_rows` | No successor stands. `skills/evidence-check/scripts/evidence_check.py#overflow_rows` left with #944 and #950, and nothing at `1cdde66f` reads a ledger row's width (design Scope 3) | rejected: the item leaves the list |
| 9. Rewrite also the past-tense sentences in `hooks/lib/routing.py#declarations` and `tests/hooks/test_routing.py` that name `except Exception: return ""` | Each states the handler as it stood when the defect it records happened, before #28 (design *Scope*, Out). Rewriting them would make history read as if the handler had always been `run_gate`'s current form | rejected |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | Design *Scope* 1 | The Scope 1 case, seen red against the base before the fix (rule 15) and green after. Run narrowly in one command at the phase boundary: `tests/hooks/test_console.py`, `tests/github/test_release_report.py`, `tests/github/test_release_seal.py`, `tests/github/test_rules.py`, and every other test module that reads a changed path | |
| 2 | Design *Scope* 2, 3, 4 and 5 | Each item's method, run at the phase's commit as design *User scenarios & acceptance* S4 to S6 state it. Run narrowly: the test modules that read `hooks/lib/cmdline.py`, `hooks/lib/console.py`, `skills/verify/scripts/unverified_check.py` or `tests/hooks/test_console.py`. `uvx ruff format --check` on the changed files | |

Phase 2 follows phase 1 because Scope 4's docstring names the places phase 1 leaves.

## Operational impact

None. No migration, environment variable, dependency or compatibility break. The publish-release workflow runs `release_seal.py` as before, and its `continue-on-error` and exit-0 contract are unchanged.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
