# Review round 1: 1793539662-the-wording-pin-module-leaves

```seal
target: a87e88d6 against origin/release/v0.27.3
```

The target is the branch's diff against `origin/release/v0.27.3` (14bfd992) at a87e88d6: the build b27b9835, its records 5b0beb72, and the orchestrator's version move a87e88d6. No earlier round exists, so nothing is carried from one. The frame's G4 table, which gives each of the 24 deleted cases its holder, is carried from the framer's `ls` at 18e3bd1a and not re-established: the diff touches none of the holder modules that table names. `seal/parity.md` is not declared, so the round block has no `original:` line. The record is in English because `seal/config.md` has no `Record language` row.

## Findings

### 1. The rewritten comment above `EMPHASIS` says two constants of that name mean one thing, and the tree holds one

```seal
severity: should
location: `tests/behaviour/test_chain_hooks_hardening.py:624-636`
evidence: executed `git grep -n -w EMPHASIS`, `git show 7a8899d5 -- skills/code-review/scripts/chain_check.py | grep -n EMPHASIS`, `git show 14bfd992:skills/code-review/scripts/chain_check.py | grep -c EMPHASIS`
```

Why it matters: the build claimed (`trail/phases/phase-1.md`, the paragraph that opens *The comments keep the fact each states for its own code*) that the comment "now ends by saying the two constants of that name mean one thing, which is the fact the old citation stood for". That fact does not hold. `git grep -n -w EMPHASIS` lists one constant in the tree, `tests/behaviour/test_chain_hooks_hardening.py:637`, and its three uses in the same module. The constant `skills/code-review/scripts/chain_check.py` held, `EMPHASIS = re.compile(r"[*_`]+")`, was deleted by 7a8899d5 (#1211) with its two readers. At the base 14bfd992 `chain_check.py` holds the name zero times. So the new sentence at `:634-636` adds a false claim to the comment it amends. The same comment's opening clause at `:624-625` cites "the normaliser of this same name in `skills/code-review/scripts/chain_check.py`" as the source of the three markers, and that clause stands on the same deleted constant. Contract rule 19 says a change that amends a text also removes what stood on the old fact in the same commit. A reader who acts on the comment, for example a fix pass told to keep this constant in step with `chain_check.py`, looks for a constant that is gone. Scope item 5 of `frame/design.md` asks each comment to keep the fact it states for its own code. The fact this comment can keep is the trade itself: stripping `_` costs a readable file name and finds nothing less.

The fix, in words for the first line because it holds a mark this record does not quote (code point U+1F7E1). At `:624-625`, delete ", which is what the normaliser of this same name" and "in `skills/code-review/scripts/chain_check.py` already settled on", so that line 624 reads `# All three markdown markers.` and the text from "Round 1's" onward is unchanged, then rewrap. At `:633-636`:

```python
# change what is found, since no stem in `ASKING` and no word in
# `BATCH_PHRASE` carries one. A printed file name losing its underscores is
# worth less than a spelling the guard cannot see.
EMPHASIS = re.compile(r"[*_`]+")
```

The fix touches a comment and no code, so it owes no case (`skills/verify/SKILL.md` *The narrow command still has to be able to fail*, the row for a comment or docstring inside source).

## Confirmations

```seal
confirms: none
```
What matched: S1 and S2 of `frame/design.md` hold at a87e88d6, executed in a clone. `git grep -n one_word_one_meaning -- . ':!seal/threads'` listed nothing and exited 1. `bin/seal rules --check` exited 0 and printed `seal rules: all 283 check lines in 55 rule files hold.`, the count the crafter reported.

```seal
confirms: none
```
What matched: the crafter's S3 and S4 claims, re-run as one probe. With `skills/writing-style/SKILL.md:278` set back to `check: tests/behaviour/test_one_word_one_meaning.py` and the module's row put back into `APPLIES_THE_SHARED_GUARD` at `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:77`, below the `before_any_floor` row, the two modules exited 1 with `5 failed, 6 passed`. One failure is `test_the_rules_for_text_an_agent_or_a_check_reads_reach_both_languages`. The other four are the four shrunken-corpus cases `trail/phases/phase-1.md` names, which confirms the crafter's report that S4 turns four cases red where the frame named one. Both files were restored with `git checkout`.

```seal
confirms: none
```
What matched: a narrow run over the six edited test modules and the modules that read the other changed paths (`tests/github/test_rules.py`, `tests/behaviour/test_release_hygiene.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/hooks/test_config.py`, `tests/skills/test_session_cost.py`, `tests/behaviour/test_the_release_check_watches_what_ships.py`) exited 0 with `872 passed`, executed through `bin/test` at a87e88d6. This is a probe of the slice and no seal. The crafter's 38-module run was not repeated whole.

```seal
confirms: none
```
What matched: the frame's G5 claim that no other file uses the module's units, re-taken. The module at 14bfd992 defines 55 top-level names, 24 of them cases, listed with `ast`. A `git grep -n -w` for each name outside `seal/threads` and `.test_durations` lists only units named `flat` in other files that import nothing from the module. `.test_durations` loses exactly 24 lines, all naming the module, and it loads with `json.load` as one object of 6157 keys with none naming it (executed).

```seal
confirms: none
```
What matched: each rewritten citation keeps a fact that holds. `hooks/lib/config.py:1413-1415` says the unit spells the old header in order to read it, and `docs/the-pact.md:32-41`, the third rule of *The words*, says such a text names no signer another way (read). `git grep -n -i signator` lists `hooks/lib/config.py:1425` as the only place outside tests and `docs/` that writes the old word, so the comment's "the one place" still holds for shipped code (executed). `skills/verify/scripts/session_cost.py:62-63` now cites *Measure the segment, and feed the flow log*, and that heading stands at `skills/verify/orchestration.md:158` (executed). The docstrings and comments in `tests/behaviour/test_a_release_is_sized_by_a_criterion.py`, `tests/behaviour/test_the_pull_request_language_is_the_repositorys.py` and `tests/text/test_edits_go_through_the_edit_tool.py` drop the citation and add no claim (read).

```seal
confirms: none
```
What matched: S7. The last paragraph of *여럿이 가질 수 있는 것은 누구 것인지 밝힌다* (`skills/writing-style/SKILL.md:245-250`) keeps that the sentence is no guarantee and that the rule broke seven times. It names the proofer at review as the reader and points to the second rule of the next section, whose line at `:278` now reads `check: none reader: the proofer at review`. It gives the meaning ground with the `skills/core/SKILL.md` heading as written there. It names no module, no fixing check and no #331 (read).

```seal
confirms: none
```
What matched: the orchestrator's version move a87e88d6 and its grounds in `frame/plan.md` *Judgments of the run*. `.claude-plugin/plugin.json` is the one file in the tree with a `"version"` key (executed: `git grep -n '"version"' -- '*.json'`). `.github/workflows/hygiene.yml:77-79` exits 0 on any base but `main`, as the row says (read). None of the three sibling branches changes `.claude-plugin/` or a file this diff touches (executed: `git diff --name-only origin/release/v0.27.3...<branch>` for each). `tests/behaviour/test_release_hygiene.py` passed inside the narrow run above.

```seal
confirms: none
```
What matched: the crafter's labels are honest. The full suite, lint and format are labelled `unverified` and named for the orchestrator's broad gate in `gaps.md` *Not verified*. The prose search for the module's name is labelled a sample in `trail/phases/phase-1.md` and `gaps.md`, as contract rule 12 asks for an unbounded class.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The suite beyond the modules this round and the crafter ran, and the repository-wide lint and format at a87e88d6 | `seal/config.md` *Broad gate* | the orchestrator, by `seal gate --base origin/release/v0.27.3 --record seal/threads/1793539662-the-wording-pin-module-leaves` |
| A sentence naming the module in words that no search reached. This round searched the tree outside `seal/threads` for spellings of "one word", "wording pin" and "word sweep", and for a word, case, check or 검사 joined to seal, sweep, pin, meaning or the old signer word. It found nothing that names the module. The class is unbounded in its spellings, so this is a sample, and its open part stands with the proofer of each later diff that touches prose | `skills/`, `docs/`, `agents/`, `templates/`, `hooks/`, `README.md`, `README.ko.md`, `CLAUDE.md`, `CONTRIBUTING.md` | the proofer of a later round whose diff touches prose |
| Whether the version move belongs in the commit that adds the changelog entry. `skills/implement/orchestration.md:330-333` puts it there, and a87e88d6 is a separate commit after 5b0beb72. The row in *Judgments of the run* argues which pull request carries the move and does not speak to the commit | `skills/implement/orchestration.md:330-333`, `frame/plan.md` *Judgments of the run* | the orchestrator |
| S8, that each of the 24 cases' facts keeps the holder G4 names. This round carried the framer's coordinates and did not reopen the holders | `frame/design.md` G4 | the sealer, by S8 |

## Probes

| Command | Result |
|---|---|
| `git grep -n -w EMPHASIS` at a87e88d6 | one definition, `tests/behaviour/test_chain_hooks_hardening.py:637`, and three uses in the same module |
| `git show 7a8899d5 -- skills/code-review/scripts/chain_check.py \| grep -n EMPHASIS` | the definition and its two readers, each on a removed line |
| `bin/seal rules --check` | exit 0, `all 283 check lines in 55 rule files hold` |
| `bin/test -q -p no:xdist tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/text/test_a_language_section_of_writing_style_opens_alone.py`, with the old check line and the old row put back through the `Edit` tool | exit 1, `5 failed, 6 passed`; both files restored with `git checkout`, and `git status --short` printed nothing |
| `bin/test -q` over the 13 modules named in the third confirmation | exit 0, `872 passed` |
| `git grep -n -w <name>` for each of the module's 55 top-level names, outside `seal/threads` and `.test_durations` | hits for `flat` alone, each in a file that imports nothing from the module |
