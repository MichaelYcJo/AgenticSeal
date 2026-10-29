# Questions for the planner: 1793251201-a-push-only-workflow-answers-a-deferral

## Settled from the tree

These are the judgments #1123 left open that the tree or a probe answered.
Each answer's grounds are in `frame/design.md` or `plan.md`, and nobody
reopens them without opening those grounds first.

- **Which spellings fail open at this base.** Probes 1 and 2 at `ea08c39c`
  (executed, `frame/design.md` *Grounding*) enumerate them: `"on":`,
  `'on':`, an event block at four spaces, a block sequence at indent zero,
  a multi-line flow list, no `on` key, and an event key carrying a value or
  a comment on its line. The audit's measurement at `c825fd2c` holds here,
  because `deferral_check.py` has not changed since (executed).
- **Whether "seen red against `c825fd2c`" needs a checkout of that
  commit.** It does not: the script and its test module are identical at
  `c825fd2c` and this branch's base (executed), so a case red at the base
  is red against `c825fd2c`'s script.
- **Whether a partly read trigger counts as the events it did read.** It
  does not. One unreadable element makes the whole trigger unread
  (`frame/design.md` *Scope* item 2, and `plan.md`'s last Alternatives row).
- **Whether the closing sentence "Deferring <kinds> to CI names an
  answerer that is not there." changes.** It stays. A workflow whose
  trigger nobody read is not an answerer the deferral row can name, and
  the `unread` line beside it says why the kind did not resolve. A
  different answer would change one string and not what gets built.
- **Whether a policy rule changes.** No policy document covers
  `seal deferrals` (`docs/README.md`, read), so `## Rule changes` holds the
  no-change block.
- **Whether the replay eval's line-number pin moves with this edit.** It
  does not: `scaffold.sh` checks out `7ef6abbf` (read).
- **Whether a parallel work item edits a file this one changes.** None
  does at the time of framing. The three branches
  `test/1127-the-citation-case-misses-files-and-wrapped-comments`,
  `fix/1132-seal-pact-passes-near-misses-of-an-anchor` and
  `feat/1158-the-framer-is-handed-the-body-without-its-comments` each
  differ from `8d8d6390` by their `routing.md` alone (executed,
  `git diff --name-only 8d8d6390...<branch>`). Their uncommitted frames
  name none of this work's files as an edit: #1132's and #1158's mention
  none of them, and #1127's reads `README.md` and `README.ko.md` as part
  of its corpus and lists `deferral_check.py` among the files it does not
  edit (executed `grep`, and read).

## Rows

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| W1 | The wording of the `KNOWN_LIMITS` clause, of the fifth outcome in `skills/verify/SKILL.md` *The answerer has to exist* and the module docstring, and of the added outcome in `README.md`'s and `README.ko.md`'s `seal deferrals` rows. `frame/design.md` *Scope* items 4 and 5 fix what each says; the sentences are written where they are built | the work: phase 1 | Any wording that says an unread trigger is reported and not counted, names a flow mapping in the limit, and keeps the two README editions saying the same thing. The choice goes into `trail/phases/phase-1.md` | The shortest sentence that meets those conditions | answered 2026-10-29 by the crafter: the wording `trail/phases/phase-1.md` *What this phase found* records |
