# Review round 2: 1793539662-the-wording-pin-module-leaves

```seal
target: b2da123a, fixes 6c85482c..b2da123a
```

This is a verifying round. Its target is the diff of round 1's fix pass at b2da123a: 36f836f5, which rewrites the comment above `EMPHASIS` in `tests/behaviour/test_chain_hooks_hardening.py`, and b2da123a, which appends round 1's close block. The diff changes no other path. Carried from round 1 and not re-established, because the fix diff touches none of them: S1 to S5 and S7 of `frame/design.md`, the G5 search over the deleted module's 55 names, the version move a87e88d6, and the frame's G4 table of holders. Re-derived this round: whether the rewritten comment holds against the tree, and whether the close block's claims hold. `seal/parity.md` is not declared, so the round block has no `original:` line. The record is in English because `seal/config.md` has no `Record language` row.

## Findings

### 1. The residue list under the batch sweep says the guard reads `*` and not `_`, and `EMPHASIS` strips `_`

```seal
severity: should
location: `tests/behaviour/test_chain_hooks_hardening.py:889`
evidence: read `tests/behaviour/test_chain_hooks_hardening.py:623-634`, `tests/behaviour/test_chain_hooks_hardening.py:657`, `tests/behaviour/test_chain_hooks_hardening.py:779-795`, `tests/behaviour/test_chain_hooks_hardening.py:878-893`
```

Why it matters: the comment above the sweep lists "what the window cannot see", and its second bullet at `:889` reads "It reads `*` and not `_`. See `EMPHASIS` above for why." That is false of the code. `EMPHASIS` at `:634` is `re.compile(r"[*_`]+")`, so it strips `_`. `batch_instructions` applies it to the whole body before the search at `:657`. The case at `:779-795` asserts that `collect them in _one batch_` is found. The comment the bullet points to "for why" is the one 36f836f5 rewrote, and at b2da123a it opens "All three markdown markers" and argues why `_` is stripped. So the pointer sends the reader to grounds for the opposite of what the bullet says. A maintainer who reads the residue list as the guard's known blind spots is told that a spelling in `_` escapes the guard, when the guard and its case both say it does not. The fix pass did not introduce this. The bullet and the three-marker constant both stand at the base 14bfd992 (`:893` and `:638` there), both since e391ea04 (#1099). This round found the bullet through the fix's own search, `git grep -n -w EMPHASIS`, which lists it as the fourth hit. It is neither a regression nor a reopened close, so the block carries neither line. Scope item 5 of `frame/design.md` asks each comment this work rewrote to keep the fact it states for its own code, and the bullet is the one other sentence in the module that states what `EMPHASIS` does.

The fix deletes the bullet, since an emphasis marker is no longer residue. The bullets above and below it are unchanged:

```python
    #   · It CROSSES HEADINGS. 140 characters over the flattened file is a
    #     span with no structural boundary in it, and #422 measured 42 % of
    #     `agents/framer.md` and 60 % of `agents/crafter.md` as positions where
    #     a new occurrence would fire. Bounding it at a heading is a change
    #     with its own failure direction — an instruction whose sentence
    #     straddles a heading would pass — and it is ruled out with grounds in
    #     `aa687d35:seal/specs/1789540097-three-checks-that-do-not-see-what-they-are-named-for/spec.md`
    #     *Out*.
    #   · It refuses by the WORDS in the window, so a definition that names a
```

The fix changes a comment and no code, so it owes no case (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the row for a comment or docstring inside source).

```seal
verdict: fixed 9e99aa4b
answer: The finding holds: `EMPHASIS` is `[*_`]+`, `batch_instructions` strips it from the whole body before the search, and the case at `:779-795` asserts that `collect them in _one batch_` is found (read). The round's fix was applied as written: the bullet "It reads `*` and not `_`. See `EMPHASIS` above for why." is deleted, and the bullets above and below it are unchanged. The class is every sentence in the module that states which emphasis markers the guard strips. It was listed with `grep -n -i -E "emphasis|underscore|asterisk|\`_\`"` over the module, which found the residue bullet and the comment above `EMPHASIS`. Every hit left after the fix says or assumes that all three markers are stripped, and `git grep -n -w EMPHASIS` outside `seal/threads` lists the constant and its two uses alone (executed). The fix changes a comment alone, so it owes no case and no mutation run (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*). `bin/test tests/behaviour/test_chain_hooks_hardening.py -q` exited 0, and `uvx ruff check` and `uvx ruff format --check` on the file exited 0 (executed). The fix changes nothing the work item ships, so `changelog.md` is unchanged.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: the close `fixed 36f836f5`. At b2da123a the comment at `tests/behaviour/test_chain_hooks_hardening.py:623-633` opens "All three markdown markers." and ends "worth less than a spelling the guard cannot see.", which is round 1's paste-ready text, rewrapped. It names neither `chain_check.py` nor a second constant (read). The close claimed the class was listed whole by its searches. Re-run at b2da123a, they hold. `git grep -n -w EMPHASIS` lists the one definition at `:634`, its uses at `:657` and `:794`, the comment at `:889`, and outside the module only this work item's records. `git grep -n -i -E "normali[sz]er of this|same name"` outside `seal/threads` and `.test_durations` lists nothing about `EMPHASIS` or `chain_check.py`. `git grep -n chain_check` over the module exits 1, and `git grep -c EMPHASIS` over `skills/code-review/scripts/chain_check.py` exits 1 (executed). The close claimed `bin/test tests/behaviour/test_chain_hooks_hardening.py -q` exits 0 and ruff passes on the file. Re-run in a clone at b2da123a, the module exited 0 with `29 passed`, and `uvx ruff check` and `uvx ruff format --check` on the file each exited 0 (executed). The close block is appended after the paste-ready fix and edits nothing else in round 1's record (read: `git diff 6c85482c..b2da123a`).

The prompt asked whether `trail/phases/phase-1.md:17` stands. It still says the comment "now ends by saying the two constants of that name mean one thing, which is the fact the old citation stood for". This round judges that the line stands and is no finding, for four reasons. First, `agents/crafter.md` *A fix pass appends close blocks and writes no phase record* gives the fix pass no write to a phase record, so the pass could not change the line. That rule also asks the pass to correct each other statement of what it reworded or to say why it stands. The close block does the second: it names `phase-1.md:17` as the build's past claim. Second, the line describes the build at b27b9835. Its descriptive half was true of that commit. Its false half, that two constants of that name exist, is exactly round 1's finding 1, which quotes it and is closed `fixed 36f836f5`. Third, `skills/core/SKILL.md` *The rule a mechanism is kept against* sends history to git, the release notes and the work record. A phase record is that history, and contract rule 19 governs a change to the text it amends, which no fix pass makes to a phase record. Fourth, `skills/code-review/scripts/pr_body.py` copies the phase records' paths alone and each round record's blocks with their close blocks (read: `:11-12`, `:310-315`, `:319-353`). The pull request's reader therefore sees round 1's finding and its correction, and never the phase record's sentence. No later phase reads the line: the plan has one phase, closed at b27b9835. The sealer reads phase records as claims, beside the round records that answer them.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite and the repository-wide lint and format at b2da123a. This round ran the one module the fix changed. The crafter's and round 1's labels for the suite stay `unverified` | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate --base origin/release/v0.27.3 --record seal/threads/1793539662-the-wording-pin-module-leaves` |
| Round 1's other rows of `## Not judged`: a sentence naming the module in words that no search reached, whether the version move belongs in the changelog commit, and S8. The fix diff touches none of them, so they stand with the answerers round 1 named | `trail/rounds/round-1.md` *Not judged* | the answerers that table names |

## Probes

| Command | Result |
|---|---|
| `git grep -n -w EMPHASIS` at b2da123a | the definition at `tests/behaviour/test_chain_hooks_hardening.py:634`, uses at `:657` and `:794`, the residue bullet at `:889`, and this work item's records |
| `git grep -n -i -E "normali[sz]er of this\|same name" -- . ':!seal/threads' ':!.test_durations'` at b2da123a | 14 lines, none about `EMPHASIS` or `chain_check.py` |
| `git grep -n chain_check -- tests/behaviour/test_chain_hooks_hardening.py` and `git grep -c EMPHASIS -- skills/code-review/scripts/chain_check.py` | each exit 1 |
| `git log --oneline -S` for the `EMPHASIS` definition and for the residue bullet | each first appears in e391ea04 (#1099) |
| `bin/test tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist` in a clone at b2da123a | exit 0, `29 passed` |
| `uvx ruff check` and `uvx ruff format --check` on `tests/behaviour/test_chain_hooks_hardening.py` | each exit 0 |
