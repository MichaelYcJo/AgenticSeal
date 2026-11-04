# Review round 1: 1793795305-the-behaviour-suite-is-a-smoke-run

```seal
target: c6b0fecb6 against release/v0.32.0
```

The target is the branch at `c6b0fecb6` against `release/v0.32.0`, which
is `479a79d15`, the commit `origin/main` names (executed:
`git rev-parse release/v0.32.0 origin/main`). The round read the ten
commits from `bac426446` to `c6b0fecb6`, the frame fold `c6b0fecb6`
among them. It worked in a `git clone --no-local` of the repository under
the session's scratchpad. No earlier round exists, so no fact is carried
and every verdict below was reached this round. `seal/parity.md` is
absent, so no original was compared.

Stage 1 read the code against `skills/core/SKILL.md`, issue #1254's body
and its one comment, `frame/design.md`, `frame/plan.md` and
`frame/questions.md`. Stage 2 read correctness and test quality. The
axes were the verdict's inputs (which keys `verdict` reads), its
exclusions and boundaries (each rule's edge, each `no result` arm), its
error paths (what still gives `no result`), and the order of its reason
lines. Two more axes were added for this change: the text a person reads
(the record's title, the reason suffixes, both READMEs, the changelog
fragment), and the callers of `verdict` that inherit its narrower
`no result` (`cheaper_model`, `read_record`, `check_record`). Security
and concurrency have no surface here: the change is pure functions over
numbers and text.

## Findings

This round opens no finding.

## Confirmations

What matched: the three pass rules state what the issue's *What changes*
asks. The issue reads "the new side's shape and reach graders, read
against a recorded baseline. Recall, the false-finding rate and the token
figures are recorded and judge nothing, and the preload's bytes are read
with no run" (executed: `gh issue view 1254 --json body`).
`evals/README.md:19-22` states the smoke run and that a pass claims
nothing about meaning. `evals/README.md:40-44` numbers three rules, one
for each clause of the old rule 3, in the old order.
`evals/README.md:46-53` writes the other figures as judging nothing and
keeps three `no result` causes. `evals/scripts/noninferiority.py:760-839`
does the same. It returns `no result` for a cut side (`:773-779`), for a
case the new side did not run (`:784-792`) and for unequal run counts
(`:797-803`). It then gives rule 1 the pooled total (`:811-826`), rule 2
the named grader (`:827-832`) and rule 3 the grader the baseline lacks
(`:833-838`). Each reason ends in its own number. It reads no key but
`graders`, `old_cut` and `new_cut` (read). The two passages of the
issue's *What stays* stand: the cases under `evals/behaviour/`, untouched
by the diff (executed: `git diff --stat 479a79d15..HEAD`), and
`evals/README.md:54-55`, "Nothing in the tree makes a later edit owe a
run".

What matched: S1's claim that the preload's bytes are read with no run
holds. `.github/scripts/release_report.py:7-15` prints each agent's
preload as the bytes of `agents/<agent>.md` and of each skill its
`skills:` list names. That is the file set
`evals/scripts/noninferiority.py#preload_files` sums.
`.github/workflows/test.yml:257-259` runs the job on a pull request whose
base is `main` (read).

What matched: D1 left no rule clause and no `no result` arm unpinned.
`bin/seal mutate` ran seven mutants of `verdict` against
`tests/evals/test_noninferiority.py`, and six went red. Those six named
no grader in rule 2, cut rule 1, let truth graders into the pooled total,
cut the unrun-case arm, cut the shape-and-reach exemption from the
run-count arm, and dropped the baseline from the cut arm. The ten rows D1
removed held recall's noise boundary, rule 2's margin and rule 5's
figures. No code reads any of those now. What they held of the kept code
is still held by the rows that stayed. "recall fallen by two finds is
written and not judged" holds both that truth graders stay out of the
pooled total and that rule 2 names no truth grader: its truth grader
fails every new run where the baseline passed it, and the mutant that let
truths into the total went red on it. The count went from 35 rows to 25
(executed, keys counted at `479a79d15` and at HEAD), as D1 says.

One mutant survived, at HEAD and at `479a79d15` alike: rule 3's
`np_ < nruns` at `evals/scripts/noninferiority.py:834` turned into
`np_ <= nruns`. No case asserts that a shape or reach grader the baseline
lacks, passing every new run, passes the side. The one case with such a
grader also loses a run elsewhere and expects `fail` for that reason
(`tests/evals/test_noninferiority.py:1518-1526`). The guard is code the
diff did not change, and the gap predates D1. Under
`skills/code-review/SKILL.md` *The record* that is no finding. A fix
pass that wants it would add one `VERDICTS` row expecting `pass` with
`("c1", "reach-sealer"): ("reach", 0, 0, 2, 2)` alone.

What matched: no sentence outside the closed set still calls the suite
the proof of a rewrite, except `docs/running/measuring-a-run.md:84-87`.
The design's `## Rule changes` changes that sentence at the settle. Its
`from` text stands in that file's section *What a measurement must
survive, and what it must not invent* (read, heading at
`docs/running/measuring-a-run.md:50`). The crafter's account names a
phrase sample, and `docs/experiments/` was not reached. This round
listed that directory whole: `git ls-files docs/experiments` gives four
files, and the only hits for the suite's terms in them are about skill
preload in 2026-09-03's experiment, never this suite (executed). A
closed list, so no sample there. For the open class, three more searches
went past the crafter's patterns, and their hits are a sample, since a
claim in other words still escapes them. They covered: `worse`, `proved`,
`prove`, `proof`, `inferior` and `증명` over the tree outside `seal/`
and `CHANGELOG.md`; `rewrite` near `suite`, `eval`, `preload`,
`definition`, `measure` or `compare`; and the same proof words over
`evals/behaviour/`. Every hit outside the closed set either names
something else (`docs/checks/the-stamp.md:93`,
`README.ko.md:347`, `skills/writing-style/SKILL.md:300`,
`evals/behaviour/crafter/rule-crafter-rename/graders/shape-proved-by.md:7`)
or is the `docs/` sentence above.

What matched: each changed case was seen red, as `trail/phases/phase-1.md`
*How each changed case was shown red* claims. The selection it names ran
again with the tree at `4a9e1dd56`, whose script equals the base's
(executed: `git diff --quiet 479a79d15 4a9e1dd56 --
evals/scripts/noninferiority.py`, exit 0). The result was the same
14 failed and 50 passed, and each failing id is a case D1 to D5 reworked.

What matched: the frame fold at `c6b0fecb6` states the build. S1's new
row-count sentence is `evals/README.md:55-59`, and S4's account of the
reworked cases matches the test diff. `## Removes` counts the ten rows.
The measure cited at `569780eff` holds row C8 with the figures
*Grounding* quotes. `origin/main` reaches the commit (executed:
`git branch -r --contains 569780eff`), and
`tests/text/test_a_cited_commit_outlives_the_squash.py` passes.
The plan's *Judgments of the run* row gives its grounds and the document
it judged against. The version moves to `0.32.0` in
`.claude-plugin/plugin.json:4`, the only file outside `seal/` and
`CHANGELOG.md` that carries the plugin's version (executed: `git grep -F
0.31.2`). That follows `docs/releasing/branch-and-release.md`
*Cutting a release*.

What matched: the rename is a move. Git reports the module as
`similarity index 100%`. Outside `.test_durations` and this work item,
the old name stands only in
`seal/threads/1793787547-each-statement-is-corrected-to-the-tree/frame/design.md:236`
and `frame/plan.md:77`, both commands of a phase closed at `d66106009`
(executed: `git grep -n proved_non_inferior HEAD`). The four rewritten
docstrings say what is true: `git log --follow` shows that at #942 the
module stood at `tests/test_a_rewritten_definition_proved_non_inferior.py`
and moved under `tests/behaviour/` at `e391ea04b`.

One consequence of the change was weighed and opens no finding.
`cheaper_model` takes every `no result` of `verdict` as `opus`
(`evals/scripts/noninferiority.py:1080-1082`). So a Sonnet record whose
token count is unknown, with every grader held and lower spend, used to
print `opus` and now prints `sonnet`. Both were executed in memory,
against the base's and HEAD's script, and printed exactly that. The
frame's *Scope* Out names this inheritance, and A4 decides that an
unknown figure judges nothing. `model` reads no token figure, so the new
answer agrees with what it reads. The changelog fragment states the
`verdict` change and not this result of it. The fix pass may add one
clause there. No sentence in the tree says the old answer, so nothing
there is wrong.

## Not judged

| What | Location | Who answers |
|---|---|---|
| The full suite, the repository-wide lint and the typecheck at HEAD, labelled `unverified` in `gaps.md` *Not verified*; the label is honest, since the phase record names a scoped run of 84 modules and no broad run | `seal/threads/1793795305-the-behaviour-suite-is-a-smoke-run/gaps.md` | the orchestrator, at the broad gate |
| How the narrowed verdict reads two real paid sides; no paid run is in scope | `evals/scripts/noninferiority.py#verdict` | the owner, at the next paid `noninferiority.py compare` |

This round leaves nothing open. What comes due is the orchestrator's
broad run, then the sealer's spawn.

## Probes

| Command | Result |
|---|---|
| `bin/test -q` over the plan row's nine modules and `tests/text/test_a_cited_commit_outlives_the_squash.py`, at HEAD | exit 0, 412 passed |
| `bin/seal mutate evals/scripts/noninferiority.py` with seven `--replace` pairs, `--tests "bin/test -q -p no:xdist tests/evals/test_noninferiority.py"`, at HEAD | 6 red, 1 survived: rule 3's `np_ < nruns` turned into `np_ <= nruns` |
| the same surviving mutant, with the script and its test module at `479a79d15` | survived, 261 passed |
| `bin/test -q -p no:xdist tests/evals/test_noninferiority.py -k "Test_verdict or Test_render or Test_read_record or Test_check_record or Test_parse_record or Test_cheaper_model or Test_check or Test_model or Test_tokens_read"`, with both files at `4a9e1dd56` | exit 1, 14 failed and 50 passed, the ids the phase record names |
| `python -c` that loads the script from `git show <rev>:evals/scripts/noninferiority.py` in memory and calls `verdict` and `cheaper_model` on a Sonnet record with `new_tokens=None` | at `479a79d15`: `no result`, `opus`; at HEAD: `pass`, `sonnet` |
