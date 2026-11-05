# Review round 1: 1793853197-a-bare-commit-goes-or-states-its-reason

```seal
target: 8a6aa184 against release/v0.32.4
```

This round read the branch against its base, 31558c76, the commit
`release/v0.32.4` stood at when the branch was cut. It worked in the
branch's own worktree at 8a6aa184, which the spawn named, with a clean
status before and after. The commits read are 2a11993e, 665eef15,
43b9b1be, 742a5f03, bba2f57b, 50824c2c, fb35d158, 8af53e6f and 8a6aa184.
The records read whole are `routing.md`, `frame/design.md`, `frame/plan.md`,
`frame/questions.md`, `gaps.md`, `changelog.md` and both phase records. No
earlier round exists, so no fact was carried: every fact below was opened or
run this round.

The implementer's account was read as claims. Phase 1 claimed that 85
comment and docstring lines in 29 files were rewritten by D1's rows, that 30
data lines stayed, that only D1 rows 41 to 46's tokens resolve after it,
and that the two non-test files changed comments alone. Phase 2 claimed a
bare reader inside `cited` with one `git cat-file --batch-check` process,
four new cases each seen red, S11's twelve bare entries with
`unreached(ROOT) == []`, and a tree case about one second slower. Each is
answered below by what this round ran or read. The full suite, the CI legs'
cost and every count of passed cases across many modules stay the
orchestrator's, as `gaps.md` labels them.

## Findings

None. The round opens no finding. What follows under `## Confirmations`
is what it checked and found holding, and `## Not judged` names the two
things it left to their answerers. Nothing is open for a fix pass, so what
comes due is the orchestrator's broad run at HEAD and the sealer's spawn
after it.

## Confirmations

What matched, compliance, the class phase 1 rewrote: phase 1 claimed that
no rewritten token is left outside `seal/`. A `git grep -nwE` at HEAD for
43 of the 44 commit tokens D1 rows 1 to 40 rewrite, outside `seal/`,
printed nothing and exited 1 (executed). The 44th, 15a5ce66, stays as data
in D1 row 41's scaffolds, and `grep -n` finds it no longer in
`tests/skills/test_seal_stamp.py`, the file row 32 rewrote (executed). M1 run again at HEAD, with `git grep -I
-ohP '\b[0-9a-f]{7,40}\b' HEAD -- . ':(exclude)seal/'` fed to one `git
cat-file --batch-check`, gave 6,454 distinct tokens of which 18 resolve as
commits (executed). Eighteen is the count `trail/phases/phase-1.md` *S1*
lists, all D1 rows 41 to 46 tokens. Phase 1 claimed 29 files: `git diff
--name-only 665eef15 43b9b1be` outside `seal/` lists 29 (executed).

What matched, compliance, S3: `.github/workflows/test.yml:78-84` and
`skills/implement/scripts/seal.py:1215-1219` and `:2190-2193` change
comment lines alone in `git diff 31558c76..HEAD` (read). The workflow's
rewrap leaves "Four is the smallest Windows count whose" opening a line of
its own, which reads unevenly and changes no word.

What matched, the meaning of each rewrite (`gaps.md` row 3 hands this to
the proofer): every hunk of `git diff 665eef15..43b9b1be` outside `seal/`
was read against its paragraph and its case (read). Each P removal leaves a
docstring that still states what the case refuses. Each N rewrite says in
the present what its case or constant holds. Three were checked against the
code they describe. `ONLY_ON_SOME_PYTHONS`, which
`tests/skills/test_arm_check.py:701` now names, stands at
`skills/verify/scripts/arm_check.py:307` (executed, `git grep`). The six
ids that `tests/skills/test_pact_check.py:885-887` now says are refused too
are six of the eight parameters at `:860-880`, each asserted at exit 2
(read). The `as filed` shape that `tests/skills/test_seal_stamp.py:1676`
now names is a parameter id at `:1669` (read). Rewrites of the
*Red how* lines for `6bbaa4d1` and `dc1b0d14`, which resolve nowhere in
this clone (executed, `git cat-file -t`), describe the defect the docstring
above each already states, as the phase record says. This round could not
open those commits, so it read each against its own docstring and not
against the code it names.

What matched, phase 1's departure on D1 row 31: the phase took Q1 (c) and
kept `#1177` as the case's tag, not as the source of the harness behaviour,
because the issue page holds the question and not the probe's answer. The
dropped pointer, 346cd01d, is contained by no `main`, `origin/main` or
`origin/release/*` ref (executed, `git for-each-ref --contains`), so a fresh
clone could not open it. Dropping it removes nothing a reader could reach.
The departure holds against Q1's default.

What matched, compliance, D2 and *Data & interfaces*: `cited`
(`tests/text/test_a_cited_commit_outlives_the_squash.py:95-125`) reads
`BARE` tokens outside `seal/` and outside `COMMIT_PATH` spans. It resolves
them with one `git cat-file --batch-check` process fed bytes on stdin
(`:128-161`), and only resolved tokens reach `unreached` (`:169-188`),
whose one refusal path, `REACHING` and skip are unchanged (read). Stdin as
bytes means no newline is written as CRLF on Windows. The answers are
zipped with `strict=True`, so a short answer raises rather than shifting
(read). The tokens are hex alone, so no token can carry a newline into the
batch input (read). The refusal header, `REPAIR` and `NO_REF` name the bare
form at `:56-65` and `:196-198` (read). The *Rule changes* `from:` passages
match `docs/layout/the-record-layout.md:155-157` and `:165-168` word for
word (read).

What matched, S11: phase 2 claimed `cited(ROOT)` gives 12 bare entries over
six commits and `unreached(ROOT) == []`. Called once from the worktree's
`.venv` at HEAD, `cited(ROOT)` returned 37 entries, 12 of them outside
`seal/` at exactly the lines `trail/phases/phase-2.md` *S11* lists, and
`unreached(ROOT)` returned `[]` (executed).

What matched, the cost: D2 *What it costs* says the reading adds about
half a second on the framer's machine. Three timed calls of
`unreached(ROOT)` at HEAD took 0.89, 0.95 and 0.91 s (executed), against
the base's 0.35 to 0.39 s that phase 2 records. That is about half a second
added on this machine, so D2's figure holds. The changelog's "about one
second longer" is the tree case's pytest duration, a different measure,
and phase 2's table carries both.

What matched, the collision risk `frame/plan.md` *Technical context* calls
rare: this clone holds 918 commits on its refs, 337 of them contained by
no `main` or release ref (executed, `git rev-list --count`). Outside `seal/`
and `evals/behaviour/`, 30 distinct tokens are seven hex long and 24 are
eight long (executed). The expected number of seven-hex tokens that prefix
an unreached commit is about 30 times 337 over 16 to the seventh, under
0.0001. Longer tokens add less.

What matched, the new cases against their group: the four cases read
against the module's existing ones (read). S7 holds a bare token where
`test_a_citation_of_a_feature_branchs_commit_is_refused` holds a
`<commit>:<path>` one. S8 holds the `seal/` exclusion, which no older case
reads, and its control line in `docs/a.md` makes it fail with the bare
reading removed. S9 holds resolution and containment for the bare form. S10
holds the literal text of the bare header and the bare repair sentence.
`test_the_refusal_says_where_and_the_repair` asserts `REPAIR` only as the
constant, so it cannot pin either sentence. None covers only what its
group already covers. The module declares no `TARGET`, so `seal layout
--pairs` names no pair for it.

What matched, the narrow runs: `bin/test
tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist` gave
17 passed at exit 0. `bin/test
tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -q`, the module
whose `#cited` comment phase 2 changed, gave 9 passed at exit 0 (executed).
Each case's red, as phase 2 records it, was read and not re-run. Each
`seal mutate` row names the break, the case and the failing line, and the
header's survival before 50824c2c is recorded with its cause (read).

What matched, the labels: `gaps.md` labels the full suite, the lint and
the typecheck `unverified` with the orchestrator as answerer. It also labels
the CI legs' cost `unverified`, answered by the pull request's
`--durations` tables (read). The labels are honest: neither phase claims a
broad run.

What matched, the siblings: `git merge-tree --write-tree HEAD
origin/release/v0.32.4` exited 0, so the four sibling squashes merge
without a conflict in the shared test files (executed). The lines those
squashes added outside `seal/` and `evals/behaviour/` hold no bare token
that resolves as a commit in this clone (executed). The tree case should
therefore pass on the merged tree, and the broad run at the merged HEAD
answers whether it does.

## Not judged

| What | Location | Who answers |
|---|---|---|
| Whether the four cases the module docstring names still stay green with contract rule 9's body pasted back under a new heading in `agents/proofer.md`, now that the sentence states it in the present and not as a measurement. Settling it is a probe that edits a tracked file, and this round ran none | `tests/text/test_a_moved_rule_leaves_its_definition.py:8-13` | the sealer, if it samples the claim |
| The full suite, the repository-wide lint and the typecheck at HEAD, and the bare reader's cost on the Windows and macOS CI legs | `gaps.md` *Not verified* rows 1 and 2 | the orchestrator, at the broad run and on the pull request's CI `--durations` tables |

## Probes

| Command | Result |
|---|---|
| `bin/test tests/text/test_a_cited_commit_outlives_the_squash.py -q -p no:xdist` | 17 passed, exit 0 |
| `bin/test tests/behaviour/test_a_shrunken_corpus_declines_to_judge.py -q` | 9 passed, exit 0 |
| `cited(ROOT)` and `unreached(ROOT)` called once from `.venv/bin/python` with `tests` and `tests/text` on the path | 37 entries, 12 outside `seal/` at the lines phase 2 lists; `unreached` returned `[]` |
| `unreached(ROOT)` timed three times | 0.89, 0.95 and 0.91 s |
| M1 at HEAD outside `seal/`, its tokens through one `git cat-file --batch-check` | 6,454 distinct tokens, 18 commits |
| `git grep -nwE` of 43 of the 44 commit tokens D1 rows 1 to 40 rewrite, all but 15a5ce66, at HEAD outside `seal/` | no line, exit 1 |
| `grep -n 15a5ce66 tests/skills/test_seal_stamp.py` | no line, exit 1 |
| `git for-each-ref --contains` on ten provenance commits D1 named, against `main`, `origin/main` and `origin/release/*` | 346cd01d, 55aea15d and 4edc5de6 contained by none; the other seven by `refs/heads/main` |
| `git rev-list --all --count`, then with the `main` and release refs excluded | 918 and 337 |
| `git merge-tree --write-tree HEAD origin/release/v0.32.4` | exit 0 |
| the added lines of `git diff -U0 31558c76 origin/release/v0.32.4` outside `seal/` and `evals/behaviour/`, their bare tokens through `git cat-file --batch-check` | 0 commits |
| `python3 skills/code-review/scripts/chain_check.py --baseline 31558c76 --root <worktree> --worktree`, before this record | exit 0; it named the missing round, gate record and guarantee, and no notice on `frame/design.md` |
