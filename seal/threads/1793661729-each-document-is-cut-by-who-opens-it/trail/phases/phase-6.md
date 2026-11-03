# Phase 6: 1793661729-each-document-is-cut-by-who-opens-it

## What this phase found

**The frame holds for this phase, with one coordinate off.** It was read
against the tree at d397a3bec before the first edit (read). The core's
*Asking a person is the most expensive step* held the sentence D2 item 1
removes, at lines 86-91 after phase 4's re-pointed citation. Contract rule
20 was 388 bytes, as `frame/plan.md` *Technical context* says (executed).
`agents/sealer.md` step 1 cited `docs/checks/the-pull-request-check.md`
*What the check reads at the pull request* beside `chain_check.py#follows`.
The coordinate that is off is the plan's claim that the one citation of
rule 20 by number is the comment at
`tests/text/test_the_rules_have_one_owner.py:206`. That comment names a
different rule. fdfb20d55, which wrote it, says in its message that the
sentence is "pinned as rule 20 of tests/text/test_the_rules_have_one_owner.py"
(executed: `git show fdfb20d55`). So the comment is not a citation of the
contract, and this phase left it as it was.

**The commits.**

- bad177508: the core. D1's paragraph stands after *Each agent judges its
  own target*, in D1's words. D2 item 1's sentence is gone. One offset
  beyond D2 is taken (below). `skills/settle/SKILL.md` *A document past its
  ceiling is split, never trimmed* now cites the core for the reader rule.
  Phase 3 left that citation to this phase.
  `tests/text/test_review_axes.py#test_the_core_names_where_the_routing_question_is`
  is removed, along with its `.test_durations` key.
- e6fd2287a: the contract. Rule 20 retires to one line. Rule 2 loses one
  sentence (below).
  `tests/text/test_broad_gate_rule.py#test_the_contract_and_the_orchestration_name_the_broad_run_command`
  becomes `#test_the_orchestration_names_the_broad_run_command`, and its
  key in `.test_durations` is renamed.
- 308424df6: the sealer's step 1 cites
  `skills/code-review/scripts/chain_check.py#follows` in place of the
  document (D2 item 3).

**D1 went in at its framed length.** D1 lets the build tighten the text. No
tightening kept every clause's meaning, and S2 held without it. The
paragraph is five sentences, as S1 allows, and 473 bytes.

**S2 alone would have failed after D2's three items. Two more offsets were
taken, as D2's last paragraph asks.** At d397a3bec every agent's preload
was already above the base (executed, the command below). Phase 5's longer
`docs/<group>/` paths grew the core and the contract by 42 bytes, and
phase 1's 90 bytes, with phase 4's longer ladder citation, grew
`agents/framer.md` by 124. D1 adds 473 bytes. D2 item 1 removes 323, and
the retirement of rule 20 saves 124 (388 bytes to 264, `awk | wc -c`,
executed). With those alone the framer would have stood about 190 bytes
above the base. Two offsets came from preload text that
only the orchestrator acts on, or that no agent acts on:

- Contract rule 2's sentence "The orchestrator runs `seal gate --base
  <base> --record <item>` with nothing else running, then spawns the sealer,
  which reads the record that run wrote." Only the orchestrator types that
  command. The sealer's own step 1 says what it reads. The sentence is a
  copy of `docs/running/the-broad-gate.md` (lines 11-13) and
  `skills/verify/orchestration.md` *The broad gate*, the section the
  orchestrator reads when it runs the gate. The rule's title and its last
  sentence still name the orchestrator as the gate's owner and the suite's
  answerer. The sentence was pinned in
  `tests/text/test_broad_gate_rule.py`. That case keeps the orchestration's
  half, the preflight, the run and the log, and its docstring says why the
  contract's half left. 154 bytes.
- The core's "where first setup or `seal pr-checks install` put its
  workflow in the tree" became "where its workflow is installed". How the
  workflow gets installed is a setup fact. No agent acts on it, and
  `docs/layout/one-root-by-lifetime.md` states it in its table's CI row.
  The shorter clause keeps the condition, so the sentence still says the
  check refuses nothing where no workflow is installed. 43 bytes.

Judged against D2's last paragraph ("takes the next offset from preload
text that only the orchestrator acts on, names it in the phase record, and
never grows another file to do it") and the core's *The rule a mechanism is
kept against* ("A fact has one source, and every other place links to it").
Neither offset grows another file. The test edit removes an assertion and
grows nothing.

**S2 (executed).** Both trees are measured by the HEAD tree's
`.github/scripts/release_report.py#preloads`, with the HEAD tree's
`payload_meter.py` as its kernel, as `release_report.py#main` measures the
tag and the tree. The base tree came from `git archive 2d38c75af`, extracted
under the scratchpad. The probe script was deleted after the run. This is
its whole text:

```python
import importlib.util, sys
spec = importlib.util.spec_from_file_location("rr", sys.argv[1] + "/.github/scripts/release_report.py")
rr = importlib.util.module_from_spec(spec); spec.loader.exec_module(rr)
k = rr.meter()
for root in sys.argv[2:]:
    p = rr.preloads(root, k)
    print(root, " ".join(f"{a}={p[a]}" for a in sorted(p)))
```

`python3 preloads.py <repo> <scratch>/base <repo>` printed, at d397a3bec
before the first edit:

```
<scratch>/base crafter=33203 framer=36365 proofer=32414 sealer=32262 tracer=25212
<repo>         crafter=33250 framer=36531 proofer=32462 sealer=32103 tracer=25254
```

and at 308424df6:

```
<scratch>/base crafter=33203 framer=36365 proofer=32414 sealer=32262 tracer=25212
<repo>         crafter=33081 framer=36362 proofer=32293 sealer=31879 tracer=25085
```

No agent's preload at HEAD exceeds its preload at the base. The changes
are crafter −122, framer −3, proofer −121, sealer −383 and tracer −127. The
framer's margin is 3 bytes. A later edit that grows the core, the contract
or `agents/framer.md` puts the framer above the base again.

File bytes at each commit (`git show <commit>:<path> | wc -c`, executed):

| Commit | core | contract | `agents/sealer.md` | `agents/framer.md` |
|---|---|---|---|---|
| 2d38c75af (base) | 9077 | 13179 | 10006 | 14109 |
| d397a3bec | 9114 | 13184 | 9805 | 14233 |
| bad177508 | 9223 | 13184 | 9805 | 14233 |
| e6fd2287a | 9223 | 12906 | 9805 | 14233 |
| 308424df6 | 9223 | 12906 | 9750 | 14233 |

**A decision: the retirement line cites the core by path.** D2 item 2's
text reads "the core's *The rule a mechanism is kept against* states it".
The line now reads `` `skills/core/SKILL.md` *The rule a mechanism is kept
against* states it ``. `skills/writing-style/SKILL.md` *에이전트와 검사가
읽는 글은 한 가지로만 읽히게 쓴다* asks for a section of another file to be
cited by its backticked path and its title. The path costs 12 bytes, and S2
holds with it. The heading follows rule 8's shape, `## 20 Retired:`
and then what the rule was. Its `check:` stays `none reader: the proofer at
review`, since the line's second clause still states a rule that a reader
holds.

**A decision: the case that pinned the core's routing sentence is removed,
not narrowed.** The case held #1177's reading that the core is where a
session that has opened no skill learns which section asks the routing
question. D2 item 1 removes that sentence: only the orchestrator acts on
it, the invariant table's first row names the hook, and
`skills/implement/orchestration.md` *Orchestrator: how the work is routed*
holds the act. A session that has opened no skill still learns the section
at the refusal, since `hooks/routing-edit-gate.py` names it in its message
(lines 97-98, read). A narrower pin, on the table's hook path alone, would
be a new mechanism with no catch record. Judged against D2 and the core's
*The rule a mechanism is kept against*.

**The sealer's citation (D2 item 3).** Step 1 now reads "the rule it
applies is the one `skills/code-review/scripts/chain_check.py#follows`
reads". The pin in
`tests/behaviour/test_the_sealer_guarantees.py#TestDefinition::test_step_1_reads_the_record_and_runs_nothing`
asked for `` `chain_check.py#follows` ``. It now asks for the full path, as
D2 writes it. No agent-side citation of `docs/checks/the-pull-request-check.md`
is left in `agents/`, the core or the contract (`git grep`, executed: no
lines). That is D3's line for `checks/`.

**Seen red (executed).**

- The sealer pin, edited first, failed against the old step 1:
  `bin/test -q -p no:xdist tests/behaviour/test_the_sealer_guarantees.py`
  printed `1 failed, 10 passed`, with the failure at line 166. It passed once
  step 1 changed.
- After the commit, `seal mutate agents/sealer.md --replace
  "\`skills/code-review/scripts/chain_check.py#follows\` reads."
  "\`chain_check.py#follows\` reads." --tests "bin/test -q -p no:xdist
  tests/behaviour/test_the_sealer_guarantees.py -k
  test_step_1_reads_the_record_and_runs_nothing"` printed `red: the cases
  failed against the mutation (exit 1)` and exited 0. `git status` was clean
  after it.
- The narrowed broad-gate case and the removed core case add no behaviour,
  so no red was owed. The narrowed case only drops an assertion, and it
  cannot be shown red against the old text.

S1 adds no case. Its *Verifiable how* is the proofer's reading of the core
against D1. The core carries no `check:` lines.

**Other places that stated the changed rules (contract rule 19).** The list
is a sample (contract rule 12), from `git grep` of each removed sentence's
words outside `seal/` and `CHANGELOG.md`:

- "routing question is one of that batch", "orchestrating session puts" and
  "refuses the first edit until" listed only the core.
  `-i -E "core.{0,80}routing (question|section)"` listed nothing.
- "with nothing else running" and "spawns the sealer, which reads" listed
  the contract, `docs/running/the-broad-gate.md`,
  `skills/verify/orchestration.md`, `skills/verify/scripts/broad_gate.py`
  and `templates/setup/config.md`. Each of the last four states the
  orchestrator's run in its own place and stands. Every `contract rule 2`
  citation (`git grep -n "contract rule 2"`) cites the rule for giving the
  gate to the orchestrator or for forbidding it to agents. The rule still
  says both.
- "premise" listed `agents/framer.md` *Replacing a structure is weighed with
  keeping it*. That rule is the framer's own application, and it stands.
- The reader rule: `git grep -i -e "who opens" -e "which step"` listed
  `skills/settle/SKILL.md:416`, which now cites the core, and
  `skills/implement/SKILL.md:86`, the axis sentence D5 wrote. The axis
  sentence states how the policy root is grouped, not the rule. The fold's
  message and docstring in `skills/settle/scripts/fold_check.py` speak to a
  person, and they stand.

**The narrow run (executed).** The phase-boundary set is
`tests/text/test_the_agent_contract_holds_the_universal_rules.py` and every
test module that reads a path this phase changed. The list came from `git
grep -l -E
'skills/core|"core"|agent-contract|agent_contract|sealer\.md|"sealer"|"settle"|skills/settle|"agents"|agents/|SKILL\.md|test_durations'
-- 'tests/*.py'`, without `conftest.py`, and holds 75 modules.
`bin/test -q --no-header $(cat mods6.txt)` exited 0 with 3620 passed and 11
skipped. `seal rules --check` exited 0, and `seal layout --check tests`
printed "150 files read, 0 refused". `uvx ruff check` and `uvx ruff format
--check` passed over the three changed test modules before each commit.
