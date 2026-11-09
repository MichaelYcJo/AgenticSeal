# Closing memo: 1794142459-parity-reads-original-forward

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran its 80 scoped modules and the lint and format check over the one Python file it changed, phase 2 ran its 82 scoped modules and changed no Python file, and the fix passes of rounds 1 and 2 each ran the modules that read the paths they changed and the lint and format check over the one Python file they changed | answered by the work item's broad gate, `trail/gate.md` `run: 0e9af18a1 against 9e758b0b0`, which names no failing case and on which `guarantee.md` sealed |
| closed whether a framer, a tracer and a proofer in a migration act on the sentences phase 1 wrote: the framer lists the original's output surface in its *Grounding*, the tracer names what the list lacks, and the proofer walks the surface from the original forward and leaves a line per item in the round record; the cases read the text, and no case runs any of the three against an original (`frame/questions.md` Q1) | a measurement no record asks for: the answer would decide whether the three agents' migration sentences need rewording; no migration run has happened since the release, and no open issue, failed run or other work item's rule waits on it, so nothing is opened |
| closed whether a proofer walks the response-shape axis from the reference's fields to the code's and raises a field the code lacks and a field the reference leaves out that the code sends, as the paragraph under `skills/code-review/SKILL.md` *Comparison axes* asks; no case reads the paragraph and no case runs a proofer on it (`trail/phases/phase-2.md`) | a measurement no record asks for: the answer would decide whether the *Comparison axes* paragraph needs rewording; no open issue, failed run or other work item's rule waits on it, and nothing is opened |

## Not done

No case pins where `agents/tracer.md` step 3 and the lead of its rule
*Start at the original's entry point, open the design's coordinates there,
and report the axis nobody looked at* start the tracer. The fix pass of
round 1's first finding rewrote both in place. The start point the skill gives in
`skills/legacy-parity/SKILL.md` *The original's coordinates* is not pinned
either, and a guard on the step's or the lead's words would pin wording,
which `docs/running/what-a-script-gates.md` *The checks* refuses. Review
reads them.
