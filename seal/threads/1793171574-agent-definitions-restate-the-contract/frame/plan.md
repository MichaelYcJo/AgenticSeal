# Implementation Plan: 1793171574-agent-definitions-restate-the-contract

Approved 2026-10-28 by the orchestrator under the owner's automation answer, when `crafter` was spawned.

## Summary

Five agent definitions restate contract rules 2, 6, 7 and 9 in their own
words. This work removes the 13 sentences #1040 lists. Each paragraph that
also narrows a rule for one agent keeps the narrowing and cites the rule by
number. Every test assertion that read a removed sentence is re-pointed at
the narrowing that stays, or removed with its sentence, in the same commit.
The contract and the policy root do not change. One phase builds it.

## Technical context

- **The premise the removal rests on.** Each of the five definitions lists
  `agent-contract` under `skills:` (`agents/crafter.md:8`, `proofer.md:8`,
  `sealer.md:13`, `framer.md:10`, `tracer.md:9`; executed `grep`), and
  `tests/text/test_every_agent_reads_the_contract.py` holds that list and the
  opening sentence for every file under `agents/`. The contract reaches each
  agent before its first tool call, so a definition's copy adds no reader.
- **The homes.** `skills/agent-contract/SKILL.md` rules 2, 6, 7 and 9 (read).
  Rule 2: "no agent runs any of the three", and the orchestrator runs
  `seal gate --base <base> --record <item>`. Rule 6: "four acts are withheld
  from every agent: post nothing, push nothing, open no pull request, and
  spawn no agent". Rule 7: "Probe only what reading cannot settle." Rule 9
  names "a `sed -i`, a redirection or a script". The installed copy at the
  plugin root and the tree's copy are the same file (executed `diff`).
- **The sentences.** `frame/design.md` *Removes*, rows 1 to 12, each with its
  line at `4c90a988`. No agent definition changed between `0b75346f`, where
  #1040 measured, and `4c90a988` (executed `git diff --stat`).
- **The assertions.** `frame/design.md` *Scope*, item 3. They were found by
  `git grep` over `tests/` and `evals/` on the words of each sentence
  (executed). Three read the crafter's paragraph
  (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:883` and
  `:886`, and `tests/text/test_broad_gate_rule.py:139` through the only
  `rule 2` in the crafter). Two read the sealer's
  (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:1007` and
  `tests/behaviour/test_the_sealer_guarantees.py:207`). One case reads the
  crafter's rule 9 bullet
  (`tests/text/test_edits_go_through_the_edit_tool.py:111-123`). No eval
  grader reads a removed sentence (executed `git grep` over `evals/`).
- **What already holds the narrowings.** `tests/text/test_broad_gate_rule.py`
  reads the proofer's label audit (`:288-296`), its `## Not judged` row
  (`:331-339`) and the crafter's hand-back (`:138-157`).
  `tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:846` reads
  what comes due after the proofer's round.
  `tests/behaviour/test_the_sealer_guarantees.py:161` reads the sealer's
  step 1. None of them reads a removed sentence.
- **The verbatim checks.** `tests/text/test_a_moved_rule_leaves_its_definition.py`
  and `tests/text/test_no_passage_is_pasted_into_a_second_file.py` count
  15-word runs. A removal can only lower a count, and the ratchet passes a
  lower count (its docstring, read). A rewritten paragraph is what could
  raise one, and S5 runs both.
- **The failure scenario of the chosen approach: what breaks in six
  months.** The contract stops reaching an agent: a harness or a plugin
  setting blocks `skills:` preload, or a sixth definition ships without the
  list. Before this work, four of the five definitions still said *post
  nothing, push nothing* and three said *no broad gate* on their own. After
  it, an agent without the contract has no such sentence anywhere it reads.
  What stands against that is
  `tests/text/test_every_agent_reads_the_contract.py`, which reads every
  file under `agents/` by glob, and the contract's own `check:` lines. A
  preload blocked at runtime is not something a test in this tree can see
  (`tests/text/test_the_agent_contract_holds_the_universal_rules.py:132`
  names that flag).

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| A. Remove the 13 sentences; keep each narrowing with its rule number; re-point each assertion at the kept narrowing or the citation, or remove it with its sentence | The scenario in *Technical context*: an agent the contract does not reach meets no prohibition in its definition. A re-pointed assertion pins a phrase, which #1111 may then remove | **chosen**: one source for each rule, as `docs/the-record-layout.md` and `docs/the-agent-set.md` require, and every changed assertion still reads something the definition keeps |
| B. Keep the structure: leave the sentences where they are | The next change to rule 2 or rule 6 leaves up to five definitions stating the old rule, and the 15-word check passes all of them, as it passes these 13 today (#1040, executed by its author). #969 is the precedent: it moved the broad run, and the sealer's definition carried the contradiction until #120 closed it (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:964-1010`, read). The premise that would keep the copies, that an agent might not receive the contract, is false for every definition in the tree (S6) | rejected |
| C. Replace the structure: definitions say nothing of a universal rule, citations included | The narrowings lose their anchor. A crafter reading `failing on base too` cannot tell which rule makes a broad gate failure someone else's run. `"rule 2" in crafter` (`tests/text/test_broad_gate_rule.py:139`) and `"rule 2" in text` for the sealer (`tests/behaviour/test_the_seal_is_taken_once_by_the_sealer.py:996`) fail, and #1040's *Done when* asks for the citation | rejected |
| D. Replace the structure: move each narrowing into the contract as a clause for one agent | `docs/the-agent-set.md` *One contract every agent receives, and one definition each*: "A rule that would need a per-role exception is not universal". Every agent would carry four other agents' instructions on every spawn | rejected |
| E. Turn each removed assertion into an absence assertion on the removed sentence | It pins one spelling. A restatement comes back in other words and passes, which is the verbatim-versus-paraphrase argument `tests/text/test_no_passage_is_pasted_into_a_second_file.py` makes. It adds phrase pins in the work #1111 runs to reduce them, and `CLAUDE.md` says a check guessed from words is a report | rejected |
| F. Two phases: the rule 2 paragraphs first, then the rules 6, 7 and 9 bullets | A second crafter spawn and a second review slice for about 20 changed lines. The two groups share no file in the tests and no order between them | rejected; one phase |

## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | The 13 sentences of `frame/design.md` *Removes* rows 1 to 12 gone from `agents/crafter.md`, `proofer.md`, `sealer.md`, `framer.md` and `tracer.md`; each narrowing of *Scope* item 2 kept and citing its rule; each assertion of *Scope* item 3 re-pointed or removed, with the two docstrings rewritten in place; `changelog.md` written for this work item | S1 by the whitespace-collapsed search, its phrases found at `4c90a988` first; S3 by `seal mutate` over each sentence a re-pointed assertion reads, seen red; S2, S4, S5 and S6 green through `bin/test`, one module per call, the modules S4 names. The suite is labelled `unverified`, its answerer the orchestrator (contract rule 2) | 3eecf8a0 |

## Operational impact

None. No migration, environment variable, dependency or compatibility
break. A plugin user's agents read shorter definitions. Each removed
sentence still reaches them through the contract, which every definition
preloads, so no agent's permitted acts change. The changelog fragment says
so.
