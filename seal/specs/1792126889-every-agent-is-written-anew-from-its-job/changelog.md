### Changed

- **The warden preloads the contract alone and opens `code-review` and
  `writing-style` at the step that needs them (#957).** `agents/warden.md`
  and `skills/code-review/SKILL.md` are written anew from the warden's job,
  about half their former size, and a warden spawn preloaded 27,032 bytes at
  its evaluation (`93c1878c`) where it preloaded 76,019 at `af9c924b`. Before
  it hands back, the warden reads its round record through `chain_check.py`
  and corrects what the check refuses, so a finding without its `verdict:`
  line no longer reaches the fix pass. On this
  repository's evaluation of 12 known defects, each run twice, it made 16 of
  24 finds where the warden at the start of the release made 13, wrote fewer
  false findings, and read 9.2% fewer tokens per tool call. Nothing to do.

  | Agent | Preload bytes | Tokens per tool call | Spend USD | Verdict |
  |---|---|---|---|---|
  | warden | 76,019 → 27,032 | 89,100.4 → 80,940.4 | 36.0352 → 36.6656 | pass |
  | smith | 94,693 → 90,594 | 45,574.6 → 45,194.4 | 6.3830 → 5.9980 | pass |
  | framer | 93,453 → 89,310 | 28,253.1 → 33,595.1 | 16.5896 → 17.3532 | fail on tokens per call, carried to #968 |

  Each figure is the tree at `af9c924b` → at `93c1878c`, read from the work
  item's `evals/<agent>-phase-3.md` at `314f6166`. The smith and the framer
  changed through the contract and the loss of their tools-per-turn
  figures; their own rewrites are #967 and #968.
  (`1792126889-every-agent-is-written-anew-from-its-job`, #957)
- **The agent contract is written anew as twenty rules, each naming what
  enforces it (#957).** `skills/agent-contract/SKILL.md`, which every agent
  preloads, drops its incident histories and is about a fifth smaller. A
  rule that stayed keeps its section number; the four new ones are §17 to
  §20: clean up only what you started, fix or report a check that refuses
  correct code rather than bending the code, rewrite a text in place, and do
  not avoid the change a problem calls for. Its §2 now says no agent but the
  sealer runs the broad gate. Two numbers moved: the old `§16` is now part
  of `§11`, and the old `§17`, the commit rule, is now `§16`; a spawn prompt
  of your own that cites either is rewritten to the new number.
  (`1792126889-every-agent-is-written-anew-from-its-job`, #957)
