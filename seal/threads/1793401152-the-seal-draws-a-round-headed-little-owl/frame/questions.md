# Questions for the planner: 1793401152-the-seal-draws-a-round-headed-little-owl

The judgments the issue and the owner's decisions left open that the tree, or
a probe, answered. Each probe is in `frame/design.md` *Grounding* with its
command.

- **Do the two input files stay under `candidates/` once installed?** No.
  They move by `git mv` to `skills/verify/scripts/seal-mark.txt` and
  `assets/seals/owl.svg`. A copy would be a second source of a shipped file
  (`skills/core/SKILL.md` *The rule a mechanism is kept against*), and the
  shipped owl of #857 had no copy in `candidates/` either.
- **Does the horned owl leave the directory?** No. Its files are renamed to
  `horned-owl.*` and its entry keeps its command. `assets/seals/README.md`
  says the directory keeps each shipped version so a reader can see it
  without checking out an old tag. The owner's decision to keep no
  runners-up covers drawings that never shipped, and the horned owl shipped
  from 0.23.1 to 0.25.0.
- **Does the wax disc fit the hook's budget?** Yes. The widest reference
  panel with its label is 5,725 UTF-16 units against `MESSAGE_BUDGET` 9,000,
  and 5,959 today (probe P1).
- **Is the committed sprite the one the approved disc was drawn from, and
  is the frame's transcription of the prototype that disc?** Yes to both:
  `cmp` exits 0, and 784 half-cells differ in none (probe P2).
- **Is the disc still 28 cells across?** The grid is, and `compose` lays it
  out as today. The painted wax fills columns 1 to 27 and half-rows 0 to 26,
  because the owner's edge wobbles. That is the approved picture, and the
  frame keeps it (probe P2).
- **Which renderer draws the icon?** `resvg_py` 0.5.0, the one installed
  here. `rsvg-convert` is not (probe P4). The README names whichever
  renderer drew the committed file.
- **What are the twin's letters and the colours' names?** The frame's choice
  (*Data & interfaces*): no decision of the owner's names them, as #832's
  frame found for the nine.
- **Where does the brand notice live?** `TRADEMARKS.md` at the root, with
  links from both READMEs and the seals README (`frame/plan.md` rows G to J).
  The wording is not legal advice.
- **Does the issue have comments that change the request?** No.
  `gh issue view 1174 --json body,comments` returned none.
- **Does the behaviour suite need a run?** No. No agent definition changes.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
