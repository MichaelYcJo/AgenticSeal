### Removed

- **`seal cost --segments` prints each segment's tools per turn with no verdict: the bars for each kind of segment and the grade under the table leave (#1440).** The page held each framer row against a bar of 1.4 tools per turn and each proofer row against 1.8. Under the table it named every row below its bar and counted the rows graded, exempt and ungraded. No release since 0.17.0 moved a reading toward a bar, although 0.17.0 wrote the instruction to batch into the framer's definition and contract rule 10. Over the transcripts on disk, 65 Opus framers read a median of 1.31 and 67 Opus proofers a median of 1.12, and no proofer reached 1.8. Opus does batch its reads, but it chains them inside one Bash call, so the ratio counts one call for a turn that read two or three files. The grade, the `SEGMENT_BARS` table in `skills/verify/scripts/session_cost.py`, and the `kind` and `bar` keys of each `--segments --json` row leave. The `t/turn` column and `numbers.tools_per_turn` stay, so a reading stays comparable with those posted since 0.9.4.
- **The plain reading, `seal cost <transcript>`, no longer prints a `batching` line.** It printed one below 1.2 tools per turn, saying that independent calls were going out one at a time, which is false for a segment that chains its reads. The `nothing obvious` line now prints wherever no check was re-run. The ratio and its denominator stay in `--json` as `tools_per_turn` and `call_turns`.
- **Contract rule 10 no longer points at the bars.** The rule still asks every agent to open every file a coordinate names in one call and to batch independent reads. Its last sentence, which named `docs/running/the-run.md` *The per-segment bars*, leaves. `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* no longer says that the page names the rows under their bar. The policy section and the sentence in `docs/running/measuring-a-run.md` that cites it leave at the settle after this release.

Updating: nothing to do. A program that read `kind` or `bar` from a `--segments --json` row finds neither key.

### Process changes

| Date | Change | Why | Source |
|---|---|---|---|
| 2026-11-09 | Contract rule 10 asks every agent to batch independent reads and no longer names a bar its segment is judged by | No segment kind met its bar since 0.17.0, and Opus chains its reads inside one Bash call, which the ratio cannot see | https://github.com/MichaelYcJo/AgenticSeal/issues/1440 |
| 2026-11-09 | `skills/verify/orchestration.md` *Measure the segment, and feed the flow log* step 1 no longer says the `--segments` page names the rows under their kind's bar | The page prints the ratio with no verdict, and a reading is judged against earlier readings | https://github.com/MichaelYcJo/AgenticSeal/issues/1440 |
