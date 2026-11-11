# Implementation Plan: 1794358502-a-fix-owes-its-diff-in-five-places

## Technical context

The tree as read at `ebe6ceed3`.

Contract rule 12 (`skills/agent-contract/SKILL.md:141-164`) is two rules in one section. R1 to R4 bind every party that fixes anything: count the class by a method that makes the list whole. R5 to R11 define what one party, the one that fixes inside a work item, reads whole, and tell the proofer how to read that party's account (`frame/design.md` G4). The crafter's rule at `agents/crafter.md:178-200` states the same reading with the files named, and points back at rule 12 for the one thing it does not say, why the set is closed (`frame/design.md` G6). Every spawn of every agent preloads both halves of rule 12.

The work is an edit of sentences in the files `frame/design.md` *Scope* items 1 to 6 name, and of the pins item 7 names. `frame/design.md` *Data & interfaces* gives each replacement text, T1 to T5.

Three constraints bind the build.

- **The byte margin is 22 B.** T1 and T2 leave the contract at 12,364 B against S1's bound of 12,386 B (`frame/design.md` G11, S1). Words a round adds to either text spend that margin, and a reflow does not.
- **Three pins turn red with their sentences.** They are the clause at `tests/text/test_a_moved_rule_leaves_its_definition.py:491` and the clauses at `tests/text/test_the_rules_have_one_owner.py:589-594` and `:716-718` (`frame/design.md` G12). Each case reads its text with whitespace collapsed, so a clause is the sentence as it stands, not as it wraps.
- **A moved sentence must not stay behind.** `test_no_definition_carries_a_sections_own_sentences` fails where a definition and a contract section share a run of `WINDOW` words, so T3b and T5 enter the definitions in the same commit that takes R10 and R11 out of the contract.

One statement in the unit the phase edits is already false at this commit. The docstring of the crafter's case says "the five files that state the present" (`tests/text/test_a_moved_rule_leaves_its_definition.py:469`), and the rule names `routing.md`, the three frame files, `gaps.md` and `changelog.md` (`agents/crafter.md:182-183`). The phase edits that case, so the docstring is in its range.

What breaks in six months. First, a party that fixes without the crafter's definition no longer reads, in so many words, that its own diff and the work item's records are a closed set. Two such parties exist: a session that runs a fix pass where `routing.md` names no crafter, and the orchestrator writing a fix after the last round (`skills/code-review/orchestration.md:60-65`). Rule 12 still binds both where they loaded the contract: the fix is owed to every instance, the second method takes an artefact apart into every part, and T1 lets a list stay a sample only where no method makes it whole, which a party's own diff never is. The signal is a `regression:` finding located in the diff or the records of a commit no crafter wrote; `frame/questions.md` Q1 names how that is read. Second, a proofer under the new definition does not connect T5 with the account it is handed, because the account reaches it in the spawn prompt and the orchestrator's file, not the proofer's, says the round reads it as a claim (`skills/code-review/orchestration.md:73-74`). The signal is a round record that confirms a `fixed` close and says nothing of the method where a later round finds a statement in the same fix's diff.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. The closed set is defined in the crafter's rule alone; rule 12 keeps the class, the methods and the sample; the proofer's half of R11 becomes one sentence of its own rule; the citations of `frame/design.md` *Scope* items 5 and 6 name the second method | The failures *Technical context* names | Chosen. It meets both lines of the issue's *Done when* (`frame/design.md` S1, S4, S5), and each party keeps in its preload only the sentences it acts on (`frame/design.md` G1) |
| 2. Keep the structure: rule 12 keeps R5 to R11, and the crafter's rule shrinks to a citation of rule 12 | The contract does not shrink, so a tracer, a sealer and a first-frame framer keep preloading about 0.8 KB that none of them acts on. Rule 12 binds every agent and cannot name the crafter's files, its Status cell or the orchestrator as the party that folds, which is why #1318 gave the crafter a rule of its own (`frame/design.md` G14) | Rejected. The premise that would keep the structure is that every agent acts on R5 to R11. It was read against each definition's *Job*: the tracer writes nothing durable, the sealer writes `guarantee.md` and fixes nothing, and a first-frame framer has no diff of its own to read |
| 3. Rule 19 cites `agents/crafter.md` for the closed set, as the issue's *Change* words it | Rule 19 states nothing of the closed set at this commit (`frame/design.md` G5), so the citation would be a new sentence in every agent's preload, naming a file only the crafter preloads, and it would take more bytes than S1's margin holds. The contract holds what is true of every agent (`frame/design.md` G3) | Rejected. Rule 19's third sentence becomes a citation of rule 12 (T2), which is the restatement the rule did hold |
| 4. Move the crafter's rule into a file the crafter opens at its hand-back, as #1471 moved the fix pass | A phase and a fix pass both end with a hand-back, so every crafter spawn would open the file. The move would add a read and remove no preloaded byte that some spawn does not use | Rejected |
| 5. One new file states the closed set, and the crafter, the orchestrator and the framer cite it | The three parties read three different sets: the crafter its range and the files `agents/crafter.md:182-183` names, the orchestrator its fold commit and every record that states the present, the framer its three files. Each already states its own set at the step where it acts (`frame/design.md` G8), so the file would hold one sentence in common and cost each party a read | Rejected |
| 6. Keep R11 in the contract, or put the proofer's sentence in `agents/proofer.md` *The implementer's account is a claim* | Kept in the contract, every other agent preloads a sentence addressed to the proofer. Put in *The implementer's account is a claim*, it stands in the rule #1474 reduces to a citation of contract rule 5, where the issue itself warns of "a narrowing read as a copy and deleted" (`frame/design.md` G20) | Rejected. T5 goes into the rule on the records, which names the reading the account is checked against and which #1474 does not name |
| 7. Leave the proofer's rule naming the records a second time | A proofer's preload then holds the list twice, in step 3 and in the rule, and the first line of the issue's *Done when* reads "once across all preloaded files" | Rejected. T4 cites step 3 |
| 8. Turn the crafter's and the proofer's sentences on a dated frame section into citations of `skills/implement/SKILL.md` *Document layout — two roots, three lifetimes* | The proofer does not open that file (`frame/design.md` G7). #1477 wrote both sentences one release ago, after a round was told the target does not contradict a stale conclusion (`frame/design.md` G15), and a bare citation makes the crafter judge at its hand-back from a section it read at step 1 | Rejected, and out of scope |
| 9. Copy R6 into the crafter's rule | The crafter's rule names the files it reads one by one, and neither a phase record nor a round record is among them, so the sentence would guard against a reading the rule does not ask for. Its source is the section the rule already cites (`frame/design.md` G9) | Rejected |
| 10. Reword `skills/implement/fix-pass.md:47-49` so that every fix pass, a session's too, makes the reading `agents/crafter.md` asks for | #1471 wrote "A crafter then makes the reading" one work item ago. The crafter's rule speaks of "your *Job*" and of naming a frame statement "for the orchestrator to fold", and a session that builds writes the frame itself. Rule 12 still binds that session (*Technical context*, first failure) | Rejected. `frame/questions.md` Q1 holds the measurement that would reopen it |
| 11. Add a case asserting that rule 12 holds none of the moved phrases | A paste of T3 or T5 back into the contract already turns `test_no_definition_carries_a_sections_own_sentences` red (`frame/design.md` G12). A list of phrases the contract may not hold would pin wording (`frame/design.md` G13) and has caught nothing on the day it is added | Rejected. S2 is read by `git grep` at review |
| 12. Add no clause for T5 | #1474 rewrites `agents/proofer.md` next, and its issue names the loss of a narrowing read as a copy. Rule 12 had no case, so R11 arrives in the proofer's file with nothing behind it | Rejected. One clause pins the fact (`frame/design.md` *Scope* item 7) |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 8, in one commit for items 1 to 7 so that no sentence stands in two files between commits | S1 to S8 of `frame/design.md`; each changed or added clause seen red with its sentence deleted; the narrow run of S7 | `3acdc8065` |

## Overlap with the release

The spawn names #1474 with #1503, #1480 and #1475 as the release's other open items, and none has a branch or a frame yet (`frame/design.md` G20), so each is read from its issue. #1480 does not meet this work: it edits `agents/framer.md` and removes two skills, and this work edits neither (`frame/design.md` *Scope* item 10).

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1474 with #1503 | `agents/crafter.md`, `agents/proofer.md` and `skills/agent-contract/SKILL.md`. This work changes the crafter's rule *Before you hand back…*, the proofer's rule *Every round reads…* and contract rules 12 and 19. #1474 names other sentences of the same files: step 10, the scratch, runner and test-group rules, the proofer's *The implementer's account is a claim*, and contract rules 17 and 21 | #1472 | The milestone states this order. #1474's *Done when* measures the four definitions before and after, and this work adds about 112 B to the crafter's and about 218 B to the proofer's (`frame/design.md` G11), so #1474 takes its "before" after this merge. Its framer then reads T3b and T5 as narrowings that stay, each with a clause behind it |
| #1475 | The same three files: #1475 deletes their `check:` lines, the one under the crafter's rule this work edits among them, and weighs the crafter's clause "and by its `check:` target", which this work leaves (`frame/design.md` *Out*) | #1472 | The milestone puts #1475 last because it touches every definition. Its deletions are whole lines this work does not edit, so the later item integrates nothing of this one by hand |

## Operational impact

None for a deployer: no migration, environment variable, dependency or compatibility break. The pull request moves no version, because the release's move to 0.37.3 landed with #1471 (`frame/design.md` G21). Every agent spawned after the release preloads 822 B less of the contract; a crafter's definition grows by about 112 B and a proofer's by about 218 B (`frame/design.md` G11).

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | The issue's "at least 0.8 KB smaller" reads as 800 B, so S1 bounds the contract at 12,386 B or fewer, not 12,366 B | The release reads a KB in a *Done when* as 1,000 B: #1473's "at least 2.3 KB smaller" was met and sealed with 2,348 B (`af923302c`, PR #1514), which the 1,024 B reading would have failed, since it asks for 2,356 B. The 820 B reading left a 2 B margin, so any word a round asks T1 or T2 to take would fail S1 although the issue holds | Issue #1472 *Done when*; `seal/threads/1794352647-a-first-frame-preloads-the-fold-procedure/` as merged at `af923302c` |
| 2026-11-11 | The title takes `refactor:` | The diff moves the definition of the closed set from contract rule 12 into the crafter's rule and the contract's sentence to the proofer into the proofer's rule, and replaces two citations of rule 12 with its second method; what each party does is unchanged, no gate, check or hook is added or removed, and the one case added pins the proofer's moved sentence | `skills/commit-pr-convention/SKILL.md` |
