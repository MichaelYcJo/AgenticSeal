# 1792363189-rule-3-decides-on-the-agent-not-one-run — review round 1

target: 4279671d against release/v0.22.2

## Findings

### 1. #957's spec still states the per-grader rule 3 as the standing rule, where `settle` will fold it

severity: should
location: `seal/specs/1792126889-every-agent-is-written-anew-from-its-job/spec.md:224-227`
verdict: open

Why it matters. #957 shipped in 0.22.1 (`git tag --contains 2fc33333`
prints `v0.22.1`), so its `spec.md` is now the input `settle` folds into
`docs/`. `skills/settle/SKILL.md` keeps a released item's SDD set until the
fold absorbs it. Its §*How the rewrite is proved not worse* still says
`verdict`'s rules include "each shape and reach grader passing on the new
side at least as often as on the baseline". A few lines later it adds "This
rule holds unchanged for every later phase". The session that folds #957
reads that sentence as a standing rule. The code it would describe no
longer exists. No document under `docs/` states the evaluation's rules (this
work item's `spec.md` §*Grounding*), so nothing in `docs/` would contradict
the folded sentence.

Grounds, read. This work item's own Grounding row cites `CLAUDE.md`
§*The rule a mechanism is kept against* and contract §19: "Every sentence
stating the per-grader rule is rewritten in place, in the commit that
changes the code. `git grep` on its words is how they are found". Scope
item 4 then limited the grep to `evals/` and `tests/`, and this sentence
sits outside both. The caller asked whether any statement of the old rule
survives anywhere in the tree. I searched `git grep -n -i -e "at least as" -e
"as often" -e "less often" -e "per.grader" -e "each shape" -e "rule 3" -e
"shape and reach"` over the whole tree. A second search for `grader`,
`noninferiority`, `not worse` and `against the baseline` covered `docs`,
`skills`, `agents`, `templates`, `hooks`, `bin`, both READMEs,
`CONTRIBUTING.md` and the changelogs. Every survivor, enumerated (§12):

- `seal/specs/1792126889-…/spec.md:224-227`: this finding. It states the
  rule as standing, in a file the fold reads.
- `seal/specs/1792126889-…/plan.md:151`: phase 1b's row, closed at
  `ad1a93a2`. It says what that phase delivered, which is still true, so it
  is not part of this finding.
- `seal/specs/1792126889-…/phases/phase-1b.md:14`, `:45`: process record,
  which `settle --retire-process` removes. Not part of this finding.
- `seal/specs/1792126889-…/evals/*.md`, the old reason lines: out of scope
  by this work item's `spec.md` §*Scope*, Out, with its reason.
- `.test_durations:1578`, `:1583`: the two old case names. Out of scope by
  `spec.md` §*Scope*, Out.

Nothing in `docs/`, `skills/`, `agents/`, `templates/`, `hooks/` or `bin/`
states the evaluation's rules at all, old or new (read).

The fix rewrites the rule 3 clause in place. It points at the rule's one
home and keeps the sentence true of #957's own phases, which were judged
per grader:

```markdown
`evals/scripts/noninferiority.py#verdict`'s rules after phase 1b: recall not
fallen, false rate within `FALSE_MARGIN` of the baseline's, the shape and
reach graders as rule 3 of `evals/README.md` §*The behaviour suite* states
them (#957's phases judged each grader on its own; #966 pooled them per
agent in 0.22.2), preload bytes below the baseline, and the tokens the run
read across every
```

answer:

## Confirmations

confirms: none
Rule 3 is built as `spec.md` *Data & interfaces* says (read,
`evals/scripts/noninferiority.py:660-693`). `common` holds the shape and
reach graders with old runs and new runs both above zero, sorted by
`(case, grader)`. Every grader in it has equal runs on both sides, because
the "different number of times" check at `:623-628` returns `no result`
otherwise. So the one `{runs}` printed for both sides is true. The total
line fires on `new_total < old_total` only, so equal totals pass. The
naming line needs `op` at 1 or more and `np_` at 0. The baseline-lacks
condition and text are those of 769f2aa4. The lines come in the order total,
naming, baseline-lacks, each sorted. The axes, walked: the signature and
input of `verdict` are unchanged; the change adds no failure path, and every
`no result` check above rule 3 is untouched; it adds no I/O, so the
concurrency and security axes have nothing to reach.

confirms: none
The implementer's account says each new case was seen red (`phases/phase-1.md`,
the table under *Each new case seen red*). I settled each one by reading the
code against the case's numbers rather than re-running `mutation-check`
(read). S1 and S5 fail under 769f2aa4's `np_ * oruns < op * nruns`. S2 and the
reach rename pass with the total check removed, since no grader there falls
to 0. S3 passes with the naming clause removed, since its totals are 4 and 4.
S4 fails under a clause naming every 0/n grader. S6 passes with the filter
widened to `v[4]`: old 4 against new 5.

confirms: none
Each new test was read against its group (read,
`tests/test_a_rewritten_definition_proved_non_inferior.py:106-206`, `:329-376`).
S1 looked like a duplicate of S5 at first, but it is not. A rule 3 that
judges shape graders per grader and puts reach graders only in the total
fails S1 and passes S5, and no other case catches that partial rewrite.
`RULE_3_REASONS` asserts whole reason lists, which no `CASES` entry reads. Its
third entry is the only test of the line order and of the sort inside the
total line.

confirms: none
S9 holds, executed at 4279671d in a scratch clone. `compare` for the six
records against #957's committed side JSONs exited 0 each, and `cmp`
against this work item's committed `evals/957-*.md` exited 0 for all six.
`diff` against #957's records shows that `warden-phase-3`, `smith-phase-3`
and `framer-phase-3` are identical. The other three differ only in their
verdict block. `check` on the six new records exited 0, 1, 0, 0, 1 and 1
for `warden-phase-2`, `warden-phase-2-run-1`, `warden-phase-3`,
`smith-phase-3`, `framer-phase-3` and `sealer-phase-3`. None printed "it
says … and its numbers give …". The verdicts match `spec.md` S9's
predictions. `check` on #957's own `warden-phase-2.md` exited 1 with "it
says `fail` and its numbers give `pass`", which is the side effect
`plan.md` §*Operational impact* names.

confirms: none
S8 holds in `evals/` and `tests/`, read. The implementer reported that
`git grep "at least as often"` cannot see the two docstrings. That holds:
the old sentences broke across a line inside the phrase, which
`git show 769f2aa4:evals/scripts/noninferiority.py` confirms at its lines
27-28 and 586-587. The wider search under finding 1 replaces that grep.
`evals/README.md:32-35`, the module docstring at
`evals/scripts/noninferiority.py:27-30` and the `verdict` docstring at
`:587-589` each state the total and the naming clause. None compares
graders one by one. The `as often`/`less often` lines at
`evals/scripts/noninferiority.py:36`, `:944` and
`tests/test_a_rewritten_definition_proved_non_inferior.py:597` are the
`model` subcommand's rule, which `questions.md` Q1 leaves alone.

confirms: none
Out of scope stays out (read, `git diff 769f2aa4..4279671d`).
`cheaper_model`, `evals/behaviour/` and `--runs` are not in the diff. The
diff touches no code after phase 1: `git diff --stat 8c244ae0..4279671d --
evals tests` prints nothing (executed). So the caller's narrow run at
8c244ae0 still covers the code under review. I carried that run. Nothing
else was carried, because there is no earlier round.

confirms: none
`plan.md` §*Operational impact* says nothing in the tree runs `check` over
committed records. That holds: `git grep` for `noninferiority` and
`check_record` in `.github`, `bin`, `hooks`, `skills`, `agents` and `docs`
finds nothing (read). The changelog fragment's statements match the code
and the six records: the two reason-line forms, the case where one run
still decides, and the table (read, `changelog.md`).

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck: unverified | the branch at 4279671d | the orchestrator, by `broad-gate --base release/v0.22.2` after the rounds settle |
| Whether the S1 to S6 breaks, run through `mutation-check`, went red as `phases/phase-1.md` reports. Settled by reading above, not re-executed | `phases/phase-1.md`, the seen-red table | the orchestrator, who may re-run any one of them; the sealer samples claims |

## Probes

| Command | Result |
|---|---|
| `git clone --no-local` of the repository into `<scratch>/1792363189-rule-3-decides-on-the-agent-not-one-run/round-1/clone`, then `git checkout 4279671d` | exit 0; removed before hand-back |
| `git diff --stat 8c244ae0..4279671d -- evals tests` | no output |
| `python3 evals/scripts/noninferiority.py compare --agent <a> --phase <N> --old <#957>/evals/baseline-<a>.json --new <#957>/evals/<name>.json --out <scratch>/out/957-<name>.md`, six times | exit 0 each |
| `cmp` of each output against `seal/specs/1792363189-rule-3-decides-on-the-agent-not-one-run/evals/957-<name>.md` | exit 0 each |
| `diff` of each `957-<name>.md` against #957's `evals/<name>.md` | `warden-phase-3`, `smith-phase-3`, `framer-phase-3`: exit 0; the other three differ in the `Verdict:` block only |
| `python3 evals/scripts/noninferiority.py check` on each of the six new records | exit 0, 1, 0, 0, 1, 1 in the order of `spec.md` S9's table; each `fail` printed only `its numbers give \`fail\`:` and its reasons |
| `python3 evals/scripts/noninferiority.py check` on #957's `evals/warden-phase-2.md` | exit 1, "it says `fail` and its numbers give `pass`" |
