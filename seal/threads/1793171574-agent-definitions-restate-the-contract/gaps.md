# Overview: 1793171574-agent-definitions-restate-the-contract

## Why this work exists

Five agent definitions restated contract rules 2, 6, 7 and 9 in their own words, so the next change to one of those rules would have left up to five old copies that no check sees; the copies are gone, and each rule has one home.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| The duration key of the removed case | `frame/design.md` *Removes* names the case `test_the_implementer_keeps_the_half_that_makes_the_rule_its_own` and not its key in `.test_durations`. The phase removed the key with the case | the key goes | The spawn prompt names `.test_durations` "if a case is renamed or removed", and a key with no case behind it is a copy of a fact that left |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck at this work item's last commit | executed by the orchestrator's broad gate at `2bad2cef` against `c825fd2c`, passed (`trail/gate.md`), and this repository declares no typecheck (`seal/config.md` *Broad gate*; #951 would add one) |
| closed Three units this phase wrote survive `seal mutate`, so no case reads them: the proofer's `a check rule 2 excludes`, the sealer's lead `A missing or stale gate record earns what step 1 says.`, and the crafter's `the label is step 10's` (`trail/phases/phase-1.md`) | answered by #1111 (work item `1793226630-most-contract-rules-are-proved-by-their-own-wording`, merged in #1146, closed completed): a phrase pin on a rule sentence stops nothing the check exists to stop, so it removed them, and the three units are rule phrases (`agents/proofer.md:139`, `agents/sealer.md:123`, `agents/crafter.md:146`) that are owed no pin |

## Not done

The four glosses `frame/questions.md` head item 3 names stay, on P1's default (a). The owner has not answered P1.

## Fed back into the spec

none
