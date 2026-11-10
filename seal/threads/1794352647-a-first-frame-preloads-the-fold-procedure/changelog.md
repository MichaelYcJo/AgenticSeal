### Changed

- **A first frame no longer preloads the fold and reframe procedure (#1473).** `agents/framer.md`, which every framer spawn preloads, held the rule for a decision folded into a committed frame and for a `regression:` routed back to the framer. A first frame takes neither route, and no `frame/design.md` at v0.32.0, v0.34.0, v0.36.0, v0.37.0, v0.37.1 or v0.37.2 carries a `Reframed` line. The rule now stands in `skills/implement/fold-and-reframe.md`, and the definition keeps one sentence telling the framer to open that file before it answers a decision to fold or a `regression:`, whether it was spawned or resumed. `agents/framer.md` falls from 17,298 B to 14,946 B, and the framer's preload from 39,806 B to 37,454 B. The fold's text moves word for word, except that its four citations of the definition's own rules now name `agents/framer.md` or the contract.
- **The reframe cites its two owners instead of restating them (#1473).** The new file sends the framer to the row *The framer* of `skills/code-review/orchestration.md` *A regression is routed by comparing the fix with the frame* for what it rewrites, and to `docs/running/the-run.md` *The run* for the `Reframed` line under its mark.
- **The orchestrator names the file in every fold message (#1473).** `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket* cites `skills/implement/fold-and-reframe.md` as the place that states the fold. The message that resumes the framer, and the prompt that spawns a fresh one, each name that file for the framer to open before it answers, because a resumed framer has its definition in context and may answer without opening it.

### Removed

- **The sentence in `agents/framer.md` saying that a framer mark under the git directory is no evidence (#1473).** Nothing writes such a mark: no hook, library or script does, and `hooks/hooks.json` registers only `Stop` and `SessionStart`. The two docstring sentences in `tests/behaviour/test_waiver_decided_at_start.py` that said such a mark exists go with it. The mark at the foot of `frame/design.md` is unchanged.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-11 | `agents/framer.md` *You have two routes back* moves to `skills/implement/fold-and-reframe.md`, which the framer opens before it answers a decision to fold or a `regression:`; its reframe half cites `skills/code-review/orchestration.md` and `docs/running/the-run.md` | Every framer spawn preloaded 2,348 B that only a fold or a reframe uses, and the reframe half restated two owners | https://github.com/MichaelYcJo/AgenticSeal/issues/1473 |
| 2026-11-11 | `skills/implement/orchestration.md` *Orchestrator: the order inside a ticket*: the message that resumes the framer, and the prompt that spawns a fresh one, each name `skills/implement/fold-and-reframe.md` | A resumed framer has its definition in context and may answer a fold without opening the file that states it | https://github.com/MichaelYcJo/AgenticSeal/issues/1473 |
