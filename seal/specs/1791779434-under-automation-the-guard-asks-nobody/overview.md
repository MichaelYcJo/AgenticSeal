# 1791779434-under-automation-the-guard-asks-nobody — overview

📋 implement applied
· spec:     `spec.md`, `plan.md`, `questions.md` of this item; `docs/worktree-guard-spec.md` §A, *The stop has two readers*, §*Creation consent* (the five sources, rule 1), §*Choice sites*, §*Known limits*; `docs/commit-review-gate-spec.md` §*Where the person said nobody would be answering, every stop is a deny*; `docs/the-evidence-ledger.md` §*A released row is read again in the branch's fragment*, §*A claim held by a test*; `docs/the-record-layout.md` (changelog fragment); `skills/implement/orchestration.md` §*Orchestrator: how the work is routed*; `skills/code-review/orchestration.md` §*Orchestrator: a fix pass resumes the implementer*
· evidence: `seal/ledger/1791779434-under-automation-the-guard-asks-nobody.md` — S1–S5, S7–S10, S12, W2, `Corrected ·` A4, S2, S6, W9, and four `Re-read ·` rows, S1, S4, S9 and `Corrected · S2` restated at the reframe; in-place re-stamps in `seal/ledger/1791384154-…`, `1791384157-…`, `1791384160-…`
· verified: executed — the guard modules, the nine suite-wide guards and phase 2's modules (1316 passed, 1 skipped), each new case seen red at `c38f97d7` or through `mutation-check`, `evidence-check --strict` 0, `survivor-check` 0, `correction-check` 0, `uvx ruff check` / `format --check` 0, M1 and M2; read — the 93 drifted ledger rows' claims, Windows behaviour

## Why this work exists

Under `automation` the worktree guard asked the owner yes/no over a dirty
switch, so that row now denies to the model with the facts it read and the
commands that pass it, and a run resumed in a new session presses again so
the press is there to read.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| When the ledger fragment is written | `plan.md` phase 2: "`seal/ledger/1791779434-….md` holds S1–S10's rows and the `Corrected ·` row for 0.20.0 S6". Phase 1's own rows, the corrections and the re-reads landed at phase 1's close (`8bdd6680`) | phase 1 | The spawn prompt closes each phase on `bin/evidence-check --strict` over the tree, and phase 1's edit drifted 45 rows; strict exits 2 until they are read again |
| How many released claims are corrected | `spec.md` S11 and the spawn prompt: "a `Corrected ·` citing row for the released 0.20.0 S6 row". Written: three, S6, S2 and A4 | three | 0.20.0 S2: "with the same verdicts and reasons" as before #826. 0.15.5 A4: "the switch direction reads neither consent". Both are false once the dirty row reads the press (`phases/phase-1.md`) |
| In 3's list of new sessions | `spec.md` In 3: "a new day, a `/clear`, another machine". Written: "a `/clear`, a new `claude` start, or another machine, and a new day is one only where it starts one" | the written list | M2: `claude --resume` keeps the session id and its transcript, so a new day resumed is not a new session |
| The lint command | Spawn prompt: `uv run --frozen ruff check` and `ruff format --check`. Ran: `uvx ruff` | `uvx ruff` | `uv run --frozen ruff` fails with *Failed to spawn: `ruff`*; ruff is no dependency of the project, and `CONTRIBUTING.md` names `uvx ruff check . && uvx ruff format .` |
| The deny's text, reframed after round 3 | The first frame's In 2: "names the ways on that need nobody, each as a command of its own: 1. commit the changes here first … 2. `git stash`, then the switch, then `git stash pop`". Phases 1 to 2 and two fix passes built that, and each of rounds 1 to 3 found a switch form it was wrong for. The reframed In 2: "The reason states what the guard read, and infers nothing beyond the index-residue note it shares with the `ask`" | the reframe, built in phases 3 and 4 | `spec.md` §*Why the deny predicts nothing*: fourteen of round 3's sixteen setups held and two did not, with no fact the guard reads to tell them apart. The press sentence stayed byte-identical for #896 |
| Where the `Enforced by:` line moved | `plan.md` phase 4: the line "losing the three removed cases and gaining S12's". Done in phase 3 (`6beb4b21`) | phase 3 | The removed cases would have failed `tests/test_a_folded_statement_names_what_enforces_it.py` at phase 3's close; the paragraph's prose moved in phase 4 |
| Records naming the removed cases | Not in the plan. 23 lines across `spec.md`, `plan.md`, `questions.md` and six round records, then `phases/phase-3.md`, named a removed case | `NAME NOT IN TREE` on each line, in phase 3 | `tests/test_a_record_states_what_the_tree_has.py` refuses a record naming what the tree lacks, and that marker is its prescribed repair; every verdict and ground stays as written |
| The lead's first clause | Not in the plan. The lead's *so the switch itself may go ahead* became *so no other row of this guard stops the switch* | the guard's own fact | git refuses `--orphan` over the changes, so *may go ahead* was a prediction too (`phases/phase-3.md`) |

## Not verified

| Item | Who must answer |
|---|---|
| closed The full suite, the repository-wide lint and the typecheck: `unverified`, because the broad run is the sealer's, once, after the rounds settle | #897, merged with lint and the suite green on the ubuntu, macOS and Windows legs; the repository configures no typecheck |
| closed M3: whether the deny loops, that is, how many dirty-row denies a session meets at the next `automation` run, how many were the same switch re-issued, and whether any guard `ask` reached a person | another session's behaviour: the re-issue bullet of `docs/worktree-guard-spec.md` *Known limits* |
| closed M4: whether a model told less finishes what it started, that is, stashes left with no pop or apply after them and commits left on a detached HEAD with no branch named | another session's behaviour: the same bullet of `docs/worktree-guard-spec.md` *Known limits* |
| closed That a `/clear` and a new `claude` start issue a new session id. M2 measured only that `--resume` and compaction keep it | a live harness: the press bullet of `docs/worktree-guard-spec.md` *Known limits* |
| closed Windows: the dirty row is reached there only under `[shared-tree-ok]` from the detection-unusable row, which S3 covers on macOS with the session count stubbed. Read from the code, not run on Windows | #997's `windows-latest` leg ran the guard's modules green |

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

0.15.6 W9's *a dirty repository reached from elsewhere asks* was true
attended only. Round 1's note 3 gave it a `Corrected ·` row, and round 2's
note 3 put its re-read row in fragment `1791384157` back at the base's hash.

P3, whether the deny should name `git stash` at all, stands at its default
(a): both commands, as the attended `ask` names both. M4 is the count that
would move it.

## Fed back into the spec

Inferred during implementation, so a planner may overturn each:

- W1's detached-HEAD sentence, inferred in phase 1, was taken out at the
  reframe with every other per-form sentence; the policy paragraph now says
  why (*Why the row's own sentences predict nothing*).
- `docs/worktree-guard-spec.md` §A, *The tracked-changes row has two readers
  too*: the lead's first clause is a fact about the guard, *no other row of
  this guard stops the switch* (phase 3).
- The same paragraph: the press is read against the root of the session's own
  directory, never the switch's tree, pinned from both sides (W2).
- §*Known limits* and `skills/implement/orchestration.md`: `claude --resume`
  and compaction keep the press (M2).
