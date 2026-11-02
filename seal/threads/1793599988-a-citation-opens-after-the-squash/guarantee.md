# Guarantee: 1793599988-a-citation-opens-after-the-squash

| Field | Value |
|---|---|
| Broad gate | d04f8fa9d against d57e9ee7a (`trail/gate.md`, its last `seal` block). Followed to HEAD only by 1793c862 (`trail/gate.md`) and dc9d47ea (`frame/questions.md`), both under this work item's directory (executed: `git log --no-merges --name-only d04f8fa9d..HEAD ^d57e9ee7a`). d04f8fa9d is an ancestor of HEAD (executed: `git merge-base --is-ancestor`, exit 0) |

The base `release/v0.29.0` resolves to no local branch and no upstream here;
`origin/release/v0.29.0` resolves to d57e9ee7a (executed: `git rev-parse
--verify --quiet` over the three names in order). `seal pr-body
seal/threads/1793599988-a-citation-opens-after-the-squash --body <scratchpad>/1793599988-a-citation-opens-after-the-squash/pr-body.md
--check` exited 0 (executed, the tree's `bin/seal`), so the part of the body
below `## From the records` is the records' text. No `seal/parity.md` is
tracked (executed: `git ls-files seal/parity.md`, empty), so this block has
no `original:` line.

Every re-run below ran in `<scratchpad>/1793599988-a-citation-opens-after-the-squash/at-base/`,
a `git clone --no-local` of the branch worktree at dc9d47ea. The source's
`refs/remotes/origin/main` and `refs/remotes/origin/release/*` were fetched
in as `refs/remotes/src/*` and every `refs/remotes/origin/*` of the clone
was deleted, so the tree case judged with remote-tracking `main` and
`release/*` refs alone, as CI's checkout holds them. The clone and its logs
were removed before this file was written. Mutants ran through the `bin/seal`
of the worktree of `fix/898-a-mutant-that-does-not-compile-reads-as-caught`
at a3747c18, which refuses a mutant that does not compile.

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| S1 seen red: the tree case fails before *Scope* item 5's edit, naming `1793538230` `frame/design.md:18` and `79252e48` | `trail/phases/phase-1.md:68-74` | in the clone, `git checkout d57e9ee7a -- seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md`, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -p no:xdist -rfEs -q` | holds (executed): exit 1, 1 failed and 11 passed, the failure naming `seal/threads/1793538230-code-text-brought-to-the-tree/frame/design.md:18 cites 79252e48` with the repair and the `git fetch` sentence. 11 and not 9 passed because S3 gained two parameters in b01ec5b1 |
| The tree case passes at HEAD with CI's shape of refs, and judges rather than skipping; this is also `frame/questions.md` Q1 at HEAD, whose tree is d04f8fa9d's plus two record files | `trail/phases/phase-1.md:68-74`, `frame/questions.md:15` | the edit restored with `git checkout HEAD -- <same path>`, then `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -p no:xdist -rfEs -q` | holds (executed): exit 0, 21 passed, nothing skipped |
| Mutants 1, 2, 4 and 5 of the phase record, which no round planted again (round 1's fourth confirmation), and round 2's finding mutant, each red | `trail/phases/phase-1.md:90-99`, `trail/rounds/round-2.md` finding 1 | `seal mutate tests/text/test_a_cited_commit_outlives_the_squash.py --tests "bin/test <module> -q -p no:xdist -k 'not every_cited'"` with five `--replace` pairs: `read_here`'s work-item return to `return False and not (`; the `--contains` call rewritten into `git -C <root> cat-file -t <commit>`; `if not refs:` to `if False:`; the `FETCH,` line deleted; `if found is None:` to `if not found:` | holds (executed): baseline passed, 5 mutants, 5 red, 0 SURVIVED, exit 0 |
| Each of those five is red against the case the record names for it | `trail/phases/phase-1.md:90-99`, `trail/rounds/round-2.md` close of finding 1 | the same five mutants, one `seal mutate` each, with `-k rest_of_a_work_item`, `-k feature_branchs_commit`, `-k no_reaching_ref`, `-k refusal_says` and `-k squash_is_accepted` | holds (executed): `test_the_rest_of_a_work_item_is_read` 1 failed; S2 both extensions, 2 failed; `test_no_reaching_ref_judges_nothing` 1 failed; `test_the_refusal_says_where_and_the_repair` 1 failed; S3 all four parameters, 4 failed |
| `## Removes`: the citation of the measure at `79252e48` no longer stands at `1793538230` `frame/design.md:18`, and the row cites the squash `48d035aa` | `frame/design.md:142` | `git grep -n '79252e48:' HEAD -- ':!seal/threads/*/trail/' ':!seal/threads/*/guarantee.md'`; `git cat-file -e 48d035aa:seal/threads/1793490088-each-kind-of-restatement-is-measured/trail/phases/phase-2.md`; `git for-each-ref --contains 48d035aa 'refs/remotes/origin/main' 'refs/remotes/origin/release/*'`; `git cat-file -t 79252e48` | holds (executed): no `<commit>:<path>` token of `79252e48` stands outside `trail/` and `guarantee.md`; every remaining hit is a quoted command or a bare id. `48d035aa` holds the path (exit 0) and `origin/main` and three release refs contain it. `79252e48` is no object here (exit 128). Line 25 of the same file still cites `79252e48:…/phase-2.md`, which `COMMIT_PATH` does not match; `frame/design.md:61` puts such paths out of scope, so this is the declared limit and no contradiction |
| G1's record: refused citations in released frames at `v0.26.0`, `v0.27.2` and `v0.27.3` | `frame/design.md:15` | `git show <tag>:<file>` at the four coordinates G1 names, then `git for-each-ref --contains <commit> 'refs/remotes/*/main' 'refs/remotes/*/release/*'` for `efb91989` and `79252e48` | holds (executed): each line holds the named `<commit>:<path>` token, and both commits answer `malformed object name` |
| The merge d04f8fa9d resolved no conflict | `trail/gate.md` context; pull request body, *The merge* | `git merge-tree --write-tree d04f8fa9d^1 d04f8fa9d^2` against `git rev-parse d04f8fa9d^{tree}` | holds (executed): exit 0 and the same tree, 26460ef2 |
| The orchestrator's commits touch only the work item's records, except that merge | pull request body, *The orchestrator's commits* | `git log --no-merges --name-only d57e9ee7a..HEAD`, paths outside this work item's directory | holds (executed): only 44b215bc (the build), b01ec5b1 and 34c55c1e (the fix passes) touch other paths |
| #1234, #1236, #1255 and #1256 are open and still cite `79252e48` | pull request body, last bullet; `frame/design.md:58` | `gh issue view <N> --json state`, and the body searched for `79252e48` | holds (executed): all four OPEN, each body citing it |

Not re-run: the full suite, the lint and the typecheck at d04f8fa9d, which
`trail/gate.md` records and the orchestrator ran (unverified by this file;
the gate record is its answerer). The module on CI's Windows leg (unverified;
CI's Windows leg on the pull request answers it).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | A test module refuses a `<commit>:<path>` whose commit no `main` or `release/*` ref contains, outside `evals/behaviour/`, `trail/` and `guarantee.md`; bare SHAs are decided against (G2); issue bodies are left to the orchestrator (`frame/design.md:58`); one record line is corrected; the rule changes land at the settle | the issue's *Done when* (a check weighed and built with a case); the tree (the module at `tests/text/test_a_cited_commit_outlives_the_squash.py`, no file under `docs/` changed, as `skills/implement/SKILL.md:73` has a pull request leave the policy root to the settle) | none |
| the build | `trail/phases/phase-1.md`: the module and the one correction, S1 seen red, ten mutants red, one equivalent mutant left unverified under contract rule 13, one departure (the corpus-guard row) | the design; the diff; the re-runs above | none. Its sentences at `:49-51` and `:99` state S3's two-ref parametrisation of 44b215bc, which rounds 1 and 2 record as superseded; they are true at the commit the record names (read) |
| the last round | `trail/rounds/round-3.md`: round 2's one finding confirmed, 13 mutants red, no finding | the diff at HEAD (read); the `if not found:` mutant red against S3 (executed above) | none |
| the changelog | `changelog.md`: the new case, what it reads and refuses, the skip, the files it leaves out, the one correction, no shipped file changed | the design, the diff (only `tests/` and `seal/` change, executed: `git diff --stat`) | none |
| the orchestrator's part of the pull request body | the change, the alternatives, the scope, the failure direction, the removal, the rounds, the merge, the open issue bodies | the design, the plan, the rounds, the changelog and the tree on every claim checked above, except the one in the next cell | Its bullet **What it does not read** says "Bare commit ids, the work items' `trail/` and `guarantee.md`, and issue bodies stay the proofer's, because a round record cites its own branch's commits by design (`frame/plan.md` A3, A4)". `frame/design.md:58` leaves issue bodies to the orchestrator, not the proofer, and the body's own last bullet says the same ("the frame leaves them to the orchestrator"). `frame/plan.md:43-44` (A3, A4) speak of `trail/` and `guarantee.md` only; bare ids are decided at `frame/design.md:16` (G2) and `:56`. The design and the body's last bullet decide it: the bullet's "and issue bodies stay the proofer's" does not hold, and its citation does not carry bare ids (read) |

```seal
target: dc9d47ea against d57e9ee7
Verdict: withheld reason: the orchestrator's part of the pull request body, bullet "What it does not read", says issue bodies "stay the proofer's" citing frame/plan.md A3 and A4; frame/design.md:58 and the body's own last bullet leave issue bodies to the orchestrator, and A3 and A4 (frame/plan.md:43-44) cover trail/ and guarantee.md only, with bare ids decided at frame/design.md:16 (G2); drop "and issue bodies" from that bullet and cite G2 for bare ids
```

## Re-audit at f2af3a56

| Field | Value |
|---|---|
| Broad gate | d04f8fa9d against d57e9ee7a (`trail/gate.md`, its last `seal` block, unchanged). Followed to HEAD only by 1793c862 (`trail/gate.md`), dc9d47ea (`frame/questions.md`) and f2af3a56 (`guarantee.md`), all under this work item's directory (executed: `git log --no-merges --name-only d04f8fa9d..HEAD ^d57e9ee7a`) |

`origin/release/v0.29.0` still resolves to d57e9ee7a (executed). f2af3a56
adds this file and nothing else (executed: `git diff --stat dc9d47ea..HEAD`),
and the working copy matched it before this block was appended (executed:
`git status --short`, empty). No claim of the earlier block has a coordinate
that f2af3a56 touched, so none is re-run; the earlier block's re-runs were
made at dc9d47ea, whose tree differs from f2af3a56's in this file alone.
`seal pr-body seal/threads/1793599988-a-citation-opens-after-the-squash --body <scratchpad>/1793599988-a-citation-opens-after-the-squash/pr-body.md
--check` exited 0 at f2af3a56 (executed, the tree's `bin/seal`).

## Claims re-run

| Claim | Source | Command | Result |
|---|---|---|---|
| The withheld claim is gone: the bullet no longer assigns issue bodies to the proofer, and its citations carry what it states | pull request body, bullet **What it does not read** | read the body file above `## From the records` against `frame/design.md:16` (G2), `:56`, `:58` and `frame/plan.md:43-44` (A3, A4) | holds (read): "Bare commit ids stay the proofer's (`frame/design.md` G2)" matches G2's "the proofer goes on reading it"; "`trail/` and `guarantee.md` stay out ... (`frame/plan.md` A3, A4)" matches A3's grounds; issue bodies are named only in the last bullet, which leaves them to the orchestrator as `frame/design.md:58` does |
| The orchestrator's commits touch only the work item's records, except the merge | pull request body, *The orchestrator's commits* | `git log --no-merges --name-only d57e9ee7a..HEAD`, paths outside this work item's directory | holds (executed): f2af3a56 touches `guarantee.md` alone; outside the directory only 44b215bc, b01ec5b1 and 34c55c1e, the crafter's, as before |

Not re-run, as in the earlier block: the full suite, lint and typecheck at
d04f8fa9d (unverified here; `trail/gate.md` and the orchestrator's `seal gate`
answer it), and the module on CI's Windows leg (unverified; CI's Windows leg
on the pull request answers it).

## The parties

| Party | Says | Agrees with | Disagrees with |
|---|---|---|---|
| the design | unchanged since the earlier block | the issue's *Done when*; the tree | none |
| the build | unchanged since the earlier block | the design; the diff; the earlier block's re-runs | none |
| the last round | `trail/rounds/round-3.md`, unchanged | the diff at HEAD | none |
| the changelog | `changelog.md`, unchanged | the design; the diff | none |
| the orchestrator's part of the pull request body | as before, with the **What it does not read** bullet rewritten | the design, the plan, the rounds, the changelog and the tree on every claim the earlier block checked, and on the rewritten bullet | none |

```seal
target: f2af3a56 against d57e9ee7
Verdict: sealed
```
