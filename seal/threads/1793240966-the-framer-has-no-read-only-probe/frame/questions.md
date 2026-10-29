# Questions for the planner: 1793240966-the-framer-has-no-read-only-probe

## Answered by the tree, not to be reopened

- **Where a probe runs.** A command that only reads runs against the tree.
  Anything that writes runs under `<scratchpad>/<work-item-id>/frame/`, and
  the repository's code runs from a `git clone --no-local` there.
  `docs/the-agent-set.md` names an agent's scratch for its work item, and
  `agents/proofer.md` *Rules* is the clone's precedent (`plan.md` A2 and A3).
- **The framer still runs none of the repository's checks.** No test module,
  no lint, no typecheck and no `seal gate`, as a probe or otherwise. Contract
  rule 2 and step 8's pinned "no check of the repository's" hold it
  (`plan.md` A4).
- **The label is `executed`.** No new label or mark is added (`plan.md` A6).
- **`skills/implement/SKILL.md` is not edited.** Its `a measurement`
  sentence names no party and stays true, and `agents/framer.md` is the one
  source for when the framer runs the probe (`plan.md` A8). This also keeps
  the work out of the file #1091 edits.
- **`a measurement` stays an answerer value.** A CI leg on another platform
  and a harness behaviour no subagent can trigger still need it (`plan.md`
  A5).
- **The design template's `## Grounding` column stays `Policy clause`.**
  #955's frame put a probe's answer in that table, and the issue names
  *Grounding* as where the answer goes (`frame/design.md` *Scope*, Out).
- **The policy sentence is a `## Rule changes` item, not a build edit.** The
  settle writes it into `docs/the-agent-set.md` at the release
  (`skills/settle/SKILL.md` *Rule changes*). It parses, executed at
  `c48cd5e3` (`plan.md` *Technical context*).
- **The new case's question and its answer.** `"straße".upper() + "!"`
  gives `'STRASSE!'`, executed. Reading `shout` alone does not show that a
  word grows, so a framer that answers it without running anything is
  answering from memory.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | How much is spent on paid runs to show the new framer case red on the old definition and green on the new one? Contract rule 15 asks for a new case seen red before it is relied on. For this case that means running the framer, which costs about 2 USD a run (executed: #968's framer side, 16.12 USD for eight runs). The tree cannot choose a spend. | a person | (a) The new case alone, two runs on each side, capped at 20 USD with `--max-cost-usd`, about 8 USD expected. It satisfies rule 15 for this case only. (b) The whole framer suite, five cases with two runs each on each side, about 40 USD. It also tells whether the new rule made the other four cases worse, the reading #947 otherwise takes at the end of the milestone. (c) No paid run. The case is committed unseen-red, `gaps.md` names that under *Not verified* with the owner as answerer, and #947's run is the first to exercise it. | (a) | answered 2026-10-29 by the orchestrator under the owner's automation answer: the default (a); the runs cost 10.01 USD (`trail/phases/phase-3.md`) |
| Q2 | What if the old side passes the new graders on every run, so the case does not separate the definitions? A framer under the old text may run `python3 -c` on its own, as #955's did. Only the run tells. | the work | (a) Keep the case as the pin of the new rule, and record in `gaps.md` that the old side passed, with the side file's path. (b) Reword the case's issue and run again until the old side fails, which spends again on noise. | (a). No re-run for a case that measured what it measured. | answered 2026-10-29 by the work: not reached, the old side failed `shape-answers-by-probe` on both runs (`trail/phases/phase-3.md`) |
| Q3 | Can the crafter start `claude plugin eval` from its own environment for phase 3? A nested session's sandbox and credentials are not visible from the tree. | the work | (a) The crafter runs phase 3. (b) Where it cannot, the crafter says so in its hand-back and the orchestrator runs the two sides, then the crafter writes the phase record from the side files. | (a), then (b) where (a) fails | answered 2026-10-29 by the work: (a), the crafter ran both sides (`trail/phases/phase-3.md`) |
