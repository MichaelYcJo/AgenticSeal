# 1792619407-the-replay-scaffold-and-reader-misread-rounds — phase 2

| Field | Value |
|---|---|
| Phase | 2 |
| Commit | 5ed3d66c |

## What this phase was asked

Build the seeded case in `evals/scripts/seed_defects.py`. Targets come from
round 1's record at each shipped squash commit, read through the
`replay_targets.py` readers. The seed is chosen over `base..target`. The
scaffold is the one `spec.md` *Data & interfaces* gives, with no `git rm`.
Round 1's confirmed fixes are truths beside `truth-seeded`, and the case name
stays the squash commit's first 8 hex. The six seeded entries leave
`recurred_truths.json`. The four seeded cases are regenerated with `--case`,
and `questions.md` Q3 covers a case that cannot be built. Spec S8 and S9 are
written test-first, and the generator cases that name `seeded-279a580b` are
updated in place. Also written: `evals/README.md`'s `seed_defects.py` row,
the stated point, the module docstring and this directory's `changelog.md`.
Each regenerated scaffold is run once and every check of S10 recorded
(`questions.md` Q2).

## What this phase found

**The frame does not hold at one point, and the build follows the part that
holds.** `plan.md`'s summary says nothing in the clone holds the build
without the seed. That is false. The amend rewrites only the target commit,
and every branch commit before it holds the line unmutated. All four
targets end in a commit that touches records only. So in each clone, `git
diff --stat HEAD^ HEAD` shows the seeded Python file changed by one line
inside a records commit:

| Case | `git diff --stat HEAD^ HEAD` in the clone, executed |
|---|---|
| `seeded-279a580b` | the ledger rename, `overview.md`, four `phases/phase-N.md`, and `skills/code-review/scripts/chain_check.py`, 1 line each way |
| `seeded-ad447367` | four `phases/phase-N.md` and `skills/code-review/scripts/chain_check.py`, 1 line each way |
| `seeded-8a100e13` | `evals/scripts/noninferiority.py` 1 line each way, `phases/phase-2.md`, `plan.md` |
| `seeded-f1c9932d` | `plan.md`, `questions.md`, and `skills/code-review/scripts/chain_check.py`, 1 line each way |

This is the leak `plan.md` row S2 was rejected for: a diff of a few lines
shows the seed. It is narrower here, because it needs `HEAD^`, but it is
there. Keeping cited commits resolvable and leaving no unmutated copy
conflict whenever the seed line existed before the target commit. Seeding
only a line the target commit itself added would avoid it, but each of the
four targets' last commits adds no Python line. Whether to accept this, or
to choose another design, is a question for a person, named in the
hand-back. S10's checks as written all hold.

**A base ref deleted after its release.** Some round 1 records name a base
branch the remote no longer has; `spec.md` scope item 5 states which. The
remote's release branches are only `release/v0.22.2` and `release/v0.22.3`
(`git ls-remote origin 'refs/heads/release/*'`), so the replay readers find
no base for those records.
`replay_targets.py#ref_base` lets the commit the work landed on stand for a
ref that no longer resolves. `seed_defects.py#target_of` passes the squash
commit's first parent, the release branch it shipped on. A squash puts none
of the target's commits on that branch, so their merge-base is the fork the
named ref had. The replay generator passes nothing and is unchanged.

**One reader per round, shared.** The per-round body of
`replay_targets.py#targets` moved into `round_target`. Both generators call
it, and `replay=False` keeps a round that has no round 2 or no confirmed fix.
The replay cases regenerate byte for byte (S11, S12).

**Q3 applied twice.** Two of the four cannot be built at round 1's target,
and each was replaced by the next smallest shipped commit that builds in
`seed_defects.py --list`. The executed list put `8a100e13` at 1334 lines and
`f1c9932d` at 3485 lines.

- `seeded-4d316179` takes no seed at its round 1 target `44c67f9f`: no line
  `34fc36e9..44c67f9f` added in `hooks/worktree-guard.py`, its one non-test
  Python file, takes an operator. Its seed at the squash, line 3154, came
  from a later commit. It is replaced by `seeded-8a100e13`.
- `seeded-9b644676` builds a seed, but round 1's findings 3 and 5 are five
  lines apart in `docs/release-checklist.md` (360 and 365), and both truths
  accept a `location:` line naming `docs/release-checklist.md:350`. The
  first generation
  wrote the case anyway, and
  `test_no_two_truths_of_a_warden_case_accept_one_location` refused it. The
  generator now leaves such a commit out with the line named
  (`seed_defects.py#shared_line`), and the seed already skips any line a
  truth's window accepts. It is replaced by `seeded-f1c9932d`.

The truths the four cases carry beside the seed are 279a580b round 1's
findings 2 to 5, ad447367's finding 2, 8a100e13's finding 1, and
f1c9932d's findings 1 and 3.

**S10, executed once per case** in an empty scratch directory with `sh
scaffold.sh`, each fetching from the repository's GitHub remote (Q2):

| Case | Scaffold exit | `git grep -n 'seal/specs/<item>/rounds/'` | `plan.md` Status commits resolving | `git cat-file -e` of the original target | `grep -r <target> .git --exclude-dir=objects` |
|---|---|---|---|---|---|
| `seeded-279a580b` | 0 | exit 1, no line | 61721ab6 45077c75 1e9d98f0 19167d11, all | exit 128 | exit 1, no file |
| `seeded-ad447367` | 0 | exit 1, no line | 6d12e2ea 925216d7 bffcb3a2 88d5fe61, all | exit 128 | exit 1, no file |
| `seeded-8a100e13` | 0 | exit 1, no line | d6945b16 c8e8329e, all | exit 128 | exit 1, no file |
| `seeded-f1c9932d` | 0 | exit 1, no line | fe201329 0dd09a37 dddcdfdc, all | exit 128 | exit 1, no file |

`test_the_seeded_scaffold_leaves_round_1s_tree_and_no_copy_of_it` runs the
same checks against a fixture repository, so CI holds them with no network.

**S11, executed.** Every warden case was regenerated: four `replay_targets.py
--case`, `rule_cases.py`, and four `seed_defects.py --case`, each exit 0.
`git status --porcelain evals/behaviour/` was then empty.

**S12, executed.** `git rev-parse 5aed51cb:<dir>` equals `HEAD:<dir>` for
the four `replay-*` cases, `rule-warden-one-finding`, and the `smith`,
`framer` and `sealer` suites.

**S13.** `git grep -n -e report_rows -e FINDING_ROW -- ':!seal'` finds the
two test lines phase 1 records, and nothing else.

**Seen red.** Against e01a32a0's parent, the three S8, S9 and S10 cases
failed: `seed_defects` had no `target_of`. Each case's content was then
shown red by `mutation-check` against the unit it guards.

**Mutation.** 16 runs of `bin/mutation-check`, each exit 0 `red`. The units
were: `seed`'s truth window; `target_of`'s landing commit, its record
writer, its round 1 read, its round 2 read and its `shared_line` bound; the
scaffold's reflog expiry, `FETCH_HEAD` removal, `gc`, and its base ref line;
`graders`' round 1 truths; `ref_base`'s fallback; `round_target`'s
`replay` flag at both places; its confirmations where no round follows; and
the truth's `location` key. The first run of `seed`'s mutation named a line
the formatter had wrapped, so it measured nothing (exit 2). It was rerun on
the wrapped line and went red.

**Phase boundary, executed.** The touched and meta modules named in the
spawn ran in one `bin/test` call. The first run failed one case:
`test_only_neutral_domains` refused a token this work item's own phase 1
record and overview quoted. Phase 1's run had not seen it, because the scan
reads tracked files and the records were not yet committed. The two
sentences were reworded, and the rerun is in the hand-back. `bin/rules
--check`, `bin/settle --released-at HEAD` and `bin/unverified-check
seal/specs/` each exited 0. `ruff check` and `ruff format --check` exited 0
on each touched `.py` file.
