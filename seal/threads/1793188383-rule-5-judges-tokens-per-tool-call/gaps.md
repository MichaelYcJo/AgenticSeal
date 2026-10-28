# Overview: 1793188383-rule-5-judges-tokens-per-tool-call

## Why this work exists

Rule 5 failed rewrites that made fewer calls and read fewer tokens in all, and rises under one percent decided it; it now fails a side only where its total and its tokens per tool call both rose past `TOKEN_MARGIN`.

## Where spec and implementation diverged

| Divergence | Spec says / code did | Chosen | Grounds |
|---|---|---|---|
| What `check`'s exit code says on a re-read record | `frame/plan.md`, phase 2's *Verified by* cell: "17 `check` runs, each exit code read directly: 0 for `pass` and 1 for `fail`". `check` exited 1 on `967-framer-p4`, `967-warden-p4` and `943-sealer-p3b`, whose numbers give `pass`, and on `957-warden-p2` at the base and after | The computed verdict is read from the line `check` prints, and the exit code is recorded beside it in `trail/phases/phase-2.md` | `noninferiority.py#check` returns 1 whenever `check_record` reports a problem, and `read_record` reports a record whose stated verdict differs from the verdict its numbers give. `frame/plan.md` *Operational impact* itself predicts "it says `fail` and its numbers give `pass`" on those three records. S9's verdict prediction holds on all 17 records |

## Not verified

| Item | Who must answer |
|---|---|
| The full suite, the repository-wide lint and the typecheck over the branch | the orchestrator, at its one `seal gate` run (contract rule 2) |
| `TOKEN_MARGIN`'s size, built on `frame/questions.md` Q1's default of 0.07 | the owner, who answers Q1; a different value changes the one constant, and S5 and S7 read it |
| The spread of the total tokens between two takes of one tree, which the margin is applied to with no measurement of its own | a measurement of two paid sides of one tree for one agent (`frame/questions.md` Q3), taken in the release the owner chooses to pay for it |

## Not done

Rules 1 and 2 judged against a baseline drawn high. The issue's section *The
same shape on rules 1 and 2* widens its question to every rule judged
against one baseline side at two runs a case. This work changes rule 5
alone, on `frame/questions.md` Q2's default, "rule 5 alone". Any change to
rules 1 and 2 needs a baseline pooled from several paid sides of one suite,
or a decision that those rules become a report, and Q2 holds that choice
for the owner.

## Fed back into the spec

none
