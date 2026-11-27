# Review round 2: 1795742081-records-name-the-base-and-version-as-values

```seal
target: d22e62cf7, fixes 4a16d6e24..d22e62cf7
```

This is a verifying round. The base is the release branch at `68bb3d5a9`, the merge base. The fix range is the framer's fold `665fcf9f2`, the orchestrator's correction `941e217a4`, the crafter's fix `535a2a33e` and records commit `7991077ec`, and the close blocks `d22e62cf7`. No code unit is in the range. The new units are rule 19's narrowed moment and its sentence for clause R6, both in `skills/agent-contract/SKILL.md`, and the reworded records. The work item's records were read whole at `d22e62cf7`: `routing.md`, `frame/design.md`, `frame/plan.md`, `frame/questions.md`, `gaps.md`, `changelog.md` and `pr.md`, then `trail/phases/phase-1.md` and `trail/rounds/round-1.md`. No `pr.<lang>.md` stands, because `Commit and pull request language` is English. `seal/parity.json` is not declared.

Carried from round 1 and not re-run: the `gh issue view` reads of #1624, #1628 and #1629 on finding 3's `evidence:` line. Re-established this round: the *Scope* items of the other work item's frame at `762f284f7`, by `git show 762f284f7:seal/threads/1795742080-a-session-is-bound-by-the-crafters-rules/frame/design.md`. Its items 4, 5 and 6 change `skills/implement/fix-pass.md`, `skills/code-review/orchestration.md` and `skills/implement/orchestration.md`.

## Findings

### 1. Clause R6 keeps "a value the work item's own commit writes", which is also every value a record states, so it can be read to cancel R1 and to make R5 redundant

```seal
severity: should
location: `skills/agent-contract/SKILL.md:234-237`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:82`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:119-122`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/changelog.md:3`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/changelog.md:12`
evidence: executed `git grep -n -F 'own commit' -- ':!seal/threads/*/trail/rounds'`; read `skills/agent-contract/SKILL.md:215-237`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:54`, `templates/records/sdd-routing.md:16`, `templates/records/sdd-plan.md:31`
regression: round-1#2
```

The unit is the sentence `535a2a33e` added to rule 19's third paragraph, at `skills/agent-contract/SKILL.md:234-237`. The fold's R6 (`frame/design.md:82`) says "A value that the work item's own commit writes is a state of its branch". The fix wrote that sentence into the rule in like words. Both took their wording from round 1's paste-ready fix for finding 2, so the defect came from that snippet.

Why it matters: the paragraph opens at `:215` with "Nor does what a change writes state the value of a state outside the work item's branch". In this paragraph, "writes" means the text a change writes. R6 at `:234` then keeps "A value the work item's own commit writes". Read with the paragraph's own sense of the verb, every value a record states is a value its work item's commit writes. A `routing.md` sentence that says "the pull request merges into `release/v0.0.5`" is one, so R6 keeps the very sentence of the issue's evidence that R1 refuses. On that reading, R5 at `:231-234` also becomes redundant: a `Branch` row and a `target:` line are values the work item's commit writes. The example at `:235-237` points to the intended reading, a value whose source is the version file, which the commit writes and the `changelog.md` states. But the clause is the rule and the example is not. `frame/design.md:54` already words the intended reading: "a state the work item's commits make".

The tense matters too. "Writes" reads as present or future, so a framer can take R6 to keep the version that a later phase will write. The routing placeholder (`templates/records/sdd-routing.md:16`) and the *Operational impact* placeholder (`templates/records/sdd-plan.md:31`) both ask for a version number "only of a named moment". They agree with R6 only where R6 covers a value the commit has written. Before that commit, the number is a prediction of the version the release carries, which R1 holds.

Claimed: round 1's close of finding 2 says R6 was "applied in like words" from the fold, and that holds. The search printed `skills/agent-contract/SKILL.md:234`, `frame/design.md:54`, `:82` and `:121`, `changelog.md:3` and `:12`, `frame/plan.md:53`, round 1's lines, and lines about other facts elsewhere. `frame/plan.md:53` is a dated *Judgments of the run* row recording what was judged, and it stays. `frame/design.md:54` already states the intended reading, and it stays. The search is a sample under contract rules 12 and 19, because a statement of R6 in other words escapes it.

```markdown
<!-- skills/agent-contract/SKILL.md:234-237, from "A value the work item's own commit" to "is one. The rule" -->
round record and of `guarantee.md`. A value whose source is a file the
work item's own commit has written is a state of its branch, not one
outside it, and a sentence that states it stays: the version that the work
item carrying the move has written to the version file, and states in its
`changelog.md`, is one. The rule

<!-- frame/design.md:82, R6 -->
- R6. A value whose source is a file the work item's own commit has written is a state of its branch and not one outside it, and a sentence that states it stays. The example is the version that the work item carrying the move has written to the version file and states in its `changelog.md` (round 1, finding 2). Before that commit, the number is a prediction, which R1 holds.

<!-- frame/design.md:120-122, inside the `to` value -->
    check reads by value keeps its value, and so does a value whose source
    is a file the work item's own commit has written, such as the version
    that the item carrying the move writes to the version file. The placeholders of

<!-- changelog.md:3, the sentence after the form lines -->
So does a value whose source is a file the work item's own commit has written, such as the version the work item carrying the move writes to the version file and states in its `changelog.md`.

<!-- changelog.md:12, the clause in the Change cell -->
while a value of a published release, or one whose source is a file its own commits have written, stays;
```

```seal
verdict: fixed bfa001321
answer: The finding holds. `bfa001321` rewrites the sentence at `skills/agent-contract/SKILL.md:234-237` as the paste-ready fix and the fold's R6 (`df70a0369`, `frame/design.md:82`) state it: a value whose source is a file the work item's own commit has written stays, with the version the item carrying the move has written to the version file as the example. It also adds the fold's sentence that before that commit the number is a prediction. The paste-ready fix was read against the fold and applied with that added sentence. `8a341c1c0` rewords the added sentence: it first cited "this paragraph's first sentence", but the paragraph's prediction clause stands in its second sentence, so it now says the number is "a prediction of a state outside the branch, held as this paragraph holds every such prediction". `changelog.md:3` and `:12` take the paste-ready wording, and `:3` adds that before that commit the number is a prediction the paragraph refuses. `frame/design.md:82` and `:120-123` are the fold's lines. `gaps.md:9` now names the proofer in round 3 as its answerer, since R6 changed after round 2 read it. Executed after `8a341c1c0`: the finding's search prints `skills/agent-contract/SKILL.md:235`, `frame/design.md:54`, `:82` and `:121`, `changelog.md:3` and `:12`, `frame/plan.md:53` and `:54`, and the round records' lines, each now stating the written-file reading or a dated row of what was judged, and lines about other facts across `docs/`, `skills/`, `tests/`, `.github/`, `evals/` and other work items' records, which stand. `bin/test -q tests/text tests/behaviour`: 887 passed, 9 skipped, exit 0. `chain_check.py --worktree` prints no notice of a copy or a test pin.
```

### 2. Grounding G7 says the routing lines "cut from `<ref>` at `<commit>`" name no moment, but clause R4 at the target keeps them, and so do the plan's own lines

```seal
severity: should
location: `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:17`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/design.md:48`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/plan.md:23`
evidence: executed ``git grep -n -o -E 'cut from `origin/release/v[0-9.]+` at `[0-9a-f]+`' HEAD -- 'seal/threads/*/routing.md'``; executed `git grep -n -o -E '.{0,160}G7.{0,160}' -- seal/threads/1795742081-records-name-the-base-and-version-as-values/ ':!*/trail/rounds/*'`; executed `git ls-remote --tags origin 'v0.39*'` on 2026-11-27; read `skills/agent-contract/SKILL.md:228-231`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/plan.md:9`, `seal/threads/1795742081-records-name-the-base-and-version-as-values/frame/plan.md:22`
```

Why it matters: the orchestrator asked whether R4 and R6 together keep or refuse any value in this release's own records wrongly. One case is the line G7 lists for `1795736973-the-preflight-passes-where-a-round-is-owed`, the release's first work item: "The branch is cut from `origin/release/v0.39.2` at `e65830869`". G7 (`frame/design.md:17`) concludes that each such line "is true of the cut and names no moment, so it reads as a statement of today". That conclusion is no statement of the tree at `82169bfcc`, so it is read against the target (`skills/implement/SKILL.md` *Document layout — two roots, three lifetimes*). At the target, rule 19 (`skills/agent-contract/SKILL.md:228-231`) keeps "a value stated of a named commit ... or a date or a cut the sentence names". Each G7 line names the cut and its commit, so R4 keeps it. The clause "a release still open is no such moment" does not reach the line: the open release's ref is the value, and the cut's commit is the moment.

The frame's plan reads it the same way as R4. `frame/plan.md:9` names, as the drift to avoid, "a proofer raises a finding on a branch name that the sentence states of a named commit". `frame/plan.md:22` lists "the lines of `frame/design.md` G7" among the correct lines a report would print as noise. `frame/plan.md:23` takes the other side and counts G7 among the writes a hook "misses". The frame therefore gives two answers about the shape this repository's routing records use. A sealer, or a later framer who cites G7 as this tree's instance of the class, would raise findings on lines the rule keeps. That is the failure `frame/plan.md:9` names.

`frame/design.md:48` says "Those work items are released". One of G7's items, `1795736973-the-preflight-passes-where-a-round-is-owed`, is in release 0.39.2, which is still open: on 2026-11-27, `git ls-remote --tags origin 'v0.39*'` printed `v0.39.0` and `v0.39.1` and no `v0.39.2`. The bullet's decision, to leave those records as they are, still holds, because the settle removes each directory after its release ships and R4 keeps G7's lines anyway.

The `G7` search printed `frame/design.md:17`, `:18`, `:48` and `:137`, and `frame/plan.md:22` and `:23`. Lines `:18` and `:137` say that G7's bullets follow no form, which stays true. `frame/plan.md:22` already reads G7's lines as correct. The search is a sample under contract rules 12 and 19, because a statement of G7's conclusion that does not name G7 escapes it. Every statement it reaches is in the frame, so the fix is the framer's fold.

```markdown
<!-- frame/design.md:17, the last sentence of G7's second cell -->
Each sentence names the cut and the commit it was made at, so it states the ref of that moment, and clause R4 keeps it. A reader who takes the present tense "is cut" for today's state is the drift `frame/plan.md` *Technical context* names

<!-- frame/design.md:48 -->
- Rewriting the sentences of G6 and G7, or any other record under `seal/threads/`. Those records are other work items', the settle removes each directory after the release that ships it, and rule 19 binds what a change writes from here on.

<!-- frame/plan.md:23, in the second cell -->
so it misses the writes where `frame/design.md` G4 and G6 stand, or it is matched on `Write` too
<!-- and, later in the same cell -->
Its note falls on the `Branch` row and on each sentence that states a ref of a named moment, the lines of `frame/design.md` G7 among them.
```

```seal
verdict: fixed df70a0369
answer: The finding holds, and each sentence it names stands in the frame, which the framer's fold `df70a0369` rewrote as the paste-ready fix asks; this pass made no edit for it. Read at HEAD: `frame/design.md:17` says each G7 line names the cut and its commit, so R4 keeps it; `frame/design.md:48` says those records are other work items' and the settle removes each directory after the release that ships it; `frame/plan.md:23` drops G7 from the writes the hook misses and adds its lines to the sentences the hook's note falls on. Executed after `8a341c1c0`: the finding's `G7` search prints `frame/design.md:17`, `:18`, `:48` and `:138`, and `frame/plan.md:22`, `:23` and `:54`; `:18` and `:138` say G7's bullets follow no form, and `:54` is the orchestrator's dated row, so each stands. Not re-run: the finding's routing-line search and `git ls-remote --tags origin 'v0.39*'`, which the fold stands on. The read of the range and the records after `8a341c1c0`, the pass's last fix commit: executed `git diff --stat df70a0369 HEAD`, which names `skills/agent-contract/SKILL.md`, `changelog.md` and `gaps.md`, and printed rule 19's lines 228 to 242, `gaps.md`'s `## Not verified` rows and the end of `changelog.md:3`. Held from this pass's earlier prints and not printed again after `8a341c1c0`: `changelog.md:12`, the start of `changelog.md:3`, `routing.md` and the three frame files, which no commit of this pass touched and whose change `df70a0369` this pass read as a diff. HEAD contradicts none of them. Round 2's *Not judged* row on whether owlery release 0.1.0 is still open leaves `changelog.md:3` and `seal/follow-up.md:49` true either way, since each states the count as #1632's comment made it on 2026-11-27. The other places across the tree that state R6 were listed by the finding 1 search `git grep -n -F 'own commit'`, a sample under contract rules 12 and 19, and a statement of R6 in other words stands outside it.
```

## Confirmations

```seal
confirms: round-1#1
```
What holds: rule 19 at `skills/agent-contract/SKILL.md:228-231` now keeps a value of "a published release" and says "a release still open is no such moment". It stays one sentence for a count, a universal and a value. R4 at `frame/design.md:80`, `changelog.md:3` and the process row at `changelog.md:12` say the same (read). Executed: the finding's search at `d22e62cf7` printed `frame/design.md:12` and `:134`, which quote the old sentence in a dated *Grounding* row and in *Removes*, and round 1's lines 16 and 19. The crafter claimed it reworded the count at `changelog.md:3` and in the `seal/follow-up.md:49` row because release 0.1.0 was open. Executed: `gh issue view 1632 --json comments` prints one comment, created 2026-11-27T00:59:34Z, which counts "so far" and gives "12 transitional (stale after a release was renamed, merged or tagged)" of 120 findings. Each reworded line states the count as that comment's on that date, a dated measurement R4 keeps. `frame/questions.md:16` and `frame/design.md:15` state the count as the comment's, in a question and in a dated *Grounding* row, and stand. Whether owlery release 0.1.0 is still open is unverified, because it is another repository's state: the comment's "so far" is the reading this round took.

```seal
confirms: round-1#2
```
What holds: the sentence at `skills/agent-contract/SKILL.md:234-237` keeps the fragment line "The version moves to" a number. Executed: the finding's search at `d22e62cf7` prints that line in each `changelog.md` that carries a move, from `1794465688-feature-prs-wait-on-the-macos-runner` to `1795736973-the-preflight-passes-where-a-round-is-owed`. For the last one, executed: `git show --stat 68bb3d5a9 -- .claude-plugin/plugin.json` shows that the item's own squash changed the version file, so its line states a value its own commit wrote. The close holds. This round's finding 1 is about the wording of that same sentence, not about whether it keeps the line.

```seal
confirms: round-1#3
```
What holds: `frame/design.md:50`, `frame/plan.md:16` and `frame/plan.md:27` each tie what the other work item changes to its frame at `762f284f7` and name *Scope* items 4 and 5, or item 6. Executed: `git show 762f284f7:` of that frame prints items 4, 5 and 6 on those files, and none of its items names `skills/implement/fold-and-reframe.md`. The crafter claimed it made no edit for this finding. Executed: `git show --name-only` of `535a2a33e` and `7991077ec` names no frame file, and `665fcf9f2` and `941e217a4` touch the frame files alone. Executed: the finding's search printed `frame/plan.md:27`, now dated, and round 1's lines. `frame/plan.md:53`, the row `941e217a4` corrected, names `762f284f7` as the commit those sentences cite (read).

What matched: `gaps.md:9` asks the proofer, in round 2, whether rule 19's new paragraph states clauses R1 to R6, and whether the placeholders read one way. The paragraph at `skills/agent-contract/SKILL.md:215-237` holds R1 at `:215-221` with the examples and the prediction, R2 at `:221-224`, R3 at `:224-228`, R4 at `:228-231`, R5 at `:231-234` and R6 at `:234-237`. The sentence on the rule's reach comes last (read). The three placeholders, at `templates/records/sdd-routing.md:16`, `templates/records/sdd-plan.md:23` and `templates/records/sdd-plan.md:31`, read one way on their own. Each agrees with the rule once R6 says "has written", as finding 1 asks. The row stays open: closing it is not this record's write.

What matched: the crafter's claim that no case pins a sentence of rule 19. Executed: `git grep -n -F` over `tests` for five phrases of the new heading and paragraph printed only `tests/behaviour/test_release_hygiene.py:254`, a docstring about another fact. That search is a sample. The fix adds no citation that the `RULES` row reads, so no case is owed (contract rule 15).

What matched: the crafter declined to edit `trail/phases/phase-1.md:9` ("R1 to R5"). `skills/implement/fix-pass.md:128` says a fix pass "writes no phase record", and `:147` says "The build's phases keep their records" (read). The phase record is the account of the phase closed at `a96ec2237`, when the frame held five clauses. `agents/proofer.md` reads `trail/phases/` apart from the records that state the present. So the line stands, and no finding is opened on it.

What matched, record against another work item's frame: the only unsettled `add` on `docs/running/the-agent-set.md` *One contract every agent receives, and one definition each* other than this one is #1613's (`seal/threads/1795569535-a-fix-writes-a-count-into-a-record/frame/design.md:95-111`, read). It states no exemption for a named moment, so the narrowed moment contradicts nothing the settle will write beside it.

What matched, R4 and R6 over this release's own records. This work item: `routing.md:16` and `:24`, `frame/design.md` G5, G7, G17, G19 and G20, `frame/plan.md:38` and `:47`, `changelog.md:3` and `:12`, and the `seal/follow-up.md:49` row. Each names a moment, a role or a decision (read), apart from G7's conclusion (finding 2). `pr.md:1` quotes `frame/plan.md:47` word for word. The release's first item, `1795736973-the-preflight-passes-where-a-round-is-owed`, has a `frame/plan.md:36` that says "`origin/release/v0.39.2` stands at `e65830869`". R1 refuses that sentence. R4 does not keep it, because the commit is the ref's value and not a moment the sentence names. It is false at `d22e62cf7`'s date, and this item's *Scope*, Out leaves it, since rule 19 binds what a change writes from here on. That record is another work item's, and no finding is opened on it here.

What matched: the narrow modules of the plan's *Verified by* cell pass at the target, with `tests/behaviour/test_docs_line_wrap.py` beside them (executed, see `## Probes`). `gaps.md:7` labels the broad gate unverified and names the orchestrator, which is honest, since the fix range ran no repository-wide lint.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the format check, run once at the settled HEAD | `seal/config.json` `Broad gate` | the orchestrator's broad run |
| Whether the next release counts fewer findings of this class than #1632's comment counted | `seal/follow-up.md:49`, `frame/questions.md` Q1 | the repository owner |
| Whether owlery release 0.1.0 is still open, which the crafter's rewording of the count assumed | `changelog.md:3`, `seal/follow-up.md:49` | the repository owner |

## Probes

| Command | Result |
|---|---|
| `bin/test -q tests/text/test_the_rules_have_one_owner.py tests/text/test_the_agent_contract_holds_the_universal_rules.py tests/text/test_every_agent_reads_the_contract.py tests/text/test_no_passage_is_pasted_into_a_second_file.py tests/behaviour/test_the_set_a_work_item_always_has.py tests/behaviour/test_waiver_decided_at_start.py tests/lib/test_routing.py tests/behaviour/test_docs_line_wrap.py` | 247 passed, exit 0, at `d22e62cf7` |
| `python3 -I skills/code-review/scripts/chain_check.py --baseline 68bb3d5a9 --root <worktree> --worktree`, before this record | exit 0, and it reported that a verifying round was owed for findings 1 and 2 and for `535a2a33e`. It printed no notice at a line of `frame/design.md` naming a test pin or a copy |
