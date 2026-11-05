# Review round 1: 1793853198-tests-name-the-gate-that-exists

```seal
target: 19b4cf84 against release/v0.32.4
```

The range is `c54f0040..19b4cf84` over `31558c76`: the routing, the frame, the build `b965a9a8`, the one comment outside D1 in `cebd347f`, the records `ed5a18bf` and `3425ea7e`, and the orchestrator's fold `19b4cf84`. This is round 1, so no earlier round carries a coordinate or a fact into it; every fact below was opened this round. No `seal/parity.md` is declared, and `seal/config.md` holds no `Pact` row and no `Record language` row.

The frame says the class is a sample over spellings, and it leaves to this round the part no method reached: a line in the diff's files that describes the commit gate as present in none of M3's nine words. This round read the eight touched modules for that part. It searched them for `waiver`, `no-review`, `marker`, `per-command`, `silenc`, `asks`, `asking`, `the gate`, `a gate` and `commit`, and it searched `tests/` as a whole for the commit gate's waiver words. Each hit was read. Finding 1 is what that read found. This list is a sample too, because the class is open over spellings. The part it did not reach is a sentence in the diff's files, or anywhere else under `tests/`, that describes the gate in words neither list holds. Nothing in this round reaches that part.

## Findings

### 1. A comment still says the commit gate's per-command waiver stands in `skills/implement/SKILL.md`

```seal
severity: should
location: `tests/behaviour/test_waiver_decided_at_start.py:41-46`
evidence: executed `git grep -n -i -E "no-review|no-parity|per-command|review mark|has_marker|waives? (one|a) (command|commit)" -- tests`; `grep -n -i "waive\|no-review\|per-command" skills/implement/SKILL.md skills/implement/orchestration.md`; `git show 61a8455a^:skills/implement/SKILL.md`; read `tests/behaviour/test_waiver_decided_at_start.py:41-46`, `tests/behaviour/test_waiver_decided_at_start.py:749-756`
```

Why it matters: at HEAD, the comment above `ORCH` in `tests/behaviour/test_waiver_decided_at_start.py:44-46` says "The per-command waiver stays in `SKILL.md`, because the implementer is who types the command." That waiver was `[no-review]`, the per-command way past the commit gate. Before #1027, `skills/implement/SKILL.md:196-197` said "`[no-review]` still works and is unchanged: it waives **one command**" (`git show 61a8455a^:skills/implement/SKILL.md`). At HEAD, neither `skills/implement/SKILL.md` nor `skills/implement/orchestration.md` holds a per-command waiver. The grep over both prints only `orchestration.md:410` and `:412`, which say the declaration "waives nothing" and cite *There is no standing waiver*. The same module asserts the absence itself: `test_the_skill_names_the_record_and_no_per_command_waiver` at `:749-756` requires that `[no-review]` and "waives **one command**" are in neither file. So the comment describes a part of the removed gate as standing, which is the class #1352's *Done when* asks to be gone. The comment is in a file this diff touched, at rows 13 and 14. M3's nine words do not include `waiver`, so the frame's sample did not reach it. `frame/design.md` *The class* hands that part to this round. The search over `tests/` for the waiver's words finds no other present-tense instance. `tests/text/test_review_axes.py:143` says the waiver went with #1027.

This is disposition D: the clause names something the tree no longer holds, and nothing does its job. The rest of the comment stays, because it is true of the orchestrator's half.

```python
# The routing section — the axes, the checkbox, the file, the four
# combinations, the wake/quiet table — is `implement`'s orchestrator half
# since #292: the session that asks reads `orchestration.md`, and no crafter
# spawn preloads it.
ORCH = ("skills", "implement", "orchestration.md")
```

The snippet covers the one sentence in the code. The fix pass also owes the records that count the class. `trail/phases/phase-1.md` lists 19 rows and needs a row for this line. `changelog.md` says "nineteen places under `tests/`" and needs the new count. The frame's D1 table and *Scope* item 1 are the orchestrator's fold.

### 2. The plan and the phase record count nine touched files where the diff touches eight

```seal
severity: should
location: `seal/threads/1793853198-tests-name-the-gate-that-exists/frame/plan.md:5`, `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:59`
evidence: executed `git diff --name-only 31558c76 19b4cf84 -- tests` (8 paths); read `seal/threads/1793853198-tests-name-the-gate-that-exists/frame/plan.md:5-14`, `seal/threads/1793853198-tests-name-the-gate-that-exists/trail/phases/phase-1.md:59`
```

Why it matters: `frame/plan.md:5` says "The work edits text in nine files under `tests/`", and the eight bullets right below it list eight files. `trail/phases/phase-1.md:59` says ruff ran "over the nine touched files". The diff under `tests/` touches eight paths, and the same paragraph of the phase record says "the eight touched modules". The pull request body copies the records. The sealer reads every account against the tree and re-runs a sample of the crafter's claims, so a sealer that re-runs the ruff claim looks for a ninth file that the diff does not hold. The ruff result holds for the eight files: `uvx ruff check` and `uvx ruff format --check` over them both exit 0 (executed, this round). Finding 1's fix edits a file that is already touched, so the count stays eight.

```text
frame/plan.md:5            The work edits text in eight files under `tests/` and removes one unit of code.
trail/phases/phase-1.md:59 ... `uvx ruff check` and `uvx ruff format --check` over the eight touched files exit 0 (executed).
```

## Confirmations

What matched: each of D1's 19 rows is at HEAD as `trail/phases/phase-1.md` *Each of the 19 rows* records it (read: `git diff 31558c76 19b4cf84 -- tests`, every hunk against its row). The diff under `tests/` changes only docstrings and comments, the one f-string message at `tests/hooks/test_routing.py:63`, and the removal of `tests/conftest.py#fired`. So S4 holds by reading the diff, and this round re-ran no `ast` probe. Row 16's coordinate, which the fold corrected to `tests/censuses.py:892`, is the line the base hunk opens at `@@ -889` (read).

What matched: gaps.md's third *Not verified* row says that rows 5, 8, 9, 10, 11, 13 and 14 state what the edit check does with a declaration it cannot read, and that no case runs that path. The claim holds. In `hooks/routing-edit-gate.py:243-269`, `decide` lets the edit through at `:257` when `routing.for_branch` returns a declaration. Otherwise the edit is refused, with four exceptions: a file under the `seal/` root, a git-ignored file, a detached HEAD at a commit a declared branch holds, and a branch with a `seal no-work-item` record. The module docstring at `:30-32` says the same. `routing.for_branch` at `hooks/lib/routing.py:388-399` returns None for no match and for two matches (read). "Refuses the next edit" is true for any edit outside those four exceptions.

What matched: phase 1 claimed a departure at row 7, that D1's wording would name a refusal the predicate never meets. In `tests/hooks/test_routing.py:55`, `assert parsed is not None, path` runs before the message at `:61-64`, so the file is a declaration whenever the message prints. The new message, "or every declaration like it carries an answer its author never gave", says what a wrong read of an absent optional row gives (read). The fold's change to D1 row 7 matches the phase record.

What matched: phase 1 claimed a second departure, the `CRAFTER` comment in `cebd347f`. At HEAD, `tests/text/test_a_moved_rule_leaves_its_definition.py:260-262` tells the waiver example in the past tense. The module docstring at `:21-27` no longer names that example, and `grep -n "pathspec\|1\.08\|1\.17\|waiv" agents/crafter.md` prints only `:192`, "waiving the reading below", which is no waiver example (executed). The comment at `:324-326` and the comment at `:380-382` tell the waiver's removal in the past tense (read).

What matched: the crafter claimed that S1 prints 9 lines, that S2 prints 8 lines, and that S3 prints nothing under `-P`. All three hold at `19b4cf84`, and this round re-ran each (executed). S1's nine lines are the ones *Left as they stand* names, with `tests/hooks/test_routing.py:535` as the past narration D1 places at `:533`. S2's eight lines say the git hooks are gone or are a case's input. `git grep -n -P "\bfired\(" -- . ':!seal/threads'` exits 1. `git grep -n -w fired -- . ':!seal/threads'` prints no call to `conftest.fired`, only prose and the attribute `self.fired` in `tests/skills/test_session_cost.py:926` (executed).

What matched: row 17's example holds. `ruff.toml:45` reads `"hooks/*.py" = "py39"  # its `*` crosses a `/`, so hooks/lib/ too`, and `hooks/lib/routing.py` exists (read). `tests/test_censuses.py:788` keeps its input, as plan A8 says.

What matched: the crafter claimed S5, 763 passed and 2 skipped over its scoped set. This round ran a narrower set through the repository's runner: `bin/test -q` over the seven touched test modules with `tests/test_censuses.py` and `tests/test_conftest.py`. It gave 549 passed, exit 0 (executed). The crafter's wider set was not re-run. `gaps.md` labels the full suite `unverified` and names the orchestrator's broad run as its answerer, which matches agent-contract rule 2.

What matched: the fold `19b4cf84` answers Q2 with the phase's wording, and each sentence stands beside its row in `trail/phases/phase-1.md` (read). Q1 was built on its default (b), and `hooks/lib/routing.py` is untouched by the diff (read: the diff's file list).

The diff adds no test, so there is no new case to read against its group.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD | `seal/config.md` `Broad gate` row | the orchestrator's broad run, then the sealer's spawn after it |
| Whether `hooks/lib/routing.py`'s module docstring, which still speaks of "the gate" in the present, joins this work item (`frame/questions.md` Q1, built on default (b)) | `hooks/lib/routing.py:1-31` | a person, through the orchestrator's release report |

## Probes

| Command | Result |
|---|---|
| `git grep -n -i "commit gate" -- tests` | 9 lines, exit 0, each in *Left as they stand* |
| `git grep -n -i -E "git hook\|hooks/git/" -- tests` | 8 lines, exit 0, as phase 1 lists them |
| `git grep -n -P "\bfired\(" -- . ':!seal/threads'` | no output, exit 1 |
| `git grep -n -w fired -- . ':!seal/threads'` | no call to `conftest.fired`; prose and `self.fired` in `tests/skills/test_session_cost.py` |
| `git grep -n -i -E "no-review\|no-parity\|per-command\|review mark\|has_marker\|waives? (one\|a) (command\|commit)" -- tests` | 5 lines; `tests/behaviour/test_waiver_decided_at_start.py:45` is the one present-tense statement (finding 1) |
| `grep -n -i "waive\|no-review\|per-command" skills/implement/SKILL.md skills/implement/orchestration.md` | `orchestration.md:410` and `:412` only |
| `uvx ruff check` and `uvx ruff format --check` over the eight touched `tests/` files | both exit 0 |
| `bin/test -q` over the seven touched test modules, `tests/test_censuses.py` and `tests/test_conftest.py` | 549 passed, exit 0 |
