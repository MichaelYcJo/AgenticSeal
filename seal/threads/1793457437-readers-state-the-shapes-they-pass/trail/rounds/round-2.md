# Review round 2: 1793457437-readers-state-the-shapes-they-pass

```seal
target: f6d83501, fixes 49acc5c1..f6d83501
```

This is a verifying round. Its target is the diff `49acc5c1..f6d83501`: fd549f8e and b5a4d754, which answer round 1's two findings, a56f2bcf (`gaps.md`), 4f586f0d (round 1's close blocks), and f6d83501, the orchestrator's fold of `frame/design.md` *Scope* items 1 and 3 with its row in `frame/plan.md` *Judgments of the run*. Neither `seal/parity.md` nor a `Reference specs` row exists, so no behaviour is compared with an original and the round block carries no `original:` line.

Carried from round 1 and not established again: the probe result that `home_at` returns `.git/seal` for a repository holding both roots once the shared README's first line has a trailing space (round 1 *Probes*). This round re-read `hooks/lib/optin.py:215-255` and did not rebuild that repository. Re-established this round: what `header_field` reads (`evals/scripts/noninferiority.py:1058-1063`), that `parse_record` turns a missing count into 0 (`evals/scripts/noninferiority.py:1077-1080`), and every verdict below.

## Findings

### 1. The frame's acceptance row S3, its count of cases and its R41 grounding still state the count rule that round 1's finding 2 corrected

```seal
severity: should
location: `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:18`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:48`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:54`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:74`
evidence: read `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:18`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:48`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:54`, `seal/threads/1793457437-readers-state-the-shapes-they-pass/frame/design.md:74`, `tests/evals/test_noninferiority.py:1905-1943`, `skills/code-review/orchestration.md:71-82`
```

Why it matters: f6d83501 folds *Scope* item 3 to the row spelling `header_field` reads (`frame/design.md:30`). Its row in `frame/plan.md` says the fold is made because the next crafter and the verifying round read the frame. Four other places in the same file still stand on the older reading.

- S3 at `frame/design.md:48` says a record "with its `New false rows` cell spaced off" and its verdict edited to `pass` makes `check_record` return no problem. Read as the name cell, the spelling the framer probed, it holds. Read as any cell spaced otherwise, it does not: `test_a_count_padded_with_more_spaces_is_read` at `tests/evals/test_noninferiority.py:1934-1943` asserts that a value cell padded with more spaces is read and the `pass` refused. A row with two readings is the defect finding 2 named.
- The *Verifiable how* cell of S3 names one case, seen red with `header_field` accepting any spacing. The padded case cannot go red under that mutation. Round 1's close of finding 2 says it was seen red with the value read as `\S*`.
- `frame/design.md:54` says the work adds one case in `tests/evals/test_noninferiority.py`. The module now holds two new cases, one of them parametrized over four spellings.
- `frame/design.md:74` counts "the three cases" this work adds. With the padded case they are four.
- The *Grounding* row R41 at `frame/design.md:18` says `header_field` matches the row "with single spaces". `evals/scripts/noninferiority.py:1062` takes at least one space on each side of the value, which is what finding 2 showed.

`skills/code-review/orchestration.md:71-82` (*The fix pass then finds what the fixes left standing*) has the fix pass find every other statement of a rule its range reworded. It has the orchestrator fold each one that stands in the frame, so that the round and the next crafter read one rule. The fold took item 3 and none of these four. The sealer reads the frame's acceptance rows against the tree, and S3 under its wider reading describes a case the tree contradicts.

This finding takes neither a `regression:` nor a `reopens:` line. The four sentences are the framer's wording, which no commit of the fix range introduced. Round 1's finding 2 named `evals/README.md`, the case's docstring and the changelog, and its close holds at each of them (the confirmation of `round-1#2` below). The four sentences are further instances of the class finding 2 belongs to, left standing by the fold in a file it edited.

The fix replaces the sentence in the R41 cell at line 18, the S3 row at line 48, the sentence at line 54, and the count at line 74. It touches no other file.

```markdown
Line 18, in the R41 cell, the sentence that names `header_field`:
`header_field` matches `\| <name> \| <value> \|` with one space on each side of the name, at least one on each side of the value and nothing outside the pipes, and `parse_record` reads a missing count as 0.

Line 48, the whole row:
| S3, R41 | Given a record whose numbers fail, with its `New false rows` row spelt otherwise than `\| <name> \| <value> \|` with one space on each side of the name, at least one on each side of the value and nothing outside the pipes, and its verdict edited to `pass`, when `check_record` reads it, then it returns no problem. Given the same record with the value cell padded by more spaces, it refuses the `pass`. `evals/README.md` says both. | `tests/evals/test_noninferiority.py` *Test_check_record*: `test_a_count_row_spelt_otherwise_is_read_as_naught`, its four ids seen red with `header_field` accepting any spacing, and `test_a_count_padded_with_more_spaces_is_read`, seen red with the value read as `\S*`, each in a scratch clone |

Line 54, the second sentence:
The tests gain two parametrize ids in `tests/hooks/test_optin.py`, one case in `tests/hooks/test_config.py`, two cases in `tests/evals/test_noninferiority.py`, one of them parametrized over four spellings, and one marker on two cases of `tests/github/test_release_completeness_check.py`.

Line 74, in the first cell:
nothing in return for the four sentences, the four cases and the one marker this work adds
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: fd549f8e. The marker paragraph at `templates/setup/seal-README.md:55-64` now says that every gate passes over a `seal/` whose `README.md` does not open with the marker. It says that the gates then read the root under the git directory where that root's `README.md` opens with the marker, and read the repository as one that never opted in where none does. `hooks/lib/optin.py:251-255` does this: the opt-out file first, then the two places in order, the first marked one winning (read). `seal/README.md` is byte-identical to the template (executed, `cmp`, exit 0). The changelog clause at `changelog.md:3` says the same (read).

The close claims that the paste-ready sentence would drop the words `never opted in`, which `tests/behaviour/test_first_setup_asks_once.py:686` pins. That test asserts the words anywhere in the paragraph. So the paste-ready sentence would have failed it only together with the rewrite of the paragraph's opening sentence, which held those words before. The close made both edits, so its reason holds for the pair it made, and the wording it kept matches the opt-out paragraph at `templates/setup/seal-README.md:66-68` (read). The narrow run passed with the pinning module in it (executed).

"Every gate" is read with this tree's meaning of a gate, a hook the dispatcher runs (`docs/the-session-hooks.md:10-11`, `hooks/lib/optin.py:3`). Under that reading the sentence holds. The review-chain check is not a gate in that vocabulary. It reads the routing declarations git carries under `seal/threads/` with no marker test (`skills/code-review/scripts/chain_check.py:1426-1441`, `skills/code-review/scripts/chain_check.py:1454-1456`, read), and the README does not speak of it.

The close cites contract rule 12 for the paragraph's opening sentence and names no method. This round searched the tree for the claim's words (executed, `git grep` on `never opted in`, `does not open with`, `without the marker` and `every gate is then silent`). The search listed `docs/one-root-by-lifetime.md:58-63`, `skills/implement/bootstrap.md:33-42`, `hooks/lib/optin.py:8-12` and `skills/implement/scripts/seal.py:766-770`. Each holds: the first says the place that holds the marker decides, the next two say an unmarked `seal/` is the project's own, and the last speaks of the opt-out file. The search is a sample built from words.

```seal
confirms: round-1#2
```
What holds: b5a4d754. `evals/README.md:62-67` says `check` finds each count only on a line spelt `| <name> | <value> |`, with nothing before the first pipe or after the last, one space on each side of the name, and at least one on each side of the value. That is the pattern at `evals/scripts/noninferiority.py:1062`, searched with `re.M`, so `^` and `$` bound the line (read). The changelog clause and the docstring at `tests/evals/test_noninferiority.py:1921-1925` say the same (read). The added clause `nothing before the first pipe` is the `^` the close names.

The close says each case was seen red under a mutation of `header_field`. This round wrote its own two mutants, one probe file, run once (executed). Under a pattern that takes any spacing around the name and value and trailing blanks after the last pipe, each of the four ids of `test_a_count_row_spelt_otherwise_is_read_as_naught` failed. Under a value read as `\S*`, `test_a_count_padded_with_more_spaces_is_read` failed. With the reader as it stands, the four ids passed. The crafter's own `seal mutate` runs were not repeated.

Read against its group, `Test_check_record` at `tests/evals/test_noninferiority.py:1883-1943`: the padded case is the only case whose value cell has more than one space. Its sibling `test_refuses_an_edited_cell_the_verdict_does_not_follow` writes single spaces, so it stays green under the `\S*` mutant (read). `bin/seal layout --pairs` names no pair for the module (executed).

```seal
confirms: none
```
What matched: the fold's two *Scope* items. Item 1 at `frame/design.md:28` and item 3 at `frame/design.md:30` state what the two README sentences now say (read). The `frame/plan.md` row of *Judgments of the run* cites `skills/code-review/orchestration.md` *The fix pass then finds what the fixes left standing*, which stands at `skills/code-review/orchestration.md:71` (read). Finding 1 concerns the sentences of the same file that the fold did not take.

```seal
confirms: none
```
What matched: the suite's label. The row a56f2bcf adds to `gaps.md` *Not verified* names the full suite, the lint and the format check after round 1's fix pass as not run. It names the orchestrator as their answerer and calls the 67-module set a sample built from two searches (read). The label is honest. No suite count is claimed in it.

```seal
confirms: none
```
What matched: the close blocks of 4f586f0d. The commit adds one close block under each of round 1's two findings and changes no other line of `trail/rounds/round-1.md` (executed, `git diff 49acc5c1..f6d83501`). Each `fixed` commit it names, fd549f8e and b5a4d754, is an ancestor of the target (executed, `git log`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at the branch head | the whole tree | the orchestrator, by `seal gate` under the `Broad gate` row of `seal/config.md` |
| The crafter's `seal mutate` runs that round 1's close of finding 2 reports; this round ran its own two mutants instead | `trail/rounds/round-1.md`, the close of finding 2 | the sealer, which re-runs a sample of the crafter's claims |

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over `tests/evals/test_noninferiority.py`, `tests/behaviour/test_first_setup_asks_once.py`, `tests/behaviour/test_docs_line_wrap.py`, `tests/hooks/test_optin.py`, `tests/behaviour/test_one_word_one_meaning.py`, `tests/behaviour/test_evals_layout.py`, `tests/behaviour/test_no_document_names_the_old_roots.py` and `tests/behaviour/test_both_editions_carry_the_same_folds.py` | 476 passed, exit 0 |
| `bin/test -q -p no:xdist tests/evals/test_tmp_round2.py` in the worktree | 9 passed: each of the four spellings failed its case under the any-spacing mutant, the padded case failed under the `\S*` mutant, and the four spellings passed with the reader unchanged. The file and its bytecode were deleted after the one run |
| `bin/seal layout --pairs tests/evals/test_noninferiority.py` | 1 file read, 0 pairs, exit 0 |
| `cmp seal/README.md templates/setup/seal-README.md` | exit 0 |
| `git grep -n` on `never opted in`, `does not open with`, `without the marker`, `every gate is then silent`, `only in the spacing`, `spaced otherwise` and the old case name | the four places named under `round-1#1`, the earlier phase and round records, and the new case's id `the name spaced otherwise`; no other statement of either old claim |
