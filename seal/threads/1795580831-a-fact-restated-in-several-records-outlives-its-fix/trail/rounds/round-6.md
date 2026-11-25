# Review round 6: 1795580831-a-fact-restated-in-several-records-outlives-its-fix

```seal
target: cc88ba151, fixes 15fd04b81..cc88ba151
```

This is the verifying round over round 5's fix pass. The fix diff is `15fd04b81..cc88ba151`, read in a `git clone --no-local` checked out at `cc88ba151` under this round's scratch directory. It holds four commits. `a578c2c7d` is round 5's record. `1dd2f85f2` is the orchestrator's fold, which rewrote Q2's *Options & what each implies* cell at `frame/questions.md:15` and the last sentence of the older *Judgments of the run* row at `frame/plan.md:68`. `10635995c` is the fix pass's docstring change at `hooks/edit-leaves-copies.py:61-70`. `cc88ba151` holds round 5's close blocks. The one code change is the docstring, and the fix diff adds no unit and no test.

Read whole at the target: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md`, `pr.md` and `trail/rounds/round-5.md`. Also read: the hook's module docstring and constants at `hooks/edit-leaves-copies.py:1-90`, `lib/optin.py:226-265`, `hooks/ask-under-automation.py:50-96` and `:185-200`, and `seal/follow-up.md:40-45`. `trail/phases/phase-1.md` and `phase-2.md` were read for their coordinates, and the fix diff changes neither. No `pr.<lang>.md` stands. `seal/config.json` sets both language keys to English, so none is owed. No `seal/parity.json` is declared, and `seal/config.json` has no `Pact` key.

Carried from rounds 1 to 5 and not re-established: everything the fix diff does not touch. That covers the guard at `hooks/edit-leaves-copies.py:274-278` and `Test__located`, which round 5 confirmed; round 4's Probes H and I; round 2's list of the hook's calls that resolve a path; and the boundary at `SECURITY.md:43-46`. Also carried is round 5's judgment that `frame/plan.md:13` agrees with the follow-up row, since the fix diff changes neither. The caller's scope keeps the hook's link handling closed at the limit `frame/design.md:91` and `frame/plan.md:67` state, by the repository owner's decision of 2026-11-25.

## Findings

None. Each of round 5's three findings is closed by the commit its close block names. Each sentence the fix diff wrote holds against the code and the other records at `cc88ba151`.

## Confirmations

```seal
confirms: round-5#1
```
What holds: the docstring at `hooks/edit-leaves-copies.py:61-64` now says the two marker reads outside the link guard are "bounded at the marker's length and the two characters a line end can take". This matches the read `f.readline(len(MARKER) + 2)` at `lib/optin.py:243`, its docstrings at `:238-239` and `:260-261`, and the frame's "marker's length plus two characters" at `frame/design.md:91`, `:133` and `frame/plan.md:67` (read). `git diff 15fd04b81..cc88ba151 -- hooks` shows only the docstring changed; the rest of the paragraph is rewrapped and has the same words (read). Round 5's listing command, re-run at the target with `trail/` left out, printed the hook's `:62-63`, `lib/optin.py:238` and `:260`, and `frame/design.md:91`, `:133` and `frame/plan.md:67`, as the close says (executed). A wider `git grep -n -E "marker's length|line end can take" -- ':!seal/threads'` printed only the hook and `lib/optin.py` (executed). That is a search on words, so it is a sample.

```seal
confirms: round-5#2
```
What holds: Q2's *Options & what each implies* cell at `frame/questions.md:15` now reads "What each answer sends to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against*, the count and each mechanism's own record together, is #1612's row of `seal/follow-up.md`". It no longer says a lower count leaves the mechanisms as built. It cites the home, as `frame/design.md` G3 has a drifted copy answered. The row at `seal/follow-up.md:45` says what the count and each mechanism's record send to the weighing. It holds the clause "even where the count fell" and the sentence opening "As many or more sends" (read). So the cell describes what the row holds. Round 5's listing command, re-run at the target, printed `seal/follow-up.md:44` (#1613's row, another fact) and `:45` (the home), and no longer prints `frame/questions.md:15` (executed). Q2's *Default until answered* cell is unchanged, and the quote of it at `pr.md:3` stands: `bin/seal pr-body` exited 0 with a `wrote:` line and no note (executed).

```seal
confirms: round-5#3
```
What holds: the older row's last sentence at `frame/plan.md:68` now says that `lib/routing.py#read_declaration` "is decided in the row on the hook's handling of links". That row, `:67`, closes with the owner's decision that `read_declaration` is `lib/`'s and gets no issue in this release, so the plan gives it one home (read). The row places `hooks/ask-under-automation.py#_paragraph` outside the class because "it opens `docs/running/the-run.md` under `CLAUDE_PLUGIN_ROOT`, the plugin's own copy, and no file of the repository being checked". The code matches this. `_paragraph` opens `os.path.join(root, *DOC.split("/"))` with `DOC = "docs/running/the-run.md"` (`hooks/ask-under-automation.py:70`, `:84`). `main` passes `root = os.environ.get("CLAUDE_PLUGIN_ROOT") or OWN_ROOT` (`:191`), where `OWN_ROOT` is two directories above the script, which is the plugin root too (`:58`) (read). `frame/design.md` G18 says the same of that hook. Round 5's listing command, re-run at the target, printed `frame/plan.md:67` and `:68` alone in this work item's records outside `trail/`, and they agree. It also printed other work items' records, which state their own facts (executed). This also answers round 5's third *Not judged* row, the home of `_paragraph`: the fold gives it none because it is outside the class.

One case of that claim was weighed, and it is no finding. In a session that loads the plugin with `--plugin-dir` pointing at a clone of this repository, `CLAUDE_PLUGIN_ROOT` is that clone, so `the-run.md` is a file of the repository the session works in. The hook then reads a file of the plugin it is running from, and a person running that plugin runs its code anyway. So no link in that file crosses a boundary the plugin's own code does not already cross. The row's claim holds for an installed plugin, and this case does not make it wrong.

What matched: the records read whole state nothing that the target contradicts. `changelog.md:3` states the guard as built and names no bound. `gaps.md`'s open rows name the orchestrator's broad gate. `routing.md` and the frame's sections dated to `aa32e8473` state that commit. `pr.md`'s three quotes stand, by the `seal pr-body` run above (executed).

What matched: the hook's module and the hook registry pass their narrow run after the docstring change. `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` passed 48. `uvx ruff check` and `uvx ruff format --check` on `hooks/edit-leaves-copies.py` both exited 0 (executed).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the two modules this round ran, and the repository-wide lint and format: `unverified` | `seal/config.json`, `Broad gate` | the orchestrator's broad run |
| A Windows run of the link cases and `Test__located`, carried from round 5 and not changed by the fix diff | `tests/hooks/test_edit_leaves_copies.py:307-381`, `tests/hooks/test_edit_leaves_copies.py:489-525` | the orchestrator's broad run on the workflow's `windows-latest` rows |

This round leaves no finding open. Next comes the orchestrator's broad run, and then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `git grep -n -o -E ".{0,40}(bounded at\|marker's length).{0,50}" -- hooks lib <item> ':!<item>/trail'` | `hooks/edit-leaves-copies.py:62-63`, `lib/optin.py:238`, `:260`, `frame/design.md:91`, `:133`, `frame/plan.md:67` |
| `git grep -n -o -E ".{0,60}(hold as built\|even where the count fell\|what it named against what was\|As many or more).{0,60}" -- seal/follow-up.md <item> ':!<item>/trail'` | `seal/follow-up.md:44` and `:45` alone |
| `git grep -n -E "read_declaration\|#_paragraph\|issue of its own\|get no issue" -- seal ':!<item>/trail'` | for this item, `frame/plan.md:67` and `:68` alone; other items' records beside them |
| `git grep -n -E "marker's length\|line end can take" -- ':!seal/threads'` | `hooks/edit-leaves-copies.py:63`, `lib/optin.py:238-239`, `:260-261` |
| `bin/test -q tests/hooks/test_edit_leaves_copies.py tests/behaviour/test_chain_hooks_hardening.py` | 48 passed |
| `uvx ruff check hooks/edit-leaves-copies.py`; `uvx ruff format --check hooks/edit-leaves-copies.py` | both exit 0 |
| `bin/seal pr-body seal/threads/1795580831-a-fact-restated-in-several-records-outlives-its-fix --body <scratch>/body.md` | exit 0, `wrote:` line, no note |
