# Review round 1: 1793833680-a-transcript-not-yet-written-is-named

```seal
target: e9dd4df9 against release/v0.32.2
```

The round read `release/v0.32.2..e9dd4df9`: the routing and frame commits, the fix 57265336, the phase commits 8d3523e3 and 65a69426, the reflow 5dee05dc and the orchestrator's fold e9dd4df9. No earlier round exists, so no fact was carried and every coordinate below was opened this round. The probes ran in a `git clone --no-local` of the branch checked out at e9dd4df9, under the round's scratch directory, and the clone is removed before the hand-back.

Axes walked: inputs (the session id, `CLAUDE_CONFIG_DIR`, `--transcript`), error paths, the output shape (one line, exit 1), boundaries (no file against a wrong id or directory), and test quality against contract rules 14 and 15. The change adds no failure path: `find` returns the same `(None, reason)` on the same condition, and `main` prints it and returns 1 as before (`skills/verify/scripts/core_check.py:271-274`, read). Concurrency, authorization and security have nothing to judge here, since the diff changes one string literal and no path, file mode or process boundary. One case outside the frame was weighed and is no finding. A session that never writes a transcript, such as a headless run that does not persist its session, gets the added sentence, and sending a message would not help it. The first sentence still names the session and the directory searched, which is the cost `frame/plan.md` *Technical context* accepts for a wrong `CLAUDE_CONFIG_DIR`.

## Findings

### 1. The phase record's mutation run names two `--replace` pairs that `seal mutate` refuses before it writes anything

```seal
severity: should
location: `seal/threads/1793833680-a-transcript-not-yet-written-is-named/trail/phases/phase-1.md:13`
evidence: executed `bin/seal mutate skills/verify/scripts/core_check.py --replace "once a message has been sent in it" "at some point" --replace "send one message and run it again." "wait." --tests "bin/test tests/skills/test_core_check.py -q -p no:xdist -k test_refuses_with_a_reason_where_no_transcript_can_be_named"` (exit 2), the second pair alone (exit 2), `git show 57265336:skills/verify/scripts/core_check.py | grep -n -F` on each OLD; read `skills/verify/scripts/mutation_check.py:188-207`
```

Why it matters: claimed, at `trail/phases/phase-1.md:13`, that the batch with these two pairs ran, that the baseline passed, both mutants were red and the run exited 0 with 0 survived. Run as written, at e9dd4df9 and at 57265336 alike, the batch exits 2 with `refused: pair 1: OLD occurs 2 times in skills/verify/scripts/core_check.py; it must occur exactly once. Nothing was written.` The first OLD, "once a message has been sent in it", stands in the docstring (`core_check.py:48`) and in the reason (`core_check.py:127`). The second OLD, "send one message and run it again.", stands nowhere in one piece: the reason splits it across the literals `"... send one "` and `"message and run it again."` (`core_check.py:128-129`), and the run of the second pair alone exits 2 with `OLD occurs 0 times`. `mutation_check.py#mutated` refuses both before any run (`mutation_check.py:188-207`). So the sentence does not state the run that showed the second assertion red, and the sealer re-running a sample of the crafter's claims gets a refusal from this one.

The fact the sentence argues does hold. Each pair below lands once, and each mutant went red on the assertion of the part it replaced: the first at `tests/skills/test_core_check.py:141`, the second at `tests/skills/test_core_check.py:142` (executed, `## Probes`, one pair per call so that `seal mutate` printed the cases' output). The fix is to the record, not the code. Round 1 ran each pair on its own, so the fix pass runs the batch below before it writes `executed`. The paragraph's last two sentences, which say which line failed is read from the case, are replaced with the failing lines the single runs print.

```markdown
**Mutation** (executed, after commit 57265336): `bin/seal mutate skills/verify/scripts/core_check.py` with two `--replace` pairs over `bin/test tests/skills/test_core_check.py -q -p no:xdist -k test_refuses_with_a_reason_where_no_transcript_can_be_named`. Each OLD is one string literal of the reason in `find`: the docstring repeats the reason's first added clause, and the reason splits its instruction across two literals, so an OLD written as the sentence's words lands twice or nowhere and is refused. The first pair replaced `"writes a session's transcript once a message has been sent in it, "` with `"writes a session's transcript at some point, "`. The second replaced `"message and run it again."` with `"message."`. The baseline passed, both mutants were red, and the run exited 0 with 0 survived. A batch prints no failing line, so each pair was also run alone, which prints the cases' output: the first mutant failed at `tests/skills/test_core_check.py:141`, the assertion on "transcript once a message has been sent in it", and the second at `:142`, the assertion on "send one message and run it again" (executed).
```

## Confirmations

What matched: `frame/design.md` *Scope* 1. The reason at `skills/verify/scripts/core_check.py:125-130` is the frame's offered wording word for word, its first sentence is the old reason unchanged, and the exit stays 1 (`core_check.py:271-274`). Read against `git show 920a9584:skills/verify/scripts/core_check.py` at `:121-122`.

What matched: `frame/design.md` *Scope* 2 and contract rule 14. The docstring's *It fails, exit 1* list at `core_check.py:45-54` names the `--transcript` reason and the session reason apart, and carries the added sentence for the session reason only, in the same commit as the code (57265336). The `--transcript` reason at `core_check.py:113` is unchanged, as *Scope*, *Out* puts it (read).

What matched: `frame/design.md` *Scope* 3 and contract rule 15. The two new assertions at `tests/skills/test_core_check.py:141-142` each fail with only their own part removed: the old reason fails at `:141`, a mutant that drops the timing clause fails at `:141`, and one that drops "and run it again" fails at `:142` (executed, `## Probes`). The crafter's red-first claim, the first new assertion failing on the old reason, matches the run with the old reason restored. The existing assertions on the session id and directory (`:140`), the `--transcript` reason (`:144`) and `Test_main`'s prefix (`:436`) are unchanged. No test function was added, so no new case is read against its group: the change adds assertions to the case that already covers this reason.

What matched: the phase boundary. Claimed, `bin/test tests/skills/test_core_check.py -q`, 27 passed. Run in the clone at e9dd4df9, it gives 27 passed, exit 0 (executed).

What matched: the reflow 5dee05dc. The crafter reported a word diff against 8d3523e3 showing line breaks only. `git diff --word-diff 8d3523e3 5dee05dc -- skills tests` prints no removed or added word, and the plain diff touches six lines, all inside the module docstring and the case's docstring (executed).

What matched: the closed set of contract rule 12 for the reason's text. `git grep -n -i 'no transcript'` and `git grep -n 'seal core'` outside `seal/threads/` find the reason written at `core_check.py:126` alone and paraphrased in its docstring at `:46-49`. `docs/checks/the-session-hooks.md:51-52`, `docs/running/what-a-script-gates.md:73`, `README.md:217`, `:330`, `README.ko.md:221`, `:334`, `hooks/lib/core.py:9` and `skills/implement/orchestration.md:28-32` say what `seal core` reads or when it runs, and none states a reason, so the added sentence leaves each true (executed for the searches, read for each hit). The orchestrator's step runs `seal core` after the person's first message, so it never meets the first-input case.

What matched: the orchestrator's fold e9dd4df9, read as a claim. `skills/implement/orchestration.md:53-56` asks the orchestrator to rewrite every frame statement HEAD contradicts. The fold dates the frame's tree coordinates and quoted text to 920a9584 instead, and gives its grounds in a row of `frame/plan.md` *Judgments of the run*. Each coordinate the frame names was opened at 920a9584 and holds there: `core_check.py:34`, `:43`, `:45-51`, `:104-123`, `:110`, `:117`, `:121-122`, `:212-220`, `:263-266`, and `tests/skills/test_core_check.py:127`, `:138`, `:140`, `:419`, `:432` (executed, `git show 920a9584:<path> | sed -n`). Dated, none of them is a present-state claim HEAD can contradict. A statement rewritten to HEAD's lines would have to quote the new reason as the before-state, which removes the grounds the change stands on. The fold therefore leaves no frame statement false, and the row names the document it departs from with grounds. This round finds the judgment holds.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at HEAD, including `tests/skills/test_seal.py`, which names `core_check.py` at `:3798`, and the modules that glob `skills/verify/scripts/`. The suite stays labelled `unverified`, as `gaps.md` *Not verified* row 1 labels it, and that label is honest: only `tests/skills/test_core_check.py` was run, by the crafter and by this round. | `gaps.md:7` | the orchestrator, at the broad gate |
| Probes B1 and B2, a `claude --bare` session against a stand-in Messages API, which the changelog fragment copies as the `--bare` answer. This round did not re-run them: they need the `claude` command line and a local stand-in server, and they change no code in this diff. In the tree, `Test_judge::test_refuses_under_bare_and_names_it` and the bare branch of `Test_main` hold the same reading on planted transcripts, and they passed in the run above. | `frame/design.md:22-23`, `changelog.md:3` | the sealer, which samples the records' executed claims |
| Whether `! seal core` typed as an interactive session's first input prints the new reason, and passes once one message has been sent. | `frame/questions.md:14` (Q1) | the owner, once, after updating to 0.32.2 |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_core_check.py -q`, in the clone at e9dd4df9 | 27 passed, exit 0 |
| `git diff --word-diff 8d3523e3 5dee05dc -- skills tests`, filtered for removed or added words | none printed (grep exit 1); `git diff --stat` shows 6 lines changed in two files |
| `bin/seal mutate skills/verify/scripts/core_check.py --replace "once a message has been sent in it" "at some point" --replace "send one message and run it again." "wait." --tests "<T>"`, the phase record's pairs verbatim, where `<T>` is `bin/test tests/skills/test_core_check.py -q -p no:xdist -k test_refuses_with_a_reason_where_no_transcript_can_be_named` | exit 2, `refused: pair 1: OLD occurs 2 times`; nothing written |
| `bin/seal mutate skills/verify/scripts/core_check.py --replace "send one message and run it again." "wait." --tests "<T>"` | exit 2, `OLD occurs 0 times`; nothing written |
| `bin/seal mutate skills/verify/scripts/core_check.py --replace` the four lines of the reason literal (`core_check.py:126-129`) with the old one-line reason, `--tests "<T>"` | `red`, exit 0; failed at `tests/skills/test_core_check.py:141` on the old reason |
| `bin/seal mutate skills/verify/scripts/core_check.py --replace "\"writes a session's transcript once a message has been sent in it, \"" "\"writes a session's transcript at some point, \"" --tests "<T>"` | `red`, exit 0; failed at `tests/skills/test_core_check.py:141` |
| `bin/seal mutate skills/verify/scripts/core_check.py --replace '"message and run it again."' '"message."' --tests "<T>"` | `red`, exit 0; failed at `tests/skills/test_core_check.py:142` |
| `git status --short` in the clone after the mutants | clean: each mutant restored the file |
