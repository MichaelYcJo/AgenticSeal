# Review round 2: 1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words

```seal
target: 16d5454d4, fixes 4b57687b7..16d5454d4
```

This verifying round read `git diff 4b57687b7..16d5454d4`, the four commits of round 1's fix pass, in a `git clone --no-local` checked out at `16d5454d4`. The branch's base is `origin/release/v0.31.1`, which names `c186a59ac`. The `target:` line takes the verifying round's form, `<sha>, fixes <a>..<b>`, because the check refuses a line that joins both forms. Its job is to answer round 1's three findings, each closed `fixed`, and to read the units the fix pass changed as code. It stayed inside that diff. It opened what the fix commits cite outside it: `chain_check.py#channel` and its docstring, `unverified_check.py#items`, `#field_values` and `#nothing_block`, `skills/settle/rule-changes.md` *Rule changes*, `templates/setup/config.md` *What no row governs*, the rest of `skills/implement/SKILL.md` *4.*, and `frame/plan.md` *Judgments of the run*. No `seal/parity.md` is declared, and `seal/config.md` holds no `Record language` row, so this record is English.

Carried from round 1 as coordinates and not re-established: where `channel` builds its references (`chain_check.py:863-866`), where the no-change block is read (`unverified_check.py#nothing_block`), and which plan row records the orchestrator's acceptance (`frame/plan.md:81`). Each was opened again at the target, and each still stands where round 1 put it. Round 1's verdicts on the build outside the fix diff are not carried and not re-reviewed here. No earlier finding is closed `deferred`.

The implementer's account was read as a claim and checked against the tree. The fix pass claimed that finding 1's changed assertion failed against the old message. This round restored the old message in the clone and ran the case. It failed at `tests/skills/test_chain_check.py:1283`, on the new assertion and on no other line (Probes). The fix pass also claimed that `seal unverified` exits 0 on the work item. It does, with 7 open and 1 closed. The phase 3 record still says the old implement §4 sentence "stays true" (`trail/phases/phase-3.md`, *Decisions in the build*). A phase record states the commit it names, and HEAD contradicting it is no defect (contract rule 12), so this round agrees with the orchestrator's reading that the record stays.

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-1#1
```
What holds: the first-record refusal now names all three reference lines. At `skills/code-review/scripts/chain_check.py:870-876` it reads "names `<ref>` in the first record: there is no earlier round to name, so it holds no `confirms:`, `reopens:` or `regression:` line, and what it confirms is prose". That is the text round 1's fix gave. It holds for a `regression:` or `reopens:` line as well as a `confirms:` line, and it agrees with the function's docstring ("the first record writes none", `:850`). The pin at `tests/skills/test_chain_check.py:1283-1286` asserts the new clause for both first-record refusals, and the case's docstring (`:1249-1254`) says the same. `docs/forms/the-round-record.md:78-80` names the three lines, and the paragraph is rewrapped. Contract rule 14's two duties are met in the same commit, since the message is documented in the form and the fragment and is pinned by the case. Contract rule 15 is met as well: the case went red with only the message reverted. Every other statement of the fact was listed by `git grep -n -e 'confirms is prose' -e 'confirmations are prose' -e 'first record' -e 'no earlier round to name'` outside `seal/threads/`, which lists only the message and the docstring (executed). Read: the diff of `669d93cab`. Executed: the case, red on the old message and green at the target.

```seal
confirms: round-1#2
```
What holds: `skills/implement/SKILL.md:355-363` now says the no-change block may leave out `why:`, which matches `unverified_check.py#nothing_block` (`field_values(found[0], (), (WHY,))`, `:715`) and `skills/settle/rule-changes.md:47-54`. Each refusal the new sentence names is one the reader makes. A second item is refused at `:713-714`. A field other than `why:` and an empty `why:` are refused by `field_values` (`:669-678`). A `- nothing` line spelt any other way fails `ITEM_RE` (`:145`), so `nothing_block` returns None and the section is refused as prose. The sentence does not list a line outside the item, a line that is not a field, or a field given twice, which `items` (`:637-662`) also refuses. "alone" and "its one field `why:`" in the same sentence already exclude all three, so a builder reading it writes nothing the check refuses. The other statements of the field were listed by `git grep -n -E '`why:`|why: '` over `skills`, `docs`, `templates`, `agents`, `hooks` and `CONTRIBUTING.md` (executed). They are `skills/settle/rule-changes.md:48`, which agrees, and `templates/setup/config.md:137` and `:141`, which list `why:` as a word that stays English and say nothing about whether it is required. Read: the diff of `b46133128`. Executed: `tests/behaviour/test_docs_line_wrap.py`, `tests/behaviour/test_unverified_rows_close.py`, `tests/skills/test_passages.py` and `tests/skills/test_unverified_check.py` among the modules in Probes.

```seal
confirms: round-1#3
```
What holds: the process-rows item of `gaps.md:14` opens with `closed`. Its second cell names what closed it, the orchestrator's acceptance in `frame/plan.md:81`, the last row of *Judgments of the run*. It does not name the original answerer, which `skills/implement/SKILL.md` *4.* says leaves a closing unproven. `seal unverified` on the work item exits 0 and counts the row as closed (executed). The fix pass also added a sentence to `changelog.md` naming the reworded message. That sentence says that "a first round that writes a `confirms:`, `reopens:` or `regression:` line is refused". It does not hold for `confirms: none`, which `channel` still passes in a first record under C1 (`tests/skills/test_chain_check.py:1291-1292`). The same bullet already says that the template no longer writes that line and that a record written before the change still reads. So a reader acting on the bullet writes no line the check refuses, and this round opens no finding for it. Read: the diff of `590664858`.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The fix pass edited `tests/skills/test_chain_check.py` through a Python substitution, a departure from contract rule 9. Its content is right (`confirms: round-1#1`, read in `git diff 669d93cab^ 669d93cab`). Whether the departure needs an act beyond its disclosure is not this round's to decide | `669d93cab`, `tests/skills/test_chain_check.py:1249-1254`, `:1283-1286` | the orchestrator |
| The full suite, the repository-wide lint and the format check at HEAD, which include whether the changed lines of `chain_check.py` and the case meet `ruff format`. The build labels them `unverified`, and the label is honest, since the fix pass names only narrow runs | `gaps.md`, its first row | the orchestrator, at the one broad run after the rounds settle |

This round leaves nothing open. What comes due is the orchestrator's broad run, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test tests/skills/test_chain_check.py -q -k channel` at the target | 5 passed, exit 0 |
| the old first-record message restored in the clone's `chain_check.py:872-875` through the edit tool, then `bin/test tests/skills/test_chain_check.py -q -k test_refuses_a_reference_naming_no_earlier_record_or_finding`, then the edit undone | 1 failed, exit 1, at the `so it holds no` assertion; the clone was clean after the restore |
| `bin/test tests/behaviour/test_docs_line_wrap.py tests/behaviour/test_unverified_rows_close.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/skills/test_passages.py tests/text/test_the_record_is_written_in_words.py tests/text/test_review_axes.py tests/skills/test_unverified_check.py tests/skills/test_chain_check.py -q` | 730 passed, exit 0 |
| `bin/seal unverified seal/threads/1793769283-each-form-a-script-does-not-decide-on-goes-to-plain-words` | exit 0; 7 open, 1 closed, 0 unreadable |
