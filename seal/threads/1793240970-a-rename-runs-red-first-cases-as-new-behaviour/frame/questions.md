# Questions for the planner: 1793240970-a-rename-runs-red-first-cases-as-new-behaviour

## Answered by the tree, not to be reopened

- **The census is not a case written new.** The issue's *The change* says a
  rename is proved by "the existing cases passing at the new name or path,
  plus a census case where the old spelling must be gone". Its first *Done
  when* says such a phase "writes no new case". Both hold when the census is
  an entry added to a census the repository already keeps, as this
  repository's `tests/censuses.py#old_names` is, and otherwise the search
  for the old spelling with its empty result in the phase record. An old
  name in code fails an import or a call in the existing cases. An old name
  in prose fails nothing, which is what the census covers. A reader who
  wants a new census test per rename overturns this by changing one cell of
  the verify row.
- **No rule of the policy root changes.** No `docs/` section states the
  crafter's cadence, the verify table or the phase-boundary scope
  (`frame/design.md` *Grounding*). `docs/the-broad-gate.md:148` speaks of
  new cases being seen red, and a rename writes none.
- **Contract rule 15 keeps its wording.** It binds a new case. The eval case
  this work adds is one, so phase 1 shows it red before phase 2 changes the
  text.
- **A phase that renames and adds behaviour owes the cadence for its new
  behaviour only.** The verify row sorts by what changed, unit by unit. A
  unit whose body, signature or output changes beside its name is the
  *Logic* row.
- **The phase record carries the proving cases under
  `## What this phase found`.** No new field, line grammar or mark is added.
- **Contract rule 2 is rewritten with the crafter.** Rule 12 asks for every
  statement of the phase-boundary scope, and rule 2's "the ones it touches"
  is one of the three (`frame/design.md` *Scope* item 5). The contract's
  preamble lets a rule be reworded in place under its number.
- **The proofer's "Type the narrow form, one module" stays.** It is about a
  reviewer's runs and probes. The review of a rename is reached through
  `skills/code-review/SKILL.md`'s *Regression test* judgment.
- **The pins on rewritten sentences are re-pointed, not removed.** Each
  guards that a rule still exists after it moved (`frame/plan.md`
  *Alternatives considered*, last row).
- **The behaviour arm keeps its existing graders.** The four build cases
  grade a case written beside each new unit, and no `seal mutate` grader is
  added to them (`frame/plan.md` *Alternatives considered*).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does this work item pay for the behaviour eval runs that show the new rename case red against the base's definitions and green against the branch's? The runs are `claude plugin eval` sessions of the crafter on `claude-opus-5-5`, two runs a side: the rename case at `--rev 1e82fd0a` in phase 1, then the rename case and `rule-crafter-slugify` at the branch tree in phase 2, six crafter sessions in all. Each call is capped with `--max-cost-usd 15`. The tree cannot settle it, because a spend is a value somebody has to be accountable for | a person | **Pay, as capped**: contract rule 15 is met for the new case, and phase 2 shows the behaviour arm still writes its case. **Pay nothing**: the case is planted without being seen red. The phase records label its red and its green `unverified` with the repository owner as answerer, and `gaps.md` names the case under `## Not verified` | Pay, as capped | answered 2026-10-29 by the orchestrator under the owner's automation answer: the default; the runs cost 3.59 USD in all (`trail/phases/phase-1.md`, `trail/phases/phase-2.md`) |
| Q2 | Does the base's crafter definition go red on the rename case: on either run, does it call `seal mutate` or write a second test function? The fixture is three lines, and the old step 6 says "each unit you added", which a crafter may or may not read as covering a renamed unit | a measurement | **Red on a run**: the case is planted as it stands. **Green on both runs**: the old definition did not over-verify a fixture this small, so the case cannot show the change. It is still planted as the guard of the new row. The phase 1 record says so, and `gaps.md` names the case as not seen red under `## Not verified`, with the repository owner as answerer | Proceed as the base run reads | answered 2026-10-29 by the measurement: red on both base runs, each failing `shape-no-mutation` (`trail/phases/phase-1.md`) |
| Q3 | Can the crafter start `noninferiority.py run` from its own environment? The command starts `claude plugin eval` sessions, and no phase record in the tree shows a crafter doing so | the work | **It can**: the phase runs it as its *Verified by* cell says. **It cannot**: the phase record names the command unrun, and the orchestrator runs the same command before it spawns round 1 and names the output file in that spawn prompt | The phase tries it once, and on failure records the command and its error | answered 2026-10-29 by the work: the crafter ran every call itself (`trail/phases/phase-1.md`) |
