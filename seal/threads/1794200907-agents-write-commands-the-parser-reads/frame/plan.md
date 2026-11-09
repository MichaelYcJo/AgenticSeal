# Implementation Plan: 1794200907-agents-write-commands-the-parser-reads

## Technical context

The tree as read at `bdac7850`.

- `skills/agent-contract/SKILL.md` holds rules 1 to 19, with 8, 16 and 20 retired, and rule 19 ends the file at line 214. Rule 21 goes after it.
- `tests/text/test_the_agent_contract_holds_the_universal_rules.py:54-63` is `FACTS`, with entries for rules 1 and 11. The docstring at lines 22-27 says "Two facts are pinned" and names both. `test_each_section_holds_its_rule` and `test_deleting_a_pinned_phrase_is_caught` are parametrized over `FACTS`, so a new entry needs no new case function.
- `skills/update/SKILL.md:97` sets `f=$(mktemp)`, and line 117 removes it with `rm -f "$f"`. No test pins either line (`git grep`, executed).
- `skills/implement/orchestration.md:28-32`, step 1 of *Orchestrator: the order inside a ticket*, has the orchestrator hold the core before the first edit and names no other file. The sentence of *Scope* item 5 goes after it.
- `.claude-plugin/plugin.json:4` reads `"version": "0.36.0"`, and no other shipped file names that version (`git grep`, executed).
- The agents of this repository run the installed plugin's contract, the last release's. Rule 21 reaches them after 0.37.0 is released and installed, and reaches a user's agents at their next update.

The chosen approach's failure scenario, six months out: Claude Code changes which forms its parser refuses. It may start to ask about `$(cat list)`, or stop accepting `"${VAR:?}"`. Rule 21's examples then teach a form that prompts, and nothing in the tree notices, because no check reads an agent's command (`frame/design.md` G2). What limits the damage is the rule's own wording: it states the aim, a command the parser reads, and gives the forms as examples, so an agent that meets the prompt has the aim to rewrite against. A second scenario is that agents do not follow a rule they hold in text. The prompts then recur, and the reading `frame/questions.md` Q1 asks for is what shows it.

## Alternatives considered

| Approach | Failure scenario | Verdict |
|---|---|---|
| 1. A new contract rule 21 that states the aim, with the zsh forms and the `rm` forms as examples, and the right forms pinned as rule 1's are | Claude Code's judgment moves and an example goes stale (see *Technical context*) | Chosen. The contract reaches every agent in every repository by the `skills:` list (`docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*), and the rule has a number a spawn prompt or a round record can cite. |
| 2. One sentence beside rule 10, as the issue names as the likely home | Rule 10 is about batching. The `rm` form the comment adds has nothing to do with batching, so the sentence would either leave it out or make rule 10 hold two subjects, and a reader looking for how to remove a directory would not look under batching. | Rejected. The list form starts in rule 10's demand (`frame/design.md` G3), so rule 21 sits right after it in a reader's path, under its own number. |
| 3. A line in the spawn prompts, as this repository's orchestrator already writes | No shipped orchestration text carries the line (`frame/design.md` G5), so an orchestrator in a user's repository never writes it, and the prompts this work answers came from such a repository. A rule kept in spawn prompts "goes missing without a trace" (`docs/running/the-agent-set.md` *One contract every agent receives, and one definition each*). | Rejected |
| 4. Remove the cause of the cleanup `rm`: rule 7 stops asking an agent to remove what it made under the scratchpad, and the sealer's "Remove the clone once its runs are done" leaves, as the issue's comment proposes. This replaces the structure, and is weighed as the equal of keeping it. | The harness does not clear a scratchpad when its session ends, and the operating system clears it only at boot (`frame/design.md` G12). A `--no-local` clone copies the whole object store, 128.81 MiB of packs in the repository where the prompts arose, so a release's worth of rounds and seals left in place can reach gigabytes. A sealer spawned again for the same work item meets its predecessor's clone at `<scratchpad>/<work-item-id>/at-base/`, cannot clone there, and may not remove it (rule 17). Fixing that needs a new naming rule for each agent's scratch directory, a mechanism added to remove one. Rule 21 is still needed for the zsh forms and for the removals that are not cleanup (G9), so this alternative does not save the rule agents must remember. | Rejected. The premise that keeps the structure, that the cleanup can be written in a form the parser reads, was checked: this framing's own `rm -rf "${D:?}/clone"` ran with no prompt, and every guarded `rm` in the transcripts since 2026-10-20 was accepted (`frame/design.md` G10). One removal of the directory also replaces the file-by-file loops that made most of the cleanup prompts (G9). |
| 5. Remove only the small scratch files' cleanup and keep the clone's | Agents must tell a small file from a clone each time, a distinction no reader can check, and the loops it would remove are already replaced by one removal of the directory | Rejected |
| 6. A check: a hook or script that reads an agent's command before it runs | It re-encodes Claude Code's judgment, refuses what the parser reads or passes what it refuses, and brings back the `PreToolUse` gates #1416 and #1430 removed | Rejected (`skills/core/SKILL.md` *The rule a mechanism is kept against*, and the issue's *Done when*) |
| 7. Change nothing, and treat the prompts as the cost of automation | The prompts the reading counts recur in every run that batches a list in zsh or cleans up in a loop (`frame/design.md` G8, G9) | Rejected (`skills/core/SKILL.md` *Asking a person is the most expensive step*) |
| 8. Add text for heredocs, a `cd` before git, `sed -i` and history rewrites as well | None of them prompted a person on its own after 2026-10-20 (`frame/design.md` G9), and rule 9 and `skills/implement/SKILL.md` *A commit names its repository in the command that makes it* already hold them | Rejected. The rule's aim covers them as it covers every form, without naming them. |
| 9. Rule 21 in the contract alone, reaching the orchestrator only where it chooses to open the contract (this frame's first version) | The orchestrator writes the commits, the broad run and its own cleanup under automation, and nothing has it open the contract (`frame/design.md` G17). Its commands prompted in the 0.36.0 run (G8), and would go on prompting. | Rejected on the orchestrator's reading of the frame, agreed with a change: *Scope* item 5 points the orchestrator at rule 21 from step 1 of `skills/implement/orchestration.md`. |
| 10. The rule's aim stated in `skills/core/SKILL.md`, which every party receives, with rule 21 holding the examples | The core is paid on every spawn and every session, and every agent already receives rule 21 through the contract. Only the orchestrator lacks it, so the core would carry a sentence for one party's gap, and the rule would stand in two files that a later edit can set apart. | Rejected. The gap is the orchestrator's, so it is closed in the file the orchestrator opens before its first edit (`skills/core/SKILL.md` *A document is cut by who opens it and at which step, so a party opens only what its step needs*). |
## Phases

| Phase | Delivers | Verified by | Status |
|---|---|---|---|
| 1 | *Scope* items 1, 2, 3, 4 and 5 | The entry for 21 in `FACTS` seen red before rule 21 is written, then green. Then the phase boundary set of `skills/verify/SKILL.md` *Scope: cheap and often, broad and once* in one command, which holds at least `tests/text/test_the_agent_contract_holds_the_universal_rules.py`, `tests/text/test_every_agent_reads_the_contract.py`, `tests/text/test_a_moved_rule_leaves_its_definition.py`, `tests/behaviour/test_docs_line_wrap.py` and `tests/behaviour/test_a_cited_section_stands_in_its_file.py` | df508485 |

## Overlap with the release

Both other items' frames held only their skeletons when this frame was written, so each row reads the item's issue and the spawn's description of it.

| Work item | Where both change | Merges first | Grounds |
|---|---|---|---|
| #1059, a second records root `agentic-seal/` | `skills/agent-contract/SKILL.md`: #1059 changes rule 11, which states where the `seal/` root resolves, and this work adds rule 21 after rule 19. `tests/text/test_the_agent_contract_holds_the_universal_rules.py#FACTS`: #1059 is likely to change entry 11's spellings, and this work adds entry 21 after it. `skills/implement/orchestration.md`: its opening paragraph names where the `seal/` root stands, which #1059 is likely to change, and this work adds one sentence to step 1 of *Orchestrator: the order inside a ticket*. | #1445 | This item carries the version move and is the smaller diff, likely sealed first. The changes sit in different rules, with unchanged lines between them, so #1059 takes the base in with at most a context-only resolution, inside a round it runs anyway. |
| #1454, settings read and written as JSON | `skills/agent-contract/SKILL.md`: rule 11 names `Record language` in `config.md`, which #1454's move to JSON may rename, and this work adds rule 21 and does not touch rule 11. `skills/implement/orchestration.md`: *Orchestrator: what needs a person is asked in one batch, before the first edit* names the language rows of `config.md`, which #1454 may rename, and this work adds one sentence to step 1 of *Orchestrator: the order inside a ticket*. | #1445 | The same grounds as the row above. Neither item adds a check that reads the other's content. |

## Operational impact

- This pull request moves the version from 0.36.0 to 0.37.0, in `.claude-plugin/plugin.json`. It is the first pull request into `release/v0.37.0`. Phase 1's crafter makes the move in the commit that adds `changelog.md`.
- No migration, environment variable or dependency. Rule 21 reaches an agent at its first spawn under a plugin that holds it.

## Judgments of the run

| Date | Judgment | Grounds | Judged against |
|---|---|---|---|
| | | | |
