# Questions for the planner: the census reads every entry point (#1255)

The issue left these open, and the tree answered each one. They are not
reopened here.

- Which files the census reads: `frame/plan.md` *Alternatives considered*
  A1, and `frame/design.md` *Grounding*, the `run_tests.py` row.
- Whether a loop is an answer, or only the call is: `frame/plan.md` A3.
- Whether the five loops without `stdin` are drifted: `frame/plan.md` A4.
- Where an answer that must come after another statement is exempted:
  `frame/plan.md` A5.
- Which of a file's `__main__` blocks the census reads: `frame/plan.md` A6.
- Where the five calls inside `main()` go: `frame/plan.md` A7.
- Whether the three drifted answers still stand: `frame/design.md`
  *Grounding*, the *Command C9* row.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Which entry points owe `hooks/lib/console.py#STREAMS`' answer: every tracked `.py` with a `__main__` block, or something narrower? The issue reserves it for the owner where the frame cannot decide it. The tree argues for (a) but cannot decide it: whether a script that never reaches a person's console should carry one more statement is a value for the owner, and no probe measures a value | a person | (a) Every entry point gives the answer, and one that cannot give it carries its reason at its line, as `hooks/lib/launch.py` does. Twelve scripts gain the answer and none gains an exemption for where it runs. (b) A script that runs only on CI's UTF-8 runner carries an exemption that says so. At HEAD that is seven scripts under `.github/scripts/` that only a workflow runs (`close_issues_on_release.py`, `durations_union.py`, `label_merged_on_release_branch.py`, `release_completeness_check.py`, `roll_flow_measurement_issue.py`, `publish_release_note.py`, `tag_release.py`). Each exemption is a claim no check reads, and the premise of the option does not hold for the other ten scripts without an answer, which a person, `bin/test` or `seal` runs (`frame/plan.md` A2') | (a), which the build follows | open |
| Q2 | Does one of the seventeen entry points without an answer meet a reason, while it is built, why the answer cannot stand as the first statement of its first `__main__` block? | the work | The phase that meets it exempts that line with its reason, as `broad_gate.py` and `seal_stamp.py` are exempted, and records the reason in `trail/phases/phase-1.md` *What this phase found*. None is known at framing time: the frame read each file's imports and `__main__` block and found none (`frame/design.md` *Grounding*, the row on the 18 with no answer) | every one gives the answer | answered 2026-11-04 by crafter (phase 1, `trail/phases/phase-1.md`): none of the seventeen meets such a reason |
