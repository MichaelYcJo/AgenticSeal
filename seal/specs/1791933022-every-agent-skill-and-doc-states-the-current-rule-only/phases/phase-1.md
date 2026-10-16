# 1791933022-every-agent-skill-and-doc-states-the-current-rule-only — phase 1

| Field | Value |
|---|---|
| Phase | 1 |
| Commit | c7d8bcc8 |
| Ran by | specseal:smith on Opus 5.5, two spawns — the model read off each commit's `Co-Authored-By` line, since this record was written afterwards by phase 2's spawn |

## What this phase was asked

`plan.md`'s row 1, in two acts. (i) The proof made light: every `rule-*.md`
grader removed and `rule_cases.py` writing outcome graders only; the rule
census and the owed-record coupling removed; `noninferiority.py run`
recording `total_cost_usd`, `duration_ms` and `usage` per run, `compare` and
`verdict` carrying pass rule 4, and a run with no cost pooling to unknown;
`replay-1791852615-r2` and `seeded-770d721f` replaced through the
generators; `evals/README.md` rewritten in place. (ii) The five eval cases
that predate 0.22.0 (#946) each fixed to the runner's measured schema or
removed, and `tests/test_evals_layout.py` applying that schema to every case
under `evals/`.

## What this phase found

**The acts landed as seven commits.** Act (i): a5c6971c (the 149 sentence
graders gone, the layout test refusing a `rule-` grader), be8802db (cost
recorded per run, rule 4, the census and `owed_records` gone), 50e60e4c (a
side with one run of two missing its cost pools to unknown), 311beed0 (the
two cases replaced through `--case`), ab20e4a4 (`evals/README.md`), 1d8e1ff0
(the overview's two divergences). Act (ii): c7d8bcc8.

**`plan.md` and `spec.md` name act (i) by pre-rebase hashes.** a4952d90,
6cfea707, 7f4b3046, e38f2dfa and bb519165 are commit objects in the clone
and none is an ancestor of this branch (`git merge-base --is-ancestor`,
exit 1 each). The commits above are the same acts on the rebased branch.

**None of the five pre-0.22.0 cases could run as written, and all five
left.** Each case's grounds are its row in `overview.md` §*Where spec and
implementation diverged*. Two outcomes no case reads now, a bare session's
use of implement or code-review and a PR body written to writing-style, are
a row in `overview.md` §*Not verified*.
