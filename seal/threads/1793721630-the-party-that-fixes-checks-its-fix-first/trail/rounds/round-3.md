# Review round 3: 1793721630-the-party-that-fixes-checks-its-fix-first

```seal
target: 9bc5519e5, fixes 1e7d196ba..9bc5519e5
```

This is a verifying round. Its target is `git diff 1e7d196ba..9bc5519e5`, read in a `git clone --no-local` at `9bc5519e5` under the round's scratch directory. The diff holds five commits. `cc57960ce` is the fix pass: it rewrites the fold sentence of `skills/code-review/orchestration.md`, adds a clause to a case in `tests/text/test_the_rules_have_one_owner.py`, and edits `gaps.md`. `5bd959407` edits `gaps.md` again, `f766d927a` moves the new clause's comment, `f0fd5e258` is the orchestrator's fold of `frame/design.md` *Scope* items 6 and 7 with `frame/plan.md` *Judgments of the run* row 4, and `9bc5519e5` adds round 2's close block and nothing else. Outside `seal/`, the diff touches `skills/code-review/orchestration.md` and `tests/text/test_the_rules_have_one_owner.py` alone (executed, `git diff --name-only 1e7d196ba..9bc5519e5 -- ':!seal/'`). The routing commit `1e7d196ba` stands just before the range, and this round read it with `git show` too. `seal/parity.md` is not declared, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is in English.

Carried from rounds 1 and 2 as coordinates, not re-established: the runner `bin/test` and the form of a `bin/seal mutate` run, the home of the fold rule at `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*, and the frame's scenarios S1 to S7 as the commands to re-run. Every verdict below was reached this round.

The implementer's account was read as claims. The crafter claimed it shortened round 2's paste-ready text because "not at the named line alone" repeats the home's "not only the named line". `skills/implement/orchestration.md:58-61` does say "reads each such file whole against HEAD, not only the named line", and the review sentence cites that home, so the claim holds (read). It claimed that `seal mutate` restoring "folds it as" turns the new pin red. This round ran that mutant and a second one, and both went red (`## Probes`). It claimed 522 passed over six modules. This round ran the line-wrap, paste, cited-section, one-owner, `tests/skills/test_unverified_check.py` and record-words modules and got 522 passed (executed). It claimed S5 with "folds it as" added prints nothing, and this round's run printed nothing and exited 1 (executed). The orchestrator claimed it read `frame/design.md` whole against HEAD after its fold and found *Scope* item 7 silent on the new pin besides item 6. This round read `frame/design.md` whole against HEAD and found no other statement HEAD contradicts (see the confirmations below).

## Findings

This round opens no finding.

## Confirmations

```seal
confirms: round-2#1
```
What holds: the fold sentence at `skills/code-review/orchestration.md:78-83` now reads "Where the hand-back names a frame or `routing.md` statement, which the fix pass does not edit, the orchestrator folds each file that holds such a statement, read whole, as `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* states, in a commit of its own, before it spawns the verifying round" (read). Its object is now each file, read whole, and no longer the one named statement. That is what the folded `frame/design.md` *Scope* item 6 says (`:47`) and what *Removes* row 4 (`:94`) takes out: "the fold of 'that statement', the one line a hand-back names". It agrees with the home at `skills/implement/orchestration.md:58-71`, which reads each such file whole against HEAD, not only the named line. The plan's second failure scenario at `frame/plan.md:14`, an orchestrator that folds the named cells without reading the file, has no support in the sentence any longer (read). The pin at `tests/text/test_the_rules_have_one_owner.py:206-208` reads that clause inside the section the case already reads (`:196-197`). A mutant restoring "folds it as" and a mutant writing "folds each such file as" both went red (`## Probes`). The clause sits in the one case that reads this section of `skills/code-review/orchestration.md`. `test_a_decision_after_the_frame_is_folded_into_it` (`:375-403`) reads the other file, `skills/implement/orchestration.md`, so the new clause covers nothing a case of its group already covered (read). The comment at `:204-205` now stands above the clause it names, and #1041's comment at `:209-214` stands above its own clauses again (read). The paragraph's rewrap passes `tests/behaviour/test_docs_line_wrap.py`, and the cited heading passes `tests/behaviour/test_a_cited_section_stands_in_its_file.py` (executed, in the 522 run). The other statements round 2 listed hold at HEAD: S5 (`frame/design.md:73`) prints nothing, *Removes* row 4 stays true, and `changelog.md:3` "cites both homes" stays true, since the paragraph cites contract rule 12 and the fold rule's home (read; S5 executed). The case's docstring at `:192-195` lists what #945 pinned and did not list #1041's clauses before this fix either. It states nothing about the fold sentence, so it stands on no fact the fix changed (read).

```seal
confirms: none
```
What matched: `gaps.md` *Not verified* row 2 (`gaps.md:8`) as `cc57960ce` and `5bd959407` left it. It says no case reads the sentences on what the fix pass's hand-back carries, `routing.md` among it, or on the round reading that account as a claim. It says the fix-pass case reads the close-block sentence and the fold sentence's clause "folds each file that holds such a statement, read whole", and nothing before them. The pin starts at "the orchestrator folds each file", so the sentence's opening condition "Where the hand-back names a frame or `routing.md` statement" is unpinned, and "nothing before them" discloses that (read). `git grep` under `tests` and `evals` for "fix pass's hand-back carries" and "reads that account as a claim" matched no line, and its wider pattern "hand-back carries" matched only an unrelated comment (`## Probes`, executed). The row's answerer is "the proofer at review", and this round read those sentences at `skills/code-review/orchestration.md:74-78` against `frame/design.md` *Scope* item 6 and found them as the item states (read).

```seal
confirms: none
```
What matched: the orchestrator's fold `f0fd5e258`. *Scope* item 6 (`frame/design.md:47`) now says the fold sentence has the orchestrator fold each file that holds a named statement, a frame file or `routing.md`, read whole, as the home states, and HEAD says the same (read). *Scope* item 7 (`:48`) now names `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` as gaining item 6's fold clause, and the case holds it (read). The fold's row at `frame/plan.md:55` gives the decision, its grounds and the document judged against (read). This round read `frame/design.md` whole against HEAD for any other statement the fix contradicts. S6 (`:74`) still lists the four texts and the two test modules, since `tests/text/test_the_rules_have_one_owner.py` was already one of them (executed below). G6 (`:14`) still says the fold takes "that statement", but the Grounding section reads the tree at `6ca420572` (`:5`), so HEAD does not contradict it (read). `frame/plan.md` *Technical context* is pinned to `6ca420572` in the same way (`:5`). Its line `:10`, "No case pins its sentences", already overreached its own `git grep` at that SHA, since the base's `test_the_fix_pass_reads_the_implementers_context_before_it_resumes` pinned the paragraph's close-block sentence (executed, `git show 6ca420572:tests/text/test_the_rules_have_one_owner.py`). That line stands outside the fix diff and is a base reading, which no party acts on after phase 1 closed, so this round opens no finding on it.

```seal
confirms: none
```
What matched: the routing row `1e7d196ba` (`frame/plan.md:54`). It routes round 2's regression to an ordinary fix pass because the fix at `ad41ec7a8` did something the frame does not say. That is the second row of `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame*. The third row does not apply, since the fold sentence had no regression routed before round 2 (read). The close block `9bc5519e5` adds round 2's verdict and answer and nothing else. Its `fixed cc57960ce` names a commit that touches `skills/code-review/orchestration.md`, a path the finding's `location:` names. Its answer's claims, the line range `:78-83`, the rewrap, the passing modules, the red mutant and the moved comment, each match what this round found (read and executed, above).

```seal
confirms: none
```
What matched: S1, S3, S5, S6 and S7 of `frame/design.md` at `9bc5519e5` (executed in the clone). S1 printed `skills/agent-contract/SKILL.md:171` alone. S3's and S5's `git grep` printed nothing and exited 1. S6's `git diff --name-only 6ca420572...HEAD -- ':!seal/'` listed `agents/crafter.md`, `skills/agent-contract/SKILL.md`, the two orchestration files and the two test modules, and nothing else. `bin/test` over the seven S7 modules exited 0 with 355 passed. That is a narrow run of the slice, not the broad gate. No reference root is touched.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `9bc5519e5`. The suite stays `unverified`. This round leaves nothing open, so what comes due is the orchestrator's broad run, then the sealer's spawn after it. | the whole tree | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/seal mutate skills/code-review/orchestration.md --replace` "folds each file that holds such a statement, read whole, as" "folds it as" `--replace` "orchestrator folds each file that holds such a statement, read whole, as" "orchestrator folds each such file as" `--tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -k reads_the_implementers_context"` | baseline passed; mutant 1 red, mutant 2 red; the file was restored, and `git status --short` printed nothing |
| `bin/test` over `tests/behaviour/test_docs_line_wrap.py`, `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, `tests/behaviour/test_a_cited_section_stands_in_its_file.py`, `tests/text/test_the_rules_have_one_owner.py`, `tests/skills/test_unverified_check.py` and `tests/text/test_the_record_is_written_in_words.py`, `-q` | exit 0; 522 passed |
| `bin/test` over the seven S7 modules, `-q` | exit 0; 355 passed |
| `git grep -n -e 'by its words and by the' -e 'folds that statement' -e 'folds it as' -- skills/code-review/orchestration.md` (S5 with the old wording added) | exit 1, nothing printed |
| `git grep -n -e "fix pass's hand-back carries" -e "reads that account as a claim" -e "hand-back carries" -- tests evals` | exit 0; one line, `tests/text/test_the_rules_have_one_owner.py:81`, a comment on #967's three labels that matches the third, wider pattern alone; the two phrases of the paragraph printed nothing |
