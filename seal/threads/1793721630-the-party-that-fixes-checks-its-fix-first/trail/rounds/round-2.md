# Review round 2: 1793721630-the-party-that-fixes-checks-its-fix-first

```seal
target: e7ca44b9b, fixes c763863c2..e7ca44b9b
```

This is a verifying round. Its target is `git diff c763863c2..e7ca44b9b`: the fix commit `ad41ec7a8`, the record commits `908706952`, `dbe698972` and `f70ee91e4`, the orchestrator's fold `fc18e1ea2`, and `e7ca44b9b`, which adds round 1's three close blocks and nothing else (`git diff --numstat` printed 15 added lines and 0 removed). It was read in a `git clone --no-local` at `e7ca44b9b` under the round's scratch directory. `seal/parity.md` is not declared, so no `original:` line is owed. `seal/config.md` has no `Record language` row, so the record is in English.

Carried from round 1, not re-established: the coordinates of the two pinned cases (`tests/text/test_the_rules_have_one_owner.py#test_a_decision_after_the_frame_is_folded_into_it` and `tests/text/test_a_moved_rule_leaves_its_definition.py#test_the_crafter_reads_its_range_and_the_records_whole_before_it_hands_back`), the runner `bin/test` and the form of a `bin/seal mutate` run, and where the fold rule's home is. G9's figures lie outside the fix diff and were not re-read. Every verdict below was reached this round.

The implementer's account was read as claims. The crafter claimed it did not apply finding 2's and finding 3's paste-ready text as given, and gave grounds in each `answer:` line. For finding 2 it said "the implementer" names no crafter after a phase or an issue-comment fold. `skills/code-review/orchestration.md:30-31` defines the implementer as "the crafter that wrote the last commit the round reviewed", and no round has reviewed anything at a fold after a phase, so that claim holds (read). For finding 3 it said "that open part" had no referent. In round 1's snippet the nearest antecedent is "where the class is open", which names a class and not a part, so that claim holds too (read). The crafter claimed `seal mutate` red over the fold paragraph and the crafter rule at `ad41ec7a8`. This round re-ran one mutant in each file at HEAD, and both went red (`## Probes`). It claimed S7's modules at 355 passed, and this round ran them and got 355 passed. It claimed S1, S3, S5 and S6 as the frame states them, and this round re-ran each with the same result. Its `unverified` claim, that no case reads *Job*'s new clause, rule 12's new sentences or the review paragraph's `routing.md` clause, was searched this round. `git grep` under `tests` and `evals` for "in every fix pass", "proofer's share", "or `routing.md` statement" and "folds it as" found only the crafter rule's own pin at `tests/text/test_a_moved_rule_leaves_its_definition.py:491-493`, so the claim holds (executed). The orchestrator claimed it read `frame/design.md` whole against HEAD after its fold and removed a clause from *Scope* item 5. The committed item 5 holds no such clause (read). A clause removed before the commit leaves nothing in git, so its removal cannot be seen. Its whole-file reading missed one statement, which finding 1 names.

## Findings

### 1. The review file's fold sentence now folds "it", the named statement, which the frame's *Scope* item 6 had removed, and item 6 still says the sentence folds the frame

```seal
severity: should
location: `skills/code-review/orchestration.md:78-82`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:47`
evidence: read `skills/code-review/orchestration.md:71-89`, `skills/implement/orchestration.md:51-71`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:47`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:73`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/design.md:94`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/plan.md:14`, `seal/threads/1793721630-the-party-that-fixes-checks-its-fix-first/frame/plan.md:37`
regression: round-1#2
```

The unit is the fold sentence of `skills/code-review/orchestration.md` *Orchestrator: a phase is a fresh crafter, and a fix pass resumes the implementer*, at `:78-82`. `frame/design.md` *Scope* item 6, which phase 1's `frame/plan.md` row (`:37`) delivers, says the sentence folds the frame as the fold rule's home states and "no longer reads as folding the one named statement", but `ad41ec7a8`, adding `routing.md` for round 1's finding 2, replaced "folds the frame" with "folds it", so the defect came from the fix rewording the sentence's object, a part round 1's snippet did not cover.

Why it matters: the sentence at HEAD reads "Where the hand-back names a frame or `routing.md` statement, which the fix pass does not edit, the orchestrator folds it as `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* states". The only antecedent of "it" is the named statement. So the sentence again tells the orchestrator to fold the one statement the hand-back names. That is the fold `frame/design.md` *Removes* row 4 (`:94`) takes out: "the fold of 'that statement', the one line a hand-back names". It is also the second failure `frame/plan.md` *Technical context* names (`:14`): an orchestrator that folds the cells a crafter named without reading the file. The citation of the home softens this, since the home says "not only the named line". But an orchestrator reads this paragraph right after a fix pass, and the paragraph's own words point the other way. `frame/design.md` S5 cannot catch the change: its `git grep` for "folds that statement" printed nothing this round (`## Probes`), because the same meaning now has other words. The crafter's answer to finding 2 states the choice: "folds 'it'". The orchestrator's fold `fc18e1ea2` then read `frame/design.md` whole and left *Scope* item 6's "The fold sentence folds the frame as" standing, which HEAD now contradicts. That is a statement of the kind this work item moves to the party that folds.

The fix names the files rather than the statement, at `skills/code-review/orchestration.md:78-82`:

```markdown
round that follows reads that account as a claim. Where the hand-back names
a frame or `routing.md` statement, which the fix pass does not edit, the
orchestrator folds each file that holds one, read whole and not at the
named line alone, as `skills/implement/orchestration.md` *Orchestrator:
the order inside a ticket* states, in a commit of its own, before it spawns
the verifying round, so the round and the next crafter read one rule.
```

The first and last lines join the paragraph's text as it stands at `:78` and `:82`. The fix pass rewraps the paragraph to the file's width after the change, as `dbe698972` did after round 1. This snippet does not reach every statement of the fact, and these are owed too:

- `frame/design.md` *Scope* item 6 (`:47`): "The fold sentence folds the frame as" becomes a sentence saying the fold sentence folds each file that holds a named frame or `routing.md` statement, read whole, as the home states. That line is the orchestrator's to fold, with a `frame/plan.md` *Judgments of the run* row, and the fix pass names it in its hand-back.
- `frame/design.md` S5 (`:73`) and *Removes* row 4 (`:94`) stay true after the fix, and so does the work item's `changelog.md`, whose last sentence says the paragraph "cites both homes". The fix pass reads each of them against its wording.
- No case reads the fold sentence. `gaps.md` *Not verified* row 2 says so, and it stays true. Whether the fix pass adds a clause of this sentence to a case is its decision, and it says which in its answer.

```seal
verdict: fixed cc57960ce
answer: Holds. I wrote the sentence in my own words, shorter than the paste-ready text. "Read whole and not at the named line alone" restated the home's "not only the named line", which the citation already brings, so `skills/code-review/orchestration.md:78-83` now reads "the orchestrator folds each file that holds such a statement, read whole, as `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* states". The paragraph is rewrapped. The line-wrap, paste and cited-section cases pass, and S5's `git grep` still prints nothing. I added the clause to `tests/text/test_the_rules_have_one_owner.py#test_the_fix_pass_reads_the_implementers_context_before_it_resumes`, which reads this section already. It went red with round 1's "folds it as" put back by `seal mutate`. `f766d927a` moved its comment above it. `gaps.md` row 2 now says which sentences that case reads (`cc57960ce`, `5bd959407`). S5, *Removes* row 4 and `changelog.md`'s "cites both homes" stay true. `frame/design.md` *Scope* item 6's "The fold sentence folds the frame as" is named in the hand-back for the orchestrator to fold.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: `agents/crafter.md:19-25`, the *Job*, now names "`changelog.md` in the last phase and in every fix pass", so the new rule's "a file your *Job* lets you write" (`agents/crafter.md:166-167`) (`agents/crafter.md:167-169`) covers the fragment in a fix pass. That matches `docs/layout/the-record-layout.md:66-73` ("The rule binds whoever writes the commit: the crafter's fix pass, ...") and `skills/implement/SKILL.md:416-420` (read). No other statement of the crafter's writes was found to contradict it: `git grep` for "last phase" with "changelog" over `agents`, `skills`, `docs`, `templates`, `README.md` and `CONTRIBUTING.md` printed `agents/crafter.md:23` and `docs/layout/the-record-layout.md:68` alone (executed). The fragment's *Changed* entry and first process row name the new write (read). `gaps.md` *Not verified* row 3 is honest: `git grep -n 'in every fix pass' -- tests evals` printed nothing and exited 1 (executed).

```seal
confirms: round-1#2
```
What holds, for what finding 2 asked: `skills/implement/orchestration.md:58-71` takes a statement "in a file the crafter does not write, a frame file or `routing.md`" and has the orchestrator read "each such file whole against HEAD, not only the named line". A statement found in `gaps.md` or `changelog.md` goes to "a fix pass", which is "the crafter that wrote the work item's last build or fix commit, resumed or spawned fresh" as the review file's section states. That names a party after a phase, after an issue comment and after a fix pass alike. Before any phase, neither `gaps.md` nor `changelog.md` exists yet (`agents/crafter.md:21-23`), so no party is needed there (read). `skills/code-review/orchestration.md:75-79` names "a frame or `routing.md` statement" in both places, and `agents/crafter.md` step 10 says "each statement named for the orchestrator" (read). The pins at `tests/text/test_the_rules_have_one_owner.py:383-396` follow the new wording, and a mutant that dropped "or `routing.md`" from the fold paragraph went red (`## Probes`). The rewording of the review file's fold object, which this fix also made, is finding 1 above.

```seal
confirms: round-1#3
```
What holds: `skills/agent-contract/SKILL.md:163-174` keeps the closed set and says that, for an open class, "the hand-back says so, and says where the part of the class its list did not reach stands", and that "Neither the part a sample did not reach nor what you did not finish is the proofer's share" (read). That restores, for the open class alone, the duty round 1 found removed, and the crafter's grounds for its own wording hold (see above). `agents/crafter.md:173-177` applies it to the tree-wide sample. A mutant that dropped "and says where the part it did not reach stands" from that sentence went red (`## Probes`). S1's `git grep` printed `skills/agent-contract/SKILL.md:171` alone (executed). The fragment's *Changed* entry and first process row say a closed list's rest is no longer handed on and an open class's still says where it stands, and `gaps.md` *Not verified* row 1 names the new sentences (read). Contract rule 19's "the hand-back says so as rule 12 asks" stays true against the new rule 12 (read). No case reads rule 12's new sentences: the only `git grep` hits for "did not reach" and "proofer's share" under `tests` and `evals` are the crafter rule's pin (executed). `frame/design.md` G4 decides that no case is added, so this is no finding.

```seal
confirms: none
```
What matched: S1, S3, S5, S6 and S7 of `frame/design.md` at `e7ca44b9b` (executed in the clone). S1 printed `skills/agent-contract/SKILL.md:171` alone. S3's and S5's `git grep` printed nothing and exited 1. S6's `git diff --name-only 6ca420572...HEAD -- ':!seal/'` listed the four texts and the two test modules, and nothing else. `bin/test` over the seven S7 modules exited 0 with 355 passed. That is a narrow run of the slice, not the broad gate. No reference root is touched.

```seal
confirms: none
```
What matched: the orchestrator's fold `fc18e1ea2`, apart from finding 1. *Scope* items 1, 2, 4 and 5, S2 and *Removes* row 2 now state what `ad41ec7a8` built. The drafts of rule 12 and of the crafter rule are gone, and each item names the heading its text stands under, as `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* asks of a fact with one source (read). The fold's row at `frame/plan.md:53` gives the decision, its grounds and the documents it was judged against (read). The record commits `908706952`, `dbe698972` and `f70ee91e4` touch `gaps.md`, a rewrap of the review file's paragraph and the fragment, and each line they change states what HEAD holds (read). The two changed pins' comments name the round and finding they answer, and each pin is a clause of the case that already held its sentence, so no new case is owed a group read (read).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at `e7ca44b9b`. The suite stays `unverified`. This round leaves finding 1 open, so what comes due next is its fix pass and its reader, then the orchestrator's broad run and the sealer's spawn after it. | the whole tree | the orchestrator |

## Probes

| Command | Result |
|---|---|
| `bin/test` over the seven S7 modules, `-q`, in a `git clone --no-local` at `e7ca44b9b` | exit 0; 355 passed |
| `bin/seal mutate skills/implement/orchestration.md --replace` "write, a frame file or `routing.md`, the orchestrator" "write, a frame file, the orchestrator" `--tests "bin/test tests/text/test_the_rules_have_one_owner.py -q -k folded_into_it"` | the case failed at `tests/text/test_the_rules_have_one_owner.py:398`; the file was restored |
| `bin/seal mutate agents/crafter.md --replace` "calls it one and says where the part it did not reach stands." "calls it one." `--tests "bin/test tests/text/test_a_moved_rule_leaves_its_definition.py -q -k reads_its_range"` | the case failed at `tests/text/test_a_moved_rule_leaves_its_definition.py:496`; the file was restored, and `git status --short` printed nothing |
| `git grep -n -e 'by its words and by the' -e 'folds that statement' -- skills/code-review/orchestration.md` (S5) | exit 1, nothing printed, while `:80` holds "folds it as" |
