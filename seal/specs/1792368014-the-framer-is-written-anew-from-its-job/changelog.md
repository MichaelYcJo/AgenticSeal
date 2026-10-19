### Changed

- **The framer preloads the contract alone and opens `implement` and
  `writing-style` by section, at the steps that need them (#968).**
  `agents/framer.md` is written to the shape the warden, the smith, the
  sealer and the scribe have: `skills: [agent-contract]`, then `## Job`,
  `## Order of work`, `## Never` and `## Rules`.
  - At the step that decides the ladder and the file set, it reads three
    sections of `skills/implement/SKILL.md`: the record language, §1 and §3.
  - Before it writes, it reads the section of
    `skills/writing-style/SKILL.md` for the record's language.
  - Where one of `implement`'s headings is not found, it reads that file
    whole.
  - It now weighs the alternative that replaces a structure as an equal of
    the one that keeps it, in `plan.md`'s Alternatives table.
  - Its incident histories and release readings are gone.
  - In all eight measured runs it opened `implement` by its three sections
    and `writing-style` by its English section. No run read either file
    whole.
- **The README says who preloads what (#968).** The framer's row in both
  editions lists `agent-contract` alone. The skills row counts one skill
  preloaded, fifteen that a session loads or an agent opens at a step, and
  six you type.

  | Agent | Preload bytes | Tokens per tool call | Spend USD | Graders passed | Verdict |
  |---|---|---|---|---|---|
  | framer | 86,353 → 26,027 | 29,894.6 → 17,190.9 | 16.1196 → 14.7490 | 64 → 64 of 64 | pass |

  Each pair is #967's last framer side, which measured the tree at
  `af716289`, → this item's side at `b434e145`. Both ran suite `af9c924b`,
  eight runs a side, none cut short. At `43cbc361`, the four files the old
  framer preloaded hash as #967's side recorded them, so that side stands as
  the baseline, byte-copied to the work item's `evals/baseline-framer.json`. On
  the new side, total tokens fell 9.3%, from 3,258,508 to 2,956,842, and
  tool calls rose from 109 to 172. The framer reads each section as its own
  ranged call, so most of the fall in tokens per call is the larger call
  count. Each figure is read from `evals/baseline-framer.json` and
  `evals/framer-phase-2.json`. The verdict is `evals/framer-phase-2.md`,
  committed at `5dc581c9`. The side measured the definition at `b434e145`.
  Review round 1's fix (`5bdad9db`) adds 577 bytes to `agents/framer.md`,
  so the preload that ships is 26,604 bytes. That tree was not measured
  again.
  (`1792368014-the-framer-is-written-anew-from-its-job`, #968)
