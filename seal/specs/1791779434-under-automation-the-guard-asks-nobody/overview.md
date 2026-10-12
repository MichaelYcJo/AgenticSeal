# 1791779434-under-automation-the-guard-asks-nobody — overview

📋 implement applied
· spec:     `spec.md`, `plan.md`, `questions.md` of this item; `docs/worktree-guard-spec.md` §A, *The stop has two readers*, §*Creation consent* (the five sources, rule 1), §*Choice sites*, §*Known limits*; `docs/commit-review-gate-spec.md` §*Where the person said nobody would be answering, every stop is a deny*; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*, §*A claim held by a test*; `docs/the-record-layout.md` (changelog fragment); `skills/implement/orchestration.md` §*Orchestrator: how the work is routed*; `skills/code-review/orchestration.md` §*Orchestrator: a fix pass resumes the implementer*
· evidence: `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` — S1–S5, S7–S10, W2, `Corrected ·` A4, S2, S6, and four `Re-read ·` rows; in-place re-stamps in `seal/ledger/1791384154-…`, `1791384157-…`, `1791384160-…`
· verified: executed — the guard modules, the nine suite-wide guards and phase 2's modules (1316 passed, 1 skipped), each new case seen red at `c38f97d7` or through `mutation-check`, `evidence-check --strict` 0, `survivor-check` 0, `correction-check` 0, `uvx ruff check` / `format --check` 0, M1 and M2; read — the 93 drifted ledger rows' claims, Windows behaviour

## Why this work exists

Under `automation` the worktree guard asked the owner yes/no over a dirty
switch, so that row now denies to the model with the ways on that need
nobody, and a run resumed in a new session presses again so the press is
there to read.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When the ledger fragment is written | `plan.md` phase 2: "`seal/ledger/1791779434-….md` holds S1–S10's rows and the `Corrected ·` row for 0.20.0 S6". Phase 1's own rows, the corrections and the re-reads landed at phase 1's close (`8bdd6680`) | phase 1 | The spawn prompt closes each phase on `bin/evidence-check --strict` over the tree, and phase 1's edit drifted 45 rows; strict exits 2 until they are read again |
| How many released claims are corrected | `spec.md` S11 and the spawn prompt: "a `Corrected ·` citing row for the released 0.20.0 S6 row". Written: three, S6, S2 and A4 | three | 0.20.0 S2: "with the same verdicts and reasons" as before #826. 0.15.5 A4: "the switch direction reads neither consent". Both are false once the dirty row reads the press (`phases/phase-1.md`) |
| In 3's list of new sessions | `spec.md` In 3: "a new day, a `/clear`, another machine". Written: "a `/clear`, a new `claude` start, or another machine, and a new day is one only where it starts one" | the written list | M2: `claude --resume` keeps the session id and its transcript, so a new day resumed is not a new session |
| The lint command | Spawn prompt: `uv run --frozen ruff check` and `ruff format --check`. Ran: `uvx ruff` | `uvx ruff` | `uv run --frozen ruff` fails with *Failed to spawn: `ruff`*; ruff is no dependency of the project, and `CONTRIBUTING.md` names `uvx ruff check . && uvx ruff format .` |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck: `unverified`, because the broad run is the sealer's, once, after the rounds settle | the orchestrator, through the sealer |
| M3: whether the deny loops, that is, how many dirty-row denies a session meets at the next `automation` run, how many were the same switch re-issued, and whether any guard `ask` reached a person | the orchestrator of the next `automation` run, from its own transcript |
| That a `/clear` and a new `claude` start issue a new session id. M2 measured only that `--resume` and compaction keep it | the orchestrator, at the next `/clear` of a run, by the transcript's file name |
| Windows: the dirty row is reached there only under `[shared-tree-ok]` from the detection-unusable row, which S3 covers on macOS with the session count stubbed. Read from the code, not run on Windows | the Windows CI leg at the pull request |

## Not done

The issue P1's default (a) names, for the two choice rows under the press,
is not filed: this session posts nothing, and the frame names the
orchestrator as its filer.

The rows the edits drifted, 45 at phase 1's close and 48 at phase 2's as
`evidence-check --strict` counted them, were re-read rather than moved onto
their tests, apart from the three corrected below. `docs/the-evidence-ledger.md` asks the
drifting branch to write a test-held `Corrected ·` row "where reading the
claim shows a test holds it". Settling that for each family means reading
its tests against every clause of its claim. That was done for the three
rows corrected anyway (A4 and S6 moved onto their tests, S2 kept hashed
because no test holds *the ladder is otherwise unchanged*), and not for the
rest.

0.15.6 W9's *a dirty repository reached from elsewhere asks* is true
attended only, as are all its cases. It was judged to hold and re-stamped in
fragment `1791384157` without a note; a `Corrected ·` row narrowing it is
available to whoever wants the claim exact.

## Fed back into the spec

Inferred during implementation, so a planner may overturn each:

- `docs/worktree-guard-spec.md` §A, *The tracked-changes row has two readers
  too*: a detached HEAD is named as a check the model runs (`git branch
  --show-current` prints nothing) followed by `git branch <name>`, rather
  than read by the guard (W1).
- The same paragraph: the press is read against the root of the session's own
  directory, never the switch's tree, pinned from both sides (W2).
- §*Known limits* and `skills/implement/orchestration.md`: `claude --resume`
  and compaction keep the press (M2).
