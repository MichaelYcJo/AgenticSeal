# tests rebuilt one file per module (#942) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. -->

Under `routing.md`'s `Automation` row nobody answers a row during the run. The build proceeds on each row's default, and the pull request body names the rows it built on.

## What the tree answered, so nobody reopens it

- The `Reads:` census and `tests/undeclared_readers.txt` are gone (executed: no `tests/*.txt` at a16acb40), and the two group sentences stand in `agents/smith.md` line 98 and `agents/warden.md` line 131 (executed grep). The issue's item 4 and its sentence about #923 are done; phase 1 adds only the command name.
- Where the placement check and the pairs report live: one script, `skills/verify/scripts/test_layout.py`, run as a suite case and as `bin/test-layout`, because #929 removed the `cases` job and a check as a case needs no job (`plan.md` Alternatives).
- Where the per-module report lives: `.github/scripts/release_report.py`, which already reads `.test_durations` in the head and the tag trees; the rows are the same reading grouped by file.
- The pair of cases is named by prefix, `test_accepts_` and `test_refuses_`, because a check reads a spelling and a word list of near synonyms is a spelling a near miss passes. Any two fixed prefixes would serve; these are the gate's own words.
- `CONTRIBUTING.md` is not under `docs/`, so its paragraphs change by plain edit and not through `## Rule changes`; only `docs/release-checklist.md` goes through it.
- No `git init` helper is a twin at a16acb40 (executed, by `ast` over `tests/*.py`), so the issue's fixture for them is the existing `repo` fixture extended to a module-scoped world.
- The twin count is 141 definitions and not the issue's 249: the issue measured before #929 and #944.

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | Does the commit gate keep its text reading (`hooks/cmdline.py` and the PreToolUse reading in `hooks/commit-review-gate.py`)? The tree cannot answer it: the reading alone judges a foreign hooks slot and an unreached clone, no record since #692 shows it catching a commit, and nothing counts installs in either state, so the weighing is a value judgment under `CONTRIBUTING.md` *What a change to a gate must carry* | a person | keep: the three files are sampled per kind on #929's pattern in phase 5, 725.8 Windows seconds at a16acb40 become a sample. remove: a work item of its own takes out the reader, the reading and the three files whole, and phase 5 skips them | keep | answered 2026-10-22 by the repository owner: the default |
| Q2 | Is 60 seconds the threshold at which a module's tests are written anew rather than trimmed? At a16acb40 it selects the sixteen files that hold three quarters of the suite's seconds; a lower value rewrites more modules from the code, a higher one trims more. The tree has no rule for the value | a person | 60 s: sixteen files rewritten. 30 s: the smith recounts, more files rewritten. 120 s: fewer | 60 s | answered 2026-10-22 by the repository owner: the default |
| Q3 | Which cases of a heavy module are cut, and which `run_gate` call sites of the sealer file share one run: unknowable until the mutation table runs at the build's tree | the work | decided per module in phase 5's record | the table decides | open |
| Q4 | Which flows besides the commit gate belong under `tests/e2e/`: the worktree guard's switch and creation arms run real git too, and whether their cases are a flow or module cases is read from the files at the build's tree | the work | decided in phase 5 or 6 when the files are read | the commit flow alone until a batch finds another | open |
| Q5 | What the suite costs in CI minutes after the rebuild: only the release report at the next release measures the Windows seconds and the legs' minutes | a measurement | read off the release table at the next release pull request | the local wall time in phase 7's memo stands in | open |

**`Who can answer` takes one of three values and nothing else.** They were one
shape on the page before this, and #84's second comment measured all three
inside a single run's four rows.

- **a person** — what the product should be, or a value somebody has to be
  accountable for. This is the file's stated purpose, and the only kind of row
  that blocks the build.
- **a measurement** — a probe, a command or a count settles it, so asking a
  person is the wrong instrument and queueing it behind one wastes a round
  trip.
- **the work** — unknowable at framing time. The phase that meets it decides
  it there and records a divergence row; it does not travel back to the
  framer.

**The framer opens rows and does not own their answers.** The `Status` column
is written by whoever answered, as `answered <date> by <who>`, never by
whoever asked.
