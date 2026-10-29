# Questions for the planner: 1793251202-the-citation-case-misses-files-and-wrapped-comments

## Answered by the tree, not to be reopened

- **The case reads every tracked text file outside the records.** The
  issue's first *Done when* allows either that or a stated list of files
  left out. The tree already defines the wider corpus in
  `tests/behaviour/test_a_cited_section_stands_in_its_file.py#citations`.
  At the base, the wider corpus finds no dangling citation and no near
  miss, and reads in 0.066 s (`frame/design.md` *What the probes
  answered*). So the narrow option buys nothing.
- **The fix is a move, not a widened second walk.** `CLAUDE.md` (a fact
  has one source) and `CONTRIBUTING.md` *The test layout* (a `tests/text/`
  module loads no shipped code) settle it. `frame/plan.md` *Alternatives
  considered* gives each rejected option with its failure scenario.
- **The class is wider than `#` in a hook.** Contract rule 12 asks for the
  class, so a `#` marker in every file that is not `.md`, and adjacent
  `.py` string literals, are read through the module's existing
  `flowing`. A `#` in a `.md` file opens a heading, and markers other
  than `#` are a stated limit (`frame/design.md` *Scope*, *Out, and
  why*).
- **The red for the wrapped-comment case is shown against the base's
  reader, not by checking out `c825fd2c`.** The contract-rule reader is
  the same at both commits (`git diff c825fd2c HEAD` over the module,
  executed). Phase 2 shows each new case red against phase 1's commit,
  which still holds that reader.
- **`BARE_HOMES` stays `("agents",)`.** A bare `rule <N>` in a newly read
  file such as `CLAUDE.md` or a workflow can be any list's rule. The
  existing case pins this and moves unchanged.
- **No rule of the policy root changes.** No `docs/` section states the
  citation case's reach (`frame/design.md` *Rule changes*).
- **`skills/writing-style/SKILL.md`'s `check:` line is not edited.** It
  already names both modules, and the contract module keeps a case that
  refuses a heading near miss at its line.
- **Stale `.test_durations` keys left by #1111 are not this work's.**
  Only the 15 keys of the moved cases are rewritten.

## Assumptions written down, because no answer changes what gets built

- The shared corpus function's name and return shape are the build's
  choice. `frame/design.md` *Data & interfaces* states what it must hand
  back.
- The fixture files in S3 (`CLAUDE.md`, `.github/workflows/x.yml`,
  `evals/scripts/x.py`, `templates/x.yml`) are examples of files the old
  walk did not read. The build may pick others that the old walk also
  misses.

No row is open. Nothing in this work needs a person, a measurement before
the build, or a decision that only the build can make.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
