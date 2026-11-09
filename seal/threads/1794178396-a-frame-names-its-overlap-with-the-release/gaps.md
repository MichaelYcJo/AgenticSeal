# Closing memo: 1794178396-a-frame-names-its-overlap-with-the-release

## Not verified

| Item | Who must answer |
|---|---|
| closed the full suite, the repository-wide lint and the format check at the branch's head; phase 1 ran its 85 scoped modules in one command and the lint and format check over the one Python file it changed (`trail/phases/phase-1.md`), and the fix passes of rounds 1 and 2 each ran the plan row's three modules and `tests/behaviour/test_docs_line_wrap.py`, the fix pass of the broad gate's regression ran those four and `tests/text/test_no_passage_is_pasted_into_a_second_file.py`, and none changed a Python file | answered by the work item's broad gate, `trail/gate.md` `run: 35f4fb5a against 94d04d30`, which names no failing case and on which `guarantee.md` sealed |
| closed whether a framer writes `frame/plan.md` *Overlap with the release* as `agents/framer.md` steps 4 and 8 ask, and whether an orchestrator merges in the stated order, writes a *Judgments of the run* row where it departs from it, and takes the base into the later branch of an ordered pair before its next round or broad run; the case reads the template, and no case runs a framer or an orchestrator on the instruction text | answered by later runs: the plans of `1794187229` and `1794188289` (0.36.0) and of the four 0.37.0 work items each hold `## Overlap with the release`, and `seal/threads/1794187229-the-body-carries-the-seal-mark/frame/plan.md:105` records the stated order, #1452 merging first, which `git log` shows (#1455 before #1456), read by the settling session |

## Not done

`docs/layout/the-record-layout.md` names what `frame/plan.md` holds in two
places, the row for `frame/plan.md` in *seal/threads/<work-item-id>/* and
the paragraph opening **A fact of a work item has one record**, and neither
names the overlap and the merge order the new section holds. Neither lists
*Operational impact* either, so neither was a whole list before this work,
and neither states a rule this work contradicts. They were left as they
stand: the file is in the policy root, and `frame/design.md` *Rule changes*
holds the no-change block, so a phase of this work item does not edit it.
Whether the settle should add the section to those two places is for the
orchestrator to fold into the frame or leave.
