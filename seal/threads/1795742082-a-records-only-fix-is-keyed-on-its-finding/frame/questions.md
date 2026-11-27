# Questions for the planner: 1795742082-a-records-only-fix-is-keyed-on-its-finding

The ticket left these open, and the tree answered each:

- How often a records-only fix closed a finding located in code as well as records: `frame/design.md` G7 and G9.
- What the next round found after such a fix: `frame/design.md` G8, G9 and G10.
- How often the sealer withholds over a record sentence: `frame/design.md` G11.
- What a key on the fix's changed paths alone would let through, and why the finding's own block stays in the key: `frame/plan.md` *Alternatives considered*, the row opening "Replace the structure".
- Whether the condition is kept as it stands: `frame/plan.md` *Alternatives considered*, the row opening "Keep the structure".
- Whether the proofer cites code under `evidence:` alone, the owner's middle option: `frame/plan.md` *Alternatives considered*, the row opening "The owner's middle option".
- Which mechanism beside text fits: `frame/plan.md` *Alternatives considered*, the rows on the notice, the new line, the `--sealing` line and the reader before the sealer.
- Whether a round after a merge of the base reads text the merge brought in, or leaves it to the settle: `frame/design.md` G16 to G18 and *Scope* item 6, and `frame/plan.md` *Alternatives considered*, the last three rows.
- Where this work stands under #1631: `frame/plan.md` *Overlap with the release*, the row for #1631.
- Whether the work moves the version: `frame/design.md` G21.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does a sealer, in a real run, withhold where a records-only fix left unchanged a path outside the records that its finding asked to change, and does it catch a defect in the sentence such a fix wrote? The tree could not answer: no pass in this repository's history left such a path unchanged where a change was owed (`frame/design.md` G9), and the three rounds that found a defect after such a pass ran before the sealer had its read of a records-only pass (G8). No probe could either: it takes a sealer spawned on a real work item's last record, which no subagent can start | a measurement: the repository owner, reading the next release through the row of `seal/follow-up.md` that `frame/design.md` *Scope* item 8 amends | (a) The sealer withholds, or no such pass occurs: the key stands. (b) A `sealed` verdict passed such a defect and a later reader found it: the clause *Scope* item 1 removes goes back to the weighing of `skills/core/SKILL.md` *The rule a mechanism is kept against* | (a), and the build goes as framed | open |
