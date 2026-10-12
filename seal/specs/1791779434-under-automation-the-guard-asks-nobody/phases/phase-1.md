# 1791779434-under-automation-the-guard-asks-nobody — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | 8bdd6680 |
| Ran by | unknown — the spawn prompt named neither the agent nor the model, and a segment does not supply that value about itself |

## What this phase was asked

Under the `automation` press, the tracked-changes row in
`hooks/worktree-guard.py#main` answers `deny` to the model with the ways on.
Attended, it stays byte-identical to the base's `ask`.
`hooks/commit-review-gate.py`, `hooks/worktree_consent.py` and
`hooks/cmdline_base.py` stay byte-identical to `c38f97d7` (S8). No new
reader, no fallback, and no heuristic about payload shapes: the design reads
the press the guard already reads. M1 is this phase's measurement, and W1 and
W2 are its choices, recorded here and in `overview.md`.

## What this phase found

**M1, executed: the diagnosis holds.** The session whose `smith` met both
stops is `20f122bc-1e8b-46c6-8158-88431e504d2d` on this machine. Stop 1's
command first appears at line 7042 of its transcript (04:02:51Z). Replayed
against the transcript cut just before that line,
`automation_answered(<main checkout root>, <that id>, "")` returns `False`.
The transcript holds one `AskUserQuestion` result in all, and it is the
routing question, answered `automation (Recommended)` at 04:59:51Z, line 7375
(put at line 7373, 04:45:29Z). That is after both stops. Read whole today,
the reader returns `True`, because the orchestrator put question 1 again by
hand, which is In 3 practised before it was written. The scripts ran outside
the suite from the scratch directory and wrote nothing under the repository;
the replay's copy of the transcript was deleted with its directory.

**W1, the text and the detached HEAD.** The deny opens with the row's
existing lead, the listing and the phantom note. Then it says the person
pressed `automation`, so nobody is asked and nobody is to be asked in its
place. Two ways on follow, each a command of its own, because `git stash &&
git switch <branch>` on one line meets the same row (S5). Way 1 is commit
here first. Way 2 is `git stash`, the switch, `git stash pop`, with what the
pop applies to. Every command carries `git_at`'s word, so a switch into
another tree names that tree. The text ends with the commit gate's sentence
about re-issuing unchanged. The detached HEAD is a check the model runs
(`git branch --show-current` prints nothing), followed by `git branch <name>`
before the switch. Reading HEAD in the guard would cost one more git spawn on
every dirty switch for a sentence the model can test itself. The commit
leaves the tree clean, so the later switch and the `git branch` are silent.
`git switch -c <name>` is not offered, because in a dirty tree it is a switch
and meets this same row.

**W2, where the press is read.** It is read inside the `if entries:` block,
against `repo_paths(cwd)[0]`, and not cached beside `seen`. Caching would buy
nothing: `stop_unrecognised` exits through `respond` whenever it fires, so a
command that reaches the ladder never read the press above it. A
mutation-check showed that no case told the session's own root from the
switch's tree. `test_the_press_is_read_from_the_sessions_own_root` now does,
from both sides.

**The ledger work moved into this phase.** `plan.md` puts the fragment in
phase 2. But `evidence-check --strict` closes phase 1, and the edit drifted
45 released and fragment rows citing `hooks/worktree-guard.py#main` and the
two cases this phase rewrote. Reading them found three claims that no longer
hold as written, where the frame named one:

- 0.20.0 S6, as the frame said.
- 0.20.0 S2: "the same verdicts and reasons" as before #826.
- 0.15.5 A4: "the switch direction reads neither consent". The
  unrecognised-shape stop had read the routing answer since #826, and A4 was
  re-read as holding then.

Each takes a `Corrected ·` row in this item's fragment, A4 and S6 held by
their tests from here on, S2 hashed because no test holds *the ladder is
otherwise unchanged*. The corrections were written before `--reverify
--into`, so the other work item's `Re-read · A4` and `Re-read · S2` rows were
superseded rather than re-stamped as holding. The rest were read and judged
to hold: the in-place re-stamps went to fragment
`1791384157-the-hooks-read-the-session-waiver-and-creation-one-way`, and one
`Re-read · W4` row went here. Two claims are true attended only, as every
case they cite runs: W4's *the verdict is unchanged*, which the W4 row's note
says, and W9's *a dirty repository reached from elsewhere asks*, whose
re-read is that other fragment's in-place re-stamp and carries no note. A
`Corrected ·` row for W9 is a reading somebody may want; nothing here was
falsified by it.

**`uv run --frozen ruff` cannot start ruff in this project**: ruff is no
dependency of it. `uvx ruff` is the spelling `CONTRIBUTING.md` names, and it
is what ran.

## What this phase removes

| Removed item | Where it must land |
|---|---|
| 0.20.0 S6's claim that the plain retry in a dirty tree is the `ask` under the press | `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md`, `Corrected · S6` |
| `test_the_plain_retry_meets_todays_rows`'s `ask` assertion on the retry | the same case, now asserting S1's `deny` text |
