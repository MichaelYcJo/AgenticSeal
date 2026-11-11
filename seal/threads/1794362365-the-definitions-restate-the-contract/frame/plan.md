# Implementation Plan: 1794362365-the-definitions-restate-the-contract

## Technical context

The tree as read at `0eaaad4e1`.

The work is text an agent preloads or opens: the contract, the agent definitions, the skill files and the READMEs `frame/design.md` *Scope* names, and one test module. `frame/design.md` *Grounding* holds each sentence's coordinate (G5 to G12), the pins that read them (G13), and the sizes and the census before the work and with its texts in place (G16 to G18). *Data & interfaces* holds each text as it will stand.

Three constraints bind the build.

- **The paste check reads every definition against every contract section.** `tests/text/test_a_moved_rule_leaves_its_definition.py#test_no_definition_carries_a_sections_own_sentences` fails where a definition shares a run of `passages.py#WINDOW` words with a section, and `#test_the_window_sits_between_what_was_measured` fails where the widest shared run passes 10 words. The scratch reason moves from the definitions into rule 17, so the definitions' sentences and rule 17 change in one commit; between two commits the reason would stand in both or in neither. With the texts in place the widest run is 10 words, the sealer's with rule 15, as at HEAD (`frame/design.md` G17).
- **A contract rule keeps its number.** Rule 17 is rewritten in place and no number is added or retired, so the preamble's list of retired numbers and `tests/text/test_the_agent_contract_holds_the_universal_rules.py` stand as they are.
- **The pins stay green on the texts as written** (`frame/design.md` G13). The one module whose cases change is the scratch module (`frame/design.md` *Scope* item 11).

What breaks in six months, for the approach chosen:

- **A narrowing was read as a copy and deleted.** #1474 names this loss. The sentences this plan removes whole are the crafter rules `frame/design.md` *Removes* names and the proofer's *Never* bullet. Each row there names the sentence that keeps the fact. The signal that one was a narrowing after all is a crafter that guesses a rung where the frame is absent, a phase record that omits a departure from the frame, or a hand-back with no label on the suite, and a proofer or the sealer reads each of those.
- **A standing directory is reused.** Rule 17 tells an agent to take the next free name, and nothing checks that it did. An agent that works in an earlier spawn's clone reviews or re-runs an old commit. The round record's `target:` line and the sealer's `<sha> against <base>` name the commit, so a mismatch shows at the pull request check, after the round is spent.
- **An agent removes from habit.** The texts no longer ask for a removal and rule 17 forbids one, and an agent can still write an `rm` on a variable path at its hand-back. Rule 21's `rm` sentence stays for that command. `frame/questions.md` Q2 holds the measurement.
- **The scratchpad fills.** Every clone of a session stays until the scratchpad goes: one per review round, one per audit, one per framer probe that runs the repository's code. #1503 accepts this loss. `frame/questions.md` Q1 holds what is not verified.
- **The contract is larger.** It grows by 455 B (`frame/design.md` G17), so a framer, a proofer, a sealer and a tracer each preload more than before, and only the crafter less (*Operational impact*). A later item that adds to rule 17 pays that on every spawn.
- **The policy paragraph is stale until the settle.** `docs/running/the-agent-set.md:140-142` says the name lives in the definitions until the settle writes the operation of `frame/design.md` *Rule changes*.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. Rule 17 states the scratch rule once and forbids the removal; each definition names its directory and cites rule 17; rule 7 keeps what stands under the scratch directory; every copy of rules 2 to 5 becomes a citation or a narrowing; the crafter's inner repeats and the sealer's go | The failures *Technical context* names | Chosen. It meets both issues' *Done when* (`frame/design.md` S1 to S6), and the reason for the name stands in one file every agent receives |
| 2. Keep the structure: each definition keeps its own scratch statement, and only the removal sentences go, which is all #1503 asks | The shared-scratchpad reason stays in each definition that states it, the tracer still has no directory (`frame/design.md` G7), and the sentence on a standing directory, which the removal's end makes necessary (`frame/design.md` G15), would be written into each definition that clones. #1474's *Change* asks for the rule once, in the contract | Rejected. The premise that would keep the structure is that a rule in each definition costs fewer preloaded bytes than one in the contract. Checked: it does for a framer, a proofer and a tracer, by the 455 B of `frame/design.md` G17, and the crafter's preload falls by more than that. The owner's issue chose the contract, and the tracer's missing directory is the class #544, #1047 and #1445 each closed for one agent |
| 3. A new rule 22 holds the scratch rule, and rule 17 keeps the processes | Every agent preloads one more heading, rule 17 is left with two sentences, and the two rules give one reason twice: another agent's file, or another session's process, answers to the same name | Rejected. Rule 17 is rewritten in place |
| 4. Each definition names the bare leaf, `phase-<n>`, `round-<n>`, `frame`, `at-base`, as #1474's *Change* words it | The spellings the scratch module pins would change, and #1503's *Done when* asks that those sentences stand and their case stay green. An agent would also assemble its path from two files. The bare leaf saves about 30 B a definition | Rejected. Each definition holds the whole path and cites rule 17 (`frame/design.md` T8, T11, T19, T21) |
| 5. Move the runner clause the crafter and the proofer share into contract rule 2 | A framer and a tracer run no test and would preload it. The contract would grow by about 120 B on every spawn to take about 240 B out of the crafter's and the proofer's. The proofer's rule carries a fallback of its own, the `uv` venv in its clone, and each definition pins a different sentence on a coverage probe (`frame/design.md` G9) | Rejected. Each rule is that agent's narrowing of rule 2, and `tests/behaviour/test_the_suite_has_a_command_that_is_cheap_twice.py:360-369` holds that both carry the generic shape. Both keep their text |
| 6. Move the definition of a test's group into one file the crafter and the proofer both open | No such file stands: the crafter opens `skills/implement/SKILL.md` and the proofer `skills/code-review/SKILL.md` (`frame/design.md` G10). Moved into both skills, the definition still stands twice, in files a session reads too. Moved into the contract, the agents that neither write nor review a test preload it | Rejected. The crafter's rule says what a builder does with a new case and the proofer's what a reviewer finds, and each is that agent's own. Both keep their text |
| 7. Leave rule 7, the proofer's probe rule and `skills/code-review/SKILL.md` as they are, since #1503's *Change* names none of them | Rule 7 lists "a scratch clone" among what goes, and the proofer's rule has "everything it made" in the clone gone, so a proofer still writes an `rm` under its scratch directory at each hand-back. #1503's *Done when* reads every hit of a search over `agents/` and `skills/` (`frame/design.md` G8) | Rejected. T1, T14 and T23 |
| 8. Where a scratch directory already stands, reuse it, or name the leaf after the commit | Reuse needs the clone reset first, with `git reset --hard` or an `rm`, which are the destructive forms the removal's end is meant to spare, and a capture left by the earlier spawn reads as current. A leaf named after the commit still collides for two spawns at one commit, and each definition that clones would need the rule | Rejected. The agent leaves the directory and adds `-2` to the leaf, or the next number free (`frame/design.md` T2) |
| 9. Give rule 17 the `check:` target rule 21 loses | #1475 deletes every `check:` line of the preloaded files as the release's last item, by the owner's decision, so the line would ride in every preload for one work item | Rejected. The target leaves rule 21's line, and the crafter's, the proofer's and the framer's rules keep naming the module until #1475 |
| 10. Drop rule 17's ban on a glob delete with the file removal | The ban orders no removal. An `rm` an agent still runs, such as rule 7's deletion of a probe in a working tree, can take another session's file in a shared directory | Rejected. T2 keeps the ban in one sentence |
| 11. Keep the crafter's rule *Each phase closes with its record* | Removing it leaves the crafter's preload without "every departure from the frame among it". The crafter opens `skills/implement/SKILL.md` at step 1, whose *3. The SDD file set* holds the sentence, and step 8 starts the record from `templates/records/sdd-phase.md`, whose one section asks for "each departure from the frame" (read) | Rejected: the rule goes. The premise that would keep it, that no text the crafter opens at that step says what the record holds, does not hold |
| 12. Keep the sealer's description as it is | Cut too far, the session that chooses an agent no longer reads when the sealer may be spawned | Rejected. T15 keeps what comes before the spawn and drops the list of the sealer's own steps, which its *Order of work* holds |
| 13. Add a case for each narrowing a rewrite keeps | Each would pin wording: `docs/running/what-a-script-gates.md` *The checks* keeps a case for a fact a reader acts on. Most of the narrowings are pinned already (`frame/design.md` G13), and a case added at a rewrite has caught nothing on the day it lands | Rejected. The review reads `frame/design.md` S3 |
| 14. Two phases, the texts and then the measurement | A second spawn would preload 33 KB to run the measurement and write the records. The measurement reads the last code commit, which the one phase makes | Rejected. One phase |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | `frame/design.md` *Scope* items 1 to 14: items 1 to 12 in one commit, so that no sentence stands in two files or in none between commits, then the measurement of item 13 and the records | S1 to S11 of `frame/design.md`; each changed or added clause of *Scope* item 11 seen red as that item says; the narrow run of S10 | |

## Overlap with the release

The spawn names #1480 and #1475 as the release's other open items. Neither has a branch or a frame (`frame/design.md` G24), so each is read from its issue.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1480 | `agents/framer.md`: #1480 rewrites step 5 (`:96-103`) and folds a few checks into the definition, and this work changes the rules at `:149-151` and `:156-165`. `README.md`: #1480 changes `:282`, and this work `:377-378`. #1480 also removes two skills, which are files of the census's corpus, and it adds bytes to one of the definitions S1 sums | this work | The orchestrator runs the release's items one after another, and #1480 has no branch or frame, so this work is sealed and merged before #1480 is built (*Judgments of the run*, row 1). Neither item edits a section the other edits, so #1480 integrates this work's edits of `agents/framer.md` and `README.md` without a hand edit. #1480's removal of two skills and its bytes in `agents/framer.md` land after this work's measurement, so the "before" of S1 and of the census stays `9c6907942` |
| #1475 | The preloaded files: #1475 deletes every `check:` line of the contract and of every definition. This work removes the second target of rule 21's line, removes one whole line with the crafter's rule *Each phase closes with its record*, and rewrites rules whose lines it keeps | this work | #1475's issue puts it last of the agent items because it touches every definition. Its deletions are whole lines, so it integrates nothing of this work by hand, and its count of the lines is taken after this merge. S1 is measured before #1475 takes its bytes out |

## Operational impact

None for a deployer: no migration, environment variable, dependency or compatibility break. The pull request moves no version, because the release's move to 0.37.3 landed with #1471 (`frame/design.md` G25).

After the release, a spawn preloads the core, the contract and its definition as follows (executed, the probe of `frame/design.md` G17): a crafter 32,327 B, 770 B less; a framer 36,965 B, 333 B more; a proofer 32,904 B, 219 B more; a sealer 33,175 B, 35 B more; a tracer 25,035 B, 455 B more.

A session's scratchpad keeps every agent's scratch directory until the scratchpad itself goes. A user who watched the directory empty after each hand-back will see it grow, one clone per review round and per audit.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| 2026-11-11 | This work item merges into `release/v0.37.3` before #1480, and #1480 is built on the release after this merge | The orchestrator runs the release's items one after another, and #1480 has no branch or frame yet, so this item is sealed first. #1480 then measures and builds on a release that holds this item's edits of `agents/framer.md` and `README.md`, and this item's "before" stays `9c6907942` | `skills/implement/merge-order.md` *Orchestrator: the order the work items of a release merge in* |
