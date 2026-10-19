# the scribe and legacy-parity are written anew from the scribe's job (#970) — questions for the planner

<!-- seal/specs/<unix-epoch-seconds>-<slug>/questions.md — decisions only a human can make,
extracted so nothing ships on a silent assumption. Before adding a row,
check the inheritance rule: if policy is silent but existing behavior
answers it, inherit and record — only genuinely NEW rules belong here. -->

## What the tree answered, so nobody reopens it

The ticket and its comment left these open and the repository settled them;
the grounds are in `spec.md` and in `plan.md`'s Alternatives table.

- **The four verdict words are `differs`, `grounded`, `equivalent` and
  `unread`.** #957's `spec.md` §*Marks and labels* and §*Data & interfaces*
  chose them under the owner's rule of 2026-10-16; this item applies them.
- **The writer of the parity mark (C5)** is the party that compared and
  whose definition names the write: the warden in a review round
  (`agents/warden.md` §*Job*, step 5), a session where it compared itself.
  The scribe writes nothing durable and the smith's definition names no
  parity mark (#2's C1).
- **The policy root (B5)** is a placeholder with `none` as a value, and no
  setup proposes creating `docs/policies/`: `implement`'s layout says a work
  item does not create a policy document, and
  `skills/implement/orchestration.md:52-55` says the same of
  `docs/policies/<domain>/` (Alternative H).
- **The byte figure that has to hold is the read set**, not the preload,
  because the scribe opens `legacy-parity` at step 1 of every spawn (#957's
  preload paragraph; Alternative E).
- **The smith and the warden are not measured again**: their steps open
  `legacy-parity` only where `seal/parity.md` is declared, and no case under
  `evals/` declares it (Alternative I).
- **The scribe does not open `writing-style`**: its report is facts for a
  caller, and #957 named `legacy-parity` alone for it (Alternative F).
- **The scribe is spawned by the session**, not by the smith: contract §6
  and `agents/smith.md` §*Never* withhold the spawn from every agent.
- **The README sentences naming the smith as the party that asks a setup
  question** (`README.md:234`, `:421`, `README.ko.md:226`, `:379`) are one
  class with the scribe's description and are corrected together (contract
  §12).
- **`SKIP` leaves rather than staying empty** (Alternative G).
- **The hook messages and `docs/the-review-and-parity-arms.md:210` stay**:
  they name the procedure the mark comes from (Alternative J).

| # | Question | Who can answer | Options & what each implies | Default until answered | Status |
|---|---|---|---|---|---|
| Q1 | **Who records the comparison for a smith's commit in a repository that declares `seal/parity.md`?** The smith's definition names no parity mark among its writes (#2's C1), and a routing declaration does not quiet the parity arm (`skills/implement/orchestration.md:458-466`), so every code commit a smith makes there meets the parity ask, under `automation` too. The tree cannot answer it because it is a design choice between two rules the owner set, and #970 asks for neither | a person — the owner | **leave as it stands** (the default): this item names the writers the tree already has and changes nothing the gate does; the owner may open an issue · **open an issue now**: the orchestrator files it with this row's text, and #970 still builds as framed | leave as it stands; the run does not stop | answered 2026-10-19 by the repository owner: a defect, since every `automation` run in a parity repository stops at the smith's first code commit; filed as #988 in 0.22.3, after this item names who writes the parity mark. #970 builds as framed |
| Q2 | **Does the read set fall to or below 25,691 B?** The rewrite adds `Enforced by:` lines and a writer sentence to `legacy-parity` and `## Rules` to the scribe, and removes the field table, narration and the contract paragraph | a measurement — phase 3's `payload-meter --agent scribe` plus `legacy-parity`'s bytes at the build's commit | — | the acceptance in `spec.md` S12 | open |
| Q3 | **Which of the scribe's and `legacy-parity`'s pins hold a rule, and which narration?** Five modules name the scribe, three name `legacy-parity` (`plan.md` §*Technical context*) | the work — phases 1 and 2 sort them, re-pointing a pin on a rule that stays and removing one on narration with a line in the phase record (#957's Q7) | — | — | open |
| Q4 | **Which module holds T5?** `tests/test_review_axes.py` is the one that pins `legacy-parity` today; the smith's rule *a new test starts from its group* may find a closer group | the work — phase 1 reads the group and names the module in the phase record | — | `tests/test_review_axes.py` | open |
| Q5 | **Which item merges second on the lines #968 also edits?** `plan.md` §*Lines another item also edits* | the work — the rebase of whichever lands second, which removes `NOT_YET_REWRITTEN` whole where it is empty and recounts the README's skills | — | — | open |

**`Who can answer` takes one of three values and nothing else.**

- **a person** — what the product should be, or a value somebody has to be
  accountable for. Q1 is this kind, and it does not block the build: it
  carries the default the run takes.
- **a measurement** — a probe, a command or a count settles it. Q2 is read
  off phase 3's command.
- **the work** — unknowable at framing time. Q3 to Q5 are decided by the
  phase that meets them and recorded there.

**The framer opens rows and does not own their answers.** The `Status`
column is written by whoever answered, as `answered <date> by <who>`, never
by whoever asked.

Answered rows feed back into docs/ (policy clause or open-questions section)
before this directory's work merges.
