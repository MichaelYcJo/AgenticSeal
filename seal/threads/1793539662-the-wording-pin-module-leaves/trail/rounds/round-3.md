# Review round 3: 1793539662-the-wording-pin-module-leaves

```seal
target: 05b3fedf, fixes c92b77a9..05b3fedf
```

This is a verifying round. Its target is the diff of round 2's fix pass at 05b3fedf. That diff holds two commits. 9e99aa4b deletes one comment line in `tests/behaviour/test_chain_hooks_hardening.py`. 05b3fedf appends round 2's close block. The diff changes no other path (executed: `git diff --stat c92b77a9..05b3fedf`). Carried from rounds 1 and 2 and not re-established, because the fix diff touches none of them: S1 to S5 and S7 of `frame/design.md`, the G5 search over the deleted module's 55 names, the version move a87e88d6, the frame's G4 table of holders, and round 2's reading that `trail/phases/phase-1.md:17` stands. Re-derived this round: whether the module's comments still say what `EMPHASIS` strips correctly after the deletion, and whether the close block's claims hold. The review ran in a `git clone --no-local` of the worktree at 05b3fedf. `seal/parity.md` is not declared, so the round block has no `original:` line. The record is in English because `seal/config.md` has no `Record language` row.

## Findings

None. This round found no defect in the fix diff, and the fix pass's commit adds no unit, so no `regression:` line is owed.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the close `fixed 9e99aa4b`. Round 2 asked for one line to be deleted: the bullet "It reads `*` and not `_`. See `EMPHASIS` above for why." 9e99aa4b deletes exactly that line and nothing else (executed: `git show --stat 9e99aa4b` lists one file, one deletion). At 05b3fedf the residue list under the batch sweep, `tests/behaviour/test_chain_hooks_hardening.py:878-893`, holds two bullets: *It CROSSES HEADINGS* and *It refuses by the WORDS in the window*. Both are unchanged from b2da123a, and the list's lead-in still reads correctly over two bullets (read). The code it described is unchanged. `EMPHASIS` at `:634` is `re.compile(r"[*_`]+")`. `batch_instructions` strips it at `:657` before the search. The case at `:779-795` keeps `collect them in _one batch_`, at `:791`, among the spellings that must be found (read).

The close claimed that its search listed every sentence in the module that states which markers the guard strips. Re-run at 05b3fedf, that holds. `grep -n -i -E "emphasis|underscore|asterisk|markers?|\`_\`"` over the module returns sixteen lines. The search matches more than the two sentences the close names, but none of the others states which markers are stripped. Lines `:614`, `:618`, `:646`, `:670`, `:776` and `:895` name the strip or the markers without naming one, and `:634`, `:657` and `:794` are the constant and its two uses. The comment at `:623-632` says all three markers are stripped and argues why for `_`. The case comment at `:787-788` says the marker set was widened. No line says a marker is kept (executed). The close said that nothing outside the module was searched. This round searched outside it. `git grep -n -w EMPHASIS -- . ':!seal/threads'` lists the definition at `:634` and its uses at `:657` and `:794`, and nothing in another file. `git grep -n -i -E 'and not \`_\`|not \`_\`|reads \`\*\`|batch_instructions|emphasis (strip|pattern|marker)'` outside `seal/threads` and `.test_durations` lists hits in this module alone. `git grep -n -i -E 'emphasis|underscore|asterisk'` over the six other files that contain "one batch" or "single batch" exits 1 (executed). Both searches look for wordings, so they are a sample of an unbounded class of spellings. The guard has no other definition in the tree, and the three files whose `check:` lines name the module (`agents/crafter.md:94` and `:193`, `docs/the-session-hooks.md:24`) state nothing about its markers (executed: `git grep -n test_chain_hooks_hardening`). So the open part of the sample is small.

The close claimed that the module passes and that ruff passes on the file. Re-run in the clone at 05b3fedf: `bin/test tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist` exited 0 with `29 passed`. `uvx ruff check` and `uvx ruff format --check` on the file each exited 0 (executed). The close block is appended after round 2's paste-ready fix and removes no line from the records (executed: `git diff c92b77a9 05b3fedf -- seal/` has no removed line).

```seal
confirms: none
```
What matched: the fix pass's labels are honest. The close labels its narrow run and its ruff calls `executed`. It labels its class search as covering the module and not the tree, which is what it ran. It claims no suite beyond the one module. The broad gate stays `unverified` and is the orchestrator's (read: round 2's close block, and `gaps.md` *Not verified*).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite and the repository-wide lint and format at 05b3fedf. This round ran the one module the fix changed. The crafter's labels and those of rounds 1 and 2 for the suite stay `unverified`. With this round nothing is open, so what comes due is the broad run and then the sealer's spawn | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate --base origin/release/v0.27.3 --record seal/threads/1793539662-the-wording-pin-module-leaves` |
| Round 1's other rows of `## Not judged`: a sentence naming the deleted module in words no search reached, whether the version move belongs in the changelog commit, and S8. The fix diff touches none of them, so they stand with the answerers round 1 named | `trail/rounds/round-1.md` *Not judged* | the answerers that table names |

## Probes

| Command | Result |
|---|---|
| `git diff --stat c92b77a9..05b3fedf` | two files: round 2's record, 5 lines added; `tests/behaviour/test_chain_hooks_hardening.py`, 1 line removed |
| `grep -n -i -E "emphasis\|underscore\|asterisk\|markers?\|\`_\`"` over `tests/behaviour/test_chain_hooks_hardening.py` at 05b3fedf | 16 lines; none says a marker is left unstripped |
| `git grep -n -w EMPHASIS -- . ':!seal/threads'` at 05b3fedf | the definition at `:634` and uses at `:657` and `:794`, all in the module |
| `git grep -n -i -E` for the bullet's wording, `batch_instructions` and the emphasis strip, outside `seal/threads` and `.test_durations` | hits in `tests/behaviour/test_chain_hooks_hardening.py` alone |
| `git grep -n -i -E 'emphasis\|underscore\|asterisk'` over the six other files containing "one batch" or "single batch" | exit 1 |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist` in the clone at 05b3fedf | exit 0, `29 passed` |
| `uvx ruff check` and `uvx ruff format --check` on `tests/behaviour/test_chain_hooks_hardening.py` | each exit 0 |
| `git diff c92b77a9 05b3fedf -- seal/`, filtered to removed lines | none |
