### Changed

- **The smith preloads the contract alone and opens its two skills when
  their act comes (#967).** `agents/smith.md` is written to the warden's
  shape: `skills: [agent-contract]`, then `## Job`, `## Order of work`,
  `## Never` and `## Rules`. Its first step opens
  `skills/implement/SKILL.md`, and the steps that write a record or the
  hand-back open `skills/writing-style/SKILL.md`'s section for the record's
  language. `implement` keeps every heading other files cite and loses its
  incident narration. The smith no longer names who runs the broad gate; it
  says only that it does not run it. In every one of the eight measured runs
  the smith opened both skills.
- **No agent writes a proof block any more (#967).** The hand-back carries
  its claims under the three labels `executed`, `read` and `unverified`, and
  the sealer's `guarantee.md` is the one seal. A session of yours that loads
  `implement` directly ends no response with a block, and a spawn prompt
  that asks a smith for one gets the labels instead. A test now refuses an
  emoji or such a block in any `agents/*.md`, `skills/*/SKILL.md` or
  `templates/*.md`; `skills/legacy-parity/SKILL.md` is skipped by name until
  #970.
- **The writing rules, the questions template and the audit result are in
  words (#967).** Each of `writing-style`'s two language sections now opens
  with one line naming the sections that also apply, so a reader who opens
  one section alone still finds the structure rules; no rule left the file.
  A `questions.md` status reads `open` or `answered <date> by <who>`,
  written by whoever answered. The `audit` result block reads `passed`,
  `warnings` and `violations` where it showed marks.

  | Agent | Preload bytes | Tokens per tool call | Spend USD | Graders passed | Verdict |
  |---|---|---|---|---|---|
  | smith | 90,728 → 26,879 | 43,068.0 → 35,691.6 | 6.6210 → 5.4509 | 48 → 48 of 48 | pass |
  | warden | 27,198 → 27,173 | 87,197.6 → 87,862.4 | 42.2333 → 41.7424 | 86 → 91 of 96 | fail, rule 5 alone: tokens per call up 0.8%, five more truths found |
  | framer | 89,444 → 86,353 | 27,296.7 → 29,894.6 | 16.9055 → 16.1196 | 64 → 64 of 64 | fail, rule 5 alone: tokens per call up 9.5% with total tokens down 0.5%, carried to #968 |

  Each pair is the tree at `2fc33333` → the tree at `af716289` (the
  smith's at `28d6a453`, after round 1's fixes to its definition), on one
  suite (`af9c924b`), eight runs a side for the smith and the framer and
  eighteen for the warden, none cut short. The second tree includes #969's
  changes, merged in at `16e8d4c8`, as well as this item's: contract §2,
  which all three agents preload, and for the warden
  `docs/the-review-record.md`, `skills/code-review/scripts/chain_check.py`
  and `agents/sealer.md` too.
  Each figure is read with `noninferiority.py#side_numbers` from the work
  item's `evals/baseline-<agent>.json` (committed at `b4e72dbe`, `dc8991c2`
  and `adbbea77`) and `evals/<agent>-phase-4.json`; the verdict is
  `evals/<agent>-phase-4.md`, both committed at `6f3ee98b`.
  (`1792251842-the-smith-is-written-anew-from-its-job`, #967)
