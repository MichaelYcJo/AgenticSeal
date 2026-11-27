# Questions for the planner: scripts read git past submodule settings and a floor (#1640, #1642)

Judgments the tickets left open and the tree answered. None of them is a row below.

- Which reads carry `--ignore-submodules=none`: each `diff`, `diff-tree`, `log` and `status` a script starts, through the runner, and the listing `agents/sealer.md` step 1 has the sealer type, in the step's own text. The grounds are `frame/design.md` G1 to G6, G16 and G17 and `frame/plan.md` *Alternatives considered* rows 1 to 4 and 12.
- Whether `chain_check.py#changed` is harmless, as #1640 supposed: it is not, and `chain_check.py#touched`, which #1640 does not list, decides more. The grounds are `frame/design.md` G5 and G6.
- Which version the floor is, and why: 2.30. #1642 first gave 2.24, and its body was corrected to 2.30 on 2026-11-27 after this frame read it. The grounds are `frame/design.md` G9 and G10 and `frame/plan.md` row 7.
- Which branch of #1642's second *Done when* line is taken: both, the floor stated and `seal range` saying so. The grounds are `frame/plan.md` rows 5, 6 and 8.
- Where the floor is stated: `lib/gitcmd.py#OLDEST` and the README's requirements sentence. The grounds are `frame/design.md` G11 and `frame/plan.md` row 10.
- What a git older than 2.30 prints for `seal range`'s `rev-parse`: not run, and the build does not rest on it, because `seal range` asks the version before that command (`frame/design.md` *Scope* item 5).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does git 2.30 read each git command the scripts under `lib/`, `skills/` and `hooks/` start as git 2.50.1 reads it? The tree could not answer: it holds no run under a git older than 2.39.3. No probe could either: the gits on this machine are 2.50.1 and 2.39.3 (`git --version` and `/Library/Developer/CommandLineTools/usr/bin/git --version`, executed), and the environment refused the download and build of git 2.30.0 into the scratch directory. | a measurement | The suite's modules for those scripts, or the commands `frame/design.md` G4 lists, run once on a machine or in a container whose `git --version` prints 2.30. Reads the same: `OLDEST` stands as built. A command refused or read otherwise: `OLDEST` is raised to the version that reads it, or the command is rewritten, in a work item of its own. | `OLDEST` is `(2, 30)`, on git's release notes (`frame/design.md` G9, G10), and `gaps.md` carries the run as not made. | open |
