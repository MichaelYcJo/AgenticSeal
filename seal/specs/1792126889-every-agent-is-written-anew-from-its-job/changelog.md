### Changed

- **The warden preloads the contract alone and opens `code-review` and
  `writing-style` at the step that needs them (#957).** `agents/warden.md`
  and `skills/code-review/SKILL.md` are written anew from the warden's job,
  about half their former size, and a warden spawn preloads 27,032 bytes
  where it preloaded 76,019. Before it hands back, the warden reads its round
  record through `chain_check.py` and corrects what the check refuses, so a
  finding without its `verdict:` line no longer reaches the fix pass. On this
  repository's evaluation, against the warden at the start of the release,
  it found 16 of 24 known defects where it found 13, wrote fewer false
  findings, and read 9.2% fewer tokens per tool call. Nothing to do.
  (`1792126889-every-agent-is-written-anew-from-its-job`, #957)
- **The agent contract is written anew as twenty rules, each naming what
  enforces it (#957).** `skills/agent-contract/SKILL.md`, which every agent
  preloads, drops its incident histories and is about a fifth smaller. A
  rule that stayed keeps its section number; the four new ones are §17 to
  §20: clean up only what you started, fix or report a check that refuses
  correct code rather than bending the code, rewrite a text in place, and do
  not avoid the change a problem calls for. Its §2 now says no agent runs
  the broad gate. Two numbers moved: the old `§16` is now part of `§11`,
  and the old `§17`, the commit rule, is now `§16`; a spawn prompt of your
  own that cites either is rewritten to the new number.
  (`1792126889-every-agent-is-written-anew-from-its-job`, #957)
