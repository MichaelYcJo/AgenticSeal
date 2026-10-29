# Phase 4: 1793251203-seal-pact-passes-near-misses-of-an-anchor

| Field | Value |
|---|---|
| Phase | 4 |
| Commit | 6303f97f |

## What this phase was asked

Build phase 4 after phase 3, as its `frame/plan.md` row says: the proofer's
judgment for the shapes the normalisation leaves out, one sentence in
`skills/code-review/SKILL.md` stage 1. Commit it with this record and its
Status cell, and run what the row's *Verified by* cell names. `questions.md`
W2 leaves the sentence's words and placement to this phase, and the
decision, its grounds and the source it was judged against go here.

## What this phase found

**The frame holds for this phase.** `agents/proofer.md` step 3 already has
the proofer read `frame/design.md`, and stage 1 is where the work item's
SDD set is read against the ratified documents, so the sentence needs no
new spawn and no new read.

**W2, the words and the placement.** The text stands under *Two stages, in
order*, after the paragraph on `gaps.md` and before *Review beyond the
changed files*, so it sits inside the stage 1 rule whose `check:` line
names `evals/behaviour/proofer/rule-proofer-one-finding/`:

> Where `seal/config.md` has a `Pact` row, the proofer reads the work item's
> `frame/design.md` at stage 1 against the shape
> `skills/verify/scripts/pact_check.py` states under *What each frame is
> read for*, which is all `seal pact` reads. A line written as an anchor of
> a pact that row declares, and outside that shape, is a finding:
> `seal pact` reads it as no anchor and reports the signer as citing
> nothing. Examples are a table under a plural or other wording of the
> anchor header, a row with no header and a row outside the anchor table.

The grounds, each against its source:

- **Three sentences where the plan's row says one.** The instruction is
  one: a single sentence holding the condition, the reader, the file, the
  shape, the verdict and the examples needed three commas past the limit
  `skills/writing-style/SKILL.md` *English prose rules* sets ("If a
  sentence needs two dashes or three commas, split it").
- **The shape is named, not restated.** W2 forbids a second source of the
  shape. The text cites the docstring section by path and heading, as
  *에이전트와 검사가 읽는 글은 한 가지로만 읽히게 쓴다* asks, and the
  examples name only shapes outside it, which the docstring states as not
  read.
- **The actor and the moment are named.** The skill is read by the
  proofer and by an orchestrating session, so the text says "the proofer"
  and "at stage 1" rather than an imperative (the same writing-style
  section, its third rule).
- **"Examples are", not a list.** `frame/design.md` *Scope* item 7 makes
  the three shapes examples of a judgment of meaning, so the wording keeps
  the judgment open rather than closing it to three shapes.
- **The condition is the `Pact` row.** A frame in a repository with no
  `Pact` row cites no pact, so the proofer's read costs nothing there.

**No case and no mutation run.** The change is prose in a skill. What can
fail is whatever parses that file (`skills/verify/SKILL.md` *The narrow
command still has to be able to fail*, the prose row), which the boundary
command below ran. `frame/design.md` *Out* leaves a behaviour eval for this
sentence to a later work item.

**Phase boundary, executed.** One `bin/test` command ran fourteen modules:
`tests/text/test_review_axes.py`, every module
`git grep -l "code-review/SKILL.md" tests/` lists, the module that globs
`skills/*/SKILL.md` (`test_chain_hooks_hardening.py`), the cited-section
module and the census module. It counted 988 passed, exit 0.
