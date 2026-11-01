# Review round 1: 1793538229-each-passage-keeps-its-home

```seal
target: c1837d28 against release/v0.27.3
```

This is the first round, so no fact was carried from an earlier one; every coordinate below was opened at `c1837d28`. No `seal/parity.md` is declared, so the round writes no `original:` line. The review ran in a `git clone --no-local` of the branch worktree under the round's scratch directory.

The axes walked, beside the table in `skills/code-review/SKILL.md`: whether each moved passage keeps its meaning at its home; whether each new citation resolves to a section that states the removed words; the boundary of the pair filter (both paths under `agents/`, one path under it, a path that only starts with the letters `agents`); what `BASELINE` still stores; whether the module holds a passage's text; whether each citation the diff adds can be opened from a clone; and the honesty of the suite's label. Authorization, query scope, concurrency and security have no surface here: the diff changes two prose files and one test module, and no script, hook or printed message.

## Findings

### 1. The module's docstring pins the measure to a commit that no branch holds, so a clone cannot open the citation

```seal
severity: should
location: `tests/text/test_no_passage_is_pasted_into_a_second_file.py:30`, `seal/threads/1793538229-each-passage-keeps-its-home/frame/design.md:3`, `seal/threads/1793538229-each-passage-keeps-its-home/frame/design.md:14`
evidence: executed `git clone --no-local <worktree> <clone> && git -C <clone> cat-file -t 79252e48`, `git for-each-ref --contains 79252e48`, `git merge-base --is-ancestor 79252e48 origin/main`, `git merge-base --is-ancestor 48d035aa origin/main`, `git merge-base --is-ancestor 48d035aa release/v0.27.3`, `git diff --quiet 79252e48:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md 48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md`
```

Why it matters: the rewritten *What is counted* paragraph gives the grounds for leaving a pair of two definitions out as `79252e48:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` *The table*, row K2. A contributor who reads the docstring and runs `git show` on that citation gets an error. In a fresh clone, `git cat-file -t 79252e48` answered "Not a valid object name". In the main checkout, `git for-each-ref --contains 79252e48` lists no ref, and the commit is no ancestor of `origin/main` (exit 1). It is a commit of #1237's feature branch. That branch was squashed into the release branch as `48d035aa`, and `docs/branch-and-release.md:158` states what a squash does: it "discards every commit" the branch wrote, "and anything naming one of them by SHA stops resolving". `docs/one-root-by-lifetime.md:45-46` gives the same rule for a citation: "a squash orphans it". The commit is only fetchable from GitHub's `refs/pull/1237/head`, which no clone fetches by default.

The claim was that the docstring cites "the measure at its commit, as the docstring already cites `67694cba:seal/specs/…`" (`frame/design.md` *Scope* item 7). The precedent holds and this pin does not. `67694cba`, `aa687d35` and `0ed5dd3b`, the other pins under `tests/`, are each an ancestor of `origin/main` (exit 0). `48d035aa` is an ancestor of `origin/main` and of `release/v0.27.3` (exit 0). It holds the same file byte for byte (`git diff --quiet` exit 0), and its *The table* row K2 carries the grounds the docstring quotes. The module is the only tracked file outside `seal/threads/` that cites `79252e48` (`git grep 79252e48`). `frame/design.md:3` and `:14` carry the same pin and tell the reader to "read with `git show 79252e48:<path>`". Those lines leave with the work item at the settle, so the docstring is the line the fix must change. The frame's lines are named because the same command fails there while the work item stands.

```python
(`48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md`
*The table*, row K2). A definition paired with any other file is counted,
```

The same commit replaces `79252e48` with `48d035aa` at `frame/design.md:3` and `:14`, where the frame says the measure is read.

```seal
verdict: fixed 25c268b4
answer: The finding holds. `tests/text/test_no_passage_is_pasted_into_a_second_file.py:30` now cites `48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-1.md` *The table*, row K2. `48d035aa` is an ancestor of `origin/release/v0.27.3` (executed: `git merge-base --is-ancestor`, exit 0), and its file holds the row `| K2 policy and instructions` that the docstring quotes (executed: `git show 48d035aa:<path>`). The module ran green after the edit, 9 passed, and `ruff check` and `ruff format --check` exit 0 on it (executed). The two frame lines, `frame/design.md:3` and `:14`, were changed by the orchestrator in `541e8c5e`, and this pass does not edit the frame. `git grep 79252e48` over `tests`, `docs`, `skills`, `agents`, `templates` and the three root files finds nothing after `25c268b4` (executed). The one other place in this work item's diff that still cites `79252e48` is `trail/phases/phase-1.md:7`. That line records what phase 1 read, and a fix pass writes no phase record, so it stands, and the hand-back names it.
```

## Confirmations

```seal
confirms: none
```
What matched: K2.6 is gone from `agents/crafter.md` and cited at its home. `agents/crafter.md:45-47` now cites `skills/implement/SKILL.md` *2. Implement test-first, and let each rule name its test*. `skills/implement/SKILL.md:224-226` states the removed clause word for word: "its case first, seen red against the tree as it stands, then the code, then the case green". The sentence "Build the phase as a vertical slice", which `tests/behaviour/test_chain_hooks_hardening.py:1084` needs, stands. Step 1 makes every `skills/` path in the definition the plugin's, so the citation resolves for a spawned crafter. Read, and executed through the narrow run below.

```seal
confirms: none
```
What matched: K2.8 keeps the fact and cites its reasons. `skills/implement/SKILL.md:53-55` keeps "Setting one does not carry the other" and cites `docs/one-root-by-lifetime.md` *What the repository decides for itself, and how it is read*. `docs/one-root-by-lifetime.md:220-230` gives both reasons the skill dropped: one row cannot express the middle answer, and the two surfaces have different audiences. Read.

```seal
confirms: none
```
What matched: K2.9 keeps the route and cites contract rule 5. `skills/implement/SKILL.md:161-164` keeps the handoff route and the three labels, which `tests/text/test_the_handoff_before_round_one.py` reads. `skills/agent-contract/SKILL.md:71-80` states the removed facts: a fact with neither a coordinate nor a label is an assertion nobody has opened and is opened before it is built on, and an aggregate is not a coordinate. The citation form `contract rule <N>` is the one `skills/writing-style/SKILL.md:261` gives a skill, and the same skill already cites contract rule 2 at `:257`. The dropped history clause, "one such fact reached five documents", goes to git, as `skills/core/SKILL.md` *The rule a mechanism is kept against* sends history. Read; `tests/behaviour/test_a_cited_section_stands_in_its_file.py` executed green in the narrow run.

```seal
confirms: none
```
What matched: the filter is exactly the frame's and its boundary holds. `tests/text/test_no_passage_is_pasted_into_a_second_file.py:150` skips a pair only when both paths start with `agents/` (`:75`). The slash keeps a path like `agents.md` out. `git ls-files agents` lists only the five definitions, so the filter exempts nothing that is not a definition. `corpus` is unchanged and keeps its one `git_listing` call, which `tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py:85` counts. `over_baseline` keeps its message. `BASELINE` (`:199-204`) holds the two `README.md` keys at 2 and 1 and nothing else. Its comment states the stored count and who removes it. Read.

```seal
confirms: none
```
What matched: the frame's S1 and S2. With `BASELINE` at two entries, `test_no_pair_shares_more_than_it_was_measured_at` passed over the tree at `c1837d28`. The module's own source shares no 15-word run with any corpus file, and none with the rule change's `to` text, both counted through the module's own `words` and `windows`. Executed (*Probes*).

```seal
confirms: none
```
What matched: the frame's S7. `skills/settle/scripts/rule_changes.py#parse` read `frame/design.md` as one `change` with `errors=[]` and `unread=[]`. Its `from` stands at `docs/the-record-layout.md:348-350` inside *The root records* (`section_lines` gives 336 to 354). Executed.

```seal
confirms: none
```
What matched: the seen-red claims of `trail/phases/phase-1.md` *Seen red*, as far as reading settles them. The crafter claimed that S4 was red at the base. At the base, `shared_counts` has no filter, so the case's `agents/a.md` with `agents/b.md` pair is counted and its equality fails, as the quoted message says. The crafter claimed S3 was red under the `or` mutant. Under that mutant, the pair `agents/crafter.md` with `skills/planted/SKILL.md` leaves the count, so `named` is empty. The crafter claimed S5 was red under the `>=` and `!=` mutants of `over_baseline`'s comparison. Each makes one of the two rebuilt cases name the planted pair at or below its entry. The four `seal mutate` runs were not re-run this round. Read.

```seal
confirms: none
```
What matched: each new test, read against its group. The new `test_a_run_two_definitions_share_is_not_counted_and_one_beside_a_skill_is` (`:337`) is the only case that pins the filter on two definitions. The second parameter of `test_a_paste_is_named_with_the_pair_the_run_and_the_act` (`:238`) overlaps it on a definition paired with a skill. It also covers something no other case does: it reads `agents/crafter.md` through `tree()` and `corpus`, so leaving `agents/` out of the corpus, the frame's rejected A5, turns it red with a `KeyError`, while the planted-text case stays green. The module declares no `TARGET`, so no `seal layout --pairs` pair applies. `planted_pair` (`:257`) builds placeholder words and pins no sentence of a definition, as `docs/what-a-script-gates.md` *The checks* asks. Read.

```seal
confirms: none
```
What matched: the three *Departures from the frame* in `trail/phases/phase-1.md`. S3 as a parameter is the group rule `agents/crafter.md` *A new test starts from its group* states. The definition pair stated under *What is counted* matches where the filter acts (`frame/design.md` *Data & interfaces*). The one constant `DEFINITIONS` is named twice in the filter and adds no unit. Read.

```seal
confirms: none
```
What matched: nothing left standing on the old fact. `git grep` over `tests`, `docs`, `skills`, `agents` and `CONTRIBUTING.md`, outside `seal/threads/`, for `cluster by cluster`, `#755`, `BASELINE` and the module's name finds no sentence that states the removed entries or #755's clustering. The module's two other readers, `docs/the-record-layout.md:351` and `tests/behaviour/test_waiver_decided_at_start.py:61`, name the module and none of its stored counts. `.test_durations` still holds the unparametrised id of the paste case. Durations are runner data and state no rule. Executed.

```seal
confirms: none
```
What matched: the census row that `gaps.md` closed. The orchestrator claimed `tests/test_censuses.py` passed at `c1837d28` after `frame/design.md:24` was rewritten. The module ran green in the clone at that commit, 176 passed. Executed.

```seal
confirms: none
```
What matched: the suite's label is honest. `gaps.md` *Not verified* names the full suite, the repository-wide lint and the format check as unverified at HEAD, with the orchestrator by `seal gate` as the answerer. `trail/phases/phase-1.md` *The phase-boundary run* calls its 82 modules a `git grep` sample, as contract rule 12 asks. The design's P1 names its method, the module's own reader over the whole corpus, as making the verbatim list whole. It leaves the fresh-words part of the class open and says so. Read.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check at `c1837d28` | `gaps.md` *Not verified*, first row | the orchestrator, by `seal gate`, once the rounds settle |
| Whether a case should refuse a `<sha>:<path>` citation to a commit no branch holds; the class beyond this diff is not enumerated here | `tests/` | the orchestrator, filing it if the class is wanted |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/text/test_the_handoff_before_round_one.py tests/behaviour/test_the_pull_request_language_is_the_repositorys.py tests/behaviour/test_a_cited_section_stands_in_its_file.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_a_moved_rule_leaves_its_definition.py tests/behaviour/test_chain_hooks_hardening.py -q -p no:xdist`, in the clone at `c1837d28` | exit 0, 442 passed |
| `bin/test tests/test_censuses.py -q -p no:xdist`, in the clone | exit 0, 176 passed |
| `uvx ruff check` and `uvx ruff format --check` on `tests/text/test_no_passage_is_pasted_into_a_second_file.py` alone | both exit 0 |
| an inline `python -c`, with no file written, importing the module and counting `windows(words(...))` of its own source against each `tree()` text and against the rule change's `to` | no corpus file shares a run with the module; the `to` shares 0 runs with it |
| `rule_changes.parse` and `section_lines` on `frame/design.md` and `docs/the-record-layout.md`, inline | one `change`, `errors=[]`, `unread=[]`; *The root records* at 336 to 354 |
| `git clone --no-local` of the worktree, then `git cat-file -t 79252e48` in the clone | `fatal: Not a valid object name 79252e48`; after `git fetch` of `refs/pull/1237/head` from the remote, the object resolves, and it is an ancestor of that ref (exit 0) |
